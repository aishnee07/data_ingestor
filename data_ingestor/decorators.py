import functools
import time

def timer(func):
	@functools.wraps(func)
	def wrapper(self, *args, **kwargs):
		start = time.time()
		result = func(self, *args, **kwargs)  # capture result
		end = time.time()
		print(f"[timer] {func.__name__} took {end - start:.4f}s")  # print the time
		return result                          # return the dataframe, not the time
	return wrapper
		
def validate_dataframe(func):
	@functools.wraps(func)
	def wrapper(self, *args, **kwargs):
		df = func(self, *args, **kwargs)
		print(f"[validate] Shape: {df.shape}")
		print(f"[validate] Nulls found: {df.isnull().values.any()}")
		return df
	return wrapper
	