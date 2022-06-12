from .models import Order
from django.forms import ModelForm, TextInput, HiddenInput
from .models import Item


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['id_of_item', 'name_of_item', 'category', 'price', 'surname',
                  'name', 'patronymic', 'phone', 'city', 'post_office']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control border-lightgreen buy-input',
                'placeholder': 'Фамилия'
            }),
            "name": TextInput(attrs={
                'class': 'form-control border-lightgreen buy-input',
                'placeholder': 'Имя'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control border-lightgreen buy-input',
                'placeholder': 'Отчество'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control border-lightgreen buy-input',
                'placeholder': 'Мобильный телефон'
            }),
            "city": TextInput(attrs={
                'class': 'form-control border-lightgreen buy-input',
                'placeholder': 'Город'
            }),
            "post_office": TextInput(attrs={
                'class': 'form-control border-lightgreen buy-input',
                'placeholder': 'Отделение Новой почты'
            }),
        }

    def __init__(self, *args, **kwargs):
        id_of_item = kwargs.pop('id_of_item')

        if type(id_of_item) == str:
            item = Item.objects.get(id=id_of_item)

            super(OrderForm, self).__init__(*args, **kwargs)
            self.fields['id_of_item'].widget.attrs['value'] = item.id
            self.fields['name_of_item'].widget.attrs['value'] = item.name
            self.fields['category'].widget.attrs['value'] = item.category
            self.fields['price'].widget.attrs['value'] = item.price

        # если id_of_item это массив, то делаем свои манипуляции и все четко )
        else:
            ids = ''
            for i in id_of_item:
                ids += i.id + ', '
            ids = ids[:-1]
            ids = ids[:-1]

            names = ''
            for a in id_of_item:
                names += a.name + ', '
            names = names[:-1]
            names = names[:-1]

            categories = ''
            for j in id_of_item:
                categories += j.category + ', '
            categories = categories[:-1]
            categories = categories[:-1]

            prices = 0
            for k in id_of_item:
                k.price = k.price[:-1]
                k.price = int(k.price)
                prices += k.price

            super(OrderForm, self).__init__(*args, **kwargs)
            self.fields['id_of_item'].widget.attrs['value'] = ids
            self.fields['name_of_item'].widget.attrs['value'] = names
            self.fields['category'].widget.attrs['value'] = categories
            self.fields['price'].widget.attrs['value'] = prices
