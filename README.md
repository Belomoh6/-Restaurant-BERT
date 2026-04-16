# Restaurant-BERT: Low-Latency Intent Classification Engine

### Overview
This repository contains a proof-of-concept (PoC) intent classification module designed to serve as a low-latency triage layer preceding Generative LLM pipelines. By utilizing a fine-tuned DistilBERT architecture, the system deterministically categorizes high-volume restaurant client queries, significantly reducing API overhead, mitigating hallucination risks, and minimizing inference latency.

### System Architecture
* **Base Model:** `distilbert-base-uncased` (~66M parameters)
* **Serving Layer:** FastAPI (Local deployment)
* **Orchestration:** Designed for seamless integration with downstream webhook routers (e.g., n8n).

### Routing Logic & Taxonomy
The model maps incoming text payloads to four deterministic intents, allowing standard queries to be handled by zero-cost automated flows, while reserving expensive generative AI compute strictly for complex support issues.
1. `order`: Routes to menu/ordering systems.
2. `inquiry`: Routes to static FAQ responses (hours, location).
3. `greeting`: Routes to automated welcome messages.
4. `support`: Routes to human agents or advanced LLM pipelines.

### Performance Metrics
* **Inference Latency:** ~50 milliseconds (Benchmarked on local NVIDIA GPU).
* **Operating Cost:** Zero per-query API costs (Local execution).
* **Baseline Accuracy:** 94.50% (See Evaluation Methodology below).

### Evaluation Methodology & Limitations
The current V2 weights achieved a 94.50% accuracy with an average confidence score of 80.57% on a holdout test set. 

**Distribution Shift Disclaimer:** Both the training and evaluation datasets were synthetically generated to establish baseline intent definitions. Consequently, real-world inference confidence on organic human phrasing is expected to exhibit a distribution shift. Deployment into a production environment requires compiling a dataset of organic human-agent chat logs to retrain the classifier and optimize the calibration curve.

### Repository Contents
* `main.py`: FastAPI server for local model inference.
* `n8n_workflow.json`: Exported n8n orchestration nodes demonstrating the triage routing logic.

### Model Weights
The compiled `.safetensors` model and tokenizer configurations are hosted via Hugging Face to keep this repository lightweight.

https://huggingface.co/Belomoh66/Restaurant-BERT-Triage
