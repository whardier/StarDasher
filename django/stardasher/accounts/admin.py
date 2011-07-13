from django.contrib import admin

from stardasher.accounts.models import Account, UserProfile

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'date_modified')

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, admin.ModelAdmin)

