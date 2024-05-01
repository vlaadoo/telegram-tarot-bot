from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.database.database import get_layout_from_db
import json

start_card_of_day = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Выбрать карту",
            callback_data="2_select_card_of_day"
        )
    ]
])

def admin_panel_inline():
    admin_panel_inline_keyboard = InlineKeyboardBuilder()
    admin_panel_inline_keyboard.button(text="Изменить значения карт", callback_data="change_cards")
    admin_panel_inline_keyboard.button(text="Посмотреть значения карт", callback_data="check_cards")
    admin_panel_inline_keyboard.button(text="Изменить расклад", callback_data="my_change_layout")

    admin_panel_inline_keyboard.adjust(1)
    return admin_panel_inline_keyboard.as_markup()



def layout_inline():
    layout_inline_keyboard = InlineKeyboardBuilder()
    values = json.loads(get_layout_from_db()[2])
    count = 0
    for value in values:
        count += 1
        layout_inline_keyboard.button(text=str(count), callback_data=f"layout_{count}_call")

    return layout_inline_keyboard.as_markup()

def get_zodiac_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Овен', callback_data='aries')
    keyboard_builder.button(text='Телец', callback_data='taurus')
    keyboard_builder.button(text='Близнецы', callback_data='gemini')
    keyboard_builder.button(text='Рак', callback_data='cancer')
    keyboard_builder.button(text='Лев', callback_data='leo')
    keyboard_builder.button(text='Дева', callback_data='virgo')
    keyboard_builder.button(text='Весы', callback_data='libra')
    keyboard_builder.button(text='Скорпион', callback_data='scorpio')
    keyboard_builder.button(text='Стрелец', callback_data='sagittarius')
    keyboard_builder.button(text='Козерог', callback_data='capricorn')
    keyboard_builder.button(text='Водолей', callback_data='aquarius')
    keyboard_builder.button(text='Рыбы', callback_data='pisces')
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()



def edit_cards_arcans_kb():
    edit_cards_arcans_keyboard = InlineKeyboardBuilder()
    edit_cards_arcans_keyboard.button(text="Старшие арканы", callback_data="big_arcans")
    edit_cards_arcans_keyboard.button(text="Пентакли", callback_data="pentacli")
    edit_cards_arcans_keyboard.button(text="Жезлы", callback_data="zhezly")
    edit_cards_arcans_keyboard.button(text="Мечи", callback_data="mechi")
    edit_cards_arcans_keyboard.button(text="Чаши", callback_data="chashi")
    edit_cards_arcans_keyboard.button(text="← Назад", callback_data="adminka")

    edit_cards_arcans_keyboard.adjust(1)
    return edit_cards_arcans_keyboard.as_markup()


def edit_big_arcans_kb():
    edit_big_arcans_keyboard = InlineKeyboardBuilder()
    edit_big_arcans_keyboard.button(text="Дурак", callback_data="0")
    edit_big_arcans_keyboard.button(text="Маг", callback_data="1")
    edit_big_arcans_keyboard.button(text="Жрица", callback_data="2")
    edit_big_arcans_keyboard.button(text="Императрица", callback_data="3")
    edit_big_arcans_keyboard.button(text="Император", callback_data="4")
    edit_big_arcans_keyboard.button(text="Иерофант", callback_data="5")
    edit_big_arcans_keyboard.button(text="Влюбленные", callback_data="6")
    edit_big_arcans_keyboard.button(text="Колесница", callback_data="7")
    edit_big_arcans_keyboard.button(text="Регулирование", callback_data="8")
    edit_big_arcans_keyboard.button(text="Отшельник", callback_data="9")
    edit_big_arcans_keyboard.button(text="Фортуна", callback_data="10")
    edit_big_arcans_keyboard.button(text="Вожделение", callback_data="11")
    edit_big_arcans_keyboard.button(text="Повешенный", callback_data="12")
    edit_big_arcans_keyboard.button(text="Смерть", callback_data="13")
    edit_big_arcans_keyboard.button(text="Искусство", callback_data="14")
    edit_big_arcans_keyboard.button(text="Дьявол", callback_data="15")
    edit_big_arcans_keyboard.button(text="Башня", callback_data="16")
    edit_big_arcans_keyboard.button(text="Звезда", callback_data="17")
    edit_big_arcans_keyboard.button(text="Луна", callback_data="18")
    edit_big_arcans_keyboard.button(text="Солнце", callback_data="19")
    edit_big_arcans_keyboard.button(text="Эон", callback_data="20")
    edit_big_arcans_keyboard.button(text="Вселенная", callback_data="21")
    edit_big_arcans_keyboard.button(text="← Назад", callback_data="change_cards")

    edit_big_arcans_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1)

    return edit_big_arcans_keyboard.as_markup()

