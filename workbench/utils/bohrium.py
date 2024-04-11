import requests
from loguru import logger


def get_default_project(token: str):
    # 设置请求头
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}

    # 设置请求参数
    params = {"cost": "0"}

    # 发起 GET 请求
    url = "https://bohrium.dp.tech/bohrapi/v2/project/available_v2"
    response = requests.get(url, headers=headers, params=params)

    # 检查响应
    if response.status_code == 200:
        data = response.json()
        logger.debug(data)
    else:
        logger.error(f"Request failed with status code: {response.status_code}")
        return None
    return data["data"]["private"][0]["projectId"]


def get_projects(token: str):
    # 设置请求头
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}

    # 设置请求参数
    params = {"cost": "0"}

    # 发起 GET 请求
    url = "https://bohrium.dp.tech/bohrapi/v2/project/available_v2"
    response = requests.get(url, headers=headers, params=params)

    # 检查响应
    if response.status_code == 200:
        data = response.json()
        logger.debug(data)
    else:
        logger.error(f"Request failed with status code: {response.status_code}")
        return None
    private_projects = data["data"]["private"]
    public_projects = data["data"]["public"]
    projects = []
    for p in private_projects:
        if p["available"]:
            projects.append(
                {"projectId": p["projectId"], "projectName": p["projectName"]}
            )
    for p in public_projects:
        if p["available"]:
            projects.append(
                {"projectId": p["projectId"], "projectName": p["projectName"]}
            )
    return projects
