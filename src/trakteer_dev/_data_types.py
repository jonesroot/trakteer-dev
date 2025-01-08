# ############################################

# 

#          Trakteer Donate Data Types
#          ~~ 2023 (c) by Realzzy ~~
#           2025 Recode by ©Lucifer
# 
# ############################################


class TrakteerDonationData:
    def __init__(self, data: dict):
        self.__supporter_name = data.get("supporter_name", "")
        self.__unit = data.get("unit", "")
        self.__quantity = int(data.get("quantity", 0))
        self.__supporter_message = data.get("supporter_message", "")
        self.__supporter_avatar = data.get("supporter_avatar", "")
        self.__unit_icon = data.get("unit_icon", "")
        self.__price = data.get("price", "")
        self.__media = data.get("media")
        self.__id = data.get("id", "")

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "unit": self.unit,
            "amount": self.amount,
            "message": self.message,
            "avatar": self.avatar,
            "unit_icon": self.unit_icon,
            "price": self.price,
            "media": self.media,
            "id": self.id,
        }

    @property
    def name(self) -> str:
        return self.__supporter_name

    @property
    def unit(self) -> str:
        return self.__unit

    @property
    def amount(self) -> int:
        return self.__quantity

    @property
    def message(self) -> str:
        return self.__supporter_message

    @property
    def avatar(self) -> str:
        return self.__supporter_avatar

    @property
    def unit_icon(self) -> str:
        return self.__unit_icon

    @property
    def price(self) -> str:
        return self.__price

    @property
    def media(self) -> str:
        return self.__media

    @property
    def id(self) -> str:
        return self.__id
