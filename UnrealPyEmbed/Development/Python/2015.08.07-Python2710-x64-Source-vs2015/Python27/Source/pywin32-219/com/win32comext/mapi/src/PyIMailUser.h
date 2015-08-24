class PyIMailUser : public PyIMAPIContainer
{
public:
MAKE_PYCOM_CTOR(PyIMailUser);
static PyComTypeObject type;
static IMailUser *GetI(PyObject *self);
protected:
	PyIMailUser(IUnknown *);
	~PyIMailUser();
};

