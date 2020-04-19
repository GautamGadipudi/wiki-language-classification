def put_lines_into_file(file_path: str, lines: list):
    try:
        file = open(file_path, 'w', encoding='latin-1')
        for line in lines:
            file.writelines(line + '\n')
    except IOError as e:
        print('File error!')
        print(e)
    except Exception as e:
        print('Some other error!')
        print(e)
    finally:
        if not file.closed:
            file.close()