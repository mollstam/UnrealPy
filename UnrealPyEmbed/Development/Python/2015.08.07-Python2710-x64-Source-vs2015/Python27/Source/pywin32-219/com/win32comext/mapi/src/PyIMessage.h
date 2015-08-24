class PyIMessage : public PyIMAPIProp
{
public:
MAKE_PYCOM_CTOR(PyIMessage);
static PyComTypeObject type;
static IMessage *GetI(PyObject *self);
	static PyObject *SubmitMessage(PyObject *self, PyObject *args);
	static PyObject *GetRecipientTable(PyObject *self, PyObject *args);
	static PyObject *ModifyRecipients(PyObject *self, PyObject *args);
	static PyObject *DeleteAttach(PyObject *self, PyObject *args);
	static PyObject *CreateAttach(PyObject *self, PyObject *args);
	static PyObject *OpenAttach(PyObject *self, PyObject *args);
	static PyObject *GetAttachmentTable(PyObject *self, PyObject *args);
	static PyObject *SetReadFlag(PyObject *self, PyObject *args);
protected:
	PyIMessage(IUnknown *);
	~PyIMessage();
};

