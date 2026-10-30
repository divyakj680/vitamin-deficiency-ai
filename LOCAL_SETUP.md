# 🖥️ Running NutriVision AI Locally (VS Code Setup)

> **Why it works on the live site but not locally:**  
> The live website has **3 servers running simultaneously** (Frontend, Backend, AI Engine) plus a **MySQL database** — all pre-configured and connected. When you clone to a new laptop and just open VS Code, **none of those servers are running**, so photo upload fails because there's nothing to receive the request.

---

## ✅ What You Need to Install First

Install these **once** before anything else:

| Tool | Version | Download |
|------|---------|---------|
| **Java JDK** | 17 | https://adoptium.net/temurin/releases/?version=17 |
| **Maven** | 3.9+ | https://maven.apache.org/download.cgi |
| **Node.js** | 20+ (LTS) | https://nodejs.org/en/download |
| **Python** | 3.11 | https://www.python.org/downloads/release/python-3110/ |
| **MySQL** | 8.0 | https://dev.mysql.com/downloads/mysql/ |

> **Verify installs:** Open a new terminal and run:
> ```
> java -version       → should say: openjdk version "17.x.x"
> mvn -version        → should say: Apache Maven 3.x.x
> node -version       → should say: v20.x.x or v22.x.x
> python --version    → should say: Python 3.11.x
> mysql --version     → should say: mysql  Ver 8.x
> ```

---

## 📁 Step 1 — Clone the Repository

```bash
git clone https://github.com/divyakj680/vitamin-deficiency-ai.git
cd vitamin-deficiency-ai
```

---

## 🗄️ Step 2 — Set Up the Database (MySQL)

Open MySQL command line or MySQL Workbench and run these commands:

```bash
# Option A: Using terminal (Windows)
mysql -u root -p < database\schema.sql
mysql -u root -p nutrivision_db < database\seed_symptoms.sql
mysql -u root -p nutrivision_db < database\seed_nutrition.sql
```

> **Default MySQL credentials assumed:** Username = `root`, Password = `root`  
> If your MySQL has a different password, update it in Step 3 (Backend `.env`).

**Verify:** In MySQL, run `SHOW DATABASES;` — you should see `nutrivision_db`.

---

## ⚙️ Step 3 — Configure Environment Files

You need to create **3 `.env` files** (one per service). These are NOT in GitHub for security reasons.

### 3A. Backend `.env` → create file: `backend/.env`
```env
SPRING_PROFILES_ACTIVE=dev
SPRING_DATASOURCE_URL=jdbc:mysql://localhost:3306/nutrivision_db?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
SPRING_DATASOURCE_USERNAME=root
SPRING_DATASOURCE_PASSWORD=root
APP_JWT_SECRET=nutrivision_local_dev_secret_key_at_least_32_chars_long_abc123
APP_CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173
AI_SERVICE_BASE_URL=http://127.0.0.1:8000/api/ai
APP_STORAGE_UPLOAD_DIR=./uploads/assessments
```
> Change `SPRING_DATASOURCE_PASSWORD=root` to your actual MySQL password if different.

### 3B. AI Service `.env` → create file: `ai-service/.env`
```env
APP_ENV=development
HOST=0.0.0.0
PORT=8000
DEBUG=True
MODELS_DIR=./models/trained
ACTIVE_MODEL_VERSION=v1.0.0-mobilenetv2
BLUR_LAPLACIAN_THRESHOLD=100.0
MIN_BRIGHTNESS_LUMINANCE=40.0
MAX_BRIGHTNESS_LUMINANCE=220.0
MIN_IMAGE_WIDTH=224
MIN_IMAGE_HEIGHT=224
DEFAULT_TOP_K=3
CONFIDENCE_INCONCLUSIVE_THRESHOLD=0.35
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173
LOG_LEVEL=INFO
```

### 3C. Frontend `.env` → create file: `frontend/.env`
```env
VITE_API_BASE_URL=http://localhost:8080/api
VITE_AI_SERVICE_URL=http://localhost:8000/api/ai
VITE_APP_ENV=development
VITE_APP_NAME="NutriVision AI"
VITE_DEFAULT_LANGUAGE=en
VITE_ENABLE_VOICE_INPUT=true
VITE_ENABLE_TEXT_TO_SPEECH=true
VITE_ENABLE_GRAD_CAM_VIEWER=true
VITE_ENABLE_MAPS=true
```
> **Note:** The frontend uses a Vite proxy (configured in `vite.config.ts`), so you may also leave `VITE_API_BASE_URL` and `VITE_AI_SERVICE_URL` blank — the proxy handles routing automatically in dev mode.

