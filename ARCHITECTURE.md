# HRM-AI: Architecture & Process Flow

## 1. Project Objective
To develop a fully automated, production-grade, open-source Applicant Tracking System (ATS) using cutting-edge AI agents, multi-modal LLMs, and modern full-stack architecture. The system is designed to be self-hosted on Ubuntu servers, providing end-to-end automation of the recruitment lifecycle—from resume parsing to final offer rollout—while maintaining high security, observability, and a premium user experience.

## 2. System Architecture

The system follows a microservices-like architecture orchestrated by Docker Compose.

### High-Level Diagram

```mermaid
graph TD
    User[User (Admin/Recruiter/Candidate)] -->|HTTPS| Nginx[Nginx Reverse Proxy]
    Nginx --> Frontend[React + Vite UI]
    Nginx --> Backend[FastAPI Backend]
    
    subgraph "Application Layer"
        Backend --> Auth[Auth Service (OAuth2)]
        Backend --> API[REST API]
        Backend --> WS[WebSocket Manager]
    end
    
    subgraph "Data Layer"
        Backend --> DB[(PostgreSQL + pgvector)]
        Backend --> MinIO[(MinIO Object Storage)]
        Backend --> Redis[(Redis Cache/Queue)]
    end
    
    subgraph "Async Processing & AI"
        Backend -->|Task| Celery[Celery Workers]
        Celery -->|Orchestrate| Supervisor[LangGraph Supervisor Agent]
        
        Supervisor --> Parser[Resume Parser Agent]
        Supervisor --> Scorer[Candidate Scorer Agent]
        Supervisor --> Assessor[Assessment Agent]
        Supervisor --> Scheduler[Scheduler Agent]
        Supervisor --> Emailer[Emailer Agent]
        
        Parser & Scorer & Assessor & Scheduler & Emailer -->|Tool Calls| MCP[MCP Server]
    end
    
    subgraph "External Integrations (via MCP)"
        MCP --> Claude[Claude 3.5/3.7 API]
        MCP --> Gmail[Gmail/SMTP]
        MCP --> Cal[Outlook/Google Calendar]
        MCP --> Zoom[Zoom API]
    end
```

### Component Description

1.  **Frontend (React + Vite)**:
    *   Built with TypeScript, Tailwind CSS, and ShadCN UI.
    *   Provides the Admin Dashboard, Kanban Board, and Candidate Portal.
    *   Communicates with Backend via REST and WebSockets.

2.  **Backend (FastAPI)**:
    *   High-performance Python API.
    *   Handles authentication, business logic, and data persistence.
    *   Dispatches background tasks to Celery.

3.  **Database (PostgreSQL + pgvector)**:
    *   Stores relational data (Users, Jobs, Candidates).
    *   Stores **Vector Embeddings** of resumes and job descriptions for semantic search.

4.  **Object Storage (MinIO)**:
    *   S3-compatible storage for raw resume files (PDF/DOCX) and logs.
    *   Secure and private.

5.  **AI Orchestration (LangGraph + Celery)**:
    *   **Supervisor Agent**: Manages the state of a candidate application.
    *   **Specialized Agents**: Perform specific tasks (Parsing, Scoring, Scheduling).
    *   **MCP Server**: A secure bridge connecting AI agents to external tools (Zoom, Outlook, Gmail) without hardcoding integrations into the core agent logic.

## 3. Process Flow (End-to-End)

### Step 1: Candidate Application
1.  Candidate uploads resume via the Public Career Page.
2.  File is uploaded securely to **MinIO**.
3.  Backend creates a `Candidate` record and triggers the **Parsing Workflow**.

### Step 2: Intelligent Parsing & Scoring
1.  **Parser Agent** retrieves the file from MinIO.
2.  Uses OCR/LLM to extract structured JSON (Skills, Experience, Education).
3.  Generates a vector embedding of the resume.
4.  **Scorer Agent** compares the resume embedding with the Job Description embedding.
5.  Calculates a match score (0-100%) and generates a textual analysis.

### Step 3: Automated Assessment
1.  If Score > Threshold (e.g., 80%):
2.  **Assessment Agent** generates a unique set of technical questions based on the candidate's weak areas identified during parsing.
3.  **Emailer Agent** sends the assessment link to the candidate.

### Step 4: Interview Scheduling
1.  Candidate passes assessment.
2.  **Scheduler Agent** checks the Panel's calendar (via Microsoft Graph/MCP).
3.  Proposes available slots to the candidate.
4.  Once confirmed, auto-creates a Zoom/Teams meeting and sends invites.

### Step 5: Interview & Feedback
1.  Interview takes place.
2.  Panel submits feedback via the Admin Dashboard.
3.  System aggregates scores and moves candidate to "Offer" or "Reject" stage.

## 4. Deployment Strategy (Ubuntu Server)

The entire system is containerized using Docker.

1.  **Infrastructure**: Single Ubuntu Server (VPS/Cloud).
2.  **Orchestration**: Docker Compose manages all services (Frontend, Backend, DB, Redis, MinIO, Nginx).
3.  **Security**:
    *   **Nginx** handles SSL termination (HTTPS).
    *   **Docker Networks** isolate internal services (DB, Redis) from the public internet.
    *   **Environment Variables** manage secrets.

Refer to `server_implementation_guide.md` for step-by-step installation commands.
