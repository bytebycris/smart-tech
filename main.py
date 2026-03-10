def sort(width, height, length, mass):
    package_volume = width * height * length

    is_bulky_package = (
        package_volume >= 1_000_000
        or width >= 150
        or height >= 150
        or length >= 150
    )
    is_heavy_package = mass >= 20

    if is_bulky_package and is_heavy_package:
        return "REJECTED"
    if is_bulky_package or is_heavy_package:
        return "SPECIAL"
    return "STANDARD"


if __name__ == "__main__":
    assert sort(10, 10, 10, 1) == "STANDARD"
    assert sort(100, 100, 100, 10) == "SPECIAL"   # bulky by volume
    assert sort(150, 10, 10, 10) == "SPECIAL"     # bulky by single dimension 
    assert sort(10, 10, 10, 20) == "SPECIAL"      # heavy 
    assert sort(150, 100, 100, 20) == "REJECTED"  # both bulky and heavy

    print("All tests passed.")
