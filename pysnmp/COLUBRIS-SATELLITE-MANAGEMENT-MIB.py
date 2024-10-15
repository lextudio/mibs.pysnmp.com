# SNMP MIB module (COLUBRIS-SATELLITE-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-SATELLITE-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:23 2024
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

(ColubrisNotificationEnable,
 ColubrisSSIDOrNone) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable",
    "ColubrisSSIDOrNone")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

colubrisSatelliteManagementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisSatelliteManagementMIBObjects_ObjectIdentity = ObjectIdentity
colubrisSatelliteManagementMIBObjects = _ColubrisSatelliteManagementMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1)
)
_SatelliteInfo_ObjectIdentity = ObjectIdentity
satelliteInfo = _SatelliteInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1)
)
_SatelliteTable_Object = MibTable
satelliteTable = _SatelliteTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    satelliteTable.setStatus("current")
_SatelliteEntry_Object = MibTableRow
satelliteEntry = _SatelliteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1)
)
satelliteEntry.setIndexNames(
    (0, "COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIndex"),
)
if mibBuilder.loadTexts:
    satelliteEntry.setStatus("current")


class _SatelliteIndex_Type(Integer32):
    """Custom type satelliteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SatelliteIndex_Type.__name__ = "Integer32"
_SatelliteIndex_Object = MibTableColumn
satelliteIndex = _SatelliteIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 1),
    _SatelliteIndex_Type()
)
satelliteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satelliteIndex.setStatus("current")
_SatelliteDeviceId_Type = DisplayString
_SatelliteDeviceId_Object = MibTableColumn
satelliteDeviceId = _SatelliteDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 2),
    _SatelliteDeviceId_Type()
)
satelliteDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteDeviceId.setStatus("current")
_SatelliteMacAddress_Type = MacAddress
_SatelliteMacAddress_Object = MibTableColumn
satelliteMacAddress = _SatelliteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 3),
    _SatelliteMacAddress_Type()
)
satelliteMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteMacAddress.setStatus("current")
_SatelliteIpAddress_Type = IpAddress
_SatelliteIpAddress_Object = MibTableColumn
satelliteIpAddress = _SatelliteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 4),
    _SatelliteIpAddress_Type()
)
satelliteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteIpAddress.setStatus("current")
_SatelliteName_Type = DisplayString
_SatelliteName_Object = MibTableColumn
satelliteName = _SatelliteName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 5),
    _SatelliteName_Type()
)
satelliteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteName.setStatus("current")
_SatelliteSSID_Type = ColubrisSSIDOrNone
_SatelliteSSID_Object = MibTableColumn
satelliteSSID = _SatelliteSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 6),
    _SatelliteSSID_Type()
)
satelliteSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteSSID.setStatus("current")
_SatelliteChannelNumber_Type = Unsigned32
_SatelliteChannelNumber_Object = MibTableColumn
satelliteChannelNumber = _SatelliteChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 7),
    _SatelliteChannelNumber_Type()
)
satelliteChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteChannelNumber.setStatus("current")
_SatelliteForwardWirelessToWireless_Type = TruthValue
_SatelliteForwardWirelessToWireless_Object = MibTableColumn
satelliteForwardWirelessToWireless = _SatelliteForwardWirelessToWireless_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 8),
    _SatelliteForwardWirelessToWireless_Type()
)
satelliteForwardWirelessToWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteForwardWirelessToWireless.setStatus("current")
_SatelliteMasterTrafficOnly_Type = TruthValue
_SatelliteMasterTrafficOnly_Object = MibTableColumn
satelliteMasterTrafficOnly = _SatelliteMasterTrafficOnly_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 9),
    _SatelliteMasterTrafficOnly_Type()
)
satelliteMasterTrafficOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteMasterTrafficOnly.setStatus("current")


class _SatelliteSNMPPort_Type(Integer32):
    """Custom type satelliteSNMPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SatelliteSNMPPort_Type.__name__ = "Integer32"
_SatelliteSNMPPort_Object = MibTableColumn
satelliteSNMPPort = _SatelliteSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 10),
    _SatelliteSNMPPort_Type()
)
satelliteSNMPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteSNMPPort.setStatus("current")


