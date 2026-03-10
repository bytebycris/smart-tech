from main import sort


def test_standard_package():
    assert sort(10, 10, 10, 1) == "STANDARD"


def test_special_when_bulky_by_volume_threshold():
    assert sort(100, 100, 100, 10) == "SPECIAL"


def test_special_when_bulky_by_dimension_threshold():
    assert sort(150, 10, 10, 10) == "SPECIAL"


def test_special_when_heavy_threshold():
    assert sort(10, 10, 10, 20) == "SPECIAL"


def test_rejected_when_bulky_and_heavy():
    assert sort(150, 100, 100, 20) == "REJECTED"


def test_standard_just_below_volume_threshold():
    assert sort(100, 100, 99, 19.9) == "STANDARD"


def test_standard_just_below_dimension_threshold():
    assert sort(149.9, 10, 10, 10) == "STANDARD"


def test_standard_just_below_mass_threshold():
    assert sort(10, 10, 10, 19.9) == "STANDARD"
