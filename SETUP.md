# Horcruxt GenAI Setup Guide

## 🚀 Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

You have several options to set your OpenAI API key:

#### Option A: Environment Variable (Recommended)

```bash
export OPENAI_API_KEY="your-actual-api-key-here"
```

#### Option B: Direct in config.py

Edit `config.py` and replace:

```python
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-api-key-here')
```

with:

```python
OPENAI_API_KEY = 'your-actual-api-key-here'
```

#### Option C: .env File (Create one)

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-actual-api-key-here
```

### 3. Run the Application

```bash
python app.py
```

### 4. Access the Application

Open your browser and go to: `http://localhost:5000`

## 🔧 Configuration Options

### AI Response Settings (config.py)

- `ENABLE_AI_RESPONSES`: Set to `False` to use fallback responses (no API calls)
- `FALLBACK_RESPONSES`: Set to `False` to disable fallback responses
- `MAX_TOKENS`: Maximum response length (default: 500)
- `TEMPERATURE`: Response creativity (0.0-1.0, default: 0.8)

### API Configuration

- `OPENAI_MODEL`: AI model to use
- `OPENAI_BASE_URL`: API endpoint

## 🎭 Character System Prompts

Each character has a detailed system prompt that includes:

- **Personality & Speech**: How they talk and behave
- **Knowledge & Expertise**: What they know about magic and the world
- **Relationships & Opinions**: Their feelings about other characters
- **Edge Cases & Limitations**: Their flaws and limitations
- **Response Style**: How they should respond to questions

## 🔍 Troubleshooting

### API Key Issues

- Make sure your API key is valid and has credits
- Check that the API key is properly set in the environment
- Verify the base URL is correct for your provider

### No AI Responses

- Check if `ENABLE_AI_RESPONSES` is set to `True` in config.py
- Verify your API key is working
- Check the console for error messages

### Fallback Mode

If AI responses fail, the app will use fallback responses. You can:

- Check the console for error messages
- Verify your internet connection
- Ensure your API provider is working

## 🎨 Customization

### Adding New Characters

1. Add character data to the `characters` list in `app.py`
2. Create a detailed system prompt for authentic responses
3. Add character image to `static/images/`
4. Update the character cards in templates

### Modifying Character Responses

Edit the `system_prompt` for each character in `app.py` to change:

- How they speak and behave
- What they know and don't know
- Their relationships and opinions
- Their limitations and flaws

### Changing AI Settings

Modify `config.py` to adjust:

- Response length and creativity
- API model and endpoint
- Error handling behavior

## 🔒 Security Notes

- Never commit your API key to version control
- Use environment variables for production deployments
- Consider rate limiting for production use
- Monitor API usage and costs

## 🎯 Ready to Chat!

Once configured, you can:

1. Choose any character from the home page
2. Start chatting with authentic Harry Potter character responses
3. Conversations are saved in your browser's localStorage
4. Each character responds in their unique voice and personality

Enjoy your magical conversations! 🧙‍♂️✨
