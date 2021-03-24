from requests import get


def download(url, filename, extention):
    img_data = get(url).content
    with open('images/' + filename + '.' + extention, 'wb') as handler:
        handler.write(img_data)


if __name__ == "__main__":
    print('this is a module not meant to be run directly')
