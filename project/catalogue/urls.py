from django.urls import path

from .views import (ProjectsByLanguage, ProjectsByTechnology, ProjectsByFeature,
                    AllProjects, ProjectDetail, DataView, ProjectDelete,
                    ProjectUpdate, SuccessfulUpdateView, SuccessfulDeleteView, SuccessfulCreateView,
                    FeatureDelete, TechnologyDelete, LanguageDelete, ProjectAdd, FeatureAdd,
                    TechnologyAdd, LanguageAdd, LanguageSelect, TechnologySelect, FeatureSelect,
                    AboutView)

urlpatterns = [
    path('', AllProjects.as_view(), name='home'),
    path('by-language/<str:name>', ProjectsByLanguage.as_view(), name='projects_by_language'),
    path('by-technology/<str:name>', ProjectsByTechnology.as_view(), name='projects_by_technology'),
    path('by-feature/<str:name>', ProjectsByFeature.as_view(), name='projects_by_feature'),
    path('add/language', LanguageAdd.as_view(), name='add_language'),
    path('add/technology', TechnologyAdd.as_view(), name='add_technology'),
    path('add/feature', FeatureAdd.as_view(), name='add_feature'),
    path('add/project', ProjectAdd.as_view(), name='add_project'),
    path('select/language', LanguageSelect.as_view(), name='select_language'),
    path('select/technology', TechnologySelect.as_view(), name='select_technology'),
    path('select/feature', FeatureSelect.as_view(), name='select_feature'),
    path('delete/language/<int:pk>', LanguageDelete.as_view(), name='delete_language'),
    path('delete/technology/<int:pk>', TechnologyDelete.as_view(), name='delete_technology'),
    path('delete/feature/<int:pk>', FeatureDelete.as_view(), name='delete_feature'),
    path('<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('<int:pk>/update', ProjectUpdate.as_view(), name='project_update'),
    path('<int:pk>/delete', ProjectDelete.as_view(), name='project_delete'),
    path('data-page', DataView.as_view(), name='data_page'),
    path('about', AboutView.as_view(), name='about'),
    path('successful-update', SuccessfulUpdateView.as_view(), name='successful_update'),
    path('successful-delete/<str:obj>', SuccessfulDeleteView.as_view(), name='successful_delete'),
    path('successful-create', SuccessfulCreateView.as_view(), name='successful_create')
]
