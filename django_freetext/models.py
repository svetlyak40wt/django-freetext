from django.db import models
from django.utils.translation import ugettext_lazy as _

class FreeText(models.Model):
    """
    A FreeText is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(_('key'),
                           help_text=_('A unique name for this FreeText of content'),
                           blank=False, max_length=255, unique=True)
    content = models.TextField(_('content'), blank=True)
    active = models.BooleanField(_('active'), default=False)

    class Meta:
        verbose_name = _('free text')
        verbose_name_plural = _('free texts')

    def __unicode__(self):
        return u"%s" % (self.key,)

