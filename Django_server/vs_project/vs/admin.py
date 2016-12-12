# WGG batteries-included, admin interface
from django.contrib import admin

#WGG  category and page models
from vs.models import UserProfile, PointOfInterest

# WGG Register models with the admin interface
admin.site.register(UserProfile)
class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'position_map',)

    def position_map(self, instance):
        if instance.position is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?key=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.position.latitude,
                'longitude': instance.position.longitude,
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }
    position_map.allow_tags = True


admin.site.register(PointOfInterest, PointOfInterestAdmin)
#admin.site.register(PointOfInterest)


