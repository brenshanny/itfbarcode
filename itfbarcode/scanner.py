#!/usr/bin/env python

import random
from . import parser


def scan_image_y(im, start_x, end_x, y, scan_range=50):
    if scan_range < 1:
        raise ValueError("Invalid scan_range: %s" % scan_range)
    dy = 0
    bc = 0
    while isinstance(bc, int) and dy < scan_range:
        bc = parser.read_barcode(im[y + dy, start_x:end_x])
        dy += 1
    dy = 1
    while isinstance(bc, int) and dy < scan_range:
        bc = parser.read_barcode(im[y - dy, start_x:end_x])
        dy += 1
    return bc


def scan_image_x(im, start_y, end_y, x, scan_range=50):
    if scan_range < 1:
        raise ValueError("Invalid scan_range: %s" % scan_range)
    dx = 0
    bc = 0
    while isinstance(bc, int) and dx < scan_range:
        bc = parser.read_barcode(im[start_y:end_y, x + dx])
        dx += 1
    dx = 1
    while isinstance(bc, int) and dx < scan_range:
        bc = parser.read_barcode(im[start_y:end_y, x - dx])
        dx += 1
    return bc


def scan_image_y_random_lpn(im, start_x, end_x, y,
                            scan_range=50, lpn_range=(50, 150)):
    if scan_range < 1:
        raise ValueError("Invalid scan_range: %s" % scan_range)
    if (lpn_range[1] - lpn_range[0]) < 2:
        raise ValueError(
            "Invalid tuple passed in to lpn_range! %s" % lpn_range)
    dy = 0
    bc = 0
    while isinstance(bc, int) and dy < scan_range:
        random_lpn = random.randrange((lpn_range[0] - 1), (lpn_range[1] + 1))
        bc = parser.read_barcode(im[y + dy, start_x:end_x], lpn=random_lpn)
        dy += 1
    dy = 1
    while isinstance(bc, int) and dy < scan_range:
        random_lpn = random.randrange((lpn_range[0] - 1), (lpn_range[1] + 1))
        bc = parser.read_barcode(im[y - dy, start_x:end_x], lpn=random_lpn)
        dy += 1
    return bc


def scan_image_x_random_lpn(im, start_y, end_y, x,
                            scan_range=50, lpn_range=(50, 150)):
    if scan_range < 1:
        raise ValueError("Invalid scan_range: %s" % scan_range)
    if (lpn_range[1] - lpn_range[0]) < 2:
        raise ValueError(
            "Invalid tuple passed in to lpn_range! %s" % lpn_range)
    dx = 0
    bc = 0
    while isinstance(bc, int) and dx < scan_range:
        random_lpn = random.randrange((lpn_range[0] - 1), (lpn_range[1] + 1))
        bc = parser.read_barcode(im[start_y:end_y, x + dx], lpn=random_lpn)
        dx += 1
    dx = 1
    while isinstance(bc, int) and dx < scan_range:
        random_lpn = random.randrange((lpn_range[0] - 1), (lpn_range[1] + 1))
        bc = parser.read_barcode(im[start_y:end_y, x - dx], lpn=random_lpn)
        dx += 1
    return bc


def scan_image_y_lpn_range(im, start_x, end_x, y,
                           scan_y_range=50, lpn_range=(1, 201)):
    if scan_y_range < 1:
        raise ValueError("Invalid scan_range: %s" % scan_y_range)
    if (lpn_range[1] - lpn_range[0]) < 2:
        raise ValueError(
            "Invalid tuple passed in to lpn_range! %s" % lpn_range)
    dy = 0
    bc = 0
    while isinstance(bc, int) and dy < scan_y_range:
        for r in range(lpn_range[0], lpn_range[1]):
            bc_try = parser.read_barcode(im[y + dy, start_x:end_x], lpn=r)
            if type(bc_try) != int:
                if any(b < 0 for b in bc_try):
                    bc = 0
                else:
                    bc = bc_try
            else:
                bc = 0
        dy += 1
    dy = 1
    while isinstance(bc, int) and dy < scan_y_range:
        for r in range(lpn_range[0], lpn_range[1]):
            bc_try = parser.read_barcode(im[y - dy, start_x:end_x], lpn=r)
            if type(bc_try) != int:
                if any(b < 0 for b in bc_try):
                    bc = 0
                else:
                    bc = bc_try
            else:
                bc = 0
        dy += 1
    return bc


def scan_image_x_lpn_range(im, start_y, end_y, x,
                           scan_x_range=50, lpn_range=(1, 201)):
    if scan_x_range < 1:
        raise ValueError("Invalid scan_range: %s" % scan_x_range)
    if (lpn_range[1] - lpn_range[0]) < 2:
        raise ValueError(
            "Invalid tuple passed in to lpn_range! %s" % lpn_range)
    dx = 0
    bc = 0
    while isinstance(bc, int) and dx < scan_x_range:
        for r in range(lpn_range[0], lpn_range[1]):
            bc_try = parser.read_barcode(im[start_y:end_y, x + dx], lpn=r)
            if type(bc_try) != int:
                if any(b < 0 for b in bc_try):
                    bc = 0
                else:
                    bc = bc_try
            else:
                bc = 0
        dx += 1
    dx = 1
    while isinstance(bc, int) and dx < scan_x_range:
        for r in range(lpn_range[0], lpn_range[1]):
            bc_try = parser.read_barcode(im[start_y:end_y, x - dx], lpn=r)
            if type(bc_try) != int:
                if any(b < 0 for b in bc_try):
                    bc = 0
                else:
                    bc = bc_try
            else:
                bc = 0
        dx += 1
    return bc
