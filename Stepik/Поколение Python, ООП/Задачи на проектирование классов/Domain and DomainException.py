import re


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, domain):
        if not self._is_valid_domain(domain):
            raise DomainException("Недопустимый домен, url или email")
        self.domain = domain

    def __str__(self):
        return self.domain

    @classmethod
    def from_url(cls, url):
        match = re.fullmatch(r"https?://([a-zA-Z]+\.[a-zA-Z]+)", url)
        if not match:
            raise DomainException("Недопустимый домен, url или email")
        return cls(match.group(1))

    @classmethod
    def from_email(cls, email):
        match = re.fullmatch(r"[a-zA-Z]+@([a-zA-Z]+\.[a-zA-Z]+)", email)
        if not match:
            raise DomainException("Недопустимый домен, url или email")
        return cls(match.group(1))

    @staticmethod
    def _is_valid_domain(domain):
        return bool(re.fullmatch(r"[a-zA-Z]+\.[a-zA-Z]+", domain))
