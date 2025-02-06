import requests
import json
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=5NI1wgZX5OHJXox7MUewT3TwrjmvStFA&data=AP01' 
session = requests.Session()
res = session.get(url).text
data = json.loads(res)
# print(type(data))
result = data[-1]['deal_bas_r']
# print(result,type(result))
print('='*40)
print(f"오늘의 환율은 1달러에 {result} 원 입니다.")
print('='*40)
