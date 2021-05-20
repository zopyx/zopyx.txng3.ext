#define PY_SSIZE_T_CLEAN
#include <Python.h>

#if PY_MAJOR_VERSION >= 3
# define PY3K
# define INT_FROM_LONG(x) PyLong_FromLong(x)
# define INT_CHECK(x) PyLong_Check(x)
# define UNICODE_LENGTH(x) PyUnicode_GET_LENGTH(x)
# define UNICODE_T wchar_t
# define PYSTR_TO_UNICODE_T(unicode, len) PyUnicode_AsWideCharString(unicode, len)
# define UNICODE_T_TO_PYSTR(chars, len) PyUnicode_FromWideChar(chars, len)
# define FREE_UNICODE_T(x) PyMem_Free(x)
#else /* Python 2 */
# define INT_FROM_LONG(x) PyInt_FromLong(x)
# define INT_CHECK(x) PyInt_Check(x)
# define UNICODE_LENGTH(x) PyUnicode_GET_SIZE(x)
# define UNICODE_T Py_UNICODE
static UNICODE_T* PYSTR_TO_UNICODE_T(PyObject* unicode, Py_ssize_t* len)
{
    *len = UNICODE_LENGTH(unicode);
    return PyUnicode_AS_UNICODE(unicode);
}
# define UNICODE_T_TO_PYSTR(chars, len) PyUnicode_FromUnicode(chars, len)
# define FREE_UNICODE_T(x)
#endif

#ifndef PyInt_AS_LONG
# define PyInt_AS_LONG(x) PyLong_AsLong(x)
#endif
