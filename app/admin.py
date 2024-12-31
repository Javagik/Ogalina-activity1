from django.contrib import admin
from .models import Post, Publisher, Category, Score, Activity, UserProfile

admin.site.register(Post)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Score)
admin.site.register(Activity)
admin.site.register(UserProfile)