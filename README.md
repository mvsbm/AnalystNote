Analyst Note Generator

This is a tool designed to generate analyst notes based on PDF files. It uses natural language processing models to analyze the content of the PDF and extract key information for the analyst note.
Installation

To use this tool, please follow these steps:

    Clone the repository: git clone https://github.com/mvsbm/AnalystNote
    Navigate to the project directory: cd AnalystNote
    Install the required dependencies: pip install -r requirements.txt

Usage

    Run the Streamlit app: streamlit run app.py
    Access the app through your web browser (usually at http://localhost:8501)
    Select the language model (LLM) to use. Currently supported models are GPT4 and ChatGPT.
    Choose the chain type for the summarization process: map_reduce, stuff, or refine.
    Adjust the chunk size and overlap using the sliders to optimize the summarization process.
    Enter the company name for the analyst note.
    Upload the PDF file containing the earnings call details.
    Click the "Generate Analyst Note" button to start the analysis and summarization process.
    Wait for the process to complete. Progress updates will be displayed.
    Once the summary is generated, it will be displayed in the app.

Troubleshooting

If you encounter any issues or have questions, please refer to the README.md in the GitHub repository for more information. You can also reach out to the developer via email at s-ma@coloplnext.co.jp.
License

This project is licensed under the BSD 3-Clause License. Please refer to the LICENSE file for more details.

Note: This readme assumes that you have the necessary dependencies and a compatible Python environment set up. If you encounter any issues during installation or usage, please consult the project's documentation and ensure that you have met all the requirements.
