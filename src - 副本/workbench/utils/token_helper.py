import jwt
import requests
from loguru import logger


PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnn3jPyW81YqSjSLWBkdE
ZzurZ5gimj6Db693bO0WvhMPABpYdOTeAU1mnQh2ep4H7zoUdz4PKARh/p5Meh6l
ejtbyliptvW9WXg5LoquIzPyTe5/2W9GoTrzDHMdM89Gc2dn16TbsKU5z3lROlBP
Q2v7UjQCbs8VpSogb44kOn0cx/MV2+VBfJzFWkJnaXxc101YUteJytJRMli0Wqev
nYqzCgrtbdvqVF/8hqETZOIWdWlhRDASdYw3R08rChcMJ9ucZL/VUM+aKu+feekQ
UZ6Bi6CeZjgqBoiwccApVR88WbyVXWR/3IFvJb0ndoSdH85klpp25yVAHTdSIDZP
lQIDAQAB
-----END PUBLIC KEY-----
""".strip()


def is_valid_token(token):
    public_key = PUBLIC_KEY
    try:
        return jwt.decode(
            jwt=token,
            key=public_key,
            algorithms=[
                "RS256",
            ],
            options={"verify_signature": bool(public_key)},
        )
    except Exception:
        pass


def get_user_id(token):
    if not token:
        return None
    token_info = is_valid_token(token)
    if not token_info:
        return None
    return str(token_info.get("identity").get("userId"))


def get_user_key(token):
    if not token:
        return None
    token_info = is_valid_token(token)
    if not token_info:
        logger.warning("failed to get token_info")
        return None
    try:
        headers = {
            "Authorization": f"Bearer {token}",
        }
        response = requests.get(
            "https://bohrium.dp.tech/brm/v1/account/info",
            headers=headers,
        )
        response.raise_for_status()
        res = response.json()
        logger.debug(res)
        if str(res["code"]) != "0":
            raise Exception(f"error code return : {res}")
        return res["data"]["email"] or res["data"]["phone"]
    except Exception:
        pass
