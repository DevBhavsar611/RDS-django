from django.contrib import admin
from .models import Product, Variation, ReviewRating


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'slug', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')


class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'product', 'user', 'rating', 'status', 'updated_at')
    list_filter = ('status', 'rating', 'updated_at')
    search_fields = ('subject', 'review', 'user__email', 'product__product_name')

    def review_title(self, obj):
        return obj.subject or '(No title)'

    review_title.short_description = 'Title'


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
