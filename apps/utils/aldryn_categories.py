from datetime import datetime

from django.contrib.sites.models import Site
from django.db.models import Q, F, Count
from django.utils.translation import ugettext_lazy as _

from aldryn_newsblog.feeds import LatestArticlesFeed
from aldryn_newsblog.models import Article, Category, NewsBlogCategoriesPlugin


def custom_blog_feeds_title(self):
    return _('Posts on {}'.format(Site.objects.get_current().name))


def custom_get_categories(self, request):
    return Category.objects.all().annotate(num_articles=Count('article')).distinct()


LatestArticlesFeed.title = custom_blog_feeds_title
NewsBlogCategoriesPlugin.get_categories = custom_get_categories
