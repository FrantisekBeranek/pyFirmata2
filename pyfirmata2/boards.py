BOARDS = {
    'arduino': {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(6)),
        'pwm': (3, 5, 6, 9, 10, 11),
        'use_ports': True,
        'disabled': (0, 1), # Rx, Tx, Crystal
        'serial' : (),    # Serial0 unavailable
        'i2c' : (18, 19)
    },
    'arduino_mega': {
        'digital': tuple(x for x in range(86)),
        'analog': tuple(x for x in range(16)),
        'pwm': tuple(x for x in range(2, 14)),
        'use_ports': True,
        'disabled': (0, 1),     # Rx, Tx, Crystal
        'serial' : ({'port': 3, 'rx': 15, 'tx': 14}, 
                    {'port': 2, 'rx': 17, 'tx': 16}, 
                    {'port': 1, 'rx': 19, 'tx': 18}),    # Serial0 unavailable
        'i2c' : (20, 21)
    },
    'arduino_due': {
        'digital': tuple(x for x in range(54)),
        'analog': tuple(x for x in range(12)),
        'pwm': tuple(x for x in range(2, 14)),
        'use_ports': True,
        'disabled': (0, 1),     # Rx, Tx, Crystal
        'serial' : ({'port': 3, 'rx': 15, 'tx': 14}, 
                    {'port': 2, 'rx': 17, 'tx': 16}, 
                    {'port': 1, 'rx': 19, 'tx': 18}),    # Serial0 unavailable
        'i2c' : (20, 21)
    },
    'arduino_nano': {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(8)),
        'pwm': (3, 5, 6, 9, 10, 11),
        'use_ports': True,
        'disabled': (0, 1), # Rx, Tx, Crystal
        'serial' : (),    # Serial0 unavailable
        'i2c' : (18, 19)
    }
}
