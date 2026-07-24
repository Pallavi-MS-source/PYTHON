# KEYWORD ARGUMENT
def score(kan,eng,hin,math,sci,ss=30):
    print(f"kan = {kan}")
    print(f"eng = {eng}")
    print(f"hin = {hin}")
    print(f"math = {math}")
    print(f"sci = {sci}")
    print(f"ss = {ss}")
    total = kan + eng + hin + math + sci + ss
    print(total)
score(kan=12,eng=45,hin=34,math=44,sci=50)