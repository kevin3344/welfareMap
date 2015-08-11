from django import forms
from welfare.models import Welfare


URGENT = (('普通','普通'),
          ('困難','困難'),
          ('緊急','緊急'),
          )

HELPTYPE = (('勞力','勞力'),
            ('智力','智力'),
            ('金錢','金錢'),
            )

class WelfareForm(forms.ModelForm):
    address = forms.CharField(label='地址')
    content = forms.CharField(label='內容') 
    note = forms.CharField(label='備註') 
    urgent = forms.ChoiceField(label='緊急程度', choices=URGENT) 
    helpType = forms.ChoiceField(label='求救類型', choices=HELPTYPE)
   
    class Meta:
        model = Welfare
        fields = ('address', 'content', 'note', 'urgent', 'helpType')
    