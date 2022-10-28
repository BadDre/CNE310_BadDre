def ip_to_operating_system(octet):
    if octet == 0:
        return "Router"
    elif octet % 2 == 0:
        return 'Windows'
    else:
        return 'Linux'