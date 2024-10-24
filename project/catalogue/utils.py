from .models import Language, Technology, Feature, Project


# Миксин для добавления в контекст данных из БД (Languages, Technologies, Features)
# и заголовка для шаблона
class CategoriesMixin:
    @staticmethod
    def get_user_context(**kwargs):
        context = kwargs
        languages = Language.objects.all().order_by('name')
        technologies = Technology.objects.all().order_by('name')
        features = Feature.objects.all().order_by('name')
        context['languages'] = languages
        context['technologies'] = technologies
        context['features'] = features
        return context


# Миксин для DRY записи в class-based представлениях (Убираем дублирование кода)
class ProjectsDataMixin:
    model = Project
    template_name = 'main.html'
    context_object_name = 'projects'
    ordering = ['languages', 'technologies', 'features', 'created_at']
