from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def customize():
    custom_fields = {
        "Customer": [
            dict(fieldname='Salutation', label='salutation',
                fieldtype='Data', insert_after='customer_name', read_only=0),
            
        ]
                }
    create_custom_fields(custom_fields)

