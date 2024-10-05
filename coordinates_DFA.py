final_states = {35, 49, 50, 51, 52, 53, 55, 56}

transitions = {
    56: {'0-9': 56},
    54: {'0-9': 56},
    53: {'.': 54},
    52: {'.': 54, '0': 55},
    51: {'.': 54},
    50: {'0-7': 49, '8': 52, '9': 53,'.': 54},
    49: {'0-9': 51, '.': 54},
    48: {'0': 49, '2-9': 49, '1': 50},
    47: {' ': 47, '+': 48, '-': 48, '0': 49, '2-9': 49, '1': 50},
    46: {',': 47},
    45: {'0-9': 45, ',': 47},
    44: {'0-9': 45},
    43: {'.': 44, ',': 47},
    42: {'.': 44, '0': 46, ',': 47},
    41: {'0-9': 43, '.': 44, ',': 47},
    40: {'0-8': 41, '9': 42},
    39: {"'": 34, '0-9': 39},
    38: {'0-9': 39},
    37: {'"': 34, '0-9': 37},
    36: {'0-9': 37},
    35: {' ': 35},
    34: {' ': 34, 'E': 35, 'e': 35, 'O': 35, 'o': 35},
    33: {'"': 34, '.': 36},
    32: {'"': 34, '.': 36},
    31: {'0-9': 33, '"': 34, '.': 36},
    30: {' ': 30, '0-5': 31, '6-9': 32, 'E': 35, 'e': 35, 'O': 35, 'o': 35},
    29: {"'": 30, '.': 38},
    28: {"'": 30, '.': 38},
    27: {'0-9': 29, "'": 30, '.': 38},
    26: {' ': 26, '0-5': 27, '6-9': 28, 'E': 35, 'e': 35, 'O': 35, 'o': 35},
    25: {'°': 34},
    24: {'°': 26},
    23: {'0': 25, '°': 26},
    22: {'°': 26},
    21: {'0-7': 20, '8': 23, '9': 24, '°': 26},
    20: {'0-9': 22, '°': 26},
    19: {' ': 19, '0': 20, '2-9': 20, '1': 21},
    18: {"'": 13, '0-9': 18},
    17: {'0-9': 18},
    16: {'"': 13, '0-9': 16},
    15: {'0-9': 16},
    14: {',': 19, ' ': 19},
    13: {' ': 13, 'N': 14, 'n': 14, 'S': 14, 's': 14},
    12: {'"': 13, '.': 15},
    11: {'"': 13, '.': 15},
    10: {'0-9': 12, '"': 13, '.': 15},
    9: {' ': 9, '0-5': 10, '6-9': 11, 'N': 14, 'n': 14, 'S': 14, 's': 14},
    8: {"'": 9, '.': 17},
    7: {"'": 9, '.': 17},
    6: {'0-9': 8, "'": 9, '.': 17},
    5: {' ': 5, '0-5': 6, '6-9': 7, 'N': 14, 'n': 14, 'S': 14, 's': 14},
    4: {'°': 13, ',': 47},
    3: {'°': 5, '.': 44, ',': 47},
    2: {'0': 4, '°': 5, '.': 44, ',': 47},
    1: {'0-9': 3, '°': 5, '.': 44, ',': 47},
    0: {'0-8': 1, '9': 2, '+': 40, '-': 40}
}

def is_in_range(char, symbol):
    if symbol == '0-9':
        return '0' <= char <= '9'
    elif symbol == '0-8':
        return '0' <= char <= '8'
    elif symbol == '0-7':
        return '0' <= char <= '7'
    elif symbol == '0-5':
        return '0' <= char <= '5'
    elif symbol == '6-9':
        return '6' <= char <= '9'
    elif symbol == '2-9':
        return '2' <= char <= '9'
    return char == symbol

def extract_coordinates_from_text(text):
    lines = text.split('\n')
    valid_coordinates = []
    for line_index, line in enumerate(lines):
        length = len(line)
        start_index = 0
        while start_index < length:
            current_state = 0
            coord_candidate = ""
            found_coordinate = False
            i = start_index

            while i < length:
                char = line[i]
                found_transition = False
                for symbol, next_state in transitions.get(current_state, {}).items():
                    if is_in_range(char, symbol):
                        current_state = next_state
                        coord_candidate += char
                        found_transition = True
                        break
                
                if not found_transition:
                    break
                if current_state in final_states:
                    found_coordinate = True
                i += 1
            
            if found_coordinate:
                valid_coordinates.append((coord_candidate.strip(), line_index + 1, i + 1))
                start_index = i + 1
            else:
                start_index += 1

    return valid_coordinates