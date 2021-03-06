from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.

@python_2_unicode_compatible
class BaseNews(models.Model):

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    publish_date = models.DateTimeField(_('publish_date'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class News(BaseNews):


    class Meta:
        verbose_name = _('news item')
        verbose_name_plural = _('news')



class Event(BaseNews):

    start_date = models.DateTimeField(_('start_date'))
    end_date = models.DateTimeField(_('end_date'))

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
