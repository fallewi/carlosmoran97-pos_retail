{
    'name': "POS All In One Futures",
    'version': '6.3.0',
    'category': 'Point of Sale',
    'author': 'TL Technology',
    'live_test_url': 'http://posodoo.com/web/signup',
    'price': '450',
    'website': 'http://posodoo.com/web/signup',
    'sequence': 0,
    'depends': [
        'sale_stock',
        'account',
        'account_cancel',
        'point_of_sale',
        'bus',
        'stock',
        'purchase',
        'mrp',
        'product_expiry',
    ],
    'demo': ['demo/demo_data.xml'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_menu.xml',
        'reports/pos_manufacturing_report.xml',
        'reports/pos_tracking_client.xml',
        'reports/pos_sale_analytic.xml',
        'reports/report_pos_order.xml',
        'reports/pos_sale_report_template.xml',
        'reports/pos_sale_report_view.xml',
        'datas/schedule.xml',
        'datas/email_template.xml',
        'datas/customer.xml',
        'datas/barcode_rule.xml',
        'datas/pos_loyalty_category.xml',
        'datas/product.xml',
        'datas/stock_picking_type.xml',
        'datas/pos_bus.xml',
        'import/import_libraties.xml',
        'views/pos_config.xml',
        'views/pos_config_image.xml',
        'views/pos_session.xml',
        'views/product.xml',
        'views/pos_order.xml',
        'views/sale_order.xml',
        'views/pos_loyalty.xml',
        'views/res_partner_credit.xml',
        'views/res_partner.xml',
        'views/res_users.xml',
        'views/pos_promotion.xml',
        'views/account_journal.xml',
        'views/pos_voucher.xml',
        'views/pos_bus.xml',
        'views/mrp_production.xml',
        'views/pos_tag.xml',
        'views/pos_note.xml',
        'views/pos_combo_item.xml',
        'views/product_variant.xml',
        'views/product_barcode.xml',
        'views/stock_production_lot.xml',
        'views/pos_quickly_payment.xml',
        'views/pos_global_discount.xml',
        'views/account_invoice.xml',
        'views/purchase_order.xml',
        'views/medical_insurance.xml',
        'views/pos_call_log.xml',
        'views/pos_cache_database.xml',
        'views/sale_extra.xml',
        'views/pos_parameter.xml',
        'wizards/account_invoice_refund.xml',
        'wizards/sale_order_line_insert.xml',
        'wizards/remove_pos_order.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    "currency": 'EUR',
    'installable': True,
    'application': True,
    'images': ['static/description/icon.png'],
    'support': 'thanhchatvn@gmail.com',
    "license": "OPL-1",
    'post_init_hook': '_auto_clean_cache_when_installed',
}
