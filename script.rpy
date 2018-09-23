# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。




init python:
    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        """
        Represents a section of the tutorial menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)


    Section(_("In Depth"))

    Tutorial("starter2", _("Screen Basics"), move=None)






label start:
    
    menu:
        "从头开始":
            jump starter_start

        "跳过开头":
            jump meet


label meet:
    call meet_start

    call routine_start

    pause

    return
