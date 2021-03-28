# Class template used primarily for the generation of NPC opponents. The stat prioritization is listed with each class ID. The delta refers to the difference between
# the top stat and the least important stat, with 10 being the greatest difference and 1 being hardly any difference.
classTemplate = {
    'none': 0,      # Balanced growth
    # Melee classes:
    'warrior': 1,     # 1) Strength,      2) Constitution,  3) Stamina,      4) Will,      5) Dexterity,    6) Wisdom,    7) Agility,      8) Spirit,       9) Intellect.  Delta = 9
    'sentry': 2,      # 1) Constitution,  2) Stamina,       3) Strength,     4) Will,      5) Spirit,       6) Dexterity, 7) Wisdom,       8) Agility,      9) Intellect.  Delta = 7
    'soldier': 3,     # 1) Stamina,       2) Strength,      3) Constitution, 4) Dexterity, 5) Agility,      6) Wisdom,    7) Intellect,    8) Will,         9) Spirit.     Delta = 4
    'paladin': 4,     # 1) Strength,      2) Constitution,  3) Will,         4) Spirit,    5) Dexterity,    6) Intellect, 7) Stamina,      8) Wisdom,       9) Agility.    Delta = 6
    'darkKnight': 5,  # 1) Strength,      2) Stamina,       3) Constitution, 4) Dexterity, 5) Intellect,    6) Wisdom,    7) Agililty,     8) Will,         9) Spirit.     Delta = 7
    'spellsword': 6,  # 1) Stamina,       2) Strength,      3) Dexterity,    4) Intellect, 5) Constitution, 6) Wisdom,    7) Agililty,     8) Will,         9) Spirit.     Delta = 6

    # Specialist classes:
    'rogue': 7,       # 1) Agility,       2) Dexterity,     3) Wisdom,       4) Stamina,   5) Strength,     6) Intellect, 7) Will,         8) Constitution, 9) Spirit.     Delta = 8
    'ranger': 8,      # 1) Dexterity,     2) Will,          3) Spirit,       4) Agility,   5) Stamina,      6) Strength,  7) Constitution, 8) Intellect,    9) Wisdom      Delta = 6
}

elements = {
    'physical': 0,
    'fire': 1,
    'water': 2,
    'earth': 3,
    'wind': 4,
    'light': 5,
    'darkness': 6,
    'venom': 7
}

races = {
    'human': 0,
    'elf': 1,
    'dwarf': 2,
    'gnome': 3,
    'goblin': 4,
    'orc': 5,
    'ogre': 6,
    'undead': 7,
    'spirit': 8,
    'insectoid': 9,
    'birdkin': 10,
    'beast': 11,
    'dragonkin': 12,
    'geddian': 13
}

weaponTypes = {
    'unarmed': 0,
    'dagger': 1,
    'sword': 2,
    'greatsword': 3,
    'staff': 4,
    'spear': 5,
    'blunt': 6,
    'heavyBlunt': 7
    'axe': 8
    'battleaxe': 9
    'bow': 10
    'arrow': 11
    'throwing': 12
}
skills = {
    # Weapon skills:
    'swordsmanship': 0,   # Special techniques and bonuses for swords and greatswords.
    'closeQuarters': 0,   # Special techniques and bonuses for daggers.
    'handToHand': 0,      # Special techniques and bonuses for unarmed combat.
    'polearms': 0,        # Special techniques and bonuses for spears and staffs.
    'axeTechnique': 0,    # Special techniques and bonuses for axes and battleaxes.
    'bluntTechnique': 0,  # Special techniques and bonuses for maces and blunt weapons.
    'marksmanship': 0,    # Special techniques and bonuses for bows & arrows.
    'juggling': 0,        # Special techniques and bonuses for thrown weapons.
    
    # Misc combat skills:
    'tactics': 0,         # Bonus to damage for normal attacks.
    'blocking': 0,        # Affects chance to block and amount of damage blocked with a shield.
    'parrying': 0,        # Affects chance to parry an attack. Affects damage mitigated when unarmed.
    'acrobatics': 0,      # Affects chance to dodge attacks.
    'heavySpecialist': 0, # Bonus to hit and damage with 2-handed weapons.
    'swordAndBoard': 0,   # Bonuses when using 1-handed weapon and shield.
    'dualWield': 0,       # Bonuses when using 2 1-handed weapons.
    
    # Other useful skills:
    'focus': 0,           # Affects auto recovery rate of magic and special

    # Magic abilities:
    'music': 0,           # Use songs to give an edge in combat.
}
