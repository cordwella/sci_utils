import argparse
import re
from unidecode import unidecode

CAPTURE_CITATION_NAMES = re.compile(b"citep?{([\\w\-_,\s]*)}")
CAPTURE_CITATION_BIBTEX = re.compile(b"{([\\w\-_1-9]*),")

def get_used_citations(filename):

	with open(filename, 'rb') as f:
		file_contents = f.read()
		matches = [x.strip() for xs in re.findall(CAPTURE_CITATION_NAMES, file_contents) for x in xs.split(b',')]

		# return unique citations
		return matches


def parse_bibtex(filename):
	""" returns a dict of 'keyword': 'full text string' bibtex entries """

	with open(filename, 'rb') as f:
		data = f.read()

		entries = {get_cite_code(b'@' + x): x for x in data.split(b'@') if len(x) > 2}
		return entries


def get_cite_code(bibstr):
	a = re.search(CAPTURE_CITATION_BIBTEX, bibstr).group(1)
	return a


def main(bibtex_file, latex_file, output_filename):
	## Get parser
	bibtex_codes = parse_bibtex(bibtex_file)
	print('Initial bib entries  : ' +  str(len(bibtex_codes)))

	citations_used = set(get_used_citations(latex_file))
	print('Citations used in TeX: ' +  str(len(citations_used)))

	output_bibtex = {x: y for (x, y) in bibtex_codes.items() if x in citations_used}
	print('Output bib entries   : ' +  str(len(output_bibtex)))


	# alphabetically organise
	output_citation_keys = sorted(output_bibtex.keys(), key=lambda x:x.decode("utf-8").lower())

	with open(output_filename, 'w') as f:
		# Do the thing, but first remove any annoying unicode 
		for x in output_citation_keys:
			f.write('@' + unidecode(output_bibtex[x].decode("utf-8")))



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate disk files and folders')
	parser.add_argument('bibtex_file', help='Input bibtex filename')
	parser.add_argument('latex_file', help='Input latex filename')
	parser.add_argument('output_file', help='Input latex filename')

	args = parser.parse_args()


	main(args.bibtex_file, args.latex_file, args.output_file)