# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='',
        help_text='請依照 "公司名稱_檔名" 命名 , 已加速審核謝謝! (大小上限 : 42 megabytes)'
    )