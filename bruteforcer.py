import threading
from random import choice
from string import ascii_letters
from requests import get

imgur_empty_len = 484
worker_id = 0


def generator(lenght=7, extention='jpeg'):
    random = ''.join(choice(ascii_letters) for k in range(lenght))
    url = 'https://i.imgur.com/' + random + '.' + extention
    return url


def worker():
    global worker_id

    worker_id += 1
    link = generator()
    r = get(link)

    if len(r.text) != imgur_empty_len:
        print('worker:', worker_id, 'image found:', link)

    worker_id -= 1

if __name__ == "__main__":

    worker_ammount = 4000
    worker_list = []

    for t in range(worker_ammount):
        thread = threading.Thread(target=worker)
        worker_list.append(thread)

    for worker in worker_list:
        worker.start()

    print(len(worker_list))
