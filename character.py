import logging
import random

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""


class Character:
    """Represent a character in the game"""
    def __init__(self, name: str, life: float = 100, attack: float = 20, defense: float = 0.1):
        self._name = name
        self._life = life
        self._attack = attack
        self._defense = defense

    def take_damage(self, damage_value: float) -> None:
        """Apply damage to the character after defense reduction"""
        reduced_damage = damage_value * (1 - self._defense)
        self._life -= max(0, reduced_damage)
        if self._life <= 0:
            self._life = 0
            log.info(f"{self._name} is dead")

    def attack(self, target: "Character") -> None:
        """Attack another character"""
        if not isinstance(target, Character):
            raise CharacterError("Target must be a Character")
        log.info(f"{self._name} attacks {target._name} for {self._attack} damage")
        target.take_damage(self._attack)
    

    @property
    def name(self) -> str:
        """Return the name of the character"""
        return self._name

    @property
    def is_dead(self) -> bool:
        """Check if the character is dead"""
        return self._life <= 0

    def __repr__(self) -> str:
        """Representation of the character"""
        return f"{self._name} <{self._life:.3f}>"


class Weapon:
    """Represent a weapon in the game"""
    def __init__(self, name: str, attack: float):
        self._name = name
        self._attack = attack

    @classmethod
    def default(cls):
        """Create a default weapon"""
        return cls("Wood stick", 1)

    @property
    def name(self) -> str:
        """Return the name of the weapon"""
        return self._name

    @property
    def attack(self) -> float:
        """Return the attack value of the weapon"""
        return self._attack

    def __repr__(self) -> str:
        return f"Weapon({self._name}, Attack: {self._attack})"


class Warrior(Character):
    """Represent a warrior character"""
    def __init__(self, name: str, weapon: Weapon = None):
        super().__init__(name, life=150, attack=20, defense=0.12)  
        self.weapon = weapon if weapon else Weapon.default() 

    @property
    def is_raging(self) -> bool:
        """Check if the warrior is in rage mode (health < 20% of max health)"""
        return self._life < 0.2 * 150  

    def attack(self, target: Character) -> None:
        """Attack a target with weapon and rage bonus"""
        total_attack = self._attack + self.weapon.attack
        if self.is_raging:
            total_attack *= 1.2  
        log.info(f"{self._name} attacks {target.name} with {total_attack:.2f} damage")
        target.take_damage(total_attack)

    def __repr__(self) -> str:
        return f"Warrior({self._name}, Health: {self._life:.3f}, Attack: {self._attack}, Defense: {self._defense}, Weapon: {self.weapon})"


class Magician(Character):
    """Represent a magician character"""
    def __init__(self, name: str):
        super().__init__(name, life=80, attack=40, defense=0.1)  

    def _activate_magical_shield(self) -> bool:
        """Activate magical shield with a 1/3 chance"""
        return random.randint(1, 3) == 1

    def take_damage(self, damage_value: float) -> None:
        """Take damage with a chance to activate magical shield"""
        if self._activate_magical_shield():
            log.info(f"{self._name} activated magical shield and took no damage")
            return
        super().take_damage(damage_value)

    def __repr__(self) -> str:
        return f"Magician({self._name}, Health: {self._life:.3f}, Attack: {self._attack}, Defense: {self._defense})"


def main():

    warrior = Warrior("Conan")
    magician = Magician("Merlin")
    sword = Weapon("Sword", attack=15)
    warrior.weapon = sword
    print(warrior)
    print(magician)
    warrior.attack(magician)
    print(magician)
    magician.attack(warrior)
    print(warrior)


if __name__ == "__main__":
    main()
