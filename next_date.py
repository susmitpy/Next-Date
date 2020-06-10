#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:05:06 2020

@author: susmitvengurlekar
"""

def is_leap_year(year: int) -> bool:
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

def next_date(date: str) -> str:
    """
        Given a date as a str in yyyy/mm/dd format
        this function returns the next date in
        yyyy/mm/dd format
    """
    ny, nm, nd = 0,0,0
    ans = "{}/{}/{}"

    cy,cm,cd = [int(i) for i  in date.split("/")]

    if cm != 2:
        # not feb
        if cm in [4,6,9,11]:
            # 30 days in month
            if cd == 30:
                nm = cm+1
                nd = 1
            else:
                nd = cd+1
                nm = cm
            ny = cy

        else:
            # 31 days in month
            if cd == 31:
                if cm == 12:
                    ny = cy + 1
                    nm = 1
                    nd = 1
                else:
                    nm = cm + 1
                    nd = 1
                    ny = cy
            else:
                nd = cd + 1
                nm = cm
                ny = cy

    else:
        # feb
        if is_leap_year(cy):
            if cd == 29:
                nm = 3
                nd = 1
            else:
                nd = cd + 1
                nm = cm 
                
        else:
            if cd == 28:
                nm = 3
                nd = 1
            else:
                nd = cd + 1
                nm = cm 
        ny = cy
                
    return ans.format(ny,nm,nd)
