from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def item():
    item_fields = {
        "Item": [
           
            dict(fieldname='part_no', label='Part No',
                fieldtype='Data', insert_after='item_name'),

            dict(fieldname='brand_ts', label='Brand',
                fieldtype='Link', insert_after='part_no', options='Brand'),

            dict(fieldname='warranty_period_ts', label='Warranty Period (in days)',
                fieldtype='Data', insert_after='is_item_from_hub'),

            dict(fieldname='column_break', fieldtype='Column Break', ),

            dict(fieldname='opening_stock_ts', label='Opening Stock',
                fieldtype='Float', insert_after='column_break0'),
            
        ],
    
    }
    create_custom_fields(item_fields)
    print('finished')