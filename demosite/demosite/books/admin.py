#-*- coding:utf-8 -*-
from django.contrib import admin
from demosite.books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
	#列表显示方式
	list_display = ('first_name', 'last_name', 'email')
	#字列表上方显示查询栏
	search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publisher','publication_date')
	#列表右侧显示过滤器,过滤列表中显示点内容
	list_filter = ('publication_date',) 
	#列表顶端显示逐层深入点导航条
	date_hierarchy = 'publication_date'
	#倒序排序
	ordering = ('-publication_date',)
	#自定义字段字编辑时点排列顺序,如果不想显示在编辑项目，从List删除即可
	#fields = ('title','authors','publisher','publication_date')
	#两侧多选列表，不能与fields同时使用,只能用在多对多字段，不能用 在Foreignkey字段
	#filter_horizontal = ('authors',)
	filter_vertical = ('authors',)
	#它时一个包含外键字段名称的元组，它包含的字段将被展现成文本框，而不是下拉框，可以通过放大镜图片进入窗口选择其它项
	raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book,BookAdmin)
