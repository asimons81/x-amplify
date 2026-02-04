# ⚡ X-Amplify

> Transform any idea into 10 viral X posts using The Stijn Method.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Gemini API Key (from Google AI Studio)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/x-amplify.git
cd x-amplify

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📋 The 10 Stijn Formats

| Format | Description |
|--------|-------------|
| ❌✅ Contrast | Visual System A vs System B layout |
| 📈 Milestone | Humble growth update |
| ⚖️ Symmetric | Two-column year comparison |
| 📋 List | 5-item numbered list with bold headers |
| 💥 Split Hook | 2-line suspense + punchline |
| 🔥 Raw & Real | Intentional minor grammar break |
| 🎭 Amateur vs Pro | Definition contrast |
| 🔺 Triad | 3-line rhythmic structure |
| ⚡ Extremes | Superlative hook + hard truth |
| 🎯 Callout | Popular vs contrarian opinion |

## ⚙️ Architecture

```
x-amplify/
├── app.py              # Streamlit UI
├── logic/
│   ├── engine.py       # Gemini API integration
│   ├── scraper.py      # URL content extraction
│   └── validator.py    # Output validation
└── config/
    └── prompts.py      # The "God Prompt" template
```

## 🔒 Style Guardrails

The app enforces strict style rules:
- ❌ No em dashes (—)
- ❌ No "delve", "game-changer", "In today's world"
- ✅ Aesthetic whitespace
- ✅ Sentence variance
- ✅ Human cadence

## 📄 License

MIT License
