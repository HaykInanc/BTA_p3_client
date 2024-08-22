import requests
from urllib.parse import urljoin

BASE_URL = 'http://127.0.0.1:8000/api/'

def login(username, password):
    url = BASE_URL + 'login/'
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    return response.json()

def logout(token):
    url = urljoin(BASE_URL, 'logout/')
    headers = {'Authorization': f'Token {token}'}
    response = requests.post(url, headers=headers)
    return response.json()

def create_user(username, password, email):
    url = urljoin(BASE_URL, 'user/create/')
    data = {'username': username, 'password': password, 'email': email}
    response = requests.post(url, data=data)
    return response.json()

def create_task(token, task_data):
    url = urljoin(BASE_URL, 'task/create/')
    headers = {'Authorization': f'Token {token}'}
    response = requests.post(url, headers=headers, json=task_data)
    return response.json()

def get_user_tasks(token):
    url = urljoin(BASE_URL, 'user/tasks/')
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_tasks_with_executor():
    url = urljoin(BASE_URL, 'task/executor/')
    response = requests.get(url)
    return response.json()

# =========

def get_my_tasks(auth_token):
    url = urljoin(BASE_URL, 'tasks-created-by-user/')
    headers = {'Authorization': f'Token {auth_token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def mark_task_done(auth_token, task_id):
    url = urljoin(BASE_URL, f'mark-task-done/{task_id}/')
    headers = {'Authorization': f'Token {auth_token}'}
    response = requests.patch(url, headers=headers)
    return response.json()

def get_user_tasks_stats(auth_token):
    url = urljoin(BASE_URL, 'user-tasks-stats/')
    headers = {'Authorization': f'Token {auth_token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_user_tasks(auth_token):
    url = urljoin(BASE_URL, 'user-tasks/')
    headers = {'Authorization': f'Token {auth_token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_unassigned_tasks(auth_token):
    url = urljoin(BASE_URL, 'unassigned-tasks/')
    headers = {'Authorization': f'Token {auth_token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def become_executor(auth_token, task_id):
    url = urljoin(BASE_URL, f'become-executor/{task_id}/')
    headers = {'Authorization': f'Token {auth_token}'}
    response = requests.patch(url, headers=headers)
    return response.json()

if __name__ == '__main__':


    result = login("user_2", "password_2")
    token = result['token']
    # print(result)

    # token = '4a73ec74a0acdb0a9cbc149412a6209d8a528ea7'
    # logout_result = logout(token)
    # print(logout_result)

    # task_data = {
    #     "executor": 6,
    #     "name": "__",
    #     "cost": 1200,
    #     "deadline": "2024-05-30"
    # }

    

    # response = create_task(token, task_data)
    # print(response)

    # response = get_user_tasks(token)
    # print(response)

    # print(get_my_tasks(token))

    # print(mark_task_done(token, 24))


    print(get_user_tasks_stats(token))

    # print(get_my_tasks(token))

    # print(get_unassigned_tasks(token))

    # print(become_executor(token, 17))