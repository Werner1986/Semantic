# Semantic Similarity Task

This repository contains code for the Semantic Similarity Task. It utilizes spaCy, a Natural Language Processing (NLP) library, to detect similarity within texts. The code demonstrates how to compare words, sentences, and short passages using spaCy's similarity functionality.

## Prerequisites

- Python 3.9 or later
- pip package manager

## Installation

1. Clone this repository to your local machine:

   git clone <repository-url>

2. Navigate to the project folder:

    cd semantic-similarity-task

3. Install the required dependencies using the following command:

    pip install -r requirements.txt

## Usage

To run the code, execute the following command:

    (copy code)
    python semantic.py

This will run the script and display the output demonstrating semantic similarity comparisons using spaCy.

Modify the code in semantic.py to experiment with different word or sentence comparisons and observe the similarity scores.

Additionally, you can run the watch_next.py script to find the most similar movie description based on a given input. Modify the function call in the script to pass your desired description.

## Docker Support

If you have Docker installed, you can also containerize the application using the provided Dockerfile. Follow these steps:

Build the Docker image:

docker build -t semantic-similarity .
Run a container from the image:

docker run --name semantic-container semantic-similarity
This will execute the script inside a Docker container.

Note: Replace <repository-url> with the actual URL of your Git repository.

Feel free to explore the code and experiment with different text inputs to observe the semantic similarity results.

Make sure to replace `<repository-url>` with the actual URL of your Git repository.

These instructions will guide users on how to clone the repository, install the required dependencies, and run the code either directly or using Docker. They also provide details on how to modify the code and experiment with different inputs.
