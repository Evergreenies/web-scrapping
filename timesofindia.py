from bs4 import BeautifulSoup
import requests, sys, csv, re


class Scrap(object):

	def __init__(self):
		try:
			# Get source code of page
			self.source_code = requests.get('https://timesofindia.indiatimes.com/india').text
			self.soup = BeautifulSoup(self.source_code, 'lxml')			
		except BaseException as e:
			print(e)

	def scrap_news(self):
		
		# Creating and writting data into CSV file
		csv_file = open('times_of_india_csv.csv', 'w')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(["Sr. No.","Today's News", "Description", "Link", "Date", "Time"])

		count = 0

		for news in self.soup.find_all('ul', class_='list5 clearfix'):

			for lis in news.find_all('li'):

				# Extracting news
				new1 = lis.a.text				

				# Get link of each news
				link = lis.a.get('href')

				# Rendering each news to their description page
				descri = requests.get('https://timesofindia.indiatimes.com'+link).text
				soup_descri = BeautifulSoup(descri, 'lxml')

				# Extracting detail description of news
				article = soup_descri.find('div', class_='Normal').text

				# Extracting date and time of news
				date_time = lis.find('span', class_='strlastupd').text	
				date = date_time.split(',')[0]
				time = date_time.split(',')[1]	

				count += 1

				print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(count,new1, article, 'https://timesofindia.indiatimes.com'+link, date, time), end="")

				# Writting data of each news into CSV file
				csv_writer.writerow([count, new1, article, 'https://timesofindia.indiatimes.com'+link, date, time])

		csv_file.close()


if __name__ == '__main__':
	scp = Scrap()
	scp.scrap_news()
		