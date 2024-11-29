from pydantic import BaseModel, HttpUrl, validator

class URLInput(BaseModel):
    url: HttpUrl

    @validator("url")
    def validate_domain(cls, value):
        allowed_domains = ["youtube.com", "youtu.be", "kwai.com"]
        if not any(domain in value.host for domain in allowed_domains):
            raise ValueError("A URL deve ser do YouTube ou Kwai.")
        return value