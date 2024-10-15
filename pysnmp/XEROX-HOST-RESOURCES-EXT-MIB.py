# SNMP MIB module (XEROX-HOST-RESOURCES-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-HOST-RESOURCES-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:22 2024
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

(ProductID,
 hrDeviceIndex,
 hrDeviceStatus,
 hrSWInstalledIndex,
 hrSWRunIndex,
 hrStorageIndex) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "ProductID",
    "hrDeviceIndex",
    "hrDeviceStatus",
    "hrSWInstalledIndex",
    "hrSWRunIndex",
    "hrStorageIndex")

(PresentOnOff,) = mibBuilder.importSymbols(
    "Printer-MIB",
    "PresentOnOff")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(Cardinal32,
 Ordinal32,
 XcmFixedLocaleDisplayString,
 XcmGenNotifySeverityFilter,
 XcmGenNotifyTrainingFilter,
 XcmGenSNMPv2ErrorStatus,
 zeroDotZero) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Cardinal32",
    "Ordinal32",
    "XcmFixedLocaleDisplayString",
    "XcmGenNotifySeverityFilter",
    "XcmGenNotifyTrainingFilter",
    "XcmGenSNMPv2ErrorStatus",
    "zeroDotZero")

(XcmHrConsoleDefaultService,
 XcmHrDetailTableEnumTC,
 XcmHrDevCalendarDayOfWeek,
 XcmHrDevCalendarTimeOfDay,
 XcmHrDevDetailType,
 XcmHrDevDetailUnitClass,
 XcmHrDevInfoConditions,
 XcmHrDevInfoRealization,
 XcmHrDevInfoStatus,
 XcmHrDevInfoXConditions,
 XcmHrDevInfoXStatus,
 XcmHrDevMgmtCommandData,
 XcmHrDevMgmtCommandRequest,
 XcmHrDevPowerTimeUnit,
 XcmHrDevTrafficUnit,
 XcmHrGroupSupport,
 XcmHrSWRunXStatus,
 XcmHrStorageDetailType,
 XcmHrStorageRealization,
 XcmHrSuppliesClassTC) = mibBuilder.importSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    "XcmHrConsoleDefaultService",
    "XcmHrDetailTableEnumTC",
    "XcmHrDevCalendarDayOfWeek",
    "XcmHrDevCalendarTimeOfDay",
    "XcmHrDevDetailType",
    "XcmHrDevDetailUnitClass",
    "XcmHrDevInfoConditions",
    "XcmHrDevInfoRealization",
    "XcmHrDevInfoStatus",
    "XcmHrDevInfoXConditions",
    "XcmHrDevInfoXStatus",
    "XcmHrDevMgmtCommandData",
    "XcmHrDevMgmtCommandRequest",
    "XcmHrDevPowerTimeUnit",
    "XcmHrDevTrafficUnit",
    "XcmHrGroupSupport",
    "XcmHrSWRunXStatus",
    "XcmHrStorageDetailType",
    "XcmHrStorageRealization",
    "XcmHrSuppliesClassTC")


# MODULE-IDENTITY

xcmHrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmHrZeroDummy_ObjectIdentity = ObjectIdentity
xcmHrZeroDummy = _XcmHrZeroDummy_ObjectIdentity(
    (0, 0, 53)
)
_XcmHrMIBConformance_ObjectIdentity = ObjectIdentity
xcmHrMIBConformance = _XcmHrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2)
)
_XcmHrMIBGroups_ObjectIdentity = ObjectIdentity
xcmHrMIBGroups = _XcmHrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2)
)
_XcmHrDevInfo_ObjectIdentity = ObjectIdentity
xcmHrDevInfo = _XcmHrDevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3)
)
_XcmHrDevInfoV1EventOID_ObjectIdentity = ObjectIdentity
xcmHrDevInfoV1EventOID = _XcmHrDevInfoV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 1)
)
if mibBuilder.loadTexts:
    xcmHrDevInfoV1EventOID.setStatus("current")
_XcmHrDevInfoV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmHrDevInfoV2EventPrefix = _XcmHrDevInfoV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 1, 0)
)
_XcmHrDevInfoTable_Object = MibTable
xcmHrDevInfoTable = _XcmHrDevInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevInfoTable.setStatus("current")
_XcmHrDevInfoEntry_Object = MibTableRow
xcmHrDevInfoEntry = _XcmHrDevInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1)
)
xcmHrDevInfoEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevInfoEntry.setStatus("current")
_XcmHrDevInfoRowStatus_Type = RowStatus
_XcmHrDevInfoRowStatus_Object = MibTableColumn
xcmHrDevInfoRowStatus = _XcmHrDevInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 1),
    _XcmHrDevInfoRowStatus_Type()
)
xcmHrDevInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoRowStatus.setStatus("current")


class _XcmHrDevInfoName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevInfoName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevInfoName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevInfoName_Object = MibTableColumn
xcmHrDevInfoName = _XcmHrDevInfoName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 2),
    _XcmHrDevInfoName_Type()
)
xcmHrDevInfoName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoName.setStatus("current")


class _XcmHrDevInfoSerialNumber_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevInfoSerialNumber based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevInfoSerialNumber_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevInfoSerialNumber_Object = MibTableColumn
xcmHrDevInfoSerialNumber = _XcmHrDevInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 3),
    _XcmHrDevInfoSerialNumber_Type()
)
xcmHrDevInfoSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoSerialNumber.setStatus("current")


class _XcmHrDevInfoRealization_Type(XcmHrDevInfoRealization):
    """Custom type xcmHrDevInfoRealization based on XcmHrDevInfoRealization"""


_XcmHrDevInfoRealization_Object = MibTableColumn
xcmHrDevInfoRealization = _XcmHrDevInfoRealization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 4),
    _XcmHrDevInfoRealization_Type()
)
xcmHrDevInfoRealization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoRealization.setStatus("current")
_XcmHrDevInfoXStatus_Type = XcmHrDevInfoXStatus
_XcmHrDevInfoXStatus_Object = MibTableColumn
xcmHrDevInfoXStatus = _XcmHrDevInfoXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 5),
    _XcmHrDevInfoXStatus_Type()
)
xcmHrDevInfoXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevInfoXStatus.setStatus("current")


class _XcmHrDevInfoConditions_Type(XcmHrDevInfoConditions):
    """Custom type xcmHrDevInfoConditions based on XcmHrDevInfoConditions"""
    defaultValue = 0


_XcmHrDevInfoConditions_Object = MibTableColumn
xcmHrDevInfoConditions = _XcmHrDevInfoConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 6),
    _XcmHrDevInfoConditions_Type()
)
xcmHrDevInfoConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevInfoConditions.setStatus("current")


class _XcmHrDevInfoXConditions_Type(XcmHrDevInfoXConditions):
    """Custom type xcmHrDevInfoXConditions based on XcmHrDevInfoXConditions"""
    defaultValue = 0


_XcmHrDevInfoXConditions_Object = MibTableColumn
xcmHrDevInfoXConditions = _XcmHrDevInfoXConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 7),
    _XcmHrDevInfoXConditions_Type()
)
xcmHrDevInfoXConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevInfoXConditions.setStatus("current")


class _XcmHrDevInfoInstallDate_Type(DateAndTime):
    """Custom type xcmHrDevInfoInstallDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrDevInfoInstallDate_Object = MibTableColumn
xcmHrDevInfoInstallDate = _XcmHrDevInfoInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 8),
    _XcmHrDevInfoInstallDate_Type()
)
xcmHrDevInfoInstallDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoInstallDate.setStatus("current")


class _XcmHrDevInfoResetDate_Type(DateAndTime):
    """Custom type xcmHrDevInfoResetDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrDevInfoResetDate_Object = MibTableColumn
xcmHrDevInfoResetDate = _XcmHrDevInfoResetDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 9),
    _XcmHrDevInfoResetDate_Type()
)
xcmHrDevInfoResetDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevInfoResetDate.setStatus("current")


class _XcmHrDevInfoNextDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrDevInfoNextDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrDevInfoNextDeviceIndex_Object = MibTableColumn
xcmHrDevInfoNextDeviceIndex = _XcmHrDevInfoNextDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 10),
    _XcmHrDevInfoNextDeviceIndex_Type()
)
xcmHrDevInfoNextDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoNextDeviceIndex.setStatus("current")


class _XcmHrDevInfoPreviousDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrDevInfoPreviousDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrDevInfoPreviousDeviceIndex_Object = MibTableColumn
xcmHrDevInfoPreviousDeviceIndex = _XcmHrDevInfoPreviousDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 11),
    _XcmHrDevInfoPreviousDeviceIndex_Type()
)
xcmHrDevInfoPreviousDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPreviousDeviceIndex.setStatus("current")


class _XcmHrDevInfoPhysicalDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrDevInfoPhysicalDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrDevInfoPhysicalDeviceIndex_Object = MibTableColumn
xcmHrDevInfoPhysicalDeviceIndex = _XcmHrDevInfoPhysicalDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 12),
    _XcmHrDevInfoPhysicalDeviceIndex_Type()
)
xcmHrDevInfoPhysicalDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPhysicalDeviceIndex.setStatus("current")


class _XcmHrDevInfoPriority_Type(Integer32):
    """Custom type xcmHrDevInfoPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmHrDevInfoPriority_Type.__name__ = "Integer32"
_XcmHrDevInfoPriority_Object = MibTableColumn
xcmHrDevInfoPriority = _XcmHrDevInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 13),
    _XcmHrDevInfoPriority_Type()
)
xcmHrDevInfoPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPriority.setStatus("current")


class _XcmHrDevInfoXeroxAssetTagNumber_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevInfoXeroxAssetTagNumber based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XcmHrDevInfoXeroxAssetTagNumber_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevInfoXeroxAssetTagNumber_Object = MibTableColumn
xcmHrDevInfoXeroxAssetTagNumber = _XcmHrDevInfoXeroxAssetTagNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 14),
    _XcmHrDevInfoXeroxAssetTagNumber_Type()
)
xcmHrDevInfoXeroxAssetTagNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoXeroxAssetTagNumber.setStatus("current")


class _XcmHrDevInfoCustomerAssetNumber_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevInfoCustomerAssetNumber based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XcmHrDevInfoCustomerAssetNumber_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevInfoCustomerAssetNumber_Object = MibTableColumn
xcmHrDevInfoCustomerAssetNumber = _XcmHrDevInfoCustomerAssetNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 15),
    _XcmHrDevInfoCustomerAssetNumber_Type()
)
xcmHrDevInfoCustomerAssetNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoCustomerAssetNumber.setStatus("current")


class _XcmHrDevInfoPagePackPIN_Type(OctetString):
    """Custom type xcmHrDevInfoPagePackPIN based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XcmHrDevInfoPagePackPIN_Type.__name__ = "OctetString"
_XcmHrDevInfoPagePackPIN_Object = MibTableColumn
xcmHrDevInfoPagePackPIN = _XcmHrDevInfoPagePackPIN_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 16),
    _XcmHrDevInfoPagePackPIN_Type()
)
xcmHrDevInfoPagePackPIN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackPIN.setStatus("current")


class _XcmHrDevInfoPagePackReset_Type(Integer32):
    """Custom type xcmHrDevInfoPagePackReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XcmHrDevInfoPagePackReset_Type.__name__ = "Integer32"
_XcmHrDevInfoPagePackReset_Object = MibTableColumn
xcmHrDevInfoPagePackReset = _XcmHrDevInfoPagePackReset_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 17),
    _XcmHrDevInfoPagePackReset_Type()
)
xcmHrDevInfoPagePackReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackReset.setStatus("current")


class _XcmHrDevInfoPagePackTimer_Type(Integer32):
    """Custom type xcmHrDevInfoPagePackTimer based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_XcmHrDevInfoPagePackTimer_Type.__name__ = "Integer32"
_XcmHrDevInfoPagePackTimer_Object = MibTableColumn
xcmHrDevInfoPagePackTimer = _XcmHrDevInfoPagePackTimer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 18),
    _XcmHrDevInfoPagePackTimer_Type()
)
xcmHrDevInfoPagePackTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackTimer.setStatus("current")
_XcmHrDevHelp_ObjectIdentity = ObjectIdentity
xcmHrDevHelp = _XcmHrDevHelp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4)
)
_XcmHrDevHelpTable_Object = MibTable
xcmHrDevHelpTable = _XcmHrDevHelpTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevHelpTable.setStatus("current")
_XcmHrDevHelpEntry_Object = MibTableRow
xcmHrDevHelpEntry = _XcmHrDevHelpEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1)
)
xcmHrDevHelpEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevHelpEntry.setStatus("current")
_XcmHrDevHelpRowStatus_Type = RowStatus
_XcmHrDevHelpRowStatus_Object = MibTableColumn
xcmHrDevHelpRowStatus = _XcmHrDevHelpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1, 1),
    _XcmHrDevHelpRowStatus_Type()
)
xcmHrDevHelpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevHelpRowStatus.setStatus("current")


class _XcmHrDevHelpOperatorMessage_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevHelpOperatorMessage based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevHelpOperatorMessage_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevHelpOperatorMessage_Object = MibTableColumn
xcmHrDevHelpOperatorMessage = _XcmHrDevHelpOperatorMessage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1, 2),
    _XcmHrDevHelpOperatorMessage_Type()
)
xcmHrDevHelpOperatorMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevHelpOperatorMessage.setStatus("current")


class _XcmHrDevHelpProblemMessage_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevHelpProblemMessage based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevHelpProblemMessage_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevHelpProblemMessage_Object = MibTableColumn
xcmHrDevHelpProblemMessage = _XcmHrDevHelpProblemMessage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1, 3),
    _XcmHrDevHelpProblemMessage_Type()
)
xcmHrDevHelpProblemMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevHelpProblemMessage.setStatus("current")


class _XcmHrDevHelpCommsAddressIndex_Type(Cardinal32):
    """Custom type xcmHrDevHelpCommsAddressIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrDevHelpCommsAddressIndex_Object = MibTableColumn
xcmHrDevHelpCommsAddressIndex = _XcmHrDevHelpCommsAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1, 4),
    _XcmHrDevHelpCommsAddressIndex_Type()
)
xcmHrDevHelpCommsAddressIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevHelpCommsAddressIndex.setStatus("current")
_XcmHrDevMgmt_ObjectIdentity = ObjectIdentity
xcmHrDevMgmt = _XcmHrDevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5)
)
_XcmHrDevMgmtV1EventOID_ObjectIdentity = ObjectIdentity
xcmHrDevMgmtV1EventOID = _XcmHrDevMgmtV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 1)
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtV1EventOID.setStatus("current")
_XcmHrDevMgmtV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmHrDevMgmtV2EventPrefix = _XcmHrDevMgmtV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 1, 0)
)
_XcmHrDevMgmtTable_Object = MibTable
xcmHrDevMgmtTable = _XcmHrDevMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtTable.setStatus("current")
_XcmHrDevMgmtEntry_Object = MibTableRow
xcmHrDevMgmtEntry = _XcmHrDevMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1)
)
xcmHrDevMgmtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtEntry.setStatus("current")
_XcmHrDevMgmtRowStatus_Type = RowStatus
_XcmHrDevMgmtRowStatus_Object = MibTableColumn
xcmHrDevMgmtRowStatus = _XcmHrDevMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 1),
    _XcmHrDevMgmtRowStatus_Type()
)
xcmHrDevMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtRowStatus.setStatus("current")


class _XcmHrDevMgmtCommandRequest_Type(XcmHrDevMgmtCommandRequest):
    """Custom type xcmHrDevMgmtCommandRequest based on XcmHrDevMgmtCommandRequest"""


_XcmHrDevMgmtCommandRequest_Object = MibTableColumn
xcmHrDevMgmtCommandRequest = _XcmHrDevMgmtCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 2),
    _XcmHrDevMgmtCommandRequest_Type()
)
xcmHrDevMgmtCommandRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandRequest.setStatus("current")


class _XcmHrDevMgmtCommandData_Type(XcmHrDevMgmtCommandData):
    """Custom type xcmHrDevMgmtCommandData based on XcmHrDevMgmtCommandData"""
    defaultHexValue = ""

    subtypeSpec = XcmHrDevMgmtCommandData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtCommandData_Type.__name__ = "XcmHrDevMgmtCommandData"
_XcmHrDevMgmtCommandData_Object = MibTableColumn
xcmHrDevMgmtCommandData = _XcmHrDevMgmtCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 3),
    _XcmHrDevMgmtCommandData_Type()
)
xcmHrDevMgmtCommandData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandData.setStatus("current")
_XcmHrDevMgmtCommandStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmHrDevMgmtCommandStatus_Object = MibTableColumn
xcmHrDevMgmtCommandStatus = _XcmHrDevMgmtCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 4),
    _XcmHrDevMgmtCommandStatus_Type()
)
xcmHrDevMgmtCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandStatus.setStatus("current")


class _XcmHrDevMgmtUserPassword_Type(OctetString):
    """Custom type xcmHrDevMgmtUserPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtUserPassword_Type.__name__ = "OctetString"
