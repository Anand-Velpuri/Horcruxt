# Horcruxt GenAI Chat Application

A beautiful Flask web application that allows users to chat with Harry Potter characters using AI. The application features a stunning interface with character selection, detailed character profiles, and an interactive chat system.

## Features

- 🏰 **Beautiful Harry Potter-themed UI** with Tailwind CSS
- 🧙‍♂️ **Character Selection** - Choose from 6 iconic characters
- 💬 **Interactive Chat Interface** - Real-time chat with characters
- ✨ **Animations & Effects** - Smooth transitions and magical animations
- 📱 **Responsive Design** - Works on desktop and mobile devices
- 🎨 **House-themed Styling** - Each character has their house colors

## Characters Available

- **Harry Potter** (Gryffindor) - The Boy Who Lived
- **Hermione Granger** (Gryffindor) - The brightest witch of her age
- **Ron Weasley** (Gryffindor) - Harry's loyal best friend
- **Albus Dumbledore** (Gryffindor) - The greatest headmaster
- **Severus Snape** (Slytherin) - The complex Potions Master
- **Lord Voldemort** (Slytherin) - The Dark Lord

## Installation & Setup

1. **Clone or download the project files**

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**

   ```bash
   python app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Project Structure

```
CHAT/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   ├── index.html        # Main character selection page
│   └── character.html    # Character detail and chat page
└── static/
    └── images/           # Character images (to be added)
```

## Technology Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, Tailwind CSS, Alpine.js
- **Styling:** Custom CSS animations and Hogwarts-themed design
- **Interactivity:** JavaScript with Alpine.js for reactive components

## Current Features

### Home Page (`/`)

- Displays all available characters in a beautiful grid
- Each character card shows:
  - Character name and house
  - Brief description
  - House-themed styling
  - Hover animations and effects

### Character Page (`/character/<character_id>`)

- Detailed character profile
- Interactive chat interface
- Quick action buttons for common questions
- Real-time message display
- Typing indicators

### Chat System

- RESTful API endpoint for chat functionality
- Character-specific responses
- Message history
- Responsive design

## Next Steps - GenAI Integration

The application is ready for GenAI integration. The chat endpoint in `app.py` is prepared to connect with:

- **OpenAI GPT models**
- **Google Gemini**
- **Anthropic Claude**
- **Local LLMs** (via API)

### Integration Points

1. **Modify the `/chat` route** in `app.py` to call your preferred AI service
2. **Add character-specific prompts** to maintain personality consistency
3. **Implement conversation memory** for context-aware responses
4. **Add error handling** for API rate limits and failures

### Example GenAI Integration

```python
# In app.py, replace the simple response with:
import openai

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    character_id = data.get('character_id', '')

    character = next((c for c in characters if c['id'] == character_id), None)

    if character:
        # Create character-specific prompt
        system_prompt = f"You are {character['name']} from Harry Potter. {character['personality']} Respond in character."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        ai_response = response.choices[0].message.content
    else:
        ai_response = "I'm sorry, I don't recognize that character."

    return jsonify({
        'response': ai_response,
        'character': character['name'] if character else 'Unknown'
    })
```

## Customization

### Adding New Characters

1. Add character data to the `characters` list in `app.py`
2. Include character images in `static/images/`
3. Update the character cards in `templates/index.html`

### Styling Changes

- Modify CSS in the `<style>` sections of HTML files
- Update Tailwind classes for different color schemes
- Add new animations in the CSS keyframes

### Adding Features

- **Voice Chat:** Integrate speech-to-text and text-to-speech
- **Image Generation:** Add character image generation with AI
- **Multiplayer:** Allow multiple users to chat simultaneously
- **Character Switching:** Enable switching characters mid-conversation

## Contributing

Feel free to enhance the application with:

- Additional characters
- New UI features
- Improved animations
- Better error handling
- Performance optimizations

## License

This project is for educational and entertainment purposes. Harry Potter characters and themes are property of J.K. Rowling and Warner Bros.

---

**Ready to experience the magic?** Run the application and start chatting with your favorite Harry Potter characters! 🧙‍♂️✨
