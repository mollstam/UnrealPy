class PyIAddrBook : public PyIMAPIProp
{
public:
MAKE_PYCOM_CTOR(PyIAddrBook);
static PyComTypeObject type;
static IAddrBook *GetI(PyObject *self);
	static PyObject *CompareEntryIDs(PyObject *self, PyObject *args);
	static PyObject *OpenEntry(PyObject *self, PyObject *args);
	static PyObject *ResolveName(PyObject *self, PyObject *args);
protected:
	PyIAddrBook(IUnknown *);
	~PyIAddrBook();
};

