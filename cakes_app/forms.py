from django import forms
from cakes_app.models import Cake

class CakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f_name, f in self.fields.items():
            f.widget.attrs["class"] = "form-control"

    class Meta:
        model = Cake
        fields = ['name', 'desciption', 'price', 'weight', 'image', 'baker']