#include <Python.h>
#include <floatobject.h>

/**
 * print_python_list - Print some basic info about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    for (i = 0; i < size; i++)
    {
        PyObject *obj = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}

/**
 * print_python_bytes - Print some basic info about Python bytes
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    const char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    if (size > 10)
        size = 10;

    printf("  first %zd bytes:", size);
    for (i = 0; i < size; i++)
        printf(" %02hhx", str[i]);
    printf("\n");
}

/**
 * print_python_float - Print some basic info about Python floats
 * @p: PyObject pointer to a Python float object
 */
void print_python_float(PyObject *p)
{
    PyObject *repr;
    const char *str;
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    printf("  value: %f\n", value);

    repr = PyObject_Repr(p);
    str = PyUnicode_AsUTF8(repr);
    printf("  repr: %s\n", str);
    Py_XDECREF(repr);
}
