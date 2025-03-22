
# 📑GRAMMAR-CHECKER

A Python-based NLP tool that detects and corrects grammatical errors in text. It uses Machine Learning & Natural Language Processing (NLP) to enhance text accuracy.


###
## Table of Contents
⚫Features

⚫Installation

⚫Usage

⚫Project Architecture

⚫File Structure

⚫Technologies Used

⚫
How It Works

⚫Contributing
###
How It Works

⚫Contributing
###
## ✨Features

- ✅Grammar Error Detection -Identifies spelling  and grammatical mistakes
- ✅Correction Suggestions - Provides suggested alternatives.
- ✅Machine Learning Model - Uses NLP-based models for accuracy.
- ✅Web Interface - Flask-based web app for checking grammar.
- ✅Batch-Processing - Supports checking mulitple sentences at once.
- ✅Pre-trained Model Support - Uses pre-trained NLP models for correction.

###
## Installation

### 1.Clone the repository

```bash
git clone https://github.com/swetasachan777/grammar-checker.git
cd grammar-checker

```
### 2. Create a Virtual Environment

```bash
python -m venv env

```
Activate it:

Windows: ``` env\Scripts\activate```

Linux/macOS: ```source env/bin/activate```

### 3. Install Dependencies

```Bash
pip install -r requirements.txt
```

###
## 🔧Usage

### Run the Grammar Checker
To check grammar from the command line:
```Bash
python grammar_checker.py
```
Enter the text when prompted and receive correction suggestions.

### Launch the Web Interface
To use the web-based Interface:
```Bash
python app.py
```

###
## 📁Project Architecture

The Project follows a modular design:
```
grammar-checker/
│── app.py              # Flask web application
│── grammar_checker.py  # Command-line grammar checker
│── train_model.py      # Machine Learning model training
│── data_preprocessing.py  # Prepares data for training
│── requirements.txt    # Dependencies
│── frontend/           # Web UI (HTML, CSS, JavaScript)
│── models/             # Trained NLP models
│── datasets/           # Grammar correction dataset
└── README.md           # Project documentation

```

###
## 📂File Structure

| File/Folder           | Description                                  |
|----------------------|----------------------------------------------|
| app.py              | Flask web app for user interaction          |
| grammar_checker.py  | Command-line tool for grammar checking      |
| train_model.py      | Trains the NLP-based grammar correction model |
| data_preprocessing.py | Prepares text data for training             |
| frontend/           | Contains HTML, CSS, JavaScript for UI        |
| models/            | Stores trained machine learning models       |
| datasets/          | Contains sample text datasets                |
| requirements.txt   | List of required dependencies                |

###
## 🛠️Technologies Used
▪ Python 3.x

▪ Flask - Web Framework

▪ NLTK - Natural Language Toolkit for text processing. 

▪ Scikit-learn - Macine learning library

▪ pandas - Data manipulation and preprocessing

###


## ⚙️How It Works

***1. Text Input:*** The user enters text either in the command-line tool or in the web application.

***2. Text Preprocessing:*** The text is cleaned using NLTK (tokenization, stopwords removal, lemmatization, etc.).

***3. Grammar Error Detection:*** The model identifies errors using rule-based and ML-based approaches.

***4. Correction Suggestions:*** The system suggests possible corrections based on an NLP model.

***5. Output Display:*** The corrected text is displayed in the console or on the web interface.
