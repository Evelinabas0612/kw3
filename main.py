from utils import get_json, filter_data, sort_data, format_data


def main():
    data = get_json()
    #print('Данные из json')
    #print(data)
    data = filter_data(data)
    #print('Отфильтрованные данные из json')
    #print(data)
    data = sort_data(data)
    #print('Отсортированные данные по времени из json')
    #print(data)
    #print(len(data))
    data = format_data(data)
    #print('Отформатированные данные')
    for row in data:
        print(row)



if __name__ == '__main__':
    main()


