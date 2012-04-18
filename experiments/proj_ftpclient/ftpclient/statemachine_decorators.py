
def precond_state(shouldBe):
	def precond_state_impl(meth):
		def method_with_state_check(self, *args):
			self._assertState(shouldBe)
			return meth(self, *args)
		return method_with_state_check
	return precond_state_impl

def precond_states3(shouldBe, orShouldBe, orShouldBe2):
	def precond_state_impl(meth):
		def method_with_state_check(self, *args):
			self._assertStates3(shouldBe, orShouldBe, orShouldBe2)
			return meth(self, *args)
		return method_with_state_check
	return precond_state_impl

def precond_state_inverse(shouldNotBe):
	def precond_state_inverse_impl(meth):
		def method_with_inverse_state_check(self, *args):
			self._assertNotState(shouldNotBe)
			return meth(self, *args)
		return method_with_inverse_state_check
	return precond_state_inverse_impl


def postcond_state(shouldBe):
	def postcond_state_impl(meth):
		def method_with_state_post_check(self, *args):
			result = meth(self, *args)
			self._assertState(shouldBe)
			return result
		return method_with_state_post_check
	return postcond_state_impl

def postcond_states(shouldBe, orShouldBe):
	def postcond_state_impl(meth):
		def method_with_state_post_check(self, *args):
			result = meth(self, *args)
			self._assertStates(shouldBe, orShouldBe)
			return result
		return method_with_state_post_check
	return postcond_state_impl

def postcond_states3(shouldBe, orShouldBe, orShouldBe2):
	def postcond_state_impl(meth):
		def method_with_state_post_check(self, *args):
			result = meth(self, *args)
			self._assertStates3(shouldBe, orShouldBe, orShouldBe2)
			return result
		return method_with_state_post_check
	return postcond_state_impl

def postcond_state_any(meth):
	def method_without_state_post_check(self, *args):
		return meth(self, *args)
	return method_without_state_post_check
