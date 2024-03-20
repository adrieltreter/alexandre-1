print("programa de que mede glicose do sangue")
glicose=int(input("digite quantidade de glicose"))
if(glicose <100):
    print("normal")
elif( 100<glicose>=140):
    print("glucose alta")
elif(glicose >140 ):
    print("diabete")
