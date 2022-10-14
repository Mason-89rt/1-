import string
def klopp(s):
    return s
s = "./,.,.,In., a "
s = s.translate(str.maketrans('', '', string.punctuation))
print(s.split()[0])

