from django.contrib import admin

# Register your models here.
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date time',{'fields':['pub_date']})
    ]

class MyAdminSite(admin.AdminSite):
    site_header = 'Martin Django Admin'

admin_site = MyAdminSite(name='admin')

admin.site.register(Question,QuestionAdmin)

