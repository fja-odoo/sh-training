# from odoo.addons.training.migrations import util
from .. import util



def migrate(cr, version):

    util.remove_menus(cr, 'training', [
        "menu_2",
        "menu_2_list",
    ])

    util.remove_server_actions(cr, 'training', ["action_server"])
