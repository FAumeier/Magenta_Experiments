import scrapy


class MidiSpider(scrapy.Spider):
    name = "midi"

    def start_requests(self):
        urls = [
            'http://www.piano-e-competition.com/midi_2011.asp',
            'http://www.piano-e-competition.com/midi_2009.asp',
            'http://www.piano-e-competition.com/midi_2008.asp',
            'http://www.piano-e-competition.com/midi_2006.asp',
            'http://www.piano-e-competition.com/midi_2004.asp',
            'http://www.piano-e-competition.com/midi_2002.asp'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for midilink in response.xpath('//*[@id="body"]/table[1]/tr/td[2]/table/tr/td/table[2]/tr/td[2]/div/div/table[*]/tr/td[3]/a/@href').extract():
            yield {
                'link': midilink,
            }
