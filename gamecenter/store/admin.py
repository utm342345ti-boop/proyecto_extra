from django.contrib import admin
from .models import Category, Product, ProviderSubmission, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display=('name',)

class productAdmin(admin.ModelAdmin):
        prepopulated_fields={'slug':("name",)}
        list_display=('name','category','price','stock')
        list_filter=('category',)
        search_fields=('name','descrption')

class providerSubmissionAdemin(admin.ModelAdmin):
      list_display=('provider_name','created_at')

class CommentAdmin(admin.ModelAdmin):
      list_display=('author_name','product','created_at','approved')
      list_filter=('approved','created_at')
      actions=['approve_coments']

      def approve_coments(self, request, queryset):
            queryset.update(approved=True)
            approve_comments.short_description="aprovar comentrios selecionados"

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,productAdmin)
admin.site.register(ProviderSubmission,providerSubmissionAdemin)
admin.site.register(Comment,CommentAdmin)