class _SatelliteSecureWebPort_Type(Integer32):
    """Custom type satelliteSecureWebPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SatelliteSecureWebPort_Type.__name__ = "Integer32"
_SatelliteSecureWebPort_Object = MibTableColumn
satelliteSecureWebPort = _SatelliteSecureWebPort_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 11),
    _SatelliteSecureWebPort_Type()
)
satelliteSecureWebPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteSecureWebPort.setStatus("current")
_SatelliteDeviceMacAddress_Type = MacAddress
_SatelliteDeviceMacAddress_Object = MibTableColumn
satelliteDeviceMacAddress = _SatelliteDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 12),
    _SatelliteDeviceMacAddress_Type()
)
satelliteDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteDeviceMacAddress.setStatus("current")
_SatelliteProductName_Type = DisplayString
_SatelliteProductName_Object = MibTableColumn
satelliteProductName = _SatelliteProductName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 13),
    _SatelliteProductName_Type()
)
satelliteProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteProductName.setStatus("current")
_SatelliteFirmwareRevision_Type = DisplayString
_SatelliteFirmwareRevision_Object = MibTableColumn
satelliteFirmwareRevision = _SatelliteFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 14),
    _SatelliteFirmwareRevision_Type()
)
satelliteFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteFirmwareRevision.setStatus("current")
_SatelliteGroupName_Type = DisplayString
_SatelliteGroupName_Object = MibTableColumn
satelliteGroupName = _SatelliteGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 15),
    _SatelliteGroupName_Type()
)
satelliteGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteGroupName.setStatus("current")
_SatelliteChannelNumberRadio2_Type = Unsigned32
_SatelliteChannelNumberRadio2_Object = MibTableColumn
satelliteChannelNumberRadio2 = _SatelliteChannelNumberRadio2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 16),
    _SatelliteChannelNumberRadio2_Type()
)
satelliteChannelNumberRadio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteChannelNumberRadio2.setStatus("current")
_SatelliteVLAN_Type = Integer32
_SatelliteVLAN_Object = MibTableColumn
satelliteVLAN = _SatelliteVLAN_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 17),
    _SatelliteVLAN_Type()
)
satelliteVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteVLAN.setStatus("current")
_SatelliteDetectionPort_Type = DisplayString
_SatelliteDetectionPort_Object = MibTableColumn
satelliteDetectionPort = _SatelliteDetectionPort_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 18),
    _SatelliteDetectionPort_Type()
)
satelliteDetectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteDetectionPort.setStatus("current")
_SatelliteNumber_Type = Unsigned32
_SatelliteNumber_Object = MibScalar
satelliteNumber = _SatelliteNumber_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 2),
    _SatelliteNumber_Type()
)
satelliteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteNumber.setStatus("current")
_MasterSettings_ObjectIdentity = ObjectIdentity
masterSettings = _MasterSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2)
)


class _SatelliteUpNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type satelliteUpNotificationEnabled based on ColubrisNotificationEnable"""


_SatelliteUpNotificationEnabled_Object = MibScalar
satelliteUpNotificationEnabled = _SatelliteUpNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2, 1),
    _SatelliteUpNotificationEnabled_Type()
)
satelliteUpNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satelliteUpNotificationEnabled.setStatus("current")


