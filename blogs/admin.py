from django.contrib import admin

# Register your models here.
from . import models

# class ChoiceInline(admin.StackedInline):#默认的情况下是占用空间很大
class ChoiceInline(admin.TabularInline):#是一种表格式
    model = models.Entry
    extra = 1 #表示默认情况下另外显示的三个空的添加项

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name label',{'fields':['name','pub_time']}),
        ('tagline',{'fields':['tagline'],'classes': ['collapse']})
    ]
    inlines = [ChoiceInline] #用在 含有foreignkey的表格中

    #默认地，Django显示每个对象的str()返回的内容。
    # 但有时如果我们能显示个别的字段将很有帮助。 我们使用list_display
    # 选项来实现这个功能，它是一个要显示的字段名称的元组，在对象的变更列表页面上作为列显示
    list_display = ('name', 'tagline','was_xiaoming') # was_xiaoming是一个函数
                                                        # 这个函数可以在models里面 添加自定义属性

    # list_filter = ['pub_time'] #可以添加一个筛选的小面板
    # 这行代码添加一个“Filter”侧边栏，可以使人们通过pub_date字段对变更列表进行过滤：
    list_filter = ['tagline','pub_time'] #可以添加一个筛选的小面板



admin.site.register(models.Blog,BlogAdmin)
# admin.site.register(models.Entry)