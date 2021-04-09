import requests


def func(api, port, name='', *args, **kwargs):
    # "name" in args
    # dict na servere
    # key = name
    # value = tuple with dict
    # return .json
    url = f'http://{api}:{port}/get_data/{name},12'
    a = requests.get(url).json()
    print(a)


func("127.0.0.1", "8080", name="Егор")

