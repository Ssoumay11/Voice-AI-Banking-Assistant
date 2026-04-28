# Voice AI Banking Assistant

## Overview
Voice AI Banking Assistant is a Python-based application that simulates basic banking operations using voice interaction. The system allows users to interact through speech and perform tasks such as checking balance, transferring money, validating cheque images, and completing KYC.

## Features
- Voice interaction using Speech-to-Text and Text-to-Speech
- Balance inquiry using dummy data
- Money transfer with multi-step conversational workflow
- Cheque validation using image input (mock validation)
- KYC using audio and video recording
- Transaction logging using JSON files
- Text-based testing mode without voice

## Project Structure
voice-ai-banking-assistant/
│
├── app/
│   ├── main.py
│   ├── test_main.py
│   ├── voice/
│   ├── nlp/
│   ├── modules/
│   ├── workflows/
│   ├── utils/
│   └── data/
│
├── assets/
│   └── images/
│
├── requirements.txt
└── README.md

## Installation

1. Clone the repository
git clone https://github.com/your-username/voice-ai-banking-assistant.git
cd voice-ai-banking-assistant

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   (for Windows)

3. Install dependencies
pip install -r requirements.txt

## Run the Project (Voice Mode)
python -m app.main

## Run in Text Mode (Testing)
python -m app.test_main

## Technologies Used
Python  
SpeechRecognition  
pyttsx3  
OpenCV  
NumPy  
SoundDevice  
SciPy  

## Data Files
dummy_db.json stores user details and balance  
transactions.json stores transaction history  
kyc_records/ stores recorded audio and video  

## Limitations
Uses dummy data and does not connect to real banking systems  
Cheque validation is basic and does not use OCR or machine learning  
Speech recognition accuracy depends on environment and microphone quality  

## Future Improvements
Integrate LLM frameworks such as LangChain or LangGraph  
Replace JSON storage with a database such as SQLite or PostgreSQL  
Improve speech recognition using Whisper  
Build a user interface using Streamlit or a web framework  

## Summary
This project demonstrates a complete voice-based AI system with multi-step workflows, combining speech processing, simple computer vision, and backend simulation of banking operations.