def edit_pentacli_kb():
    edit_pentacli_keyboard = InlineKeyboardBuilder()
    edit_pentacli_keyboard.button(text="Туз дисков", callback_data="22")
    edit_pentacli_keyboard.button(text="Двойка дисков", callback_data="23")
    edit_pentacli_keyboard.button(text="Тройка дисков", callback_data="24")
    edit_pentacli_keyboard.button(text="Четверка дисков", callback_data="25")
    edit_pentacli_keyboard.button(text="Пятерка дисков", callback_data="26")
    edit_pentacli_keyboard.button(text="Шестерка дисков", callback_data="27")
    edit_pentacli_keyboard.button(text="Семерка дисков", callback_data="28")
    edit_pentacli_keyboard.button(text="Восьмерка дисков", callback_data="29")
    edit_pentacli_keyboard.button(text="Девятка дисков", callback_data="30")
    edit_pentacli_keyboard.button(text="Десятка дисков", callback_data="31")
    edit_pentacli_keyboard.button(text="Принц дисков", callback_data="32")
    edit_pentacli_keyboard.button(text="Принцесса дисков", callback_data="33")
    edit_pentacli_keyboard.button(text="Королева дисков", callback_data="34")
    edit_pentacli_keyboard.button(text="Рыцарь дисков", callback_data="35")
    edit_pentacli_keyboard.button(text="← Назад", callback_data="change_cards")

    edit_pentacli_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 1)

    return edit_pentacli_keyboard.as_markup()

def edit_zhezly_kb():
    edit_zhezly_keyboard = InlineKeyboardBuilder()
    edit_zhezly_keyboard.button(text="Туз жезлов", callback_data="36")
    edit_zhezly_keyboard.button(text="Двойка жезлов", callback_data="37")
    edit_zhezly_keyboard.button(text="Тройка жезлов", callback_data="38")
    edit_zhezly_keyboard.button(text="Четверка жезлов", callback_data="39")
    edit_zhezly_keyboard.button(text="Пятерка жезлов", callback_data="40")
    edit_zhezly_keyboard.button(text="Шестерка жезлов", callback_data="41")
    edit_zhezly_keyboard.button(text="Семерка жезлов", callback_data="42")
    edit_zhezly_keyboard.button(text="Восьмерка жезлов", callback_data="43")
    edit_zhezly_keyboard.button(text="Девятка жезлов", callback_data="44")
    edit_zhezly_keyboard.button(text="Десятка жезлов", callback_data="45")
    edit_zhezly_keyboard.button(text="Принц жезлов", callback_data="46")
    edit_zhezly_keyboard.button(text="Принцесса жезлов", callback_data="47")
    edit_zhezly_keyboard.button(text="Королева жезлов", callback_data="48")
    edit_zhezly_keyboard.button(text="Рыцарь жезлов", callback_data="49")
    edit_zhezly_keyboard.button(text="← Назад", callback_data="change_cards")

    edit_zhezly_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 1)

    return edit_zhezly_keyboard.as_markup()

