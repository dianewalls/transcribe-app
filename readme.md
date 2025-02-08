# Transcribe Video to Text

This project uses OpenAI Whisper to transcribe audio from video files into text.

## 🚀 Features
- Converts video speech to text automatically
- Supports multiple languages

---

## 📌 Prerequisites
Before running the script, ensure you have the following installed:

### 1️⃣ Install Python (Recommended: **Python 3.11**)

#### **Mac (Using Homebrew)**
```sh
brew install python@3.11
brew link --force --overwrite python@3.11
```

#### **Windows/Linux**
Download from: [Python Official Website](https://www.python.org/downloads/)

Verify installation:
```sh
python3 --version
```

### 2️⃣ Install **ffmpeg** (Required for extracting audio from video)

#### **Mac (Using Homebrew)**
```sh
brew install ffmpeg
```

#### **Windows (Using Chocolatey)**
```sh
choco install ffmpeg
```

#### **Linux (Ubuntu/Debian)**
```sh
sudo apt update && sudo apt install ffmpeg -y
```

Verify installation:
```sh
ffmpeg -version
```

---

## 📥 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/dianewalls/transcribe-app.git
cd transcribe-app
```

### 2️⃣ Create a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

## 🏃 Usage

### **Basic Transcription (Default Whisper Model)**
```sh
python transcribe_video.py path/to/video.mp4
```
The transcript will be saved in `transcript.txt`.

---

## ✅ Troubleshooting

### **1. `ffmpeg: command not found`**
Ensure `ffmpeg` is installed and available in PATH. Run:
```sh
ffmpeg -version
```

### **2. `python3: command not found`**
Ensure Python 3.11 is installed and set correctly:
```sh
python3 --version
```

---

## 📜 License
This project is open-source under the MIT License.

---

## 🤝 Contributing
Feel free to submit issues or pull requests!

---

## 📧 Contact
For any questions, reach out to **dianewalls+github@gmail.com** or open an issue in the repository.

Happy Transcribing! 🚀

