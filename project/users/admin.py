from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Documents, Presentation, Video, Metodics, Contest


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('user_permissions', 'groups', 'date_joined', 'last_login')


admin.site.register(Documents)
admin.site.register(Presentation)
admin.site.register(Video)
admin.site.register(Metodics)
admin.site.register(Contest)
