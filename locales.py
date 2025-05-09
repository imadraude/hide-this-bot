from locales_dict import Locale, LocalesDict

locale_en = Locale()
locale_uk = Locale()

locales = LocalesDict(
    {
        "en": locale_en,
        "uk": locale_uk,
    },
    locale_en,
)

# TOO_LONG_TITLE
locale_en.too_long_title = "Your message is too long"
locale_uk.too_long_title = "Занадто довге повідомлення"

# FOR_TITLE
locale_en.for_title = "For %s"
locale_uk.for_title = "Для %s"

# EXCEPT_TITLE
locale_en.except_title = "Except %s"
locale_uk.except_title = "Крім %s"

# SPOILER_TITLE
locale_en.spoiler_title = "Spoiler"
locale_uk.spoiler_title = "Спойлер"


# TOO_LONG_MESSAGE
locale_en.too_long_message = (
    "🥺 Sorry, your message can't be sent as it exceeds the limit of 200 characters."
)
locale_uk.too_long_message = "🥺 Ваше повідомлення не може бути відправлено, так як його довжина перевищує ліміт в 200 символів."

# FOR_MESSAGE
locale_en.for_message = "Private message for %s."
locale_uk.for_message = "Приватне повідомлення для %s."

# EXCEPT_MESSAGE
locale_en.except_message = "Private message for everyone except %s."
locale_uk.except_message = "Приватне повідомлення для всіх, крім %s."

# SPOILER_MESSAGE
locale_en.spoiler_message = "Public spoiler message."
locale_uk.spoiler_message = "Публічне повідомлення під спойлером."

# GROUP_GREETING_MESSAGE
locale_en.group_greeting_message = (
    "👋 Hi! My name is %s and I can help you send private messages that only certain people can view. " \
    "To learn more send /start@%s and feel free to ask for help in our " \
    "<a href=\"t.me/radzinsky_chat\">public community</a> if you've got any questions."
)
locale_uk.group_greeting_message = (
    "👋 Привіт! Мене звуть %s і я можу допомогти вам відправляти повідомлення, які зможуть прочитати тільки " \
    "певне коло осіб. Щоб дізнатися більше відправте команду /start@%s і не соромтеся просити про допомогу " \
    "в нашому <a href=\"t.me/radzinsky_chat\">публічному чаті</a>, якщо у вас виникнуть будь-які питання."
)

# INFO_MESSAGE
locale_en.info_message = (
    "If you still have questions after reading the article, you can contact support or simply ask " \
    "for help in our public chat at any time you want.\n\n" \
    "👥 Public chat: @radzinsky_chat\n" \
    "⚙ Support: @undrcrxwn"
)
locale_uk.info_message = (
    "Якщо у вас залишилися питання після прочитання статті, ви можете в будь-який час звернутися в службу " \
    "підтримки або попросити про допомогу в нашому публічному чаті.\n\n" \
    "👥 Публічний чат: @radzinsky_chat\n" \
    "⚙ Підтримка: @undrcrxwn"
)

# HOW_TO_USE
locale_en.how_to_use = "How to use this bot?"
locale_uk.how_to_use = "Як користуватися цим ботом?"

# TOO_LONG_DESCRIPTION
locale_en.too_long_description = "Please shorten the length of your message so that it doesn't exceed the limit of 200 characters."
locale_uk.too_long_description = "Будь ласка, скоротіть довжину Вашого повідомлення, щоб вона не перевищувала ліміт в 200 символів."


# NOT_ALLOWED
locale_en.not_allowed = "You are not allowed to view this content."
locale_uk.not_allowed = "Вам заборонено переглядати цей контент."

# NOT_ACCESSIBLE
locale_en.not_accessible = "This content is no longer accessible."
locale_uk.not_accessible = "Цей контент більше недоступний."


# VIEW
locale_en.view = "View"
locale_uk.view = "Відкрити"

# AND_CONNECTOR
locale_en.and_connector = "and"
locale_uk.and_connector = "i"
