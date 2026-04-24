# 🤖 Gemini ChatBot Using Gradio

A conversational AI chatbot powered by Google's Gemini Pro model with a clean Gradio web interface. This project includes two versions: a simple chatbot and an advanced one with configurable settings.

## ✨ Features

### Basic Chatbot (`gemini_chatbot.py`)
- 💬 Interactive chat interface
- 🤖 Powered by Google's Gemini Pro model
- 🎨 Clean and modern UI with Gradio Soft theme
- 📝 Conversation history support
- 🔄 Clear chat button to restart conversations

### Advanced Chatbot (`gemini_chatbot_advanced.py`)
- Everything in the basic version, plus:
- ⚙️ Customizable **system prompt** to set the model's persona
- 🌡️ **Temperature slider** to control creativity (0.0 – 1.0)
- 📏 **Max tokens slider** to control response length (100 – 8000)
- 📋 Copy button on chat messages
- 🔄 Retry button to regenerate the last response

## 🛠️ Prerequisites

- Python 3.8 or higher
- A Google Gemini API key — get one free from [Google AI Studio](https://aistudio.google.com/app/apikey)

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/technicalabinesh/Gemini-ChatBot-Using-Gradio.git
cd Gemini-ChatBot-Using-Gradio
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set your Gemini API key:**

**Option A — Environment variable (recommended):**
```bash
# Linux / macOS
export GEMINI_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:GEMINI_API_KEY="your-api-key-here"
```

**Option B — Edit the source file:**

Open `gemini_chatbot.py` (or `gemini_chatbot_advanced.py`) and replace:
```python
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
```
with your actual key:
```python
API_KEY = "your-actual-api-key-here"
```

> ⚠️ Never commit your API key to source control.

## 🚀 Usage

### Run the basic chatbot
```bash
python gemini_chatbot.py
```

### Run the advanced chatbot
```bash
python gemini_chatbot_advanced.py
```

Then open your browser and navigate to:
```
http://localhost:7860
```

## ⚙️ Configuration

| Parameter | File | Description |
|-----------|------|-------------|
| `model` | both | Change `gemini-pro` to another available Gemini model |
| `server_port` | both | Default `7860` — change to avoid port conflicts |
| `share` | both | Set `True` in `demo.launch()` to generate a public Gradio URL |
| `temperature` | advanced | Controls creativity: `0.0` (focused) → `1.0` (creative) |
| `max_output_tokens` | advanced | Maximum number of tokens in a single response |

## 💡 Example Prompts

- *"Explain quantum computing in simple terms"*
- *"Write a Python function to calculate Fibonacci numbers"*
- *"What are the top 5 tourist attractions in Paris?"*
- *"Help me write a professional email declining a meeting"*
- *"Debug this code and explain what's wrong: ..."*

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| `API key not found` | Set the `GEMINI_API_KEY` environment variable or update it directly in the code |
| `Module not found` | Run `pip install -r requirements.txt` |
| `Port already in use` | Change `server_port` in `demo.launch()` to an unused port |
| Slow or no response | Check your internet connection and Gemini API rate limits |

## 📁 Project Structure

```
Gemini-ChatBot-Using-Gradio/
├── gemini_chatbot.py           # Basic chatbot
├── gemini_chatbot_advanced.py  # Advanced chatbot with extra controls
├── requirements.txt            # Python dependencies
└── README.md
```

## 📋 Requirements

```
gradio>=4.0.0
google-generativeai>=0.3.0
pandas
```

## 🔑 Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **Create API Key**
4. Copy the key and use it as described in the [Installation](#-installation) section

## 📚 Resources

- [Gradio Documentation](https://www.gradio.app/docs)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Google AI Studio](https://aistudio.google.com/)

## 📄 License

This project is open source and available for personal and educational use.
