import threading
import time

def calculate_squares():
    print("Квадраты числе от 1 до 10:")
    for i in range(1, 11):
        square = i ** 2
        print(f"{i} в квадрате = {square}")
        time.sleep(0.1)

def calculate_cubes():
    print("Кубы чисел от 1 до 10:")
    for i in range(1, 11):
        cube = i ** 3
        print(f"{i} в кубе = {cube}")
        time.sleep(0.1)

if __name__ == '__main__':
    thread1 = threading.Thread(target=calculate_squares)
    thread2 = threading.Thread(target=calculate_cubes)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("comleted")