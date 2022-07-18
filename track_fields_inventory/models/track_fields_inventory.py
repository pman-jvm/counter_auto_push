from odoo import models, fields, api


class TrackFieldsInventory(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'mail.thread']

    name = fields.Char(string='Product Name', track_visibility='always')
    sale_ok = fields.Boolean(string='Can be Sold', track_visibility='always')
    purchase_ok = fields.Boolean(string='Can be Purchased', track_visibility='always')

    # Smart Button
    active = fields.Boolean(string='Active', track_visibility='always')

    # General Information
    type = fields.Selection(string='Product Type', track_visibility='always')
    categ_id = fields.Many2one(string='Product Category', track_visibility='always')
    default_code = fields.Char(string='Internal Reference', track_visibility='always')
    barcode = fields.Char(string='Barcode', track_visibility='always')
    list_price = fields.Float(string='Sales Price', track_visibility='always')
    standard_price = fields.Float(string='Cost', track_visibility='always')
    uom_id = fields.Many2one(string='Unit of Measure', track_visibility='always')
    uom_po_id = fields.Many2one(string='Unit of Measure', track_visibility='always')
    description = fields.Text(string='Description', track_visibility='always')

    # Sales
    description_sale = fields.Text(string='Sale Description', track_visibility='always')
    available_in_pos = fields.Boolean(string='Available in PoS', track_visibility='always')
    to_weight = fields.Boolean(string='To Weigh With Scale', track_visibility='always')

    # Vendor
    description_purchase = fields.Text(string='Description for Vendors', track_visibility='always')

    # Inventory
    route_ids = fields.Many2many(string='Routes', track_visibility='always')
    sale_delay = fields.Float(string='Customer Lead Time', track_visibility='always')
    weight = fields.Float(string='Weight', track_visibility='always')
    volume = fields.Float(string='Volume', track_visibility='always')
    responsible_id = fields.Many2one(string='Responsible', track_visibility='always')
    property_stock_production = fields.Many2one(string='Production Location', track_visibility='always')
    property_stock_inventory = fields.Many2one(string='Inventory Location', track_visibility='always')
    description_pickingout = fields.Text(string='Description on Delivery Orders', track_visibility='always')
    description_pickingin = fields.Text(string='Description for Receipts', track_visibility='always')
    description_picking = fields.Text(string='Description for Internal Transfers', track_visibility='always')
    tracking = fields.Selection(string='Tracking', track_visibility='always')
    use_time = fields.Integer(string='Product Use Time', track_visibility='always')
    life_time = fields.Integer(string='Product Life Time', track_visibility='always')
    removal_time = fields.Integer(string='Product Removal Time', track_visibility='always')
    alert_time = fields.Integer(string='Product Alert Time', track_visibility='always')

    @api.onchange('list_price')
    def notif_counter_price(self):
        model_id = self.env['product.template'].search([('name', '=', self.name)])
        counter_id =self.env['res.partner'].search([('name', '=', 'Counter')]).id
        apri_id =self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
        farietz_id =self.env['res.partner'].search([('name', '=', 'Farietz')]).id
        miswanto_id =self.env['res.partner'].search([('name', '=', 'Miswanto')]).id
        if (bool(model_id)) == False:
            pass
        else:
            old_price = model_id.list_price
            new_price = self.list_price

            if new_price > old_price:
                final_price = f'{int(self.list_price):,}'
                msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini NAIK menjadi Rp' + str(final_price)
                model_id.message_post(body=msg_body, partner_ids=[counter_id, miswanto_id, farietz_id, apri_id], type='danger', message_type='notification', subtype='mail.mt_comment')
            else:
                final_price = f'{int(self.list_price):,}'
                msg_body = 'Team Counter harap segera mengganti harga barang ' + str(self.name) + ' ini TURUN menjadi Rp' + str(final_price)
                model_id.message_post(body=msg_body, partner_ids=[counter_id, miswanto_id, farietz_id, apri_id], type='danger', message_type='notification', subtype='mail.mt_comment')

    @api.onchange('barcode')
    def notif_counter_barcode(self):
        model_id = self.env['product.template'].search([('name', '=', self.name)])
        counter_id =self.env['res.partner'].search([('name', '=', 'Counter')]).id
        apri_id =self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
        farietz_id =self.env['res.partner'].search([('name', '=', 'Farietz')]).id
        miswanto_id =self.env['res.partner'].search([('name', '=', 'Miswanto')]).id
        if (bool(model_id)) == False:
            pass
        else:
            msg_body = 'Team Counter harap segera mengganti barcode barang ' + str(self.name) + ' ini menjadi ' + str(self.barcode)
            model_id.message_post(body=msg_body, partner_ids=[counter_id, miswanto_id, farietz_id, apri_id], type='danger', message_type='notification', subtype='mail.mt_comment')
