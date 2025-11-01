import threading
import time

def print_numbers():

    for i in range(1, 11):
        print(i)
        time.sleep(1)

if __name__ == "__main__":

    num_threads = 3 

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=print_numbers)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Все потоки завершены")