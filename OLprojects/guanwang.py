
import requests                                
import re                                     
from bs4 import BeautifulSoup                 
import xlwt                                   
import datetime                
import time



def main():  
    til=int(input("请输入您要每几秒爬一次通知信息："))  
    i=0
    while True:
        i=i+1
        now = datetime.datetime.now()
        print("现在时间为：",now.hour,":",now.minute)
        print('这个程序要开始疯狂的运转啦,这是第',i,"次启动爬虫")
        time.sleep(til)  
        doSth() 

def doSth():   #dosth程序模块

    uk="https://www.bkjx.sdu.edu.cn/sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010"
    r=requests.get(uk,timeout=30)
    soup= BeautifulSoup(r.text,"html.parser")
    div=soup.find_all(id=re.compile('line_u7')) 
  
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)  
    sheet = book.add_sheet('学校官网通知',cell_overwrite_ok=True)  
   
    col=('日期','网址','通知内容')  
    sheet.write(0, 0, '内容')      
    for i in range(0,3):            
        sheet.write(0,i,col[i])    


    #以下写把日期提取出来
    yy=1
    for k in div: 
        zf=k.text
        zf1=zf[-12:-2]     
        sheet.write(yy,0,zf1)  
        zf2=zf[0:-13]         
        sheet.write(yy,2,zf2)  
        yy=yy+1

    #以下网址提取并写入excel
    iop=re.compile('div style="float:left"><a href="(?P<url>.*?)" target=_blank title="',re.S)   #将变量变成电脑能识别的类型
    result=re.finditer(iop,r.text)
    zz=1
    for i in result:
        a=i.group("url")
        kk=a[0:4]  
        if kk!='http':
            a="https://www.bkjx.sdu.edu.cn/"+a
        sheet.write(zz,1,a)
        zz=zz+1

    savepath = 'C:/Users/jxc/Desktop/通知表格.xls'    
    book.save(savepath)            
    print("===============程序运行结束==============")


#======以下主程序直接调用上面的main()子程序=============
main() 

