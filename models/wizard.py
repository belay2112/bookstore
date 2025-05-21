from odoo import models, fields

class CreateAuthorWizard(models.TransientModel):
    _name = 'create.author.wizard'
    _description = 'Create Author Wizard'

    name = fields.Char(string="Author Name", required=True)

    def action_create_author(self):
        self.env['book.details'].create({'author_id': self.name})
