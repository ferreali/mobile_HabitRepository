from abc import ABC, abstractmethod

# Interface
class HabitRepository(ABC):

    @abstractmethod
    def criar_habito(self, habito):
        pass

    @abstractmethod
    def listar_habitos(self):
        pass

    @abstractmethod
    def atualizar_habito(self, id, novo_habito):
        pass

    @abstractmethod
    def deletar_habito(self, id):
        pass


# Implementação da interface
class HabitRepositoryMemoria(HabitRepository):

    def __init__(self):
        self.habitos = []

    def criar_habito(self, habito):
        self.habitos.append(habito)
        print("Hábito criado!")

    def listar_habitos(self):
        return self.habitos

    def atualizar_habito(self, id, novo_habito):
        if 0 <= id < len(self.habitos):
            self.habitos[id] = novo_habito
            print("Hábito atualizado!")
        else:
            print("ID não encontrado.")

    def deletar_habito(self, id):
        if 0 <= id < len(self.habitos):
            removido = self.habitos.pop(id)
            print(f"Hábito '{removido}' removido!")
        else:
            print("ID não encontrado.")


# Testando
repositorio = HabitRepositoryMemoria()

repositorio.criar_habito("Beber água")
repositorio.criar_habito("Estudar Python")

print(repositorio.listar_habitos())

repositorio.atualizar_habito(1, "Estudar Mobile")

print(repositorio.listar_habitos())

repositorio.deletar_habito(0)

print(repositorio.listar_habitos())
