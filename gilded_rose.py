# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.max_quality_value = 50

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        self._decrease_item_quality(item)
            else:
                self._increase_item_quality(item)
                self.update_ticket_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                self._decrease_item_quality(item)
                    else:
                        self._drop_item_quality(item)
                else:
                    self._increase_item_quality(item)

    def update_ticket_quality(self, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 11:
                self._increase_item_quality(item)
            if item.sell_in < 6:
                self._increase_item_quality(item)

    def _increase_item_quality(self, item):
        if self._not_at_max_item_quality(item):
            item.quality += 1

    def _decrease_item_quality(self, item):
        item.quality -= 1

    def _drop_item_quality(self, item):
        item.quality = 0

    def _not_at_max_item_quality(self, item):
        return item.quality < self.max_quality_value

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
