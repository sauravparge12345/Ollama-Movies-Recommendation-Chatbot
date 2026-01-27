import gradio as gr
from utils import run_conversation


def chatbot(input_text):
    return run_conversation(input_text)


with gr.Blocks(title="Ollama Movies Recommendation Chatbot") as demo:
    gr.Markdown("## 🎬 Ollama Movies Recommendation Chatbot")

    with gr.Row():
        input_text = gr.Textbox(
            label="Input",
            placeholder="Type something like: inception like movies",
            lines=8
        )

        output_text = gr.Textbox(
            label="Output",
            lines=8
        )

    submit_btn = gr.Button("Submit")
    clear_btn = gr.Button("Clear")

    submit_btn.click(
        fn=chatbot,
        inputs=input_text,
        outputs=output_text
    )

    clear_btn.click(
        fn=lambda: ("", ""),
        outputs=[input_text, output_text]
    )

demo.launch()
