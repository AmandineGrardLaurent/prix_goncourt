# -*- coding: utf-8 -*-

from goncourt.business.goncourt import Goncourt


def main():

    goncourt: Goncourt = Goncourt()
    print(goncourt.get_author_by_id(1))

if __name__ == '__main__':
    main()