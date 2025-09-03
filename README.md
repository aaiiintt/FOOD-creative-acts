# FOOD Creative Acts Generator

**Turn everyday moments into artistic adventures!**

Imagine having a personal creative coach that gives you challenges inspired by famous artists and philosophers. Click a button, get a unique creative task, and see the world differently.

---

## ✨ What Does This Do?

This app generates **creative provocations** - little artistic challenges that help you see the real world differently. Each one includes:

🎭 **A setup** (like "The city speaks in forgotten alphabets")  
🎯 **A task** (like "Walk backwards and photograph only shadows")

---

## 🚀 Building This Web App

I tried to create this so it was easy and fun to play with. If you can help me make it even more so, please join in.

**Perfect for beginners because:**
- 📁 **Simple structure** - just a few files to understand
- 🤖 **AI powered** - watch Google's Gemini create ideas for you
- 🎨 **Instant creativity** - see your code make something nice
- ⚡ **Quick setup** - up and running in minutes
- 🛠️ **Easy to customize** - change everything by editing simple text files

**What you'll learn:**
- How to build a real web app with Python Flask
- How to connect to AI services
- How to create clean, beautiful interfaces
- How to structure a professional project

---

## 🛠️ Tech Stack

- **🐍 Python Flask** - The easiest way to build web apps
- **🤖 Google Gemini AI** - The smart brain that creates ideas
- **🎨 HTML/CSS/JavaScript** - For the pretty interface
- **📦 JSON files** - Simple text files that store everything

*No databases, no complex setup, no headaches!*

---

## 🎯 Quick Start (5 Minutes to Magic!)

### Step 1: Get the Code
```bash
# Copy the project to your computer
git clone https://github.com/aaiiintt/FOOD-creative-acts.git
cd FOOD-creative-acts
```

### Step 2: Set Up Python (One Time Only)
```bash
# Create your own Python playground
python3 -m venv venv

# Activate it (like turning on a light switch)
source venv/bin/activate  # Mac/Linux
# OR on Windows:
venv\Scripts\activate
```

### Step 3: Install the Magic Ingredients
```bash
# Get all the tools you need
pip install -r requirements.txt
```

### Step 4: Get Your AI Key (Free!)
1. 🌐 Visit: https://makersuite.google.com/app/apikey
2. 🔑 Create a free Google account if needed
3. 📋 Copy your API key
4. 📝 Create a file called `.env` with:
```bash
GOOGLE_API_KEY="paste_your_key_here"
```

### Step 5: Launch Your App! 🚀
```bash
# Start your creative generator
gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi:app
```

**That's it!** Open http://localhost:5000 and start generating creative acts!

---

## 📂 Project Structure (Super Simple!)

```
Your Creative App/
├── 🐍 app.py                 # The main Python code (heart of your app)
├── 🚀 wsgi.py               # Makes your app super fast
├── 📁 templates/
│   └── 🎨 index.html        # Your beautiful web page
├── 🎭 thinkers.json         # Famous artists & philosophers  
├── 🌱 seeds.json            # Creative starting ideas
├── 🎯 prompt.json           # Instructions for the AI
├── 💾 provocations.json     # Your generated masterpieces
├── 📋 requirements.txt      # Python ingredients list
└── 🔐 .env                  # Your secret AI key
```

*Each file has one simple job - no confusion!*

---

## 🎪 How the Magic Works

1. **🎲 Random Selection** - App picks a creative legend 
2. **🌱 Inspiration Seed** - Grabs a concept like "forgotten sounds" 
3. **🤖 AI Collaboration** - Gemini combines them
4. **✨ Creative Output** - You get a unique challenge

**The best part?** You can customize everything by editing simple text files

---

## 🎨 Example Creative Acts

> **"Empty rooms hold the weight of departed conversations."**  
> **Task:** Sit in a café for exactly 7 minutes, writing down only the last word you hear each minute.

> **"The city speaks in forgotten alphabets."**  
> **Task:** Walk your usual route backwards, photographing only shadows cast by signs.

*Your app will generate hundreds of unique combinations like these!*

---

## 🎮 Make It Your Own (The Fun Part!)

### 🌱 Add Your Own Creative Seeds
Edit `seeds.json` to add ideas that inspire you:
```json
{
  "seeds": [
    "The rhythm of raindrops on windows",
    "Conversations between streetlights",
    "Your amazing idea here!"
  ]
}
```

### 🎭 Add Your Favorite Artists
Edit `thinkers.json` to include artists you love:
```json
{
  "thinkers": [
    {
      "name": "Your Favorite Artist",
      "spirit_instruction": "Creates art that challenges normal thinking..."
    }
  ]
}
```

### 🎯 Advanced: Customize the AI Brain
Edit `prompt.json` to change how the AI thinks:
- Make it more playful or serious
- Focus on different art styles
- Create themed generation modes

*Don't worry - you can't break anything! Just edit and experiment.*

---

## 🏆 What You'll Accomplish

By building this project, you'll:
- ✅ **Build a real web application** that people can actually use
- ✅ **Connect to AI services** like a professional developer
- ✅ **Create something beautiful** that generates endless creativity
- ✅ **Learn modern web development** with a simple, clean structure
- ✅ **Have a portfolio project** you can show off to anyone

---

## 🌟 Level Up Ideas (When You're Ready!)

- 🎨 **Theme Modes** - "Nature," "Urban," "Surreal" generation styles
- 📸 **Photo Gallery** - Save and display completed creative acts
- 🔗 **Social Sharing** - Let people share their favorite provocations
- 📱 **Mobile App** - Take creativity on the go
- 🎯 **Personal Collections** - Import/export custom seed sets

---

## 🤝 Join the Creative Community

Found a bug? Have an amazing idea? Want to add your favorite artist?

**Contributing is easy:**
1. 🍴 Fork the project
2. ✨ Make your improvements  
3. 📤 Submit a pull request
4. 🎉 Celebrate your contribution!

*Every contribution makes the app more creative for everyone!*

---

## 📜 License

MIT License - Build, modify, and share freely!

---

## 🎯 Ready to Go?

```bash
git clone https://github.com/aaiiintt/FOOD-creative-acts.git
cd FOOD-creative-acts
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Add your API key to .env
gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi:app
```