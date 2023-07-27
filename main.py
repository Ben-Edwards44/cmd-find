import app.tool as tool
import app.check_setup as check_setup
import app.change_dir as change_dir





def main():
    check_setup.main()
    change_dir.change_to_main()
    tool.main()


if __name__ == "__main__":
    main()