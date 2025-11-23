import torch
from diffusers import StableDiffusionPipeline
import gradio as gr

# Detect device (CPU only in free Spaces)
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Running on:", device)

# Load Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32  # use float32 for CPU
).to(device)

# Only enable xformers if GPU is available
if torch.cuda.is_available():
    try:
        pipe.enable_xformers_memory_efficient_attention()
        print("Enabled xFormers optimization.")
    except Exception as e:
        print("xFormers not available:", e)
else:
    print("Skipping xFormers — CPU mode.")

# Image generation function
def generate(prompt, negative_prompt, steps, guidance, width, height):
    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt if negative_prompt else None,
        num_inference_steps=int(steps),
        guidance_scale=float(guidance),
        height=int(height),
        width=int(width)
    ).images[0]
    return image

# Gradio interface
demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Textbox(label="Negative Prompt"),
        gr.Slider(10, 50, value=30, step=1, label="Steps"),
        gr.Slider(1, 15, value=7.5, step=0.5, label="Guidance"),
        gr.Slider(256, 768, value=512, step=64, label="Width"),
        gr.Slider(256, 768, value=512, step=64, label="Height"),
    ],
    outputs=gr.Image(label="Generated Image"),
)

demo.launch(share=True)
