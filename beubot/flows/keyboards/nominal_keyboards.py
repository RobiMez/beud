from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from misc.menu_builder import build_menu


str_place_order = "➕ Place order"
str_view_orders = "👀 View placed orders"

nominal_menu = [
    [str_place_order],
    [str_view_orders]
]

str_r_view_orders = "👀 View pending orders"
# str_r_add_menu = "➕ Add a new food menu"

nominal_r_menu = [
    [str_r_view_orders],
    # [str_r_add_menu]
]
# # --------------------------------
# async def make_restaurant_keyboard(update,context):
#     restaurants = []
#     # restaurantsf = users.find({"role":"restaurant"})
#     restaurantsf = context.bot_data['users']

#     for restaurant in restaurantsf:
#         if restaurant['role'] == 'restaurant':
#             restaurants.append((str(restaurant['user_id']), restaurant))
        
#     restaurant_menu = []

#     for restaurant in restaurants:
#         restaurant_menu.append(InlineKeyboardButton(
#             restaurant[1]['full_name'], callback_data='restaurant_'+restaurant[0]))


#     restaurant_menu = build_menu(restaurant_menu, 1)

# # --------------------------------
# # TODO: aint got enough time to implement a fancy one 

# # def build_food_menu_for_restaurant(restaurant):
# #     food_menu = []
# #     restaurantsf = users.find({
# #         "role":"restaurant" , 
# #         "user_id":restaurant})

# #     for restaurant in restaurants:
# #         food_menu.append(InlineKeyboardButton(
# #             restaurant, callback_data='food_'+restaurant))


# food_menu = [
#     InlineKeyboardButton(text ='Tibs' ,callback_data='food_Tibs') ,
#     InlineKeyboardButton(text ='Pasta' ,callback_data='food_Pasta') ,
#     InlineKeyboardButton(text ='Pizza' ,callback_data='food_Pizza') ,
#     InlineKeyboardButton(text ='Bule' ,callback_data='food_Bule') 
#     ]

# food_menu = build_menu(food_menu, 1)

# async def make_accept_decline_keyboard(update,context):
#     accept_decline_keyboard = [
#         InlineKeyboardButton(text ='Accept' ,callback_data='accept_'+context.user_data['']),
#         InlineKeyboardButton(text ='Reject' ,callback_data='reject_') ,
#         ]