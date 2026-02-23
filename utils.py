import numpy as np
import matplotlib.pyplot as plt
import re
import pylab

def func_graph():
    """
    Plots a graph according to a function.
    """
    t = np.linspace(-2, 5, 300)
    y = t * np.sin(5 * t)

    plt.figure()
    plt.plot(t, y)
    plt.savefig('function_graph.png', dpi=200)

def hist_freq_char(text_file):
    """
    Opens a text file for reading.
    Counts the number of letters and saves them to a list.
    Plots a histogram of a number of letters.

    Parameters:
        text_file (string): filename of text file
    """
    with open(text_file, 'r') as fd:
        freq = {}
        clean_text = re.sub(r"[^a-zA-Za]", "", fd.read())
        clean_text = clean_text.lower()

        for c in clean_text:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

    keys = list(freq.keys())
    values = list(freq.values())

    plt.figure()
    pylab.bar(keys, values)
    pylab.savefig('frequency_char.png', dpi=200)
    pylab.show()

def hist_freq_sentence(text_file):
    """
    Opens a text file for reading.
    Counts the number of exclamatory, question, affirmative sentences, and sentences with 3 points: '...'
    Plots a histogram of a number of sentences.

    Parameters:
         text_file (string): filename of text file
    """
    with open(text_file, 'r') as fd:
        freq = {}
        clean_text = re.sub(r"[^a-zA-Za.!?]", "", fd.read())

        freq["."] = len(re.findall(r"\.", clean_text))
        freq["?"] = len(re.findall(r"\?", clean_text))
        freq["!"] = len(re.findall(r"!", clean_text))
        freq["..."] = len(re.findall(r"\.\.\.", clean_text))

    keys = list(freq.keys())
    values = list(freq.values())

    plt.figure()
    pylab.bar(keys, values)
    pylab.savefig('frequency_sentence.png', dpi=200)
    pylab.show()
