# Write the program to display first 10 Even numbers on screen

def main():
    cnt=0
    i=1

    while cnt < 10:
            if i % 2==0:
                cnt +=1
                print (i,end=" ")
            i +=1    

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_16>python Assignment16_9.py
# 2 4 6 8 10 12 14 16 18 20
    