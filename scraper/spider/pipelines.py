# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from spider.items import *
import project.models as project
import filemanager.models as files
import djangoAutoItem
from django.contrib.auth.models import User
from twisted.internet import reactor

class saveProject(object):
    def process_item(self, item, spider):
        print("save project 1 ----------\n\n\n\n")
        if type(item) == type(ProjectItem()):
            if not hasattr(item, 'author'):
                item['author']= User.objects.filter(pk=1)
            item.save()
            print(str(djangoAutoItem.SIDmap)+"----sidmap")
        return item

class saveThing(object):
    def process_item(self, item, spider):
        if type(item) == type(fileObjectItem()):
           pass
#           item.save()
        return item
