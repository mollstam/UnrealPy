 /*
 Microsoft Developer Support
 Copyright (c) 1992 Microsoft Corporation

 This file contains the message definitions for the Win32
 messages.exe sample program.
-------------------------------------------------------------------------
 HEADER SECTION

 The header section defines names and language identifiers for use
 by the message definitions later in this file. The MessageIdTypedef,
 SeverityNames, FacilityNames, and LanguageNames keywords are
 optional and not required.



 The MessageIdTypedef keyword gives a typedef name that is used in a
 type cast for each message code in the generated include file. Each
 message code appears in the include file with the format: #define
 name ((type) 0xnnnnnnnn) The default value for type is empty, and no
 type cast is generated. It is the programmer's responsibility to
 specify a typedef statement in the application source code to define
 the type. The type used in the typedef must be large enough to
 accomodate the entire 32-bit message code.


 Use Default

 The SeverityNames keyword defines the set of names that are allowed
 as the value of the Severity keyword in the message definition. The
 set is delimited by left and right parentheses. Associated with each
 severity name is a number that, when shifted left by 30, gives the
 bit pattern to logical-OR with the Facility value and MessageId
 value to form the full 32-bit message code. The default value of
 this keyword is:

 SeverityNames=(
   Success=0x0
   Informational=0x1
   Warning=0x2
   Error=0x3
   )

 Severity values occupy the high two bits of a 32-bit message code.
 Any severity value that does not fit in two bits is an error. The
 severity codes can be given symbolic names by following each value
 with :name


 XXX - Default facility names?
 The FacilityNames keyword defines the set of names that are allowed
 as the value of the Facility keyword in the message definition. The
 set is delimited by left and right parentheses. Associated with each
 facility name is a number that, when shift it left by 16 bits, gives
 the bit pattern to logical-OR with the Severity value and MessageId
 value to form the full 32-bit message code. The default value of
 this keyword is:

 FacilityNames=(
   System=0x0FF
   Application=0xFFF
   )

 Facility codes occupy the low order 12 bits of the high order
 16-bits of a 32-bit message code. Any facility code that does not
 fit in 12 bits is an error. This allows for 4,096 facility codes.
 The first 256 codes are reserved for use by the system software. The
 facility codes can be given symbolic names by following each value
 with :name


 The LanguageNames keyword defines the set of names that are allowed
 as the value of the Language keyword in the message definition. The
 set is delimited by left and right parentheses. Associated with each
 language name is a number and a file name that are used to name the
 generated resource file that contains the messages for that
 language. The number corresponds to the language identifier to use
 in the resource table. The number is separated from the file name
 with a colon. The initial value of LanguageNames is:

 LanguageNames=(English=1:MSG00001)

 Any new names in the source file which don't override the built-in
 names are added to the list of valid languages. This allows an
 application to support private languages with descriptive names.


-------------------------------------------------------------------------
 MESSAGE DEFINITION SECTION

 Following the header section is the body of the Message Compiler
 source file. The body consists of zero or more message definitions.
 Each message definition begins with one or more of the following
 statements:

 MessageId = [number|+number]
 Severity = severity_name
 Facility = facility_name
 SymbolicName = name

 The MessageId statement marks the beginning of the message
 definition. A MessageID statement is required for each message,
 although the value is optional. If no value is specified, the value
 used is the previous value for the facility plus one. If the value
 is specified as +number then the value used is the previous value
 for the facility, plus the number after the plus sign. Otherwise, if
 a numeric value is given, that value is used. Any MessageId value
 that does not fit in 16 bits is an error.

 The Severity and Facility statements are optional. These statements
 specify additional bits to OR into the final 32-bit message code. If
 not specified they default to the value last specified for a message
 definition. The initial values prior to processing the first message
 definition are:

 Severity=Success
 Facility=Application

 The value associated with Severity and Facility must match one of
 the names given in the FacilityNames and SeverityNames statements in
 the header section. The SymbolicName statement allows you to
 associate a C/C++ symbolic constant with the final 32-bit message
 code.
 */
//
//  Values are 32 bit values laid out as follows:
//
//   3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
//   1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
//  +---+-+-+-----------------------+-------------------------------+
//  |Sev|C|R|     Facility          |               Code            |
//  +---+-+-+-----------------------+-------------------------------+
//
//  where
//
//      Sev - is the severity code
//
//          00 - Success
//          01 - Informational
//          10 - Warning
//          11 - Error
//
//      C - is the Customer code flag
//
//      R - is a reserved bit
//
//      Facility - is the facility code
//
//      Code - is the facility's status code
//
//
// Define the facility codes
//


//
// Define the severity codes
//


//
// MessageId: MSG_ER1
//
// MessageText:
//
// %1
//
#define MSG_ER1                          ((DWORD)0xC0000001L)

//
// MessageId: MSG_ER2
//
// MessageText:
//
// %1
//
#define MSG_ER2                          ((DWORD)0xC0000002L)

