class PyIDistList : public PyIMAPIContainer
{
public:
MAKE_PYCOM_CTOR(PyIDistList);
static PyComTypeObject type;
static IDistList *GetI(PyObject *self);
protected:
	PyIDistList(IUnknown *);
	~PyIDistList();
};