def edit_mechi_kb():
    edit_mechi_keyboard = InlineKeyboardBuilder()
    edit_mechi_keyboard.button(text="Туз мечей", callback_data="50")
    edit_mechi_keyboard.button(text="Двойка мечей", callback_data="51")
    edit_mechi_keyboard.button(text="Тройка мечей", callback_data="52")
    edit_mechi_keyboard.button(text="Четверка мечей", callback_data="53")
    edit_mechi_keyboard.button(text="Пятерка мечей", callback_data="54")
    edit_mechi_keyboard.button(text="Шестерка мечей", callback_data="55")
    edit_mechi_keyboard.button(text="Семерка мечей", callback_data="56")
    edit_mechi_keyboard.button(text="Восьмерка мечей", callback_data="57")
    edit_mechi_keyboard.button(text="Девятка мечей", callback_data="58")
    edit_mechi_keyboard.button(text="Десятка мечей", callback_data="59")
    edit_mechi_keyboard.button(text="Принц мечей", callback_data="60")
    edit_mechi_keyboard.button(text="Принцесса мечей", callback_data="61")
    edit_mechi_keyboard.button(text="Королева мечей", callback_data="62")
    edit_mechi_keyboard.button(text="Рыцарь мечей", callback_data="63")
    edit_mechi_keyboard.button(text="← Назад", callback_data="change_cards")

    edit_mechi_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 1)

    return edit_mechi_keyboard.as_markup()

def edit_chashi_kb():
    edit_chashi_keyboard = InlineKeyboardBuilder()
    edit_chashi_keyboard.button(text="Туз чаш", callback_data="64")
    edit_chashi_keyboard.button(text="Двойка чаш", callback_data="65")
    edit_chashi_keyboard.button(text="Тройка чаш", callback_data="66")
    edit_chashi_keyboard.button(text="Четверка чаш", callback_data="67")
    edit_chashi_keyboard.button(text="Пятерка чаш", callback_data="68")
    edit_chashi_keyboard.button(text="Шестерка чаш", callback_data="69")
    edit_chashi_keyboard.button(text="Семерка чаш", callback_data="70")
    edit_chashi_keyboard.button(text="Восьмерка чаш", callback_data="71")
    edit_chashi_keyboard.button(text="Девятка чаш", callback_data="72")
    edit_chashi_keyboard.button(text="Десятка чаш", callback_data="73")
    edit_chashi_keyboard.button(text="Принц чаш", callback_data="74")
    edit_chashi_keyboard.button(text="Принцесса чаш", callback_data="75")
    edit_chashi_keyboard.button(text="Королева чаш", callback_data="76")
    edit_chashi_keyboard.button(text="Рыцарь чаш", callback_data="77")
    edit_chashi_keyboard.button(text="← Назад", callback_data="change_cards")

    edit_chashi_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 1)

    return edit_chashi_keyboard.as_markup()





def show_cards_arcans_kb():
    show_cards_arcans_keyboard = InlineKeyboardBuilder()
    show_cards_arcans_keyboard.button(text="Старшие арканы", callback_data="check_big_arcans")
    show_cards_arcans_keyboard.button(text="Пентакли", callback_data="check_pentacli")
    show_cards_arcans_keyboard.button(text="Жезлы", callback_data="check_zhezly")
    show_cards_arcans_keyboard.button(text="Мечи", callback_data="check_mechi")
    show_cards_arcans_keyboard.button(text="Чаши", callback_data="check_chashi")
    show_cards_arcans_keyboard.button(text="← Назад", callback_data="adminka")

    show_cards_arcans_keyboard.adjust(1)
    return show_cards_arcans_keyboard.as_markup()

