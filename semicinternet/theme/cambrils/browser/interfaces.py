from z3c.form import interfaces
from z3c.form.browser import checkbox

from zope import schema
from zope.interface import Interface

from semicinternet.theme.cambrils import cambrilsMessageFactory as _

from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "SEMIC Internet - Plone Theme 01" theme, this interface must be its layer
       (in theme/cambrils/viewlets/configure.zcml).
    """

class IHomepage(Interface):
    """Browser view for homepage logic"""

    def getSlideshowImages():
        """Returns a list of images to appear in a slot, these images should be width:960 and height:238
           User can customize the slideshow images, and there's a limit of 10
        """

class ICambrilsSettings(Interface):
    """Global cambrils settings. This describes records stored in the configuration 
       registry and otainable via plone.registry."""

    slideshow_folder = schema.TextLine(title=_(u"Slideshow folder"),
                                           description=_(u"help_slideshow_folder",
                                           default=u"Name of the folder containing the slideshow images."),
                                       required=True,
                                       default=u'slideshow',)

    company_name = schema.TextLine(title=_(u"Company name"),
                                       description=_(u"help_company_name",
                                       default=u"Name of the website owner."),
                                   required=False,
                                   default=u'Cambrils Park',)

    company_about_line1 = schema.TextLine(title=_(u"Company about line 1"),
                                              description=_(u"help_company_about_line1",
                                              default=u"Address or other information (line 1)."),
                                          required=False,
                                          default=u'',)

    company_about_line2 = schema.TextLine(title=_(u"Company about line 2"),
                                              description=_(u"help_company_about_line2",
                                              default=u"Address or other information (line 2)."),
                                          required=False,
                                          default=u'',)

    company_about_line3 = schema.TextLine(title=_(u"Company about line 3"),
                                              description=_(u"help_company_about_line3",
                                              default=u"Address or other information (line 3)."),
                                          required=False,
                                          default=u'',)

    company_about_line4 = schema.TextLine(title=_(u"Company about line 4"),
                                              description=_(u"help_company_about_line4",
                                              default=u"Address or other information (line 4)."),
                                          required=False,
                                          default=u'',)

    author_name = schema.TextLine(title=_(u"Website author name"),
                                     description=_(u"help_author_name",
                                     default=u"Name of your company, or website creator."),
                                 required=False,
                                 default=u'SEMIC Internet',)

    author_url = schema.TextLine(title=_(u"Website author URL"),
                                    description=_(u"help_author_url",
                                    default=u"Website URL of your company or website creator."),
                                required=False,
                                default=u'http://www.semicinternet.com',)
