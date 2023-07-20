print("Loading....")
import functions.functions as func
import openCV.functions.image as CVimg
import os


def main():
    print(
        "Compare an image, take a Template image, Sync files from camera or Find board?"
    )
    operation = input("C/T/S/F ")
    operation = operation.lower()
    if operation == "c":
        name = input("Specify an image name: ")
        image = CVimg.takeComparisonImage(name)
        # sleep(1)
        print("Select image to compare against ")
        dir = os.listdir("C://Users//Oliver//Downloads//picam//templates")
        print(dir)
        template = input()
        template = "templates/" + template
        removeErrs = input(
            "Would you like to try and remove any errors in the image? (Y/N) "
        )
        removeErrs = str(removeErrs).lower()
        if removeErrs == "y":
            print("Removing errors...")
            CVimg.compare(image, template, True)
        else:
            CVimg.compare(image, template)

    elif operation == "t":
        CVimg.setTemplateImage()
    elif operation == "s":
        func.syncDir()
    elif operation == "f":
        print("What board/part would you like to find? ")
        dir = os.listdir("C://Users//Oliver//Downloads//picam//templates")
        print(dir)
        lookingFor = input(" ")
        lookingFor = "C:\\Users\\Oliver\\Downloads\\picam\\templates\\" + lookingFor
        print("Specify an image name: ")
        imageName = input(" ")
        image = CVimg.takeComparisonImage(imageName)  # just taken
        CVimg.findImageInImage(lookingFor, image, imageName)


main()
