from zope.interface import implements
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView

from Products.ATContentTypes.interface.folder import IATFolder

from semicinternet.theme.cambrils.browser.interfaces import IHomepage

#from zope.component import getUtility

#from plone.registry import Registry
#registry = Registry()

#from plone.registry.interfaces import IRegistry

#from plone.registry import Registry
from plone.registry.fieldfactory import persistentFieldAdapter

from semicinternet.theme.cambrils.browser.interfaces import ICambrilsSettings

#registry = getUtility(IRegistry)

#settings = registry.forInterface(ICambrilsSettings)

DEFAULT_NUMBER_OF_ITEMS = 10

class Homepage(BrowserView):
    
    implements(IHomepage)

    def __init__(self, context, request):
        super(Homepage, self).__init__(context, request)
        self.portal = getToolByName(self.context, "portal_url").getPortalObject()

    def getSlideshowImages(self,
                           folder_id,
                           num_items=DEFAULT_NUMBER_OF_ITEMS):
        urltool = getToolByName(self, 'portal_url')
        catalog = getToolByName(self, 'portal_catalog')
        section_path = urltool.getPortalPath() + '/' + folder_id

        query_result = catalog({'Type':{'query':['Image','ATImage']},
                                'path':{'query':section_path,'level':0},
                              })[:num_items]

        if query_result:
            return [brain.getObject() for brain in query_result]
        else:
            return False

    def getSlideshowImageItems(self,
                               folder_id):
        urltool = getToolByName(self, 'portal_url')
        catalog = getToolByName(self, 'portal_catalog')
        section_path = urltool.getPortalPath() + '/' + folder_id
        query_result = catalog({'Type':{'query':['Image','ATImage']},
                                'path':{'query':section_path,'level':0},
                              })
        if query_result:
            return len(query_result)
        else:
            return False

    #def getFooterCopyright(self):
    #    settings = registry.forInterface(ICambrilsSettings)
    #    return self.settings.author_name
        
