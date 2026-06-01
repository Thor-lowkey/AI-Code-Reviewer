# AI Code Reviewer

AI Code Reviewer is a web-based application that leverages Google's Gemini model to perform automated code reviews across multiple programming languages.

The platform analyzes submitted source code and generates structured engineering feedback covering code quality, potential defects, performance considerations, security risks, maintainability, and industry best practices.

Built with FastAPI, Streamlit, and Google Gemini, the project demonstrates the integration of modern AI systems into software development workflows.

---

## Features

* Automated code review using Google Gemini
* Multi-language support

  * Python
  * C++
  * Java
  * JavaScript
* Bug and issue detection
* Security vulnerability assessment
* Performance analysis
* Code quality evaluation
* Engineering scorecard generation
* Modern web-based interface

---

## Technology Stack

| Layer             | Technology       |
| ----------------- | ---------------- |
| Frontend          | Streamlit        |
| Backend           | FastAPI          |
| AI Model          | Gemini 2.5 Flash |
| Language          | Python           |
| API Communication | REST             |

---

## Project Structure

```text
AI-Code-Reviewer/
│
├── backend/
│   ├── ai_service.py
│   ├── main.py
│   └── .env
│
├── frontend/
│   └── app.py
│
├── run.sh
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Thor-lowkey/AI-Code-Reviewer.git
cd AI-Code-Reviewer
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the `backend` directory:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## Running the Application

Make the startup script executable:

```bash
chmod +x run.sh
```

Start the application:

```bash
./run.sh
```

The startup script automatically:

* Launches the FastAPI backend
* Starts the Streamlit frontend
* Uses the project's virtual environment
* Handles process cleanup on exit

---

## Application Access

| Service           | URL                        |
| ----------------- | -------------------------- |
| Frontend          | http://localhost:8501      |
| Backend API       | http://localhost:8000      |
| API Documentation | http://localhost:8000/docs |

---

## Future Enhancements

* Repository-level analysis
* Multi-file code review
* PDF report generation
* GitHub integration
* Review history and analytics
* CI/CD workflow support

---

## Author

Ali Bhai

Bachelor of Artificial Intelligence

---
