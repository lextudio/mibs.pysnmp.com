"""SNMP MIB module (XEROX-SIMPLE-JOB-MGMT-TC) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-SIMPLE-JOB-MGMT-TC
Produced by pysmi-1.3.3 at Sun Mar 10 06:00:46 2024
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
 ModuleIdentity,
 Counter32,
 IpAddress,
 Counter64,
 ObjectIdentity,
 Bits,
 Unsigned32,
 iso,
 Gauge32,
 Integer32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 MibIdentifier) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "TimeTicks",
    "ModuleIdentity",
    "Counter32",
    "IpAddress",
    "Counter64",
    "ObjectIdentity",
    "Bits",
    "Unsigned32",
    "iso",
    "Gauge32",
    "Integer32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "MibIdentifier")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmSimpleJobMgmtTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 75)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmSimpleJobMgmtGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



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



class XcmSimpleJobMgmtData(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



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
_XCmSimpleJobMgmtOperation_Type = XcmSimpleJobMgmtOperation
_XCmSimpleJobMgmtOperation_Object = MibScalar
xCmSimpleJobMgmtOperation = _XCmSimpleJobMgmtOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 75, 999, 2),
    _XCmSimpleJobMgmtOperation_Type()
)
xCmSimpleJobMgmtOperation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSimpleJobMgmtOperation.setStatus("current")
_XCmSimpleJobMgmtData_Type = XcmSimpleJobMgmtData
_XCmSimpleJobMgmtData_Object = MibScalar
xCmSimpleJobMgmtData = _XCmSimpleJobMgmtData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 75, 999, 3),
    _XCmSimpleJobMgmtData_Type()
)
xCmSimpleJobMgmtData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSimpleJobMgmtData.setStatus("current")

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
