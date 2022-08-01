#author:一只小流浪(http://github.com/YiZhiXiaoLiuLang)
#data:2022/8/1 14:30(UTC+8)

import requests,time
print("=========ip定位===========")
#https://www.douyacun.com/api/openapi/geo/location?ip=&token=
'''
{
'code':0,
'message':'success',
'data':
    {
    'countryCode':'CN',
    'country':'中国',
    'province':'浙江',
    'city':'嘉兴',
    'ip':'111.3.2.222',
    'latitude':'30.75220',
    'longitude':'120.75000',
    'zipcode':'314000',
    'timezone':'+08:00',
    'refer':'douyacun.com'
    }
}
'''
token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBY2NvdW50SWQiOiJlZWQ4ZmQ1ODBmYTRmNjkyIn0.d7qF_mjdXMC0R5M6f04Lnh6x61kaU4lqHT0Axt9xUOY"
ip=input("请输入要查询的ip地址：")
print("正在定位中")
res=requests.get("https://www.douyacun.com/api/openapi/geo/location?ip="+ip+"&token="+token)
jsondata=res.json()


print("状态:",end='')
code=jsondata['code']#0代表成功

if code==0:
    print("成功",end='')
    
else:
    print("失败",end='')
try:    
    print("("+jsondata['message']+")")
except:
    print("(无法获取详细信息)")
if code==0:
    print("地址: ",jsondata['data']['country'],jsondata['data']['province'],jsondata['data']['city'])
    print("时区：UTC"+jsondata['data']['timezone'])
    
time.sleep(5000)
