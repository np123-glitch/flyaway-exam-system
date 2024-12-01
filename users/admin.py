from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_student', 'is_teacher', 'is_hod', 'is_staff')
    list_filter = ('is_student', 'is_teacher', 'is_hod', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('is_student', 'is_teacher', 'is_hod')}),
    )
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(StudentRequest)
admin.site.register(Teacher)
admin.site.register(TeacherRequest)
