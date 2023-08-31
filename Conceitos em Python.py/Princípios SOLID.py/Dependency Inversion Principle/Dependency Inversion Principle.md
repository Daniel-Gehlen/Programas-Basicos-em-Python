class LightBulb:
    def turn_on(self):
        return "Lâmpada ligada"

    def turn_off(self):
        return "Lâmpada desligada"

class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        if isinstance(self.device, Switchable):
            return self.device.turn_on()
        else:
            return "Dispositivo não pode ser ligado/desligado"

class ElectricSocket:
    def connect(self, device):
        return Switch(device)

bulb = LightBulb()
socket = ElectricSocket()
switch = socket.connect(bulb)

print(switch.operate())


# Neste exemplo, temos as classes LightBulb (lâmpada) e Switchable (interface para dispositivos
# que podem ser ligados/desligados). A classe Switch depende da abstração Switchable, permitindo
# que possa ser usado para controlar qualquer dispositivo que implemente essa interface.

# O princípio é atendido porque o módulo de alto nível (Switch) não está diretamente dependente 
# do módulo de baixo nível (LightBulb). Ambos dependem da abstração (Switchable), o que torna 
# o código mais flexível e permite que novos dispositivos que implementem Switchable sejam 
# adicionados sem alterar o código do Switch.

# O método operate() no Switch verifica se o dispositivo é uma instância de Switchable 
# antes de tentar ligá-lo, garantindo que apenas dispositivos compatíveis possam ser operados.

# Portanto, o exemplo exemplifica a inversão de dependência, onde os módulos de alto e
# baixo nível dependem de uma abstração em vez de dependerem diretamente uns dos outros. 
# Isso promove maior flexibilidade e extensibilidade do código.