from django.contrib import admin
from .models import Notes
from django.contrib.auth.models import User

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at', 'updated_at', 'user')
    search_fields = ('title', 'text')
    list_filter = ('user',)

    def queryset(self, request):
        qs = super().queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(Notes, NotesAdmin)