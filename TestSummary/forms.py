from django import forms
import time

class summary_form(forms.Form):
    remark = forms.CharField(
        required = True,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '2', 'cols': '100', 'placeholder': '备注，如修改功能点 or 哪个测试任务'}),
        label='remark',
    )
    
    test_svn = forms.CharField(
        required = True,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '10', 'cols': '100', 'placeholder': 'test svn(dailybuild->job.ini format):'}),
        label='test_svn',
    )
    
    base_svn = forms.CharField(
        required = True,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '10', 'cols': '100', 'placeholder': 'base svn(dailybuild->job.ini format):'}),
        label='base_svn',
    )
    
    new_conf_ip = forms.CharField(
        required = False,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '1', 'cols': '50', 'placeholder': '10.144.12.98'}),
        label='new_conf_ip',
    )
    
    new_conf_path = forms.CharField(
        required = False,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '1', 'cols': '50', 'placeholder': '/search/odin/daemon/summary/...'}),
        label='new_conf_path',
    )
    
    new_conf_user = forms.CharField(
        required = False,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '1', 'cols': '50', 'placeholder': 'root or guest'}),
        label='new_conf_user',
    )
    
    new_conf_passwd = forms.CharField(
        required = False,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '1', 'cols': '50', 'placeholder': '*****'}),
        label='new_conf_passwd',
    )
    
    new_data_ip = forms.CharField(
        required = False,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '1', 'cols': '50', 'placeholder': '10.144.12.98'}),
        label='new_data_ip',
    )
    
    new_data_path = forms.CharField(
        required = False,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '1', 'cols': '50', 'placeholder': '/search/odin/daemon/summary/...'}),
        label='new_data_path',
    )
    
    new_data_user = forms.CharField(
        required = False,
        max_length = None,
        widget=forms.Textarea(attrs={'rows': '1', 'cols': '50', 'placeholder': 'root or guest'}),
        label='new_data_user',
    )
    
    new_data_passwd = forms.CharField(
        required = False,
        max_length = None,
        widget = forms.Textarea(attrs={'rows': '1', 'cols': '50', 'placeholder': '*****'}),
        label = 'new_data_passwd',
    )
    

    test_item = forms.MultipleChoiceField(
        required = False,
        widget = forms.CheckboxSelectMultiple(), 
        choices = (
            ('性能测试', 'performance'),
            ('代码覆盖率', 'gcov'),
            ('DIFF对比', 'difftest')
        ),
        label = 'test_item'
    )


    test_item2 = forms.ChoiceField(
        required = False,
        choices = (
            ('performance', '性能测试'),
            ('gcov', '代码覆盖率'),
        ),
        label = 'test_item2',
    )

        
    
    
    