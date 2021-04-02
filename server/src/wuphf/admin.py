from django.contrib import admin
from wuphf.models import WuphfReceiver, Wuphf


site_name = "WUPHF.com"
admin.site.site_header = site_name
admin.site.site_title = site_name
admin.site.index_title = site_name


@admin.register(WuphfReceiver)
class WuphfReceiverAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Wuphf)
class WuphfAdmin(admin.ModelAdmin):
    list_display = ['message',]
