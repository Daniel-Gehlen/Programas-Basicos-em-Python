def linear_interpolation(x_known, y_known, x_interp):
    """
    Realiza interpolação linear para um conjunto de dados uniformemente distribuídos.
    
    Args:
    x_known (list): Lista dos valores x conhecidos.
    y_known (list): Lista dos valores y conhecidos correspondentes.
    x_interp (float): Valor x para o qual deseja-se interpolar o valor y.
    
    Returns:
    float: Valor interpolado de y.
    """
    n = len(x_known)
    
    if n != len(y_known) or n == 0:
        raise ValueError("As listas x_known e y_known devem ter o mesmo tamanho e não podem ser vazias.")
    
    if x_interp < x_known[0] or x_interp > x_known[-1]:
        raise ValueError("O valor x_interp está fora do intervalo dos valores conhecidos.")
    
    # Encontra os índices dos dois pontos conhecidos mais próximos
    idx_left = 0
    idx_right = n - 1
    
    for i in range(1, n):
        if x_interp < x_known[i]:
            idx_right = i
            break
        idx_left = i
    
    # Realiza a interpolação linear
    x_left = x_known[idx_left]
    x_right = x_known[idx_right]
    y_left = y_known[idx_left]
    y_right = y_known[idx_right]
    
    slope = (y_right - y_left) / (x_right - x_left)
    y_interp = y_left + slope * (x_interp - x_left)
    
    return y_interp

# Exemplo de uso
x_known = [0, 1, 2, 3, 4, 5]
y_known = [0, 2, 4, 6, 8, 10]
x_interp = 2.5
y_interp = linear_interpolation(x_known, y_known, x_interp)
print(f"Para x = {x_interp}, a interpolação linear resulta em y = {y_interp}")

# Neste exemplo, temos um conjunto de dados conhecidos x_known e y_known que estão uniformemente
# distribuídos. A função linear_interpolation recebe esses valores, juntamente com um valor x_interp 
# para o qual queremos interpolar o valor correspondente de y. O algoritmo encontra os dois pontos
# conhecidos mais próximos do x_interp, calcula a inclinação entre eles e, em seguida,
# usa essa inclinação para estimar o valor interpolado de y.

# Vale ressaltar que a interpolação linear é apropriada quando você tem certeza de que os dados
# estão uniformemente distribuídos e que a variação entre os pontos é aproximadamente linear. 
# Em casos mais complexos, onde a relação entre os pontos não é linear, podem ser necessários
# métodos de interpolação mais avançados, como spline cúbico ou polinomial.







