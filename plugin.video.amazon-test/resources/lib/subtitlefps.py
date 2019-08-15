#!/usr/bin/env python
# coding: utf-8

import io
import re

def sub_change_fps(input_file, output_file, factor = 24 / 23.976):

	def modify_date(f):
		h = int(f.group('h'))
		m = int(f.group('m'))
		s = int(f.group('s'))
		ms = int(f.group('ms'))
		sep = f.group('sep')

		seconds = (h * 60 * 60) + (m * 60) + s + (float(ms) / 1000)
		converted_seconds = seconds * factor

		h2, remainder = divmod(converted_seconds, 3600)
		m2, s2 = divmod(remainder, 60)
		ms2 = round((s2 - int(s2)) * 1000)
		s2 = int(s2)
		r = "%02d:%02d:%02d%s%03d" % (h2, m2, s2, sep, ms2)
		return r

	with io.open(input_file, "r", encoding="utf-8") as f:
		content = f.read()
		res = re.sub('(?P<h>\d+):(?P<m>\d+):(?P<s>\d+)(?P<sep>[,.])(?P<ms>\d+)', modify_date, content)
		with io.open(output_file, 'w', encoding='utf-8') as fo:
			fo.write(res)
