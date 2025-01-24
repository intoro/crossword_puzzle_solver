import re

def parse_input(file_path):
    """ 
    Parse the provided file and extract grid dimensions, grid data, and words to find
    """
    with open(file_path, 'r') as file:
        try:
            # First part: dimensions
            dimensions = file.readline().strip()
            
            # Regex to validate dimensions format (e.g., '5x5')
            match = re.match(r'^(\d+)x(\d+)$', dimensions)
            if not match:
                raise ValueError(f"Invalid grid dimensions format in file: {dimensions}")
            
            # Extract rows and cols from the regex match groups
            rows, cols = map(int, match.groups())
        
        except ValueError as e:
            raise ValueError(f"Error parsing grid dimensions: {e}")

        # Second part: the grid
        grid = [
            row if len(row := file.readline().strip().split()) == cols else
            ValueError(f"Invalid row length: expected {cols}, got {len(row)} in row {row}")
            for _ in range(rows)
        ]

        # Third part: words to find (store all words as a list to avoid file closure issues)
        words = [line.strip() for line in file if line.strip()]

    return rows, cols, grid, words
