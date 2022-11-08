
from flask import Blueprint, render_template, request

bp = Blueprint('user', __name__)


@bp.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
    # return '''당신의 책 만족도가 궁금하신가요!?\n\n 
    # 127.0.0.1:5000뒤에 /장르/가격/리뷰수를 쳐보세요!\n\n
    # 장르는 공포/스릴러:1, 추리/미스터리:2, 로맨스:3, sf:4, 판타지:5, 역사:6 입니다!!\n
    # 장르별로 추천 받고 싶다면 recommend/장르를 쳐주세요~!'''


