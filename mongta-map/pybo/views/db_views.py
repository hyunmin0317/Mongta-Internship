import csv
from pathlib import Path

from django.http import HttpResponse

from pybo.models import Question
from django.utils import timezone
from django.contrib.auth.models import User

def save(subject, content, url):
    user = User.objects.get(id=2)
    d = Question(author=user, subject=subject, content=content, create_date=timezone.now(), url=url)
    d.save()

def update(self):
    BASE_DIR = Path(__file__).resolve().parent.parent
    data = list()
    f = open(str(BASE_DIR)+"\DB.csv", 'r')
    rea = csv.reader(f)
    for row in rea:
        data.append(row)

    for d in data:
        save(d[0], d[1], d[9])

    return HttpResponse("업데이트 완료")

def delete(self):
    d = Question.objects.all()
    d.delete()
    return HttpResponse("삭제 완료")
