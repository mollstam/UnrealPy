class PyIConverterSession : public PyIUnknown
{
public:
MAKE_PYCOM_CTOR(PyIConverterSession);
static PyComTypeObject type;
static IConverterSession *GetI(PyObject *self);
	static PyObject *SetAdrBook(PyObject *self, PyObject *args);
	static PyObject *MAPIToMIMEStm(PyObject *self, PyObject *args);
	static PyObject *MIMEToMAPI(PyObject *self, PyObject *args);
protected:
	PyIConverterSession(IUnknown *);
	~PyIConverterSession();
};

