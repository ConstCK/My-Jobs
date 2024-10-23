from django.urls import path

from .views import (ProjectsByLanguage, ProjectsByTechnology, ProjectsByFeature,
                    AllProjects, ProjectDetail, AddLanguage, AddTechnology, AddFeature,
                    AddProject, add_data, about, ProjectDelete, ProjectUpdate, successful_update, successful_delete,
                    successful_create)

urlpatterns = [
    path('', AllProjects.as_view(), name='home'),
    path('by-language/<str:name>', ProjectsByLanguage.as_view(), name='projects_by_language'),
    path('by-technology/<str:name>', ProjectsByTechnology.as_view(), name='projects_by_technology'),
    path('by-feature/<str:name>', ProjectsByFeature.as_view(), name='projects_by_feature'),
    path('add', add_data, name='add_data'),
    path('add/language', AddLanguage.as_view(), name='add_language'),
    path('add/technology', AddTechnology.as_view(), name='add_technology'),
    path('add/feature', AddFeature.as_view(), name='add_feature'),
    path('add/project', AddProject.as_view(), name='add_project'),
    path('details/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('details/<int:pk>/update', ProjectUpdate.as_view(), name='project_update'),
    path('details/<int:pk>/delete', ProjectDelete.as_view(), name='project_delete'),
    path('successful-update', successful_update, name='successful_update'),
    path('successful-delete', successful_delete, name='successful_delete'),
    path('successful-create', successful_create, name='successful_create'),
    path('about', about, name='about'),
]
