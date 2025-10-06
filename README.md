# rag_pipeline_PanScience_Innovations

Built a document parsing and LLM query application that extracts and structures information from PDFs, enabling natural language queries on the content using a vector database and local LLMs.

**Note:** To function properly, this pipeline requires a running **Mistral model on Ollama**, which serves as the local LLM backend for generating responses.

---

## Features

- Parse PDF documents and extract structured information.
- Store and query data using a vector database.
- Query PDFs using natural language via a local LLM (Mistral on Ollama).
- Fully containerized using Docker for easy setup.
- Works on **Windows** and **Mac**. For **Linux**, future modifications may be required.

---

## Prerequisites

- Docker installed on your system ([Docker Desktop](https://www.docker.com/products/docker-desktop)).
- Ollama installed and the Mistral model running locally.
- (Optional) Git, if you want to clone the repository.

---

## Setup Instructions

### 1. Pull the Docker Image

```bash
docker pull ghcr.io/harshindcoder/rag-pipeline-panscience-innovations:latest
````

### 2. Run the Container

Open a terminal and run:

```bash
docker run -it -p 8000:8000 ghcr.io/harshindcoder/rag-pipeline-panscience-innovations:latest
```

* `-p 8000:8000` maps the FastAPI port in the container to your local machine.
* `-it` allows interactive terminal access.
* `--rm` can be added if you want the container to be removed after stopping.

---

### 3. Start Ollama with Mistral

Open another terminal and run:

```bash
ollama run mistral
```

* The container expects to connect to Ollama at `http://localhost:11434`. Make sure this port is open.
* Mistral must be running while using the API.

---

### 4. Upload a PDF

Open a **new terminal** and run:

```bash
curl -X POST -F "file=@/path/to/your/document.pdf" http://localhost:8000/upload
```

* Replace `/path/to/your/document.pdf` with the actual path of your PDF.
* This uploads the PDF to the pipeline for parsing and vectorization.

---

### 5. Ask Questions

Once the file is uploaded, in the same terminal (or a new one), run:

```bash
curl -X POST -F "question=What is this file about?" http://localhost:8000/ask
```

* The pipeline will query the parsed document via Mistral on Ollama and return the answer.

---

## Notes

* **Terminals:** You need at least **two terminals**: one for Docker/FastAPI, one for Ollama. The `curl` commands can run in the same terminal or separate ones.
* **File paths:** Replace `/path/to/your/document.pdf` with your PDF location.
* **Port:** The API assumes `FastAPI` runs on port `8000`. Adjust `-p` in `docker run` if needed.

---

## Future Improvements

* Add Linux compatibility.
* Multi-user support for larger document processing.
* Better error handling for missing Mistral/Ollama connections.
