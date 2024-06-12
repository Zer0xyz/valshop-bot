from random import choice, randint

def get_response(user_input: str) -> str:
    # TODO implement commands and responses

    lowered: str = user_input.lower()

    if 'hello' in lowered:
        return 'hello there'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
