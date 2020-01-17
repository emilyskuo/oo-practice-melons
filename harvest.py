############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 'Muskmelon', 1998, 'green',
                     True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    cas.add_pairing('strawberries', 'mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_type_dict = {}

    for melon in melon_types:
        melon_type_dict[melon.code] = melon

    return melon_type_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape, color, field, harvester):
        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons():
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons = []

    melons_by_id = make_melon_type_lookup(make_melon_types())
    melon1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    melons.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9])

    return melons


def make_melons_from_file(file_name):
    melons = []

    melon_info = open(file_name)
    melons_by_id = make_melon_type_lookup(make_melon_types())

    for melon_stats in melon_info:
        melon_stats = melon_stats.rstrip()
        melon_stats = melon_stats.split()
        code = melon_stats[5]
        shape = int(melon_stats[1])
        color = int(melon_stats[3])
        field = int(melon_stats[-1])
        harvester = melon_stats[8]
        melon = Melon(melons_by_id[code], shape, color, field, harvester)
        melons.append(melon)

    melon_info.close()

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvester} from Field {melon.field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvester} from Field {melon.field} (NOT SELLABLE)")


get_sellability_report(make_melons_from_file("harvest_log.txt"))
