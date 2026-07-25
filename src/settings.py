from pathlib import Path

DOWNLOADS_DIR = "/home/rai/Desktop/fake_downloads"
DOWNLOADS_PATH = Path(DOWNLOADS_DIR)

DIRECTORIES = {
        "html": (".html5", ".html", ".htm", ".xhtml"),
        "images": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   ".svg",
                   ".heif", ".psd"),
        "videos": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "documents": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      ".pptx"),
        "archives": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "audio": (".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"),
        "plaintext": (".txt", ".in", ".out"),
        "pdf": (".pdf",),
        "python": (".py",),
        "exe": (".exe",),
        "miscs" : ()
    }

EXTENSION_LIST = [
    ".html5", ".html", ".htm", ".xhtml", 
    ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd", 
    ".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv", 
    ".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", 
    ".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip", 
    ".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma", 
    ".txt", ".in", ".out", 
    ".pdf", 
    ".py", 
    ".exe"
    ]

FOLDER_LIST = ["html", "images", "videos", "documents", "archives", "audio", "plaintext", "pdf", "python", "exe", "miscs"]

folder_path_list = [ DOWNLOADS_PATH / folder for folder in FOLDER_LIST]
MISCS_PATH = DOWNLOADS_PATH / "miscs"