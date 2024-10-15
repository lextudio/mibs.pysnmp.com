# SNMP MIB module (XEROX-SIMPLE-JOB-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-SIMPLE-JOB-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:37 2024
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(Ordinal32,
 XcmFixedLocaleDisplayString,
 XcmGenSNMPv2ErrorStatus) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Ordinal32",
    "XcmFixedLocaleDisplayString",
    "XcmGenSNMPv2ErrorStatus")

(xcmJobGenBasicEntry,
 xcmJobIdentifierOnSystem) = mibBuilder.importSymbols(
    "XEROX-JOB-MONITORING-MIB",
    "xcmJobGenBasicEntry",
    "xcmJobIdentifierOnSystem")

(XcmSimpleJobMgmtData,
 XcmSimpleJobMgmtGroupSupport,
 XcmSimpleJobMgmtOperation) = mibBuilder.importSymbols(
    "XEROX-SIMPLE-JOB-MGMT-TC",
    "XcmSimpleJobMgmtData",
    "XcmSimpleJobMgmtGroupSupport",
    "XcmSimpleJobMgmtOperation")


# MODULE-IDENTITY

xcmSimpleJobMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmSimpleJobBase_ObjectIdentity = ObjectIdentity
xcmSimpleJobBase = _XcmSimpleJobBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1)
)
_XcmSimpleJobBaseTable_Object = MibTable
xcmSimpleJobBaseTable = _XcmSimpleJobBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2)
)
if mibBuilder.loadTexts:
    xcmSimpleJobBaseTable.setStatus("current")
_XcmSimpleJobBaseEntry_Object = MibTableRow
xcmSimpleJobBaseEntry = _XcmSimpleJobBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1)
)
xcmSimpleJobBaseEntry.setIndexNames(
    (0, "XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseIndex"),
)
if mibBuilder.loadTexts:
    xcmSimpleJobBaseEntry.setStatus("current")
_XcmSimpleJobBaseIndex_Type = Ordinal32
_XcmSimpleJobBaseIndex_Object = MibTableColumn
xcmSimpleJobBaseIndex = _XcmSimpleJobBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 1),
    _XcmSimpleJobBaseIndex_Type()
)
xcmSimpleJobBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseIndex.setStatus("current")
_XcmSimpleJobBaseRowStatus_Type = RowStatus
_XcmSimpleJobBaseRowStatus_Object = MibTableColumn
xcmSimpleJobBaseRowStatus = _XcmSimpleJobBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 2),
    _XcmSimpleJobBaseRowStatus_Type()
)
xcmSimpleJobBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseRowStatus.setStatus("current")


class _XcmSimpleJobBaseGroupSupport_Type(XcmSimpleJobMgmtGroupSupport):
    """Custom type xcmSimpleJobBaseGroupSupport based on XcmSimpleJobMgmtGroupSupport"""
    defaultValue = 3


_XcmSimpleJobBaseGroupSupport_Object = MibTableColumn
xcmSimpleJobBaseGroupSupport = _XcmSimpleJobBaseGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 3),
    _XcmSimpleJobBaseGroupSupport_Type()
)
xcmSimpleJobBaseGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseGroupSupport.setStatus("current")


class _XcmSimpleJobBaseCreateSupport_Type(XcmSimpleJobMgmtGroupSupport):
    """Custom type xcmSimpleJobBaseCreateSupport based on XcmSimpleJobMgmtGroupSupport"""
    defaultValue = 0


_XcmSimpleJobBaseCreateSupport_Object = MibTableColumn
xcmSimpleJobBaseCreateSupport = _XcmSimpleJobBaseCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 4),
    _XcmSimpleJobBaseCreateSupport_Type()
)
xcmSimpleJobBaseCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseCreateSupport.setStatus("current")


class _XcmSimpleJobBaseUpdateSupport_Type(XcmSimpleJobMgmtGroupSupport):
    """Custom type xcmSimpleJobBaseUpdateSupport based on XcmSimpleJobMgmtGroupSupport"""
    defaultValue = 2


