import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

cloudinary.config(
    cloud_name = "dnloqwpl4",
    api_key = "431372482563836",
    api_secret = "DrW7i48ikJmtd3YpFUdxuqiE3HA",
    secure = True
)

def upload_image(path):
    response = upload(path)
    url = response["secure_url"]
    return url
