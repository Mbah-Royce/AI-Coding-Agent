# 🤖 AI Agent with Google GenAI Function Calling

A Python-based AI agent built using **Google GenAI** and the **Gemini 3.6 Flash** model. The project explores how an LLM can interact with the local environment by calling custom Python functions.

The agent was designed and tested with tools that allow it to **inspect directories, read files, write files, and execute Python files**. A simple calculator application was also used to test the agent's ability to interact with Python code through function calling.

## ✨ Features

* 🤖 AI agent powered by **Google GenAI**
* ⚡ Uses **Gemini 3.6 Flash**
* 🐍 Built with **Python**
* 🔧 Implements LLM **function calling**
* 📂 Read directory contents
* 📖 Read file contents
* ✍️ Write content to files
* ▶️ Execute Python files
* 🧮 Tested with a Python calculator application
* 🔄 Agent can select and invoke tools based on the user's request

## 🛠️ Implemented Tools

The agent has access to several custom Python functions that allow it to interact with the local filesystem and execute Python code.

### 1. Read Directory

Allows the agent to inspect the contents of a directory.

Example request:

```text
List the files in the current directory.
```

The model can invoke the directory-reading function and use the returned file/folder information in its response.

---

### 2. Read File

Allows the agent to retrieve and inspect the contents of a file.

Example:

```text
Read the contents of calculator.py
```

The agent determines that the file-reading tool is required, invokes it, and receives the file contents.

---

### 3. Write to File

Allows the agent to create or modify files by writing content to them.

Example:

```text
Create a Python file called calculator.py
that contains a simple addition function.
```

The model can generate the required content and invoke the file-writing function.

---

### 4. Run Python File

Allows the agent to execute a Python file and receive its output.

Example:

```text
Run calculator.py
```

The agent invokes the Python execution function, receives the program output, and can use that output when generating its final response.

## 🧮 Calculator Application

A simple **Python calculator application** was used as a test case for the agent.

This provided a practical way to test the complete tool-calling workflow:

```text
User Request
     │
     ▼
Gemini 3.6 Flash
     │
     │ Determines required tool
     ▼
Function Call
     │
     ▼
Python Function
     │
     ├── Read Directory
     ├── Read File
     ├── Write File
     └── Run Python File
     │
     ▼
Tool Result
     │
     ▼
Gemini 3.6 Flash
     │
     ▼
Final Response
```

For example, the agent could be asked to inspect a calculator file, modify it, and execute it:

```text
User:
Read calculator.py, add a multiplication function,
and run the file to test it.
```

The agent can break this request into a sequence of tool calls:

```text
1. Read calculator.py
        ↓
2. Generate updated code
        ↓
3. Write updated calculator.py
        ↓
4. Run calculator.py
        ↓
5. Return the result to the user
```

This demonstrates how an LLM can act as an **orchestration layer** between a user and traditional Python functionality.

## 🧠 How Function Calling Works

Function calling allows the model to request that the application execute a specific function with specific arguments.

Conceptually, the interaction looks like:

```text
                 ┌──────────────┐
                 │     User     │
                 └──────┬───────┘
                        │
                        ▼
              ┌───────────────────┐
              │  Gemini 3.6 Flash │
              └─────────┬─────────┘
                        │
                  Tool Selection
                        │
                        ▼
              ┌───────────────────┐
              │   Function Call   │
              └─────────┬─────────┘
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
       Read File   Write File   Run Python
            │           │           │
            └───────────┼───────────┘
                        │
                        ▼
                 Tool Response
                        │
                        ▼
              ┌───────────────────┐
              │  Gemini 3.6 Flash │
              └─────────┬─────────┘
                        │
                        ▼
                 Final Response
```

The important distinction is that the **model does not directly perform these operations**. Instead, it requests a tool call, and the Python application executes the corresponding function.

## 🔧 Technologies

| Technology                 | Purpose                                                |
| -------------------------- | ------------------------------------------------------ |
| **Python**                 | Core programming language                              |
| **Google GenAI**           | SDK for interacting with Google's generative AI models |
| **Gemini 3.6 Flash**       | LLM powering the agent                                 |
| **Function Calling**       | Connects the LLM with custom Python functions          |
| **Python Filesystem APIs** | Used for directory and file operations                 |

## 🚀 Getting Started

### Prerequisites

* Python >=3.10
* Google GenAI API key
* pip

### Clone the repository

```bash
git clone https://github.com/Mbah-Royce/AI-Coding-Agent
cd AI-Coding-Agent
```

### Create a virtual environment

```bash
uv venv
```


### Install dependencies

```bash
uv pip install -r pyproject.toml
```

### Configure the API key

Create a `.env` file and add your Google GenAI API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit your `.env` file to the repository.

### Run the agent

```bash
uv run aiagent <prompt>
```

Use the application to send requests to the agent and observe how it selects and executes the available tools.

## 🧪 Example Tasks

Once the agent is running, example prompts include:

```text
List the files in this directory.
e.g uv run aiagent "what files are in the tests directory"
```

```text
Read the contents of calculator.py.
e.g uv run aiagent "what is the content of calculator.py"
```

```text
Create a new Python file called test.py containing
a program that prints "Hello World".
```

```text
Run test.py.
```

```text
Read calculator.py, modify it to add multiplication,
and run it.
```

These tasks test different combinations of the implemented functions.

## 🎯 Project Goals

The main objective of this project was to understand how **LLMs can interact with external tools and application logic** through function calling.

The project demonstrates several fundamental concepts behind modern AI agents:

* Tool definition
* Function calling
* Tool selection by an LLM
* Passing arguments from the model to Python
* Executing application functions
* Returning function results to the model
* Chaining multiple tool calls
* Using an LLM to orchestrate multiple operations

## 🔮 Future Improvements

Potential improvements include:

* Add more tools and APIs
* Implement persistent conversation memory
* Add better tool error handling
* Add input validation
* Support more programming languages
* Add automated unit and integration tests
* Add a web-based interface
* Add permission controls for file operations
* Add sandboxing for Python execution
* Add logging and agent execution traces
* Deploy the agent as a web service

## ⚠️ Security Considerations

Because the agent can **read files, write files, and execute Python code**, these capabilities should be treated carefully.

For production use, file and code execution tools should be restricted using appropriate:

* Directory permissions
* Input validation
* Sandboxed execution environments
* Resource limits
* Authentication and authorization

The implementation is intended primarily as an educational demonstration of **LLM tool use and function calling** and caution should be taken when any apsect of the project is to be made use of.

## 📚 Key Takeaway

This project demonstrates the transition from a simple LLM chatbot to a **tool-using AI agent**.

Instead of only generating text, the agent can interact with its environment:

```text
                 LLM
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
     Inspect    Modify    Execute
     Files      Files     Python
```

The calculator application serves as a simple practical example, while the underlying architecture can be extended to much more powerful tools such as APIs, databases, web services, development tools, and other external systems.

## Resources
This project is a tutorial from https://www.youtube.com/watch?v=YtHdaXuOAks
