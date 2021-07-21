from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets=((None,
        {'fields':('title','content','description','slug')}
    ),
    ('Advance option',
        {
            'fields': ('author','status','published_at'),
            'classes': ('collapse',)
        }
    ))