_XcmHrDevMgmtUserPassword_Object = MibTableColumn
xcmHrDevMgmtUserPassword = _XcmHrDevMgmtUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 5),
    _XcmHrDevMgmtUserPassword_Type()
)
xcmHrDevMgmtUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtUserPassword.setStatus("current")


class _XcmHrDevMgmtOperatorPassword_Type(OctetString):
    """Custom type xcmHrDevMgmtOperatorPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtOperatorPassword_Type.__name__ = "OctetString"
_XcmHrDevMgmtOperatorPassword_Object = MibTableColumn
xcmHrDevMgmtOperatorPassword = _XcmHrDevMgmtOperatorPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 6),
    _XcmHrDevMgmtOperatorPassword_Type()
)
xcmHrDevMgmtOperatorPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtOperatorPassword.setStatus("current")


class _XcmHrDevMgmtAdminPassword_Type(OctetString):
    """Custom type xcmHrDevMgmtAdminPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtAdminPassword_Type.__name__ = "OctetString"
_XcmHrDevMgmtAdminPassword_Object = MibTableColumn
xcmHrDevMgmtAdminPassword = _XcmHrDevMgmtAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 7),
    _XcmHrDevMgmtAdminPassword_Type()
)
xcmHrDevMgmtAdminPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtAdminPassword.setStatus("current")


class _XcmHrDevMgmtCommandInProgress_Type(TruthValue):
    """Custom type xcmHrDevMgmtCommandInProgress based on TruthValue"""


_XcmHrDevMgmtCommandInProgress_Object = MibTableColumn
xcmHrDevMgmtCommandInProgress = _XcmHrDevMgmtCommandInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 8),
    _XcmHrDevMgmtCommandInProgress_Type()
)
xcmHrDevMgmtCommandInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandInProgress.setStatus("current")


class _XcmHrDevMgmtUserName_Type(OctetString):
    """Custom type xcmHrDevMgmtUserName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtUserName_Type.__name__ = "OctetString"
_XcmHrDevMgmtUserName_Object = MibTableColumn
xcmHrDevMgmtUserName = _XcmHrDevMgmtUserName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 9),
    _XcmHrDevMgmtUserName_Type()
)
xcmHrDevMgmtUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtUserName.setStatus("current")


class _XcmHrDevMgmtOperatorName_Type(OctetString):
    """Custom type xcmHrDevMgmtOperatorName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtOperatorName_Type.__name__ = "OctetString"
_XcmHrDevMgmtOperatorName_Object = MibTableColumn
xcmHrDevMgmtOperatorName = _XcmHrDevMgmtOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 10),
    _XcmHrDevMgmtOperatorName_Type()
)
xcmHrDevMgmtOperatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtOperatorName.setStatus("current")


class _XcmHrDevMgmtAdminName_Type(OctetString):
    """Custom type xcmHrDevMgmtAdminName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtAdminName_Type.__name__ = "OctetString"
_XcmHrDevMgmtAdminName_Object = MibTableColumn
xcmHrDevMgmtAdminName = _XcmHrDevMgmtAdminName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 11),
    _XcmHrDevMgmtAdminName_Type()
)
xcmHrDevMgmtAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtAdminName.setStatus("current")


class _XcmHrDevMgmtCustomPassword_Type(OctetString):
    """Custom type xcmHrDevMgmtCustomPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtCustomPassword_Type.__name__ = "OctetString"
_XcmHrDevMgmtCustomPassword_Object = MibTableColumn
xcmHrDevMgmtCustomPassword = _XcmHrDevMgmtCustomPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 12),
    _XcmHrDevMgmtCustomPassword_Type()
)
xcmHrDevMgmtCustomPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCustomPassword.setStatus("current")
_XcmHrDevPower_ObjectIdentity = ObjectIdentity
xcmHrDevPower = _XcmHrDevPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6)
)
_XcmHrDevPowerTable_Object = MibTable
xcmHrDevPowerTable = _XcmHrDevPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevPowerTable.setStatus("current")
_XcmHrDevPowerEntry_Object = MibTableRow
xcmHrDevPowerEntry = _XcmHrDevPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1)
)
xcmHrDevPowerEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevPowerEntry.setStatus("current")
_XcmHrDevPowerRowStatus_Type = RowStatus
_XcmHrDevPowerRowStatus_Object = MibTableColumn
xcmHrDevPowerRowStatus = _XcmHrDevPowerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 1),
    _XcmHrDevPowerRowStatus_Type()
)
xcmHrDevPowerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerRowStatus.setStatus("current")


class _XcmHrDevPowerWarmUpSupport_Type(PresentOnOff):
    """Custom type xcmHrDevPowerWarmUpSupport based on PresentOnOff"""


_XcmHrDevPowerWarmUpSupport_Object = MibTableColumn
xcmHrDevPowerWarmUpSupport = _XcmHrDevPowerWarmUpSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 2),
    _XcmHrDevPowerWarmUpSupport_Type()
)
xcmHrDevPowerWarmUpSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpSupport.setStatus("current")


class _XcmHrDevPowerCoolDownSupport_Type(PresentOnOff):
    """Custom type xcmHrDevPowerCoolDownSupport based on PresentOnOff"""


_XcmHrDevPowerCoolDownSupport_Object = MibTableColumn
xcmHrDevPowerCoolDownSupport = _XcmHrDevPowerCoolDownSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 3),
    _XcmHrDevPowerCoolDownSupport_Type()
)
xcmHrDevPowerCoolDownSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownSupport.setStatus("current")


class _XcmHrDevPowerEnergySaveSupport_Type(PresentOnOff):
    """Custom type xcmHrDevPowerEnergySaveSupport based on PresentOnOff"""


_XcmHrDevPowerEnergySaveSupport_Object = MibTableColumn
xcmHrDevPowerEnergySaveSupport = _XcmHrDevPowerEnergySaveSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 4),
    _XcmHrDevPowerEnergySaveSupport_Type()
)
xcmHrDevPowerEnergySaveSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveSupport.setStatus("current")


class _XcmHrDevPowerTimeUnit_Type(XcmHrDevPowerTimeUnit):
    """Custom type xcmHrDevPowerTimeUnit based on XcmHrDevPowerTimeUnit"""


_XcmHrDevPowerTimeUnit_Object = MibTableColumn
xcmHrDevPowerTimeUnit = _XcmHrDevPowerTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 5),
    _XcmHrDevPowerTimeUnit_Type()
)
xcmHrDevPowerTimeUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerTimeUnit.setStatus("current")


class _XcmHrDevPowerWarmUpDelay_Type(Integer32):
    """Custom type xcmHrDevPowerWarmUpDelay based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerWarmUpDelay_Object = MibTableColumn
xcmHrDevPowerWarmUpDelay = _XcmHrDevPowerWarmUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 6),
    _XcmHrDevPowerWarmUpDelay_Type()
)
xcmHrDevPowerWarmUpDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpDelay.setStatus("current")


class _XcmHrDevPowerWarmUpDuration_Type(Integer32):
    """Custom type xcmHrDevPowerWarmUpDuration based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerWarmUpDuration_Object = MibTableColumn
xcmHrDevPowerWarmUpDuration = _XcmHrDevPowerWarmUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 7),
    _XcmHrDevPowerWarmUpDuration_Type()
)
xcmHrDevPowerWarmUpDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpDuration.setStatus("current")


class _XcmHrDevPowerCoolDownDelay_Type(Integer32):
    """Custom type xcmHrDevPowerCoolDownDelay based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerCoolDownDelay_Object = MibTableColumn
xcmHrDevPowerCoolDownDelay = _XcmHrDevPowerCoolDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 8),
    _XcmHrDevPowerCoolDownDelay_Type()
)
xcmHrDevPowerCoolDownDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownDelay.setStatus("current")


class _XcmHrDevPowerCoolDownDuration_Type(Integer32):
    """Custom type xcmHrDevPowerCoolDownDuration based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerCoolDownDuration_Object = MibTableColumn
xcmHrDevPowerCoolDownDuration = _XcmHrDevPowerCoolDownDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 9),
    _XcmHrDevPowerCoolDownDuration_Type()
)
xcmHrDevPowerCoolDownDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownDuration.setStatus("current")


class _XcmHrDevPowerEnergySaveDelay_Type(Integer32):
    """Custom type xcmHrDevPowerEnergySaveDelay based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerEnergySaveDelay_Object = MibTableColumn
xcmHrDevPowerEnergySaveDelay = _XcmHrDevPowerEnergySaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 10),
    _XcmHrDevPowerEnergySaveDelay_Type()
)
xcmHrDevPowerEnergySaveDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveDelay.setStatus("current")


class _XcmHrDevPowerEnergySaveDuration_Type(Integer32):
    """Custom type xcmHrDevPowerEnergySaveDuration based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerEnergySaveDuration_Object = MibTableColumn
xcmHrDevPowerEnergySaveDuration = _XcmHrDevPowerEnergySaveDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 11),
    _XcmHrDevPowerEnergySaveDuration_Type()
)
xcmHrDevPowerEnergySaveDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveDuration.setStatus("current")


class _XcmHrDevPowerWakeUpSupport_Type(PresentOnOff):
    """Custom type xcmHrDevPowerWakeUpSupport based on PresentOnOff"""


_XcmHrDevPowerWakeUpSupport_Object = MibTableColumn
xcmHrDevPowerWakeUpSupport = _XcmHrDevPowerWakeUpSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 12),
    _XcmHrDevPowerWakeUpSupport_Type()
)
xcmHrDevPowerWakeUpSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpSupport.setStatus("current")


class _XcmHrDevPowerWakeUpDelay_Type(Integer32):
    """Custom type xcmHrDevPowerWakeUpDelay based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerWakeUpDelay_Object = MibTableColumn
xcmHrDevPowerWakeUpDelay = _XcmHrDevPowerWakeUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 13),
    _XcmHrDevPowerWakeUpDelay_Type()
)
xcmHrDevPowerWakeUpDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpDelay.setStatus("current")


class _XcmHrDevPowerWakeUpDuration_Type(Integer32):
    """Custom type xcmHrDevPowerWakeUpDuration based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerWakeUpDuration_Object = MibTableColumn
xcmHrDevPowerWakeUpDuration = _XcmHrDevPowerWakeUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 14),
    _XcmHrDevPowerWakeUpDuration_Type()
)
xcmHrDevPowerWakeUpDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpDuration.setStatus("current")


class _XcmHrDevPowerShutdownDelay_Type(Integer32):
    """Custom type xcmHrDevPowerShutdownDelay based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerShutdownDelay_Object = MibTableColumn
xcmHrDevPowerShutdownDelay = _XcmHrDevPowerShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 15),
    _XcmHrDevPowerShutdownDelay_Type()
)
xcmHrDevPowerShutdownDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerShutdownDelay.setStatus("current")


class _XcmHrDevPowerShutdownDuration_Type(Integer32):
    """Custom type xcmHrDevPowerShutdownDuration based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerShutdownDuration_Object = MibTableColumn
xcmHrDevPowerShutdownDuration = _XcmHrDevPowerShutdownDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 16),
    _XcmHrDevPowerShutdownDuration_Type()
)
xcmHrDevPowerShutdownDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerShutdownDuration.setStatus("current")


