import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kme_project.settings')

import django
django.setup()

from kme.models import Vlagatelj, Raziskava

def populate():

    vlagatelji = [
        {"ime": "Akakij",
         "priimek": "Akakijevic",
         "sifra_arrs": "134l2k41",
         "email": "akakij.akakijevic@gmail.com",
         },
         {"ime": "Bozidar",
          "priimek": "Bogdanov",
          "sifra_arrs": "fhjdsa323",
          "email": "bozidar.bogdanov@gmail.com",
          },
          {"ime": "Cene",
           "priimek": "Cukjati",
           "sifra_arrs": "r32hqkr",
           "email": "cene.cukjati@gmail.com",
           }
    ]

    for vl in vlagatelji:
        dodaj_vlagatelja(vl["ime"],
                         vl["priimek"],
                         vl["sifra_arrs"],
                         vl["email"])
        print("Dodajam vlagatelja:", vl)

def dodaj_vlagatelja(ime, priimek, sifra_arrs, email):
    v = Vlagatelj.objects.get_or_create(ime=ime,
                                        priimek=priimek,
                                        sifra_arrs=sifra_arrs,
                                        email=email)[0]
    print("vlagatelj", type(v))
    v.save()
    return v

#execution time
if __name__ == '__main__':
    print("Starting population script...")
    populate()
