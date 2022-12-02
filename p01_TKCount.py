sss=["ㅋㅋㅋ","ㅁㅁㅁ","ㅂㅂㅂ","ㅎㅎㅎ","ㅋㅋㅋ","ㄹㄹㄹ"]
# for s in sss:
    # print(s.find("ㅋㅋ"))
    #찾는 문자열이 존재하는 경우 0을 리턴 else -1 리턴
    
jojo=0
ubi=0
for x in range(1,10):
    with open(f"C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/samgugji/0{x}.txt","r",encoding="UTF-8")as f:
        for a in f:
            if a.find("조조"):
                jojo+=1
            elif a.find("유비"):
                ubi+=1
                print(f"조조={jojo},유비={ubi}")
        
with open ("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/samgugji/11.txt","a",encoding="UTF-8")as f:
    f.write(f"조조{jojo},유비{ubi}")
#1=조조 5244 유비=12
#1=조조 5919 유비=30
#1=조조 5757 유비=46
#1=조조 7470 유비=78
#1=조조 6029 유비=30
#1=조조 7529 유비=55
#1=조조 5540 유비=38
#1=조조 5484 유비=28
#1=조조 808 유비=1
#52476 318
#52476 318