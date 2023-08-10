from django.contrib import admin
from archive.models import Book, AudioRecording, Photograph,Document,AssociatedImage, Artifact
# Register your models here.

class AssociatedImageInline(admin.StackedInline):
    model = AssociatedImage
    extra = 1
class DocumentAdmin(admin.ModelAdmin):
    inlines = [AssociatedImageInline]
admin.site.register(Photograph,DocumentAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Artifact,DocumentAdmin)
admin.site.register(AudioRecording,DocumentAdmin)
admin.site.register(Book,DocumentAdmin)