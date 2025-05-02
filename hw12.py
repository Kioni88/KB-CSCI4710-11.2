import numpy as np
import re 
from collections import defaultdict
import random as rm
def build_transition_matrix(corpus):
    words = re.findall(r'\b\w+\b', corpus.lower()) # Tokenize words 

    transtions = defaultdict(lambda: defaultdict(int))

    # Count word transitions 
    for i in range(len(words) - 1):
        transtions[words[i]][words[i+1]] += 1

    # Normalize to probabilities
    transition_matrix = {
        word: {next_word: count / sum(next_words.values())
            for next_word, count in next_words.items()}
            for word, next_words in transtions.items()
    }

    return transition_matrix

def markov_chain_simulator(start_word, num_words, transition_matrix):
    current_word = start_word 
    sequence = [current_word]

    for _ in range (num_words):
        if current_word not in transition_matrix:
            break # Stop if not further transisition exist 
        next_words = list(transition_matrix[current_word].keys())
        probabilities = list(transition_matrix[current_word].values())
        current_word = np.random.choice(next_words, p=probabilities)
        sequence.append(current_word)

    return " ".join(sequence)


if __name__ == "__main__":
    # Sample corpus
    corpus = """The Cherry Coke was gas. The song Lost by Frank Ocean is good.
                My sister likes Frank Ocean. Frank Ocean has 2 albums. Frank Ocean's best album is blond."""

    # Build transition matrix 
    transition_matrix = build_transition_matrix(corpus)

    # Generate text starting from "The"
    generated_text = markov_chain_simulator ("the", 4, transition_matrix)

    print("Generate Text:", generated_text)