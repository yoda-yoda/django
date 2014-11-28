from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import HelloTemplate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'naxxserian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/', 'article.views.hello'),
	url(r'^hello_template_simple/', 'article.views.hello_template_simple'),
	url(r'^hello_template/', 'article.views.hello_template'),
	url(r'^hello_class/', HelloTemplate.as_view()),

	#tell amin project the urls file
	(r'^articles/', include('article.urls'),
)
