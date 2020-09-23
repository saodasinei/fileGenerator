from django.contrib import admin
from DB.models import File, Profile, PartTimer, UploadList, UploadFile


# Register your models here.

# class FileAdmin(admin.ModelAdmin):
    # fields = ('title', 'content')
    # fieldsets = (
    #     ['Main', {
    #         'fields': ('name', 'content'),
    #     }],
    #     ['Advance', {
    #         'classes': ('collapse',),
    #         'fields': ('age',),
    #     }]
    # )

#
# admin.site.register(File, FileAdmin)
admin.site.register([File, Profile, PartTimer, UploadList, UploadFile])
