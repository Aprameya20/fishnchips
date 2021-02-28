from django.contrib import admin
from . models import a_fleet,b_subfleet,c_wholesaler,d_retailer,e_consumer
# Register your models here.

class fleetAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(a_fleet,fleetAdmin)
admin.site.register(b_subfleet)
admin.site.register(c_wholesaler)
admin.site.register(d_retailer)
admin.site.register(e_consumer)

admin.site.site_title ='Fish n Chips ADMIN'
admin.site.site_header ="Fish n Chips Admin"
admin.site.index_title = "ADMIN Fish n Chips"