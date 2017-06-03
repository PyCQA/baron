import re


def has_print_function(tokens):
    p = 0
    while p < len(tokens):
        if tokens[p][0] != 'FROM':
            p += 1
            continue
        if tokens[p + 1][0:2] != ('NAME', '__future__'):
            p += 1
            continue
        if tokens[p + 2][0] != 'IMPORT':
            p += 1
            continue

        current = p + 3
        # ignore LEFT_PARENTHESIS token
        if tokens[current][0] == 'LEFT_PARENTHESIS':
            current += 1

        while (current < len(tokens) and tokens[current][0] == 'NAME'):
            if tokens[current][1] == 'print_function':
                return True

            # ignore AS and NAME tokens if present
            # anyway, ignore COMMA token
            if current + 1 < len(tokens) and tokens[current + 1][0] == 'AS':
                current += 4
            else:
                current += 2
        p += 1

    return False


def replace_print_by_name(tokens):
    def is_print(token):
        return token[0] == 'PRINT'

    return [('NAME', 'print') if is_print(x) else x for x in tokens]
