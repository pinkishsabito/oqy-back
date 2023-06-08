from drf_yasg import openapi

title = "OQY API"
version = "1.0.0"
description = "API documentation for OQY App"
terms_of_service = "https://nometa.xyz"
contact = openapi.Contact(email="ozhetov.arsen@gmail.com")
license_info = openapi.License(name="AITU License", url="https://opensource.org/licenses/MIT")

swagger_info = openapi.Info(
    title=title,
    default_version=version,
    description=description,
    terms_of_service=terms_of_service,
    contact=contact,
    license=license_info,
)