//
// MessageId: MSG_ER3
//
// MessageText:
//
// %1
//
#define MSG_ER3                          ((DWORD)0xC0000003L)

//
// MessageId: MSG_ER4
//
// MessageText:
//
// %1
//
#define MSG_ER4                          ((DWORD)0xC0000004L)

//
// MessageId: MSG_ER5
//
// MessageText:
//
// %1
//
#define MSG_ER5                          ((DWORD)0xC0000005L)

//
// MessageId: MSG_ER6
//
// MessageText:
//
// %1
//
#define MSG_ER6                          ((DWORD)0xC0000006L)

//
// MessageId: MSG_ER7
//
// MessageText:
//
// %1
//
#define MSG_ER7                          ((DWORD)0xC0000007L)

//
// MessageId: MSG_ER8
//
// MessageText:
//
// %1
//
#define MSG_ER8                          ((DWORD)0xC0000008L)

//
// MessageId: MSG_ER9
//
// MessageText:
//
// %1
//
#define MSG_ER9                          ((DWORD)0xC0000009L)

//
// MessageId: MSG_IR1
//
// MessageText:
//
// %1
//
#define MSG_IR1                          ((DWORD)0x40000001L)

//
// MessageId: MSG_IR2
//
// MessageText:
//
// %1
//
#define MSG_IR2                          ((DWORD)0x40000002L)

//
// MessageId: MSG_IR3
//
// MessageText:
//
// %1
//
#define MSG_IR3                          ((DWORD)0x40000003L)

//
// MessageId: MSG_IR4
//
// MessageText:
//
// %1
//
#define MSG_IR4                          ((DWORD)0x40000004L)

//
// MessageId: MSG_IR5
//
// MessageText:
//
// %1
//
#define MSG_IR5                          ((DWORD)0x40000005L)

//
// MessageId: MSG_IR6
//
// MessageText:
//
// %1
//
#define MSG_IR6                          ((DWORD)0x40000006L)

//
// MessageId: MSG_IR7
//
// MessageText:
//
// %1
//
#define MSG_IR7                          ((DWORD)0x40000007L)

//
// MessageId: MSG_IR8
//
// MessageText:
//
// %1
//
#define MSG_IR8                          ((DWORD)0x40000008L)

//
// MessageId: MSG_IR9
//
// MessageText:
//
// %1
//
#define MSG_IR9                          ((DWORD)0x40000009L)

//
// MessageId: MSG_SR1
//
// MessageText:
//
// %1
//
#define MSG_SR1                          ((DWORD)0x00000001L)

//
// MessageId: MSG_SR2
//
// MessageText:
//
// %1
//
#define MSG_SR2                          ((DWORD)0x00000002L)

//
// MessageId: MSG_SR3
//
// MessageText:
//
// %1
//
#define MSG_SR3                          ((DWORD)0x00000003L)

//
// MessageId: MSG_SR4
//
// MessageText:
//
// %1
//
#define MSG_SR4                          ((DWORD)0x00000004L)

//
// MessageId: MSG_SR5
//
// MessageText:
//
// %1
//
#define MSG_SR5                          ((DWORD)0x00000005L)

//
// MessageId: MSG_SR6
//
// MessageText:
//
// %1
//
#define MSG_SR6                          ((DWORD)0x00000006L)

//
// MessageId: MSG_SR7
//
// MessageText:
//
// %1
//
#define MSG_SR7                          ((DWORD)0x00000007L)

//
// MessageId: MSG_SR8
//
// MessageText:
//
// %1
//
#define MSG_SR8                          ((DWORD)0x00000008L)

//
// MessageId: MSG_SR9
//
// MessageText:
//
// %1
//
#define MSG_SR9                          ((DWORD)0x00000009L)

//
// MessageId: MSG_WR1
//
// MessageText:
//
// %1
//
#define MSG_WR1                          ((DWORD)0x80000001L)

//
// MessageId: MSG_WR2
//
// MessageText:
//
// %1
//
#define MSG_WR2                          ((DWORD)0x80000002L)

//
// MessageId: MSG_WR3
//
// MessageText:
//
// %1
//
#define MSG_WR3                          ((DWORD)0x80000003L)

//
// MessageId: MSG_WR4
//
// MessageText:
//
// %1
//
#define MSG_WR4                          ((DWORD)0x80000004L)

//
// MessageId: MSG_WR5
//
// MessageText:
//
// %1
//
#define MSG_WR5                          ((DWORD)0x80000005L)

//
// MessageId: MSG_WR6
//
// MessageText:
//
// %1
//
#define MSG_WR6                          ((DWORD)0x80000006L)

//
// MessageId: MSG_WR7
//
// MessageText:
//
// %1
//
#define MSG_WR7                          ((DWORD)0x80000007L)

//
// MessageId: MSG_WR8
//
// MessageText:
//
// %1
//
#define MSG_WR8                          ((DWORD)0x80000008L)

//
// MessageId: MSG_WR9
//
// MessageText:
//
// %1
//
#define MSG_WR9                          ((DWORD)0x80000009L)

