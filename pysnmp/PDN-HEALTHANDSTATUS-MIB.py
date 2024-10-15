# SNMP MIB module (PDN-HEALTHANDSTATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-HEALTHANDSTATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:43 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_devStatus,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-devStatus")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DevStatus_ObjectIdentity = ObjectIdentity
devStatus = _DevStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1)
)


class _DevHealthAndStatus_Type(DisplayString):
    """Custom type devHealthAndStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevHealthAndStatus_Type.__name__ = "DisplayString"
_DevHealthAndStatus_Object = MibScalar
devHealthAndStatus = _DevHealthAndStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 1),
    _DevHealthAndStatus_Type()
)
devHealthAndStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devHealthAndStatus.setStatus("mandatory")


class _DevSelfTestResults_Type(DisplayString):
    """Custom type devSelfTestResults based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevSelfTestResults_Type.__name__ = "DisplayString"
_DevSelfTestResults_Object = MibScalar
devSelfTestResults = _DevSelfTestResults_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 2),
    _DevSelfTestResults_Type()
)
devSelfTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSelfTestResults.setStatus("mandatory")


class _DevAbortStatus_Type(DisplayString):
    """Custom type devAbortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevAbortStatus_Type.__name__ = "DisplayString"
_DevAbortStatus_Object = MibScalar
devAbortStatus = _DevAbortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 3),
    _DevAbortStatus_Type()
)
devAbortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devAbortStatus.setStatus("mandatory")
_DevSNMPSetStatusTable_Object = MibTable
devSNMPSetStatusTable = _DevSNMPSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    devSNMPSetStatusTable.setStatus("mandatory")
_DevSNMPSetStatusEntry_Object = MibTableRow
devSNMPSetStatusEntry = _DevSNMPSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 4, 1)
)
devSNMPSetStatusEntry.setIndexNames(
    (0, "PDN-HEALTHANDSTATUS-MIB", "devSNMPSetReqId"),
)
if mibBuilder.loadTexts:
    devSNMPSetStatusEntry.setStatus("mandatory")
_DevSNMPSetReqId_Type = Integer32
_DevSNMPSetReqId_Object = MibTableColumn
devSNMPSetReqId = _DevSNMPSetReqId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 4, 1, 1),
    _DevSNMPSetReqId_Type()
)
devSNMPSetReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSNMPSetReqId.setStatus("mandatory")


class _DevSNMPSetStatus_Type(DisplayString):
    """Custom type devSNMPSetStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevSNMPSetStatus_Type.__name__ = "DisplayString"
_DevSNMPSetStatus_Object = MibTableColumn
devSNMPSetStatus = _DevSNMPSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 4, 1, 2),
    _DevSNMPSetStatus_Type()
)
devSNMPSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSNMPSetStatus.setStatus("mandatory")
_DevAuthenticationFailureIpAddress_Type = IpAddress
_DevAuthenticationFailureIpAddress_Object = MibScalar
devAuthenticationFailureIpAddress = _DevAuthenticationFailureIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 5),
    _DevAuthenticationFailureIpAddress_Type()
)
devAuthenticationFailureIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devAuthenticationFailureIpAddress.setStatus("mandatory")


class _DevLastTrapString_Type(DisplayString):
    """Custom type devLastTrapString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevLastTrapString_Type.__name__ = "DisplayString"
_DevLastTrapString_Object = MibScalar
devLastTrapString = _DevLastTrapString_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 6),
    _DevLastTrapString_Type()
)
devLastTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devLastTrapString.setStatus("mandatory")


class _DevFailureStatus_Type(DisplayString):
    """Custom type devFailureStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevFailureStatus_Type.__name__ = "DisplayString"
_DevFailureStatus_Object = MibScalar
devFailureStatus = _DevFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 7),
    _DevFailureStatus_Type()
)
devFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFailureStatus.setStatus("mandatory")
_DevStatusTrapEnable_Type = Integer32
_DevStatusTrapEnable_Object = MibScalar
devStatusTrapEnable = _DevStatusTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 8),
    _DevStatusTrapEnable_Type()
)
devStatusTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devStatusTrapEnable.setStatus("mandatory")
_DevSelfTestResultTable_Object = MibTable
devSelfTestResultTable = _DevSelfTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 9)
)
if mibBuilder.loadTexts:
    devSelfTestResultTable.setStatus("mandatory")
_DevSelfTestResultEntry_Object = MibTableRow
devSelfTestResultEntry = _DevSelfTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 9, 1)
)
devSelfTestResultEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    devSelfTestResultEntry.setStatus("mandatory")
_DevSelfTestResult_Type = DisplayString
_DevSelfTestResult_Object = MibTableColumn
devSelfTestResult = _DevSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 9, 1, 1),
    _DevSelfTestResult_Type()
)
devSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSelfTestResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects

devSelfTestFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 0, 1)
)
devSelfTestFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-HEALTHANDSTATUS-MIB", "devSelfTestResults"))
)
if mibBuilder.loadTexts:
    devSelfTestFailure.setStatus(
        ""
    )

deviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4, 1, 0, 2)
)
deviceFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-HEALTHANDSTATUS-MIB", "devFailureStatus"))
)
if mibBuilder.loadTexts:
    deviceFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-HEALTHANDSTATUS-MIB",
    **{"devStatus": devStatus,
       "devSelfTestFailure": devSelfTestFailure,
       "deviceFailure": deviceFailure,
       "devHealthAndStatus": devHealthAndStatus,
       "devSelfTestResults": devSelfTestResults,
       "devAbortStatus": devAbortStatus,
       "devSNMPSetStatusTable": devSNMPSetStatusTable,
       "devSNMPSetStatusEntry": devSNMPSetStatusEntry,
       "devSNMPSetReqId": devSNMPSetReqId,
       "devSNMPSetStatus": devSNMPSetStatus,
       "devAuthenticationFailureIpAddress": devAuthenticationFailureIpAddress,
       "devLastTrapString": devLastTrapString,
       "devFailureStatus": devFailureStatus,
       "devStatusTrapEnable": devStatusTrapEnable,
       "devSelfTestResultTable": devSelfTestResultTable,
       "devSelfTestResultEntry": devSelfTestResultEntry,
       "devSelfTestResult": devSelfTestResult}
)
