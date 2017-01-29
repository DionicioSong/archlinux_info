# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Default(ColorScheme):
    progress_bar_color = 222

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                bg = 203
            if context.border:
                fg = default
            if context.media:
                if context.image:
                    fg = 215
                else:
                    fg = 207
            if context.container:
                fg = 135
            if context.directory:
                attr |= bold
                fg = 75
            elif context.executable and not \
                    any((context.media, context.container,
                        context.fifo, context.socket)):
                attr |= bold
                fg = 42
            if context.socket:
                fg = magenta
                attr |= bold
            if context.fifo or context.device:
                fg = 215
                if context.device:
                    attr |= bold
            if context.link:
                fg = cyan
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (203, magenta):
                    fg = white
                else:
                    fg = 203
            if not context.selected and (context.cut or context.copied):
                fg = black
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = black
                    bg = 222
            if context.badinfo:
                if attr & reverse:
                    bg = magenta
                else:
                    fg = magenta

        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg = context.bad and 203 or 222
            elif context.directory:
                fg = blue
            elif context.tab:
                if context.good:
                    bg = 42
            elif context.link:
                fg = cyan

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = 208
                elif context.bad:
                    fg = 207
            if context.marked:
                attr |= bold | reverse
                fg = 215
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = 203
            if context.loaded:
                bg = self.progress_bar_color
            if context.vcsinfo:
                fg = blue
                attr &= ~bold
            if context.vcscommit:
                fg = 215
                attr &= ~bold


        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = blue

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color


        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = magenta
            elif context.vcschanged:
                fg = 203
            elif context.vcsunknown:
                fg = 203
            elif context.vcsstaged:
                fg = 42
            elif context.vcssync:
                fg = 42
            elif context.vcsignored:
                fg = default

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync:
                fg = 42
            elif context.vcsbehind:
                fg = 203
            elif context.vcsahead:
                fg = blue
            elif context.vcsdiverged:
                fg = magenta
            elif context.vcsunknown:
                fg = 203

        return fg, bg, attr
