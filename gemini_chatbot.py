"""
Gemini Chatbot using Gradio
A simple chatbot interface powered by Google's Gemini AI model
"""

import gradio as gr
import google.generativeai as genai
import os

# Configure the Gemini API
# You need to set your API key as an environment variable or replace the string below
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

def chat_with_gemini(message, history):
    """
    Function to handle chat interactions with Gemini
    
    Args:
        message: Current user message
        history: List of previous messages in the conversation
    
    Returns:
        Response from Gemini model
    """
    try:
        # Create a chat session with history
        chat = model.start_chat(history=[])
        
        # Add conversation history to the chat
        for human, assistant in history:
            chat.send_message(human)
            # Note: The response is already stored, we just need to maintain context
        
        # Send the current message and get response
        response = chat.send_message(message)
        
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}\n\nPlease make sure you've set your GEMINI_API_KEY environment variable or updated the API_KEY in the code."

# Create the Gradio interface
with gr.Blocks(title="Gemini Chatbot", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🤖 Gemini Chatbot
        Chat with Google's Gemini AI model! Ask questions, get creative, or just have a conversation.
        """
    )
    
    chatbot = gr.Chatbot(
        height=500,
        bubble_full_width=False,
        avatar_images=(None, "🤖")
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here...",
            show_label=False,
            scale=4
        )
        submit = gr.Button("Send", variant="primary", scale=1)
    
    with gr.Row():
        clear = gr.Button("Clear Chat")
    
    gr.Markdown(
        """
        ### 💡 Tips:
        - Ask questions about any topic
        - Request creative writing or code
        - Get explanations and summaries
        - Explore ideas and brainstorm
        
        **Note:** Make sure to set your `GEMINI_API_KEY` environment variable before running!
        """
    )
    
    # Event handlers
    msg.submit(chat_with_gemini, [msg, chatbot], [chatbot])
    submit.click(chat_with_gemini, [msg, chatbot], [chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)
    
    # Clear the input box after submission
    msg.submit(lambda: "", None, msg)
    submit.click(lambda: "", None, msg)

# Launch the app
if __name__ == "__main__":
    demo.launch(
        share=False,  # Set to True if you want a public link
        server_name="0.0.0.0",
        server_port=7860
    )
