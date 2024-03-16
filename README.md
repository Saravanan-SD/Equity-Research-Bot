# News Research Tool using 🦜️🔗 LangChain

## Introduction
This is a News Research Tool built using Streamlit and Langchain, a library for natural language processing tasks. The tool allows users to input URLs of news articles, ask questions related to the content of these articles, and receive answers along with relevant sources.


![Working](https://github.com/Saravanan-SD/Equity-Research-Bot/blob/main/Screenshot%20of%20app.png)

## Features
- Input URLs of news articles via the sidebar.
- Process upto three URLs simultaneously.
- Utilize the GPT-3.5 model for question answering.
- Extract information from news articles and generate answers.
- Display relevant sources for the answers provided.

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/Saravanan-SD/Equity-Research-Bot.git
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Set up your OpenAI key in the .env file
    ```
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage
1. Run the application:
    ```
    streamlit run main.py
    ```
2. Input URLs of news articles in the sidebar.
3. Click on the "Process URL" button to extract information.
4. Enter your question in the text box provided.
5. The embeddings will be stored and indexed using FAISS, enhancing retrieval speed and the FAISS index will be saved in a local file path in pickle format for future use.
6. The tool will generate an answer based on the provided question.
7. Relevant sources for the answer will be displayed.
8. Following news articles were used in the example
   - https://www.reuters.com/world/india/us-probing-adani-group-founder-over-potential-bribery-bloomberg-reports-2024-03-15/
   - https://www.livemint.com/companies/news/us-probing-adani-group-over-potential-bribery-company-denies-foul-11710550688601.html
   - https://www.indiatoday.in/business/story/us-investigating-bribery-allegations-against-adani-group-gautam-adani-2515679-2024-03-16

## Contact
For any inquiries or support, please feel free to contact us:

- Email: [saravanansd634@gmail.com](mailto:saravanansd634@gmail.com)
- LinkedIn: [Saravanan S](https://www.linkedin.com/in/sdsaravanan/)
