```
# Analyst Note Generator

Analyst Note Generator is a tool that generates analyst notes based on PDF files. It uses natural language processing models to analyze the content of the PDF and extract key information for the analyst note.

## Features

- Easy-to-use interface to upload PDF files and generate analyst notes.
- Supports multiple language models (LLM) such as GPT4 and ChatGPT.
- Provides options for different chain types (map_reduce, stuff, refine).
- Adjustable chunk size and overlap for fine-tuning the summarization process.
- Generates a comprehensive summary including financial highlights, segment performance, key remarks, outlook, market trends, strategies, challenges, and opportunities.

## Installation

To use Analyst Note Generator, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/mvsbm/AnalystNote
```

2. Navigate to the project directory:

```shell
cd AnalystNote
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

```shell
streamlit run app.py
```

2. Access the app through your web browser (usually at http://localhost:8501).
3. Select the language model (LLM) to use from the sidebar.
4. Choose the chain type for the summarization process from the sidebar.
5. Adjust the chunk size and overlap using the sliders to optimize the summarization process.
6. Enter the company name for the analyst note.
7. Upload the PDF file containing the earnings call details.
8. Click the "Generate Analyst Note" button to start the analysis and summarization process.
9. Wait for the process to complete. Progress updates will be displayed.
10. Once the summary is generated, it will be displayed in the app.

## Troubleshooting

If you encounter any issues or have questions, please refer to the [README.md](https://github.com/mvsbm/AnalystNote) in the GitHub repository for more information. You can also reach out to the developer via email at s-ma@coloplnext.co.jp.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or submit a pull request in the GitHub repository.

## License

This project is licensed under the [MIT Licence](https://opensource.org/licenses/mit). Please refer to the LICENSE file for more details.

---

**Note:** This readme assumes that you have the necessary dependencies and a compatible Python environment set up. If you encounter any issues during installation or usage, please consult the project's documentation and ensure that you have met all the requirements.
```
```
