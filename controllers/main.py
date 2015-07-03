import logging

from openerp import http, SUPERUSER_ID
from openerp.http import request
from openerp.addons.website_sale.controllers.main import website_sale

_logger = logging.getLogger(__name__)


class website_sale_logging(website_sale):

    @http.route()
    def shop(self, page=0, category=None, search='', **post):
        self.log(search)
        return super(website_sale_logging, self).shop(page=page, category=category, search=search, **post)

    @http.route()
    def product(self, product, category='', search='', **kwargs):
        self.log(search)
        return super(website_sale_logging, self).product(product, category=category, search=search, **kwargs)

    def log(self, search):
        if not search:
            return
        cr, uid, context, pool = request.cr, SUPERUSER_ID, request.context, request.registry
        log_obj = pool['website.search.log']
        log = log_obj.search(cr, uid, [('name', '=', search)])
        if log:
            log_obj.write(cr, uid, log[0], {'count': log_obj.read(cr, uid, log[0], ['count'])['count'] + 1})
        else:
            log_obj.create(cr, uid, {'name': search, 'count': 1})
        _logger.info('>>> searching for %s' % (search,))
