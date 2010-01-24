import eyeD3
import uuid
import sys
import os
from options import OptionsLoader
from errors import *
from fileFilters import *
from fileMover import *
from organizer import *
from views.consoleView import ConsoleView
from views.formView import FormView

def Main():
    loader = OptionsLoader()
    options = loader.loadFromArguments(sys.argv)
    
    view = ConsoleView()

    directoryOrGui = options.rootDirectory
    if options.startGuiMode:
        print "Gui mode not implemented yet."
        return
    
    if not os.path.isdir(directoryOrGui):
        view.displayLine("Directory not found")
        view.displayLine(usage)
        return

    view.displayLine("Directory to organize is %s" % directoryOrGui)
    view.displayLine("Retrieving all MP3 files...")
    
    fileSource = FileSource(directoryOrGui)
    filter = Mp3FileFilter(fileSource)
    mp3files = filter.getFiles()

    view.displayLine("Directory contains %s MP3 files" % len(mp3files))
    
    tempFolder = os.path.join(directoryOrGui, str(uuid.uuid4()))
    view.displayLine("Moving files to temporary location %s..." % tempFolder)

    mover = FileMover(mp3files, tempFolder)
    tempFiles = mover.move()

    view.displayLine("Finding non MP3 files...")

    nonMp3FilesFilter = NonMp3FileFilter(fileSource)
    nonMp3Files = nonMp3FilesFilter.getFiles()

    for file in nonMp3Files:
        os.remove(file)

    view.displayLine("Directory contains %s non-MP3 files. Deleting..."
                     % len(nonMp3Files))
    view.displayLine("Organizing files...")

    organizer = Organizer(tempFiles, directoryOrGui)
    organizer.organize()

    view.displayLine("Done!")

if __name__ == "__main__":
    Main()


