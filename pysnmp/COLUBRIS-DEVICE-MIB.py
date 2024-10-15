# SNMP MIB module (COLUBRIS-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:14 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisNotificationEnable,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

colubrisDeviceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisDeviceMIBObjects_ObjectIdentity = ObjectIdentity
colubrisDeviceMIBObjects = _ColubrisDeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1)
)
_CoDeviceConfigGroup_ObjectIdentity = ObjectIdentity
coDeviceConfigGroup = _CoDeviceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1)
)


class _CoDeviceStateChangeNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type coDeviceStateChangeNotificationEnabled based on ColubrisNotificationEnable"""


_CoDeviceStateChangeNotificationEnabled_Object = MibScalar
coDeviceStateChangeNotificationEnabled = _CoDeviceStateChangeNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 1),
    _CoDeviceStateChangeNotificationEnabled_Type()
)
coDeviceStateChangeNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDeviceStateChangeNotificationEnabled.setStatus("current")


class _CoDeviceAuthorizationFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type coDeviceAuthorizationFailureNotificationEnabled based on ColubrisNotificationEnable"""


_CoDeviceAuthorizationFailureNotificationEnabled_Object = MibScalar
coDeviceAuthorizationFailureNotificationEnabled = _CoDeviceAuthorizationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 2),
    _CoDeviceAuthorizationFailureNotificationEnabled_Type()
)
coDeviceAuthorizationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDeviceAuthorizationFailureNotificationEnabled.setStatus("current")


class _CoDeviceSecurityFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type coDeviceSecurityFailureNotificationEnabled based on ColubrisNotificationEnable"""


_CoDeviceSecurityFailureNotificationEnabled_Object = MibScalar
coDeviceSecurityFailureNotificationEnabled = _CoDeviceSecurityFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 3),
    _CoDeviceSecurityFailureNotificationEnabled_Type()
)
coDeviceSecurityFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDeviceSecurityFailureNotificationEnabled.setStatus("current")


class _CoDeviceFirmwareFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type coDeviceFirmwareFailureNotificationEnabled based on ColubrisNotificationEnable"""


_CoDeviceFirmwareFailureNotificationEnabled_Object = MibScalar
coDeviceFirmwareFailureNotificationEnabled = _CoDeviceFirmwareFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 4),
    _CoDeviceFirmwareFailureNotificationEnabled_Type()
)
coDeviceFirmwareFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDeviceFirmwareFailureNotificationEnabled.setStatus("current")


class _CoDeviceConfigurationFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type coDeviceConfigurationFailureNotificationEnabled based on ColubrisNotificationEnable"""


_CoDeviceConfigurationFailureNotificationEnabled_Object = MibScalar
coDeviceConfigurationFailureNotificationEnabled = _CoDeviceConfigurationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 5),
    _CoDeviceConfigurationFailureNotificationEnabled_Type()
)
coDeviceConfigurationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDeviceConfigurationFailureNotificationEnabled.setStatus("current")
_CoDeviceDiscoveryGroup_ObjectIdentity = ObjectIdentity
coDeviceDiscoveryGroup = _CoDeviceDiscoveryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2)
)
_CoDeviceDiscoveryTable_Object = MibTable
coDeviceDiscoveryTable = _CoDeviceDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceDiscoveryTable.setStatus("current")
_CoDeviceDiscoveryEntry_Object = MibTableRow
coDeviceDiscoveryEntry = _CoDeviceDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1)
)
coDeviceDiscoveryEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
)
if mibBuilder.loadTexts:
    coDeviceDiscoveryEntry.setStatus("current")


class _CoDevDisIndex_Type(Integer32):
    """Custom type coDevDisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevDisIndex_Type.__name__ = "Integer32"
_CoDevDisIndex_Object = MibTableColumn
coDevDisIndex = _CoDevDisIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 1),
    _CoDevDisIndex_Type()
)
coDevDisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevDisIndex.setStatus("current")
_CoDevDisSerialNumber_Type = DisplayString
_CoDevDisSerialNumber_Object = MibTableColumn
coDevDisSerialNumber = _CoDevDisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 2),
    _CoDevDisSerialNumber_Type()
)
coDevDisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisSerialNumber.setStatus("current")
_CoDevDisMacAddress_Type = MacAddress
_CoDevDisMacAddress_Object = MibTableColumn
coDevDisMacAddress = _CoDevDisMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 3),
    _CoDevDisMacAddress_Type()
)
coDevDisMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisMacAddress.setStatus("current")
_CoDevDisIpAddress_Type = IpAddress
_CoDevDisIpAddress_Object = MibTableColumn
coDevDisIpAddress = _CoDevDisIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 4),
    _CoDevDisIpAddress_Type()
)
coDevDisIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisIpAddress.setStatus("current")


