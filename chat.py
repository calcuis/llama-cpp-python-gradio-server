from llama_cpp import Llama
llm = Llama(model_path="chat.gguf")

def submit(message,chat_history):
    output=llm("Q: "+message, max_tokens=2048, echo=True)
    output_texts=output['choices'][0]['text']
    return output_texts

import gradio as gr
title = "chatGPT"

gr.ChatInterface(
    fn=submit,
    title=title,
).launch(
    # share=True
)
