# Data structure 

## User =
    personal_info 
        name: string
        phone : numeric
        telegram_id : numeric
    state 
        is_banned : bool
        is_vip : bool 
    live_orders : list of orders
    order_history: list of orders

## Restaurant =

    phone : numeric
    location : string or lat, long

    is_currently_open : bool 
    working_hours : list of hours

    menu : list of meals
    orders : Queue of orders


## Order =

    issuer : User
    issued_for : Restaurant
    order_id : numeric
    ordered_meals : list of meals
    sum_price : numeric
    is_paid : bool
    state : string
        accepted
        prepared 
        dispatched
        delivered
        recieved 

## Meal =

    meal_code : numeric
    meal_name : string
    image_url : string
    price : numeric
    ingredients : list of ingredients

# Commands 
    
    [GeneralScope]{user}
        /start : starts the bot and also inits you 
        /register_as_restaurant : sets user with additional [restscope] perms
        /register_as_dispatcher : sets user with additional [dispatchscope] perms
        /register_for_vip : sets user with additional [vipscope] perms

    [VipScope]<[GeneralScope]
        /place_vip_order : places an order with special care

    [UserScope]
    {order}
        /place_order :  place order 
        /cancel_order : cancel unsubmitted order 
        /submit_order : no turning back 
        /list_placed_orders : list all orders 
        /order_recieved : order recieved by user 
    /rate : rate the restaurant
        {restaurant} : rate the restaurant
        {deliverer} : rate the deliverer


    [RestScope]
    {order}
        /accept_order : accept order 
        /reject_order : reject order 
        /list_pending_orders : list all orders 
        /dispatch_order : mark order as dispatched 
    {user}
        /ban_user : ban user
        /unban_user : unban user
    {restaurant}
        /set_working_hours : set working hours
        /set_location : set location
        /set_is_currently_open : set is currently open
        /clear_menu : clear menu
        {meal , restaurant{menu} }
        /add_meal : adds a meal to the restaurant menu 
        /remove_meal : remove a meal from the restaurant menu 

    [AdminScope] ;> find out lol 

    [DelivererScope]<[DispatcherScope]{order}
        /order_delivered : mark order as delivered
        /order_on_the_way : mark order as on the way
        /order_damaged : mark order as damaged on transit 





# Brainstorming 

    notify incoming 
    accept / decline
    see pending 
    mark pending 
    identify restaurants by phone 


    bot replies should update keyboards and states and talk text
     while user inputs should soley be MDkeyboard based , ie 
    click on inline buttons for orders and app keyboards for menus and so on

    use custom context types that get populated from db on startup 