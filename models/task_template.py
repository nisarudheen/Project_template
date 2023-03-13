from odoo import models, fields


class TaskTemplate(models.Model):
    _name = 'task.template'
    _description = 'TaskTemplate'

    name = fields.Char()
    customer_id = fields.Many2one('res.partner', string='Customer')
    tags_ids = fields.Many2many('project.tags', string='Tags')
    company_id = fields.Many2one('res.company',
                                 default=lambda self: self.env.company,
                                 string='Company')
    sale_order_item = fields.Many2one('sale.order.line')
    project_id = fields.Many2one('project.project', string='Project')
    deadline = fields.Date(string='Deadline')
    description = fields.Char(string='Discription')
    assignees = fields.Many2one('res.users',string='Assignees', default=lambda self: self.env.user)

    def create_task(self):
        task = self.env['project.task'].create({
            'name': self.name,
            'partner_id': self.customer_id.id,
            'project_id': self.project_id.id,
            'tag_ids': self.tags_ids,
            'date_deadline': self.deadline,
            'sale_line_id': self.sale_order_item.id,
        })
