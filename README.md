# AI-story-write

It is an interactive storytelling application that helps users create engaging stories based on their input. The app uses the OpenAI API and Langchain to generate story responses and build upon the user's prompts.

## Features

- **Interactive storytelling:** Users can provide input to guide the story's direction and see the story unfold in real-time.
- **Engaging story elements:** The AI assistant generates interesting paragraph headings, plot twists, and even image descriptions to enhance the story.
- **User-friendly interface:** The app features a clean and intuitive sidebar for user input and a main area to display the story.

### Understand this code using: https://getarchieai.com/snippet/Ec5NYU

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/story-bot.git
   ```

Navigate to the project directory:

```
cd story-bot
```

Create a virtual environment:
```
python -m venv venv
```

Activate the virtual environment:
For Windows:
```
venv\Scripts\activate
```
For macOS and Linux:

```
source venv/bin/activate
```

Install the required dependencies:
```
pip install -r requirements.txt
```

Set up your OpenAI API key:
- Create a .env file in the project root directory.
- Add the following line to the .env file, replacing YOUR_API_KEY with your actual OpenAI API key:
```
OPENAI_API_KEY=YOUR_API_KEY
```

Run the application:
```
streamlit run story.py
```

This will start the Streamlit server and open the application in your default web browser.

## Usage
- Once the application is running, you will see a sidebar on the left with the title "Story Bot" and a welcome message.
- In the "Your Input" section, type your message or prompt to guide the story's direction.
- Press Enter or click outside the input box to submit your message.
- The AI assistant will generate a response based on your input and the conversation history. The response will be displayed in the main area of the app.
- Continue providing input to further develop the story and see how it unfolds.

## Dependencies
- The application relies on the following main dependencies:
- Streamlit: A framework for building interactive web applications.
- OpenAI API: Used to generate story responses using the GPT-3.5 language model.
- Langchain: A library for building applications with language models.
- For a complete list of dependencies, please refer to the requirements.txt file.

## Contributing
Contributions to Story Bot are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

This project is licensed under the MIT License.
