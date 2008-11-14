from django.contrib import admin
from models import FreeText

admin.site.register(FreeText,
                    list_display = ('key','active'),
                    search_fields = ('key', 'content'))
