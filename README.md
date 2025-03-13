# 🚀 CodeBuddy - AI-Powered Code Generator Bot

CodeBuddy is a **Telegram bot** that helps you generate code for various tasks. Whether you're working on Python scripts, chatbot creation, or tax calculations, CodeBuddy assists with **dynamic code generation** based on user input.

---

## ✨ Features
- 🤖 **AI-Powered Code Generation** - Get instant Python code for different tasks.
- 🔘 **Interactive Telegram Bot** - Easy-to-use button-based menu.
- 📝 **Supports Various Code Requests** - Chatbot creation, tax calculation, and more.
- 💡 **Built with DeepSeek AI** - Provides intelligent responses and clean code.

---

## 🛠️ How It Works
1. **Start the Bot** - Send `/start` to begin.
2. **Select "Generate Code"** - Tap the button to request a code snippet.
3. **Ask for a Code Example** - Send a prompt like:
   ```
   python code for creation of chatbot
   ```
4. **Receive the Generated Code** - The bot will provide a relevant Python script.

---

## 📸 Example Conversation
```
👤 You: /start
🤖 Bot: Welcome to AI Learning Companion! Choose an option:
   [Generate Code]
👤 You: python code for creation of chatbot
🤖 Bot:

```python
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.get_response(user_input)
    print(f"MyBot: {response}")
```  
```

---

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/codebuddy-bot.git
cd codebuddy-bot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and add your Telegram bot token and API key:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
DEEPSEEK_API_KEY=your_deepseek_api_key
```

### 4️⃣ Run the Bot
```bash
python bot.py
```

---

## 💡 Future Improvements
- Support for **multiple programming languages**.
- **More interactive AI responses** with debugging support.
- **Integration with cloud execution** to run generated code instantly.

---

## 📜 License
This project is open-source under the **MIT License**.

---

🔗 **Follow & Star** ⭐ the repo if you find this helpful!

