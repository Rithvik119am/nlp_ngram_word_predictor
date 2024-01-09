# N-gram Model Prediction

This project uses an N-gram model to predict the next word in a sentence. It's implemented in Python using the NLTK and Streamlit libraries.

## Features

- Upload a text file to train the N-gram model.
- Select the 'n' for the N-gram model.
- Enter a sentence for prediction.
- Predict the next set of words based on the input sentence.

## How to Run

1. Install the required Python libraries:

```sh
pip install nltk streamlit
```
2. Run the Streamlit app:
```sh
streamlit run app.py
```
## Functions

- `generate_ngrams(words, n)`: Generates n-grams from a list of words.
- `create_ngram_model(text, n)`: Creates an N-gram model from a given text.
- `predict_next_word(model, prefix)`: Predicts the next word based on the given model and prefix.
- `main()`: The main function that runs the Streamlit app.

## Files

- `app.py`: The main Python script that contains the N-gram model and the Streamlit app.
- Text files: Used for training the N-gram model.
