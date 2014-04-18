import re


def has_print_function(tokens):
    searching_sequence = ['FROM', 'NAME', 'IMPORT', 'NAME']
    for sequence in get_sequence_occurences(tokens, searching_sequence):
        if sequence[1][1] == 'future' and sequence[3][1] == 'print_function':
            return True
    return False


def get_sequence_occurences(tokens, sequence):
    if len(sequence) == 0:
        return

    for pos in range(len(tokens)):
        current_tokens = tokens[pos:pos+len(sequence)]
        if sequences_match(current_tokens, sequence):
            yield current_tokens


def sequences_match(tokens, type_sequence):
    for pos in range(len(type_sequence)):
        if tokens[pos][0] != type_sequence[pos]:
            return False
        pos += 1

    return True


def replace_print_by_name(tokens):
    def is_print(token):
        return token[0] == 'PRINT'

    return [('NAME', 'print') if is_print(x) else x for x in tokens]
    
