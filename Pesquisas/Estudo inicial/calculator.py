# calculator.py

def add(numbers: str) -> int:
    if not numbers:
        return 0

    if ',\n' in numbers:
        raise ValueError("Input inválido.")

    numbers_list = [int(num) for num in numbers.replace('\n', ',').split(',')]
    return sum(numbers_list)

def test_add_string_vazia():
    result = add('')
    assert result == 0, f"Esperado: 0, Obtido: {result}"

def test_add_unico_numero():
    result = add('5')
    assert result == 5, f"Esperado: 5, Obtido: {result}"

def test_varios_numeros():
    result = add('2,3,5, 4, 5')
    assert result == 19

def test_add_new_lines_as_separator():
    result = add('1,2\n3')
    assert result == 6, f"Esperado: 6, Obtido: {result}"

def test_input_invalido_quebra_de_linha():
    try:
        add('2,\n3')
        assert False
    except ValueError as e:
        assert str(e) == "Input inválido."

if __name__ == "__main__":
    numero1 = int(input('Insira o primeiro número: '))
    numero2 = int(input('Insira o segundo número: '))
    print(add(f"{numero1},{numero2}"))
