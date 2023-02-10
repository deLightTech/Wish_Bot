# Бот создан прораммистом Владиславом Тёровым by delight Bots
# Copyright 2021 Все права защищены
# deLight Bots оставляет за собой авторское право на созданные продукты


import telebot
from PIL import Image, ImageDraw, ImageFont
from telebot import types
from config import TG_TOKEN
from config import style1, style2, style3, style4, style5, style6, style7
from config import command, command_cat
from config import dialog1, dialog2, dialog3, dialog4, dialog5, dialog6
from config import text_btn1, text_btn2
from config import font1, font3, font_size_3, font_size_1
from config import text_color_1, text_color_3
from config import image1, image2, image3, image4, image5, image6, image7
from config import end_image, start_image, not_image
from config import text_11_loc_a, text_11_loc_b, text_13_loc_a, text_13_loc_b, text_21_loc_a, text_21_loc_b
from config import text_23_loc_a, text_23_loc_b, text_31_loc_a, text_31_loc_b, text_33_loc_a, text_33_loc_b
from config import text_41_loc_a, text_41_loc_b, text_43_loc_a, text_43_loc_b, text_51_loc_a, text_51_loc_b
from config import text_53_loc_a, text_53_loc_b, text_61_loc_a, text_61_loc_b, text_63_loc_a, text_63_loc_b
from config import text_71_loc_a, text_71_loc_b, text_73_loc_a, text_73_loc_b

bot = telebot.TeleBot(TG_TOKEN)

cat = ''
name = ''

# Бот создан прораммистом Владиславом Тёровым by delight Bots
# Copyright 2022 Все права защищены
# deLight Bots оставляет за собой авторское право на созданные продукты

keyboard = types.InlineKeyboardMarkup(row_width=1)
keyboard2 = types.InlineKeyboardMarkup(row_width=1)
btn_1 = types.InlineKeyboardButton(text=style1, callback_data='do_one')
keyboard.add(btn_1)
btn_2 = types.InlineKeyboardButton(text=style2, callback_data='do_two')
keyboard.add(btn_2)
btn_3 = types.InlineKeyboardButton(text=style3, callback_data='do_three')
keyboard.add(btn_3)
btn_4 = types.InlineKeyboardButton(text=style4, callback_data='do_four')
keyboard.add(btn_4)
btn_5 = types.InlineKeyboardButton(text=style5, callback_data='do_five')
keyboard.add(btn_5)
btn_6 = types.InlineKeyboardButton(text=style6, callback_data='do_six')
keyboard.add(btn_6)
btn_7 = types.InlineKeyboardButton(text=style7, callback_data='do_seven')
keyboard.add(btn_7)

btn_10 = types.InlineKeyboardButton(text=text_btn1, callback_data='do_yes')
keyboard2.add(btn_10)

btn_11 = types.InlineKeyboardButton(text=text_btn2, callback_data='do_no')
keyboard2.add(btn_11)


# Бот создан прораммистом Владиславом Тёровым by delight Bots
# Copyright 2022 Все права защищены
# deLight Bots оставляет за собой авторское право на созданные продукты

@bot.message_handler(commands=[command])
def do_start(message):
    bot.send_photo(chat_id=message.chat.id, photo=open(start_image, 'rb'))
    bot.send_message(
        message.chat.id,
        dialog1
    )
    bot.register_next_step_handler(message, do_cat)


@bot.message_handler(commands=['about'])
def do_st(message):
     bot.send_message(
        message.chat.id,
        'Бот создан Владиславом Тёровым by deLight Bots.\nСоздаю ботов справочников, ботов магазинов, ботов для оформления заказов и других. Если Вам нужен бот, то обращайтесь в telegram по имени пользователя @tyorov_dkfl'
    )


def do_cat(message):
    global cat
    cat = message.text
    if cat == '/start':
        bot.send_message(
            message.chat.id,
            'Хорошо, сделаем поздравление снова!'
        )
        do_start(message)
    else:
        bot.send_message(
            message.chat.id,
            dialog2,
            reply_markup=keyboard
        )


