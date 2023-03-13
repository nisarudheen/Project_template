from odoo import models,fields


class TaskInherit(models.Model):
    _inherit = 'project.task'
    _description = 'ProjectTask'

    def create_template(self):
        task = self.env['task.template'].create({
            'name': self.name,
            'customer_id': self.partner_id.id,
            'project_id': self.project_id.id,
            'tags_ids': self.tag_ids,
            'deadline': self.date_deadline,
            'sale_order_item': self.sale_line_id,
        })