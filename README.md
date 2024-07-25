# PDFChatbot
A chatbot that is capable enough in answering questions related to the given PDF 
# PDF Chatbot

## Overview

The PDF Chatbot is an interactive web application built using Streamlit. This app allows users to interact with PDFs and extract information using a chatbot interface. The application leverages various APIs and tools to provide seamless and accurate information extraction from PDFs.

## Features

- Interactive chatbot interface for querying PDFs.
- Easy-to-use web interface built with Streamlit.
- Support PDF document.
- Efficient and accurate information extraction.

## Requirements

- Python 3.10.14
- Streamlit
- Poetry (for dependency management)
- API keys: REPLICATE_API_TOKEN

## Installation

### Clone the Repository

First, clone the repository from GitHub:

```sh
git clone https://github.com/yourusername/pdf-chatbot.git
cd pdf-chatbot
```

### Install Dependencies

This project uses Poetry for dependency management. To install Poetry, follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

Once Poetry is installed, run the following command to install the project dependencies:

```sh
poetry install
```

### API Keys

The application requires API keys for certain functionalities. Obtain the necessary API keys and set them as environment variables. For example:

```sh
export REPLICATE_API_TOKEN=your_replicate_api_token
```

## Usage

To run the Streamlit app, use the following command:

```sh
poetry run streamlit run app.py
```

This will start the Streamlit server, and you can access the application in your web browser at `http://localhost:8501`.

## Contributing

We welcome contributions to the PDF Chatbot project. If you have suggestions, bug reports, or pull requests, please feel free to submit them on our GitHub repository.


## Acknowledgements

We would like to thank the developers of Streamlit, Poetry, and other open-source projects that made this application possible.

## Contact

For any questions or inquiries, please contact us at [your email address].
