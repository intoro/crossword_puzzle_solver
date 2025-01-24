import sys
from alphabet_soup import parse_input, find_word

def main(file_path):
    """
    Main function to solve the word search.
    """
    # Parse the input file
    try:
        rows, cols, grid, words = parse_input(file_path)
    except Exception as e:
        print(f"Error parsing input file: {e}")
        sys.exit(1)

    # Search for each word removing enpty values if present
    results = list(filter(None, (find_word(grid, word, rows, cols) for word in words)))


    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    # Provide the file path as a command-line argument
    if len(sys.argv) != 2: 
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)