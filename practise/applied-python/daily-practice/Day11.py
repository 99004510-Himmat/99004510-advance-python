# regular expression

import re

test = r"shaktimaan"

if re.match(test, "shaktishaktishakti"):
    print("hain!")
else:
    print("nahi hain")
