class PyIProfSect : public PyIMAPIProp
{
public:
MAKE_PYCOM_CTOR(PyIProfSect);
static PyComTypeObject type;
static IProfSect *GetI(PyObject *self);
protected:
	PyIProfSect(IUnknown *);
	~PyIProfSect();
};

