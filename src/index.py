import torch
from flask import Flask
from flask import request
from diffusers import StableDiffusionPipeline
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

app = Flask(__name__)

APP_VERSION = "v1"

cloudinary.config(
  cloud_name = "dnloqwpl4",
  api_key = "431372482563836",
  api_secret = "DrW7i48ikJmtd3YpFUdxuqiE3HA",
  secure = True
)

pipe = StableDiffusionPipeline.from_pretrained("./models/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("mps")
pipe.enable_attention_slicing()

@app.route("/")
def home():
    return { "name": "Cover Banner API @ Moises Hackathon", "version": "1.0.0" }


@app.route("/cover", methods=['GET'])
def get_cover():
    query = request.args.get('query')
    # Salvar imagem pegar e retornar `URL` [MA]
    image = pipe("create an album cover inspired by the blend of different music genres including \"pop, r&b, house music, rap\", digital art", num_inference_steps=100, negative_prompt="words, letters").images[0]
    image.save("./tmp/bar.jpg")
    response = upload("./tmp/bar.jpg")
    url = response["secure_url"]

    return { "url": url }
