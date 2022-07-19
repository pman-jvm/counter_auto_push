from odoo import models, fields, api


class InventoryPushNotification(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'mail.thread']

    # Mengepush Notif Sales Price
    @api.onchange('list_price')
    def notif_counter_price_no(self):
        model_id = self.env['product.template'].search([('name', '=', self.name)])
        counter_id =self.env['res.partner'].search([('name', '=', 'Counter')]).id
        apri_id =self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
        # farietz_id =self.env['res.partner'].search([('name', '=', 'Farietz')]).id
        warehouse_id =self.env['res.partner'].search([('name', '=', 'Warehouse')]).id
        if (bool(model_id)) == False:
            pass
        else:
            old_price = model_id.list_price
            new_price = self.list_price

            if new_price > old_price:
                final_price = f'{int(self.list_price):,}'
                msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini NAIK menjadi Rp' + str(final_price)
                model_id.message_post(body=msg_body, partner_ids=[counter_id, warehouse_id, apri_id], type='danger', message_type='notification', subtype='mail.mt_comment')
            else:
                final_price = f'{int(self.list_price):,}'
                msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini TURUN menjadi Rp' + str(final_price)
                model_id.message_post(body=msg_body, partner_ids=[counter_id, warehouse_id, apri_id], type='danger', message_type='notification', subtype='mail.mt_comment')

    # Mengepush Notif Barcode
    @api.onchange('barcode')
    def notif_counter_barcode(self):
        model_id = self.env['product.template'].search([('name', '=', self.name)])
        counter_id =self.env['res.partner'].search([('name', '=', 'Counter')]).id
        apri_id =self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
        # farietz_id =self.env['res.partner'].search([('name', '=', 'Farietz')]).id
        warehouse_id =self.env['res.partner'].search([('name', '=', 'Warehouse')]).id
        if (bool(model_id)) == False:
            pass
        else:
            msg_body = 'Team Counter & Warehouse harap segera mengganti barcode barang ' + str(self.name) + ' ini menjadi ' + str(self.barcode)
            model_id.message_post(body=msg_body, partner_ids=[counter_id, warehouse_id, apri_id], type='danger', message_type='notification', subtype='mail.mt_comment')











    # Mengepush Notif menggunakan to-do
    # @api.onchange('list_price')
    # def notif_counter_price(self):
    #     counter_id = self.env['res.partner'].search([('name', '=', 'Counter')]).id
    #     product_id = self.env['product.template'].search([('name', '=', self.name)]).id
    #
    #     data = {
    #         'res_id': product_id,
    #         'res_model_id': 159,
    #         # 'res_model_id': self.env['ir.model'].search([('model', '=', 'product.template')]).id,
    #         'user_id': 7,
    #         'summary': 'Team Counter - Update Harga',
    #         'note' : 'harap melakukan update harga barang ' + self.name,
    #         'activity_type_id': 4,
    #         'date_deadline': '07/20/2022'
    #     }
    #
    #     self.env['mail.activity'].create(data)