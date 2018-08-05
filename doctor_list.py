from bs4 import BeautifulSoup
import requests, sys, csv, re


class Scrap(object):

	def __init__(self):		
		# Get source code of page
		self.source_code = requests.get('https://www.practo.com/pune/doctors/chinchwad').text
		self.soup = BeautifulSoup(self.source_code, 'lxml')						

	def scrap_dr(self):
		
		# Creating if not exist and simultaneously writting data into CSV file
		csv_file = open('doctors_csv.csv', 'w')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(["Sr. No.","Name", "Qualification", "Specialization", "Experience", "Hospital", "Profile"])
		
		count = 0

		for dr in self.soup.find_all('div', class_='c-card'):
			name = dr.find('h2', class_='u-title-font u-c-pointer u-bold').text
			profile = 'https://www.practo.com'+dr.a.get('href')
			qualification = dr.find('h3', class_='u-t-ellipsis').text
			experience = dr.span.text
			specialization = dr.find('h3', class_='u-d-inline').span.text
			hospital = dr.find('a', class_='u-bold u-c-pointer').text

			count += 1

			print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(count, name, qualification, specialization, experience, hospital, profile))

			# Writting data of each news into CSV file
			csv_writer.writerow([count, name, qualification, specialization, experience, hospital, profile])

		csv_file.close()


if __name__ == '__main__':
	scp = Scrap()
	scp.scrap_dr()
		