class _XcmHrDevPowerStartupDelay_Type(Integer32):
    """Custom type xcmHrDevPowerStartupDelay based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerStartupDelay_Object = MibTableColumn
xcmHrDevPowerStartupDelay = _XcmHrDevPowerStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 17),
    _XcmHrDevPowerStartupDelay_Type()
)
xcmHrDevPowerStartupDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerStartupDelay.setStatus("current")


class _XcmHrDevPowerStartupDuration_Type(Integer32):
    """Custom type xcmHrDevPowerStartupDuration based on Integer32"""
    defaultValue = 0


_XcmHrDevPowerStartupDuration_Object = MibTableColumn
xcmHrDevPowerStartupDuration = _XcmHrDevPowerStartupDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 18),
    _XcmHrDevPowerStartupDuration_Type()
)
xcmHrDevPowerStartupDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerStartupDuration.setStatus("current")
_XcmHrDevTraffic_ObjectIdentity = ObjectIdentity
xcmHrDevTraffic = _XcmHrDevTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7)
)
_XcmHrDevTrafficTable_Object = MibTable
xcmHrDevTrafficTable = _XcmHrDevTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevTrafficTable.setStatus("current")
_XcmHrDevTrafficEntry_Object = MibTableRow
xcmHrDevTrafficEntry = _XcmHrDevTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1)
)
xcmHrDevTrafficEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevTrafficEntry.setStatus("current")
_XcmHrDevTrafficRowStatus_Type = RowStatus
_XcmHrDevTrafficRowStatus_Object = MibTableColumn
xcmHrDevTrafficRowStatus = _XcmHrDevTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 1),
    _XcmHrDevTrafficRowStatus_Type()
)
xcmHrDevTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficRowStatus.setStatus("current")


class _XcmHrDevTrafficInputSupport_Type(PresentOnOff):
    """Custom type xcmHrDevTrafficInputSupport based on PresentOnOff"""


_XcmHrDevTrafficInputSupport_Object = MibTableColumn
xcmHrDevTrafficInputSupport = _XcmHrDevTrafficInputSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 2),
    _XcmHrDevTrafficInputSupport_Type()
)
xcmHrDevTrafficInputSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputSupport.setStatus("current")


class _XcmHrDevTrafficOutputSupport_Type(PresentOnOff):
    """Custom type xcmHrDevTrafficOutputSupport based on PresentOnOff"""


_XcmHrDevTrafficOutputSupport_Object = MibTableColumn
xcmHrDevTrafficOutputSupport = _XcmHrDevTrafficOutputSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 3),
    _XcmHrDevTrafficOutputSupport_Type()
)
xcmHrDevTrafficOutputSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputSupport.setStatus("current")


class _XcmHrDevTrafficInputUnit_Type(XcmHrDevTrafficUnit):
    """Custom type xcmHrDevTrafficInputUnit based on XcmHrDevTrafficUnit"""


_XcmHrDevTrafficInputUnit_Object = MibTableColumn
xcmHrDevTrafficInputUnit = _XcmHrDevTrafficInputUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 4),
    _XcmHrDevTrafficInputUnit_Type()
)
xcmHrDevTrafficInputUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputUnit.setStatus("current")


class _XcmHrDevTrafficOutputUnit_Type(XcmHrDevTrafficUnit):
    """Custom type xcmHrDevTrafficOutputUnit based on XcmHrDevTrafficUnit"""


_XcmHrDevTrafficOutputUnit_Object = MibTableColumn
xcmHrDevTrafficOutputUnit = _XcmHrDevTrafficOutputUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 5),
    _XcmHrDevTrafficOutputUnit_Type()
)
xcmHrDevTrafficOutputUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputUnit.setStatus("current")
_XcmHrDevTrafficInputCount_Type = Counter32
_XcmHrDevTrafficInputCount_Object = MibTableColumn
xcmHrDevTrafficInputCount = _XcmHrDevTrafficInputCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 6),
    _XcmHrDevTrafficInputCount_Type()
)
xcmHrDevTrafficInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputCount.setStatus("current")
_XcmHrDevTrafficOutputCount_Type = Counter32
_XcmHrDevTrafficOutputCount_Object = MibTableColumn
xcmHrDevTrafficOutputCount = _XcmHrDevTrafficOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 7),
    _XcmHrDevTrafficOutputCount_Type()
)
xcmHrDevTrafficOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputCount.setStatus("current")


class _XcmHrDevTrafficInputMaxSize_Type(Cardinal32):
    """Custom type xcmHrDevTrafficInputMaxSize based on Cardinal32"""
    defaultValue = 0


_XcmHrDevTrafficInputMaxSize_Object = MibTableColumn
xcmHrDevTrafficInputMaxSize = _XcmHrDevTrafficInputMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 8),
    _XcmHrDevTrafficInputMaxSize_Type()
)
xcmHrDevTrafficInputMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputMaxSize.setStatus("current")


class _XcmHrDevTrafficOutputMaxSize_Type(Cardinal32):
    """Custom type xcmHrDevTrafficOutputMaxSize based on Cardinal32"""
    defaultValue = 0


_XcmHrDevTrafficOutputMaxSize_Object = MibTableColumn
xcmHrDevTrafficOutputMaxSize = _XcmHrDevTrafficOutputMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 9),
    _XcmHrDevTrafficOutputMaxSize_Type()
)
xcmHrDevTrafficOutputMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputMaxSize.setStatus("current")


class _XcmHrDevTrafficInputTimeout_Type(Integer32):
    """Custom type xcmHrDevTrafficInputTimeout based on Integer32"""
    defaultValue = 0


_XcmHrDevTrafficInputTimeout_Object = MibTableColumn
xcmHrDevTrafficInputTimeout = _XcmHrDevTrafficInputTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 10),
    _XcmHrDevTrafficInputTimeout_Type()
)
xcmHrDevTrafficInputTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputTimeout.setUnits("seconds")


class _XcmHrDevTrafficOutputTimeout_Type(Integer32):
    """Custom type xcmHrDevTrafficOutputTimeout based on Integer32"""
    defaultValue = 0


_XcmHrDevTrafficOutputTimeout_Object = MibTableColumn
xcmHrDevTrafficOutputTimeout = _XcmHrDevTrafficOutputTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 11),
    _XcmHrDevTrafficOutputTimeout_Type()
)
xcmHrDevTrafficOutputTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputTimeout.setUnits("seconds")
_XcmHrSystemFault_ObjectIdentity = ObjectIdentity
xcmHrSystemFault = _XcmHrSystemFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8)
)
_XcmHrSystemFaultTable_Object = MibTable
xcmHrSystemFaultTable = _XcmHrSystemFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2)
)
if mibBuilder.loadTexts:
    xcmHrSystemFaultTable.setStatus("current")
_XcmHrSystemFaultEntry_Object = MibTableRow
xcmHrSystemFaultEntry = _XcmHrSystemFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1)
)
xcmHrSystemFaultEntry.setIndexNames(
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultIndex"),
)
if mibBuilder.loadTexts:
    xcmHrSystemFaultEntry.setStatus("current")
_XcmHrSystemFaultIndex_Type = Ordinal32
_XcmHrSystemFaultIndex_Object = MibTableColumn
xcmHrSystemFaultIndex = _XcmHrSystemFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 1),
    _XcmHrSystemFaultIndex_Type()
)
xcmHrSystemFaultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrSystemFaultIndex.setStatus("current")
_XcmHrSystemFaultRowStatus_Type = RowStatus
_XcmHrSystemFaultRowStatus_Object = MibTableColumn
xcmHrSystemFaultRowStatus = _XcmHrSystemFaultRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 2),
    _XcmHrSystemFaultRowStatus_Type()
)
xcmHrSystemFaultRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSystemFaultRowStatus.setStatus("current")


class _XcmHrSystemFaultCode_Type(Integer32):
    """Custom type xcmHrSystemFaultCode based on Integer32"""
    defaultValue = 0


_XcmHrSystemFaultCode_Object = MibTableColumn
xcmHrSystemFaultCode = _XcmHrSystemFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 3),
    _XcmHrSystemFaultCode_Type()
)
xcmHrSystemFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultCode.setStatus("current")


class _XcmHrSystemFaultString_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrSystemFaultString based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrSystemFaultString_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrSystemFaultString_Object = MibTableColumn
xcmHrSystemFaultString = _XcmHrSystemFaultString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 4),
    _XcmHrSystemFaultString_Type()
)
xcmHrSystemFaultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultString.setStatus("current")


class _XcmHrSystemFaultReferenceOID_Type(ObjectIdentifier):
    """Custom type xcmHrSystemFaultReferenceOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmHrSystemFaultReferenceOID_Object = MibTableColumn
xcmHrSystemFaultReferenceOID = _XcmHrSystemFaultReferenceOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 5),
    _XcmHrSystemFaultReferenceOID_Type()
)
xcmHrSystemFaultReferenceOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultReferenceOID.setStatus("current")


class _XcmHrSystemFaultHrDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrSystemFaultHrDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSystemFaultHrDeviceIndex_Object = MibTableColumn
xcmHrSystemFaultHrDeviceIndex = _XcmHrSystemFaultHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 6),
    _XcmHrSystemFaultHrDeviceIndex_Type()
)
xcmHrSystemFaultHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultHrDeviceIndex.setStatus("current")


class _XcmHrSystemFaultDate_Type(DateAndTime):
    """Custom type xcmHrSystemFaultDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrSystemFaultDate_Object = MibTableColumn
xcmHrSystemFaultDate = _XcmHrSystemFaultDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 7),
    _XcmHrSystemFaultDate_Type()
)
xcmHrSystemFaultDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultDate.setStatus("current")
_XcmHrGeneral_ObjectIdentity = ObjectIdentity
xcmHrGeneral = _XcmHrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9)
)
_XcmHrGeneralTable_Object = MibTable
xcmHrGeneralTable = _XcmHrGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2)
)
if mibBuilder.loadTexts:
    xcmHrGeneralTable.setStatus("current")
_XcmHrGeneralEntry_Object = MibTableRow
xcmHrGeneralEntry = _XcmHrGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1)
)
xcmHrGeneralEntry.setIndexNames(
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralIndex"),
)
if mibBuilder.loadTexts:
    xcmHrGeneralEntry.setStatus("current")
_XcmHrGeneralIndex_Type = Ordinal32
_XcmHrGeneralIndex_Object = MibTableColumn
xcmHrGeneralIndex = _XcmHrGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 1),
    _XcmHrGeneralIndex_Type()
)
xcmHrGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrGeneralIndex.setStatus("current")
_XcmHrGeneralRowStatus_Type = RowStatus
_XcmHrGeneralRowStatus_Object = MibTableColumn
xcmHrGeneralRowStatus = _XcmHrGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 2),
    _XcmHrGeneralRowStatus_Type()
)
xcmHrGeneralRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralRowStatus.setStatus("current")


class _XcmHrGeneralVersionID_Type(ProductID):
    """Custom type xcmHrGeneralVersionID based on ProductID"""
    defaultValue = (0, 0)


_XcmHrGeneralVersionID_Object = MibTableColumn
xcmHrGeneralVersionID = _XcmHrGeneralVersionID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 3),
    _XcmHrGeneralVersionID_Type()
)
xcmHrGeneralVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralVersionID.setStatus("current")


class _XcmHrGeneralVersionDate_Type(DateAndTime):
    """Custom type xcmHrGeneralVersionDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrGeneralVersionDate_Object = MibTableColumn
xcmHrGeneralVersionDate = _XcmHrGeneralVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 4),
    _XcmHrGeneralVersionDate_Type()
)
xcmHrGeneralVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralVersionDate.setStatus("current")


class _XcmHrGeneralGroupSupport_Type(XcmHrGroupSupport):
    """Custom type xcmHrGeneralGroupSupport based on XcmHrGroupSupport"""
    defaultValue = 71


_XcmHrGeneralGroupSupport_Object = MibTableColumn
xcmHrGeneralGroupSupport = _XcmHrGeneralGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 5),
    _XcmHrGeneralGroupSupport_Type()
)
xcmHrGeneralGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralGroupSupport.setStatus("current")


class _XcmHrGeneralStorageLast_Type(Cardinal32):
    """Custom type xcmHrGeneralStorageLast based on Cardinal32"""
    defaultValue = 0


_XcmHrGeneralStorageLast_Object = MibTableColumn
xcmHrGeneralStorageLast = _XcmHrGeneralStorageLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 6),
    _XcmHrGeneralStorageLast_Type()
)
xcmHrGeneralStorageLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralStorageLast.setStatus("current")


class _XcmHrGeneralDeviceLast_Type(Cardinal32):
    """Custom type xcmHrGeneralDeviceLast based on Cardinal32"""
    defaultValue = 0


_XcmHrGeneralDeviceLast_Object = MibTableColumn
xcmHrGeneralDeviceLast = _XcmHrGeneralDeviceLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 7),
    _XcmHrGeneralDeviceLast_Type()
)
xcmHrGeneralDeviceLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralDeviceLast.setStatus("current")


class _XcmHrGeneralFSLast_Type(Cardinal32):
    """Custom type xcmHrGeneralFSLast based on Cardinal32"""
    defaultValue = 0


_XcmHrGeneralFSLast_Object = MibTableColumn
xcmHrGeneralFSLast = _XcmHrGeneralFSLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 8),
    _XcmHrGeneralFSLast_Type()
)
xcmHrGeneralFSLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralFSLast.setStatus("current")


class _XcmHrGeneralSWRunLast_Type(Cardinal32):
    """Custom type xcmHrGeneralSWRunLast based on Cardinal32"""
    defaultValue = 0


_XcmHrGeneralSWRunLast_Object = MibTableColumn
xcmHrGeneralSWRunLast = _XcmHrGeneralSWRunLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 9),
    _XcmHrGeneralSWRunLast_Type()
)
xcmHrGeneralSWRunLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralSWRunLast.setStatus("current")


class _XcmHrGeneralSWInstalledLast_Type(Cardinal32):
    """Custom type xcmHrGeneralSWInstalledLast based on Cardinal32"""
    defaultValue = 0


_XcmHrGeneralSWInstalledLast_Object = MibTableColumn
xcmHrGeneralSWInstalledLast = _XcmHrGeneralSWInstalledLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 10),
    _XcmHrGeneralSWInstalledLast_Type()
)
xcmHrGeneralSWInstalledLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralSWInstalledLast.setStatus("current")


class _XcmHrGeneralSystemFaultLast_Type(Cardinal32):
    """Custom type xcmHrGeneralSystemFaultLast based on Cardinal32"""
    defaultValue = 0


_XcmHrGeneralSystemFaultLast_Object = MibTableColumn
xcmHrGeneralSystemFaultLast = _XcmHrGeneralSystemFaultLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 11),
    _XcmHrGeneralSystemFaultLast_Type()
)
xcmHrGeneralSystemFaultLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralSystemFaultLast.setStatus("current")


class _XcmHrGeneralCreateSupport_Type(XcmHrGroupSupport):
    """Custom type xcmHrGeneralCreateSupport based on XcmHrGroupSupport"""
    defaultValue = 0


_XcmHrGeneralCreateSupport_Object = MibTableColumn
xcmHrGeneralCreateSupport = _XcmHrGeneralCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 12),
    _XcmHrGeneralCreateSupport_Type()
)
xcmHrGeneralCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralCreateSupport.setStatus("current")


class _XcmHrGeneralUpdateSupport_Type(XcmHrGroupSupport):
    """Custom type xcmHrGeneralUpdateSupport based on XcmHrGroupSupport"""
    defaultValue = 0


_XcmHrGeneralUpdateSupport_Object = MibTableColumn
xcmHrGeneralUpdateSupport = _XcmHrGeneralUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 13),
    _XcmHrGeneralUpdateSupport_Type()
)
xcmHrGeneralUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralUpdateSupport.setStatus("current")
_XcmHrDevCalendar_ObjectIdentity = ObjectIdentity
xcmHrDevCalendar = _XcmHrDevCalendar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10)
)
_XcmHrDevCalendarTable_Object = MibTable
xcmHrDevCalendarTable = _XcmHrDevCalendarTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevCalendarTable.setStatus("current")
_XcmHrDevCalendarEntry_Object = MibTableRow
xcmHrDevCalendarEntry = _XcmHrDevCalendarEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1)
)
xcmHrDevCalendarEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarDayOfWeek"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarTimeOfDay"),
)
if mibBuilder.loadTexts:
    xcmHrDevCalendarEntry.setStatus("current")
_XcmHrDevCalendarDayOfWeek_Type = XcmHrDevCalendarDayOfWeek
_XcmHrDevCalendarDayOfWeek_Object = MibTableColumn
xcmHrDevCalendarDayOfWeek = _XcmHrDevCalendarDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 1),
    _XcmHrDevCalendarDayOfWeek_Type()
)
xcmHrDevCalendarDayOfWeek.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDevCalendarDayOfWeek.setStatus("current")
_XcmHrDevCalendarTimeOfDay_Type = XcmHrDevCalendarTimeOfDay
_XcmHrDevCalendarTimeOfDay_Object = MibTableColumn
xcmHrDevCalendarTimeOfDay = _XcmHrDevCalendarTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 2),
    _XcmHrDevCalendarTimeOfDay_Type()
)
xcmHrDevCalendarTimeOfDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDevCalendarTimeOfDay.setStatus("current")
_XcmHrDevCalendarRowStatus_Type = RowStatus
_XcmHrDevCalendarRowStatus_Object = MibTableColumn
xcmHrDevCalendarRowStatus = _XcmHrDevCalendarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 3),
    _XcmHrDevCalendarRowStatus_Type()
)
xcmHrDevCalendarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCalendarRowStatus.setStatus("current")


class _XcmHrDevCalendarExplicitDate_Type(DateAndTime):
    """Custom type xcmHrDevCalendarExplicitDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrDevCalendarExplicitDate_Object = MibTableColumn
xcmHrDevCalendarExplicitDate = _XcmHrDevCalendarExplicitDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 4),
    _XcmHrDevCalendarExplicitDate_Type()
)
xcmHrDevCalendarExplicitDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCalendarExplicitDate.setStatus("current")


class _XcmHrDevCalendarCommandRequest_Type(XcmHrDevMgmtCommandRequest):
    """Custom type xcmHrDevCalendarCommandRequest based on XcmHrDevMgmtCommandRequest"""


_XcmHrDevCalendarCommandRequest_Object = MibTableColumn
xcmHrDevCalendarCommandRequest = _XcmHrDevCalendarCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 5),
    _XcmHrDevCalendarCommandRequest_Type()
)
xcmHrDevCalendarCommandRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCalendarCommandRequest.setStatus("current")


class _XcmHrDevCalendarCommandData_Type(XcmHrDevMgmtCommandData):
    """Custom type xcmHrDevCalendarCommandData based on XcmHrDevMgmtCommandData"""
    defaultHexValue = ""


_XcmHrDevCalendarCommandData_Object = MibTableColumn
xcmHrDevCalendarCommandData = _XcmHrDevCalendarCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 6),
    _XcmHrDevCalendarCommandData_Type()
)
xcmHrDevCalendarCommandData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCalendarCommandData.setStatus("current")
_XcmHrSWRun_ObjectIdentity = ObjectIdentity
xcmHrSWRun = _XcmHrSWRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11)
)
_XcmHrSWRunTable_Object = MibTable
xcmHrSWRunTable = _XcmHrSWRunTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2)
)
if mibBuilder.loadTexts:
    xcmHrSWRunTable.setStatus("current")
_XcmHrSWRunEntry_Object = MibTableRow
xcmHrSWRunEntry = _XcmHrSWRunEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1)
)
xcmHrSWRunEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrSWRunIndex"),
)
if mibBuilder.loadTexts:
    xcmHrSWRunEntry.setStatus("current")
_XcmHrSWRunRowStatus_Type = RowStatus
_XcmHrSWRunRowStatus_Object = MibTableColumn
xcmHrSWRunRowStatus = _XcmHrSWRunRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 1),
    _XcmHrSWRunRowStatus_Type()
)
xcmHrSWRunRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunRowStatus.setStatus("current")


class _XcmHrSWRunAdminName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrSWRunAdminName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrSWRunAdminName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrSWRunAdminName_Object = MibTableColumn
xcmHrSWRunAdminName = _XcmHrSWRunAdminName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 2),
    _XcmHrSWRunAdminName_Type()
)
xcmHrSWRunAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunAdminName.setStatus("current")
_XcmHrSWRunXStatus_Type = XcmHrSWRunXStatus
_XcmHrSWRunXStatus_Object = MibTableColumn
xcmHrSWRunXStatus = _XcmHrSWRunXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 3),
    _XcmHrSWRunXStatus_Type()
)
xcmHrSWRunXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSWRunXStatus.setStatus("current")


class _XcmHrSWRunRowCreateDate_Type(DateAndTime):
    """Custom type xcmHrSWRunRowCreateDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrSWRunRowCreateDate_Object = MibTableColumn
