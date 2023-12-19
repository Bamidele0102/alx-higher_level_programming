#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Print information about a PyFloatObject
 * @p: PyObject pointer to a Python float object
 */
void print_python_float(PyObject *p)
{
	double value;
	char *string;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
	PyMem_Free(string);
}

/**
 * print_python_bytes - Print information about a PyBytesObject
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = ((PyBytesObject *)(p))->ob_sval;
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02hhx", string[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Print information about a PyListObject
 * @p: PyObject pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < size; i++)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
