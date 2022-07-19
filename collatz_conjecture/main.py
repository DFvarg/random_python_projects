num = input("Starting number: ")
num = float(num)
step = 1
while True:
    if num == 1:
        break
    elif num % 2 == 0:
        num /= 2
    else:
        num = num*3 + 1
    print("step", step, ' : ', num)
    step += 1
