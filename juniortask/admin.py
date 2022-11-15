from django.contrib import admin
from juniortask.models import Author, Note

class Author_admin(admin.ModelAdmin):
    list_display = ( 'full_name','date_birth')

admin.site.register(Author,Author_admin)


class Note_admin(admin.ModelAdmin):
    list_display=( 'author_name','content')

    def author_name(self,obj):
        return obj.author.full_name

admin.site.register(Note,Note_admin)
