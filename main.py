from utils import *

def main():
    """
    The main function. Performing all functions.
    """
    text_file = "text.txt"

    func_graph()
    hist_freq_char(text_file)
    hist_freq_sentence(text_file)

if __name__ == '__main__':
    main()