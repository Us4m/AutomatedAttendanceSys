from django.contrib import admin
from .models import Student
from .models import Course
from .models import Contactus
from .models import AttendanceImage


from .models import Todo

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


