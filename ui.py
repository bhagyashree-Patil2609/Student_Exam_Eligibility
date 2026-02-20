import gradio as gr
from backend import evaluate_eligibility

CUSTOM_CSS = """
html, body {
    height: 100%;
}

#root,
.gradio-container {
    background-image: url("https://th.bing.com/th/id/OIG3.QOV58n0n0UdwHgslEyJK?pid=ImgGn");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* White transparent card */
#main-card {
    background: rgba(255, 255, 255, 0.88);
    padding: 35px;
    border-radius: 18px;
    max-width: 900px;
    margin: 70px auto;
    box-shadow: 0 12px 35px rgba(0,0,0,0.25);
}

/* Text */
h1, p, label {
    color: black !important;
    font-weight: bold !important;
    text-align: center;
}

/* Output box */
textarea {
    background: white !important;
    color: black !important;
    font-weight: bold !important;
}

/* Button */
button {
    background: black !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 10px !important;
}
"""

with gr.Blocks() as demo:
    with gr.Column(elem_id="main-card"):
        gr.Markdown("""
        <h1>Student Examination Eligibility Evaluation System</h1>
        <p>Upload the attendance file to determine student examination eligibility.</p>
        """)

        upload_btn = gr.UploadButton(
            "Upload Attendance File (.txt)",
            file_types=[".txt"]
        )

        output = gr.Textbox(
            label="Eligibility Report",
            lines=8
        )

        upload_btn.upload(
            fn=evaluate_eligibility,
            inputs=upload_btn,
            outputs=output
        )

demo.launch(css=CUSTOM_CSS)
