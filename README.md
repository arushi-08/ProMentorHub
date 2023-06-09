# ProMentorHub

Career mentorship is especially important for disadvantaged communities, as these individuals often face additional challenges in pursuing and achieving their professional aspirations.
Our web application helps individuals gain access to diverse range of experienced mentors by providing personalized guidance and support to help them achieve their professional aspirations



# Setup

Make sure you have python3 installed:

```
python3 --version
```

Create a virtual environment and install the dependencies:

### Linux/Mac:

```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

### Windows:

```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

# Configuration

Copy `env.sample` to `.env` and add your OpenAI API key to the file.

```
OPENAI_API_KEY=<<YOUR_API_KEY>>
```

Edit `main.py` and replace `<<PUT THE PROMPT HERE>>` with your prompt:

e.g. Create a simple AI cocktail assistant

```
INSTRUCTIONS = """You are an AI assistant that is an expert in Career Counselling, Job Mentorship and Skill Development.
You know about Career Growth, Self Improvement, Time Management.
You can provide advice on living a successful life, being productive, dealing with anxiety and stress.
If you are unable to provide an answer to a question, please respond with the phrase "I'm a ProMentor assistant, I can't help with that."
Please aim to be as helpful, creative, and friendly as possible in all of your responses.
Do not use any external URLs in your answers. Do not refer to any blogs in your answers.
Format any lists on individual lines with a dash and a space in front of each item.
"""
```

# Running

To run just do the following:

### Linux/Mac:

```
. ./venv/bin/activate
python main.py
```

### Windows:

```
venv\Scripts\activate.bat
python main.py
```

View the application on `http:\\127.0.0.1:8000`
