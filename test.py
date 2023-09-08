date_str = "The 08 of September, 2023"

# Используйте str.replace() для удаления нуля перед днем
formatted_date = date_str.replace(" 0", " ")

print(formatted_date)  # Результат: "The 8 of September, 2023"