

---

# 🚀 DAKIYA: The AI-Powered Web Scraper 📬

Welcome to **DAKIYA** – your intelligent, AI-driven tool for extracting and filtering web data, specifically job listings! 🕵️‍♂️ Powered by the **OLLaM Model**, DAKIYA combines the efficiency of **BeautifulSoup** and AI-based filtering to deliver **high-quality data** effortlessly. Let's scrape smarter, not harder! 💡

## ✨ Features
- 🔎 **Efficient Web Scraping**: Quickly extract job listings with BeautifulSoup.
- 🤖 **AI-Enhanced Filtering**: The OLLaM model intelligently filters and processes data for meaningful results.
- 🛠️ **ChromeDriver Integration**: Automate the scraping process with easy browser automation.
- 📊 **Flexible Output**: Export and save data in customizable formats.

## ⚙️ Setup Guide

### 1. Clone the Repository 🛠️
```bash
git clone https://github.com/Sunnysain/DAKIYA.git
cd DAKIYA
```

### 2. Create a Virtual Environment 🐍
To keep your dependencies isolated and avoid conflicts, it's recommended to create a virtual environment. Follow these steps:

#### On Windows:
```bash
python -m venv DAKIYA
```
#### On MacOS/Linux:
```bash
python3 -m venv DAKIYA
```

Activate the virtual environment:

- **Windows**: 
  ```bash
  .\DAKIYA\SCRIPTS\ACTIVATE.PS1
  ```
- **MacOS/Linux**:
  ```bash
  source DAKIYA/bin/activate
  ```

### 3. Install Dependencies 📦
Once your virtual environment is activated, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Install OLLaM API 🤖
- Head to the [OLLaM API Docs](https://github.com/ollam-ai) and follow the setup instructions.
- Configure your API key and settings within `parse.py` for smooth integration.

### 5. Set up ChromeDriver 🌐
- Download the latest version of **ChromeDriver** [here](https://sites.google.com/chromium.org/driver/).
- Place the `chromedriver.exe` in the project directory.

### 6. Run the Scraper 🏃‍♂️
Kick off the scraping process by running:
```bash
python main.py
```

## 📂 Project Structure

Here's what the directory structure looks like:
```
C:\AI DAKIYA
├── DAKIYA
|
├── main.py
├── parse.py
├── requirements.txt
|
└── __scrape.py__
```

## 💻 Connect with Me
- **GitHub**: [Dalchand's GitHub](https://github.com/Sunnysain)  
- **LinkedIn**: [Dalchand Sain](https://www.linkedin.com/in/dalchand-sain-26273a229/)

---

With these steps, you'll be all set to run **DAKIYA** within a virtual environment! 🚀 Happy Scraping! 😊
