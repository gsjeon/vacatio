DB data for Testing
====================

Run flask shell.::

   (venv) $ flask shell

Add data.::

from vacatio.models import Post, Account, Vacation
from datetime import datetime, date
from vacatio import db

user1 = Account(name='전광석', email='rhkdtjr132@iorchard.co.kr', password='password', status=1, create_date=datetime.now())
user2 = Account(name='조영빈', email='healthat@iorchard.co.kr', password='password', status=1, create_date=datetime.now())
user3 = Account(name='홍순민', email='akoda5555@iorchard.co.kr', password='password', status=1, create_date=datetime.now())
user4 = Account(name='김범진', email='beomjin@iorchard.co.kr', password='password', status=1, create_date=datetime.now())

q1 = Post(subject='휴가신청합니다11.', content='병원 진료로 인한 휴가', create_date=datetime.now(), start_date=date(2021,12,2), end_date=date(2021,12,3), status=0, approver='전광석', account_id=1)
q2 = Post(subject='휴가신청합니다22.', content='병원 진료로 인한 휴가', create_date=datetime.now(), start_date=date(2021,12,21), end_date=date(2021,12,23), status=0, approver='전광석', account_id=2)
q3 = Post(subject='휴가신청합니다33.', content='병원 진료로 인한 휴가', create_date=datetime.now(), start_date=date(2021,12,24), end_date=date(2021,12,25), status=0, approver='전광석', account_id=3)
q4 = Post(subject='휴가신청합니다44.', content='병원 진료로 인한 휴가', create_date=datetime.now(), start_date=date(2021,12,2), end_date=date(2021,12,5), status=0, approver='전광석', account_id=4)

v1 = Vacation(total=15, used=1, account_id=1)
v2 = Vacation(total=15, used=2, account_id=2)
v3 = Vacation(total=15, used=3, account_id=3)
v4 = Vacation(total=15, used=4, account_id=4)


db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)

db.session.add(q1)
db.session.add(q2)
db.session.add(q3)
db.session.add(q4)

db.session.add(v1)
db.session.add(v2)
db.session.add(v3)
db.session.add(v4)

db.session.commit()
