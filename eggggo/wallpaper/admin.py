from django.contrib import admin

# Register your models here.
from .models import Classify, Wall, Notice, Rate, User, Banner, Access


class ClassifyAdmin(admin.ModelAdmin):
    # 控制字段显示顺序，及分块显示
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    list_display = ('id', 'name', 'select', 'enable', 'created_at', 'updated_at')  # 显示的字段
    list_filter = ['enable']


class WallAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_id', 'publisher', 'tabs', 'score', 'description')


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'target', 'enable')


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date')


admin.site.register(Classify, ClassifyAdmin)
admin.site.register(Wall, WallAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Rate)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Access)
admin.site.register(User)
