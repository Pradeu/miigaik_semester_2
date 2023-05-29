import PySimpleGUI as sg
import os
import io
import docx2pdf
import pdf2docx
from PIL import Image


def pdf2docx_convert(pdf_path):
    docx_path = f'{pdf_path.replace(".pdf", ".docx")}'
    return pdf2docx.parse(pdf_path, docx_path)


def docx2pdf_convert(docx_path):
    pdf_path = f'{docx_path.replace(".docx", ".pdf")}'
    return docx2pdf.convert(docx_path, pdf_path)

def file_delete(file_dir, file_name):
    os.remove(f'{file_dir}' + r"/" + f"{file_name}")


layout = [
    [sg.Button('PDF -> Docx'),
     sg.Button('Docx -> PDF'),
     sg.Button('Сжатие изображений'),
     sg.Button('Удаление файлов')],
]
pic_format = str()
window = sg.Window('Office Tweaks', layout)

while True:
    event, values = window.read()
    if event == 'PDF -> Docx':
        file_types = [("PDF Files (.pdf)", ".pdf"),
                      ]
        layout = [
            [
                sg.Text("Файл PDF"),
                sg.Input(size=(25, 1), key="-FILE-"),
                sg.FileBrowse("Выбрать файл", file_types=file_types),
                sg.Button("Перевести PDF в docx"),
            ],
        ]
        window_1 = sg.Window("PDF Viewer", layout)
        while True:
            event, values = window_1.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Перевести PDF в docx":
                filename = values["-FILE-"]
                if os.path.exists(filename):
                    pdf2docx_convert(filename)

        window_1.close()
    elif event == 'Docx -> PDF':
        file_types = [("Документ Microsoft Word (.docx)", ".docx")]
        layout = [
            [
                sg.Text("Файл docx"),
                sg.Input(size=(25, 1), key="-FILE-"),
                sg.FileBrowse("Выбрать файл", file_types=file_types),
                sg.Button("Перевести docx в PDF"),
            ],
        ]
        window_2 = sg.Window("DOCX Viewer", layout)
        while True:
            event, values = window_2.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Перевести docx в PDF":
                filename = values["-FILE-"]
                if os.path.exists(filename):
                    docx2pdf_convert(filename)
        window_2.close()
    elif event == 'Сжатие изображений':
        file_types = [("JPEG (*.jpeg)", "*.jpeg"),
                      ("JPG (*.jpg)", "*.jpg"),
                      ("PNG (*.png)", "*.png")]
        layout = [
            [sg.Image(key="-IMAGE-")],
            [
                [sg.Text("Изображение"),
                 sg.Input(size=(25, 1), key="-FILE-"),
                 sg.FileBrowse("Выбрать файл", file_types=file_types),
                 sg.Button("Предпоказ"),
                 ],
                [sg.Text("Выберите процент сжатия", size=(15, 2), key="-OUTPUT-"),
                 sg.Input(size=(3, 2), key="-INPUT-"),
                 sg.Button("Сжать изображение")
                 ]
            ],
        ]
        window_3 = sg.Window("Image Viewer", layout)
        while True:
            event, values = window_3.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            filename = values["-FILE-"]
            if filename.endswith(".jpeg"):
                pic_format = ".jpeg"
            elif filename.endswith(".png"):
                pic_format = ".png"
            elif filename.endswith(".gif"):
                pic_format = ".gif"
            if event == "Предпоказ":
                if os.path.exists(filename):
                    image = Image.open(values["-FILE-"])
                    image.thumbnail((400, 400))
                    bio = io.BytesIO()
                    image.save(bio, format="PNG")
                    window_3["-IMAGE-"].update(data=bio.getvalue())
            if event == "Сжать изображение":
                if os.path.exists(filename):
                    image = Image.open(values["-FILE-"])
                    image.thumbnail((400, 400))
                    bio = io.BytesIO()
                    image.save(f'{filename.replace(pic_format,"_crop")}' + f"{pic_format}",
                               quality=100 - int(values["-INPUT-"]), optimize=True)

        window_3.close()
    elif event == "Удаление файлов":
        layout = [
                [sg.Text("Укажите подстроку/расширение: "),
                 sg.Input(size=(25, 1), key="-STROKE-"),
                 sg.Text("Выберите директорию: "),
                 sg.Input(size=(40, 1), key="-FOLDER-"),
                 sg.FolderBrowse("Выбор", initial_folder=os.getcwd())],
                [sg.Button("Удалить с подстрокой в начале"),
                 sg.Button("Удалить с подстрокой в конце"),
                 sg.Button("Удалить с подстрокой, содержащейся в файлах"),
                 sg.Button("Удалить все файлы по расширению")]
        ]
        window_4 = sg.Window("File Deleter", layout)
        while True:
            event, values = window_4.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            files_list = os.listdir(values["-FOLDER-"])
            if event == "Удалить с подстрокой в начале":
                for i in range(len(files_list)):
                    if files_list[i].startswith(values["-STROKE-"]):
                        file_delete(values["-FOLDER-"], files_list[i])
            if event == "Удалить с подстрокой в конце":
                files_list_2 = list()
                for i in range(len(files_list)):
                    files_list_2.append(files_list[i])
                for i in range(len(files_list_2)):
                    while True:
                        if not files_list_2[i].endswith("."):
                            files_list_2[i] = files_list_2[i][:len(files_list_2[i]) - 1]
                        else:
                            files_list_2[i] = files_list_2[i][:len(files_list_2[i]) - 1]
                            break
                for i in range(len(files_list)):
                    if files_list_2[i].endswith(values["-STROKE-"]):
                        file_delete(values["-FOLDER-"], files_list[i])
            if event == "Удалить с подстрокой, содержащейся в файлах":
                for i in range(len(files_list)):
                    if files_list[i].find(values["-STROKE-"]) != -1:
                        file_delete(values["-FOLDER-"], files_list[i])
            if event == "Удалить все файлы по расширению":
                for i in range(len(files_list)):
                    if files_list[i].endswith(values["-STROKE-"]):
                        file_delete(values["-FOLDER-"], files_list[i])
    elif event == sg.WINDOW_CLOSED or event == 'Quit':
        break
window.close()
