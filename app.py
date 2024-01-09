from nltk.tokenize import word_tokenize
import streamlit as st
import random

def generate_ngrams(words, n):
    print(f"Generating {n}-grams")
    ngrams_list = []
    for j in range(2, n):
        for i in range(len(words) - j + 1):
            ngrams_list.append(tuple(words[i:i+j]))
    return ngrams_list

def create_ngram_model(text, n):
    print(f"Creating {n}-gram model")
    ngrams_freq = {}
    ngrams = generate_ngrams(text, n)
    for gram in ngrams:
        prefix = gram[:-1]
        suffix = gram[-1]
        if prefix not in ngrams_freq:
            ngrams_freq[prefix] = {}
        if suffix not in ngrams_freq[prefix]:
            ngrams_freq[prefix][suffix] = 0
        ngrams_freq[prefix][suffix] += 1
    for prefix in ngrams_freq:
        total_count = float(sum(ngrams_freq[prefix].values()))
        for suffix in ngrams_freq[prefix]:
            ngrams_freq[prefix][suffix] /= total_count
    return ngrams_freq

def predict_next_word(model, prefix):
    if prefix in model:
        choices = model[prefix]
        return random.choices(list(choices.keys()), weights=list(choices.values()))[0]
    else:
        return None

def main():
    st.title("N-gram Model Prediction")
    uploaded_file = st.file_uploader("Upload Text File", type=["txt"])
    if uploaded_file is not None:
        text =  uploaded_file.read().decode("utf-8").lower()
        tokens = word_tokenize(text)
        n = st.slider("Select the n-gram:", min_value=2, max_value=10, value=3)
        ngram_model = create_ngram_model(tokens, n)
        n_more=st.slider("Select the number of words to predict:", min_value=10, max_value=150, value=50)
        input_sentence = st.text_input("Enter a sentence for prediction:")
        if st.button("Predict"):
            input_sentence = input_sentence.lower()
            output = input_sentence
            input_tokens = word_tokenize(input_sentence)
            for i in range(n_more):
                prefix = tuple(input_tokens[-(n - 2):])
                predicted_word = predict_next_word(ngram_model, prefix)
                if predicted_word is None:
                    break
                input_tokens.append(predicted_word)
            predicted_sentence = ' '.join(input_tokens)
            st.write(f"Predicted sentence: {predicted_sentence}")

if __name__ == "__main__":
    main()