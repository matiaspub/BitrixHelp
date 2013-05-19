import sublime, sublime_plugin
import webbrowser

settings = sublime.load_settings("BitrixHelp.sublime-settings")

class BitrixHelpCommand(sublime_plugin.TextCommand):
	def run(self, edit, it='bitrixAPI'):
		pages = settings.get('pages').get(it)
		lst = [p.get('title') for p in pages]
		def on_done(index):
			if index == -1:
				return
			url = pages[index].get('link')
			sublime.status_message("open: "+str(url))
			webbrowser.open_new_tab(url)
		self.view.window().show_quick_panel(lst, on_done)
		