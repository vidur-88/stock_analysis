from django.conf.urls import patterns, url
from equity_analysis.views import E


urlpatterns = patterns('equity_analysis.views',
                       url(r'', 'blog_comments', name='get_blog_comments'),
                       )
