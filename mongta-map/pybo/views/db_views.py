import csv
from pathlib import Path

from django.http import HttpResponse

from pybo.models import Question
from django.utils import timezone
from django.contrib.auth.models import User

def save(subject, content, data_format):
    user = User.objects.get(id=1)
    d = Question(author=user, subject=subject, content=content, create_date=timezone.now(), data_format=data_format)
    d.save()

def update(self):
    BASE_DIR = Path(__file__).resolve().parent.parent
    data = list()
    f = open(str(BASE_DIR)+"\DB.csv", 'r')
    rea = csv.reader(f)
    for row in rea:
        data.append(row)

    for d in data:
        save(d[0], d[1], d[4])

    return HttpResponse("업데이트 완료")