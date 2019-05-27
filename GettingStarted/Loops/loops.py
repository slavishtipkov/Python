names = ["Bravo", "Chudo", "Kifla", "Kovra", "Wow", "Blow", "Crow", "Moshbol"]

for name in names:
    print("Name is {0}".format(name))


x = 0
for index in range(3, 20):
    x += 10

    if x % 3 == 0:
        print("Devidible by 3.. Next please")
        continue

    if x > 49:
        print(f"Current value is {x}")

    if x > 100:
        print("X bigger than 100.. Stopping")
        break


x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1


def test():
    print("tested")

test()


def generate_fibbonaci_next_number(fibArray, current_index):
    currentNumber = fibArray[current_index]
    prevNumber = fibArray[current_index - 1]
    print("Next fibo num is {0}".format(currentNumber + prevNumber))

generate_fibbonaci_next_number([1,1,2,3,5], 4)