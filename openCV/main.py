import functions as func
import image as CVimg
import subprocess

def main():
    print("Compare an image, take a Template image, Sync files from camera or Quit?")
    operation = input("C/T/S/Q ")
    operation = operation.lower()
    if (operation == "c"):
        name = input("Specify an image name: ")
        imgName = CVimg.takeImage(name)
        print("Select image to compare against ")
        subprocess.run("dir C:/users/oliver/Downloads/picam/templates")
        template = input()
        CVimg.compare(imgName, template)
    elif (operation == "t"):
        CVimg.setTemplateImage()
    elif (operation == "s"):
        func.syncDir()
    else:
        return

main()