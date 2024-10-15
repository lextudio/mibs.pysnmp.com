# SNMP MIB module (XEROX-JOB-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-JOB-MONITORING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:25 2024
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

(InternationalDisplayString,
 ProductID,
 hrDeviceIndex) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString",
    "ProductID",
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(Cardinal16,
 Cardinal32,
 Cardinal64High,
 Cardinal64Low,
 CodeIndexedStringIndex,
 Ordinal16,
 Ordinal32,
 zeroDotZero) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Cardinal16",
    "Cardinal32",
    "Cardinal64High",
    "Cardinal64Low",
    "CodeIndexedStringIndex",
    "Ordinal16",
    "Ordinal32",
    "zeroDotZero")

(XcmHrDevInfoXStatus,
 XcmHrDevTrafficUnit) = mibBuilder.importSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    "XcmHrDevInfoXStatus",
    "XcmHrDevTrafficUnit")

(XcmJMDocFileNameType,
 XcmJMDocOutputMethod,
 XcmJMDocState,
 XcmJMDocType,
 XcmJMGroupSupport,
 XcmJMImpsCountType,
 XcmJMJobServiceTypeOID,
 XcmJMJobState,
 XcmJMJobStateReasons,
 XcmJMJobX2StateReasons,
 XcmJMJobXStateReasons,
 XcmJMMediumType) = mibBuilder.importSymbols(
    "XEROX-JOB-MONITORING-TC",
    "XcmJMDocFileNameType",
    "XcmJMDocOutputMethod",
    "XcmJMDocState",
    "XcmJMDocType",
    "XcmJMGroupSupport",
    "XcmJMImpsCountType",
    "XcmJMJobServiceTypeOID",
    "XcmJMJobState",
    "XcmJMJobStateReasons",
    "XcmJMJobX2StateReasons",
    "XcmJMJobXStateReasons",
    "XcmJMMediumType")

(XcmPrtChannelType,
 XcmPrtInterpreterLangFamily,
 XcmPrtMediumSize,
 XcmPrtPrintQuality) = mibBuilder.importSymbols(
    "XEROX-PRINTER-EXT-TC",
    "XcmPrtChannelType",
    "XcmPrtInterpreterLangFamily",
    "XcmPrtMediumSize",
    "XcmPrtPrintQuality")


# MODULE-IDENTITY

xcmJobMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmJobZeroDummy_ObjectIdentity = ObjectIdentity
xcmJobZeroDummy = _XcmJobZeroDummy_ObjectIdentity(
    (0, 0, 59)
)
_XcmJobMonBase_ObjectIdentity = ObjectIdentity
xcmJobMonBase = _XcmJobMonBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1)
)
_XcmJobMonBaseTable_Object = MibTable
xcmJobMonBaseTable = _XcmJobMonBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2)
)
if mibBuilder.loadTexts:
    xcmJobMonBaseTable.setStatus("current")
_XcmJobMonBaseEntry_Object = MibTableRow
xcmJobMonBaseEntry = _XcmJobMonBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1)
)
xcmJobMonBaseEntry.setIndexNames(
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseIndex"),
)
if mibBuilder.loadTexts:
    xcmJobMonBaseEntry.setStatus("current")
_XcmJobMonBaseIndex_Type = Ordinal32
_XcmJobMonBaseIndex_Object = MibTableColumn
xcmJobMonBaseIndex = _XcmJobMonBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 1),
    _XcmJobMonBaseIndex_Type()
)
xcmJobMonBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmJobMonBaseIndex.setStatus("current")
_XcmJobMonBaseRowStatus_Type = RowStatus
_XcmJobMonBaseRowStatus_Object = MibTableColumn
xcmJobMonBaseRowStatus = _XcmJobMonBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 2),
    _XcmJobMonBaseRowStatus_Type()
)
xcmJobMonBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseRowStatus.setStatus("current")


class _XcmJobMonBaseVersionID_Type(ProductID):
    """Custom type xcmJobMonBaseVersionID based on ProductID"""
    defaultValue = (0, 0)


_XcmJobMonBaseVersionID_Object = MibTableColumn
xcmJobMonBaseVersionID = _XcmJobMonBaseVersionID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 3),
    _XcmJobMonBaseVersionID_Type()
)
xcmJobMonBaseVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseVersionID.setStatus("current")


class _XcmJobMonBaseVersionDate_Type(DateAndTime):
    """Custom type xcmJobMonBaseVersionDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobMonBaseVersionDate_Object = MibTableColumn
xcmJobMonBaseVersionDate = _XcmJobMonBaseVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 4),
    _XcmJobMonBaseVersionDate_Type()
)
xcmJobMonBaseVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseVersionDate.setStatus("current")


class _XcmJobMonBaseGroupSupport_Type(XcmJMGroupSupport):
    """Custom type xcmJobMonBaseGroupSupport based on XcmJMGroupSupport"""
    defaultValue = 3


_XcmJobMonBaseGroupSupport_Object = MibTableColumn
xcmJobMonBaseGroupSupport = _XcmJobMonBaseGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 5),
    _XcmJobMonBaseGroupSupport_Type()
)
xcmJobMonBaseGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseGroupSupport.setStatus("current")


class _XcmJobMonBaseCreateSupport_Type(XcmJMGroupSupport):
    """Custom type xcmJobMonBaseCreateSupport based on XcmJMGroupSupport"""
    defaultValue = 0


_XcmJobMonBaseCreateSupport_Object = MibTableColumn
xcmJobMonBaseCreateSupport = _XcmJobMonBaseCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 6),
    _XcmJobMonBaseCreateSupport_Type()
)
xcmJobMonBaseCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseCreateSupport.setStatus("current")


class _XcmJobMonBaseUpdateSupport_Type(XcmJMGroupSupport):
    """Custom type xcmJobMonBaseUpdateSupport based on XcmJMGroupSupport"""
    defaultValue = 0


_XcmJobMonBaseUpdateSupport_Object = MibTableColumn
xcmJobMonBaseUpdateSupport = _XcmJobMonBaseUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 1, 2, 1, 7),
    _XcmJobMonBaseUpdateSupport_Type()
)
xcmJobMonBaseUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMonBaseUpdateSupport.setStatus("current")
_XcmJobMonMIBConformance_ObjectIdentity = ObjectIdentity
xcmJobMonMIBConformance = _XcmJobMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2)
)
_XcmJobMonMIBGroups_ObjectIdentity = ObjectIdentity
xcmJobMonMIBGroups = _XcmJobMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3)
)
_XcmJobGenBasic_ObjectIdentity = ObjectIdentity
xcmJobGenBasic = _XcmJobGenBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6)
)
_XcmJobGenBasicTable_Object = MibTable
xcmJobGenBasicTable = _XcmJobGenBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenBasicTable.setStatus("current")
_XcmJobGenBasicEntry_Object = MibTableRow
xcmJobGenBasicEntry = _XcmJobGenBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1)
)
xcmJobGenBasicEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
)
if mibBuilder.loadTexts:
    xcmJobGenBasicEntry.setStatus("current")


class _XcmJobIdentifierOnSystem_Type(DisplayString):
    """Custom type xcmJobIdentifierOnSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobIdentifierOnSystem_Type.__name__ = "DisplayString"
_XcmJobIdentifierOnSystem_Object = MibTableColumn
xcmJobIdentifierOnSystem = _XcmJobIdentifierOnSystem_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 1),
    _XcmJobIdentifierOnSystem_Type()
)
xcmJobIdentifierOnSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobIdentifierOnSystem.setStatus("current")


class _XcmJobIdentifierUpstream_Type(DisplayString):
    """Custom type xcmJobIdentifierUpstream based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobIdentifierUpstream_Type.__name__ = "DisplayString"
_XcmJobIdentifierUpstream_Object = MibTableColumn
xcmJobIdentifierUpstream = _XcmJobIdentifierUpstream_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 2),
    _XcmJobIdentifierUpstream_Type()
)
xcmJobIdentifierUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobIdentifierUpstream.setStatus("current")


class _XcmJobClientId_Type(OctetString):
    """Custom type xcmJobClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobClientId_Type.__name__ = "OctetString"
_XcmJobClientId_Object = MibTableColumn
xcmJobClientId = _XcmJobClientId_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 3),
    _XcmJobClientId_Type()
)
xcmJobClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobClientId.setStatus("current")


