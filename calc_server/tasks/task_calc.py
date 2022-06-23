from controller.calc_controller import CalcController
from tasks import app


@app.task(name='SOMAR')
def add(arg01: int, arg02: int):
    print('Chamado SOMAR...')
    result = CalcController.add(arg01, arg02)
    print(f'O Resultado foi = {result}')
