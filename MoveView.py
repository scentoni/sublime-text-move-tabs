import sublime
import sublime_plugin


class MoveView(sublime_plugin.WindowCommand):

    def run(self, direction):
        window = sublime.active_window()
        view = window.active_view()
        view_index = window.get_view_index(view)

        if view_index == -1:
            return

        (group, index) = view_index

        if group < 0 or index < 0:
            return

        views = window.views_in_group(window.active_group())
        num_views = len(views)
        target_index = index

        if direction == 'left':
            if index > 0:
                index -= 1
        elif direction == 'right':
            if index < num_views - 1:
                index += 1
        elif direction == 'beginning':
            if index > 0:
                index = 0
        elif direction == 'end':
            if index < num_views - 1:
                index = num_views -1
        else:
            print 'Unrecognized direction:', direction + '. Use left, right, beginning, or end.'

        # Move the view
        if target_index != index:
            window.set_view_index(view, group, index)
