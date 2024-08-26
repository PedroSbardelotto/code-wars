"""
Defina uma função que recebe um argumento inteiro e retorna um valor lógico, truedependendo falsese o inteiro é primo.

Segundo a Wikipédia, um número primo (ou um primo) é um número natural maior que 1aquele que não possui divisores positivos além de 1ele mesmo.

Requisitos
Você pode assumir que receberá uma entrada de valor inteiro.
Você não pode assumir que o inteiro será somente positivo. Você pode receber números negativos também ( ou 0).
NOTA sobre desempenho : Não há otimizações sofisticadas necessárias, mas ainda assim as soluções mais triviais podem ter tempo limite. Os números vão até 2^31 (ou similar, dependendo da linguagem). Fazer um loop até n, ou n/2, será muito lento.

"""

def is_prime(num):
  """Verifica se um número é primo."""
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    print(f"Verificando divisibilidade por {i} e {i+2}")
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True
