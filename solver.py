def find_word(grid, word, num_rows, num_cols):
    """
    Find a word in the grid and if found, return its start and end coordinates.
    """
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), 
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]

    def match_in_direction(start_row, start_col, delta_row, delta_col):
        for index, character in enumerate(word):
            current_row = start_row + index * delta_row
            current_col = start_col + index * delta_col
            if not (
                0 <= current_row < num_rows and 
                0 <= current_col < num_cols and 
                grid[current_row][current_col] == character
            ):
                return False
        return True

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == word[0]:  # Potential starting point
                for delta_row, delta_col in directions:
                    if match_in_direction(row, col, delta_row, delta_col):
                        end_row = row + (len(word) - 1) * delta_row
                        end_col = col + (len(word) - 1) * delta_col
                        return f"{word} {row}:{col} {end_row}:{end_col}"

    return None
