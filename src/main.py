from tkinter import Variable


d1='pee_pee'
health=9999
d2=350
st=200
special_move=500
print("name:" + str(d1))
print("health:" + str(health))
print("damage:" + str(d2))
print("stamina" + str(st))
enemyhp=[30,"💪",29,50,60,70,50]
print(enemyhp[1])



sum=0
for i in range(0,5):
    sum+=enemyhp[i]
    print(sum)