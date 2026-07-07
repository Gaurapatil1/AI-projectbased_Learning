# Week 1 - Day 1 | Python + Groq API Setup

## 📌 Objective

The goal of Day 1 is to set up the Python development environment and make the first API call to a Large Language Model (LLM) using the Groq SDK.

This project is the starting point of my AI Engineering journey.

---

## 🚀 What I Learned

- Python project setup using `uv`
- Creating and managing a virtual environment
- Installing Python packages
- Using `.env` files to store API keys securely
- Reading environment variables with `python-dotenv`
- Connecting to the Groq API
- Sending prompts to an LLM
- Understanding chat messages (`role` and `content`)
- Extracting the model's response

---

## 🛠 Technologies Used

- Python 3.13
- uv
- Groq SDK
- python-dotenv

---

## 📂 Project Structure

```
day1/
│── .venv/
│── .env
│── .python-version
│── hello_llm.py
│── main.py
│── pyproject.toml
│── uv.lock
│── README.md
│── .gitignore
```

---

## 📦 Installation

Clone the repository

```bash
git clone <repository-url>
cd week1/day1
```

Create virtual environment

```bash
uv venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶ Run the Project

```bash
python hello_llm.py
```

or

```bash
uv run hello_llm.py
```

---

## 💻 Code Flow

1. Load environment variables.
2. Read the Groq API key.
3. Create the Groq client.
4. Choose the LLM model.
5. Create a prompt.
6. Send the prompt to the model.
7. Receive the response.
8. Print the generated answer.

---

## 📜 Example Prompt

```
Hello, Groq! Can you tell me a joke about programming?
```

---

## 📤 Example Output

```
Why do programmers prefer dark mode?

Because light attracts bugs!
```

---

## 📚 Key Concepts Learned

- Environment Variables
- API Keys
- LLM
- Prompt
- Chat Completion API
- Role (`user`, `assistant`, `system`)
- Messages List
- Response Object

---

## 🎯 Day 1 Outcome

✅ Python environment configured

✅ Groq SDK installed

✅ First LLM API call completed

✅ Successfully received AI-generated response

---

## 📅 Roadmap Progress

- [x] Week 1 - Day 1 : Python + Groq Setup
- [ ] Day 2 : Prompt Engineering Basics
- [ ] Day 3 : Chatbot with Conversation Memory
- [ ] Day 4 : Streaming Responses
- [ ] Day 5 : Multiple LLM Providers