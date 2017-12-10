from django.contrib import admin
from jwmod.models import JwColour,JwStyle,JwBra,JwSize,JwCustomer,JwSalesBill,JwStockList

class JwColourAdmin(admin.ModelAdmin):
    list_display = ('id','colour_name','colour_type') # list

class JwStyleAdmin(admin.ModelAdmin):
    list_display = ('style_name',) # list

class JwSizeAdmin(admin.ModelAdmin):
    list_display = ('id','size_name',) # list

class JwBraAdmin(admin.ModelAdmin):
    list_display = ('style_name','colour_name','size_name','num') # list

class JwCustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_addr','customer_phone') # list

class JwSalesBillAdmin(admin.ModelAdmin):
    list_display = ('customer_name','jwbra','sale_date','sale_num') # list

class JwStockListAdmin(admin.ModelAdmin):
    list_display = ('style_name','colour_name','size_name','num','price','total','stock_date') # list

# Register your models here.
admin.site.register(JwColour,JwColourAdmin)
admin.site.register(JwStyle,JwStyleAdmin)
admin.site.register(JwSize,JwSizeAdmin)
admin.site.register(JwBra,JwBraAdmin)

admin.site.register(JwCustomer,JwCustomerAdmin)
admin.site.register(JwSalesBill,JwSalesBillAdmin)
admin.site.register(JwStockList,JwStockListAdmin)

