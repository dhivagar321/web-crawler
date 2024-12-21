from mftool import Mftool

# Initialize the Mftool object
mf = Mftool()

# Fetch and display all mutual fund scheme codes
def list_all_schemes():
    schemes = mf.get_scheme_codes()  # Fetch all schemes
    print("Total schemes found:", len(schemes))
    print("\nList of all mutual fund schemes:\n")
    for code, name in schemes.items():
        print(f"{code}: {name}")

if __name__ == "__main__":
    list_all_schemes()