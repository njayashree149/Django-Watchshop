from django.contrib import admin
from .models import watchUploads,watches,wishlist,cart,CartItem

# Register your models here.
admin.site.register(watches)
# admin.site.register(wishlist)
admin.site.register(cart)
admin.site.register(CartItem)



class watchUploadsAdmin(admin.ModelAdmin):
    list_display=('id','name','description','price','image')
    list_filter=('name','price')
    search_fields=('name','description')


# class wishlistAdmin(admin.ModelAdmin):
#     list_display=('user','product')   
#     list_filter=('user','product') 
    

admin.site.register(watchUploads,watchUploadsAdmin)
admin.site.register(wishlist)