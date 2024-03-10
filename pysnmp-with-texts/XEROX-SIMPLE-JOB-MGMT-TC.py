"""SNMP MIB module (XEROX-SIMPLE-JOB-MGMT-TC) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-SIMPLE-JOB-MGMT-TC
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:28 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance")

(TimeTicks,
 NotificationType,
 Gauge32,
 ObjectIdentity,
 Integer32,
 Unsigned32,
 Bits,
 iso,
 IpAddress,
 Counter32,
 ModuleIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Counter64,
 MibIdentifier) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "TimeTicks",
    "NotificationType",
    "Gauge32",
    "ObjectIdentity",
    "Integer32",
    "Unsigned32",
    "Bits",
    "iso",
    "IpAddress",
    "Counter32",
    "ModuleIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Counter64",
    "MibIdentifier")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmSimpleJobMgmtTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 75)
)
xcmSimpleJobMgmtTC.setLastUpdated("0209170000Z")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtTC.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmSimpleJobMgmtTC.setContactInfo("""\
 XCMI Editors Email: coherence@crt.xerox.com
""")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtTC.setDescription("""\
Version: 5.10.pub Textual Conventions companion to the XCMI Simple Job Mgmt
MIB, the MIB module for performing lightweight management of jobs in network
accessible host systems. See: Document Printing Application - Part 1: Abstract
Service (ISO/IEC 10175-1 / Final Text, March 1996). See: POSIX System
Administration - Part 4: Print Interfaces (IEEE 1387.4 / Draft 8, October
1994). See: OSI Reference Model - Part 1: Basic Reference Model (CCITT
X.200:1992 | ISO 7498-1:1992). Copyright (C) 1997-2002 Xerox Corporation. All
Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmSimpleJobMgmtGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Simple Job Mgmt MIB groups supported by this management agent
implementation (ie, version) on this host system, specified in a bit-mask. The
current set of values (which may be extended in the future) is given below: 1 :
simpleJobBaseGroup 2 : simpleJobMgmtGroup 4 : simpleJobInterceptGroup Usage:
Conforming management agents shall ALWAYS accurately report their support for
XCMI Simple Job Mgmt MIB groups.
"""


class XcmSimpleJobMgmtOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              1401,
              1402,
              1403,
              1404,
              1408,
              1409,
              1411,
              1412,
              1413,
              1414,
              1415,
              1502,
              1503,
              1504,
              1512,
              1514,
              2401,
              2501)
        )
    )
    namedValues = NamedValues(
        *(("docDelete", 1502),
          ("docList", 1503),
          ("docManage", 2501),
          ("docModify", 1512),
          ("docRemove", 1514),
          ("docSet", 1504),
          ("jobCreate", 1401),
          ("jobDelete", 1402),
          ("jobInterrupt", 1411),
          ("jobList", 1403),
          ("jobManage", 2401),
          ("jobModify", 1412),
          ("jobPause", 1408),
          ("jobPromote", 1413),
          ("jobRemove", 1414),
          ("jobResubmit", 1415),
          ("jobResume", 1409),
          ("jobSet", 1404),
          ("none", 0),
          ("other", 1),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The simple job management operation associated with this conceptual row in the
'xcmSimpleJobMgmtTable' and the 'xcmJobGenBasicTable' (XCMI Job Monitoring
MIB), OR this conceptual row in the 'xcmSimpleJobInterceptTable' and the
'xcmJobClientId' object (XCMI Job Monitoring MIB). Note: The enum of '0' (zero)
in this textual convention is illegal in strict SMIv1 (see section 3.2.1.1 of
RFC 1155), so this TC must be converted to an integer range for pure SMIv1.
"""


class XcmSimpleJobMgmtData(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
The simple job management data associated with this conceptual row in the
'xcmSimpleJobMgmtTable' and the 'xcmJobGenBasicTable' (XCMI Job Monitoring
MIB), OR this conceptual row in the 'xcmSimpleJobInterceptTable' and the
'xcmJobClientId' object (XCMI Job Monitoring MIB).
"""


# MIB Managed Objects in the order of their OIDs

_XCmSimpleJobDummy_ObjectIdentity = ObjectIdentity
xCmSimpleJobDummy = _XCmSimpleJobDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 75, 999)
)
_XCmSimpleJobMgmtGroupSupport_Type = XcmSimpleJobMgmtGroupSupport
_XCmSimpleJobMgmtGroupSupport_Object = MibScalar
xCmSimpleJobMgmtGroupSupport = _XCmSimpleJobMgmtGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 75, 999, 1),
    _XCmSimpleJobMgmtGroupSupport_Type()
)
xCmSimpleJobMgmtGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSimpleJobMgmtGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmSimpleJobMgmtGroupSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmSimpleJobMgmtOperation_Type = XcmSimpleJobMgmtOperation
_XCmSimpleJobMgmtOperation_Object = MibScalar
xCmSimpleJobMgmtOperation = _XCmSimpleJobMgmtOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 75, 999, 2),
    _XCmSimpleJobMgmtOperation_Type()
)
xCmSimpleJobMgmtOperation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSimpleJobMgmtOperation.setStatus("current")
if mibBuilder.loadTexts:
    xCmSimpleJobMgmtOperation.setDescription("""\
Dummy - DO NOT USE
""")
_XCmSimpleJobMgmtData_Type = XcmSimpleJobMgmtData
_XCmSimpleJobMgmtData_Object = MibScalar
xCmSimpleJobMgmtData = _XCmSimpleJobMgmtData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 75, 999, 3),
    _XCmSimpleJobMgmtData_Type()
)
xCmSimpleJobMgmtData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSimpleJobMgmtData.setStatus("current")
if mibBuilder.loadTexts:
    xCmSimpleJobMgmtData.setDescription("""\
Dummy - DO NOT USE
""")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-SIMPLE-JOB-MGMT-TC",
    **{"XcmSimpleJobMgmtGroupSupport": XcmSimpleJobMgmtGroupSupport,
       "XcmSimpleJobMgmtOperation": XcmSimpleJobMgmtOperation,
       "XcmSimpleJobMgmtData": XcmSimpleJobMgmtData,
       "xcmSimpleJobMgmtTC": xcmSimpleJobMgmtTC,
       "xCmSimpleJobDummy": xCmSimpleJobDummy,
       "xCmSimpleJobMgmtGroupSupport": xCmSimpleJobMgmtGroupSupport,
       "xCmSimpleJobMgmtOperation": xCmSimpleJobMgmtOperation,
       "xCmSimpleJobMgmtData": xCmSimpleJobMgmtData}
)
