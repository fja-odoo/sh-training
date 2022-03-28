from .. import util
def migrate(cr, version):

    util.remove_menus(cr, 'training', [
        "menu_2",
        "training",
    ])

    util.remove_server_actions(cr, 'training', ["action_server"])
