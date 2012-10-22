import csv
import os
import sys
from os.path import dirname
BASEDIR = dirname(__file__)

sys.path.append(os.path.join(BASEDIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'fiveqtest.settings'
from devotionals.models import Daily_Devotional

csv_filepathname = os.path.join(
    BASEDIR, 'devotionals/csv/programming-sample.tab')
reader = csv.reader(
    open(csv_filepathname), delimiter=',', quotechar='"')

for row in reader:
    if row[0] != 'title':
        Daily_Devotional.objects.create(title=row[0],
                                        month=row[1],
                                        day=row[2],
                                        body=row[3])
