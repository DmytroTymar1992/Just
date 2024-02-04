from django.contrib import admin
from .models import Resume



class ResumeAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_phone', 'get_date_of_birth')

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'Імя'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Прізвище'

    def get_phone(self, obj):
        return obj.user.phone
    get_phone.short_description = 'Телефон'  

    def get_date_of_birth(self, obj):
        return obj.user.date_of_birth
    get_date_of_birth.short_description = 'Дата народження'

admin.site.register(Resume, ResumeAdmin)