xcmHrSWRunRowCreateDate = _XcmHrSWRunRowCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 4),
    _XcmHrSWRunRowCreateDate_Type()
)
xcmHrSWRunRowCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSWRunRowCreateDate.setStatus("current")


class _XcmHrSWRunPhysicalDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrSWRunPhysicalDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSWRunPhysicalDeviceIndex_Object = MibTableColumn
xcmHrSWRunPhysicalDeviceIndex = _XcmHrSWRunPhysicalDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 5),
    _XcmHrSWRunPhysicalDeviceIndex_Type()
)
xcmHrSWRunPhysicalDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunPhysicalDeviceIndex.setStatus("current")


class _XcmHrSWRunLogicalDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrSWRunLogicalDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSWRunLogicalDeviceIndex_Object = MibTableColumn
xcmHrSWRunLogicalDeviceIndex = _XcmHrSWRunLogicalDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 6),
    _XcmHrSWRunLogicalDeviceIndex_Type()
)
xcmHrSWRunLogicalDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunLogicalDeviceIndex.setStatus("current")


class _XcmHrSWRunNextIndex_Type(Cardinal32):
    """Custom type xcmHrSWRunNextIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSWRunNextIndex_Object = MibTableColumn
xcmHrSWRunNextIndex = _XcmHrSWRunNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 7),
    _XcmHrSWRunNextIndex_Type()
)
xcmHrSWRunNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunNextIndex.setStatus("current")


class _XcmHrSWRunPreviousIndex_Type(Cardinal32):
    """Custom type xcmHrSWRunPreviousIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSWRunPreviousIndex_Object = MibTableColumn
xcmHrSWRunPreviousIndex = _XcmHrSWRunPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 8),
    _XcmHrSWRunPreviousIndex_Type()
)
xcmHrSWRunPreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunPreviousIndex.setStatus("current")
_XcmHrSWInstalled_ObjectIdentity = ObjectIdentity
xcmHrSWInstalled = _XcmHrSWInstalled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12)
)
_XcmHrSWInstalledTable_Object = MibTable
xcmHrSWInstalledTable = _XcmHrSWInstalledTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2)
)
if mibBuilder.loadTexts:
    xcmHrSWInstalledTable.setStatus("current")
_XcmHrSWInstalledEntry_Object = MibTableRow
xcmHrSWInstalledEntry = _XcmHrSWInstalledEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1)
)
xcmHrSWInstalledEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrSWInstalledIndex"),
)
if mibBuilder.loadTexts:
    xcmHrSWInstalledEntry.setStatus("current")
_XcmHrSWInstalledRowStatus_Type = RowStatus
_XcmHrSWInstalledRowStatus_Object = MibTableColumn
xcmHrSWInstalledRowStatus = _XcmHrSWInstalledRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 1),
    _XcmHrSWInstalledRowStatus_Type()
)
xcmHrSWInstalledRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledRowStatus.setStatus("current")


class _XcmHrSWInstalledAdminName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrSWInstalledAdminName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrSWInstalledAdminName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrSWInstalledAdminName_Object = MibTableColumn
xcmHrSWInstalledAdminName = _XcmHrSWInstalledAdminName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 2),
    _XcmHrSWInstalledAdminName_Type()
)
xcmHrSWInstalledAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledAdminName.setStatus("current")
_XcmHrSWInstalledXStatus_Type = XcmHrSWRunXStatus
_XcmHrSWInstalledXStatus_Object = MibTableColumn
xcmHrSWInstalledXStatus = _XcmHrSWInstalledXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 3),
    _XcmHrSWInstalledXStatus_Type()
)
xcmHrSWInstalledXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSWInstalledXStatus.setStatus("current")


class _XcmHrSWInstalledRowCreateDate_Type(DateAndTime):
    """Custom type xcmHrSWInstalledRowCreateDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrSWInstalledRowCreateDate_Object = MibTableColumn
xcmHrSWInstalledRowCreateDate = _XcmHrSWInstalledRowCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 4),
    _XcmHrSWInstalledRowCreateDate_Type()
)
xcmHrSWInstalledRowCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSWInstalledRowCreateDate.setStatus("current")


class _XcmHrSWInstalledPhysicalIndex_Type(Cardinal32):
    """Custom type xcmHrSWInstalledPhysicalIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSWInstalledPhysicalIndex_Object = MibTableColumn
xcmHrSWInstalledPhysicalIndex = _XcmHrSWInstalledPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 5),
    _XcmHrSWInstalledPhysicalIndex_Type()
)
xcmHrSWInstalledPhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledPhysicalIndex.setStatus("current")


class _XcmHrSWInstalledLogicalIndex_Type(Cardinal32):
    """Custom type xcmHrSWInstalledLogicalIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSWInstalledLogicalIndex_Object = MibTableColumn
xcmHrSWInstalledLogicalIndex = _XcmHrSWInstalledLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 6),
    _XcmHrSWInstalledLogicalIndex_Type()
)
xcmHrSWInstalledLogicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledLogicalIndex.setStatus("current")


class _XcmHrSWInstalledNextIndex_Type(Cardinal32):
    """Custom type xcmHrSWInstalledNextIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSWInstalledNextIndex_Object = MibTableColumn
xcmHrSWInstalledNextIndex = _XcmHrSWInstalledNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 7),
    _XcmHrSWInstalledNextIndex_Type()
)
xcmHrSWInstalledNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledNextIndex.setStatus("current")


class _XcmHrSWInstalledPreviousIndex_Type(Cardinal32):
    """Custom type xcmHrSWInstalledPreviousIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrSWInstalledPreviousIndex_Object = MibTableColumn
xcmHrSWInstalledPreviousIndex = _XcmHrSWInstalledPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 8),
    _XcmHrSWInstalledPreviousIndex_Type()
)
xcmHrSWInstalledPreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledPreviousIndex.setStatus("current")
_XcmHrDevDetail_ObjectIdentity = ObjectIdentity
xcmHrDevDetail = _XcmHrDevDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13)
)
_XcmHrDevDetailV1EventOID_ObjectIdentity = ObjectIdentity
xcmHrDevDetailV1EventOID = _XcmHrDevDetailV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 1)
)
if mibBuilder.loadTexts:
    xcmHrDevDetailV1EventOID.setStatus("current")
_XcmHrDevDetailV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmHrDevDetailV2EventPrefix = _XcmHrDevDetailV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 1, 0)
)
_XcmHrDevDetailTable_Object = MibTable
xcmHrDevDetailTable = _XcmHrDevDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevDetailTable.setStatus("current")
_XcmHrDevDetailEntry_Object = MibTableRow
xcmHrDevDetailEntry = _XcmHrDevDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1)
)
xcmHrDevDetailEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailType"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevDetailEntry.setStatus("current")
_XcmHrDevDetailType_Type = XcmHrDevDetailType
_XcmHrDevDetailType_Object = MibTableColumn
xcmHrDevDetailType = _XcmHrDevDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 1),
    _XcmHrDevDetailType_Type()
)
xcmHrDevDetailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevDetailType.setStatus("current")
_XcmHrDevDetailIndex_Type = Ordinal32
_XcmHrDevDetailIndex_Object = MibTableColumn
xcmHrDevDetailIndex = _XcmHrDevDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 2),
    _XcmHrDevDetailIndex_Type()
)
xcmHrDevDetailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevDetailIndex.setStatus("current")
_XcmHrDevDetailRowStatus_Type = RowStatus
_XcmHrDevDetailRowStatus_Object = MibTableColumn
xcmHrDevDetailRowStatus = _XcmHrDevDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 3),
    _XcmHrDevDetailRowStatus_Type()
)
xcmHrDevDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailRowStatus.setStatus("current")


class _XcmHrDevDetailUnitClass_Type(XcmHrDevDetailUnitClass):
    """Custom type xcmHrDevDetailUnitClass based on XcmHrDevDetailUnitClass"""


_XcmHrDevDetailUnitClass_Object = MibTableColumn
xcmHrDevDetailUnitClass = _XcmHrDevDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 4),
    _XcmHrDevDetailUnitClass_Type()
)
xcmHrDevDetailUnitClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailUnitClass.setStatus("current")


class _XcmHrDevDetailUnit_Type(Cardinal32):
    """Custom type xcmHrDevDetailUnit based on Cardinal32"""
    defaultValue = 0


_XcmHrDevDetailUnit_Object = MibTableColumn
xcmHrDevDetailUnit = _XcmHrDevDetailUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 5),
    _XcmHrDevDetailUnit_Type()
)
xcmHrDevDetailUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailUnit.setStatus("current")


class _XcmHrDevDetailValueInteger_Type(Integer32):
    """Custom type xcmHrDevDetailValueInteger based on Integer32"""
    defaultValue = 0


_XcmHrDevDetailValueInteger_Object = MibTableColumn
xcmHrDevDetailValueInteger = _XcmHrDevDetailValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 6),
    _XcmHrDevDetailValueInteger_Type()
)
xcmHrDevDetailValueInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueInteger.setStatus("current")


class _XcmHrDevDetailValueOID_Type(ObjectIdentifier):
    """Custom type xcmHrDevDetailValueOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmHrDevDetailValueOID_Object = MibTableColumn
xcmHrDevDetailValueOID = _XcmHrDevDetailValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 7),
    _XcmHrDevDetailValueOID_Type()
)
xcmHrDevDetailValueOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueOID.setStatus("current")


class _XcmHrDevDetailValueString_Type(OctetString):
    """Custom type xcmHrDevDetailValueString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevDetailValueString_Type.__name__ = "OctetString"
_XcmHrDevDetailValueString_Object = MibTableColumn
xcmHrDevDetailValueString = _XcmHrDevDetailValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 8),
    _XcmHrDevDetailValueString_Type()
)
xcmHrDevDetailValueString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueString.setStatus("current")


class _XcmHrDevDetailDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevDetailDescription based on XcmFixedLocaleDisplayString"""
    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevDetailDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevDetailDescription_Object = MibTableColumn
xcmHrDevDetailDescription = _XcmHrDevDetailDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 9),
    _XcmHrDevDetailDescription_Type()
)
xcmHrDevDetailDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailDescription.setStatus("current")
_XcmHrStorage_ObjectIdentity = ObjectIdentity
xcmHrStorage = _XcmHrStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14)
)
_XcmHrStorageTable_Object = MibTable
xcmHrStorageTable = _XcmHrStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2)
)
if mibBuilder.loadTexts:
    xcmHrStorageTable.setStatus("current")
_XcmHrStorageEntry_Object = MibTableRow
xcmHrStorageEntry = _XcmHrStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1)
)
xcmHrStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrStorageIndex"),
)
if mibBuilder.loadTexts:
    xcmHrStorageEntry.setStatus("current")
_XcmHrStorageRowStatus_Type = RowStatus
_XcmHrStorageRowStatus_Object = MibTableColumn
xcmHrStorageRowStatus = _XcmHrStorageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 1),
    _XcmHrStorageRowStatus_Type()
)
xcmHrStorageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageRowStatus.setStatus("current")


class _XcmHrStorageRealization_Type(XcmHrStorageRealization):
    """Custom type xcmHrStorageRealization based on XcmHrStorageRealization"""


_XcmHrStorageRealization_Object = MibTableColumn
xcmHrStorageRealization = _XcmHrStorageRealization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 2),
    _XcmHrStorageRealization_Type()
)
xcmHrStorageRealization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageRealization.setStatus("current")


class _XcmHrStorageStatus_Type(XcmHrDevInfoStatus):
    """Custom type xcmHrStorageStatus based on XcmHrDevInfoStatus"""


_XcmHrStorageStatus_Object = MibTableColumn
xcmHrStorageStatus = _XcmHrStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 3),
    _XcmHrStorageStatus_Type()
)
xcmHrStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrStorageStatus.setStatus("current")


class _XcmHrStorageProductDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrStorageProductDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStorageProductDeviceIndex_Object = MibTableColumn
xcmHrStorageProductDeviceIndex = _XcmHrStorageProductDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 4),
    _XcmHrStorageProductDeviceIndex_Type()
)
xcmHrStorageProductDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageProductDeviceIndex.setStatus("current")


class _XcmHrStoragePlatformDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrStoragePlatformDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStoragePlatformDeviceIndex_Object = MibTableColumn
xcmHrStoragePlatformDeviceIndex = _XcmHrStoragePlatformDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 5),
    _XcmHrStoragePlatformDeviceIndex_Type()
)
xcmHrStoragePlatformDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStoragePlatformDeviceIndex.setStatus("current")


class _XcmHrStoragePagingDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrStoragePagingDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStoragePagingDeviceIndex_Object = MibTableColumn
xcmHrStoragePagingDeviceIndex = _XcmHrStoragePagingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 6),
    _XcmHrStoragePagingDeviceIndex_Type()
)
xcmHrStoragePagingDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStoragePagingDeviceIndex.setStatus("current")


class _XcmHrStorageMatchingDeviceIndex_Type(Cardinal32):
    """Custom type xcmHrStorageMatchingDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStorageMatchingDeviceIndex_Object = MibTableColumn
xcmHrStorageMatchingDeviceIndex = _XcmHrStorageMatchingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 7),
    _XcmHrStorageMatchingDeviceIndex_Type()
)
xcmHrStorageMatchingDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageMatchingDeviceIndex.setStatus("current")


class _XcmHrStorageSWRunIndex_Type(Cardinal32):
    """Custom type xcmHrStorageSWRunIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStorageSWRunIndex_Object = MibTableColumn
xcmHrStorageSWRunIndex = _XcmHrStorageSWRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 8),
    _XcmHrStorageSWRunIndex_Type()
)
xcmHrStorageSWRunIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageSWRunIndex.setStatus("current")


class _XcmHrStorageSWInstalledIndex_Type(Cardinal32):
    """Custom type xcmHrStorageSWInstalledIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStorageSWInstalledIndex_Object = MibTableColumn
xcmHrStorageSWInstalledIndex = _XcmHrStorageSWInstalledIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 9),
    _XcmHrStorageSWInstalledIndex_Type()
)
xcmHrStorageSWInstalledIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageSWInstalledIndex.setStatus("current")


class _XcmHrStorageNextIndex_Type(Cardinal32):
    """Custom type xcmHrStorageNextIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStorageNextIndex_Object = MibTableColumn
xcmHrStorageNextIndex = _XcmHrStorageNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 10),
    _XcmHrStorageNextIndex_Type()
)
xcmHrStorageNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageNextIndex.setStatus("current")


class _XcmHrStoragePreviousIndex_Type(Cardinal32):
    """Custom type xcmHrStoragePreviousIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStoragePreviousIndex_Object = MibTableColumn
xcmHrStoragePreviousIndex = _XcmHrStoragePreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 11),
    _XcmHrStoragePreviousIndex_Type()
)
xcmHrStoragePreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStoragePreviousIndex.setStatus("current")


class _XcmHrStoragePhysicalIndex_Type(Cardinal32):
    """Custom type xcmHrStoragePhysicalIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrStoragePhysicalIndex_Object = MibTableColumn
xcmHrStoragePhysicalIndex = _XcmHrStoragePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 12),
    _XcmHrStoragePhysicalIndex_Type()
)
xcmHrStoragePhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStoragePhysicalIndex.setStatus("current")
_XcmHrStorageDetail_ObjectIdentity = ObjectIdentity
xcmHrStorageDetail = _XcmHrStorageDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15)
)
_XcmHrStorageDetailTable_Object = MibTable
xcmHrStorageDetailTable = _XcmHrStorageDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2)
)
if mibBuilder.loadTexts:
    xcmHrStorageDetailTable.setStatus("current")
