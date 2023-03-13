from odoo import models, fields


class ProjectInherit(models.Model):
    _inherit = 'project.project'
    _description = 'Project_inherit'

    def create_template(self):
        project = self.env['project.template'].create({
            'name': self.name,
            'customer_id': self.partner_id.id,
            'tags_ids': self.tag_ids
        })


