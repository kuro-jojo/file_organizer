import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] %(message)s %(asctime)s",
    handlers=[logging.FileHandler("file_organizer.log"), logging.StreamHandler()],
)

DIRECTORY_TO_ORGANIZE_PATH = os.getenv("DIRECTORY_TO_ORGANIZE_PATH")

documents_extension = {
    "doc": "word",
    "docx": "word",
    "pdf": "pdf",
    "txt": "simple_text",
    "ppt": "powerpoint",
    "pptx": "powerpoint",
    "xls": "excel",
    "xlsx": "excel",
    "csv": "excel",
}

images_extension = ["jpg", "jpeg", "png", "gif", "svg", "bmp", "tiff", "ico"]

videos_extension = [
    "mp4",
    "avi",
    "mov",
    "wmv",
    "flv",
    "3gp",
    "mkv",
    "webm",
    "mpg",
    "mpeg",
    "m4v",
]

audios_extension = [
    "mp3",
    "wav",
    "wma",
    "ogg",
    "aac",
    "flac",
    "alac",
    "aiff",
    "pcm",
    "aax",
    "m4a",
]

compressed_extension = [
    "zip",
    "rar",
    "7z",
    "tar",
    "gz",
    "bz2",
    "xz",
    "z",
    "iso",
    "dmg",
    "pkg",
    "deb",
    "rpm",
    "sit",
    "sitx",
]

dpkg_extension = {
    "deb": "dpkg",
}

scripts_extension = {
    "py": "python",
    "js": "javascript",
    "bash": "bash",
    "sh": "bash",
}


def get_extension(file: str):
    return file.split(".")[-1]


def move_file(file: str, folder: str):
    if os.path.exists(f"{DIRECTORY_TO_ORGANIZE_PATH}/{file}"):
        if not os.path.exists(folder):
            logging.info(f"Creating {folder}")
            os.makedirs(folder)
        logging.info(f'Moving "{file}" to {folder}')
        os.rename(f"{DIRECTORY_TO_ORGANIZE_PATH}/{file}", folder + "/" + file)


if DIRECTORY_TO_ORGANIZE_PATH:
    with os.scandir(DIRECTORY_TO_ORGANIZE_PATH) as directory:
        for file in directory:
            if file.is_file():
                file_name = file.name
                file_extension = get_extension(file_name)
                if file_extension in documents_extension:
                    move_file(
                        file_name,
                        f"{DIRECTORY_TO_ORGANIZE_PATH}/documents/{documents_extension.get(file_extension)}",
                    )
                elif file_extension in images_extension:
                    move_file(file_name, f"{DIRECTORY_TO_ORGANIZE_PATH}/images")
                elif file_extension in videos_extension:
                    move_file(file_name, f"{DIRECTORY_TO_ORGANIZE_PATH}/videos")
                elif file_extension in audios_extension:
                    move_file(file_name, f"{DIRECTORY_TO_ORGANIZE_PATH}/audios")
                elif file_extension in compressed_extension:
                    move_file(file_name, f"{DIRECTORY_TO_ORGANIZE_PATH}/compressed")
                elif file_extension in dpkg_extension:
                    move_file(file_name, f"{DIRECTORY_TO_ORGANIZE_PATH}/dpkg")
                elif file_extension in scripts_extension:
                    move_file(
                        file_name,
                        f"{DIRECTORY_TO_ORGANIZE_PATH}/scripts/{scripts_extension.get(file_extension)}",
                    )
