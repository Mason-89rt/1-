import string
def klopp(stroka):
    stroka=stroka.translate(str.maketrans('', '', string.punctuation))
    stroka=stroka.split()[0]
    return stroka

