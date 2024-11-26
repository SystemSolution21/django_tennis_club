from django.contrib import admin
from .views import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "firstname",
        "lastname",
        "join_date",
    )


admin.site.register(model_or_iterable=Member, admin_class=MemberAdmin)
