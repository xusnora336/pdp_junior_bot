import os

from aiogram import Router, F, types
from aiogram.client import bot
from aiogram.types import FSInputFile, contact
from handlers.keyboard import company_about, tillar, eng, courses
from handlers.keyboard import kurslar

shohruh_abdurahmonov = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "Shohruh_Abdurahmonov.png"))
abrorjon_abdusaidov=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "Abrorjon_Abdusaidov.png"))
asadbek_erkinov=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "Asadbek_Erkinov.png"))
asilbek_mamadaliyev=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "Asilbek_Mamadaliyev.png"))
bohodir_isroilov=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "Bohodir_Isroilov.png"))
habibulloh_nuriddinov=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "Habibulloh_nuriddinov.png"))
jahongir_abduraimov=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "Jahongir_Abduraimov.png"))

mentorlar=[[shohruh_abdurahmonov, "Shohruh"],
        [abrorjon_abdusaidov, "Abrorjon"],
        [asadbek_erkinov, "Asadbek"],
        [asilbek_mamadaliyev, "Asilbek"],
        [bohodir_isroilov, "Bohodir"],
        [habibulloh_nuriddinov, "Habibulloh"],
        [jahongir_abduraimov, "Jahongir"],]
router = Router()
@router.message(F.text == "Kompaniya haqida")
async def img(message: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_6.png"))
    text = "8 yillik tajribaga, 2000 mingdan ortiq o'quvchilar va tajribali mentorlarga ega!"
    await message.answer_photo(photo=img,caption=text, reply_markup=company_about)

@router.message(F.text == "Bizning mentorlar👩‍🏫")
async def images(message: types.Message):
    for image in mentorlar:
        await message.answer_photo(photo=image[0],caption=image[1], reply_markup=company_about)

@router.message(F.text == "Kontakt📞/Manzil")
async def images(message: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_1.png"))
    text=("📞-> +998 78 777 74 77\n"
          "Toshkent shahri, Shayhontohur tumani,\n"
          "Chorsu, Xadra, Zarqaynar 3-uy")
    await message.answer_photo(photo=img,caption=text, reply_markup=company_about)

@router.message(F.text == "Til")
async def images(message: types.Message):
    text=("Tilni tanlang")
    await message.answer(text, reply_markup=tillar)

@router.message(F.text=="ENG")
async def images(message: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_5.png"))
    text=("Welcome to PDP Junior bot!")
    await message.answer_photo(photo=img, caption=text, reply_markup=eng)

@router.message(F.text=="About the company")
async def images(message: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_6.png"))
    text="Has 8 years of experience, more than 2000 thousand students and experienced mentors!"
    await message.answer_photo(photo=img, caption=text, reply_markup=eng)

@router.message(F.text == "Our mentors👩‍🏫")
async def images(message: types.Message):
    for image in mentorlar:
        await message.answer_photo(photo=image[0],caption=image[1], reply_markup=eng)

@router.message(F.text == "Our courses")
async def images(message: types.Message):
    text="Our courses"
    await message.answer(text=text, reply_markup=courses)

@router.message(F.text=="Python_junior")
async def images(message: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_4.png"))
    text = ("Python-fundamentals of logical thinking and programming")
    await message.answer_photo(photo=img, caption=text, reply_markup=courses)

@router.message(F.text == "Fronted_junior")
async def images(message: types.Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "fronted.png"))
    text=("Fronted junior")
    await message.answer_photo(photo=img, caption=text, reply_markup=courses)

@router.message(F.text == "Robotics")
async def images(message: types.Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_3.png"))
    text=("Robotics")
    await message.answer_photo(photo=img,caption=text, reply_markup=courses)

@router.message(F.text == "Scratch")
async def images(message: types.Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_2.png"))
    text=("Scratch")
    await message.answer_photo(photo=img, caption=text, reply_markup=courses)

@router.message(F.text == "Back")
async def images(message: types.Message):
    text = "Back"
    await message.answer(text=text, reply_markup=eng)

@router.message(F.text == "Language")
async def images(message: types.Message):
    text = "Choose a language"
    await message.answer(text=text, reply_markup=tillar)

@router.message(F.text == "UZB🇺🇿")
async def images(message: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_5.png"))
    text = ("PDP Junior botiga xush kelibsiz!")
    await message.answer_photo(photo=img, caption=text, reply_markup=company_about)


@router.message(F.text=="Contact📞 / Location")
async def images(message: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_1.png"))
    text=("📞-> +998 78 777 74 77\n"
          "Tashkent City, Shayhontohur district,\n"
          " Chorsu, Khadra, Zarqaynar 3rd House")
    await message.answer_photo(photo=img,caption=text, reply_markup=eng)



@router.message(F.text == "Kurslarimiz")
async def images(message: types.Message):
    text=("bizning kurslarimiz")
    await message.answer(text, reply_markup=kurslar)

@router.message(F.text == "Python_junior")
async def images(message: types.Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_4.png"))
    text=("Python-mantiqiy fikrlash va dasturlash asoslari")
    await message.answer_photo(photo=img, caption=text, reply_markup=kurslar)

@router.message(F.text == "Fronted_junior")
async def images(message: types.Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "fronted.png"))
    text=("Fronted junior")
    await message.answer_photo(photo=img, caption=text, reply_markup=kurslar)


@router.message(F.text == "Robototexnika")
async def images(message: types.Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_3.png"))
    text=("Robototexnika")
    await message.answer_photo(photo=img,caption=text, reply_markup=kurslar)


@router.message(F.text == "Scratch")
async def images(message: types.Message):
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_2.png"))
    text=("Scratch")
    await message.answer_photo(photo=img, caption=text, reply_markup=kurslar)


@router.message(F.text == "Orqaga")
async def images(message: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_6.png"))
    text = "8 yillik tajribaga, 2000 mingdan ortiq o'quvchilarva tajribali mentorlarga ega!"
    await message.answer_photo(photo=img, caption=text, reply_markup=company_about)