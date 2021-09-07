import requests

def get_lettersum_list():

    request = requests.get(
        "https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt")

    res = request.text.split('\n')

    return res