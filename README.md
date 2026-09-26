# NutriVision AI - Deployment Ready

This is the production-ready source code for NutriVision AI, a full-stack nutritional analysis platform combining React, Spring Boot, and Python AI Services.

## ?? Project Architecture
- **Frontend**: React + Vite + Tailwind CSS
- **Backend API**: Java Spring Boot 17 + Spring Security + JWT
- **AI Microservice**: Python FastAPI + ONNX Runtime + OpenCV
- **Database**: MySQL 8.0

## ?? How to Run Locally

### 1. Database
Run a local MySQL instance on port 3306 and execute `init_local_db.bat`.

### 2. Backend (Spring Boot)
```bash
cd backend
mvn spring-boot:run
```
*(Runs on http://localhost:8080)*

### 3. AI Service (FastAPI)
```bash
cd ai-service
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```
*(Runs on http://localhost:8000)*

### 4. Frontend (React/Vite)
```bash
cd frontend
npm install
npm run dev
```
*(Runs on http://localhost:5173)*

## ?? Production Deployment Guide

The easiest and most reliable way to deploy this exact architecture is using **Render.com** (for backend/frontend/AI) and **Aiven.io** (for MySQL).

### Step 1: Push to GitHub
1. Create a new public/private repository on GitHub named `vitamin-deficiency-ai`.
2. Push this source code to the repository. Note that secrets are safely ignored by `.gitignore`.

### Step 2: Provision a MySQL Database (Aiven.io)
1. Go to [Aiven.io](https://aiven.io) and create a free MySQL 8.0 database.
2. Copy your Connection URI (it looks like `mysql://user:password@host:port/defaultdb`).
3. Replace the `jdbc:mysql://...` part in your backend environment variables with this host.

### Step 3: Deploy to Render (Blueprint)
1. Go to [Render.com](https://render.com) and connect your GitHub account.
2. Click **New > Blueprint**.
3. Connect your `vitamin-deficiency-ai` repository.
4. Render will automatically detect the `render.yaml` file and set up all 3 services!
5. In the Render dashboard, click on the **Environment** tab for the Backend service and enter your Aiven MySQL database credentials.

### Step 4: Verify
- Your frontend will be live at `https://your-app-name.onrender.com`.
- Test the image upload functionality to ensure the AI service is responding correctly.
