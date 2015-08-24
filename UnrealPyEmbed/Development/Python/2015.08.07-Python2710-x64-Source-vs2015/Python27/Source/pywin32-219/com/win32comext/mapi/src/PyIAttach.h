class PyIAttach : public PyIMAPIProp
{
public:
MAKE_PYCOM_CTOR(PyIAttach);
static PyComTypeObject type;
static IAttach *GetI(PyObject *self);
	static PyObject *GetLastError(PyObject *self, PyObject *args);
protected:
	PyIAttach(IUnknown *);
	~PyIAttach();
};

