from django.contrib import admin

from maps.models import ReportPDF

class ReportPDFAdmin(admin.ModelAdmin):
    pass
admin.site.register(ReportPDF, ReportPDFAdmin)
