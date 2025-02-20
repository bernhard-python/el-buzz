from ._anvil_designer import Form_14_EntscheidTemplate
from anvil import *


class Form_14_Entscheid(Form_14_EntscheidTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
