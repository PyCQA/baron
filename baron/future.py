import re


def has_print_function(tokens):
    for pos in range(len(tokens)):
        if tokens_defines_print_function(tokens[pos:]):
            return True
    return False


def tokens_defines_print_function(tokens):
    token = iter(tokens)
    try:
        if next(token)[0] != 'FROM' \
                or next(token)[0:2] != ('NAME', '__future__') \
                or next(token)[0] != 'IMPORT':
            return False
        
        current_token = next(token)
        if current_token[0] == 'LEFT_PARENTHESIS':
            current_token = next(token)

        while (current_token[0] == 'NAME'):
            if current_token[1] == 'print_function':
                return True
            if next(token)[0] == 'AS':
                next(token)
                next(token)
            current_token = next(token)
    except StopIteration:
        pass
    return False


def replace_print_by_name(tokens):
    def is_print(token):
        return token[0] == 'PRINT'

    return [('NAME', 'print') if is_print(x) else x for x in tokens]
    
