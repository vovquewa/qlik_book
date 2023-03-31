from django.contrib import admin
from .models import App, AppObject, User, UserAppObject, Department
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


class UserAppObjectInline(admin.TabularInline):
    model = UserAppObject
    min_num = 1
    extra = 0


class AppObjectAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("name", "qlik_object_id", "app", "users_custom")
    list_filter = ("name", "app__name")
    search_fields = ("name", "qlik_object_id")
    empty_value_display = "-пусто-"
    ordering = ("name",)
    inlines = [UserAppObjectInline]

    def users_custom(self, obj):
        return ", ".join([str(p) for p in obj.users.all()])
    users_custom.short_description = "Пользователи"


class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
        "username",
        "department",
        "app_objects_custom",
    )
    list_filter = ("username", "department__name")
    search_fields = ("username", "department__name")
    empty_value_display = "-пусто-"
    ordering = ("username",)
    inlines = [UserAppObjectInline]

    def app_objects_custom(self, obj):
        return ", ".join([str(p) for p in obj.app_object.all()])


class UserAppObjectResource(resources.ModelResource):
    user = fields.Field(
        column_name="user",
        attribute="user",
        widget=ForeignKeyWidget(User, "username"),
    )
    app_object = fields.Field(
        column_name="app_object",
        attribute="app_object",
        widget=ForeignKeyWidget(AppObject, "qlik_object_id"),
    )

    class Meta:
        model = UserAppObject


class UserAppObjectAdmin(ImportExportModelAdmin, ExportActionMixin):
    resource_class = UserAppObjectResource
    list_display = (
        "user",
        "app_object",
        "app_object_custom",
    )
    list_filter = (
        "user__username",
        "app_object__name",
    )
    search_fields = (
        "user__username",
        "app_object__name",
    )
    empty_value_display = "-пусто-"
    ordering = ("user", "app_object")

    def app_object_custom(self, obj):
        return obj.app_object.qlik_object_id


class AppAdmin(admin.ModelAdmin):
    list_display = ("name", "qlik_app_id")
    list_filter = ("name",)
    search_fields = ("name", "qlik_app_id")
    empty_value_display = "-пусто-"
    ordering = ("name",)


admin.site.register(App, AppAdmin)
admin.site.register(AppObject, AppObjectAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserAppObject, UserAppObjectAdmin)
admin.site.register(Department)
