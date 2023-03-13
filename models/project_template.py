from odoo import models, fields


class ProjectTemplate(models.Model):
    _name = 'project.template'
    _rec_name = 'name'
    _description = 'ProjectTemplate'

    name = fields.Char()
    customer_id = fields.Many2one('res.partner', string='Customer')
    tags_ids = fields.Many2many('project.tags', string='Tags')
    company_id = fields.Many2one('res.company',
                                 default=lambda self: self.env.company,
                                 string='Company')

    project_manger_id = fields.Many2one('res.users',
                                        string='ProjectManager'
                                        , default=lambda self: self.env.user,)
    description = fields.Text()
    lable_task = fields.Char(string='Name of the tasks')

    def create_project(self):
        project = self.env['project.project'].create({
            'name': self.name,
            'partner_id': self.customer_id.id,
            'tag_ids':self.tags_ids
        })