class _XcmJobServiceType_Type(XcmJMJobServiceTypeOID):
    """Custom type xcmJobServiceType based on XcmJMJobServiceTypeOID"""
    defaultValue = (0, 0)


_XcmJobServiceType_Object = MibTableColumn
xcmJobServiceType = _XcmJobServiceType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 4),
    _XcmJobServiceType_Type()
)
xcmJobServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobServiceType.setStatus("current")


class _XcmJobName_Type(CodeIndexedStringIndex):
    """Custom type xcmJobName based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmJobName_Object = MibTableColumn
xcmJobName = _XcmJobName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 5),
    _XcmJobName_Type()
)
xcmJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobName.setStatus("current")


class _XcmJobOwner_Type(CodeIndexedStringIndex):
    """Custom type xcmJobOwner based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmJobOwner_Object = MibTableColumn
xcmJobOwner = _XcmJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 6),
    _XcmJobOwner_Type()
)
xcmJobOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOwner.setStatus("current")


class _XcmJobSourceChannelType_Type(XcmPrtChannelType):
    """Custom type xcmJobSourceChannelType based on XcmPrtChannelType"""


_XcmJobSourceChannelType_Object = MibTableColumn
xcmJobSourceChannelType = _XcmJobSourceChannelType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 7),
    _XcmJobSourceChannelType_Type()
)
xcmJobSourceChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobSourceChannelType.setStatus("current")


class _XcmJobSubmittedLocaleIndex_Type(Cardinal32):
    """Custom type xcmJobSubmittedLocaleIndex based on Cardinal32"""
    defaultValue = 0


_XcmJobSubmittedLocaleIndex_Object = MibTableColumn
xcmJobSubmittedLocaleIndex = _XcmJobSubmittedLocaleIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 8),
    _XcmJobSubmittedLocaleIndex_Type()
)
xcmJobSubmittedLocaleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobSubmittedLocaleIndex.setStatus("current")


class _XcmJobCurrentState_Type(XcmJMJobState):
    """Custom type xcmJobCurrentState based on XcmJMJobState"""


_XcmJobCurrentState_Object = MibTableColumn
xcmJobCurrentState = _XcmJobCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 9),
    _XcmJobCurrentState_Type()
)
xcmJobCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobCurrentState.setStatus("current")


class _XcmJobStateReasons_Type(XcmJMJobStateReasons):
    """Custom type xcmJobStateReasons based on XcmJMJobStateReasons"""
    defaultValue = 0


_XcmJobStateReasons_Object = MibTableColumn
xcmJobStateReasons = _XcmJobStateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 10),
    _XcmJobStateReasons_Type()
)
xcmJobStateReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobStateReasons.setStatus("current")


class _XcmJobXStateReasons_Type(XcmJMJobXStateReasons):
    """Custom type xcmJobXStateReasons based on XcmJMJobXStateReasons"""
    defaultValue = 0


_XcmJobXStateReasons_Object = MibTableColumn
xcmJobXStateReasons = _XcmJobXStateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 11),
    _XcmJobXStateReasons_Type()
)
xcmJobXStateReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobXStateReasons.setStatus("current")


class _XcmJobX2StateReasons_Type(XcmJMJobX2StateReasons):
    """Custom type xcmJobX2StateReasons based on XcmJMJobX2StateReasons"""
    defaultValue = 0


_XcmJobX2StateReasons_Object = MibTableColumn
xcmJobX2StateReasons = _XcmJobX2StateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 6, 1, 1, 12),
    _XcmJobX2StateReasons_Type()
)
xcmJobX2StateReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobX2StateReasons.setStatus("current")
_XcmDevicesAssigned_ObjectIdentity = ObjectIdentity
xcmDevicesAssigned = _XcmDevicesAssigned_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7)
)
_XcmDevicesAssignedTable_Object = MibTable
xcmDevicesAssignedTable = _XcmDevicesAssignedTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1)
)
if mibBuilder.loadTexts:
    xcmDevicesAssignedTable.setStatus("current")
_XcmDevicesAssignedEntry_Object = MibTableRow
xcmDevicesAssignedEntry = _XcmDevicesAssignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1, 1)
)
xcmDevicesAssignedEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmDevicesAssignedHrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmDevicesAssignedEntry.setStatus("current")
_XcmDevicesAssignedHrDeviceIndex_Type = Ordinal32
_XcmDevicesAssignedHrDeviceIndex_Object = MibTableColumn
xcmDevicesAssignedHrDeviceIndex = _XcmDevicesAssignedHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1, 1, 1),
    _XcmDevicesAssignedHrDeviceIndex_Type()
)
xcmDevicesAssignedHrDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmDevicesAssignedHrDeviceIndex.setStatus("current")
_XcmDeviceStateOfDevicesAssigned_Type = XcmHrDevInfoXStatus
_XcmDeviceStateOfDevicesAssigned_Object = MibTableColumn
xcmDeviceStateOfDevicesAssigned = _XcmDeviceStateOfDevicesAssigned_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1, 1, 2),
    _XcmDeviceStateOfDevicesAssigned_Type()
)
xcmDeviceStateOfDevicesAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDeviceStateOfDevicesAssigned.setStatus("current")


class _XcmJobIdentifierDownstream_Type(DisplayString):
    """Custom type xcmJobIdentifierDownstream based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobIdentifierDownstream_Type.__name__ = "DisplayString"
_XcmJobIdentifierDownstream_Object = MibTableColumn
xcmJobIdentifierDownstream = _XcmJobIdentifierDownstream_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 7, 1, 1, 3),
    _XcmJobIdentifierDownstream_Type()
)
xcmJobIdentifierDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobIdentifierDownstream.setStatus("current")
_XcmClientIdMap_ObjectIdentity = ObjectIdentity
xcmClientIdMap = _XcmClientIdMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 8)
)
_XcmClientIdMapTable_Object = MibTable
xcmClientIdMapTable = _XcmClientIdMapTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 8, 1)
)
if mibBuilder.loadTexts:
    xcmClientIdMapTable.setStatus("current")
_XcmClientIdMapEntry_Object = MibTableRow
xcmClientIdMapEntry = _XcmClientIdMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 8, 1, 1)
)
xcmClientIdMapEntry.setIndexNames(
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobClientId"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
)
if mibBuilder.loadTexts:
    xcmClientIdMapEntry.setStatus("current")
_XcmClientIdMapHrDeviceIndex_Type = Ordinal32
_XcmClientIdMapHrDeviceIndex_Object = MibTableColumn
xcmClientIdMapHrDeviceIndex = _XcmClientIdMapHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 8, 1, 1, 2),
    _XcmClientIdMapHrDeviceIndex_Type()
)
xcmClientIdMapHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmClientIdMapHrDeviceIndex.setStatus("current")
_XcmJobGenExt_ObjectIdentity = ObjectIdentity
xcmJobGenExt = _XcmJobGenExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10)
)
_XcmJobGenExtTable_Object = MibTable
xcmJobGenExtTable = _XcmJobGenExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenExtTable.setStatus("current")
_XcmJobGenExtEntry_Object = MibTableRow
xcmJobGenExtEntry = _XcmJobGenExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenExtEntry.setStatus("current")


class _XcmJobOriginator_Type(CodeIndexedStringIndex):
    """Custom type xcmJobOriginator based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmJobOriginator_Object = MibTableColumn
xcmJobOriginator = _XcmJobOriginator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 1),
    _XcmJobOriginator_Type()
)
xcmJobOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOriginator.setStatus("current")


class _XcmJobSubmittingApplication_Type(CodeIndexedStringIndex):
    """Custom type xcmJobSubmittingApplication based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmJobSubmittingApplication_Object = MibTableColumn
xcmJobSubmittingApplication = _XcmJobSubmittingApplication_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 2),
    _XcmJobSubmittingApplication_Type()
)
xcmJobSubmittingApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobSubmittingApplication.setStatus("current")


class _XcmJobComment_Type(CodeIndexedStringIndex):
    """Custom type xcmJobComment based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmJobComment_Object = MibTableColumn
xcmJobComment = _XcmJobComment_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 3),
    _XcmJobComment_Type()
)
xcmJobComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobComment.setStatus("current")


class _XcmJobCopies_Type(Ordinal32):
    """Custom type xcmJobCopies based on Ordinal32"""
    defaultValue = 1


