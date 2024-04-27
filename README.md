# Movie Subtitle Search Engine

## Introduction
This project is a movie subtitle search engine that allows users to search for movie subtitles and retrieve relevant content based on their queries. It uses Google Colab for data preprocessing, including reading the database file, decoding movie subtitle contents using Latin-1 encoding, and cleaning the data. The cleaned data is then used to generate embeddings using BERT, and these embeddings are stored in a Chroma database.

The search engine is integrated with a Flask web application in Visual Studio Code, enabling users to interact with the system and retrieve related content.

## Features
- Search for movie subtitles based on user queries.
- Retrieve relevant movie subtitle content.
- Integration with Flask for a user-friendly interface.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Azay961/Search-Engine-using-chromaDb.git
    cd Search-Engine-using-chromaDb
    ```

2. Set up the environment:
    - Ensure you have Python installed.
    - Install the required dependencies:
        ```bash
        pip install -r requirements.txt
        ```

3. Data preprocessing:
    - Use [Google colab link](https://colab.research.google.com/drive/1NVhfQ9GGQt_lEAkiX21Zg6Uh9Pi52rBW?usp=drive_link) notebook to preprocess the movie subtitle data and generate embeddings using BERT.

4. Set up the Flask app:
    - Open the project in Visual Studio Code.
    - Ensure the Chroma database is connected and integrated with the Flask app.
    - Run the Flask app:
        ```bash
        python app.py
        ```

## Usage
1. Access the Flask app through your web browser.
2. Enter your queries related to movie subtitles.
3. The search engine will provide relevant movie subtitle content based on your queries.

## Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/new-feature
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/new-feature
    ```
5. Submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any inquiries or feedback, please contact [Ajay Chaudhary](ajay023.chaudhary@gmail.com).
[Demo on Youtube](https://youtu.be/fJiP92DAuDI)
