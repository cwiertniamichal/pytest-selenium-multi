# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


def factory(fun):
    if 'get_instance' in dir(fun):
        raise AttributeError('object {:s} already has "get_instance" '
                             'attribute'.format(fun.__name__))
    else:
        fun.get_instance = lambda *args, **kwargs: fun(*args, **kwargs)
