from django.contrib import admin

# Register your models here.

from .models import StoreInformation


class StoreInformationAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['brand'], 'fields': ['code']}),
    #     ('Date information', {'fields': ['Name'], 'fields': ['address']}),
    #     ('Date information', {'fields': ['ip'], 'fields': ['ap']}),
    #     (None, {'fields': ['contacts']}),
    #     ('Date information', {'fields': ['equipment_arrival_date'], 'fields': ['completion_date'], 'fields':
    #         ['expected_installation_date'], 'fields': ['Opening_date']}),
    #     (None, {'fields': ['engineering_head']}),
    #     (None, {'fields': ['firewall_type'], 'fields': ['status']}),
    #     (None, {'fields': ['ps']})
    # ]
    fields = (('brand', 'code'),
              ('name', 'address'),
              'contacts',
              ('equipment_arrival_date', 'completion_date'),
              ('expected_installation_date', 'Opening_date'),
              'engineering_head',
              ('firewall_type', 'ip', 'ap'),
              'status',
              'ps')
    list_display = ('code', 'name', 'ip', 'engineering_head', 'status', 'Opening_date', 'equipment_arrival_date',)
    date_hierarchy = 'Opening_date'
    empty_value_display = '-empty-'
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-Opening_date',)

    # list_editable 设置默认可编辑字段
    # list_editable = ['machine_room_id', 'temperature']
    list_filter = ('status',)  # 过滤器
    search_fields = ('code', 'name')  # 搜索字段


admin.site.site_header = '店铺管理'
admin.site.site_title = '店铺管理系统'
admin.site.register(StoreInformation, StoreInformationAdmin)


