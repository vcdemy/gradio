import gradio as gr
from PIL import Image
import random

def convert(image):
  image = Image.fromarray(image)
  image.thumbnail((200, 200))
  image.save(f"{random.randint(0, 99999):05}.jpg")
  return image.convert('L')

gr.Interface(convert, 'webcam', 'pil').launch()