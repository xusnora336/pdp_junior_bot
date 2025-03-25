from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup

company_about=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kompaniya haqida"),
         KeyboardButton(text="Bizning mentorlar👩‍🏫")],
        [KeyboardButton(text="Kurslarimiz")],
        [KeyboardButton(text="Kontakt📞/Manzil"),
         KeyboardButton(text="Til")],

    ],resize_keyboard=True,)

kurslar=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Python_junior"),
         KeyboardButton(text="Fronted_junior")],
        [KeyboardButton(text="Robototexnika"),
          KeyboardButton(text="Scratch")],
        [KeyboardButton(text="Orqaga")]
    ],resize_keyboard=True,
)

tillar=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="UZB🇺🇿"),
         KeyboardButton(text="ENG")],
    ],resize_keyboard=True,
)

eng=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="About the company"),
         KeyboardButton(text="Our mentors👩‍🏫")],
        [KeyboardButton(text="Our courses")],
        [KeyboardButton(text="Contact📞 / Location"),
         KeyboardButton(text="Language")],

    ],resize_keyboard=True,)

courses=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Python_junior"),
         KeyboardButton(text="Fronted_junior")],
        [KeyboardButton(text="Robotics"),
          KeyboardButton(text="Scratch")],
        [KeyboardButton(text="Back")]
    ],resize_keyboard=True,
)