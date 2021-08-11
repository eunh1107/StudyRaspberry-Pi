# Python 샘플 코드 #


from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'j5J6c893mZ0VRisap13rlqyVKncdyCssD+IKFN1j6EbfDeuwD2J8T6QGeriyWBeh6AXlj51/Xj16FPjj0v3dig==', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'JSON', quote_plus('base_date') : '20210810', quote_plus('base_time') : '0600', quote_plus('nx') : '57', quote_plus('ny') : '120' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)
