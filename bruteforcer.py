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

    print('py_imgur_bruteforcer, a simple utility to find and download randomly found imgur images')

    argl = len(argv)

    # inccorect arguments
    if argl != 1 and argl != 5:
        print('incorrect arguments, exitting')
        exit(-1)

    # if no arguments are passed ask user for input
    if argl == 1:
        worker_ammount = int(input('How many workers to run?\n'))
        url_ext = input('File extension? (png, jpg, jpeg)\n')
        url_len = int(input('Url lenght? (5 or 7)\n'))
        url_type_chooser = input('Type of url? ( 1: letters, 2: digits, 3: mixed) \n')

    # correct arguments
    if argl == 5:
        worker_ammount = int(argv[1])
        url_ext = argv[2]
        url_len = int(argv[3])
        url_type = int(argv[4])

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