_XcmHrStorageDetailEntry_Object = MibTableRow
xcmHrStorageDetailEntry = _XcmHrStorageDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1)
)
xcmHrStorageDetailEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrStorageIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailType"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmHrStorageDetailEntry.setStatus("current")
_XcmHrStorageDetailType_Type = XcmHrStorageDetailType
_XcmHrStorageDetailType_Object = MibTableColumn
xcmHrStorageDetailType = _XcmHrStorageDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 1),
    _XcmHrStorageDetailType_Type()
)
xcmHrStorageDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrStorageDetailType.setStatus("current")
_XcmHrStorageDetailIndex_Type = Ordinal32
_XcmHrStorageDetailIndex_Object = MibTableColumn
xcmHrStorageDetailIndex = _XcmHrStorageDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 2),
    _XcmHrStorageDetailIndex_Type()
)
xcmHrStorageDetailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrStorageDetailIndex.setStatus("current")
_XcmHrStorageDetailRowStatus_Type = RowStatus
_XcmHrStorageDetailRowStatus_Object = MibTableColumn
xcmHrStorageDetailRowStatus = _XcmHrStorageDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 3),
    _XcmHrStorageDetailRowStatus_Type()
)
xcmHrStorageDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailRowStatus.setStatus("current")


class _XcmHrStorageDetailUnitClass_Type(XcmHrDevDetailUnitClass):
    """Custom type xcmHrStorageDetailUnitClass based on XcmHrDevDetailUnitClass"""


_XcmHrStorageDetailUnitClass_Object = MibTableColumn
xcmHrStorageDetailUnitClass = _XcmHrStorageDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 4),
    _XcmHrStorageDetailUnitClass_Type()
)
xcmHrStorageDetailUnitClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailUnitClass.setStatus("current")


class _XcmHrStorageDetailUnit_Type(Cardinal32):
    """Custom type xcmHrStorageDetailUnit based on Cardinal32"""
    defaultValue = 0


_XcmHrStorageDetailUnit_Object = MibTableColumn
xcmHrStorageDetailUnit = _XcmHrStorageDetailUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 5),
    _XcmHrStorageDetailUnit_Type()
)
xcmHrStorageDetailUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailUnit.setStatus("current")


class _XcmHrStorageDetailValueInteger_Type(Integer32):
    """Custom type xcmHrStorageDetailValueInteger based on Integer32"""
    defaultValue = 0


_XcmHrStorageDetailValueInteger_Object = MibTableColumn
xcmHrStorageDetailValueInteger = _XcmHrStorageDetailValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 6),
    _XcmHrStorageDetailValueInteger_Type()
)
xcmHrStorageDetailValueInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueInteger.setStatus("current")


class _XcmHrStorageDetailValueOID_Type(ObjectIdentifier):
    """Custom type xcmHrStorageDetailValueOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmHrStorageDetailValueOID_Object = MibTableColumn
xcmHrStorageDetailValueOID = _XcmHrStorageDetailValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 7),
    _XcmHrStorageDetailValueOID_Type()
)
xcmHrStorageDetailValueOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueOID.setStatus("current")


class _XcmHrStorageDetailValueString_Type(OctetString):
    """Custom type xcmHrStorageDetailValueString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrStorageDetailValueString_Type.__name__ = "OctetString"
_XcmHrStorageDetailValueString_Object = MibTableColumn
xcmHrStorageDetailValueString = _XcmHrStorageDetailValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 8),
    _XcmHrStorageDetailValueString_Type()
)
xcmHrStorageDetailValueString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueString.setStatus("current")
_XcmHrDevCover_ObjectIdentity = ObjectIdentity
xcmHrDevCover = _XcmHrDevCover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16)
)
_XcmHrDevCoverTable_Object = MibTable
xcmHrDevCoverTable = _XcmHrDevCoverTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevCoverTable.setStatus("current")
_XcmHrDevCoverEntry_Object = MibTableRow
xcmHrDevCoverEntry = _XcmHrDevCoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1)
)
xcmHrDevCoverEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevCoverEntry.setStatus("current")
_XcmHrDevCoverIndex_Type = Ordinal32
_XcmHrDevCoverIndex_Object = MibTableColumn
xcmHrDevCoverIndex = _XcmHrDevCoverIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 1),
    _XcmHrDevCoverIndex_Type()
)
xcmHrDevCoverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDevCoverIndex.setStatus("current")
_XcmHrDevCoverRowStatus_Type = RowStatus
_XcmHrDevCoverRowStatus_Object = MibTableColumn
xcmHrDevCoverRowStatus = _XcmHrDevCoverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 2),
    _XcmHrDevCoverRowStatus_Type()
)
xcmHrDevCoverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverRowStatus.setStatus("current")


class _XcmHrDevCoverName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevCoverName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevCoverName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevCoverName_Object = MibTableColumn
xcmHrDevCoverName = _XcmHrDevCoverName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 3),
    _XcmHrDevCoverName_Type()
)
xcmHrDevCoverName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverName.setStatus("current")


class _XcmHrDevCoverDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevCoverDescription based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevCoverDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevCoverDescription_Object = MibTableColumn
xcmHrDevCoverDescription = _XcmHrDevCoverDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 4),
    _XcmHrDevCoverDescription_Type()
)
xcmHrDevCoverDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverDescription.setStatus("current")


class _XcmHrDevCoverTypeCover_Type(TruthValue):
    """Custom type xcmHrDevCoverTypeCover based on TruthValue"""


_XcmHrDevCoverTypeCover_Object = MibTableColumn
xcmHrDevCoverTypeCover = _XcmHrDevCoverTypeCover_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 5),
    _XcmHrDevCoverTypeCover_Type()
)
xcmHrDevCoverTypeCover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverTypeCover.setStatus("current")


class _XcmHrDevCoverStatusOpen_Type(TruthValue):
    """Custom type xcmHrDevCoverStatusOpen based on TruthValue"""


_XcmHrDevCoverStatusOpen_Object = MibTableColumn
xcmHrDevCoverStatusOpen = _XcmHrDevCoverStatusOpen_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 6),
    _XcmHrDevCoverStatusOpen_Type()
)
xcmHrDevCoverStatusOpen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverStatusOpen.setStatus("current")
_XcmHrDevAlert_ObjectIdentity = ObjectIdentity
xcmHrDevAlert = _XcmHrDevAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17)
)
_XcmHrDevAlertV1EventOID_ObjectIdentity = ObjectIdentity
xcmHrDevAlertV1EventOID = _XcmHrDevAlertV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 1)
)
if mibBuilder.loadTexts:
    xcmHrDevAlertV1EventOID.setStatus("current")
_XcmHrDevAlertV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmHrDevAlertV2EventPrefix = _XcmHrDevAlertV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 1, 0)
)
_XcmHrDevAlertTable_Object = MibTable
xcmHrDevAlertTable = _XcmHrDevAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevAlertTable.setStatus("current")
_XcmHrDevAlertEntry_Object = MibTableRow
xcmHrDevAlertEntry = _XcmHrDevAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1)
)
xcmHrDevAlertEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevAlertEntry.setStatus("current")
_XcmHrDevAlertIndex_Type = Ordinal32
_XcmHrDevAlertIndex_Object = MibTableColumn
xcmHrDevAlertIndex = _XcmHrDevAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 1),
    _XcmHrDevAlertIndex_Type()
)
xcmHrDevAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDevAlertIndex.setStatus("current")
_XcmHrDevAlertRowStatus_Type = RowStatus
_XcmHrDevAlertRowStatus_Object = MibTableColumn
xcmHrDevAlertRowStatus = _XcmHrDevAlertRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 2),
    _XcmHrDevAlertRowStatus_Type()
)
xcmHrDevAlertRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertRowStatus.setStatus("current")


class _XcmHrDevAlertSeverityLevel_Type(XcmGenNotifySeverityFilter):
    """Custom type xcmHrDevAlertSeverityLevel based on XcmGenNotifySeverityFilter"""
    defaultValue = 0


_XcmHrDevAlertSeverityLevel_Object = MibTableColumn
xcmHrDevAlertSeverityLevel = _XcmHrDevAlertSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 3),
    _XcmHrDevAlertSeverityLevel_Type()
)
xcmHrDevAlertSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertSeverityLevel.setStatus("current")


class _XcmHrDevAlertTrainingLevel_Type(XcmGenNotifyTrainingFilter):
    """Custom type xcmHrDevAlertTrainingLevel based on XcmGenNotifyTrainingFilter"""
    defaultValue = 0


_XcmHrDevAlertTrainingLevel_Object = MibTableColumn
xcmHrDevAlertTrainingLevel = _XcmHrDevAlertTrainingLevel_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 4),
    _XcmHrDevAlertTrainingLevel_Type()
)
xcmHrDevAlertTrainingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertTrainingLevel.setStatus("current")


class _XcmHrDevAlertCodeInteger_Type(Integer32):
    """Custom type xcmHrDevAlertCodeInteger based on Integer32"""
    defaultValue = 0


_XcmHrDevAlertCodeInteger_Object = MibTableColumn
xcmHrDevAlertCodeInteger = _XcmHrDevAlertCodeInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 5),
    _XcmHrDevAlertCodeInteger_Type()
)
xcmHrDevAlertCodeInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertCodeInteger.setStatus("current")


class _XcmHrDevAlertCodeString_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevAlertCodeString based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevAlertCodeString_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevAlertCodeString_Object = MibTableColumn
xcmHrDevAlertCodeString = _XcmHrDevAlertCodeString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 6),
    _XcmHrDevAlertCodeString_Type()
)
xcmHrDevAlertCodeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertCodeString.setStatus("current")


class _XcmHrDevAlertDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevAlertDescription based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevAlertDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevAlertDescription_Object = MibTableColumn
xcmHrDevAlertDescription = _XcmHrDevAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 7),
    _XcmHrDevAlertDescription_Type()
)
xcmHrDevAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertDescription.setStatus("current")


class _XcmHrDevAlertReferenceOID_Type(ObjectIdentifier):
    """Custom type xcmHrDevAlertReferenceOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmHrDevAlertReferenceOID_Object = MibTableColumn
xcmHrDevAlertReferenceOID = _XcmHrDevAlertReferenceOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 8),
    _XcmHrDevAlertReferenceOID_Type()
)
xcmHrDevAlertReferenceOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceOID.setStatus("current")


class _XcmHrDevAlertDateAndTime_Type(DateAndTime):
    """Custom type xcmHrDevAlertDateAndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrDevAlertDateAndTime_Object = MibTableColumn
xcmHrDevAlertDateAndTime = _XcmHrDevAlertDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 9),
    _XcmHrDevAlertDateAndTime_Type()
)
xcmHrDevAlertDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertDateAndTime.setStatus("current")


class _XcmHrDevAlertTitle_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevAlertTitle based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_XcmHrDevAlertTitle_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevAlertTitle_Object = MibTableColumn
xcmHrDevAlertTitle = _XcmHrDevAlertTitle_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 10),
    _XcmHrDevAlertTitle_Type()
)
xcmHrDevAlertTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertTitle.setStatus("current")


class _XcmHrDevAlertHelpReference_Type(OctetString):
    """Custom type xcmHrDevAlertHelpReference based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevAlertHelpReference_Type.__name__ = "OctetString"
_XcmHrDevAlertHelpReference_Object = MibTableColumn
xcmHrDevAlertHelpReference = _XcmHrDevAlertHelpReference_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 11),
    _XcmHrDevAlertHelpReference_Type()
)
xcmHrDevAlertHelpReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertHelpReference.setStatus("current")


class _XcmHrDevAlertReferenceIndex_Type(Integer32):
    """Custom type xcmHrDevAlertReferenceIndex based on Integer32"""
    defaultValue = -1


_XcmHrDevAlertReferenceIndex_Object = MibTableColumn
xcmHrDevAlertReferenceIndex = _XcmHrDevAlertReferenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 12),
    _XcmHrDevAlertReferenceIndex_Type()
)
xcmHrDevAlertReferenceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceIndex.setStatus("current")


class _XcmHrDevAlertReferenceLocation_Type(Integer32):
    """Custom type xcmHrDevAlertReferenceLocation based on Integer32"""
    defaultValue = -2


_XcmHrDevAlertReferenceLocation_Object = MibTableColumn
xcmHrDevAlertReferenceLocation = _XcmHrDevAlertReferenceLocation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 13),
    _XcmHrDevAlertReferenceLocation_Type()
)
xcmHrDevAlertReferenceLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceLocation.setStatus("current")


class _XcmHrDevAlertDevAlertIndex_Type(Integer32):
    """Custom type xcmHrDevAlertDevAlertIndex based on Integer32"""
    defaultValue = 0


_XcmHrDevAlertDevAlertIndex_Object = MibTableColumn
xcmHrDevAlertDevAlertIndex = _XcmHrDevAlertDevAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 14),
    _XcmHrDevAlertDevAlertIndex_Type()
)
xcmHrDevAlertDevAlertIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertDevAlertIndex.setStatus("current")


class _XcmHrDevAlertPriority_Type(Integer32):
    """Custom type xcmHrDevAlertPriority based on Integer32"""
    defaultValue = 0


_XcmHrDevAlertPriority_Object = MibTableColumn
xcmHrDevAlertPriority = _XcmHrDevAlertPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 15),
    _XcmHrDevAlertPriority_Type()
)
xcmHrDevAlertPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertPriority.setStatus("current")
_XcmHrDevAlertLastAlertIndex_Type = Cardinal32
_XcmHrDevAlertLastAlertIndex_Object = MibScalar
xcmHrDevAlertLastAlertIndex = _XcmHrDevAlertLastAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 3),
    _XcmHrDevAlertLastAlertIndex_Type()
)
xcmHrDevAlertLastAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertLastAlertIndex.setStatus("current")
_XcmHrDevAlertLastCriticalAlertIndex_Type = Cardinal32
_XcmHrDevAlertLastCriticalAlertIndex_Object = MibScalar
xcmHrDevAlertLastCriticalAlertIndex = _XcmHrDevAlertLastCriticalAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 4),
    _XcmHrDevAlertLastCriticalAlertIndex_Type()
)
xcmHrDevAlertLastCriticalAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertLastCriticalAlertIndex.setStatus("current")
_XcmHrConsoleScreen_ObjectIdentity = ObjectIdentity
xcmHrConsoleScreen = _XcmHrConsoleScreen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18)
)
_XcmHrConsoleScreenTable_Object = MibTable
xcmHrConsoleScreenTable = _XcmHrConsoleScreenTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2)
)
if mibBuilder.loadTexts:
    xcmHrConsoleScreenTable.setStatus("current")
_XcmHrConsoleScreenEntry_Object = MibTableRow
xcmHrConsoleScreenEntry = _XcmHrConsoleScreenEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1)
)
xcmHrConsoleScreenEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenIndex"),
)
if mibBuilder.loadTexts:
    xcmHrConsoleScreenEntry.setStatus("current")
_XcmHrConsoleScreenIndex_Type = Ordinal32
_XcmHrConsoleScreenIndex_Object = MibTableColumn
xcmHrConsoleScreenIndex = _XcmHrConsoleScreenIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 1),
    _XcmHrConsoleScreenIndex_Type()
)
xcmHrConsoleScreenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenIndex.setStatus("current")


class _XcmHrConsoleScreenName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrConsoleScreenName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrConsoleScreenName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrConsoleScreenName_Object = MibTableColumn
xcmHrConsoleScreenName = _XcmHrConsoleScreenName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 2),
    _XcmHrConsoleScreenName_Type()
)
xcmHrConsoleScreenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenName.setStatus("current")


class _XcmHrConsoleScreenDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrConsoleScreenDescription based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrConsoleScreenDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrConsoleScreenDescription_Object = MibTableColumn
xcmHrConsoleScreenDescription = _XcmHrConsoleScreenDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 3),
    _XcmHrConsoleScreenDescription_Type()
)
xcmHrConsoleScreenDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenDescription.setStatus("current")


class _XcmHrConsoleScreenParentIndex_Type(Cardinal32):
    """Custom type xcmHrConsoleScreenParentIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrConsoleScreenParentIndex_Object = MibTableColumn