class _CoDevDisState_Type(Integer32):
    """Custom type coDevDisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("configuration", 6),
          ("disconnected", 1),
          ("firmware", 4),
          ("join", 3),
          ("running", 7),
          ("security", 5))
    )


_CoDevDisState_Type.__name__ = "Integer32"
_CoDevDisState_Object = MibTableColumn
coDevDisState = _CoDevDisState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 5),
    _CoDevDisState_Type()
)
coDevDisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisState.setStatus("current")
_CoDevDisSystemName_Type = DisplayString
_CoDevDisSystemName_Object = MibTableColumn
coDevDisSystemName = _CoDevDisSystemName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 6),
    _CoDevDisSystemName_Type()
)
coDevDisSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisSystemName.setStatus("current")
_CoDevDisLocation_Type = DisplayString
_CoDevDisLocation_Object = MibTableColumn
coDevDisLocation = _CoDevDisLocation_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 7),
    _CoDevDisLocation_Type()
)
coDevDisLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisLocation.setStatus("current")
_CoDevDisContact_Type = DisplayString
_CoDevDisContact_Object = MibTableColumn
coDevDisContact = _CoDevDisContact_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 8),
    _CoDevDisContact_Type()
)
coDevDisContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisContact.setStatus("current")
_CoDevDisGroupName_Type = DisplayString
_CoDevDisGroupName_Object = MibTableColumn
coDevDisGroupName = _CoDevDisGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 9),
    _CoDevDisGroupName_Type()
)
coDevDisGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisGroupName.setStatus("current")
_CoDevDisConnectionTime_Type = Counter32
_CoDevDisConnectionTime_Object = MibTableColumn
coDevDisConnectionTime = _CoDevDisConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 10),
    _CoDevDisConnectionTime_Type()
)
coDevDisConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisConnectionTime.setStatus("current")
if mibBuilder.loadTexts:
    coDevDisConnectionTime.setUnits("minutes")


class _CoDevDisControllerIndex_Type(Integer32):
    """Custom type coDevDisControllerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CoDevDisControllerIndex_Type.__name__ = "Integer32"
_CoDevDisControllerIndex_Object = MibTableColumn
coDevDisControllerIndex = _CoDevDisControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 11),
    _CoDevDisControllerIndex_Type()
)
coDevDisControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevDisControllerIndex.setStatus("current")
_CoDeviceInformationGroup_ObjectIdentity = ObjectIdentity
coDeviceInformationGroup = _CoDeviceInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3)
)
_CoDeviceInfoTable_Object = MibTable
coDeviceInfoTable = _CoDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coDeviceInfoTable.setStatus("current")
_CoDeviceInfoEntry_Object = MibTableRow
coDeviceInfoEntry = _CoDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceInfoEntry.setStatus("current")
_CoDevInfoProductType_Type = ObjectIdentifier
_CoDevInfoProductType_Object = MibTableColumn
coDevInfoProductType = _CoDevInfoProductType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 1),
    _CoDevInfoProductType_Type()
)
coDevInfoProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevInfoProductType.setStatus("current")
_CoDevInfoProductName_Type = DisplayString
_CoDevInfoProductName_Object = MibTableColumn
coDevInfoProductName = _CoDevInfoProductName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 2),
    _CoDevInfoProductName_Type()
)
coDevInfoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevInfoProductName.setStatus("current")
_CoDevInfoFirmwareRevision_Type = DisplayString
_CoDevInfoFirmwareRevision_Object = MibTableColumn
coDevInfoFirmwareRevision = _CoDevInfoFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 3),
    _CoDevInfoFirmwareRevision_Type()
)
coDevInfoFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevInfoFirmwareRevision.setStatus("current")
_CoDevInfoBootRevision_Type = DisplayString
_CoDevInfoBootRevision_Object = MibTableColumn
coDevInfoBootRevision = _CoDevInfoBootRevision_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 4),
    _CoDevInfoBootRevision_Type()
)
coDevInfoBootRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevInfoBootRevision.setStatus("current")
_CoDevInfoHardwareRevision_Type = DisplayString
_CoDevInfoHardwareRevision_Object = MibTableColumn
coDevInfoHardwareRevision = _CoDevInfoHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 5),
    _CoDevInfoHardwareRevision_Type()
)
coDevInfoHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevInfoHardwareRevision.setStatus("current")
_CoDeviceStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceStatusGroup = _CoDeviceStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4)
)
_CoDeviceStatusTable_Object = MibTable
coDeviceStatusTable = _CoDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1)
)
if mibBuilder.loadTexts:
    coDeviceStatusTable.setStatus("current")
