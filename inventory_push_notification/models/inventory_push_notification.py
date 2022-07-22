from odoo import models, api


class InventoryPushNotification(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'mail.thread']

    # @api.onchange('list_price')
    # def price_changed(self):
    #     new_price_data = int(self.list_price)
    #
    # @api.onchange('barcode')
    # def price_changed(self):
    #     new_barcode_data = int(self.barcode)

    # Mengepush Notif Sales Price
    @api.multi
    def write(self, new_changes):
        master_product = self.env['product.template'].search([('name', '=', self.name)])
        counter_id = self.env['res.partner'].search([('name', '=', 'Counter')]).id
        # apri_id = self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
        # # farietz_id =self.env['res.partner'].search([('name', '=', 'Farietz')]).id
        # warehouse_id = self.env['res.partner'].search([('name', '=', 'Warehouse')]).id

        old_barcode = master_product.barcode

        print(new_changes)
        if new_changes.get('list_price', False):
            print("Ada perubahan harga! Harap cek naik atau turun")
            old_price = master_product.list_price
            new_price = int(new_changes["list_price"])
            if new_price > old_price:
                final_price = f'{new_price:,}'
                print("Terdapat kenaikan harga menjadi " + final_price)
                # msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini NAIK menjadi Rp' + str(final_price)
                # master_product.message_post(body=msg_body, partner_ids=[counter_id], message_type='notification', subtype='mail.mt_comment')
            else:
                final_price = f'{new_price:,}'
                print("Terdapat penurunan harga menjadi " + final_price)
                # msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini TURUN menjadi Rp' + str(final_price)
                # master_product.message_post(body=msg_body, partner_ids=[counter_id, apri_id], message_type='notification', subtype='mail.mt_comment')

        # new_price = new_changes["list_price"]
        # new_barcode = new_changes["barcode"]


        # # Hardcoded user
        # counter_id = self.env['res.partner'].search([('name', '=', 'Counter')]).id
        # apri_id = self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
        # # farietz_id =self.env['res.partner'].search([('name', '=', 'Farietz')]).id
        # warehouse_id = self.env['res.partner'].search([('name', '=', 'Warehouse')]).id


        # # Price Update?
        # if new_price_value > old_price:
        #     final_price = f'{int(new_price_value):,}'
        #     msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini NAIK menjadi Rp' + str(final_price)
        #     master_product.message_post(body=msg_body, partner_ids=[counter_id, apri_id], message_type='notification', subtype='mail.mt_comment')
        #     del new_price_value
        # else:
        #     final_price = f'{int(new_price_value):,}'
        #     msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(self.name) + ' ini TURUN menjadi Rp' + str(final_price)
        #     master_product.message_post(body=msg_body, partner_ids=[counter_id, apri_id], message_type='notification', subtype='mail.mt_comment')
        #     del new_price_value

        override_write = super(InventoryPushNotification, self).write(new_changes)
        return override_write

                        # # Pass api.onchange result as global variables
                        #
                        # # Product template domain search
                        # model_id = self.env['product.template'].search([('name', '=', self.name)])
                        #
                        # # Hardcoded user
                        # counter_id = self.env['res.partner'].search([('name', '=', 'Counter')]).id
                        # apri_id = self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
                        # # farietz_id =self.env['res.partner'].search([('name', '=', 'Farietz')]).id
                        # warehouse_id = self.env['res.partner'].search([('name', '=', 'Warehouse')]).id
                        #
                        # # Check if the product template is new or not
                        # # If new, dont push notification
                        # # If not new, push notification based on what field are changing
                        # if (bool(model_id)) == False:
                        #     pass
                        # else:
                        #     # Sales Price push notification
                        #     try:
                        #         old_price = model_id.list_price
                        #         new_price = new_price_value
                        #
                        #         if new_price == None:
                        #             pass
                        #         else:
                        #             if new_price > old_price:
                        #                 final_price = f'{int(new_price):,}'
                        #                 msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(
                        #                     self.name) + ' ini NAIK menjadi Rp' + str(final_price)
                        #                 model_id.message_post(body=msg_body, partner_ids=[counter_id, apri_id],
                        #                                       message_type='notification', subtype='mail.mt_comment')
                        #                 new_price = None
                        #             else:
                        #                 final_price = f'{int(new_price):,}'
                        #                 msg_body = 'Team Counter & Warehouse harap segera mengganti harga barang ' + str(
                        #                     self.name) + ' ini TURUN menjadi Rp' + str(final_price)
                        #                 model_id.message_post(body=msg_body, partner_ids=[counter_id, apri_id],
                        #                                       message_type='notification', subtype='mail.mt_comment')
                        #                 new_price = None
                        #
                        #     except NameError:
                        #         pass
                        #
                        #     try:
                        #         new_barcode = new_barcode_value
                        #
                        #         if new_barcode == None:
                        #             pass
                        #         else:
                        #             msg_body = 'Team Counter & Warehouse harap segera mengganti barcode ' + str(
                        #                 self.name) + ' ini menjadi ' + str(new_barcode)
                        #             model_id.message_post(body=msg_body, partner_ids=[counter_id, apri_id], message_type='notification',
                        #                                   subtype='mail.mt_comment')
                        #         new_barcode = None
                        #
                        #     except NameError:
                        #         pass


    # # Mengepush Notif Barcode
    # @api.onchange('barcode')
    # def notif_counter_barcode(self):
    #     model_id = self.env['product.template'].search([('name', '=', self.name)])
    #     counter_id =self.env['res.partner'].search([('name', '=', 'Counter')]).id
    #     apri_id =self.env['res.partner'].search([('name', '=', 'Siti Nur Apriyanti')]).id
    #     # farietz_id =self.env['res.partner'].search([('name', '=', 'Farietz')]).id
    #     warehouse_id =self.env['res.partner'].search([('name', '=', 'Warehouse')]).id
    #     if (bool(model_id)) == False:
    #         pass
    #     else:
    #         msg_body = 'Team Counter & Warehouse harap segera mengganti barcode barang ' + str(self.name) + ' ini menjadi ' + str(self.barcode)
    #         model_id.message_post(body=msg_body, partner_ids=[counter_id, warehouse_id, apri_id], type='danger', message_type='notification', subtype='mail.mt_comment')
    #
    #









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