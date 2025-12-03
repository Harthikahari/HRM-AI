# HRM-AI: The Next-Gen AI-Powered Applicant Tracking System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/react-%2320232a.svg?style=flat&logo=react&logoColor=%2361DAFB)](https://reactjs.org/)

**HRM-AI** is a production-grade, open-source Applicant Tracking System (ATS) designed to revolutionize recruitment through autonomous multi-modal AI agents. Built with a modern tech stack, it automates the entire hiring lifecycle—from intelligent resume parsing and ranking to automated assessments and interview scheduling.

## 🚀 Key Features

*   **🤖 Autonomous AI Agents**: Specialized agents for parsing, scoring, emailing, and scheduling, orchestrated by LangGraph.
*   **📄 Intelligent Resume Parsing**: Extracts structured data from PDFs/DOCX using multi-modal LLMs, stored with vector embeddings for semantic search.
*   **🎯 Context-Aware Scoring**: Ranks candidates not just by keywords, but by semantic relevance to the Job Description (JD).
*   **📝 Adaptive Assessments**: Generates unique, domain-specific technical assessments tailored to each candidate's profile.
*   **📅 Smart Scheduling**: Auto-coordinates interviews between panels and candidates using Outlook/Google Calendar integrations.
*   **📊 Observable Pipeline**: Real-time Kanban board for candidate tracking with deep analytics.
*   **🔒 Enterprise-Ready**: Role-Based Access Control (RBAC), secure API design, and self-hostable via Docker.

## 🛠️ Tech Stack

*   **Backend**: Python 3.11, FastAPI, Celery, LangChain/LangGraph
*   **Frontend**: React 18, TypeScript, Vite, Tailwind CSS, ShadCN UI
*   **Database**: PostgreSQL 16 + `pgvector` (Vector Search)
*   **Storage**: MinIO (S3-compatible object storage)
*   **Infrastructure**: Docker Compose, Nginx, Redis
*   **AI Engine**: Open-Source MCP Server connecting to Claude 3.5/3.7

## 📦 Installation & Setup

### Prerequisites
*   Docker & Docker Compose
*   Git

### Quick Start

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Harthikahari/HRM-AI.git
    cd HRM-AI
    ```

2.  **Configure Environment**
    Copy the example environment file and update the keys:
    ```bash
    cp .env.example .env
    # Edit .env with your API keys (OpenAI/Anthropic, Postgres credentials, etc.)
    ```

3.  **Launch with Docker**
    ```bash
    docker compose up -d --build
    ```

4.  **Access the Application**
    *   **Frontend Dashboard**: `http://localhost`
    *   **API Documentation**: `http://localhost/api/docs`
    *   **MinIO Console**: `http://localhost:9001`

## 📖 Documentation

For detailed deployment instructions on an Ubuntu server, please refer to the [Server Implementation Guide](server_implementation_guide.md).

## 🤝 Contributing

We welcome contributions! Please see our [Contribution Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and request features.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
