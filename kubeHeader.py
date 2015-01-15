
      #########.
     ########",#:
   #########',##".
  ##'##'## .##',##.
   ## ## ## # ##",#.
    ## ## ## ## ##'
     ## ## ## :##
      ## ## ##."

import sublime, sublime_plugin

headers = [
  {
    'text' : """
      /*#######.
     ########",#:
   #########',##".
  ##'##'## .##',##.
   ## ## ## # ##",#.
    ## ## ## ## ##'
     ## ## ## :##
      ## ## ##*/

""",
    'extensions': [
      'tpp',
      'hpp',
      'cpp',
      'C',
      'H',
      'c',
      'h'
    ]
  },
  {
    'text' : """
      #########.
     ########",#:
   #########',##".
  ##'##'## .##',##.
   ## ## ## # ##",#.
    ## ## ## ## ##'
     ## ## ## :##
      ## ## ##."

""",
    'extensions': [
      'Makefile',
      'coffee',
      'sh',
      'py',
      'rb'
    ]
  }
]


class KubeHeaderCommand(sublime_plugin.TextCommand):

  def get_extension(self):
    if (self.view.file_name() == None):
      return None;
    return self.view.file_name().split('/')[-1].split('.')[-1]

  def get_header(self, edit):
    extension = self.get_extension()

    for header in headers:
      if extension in header['extensions']:
        return header;

    return headers[0]

  def insert_header(self, edit):
    header = self.get_header(edit);

    if (header['text'] != self.view.substr(sublime.Region(0, len(header['text'])))):
      self.view.insert(edit, 0, header['text'])

  def run(self, edit):
    self.insert_header(edit)
