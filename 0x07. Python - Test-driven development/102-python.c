#include "python3.10/Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;

	fflush(stdout);
	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	length = PyUnicode_GET_LENGTH(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		const char *value = PyUnicode_AsUTF8(p);

		if (!value)
		{
			PyErr_Print();
			return;
		}
		printf("  value: %s\n", value);
	}
	else
	{
		wchar_t *value = PyUnicode_AsWideCharString(p, &length);

		if (!value)
		{
			PyErr_Print();
			return;
		}
		printf("  value: %ls\n", value);
		PyMem_Free(value);
	}
}
