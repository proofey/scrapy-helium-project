from itemadapter import ItemAdapter
import json


class MangoPipeline:
    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file = open('result.json', 'w')
 
    def close_spider(self, spider):
        self.file.close()

