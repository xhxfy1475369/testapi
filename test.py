import uuid

import requests

BASE_URL = "http://115.92.19.126:9999"  # 替换为你的实际API地址


def post_json(path, data):
    url = BASE_URL + path
    headers = {
        "Content-Type": "application/json"
    }
    resp = requests.post(url, json=data, headers=headers, verify=False)  # verify=False如有自签证书
    print(f"Request to {url} with data {data}")
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")
    print(f"Response2: {resp.json()}")
    try:
        return resp.json()
    except Exception:
        return resp.text


def import_account(file_bytes, replace=True):
    file_arr = list(file_bytes)
    data = {
        "file": file_arr,
        "replace": replace
    }
    return post_json("/v1/account/import", data)

def upload(file_bytes,ext):
    file_arr = list(file_bytes)
    data = {
        "file": file_arr,
        "ext": ext,
    }
    return post_json("/v1/file/upload", data)



def login(phone, socks5):
    data = {
        "phone": phone,
        "socks5": socks5,
        "uid": str(uuid.uuid4())
    }
    return post_json("/v1/account/login", data)


def logout(phone):
    data = {
        "phone": phone,
        "uid": str(uuid.uuid4())
    }
    return post_json("/v1/account/logout", data)


def get_content_list(phone):
    data = {
        "phone": phone,
        "uid": str(uuid.uuid4())
    }
    return post_json("/v1/contact/list", data)


def edit_user_info(phone, about, firstName, lastName):
    data = {
        "phone": phone,
        "about": about,
        "firstName": firstName,
        "lastName": lastName,
        "uid": str(uuid.uuid4())
    }
    return post_json("/v1/profile/firstLastName", data)


def edit_username(phone, userName):
    data = {
        "phone": phone,
        "username": userName,
        "uid": str(uuid.uuid4())
    }
    return post_json("/v1/profile/username", data)


if __name__ == "__main__":
    # login("919912383744","socks5://100_ID__OFB47S_1800_2:5b3c8a5fe22f9c1430ad677d031d7a58@38.46.218.39:65310")
    # logout("919912383744")
    # get_content_list("919912383744")
    # edit_user_info("919912383744", "holle every one", "Tom", "davida")
    # edit_username(phone="919912383744", userName="jpeg09876192")
    with open("account.json", "rb") as e:
        file = e.read()
    # import_account(file)
    upload(file,"json")
