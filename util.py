# encoding: utf-8


def fix_fields(fields):
    for field in fields.values():
        field.widget.attrs.update({
            'class': 'form-control'
        })
