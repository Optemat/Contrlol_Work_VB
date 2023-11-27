import invoice as inv
import position as pos
import InvoiceEditor as InEd
do = ''
editor = InEd.InvoiceEditor()
while do != 'Exit':
    print('Выберите действие:  Exit  Delete  Stat  New')
    do = (input())
    if do == 'New':
        new_invoice = inv.Invoice()
        while True:
            print('Введите название и стоимость позиции')
            position_line = input()
            if not position_line:
                editor.add(new_invoice)
                break
            (name, price) = position_line.split()
            new_invoice.add_position(pos.Position(name, int(price)))
    elif do == 'Delete':
        editor.delete()
        print('чек удалён')
    elif do == 'Stat':
        stat = editor.get_statistics()
        print(stat)
    elif do == 'Exit':
        print('Хорошего дня, спасибо за покупку')
        break
    else:
        print('Неизвестная команда')
