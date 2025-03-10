# NovaMind - AI Chatbot

NovaMind is an AI-powered chatbot built with Flask and Google Gemini AI, providing intelligent conversations and useful resources.

## 🌟 Features
- Conversational AI powered by Google Gemini API
- Multiple chatbot pages
- Flask backend with REST API for chatbot responses
- Environment variable support for API keys
- Easy deployment on **Vercel**

## 🛠️ Setup and Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/novamind.git
cd novamind
```

### 2️⃣ Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```
GEMINI_API_KEY=your_google_gemini_api_key
```

### 5️⃣ Run the Application Locally
```sh
python app.py
```
Then, visit `http://127.0.0.1:5000/` in your browser.

## 🚀 Deploy on Vercel
### 1️⃣ Install Vercel CLI
```sh
npm install -g vercel
```

### 2️⃣ Login to Vercel
```sh
vercel login
```

### 3️⃣ Initialize Vercel in Your Project
```sh
vercel init
```
- Select the project directory
- Choose "Flask" as the framework
- Configure build settings (default settings work fine)

### 4️⃣ Set Environment Variables on Vercel
```sh
vercel env add GEMINI_API_KEY your_google_gemini_api_key
```

### 5️⃣ Deploy the App
```sh
vercel --prod
```
After deployment, Vercel will provide a live URL for your app.

## 📁 Project Structure
```
novamind/
│── templates/           # HTML files
│── static/              # CSS, JS, and images
│── app.py               # Main Flask app
│── requirements.txt     # Dependencies
│── .env                 # API key (not pushed to GitHub)
│── vercel.json          # Vercel configuration
│── README.md            # Project documentation
```

## 🤝 Contributing
Feel free to fork this repository, create a new branch, and submit a pull request.

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---
Made with ❤️ by Subhajit Das, Shopnojo Sanyal