_CoDeviceStatusEntry_Object = MibTableRow
coDeviceStatusEntry = _CoDeviceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceStatusEntry.setStatus("current")
_CoDevStUpTime_Type = TimeTicks
_CoDevStUpTime_Object = MibTableColumn
coDevStUpTime = _CoDevStUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 1),
    _CoDevStUpTime_Type()
)
coDevStUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStUpTime.setStatus("current")
_CoDevStLoadAverage1Min_Type = Unsigned32
_CoDevStLoadAverage1Min_Object = MibTableColumn
coDevStLoadAverage1Min = _CoDevStLoadAverage1Min_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 2),
    _CoDevStLoadAverage1Min_Type()
)
coDevStLoadAverage1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStLoadAverage1Min.setStatus("current")
_CoDevStLoadAverage5Min_Type = Unsigned32
_CoDevStLoadAverage5Min_Object = MibTableColumn
coDevStLoadAverage5Min = _CoDevStLoadAverage5Min_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 3),
    _CoDevStLoadAverage5Min_Type()
)
coDevStLoadAverage5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStLoadAverage5Min.setStatus("current")
_CoDevStLoadAverage15Min_Type = Unsigned32
_CoDevStLoadAverage15Min_Object = MibTableColumn
coDevStLoadAverage15Min = _CoDevStLoadAverage15Min_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 4),
    _CoDevStLoadAverage15Min_Type()
)
coDevStLoadAverage15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStLoadAverage15Min.setStatus("current")
_CoDevStCpuUseNow_Type = Unsigned32
_CoDevStCpuUseNow_Object = MibTableColumn
coDevStCpuUseNow = _CoDevStCpuUseNow_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 5),
    _CoDevStCpuUseNow_Type()
)
coDevStCpuUseNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStCpuUseNow.setStatus("current")
if mibBuilder.loadTexts:
    coDevStCpuUseNow.setUnits("%")
_CoDevStCpuUse5Sec_Type = Unsigned32
_CoDevStCpuUse5Sec_Object = MibTableColumn
coDevStCpuUse5Sec = _CoDevStCpuUse5Sec_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 6),
    _CoDevStCpuUse5Sec_Type()
)
coDevStCpuUse5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStCpuUse5Sec.setStatus("current")
if mibBuilder.loadTexts:
    coDevStCpuUse5Sec.setUnits("%")
_CoDevStCpuUse10Sec_Type = Unsigned32
_CoDevStCpuUse10Sec_Object = MibTableColumn
coDevStCpuUse10Sec = _CoDevStCpuUse10Sec_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 7),
    _CoDevStCpuUse10Sec_Type()
)
coDevStCpuUse10Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStCpuUse10Sec.setStatus("current")
if mibBuilder.loadTexts:
    coDevStCpuUse10Sec.setUnits("%")
_CoDevStCpuUse20Sec_Type = Unsigned32
_CoDevStCpuUse20Sec_Object = MibTableColumn
coDevStCpuUse20Sec = _CoDevStCpuUse20Sec_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 8),
    _CoDevStCpuUse20Sec_Type()
)
coDevStCpuUse20Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStCpuUse20Sec.setStatus("current")
if mibBuilder.loadTexts:
    coDevStCpuUse20Sec.setUnits("%")
