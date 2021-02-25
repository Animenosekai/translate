class Unselected():
    """When the user decides not to use the translator"""
    def __init__(self, *args, **kwargs) -> None:
        pass

    def translate(self, *args, **kwargs) -> tuple[None, None]:
        """
        Args:
          *args: 
          **kwargs: 

        Returns:

        """
        return None, None

    def transliterate(self, *args, **kwargs) -> tuple[None, None]:
        """
        Args:
          *args: 
          **kwargs: 

        Returns:

        """
        return None, None

    def spellcheck(self, *args, **kwargs) -> tuple[None, None]:
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

    def example(self, *args, **kwargs) -> tuple[None, None]:
        """
        Args:
          *args: 
          **kwargs: 

        Returns:

        """
        return None, None

    def __repr__(self) -> str:
        return "N/A"