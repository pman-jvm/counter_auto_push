from odoo import models, api


class InventoryPushNotification(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'mail.thread']

    @api.multi
    def write(self, new_changes):
        master_product = self.env['product.template'].search([('name', '=', self.name)])
        counter_id = self.env['res.partner'].search([('name', '=', 'Counter')]).id
        apri_id = self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
        warehouse_id = self.env['res.partner'].search([('name', '=', 'Warehouse')]).id

        # Notifikasi pesaan mengganti harga
        if new_changes.get('list_price'):
            old_price = master_product.list_price
            new_price = int(new_changes["list_price"])
            if new_price > old_price:
                final_price = f'{new_price:,}'
                msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini NAIK menjadi Rp' + str(final_price)
                master_product.message_post(body=msg_body, partner_ids=[counter_id, apri_id, warehouse_id], message_type='notification', subtype='mail.mt_comment')
            else:
                final_price = f'{new_price:,}'
                msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini TURUN menjadi Rp' + str(final_price)
                master_product.message_post(body=msg_body, partner_ids=[counter_id, apri_id, warehouse_id], message_type='notification', subtype='mail.mt_comment')

        # Notifikasi pesaan mengganti barcode
        if new_changes.get('barcode'):
            old_barcode = master_product.barcode
            new_barcode = str(new_changes["barcode"])
            if old_barcode != new_barcode:
                msg_body = 'Team Counter & Warehouse harap segera mengganti barcode ' + str(self.name) + ' ini menjadi ' + str(new_barcode)
                master_product.message_post(body=msg_body, partner_ids=[counter_id, apri_id, warehouse_id], message_type='notification', subtype='mail.mt_comment')

        override_write = super(InventoryPushNotification, self).write(new_changes)
        return override_write

