import csv

f1 = open('booklist.csv', 'r', encoding='UTF8')
f2 = open('doglist.csv', 'r', encoding='UTF8')
f3 = open('walk.csv', 'r', encoding='UTF8')
reader1 = csv.DictReader(f1)
reader2 = csv.DictReader(f2)
reader3 = csv.DictReader(f3)

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yoloproject.settings")
import django
django.setup()

from yoloapp.models import BookList, PetList, Walk

if __name__=='__main__':
    for row in reader1:
        BookList(title=row['title'], author=row['author'], url=row['url']).save()
        print(row['title'] + 'is saved!')

    for row in reader2:
        PetList(number=row['공고번호'], imgurl=row['사진url'], date=row['접수일자'], kind=row['품종'], sex=row['성별'], area=row['발견장소'], feature=row['특징']).save()
        print(row['공고번호'] + 'is saved!')
    
    for row in reader3:
        Walk(name=row['공원명'], category=row['공원구분'], adress=row['제공기관명'], up=row['위도'], down=row['경도']).save()
        print(row['공원명'] + 'is saved!')