---

## 🤖 Step 4 — Start the AI Service (Python FastAPI)

Open **Terminal 1** in VS Code:

```bash
cd ai-service

# Create virtual environment (first time only)
python -m venv .venv

# Activate it
.venv\Scripts\activate          # Windows
# OR: source .venv/bin/activate  (Mac/Linux)

# Install dependencies (first time only)
pip install -r requirements.txt

# Start the AI server
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

✅ **Success looks like:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Successfully loaded model from .../mobilenetv2_nutrivision_v1.onnx
```

❌ **If you see:** `ModuleNotFoundError: No module named 'onnxruntime'`  
→ Run: `pip install onnxruntime`

❌ **If you see:** `ModuleNotFoundError: No module named 'cv2'`  
→ Run: `pip install opencv-python-headless`

---

## ☕ Step 5 — Start the Backend (Java Spring Boot)

Open **Terminal 2** in VS Code:

```bash
cd backend
mvn spring-boot:run
```

> First run downloads dependencies — may take 3–5 minutes.

✅ **Success looks like:**
```
Started NutriVisionApplication in 8.4 seconds
Tomcat started on port(s): 8080 (http)
```

❌ **If you see:** `Access denied for user 'root'@'localhost'`  
→ Check your `backend/.env` — fix `SPRING_DATASOURCE_PASSWORD` to match your MySQL password.

❌ **If you see:** `Unknown database 'nutrivision_db'`  
→ You haven't run Step 2 yet. Go back and initialize the database.

---

## ⚛️ Step 6 — Start the Frontend (React/Vite)

Open **Terminal 3** in VS Code:

```bash
cd frontend
npm install         # first time only
npm run dev
```

✅ **Success looks like:**
```
VITE v5.x.x  ready in 800 ms
➜  Local:   http://localhost:5173/
```

Now open your browser at **http://localhost:5173** — the full app is running!

---

## 🧪 Quick Verify — Does Photo Upload Work?

1. Open http://localhost:5173
2. Register a new account or log in
3. Go to **New Assessment**
4. Select a body part (e.g., Nails)
5. Upload any photo
6. Click **Analyze**

✅ If you see results — everything is working!  
❌ If you see an error — check the troubleshooting section below.

---

## 🔧 Troubleshooting Common Errors

### ❌ "Unable to connect to Vitamin Deficiency Backend"
- The Spring Boot backend is not running. Start Terminal 2 (Step 5).
- Or it crashed — check Terminal 2 for red error messages.

### ❌ "AI Service is not available" / photo upload hangs
- The FastAPI AI service is not running. Start Terminal 1 (Step 4).
- Verify it's running: open http://localhost:8000/docs in browser.

### ❌ "CORS error" in browser console
- Your backend `APP_CORS_ALLOWED_ORIGINS` in `backend/.env` must include `http://localhost:5173`.

### ❌ Backend starts but shows "Access Denied" (MySQL)
- Wrong password in `backend/.env`. Fix `SPRING_DATASOURCE_PASSWORD`.

### ❌ `java: error: release version 17 not supported`
- You have an older Java version. Install JDK 17 from https://adoptium.net

### ❌ `mvn: command not found`
- Maven is not installed or not in PATH. Add Maven's `bin/` folder to your system PATH.

### ❌ `pip install` fails with SSL errors
- Try: `pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt`

---

## 📊 Architecture Summary (Why 3 Terminals?)

```
Browser (http://localhost:5173)
    │
    ▼
Frontend: React + Vite          [Terminal 3] → Port 5173
    │ (API calls proxied by Vite)
    ▼
Backend: Java Spring Boot       [Terminal 2] → Port 8080
    │  (stores data in MySQL)
    │  (forwards image to AI service)
    ▼
AI Service: Python FastAPI      [Terminal 1] → Port 8000
    │  (runs ONNX model inference)
    ▼
MySQL Database                  [Always Running] → Port 3306
```

> All 4 of these must be running at the same time for photo upload to work.

---

## 💡 Pro Tip: VS Code Setup

1. Open the `vitamin-deficiency-ai` folder in VS Code
2. Install **Extension Pack for Java** extension
3. Install **Python** extension
4. Use VS Code's built-in terminal — press `` Ctrl+` `` to open, and use the `+` button to open multiple terminals
5. You can split the terminal panel to see all 3 running simultaneously

---

*Generated for NutriVision AI — Department of CSE, RRIT, 2026-27*
