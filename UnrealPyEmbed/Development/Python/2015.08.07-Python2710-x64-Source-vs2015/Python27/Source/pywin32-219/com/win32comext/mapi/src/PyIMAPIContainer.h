class PyIMAPIContainer : public PyIMAPIProp
{
public:
MAKE_PYCOM_CTOR(PyIMAPIContainer);
static PyComTypeObject type;
static IMAPIContainer *GetI(PyObject *self);
	static PyObject *OpenEntry(PyObject *self, PyObject *args);
	static PyObject *GetHierarchyTable(PyObject *self, PyObject *args);
	static PyObject *GetContentsTable(PyObject *self, PyObject *args);
protected:
	PyIMAPIContainer(IUnknown *);
	~PyIMAPIContainer();
};

