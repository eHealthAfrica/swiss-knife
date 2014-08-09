from django.db import models

class ReportPDF(models.Model):
    pdf_file = models.FileField(upload_to='media/pdf/')
    timestamp = models.DateTimeField(auto_now_add=True)

