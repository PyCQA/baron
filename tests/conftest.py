import os
import json


def pytest_assertrepr_compare(config, op, left, right):
    if isinstance(left, list) and isinstance(right, list) and op == "==":
        with open("/tmp/a", "w") as a:
            a.write(json.dumps(left, indent=4, sort_keys=True))
        with open("/tmp/b", "w") as b:
            b.write(json.dumps(right, indent=4, sort_keys=True))

        os.system("diff -y /tmp/a /tmp/b")
