from models.site import Site


def test_site_title():

    site = Site(
        "Apartment Block",
        "Building apartments",
        "2026-12-01"
    )

    assert site.title == "Apartment Block"