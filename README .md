# Gemini Chatbot with Gradio  

A simple and elegant chatbot interface powered by Google's Gemini AI model using Gradio.

## Features

- 💬 Interactive chat interface
- 🤖 Powered by Google's Gemini Pro model
- 🎨 Clean and modern UI with Gradio
- 📝 Conversation history support
- 🔄 Easy to clear and restart conversations

## Prerequisites

- Python 3.8 or higher
- A Google Gemini API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. **Install the required packages:**

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install gradio google-generativeai
```

2. **Set up your Gemini API key:**

You can do this in one of two ways:

**Option A: Environment Variable (Recommended)**
```bash
# On Linux/Mac
export GEMINI_API_KEY="your-api-key-here"

# On Windows (Command Prompt)
set GEMINI_API_KEY=your-api-key-here

# On Windows (PowerShell)
$env:GEMINI_API_KEY="your-api-key-here"
```

**Option B: Edit the Python file**
Open `gemini_chatbot.py` and replace:
```python
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
```
with:
```python
API_KEY = "your-actual-api-key-here"
```

## Usage

1. **Run the chatbot:**

```bash
python gemini_chatbot.py
```

2. **Access the interface:**

Open your browser and go to:
```
http://localhost:7860
```

3. **Start chatting!**

Type your message in the text box and click "Send" or press Enter.

## Configuration

You can customize the chatbot by modifying these parameters in `gemini_chatbot.py`:

- **Model**: Change `gemini-pro` to other available Gemini models
- **Port**: Modify `server_port=7860` to use a different port
- **Public sharing**: Set `share=True` in `demo.launch()` to get a public URL

## Example Questions to Try

- "Explain quantum computing in simple terms"
- "Write a Python function to calculate fibonacci numbers"
- "What are the top 5 tourist attractions in Paris?"
- "Help me write a professional email"
- "Create a story about a robot learning to paint"

## Troubleshooting

**Error: API key not found**
- Make sure you've set the `GEMINI_API_KEY` environment variable or updated it in the code

**Error: Module not found**
- Run `pip install -r requirements.txt` to install dependencies

**Port already in use**
- Change the `server_port` parameter to a different port number

## Getting a Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key and use it in the application

## License

This project is open source and available for personal and educational use.

## Notes

- The free tier of Gemini API has rate limits
- Keep your API key secure and never share it publicly
- For production use, consider implementing proper API key management

## Support

For issues with:
- Gradio: Visit [Gradio Documentation](https://www.gradio.app/docs)
- Gemini API: Visit [Google AI Documentation](https://ai.google.dev/docs)
