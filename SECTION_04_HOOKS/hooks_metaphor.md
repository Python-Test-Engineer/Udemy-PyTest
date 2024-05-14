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

You can register a HOOK for them.

You tell them:

You can contact me and I will then do what you want but you must specify this in this way:

[HOOK_SPEC] - [HOOK_IMPL:function_name(*args)]

Example:

You want me to order food from STORE_A and the items are ['apples', 'bananas']

You must send the functions with the right function name and arguments and then I can do that for you.

You send:
              do_place_food_order(name_of_store,[products])

[MID_MORNING] - [HOOK_IMPL:do_place_food_order('WALMART',['apples', 'bananas'])]

As you have complied with the HOOK_SPEC and passed in the correct HOOK_IMPL, I can then do this for you.

If there are errors in what you send, I am unable to fulfil the hook, e.g. you send me:

[MID_MORNING] - [HOOK_IMPL:_food_order('WALMART',['apples', 'bananas'])]
[10AM] - [HOOK_IMPL:do_place_food_order('WALMART',['apples', 'bananas'])]
[MID_MORNING] - [HOOK_IMPL:do_place_food_order(['apples', 'bananas'])]

I will not be able to do the hook.