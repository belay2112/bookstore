from odoo import models, fields, api
from datetime import date
import logging

_logger = logging.getLogger(__name__)  # Correct logger initialization

class BookDetails(models.Model):
    _name = 'book.details'
    _description = 'Book Details'

    author_id = fields.Char(string='Author', readonly=True)
    title = fields.Char(string='Title')
    publisher = fields.Char(string='Publisher')
    published_date = fields.Date(string='Published Date')
    book_age = fields.Integer(string='Book Age', compute='_compute_book_age')
    active = fields.Boolean(default=True)

    @api.depends('published_date')
    def _compute_book_age(self):
        for record in self:
            if record.published_date:
                record.book_age = date.today().year - record.published_date.year
            else:
                record.book_age = 0

    @api.model
    def archive_old_books(self):
        ten_years_ago = date.today().replace(year=date.today().year - 10)
        old_books = self.search([
            ('published_date', '<', ten_years_ago),
            ('active', '=', True)
        ])
        count = len(old_books)
        old_books.write({'active': False})
        _logger.info("Archived %d old books older than 10 years.", count)


