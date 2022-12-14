from django.contrib import admin
from .models import Student
from .models import Course
from .models import Contactus
from .models import AttendanceImage
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Account
 
from .models import Todo


class AccountInline(admin.StackedInline):
    model = Account
    can_delete: False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin )

admin.site.register(Todo)


# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Contactus)

admin.site.register(AttendanceImage)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id', 'ImageAdmin', 'date']

admin.site.site_header='AASystem Admin'
admin.site.site_title='AAS Dashboard'
admin.site.site_url='AAS '


