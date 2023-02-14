import uuid
import torch
from diffusers import StableDiffusionPipeline

TMP_PATH = "./tmp"
MODELS_PATH = "./models"

pipe = StableDiffusionPipeline.from_pretrained(f"{MODELS_PATH}/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")
pipe.enable_attention_slicing()

def get_cover_image(query):
    identifier = uuid.uuid4()
    image = pipe(query, num_inference_steps=50, negative_prompt="words, letters, title", width=400, height=400).images[0]
    file_path = f"{TMP_PATH}/{identifier}.jpg"
    image.save(file_path)
    return file_path
