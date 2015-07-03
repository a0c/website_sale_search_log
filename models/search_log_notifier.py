from openerp import models
from openerp.api import Environment


class search_log_notifier(models.TransientModel):
    _name = 'search.log.notifier'

    def process_search_log(self, cr, uid, context=None):
        env = Environment(cr, uid, context=context or {})
        logs = env['website.search.log'].search([])
        if not logs:
            return

        template = env.ref('website_sale_search_log.search_log_email')
        template = template.with_context(lang=env['res.users'].browse(uid).lang, logs=[l.log for l in logs])
        template.send_mail(logs[0].id, force_send=True, raise_exception=True)

        logs.unlink()