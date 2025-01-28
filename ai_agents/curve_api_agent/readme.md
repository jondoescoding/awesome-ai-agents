# 🦙 Curve Protocol Chat Agent Guide

## 🌱 Quick Start

1. **Get Python Ready**You'll need Python 3.10+ (like a new video game console for your computer)
2. **Get Secret Code Key**Get an OpenAI API key from [their website](https://platform.openai.com/) (it's like a password for AI)
3. **Install Stuff**In your terminal:

   ```bash
   pip install -e .  # Installs all required parts
   ```
4. **Add Secret Key**Create a `.env` file in your project folder with:

   ```env
   OPENAI_API_KEY=your-key-here
   ```
5. **Start the App**
   Run this magic spell:

   ```bash
   streamlit run app.py
   ```

## 🎮 Using the Chat Agent

1. **Sidebar Setup**

   - 🔑 Paste your OpenAI key in the "API Configuration" box
   - 🤖 Choose your agent (like picking a character in a game)
2. **Ask Questions**Try these starters:

   - "Show me Ethereum's fees from last week"
   - "Compare Polygon and Avalanche user growth"
   - "What's the busiest pool right now?"


## 🚨 Troubleshooting

**App won't start?**

```bash
pip install --upgrade streamlit  # Refresh Streamlit
```

**API Key Not Working?**

- Double check you copied the whole key
- Make sure your `.env` file is in the right folder

## 🆘 Need Help?

Check the agent selection area (sidebar) for example questions, or reach out:

- 🐦 [Twitter](https://twitter.com/jondoescoding)
- 💻 [GitHub Repo](https://github.com/jondoescoding/awesome-ai-agents)
