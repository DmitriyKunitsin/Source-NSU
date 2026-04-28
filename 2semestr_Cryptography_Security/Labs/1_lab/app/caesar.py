"""Methods for Labs Cesar"""


import re # Для работы с регулярными выражениями


def caesar_encrypt(text: str, key: int) -> str:
    """
    Функция шифрования
    Пробегает по тексту
    В зависимости от регистра или символ ли это
    Функция ord() для символа x вернет число, из таблицы символов Unicode
    Получается его последовательный номер, прибавляет ключ
    Ключ это типо на скок мы его шифруем ( смещаем )
    Благодаря остатку от деления получаем его положение плюс значение символа дефолтного
    """
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
        elif 'A' <= char <= 'Z':
            shifted = (ord(char) - ord('A') + key) % 26 + ord('A')
        else:
            shifted = ord(char)

        result.append(chr(shifted))
    return ''.join(result)


def caesar_decrypt(text: str, key: int) -> str:
    """Дешифрование благодаря инверсии ключа, 
    ключ при шифровании дешифровании должен быть одинаковый!!"""
    return caesar_encrypt(text, -key)


def known_plaintext_attack(plain: str, cipher: str) -> int:
    """
    Функция принимает plaintext и ciphertext,
    выбирает первую букву из plaintext и вычисляет ключ. 
    Валидация: проверка, что оба текста одинаковой длины и 
    содержат только латиницу (необязательно, но реализовано).

    Возвращает номер ключа
    """
    for p, c in zip(plain, cipher):
        if p.isalpha() and c.isalpha():
            p_pos = ord(p.lower()) - ord('a')
            c_pos = ord(c.lower()) - ord('a')
            key = (c_pos - p_pos) % 26
            return key
    raise ValueError("No valid letters found.")


def ciphertext_only_attack(cipher: str) -> dict[int, str]:
    """
    Функция последовательно расшифровывает текст ключами от 0 до 25 
    и выводит результат с указанием ключа.
    """
    return {k: caesar_decrypt(cipher, k) for k in range(26)}


def load_dictionary(filepath: str) -> set[str]:
    """_summary_

    Args:
        filepath (str): _description_

    Returns:
        set[str]: _description_
    """
    with open(filepath, 'r', encoding='utf8') as f:
        return set(word.strip().lower() for word in f)


def auto_detect_key(ciphertext: str, dictionary: set[str]) -> int:
    '''
    1.Для каждого ключа k, расшифровываею текст
    2.Разбираем расшифровку на слова
    3.Считаю сколько слов в словаре
    4.Выбираю ключ с максимальным количеством совпадений
    '''
    best_key = 0
    best_score = -1
    for k in range(26):
        plain = caesar_decrypt(ciphertext, k)
        # Разделение на слова, игнорируя знаки препинания через regex
        words = re.findall(r'\b[a-zA-Z]+\b', plain)
        score = sum(1 for w in words if w.lower() in dictionary)
        if score > best_score:
            best_score = score
            best_key = k
    return best_key
