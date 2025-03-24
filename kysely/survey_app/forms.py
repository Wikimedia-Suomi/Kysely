# survey_app/forms.py
from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    usage = forms.MultipleChoiceField(
        choices=Survey.USAGE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Kohteen käyttötarkoitus (monivalinta)"
    )

    class Meta:
        model = Survey
        fields = [
            'description',
            'usage',
            'municipality',
            'address',
            'coordinates',
            'image',
            'image_copyright',
            'info_link',
            'sender_info',
            'consent',
        ]
        labels = {
            'description': "Kohteen lyhyt kuvaus. Miksi kohde on sinulle tärkeä?",
            'municipality': "Kunta",
            'address': "Kohteen katuosoite",
            'coordinates': "Koordinaatit tai paikkalinkki karttaan (valinnainen)",
            'image': "Kuva kohteesta",
            'info_link': "Linkki verkkosivuun (valinnainen)",
            'sender_info': "Lähettäjän nimi ja yhteystiedot (ei julkaista)",
            'consent': "Annan suostumuksen julkistaa tiedot",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.usage:
            self.initial['usage'] = self.instance.usage.split(',')

    def clean_usage(self):
        usage_list = self.cleaned_data.get('usage', [])
        return ','.join(usage_list)

    def clean_consent(self):
        consent = self.cleaned_data.get('consent')
        if not consent:
            raise forms.ValidationError("Tietojen julkaisuun on annettava suostumus.")
        return consent

