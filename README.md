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
- Docker Compose installed (usually included with Docker Desktop).
- Ollama installed and the Mistral model running locally.
- (Optional) Git, if you want to clone the repository.

---

## Setup Instructions

### 1. Pull the Docker Images

The Docker Compose file will pull both the application and MongoDB images automatically. If you want to pull manually:

```bash
docker pull ghcr.io/harshindcoder/rag-pipeline-panscience-innovations:latest
docker pull mongo:latest
````

---

### 2. Run the Services via Docker Compose

Create a file named `docker-compose.yml` (or use the one provided) with the following content:

```yaml
version: "3.9"

services:
  app:
    image: ghcr.io/harshindcoder/rag-pipeline-panscience-innovations:latest
    container_name: rrag_app
    ports:
      - "8000:8000"
    depends_on:
      - mongo

  mongo:
    image: mongo:latest
    container_name: rrag_mongo
    ports:
      - "27017:27017"
```

Then, in the terminal, run:

```bash
docker-compose up
```

* To run in the background (detached mode):

```bash
docker-compose up -d
```

* To view logs:

```bash
docker-compose logs -f
```

* To stop all services:

```bash
docker-compose down
```

---

### 3. Start Ollama with Mistral

Open another terminal and run:

```bash
ollama run mistral
```

* The container expects to connect to Ollama at `http://localhost:11434`.
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

Here’s the 6th point refined for your README:

---

### 6. Quick Manual Checks

For now, you can verify that everything is running with simple commands:

* **Check Docker containers:**

```bash
docker ps
```

* **Check FastAPI is responding:**

```bash
curl -X GET http://localhost:8000/docs
```

* **Parser and VectorDB** are verified via pytest:

```bash
pytest -v tests/
```
Tests are available in the repo but are not included in the production Docker image. Run them locally using pytest.

---

## Notes

* **Terminals:** You need at least **two terminals**: one for Docker Compose (FastAPI + MongoDB), one for Ollama. The `curl` commands can run in the same terminal or separate ones.
* **File paths:** Replace `/path/to/your/document.pdf` with your PDF location.
* **Ports:** FastAPI runs on `8000` and MongoDB on `27017`. Adjust the `ports` in `docker-compose.yml` if needed.

---

## Future Improvements

* Add Linux compatibility.
* Multi-user support for larger document processing.
* Better error handling for missing Mistral/Ollama connections.

---


