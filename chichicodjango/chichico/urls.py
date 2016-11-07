from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^press/$', TemplateView.as_view(template_name='press.html'), name='press'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^media/$', TemplateView.as_view(template_name='media.html'), name='media'),
    url(r'^links/$', TemplateView.as_view(template_name='links.html'), name='links'),
    url(r'^faq/$', TemplateView.as_view(template_name='faq.html'), name='faq'),
    url(r'^calendar/$', TemplateView.as_view(template_name='calendar.html'), name='calendar'),
    url(r'^volunteer/$', views.volunteer),
    url(r'^request/$', views.request_view),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

)

