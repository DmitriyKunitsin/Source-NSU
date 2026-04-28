"""
Лабораторная работа №1: Атаки на шифр Цезаря
main.py – консольное меню демонстрации всех сценариев
"""

import os
from caesar import (
    caesar_encrypt,
    caesar_decrypt,
    known_plaintext_attack,
    ciphertext_only_attack,
    load_dictionary,
    auto_detect_key
)


def print_menu():
    """Вывод списка доступных действий."""
    print("\n" + "=" * 50)
    print("ШИФР ЦЕЗАРЯ – ЛАБОРАТОРНАЯ РАБОТА")
    print("=" * 50)
    print("1. Зашифровать текст")
    print("2. Расшифровать текст (известен ключ)")
    print("3. Атака по известному открытому тексту (KPA)")
    print("4. Атака по шифротексту (вывод 26 вариантов)")
    print("5. Автоматическое определение ключа (словарь)")
    print("6. Выход")
    print("-" * 50)


def main():
    """_summary_
    """
    dictionary = None
    dict_path = "words.txt"
    if os.path.exists(dict_path):
        try:
            dictionary = load_dictionary(dict_path)
            print(f"Словарь загружен: {len(dictionary)} слов.")
        except Exception as e:
            print(f"Ошибка загрузки словаря: {e}")
    else:
        print("Файл словаря не найден. Пункт 5 будет недоступен.")

    while True:
        print_menu()
        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":
            # Зашифрование
            text = input("Введите текст для шифрования: ")
            try:
                key = int(input("Введите ключ (0-25): "))
                if not 0 <= key <= 25:
                    print("Ошибка: ключ должен быть от 0 до 25.")
                    continue
            except ValueError:
                print("Ошибка: ключ должен быть целым числом.")
                continue
            encrypted = caesar_encrypt(text, key)
            print(f"Зашифрованный текст: {encrypted}")

        elif choice == "2":
            # Расшифрование с ключом
            text = input("Введите текст для расшифрования: ")
            try:
                key = int(input("Введите ключ (0-25): "))
                if not 0 <= key <= 25:
                    print("Ошибка: ключ должен быть от 0 до 25.")
                    continue
            except ValueError:
                print("Ошибка: ключ должен быть целым числом.")
                continue
            decrypted = caesar_decrypt(text, key)
            print(f"Расшифрованный текст: {decrypted}")

        elif choice == "3":
            # Атака по известному открытому тексту
            plain = input("Введите известный открытый текст: ")
            cipher = input("Введите соответствующий шифротекст: ")
            try:
                key = known_plaintext_attack(plain, cipher)
                print(f"Найденный ключ: {key}")
                # Дополнительно покажем расшифровку всего шифротекста
                full_decrypt = caesar_decrypt(cipher, key)
                print(f"Расшифрованный текст: {full_decrypt}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            # Атака по шифротексту (вывод всех 26 вариантов)
            cipher = input("Введите шифротекст: ")
            variants = ciphertext_only_attack(cipher)
            print("\nВсе варианты расшифрования:")
            for k in range(26):
                print(f"Ключ {k:2}: {variants[k]}")

        elif choice == "5":
            # Автоматическое определение ключа через словарь
            if dictionary is None:
                print("Словарь не загружен. Невозможно выполнить операцию.")
                continue
            cipher = input("Введите шифротекст: ")
            best_key = auto_detect_key(cipher, dictionary)
            best_plain = caesar_decrypt(cipher, best_key)
            print(f"Предполагаемый ключ: {best_key}")
            print(f"Расшифрованный текст: {best_plain}")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")


if __name__ == "__main__":
    main()
