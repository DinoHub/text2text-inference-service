import logging

import gradio as gr
from config import config
from predict import examples, inputs, outputs, predict

if __name__ == "__main__":
    logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s")
    app = gr.Interface(
        predict,
        inputs=inputs,
        outputs=outputs,
        title="FLAN-T5",
        description="Text2Text Generation",
        examples=examples,
    )
    
    app.launch(
        server_name="0.0.0.0",
        server_port=config.port
    ).queue()
    
