from django.core.management.base import BaseCommand
from subprocess import Popen
import os.path, os
import datetime

from maps.models import ReportPDF

class Command(BaseCommand):
    help = """Generates a PDF with a map of incidents from the last day"""

    def handle(self, *args, **options):
        self.generate(*args)

    def generate(self, *args):
        current_dir = os.getcwd()
        this_dir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(this_dir+'/renderPDF')
        timestamp = str(datetime.datetime.now())
        p = Popen(['./renderPDF http://54.220.157.69/ /tmp/'+timestamp], shell=True)
        p.wait()
        os.chdir(current_dir)
        pdf = ReportPDF(pdf_file='/tmp'+timestamp)
        pdf.save()
        print "PDF created"