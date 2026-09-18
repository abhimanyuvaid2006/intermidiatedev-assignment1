from email_validator import validate_email, EmailNotValidError

class Client():

    def __init__(
            self,
            client_id: int,
            name: str,
            email_address: str): 
        """Represents a client of a financial institution.

        Raises:
            ValueError: If client_id is less than or equal to zero.
            ValueError: If name is an empty string.
            EmailNotValidError: If email_address is not a valid email address.
        """
        if client_id <= 0:
            raise ValueError("client_id must be a value greater than zero")

        name = name.strip()
        if len(name) == 0:
            raise ValueError("name cannot be an empty string")

        validated_email = validate_email(email_address, check_deliverability=False)
        email_address = validated_email.normalized

        self.__client_id = client_id
        self.__name = name
        self.__email_address = email_address
    @property
    def client_id(self) -> int:
        return self.__client_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email_address(self) -> str:
        return self.__email_address

    @email_address.setter
    def email_address(self, email_address: str) -> None:
        """Sets the email address.

        Raises:
            EmailNotValidError: If email_address is not a valid email address.
        """
        validated_email = validate_email(email_address, check_deliverability=False)
        self.__email_address = validated_email.normalized