import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

new_post_payload = {
    "title": "演示标题",
    "body": "你好",
    "userId": 20251119
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

try:
    response = requests.post(url, headers=headers, json=new_post_payload, timeout=15) 

    if response.status_code == 201:
        print("POST 请求成功。状态码: 201")
        
        content_type = response.headers.get('Content-Type')
        print(f"Content-Type: {content_type}")
        
        if 'application/json' in content_type:
            response_data = response.json()
            
            print("服务器响应:")
            print(json.dumps(response_data, indent=4, ensure_ascii=False))
            
            print(f"服务器分配的 ID: {response_data.get('id')}")
            
        else:
            print("响应的 Content-Type 不是预期的 application/json。")
        
    else:
        print(f"POST 请求失败。状态码: {response.status_code}")
        print(f"错误内容预览: {response.text[:100]}")
        
except requests.exceptions.RequestException as e:
    print(f"请求过程中发生错误: {e}")