def show_big_arcans_kb():
    show_big_arcans_keyboard = InlineKeyboardBuilder()
    show_big_arcans_keyboard.button(text="Дурак", callback_data="0_check")
    show_big_arcans_keyboard.button(text="Маг", callback_data="1_check")
    show_big_arcans_keyboard.button(text="Жрица", callback_data="2_check")
    show_big_arcans_keyboard.button(text="Императрица", callback_data="3_check")
    show_big_arcans_keyboard.button(text="Император", callback_data="4_check")
    show_big_arcans_keyboard.button(text="Иерофант", callback_data="5_check")
    show_big_arcans_keyboard.button(text="Влюбленные", callback_data="6_check")
    show_big_arcans_keyboard.button(text="Колесница", callback_data="7_check")
    show_big_arcans_keyboard.button(text="Регулирование", callback_data="8_check")
    show_big_arcans_keyboard.button(text="Отшельник", callback_data="9_check")
    show_big_arcans_keyboard.button(text="Фортуна", callback_data="10_check")
    show_big_arcans_keyboard.button(text="Вожделение", callback_data="11_check")
    show_big_arcans_keyboard.button(text="Повешенный", callback_data="12_check")
    show_big_arcans_keyboard.button(text="Смерть", callback_data="13_check")
    show_big_arcans_keyboard.button(text="Искусство", callback_data="14_check")
    show_big_arcans_keyboard.button(text="Дьявол", callback_data="15_check")
    show_big_arcans_keyboard.button(text="Башня", callback_data="16_check")
    show_big_arcans_keyboard.button(text="Звезда", callback_data="17_check")
    show_big_arcans_keyboard.button(text="Луна", callback_data="18_check")
    show_big_arcans_keyboard.button(text="Солнце", callback_data="19_check")
    show_big_arcans_keyboard.button(text="Эон", callback_data="20_check")
    show_big_arcans_keyboard.button(text="Вселенная", callback_data="21_check")
    show_big_arcans_keyboard.button(text="← Назад", callback_data="check_cards")

    show_big_arcans_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1)

    return show_big_arcans_keyboard.as_markup()

def show_pentacli_kb():
    show_pentacli_keyboard = InlineKeyboardBuilder()
    show_pentacli_keyboard.button(text="Туз дисков", callback_data="22_check")
    show_pentacli_keyboard.button(text="Двойка дисков", callback_data="23_check")
    show_pentacli_keyboard.button(text="Тройка дисков", callback_data="24_check")
    show_pentacli_keyboard.button(text="Четверка дисков", callback_data="25_check")
    show_pentacli_keyboard.button(text="Пятерка дисков", callback_data="26_check")
    show_pentacli_keyboard.button(text="Шестерка дисков", callback_data="27_check")
    show_pentacli_keyboard.button(text="Семерка дисков", callback_data="28_check")
    show_pentacli_keyboard.button(text="Восьмерка дисков", callback_data="29_check")
    show_pentacli_keyboard.button(text="Девятка дисков", callback_data="30_check")
    show_pentacli_keyboard.button(text="Десятка дисков", callback_data="31_check")
    show_pentacli_keyboard.button(text="Принц дисков", callback_data="32_check")
    show_pentacli_keyboard.button(text="Принцесса дисков", callback_data="33_check")
    show_pentacli_keyboard.button(text="Королева дисков", callback_data="34_check")
    show_pentacli_keyboard.button(text="Рыцарь дисков", callback_data="35_check")
    show_pentacli_keyboard.button(text="← Назад", callback_data="check_cards")

    show_pentacli_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 1)

    return show_pentacli_keyboard.as_markup()

