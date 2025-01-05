from django.contrib import admin
from apps.main.models import Main, Over, Awards, About
from django.utils.html import format_html
# Register your models here.

admin.site.register(Main)
admin.site.register(Over)


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    fields = ['image']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height = "50px" />'.format(obj.image.url))
    
    # fields = ['image_tag']
    list_display = ("image_tag",)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    def video_tag(self, obj):
        return format_html('<video src="{}" width="auto" height = "50px" />'.format(obj.video.url))

    list_display = ('title', 'description', 'video_tag')