from django.contrib import admin

# Register your models here.
from groups.models import Groups, GroupSubject

admin.site.register(Groups)
admin.site.register(GroupSubject)