_XcmSimpleJobBaseUpdateSupport_Object = MibTableColumn
xcmSimpleJobBaseUpdateSupport = _XcmSimpleJobBaseUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 5),
    _XcmSimpleJobBaseUpdateSupport_Type()
)
xcmSimpleJobBaseUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseUpdateSupport.setStatus("current")
_XcmSimpleJobMgmtMIBConformance_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmtMIBConformance = _XcmSimpleJobMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2)
)
_XcmSimpleJobMgmtMIBGroups_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmtMIBGroups = _XcmSimpleJobMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 2)
)
_XcmSimpleJobMgmt_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmt = _XcmSimpleJobMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3)
)
_XcmSimpleJobMgmtV1EventOID_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmtV1EventOID = _XcmSimpleJobMgmtV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 1)
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtV1EventOID.setStatus("current")
_XcmSimpleJobMgmtV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmtV2EventPrefix = _XcmSimpleJobMgmtV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 1, 0)
)
_XcmSimpleJobMgmtTable_Object = MibTable
xcmSimpleJobMgmtTable = _XcmSimpleJobMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2)
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtTable.setStatus("current")
_XcmSimpleJobMgmtEntry_Object = MibTableRow
xcmSimpleJobMgmtEntry = _XcmSimpleJobMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1)
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtEntry.setStatus("current")
_XcmSimpleJobMgmtOperation_Type = XcmSimpleJobMgmtOperation
_XcmSimpleJobMgmtOperation_Object = MibTableColumn
xcmSimpleJobMgmtOperation = _XcmSimpleJobMgmtOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1, 1),
    _XcmSimpleJobMgmtOperation_Type()
)
xcmSimpleJobMgmtOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtOperation.setStatus("current")


class _XcmSimpleJobMgmtData_Type(XcmSimpleJobMgmtData):
    """Custom type xcmSimpleJobMgmtData based on XcmSimpleJobMgmtData"""
    defaultHexValue = ""

    subtypeSpec = XcmSimpleJobMgmtData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSimpleJobMgmtData_Type.__name__ = "XcmSimpleJobMgmtData"
_XcmSimpleJobMgmtData_Object = MibTableColumn
xcmSimpleJobMgmtData = _XcmSimpleJobMgmtData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1, 2),
    _XcmSimpleJobMgmtData_Type()
)
xcmSimpleJobMgmtData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtData.setStatus("current")
_XcmSimpleJobMgmtStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmSimpleJobMgmtStatus_Object = MibTableColumn
xcmSimpleJobMgmtStatus = _XcmSimpleJobMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1, 3),
    _XcmSimpleJobMgmtStatus_Type()
)
xcmSimpleJobMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtStatus.setStatus("current")


class _XcmSimpleJobMgmtInProgress_Type(TruthValue):
    """Custom type xcmSimpleJobMgmtInProgress based on TruthValue"""


