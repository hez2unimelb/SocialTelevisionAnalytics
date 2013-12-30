from django_tables2.utils import A
import django_tables2 as tables 
from models import Program
class ProgramTable(tables.Table):
    name = tables.LinkColumn('program_detail', args=[A('pk')])
    class Meta:
        model = Program
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}