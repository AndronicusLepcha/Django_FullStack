from django.contrib import admin
from showapp.models import Topic,Webpage,AccessRecord
#register your model here 

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)