import time
timenow = 1
timenow2 = 0
while timenow2 != 60:
    print(str(timenow) + ":" + str(timenow2) + "am")
    timenow2 += 1 
    time.sleep(0.000000001)
    while timenow2 == 60:
     timenow2 = 0
     timenow += 1
     print(str(timenow) + ":" + str(timenow2) + "am")
     if timenow == 10  and timenow2 == 0:
        print("its time to wake up")
        time.sleep(20.0)
        quit()
        