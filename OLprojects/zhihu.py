#导入requests库
import requests
#新建用于保存数据的csv文件
with open('知乎.csv','w') as f:
    f.write('标题,链接,热力值,分类,关注增量,浏览增量,回答增量,赞同增量\n')
    #循环爬取知乎热点榜单数据
    for i in range(0,100,20):
        #根据offset参数重组并请求url
        url=f'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset={i}&period=hour'
        response=requests.get(url)
        #以循环方式分别获取知乎热点榜单中的标题,链接,热力值,分类,关注增量,浏览增量,回答增量,赞同增量等相关数据，并将其写入至文件内
        for d in response.json()['data']:
            url=d['question']['url']
            title=d['question']['title']
            score=str(d['reaction']['score'])
            names=[]
            for t in d['question']['topics']:
                names.append(t['name'])
            new_follow_num=str(d['reaction']['new_follow_num'])
            new_pv=str(d['reaction']['new_pv'])
            new_answer_num=str(d['reaction']['new_answer_num'])
            new_upvote_num=str(d['reaction']['new_upvote_num'])
            f.write(','.join([title,url,score,'/'.join(names),new_follow_num,new_pv,new_answer_num,new_upvote_num])+'\n')
