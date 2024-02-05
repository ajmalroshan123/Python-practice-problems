while(True):
    print("press q for quite : ")
    a = (input("Enter a no: "))
    if (a == 'q'):
        break
    try:
        print("Tring...!!!")
        a = int(a)
        if (a>6):
            print("Yow entered a number greater than 6")
    except Exception as e:
        print(e)        