xcmHrConsoleScreenParentIndex = _XcmHrConsoleScreenParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 4),
    _XcmHrConsoleScreenParentIndex_Type()
)
xcmHrConsoleScreenParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenParentIndex.setStatus("current")


class _XcmHrConsoleScreenPriority_Type(Integer32):
    """Custom type xcmHrConsoleScreenPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmHrConsoleScreenPriority_Type.__name__ = "Integer32"
_XcmHrConsoleScreenPriority_Object = MibTableColumn
xcmHrConsoleScreenPriority = _XcmHrConsoleScreenPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 5),
    _XcmHrConsoleScreenPriority_Type()
)
xcmHrConsoleScreenPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenPriority.setStatus("current")


class _XcmHrConsoleScreenTabCount_Type(Cardinal32):
    """Custom type xcmHrConsoleScreenTabCount based on Cardinal32"""
    defaultValue = 0


_XcmHrConsoleScreenTabCount_Object = MibTableColumn
xcmHrConsoleScreenTabCount = _XcmHrConsoleScreenTabCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 6),
    _XcmHrConsoleScreenTabCount_Type()
)
xcmHrConsoleScreenTabCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenTabCount.setStatus("current")
_XcmHrConsoleTab_ObjectIdentity = ObjectIdentity
xcmHrConsoleTab = _XcmHrConsoleTab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19)
)
_XcmHrConsoleTabTable_Object = MibTable
xcmHrConsoleTabTable = _XcmHrConsoleTabTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2)
)
if mibBuilder.loadTexts:
    xcmHrConsoleTabTable.setStatus("current")
_XcmHrConsoleTabEntry_Object = MibTableRow
xcmHrConsoleTabEntry = _XcmHrConsoleTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1)
)
xcmHrConsoleTabEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabIndex"),
)
if mibBuilder.loadTexts:
    xcmHrConsoleTabEntry.setStatus("current")
_XcmHrConsoleTabIndex_Type = Ordinal32
_XcmHrConsoleTabIndex_Object = MibTableColumn
xcmHrConsoleTabIndex = _XcmHrConsoleTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 1),
    _XcmHrConsoleTabIndex_Type()
)
xcmHrConsoleTabIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrConsoleTabIndex.setStatus("current")


class _XcmHrConsoleTabName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrConsoleTabName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrConsoleTabName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrConsoleTabName_Object = MibTableColumn
xcmHrConsoleTabName = _XcmHrConsoleTabName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 2),
    _XcmHrConsoleTabName_Type()
)
xcmHrConsoleTabName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleTabName.setStatus("current")


class _XcmHrConsoleTabDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrConsoleTabDescription based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrConsoleTabDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrConsoleTabDescription_Object = MibTableColumn
xcmHrConsoleTabDescription = _XcmHrConsoleTabDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 3),
    _XcmHrConsoleTabDescription_Type()
)
xcmHrConsoleTabDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleTabDescription.setStatus("current")


class _XcmHrConsoleTabScreenIndex_Type(Cardinal32):
    """Custom type xcmHrConsoleTabScreenIndex based on Cardinal32"""
    defaultValue = 0


_XcmHrConsoleTabScreenIndex_Object = MibTableColumn
xcmHrConsoleTabScreenIndex = _XcmHrConsoleTabScreenIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 4),
    _XcmHrConsoleTabScreenIndex_Type()
)
xcmHrConsoleTabScreenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleTabScreenIndex.setStatus("current")


class _XcmHrConsoleTabPriority_Type(Integer32):
    """Custom type xcmHrConsoleTabPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmHrConsoleTabPriority_Type.__name__ = "Integer32"
_XcmHrConsoleTabPriority_Object = MibTableColumn
xcmHrConsoleTabPriority = _XcmHrConsoleTabPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 5),
    _XcmHrConsoleTabPriority_Type()
)
xcmHrConsoleTabPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrConsoleTabPriority.setStatus("current")
_XcmHrSupplies_ObjectIdentity = ObjectIdentity
xcmHrSupplies = _XcmHrSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20)
)
_XcmHrSuppliesTable_Object = MibTable
xcmHrSuppliesTable = _XcmHrSuppliesTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1)
)
if mibBuilder.loadTexts:
    xcmHrSuppliesTable.setStatus("current")
_XcmHrSuppliesEntry_Object = MibTableRow
xcmHrSuppliesEntry = _XcmHrSuppliesEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1)
)
xcmHrSuppliesEntry.setIndexNames(
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesIndex"),
)
if mibBuilder.loadTexts:
    xcmHrSuppliesEntry.setStatus("current")


class _XcmHrSuppliesIndex_Type(Ordinal32):
    """Custom type xcmHrSuppliesIndex based on Ordinal32"""
    subtypeSpec = Ordinal32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XcmHrSuppliesIndex_Type.__name__ = "Ordinal32"
_XcmHrSuppliesIndex_Object = MibTableColumn
xcmHrSuppliesIndex = _XcmHrSuppliesIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 1),
    _XcmHrSuppliesIndex_Type()
)
xcmHrSuppliesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrSuppliesIndex.setStatus("current")
_XcmHrSuppliesReferenceOID_Type = ObjectIdentifier
_XcmHrSuppliesReferenceOID_Object = MibTableColumn
xcmHrSuppliesReferenceOID = _XcmHrSuppliesReferenceOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 2),
    _XcmHrSuppliesReferenceOID_Type()
)
xcmHrSuppliesReferenceOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesReferenceOID.setStatus("current")
_XcmHrSuppliesType_Type = AutonomousType
_XcmHrSuppliesType_Object = MibTableColumn
xcmHrSuppliesType = _XcmHrSuppliesType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 3),
    _XcmHrSuppliesType_Type()
)
xcmHrSuppliesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesType.setStatus("current")
_XcmHrSuppliesClass_Type = XcmHrSuppliesClassTC
_XcmHrSuppliesClass_Object = MibTableColumn
xcmHrSuppliesClass = _XcmHrSuppliesClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 4),
    _XcmHrSuppliesClass_Type()
)
xcmHrSuppliesClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesClass.setStatus("current")
_XcmHrSuppliesDescr_Type = OctetString
_XcmHrSuppliesDescr_Object = MibTableColumn
xcmHrSuppliesDescr = _XcmHrSuppliesDescr_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 5),
    _XcmHrSuppliesDescr_Type()
)
xcmHrSuppliesDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesDescr.setStatus("current")
_XcmHrSuppliesPartNumber_Type = OctetString
_XcmHrSuppliesPartNumber_Object = MibTableColumn
xcmHrSuppliesPartNumber = _XcmHrSuppliesPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 6),
    _XcmHrSuppliesPartNumber_Type()
)
xcmHrSuppliesPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesPartNumber.setStatus("current")
_XcmHrDetailTable_Object = MibTable
xcmHrDetailTable = _XcmHrDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2)
)
if mibBuilder.loadTexts:
    xcmHrDetailTable.setStatus("current")
_XcmHrDetailEntry_Object = MibTableRow
xcmHrDetailEntry = _XcmHrDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1)
)
xcmHrDetailEntry.setIndexNames(
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailTableRef"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailTableIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailType"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDetailEntry.setStatus("current")
_XcmHrDetailTableRef_Type = XcmHrDetailTableEnumTC
_XcmHrDetailTableRef_Object = MibTableColumn
xcmHrDetailTableRef = _XcmHrDetailTableRef_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 1),
    _XcmHrDetailTableRef_Type()
)
xcmHrDetailTableRef.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDetailTableRef.setStatus("current")
_XcmHrDetailTableIndex_Type = ObjectIdentifier
_XcmHrDetailTableIndex_Object = MibTableColumn
xcmHrDetailTableIndex = _XcmHrDetailTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 2),
    _XcmHrDetailTableIndex_Type()
)
xcmHrDetailTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDetailTableIndex.setStatus("current")
_XcmHrDetailType_Type = XcmHrDevDetailType
_XcmHrDetailType_Object = MibTableColumn
xcmHrDetailType = _XcmHrDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 3),
    _XcmHrDetailType_Type()
)
xcmHrDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDetailType.setStatus("current")
_XcmHrDetailIndex_Type = Ordinal32
_XcmHrDetailIndex_Object = MibTableColumn
xcmHrDetailIndex = _XcmHrDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 4),
    _XcmHrDetailIndex_Type()
)
xcmHrDetailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDetailIndex.setStatus("current")


class _XcmHrDetailUnitClass_Type(XcmHrDevDetailUnitClass):
    """Custom type xcmHrDetailUnitClass based on XcmHrDevDetailUnitClass"""


_XcmHrDetailUnitClass_Object = MibTableColumn
xcmHrDetailUnitClass = _XcmHrDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 5),
    _XcmHrDetailUnitClass_Type()
)
xcmHrDetailUnitClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDetailUnitClass.setStatus("current")


class _XcmHrDetailUnit_Type(Cardinal32):
    """Custom type xcmHrDetailUnit based on Cardinal32"""
    defaultValue = 0


_XcmHrDetailUnit_Object = MibTableColumn
xcmHrDetailUnit = _XcmHrDetailUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 6),
    _XcmHrDetailUnit_Type()
)
xcmHrDetailUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailUnit.setStatus("current")
_XcmHrDetailValueInteger_Type = Integer32
_XcmHrDetailValueInteger_Object = MibTableColumn
xcmHrDetailValueInteger = _XcmHrDetailValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 7),
    _XcmHrDetailValueInteger_Type()
)
xcmHrDetailValueInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailValueInteger.setStatus("current")
_XcmHrDetailValueOID_Type = ObjectIdentifier
_XcmHrDetailValueOID_Object = MibTableColumn
xcmHrDetailValueOID = _XcmHrDetailValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 8),
    _XcmHrDetailValueOID_Type()
)
xcmHrDetailValueOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailValueOID.setStatus("current")
_XcmHrDetailValueString_Type = OctetString
_XcmHrDetailValueString_Object = MibTableColumn
xcmHrDetailValueString = _XcmHrDetailValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 9),
    _XcmHrDetailValueString_Type()
)
xcmHrDetailValueString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailValueString.setStatus("current")


class _XcmHrDetailDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDetailDescription based on XcmFixedLocaleDisplayString"""
    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDetailDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDetailDescription_Object = MibTableColumn
xcmHrDetailDescription = _XcmHrDetailDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 10),
    _XcmHrDetailDescription_Type()
)
xcmHrDetailDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailDescription.setStatus("current")
_XcmHrConsole_ObjectIdentity = ObjectIdentity
xcmHrConsole = _XcmHrConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21)
)
_XcmHrConsoleTable_Object = MibTable
xcmHrConsoleTable = _XcmHrConsoleTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2)
)
if mibBuilder.loadTexts:
    xcmHrConsoleTable.setStatus("current")
_XcmHrConsoleEntry_Object = MibTableRow
xcmHrConsoleEntry = _XcmHrConsoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1)
)
xcmHrConsoleEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleIndex"),
)
if mibBuilder.loadTexts:
    xcmHrConsoleEntry.setStatus("current")
_XcmHrConsoleIndex_Type = Ordinal32
_XcmHrConsoleIndex_Object = MibTableColumn
xcmHrConsoleIndex = _XcmHrConsoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 1),
    _XcmHrConsoleIndex_Type()
)
xcmHrConsoleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrConsoleIndex.setStatus("current")


class _XcmHrConsoleDefaultService_Type(XcmHrConsoleDefaultService):
    """Custom type xcmHrConsoleDefaultService based on XcmHrConsoleDefaultService"""


_XcmHrConsoleDefaultService_Object = MibTableColumn
xcmHrConsoleDefaultService = _XcmHrConsoleDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 2),
    _XcmHrConsoleDefaultService_Type()
)
xcmHrConsoleDefaultService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleDefaultService.setStatus("current")


class _XcmHrConsoleBrightness_Type(Integer32):
    """Custom type xcmHrConsoleBrightness based on Integer32"""
    defaultValue = 5


_XcmHrConsoleBrightness_Object = MibTableColumn
xcmHrConsoleBrightness = _XcmHrConsoleBrightness_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 3),
    _XcmHrConsoleBrightness_Type()
)
xcmHrConsoleBrightness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleBrightness.setStatus("current")


class _XcmHrConsoleContrast_Type(Integer32):
    """Custom type xcmHrConsoleContrast based on Integer32"""
    defaultValue = 5


_XcmHrConsoleContrast_Object = MibTableColumn
xcmHrConsoleContrast = _XcmHrConsoleContrast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 4),
    _XcmHrConsoleContrast_Type()
)
xcmHrConsoleContrast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleContrast.setStatus("current")


class _XcmHrConsoleAccessibility_Type(TruthValue):
    """Custom type xcmHrConsoleAccessibility based on TruthValue"""


_XcmHrConsoleAccessibility_Object = MibTableColumn
xcmHrConsoleAccessibility = _XcmHrConsoleAccessibility_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 5),
    _XcmHrConsoleAccessibility_Type()
)
xcmHrConsoleAccessibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleAccessibility.setStatus("current")


class _XcmHrConsoleAutoClearTime_Type(Integer32):
    """Custom type xcmHrConsoleAutoClearTime based on Integer32"""
    defaultValue = 60


_XcmHrConsoleAutoClearTime_Object = MibTableColumn
xcmHrConsoleAutoClearTime = _XcmHrConsoleAutoClearTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 6),
    _XcmHrConsoleAutoClearTime_Type()
)
xcmHrConsoleAutoClearTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleAutoClearTime.setStatus("current")


class _XcmHrConsoleInsertTimeout_Type(Integer32):
    """Custom type xcmHrConsoleInsertTimeout based on Integer32"""
    defaultValue = 60


_XcmHrConsoleInsertTimeout_Object = MibTableColumn
xcmHrConsoleInsertTimeout = _XcmHrConsoleInsertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 7),
    _XcmHrConsoleInsertTimeout_Type()
)
xcmHrConsoleInsertTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleInsertTimeout.setStatus("current")


class _XcmHrConsoleTray1Timeout_Type(Integer32):
    """Custom type xcmHrConsoleTray1Timeout based on Integer32"""
    defaultValue = 60


_XcmHrConsoleTray1Timeout_Object = MibTableColumn
xcmHrConsoleTray1Timeout = _XcmHrConsoleTray1Timeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 8),
    _XcmHrConsoleTray1Timeout_Type()
)
xcmHrConsoleTray1Timeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleTray1Timeout.setStatus("current")


class _XcmHrConsoleTray2nTimeout_Type(Integer32):
    """Custom type xcmHrConsoleTray2nTimeout based on Integer32"""
    defaultValue = 60


_XcmHrConsoleTray2nTimeout_Object = MibTableColumn
xcmHrConsoleTray2nTimeout = _XcmHrConsoleTray2nTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 9),
    _XcmHrConsoleTray2nTimeout_Type()
)
xcmHrConsoleTray2nTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleTray2nTimeout.setStatus("current")


class _XcmHrConsoleLoadTimeout_Type(Integer32):
    """Custom type xcmHrConsoleLoadTimeout based on Integer32"""
    defaultValue = 60


_XcmHrConsoleLoadTimeout_Object = MibTableColumn
xcmHrConsoleLoadTimeout = _XcmHrConsoleLoadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 10),
    _XcmHrConsoleLoadTimeout_Type()
)
xcmHrConsoleLoadTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleLoadTimeout.setStatus("current")


class _XcmHrConsoleSoundVolume_Type(Integer32):
    """Custom type xcmHrConsoleSoundVolume based on Integer32"""
    defaultValue = 2


_XcmHrConsoleSoundVolume_Object = MibTableColumn
xcmHrConsoleSoundVolume = _XcmHrConsoleSoundVolume_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 11),
    _XcmHrConsoleSoundVolume_Type()
)
xcmHrConsoleSoundVolume.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleSoundVolume.setStatus("current")


class _XcmHrConsoleSoundDuration_Type(Integer32):
    """Custom type xcmHrConsoleSoundDuration based on Integer32"""
    defaultValue = 15


_XcmHrConsoleSoundDuration_Object = MibTableColumn
xcmHrConsoleSoundDuration = _XcmHrConsoleSoundDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 12),
    _XcmHrConsoleSoundDuration_Type()
)
xcmHrConsoleSoundDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleSoundDuration.setStatus("current")
_XcmHrGenericParamGroup_ObjectIdentity = ObjectIdentity
xcmHrGenericParamGroup = _XcmHrGenericParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 22)
)


class _XcmHrGenericParamName_Type(OctetString):
    """Custom type xcmHrGenericParamName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrGenericParamName_Type.__name__ = "OctetString"
