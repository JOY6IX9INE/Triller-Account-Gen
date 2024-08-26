from faker import Faker
from time import perf_counter
from datetime import datetime
import requests, random, time, string, json, threading, os, ctypes
os.system('cls' if os.name == 'nt' else 'clear')

def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

config = load_config()
mail_api = 'https://api.mail.gw'
faker = Faker('en_IN')
api_key = config.get('captcha_key')
proxy = config.get('proxy')
proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}

class counter:
    success = 0
    failed = 0

red = '\x1b[31m(-)\x1b[0m'
blue = '\x1b[34m(+)\x1b[0m'
green = '\x1b[32m(+)\x1b[0m'
yellow = '\x1b[33m(!)\x1b[0m'

def get_timestamp():
    time_idk = datetime.now().strftime('%H:%M:%S')
    timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
    return timestamp

def get_captcha():
    start_time = perf_counter()
    json_data = {
        "clientKey": api_key,
        "task": {
            "type": "ReCaptchaV2TaskProxyLess",
            "websiteURL": "https://triller.co/",
            "websiteKey": "6LfUdUEaAAAAAJWJ8wlMSInIEoc2XuLrovZP7GBv",
            "isInvisible": False
        }
    }

    response = requests.post("https://api.ez-captcha.com/createTask", json=json_data)
    result = response.json()

    if result:
        captcha_id = result["taskId"]
        status = "processing"
        print(f"{get_timestamp()} {blue} Created Captcha Task : {captcha_id}")

        headers = {
            'Content-Type': 'application/json'
        }

        json_data = {
            "clientKey": api_key, 
            "taskId": captcha_id
        }

        while status != "ready":
            time.sleep(5)
            solve_response = requests.post("https://api.ez-captcha.com/getTaskResult", json=json_data, headers=headers)
            solve_result = solve_response.json()
            status = solve_result["status"]

        if "solution" in solve_result:
            end_time = perf_counter()
            elapsed_time = end_time - start_time
            time_info = f"{elapsed_time:.2f} Seconds"
            solution = solve_result["solution"]["gRecaptchaResponse"]
            print(f"{get_timestamp()} {blue} Solved Captcha In {time_info} : {solution[:50]}....")
            return solution
    else:
        print(f"{get_timestamp()} {red} Error : ", result["errorId"])

def create_mail():
    try:
        retries = 0
        while retries < 20:
            try:
                get_domain = requests.get(f'{mail_api}/domains', proxies=proxies)
                domains = [item["domain"] for item in get_domain.json()["hydra:member"]]
                domain = random.choice(domains)

                m1 = faker.last_name()
                m2 = ''.join([str(random.randint(0, 9)) for _ in range(5)])
                mail = f'{m1}{m2}@{domain}'.lower()

                data = {
                    "address": mail,
                    "password": f"{m1}:{m2}"
                }
                
                requests.post(f'{mail_api}/accounts', json=data, proxies=proxies)
                get_token = requests.post(f'{mail_api}/token', json=data)
                return mail, get_token.json()["token"]
            except:
                time.sleep(1)
                retries += 1
    except:
        print(f'{get_timestamp()} {red} Error Occurred While Creating Mail : {get_token.status_code}')

def create_acc(mail, captcha):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://triller.co',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    m1 = faker.last_name()
    m2 = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    password = ''.join(random.choices(string.ascii_letters, k=8))
    json_data = {
        'email_address': mail,
        'username': f'{m1}{m2}',
        'password': password,
        'user_captcha': captcha,
    }

    while True:
        try:
            response = requests.post('https://social.triller.co/v1.5/user/web-create', headers=headers, json=json_data, proxies=proxies)
            break
        except:
            continue
    status = response.json()["status"]
    if status == True:
        auth_token = response.json()["auth_token"]
        counter.success += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Triller Account Gen | Made With <3 By Joy | Success : {counter.success} | Failed : {counter.failed}")
        print(f"{get_timestamp()} {green} Sucessfully Created Account : {auth_token[210:]}...")
        with open("output/success.txt", "a") as file: file.write(f"{mail}:{password}" + "\n")
    else:
        counter.failed += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Triller Account Gen | Made With <3 By Joy | Success : {counter.success} | Failed : {counter.failed}")
        with open("output/failed.txt", "a") as file: file.write(f"{mail}:{password}" + "\n")
        print(f"{get_timestamp()} {red} Failed To Create Account, {response.status_code} : {response.text}")

def worker():
    while True:
        try:
            mail, mail_tk = create_mail()
        except:
            pass
        captcha = get_captcha()
        create_acc(mail, captcha)

def start(num_threads):
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        thread.start()

if __name__ == "__main__":
    num_threads = int(input(f"{get_timestamp()} {blue} Enter The Number Of Threads : "))
    start(num_threads)
