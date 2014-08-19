Sublime Quick Project
=====================

This Sublime Text plugin is dead simple.

It creates a `.sublime-project` file in the root of your currently-opened folder.
This way, you don't have to "Save Project As..." every time you start a new project.


Usage
-----
* Open a folder
* Command Palette -> Quick Create Project

Now you have a `.sublime-project` file in that folder. Cool.

What does the `.sublime-project` file look like?
------------------------------------------------

It looks like this:
``` json
{
    "folders":
    [
        {
            "follow_symlinks": true,
            "path": "."
        }
    ]
}
```


What if I have multiple folders in my project?
----------------------------------------------

You're probably better off using the builtin "Save Project As..." menu option.
