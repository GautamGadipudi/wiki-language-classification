def get_lines_from_file(file_path: str) -> list:
    try:
        file = open(file_path, 'r', encoding='utf-8')
        lines = file.readlines()
        return lines
    except IOError as e:
        print('File error!')
        print(e)
    except Exception as e: 
        print('Some other error!')
        print(e)
    finally:
        if not file.closed:
            file.close()