_CoDevStRamTotal_Type = Unsigned32
_CoDevStRamTotal_Object = MibTableColumn
coDevStRamTotal = _CoDevStRamTotal_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 9),
    _CoDevStRamTotal_Type()
)
coDevStRamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStRamTotal.setStatus("current")
if mibBuilder.loadTexts:
    coDevStRamTotal.setUnits("Kb")
_CoDevStRamFree_Type = Unsigned32
_CoDevStRamFree_Object = MibTableColumn
coDevStRamFree = _CoDevStRamFree_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 10),
    _CoDevStRamFree_Type()
)
coDevStRamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStRamFree.setStatus("current")
if mibBuilder.loadTexts:
    coDevStRamFree.setUnits("Kb")
_CoDevStRamBuffer_Type = Unsigned32
_CoDevStRamBuffer_Object = MibTableColumn
coDevStRamBuffer = _CoDevStRamBuffer_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 11),
    _CoDevStRamBuffer_Type()
)
coDevStRamBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStRamBuffer.setStatus("current")
if mibBuilder.loadTexts:
    coDevStRamBuffer.setUnits("Kb")
_CoDevStRamCached_Type = Unsigned32
_CoDevStRamCached_Object = MibTableColumn
coDevStRamCached = _CoDevStRamCached_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 12),
    _CoDevStRamCached_Type()
)
coDevStRamCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStRamCached.setStatus("current")
if mibBuilder.loadTexts:
    coDevStRamCached.setUnits("Kb")
_CoDevStStorageUsePermanent_Type = Unsigned32
_CoDevStStorageUsePermanent_Object = MibTableColumn
coDevStStorageUsePermanent = _CoDevStStorageUsePermanent_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 13),
    _CoDevStStorageUsePermanent_Type()
)
coDevStStorageUsePermanent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStStorageUsePermanent.setStatus("current")
if mibBuilder.loadTexts:
    coDevStStorageUsePermanent.setUnits("%")
_CoDevStStorageUseTemporary_Type = Unsigned32
_CoDevStStorageUseTemporary_Object = MibTableColumn
coDevStStorageUseTemporary = _CoDevStStorageUseTemporary_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 14),
    _CoDevStStorageUseTemporary_Type()
)
coDevStStorageUseTemporary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevStStorageUseTemporary.setStatus("current")
if mibBuilder.loadTexts:
    coDevStStorageUseTemporary.setUnits("%")
_ColubrisDeviceMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisDeviceMIBNotificationPrefix = _ColubrisDeviceMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 2)
)
_ColubrisDeviceMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisDeviceMIBNotifications = _ColubrisDeviceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0)
)
_ColubrisDeviceMIBConformance_ObjectIdentity = ObjectIdentity
colubrisDeviceMIBConformance = _ColubrisDeviceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3)
)
_ColubrisDeviceMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisDeviceMIBCompliances = _ColubrisDeviceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 1)
)
_ColubrisDeviceMIBGroups_ObjectIdentity = ObjectIdentity
colubrisDeviceMIBGroups = _ColubrisDeviceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2)
)
coDeviceDiscoveryEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-MIB",
     "coDeviceInfoEntry")
)
coDeviceInfoEntry.setIndexNames(*coDeviceDiscoveryEntry.getIndexNames())
coDeviceDiscoveryEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-MIB",
     "coDeviceStatusEntry")
)
coDeviceStatusEntry.setIndexNames(*coDeviceDiscoveryEntry.getIndexNames())

# Managed Objects groups

colubrisDeviceConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 1)
)
colubrisDeviceConfigMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDeviceStateChangeNotificationEnabled"),
        ("COLUBRIS-DEVICE-MIB", "coDeviceAuthorizationFailureNotificationEnabled"),
        ("COLUBRIS-DEVICE-MIB", "coDeviceSecurityFailureNotificationEnabled"),
        ("COLUBRIS-DEVICE-MIB", "coDeviceFirmwareFailureNotificationEnabled"),
        ("COLUBRIS-DEVICE-MIB", "coDeviceConfigurationFailureNotificationEnabled"))
)
if mibBuilder.loadTexts:
    colubrisDeviceConfigMIBGroup.setStatus("current")

colubrisDeviceDiscoveryMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 2)
)
colubrisDeviceDiscoveryMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisMacAddress"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisState"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisLocation"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisContact"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisGroupName"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisConnectionTime"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisControllerIndex"))
)
if mibBuilder.loadTexts:
    colubrisDeviceDiscoveryMIBGroup.setStatus("current")

colubrisDeviceInformationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 3)
)
colubrisDeviceInformationMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDevInfoProductType"),
        ("COLUBRIS-DEVICE-MIB", "coDevInfoProductName"),
        ("COLUBRIS-DEVICE-MIB", "coDevInfoFirmwareRevision"),
        ("COLUBRIS-DEVICE-MIB", "coDevInfoBootRevision"),
        ("COLUBRIS-DEVICE-MIB", "coDevInfoHardwareRevision"))
)
if mibBuilder.loadTexts:
    colubrisDeviceInformationMIBGroup.setStatus("current")

colubrisDeviceStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 4)
)
colubrisDeviceStatusMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDevStUpTime"),
        ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage1Min"),
        ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage5Min"),
        ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage15Min"),
        ("COLUBRIS-DEVICE-MIB", "coDevStCpuUseNow"),
        ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse5Sec"),
        ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse10Sec"),
        ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse20Sec"),
        ("COLUBRIS-DEVICE-MIB", "coDevStRamTotal"),
        ("COLUBRIS-DEVICE-MIB", "coDevStRamFree"),
        ("COLUBRIS-DEVICE-MIB", "coDevStRamBuffer"),
        ("COLUBRIS-DEVICE-MIB", "coDevStRamCached"),
        ("COLUBRIS-DEVICE-MIB", "coDevStStorageUsePermanent"),
        ("COLUBRIS-DEVICE-MIB", "coDevStStorageUseTemporary"))
)
if mibBuilder.loadTexts:
    colubrisDeviceStatusMIBGroup.setStatus("current")


# Notification objects

coDeviceStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 1)
)
coDeviceStateChangeNotification.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisState"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
)
if mibBuilder.loadTexts:
    coDeviceStateChangeNotification.setStatus(
        "current"
    )

coDeviceAuthorizationFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 2)
)
coDeviceAuthorizationFailureNotification.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisState"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
)
if mibBuilder.loadTexts:
    coDeviceAuthorizationFailureNotification.setStatus(
        "current"
    )

coDeviceSecurityFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 3)
)
coDeviceSecurityFailureNotification.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisState"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
)
if mibBuilder.loadTexts:
    coDeviceSecurityFailureNotification.setStatus(
        "current"
    )

coDeviceFirmwareFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 4)
)
coDeviceFirmwareFailureNotification.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisState"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
)
if mibBuilder.loadTexts:
    coDeviceFirmwareFailureNotification.setStatus(
        "current"
    )

coDeviceConfigurationFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 5)
)
coDeviceConfigurationFailureNotification.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisState"),
        ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
)
if mibBuilder.loadTexts:
    coDeviceConfigurationFailureNotification.setStatus(
        "current"
    )


# Notifications groups

colubrisDeviceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 5)
)
colubrisDeviceNotificationGroup.setObjects(
      *(("COLUBRIS-DEVICE-MIB", "coDeviceStateChangeNotification"),
        ("COLUBRIS-DEVICE-MIB", "coDeviceAuthorizationFailureNotification"),
        ("COLUBRIS-DEVICE-MIB", "coDeviceSecurityFailureNotification"),
        ("COLUBRIS-DEVICE-MIB", "coDeviceFirmwareFailureNotification"),
        ("COLUBRIS-DEVICE-MIB", "coDeviceConfigurationFailureNotification"))
)
if mibBuilder.loadTexts:
    colubrisDeviceNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-DEVICE-MIB",
    **{"colubrisDeviceMIB": colubrisDeviceMIB,
       "colubrisDeviceMIBObjects": colubrisDeviceMIBObjects,
       "coDeviceConfigGroup": coDeviceConfigGroup,
       "coDeviceStateChangeNotificationEnabled": coDeviceStateChangeNotificationEnabled,
       "coDeviceAuthorizationFailureNotificationEnabled": coDeviceAuthorizationFailureNotificationEnabled,
       "coDeviceSecurityFailureNotificationEnabled": coDeviceSecurityFailureNotificationEnabled,
       "coDeviceFirmwareFailureNotificationEnabled": coDeviceFirmwareFailureNotificationEnabled,
       "coDeviceConfigurationFailureNotificationEnabled": coDeviceConfigurationFailureNotificationEnabled,
       "coDeviceDiscoveryGroup": coDeviceDiscoveryGroup,
       "coDeviceDiscoveryTable": coDeviceDiscoveryTable,
       "coDeviceDiscoveryEntry": coDeviceDiscoveryEntry,
       "coDevDisIndex": coDevDisIndex,
       "coDevDisSerialNumber": coDevDisSerialNumber,
       "coDevDisMacAddress": coDevDisMacAddress,
       "coDevDisIpAddress": coDevDisIpAddress,
       "coDevDisState": coDevDisState,
       "coDevDisSystemName": coDevDisSystemName,
       "coDevDisLocation": coDevDisLocation,
       "coDevDisContact": coDevDisContact,
       "coDevDisGroupName": coDevDisGroupName,
       "coDevDisConnectionTime": coDevDisConnectionTime,
       "coDevDisControllerIndex": coDevDisControllerIndex,
       "coDeviceInformationGroup": coDeviceInformationGroup,
       "coDeviceInfoTable": coDeviceInfoTable,
       "coDeviceInfoEntry": coDeviceInfoEntry,
       "coDevInfoProductType": coDevInfoProductType,
       "coDevInfoProductName": coDevInfoProductName,
       "coDevInfoFirmwareRevision": coDevInfoFirmwareRevision,
       "coDevInfoBootRevision": coDevInfoBootRevision,
       "coDevInfoHardwareRevision": coDevInfoHardwareRevision,
       "coDeviceStatusGroup": coDeviceStatusGroup,
       "coDeviceStatusTable": coDeviceStatusTable,
       "coDeviceStatusEntry": coDeviceStatusEntry,
       "coDevStUpTime": coDevStUpTime,
       "coDevStLoadAverage1Min": coDevStLoadAverage1Min,
       "coDevStLoadAverage5Min": coDevStLoadAverage5Min,
       "coDevStLoadAverage15Min": coDevStLoadAverage15Min,
       "coDevStCpuUseNow": coDevStCpuUseNow,
       "coDevStCpuUse5Sec": coDevStCpuUse5Sec,
       "coDevStCpuUse10Sec": coDevStCpuUse10Sec,
       "coDevStCpuUse20Sec": coDevStCpuUse20Sec,
       "coDevStRamTotal": coDevStRamTotal,
       "coDevStRamFree": coDevStRamFree,
       "coDevStRamBuffer": coDevStRamBuffer,
       "coDevStRamCached": coDevStRamCached,
       "coDevStStorageUsePermanent": coDevStStorageUsePermanent,
       "coDevStStorageUseTemporary": coDevStStorageUseTemporary,
       "colubrisDeviceMIBNotificationPrefix": colubrisDeviceMIBNotificationPrefix,
       "colubrisDeviceMIBNotifications": colubrisDeviceMIBNotifications,
       "coDeviceStateChangeNotification": coDeviceStateChangeNotification,
       "coDeviceAuthorizationFailureNotification": coDeviceAuthorizationFailureNotification,
       "coDeviceSecurityFailureNotification": coDeviceSecurityFailureNotification,
       "coDeviceFirmwareFailureNotification": coDeviceFirmwareFailureNotification,
       "coDeviceConfigurationFailureNotification": coDeviceConfigurationFailureNotification,
       "colubrisDeviceMIBConformance": colubrisDeviceMIBConformance,
       "colubrisDeviceMIBCompliances": colubrisDeviceMIBCompliances,
       "colubrisDeviceMIBCompliance": colubrisDeviceMIBCompliance,
       "colubrisDeviceMIBGroups": colubrisDeviceMIBGroups,
       "colubrisDeviceConfigMIBGroup": colubrisDeviceConfigMIBGroup,
       "colubrisDeviceDiscoveryMIBGroup": colubrisDeviceDiscoveryMIBGroup,
       "colubrisDeviceInformationMIBGroup": colubrisDeviceInformationMIBGroup,
       "colubrisDeviceStatusMIBGroup": colubrisDeviceStatusMIBGroup,
       "colubrisDeviceNotificationGroup": colubrisDeviceNotificationGroup}
)
