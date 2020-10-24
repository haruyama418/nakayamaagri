import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import *
from time import *
from PIL import Image, ImageTk
## \n

root = tk.Tk()

fr1 = tk.Frame(root,bg='gainsboro',width=350,height=35,)
fr1.propagate(False) #フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)
fr1.grid(column=0,row=0,columnspan=2,sticky=tk.W+tk.E)
fr2=tk.Frame(root,bg='lightgray',width=200,height=100,)
fr2.propagate(False)
fr2.grid(column=0,row=1,sticky=tk.W)
fr3=tk.Frame(root,bg='lightgray',width=150,height=100)
fr3.propagate(False)
fr3.grid(column=1,row=1,sticky=tk.W)
fr4=tk.Frame(root,bg='gainsboro',width=350,height=250)
fr4.propagate(False)
fr4.grid(column=0,row=2,columnspan=2)

#----------------traffic------------------
def traffic():
    traffic_lb1 = tk.Label(fr1, text='運行状況:',bg='gainsboro')
    traffic_lb1.grid(column=0,row=0,)
    #----------------odakyu------------------
    address = "https://www.odakyu.jp/cgi-bin/user/emg/emergency_bbs.pl"
    resp = requests.get(address)
    soup = BeautifulSoup(resp.text, 'html.parser')#resp.text
    odakyu = soup.find('p', class_='ttl_daiya_blue')
    odakyu=str(odakyu.text)
    print(odakyu)
    if "平常"in odakyu:
        traffic_lb2 = tk.Label(fr1, text=odakyu,bg='skyblue')
        traffic_lb2.grid(column=1,row=0,sticky=tk.W+tk.E)
    else:
        traffic_lb2 = tk.Label(fr1, text=odakyu, foreground='white',bg='red')
        traffic_lb2.grid(column=1, row=0,sticky=tk.W+tk.E)
    # ----------------Keio------------------
    address = "https://www.keio.co.jp/unkou/unkou_pc.html"
    resp = requests.get(address)
    soup = BeautifulSoup(resp.content, 'html.parser')#文字化け防止でresp.content
    keio = soup.find(class_='status')
    keio = str(keio.text)
    print(keio)
    if "平常"in keio:
        traffic_lb3 = tk.Label(fr1, text=keio, bg='plum',)
        traffic_lb3.grid(column=1, row=1,sticky=tk.W+tk.E)
    else:
        traffic_lb3 = tk.Label(fr1, text=keio, foreground='white', bg='red',)
        traffic_lb3.grid(column=1, row=1, sticky=tk.W+tk.E)
    up_date= strftime('%H:%M:%S')
    time_label=tk.Label(fr1,text=up_date,bg='gainsboro')
    time_label.grid(column=0,row=1)
    root.after(100000, traffic)

traffic()

#------------時計--------------------------------------------------

buff = StringVar()
buff.set('')
buff2 = StringVar()
buff2.set('')
buff3 = StringVar()
buff3.set('')
#font1= tk.Fotnt(size=25)
day_label=Label(fr2,textvariable = buff3,bg='lightgray', font=("",20))
day_label.pack(anchor='w')
time=Label(fr2,textvariable = buff, bg="lightgray",font=("",60))
time.pack(side='left')
sec=Label(fr2,textvariable = buff2,bg='lightgray', font=("",25))
sec.pack(side='left',anchor='s')

def show_time():
    buff.set(strftime('%H:%M'))
    buff2.set(strftime('%S'))
    buff3.set(strftime('%m /%d (%a)'))
    root.after(1000, show_time)  #つまり、時間の取得を関数化して、毎秒行う

show_time()
#--------------------------------------------------------------

#---------天気-----------------------------------------------------
"""
sunny= tk.PhotoImage(file='sun.png')
rainy= tk.PhotoImage(file='rain.png')
cloudy= tk.PhotoImage(file='cloudy.png')
cloudy_rainy= tk.PhotoImage(file='cloudy-_rain.png')
"""
def weather():
    address = "https://tenki.jp/forecast/3/17/4610/14137/"
    resp = requests.get(address)
    soup = BeautifulSoup(resp.text, 'html.parser')  # resp.text
    weather = soup.find('p', class_='weather-telop').text
    prb1 = soup.find_all('td')[0].text#probability of rain
    prb2 = soup.find_all('td')[1].text
    prb3 = soup.find_all('td')[2].text
    prb4 = soup.find_all('td')[3].text
    print(weather)
    print(prb1,prb2,prb3,prb4)
    if weather =="晴" or weather=="晴時々曇":
        txt="☀️"
        bg="orange"
    elif weather =="晴のち曇":
        txt='⛅️'
        bg="gray"
    elif weather =="曇のち雨":
        txt="☔️"
        bg="royalblue"
    elif weather =="雨":
        txt="☔️"
        bg="royalblue"
    elif weather =="雪":
        txt="⛄️️"
    elif weather == "曇":
        txt = "☁️️️"
        bg="gray"
    elif weather =="雷":
        txt="🌪☔️"
        bg="royalblue"
    else:
        txt="?"
        bg="coral"
    tenki_label = tk.Label(fr3, text=txt,font=("",40),bg=bg)
    tenki_label.pack(fill='x')
    tenki_label2 = tk.Label(fr3, text=weather, font=("", 16), bg=bg)
    tenki_label2.pack(fill='x')
    rain_prob= tk.Label(fr3,text="|"+str(prb1)+"|"+str(prb2)+"|"+str(prb3)+"|"+str(prb4),
                        font=("",16),bg='lightgray')
    rain_prob.pack()
weather()



#--------------------------------------------------------------

#-------NEWS-------------------------------------------------------
news_update_btn =tk.Button(fr4,text="最新ニュースを更新：", foreground="steelblue")
news_update_btn.pack(anchor=tk.W)

def news():
    address = "https://news.yahoo.co.jp/"
    resp = requests.get(address)
    soup = BeautifulSoup(resp.text, 'html.parser')  # resp.text
    contents = soup.find_all('li',class_='topicsListItem')
    for content in contents:
    #latest_news = soup.find_all('em',class_='title')
        print(content.text)
        main_news=tk.Label(fr4,text=":"+str(content.text),font=("",15,"bold"),bg='gainsboro')
        #main_news.grid(column=0,columnspan=3,sticky=tk.W)
        main_news.pack(anchor=tk.W, )
    root.after(1000000, news)
news()



def update_news(event):

    print('hi')

news_update_btn.bind("<Button-1>", update_news)


#--------color------------------------------------------------------
color=['gray','skyblue']
#--------------------------------------------------------------
root.mainloop()

