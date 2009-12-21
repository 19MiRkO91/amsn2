from stringview import *
from imageview import *
from menuview import *

class ContactListView:
    def __init__(self):
        self.group_ids = []



class GroupView:
    def __init__(self, core, amsn_group):
        self.uid = amsn_group.id
        self.contact_ids = set(amsn_group.contacts)
        self.icon = ImageView() # TODO: expanded/collapsed icon
        self.name = StringView() # TODO: default color from skin/settings
        self.name.appendText(amsn_group.name) #TODO: parse for smileys
        active = len(amsn_group.contacts_online)
        total = len(self.contact_ids)
        self.name.appendText("(" + str(active) + "/" + str(total) + ")")

        self.on_click = None #TODO: collapse, expand
        self.on_double_click = None
        self.on_right_click_popup_menu = GroupPopupMenu(core)
        self.tooltip = None
        self.context_menu = None


    #TODO: @roproperty: context_menu, tooltip



""" a view of a contact on the contact list """
class ContactView:
    def __init__(self, core, amsn_contact):
        """
        @type core: aMSNCore
        @type amsn_contact: aMSNContact
        """

        self.uid = amsn_contact.uid

        self.icon = amsn_contact.icon
        #TODO: apply emblem on dp
        self.dp = amsn_contact.dp.clone()
        self.dp.appendImageView(amsn_contact.emblem)
        self.name = StringView() # TODO : default colors
        self.name.openTag("nickname")
        self.name.appendStringView(amsn_contact.nickname) # TODO parse
        self.name.closeTag("nickname")
        self.name.appendText(" ")
        self.name.openTag("status")
        self.name.appendText("(")
        self.name.appendStringView(amsn_contact.status)
        self.name.appendText(")")
        self.name.closeTag("status")
        self.name.appendText(" ")
        self.name.openTag("psm")
        self.name.setItalic()
        self.name.appendStringView(amsn_contact.personal_message)
        self.name.unsetItalic()
        self.name.closeTag("psm")
        #TODO:
        def startConversation_cb(c_uid):
            core._conversation_manager.newConversation([c_uid])
        self.on_click = startConversation_cb
        self.on_double_click = None
        self.on_right_click_popup_menu = ContactPopupMenu(core, amsn_contact)
        self.tooltip = None
        self.context_menu = None

    #TODO: @roproperty: context_menu, tooltip

class ContactPopupMenu(MenuView):
    def __init__(self, core, amsncontact):
        MenuView.__init__(self)
        remove = MenuItemView(MenuItemView.COMMAND,
                              label="Remove %s" % amsncontact.account,
                              command= lambda: core._contactlist_manager.removeContactUid(amsncontact.uid))
        self.addItem(remove)

class GroupPopupMenu(MenuView):
    def __init__(self, core):
        MenuView.__init__(self)

