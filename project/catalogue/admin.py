from django.contrib import admin

from catalogue.models import Project, Technology, Language, Feature

admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Language)
admin.site.register(Feature)
