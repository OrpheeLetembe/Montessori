from django.contrib import admin


from .models import Environment


class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year',)


admin.site.register(Environment, EnvironmentAdmin)
