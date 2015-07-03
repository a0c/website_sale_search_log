from openerp import api, models, fields


class website_search_log(models.Model):
    _name = 'website.search.log'
    _description = 'Website Search Log'
    _order = 'name'

    name = fields.Char(size=256)
    count = fields.Integer()
    log = fields.Text(compute='compute_log')

    @api.one
    @api.depends('name', 'count')
    def compute_log(self):
        self.log = '%s (x %s)' % (self.name, self.count) if self.count > 1 else self.name