class _SatelliteDownNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type satelliteDownNotificationEnabled based on ColubrisNotificationEnable"""


_SatelliteDownNotificationEnabled_Object = MibScalar
satelliteDownNotificationEnabled = _SatelliteDownNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2, 2),
    _SatelliteDownNotificationEnabled_Type()
)
satelliteDownNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satelliteDownNotificationEnabled.setStatus("current")
_ColubrisSatelliteManagementMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisSatelliteManagementMIBNotificationPrefix = _ColubrisSatelliteManagementMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 2)
)
_ColubrisSatelliteManagementMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisSatelliteManagementMIBNotifications = _ColubrisSatelliteManagementMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0)
)
_ColubrisSatelliteManagementMIBConformance_ObjectIdentity = ObjectIdentity
colubrisSatelliteManagementMIBConformance = _ColubrisSatelliteManagementMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 3)
)
_ColubrisSatelliteManagementMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisSatelliteManagementMIBCompliances = _ColubrisSatelliteManagementMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 1)
)
_ColubrisSatelliteManagementMIBGroups_ObjectIdentity = ObjectIdentity
colubrisSatelliteManagementMIBGroups = _ColubrisSatelliteManagementMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2)
)

# Managed Objects groups

colubrisSatelliteManagementMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 1)
)
colubrisSatelliteManagementMIBGroup.setObjects(
      *(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteChannelNumber"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteForwardWirelessToWireless"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMasterTrafficOnly"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSNMPPort"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSecureWebPort"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceMacAddress"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteProductName"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteFirmwareRevision"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteGroupName"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteNumber"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteChannelNumberRadio2"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteVLAN"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDetectionPort"))
)
if mibBuilder.loadTexts:
    colubrisSatelliteManagementMIBGroup.setStatus("current")

colubrisSatelliteNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 2)
)
colubrisSatelliteNotificationControlGroup.setObjects(
      *(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteUpNotificationEnabled"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDownNotificationEnabled"))
)
if mibBuilder.loadTexts:
    colubrisSatelliteNotificationControlGroup.setStatus("current")


# Notification objects

satelliteUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0, 1)
)
satelliteUpNotification.setObjects(
      *(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"))
)
if mibBuilder.loadTexts:
    satelliteUpNotification.setStatus(
        "current"
    )

satelliteDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0, 2)
)
satelliteDownNotification.setObjects(
      *(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"))
)
if mibBuilder.loadTexts:
    satelliteDownNotification.setStatus(
        "current"
    )


# Notifications groups

colubrisSatelliteNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 3)
)
colubrisSatelliteNotificationGroup.setObjects(
      *(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteUpNotification"),
        ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDownNotification"))
)
if mibBuilder.loadTexts:
    colubrisSatelliteNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisSatelliteManagementMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisSatelliteManagementMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-SATELLITE-MANAGEMENT-MIB",
    **{"colubrisSatelliteManagementMIB": colubrisSatelliteManagementMIB,
       "colubrisSatelliteManagementMIBObjects": colubrisSatelliteManagementMIBObjects,
       "satelliteInfo": satelliteInfo,
       "satelliteTable": satelliteTable,
       "satelliteEntry": satelliteEntry,
       "satelliteIndex": satelliteIndex,
       "satelliteDeviceId": satelliteDeviceId,
       "satelliteMacAddress": satelliteMacAddress,
       "satelliteIpAddress": satelliteIpAddress,
       "satelliteName": satelliteName,
       "satelliteSSID": satelliteSSID,
       "satelliteChannelNumber": satelliteChannelNumber,
       "satelliteForwardWirelessToWireless": satelliteForwardWirelessToWireless,
       "satelliteMasterTrafficOnly": satelliteMasterTrafficOnly,
       "satelliteSNMPPort": satelliteSNMPPort,
       "satelliteSecureWebPort": satelliteSecureWebPort,
       "satelliteDeviceMacAddress": satelliteDeviceMacAddress,
       "satelliteProductName": satelliteProductName,
       "satelliteFirmwareRevision": satelliteFirmwareRevision,
       "satelliteGroupName": satelliteGroupName,
       "satelliteChannelNumberRadio2": satelliteChannelNumberRadio2,
       "satelliteVLAN": satelliteVLAN,
       "satelliteDetectionPort": satelliteDetectionPort,
       "satelliteNumber": satelliteNumber,
       "masterSettings": masterSettings,
       "satelliteUpNotificationEnabled": satelliteUpNotificationEnabled,
       "satelliteDownNotificationEnabled": satelliteDownNotificationEnabled,
       "colubrisSatelliteManagementMIBNotificationPrefix": colubrisSatelliteManagementMIBNotificationPrefix,
       "colubrisSatelliteManagementMIBNotifications": colubrisSatelliteManagementMIBNotifications,
       "satelliteUpNotification": satelliteUpNotification,
       "satelliteDownNotification": satelliteDownNotification,
       "colubrisSatelliteManagementMIBConformance": colubrisSatelliteManagementMIBConformance,
       "colubrisSatelliteManagementMIBCompliances": colubrisSatelliteManagementMIBCompliances,
       "colubrisSatelliteManagementMIBCompliance": colubrisSatelliteManagementMIBCompliance,
       "colubrisSatelliteManagementMIBGroups": colubrisSatelliteManagementMIBGroups,
       "colubrisSatelliteManagementMIBGroup": colubrisSatelliteManagementMIBGroup,
       "colubrisSatelliteNotificationControlGroup": colubrisSatelliteNotificationControlGroup,
       "colubrisSatelliteNotificationGroup": colubrisSatelliteNotificationGroup}
)
