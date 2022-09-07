import gradio as gr

def greet(name):
    return f"Hello {name}!"

gr.Interface(greet, "text", "text").launch()