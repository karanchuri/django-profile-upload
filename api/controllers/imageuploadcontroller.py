from api.models.postgres.profilepicture import ProfilePictures
from PIL import Image, ExifTags, ImageChops
from datetime import datetime
import os


class ImageUploadController:

    def __init__(self, up_file, user_id, image_index):
        self.up_file = up_file
        self.user_id = user_id
        self.image_index = image_index
        self.file_name = None

    def save_image(self):
        f, file_extension = os.path.splitext(self.up_file.name)
        self.file_name = f"/tmp/{self.user_id}_{self.image_index}_{int(datetime.utcnow().timestamp())}{file_extension}"
        out_file = open(self.file_name, "wb")

        if not self.up_file.multiple_chunks():
            out_file.write(self.up_file.read())
        else:
            for chunk in self.up_file.chunks():
                out_file.write(chunk)
        out_file.close()

    def compress_image(self):
        f, file_extension = os.path.splitext(self.up_file.name)
        file_name = f"/tmp/final_{self.user_id}_{self.image_index}_{int(datetime.utcnow().timestamp())}{file_extension}"

        img = Image.open(self.file_name)

        try:
            exif = dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)
            orientation = "Orientation"
            if exif[orientation] == 3:
                img = img.rotate(180)
            elif exif[orientation] == 6:
                img = img.rotate(270)
            elif exif[orientation] == 8:
                img = img.rotate(90)
        except:
            pass

        img = img.resize((1280, 960), Image.ANTIALIAS)
        img.save(file_name)
        try:
            os.remove(self.file_name)
        except:
            pass
        self.file_name = file_name

    def is_duplicate(self):
        profile_pic = ProfilePictures.objects.filter(profile__user_id=self.user_id).all()
        for picture in profile_pic:
            image_one = Image.open(self.file_name)
            image_two = Image.open(picture.url)
            diff = ImageChops.difference(image_one, image_two)
            if diff.getbbox():
                return False
            else:
                return True

    def update_db(self):
        profile_pic = ProfilePictures.objects.filter(profile__user_id=self.user_id, image_index=self.image_index).\
            first()

        if profile_pic:
            ProfilePictures.objects.filter(profile__user_id=self.user_id, image_index=self.image_index).\
                update(url=self.file_name)
        else:
            ProfilePictures.objects.create(profile__user_id=self.user_id, image_index=self.image_index,
                                           url=self.file_name)
