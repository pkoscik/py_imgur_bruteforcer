import threading
from random import choice
from string import ascii_letters, digits
from requests import get
from sys import argv, exit
import saver

imgur_empty_len = 484

used_ids = []

worker_count = 0
url_found = 0


def limits(workers, lenght, extention, type):
    if workers < 1: return True
    if lenght not in [5, 7]: return True
    if extention not in ['png', 'jpg', 'jpeg', 'gif']: return True
    if type not in [1, 2, 3]: return True

    return False


def worker(lenght, extention, type):
    global worker_count
    global url_found

    if type == 1:
        random = ''.join(choice(ascii_letters) for k in range(lenght))

    if type == 2:
        random = ''.join(choice(digits) for k in range(lenght))

    if type == 3:
        random = ''.join(choice(ascii_letters + digits) for k in range(lenght))

    link = 'https://i.imgur.com/' + random + '.' + extention

    r = get(link)

    if len(r.text) != imgur_empty_len:
        print('image found:', link)
        saver.download(link, str(worker_count), extention)

    worker_count += 1


if __name__ == "__main__":

    argl = len(argv)

    # inccorect arguments
    if argl != 1 and argl != 5:
        print(''
              '\n\n'
              'py_imgur_bruteforcer, a simple utility to find and download randomly found imgur images\n\n'
              'bruteforcer.py [workers] [ext] [len] [type]\n'
              '\t[workers] -> int, no. of workers\n'
              '\t[ext] -> string,  filename extention - png, jpg, jpeg, gif\n'
              '\t[len] -> int, lenght of imgur_id - 5 or 7\n'
              '\t[type] -> int, type of ids to scan - 1: letters 2: digits 3: mixed\n')
        exit(1)

    # if no arguments are passed ask user for input
    if argl == 1:
        worker_ammount = int(input('How many workers to run?\n'))
        url_ext = input('File extension? (png, jpg, jpeg, gif)\n')
        url_len = int(input('Url lenght? (5, 7)\n'))
        url_type = int(input('Type of url? ( 1: letters, 2: digits, 3: mixed) \n'))

    # correct arguments
    if argl == 5:
        worker_ammount = int(argv[1])
        url_ext = argv[2]
        url_len = int(argv[3])
        url_type = int(argv[4])

    # check input
    if limits(worker_ammount, url_len, url_ext, url_type):
        print('Incorrect values for one or more fields, check your inputs and try again')
        exit(1)

    # debug info
    print('Starting', worker_ammount, 'workers')
    print('url type: https://i.imgur.com/' + '_' * url_len + '.' + url_ext, 'searching for id of type:', url_type)

    # threading
    worker_list = []
    for t in range(worker_ammount):
        thread = threading.Thread(target=worker, args=[url_len, url_ext, url_type])
        worker_list.append(thread)

    for worker in worker_list:
        worker.start()
