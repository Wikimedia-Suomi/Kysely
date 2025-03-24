# survey_app/models.py

from django.db import models

class Survey(models.Model):
    description = models.TextField(
        verbose_name="Kohteen lyhyt kuvaus. Miksi kohde on sinulle tärkeä?",
        blank=False,
        null=False
    )

    USAGE_CHOICES = [
        ('private',  'Yksityisessä käytössä (koti, vapaa-ajan asunto, piha tms.)'),
        ('public',   'Julkisessa käytössä'),
        ('open',     'Kohde on avoinna yleisölle (kahvila, asuinalue, puisto tms.)'),
        ('outside',  'Kohdetta voi katsoa ulkoa'),
        ('empty',    'Rakennus on tyhjillään'),
        ('eos',      'EOS (ei osaa sanoa)'),
    ]
    usage = models.TextField(
        verbose_name="Kohteen käyttötarkoitus (monivalinta)",
        blank=True,
        null=True
    )
    municipality = models.CharField(
        max_length=100,
        verbose_name="Kunta",
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=200,
        verbose_name="Kohteen katuosoite",
        blank=True,
        null=True
    )
    coordinates = models.CharField(
        max_length=100,
        verbose_name="Koordinaatit tai paikkalinkki karttaan (valinnainen)",
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='survey_images/',
        verbose_name="Kuva kohteesta",
        blank=True,
        null=True
    )
    image_copyright = models.CharField(
        max_length=200,
        verbose_name="Kuvan tekijänoikeustiedot (valinnainen)",
        blank=True,
        null=True
    )
    info_link = models.URLField(
        verbose_name="Linkki verkkosivuun (valinnainen)",
        blank=True,
        null=True
    )
    sender_info = models.TextField(
        verbose_name="Lähettäjän nimi ja yhteystiedot (ei julkaista)",
        blank=False,
        null=False
    )
    consent = models.BooleanField(
        verbose_name="Annan suostumuksen julkistaa tiedot",
        default=False
    )

    def __str__(self):
        return f"Survey ID {self.id} - {self.description[:30]}"

