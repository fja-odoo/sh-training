def remove_data(cr, module, model, names):
    cr.execute(
        """
            DELETE
                FROM ir_model_data
                WHERE module = %s
                AND model = %s
                AND name IN %s
            RETURNING res_id
    """,
        [module, model, tuple(names)],
    )
    return cr.fetchone()

def remove_menus(cr, module, names):
    ids = remove_data(cr, module, "ir.ui.menu", names)
    cr.execute(
        """
        WITH RECURSIVE tree(id) AS (
            SELECT id
              FROM ir_ui_menu
             WHERE id IN %s
             UNION
            SELECT m.id
              FROM ir_ui_menu m
              JOIN tree t ON (m.parent_id = t.id)
        )
        DELETE FROM ir_ui_menu m
              USING tree t
              WHERE m.id = t.id
          RETURNING m.id
    """,
        [tuple(ids)],
    )

def remove_server_actions(cr, module, names):
    ids = remove_data(cr, module, "ir.actions.server", names)
    cr.execute('DELETE FROM ir_actions WHERE id IN %s', [tuple(ids)])