_XcmHrGenericParamName_Object = MibScalar
xcmHrGenericParamName = _XcmHrGenericParamName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 22, 1),
    _XcmHrGenericParamName_Type()
)
xcmHrGenericParamName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrGenericParamName.setStatus("current")


class _XcmHrGenericParamValue_Type(OctetString):
    """Custom type xcmHrGenericParamValue based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrGenericParamValue_Type.__name__ = "OctetString"
_XcmHrGenericParamValue_Object = MibScalar
xcmHrGenericParamValue = _XcmHrGenericParamValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 22, 2),
    _XcmHrGenericParamValue_Type()
)
xcmHrGenericParamValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrGenericParamValue.setStatus("current")

# Managed Objects groups

xcmHrDevInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 3)
)
xcmHrDevInfoGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoSerialNumber"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoRealization"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoInstallDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoResetDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoNextDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoPreviousDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoPhysicalDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoPriority"))
)
if mibBuilder.loadTexts:
    xcmHrDevInfoGroup.setStatus("current")

xcmHrDevHelpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 4)
)
xcmHrDevHelpGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevHelpRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevHelpOperatorMessage"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevHelpProblemMessage"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevHelpCommsAddressIndex"))
)
if mibBuilder.loadTexts:
    xcmHrDevHelpGroup.setStatus("current")

xcmHrDevMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 5)
)
xcmHrDevMgmtGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandRequest"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandData"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtUserPassword"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtOperatorPassword"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtAdminPassword"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandInProgress"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtUserName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtOperatorName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtAdminName"))
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtGroup.setStatus("current")

xcmHrDevPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 6)
)
xcmHrDevPowerGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWarmUpSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerCoolDownSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerEnergySaveSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerTimeUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWarmUpDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWarmUpDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerCoolDownDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerCoolDownDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerEnergySaveDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerEnergySaveDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWakeUpSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWakeUpDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWakeUpDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerShutdownDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerShutdownDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerStartupDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerStartupDuration"))
)
if mibBuilder.loadTexts:
    xcmHrDevPowerGroup.setStatus("current")

xcmHrDevTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 7)
)
xcmHrDevTrafficGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputCount"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputCount"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputMaxSize"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputMaxSize"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputTimeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputTimeout"))
)
if mibBuilder.loadTexts:
    xcmHrDevTrafficGroup.setStatus("current")

xcmHrSystemFaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 8)
)
xcmHrSystemFaultGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultCode"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultString"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultReferenceOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultHrDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultDate"))
)
if mibBuilder.loadTexts:
    xcmHrSystemFaultGroup.setStatus("current")

xcmHrGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 9)
)
xcmHrGeneralGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralVersionID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralVersionDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralGroupSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralStorageLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralDeviceLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralFSLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralSWRunLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralSWInstalledLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralSystemFaultLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralCreateSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmHrGeneralGroup.setStatus("current")

xcmHrDevCalendarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 10)
)
xcmHrDevCalendarGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarExplicitDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarCommandRequest"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarCommandData"))
)
if mibBuilder.loadTexts:
    xcmHrDevCalendarGroup.setStatus("current")

xcmHrSWRunGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 11)
)
xcmHrSWRunGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunAdminName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunRowCreateDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunPhysicalDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunLogicalDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunNextIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunPreviousIndex"))
)
if mibBuilder.loadTexts:
    xcmHrSWRunGroup.setStatus("current")

xcmHrSWInstalledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 12)
)
xcmHrSWInstalledGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledAdminName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledRowCreateDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledPhysicalIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledLogicalIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledNextIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledPreviousIndex"))
)
if mibBuilder.loadTexts:
    xcmHrSWInstalledGroup.setStatus("current")

xcmHrDevDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 13)
)
xcmHrDevDetailGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailType"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailUnitClass"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailValueInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailValueOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailValueString"))
)
if mibBuilder.loadTexts:
    xcmHrDevDetailGroup.setStatus("current")

xcmHrStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 14)
)
xcmHrStorageGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageRealization"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageProductDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStoragePlatformDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStoragePagingDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageMatchingDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageSWRunIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageSWInstalledIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageNextIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStoragePreviousIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStoragePhysicalIndex"))
)
if mibBuilder.loadTexts:
    xcmHrStorageGroup.setStatus("current")

xcmHrStorageDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 15)
)
xcmHrStorageDetailGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailUnitClass"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailValueInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailValueOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailValueString"))
)
if mibBuilder.loadTexts:
    xcmHrStorageDetailGroup.setStatus("current")

xcmHrDevCoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 16)
)
xcmHrDevCoverGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverDescription"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverTypeCover"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverStatusOpen"))
)
if mibBuilder.loadTexts:
    xcmHrDevCoverGroup.setStatus("current")

xcmHrDevAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 17)
)
xcmHrDevAlertGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertSeverityLevel"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertTrainingLevel"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertCodeInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertCodeString"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertDescription"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertReferenceOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertDateAndTime"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertTitle"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertHelpReference"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertReferenceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertReferenceLocation"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertDevAlertIndex"))
)
if mibBuilder.loadTexts:
    xcmHrDevAlertGroup.setStatus("current")

xcmHrConsoleScreenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 18)
)
xcmHrConsoleScreenGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenDescription"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenParentIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenPriority"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenTabCount"))
)
if mibBuilder.loadTexts:
    xcmHrConsoleScreenGroup.setStatus("current")

xcmHrConsoleTabGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 19)
)
xcmHrConsoleTabGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabDescription"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabScreenIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabPriority"))
)
if mibBuilder.loadTexts:
    xcmHrConsoleTabGroup.setStatus("current")

xcmHrSuppliesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 20)
)
xcmHrSuppliesGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesReferenceOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesType"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesClass"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesDescr"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesPartNumber"))
)
if mibBuilder.loadTexts:
    xcmHrSuppliesGroup.setStatus("current")

xcmHrDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 21)
)
xcmHrDetailGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailUnitClass"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailValueInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailValueOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailValueString"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailDescription"))
)
if mibBuilder.loadTexts:
    xcmHrDetailGroup.setStatus("current")

xcmHrConsoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 22)
)
xcmHrConsoleGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleDefaultService"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleBrightness"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleContrast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleAccessibility"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleAutoClearTime"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleInsertTimeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTray1Timeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTray2nTimeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleLoadTimeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleSoundVolume"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleSoundDuration"))
)
if mibBuilder.loadTexts:
    xcmHrConsoleGroup.setStatus("current")


# Notification objects

xcmHrDevInfoV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 1, 0, 1)
)
xcmHrDevInfoV2Event.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("HOST-RESOURCES-MIB", "hrDeviceStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXConditions"))
)
if mibBuilder.loadTexts:
    xcmHrDevInfoV2Event.setStatus(
        "current"
    )

xcmHrDevMgmtV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 1, 0, 1)
)
xcmHrDevMgmtV2Event.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("HOST-RESOURCES-MIB", "hrDeviceStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandRequest"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandStatus"))
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtV2Event.setStatus(
        "current"
    )

xcmHrDevDetailV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 1, 0, 1)
)
xcmHrDevDetailV2Event.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailType"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailIndex"))
)
if mibBuilder.loadTexts:
    xcmHrDevDetailV2Event.setStatus(
        "current"
    )

xcmHrDevAlertV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 1, 0, 1)
)
xcmHrDevAlertV2Event.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertSeverityLevel"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertTrainingLevel"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertCodeInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertCodeString"))
)
if mibBuilder.loadTexts:
    xcmHrDevAlertV2Event.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

xcmHrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 3)
)
if mibBuilder.loadTexts:
    xcmHrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-HOST-RESOURCES-EXT-MIB",
    **{"xcmHrZeroDummy": xcmHrZeroDummy,
       "xcmHrMIB": xcmHrMIB,
       "xcmHrMIBConformance": xcmHrMIBConformance,
       "xcmHrMIBGroups": xcmHrMIBGroups,
       "xcmHrDevInfoGroup": xcmHrDevInfoGroup,
       "xcmHrDevHelpGroup": xcmHrDevHelpGroup,
       "xcmHrDevMgmtGroup": xcmHrDevMgmtGroup,
       "xcmHrDevPowerGroup": xcmHrDevPowerGroup,
       "xcmHrDevTrafficGroup": xcmHrDevTrafficGroup,
       "xcmHrSystemFaultGroup": xcmHrSystemFaultGroup,
       "xcmHrGeneralGroup": xcmHrGeneralGroup,
       "xcmHrDevCalendarGroup": xcmHrDevCalendarGroup,
       "xcmHrSWRunGroup": xcmHrSWRunGroup,
       "xcmHrSWInstalledGroup": xcmHrSWInstalledGroup,
       "xcmHrDevDetailGroup": xcmHrDevDetailGroup,
       "xcmHrStorageGroup": xcmHrStorageGroup,
       "xcmHrStorageDetailGroup": xcmHrStorageDetailGroup,
       "xcmHrDevCoverGroup": xcmHrDevCoverGroup,
       "xcmHrDevAlertGroup": xcmHrDevAlertGroup,
       "xcmHrConsoleScreenGroup": xcmHrConsoleScreenGroup,
       "xcmHrConsoleTabGroup": xcmHrConsoleTabGroup,
       "xcmHrSuppliesGroup": xcmHrSuppliesGroup,
       "xcmHrDetailGroup": xcmHrDetailGroup,
       "xcmHrConsoleGroup": xcmHrConsoleGroup,
       "xcmHrMIBCompliance": xcmHrMIBCompliance,
       "xcmHrDevInfo": xcmHrDevInfo,
       "xcmHrDevInfoV1EventOID": xcmHrDevInfoV1EventOID,
       "xcmHrDevInfoV2EventPrefix": xcmHrDevInfoV2EventPrefix,
       "xcmHrDevInfoV2Event": xcmHrDevInfoV2Event,
       "xcmHrDevInfoTable": xcmHrDevInfoTable,
       "xcmHrDevInfoEntry": xcmHrDevInfoEntry,
       "xcmHrDevInfoRowStatus": xcmHrDevInfoRowStatus,
       "xcmHrDevInfoName": xcmHrDevInfoName,
       "xcmHrDevInfoSerialNumber": xcmHrDevInfoSerialNumber,
       "xcmHrDevInfoRealization": xcmHrDevInfoRealization,
       "xcmHrDevInfoXStatus": xcmHrDevInfoXStatus,
       "xcmHrDevInfoConditions": xcmHrDevInfoConditions,
       "xcmHrDevInfoXConditions": xcmHrDevInfoXConditions,
       "xcmHrDevInfoInstallDate": xcmHrDevInfoInstallDate,
       "xcmHrDevInfoResetDate": xcmHrDevInfoResetDate,
       "xcmHrDevInfoNextDeviceIndex": xcmHrDevInfoNextDeviceIndex,
       "xcmHrDevInfoPreviousDeviceIndex": xcmHrDevInfoPreviousDeviceIndex,
       "xcmHrDevInfoPhysicalDeviceIndex": xcmHrDevInfoPhysicalDeviceIndex,
       "xcmHrDevInfoPriority": xcmHrDevInfoPriority,
       "xcmHrDevInfoXeroxAssetTagNumber": xcmHrDevInfoXeroxAssetTagNumber,
       "xcmHrDevInfoCustomerAssetNumber": xcmHrDevInfoCustomerAssetNumber,
       "xcmHrDevInfoPagePackPIN": xcmHrDevInfoPagePackPIN,
       "xcmHrDevInfoPagePackReset": xcmHrDevInfoPagePackReset,
       "xcmHrDevInfoPagePackTimer": xcmHrDevInfoPagePackTimer,
       "xcmHrDevHelp": xcmHrDevHelp,
       "xcmHrDevHelpTable": xcmHrDevHelpTable,
       "xcmHrDevHelpEntry": xcmHrDevHelpEntry,
       "xcmHrDevHelpRowStatus": xcmHrDevHelpRowStatus,
       "xcmHrDevHelpOperatorMessage": xcmHrDevHelpOperatorMessage,
       "xcmHrDevHelpProblemMessage": xcmHrDevHelpProblemMessage,
       "xcmHrDevHelpCommsAddressIndex": xcmHrDevHelpCommsAddressIndex,
       "xcmHrDevMgmt": xcmHrDevMgmt,
       "xcmHrDevMgmtV1EventOID": xcmHrDevMgmtV1EventOID,
       "xcmHrDevMgmtV2EventPrefix": xcmHrDevMgmtV2EventPrefix,
       "xcmHrDevMgmtV2Event": xcmHrDevMgmtV2Event,
       "xcmHrDevMgmtTable": xcmHrDevMgmtTable,
       "xcmHrDevMgmtEntry": xcmHrDevMgmtEntry,
       "xcmHrDevMgmtRowStatus": xcmHrDevMgmtRowStatus,
       "xcmHrDevMgmtCommandRequest": xcmHrDevMgmtCommandRequest,
       "xcmHrDevMgmtCommandData": xcmHrDevMgmtCommandData,
       "xcmHrDevMgmtCommandStatus": xcmHrDevMgmtCommandStatus,
       "xcmHrDevMgmtUserPassword": xcmHrDevMgmtUserPassword,
       "xcmHrDevMgmtOperatorPassword": xcmHrDevMgmtOperatorPassword,
       "xcmHrDevMgmtAdminPassword": xcmHrDevMgmtAdminPassword,
       "xcmHrDevMgmtCommandInProgress": xcmHrDevMgmtCommandInProgress,
       "xcmHrDevMgmtUserName": xcmHrDevMgmtUserName,
       "xcmHrDevMgmtOperatorName": xcmHrDevMgmtOperatorName,
       "xcmHrDevMgmtAdminName": xcmHrDevMgmtAdminName,
       "xcmHrDevMgmtCustomPassword": xcmHrDevMgmtCustomPassword,
       "xcmHrDevPower": xcmHrDevPower,
       "xcmHrDevPowerTable": xcmHrDevPowerTable,
       "xcmHrDevPowerEntry": xcmHrDevPowerEntry,
       "xcmHrDevPowerRowStatus": xcmHrDevPowerRowStatus,
       "xcmHrDevPowerWarmUpSupport": xcmHrDevPowerWarmUpSupport,
       "xcmHrDevPowerCoolDownSupport": xcmHrDevPowerCoolDownSupport,
       "xcmHrDevPowerEnergySaveSupport": xcmHrDevPowerEnergySaveSupport,
       "xcmHrDevPowerTimeUnit": xcmHrDevPowerTimeUnit,
       "xcmHrDevPowerWarmUpDelay": xcmHrDevPowerWarmUpDelay,
       "xcmHrDevPowerWarmUpDuration": xcmHrDevPowerWarmUpDuration,
       "xcmHrDevPowerCoolDownDelay": xcmHrDevPowerCoolDownDelay,
       "xcmHrDevPowerCoolDownDuration": xcmHrDevPowerCoolDownDuration,
       "xcmHrDevPowerEnergySaveDelay": xcmHrDevPowerEnergySaveDelay,
       "xcmHrDevPowerEnergySaveDuration": xcmHrDevPowerEnergySaveDuration,
       "xcmHrDevPowerWakeUpSupport": xcmHrDevPowerWakeUpSupport,
       "xcmHrDevPowerWakeUpDelay": xcmHrDevPowerWakeUpDelay,
       "xcmHrDevPowerWakeUpDuration": xcmHrDevPowerWakeUpDuration,
       "xcmHrDevPowerShutdownDelay": xcmHrDevPowerShutdownDelay,
       "xcmHrDevPowerShutdownDuration": xcmHrDevPowerShutdownDuration,
       "xcmHrDevPowerStartupDelay": xcmHrDevPowerStartupDelay,
       "xcmHrDevPowerStartupDuration": xcmHrDevPowerStartupDuration,
       "xcmHrDevTraffic": xcmHrDevTraffic,
       "xcmHrDevTrafficTable": xcmHrDevTrafficTable,
       "xcmHrDevTrafficEntry": xcmHrDevTrafficEntry,
       "xcmHrDevTrafficRowStatus": xcmHrDevTrafficRowStatus,
       "xcmHrDevTrafficInputSupport": xcmHrDevTrafficInputSupport,
       "xcmHrDevTrafficOutputSupport": xcmHrDevTrafficOutputSupport,
       "xcmHrDevTrafficInputUnit": xcmHrDevTrafficInputUnit,
       "xcmHrDevTrafficOutputUnit": xcmHrDevTrafficOutputUnit,
       "xcmHrDevTrafficInputCount": xcmHrDevTrafficInputCount,
       "xcmHrDevTrafficOutputCount": xcmHrDevTrafficOutputCount,
       "xcmHrDevTrafficInputMaxSize": xcmHrDevTrafficInputMaxSize,
       "xcmHrDevTrafficOutputMaxSize": xcmHrDevTrafficOutputMaxSize,
       "xcmHrDevTrafficInputTimeout": xcmHrDevTrafficInputTimeout,
       "xcmHrDevTrafficOutputTimeout": xcmHrDevTrafficOutputTimeout,
       "xcmHrSystemFault": xcmHrSystemFault,
       "xcmHrSystemFaultTable": xcmHrSystemFaultTable,
       "xcmHrSystemFaultEntry": xcmHrSystemFaultEntry,
       "xcmHrSystemFaultIndex": xcmHrSystemFaultIndex,
       "xcmHrSystemFaultRowStatus": xcmHrSystemFaultRowStatus,
       "xcmHrSystemFaultCode": xcmHrSystemFaultCode,
       "xcmHrSystemFaultString": xcmHrSystemFaultString,
       "xcmHrSystemFaultReferenceOID": xcmHrSystemFaultReferenceOID,
       "xcmHrSystemFaultHrDeviceIndex": xcmHrSystemFaultHrDeviceIndex,
       "xcmHrSystemFaultDate": xcmHrSystemFaultDate,
       "xcmHrGeneral": xcmHrGeneral,
       "xcmHrGeneralTable": xcmHrGeneralTable,
       "xcmHrGeneralEntry": xcmHrGeneralEntry,
       "xcmHrGeneralIndex": xcmHrGeneralIndex,
       "xcmHrGeneralRowStatus": xcmHrGeneralRowStatus,
       "xcmHrGeneralVersionID": xcmHrGeneralVersionID,
       "xcmHrGeneralVersionDate": xcmHrGeneralVersionDate,
       "xcmHrGeneralGroupSupport": xcmHrGeneralGroupSupport,
       "xcmHrGeneralStorageLast": xcmHrGeneralStorageLast,
       "xcmHrGeneralDeviceLast": xcmHrGeneralDeviceLast,
       "xcmHrGeneralFSLast": xcmHrGeneralFSLast,
       "xcmHrGeneralSWRunLast": xcmHrGeneralSWRunLast,
       "xcmHrGeneralSWInstalledLast": xcmHrGeneralSWInstalledLast,
       "xcmHrGeneralSystemFaultLast": xcmHrGeneralSystemFaultLast,
       "xcmHrGeneralCreateSupport": xcmHrGeneralCreateSupport,
       "xcmHrGeneralUpdateSupport": xcmHrGeneralUpdateSupport,
       "xcmHrDevCalendar": xcmHrDevCalendar,
       "xcmHrDevCalendarTable": xcmHrDevCalendarTable,
       "xcmHrDevCalendarEntry": xcmHrDevCalendarEntry,
       "xcmHrDevCalendarDayOfWeek": xcmHrDevCalendarDayOfWeek,
       "xcmHrDevCalendarTimeOfDay": xcmHrDevCalendarTimeOfDay,
       "xcmHrDevCalendarRowStatus": xcmHrDevCalendarRowStatus,
       "xcmHrDevCalendarExplicitDate": xcmHrDevCalendarExplicitDate,
       "xcmHrDevCalendarCommandRequest": xcmHrDevCalendarCommandRequest,
       "xcmHrDevCalendarCommandData": xcmHrDevCalendarCommandData,
       "xcmHrSWRun": xcmHrSWRun,
       "xcmHrSWRunTable": xcmHrSWRunTable,
       "xcmHrSWRunEntry": xcmHrSWRunEntry,
       "xcmHrSWRunRowStatus": xcmHrSWRunRowStatus,
       "xcmHrSWRunAdminName": xcmHrSWRunAdminName,
       "xcmHrSWRunXStatus": xcmHrSWRunXStatus,
       "xcmHrSWRunRowCreateDate": xcmHrSWRunRowCreateDate,
       "xcmHrSWRunPhysicalDeviceIndex": xcmHrSWRunPhysicalDeviceIndex,
       "xcmHrSWRunLogicalDeviceIndex": xcmHrSWRunLogicalDeviceIndex,
       "xcmHrSWRunNextIndex": xcmHrSWRunNextIndex,
       "xcmHrSWRunPreviousIndex": xcmHrSWRunPreviousIndex,
       "xcmHrSWInstalled": xcmHrSWInstalled,
       "xcmHrSWInstalledTable": xcmHrSWInstalledTable,
       "xcmHrSWInstalledEntry": xcmHrSWInstalledEntry,
       "xcmHrSWInstalledRowStatus": xcmHrSWInstalledRowStatus,
       "xcmHrSWInstalledAdminName": xcmHrSWInstalledAdminName,
       "xcmHrSWInstalledXStatus": xcmHrSWInstalledXStatus,
       "xcmHrSWInstalledRowCreateDate": xcmHrSWInstalledRowCreateDate,
       "xcmHrSWInstalledPhysicalIndex": xcmHrSWInstalledPhysicalIndex,
       "xcmHrSWInstalledLogicalIndex": xcmHrSWInstalledLogicalIndex,
       "xcmHrSWInstalledNextIndex": xcmHrSWInstalledNextIndex,
       "xcmHrSWInstalledPreviousIndex": xcmHrSWInstalledPreviousIndex,
       "xcmHrDevDetail": xcmHrDevDetail,
       "xcmHrDevDetailV1EventOID": xcmHrDevDetailV1EventOID,
       "xcmHrDevDetailV2EventPrefix": xcmHrDevDetailV2EventPrefix,
       "xcmHrDevDetailV2Event": xcmHrDevDetailV2Event,
       "xcmHrDevDetailTable": xcmHrDevDetailTable,
       "xcmHrDevDetailEntry": xcmHrDevDetailEntry,
       "xcmHrDevDetailType": xcmHrDevDetailType,
       "xcmHrDevDetailIndex": xcmHrDevDetailIndex,
       "xcmHrDevDetailRowStatus": xcmHrDevDetailRowStatus,
       "xcmHrDevDetailUnitClass": xcmHrDevDetailUnitClass,
       "xcmHrDevDetailUnit": xcmHrDevDetailUnit,
       "xcmHrDevDetailValueInteger": xcmHrDevDetailValueInteger,
       "xcmHrDevDetailValueOID": xcmHrDevDetailValueOID,
       "xcmHrDevDetailValueString": xcmHrDevDetailValueString,
       "xcmHrDevDetailDescription": xcmHrDevDetailDescription,
       "xcmHrStorage": xcmHrStorage,
       "xcmHrStorageTable": xcmHrStorageTable,
       "xcmHrStorageEntry": xcmHrStorageEntry,
       "xcmHrStorageRowStatus": xcmHrStorageRowStatus,
       "xcmHrStorageRealization": xcmHrStorageRealization,
       "xcmHrStorageStatus": xcmHrStorageStatus,
       "xcmHrStorageProductDeviceIndex": xcmHrStorageProductDeviceIndex,
       "xcmHrStoragePlatformDeviceIndex": xcmHrStoragePlatformDeviceIndex,
       "xcmHrStoragePagingDeviceIndex": xcmHrStoragePagingDeviceIndex,
       "xcmHrStorageMatchingDeviceIndex": xcmHrStorageMatchingDeviceIndex,
       "xcmHrStorageSWRunIndex": xcmHrStorageSWRunIndex,
       "xcmHrStorageSWInstalledIndex": xcmHrStorageSWInstalledIndex,
       "xcmHrStorageNextIndex": xcmHrStorageNextIndex,
       "xcmHrStoragePreviousIndex": xcmHrStoragePreviousIndex,
       "xcmHrStoragePhysicalIndex": xcmHrStoragePhysicalIndex,
       "xcmHrStorageDetail": xcmHrStorageDetail,
       "xcmHrStorageDetailTable": xcmHrStorageDetailTable,
       "xcmHrStorageDetailEntry": xcmHrStorageDetailEntry,
       "xcmHrStorageDetailType": xcmHrStorageDetailType,
       "xcmHrStorageDetailIndex": xcmHrStorageDetailIndex,
       "xcmHrStorageDetailRowStatus": xcmHrStorageDetailRowStatus,
       "xcmHrStorageDetailUnitClass": xcmHrStorageDetailUnitClass,
       "xcmHrStorageDetailUnit": xcmHrStorageDetailUnit,
       "xcmHrStorageDetailValueInteger": xcmHrStorageDetailValueInteger,
       "xcmHrStorageDetailValueOID": xcmHrStorageDetailValueOID,
       "xcmHrStorageDetailValueString": xcmHrStorageDetailValueString,
       "xcmHrDevCover": xcmHrDevCover,
       "xcmHrDevCoverTable": xcmHrDevCoverTable,
       "xcmHrDevCoverEntry": xcmHrDevCoverEntry,
       "xcmHrDevCoverIndex": xcmHrDevCoverIndex,
       "xcmHrDevCoverRowStatus": xcmHrDevCoverRowStatus,
       "xcmHrDevCoverName": xcmHrDevCoverName,
       "xcmHrDevCoverDescription": xcmHrDevCoverDescription,
       "xcmHrDevCoverTypeCover": xcmHrDevCoverTypeCover,
       "xcmHrDevCoverStatusOpen": xcmHrDevCoverStatusOpen,
       "xcmHrDevAlert": xcmHrDevAlert,
       "xcmHrDevAlertV1EventOID": xcmHrDevAlertV1EventOID,
       "xcmHrDevAlertV2EventPrefix": xcmHrDevAlertV2EventPrefix,
       "xcmHrDevAlertV2Event": xcmHrDevAlertV2Event,
       "xcmHrDevAlertTable": xcmHrDevAlertTable,
       "xcmHrDevAlertEntry": xcmHrDevAlertEntry,
       "xcmHrDevAlertIndex": xcmHrDevAlertIndex,
       "xcmHrDevAlertRowStatus": xcmHrDevAlertRowStatus,
       "xcmHrDevAlertSeverityLevel": xcmHrDevAlertSeverityLevel,
       "xcmHrDevAlertTrainingLevel": xcmHrDevAlertTrainingLevel,
       "xcmHrDevAlertCodeInteger": xcmHrDevAlertCodeInteger,
       "xcmHrDevAlertCodeString": xcmHrDevAlertCodeString,
       "xcmHrDevAlertDescription": xcmHrDevAlertDescription,
       "xcmHrDevAlertReferenceOID": xcmHrDevAlertReferenceOID,
       "xcmHrDevAlertDateAndTime": xcmHrDevAlertDateAndTime,
       "xcmHrDevAlertTitle": xcmHrDevAlertTitle,
       "xcmHrDevAlertHelpReference": xcmHrDevAlertHelpReference,
       "xcmHrDevAlertReferenceIndex": xcmHrDevAlertReferenceIndex,
       "xcmHrDevAlertReferenceLocation": xcmHrDevAlertReferenceLocation,
       "xcmHrDevAlertDevAlertIndex": xcmHrDevAlertDevAlertIndex,
       "xcmHrDevAlertPriority": xcmHrDevAlertPriority,
       "xcmHrDevAlertLastAlertIndex": xcmHrDevAlertLastAlertIndex,
       "xcmHrDevAlertLastCriticalAlertIndex": xcmHrDevAlertLastCriticalAlertIndex,
       "xcmHrConsoleScreen": xcmHrConsoleScreen,
       "xcmHrConsoleScreenTable": xcmHrConsoleScreenTable,
       "xcmHrConsoleScreenEntry": xcmHrConsoleScreenEntry,
       "xcmHrConsoleScreenIndex": xcmHrConsoleScreenIndex,
       "xcmHrConsoleScreenName": xcmHrConsoleScreenName,
       "xcmHrConsoleScreenDescription": xcmHrConsoleScreenDescription,
       "xcmHrConsoleScreenParentIndex": xcmHrConsoleScreenParentIndex,
       "xcmHrConsoleScreenPriority": xcmHrConsoleScreenPriority,
       "xcmHrConsoleScreenTabCount": xcmHrConsoleScreenTabCount,
       "xcmHrConsoleTab": xcmHrConsoleTab,
       "xcmHrConsoleTabTable": xcmHrConsoleTabTable,
       "xcmHrConsoleTabEntry": xcmHrConsoleTabEntry,
       "xcmHrConsoleTabIndex": xcmHrConsoleTabIndex,
       "xcmHrConsoleTabName": xcmHrConsoleTabName,
       "xcmHrConsoleTabDescription": xcmHrConsoleTabDescription,
       "xcmHrConsoleTabScreenIndex": xcmHrConsoleTabScreenIndex,
       "xcmHrConsoleTabPriority": xcmHrConsoleTabPriority,
       "xcmHrSupplies": xcmHrSupplies,
       "xcmHrSuppliesTable": xcmHrSuppliesTable,
       "xcmHrSuppliesEntry": xcmHrSuppliesEntry,
       "xcmHrSuppliesIndex": xcmHrSuppliesIndex,
       "xcmHrSuppliesReferenceOID": xcmHrSuppliesReferenceOID,
       "xcmHrSuppliesType": xcmHrSuppliesType,
       "xcmHrSuppliesClass": xcmHrSuppliesClass,
       "xcmHrSuppliesDescr": xcmHrSuppliesDescr,
       "xcmHrSuppliesPartNumber": xcmHrSuppliesPartNumber,
       "xcmHrDetailTable": xcmHrDetailTable,
       "xcmHrDetailEntry": xcmHrDetailEntry,
       "xcmHrDetailTableRef": xcmHrDetailTableRef,
       "xcmHrDetailTableIndex": xcmHrDetailTableIndex,
       "xcmHrDetailType": xcmHrDetailType,
       "xcmHrDetailIndex": xcmHrDetailIndex,
       "xcmHrDetailUnitClass": xcmHrDetailUnitClass,
       "xcmHrDetailUnit": xcmHrDetailUnit,
       "xcmHrDetailValueInteger": xcmHrDetailValueInteger,
       "xcmHrDetailValueOID": xcmHrDetailValueOID,
       "xcmHrDetailValueString": xcmHrDetailValueString,
       "xcmHrDetailDescription": xcmHrDetailDescription,
       "xcmHrConsole": xcmHrConsole,
       "xcmHrConsoleTable": xcmHrConsoleTable,
       "xcmHrConsoleEntry": xcmHrConsoleEntry,
       "xcmHrConsoleIndex": xcmHrConsoleIndex,
       "xcmHrConsoleDefaultService": xcmHrConsoleDefaultService,
       "xcmHrConsoleBrightness": xcmHrConsoleBrightness,
       "xcmHrConsoleContrast": xcmHrConsoleContrast,
       "xcmHrConsoleAccessibility": xcmHrConsoleAccessibility,
       "xcmHrConsoleAutoClearTime": xcmHrConsoleAutoClearTime,
       "xcmHrConsoleInsertTimeout": xcmHrConsoleInsertTimeout,
       "xcmHrConsoleTray1Timeout": xcmHrConsoleTray1Timeout,
       "xcmHrConsoleTray2nTimeout": xcmHrConsoleTray2nTimeout,
       "xcmHrConsoleLoadTimeout": xcmHrConsoleLoadTimeout,
       "xcmHrConsoleSoundVolume": xcmHrConsoleSoundVolume,
       "xcmHrConsoleSoundDuration": xcmHrConsoleSoundDuration,
       "xcmHrGenericParamGroup": xcmHrGenericParamGroup,
       "xcmHrGenericParamName": xcmHrGenericParamName,
       "xcmHrGenericParamValue": xcmHrGenericParamValue}
)
