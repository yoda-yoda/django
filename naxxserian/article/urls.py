from django.confs.urls import patterns, url, include

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'naxxserian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^all/', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/', 'article.views.article'),

)