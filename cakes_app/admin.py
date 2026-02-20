from django.contrib import admin
from django.db.models import Count
from cakes_app.models import Baker, Cake

# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return Baker.objects.filter(user=request.user).exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, object=None):
        return object and request.user == object.baker.user

    def has_view_permission(self, request, object=None):
        return Baker.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        baker = Baker.objects.filter(user=request.user).first()
        b_cakes = Cake.objects.filter(baker=baker).all()

        if b_cakes.count() == 10:
            return

        sum = 0
        for cake in b_cakes:
            sum += cake.price

        if not change and sum + obj.price >= 10000:
            return

        old_obj = Cake.objects.filter(id=obj.id).first()
        if change and sum + obj.price - old_obj.price >= 10000:
            return

        for cake in Cake.objects.all():
            if cake.name == obj.name:
                return

        if not change:
            obj.baker = baker
        obj.save()
        super().save_model(request, obj, form, change)

class BakerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(BakerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cake_count=Count('cakes')).filter(cake_count__lt=5)

admin.site.register(Baker, BakerAdmin)
admin.site.register(Cake, CakeAdmin)