import json

def flaten(jayzon):
    to_return = []
    for key, value in jayzon.items():
        if isinstance(value, basestring):
            to_return.append('{"%s": "%s", ..}' % (key, value))
        if isinstance(value, list):
            to_return.append('{"%s": %s, ..}' % (key, value))
        if isinstance(value, dict):
            for result in flaten(value):
                to_return.append('{"%s": %s, ..}' % (key, result))
    return to_return

def dict_diff(first, second):
    first = flaten(first)
    second = flaten(second)
    diffs = []
    for item in first:
        if item not in second:
            diffs.append("bad: %s" % item)
    for item in second:
        if item not in first:
            diffs.append("expected: %s" % item)

    return diffs

def diff(left, right):
    to_return = json.dumps(left, indent=4, sort_keys=True).split("\n")
    to_return += [""]
    to_return += ["=="]
    to_return += [""]
    to_return += json.dumps(right, indent=4, sort_keys=True).split("\n")
    to_return += [""]
    to_return += [`left`, "==", `right`]
    to_return += [""]
    a = 0
    for first, second in zip(left, right):
        if first == second:
            continue
        to_return += map(lambda x: ("[%s] " % a) + x, dict_diff(first, second))
        a += 1
    return to_return

def pytest_assertrepr_compare(config, op, left, right):
    if isinstance(left, list) and isinstance(right, list) and op == "==":
        return diff(left, right)