# Бот создан прораммистом Владиславом Тёровым by delight Bots
# Copyright 2022 Все права защищены
# deLight Bots оставляет за собой авторское право на созданные продукты


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global cat
    global name
    if call.data == "do_one":
        bot.send_message(call.message.chat.id, dialog3)
        bot.register_next_step_handler(call.message, do_one)
    elif call.data == "do_two":
        bot.send_message(call.message.chat.id, dialog3)
        bot.register_next_step_handler(call.message, do_two)
    elif call.data == "do_three":
        bot.send_message(call.message.chat.id, dialog3)
        bot.register_next_step_handler(call.message, do_three)
    elif call.data == "do_four":
        bot.send_message(call.message.chat.id, dialog3)
        bot.register_next_step_handler(call.message, do_four)
    elif call.data == "do_five":
        bot.send_message(call.message.chat.id, dialog3)
        bot.register_next_step_handler(call.message, do_five)
    elif call.data == "do_six":
        bot.send_message(call.message.chat.id, dialog3)
        bot.register_next_step_handler(call.message, do_six)
    elif call.data == "do_seven":
        bot.send_message(call.message.chat.id, dialog3)
        bot.register_next_step_handler(call.message, do_seven)
    elif call.data == "do_yes":
        do_start(call.message)
    elif call.data == "do_no":
        bot.send_photo(chat_id=call.message.chat.id, photo=open(not_image, 'rb'))
        bot.send_message(call.message.chat.id, dialog6)


# Бот создан прораммистом Владиславом Тёровым by delight Bots
# Copyright 2022 Все права защищены
# deLight Bots оставляет за собой авторское право на созданные продукты

def do_one(message):
    global name
    global cat
    name = message.text
    im = Image.open(image1)
    cat = cat + command_cat
    postcard = str(message.chat.id)
    postcard = 'postcards/' + postcard + '.jpg'
    if name == '/start':
        bot.send_message(
            message.chat.id,
            'Хорошо, сделаем поздравление снова!'
        )
        do_start(message)
    else:
        fontcat = ImageFont.truetype(font1, size=font_size_1)
        fontfrom = ImageFont.truetype(font3, size=font_size_3)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (text_11_loc_a, text_11_loc_b),
            cat,
            anchor="mb",
            font=fontcat,
            fill=text_color_1)
        draw_text.text(
            (text_13_loc_a, text_13_loc_b),
            name,
            anchor="mb",
            font=fontfrom,
            fill=text_color_3)
        im.save(postcard)
        bot.send_photo(chat_id=message.chat.id, photo=open(postcard, 'rb'))
        bot.send_message(chat_id=message.chat.id, text=dialog4)
        bot.send_message(chat_id=message.chat.id, text=dialog5, reply_markup=keyboard2)


def do_two(message):
    global name
    global cat
    name = message.text
    postcard = str(message.chat.id)
    postcard = 'postcards/' + postcard + '.jpg'
    if name == '/start':
        bot.send_message(
            message.chat.id,
            'Хорошо, сделаем поздравление снова!'
        )
        do_start(message)
    else:
        im = Image.open(image2)
        cat = cat + command_cat
        fontcat = ImageFont.truetype(font1, size=font_size_1)
        fontfrom = ImageFont.truetype(font3, size=font_size_3)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (text_21_loc_a, text_21_loc_b),
            cat,
            anchor="mb",
            font=fontcat,
            fill=text_color_1)
        draw_text.text(
            (text_23_loc_a, text_23_loc_b),
            name,
            anchor="mb",
            font=fontfrom,
            fill=text_color_3)
        im.save(postcard)
        bot.send_photo(chat_id=message.chat.id, photo=open(postcard, 'rb'))
        bot.send_message(chat_id=message.chat.id, text=dialog4)
        bot.send_message(chat_id=message.chat.id, text=dialog5, reply_markup=keyboard2)


def do_three(message):
    global name
    global cat
    name = message.text
    postcard = str(message.chat.id)
    postcard = 'postcards/' + postcard + '.jpg'
    if name == '/start':
        bot.send_message(
            message.chat.id,
            'Хорошо, сделаем поздравление снова!'
        )
        do_start(message)
    else:
        im = Image.open(image3)
        cat = cat + command_cat
        fontcat = ImageFont.truetype(font1, size=font_size_1)
        fontfrom = ImageFont.truetype(font3, size=font_size_3)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (text_31_loc_a, text_31_loc_b),
            cat,
            anchor="mb",
            font=fontcat,
            fill=text_color_1)
        draw_text.text(
            (text_33_loc_a, text_33_loc_b),
            name,
            anchor="mb",
            font=fontfrom,
            fill=text_color_3)
        im.save(postcard)
        bot.send_photo(chat_id=message.chat.id, photo=open(postcard, 'rb'))
        bot.send_message(chat_id=message.chat.id, text=dialog4)
        bot.send_message(chat_id=message.chat.id, text=dialog5, reply_markup=keyboard2)


