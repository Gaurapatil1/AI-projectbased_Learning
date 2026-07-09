# Day 2 -- AI Engineering 🚀

## What I Learned

### 1. Go Back One Folder

``` powershell
cd ..
```

Moves to the parent folder.

**Example** If you are in:

    C:\Projects\AI\Day2

After `cd ..`:

    C:\Projects\AI

------------------------------------------------------------------------

### 2. Create a New Project

``` powershell
uv init project_name
```

Creates a new Python project.

Example:

``` powershell
uv init ai-day2
```

------------------------------------------------------------------------

### 3. Create a Virtual Environment

``` powershell
uv venv --python 3.11
```

A virtual environment is like a **private room** for your project's
Python packages.

**Example** Project A uses FastAPI 0.110. Project B uses FastAPI 0.95.

Both can work without affecting each other.

------------------------------------------------------------------------

### 4. Activate the Virtual Environment

``` powershell
.\.venv\Scripts\Activate.ps1
```

After activation you will see:

``` text
(.venv)
```

This means Python installs packages only for this project.

------------------------------------------------------------------------

### 5. Install `python-dotenv`

``` powershell
uv add python-dotenv
```

`python-dotenv` loads secret values from a `.env` file.

Example `.env`

``` text
API_KEY=abc123
```

Python:

``` python
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("API_KEY"))
```

------------------------------------------------------------------------

# AI Concepts

## System Role

A **System Role** tells the AI how it should behave.

Example:

``` text
You are a Python teacher.
```

Now the AI explains everything like a teacher.

Another example:

``` text
You are a coding interviewer.
```

The AI asks interview questions instead of teaching.

------------------------------------------------------------------------

## Temperature

Temperature controls **how creative the AI is**.

-   Low temperature = safer, consistent answers
-   High temperature = more creative and varied answers

Example prompt:

``` text
Write a slogan for a coffee shop.
```

**Temperature = 0.1**

> Fresh coffee every day.

**Temperature = 1.0**

> Wake up your dreams---one magical cup at a time!

------------------------------------------------------------------------

# Quick Revision

## Commands

``` powershell
cd ..
uv init project_name
uv venv --python 3.11
.\.venv\Scripts\Activate.ps1
uv add python-dotenv
```

## Concepts

-   Virtual Environment = Private room for project packages.
-   python-dotenv = Reads secrets from a `.env` file.
-   System Role = AI's job or personality.
-   Temperature = Controls creativity.
