class PyIMAPIProp : public PyIUnknown
{
public:
MAKE_PYCOM_CTOR(PyIMAPIProp);
static PyComTypeObject type;
static IMAPIProp *GetI(PyObject *self);
	static PyObject *GetPropList(PyObject *self, PyObject *args);
	static PyObject *OpenProperty(PyObject *self, PyObject *args);
	static PyObject *GetIDsFromNames(PyObject *self, PyObject *args);
	static PyObject *DeleteProps(PyObject *self, PyObject *args);
	static PyObject *CopyProps(PyObject *self, PyObject *args);
	static PyObject *CopyTo(PyObject *self, PyObject *args);
	static PyObject *SetProps(PyObject *self, PyObject *args);
	static PyObject *GetProps(PyObject *self, PyObject *args);
	static PyObject *SaveChanges(PyObject *self, PyObject *args);
	static PyObject *GetLastError(PyObject *self, PyObject *args);
	static PyObject *GetNamesFromIDs(PyObject *self, PyObject *args);
protected:
	PyIMAPIProp(IUnknown *);
	~PyIMAPIProp();
};

