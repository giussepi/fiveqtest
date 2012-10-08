# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Daily_Devotional(models.Model):
    MONTHS = (
        ('1', 'jan'),
        ('2', 'feb'),
        ('3', 'mar'),
        ('4', 'apr'),
        ('5', 'may'),
        ('6', 'jun'),
        ('7', 'jul'),
        ('8', 'ago'),
        ('9', 'sep'),
        ('10', 'oct'),
        ('11', 'nov'),
        ('12', 'dic'),
    )
    DAYS = tuple([(str(i), str(i)) for i in xrange(1, 32)])
    """ stores daily devotionals """
    title = models.CharField(max_length=255)
    month = models.CharField(max_length=3, choices=MONTHS)
    day = models.CharField(max_length=2, choices=DAYS)
    body = models.TextField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title


def import_csv():
    """loads the csv file into the db"""
    import csv
    import os
    csv_filepathname = os.path.join(
        settings.BASEDIR, '../devotionals/csv/programming-sample.tab')
    reader = csv.reader(
        open(csv_filepathname), delimiter=',', quotechar='"')
    for row in reader:
        if row[0] != 'title':
            Daily_Devotional.objects.create(title=row[0],
                                            day=row[1],
                                            month=row[2],
                                            body=row[3])