_XcmJobCopies_Object = MibTableColumn
xcmJobCopies = _XcmJobCopies_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 4),
    _XcmJobCopies_Type()
)
xcmJobCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobCopies.setStatus("current")
_XcmJobCopiesCompleted_Type = Counter32
_XcmJobCopiesCompleted_Object = MibTableColumn
xcmJobCopiesCompleted = _XcmJobCopiesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 5),
    _XcmJobCopiesCompleted_Type()
)
xcmJobCopiesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobCopiesCompleted.setStatus("current")


class _XcmJobOutputBinIndex_Type(Integer32):
    """Custom type xcmJobOutputBinIndex based on Integer32"""
    defaultValue = 0


_XcmJobOutputBinIndex_Object = MibTableColumn
xcmJobOutputBinIndex = _XcmJobOutputBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 6),
    _XcmJobOutputBinIndex_Type()
)
xcmJobOutputBinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOutputBinIndex.setStatus("current")


class _XcmJobServiceNameRequested_Type(CodeIndexedStringIndex):
    """Custom type xcmJobServiceNameRequested based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmJobServiceNameRequested_Object = MibTableColumn
xcmJobServiceNameRequested = _XcmJobServiceNameRequested_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 7),
    _XcmJobServiceNameRequested_Type()
)
xcmJobServiceNameRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobServiceNameRequested.setStatus("current")


class _XcmJobPreviousState_Type(XcmJMJobState):
    """Custom type xcmJobPreviousState based on XcmJMJobState"""


_XcmJobPreviousState_Object = MibTableColumn
xcmJobPreviousState = _XcmJobPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 8),
    _XcmJobPreviousState_Type()
)
xcmJobPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobPreviousState.setStatus("current")


class _XcmJobEstimatedCompletionTime_Type(DateAndTime):
    """Custom type xcmJobEstimatedCompletionTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobEstimatedCompletionTime_Object = MibTableColumn
xcmJobEstimatedCompletionTime = _XcmJobEstimatedCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 9),
    _XcmJobEstimatedCompletionTime_Type()
)
xcmJobEstimatedCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobEstimatedCompletionTime.setStatus("current")


class _XcmJobSubmissionTime_Type(DateAndTime):
    """Custom type xcmJobSubmissionTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobSubmissionTime_Object = MibTableColumn
xcmJobSubmissionTime = _XcmJobSubmissionTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 10),
    _XcmJobSubmissionTime_Type()
)
xcmJobSubmissionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobSubmissionTime.setStatus("current")
_XcmJobPagesCompleted_Type = Counter32
_XcmJobPagesCompleted_Object = MibTableColumn
xcmJobPagesCompleted = _XcmJobPagesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 11),
    _XcmJobPagesCompleted_Type()
)
xcmJobPagesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobPagesCompleted.setStatus("current")


class _XcmJobOctetsCompletedHigh_Type(Cardinal64High):
    """Custom type xcmJobOctetsCompletedHigh based on Cardinal64High"""
    defaultValue = 0


_XcmJobOctetsCompletedHigh_Object = MibTableColumn
xcmJobOctetsCompletedHigh = _XcmJobOctetsCompletedHigh_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 12),
    _XcmJobOctetsCompletedHigh_Type()
)
xcmJobOctetsCompletedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOctetsCompletedHigh.setStatus("current")


class _XcmJobOctetsCompletedLow_Type(Cardinal64Low):
    """Custom type xcmJobOctetsCompletedLow based on Cardinal64Low"""
    defaultValue = 0


_XcmJobOctetsCompletedLow_Object = MibTableColumn
xcmJobOctetsCompletedLow = _XcmJobOctetsCompletedLow_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 13),
    _XcmJobOctetsCompletedLow_Type()
)
xcmJobOctetsCompletedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobOctetsCompletedLow.setStatus("current")
_XcmJobErrorCount_Type = Counter32
_XcmJobErrorCount_Object = MibTableColumn
xcmJobErrorCount = _XcmJobErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 14),
    _XcmJobErrorCount_Type()
)
xcmJobErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobErrorCount.setStatus("current")
_XcmJobWarningCount_Type = Counter32
_XcmJobWarningCount_Object = MibTableColumn
xcmJobWarningCount = _XcmJobWarningCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 15),
    _XcmJobWarningCount_Type()
)
xcmJobWarningCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobWarningCount.setStatus("current")
_XcmJobProcessingTime_Type = Counter32
_XcmJobProcessingTime_Object = MibTableColumn
xcmJobProcessingTime = _XcmJobProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 16),
    _XcmJobProcessingTime_Type()
)
xcmJobProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobProcessingTime.setUnits("seconds")


class _XcmJobNumberOfDocuments_Type(Cardinal32):
    """Custom type xcmJobNumberOfDocuments based on Cardinal32"""
    defaultValue = 0


_XcmJobNumberOfDocuments_Object = MibTableColumn
xcmJobNumberOfDocuments = _XcmJobNumberOfDocuments_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 17),
    _XcmJobNumberOfDocuments_Type()
)
xcmJobNumberOfDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobNumberOfDocuments.setStatus("current")


class _XcmJobAuthorizationUserName_Type(CodeIndexedStringIndex):
    """Custom type xcmJobAuthorizationUserName based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmJobAuthorizationUserName_Object = MibTableColumn
xcmJobAuthorizationUserName = _XcmJobAuthorizationUserName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 10, 1, 1, 18),
    _XcmJobAuthorizationUserName_Type()
)
xcmJobAuthorizationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobAuthorizationUserName.setStatus("current")
_XcmDocGenBasic_ObjectIdentity = ObjectIdentity
xcmDocGenBasic = _XcmDocGenBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12)
)
_XcmDocGenBasicTable_Object = MibTable
xcmDocGenBasicTable = _XcmDocGenBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1)
)
if mibBuilder.loadTexts:
    xcmDocGenBasicTable.setStatus("current")
_XcmDocGenBasicEntry_Object = MibTableRow
xcmDocGenBasicEntry = _XcmDocGenBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1)
)
xcmDocGenBasicEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmDocSequenceNumber"),
)
if mibBuilder.loadTexts:
    xcmDocGenBasicEntry.setStatus("current")
_XcmDocSequenceNumber_Type = Ordinal32
_XcmDocSequenceNumber_Object = MibTableColumn
xcmDocSequenceNumber = _XcmDocSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 1),
    _XcmDocSequenceNumber_Type()
)
xcmDocSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocSequenceNumber.setStatus("current")
_XcmDocName_Type = CodeIndexedStringIndex
_XcmDocName_Object = MibTableColumn
xcmDocName = _XcmDocName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 2),
    _XcmDocName_Type()
)
xcmDocName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocName.setStatus("current")
_XcmDocFileName_Type = CodeIndexedStringIndex
_XcmDocFileName_Object = MibTableColumn
xcmDocFileName = _XcmDocFileName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 3),
    _XcmDocFileName_Type()
)
xcmDocFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFileName.setStatus("current")
_XcmDocFileNameType_Type = XcmJMDocFileNameType
_XcmDocFileNameType_Object = MibTableColumn
xcmDocFileNameType = _XcmDocFileNameType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 4),
    _XcmDocFileNameType_Type()
)
xcmDocFileNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFileNameType.setStatus("current")
_XcmDocType_Type = XcmJMDocType
_XcmDocType_Object = MibTableColumn
xcmDocType = _XcmDocType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 5),
    _XcmDocType_Type()
)
xcmDocType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocType.setStatus("current")
_XcmDocFormat_Type = XcmPrtInterpreterLangFamily
_XcmDocFormat_Object = MibTableColumn
xcmDocFormat = _XcmDocFormat_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 6),
    _XcmDocFormat_Type()
)
xcmDocFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFormat.setStatus("current")
_XcmDocFormatVariants_Type = CodeIndexedStringIndex
_XcmDocFormatVariants_Object = MibTableColumn
xcmDocFormatVariants = _XcmDocFormatVariants_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 7),
    _XcmDocFormatVariants_Type()
)
xcmDocFormatVariants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFormatVariants.setStatus("current")
_XcmDocFormatVersion_Type = CodeIndexedStringIndex
_XcmDocFormatVersion_Object = MibTableColumn
xcmDocFormatVersion = _XcmDocFormatVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 8),
    _XcmDocFormatVersion_Type()
)
xcmDocFormatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocFormatVersion.setStatus("current")
_XcmDocOctetCount_Type = Cardinal32
_XcmDocOctetCount_Object = MibTableColumn
xcmDocOctetCount = _XcmDocOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 9),
    _XcmDocOctetCount_Type()
)
xcmDocOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocOctetCount.setStatus("current")
_XcmDocState_Type = XcmJMDocState
_XcmDocState_Object = MibTableColumn
xcmDocState = _XcmDocState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 12, 1, 1, 10),
    _XcmDocState_Type()
)
xcmDocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocState.setStatus("current")
_XcmDocPrintExt_ObjectIdentity = ObjectIdentity
xcmDocPrintExt = _XcmDocPrintExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13)
)
_XcmDocPrintExtTable_Object = MibTable
xcmDocPrintExtTable = _XcmDocPrintExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1)
)
if mibBuilder.loadTexts:
    xcmDocPrintExtTable.setStatus("current")
