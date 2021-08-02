from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Role, SubmissionStatus, Team
from import_export.admin import ImportExportModelAdmin

# Custom the ui of the user table
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'username', 'first_name', 'last_name']
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('email', 'first_name', 'last_name',)}),
    # )

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('speciality', 'role', 'team')}),
    )


# admin.site.register(CustomUser, CustomUserAdmin)

# @admin.register(CustomUser)
# class CustomUserImportExport(ImportExportModelAdmin):
#     pass

 
# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Team)
admin.site.register(SubmissionStatus)