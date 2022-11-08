from flask import Flask
from flask_app.routes import user
import pickle
import pandas as pd
from flask import Blueprint, render_template, request

total_book = pd.read_csv('total_book.csv')

app = Flask(__name__)
app.register_blueprint(user.bp)

with open('model.pkl','rb') as pickle_file:
    rf1 = pickle.load(pickle_file)

# 공포/스릴러 1, 추리/미스터리 2, 로맨스 3, sf 4, 판타지 5, 역사 6 으로 매핑
@app.route('/<gerne>/<price>/<review>', methods=['GET','POST'])
def index(gerne, price, review):
        sac = [{'gerne':gerne, 'price':price, 'review':review}]
        star = rf1.predict(sac)

        if star == '[0.]':
            star = '만족도가 낮다'
        else:
            star = '만족도가 높다'

        if gerne == '1':
            gerne = '공포/스릴러'
        elif gerne =='2':
            gerne ='추리/미스터리'
        elif gerne =='3':
            gerne ='로맨스'
        elif gerne =='4':
            gerne = 'sf'
        elif gerne == '5':
            gerne = '판타지'
        elif gerne== '6':
            gerne='역사'

        return f"장르가 {gerne}, 가격이 {price}원, 리뷰의 수가 {review}이면 독자들의 {star}."



a = None
@app.route('/recommend/<gg>', methods=['GET','POST'])
def gerne(gg):
    global a 
    if gg == '1':
        a  =total_book[(total_book['gerne']=='공포/스릴러') & (total_book['star_line']==1)]
        return a.head(10).to_html()
    elif gg =='2':
        a = total_book[(total_book['gerne']=='추리/미스터리') & (total_book['star_line']==1)]
        return a.head(10).to_html()
    elif gg =='3':
        a= total_book[(total_book['gerne']=='로맨스') & (total_book['star_line']==1)]
        return a.head(10).to_html()
    elif gg =='4':
        a =total_book[(total_book['gerne']=='sf') & (total_book['star_line']==1)]
        return a.head(10).to_html()
    elif gg == '5':
        a= total_book[(total_book['gerne']=='판타지') & (total_book['star_line']==1)]
        return a.head(10).to_html() 
    elif gg== '6':
        a= total_book[(total_book['gerne']=='역사') & (total_book['star_line']==1)]
        return a.head(10).to_html()


#FLASK_APP=flask_app flask run


