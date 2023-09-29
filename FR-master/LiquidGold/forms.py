from django import forms
from django.forms import ModelForm
from .models import DeiselReport, Engineer, Site, SiteReport, DieselRequests, FuelTopUp




class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ('name','sudo_name','current_fuel_level')


class FuelForm(ModelForm):
    class Meta:
        model = FuelTopUp
        fields = ('site','fuel_level_before_top_up','fuel_level_after_top_up','generator_run_hours','litres','litres')
       

class DieselReportForm(ModelForm):
    class Meta:
        model = DeiselReport
        fields = ('date_created', 'actual_remaining_litres')
        
class SiteReportForm(ModelForm):
    class Meta:
        model = SiteReport 
        fields = ('date_created',  'current_fuel_level', 'last_delivery_date', 'last_delivery_quantity')
  
       
        
class NewRequestForm(ModelForm):
    class Meta:
        model = DieselRequests
        fields = (
            
            'site',
            'engineer',
            'manager',
            'phcn_comment',
            'quantity_required',
            'justification')   
        
        read_only_fields =()
     
     
# class DieselRequestForm(ModelForm):
#     class Meta:
        
#         model = DieselRequests
#         fields = '__all__'