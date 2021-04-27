from loader import Downloader
def main():
    dl = Downloader(cookie=cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