_XcmDocPrintExtEntry_Object = MibTableRow
xcmDocPrintExtEntry = _XcmDocPrintExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1)
)
xcmDocPrintExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmDocSequenceNumber"),
)
if mibBuilder.loadTexts:
    xcmDocPrintExtEntry.setStatus("current")


class _XcmDocPrintDefaultMediumName_Type(InternationalDisplayString):
    """Custom type xcmDocPrintDefaultMediumName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmDocPrintDefaultMediumName_Type.__name__ = "InternationalDisplayString"
_XcmDocPrintDefaultMediumName_Object = MibTableColumn
xcmDocPrintDefaultMediumName = _XcmDocPrintDefaultMediumName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 1),
    _XcmDocPrintDefaultMediumName_Type()
)
xcmDocPrintDefaultMediumName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintDefaultMediumName.setStatus("current")
_XcmDocPrintDefaultInputIndex_Type = Cardinal16
_XcmDocPrintDefaultInputIndex_Object = MibTableColumn
xcmDocPrintDefaultInputIndex = _XcmDocPrintDefaultInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 2),
    _XcmDocPrintDefaultInputIndex_Type()
)
xcmDocPrintDefaultInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintDefaultInputIndex.setStatus("current")


class _XcmDocPrintFinishing_Type(InternationalDisplayString):
    """Custom type xcmDocPrintFinishing based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmDocPrintFinishing_Type.__name__ = "InternationalDisplayString"
_XcmDocPrintFinishing_Object = MibTableColumn
xcmDocPrintFinishing = _XcmDocPrintFinishing_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 3),
    _XcmDocPrintFinishing_Type()
)
xcmDocPrintFinishing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintFinishing.setStatus("current")
_XcmDocPrintOutputMethod_Type = XcmJMDocOutputMethod
_XcmDocPrintOutputMethod_Object = MibTableColumn
xcmDocPrintOutputMethod = _XcmDocPrintOutputMethod_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 4),
    _XcmDocPrintOutputMethod_Type()
)
xcmDocPrintOutputMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintOutputMethod.setStatus("current")


class _XcmDocPrintNumberUp_Type(InternationalDisplayString):
    """Custom type xcmDocPrintNumberUp based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmDocPrintNumberUp_Type.__name__ = "InternationalDisplayString"
_XcmDocPrintNumberUp_Object = MibTableColumn
xcmDocPrintNumberUp = _XcmDocPrintNumberUp_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 5),
    _XcmDocPrintNumberUp_Type()
)
xcmDocPrintNumberUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintNumberUp.setStatus("current")


class _XcmDocPrintSides_Type(Integer32):
    """Custom type xcmDocPrintSides based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XcmDocPrintSides_Type.__name__ = "Integer32"
_XcmDocPrintSides_Object = MibTableColumn
xcmDocPrintSides = _XcmDocPrintSides_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 6),
    _XcmDocPrintSides_Type()
)
xcmDocPrintSides.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintSides.setStatus("current")
_XcmDocPrintCopyCount_Type = Cardinal32
_XcmDocPrintCopyCount_Object = MibTableColumn
xcmDocPrintCopyCount = _XcmDocPrintCopyCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 7),
    _XcmDocPrintCopyCount_Type()
)
xcmDocPrintCopyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintCopyCount.setStatus("current")
_XcmDocPrintCopiesCompleted_Type = Counter32
_XcmDocPrintCopiesCompleted_Object = MibTableColumn
xcmDocPrintCopiesCompleted = _XcmDocPrintCopiesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 13, 1, 1, 8),
    _XcmDocPrintCopiesCompleted_Type()
)
xcmDocPrintCopiesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmDocPrintCopiesCompleted.setStatus("current")
_XcmJobGenSpoolingBasic_ObjectIdentity = ObjectIdentity
xcmJobGenSpoolingBasic = _XcmJobGenSpoolingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14)
)
_XcmJobGenSpoolingBasicTable_Object = MibTable
xcmJobGenSpoolingBasicTable = _XcmJobGenSpoolingBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenSpoolingBasicTable.setStatus("current")
_XcmJobGenSpoolingBasicEntry_Object = MibTableRow
xcmJobGenSpoolingBasicEntry = _XcmJobGenSpoolingBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenSpoolingBasicEntry.setStatus("current")


class _XcmJobNumberOfJobResultSets_Type(Ordinal32):
    """Custom type xcmJobNumberOfJobResultSets based on Ordinal32"""
    defaultValue = 1


_XcmJobNumberOfJobResultSets_Object = MibTableColumn
xcmJobNumberOfJobResultSets = _XcmJobNumberOfJobResultSets_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 1),
    _XcmJobNumberOfJobResultSets_Type()
)
xcmJobNumberOfJobResultSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobNumberOfJobResultSets.setStatus("current")


class _XcmJobPriority_Type(Integer32):
    """Custom type xcmJobPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmJobPriority_Type.__name__ = "Integer32"
_XcmJobPriority_Object = MibTableColumn
xcmJobPriority = _XcmJobPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 2),
    _XcmJobPriority_Type()
)
xcmJobPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobPriority.setStatus("current")


class _XcmJobTotalOctetsHigh_Type(Cardinal64High):
    """Custom type xcmJobTotalOctetsHigh based on Cardinal64High"""
    defaultValue = 0


_XcmJobTotalOctetsHigh_Object = MibTableColumn
xcmJobTotalOctetsHigh = _XcmJobTotalOctetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 3),
    _XcmJobTotalOctetsHigh_Type()
)
xcmJobTotalOctetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobTotalOctetsHigh.setStatus("current")


class _XcmJobTotalOctetsLow_Type(Cardinal64Low):
    """Custom type xcmJobTotalOctetsLow based on Cardinal64Low"""
    defaultValue = 0


_XcmJobTotalOctetsLow_Object = MibTableColumn
xcmJobTotalOctetsLow = _XcmJobTotalOctetsLow_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 4),
    _XcmJobTotalOctetsLow_Type()
)
xcmJobTotalOctetsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobTotalOctetsLow.setStatus("current")


class _XcmJobInterveningJobs_Type(Integer32):
    """Custom type xcmJobInterveningJobs based on Integer32"""
    defaultValue = -2


_XcmJobInterveningJobs_Object = MibTableColumn
xcmJobInterveningJobs = _XcmJobInterveningJobs_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 14, 1, 1, 5),
    _XcmJobInterveningJobs_Type()
)
xcmJobInterveningJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobInterveningJobs.setStatus("current")
_XcmJobGenSpoolingExt_ObjectIdentity = ObjectIdentity
xcmJobGenSpoolingExt = _XcmJobGenSpoolingExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15)
)
_XcmJobGenSpoolingExtTable_Object = MibTable
xcmJobGenSpoolingExtTable = _XcmJobGenSpoolingExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenSpoolingExtTable.setStatus("current")
_XcmJobGenSpoolingExtEntry_Object = MibTableRow
xcmJobGenSpoolingExtEntry = _XcmJobGenSpoolingExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenSpoolingExtEntry.setStatus("current")


class _XcmJobProcessAfter_Type(DateAndTime):
    """Custom type xcmJobProcessAfter based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobProcessAfter_Object = MibTableColumn
xcmJobProcessAfter = _XcmJobProcessAfter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 1),
    _XcmJobProcessAfter_Type()
)
xcmJobProcessAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobProcessAfter.setStatus("current")


class _XcmJobDeadlineTime_Type(DateAndTime):
    """Custom type xcmJobDeadlineTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobDeadlineTime_Object = MibTableColumn
xcmJobDeadlineTime = _XcmJobDeadlineTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 3),
    _XcmJobDeadlineTime_Type()
)
xcmJobDeadlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobDeadlineTime.setStatus("current")


class _XcmJobDiscardTime_Type(DateAndTime):
    """Custom type xcmJobDiscardTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobDiscardTime_Object = MibTableColumn
