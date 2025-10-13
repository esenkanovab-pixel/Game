from django.contrib import admin
from .models import Player, Question, Session, Result

admin.site.register(Player)
admin.site.register(Question)
admin.site.register(Session)
admin.site.register(Result)
