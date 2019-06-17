import requests
import re
import MySQLdb


def find_all_content(html):
        name_list=re.findall('alt="(.*)" src',html)
        other_list=re.findall('<span class="other">kongge/kongge(.*)</span>',html)
        direct_list=re.findall('导演: (.*?)kongge*',html)
        year_list=re.findall('([0-9]{2,4}).*kongge/',html)
        from_list=re.findall('kongge/kongge([\u4e00-\u9fa5\s]*?)kongge/kongge',html)
        type_list=re.findall('kongge/kongge[\u4e00-\u9fa5\s]*?kongge/kongge(.*)',html)
        content_list=re.findall('<span class="inq">(.*)</span>',html)
        return name_list,other_list,direct_list,year_list,from_list,type_list,content_list


def insql(name_list,other_list,direct_list,year_list,from_list,type_list,content_list):
        conn=MySQLdb.connect(host='localhost',user='root',passwd='admin',db='python',charset="utf8")
        cur=conn.cursor()
        count=0
        for name in name_list:
                cur.execute('INSERT INTO doubantop250_douban(d_name,d_other,d_direct,d_year,d_from,d_type,d_content) VALUES("%s","%s","%s","%s","%s","%s","%s")',(str(name),str(other_list[count]),str(direct_list[count]),str(year_list[count]),str(from_list[count]),str(type_list[count]),str(content_list[count])))
                count=count+1

        cur.close()
        conn.commit()
        conn.close()


headers={'Host':'movie.douban.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
for i in range(0,10):
        url='https://movie.douban.com/top250?start='+str(i*25)
        r=requests.get(url,headers=headers)
        html=r.text.replace("&nbsp;","kongge")
        name_list,other_list,direct_list,year_list,from_list,type_list,content_list=find_all_content(html)
        if i==8:
                direct_list.insert(8,'普特鹏·普罗萨卡·那·萨克那卡林 Puttipong Promsaka Na Sakolnakorn / 华森·波克彭')
                #能力有限，这个导演名字太长了，太长了，都把空格符给挤没了......
        insql(name_list,other_list,direct_list,year_list,from_list,type_list,content_list)
                
