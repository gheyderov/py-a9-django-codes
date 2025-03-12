
import time
import multiprocessing
import requests
import uuid

t1 = time.time()

def do_something():
    print('Process Started!')
    response = requests.get('https://picsum.photos/200/300')
    with open(f'images/image_{uuid.uuid4()}.png', 'wb') as file:
        file.write(response.content)
    print('Process end!')

threads = []

if __name__ == '__main__':
    for i in range(10):
        th = multiprocessing.Process(target=do_something)
        th.start()
        threads.append(th)

    for element in threads:
        element.join()

t2 = time.time()

print(t2 - t1)