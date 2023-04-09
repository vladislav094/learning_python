
class AttrDisplay:

	def get_attrs(self):
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('%s=%s' % (key, getattr(self, key)))
		return ', '.join(attrs)

	def __repr__(self):
		return '[%s: %s]' % (self.__class__.__name__, self.get_attrs())


# if __name__ == '__main__':
# 	class TopTest(AttrDisplay):
# 		count = 0
# 		def __init__(self):
# 			self.attr1 = TopTest.count
# 			self.attr2 = TopTest.count + 1
# 			TopTest.count += 2
#
# 		def gather_attrs(self):
# 			return 'Spam'
#
# 	class SubTest(TopTest):
# 		pass
#
# X, Y = TopTest(), SubTest()


