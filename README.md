# MCP Crash Course

A project demonstrating how to connect to an MCP (Model Context Protocol) server using LangChain and Google Gemini.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

## Setup

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Or create it manually and add the following:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

To get a `GOOGLE_API_KEY`, visit [Google AI Studio](https://aistudio.google.com/app/apikey) and generate an API key.

### 3. Run the project

```bash
uv run main.py
```
