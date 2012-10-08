# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from devotionals.models import Daily_Devotional


def get_devotional(request, day, month):
    """  """
    obj = Daily_Devotional.objects.filter(day=day).filter(month=month)
    if obj:
        obj = obj[0]
    else:
        obj = None
    return render_to_response(
        'home.html',
        {'obj': obj},
        context_instance=RequestContext(request))


def get_devotional_num_words(request, day, month):
    """  """
    obj = Daily_Devotional.objects.filter(day=day).filter(month=month)
    if obj:
        obj = obj[0]
    else:
        obj = None
    return render_to_response(
        'num_words.html',
        {'obj': obj, 'num_words': len(obj.body.split())},
        context_instance=RequestContext(request))
