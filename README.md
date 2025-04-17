
## 🤖 BlenderBot Chat API

### Quick Overview
This repository provides a FastAPI-based backend that serves as a chatbot API using Facebook's BlenderBot 400M model. It's designed to work seamlessly with the Chat Page UI in your blog application.

### ⚙️ Features
- 🚀 Built with FastAPI for high-performance API handling

- 🌍 CORS middleware configured to allow requests from your blog domain

- 🧠 Integrates BlenderBot (facebook/blenderbot-400m-distill) for conversational AI


### 📦 Dependencies
- fastapi

- pydantic

- transformers

- uvicorn

### Version
Python 3.10

##### Install with:
```pip install -r requirements.txt```

### 🚀 Run the Server
```uvicorn main:app --host 0.0.0.0 --port 8000```

### 🔗 Related Repositories
[Frontend Chat UI (React): Chat Page Repo](https://github.com/elodrigo/chatPage)

