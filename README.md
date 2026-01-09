# Image Analysis Backend (FastAPI)

## How to Run





##  Setup

1. **Clone the repository**

```bash
git clone <repo_url>
cd veefyed-image-uploads
```

2. **Create a virtual environment**

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment

# On macOS/Linux:
source venv/bin/activate

# On Windows (PowerShell):
venv\Scripts\Activate.ps1

# On Windows (Command Prompt):
venv\Scripts\activate.bat
```
3. **Install dependencies**

```bash
pip install -r requirements.txt

```

4. **Configure environment variables (.env)**

```bash
API_KEY=secretapikey123
IMAGE_DIR=app/storage/images
LOG_LEVEL=INFO
LOG_FILE=app/logs/app.log
HOST=localhost

```

5. **Install dependencies**
```bash
pip install -r requirements.txt
```
6. **Run application**
```bash
uvicorn app.main:app --reload --host $HOST --port $PORT
```
