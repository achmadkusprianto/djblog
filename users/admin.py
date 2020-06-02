from django.contrib import admin
from .models import Profile

admin.site.site_header = "ADMIN PAGE" # merubah header default 'django administrator'
admin.site.register(Profile) #memasukkan profil ke dalam page admin