xcmJobDiscardTime = _XcmJobDiscardTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 4),
    _XcmJobDiscardTime_Type()
)
xcmJobDiscardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobDiscardTime.setStatus("current")
_XcmJobRetentionPeriod_Type = Cardinal32
_XcmJobRetentionPeriod_Object = MibTableColumn
xcmJobRetentionPeriod = _XcmJobRetentionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 5),
    _XcmJobRetentionPeriod_Type()
)
xcmJobRetentionPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobRetentionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobRetentionPeriod.setUnits("seconds")
_XcmJobMessageToOperator_Type = CodeIndexedStringIndex
_XcmJobMessageToOperator_Object = MibTableColumn
xcmJobMessageToOperator = _XcmJobMessageToOperator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 6),
    _XcmJobMessageToOperator_Type()
)
xcmJobMessageToOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMessageToOperator.setStatus("current")
_XcmJobMessageFromOperator_Type = CodeIndexedStringIndex
_XcmJobMessageFromOperator_Object = MibTableColumn
xcmJobMessageFromOperator = _XcmJobMessageFromOperator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 7),
    _XcmJobMessageFromOperator_Type()
)
xcmJobMessageFromOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMessageFromOperator.setStatus("current")
_XcmJobMessageFromAdministrator_Type = CodeIndexedStringIndex
_XcmJobMessageFromAdministrator_Object = MibTableColumn
xcmJobMessageFromAdministrator = _XcmJobMessageFromAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 8),
    _XcmJobMessageFromAdministrator_Type()
)
xcmJobMessageFromAdministrator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMessageFromAdministrator.setStatus("current")
_XcmJobPageCount_Type = Cardinal32
_XcmJobPageCount_Object = MibTableColumn
xcmJobPageCount = _XcmJobPageCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 15, 1, 1, 9),
    _XcmJobPageCount_Type()
)
xcmJobPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobPageCount.setStatus("current")
_XcmJobGenAccountingBasic_ObjectIdentity = ObjectIdentity
xcmJobGenAccountingBasic = _XcmJobGenAccountingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16)
)
_XcmJobGenAccountingBasicTable_Object = MibTable
xcmJobGenAccountingBasicTable = _XcmJobGenAccountingBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenAccountingBasicTable.setStatus("current")
_XcmJobGenAccountingBasicEntry_Object = MibTableRow
xcmJobGenAccountingBasicEntry = _XcmJobGenAccountingBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1)
)
if mibBuilder.loadTexts:
    xcmJobGenAccountingBasicEntry.setStatus("current")
_XcmJobAccountingBasicRowStatus_Type = RowStatus
_XcmJobAccountingBasicRowStatus_Object = MibTableColumn
xcmJobAccountingBasicRowStatus = _XcmJobAccountingBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 1),
    _XcmJobAccountingBasicRowStatus_Type()
)
xcmJobAccountingBasicRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmJobAccountingBasicRowStatus.setStatus("current")


class _XcmJobAccountingUserName_Type(CodeIndexedStringIndex):
    """Custom type xcmJobAccountingUserName based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmJobAccountingUserName_Object = MibTableColumn
xcmJobAccountingUserName = _XcmJobAccountingUserName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 2),
    _XcmJobAccountingUserName_Type()
)
xcmJobAccountingUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobAccountingUserName.setStatus("current")


class _XcmJobAccountingInformation_Type(OctetString):
    """Custom type xcmJobAccountingInformation based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmJobAccountingInformation_Type.__name__ = "OctetString"
_XcmJobAccountingInformation_Object = MibTableColumn
xcmJobAccountingInformation = _XcmJobAccountingInformation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 3),
    _XcmJobAccountingInformation_Type()
)
xcmJobAccountingInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobAccountingInformation.setStatus("current")


class _XcmJobStartedProcessingTime_Type(DateAndTime):
    """Custom type xcmJobStartedProcessingTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobStartedProcessingTime_Object = MibTableColumn
xcmJobStartedProcessingTime = _XcmJobStartedProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 4),
    _XcmJobStartedProcessingTime_Type()
)
xcmJobStartedProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobStartedProcessingTime.setStatus("current")
_XcmJobImpressionsCompleted_Type = Counter32
_XcmJobImpressionsCompleted_Object = MibTableColumn
xcmJobImpressionsCompleted = _XcmJobImpressionsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 5),
    _XcmJobImpressionsCompleted_Type()
)
xcmJobImpressionsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpressionsCompleted.setStatus("current")
_XcmJobMediaSheetsCompleted_Type = Counter32
_XcmJobMediaSheetsCompleted_Object = MibTableColumn
xcmJobMediaSheetsCompleted = _XcmJobMediaSheetsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 6),
    _XcmJobMediaSheetsCompleted_Type()
)
xcmJobMediaSheetsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobMediaSheetsCompleted.setStatus("current")


class _XcmJobCompletionTime_Type(DateAndTime):
    """Custom type xcmJobCompletionTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmJobCompletionTime_Object = MibTableColumn
xcmJobCompletionTime = _XcmJobCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 7),
    _XcmJobCompletionTime_Type()
)
xcmJobCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobCompletionTime.setStatus("current")


class _XcmJobWorkUnitType_Type(XcmHrDevTrafficUnit):
    """Custom type xcmJobWorkUnitType based on XcmHrDevTrafficUnit"""


_XcmJobWorkUnitType_Object = MibTableColumn
xcmJobWorkUnitType = _XcmJobWorkUnitType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 8),
    _XcmJobWorkUnitType_Type()
)
xcmJobWorkUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobWorkUnitType.setStatus("current")
_XcmJobUnitsOfWorkCompleted_Type = Counter32
_XcmJobUnitsOfWorkCompleted_Object = MibTableColumn
xcmJobUnitsOfWorkCompleted = _XcmJobUnitsOfWorkCompleted_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 16, 1, 1, 9),
    _XcmJobUnitsOfWorkCompleted_Type()
)
xcmJobUnitsOfWorkCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobUnitsOfWorkCompleted.setStatus("current")
_XcmMediaConsumed_ObjectIdentity = ObjectIdentity
xcmMediaConsumed = _XcmMediaConsumed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17)
)
_XcmMediaConsumedTable_Object = MibTable
xcmMediaConsumedTable = _XcmMediaConsumedTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1)
)
if mibBuilder.loadTexts:
    xcmMediaConsumedTable.setStatus("current")
_XcmMediaConsumedEntry_Object = MibTableRow
xcmMediaConsumedEntry = _XcmMediaConsumedEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1)
)
xcmMediaConsumedEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedIndex"),
)
if mibBuilder.loadTexts:
    xcmMediaConsumedEntry.setStatus("current")
_XcmMediaConsumedIndex_Type = Ordinal16
_XcmMediaConsumedIndex_Object = MibTableColumn
xcmMediaConsumedIndex = _XcmMediaConsumedIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 1),
    _XcmMediaConsumedIndex_Type()
)
xcmMediaConsumedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmMediaConsumedIndex.setStatus("current")
_XcmMediaConsumedRowStatus_Type = RowStatus
_XcmMediaConsumedRowStatus_Object = MibTableColumn
xcmMediaConsumedRowStatus = _XcmMediaConsumedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 2),
    _XcmMediaConsumedRowStatus_Type()
)
xcmMediaConsumedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmMediaConsumedRowStatus.setStatus("current")


class _XcmMediaConsumedType_Type(XcmJMMediumType):
    """Custom type xcmMediaConsumedType based on XcmJMMediumType"""


_XcmMediaConsumedType_Object = MibTableColumn
xcmMediaConsumedType = _XcmMediaConsumedType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 3),
    _XcmMediaConsumedType_Type()
)
xcmMediaConsumedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmMediaConsumedType.setStatus("current")


