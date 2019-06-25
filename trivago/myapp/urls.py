from django.conf.urls import url
from rest_framework import routers
from myapp.views import SolutionViewSet, ClicksViewSet, CustomView,amenityList,ClicksList
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'solution', SolutionViewSet)
router.register(r'clicks', ClicksViewSet)

schema_view = get_swagger_view(title='Trivago User Profile API')


urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'^docs/', schema_view),
    url(r'^amenity/(?P<username>.+)/$', amenityList.as_view()),
    url(r'^clicks/(?P<username>.+)/$', ClicksList.as_view())
]

urlpatterns += router.urls