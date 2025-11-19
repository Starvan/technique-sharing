import requests
import json

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, timeout=15) 

    if response.status_code == 200:
        print("GET 请求成功。状态码: 200")
        
        content_type = response.headers.get('Content-Type')
        print(f"Content-Type: {content_type}")
        
        if 'application/json' in content_type:
            user_data = response.json()
            print(json.dumps(user_data, indent=4, ensure_ascii=False))

            # print(f"name: {user_data.get('name')}")
            # print(f"email: {user_data.get('email')}")
            # print(f"city: {user_data.get('address', {}).get('city')}")
        else:
            print("响应的 Content-Type 不是预期的 application/json。")
        
    else:
        print(f"GET 请求失败。状态码: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"请求过程中发生错误: {e}")