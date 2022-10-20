import requests
import json

with open('B站.csv','w') as f:
    f.write('共同关注,UID\n')

    url1='https://api.bilibili.com/x/relation/followings?vmid=31536760&pn=1&ps=50&order=desc&order_type=attention'
    url2='https://api.bilibili.com/x/relation/followings?vmid=390601281&pn=1&ps=50&order=desc&order_type=attention'
    res1=requests.get(url1)
    res2=requests.get(url2)
    yuandai1=json.loads(res1.text)
    yuandai2=json.loads(res2.text)
    datalist1=yuandai1['data']['list']
    datalist2=yuandai2['data']['list']

   

    for d in datalist1:
        mid1=str(d['mid'])
        for e in datalist2:
            mid2=str(e['mid'])
            if mid1==mid2:
                uname=str(e['uname'])
                uid=str(mid2)
                f.write(','.join([uname,uid])+'\n')
            
    
          
            

        
    
   
      
        