def do_four(message):
    global name
    global cat
    name = message.text
    postcard = str(message.chat.id)
    postcard = 'postcards/' + postcard + '.jpg'
    if name == '/start':
        bot.send_message(
            message.chat.id,
            'Хорошо, сделаем поздравление снова!'
        )
        do_start(message)
    else:
        im = Image.open(image4)
        cat = cat + command_cat
        fontcat = ImageFont.truetype(font1, size=font_size_1)
        fontfrom = ImageFont.truetype(font3, size=font_size_3)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (text_41_loc_a, text_41_loc_b),
            cat,
            anchor="mb",
            font=fontcat,
            fill=text_color_1)
        draw_text.text(
            (text_43_loc_a, text_43_loc_b),
            name,
            anchor="mb",
            font=fontfrom,
            fill=text_color_3)
        im.save(postcard)
        bot.send_photo(chat_id=message.chat.id, photo=open(postcard, 'rb'))
        bot.send_message(chat_id=message.chat.id, text=dialog4)
        bot.send_message(chat_id=message.chat.id, text=dialog5, reply_markup=keyboard2)


def do_five(message):
    global name
    global cat
    name = message.text
    postcard = str(message.chat.id)
    postcard = 'postcards/' + postcard + '.jpg'
    if name == '/start':
        bot.send_message(
            message.chat.id,
            'Хорошо, сделаем поздравление снова!'
        )
        do_start(message)
    else:
        im = Image.open(image5)
        cat = cat + command_cat
        fontcat = ImageFont.truetype(font1, size=font_size_1)
        fontfrom = ImageFont.truetype(font3, size=font_size_3)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (text_51_loc_a, text_51_loc_b),
            cat,
            anchor="mb",
            font=fontcat,
            fill=text_color_1)
        draw_text.text(
            (text_53_loc_a, text_53_loc_b),
            name,
            anchor="mb",
            font=fontfrom,
            fill=text_color_3)
        im.save(postcard)
        bot.send_photo(chat_id=message.chat.id, photo=open(postcard, 'rb'))
        bot.send_message(chat_id=message.chat.id, text=dialog4)
        bot.send_message(chat_id=message.chat.id, text=dialog5, reply_markup=keyboard2)


# Бот создан прораммистом Владиславом Тёровым by delight Bots
# Copyright 2021 Все права защищены
# deLight Bots оставляет за собой авторское право на созданные продукты

def do_six(message):
    global name
    global cat
    name = message.text
    postcard = str(message.chat.id)
    postcard = 'postcards/' + postcard + '.jpg'
    if name == '/start':
        bot.send_message(
            message.chat.id,
            'Хорошо, сделаем поздравление снова!'
        )
        do_start(message)
    else:
        im = Image.open(image6)
        cat = cat + command_cat
        fontcat = ImageFont.truetype(font1, size=font_size_1)
        fontfrom = ImageFont.truetype(font3, size=font_size_3)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (text_61_loc_a, text_61_loc_b),
            cat,
            anchor="mb",
            font=fontcat,
            fill=text_color_1)
        draw_text.text(
            (text_63_loc_a, text_63_loc_b),
            name,
            anchor="mb",
            font=fontfrom,
            fill=text_color_3)
        im.save(postcard)
        bot.send_photo(chat_id=message.chat.id, photo=open(postcard, 'rb'))
        bot.send_message(chat_id=message.chat.id, text=dialog4)
        bot.send_message(chat_id=message.chat.id, text=dialog5, reply_markup=keyboard2)


def do_seven(message):
    global name
    global cat
    name = message.text
    postcard = str(message.chat.id)
    postcard = 'postcards/' + postcard + '.jpg'
    if name == '/start':
        bot.send_message(
            message.chat.id,
            'Хорошо, сделаем поздравление снова!'
        )
        do_start(message)
    else:
        im = Image.open(image7)
        cat = cat + command_cat
        fontcat = ImageFont.truetype(font1, size=font_size_1)
        fontfrom = ImageFont.truetype(font3, size=font_size_3)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (text_71_loc_a, text_71_loc_b),
            cat,
            anchor="mb",
            font=fontcat,
            fill=text_color_1)
        draw_text.text(
            (text_73_loc_a, text_73_loc_b),
            name,
            anchor="mb",
            font=fontfrom,
            fill=text_color_3)
        im.save(postcard)
        bot.send_photo(chat_id=message.chat.id, photo=open(postcard, 'rb'))
        bot.send_message(chat_id=message.chat.id, text=dialog4)
        bot.send_message(chat_id=message.chat.id, text=dialog5, reply_markup=keyboard2)


bot.polling(none_stop=True, interval=0)

# Бот создан прораммистом Владиславом Тёровым by delight Bots
# Copyright 2021 Все права защищены
# deLight Bots оставляет за собой авторское право на созданные продукты
