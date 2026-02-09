from django.contrib import admin
from .models import BinaryVarity, BinaryReview, Student, Certificate

# Register your models here.

class BinaryReviewInLine(admin.TabularInline):
    model = BinaryReview
    extra = 2

class BinaryVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')              
    inlines = [BinaryReviewInLine]

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('binary_varieties',)       # 'binary_varieties' from models.py -> class Student -> line 45 

class BinaryCertificateAdmin(admin.ModelAdmin):
    list_display = ('binary', 'certificate_number')


admin.site.register(BinaryVarity, BinaryVarietyAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Certificate, BinaryCertificateAdmin)
