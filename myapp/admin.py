# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import UserProfile,UserChat,Project,GroupDiscussion 

admin.site.register(UserProfile)
admin.site.register(GroupDiscussion)
admin.site.register(UserChat)
admin.site.register(Project)
