import logging
from typing import Dict, Optional, List

import gradio as gr

import numpy as np
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


inputs = [
    gr.inputs.Textbox(placeholder="Your sentence here...", label="Input Prompt"),
    # gr.Textbox(
    #     placeholder="Possible class names", label="Comma Separated Labels"
    # ),
]
outputs = gr.outputs.Label()

examples = [["A step by step recipe to make bolognese pasta:"]]

tokenizer = AutoTokenizer.from_pretrained("./model/flan-t5/1/flan-t5-small-tokenizer")

def predict(text: str) -> List[str]:
    """Takes in an image, and
    calls Triton to infer it's class

    :param image: Image
    :type image: np.ndarray
    :return: Predicted classes with confidence
    :rtype: Dict[str, float]
    """
    model = AutoModelForSeq2SeqLM.from_pretrained("./model/flan-t5/1/flan-t5-small")
    logging.info("Loaded model for inference")

    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs)

    return str(tokenizer.batch_decode(outputs, skip_special_tokens=True))