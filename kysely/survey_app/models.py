# survey_app/models.py

from django.db import models

class Survey(models.Model):
    # Poistimme building-kentän kokonaan

    description = models.TextField(
        verbose_name="Kohteen lyhyt kuvaus. Miksi rakennus on sinulle tärkeä?",
        blank=False,
        null=False
    )

    USAGE_CHOICES = [
        ('private', 'Yksityisessä käytössä (koti, vapaa-ajan asunto)'),
        ('public',  'Julkisessa käytössä'),
        ('open',    'Rakennus on avoinna yleisölle (kahvila, museo)'),
        ('outside', 'Rakennusta voi katsoa ulkoa (kirkko, majakka, ulkomuseo)'),
        ('empty',   'Rakennus on tyhjillään'),
        ('eos',     'EOS (ei osaa sanoa)'),
    ]
    # Tallennetaan monivalinta pilkulla erotettuna merkkijonona
    usage = models.TextField(
        verbose_name="Rakennuksen käyttötarkoitus (monivalinta)",
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
        verbose_name="Rakennuksen osoite",
        blank=True,
        null=True
    )

    coordinates = models.CharField(
        max_length=100,
        verbose_name="Koordinaatit (valinnainen)",
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='survey_images/',
        verbose_name="Rakennuksen kuva (valinnainen)",
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

    # Vaihdettu CharField -> TextField, jotta lomakkeella voi olla tekstilaatikko
    sender_info = models.TextField(
        verbose_name="Lähettäjän nimi ja yhteystiedot",
        blank=False,
        null=False
    )

    consent = models.BooleanField(
        verbose_name="Annan suostumuksen julkistaa tiedot",
        default=False
    )

    def __str__(self):
        return f"Survey ID {self.id} - {self.description[:30]}"

