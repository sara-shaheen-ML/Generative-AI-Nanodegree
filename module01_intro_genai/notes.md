# 🧠 Generative AI Nanodegree – Cheat Sheet

A concise reference of key concepts, models, and terminology covered throughout the Generative AI Nanodegree.  
Useful for **revision**, **interviews**, and **teaching**.

---

## 1. Foundation Models & LLMs
- **Foundation Model**: A large, pre-trained, general-purpose AI model that serves as a base for many tasks.
- **LLM (Large Language Model)**: A foundation model trained specifically on text.
- **Key relationship**:  
  > All LLMs are foundation models, but not all foundation models are LLMs.

---

## 2. Model Types
- **Commercial Models**
  - GPT (OpenAI), Gemini (Google), Claude (Anthropic)
  - Closed-source, accessed via API, pay-per-use
- **Open-weight Models**
  - LLaMA (Meta), Falcon, Qwen, Mistral
  - Model weights are downloadable and runnable locally
- **Open-source Models**
  - Fully released under open licenses (e.g., Apache 2.0)
  - Example: Falcon 7B / 40B

---

## 3. Model Origins
- **Meta** → LLaMA
- **OpenAI** → GPT
- **Google DeepMind** → Gemini, Gemma
- **Anthropic** → Claude
- **Alibaba** → Qwen
- **TII (UAE)** → Falcon
- **KAUST** → Foundational AI research ecosystem and contributions

---

## 4. Weights & Training
- **Weights**: Learned parameters of a neural network.
- **Parameters**: Individual numerical values (billions in LLMs).
- **Pre-training**: Training on massive, general-purpose data.
- **Self-supervised Learning**: Learning from unlabeled data by predicting parts of the input.

---

## 5. Data Concepts
- **Common Crawl**
  - Massive open dataset of public web pages.
- **RefinedWeb**
  - Cleaned and filtered version of Common Crawl (used by Falcon).
- **Textbook-formatted Data**
  - Structured, pedagogical, high-quality data.
- **Key Insight**
  - High-quality, structured data allows models to learn faster with less data.

---

## 6. Prompting Basics
- **System Prompt**
  - Sets role, behavior, and constraints.
- **User Prompt**
  - Specifies the task to perform.
- **Prompt Engineering**
  - Designing prompts to guide model behavior.
- **Zero-shot Prompting**
  - No examples provided.
- **Few-shot Prompting**
  - Examples included in the prompt.

---

## 7. APIs & Access
- **API (Application Programming Interface)**: Interface for interacting with models.
- **API Key**: Private credential granting access to a model.
- **LiteLLM**: Unified wrapper for calling different LLM providers.
- **Vocareum Keys (`voc-...`)**
  - Work only inside Udacity/Vocareum
  - Limited usage budget

---

## 8. Local vs Cloud Execution
### Cloud / Remote Models
- GPT, Gemini, Claude
- Run on remote servers
- Require API access and payment

### Local / Offline Models
- LLaMA, Falcon, Mistral, Qwen
- Run directly on your laptop
- Free after download

**Tools for local execution**
- Ollama
- LM Studio
- Hugging Face Transformers

---

## 9. Optimization Concepts
- **Quantization**
  - Reducing precision (e.g., 4-bit, 8-bit) to run models on smaller hardware.
- **Inference**
  - Using a trained model to generate outputs.

---

## 10. Programming & Testing
- Python `.py` files
- `unittest` framework
- Test cases & test classes
- Test-Driven Development (TDD)
- LLM-assisted test generation

---

## 11. Algorithms & Exercises
- Merge Sort
- Divide-and-Conquer
- Recursion
- Edge cases (empty lists, duplicates, invalid inputs)

---

## 12. Licensing
- **Apache 2.0**
  - Permissive open-source license (e.g., Falcon 7B/40B).
- **Proprietary Licenses**
  - Closed commercial models (GPT, Claude, Gemini).

---

## 13. Practical Nanodegree Strategy
- Use **Vocareum** minimally (instructions, grading).
- Do real development **locally**.
- Prefer:
  - Local open-source models (free)
  - Small, cost-efficient API models if needed
- Push clean, documented code to GitHub as a portfolio.

---

## 🔑 Ultra-Short Memory Hook
> Foundation models are large pre-trained models.  
> LLMs are text-based foundation models.  
> Open models can run locally.  
> Commercial models require APIs.  
> Data quality beats data quantity.  
> Prompting controls behavior.

