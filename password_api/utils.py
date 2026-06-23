import string
import secrets

SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:,.<>?"


def build_alphabet_and_requirements(use_upper: bool, use_digits: bool, use_special: bool) -> tuple[str, list]:
    """Construit l'alphabet disponible et la liste des critères de validation.

    Cette fonction interne analyse les options choisies pour générer la table de caractères
    et une liste de fonctions anonymes (lambda) pour valider la présence de chaque type de caractère.

    Args:
        use_upper (bool): Activer les majuscules.
        use_digits (bool): Activer les chiffres.
        use_special (bool): Activer les caractères spéciaux.

    Returns:
        tuple[str, list]: Une chaîne contenant tout l'alphabet possible et une liste de fonctions de validation.
    """
    alphabet = string.ascii_lowercase
    requirements = [lambda psw: any(c.islower() for c in psw)]

    if use_upper:
        alphabet += string.ascii_uppercase
        requirements.append(lambda psw: any(c.isupper() for c in psw))

    if use_digits:
        alphabet += string.digits
        requirements.append(lambda psw: any(c.isdigit() for c in psw))

    if use_special:
        alphabet += SPECIAL_CHARACTERS
        requirements.append(lambda psw: any(c in SPECIAL_CHARACTERS for c in psw))

    return alphabet, requirements


def password_generator(length: int = 8, use_upper: bool = False, use_digits: bool = False,
                       use_special: bool = False) -> str:
    """Génère un mot de passe aléatoire hautement sécurisé selon les critères fournis.

    Args:
        length (int, optional): La longueur du mot de passe. Minimum 5. Defaults to 8.
        use_upper (bool, optional): Inclure des majuscules. Defaults to False.
        use_digits (bool, optional): Inclure des chiffres. Defaults to False.
        use_special (bool, optional): Inclure des caractères spéciaux. Defaults to False.

    Raises:
        ValueError: Si la longueur demandée est inférieure ou égale à 4.

    Returns:
        str: Le mot de passe généré répondant à toutes les exigences.
    """
    if length <= 4:
        raise ValueError(f"The password length must be longer than 4 characters (received: {length}).")

    alphabet, requirements = build_alphabet_and_requirements(use_upper, use_digits, use_special)

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        if all(check_condition(password) for check_condition in requirements):
            return password
