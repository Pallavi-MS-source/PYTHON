def score(kan,eng,hin,math,sci,ss=30):
    print(f"kan = {kan}")
    print(f"eng = {eng}")
    print(f"hin = {hin}")
    print(f"math = {math}")
    print(f"sci = {sci}")
    print(f"ss = {ss}")
    total = kan + eng + hin + math + sci + ss
    print(total)
score(49,35,38,50,44)


def score(kan,eng,hin,math,sci=45,ss=30):
    print(f"kan = {kan}")
    print(f"eng = {eng}")
    print(f"hin = {hin}")
    print(f"math = {math}")
    print(f"sci = {sci}")
    print(f"ss = {ss}")
    total = kan + eng + hin + math + sci + ss
    print(total)
score(49,35,38,50)