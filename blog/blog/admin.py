from django.contrib import admin

from blog.models import Tag, Post


# a subclass of admin.ModelAdmin must be created. This subclass’s attributes determine how the model is displayed
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "published_at")


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