def show_zhezly_kb():
    show_zhezly_keyboard = InlineKeyboardBuilder()
    show_zhezly_keyboard.button(text="Туз жезлов", callback_data="36_check")
    show_zhezly_keyboard.button(text="Двойка жезлов", callback_data="37_check")
    show_zhezly_keyboard.button(text="Тройка жезлов", callback_data="38_check")
    show_zhezly_keyboard.button(text="Четверка жезлов", callback_data="39_check")
    show_zhezly_keyboard.button(text="Пятерка жезлов", callback_data="40_check")
    show_zhezly_keyboard.button(text="Шестерка жезлов", callback_data="41_check")
    show_zhezly_keyboard.button(text="Семерка жезлов", callback_data="42_check")
    show_zhezly_keyboard.button(text="Восьмерка жезлов", callback_data="43_check")
    show_zhezly_keyboard.button(text="Девятка жезлов", callback_data="44_check")
    show_zhezly_keyboard.button(text="Десятка жезлов", callback_data="45_check")
    show_zhezly_keyboard.button(text="Принц жезлов", callback_data="46_check")
    show_zhezly_keyboard.button(text="Принцесса жезлов", callback_data="47_check")
    show_zhezly_keyboard.button(text="Королева жезлов", callback_data="48_check")
    show_zhezly_keyboard.button(text="Рыцарь жезлов", callback_data="49_check")
    show_zhezly_keyboard.button(text="← Назад", callback_data="check_cards")

    show_zhezly_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 1)

    return show_zhezly_keyboard.as_markup()

def show_mechi_kb():
    show_mechi_keyboard = InlineKeyboardBuilder()
    show_mechi_keyboard.button(text="Туз мечей", callback_data="50_check")
    show_mechi_keyboard.button(text="Двойка мечей", callback_data="51_check")
    show_mechi_keyboard.button(text="Тройка мечей", callback_data="52_check")
    show_mechi_keyboard.button(text="Четверка мечей", callback_data="53_check")
    show_mechi_keyboard.button(text="Пятерка мечей", callback_data="54_check")
    show_mechi_keyboard.button(text="Шестерка мечей", callback_data="55_check")
    show_mechi_keyboard.button(text="Семерка мечей", callback_data="56_check")
    show_mechi_keyboard.button(text="Восьмерка мечей", callback_data="57_check")
    show_mechi_keyboard.button(text="Девятка мечей", callback_data="58_check")
    show_mechi_keyboard.button(text="Десятка мечей", callback_data="59_check")
    show_mechi_keyboard.button(text="Принц мечей", callback_data="60_check")
    show_mechi_keyboard.button(text="Принцесса мечей", callback_data="61_check")
    show_mechi_keyboard.button(text="Королева мечей", callback_data="62_check")
    show_mechi_keyboard.button(text="Рыцарь мечей", callback_data="63_check")
    show_mechi_keyboard.button(text="← Назад", callback_data="check_cards")

    show_mechi_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 1)

    return show_mechi_keyboard.as_markup()

def show_chashi_kb():
    show_chashi_keyboard = InlineKeyboardBuilder()
    show_chashi_keyboard.button(text="Туз чаш", callback_data="64_check")
    show_chashi_keyboard.button(text="Двойка чаш", callback_data="65_check")
    show_chashi_keyboard.button(text="Тройка чаш", callback_data="66_check")
    show_chashi_keyboard.button(text="Четверка чаш", callback_data="67_check")
    show_chashi_keyboard.button(text="Пятерка чаш", callback_data="68_check")
    show_chashi_keyboard.button(text="Шестерка чаш", callback_data="69_check")
    show_chashi_keyboard.button(text="Семерка чаш", callback_data="70_check")
    show_chashi_keyboard.button(text="Восьмерка чаш", callback_data="71_check")
    show_chashi_keyboard.button(text="Девятка чаш", callback_data="72_check")
    show_chashi_keyboard.button(text="Десятка чаш", callback_data="73_check")
    show_chashi_keyboard.button(text="Принц чаш", callback_data="74_check")
    show_chashi_keyboard.button(text="Принцесса чаш", callback_data="75_check")
    show_chashi_keyboard.button(text="Королева чаш", callback_data="76_check")
    show_chashi_keyboard.button(text="Рыцарь чаш", callback_data="77_check")
    show_chashi_keyboard.button(text="← Назад", callback_data="check_cards")

    show_chashi_keyboard.adjust(2, 2, 2, 2, 2, 2, 2, 1)

    return show_chashi_keyboard.as_markup()
