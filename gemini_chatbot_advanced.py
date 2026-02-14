"""
Advanced Gemini Chatbot using Gradio
Features: Chat history, temperature control, system prompts, and more
"""

import gradio as gr
import google.generativeai as genai
import os

# Configure the Gemini API
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=API_KEY)

def chat_with_gemini(message, history, system_prompt, temperature, max_tokens):
    """
    Advanced chat function with customizable parameters
    
    Args:
        message: Current user message
        history: List of previous messages
        system_prompt: System instruction for the model
        temperature: Creativity level (0.0 to 1.0)
        max_tokens: Maximum response length
    
    Returns:
        Response from Gemini model                                   
    """
    try:
        # Configure generation parameters
        generation_config = genai.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )
        
        # Initialize model with system instruction if provided
        if system_prompt.strip():
            model = genai.GenerativeModel(
                'gemini-pro',
                generation_config=generation_config,
                system_instruction=system_prompt
            )
        else:
            model = genai.GenerativeModel(
                'gemini-pro',
                generation_config=generation_config
            )
        
        # Create chat with history
        chat = model.start_chat(history=[])
        
        # Add conversation history
        for human, assistant in history:
            chat.send_message(human)
        
        # Send current message
        response = chat.send_message(message)
        
        return response.text
    
    except Exception as e:
        return f"❌ Error: {str(e)}\n\nPlease check your API key and internet connection."

# Create the Gradio interface
with gr.Blocks(title="Advanced Gemini Chatbot", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🚀 Advanced Gemini Chatbot
        ### Powered by Google's Gemini Pro AI Model
        """
    )
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                height=600,
                bubble_full_width=False,
                avatar_images=(None, "🤖"),
                show_copy_button=True
            )
            
            with gr.Row():
                msg = gr.Textbox(
                    placeholder="Type your message here... (Press Enter to send)",
                    show_label=False,
                    scale=5,
                    lines=2
                )
                submit = gr.Button("📤 Send", variant="primary", scale=1)
            
            with gr.Row():
                clear = gr.Button("🗑️ Clear Chat")
                retry = gr.Button("🔄 Retry Last")
        
        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ Settings")
            
            system_prompt = gr.Textbox(
                label="System Prompt (Optional)",
                placeholder="E.g., 'You are a helpful coding assistant'",
                lines=3,
                value=""
            )
            
            temperature = gr.Slider(
                minimum=0.0,
                maximum=1.0,
                value=0.7,
                step=0.1,
                label="Temperature (Creativity)",
                info="Higher = more creative, Lower = more focused"
            )
            
            max_tokens = gr.Slider(
                minimum=100,
                maximum=8000,
                value=2048,
                step=100,
                label="Max Response Length",
                info="Maximum number of tokens in response"
            )
            
            gr.Markdown(
                """
                ### 💡 Quick Tips
                - **Low temperature (0.1-0.3)**: For factual, consistent answers
                - **Medium temperature (0.4-0.7)**: Balanced responses
                - **High temperature (0.8-1.0)**: For creative, diverse outputs
                
                ### 🎯 Example Prompts
                - "Explain [topic] like I'm 5"
                - "Write a Python script to..."
                - "Summarize the key points of..."
                - "Help me debug this code..."
                """
            )
    
    # Event handlers
    def user_message(user_msg, history):
        """Add user message to chat"""
        return "", history + [[user_msg, None]]
    
    def bot_response(history, system_prompt, temperature, max_tokens):
        """Generate bot response"""
        user_msg = history[-1][0]
        bot_msg = chat_with_gemini(
            user_msg, 
            history[:-1], 
            system_prompt, 
            temperature, 
            max_tokens
        )
        history[-1][1] = bot_msg
        return history
    
    # Submit message
    msg.submit(user_message, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot_response, [chatbot, system_prompt, temperature, max_tokens], chatbot
    )
    submit.click(user_message, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot_response, [chatbot, system_prompt, temperature, max_tokens], chatbot
    )
    
    # Clear chat
    clear.click(lambda: None, None, chatbot, queue=False)
    
    # Retry last message
    def retry_last(history, system_prompt, temperature, max_tokens):
        if not history:
            return history
        history[-1][1] = None
        return bot_response(history, system_prompt, temperature, max_tokens)
    
    retry.click(
        retry_last, 
        [chatbot, system_prompt, temperature, max_tokens], 
        chatbot
    )

# Launch the app
if __name__ == "__main__":
    print("🚀 Starting Gemini Chatbot...")
    print("📍 Access the app at: http://localhost:7860")
    
    demo.launch(
        share=False,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True
    )
