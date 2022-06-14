
import re
from telegram import KeyboardButton

# reg_delivery_string = '🚚 Delivery staff'
reg_restaurant_string = '🍔 Restaurant'
skip_futher_priv_string = '✔️ Skip'

contact_info_button = KeyboardButton(
    '📞 Share Phone Number ', request_contact=True)
location_share_button = KeyboardButton(
    '📍 Share location ', request_location=True)


start_keyboard = [
    [ reg_restaurant_string],
    [skip_futher_priv_string]
]

dstaff_keyboard = [
    [contact_info_button],
    # [location_share_button]
]
