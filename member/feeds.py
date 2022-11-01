from django.contrib.syndication.views import Feed, Sharing
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse


class LatestPostsFeed(Feed):
    title = "My blog"
    link = ""
    description = "New posts of my blog."

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
