from pathlib import Path
from typing import Dict, Tuple

EN_LOWER = "abcdefghijklmnopqrstuvwxyz"
EN_UPPER = EN_LOWER.upper()

RU_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RU_UPPER = RU_LOWER.upper()


def read_text_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as fh:
        return fh.read()


def write_text_file(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def build_alphabets(language: str) -> Tuple[str, str]:
    lang = language.strip().lower()
    if lang == "en":
        return EN_LOWER, EN_UPPER
    if lang == "ru":
        return RU_LOWER, RU_UPPER
    raise ValueError(f"Неподдерживаемый язык: {language!r}")


def normalize_shift(shift: int, alphabet_length: int) -> int:
    return shift % alphabet_length


def caesar_cipher_text(text: str, shift: int, lower_alpha: str, upper_alpha: str) -> str:
    result_chars = []
    n = len(lower_alpha)

    lower_index: Dict[str, int] = {ch: i for i, ch in enumerate(lower_alpha)}
    upper_index: Dict[str, int] = {ch: i for i, ch in enumerate(upper_alpha)}

    for ch in text:
        if ch in lower_index:
            i = lower_index[ch]
            new_i = (i + shift) % n
            result_chars.append(lower_alpha[new_i])
        elif ch in upper_index:
            i = upper_index[ch]
            new_i = (i + shift) % n
            result_chars.append(upper_alpha[new_i])
        else:
            result_chars.append(ch)

    return "".join(result_chars)


def make_output_path(input_path: Path, shift: int, language_tag: str) -> Path:
    parent = input_path.parent
    stem = input_path.stem
    suffix = input_path.suffix or ".txt"
    base_name = f"{stem}_cesar_{shift}_{language_tag}{suffix}"
    out_path = parent / base_name

    counter = 1
    while out_path.exists():
        out_path = parent / f"{stem}_cesar_{shift}_{language_tag}_{counter}{suffix}"
        counter += 1

    return out_path


def prompt_input_file() -> Path:
    while True:
        raw = input("Введите путь до исходного файла: ").strip()
        if raw == "":
            raise SystemExit("Отменено пользователем")
        path = Path(raw).expanduser()
        if not path.is_file():
            print(f"Файл не найден по пути: {path}, повторите ещё раз")
            continue
        return path


def prompt_shift() -> int:

    while True:
        s = input("Введите целочисленный сдвиг: ").strip()
        try:
            val = int(s)
        except ValueError:
            print("Неверно, введите целое число")
            continue

        if val <= 0:
            print("Сдвиг должен быть положительным")
            continue

        return val


def prompt_language() -> str:
    while True:
        s = input("Введите язык текста 'en' или 'ru': ").strip().lower()
        if s in ("en", "ru"):
            return s
        print("Язык выбран неверно, введите 'en'(английский) или 'ru'(русский)).")


def check_language_and_abort(text: str, chosen_lang: str) -> None:
    has_en = any(ch in EN_LOWER or ch in EN_UPPER for ch in text)
    has_ru = any(ch in RU_LOWER or ch in RU_UPPER for ch in text)

    if chosen_lang == "ru" and has_en:
        print("Содержимое вашего файла на другом языке, выберите именно его при шифровании")
        raise SystemExit
    elif chosen_lang == "en" and has_ru:
        print("Содержимое вашего файла на другом языке, выберите именно его при шифровании")
        raise SystemExit


def main() -> None:
    try:
        input_path = prompt_input_file()
    except SystemExit as exc:
        print(exc)
        return

    shift_raw = prompt_shift()
    lang_raw = prompt_language()

    try:
        lower_alpha, upper_alpha = build_alphabets(lang_raw)
    except ValueError as exc:
        print(exc)
        return

    shift = normalize_shift(shift_raw, len(lower_alpha))

    try:
        text = read_text_file(input_path)
    except Exception as exc:
        print(f"Ошибка при чтении файла {input_path}: {exc}")
        return

    try:
        check_language_and_abort(text, lang_raw)
    except SystemExit:
        return

    ciphered = caesar_cipher_text(text, shift, lower_alpha, upper_alpha)

    lang_tag = "en" if lang_raw.startswith("en") else "ru"
    output_path = make_output_path(input_path, shift_raw, lang_tag)
    try:
        write_text_file(output_path, ciphered)
    except Exception as exc:
        print(f"Ошибка при записи файла {output_path}: {exc}")
        return

    print(f"Зашифрованный файл сохранён по пути: {output_path}")


if __name__ == "__main__":
    main()
