from django.contrib import admin

from catalogue.models import Project, Technology, Language, Feature, Link

admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Language)
admin.site.register(Feature)
admin.site.register(Link)
