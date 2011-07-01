from urllib import quote_plus

from zope import interface, schema
from zope.component import getMultiAdapter, queryMultiAdapter, getAdapters, queryUtility
from zope.app.component.hooks import getSite
from z3c.form import form, field, button
from plone.app.z3cform.layout import FormWrapper, wrap_form
from plone.app.content.browser.foldercontents import FolderContentsView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.interfaces import IPloneSiteRoot

from semicinternet.theme.cambrils import cambrilsMessageFactory as _
from semicinternet.theme.cambrils.interfaces import IControlPanel

class ControlPanelForm(form.Form):
    fields = field.Fields(IControlPanel)
    ignoreContext = True # don't use context to get widget data
    label = "Manage sections and banners"

    @button.buttonAndHandler(_(u'Add'))
    def handleApply(self, action):
        data, errors = self.extractData()

        type_id = data['type']
        portal = getSite()
        base_url = self.context.absolute_url()
        adding_view = queryMultiAdapter((self.context, self.request), name='+')
        t = getattr(portal.portal_types, type_id, None)
        if t:
            # XXX: Added to support CMF 2.2 style add view actions
            context_state = getMultiAdapter((self.context, self.request),
                                            name='plone_context_state')
            addActionsById = dict([(a['id'], a['url'],) 
                                    for a in context_state.actions().get('folder/add', []) 
                                    if a['available'] and a['allowed']])

            # XXX: Added to support CMF 2.2 style add view actions
            if addActionsById.get(type_id, ''): # we have a non-empty URL
                url = addActionsById[type_id]
            elif adding_view and queryMultiAdapter((adding_view,
                                                    self.request),
                                                    name=t.factory):
                url = '%s/+/%s' % (base_url, t.factory)
            else:
                url = '%s/createObject?type_name=%s' % (base_url,
                                                        quote_plus(type_id))
        self.request.response.redirect(url)

class ControlPanelFormWrapper(FormWrapper, FolderContentsView):
    """ Wrapper for controlpanel layout
    """
    
    index = ViewPageTemplateFile('controlpanel_layout.pt')
    
ControlPanelView = wrap_form(ControlPanelForm, __wrapper_class=ControlPanelFormWrapper)
