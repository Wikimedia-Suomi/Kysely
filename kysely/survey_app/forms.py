# survey_app/forms.py
from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    # Muutetaan usage-lomakekenttä MultipleChoiceFieldiksi,
    # jossa widget on CheckboxSelectMultiple:
    usage = forms.MultipleChoiceField(
        choices=Survey.USAGE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Rakennuksen käyttötarkoitus (monivalinta)"
    )

    class Meta:
        model = Survey
        fields = [
            # Poistettu 'building'
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
            'description': "Kohteen lyhyt kuvaus. Miksi rakennus on tärkeä?",
            'municipality': "Kunta",
            'address': "Rakennuksen osoite",
            'coordinates': "Koordinaatit (valinnainen)",
            'image': "Rakennuksen kuva (valinnainen)",
            'info_link': "Linkki verkkosivuun (valinnainen)",
            'sender_info': "Lähettäjän nimi ja yhteystiedot",
            'consent': "Annan suostumuksen julkistaa tiedot",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Jos instanssissa on usage-arvo (esim. "private,open"),
        # parsitaan se listaksi, jotta checkboxit täsmäävät:
        if self.instance and self.instance.usage:
            self.initial['usage'] = self.instance.usage.split(',')

    def clean_usage(self):
        usage_list = self.cleaned_data.get('usage', [])
        # Tallennetaan tietokantaan pilkulla erotettuna merkkijonona
        return ','.join(usage_list)

    def clean_consent(self):
        consent = self.cleaned_data.get('consent')
        if not consent:
            raise forms.ValidationError("Tietojen julkaisuun on annettava suostumus.")
        return consent

