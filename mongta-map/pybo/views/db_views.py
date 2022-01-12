import csv
from pathlib import Path

from django.http import HttpResponse

from pybo.models import Question
from django.utils import timezone
from django.contrib.auth.models import User

def save(subject, category, agency, update_date, content, url):
    user = User.objects.get(id=2)
    d = Question(author=user, subject=subject, category=category, agency=agency, update_date=update_date, content=content, create_date=timezone.now(), url=url)
    d.save()

def update(self):
    BASE_DIR = Path(__file__).resolve().parent.parent
    data = list()
    f = open(str(BASE_DIR)+"\DB.csv", 'r', encoding='utf-8-sig')
    rea = csv.reader(f)
    for row in rea:
        data.append(row)

    for d in data:
        save(d[0], d[1], d[2], d[4], d[10], d[14])

    return HttpResponse("업데이트 완료")

def delete(self):
    d = Question.objects.all()
    d.delete()
    return HttpResponse("삭제 완료")
