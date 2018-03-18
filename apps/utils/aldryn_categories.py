from datetime import datetime

from django.contrib.sites.models import Site
from django.db.models import Q, F, Count
from django.utils.translation import ugettext_lazy as _

from aldryn_newsblog.feeds import LatestArticlesFeed
from aldryn_newsblog.models import Article, Category, NewsBlogCategoriesPlugin


def custom_blog_feeds_title(self):
    return _('Posts on {}'.format(Site.objects.get_current().name))


def custom_get_categories(self, request):
    filter_ = (
        Q(article__categories=F('id')) &
        Q(article__app_config=self.app_config)
    )
    if not self.get_edit_mode(request):
        filter_ |= (
            Q(article__is_published=True) &
            Q(article__publishing_date__gte=datetime.now())
        )

    categories = Category.objects.filter(filter_).distinct().annotate(
        num_articles=Count('article'))

    return categories


LatestArticlesFeed.title = custom_blog_feeds_title
NewsBlogCategoriesPlugin.get_categories = custom_get_categories
