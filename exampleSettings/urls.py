from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'post.views.list', name='home'),
    (r'^post/(.*)/$', 'post.views.post'),

    # Examples:
    # url(r'^$', 'exampleSettings.views.home', name='home'),
    # url(r'^exampleSettings/', include('exampleSettings.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^edit/(.*)/$', 'post.views.edit'),
    (r'^create/$', 'post.views.create'),

    (r'^tag/(.*)/$', 'post.views.tag'),
    (r'^tagcloud/$', 'post.views.tagcloud' ),

    (r'^editorg/(.*)/$', 'organization.views.orgedit'),

    #Search urls
    (r'^search/', include('haystack.urls')),
    #captcha urls
    url(r'^captcha/', include('captcha.urls')),

    (r'^register/$', 'userProfile.views.register'),
    (r'^login/$', 'userProfile.views.login_user'),
    (r'^logout/$', 'userProfile.views.logout_user'),

    #preview pages for the STL files.
    (r'^thumbs/stl/(.*)', 'thumbnailer.views.stlthumb'),
    (r'^preview/stl/(.*)', 'thumbnailer.views.stlview'),
    url(r'', include('multiuploader.urls')),
    (r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

    #user profile pages
    url(r'^userProfile/', include('userProfile.urls')),
    (r'^editUser/', 'userProfile.views.edit'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


