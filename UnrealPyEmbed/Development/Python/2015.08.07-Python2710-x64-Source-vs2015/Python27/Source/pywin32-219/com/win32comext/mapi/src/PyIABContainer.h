class PyIABContainer : public PyIMAPIContainer
{
public:
MAKE_PYCOM_CTOR(PyIABContainer);
static PyComTypeObject type;
static IABContainer *GetI(PyObject *self);
protected:
	PyIABContainer(IUnknown *);
	~PyIABContainer();
};

