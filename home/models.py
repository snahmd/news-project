from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtailtrans.models import TranslatablePage


class TransHomePage(TranslatablePage):
    body = RichTextField(blank=True, default="")

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class TransLandingPage(TranslatablePage):

    body = RichTextField(blank=True, default="")

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]