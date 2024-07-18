import requests

url = "https://dom.ufanet.ru/api/v0/skud/shared/12373/open/"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,et-EE;q=0.6,et;q=0.5",
    "Connection": "keep-alive",
    "Dnt": "1",
    "Host": "dom.ufanet.ru",
    "Referer": "https://dom.ufanet.ru/office/skud/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

cookies = {
    "_ga": "GA1.1.2051290483.1721153727",
    "tmr_lvid": "2e9bc631f30ef8388b6bc063e579aeee",
    "tmr_lvidTS": "1721153727537",
    "_ym_uid": "1721153729228819709",
    "_ym_d": "1721153729",
    "lhc_per": '{"vid":"3d64d8109f21c5a90405","ex":17222}',
    "_ga_LC6P9JT7DE": "GS1.1.1721153727.1.1.1721154146.60.0.0",
    "ack": "8090d0db5225b03b5d8ceae6380bd0c1",
    "tz": "Europe/Moscow",
    "_ym_isad": "2",
    "csrftoken": "mHEYZrm4FYHFHJr7CG79L4y5a0j4e1pLT8lEa9YIHWhpEVL59Qnz98RRCF6eGCvH",
    "sessionid": "bl8q1ziifwpm7l5pnjbemqdq0qj0kqwu"
}

def open():
    response = requests.get(url, headers=headers, cookies=cookies)
    print('opened')