_XcmSimpleJobMgmtInProgress_Object = MibTableColumn
xcmSimpleJobMgmtInProgress = _XcmSimpleJobMgmtInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1, 4),
    _XcmSimpleJobMgmtInProgress_Type()
)
xcmSimpleJobMgmtInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtInProgress.setStatus("current")
_XcmSimpleJobIntercept_ObjectIdentity = ObjectIdentity
xcmSimpleJobIntercept = _XcmSimpleJobIntercept_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4)
)
_XcmSimpleJobInterceptV1EventOID_ObjectIdentity = ObjectIdentity
xcmSimpleJobInterceptV1EventOID = _XcmSimpleJobInterceptV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 1)
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptV1EventOID.setStatus("current")
_XcmSimpleJobInterceptV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSimpleJobInterceptV2EventPrefix = _XcmSimpleJobInterceptV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 1, 0)
)
_XcmSimpleJobInterceptTable_Object = MibTable
xcmSimpleJobInterceptTable = _XcmSimpleJobInterceptTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2)
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptTable.setStatus("current")
_XcmSimpleJobInterceptEntry_Object = MibTableRow
xcmSimpleJobInterceptEntry = _XcmSimpleJobInterceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1)
)
xcmSimpleJobInterceptEntry.setIndexNames(
    (0, "XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptClientId"),
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptEntry.setStatus("current")


class _XcmSimpleJobInterceptClientId_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSimpleJobInterceptClientId based on XcmFixedLocaleDisplayString"""
    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_XcmSimpleJobInterceptClientId_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSimpleJobInterceptClientId_Object = MibTableColumn
xcmSimpleJobInterceptClientId = _XcmSimpleJobInterceptClientId_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 1),
    _XcmSimpleJobInterceptClientId_Type()
)
xcmSimpleJobInterceptClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptClientId.setStatus("current")
_XcmSimpleJobInterceptRowStatus_Type = RowStatus
_XcmSimpleJobInterceptRowStatus_Object = MibTableColumn
xcmSimpleJobInterceptRowStatus = _XcmSimpleJobInterceptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 2),
    _XcmSimpleJobInterceptRowStatus_Type()
)
xcmSimpleJobInterceptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptRowStatus.setStatus("current")
_XcmSimpleJobInterceptOperation_Type = XcmSimpleJobMgmtOperation
_XcmSimpleJobInterceptOperation_Object = MibTableColumn
xcmSimpleJobInterceptOperation = _XcmSimpleJobInterceptOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 3),
    _XcmSimpleJobInterceptOperation_Type()
)
xcmSimpleJobInterceptOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptOperation.setStatus("current")


class _XcmSimpleJobInterceptData_Type(XcmSimpleJobMgmtData):
    """Custom type xcmSimpleJobInterceptData based on XcmSimpleJobMgmtData"""
    defaultHexValue = ""

    subtypeSpec = XcmSimpleJobMgmtData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSimpleJobInterceptData_Type.__name__ = "XcmSimpleJobMgmtData"
_XcmSimpleJobInterceptData_Object = MibTableColumn
xcmSimpleJobInterceptData = _XcmSimpleJobInterceptData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 4),
    _XcmSimpleJobInterceptData_Type()
)
xcmSimpleJobInterceptData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptData.setStatus("current")
_XcmSimpleJobInterceptStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmSimpleJobInterceptStatus_Object = MibTableColumn
xcmSimpleJobInterceptStatus = _XcmSimpleJobInterceptStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 5),
    _XcmSimpleJobInterceptStatus_Type()
)
xcmSimpleJobInterceptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptStatus.setStatus("current")


class _XcmSimpleJobInterceptInProgress_Type(TruthValue):
    """Custom type xcmSimpleJobInterceptInProgress based on TruthValue"""


_XcmSimpleJobInterceptInProgress_Object = MibTableColumn
xcmSimpleJobInterceptInProgress = _XcmSimpleJobInterceptInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 6),
    _XcmSimpleJobInterceptInProgress_Type()
)
xcmSimpleJobInterceptInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptInProgress.setStatus("current")
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-SIMPLE-JOB-MGMT-MIB",
     "xcmSimpleJobMgmtEntry")
)
xcmSimpleJobMgmtEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())

# Managed Objects groups

xcmSimpleJobBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 2, 1)
)
xcmSimpleJobBaseGroup.setObjects(
      *(("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseRowStatus"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseGroupSupport"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseCreateSupport"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobBaseGroup.setStatus("current")

xcmSimpleJobMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 2, 3)
)
xcmSimpleJobMgmtGroup.setObjects(
      *(("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtOperation"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtData"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtStatus"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtInProgress"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtGroup.setStatus("current")

xcmSimpleJobInterceptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 2, 4)
)
xcmSimpleJobInterceptGroup.setObjects(
      *(("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptClientId"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptRowStatus"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptOperation"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptData"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptStatus"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptInProgress"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptGroup.setStatus("current")


# Notification objects

xcmSimpleJobMgmtV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 1, 0, 1)
)
xcmSimpleJobMgmtV2Event.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtOperation"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtStatus"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtV2Event.setStatus(
        "current"
    )

xcmSimpleJobInterceptV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 1, 0, 1)
)
xcmSimpleJobInterceptV2Event.setObjects(
      *(("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptClientId"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptOperation"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptStatus"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptV2Event.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

xcmSimpleJobMgmtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 3)
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-SIMPLE-JOB-MGMT-MIB",
    **{"xcmSimpleJobMgmtMIB": xcmSimpleJobMgmtMIB,
       "xcmSimpleJobBase": xcmSimpleJobBase,
       "xcmSimpleJobBaseTable": xcmSimpleJobBaseTable,
       "xcmSimpleJobBaseEntry": xcmSimpleJobBaseEntry,
       "xcmSimpleJobBaseIndex": xcmSimpleJobBaseIndex,
       "xcmSimpleJobBaseRowStatus": xcmSimpleJobBaseRowStatus,
       "xcmSimpleJobBaseGroupSupport": xcmSimpleJobBaseGroupSupport,
       "xcmSimpleJobBaseCreateSupport": xcmSimpleJobBaseCreateSupport,
       "xcmSimpleJobBaseUpdateSupport": xcmSimpleJobBaseUpdateSupport,
       "xcmSimpleJobMgmtMIBConformance": xcmSimpleJobMgmtMIBConformance,
       "xcmSimpleJobMgmtMIBGroups": xcmSimpleJobMgmtMIBGroups,
       "xcmSimpleJobBaseGroup": xcmSimpleJobBaseGroup,
       "xcmSimpleJobMgmtGroup": xcmSimpleJobMgmtGroup,
       "xcmSimpleJobInterceptGroup": xcmSimpleJobInterceptGroup,
       "xcmSimpleJobMgmtMIBCompliance": xcmSimpleJobMgmtMIBCompliance,
       "xcmSimpleJobMgmt": xcmSimpleJobMgmt,
       "xcmSimpleJobMgmtV1EventOID": xcmSimpleJobMgmtV1EventOID,
       "xcmSimpleJobMgmtV2EventPrefix": xcmSimpleJobMgmtV2EventPrefix,
       "xcmSimpleJobMgmtV2Event": xcmSimpleJobMgmtV2Event,
       "xcmSimpleJobMgmtTable": xcmSimpleJobMgmtTable,
       "xcmSimpleJobMgmtEntry": xcmSimpleJobMgmtEntry,
       "xcmSimpleJobMgmtOperation": xcmSimpleJobMgmtOperation,
       "xcmSimpleJobMgmtData": xcmSimpleJobMgmtData,
       "xcmSimpleJobMgmtStatus": xcmSimpleJobMgmtStatus,
       "xcmSimpleJobMgmtInProgress": xcmSimpleJobMgmtInProgress,
       "xcmSimpleJobIntercept": xcmSimpleJobIntercept,
       "xcmSimpleJobInterceptV1EventOID": xcmSimpleJobInterceptV1EventOID,
       "xcmSimpleJobInterceptV2EventPrefix": xcmSimpleJobInterceptV2EventPrefix,
       "xcmSimpleJobInterceptV2Event": xcmSimpleJobInterceptV2Event,
       "xcmSimpleJobInterceptTable": xcmSimpleJobInterceptTable,
       "xcmSimpleJobInterceptEntry": xcmSimpleJobInterceptEntry,
       "xcmSimpleJobInterceptClientId": xcmSimpleJobInterceptClientId,
       "xcmSimpleJobInterceptRowStatus": xcmSimpleJobInterceptRowStatus,
       "xcmSimpleJobInterceptOperation": xcmSimpleJobInterceptOperation,
       "xcmSimpleJobInterceptData": xcmSimpleJobInterceptData,
       "xcmSimpleJobInterceptStatus": xcmSimpleJobInterceptStatus,
       "xcmSimpleJobInterceptInProgress": xcmSimpleJobInterceptInProgress}
)
