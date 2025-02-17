from ._anvil_designer import Form_12_EvalTemplate
from anvil import *


class Form_12_Eval(Form_12_EvalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def navigation_link_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    pass
