Let's create a real world example of hooks.

You work and are very busy during the day but have 3 times when you are available to take calls and do things:

MID_MORNING
LUNCH
MID_AFTERNOON

At these times you do some functions:

do_place_food_order(name_of_store,[products])
do_prepare_accounts()

Your family also want to do these functions.

MID_MORNING
LUNCH
MID_AFTERNOON

are hooks in your day where others can connect with you as you are busy doing other things outside of these times.

These are like the points in PyTest where PyTest executes those functions.

You can register a HOOK for them.

You tell them:

You can send the request at any time and when I reach one of my hook points, I will look at the list of requests and find those with the same function names and the correct arguments.
L:function_name(*args)

Example:

You want me to order food from STORE_A and the items are ['apples', 'bananas']

You must send the functions with the right function name and arguments and then I can do that for you.

You send:
    do_place_food_order(name_of_store,[products])
              
    correct function name and arguments:
    [MID_MORNING] do_place_food_order('WALMART',['apples', 'bananas'])


Failled implementations:

    incorrect function name:
    [MID_MORNING] [_food_order('WALMART'),['apples', 'bananas']]

    incorrect set of arguments:
    [LUNCH]  [do_place_food_order(['apples', 'bananas'])]

    I will not be able to do the hook.