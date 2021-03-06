from django.contrib import admin
from . models import a_fleet,b_subfleet,c_wholesaler,d_retailer,e_consumer
# Register your models here.

class fleetAdmin(admin.ModelAdmin):
    list_display = ('id','fishName','quantity','lat','lon','blockchain_address')

class subfleetAdmin(admin.ModelAdmin):
    list_display = ('id','fleetid','quantity','blockchain_address')

class wholesalerAdmin(admin.ModelAdmin):
    list_display = ('id','subfleetid','quantity','blockchain_address')

class retailerAdmin(admin.ModelAdmin):
    list_display = ('id','wholesalerid', 'quantity','blockchain_address')

class consumerAdmin(admin.ModelAdmin):
    list_display = ('id','retailerid','quantity','blockchain_address')


admin.site.register(a_fleet,fleetAdmin)
admin.site.register(b_subfleet,subfleetAdmin)
admin.site.register(c_wholesaler,wholesalerAdmin)
admin.site.register(d_retailer,retailerAdmin)
admin.site.register(e_consumer,consumerAdmin)

admin.site.site_title ='Fish n Chips ADMIN'
admin.site.site_header ="Fish n Chips Admin"
admin.site.index_title = "ADMIN Fish n Chips"