class _XcmMediaConsumedName_Type(CodeIndexedStringIndex):
    """Custom type xcmMediaConsumedName based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmMediaConsumedName_Object = MibTableColumn
xcmMediaConsumedName = _XcmMediaConsumedName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 4),
    _XcmMediaConsumedName_Type()
)
xcmMediaConsumedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmMediaConsumedName.setStatus("current")
_XcmMediaConsumedSheetCount_Type = Counter32
_XcmMediaConsumedSheetCount_Object = MibTableColumn
xcmMediaConsumedSheetCount = _XcmMediaConsumedSheetCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 17, 1, 1, 5),
    _XcmMediaConsumedSheetCount_Type()
)
xcmMediaConsumedSheetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmMediaConsumedSheetCount.setStatus("current")
_XcmColorImpsConsumed_ObjectIdentity = ObjectIdentity
xcmColorImpsConsumed = _XcmColorImpsConsumed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18)
)
_XcmColorImpsConsumedTable_Object = MibTable
xcmColorImpsConsumedTable = _XcmColorImpsConsumedTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1)
)
if mibBuilder.loadTexts:
    xcmColorImpsConsumedTable.setStatus("current")
_XcmColorImpsConsumedEntry_Object = MibTableRow
xcmColorImpsConsumedEntry = _XcmColorImpsConsumedEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1)
)
xcmColorImpsConsumedEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmColorImpsConsumedIndex"),
)
if mibBuilder.loadTexts:
    xcmColorImpsConsumedEntry.setStatus("current")
_XcmColorImpsConsumedIndex_Type = Ordinal16
_XcmColorImpsConsumedIndex_Object = MibTableColumn
xcmColorImpsConsumedIndex = _XcmColorImpsConsumedIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1, 1),
    _XcmColorImpsConsumedIndex_Type()
)
xcmColorImpsConsumedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedIndex.setStatus("current")
_XcmColorImpsConsumedRowStatus_Type = RowStatus
_XcmColorImpsConsumedRowStatus_Object = MibTableColumn
xcmColorImpsConsumedRowStatus = _XcmColorImpsConsumedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1, 2),
    _XcmColorImpsConsumedRowStatus_Type()
)
xcmColorImpsConsumedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedRowStatus.setStatus("current")
_XcmColorImpsConsumedTypeIndex_Type = Ordinal16
_XcmColorImpsConsumedTypeIndex_Object = MibTableColumn
xcmColorImpsConsumedTypeIndex = _XcmColorImpsConsumedTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1, 3),
    _XcmColorImpsConsumedTypeIndex_Type()
)
xcmColorImpsConsumedTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedTypeIndex.setStatus("current")
_XcmColorImpsConsumedCount_Type = Counter32
_XcmColorImpsConsumedCount_Object = MibTableColumn
xcmColorImpsConsumedCount = _XcmColorImpsConsumedCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 18, 1, 1, 4),
    _XcmColorImpsConsumedCount_Type()
)
xcmColorImpsConsumedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmColorImpsConsumedCount.setStatus("current")
_XcmJobAlert_ObjectIdentity = ObjectIdentity
xcmJobAlert = _XcmJobAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 19)
)
_XcmJobV1AlertNew_ObjectIdentity = ObjectIdentity
xcmJobV1AlertNew = _XcmJobV1AlertNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 19, 4)
)
if mibBuilder.loadTexts:
    xcmJobV1AlertNew.setStatus("current")
_XcmJobV2AlertPrefixNew_ObjectIdentity = ObjectIdentity
xcmJobV2AlertPrefixNew = _XcmJobV2AlertPrefixNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 19, 4, 0)
)
_XcmDocAlert_ObjectIdentity = ObjectIdentity
xcmDocAlert = _XcmDocAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 20)
)
_XcmDocV1AlertNew_ObjectIdentity = ObjectIdentity
xcmDocV1AlertNew = _XcmDocV1AlertNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 20, 4)
)
if mibBuilder.loadTexts:
    xcmDocV1AlertNew.setStatus("current")
_XcmDocV2AlertPrefixNew_ObjectIdentity = ObjectIdentity
xcmDocV2AlertPrefixNew = _XcmDocV2AlertPrefixNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 20, 4, 0)
)
_XcmJobImpsByMediumSize_ObjectIdentity = ObjectIdentity
xcmJobImpsByMediumSize = _XcmJobImpsByMediumSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21)
)
_XcmJobImpsByMediumSizeTable_Object = MibTable
xcmJobImpsByMediumSizeTable = _XcmJobImpsByMediumSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1)
)
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeTable.setStatus("current")
_XcmJobImpsByMediumSizeEntry_Object = MibTableRow
xcmJobImpsByMediumSizeEntry = _XcmJobImpsByMediumSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1)
)
xcmJobImpsByMediumSizeEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
    (0, "XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeIndex"),
)
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeEntry.setStatus("current")
_XcmJobImpsByMediumSizeIndex_Type = Ordinal16
_XcmJobImpsByMediumSizeIndex_Object = MibTableColumn
xcmJobImpsByMediumSizeIndex = _XcmJobImpsByMediumSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 1),
    _XcmJobImpsByMediumSizeIndex_Type()
)
xcmJobImpsByMediumSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeIndex.setStatus("current")
_XcmJobImpsByMediumSizeRowStatus_Type = RowStatus
_XcmJobImpsByMediumSizeRowStatus_Object = MibTableColumn
xcmJobImpsByMediumSizeRowStatus = _XcmJobImpsByMediumSizeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 2),
    _XcmJobImpsByMediumSizeRowStatus_Type()
)
xcmJobImpsByMediumSizeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeRowStatus.setStatus("current")


class _XcmJobImpsByMediumSizeMediumSize_Type(XcmPrtMediumSize):
    """Custom type xcmJobImpsByMediumSizeMediumSize based on XcmPrtMediumSize"""


_XcmJobImpsByMediumSizeMediumSize_Object = MibTableColumn
xcmJobImpsByMediumSizeMediumSize = _XcmJobImpsByMediumSizeMediumSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 3),
    _XcmJobImpsByMediumSizeMediumSize_Type()
)
xcmJobImpsByMediumSizeMediumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeMediumSize.setStatus("current")


class _XcmJobImpsByMediumSizeCountType_Type(XcmJMImpsCountType):
    """Custom type xcmJobImpsByMediumSizeCountType based on XcmJMImpsCountType"""


_XcmJobImpsByMediumSizeCountType_Object = MibTableColumn
xcmJobImpsByMediumSizeCountType = _XcmJobImpsByMediumSizeCountType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 4),
    _XcmJobImpsByMediumSizeCountType_Type()
)
xcmJobImpsByMediumSizeCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCountType.setStatus("current")
_XcmJobImpsByMediumSizeCount_Type = Counter32
_XcmJobImpsByMediumSizeCount_Object = MibTableColumn
xcmJobImpsByMediumSizeCount = _XcmJobImpsByMediumSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 5),
    _XcmJobImpsByMediumSizeCount_Type()
)
xcmJobImpsByMediumSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCount.setStatus("current")


class _XcmJobImpsByMediumSizeCountQuality_Type(XcmPrtPrintQuality):
    """Custom type xcmJobImpsByMediumSizeCountQuality based on XcmPrtPrintQuality"""


_XcmJobImpsByMediumSizeCountQuality_Object = MibTableColumn
xcmJobImpsByMediumSizeCountQuality = _XcmJobImpsByMediumSizeCountQuality_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 21, 1, 1, 6),
    _XcmJobImpsByMediumSizeCountQuality_Type()
)
xcmJobImpsByMediumSizeCountQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJobImpsByMediumSizeCountQuality.setStatus("current")
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-MIB",
     "xcmJobGenExtEntry")
)
xcmJobGenExtEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-MIB",
     "xcmJobGenSpoolingBasicEntry")
)
xcmJobGenSpoolingBasicEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-MIB",
     "xcmJobGenSpoolingExtEntry")
)
xcmJobGenSpoolingExtEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-MIB",
     "xcmJobGenAccountingBasicEntry")
)
xcmJobGenAccountingBasicEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())

# Managed Objects groups

xcmJMBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 1)
)
xcmJMBaseGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseVersionID"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseVersionDate"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseGroupSupport"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseCreateSupport"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMonBaseUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmJMBaseGroup.setStatus("current")

xcmJMJobGenBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 6)
)
xcmJMJobGenBasicGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierUpstream"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobClientId"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobServiceType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobOwner"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobSourceChannelType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobSubmittedLocaleIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobCurrentState"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobStateReasons"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobXStateReasons"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobX2StateReasons"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenBasicGroup.setStatus("current")

xcmJMDevicesAssignedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 7)
)
xcmJMDevicesAssignedGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmDeviceStateOfDevicesAssigned"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierDownstream"))
)
if mibBuilder.loadTexts:
    xcmJMDevicesAssignedGroup.setStatus("current")

xcmJMClientIdMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 8)
)
xcmJMClientIdMapGroup.setObjects(
    ("XEROX-JOB-MONITORING-MIB", "xcmClientIdMapHrDeviceIndex")
)
if mibBuilder.loadTexts:
    xcmJMClientIdMapGroup.setStatus("current")

xcmJMJobGenExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 10)
)
xcmJMJobGenExtGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobOriginator"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobSubmittingApplication"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobComment"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobCopies"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobCopiesCompleted"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobOutputBinIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobServiceNameRequested"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobPreviousState"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobEstimatedCompletionTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobSubmissionTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobPagesCompleted"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobOctetsCompletedHigh"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobOctetsCompletedLow"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobErrorCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobWarningCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobProcessingTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobNumberOfDocuments"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobAuthorizationUserName"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenExtGroup.setStatus("current")

xcmJMDocGenBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 12)
)
xcmJMDocGenBasicGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmDocSequenceNumber"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFileName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFileNameType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFormat"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFormatVariants"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocFormatVersion"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocOctetCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocState"))
)
if mibBuilder.loadTexts:
    xcmJMDocGenBasicGroup.setStatus("current")

xcmJMDocPrintExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 13)
)
xcmJMDocPrintExtGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmDocPrintDefaultMediumName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintDefaultInputIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintFinishing"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintOutputMethod"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintNumberUp"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintSides"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintCopyCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocPrintCopiesCompleted"))
)
if mibBuilder.loadTexts:
    xcmJMDocPrintExtGroup.setStatus("current")

xcmJMJobGenSpoolingBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 14)
)
xcmJMJobGenSpoolingBasicGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobNumberOfJobResultSets"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobPriority"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobTotalOctetsHigh"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobTotalOctetsLow"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobInterveningJobs"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenSpoolingBasicGroup.setStatus("current")

xcmJMJobGenSpoolingExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 15)
)
xcmJMJobGenSpoolingExtGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobProcessAfter"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobDeadlineTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobDiscardTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobRetentionPeriod"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMessageToOperator"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMessageFromOperator"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMessageFromAdministrator"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobPageCount"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenSpoolingExtGroup.setStatus("current")

xcmJMJobGenAccountingBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 16)
)
xcmJMJobGenAccountingBasicGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobAccountingBasicRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobAccountingUserName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobAccountingInformation"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobStartedProcessingTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpressionsCompleted"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobMediaSheetsCompleted"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobCompletionTime"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobWorkUnitType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobUnitsOfWorkCompleted"))
)
if mibBuilder.loadTexts:
    xcmJMJobGenAccountingBasicGroup.setStatus("current")

xcmJMMediaConsumedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 17)
)
xcmJMMediaConsumedGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedName"),
        ("XEROX-JOB-MONITORING-MIB", "xcmMediaConsumedSheetCount"))
)
if mibBuilder.loadTexts:
    xcmJMMediaConsumedGroup.setStatus("current")

xcmJMColorImpsConsumedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 18)
)
xcmJMColorImpsConsumedGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmColorImpsConsumedRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmColorImpsConsumedTypeIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmColorImpsConsumedCount"))
)
if mibBuilder.loadTexts:
    xcmJMColorImpsConsumedGroup.setStatus("current")

xcmJMJobImpsByMediumSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 3, 21)
)
xcmJMJobImpsByMediumSizeGroup.setObjects(
      *(("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeRowStatus"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeMediumSize"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeCountType"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeCount"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobImpsByMediumSizeCountQuality"))
)
if mibBuilder.loadTexts:
    xcmJMJobImpsByMediumSizeGroup.setStatus("current")


# Notification objects

xcmJobV2AlertNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 19, 4, 0, 1)
)
xcmJobV2AlertNew.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"))
)
if mibBuilder.loadTexts:
    xcmJobV2AlertNew.setStatus(
        "current"
    )

xcmDocV2AlertNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 20, 4, 0, 1)
)
xcmDocV2AlertNew.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
        ("XEROX-JOB-MONITORING-MIB", "xcmDocSequenceNumber"))
)
if mibBuilder.loadTexts:
    xcmDocV2AlertNew.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

xcmJobMonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 59, 2, 1)
)
if mibBuilder.loadTexts:
    xcmJobMonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-JOB-MONITORING-MIB",
    **{"xcmJobZeroDummy": xcmJobZeroDummy,
       "xcmJobMonMIB": xcmJobMonMIB,
       "xcmJobMonBase": xcmJobMonBase,
       "xcmJobMonBaseTable": xcmJobMonBaseTable,
       "xcmJobMonBaseEntry": xcmJobMonBaseEntry,
       "xcmJobMonBaseIndex": xcmJobMonBaseIndex,
       "xcmJobMonBaseRowStatus": xcmJobMonBaseRowStatus,
       "xcmJobMonBaseVersionID": xcmJobMonBaseVersionID,
       "xcmJobMonBaseVersionDate": xcmJobMonBaseVersionDate,
       "xcmJobMonBaseGroupSupport": xcmJobMonBaseGroupSupport,
       "xcmJobMonBaseCreateSupport": xcmJobMonBaseCreateSupport,
       "xcmJobMonBaseUpdateSupport": xcmJobMonBaseUpdateSupport,
       "xcmJobMonMIBConformance": xcmJobMonMIBConformance,
       "xcmJobMonCompliance": xcmJobMonCompliance,
       "xcmJobMonMIBGroups": xcmJobMonMIBGroups,
       "xcmJMBaseGroup": xcmJMBaseGroup,
       "xcmJMJobGenBasicGroup": xcmJMJobGenBasicGroup,
       "xcmJMDevicesAssignedGroup": xcmJMDevicesAssignedGroup,
       "xcmJMClientIdMapGroup": xcmJMClientIdMapGroup,
       "xcmJMJobGenExtGroup": xcmJMJobGenExtGroup,
       "xcmJMDocGenBasicGroup": xcmJMDocGenBasicGroup,
       "xcmJMDocPrintExtGroup": xcmJMDocPrintExtGroup,
       "xcmJMJobGenSpoolingBasicGroup": xcmJMJobGenSpoolingBasicGroup,
       "xcmJMJobGenSpoolingExtGroup": xcmJMJobGenSpoolingExtGroup,
       "xcmJMJobGenAccountingBasicGroup": xcmJMJobGenAccountingBasicGroup,
       "xcmJMMediaConsumedGroup": xcmJMMediaConsumedGroup,
       "xcmJMColorImpsConsumedGroup": xcmJMColorImpsConsumedGroup,
       "xcmJMJobImpsByMediumSizeGroup": xcmJMJobImpsByMediumSizeGroup,
       "xcmJobGenBasic": xcmJobGenBasic,
       "xcmJobGenBasicTable": xcmJobGenBasicTable,
       "xcmJobGenBasicEntry": xcmJobGenBasicEntry,
       "xcmJobIdentifierOnSystem": xcmJobIdentifierOnSystem,
       "xcmJobIdentifierUpstream": xcmJobIdentifierUpstream,
       "xcmJobClientId": xcmJobClientId,
       "xcmJobServiceType": xcmJobServiceType,
       "xcmJobName": xcmJobName,
       "xcmJobOwner": xcmJobOwner,
       "xcmJobSourceChannelType": xcmJobSourceChannelType,
       "xcmJobSubmittedLocaleIndex": xcmJobSubmittedLocaleIndex,
       "xcmJobCurrentState": xcmJobCurrentState,
       "xcmJobStateReasons": xcmJobStateReasons,
       "xcmJobXStateReasons": xcmJobXStateReasons,
       "xcmJobX2StateReasons": xcmJobX2StateReasons,
       "xcmDevicesAssigned": xcmDevicesAssigned,
       "xcmDevicesAssignedTable": xcmDevicesAssignedTable,
       "xcmDevicesAssignedEntry": xcmDevicesAssignedEntry,
       "xcmDevicesAssignedHrDeviceIndex": xcmDevicesAssignedHrDeviceIndex,
       "xcmDeviceStateOfDevicesAssigned": xcmDeviceStateOfDevicesAssigned,
       "xcmJobIdentifierDownstream": xcmJobIdentifierDownstream,
       "xcmClientIdMap": xcmClientIdMap,
       "xcmClientIdMapTable": xcmClientIdMapTable,
       "xcmClientIdMapEntry": xcmClientIdMapEntry,
       "xcmClientIdMapHrDeviceIndex": xcmClientIdMapHrDeviceIndex,
       "xcmJobGenExt": xcmJobGenExt,
       "xcmJobGenExtTable": xcmJobGenExtTable,
       "xcmJobGenExtEntry": xcmJobGenExtEntry,
       "xcmJobOriginator": xcmJobOriginator,
       "xcmJobSubmittingApplication": xcmJobSubmittingApplication,
       "xcmJobComment": xcmJobComment,
       "xcmJobCopies": xcmJobCopies,
       "xcmJobCopiesCompleted": xcmJobCopiesCompleted,
       "xcmJobOutputBinIndex": xcmJobOutputBinIndex,
       "xcmJobServiceNameRequested": xcmJobServiceNameRequested,
       "xcmJobPreviousState": xcmJobPreviousState,
       "xcmJobEstimatedCompletionTime": xcmJobEstimatedCompletionTime,
       "xcmJobSubmissionTime": xcmJobSubmissionTime,
       "xcmJobPagesCompleted": xcmJobPagesCompleted,
       "xcmJobOctetsCompletedHigh": xcmJobOctetsCompletedHigh,
       "xcmJobOctetsCompletedLow": xcmJobOctetsCompletedLow,
       "xcmJobErrorCount": xcmJobErrorCount,
       "xcmJobWarningCount": xcmJobWarningCount,
       "xcmJobProcessingTime": xcmJobProcessingTime,
       "xcmJobNumberOfDocuments": xcmJobNumberOfDocuments,
       "xcmJobAuthorizationUserName": xcmJobAuthorizationUserName,
       "xcmDocGenBasic": xcmDocGenBasic,
       "xcmDocGenBasicTable": xcmDocGenBasicTable,
       "xcmDocGenBasicEntry": xcmDocGenBasicEntry,
       "xcmDocSequenceNumber": xcmDocSequenceNumber,
       "xcmDocName": xcmDocName,
       "xcmDocFileName": xcmDocFileName,
       "xcmDocFileNameType": xcmDocFileNameType,
       "xcmDocType": xcmDocType,
       "xcmDocFormat": xcmDocFormat,
       "xcmDocFormatVariants": xcmDocFormatVariants,
       "xcmDocFormatVersion": xcmDocFormatVersion,
       "xcmDocOctetCount": xcmDocOctetCount,
       "xcmDocState": xcmDocState,
       "xcmDocPrintExt": xcmDocPrintExt,
       "xcmDocPrintExtTable": xcmDocPrintExtTable,
       "xcmDocPrintExtEntry": xcmDocPrintExtEntry,
       "xcmDocPrintDefaultMediumName": xcmDocPrintDefaultMediumName,
       "xcmDocPrintDefaultInputIndex": xcmDocPrintDefaultInputIndex,
       "xcmDocPrintFinishing": xcmDocPrintFinishing,
       "xcmDocPrintOutputMethod": xcmDocPrintOutputMethod,
       "xcmDocPrintNumberUp": xcmDocPrintNumberUp,
       "xcmDocPrintSides": xcmDocPrintSides,
       "xcmDocPrintCopyCount": xcmDocPrintCopyCount,
       "xcmDocPrintCopiesCompleted": xcmDocPrintCopiesCompleted,
       "xcmJobGenSpoolingBasic": xcmJobGenSpoolingBasic,
       "xcmJobGenSpoolingBasicTable": xcmJobGenSpoolingBasicTable,
       "xcmJobGenSpoolingBasicEntry": xcmJobGenSpoolingBasicEntry,
       "xcmJobNumberOfJobResultSets": xcmJobNumberOfJobResultSets,
       "xcmJobPriority": xcmJobPriority,
       "xcmJobTotalOctetsHigh": xcmJobTotalOctetsHigh,
       "xcmJobTotalOctetsLow": xcmJobTotalOctetsLow,
       "xcmJobInterveningJobs": xcmJobInterveningJobs,
       "xcmJobGenSpoolingExt": xcmJobGenSpoolingExt,
       "xcmJobGenSpoolingExtTable": xcmJobGenSpoolingExtTable,
       "xcmJobGenSpoolingExtEntry": xcmJobGenSpoolingExtEntry,
       "xcmJobProcessAfter": xcmJobProcessAfter,
       "xcmJobDeadlineTime": xcmJobDeadlineTime,
       "xcmJobDiscardTime": xcmJobDiscardTime,
       "xcmJobRetentionPeriod": xcmJobRetentionPeriod,
       "xcmJobMessageToOperator": xcmJobMessageToOperator,
       "xcmJobMessageFromOperator": xcmJobMessageFromOperator,
       "xcmJobMessageFromAdministrator": xcmJobMessageFromAdministrator,
       "xcmJobPageCount": xcmJobPageCount,
       "xcmJobGenAccountingBasic": xcmJobGenAccountingBasic,
       "xcmJobGenAccountingBasicTable": xcmJobGenAccountingBasicTable,
       "xcmJobGenAccountingBasicEntry": xcmJobGenAccountingBasicEntry,
       "xcmJobAccountingBasicRowStatus": xcmJobAccountingBasicRowStatus,
       "xcmJobAccountingUserName": xcmJobAccountingUserName,
       "xcmJobAccountingInformation": xcmJobAccountingInformation,
       "xcmJobStartedProcessingTime": xcmJobStartedProcessingTime,
       "xcmJobImpressionsCompleted": xcmJobImpressionsCompleted,
       "xcmJobMediaSheetsCompleted": xcmJobMediaSheetsCompleted,
       "xcmJobCompletionTime": xcmJobCompletionTime,
       "xcmJobWorkUnitType": xcmJobWorkUnitType,
       "xcmJobUnitsOfWorkCompleted": xcmJobUnitsOfWorkCompleted,
       "xcmMediaConsumed": xcmMediaConsumed,
       "xcmMediaConsumedTable": xcmMediaConsumedTable,
       "xcmMediaConsumedEntry": xcmMediaConsumedEntry,
       "xcmMediaConsumedIndex": xcmMediaConsumedIndex,
       "xcmMediaConsumedRowStatus": xcmMediaConsumedRowStatus,
       "xcmMediaConsumedType": xcmMediaConsumedType,
       "xcmMediaConsumedName": xcmMediaConsumedName,
       "xcmMediaConsumedSheetCount": xcmMediaConsumedSheetCount,
       "xcmColorImpsConsumed": xcmColorImpsConsumed,
       "xcmColorImpsConsumedTable": xcmColorImpsConsumedTable,
       "xcmColorImpsConsumedEntry": xcmColorImpsConsumedEntry,
       "xcmColorImpsConsumedIndex": xcmColorImpsConsumedIndex,
       "xcmColorImpsConsumedRowStatus": xcmColorImpsConsumedRowStatus,
       "xcmColorImpsConsumedTypeIndex": xcmColorImpsConsumedTypeIndex,
       "xcmColorImpsConsumedCount": xcmColorImpsConsumedCount,
       "xcmJobAlert": xcmJobAlert,
       "xcmJobV1AlertNew": xcmJobV1AlertNew,
       "xcmJobV2AlertPrefixNew": xcmJobV2AlertPrefixNew,
       "xcmJobV2AlertNew": xcmJobV2AlertNew,
       "xcmDocAlert": xcmDocAlert,
       "xcmDocV1AlertNew": xcmDocV1AlertNew,
       "xcmDocV2AlertPrefixNew": xcmDocV2AlertPrefixNew,
       "xcmDocV2AlertNew": xcmDocV2AlertNew,
       "xcmJobImpsByMediumSize": xcmJobImpsByMediumSize,
       "xcmJobImpsByMediumSizeTable": xcmJobImpsByMediumSizeTable,
       "xcmJobImpsByMediumSizeEntry": xcmJobImpsByMediumSizeEntry,
       "xcmJobImpsByMediumSizeIndex": xcmJobImpsByMediumSizeIndex,
       "xcmJobImpsByMediumSizeRowStatus": xcmJobImpsByMediumSizeRowStatus,
       "xcmJobImpsByMediumSizeMediumSize": xcmJobImpsByMediumSizeMediumSize,
       "xcmJobImpsByMediumSizeCountType": xcmJobImpsByMediumSizeCountType,
       "xcmJobImpsByMediumSizeCount": xcmJobImpsByMediumSizeCount,
       "xcmJobImpsByMediumSizeCountQuality": xcmJobImpsByMediumSizeCountQuality}
)
