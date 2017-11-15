import scrapy


class QuotesSpider(scrapy.Spider):
	name = "french"
	start_urls = [
		#   	'http://french.languagedaily.com/wordsandphrases/most-common-words',
		'http://french.languagedaily.com/wordsandphrases/common-french-words',
		'http://french.languagedaily.com/wordsandphrases/most-common-french-words',
		'http://french.languagedaily.com/wordsandphrases/most-common-words-3',
		'http://french.languagedaily.com/wordsandphrases/most-common-words-5',
		'http://french.languagedaily.com/wordsandphrases/most-common-words-6',
		'http://french.languagedaily.com/wordsandphrases/most-common-words-7',
		'http://french.languagedaily.com/wordsandphrases/most-common-words-8',
		'http://french.languagedaily.com/wordsandphrases/most-common-words-9',
		# 'http://french.languagedaily.com/wordsandphrases/most-common-words-10',
		# 'http://french.languagedaily.com/wordsandphrases/most-common-words-11',
		# 'http://french.languagedaily.com/wordsandphrases/most-common-words-12',
	]

    # def parse(self, response):
        # for tr in response.xpath('//tr[contains(@class, "rowA") or contains(@class, "rowB")]'):
        #     yield {
        #         'word': tr.xpath('td[2]/text()').extract_first(),
        #         'englishDef': tr.xpath('td[3]/text()').extract_first(),
        #         'partOfSpeech': tr.xpath('td[4]/text()').extract_first(),
        #     }
        #-----------------------------------------------------------------
        # for tr in response.css('tr.rowA'):
        #     yield {
        #         'word': tr.css('td::text').extract()[1],
        #         'englishDef': tr.css('td::text').extract()[2],
        #         'partOfSpeech': tr.css('td::text').extract()[3],
        #     }

        # for tr in response.css('tr.rowB'):
        #     yield {
        #         'word': tr.css('td::text').extract()[1],
        #         'englishDef': tr.css('td::text').extract()[2],
        #         'partOfSpeech': tr.css('td::text').extract()[3],
        #     }


# Good: no Json; Bad: if one field is null, whole link breaks
	def parse(self, response):
		filename = 'frenchWords.txt'
		cnt = 1
		with open(filename, 'a') as f:
			for tr in response.css('tr.rowA'):
				line = 'f' + str(cnt) + '@' + tr.css('td::text').extract()[1] + '@' + tr.css('td::text').extract()[2] + '@' + tr.css('td::text').extract()[3] + '\n'
				cnt += 1
				f.write(line)
			for tr in response.css('tr.rowB'):
				line = 'f' + str(cnt) + '@' + tr.css('td::text').extract()[1] + '@' + tr.css('td::text').extract()[2] + '@' + tr.css('td::text').extract()[3] + '\n'
				cnt += 1
				f.write(line)



