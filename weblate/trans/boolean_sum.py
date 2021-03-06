# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2017 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Wrapper for Sum to work on Boolean fields."""
from django.db.models import Sum, When, Case, IntegerField


def do_boolean_sum(field, value=1):
    """Wrapper to generate SUM on boolean values"""
    cond = {field: True}
    return Sum(
        Case(
            When(then=value, **cond),
            default=0,
            output_field=IntegerField()
        )
    )
