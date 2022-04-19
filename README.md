# Bulk File Manager

A small utility to make browing media my way easier.

I like a broad selection of images or clips randomized, so I collect media, sort it to type, image, movie, or sound, then move individual files from that source to category directories further subdivided into numerical directories.

\~/Downloads will become<br>

|-audio<br>
||-0000<br>
||-0001<br>
|…………<br>
|-still<br>
||-0000<br>
||-0001<br>
|…………<br>
|-video<br>
||-0000<br>
||-0001<br>

  - Currently Linux only, MAC is easy enough for most people to figure out, and I have no access and even less desire to have access to Windows systems to test, that OS was confusing enough when I ran away screaming ages ago that I would probably break your system trying to help you figure out how to make this work on Windows.
    - There are many people on the Internet who are not so hateful toward Windows, and have a lot newer ideas about what may work today on the gross mess.
  - This is best installed in your user home if you want to modify my choices of extension, filename length, etc.
  - As is I suspect very few people enjoy their media in this way, so something fun to rip apart and learn from is probably what this is best suited for.
<br>
  - My CF module and it's deps is required.
    - The only one of those most people may want is the hashlib.
  - Other requirements are added for some features as follows:
    - `Random filenames` hashlib
  - bulkFileManager, bulkfilemanager, and bfm are installed to ~/.local/bin if no access to systemwide locations are available.
    - The same executables are installed in /usr/bin or /usr/local/bin
<br>
  - My favorite install method is:
    1. Download an archive from github.
    2. Unpack it into a temporary location.
    3. Change to the directory it has been unpacked into.
      - `cd \<directory\>`
    4. Tell pip to install it
      - `pip install --user .` for user install.
      - `sudo pip install .` for system wide install.
        - Pip will warn you about the potential issues with running it as the super user, if you fully understand that proceed, if not research and continue when you are aware of how this choice can damage your system.
  - I am probably not going to submit this to any of the collections of python code due to it's likely lack of benefit to most people.
<br>
  ## OPTIONS
  - Copy/move files from source to the distributed destinations.
  - Edit which category a file extention goes into, add or remove extensions from a category, etc.
    - You can add categories, test utilities per extension, etc. by editing the source file "configMe.py" before a systemwide install, or just edit the file "configMe.py" in the executable packages final location \(\~/local/lib/python*/site-packages/bulkFileManager/configMe.py\) for a user install.
  - Rename only to remove characters which cause issues for most OS options.
  - Rename randomly.
  - Test media files, disgarding or moving to an error directory any files which fail the basic tests configure in "configMe.py".
  - 
