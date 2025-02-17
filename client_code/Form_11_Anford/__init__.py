from ._anvil_designer import Form_11_AnfordTemplate
from anvil import *


class Form_11_Anford(Form_11_AnfordTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def navigation_link_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    pass
