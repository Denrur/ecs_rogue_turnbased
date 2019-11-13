from statemachine import StateMachine, State


class MovingMachine(StateMachine):
    walking = State('Walking', initial=True)
    enraged = State('Enraged')
    attack = State('Attack')

    moving = idle.to(move)
    stop = moving.to(idle)
