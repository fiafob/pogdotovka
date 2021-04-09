from pprint import pprint

import requests


def get_data(ip, port, *args, **kwargs):
    dic = {}
    response = requests.get(f"http://{ip}:{port}/").json()
    for i in kwargs:
        if i != 'name':
            dic[i] = kwargs[i]

    response[kwargs["name"]] = response.get(kwargs["name"], []) + [dic]
    # if kwargs["name"] in response:
    #     response[kwargs["name"]].append(dic)
    # else:
    #     response[kwargs["name"]] = [dic]
    return response


if __name__ == "__main__":
    qres = get_data("127.0.0.1", 8080, name="Egor", bio=60, rus=80, lit=60)
    pprint(qres)
