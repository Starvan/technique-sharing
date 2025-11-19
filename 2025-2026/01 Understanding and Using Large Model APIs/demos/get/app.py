import requests

url = "https://api.ipify.org/"
# url = "https://jsonplaceholder.typicode.com/posts/999999"

try:
    response = requests.get(url, timeout=15) 

    if response.status_code == 200:
        print("GET 请求成功。状态码: 200")
        content_type = response.headers.get('Content-Type')
        print(f"Content-Type: {content_type}")
        print(f"响应内容长度: {len(response.text)} 字符")

        print("响应内容:")
        print(response.text[:500])
        
    else:
        print(f"GET 请求失败。状态码: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"请求过程中发生错误: {e}")