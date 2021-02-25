from typing import Union
from translatepy.utils.annotations import Tuple, List, Dict

class Unselected():
    """When the user decides not to use the translator"""
    def __init__(self, *args, **kwargs) -> None:
        pass

    def translate(self, *args, **kwargs) -> Tuple[None, None]:
        """
        Args:
          *args: 
          **kwargs: 

        Returns:

        """
        return None, None

    def transliterate(self, *args, **kwargs) -> Tuple[None, None]:
        """
        Args:
          *args: 
          **kwargs: 

        Returns:

        """
        return None, None

    def spellcheck(self, *args, **kwargs) -> Tuple[None, None]:
        """
        Args:
          *args: 
          **kwargs: 

        Returns:

        """
        return None, None

    def language(self, *args, **kwargs) -> None:
        """
        Args:
          *args: 
          **kwargs: 

        Returns:

        """
        return None

    def example(self, *args, **kwargs) -> Tuple[None, None]:
        """
        Args:
          *args: 
          **kwargs: 

        Returns:

        """
        return None, None

    def dictionary(self, text, destination_language, source_language=None) -> Union[Tuple[str, Dict], Tuple[None, None]]:
      """
        Args:
          *args: 
          **kwargs: 

        Returns:

      """
      return None, None

    def __repr__(self) -> str:
        return "N/A"