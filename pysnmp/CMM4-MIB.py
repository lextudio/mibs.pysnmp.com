# SNMP MIB module (CMM4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CMM4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:52 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(whispBox,
 whispCMM4,
 whispModules) = mibBuilder.importSymbols(
    "WHISP-GLOBAL-REG-MIB",
    "whispBox",
    "whispCMM4",
    "whispModules")

(EventString,
 WhispLUID,
 WhispMACAddress) = mibBuilder.importSymbols(
    "WHISP-TCV2-MIB",
    "EventString",
    "WhispLUID",
    "WhispMACAddress")


# MODULE-IDENTITY

cmm4MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cmm4Groups_ObjectIdentity = ObjectIdentity
cmm4Groups = _Cmm4Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1)
)
_Cmm4Config_ObjectIdentity = ObjectIdentity
cmm4Config = _Cmm4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2)
)


class _GpsTimingPulse_Type(Integer32):
    """Custom type gpsTimingPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 0))
    )


_GpsTimingPulse_Type.__name__ = "Integer32"
_GpsTimingPulse_Object = MibScalar
gpsTimingPulse = _GpsTimingPulse_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 1),
    _GpsTimingPulse_Type()
)
gpsTimingPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpsTimingPulse.setStatus("current")
_Lan1Ip_Type = IpAddress
_Lan1Ip_Object = MibScalar
lan1Ip = _Lan1Ip_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 2),
    _Lan1Ip_Type()
)
lan1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1Ip.setStatus("current")
_Lan1SubnetMask_Type = IpAddress
_Lan1SubnetMask_Object = MibScalar
lan1SubnetMask = _Lan1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 3),
    _Lan1SubnetMask_Type()
)
lan1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1SubnetMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 4),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")
_Cmm4WebAutoUpdate_Type = Integer32
_Cmm4WebAutoUpdate_Object = MibScalar
cmm4WebAutoUpdate = _Cmm4WebAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 5),
    _Cmm4WebAutoUpdate_Type()
)
cmm4WebAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4WebAutoUpdate.setStatus("current")
if mibBuilder.loadTexts:
    cmm4WebAutoUpdate.setUnits("Seconds")


class _Cmm4ExtEthPowerReset_Type(Integer32):
    """Custom type cmm4ExtEthPowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Cmm4ExtEthPowerReset_Type.__name__ = "Integer32"
_Cmm4ExtEthPowerReset_Object = MibScalar
cmm4ExtEthPowerReset = _Cmm4ExtEthPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 6),
    _Cmm4ExtEthPowerReset_Type()
)
cmm4ExtEthPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4ExtEthPowerReset.setStatus("current")
_Cmm4PortCfgTable_Object = MibTable
cmm4PortCfgTable = _Cmm4PortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7)
)
if mibBuilder.loadTexts:
    cmm4PortCfgTable.setStatus("current")
_Cmm4PortCfgEntry_Object = MibTableRow
cmm4PortCfgEntry = _Cmm4PortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1)
)
cmm4PortCfgEntry.setIndexNames(
    (0, "CMM4-MIB", "portCfgIndex"),
)
if mibBuilder.loadTexts:
    cmm4PortCfgEntry.setStatus("current")


class _PortCfgIndex_Type(Integer32):
    """Custom type portCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PortCfgIndex_Type.__name__ = "Integer32"
_PortCfgIndex_Object = MibTableColumn
portCfgIndex = _PortCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 1),
    _PortCfgIndex_Type()
)
portCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCfgIndex.setStatus("current")
_Cmm4PortText_Type = DisplayString
_Cmm4PortText_Object = MibTableColumn
cmm4PortText = _Cmm4PortText_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 2),
    _Cmm4PortText_Type()
)
cmm4PortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4PortText.setStatus("current")


class _Cmm4PortDevType_Type(Integer32):
    """Custom type cmm4PortDevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canopy", 1),
          ("canopy56V", 2),
          ("none", 0))
    )


_Cmm4PortDevType_Type.__name__ = "Integer32"
_Cmm4PortDevType_Object = MibTableColumn
cmm4PortDevType = _Cmm4PortDevType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 3),
    _Cmm4PortDevType_Type()
)
cmm4PortDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4PortDevType.setStatus("current")


class _Cmm4PortPowerCfg_Type(Integer32):
    """Custom type cmm4PortPowerCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Cmm4PortPowerCfg_Type.__name__ = "Integer32"
_Cmm4PortPowerCfg_Object = MibTableColumn
cmm4PortPowerCfg = _Cmm4PortPowerCfg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 4),
    _Cmm4PortPowerCfg_Type()
)
cmm4PortPowerCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4PortPowerCfg.setStatus("current")


class _Cmm4PortResetCfg_Type(Integer32):
    """Custom type cmm4PortResetCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resetComplete", 0),
          ("resetPort", 1))
    )


_Cmm4PortResetCfg_Type.__name__ = "Integer32"
_Cmm4PortResetCfg_Object = MibTableColumn
cmm4PortResetCfg = _Cmm4PortResetCfg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 5),
    _Cmm4PortResetCfg_Type()
)
cmm4PortResetCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4PortResetCfg.setStatus("current")


class _Cmm4IpAccessFilter_Type(Integer32):
    """Custom type cmm4IpAccessFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Cmm4IpAccessFilter_Type.__name__ = "Integer32"
_Cmm4IpAccessFilter_Object = MibScalar
cmm4IpAccessFilter = _Cmm4IpAccessFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 8),
    _Cmm4IpAccessFilter_Type()
)
cmm4IpAccessFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4IpAccessFilter.setStatus("current")
_Cmm4IpAccess1_Type = IpAddress
_Cmm4IpAccess1_Object = MibScalar
cmm4IpAccess1 = _Cmm4IpAccess1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 9),
    _Cmm4IpAccess1_Type()
)
cmm4IpAccess1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4IpAccess1.setStatus("current")
_Cmm4IpAccess2_Type = IpAddress
_Cmm4IpAccess2_Object = MibScalar
cmm4IpAccess2 = _Cmm4IpAccess2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 10),
    _Cmm4IpAccess2_Type()
)
cmm4IpAccess2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4IpAccess2.setStatus("current")
_Cmm4IpAccess3_Type = IpAddress
_Cmm4IpAccess3_Object = MibScalar
cmm4IpAccess3 = _Cmm4IpAccess3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 11),
    _Cmm4IpAccess3_Type()
)
cmm4IpAccess3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4IpAccess3.setStatus("current")


class _Cmm4MgmtPortSpeed_Type(Integer32):
    """Custom type cmm4MgmtPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("force100Full", 5),
          ("force100Half", 4),
          ("force10Full", 3),
          ("force10Half", 2))
    )


_Cmm4MgmtPortSpeed_Type.__name__ = "Integer32"
_Cmm4MgmtPortSpeed_Object = MibScalar
cmm4MgmtPortSpeed = _Cmm4MgmtPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 12),
    _Cmm4MgmtPortSpeed_Type()
)
cmm4MgmtPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4MgmtPortSpeed.setStatus("current")
_Cmm4NTPServerIp_Type = IpAddress
_Cmm4NTPServerIp_Object = MibScalar
cmm4NTPServerIp = _Cmm4NTPServerIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 13),
    _Cmm4NTPServerIp_Type()
)
cmm4NTPServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4NTPServerIp.setStatus("current")
_SessionTimeout_Type = Integer32
_SessionTimeout_Object = MibScalar
sessionTimeout = _SessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 14),
    _SessionTimeout_Type()
)
sessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionTimeout.setStatus("current")


class _VlanEnable_Type(Integer32):
    """Custom type vlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VlanEnable_Type.__name__ = "Integer32"
_VlanEnable_Object = MibScalar
vlanEnable = _VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 15),
    _VlanEnable_Type()
)
vlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanEnable.setStatus("current")


class _ManagementVID_Type(Integer32):
    """Custom type managementVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ManagementVID_Type.__name__ = "Integer32"
_ManagementVID_Object = MibScalar
managementVID = _ManagementVID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 16),
    _ManagementVID_Type()
)
managementVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVID.setStatus("current")


class _SiteInfoViewable_Type(Integer32):
    """Custom type siteInfoViewable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SiteInfoViewable_Type.__name__ = "Integer32"
_SiteInfoViewable_Object = MibScalar
siteInfoViewable = _SiteInfoViewable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 17),
    _SiteInfoViewable_Type()
)
siteInfoViewable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteInfoViewable.setStatus("current")
_Cmm4Status_ObjectIdentity = ObjectIdentity
cmm4Status = _Cmm4Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3)
)
_Cmm4PortStatusTable_Object = MibTable
cmm4PortStatusTable = _Cmm4PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    cmm4PortStatusTable.setStatus("current")
_Cmm4PortStatusEntry_Object = MibTableRow
cmm4PortStatusEntry = _Cmm4PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 1, 1)
)
cmm4PortStatusEntry.setIndexNames(
    (0, "CMM4-MIB", "portStatusIndex"),
)
if mibBuilder.loadTexts:
    cmm4PortStatusEntry.setStatus("current")


class _PortStatusIndex_Type(Integer32):
    """Custom type portStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PortStatusIndex_Type.__name__ = "Integer32"
_PortStatusIndex_Object = MibTableColumn
portStatusIndex = _PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 1, 1, 1),
    _PortStatusIndex_Type()
)
portStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusIndex.setStatus("current")


class _Cmm4PortPowerStatus_Type(Integer32):
    """Custom type cmm4PortPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("powerOverEthernetFault", -1))
    )


_Cmm4PortPowerStatus_Type.__name__ = "Integer32"
_Cmm4PortPowerStatus_Object = MibTableColumn
cmm4PortPowerStatus = _Cmm4PortPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 1, 1, 4),
    _Cmm4PortPowerStatus_Type()
)
cmm4PortPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4PortPowerStatus.setStatus("current")
_DeviceType_Type = DisplayString
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 2),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_Cmm4pldVersion_Type = DisplayString
_Cmm4pldVersion_Object = MibScalar
cmm4pldVersion = _Cmm4pldVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 3),
    _Cmm4pldVersion_Type()
)
cmm4pldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4pldVersion.setStatus("current")
_Cmm4SoftwareVersion_Type = DisplayString
_Cmm4SoftwareVersion_Object = MibScalar
cmm4SoftwareVersion = _Cmm4SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 4),
    _Cmm4SoftwareVersion_Type()
)
cmm4SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4SoftwareVersion.setStatus("current")
_Cmm4SystemTime_Type = DisplayString
_Cmm4SystemTime_Object = MibScalar
cmm4SystemTime = _Cmm4SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 5),
    _Cmm4SystemTime_Type()
)
cmm4SystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4SystemTime.setStatus("current")
_Cmm4UpTime_Type = DisplayString
_Cmm4UpTime_Object = MibScalar
cmm4UpTime = _Cmm4UpTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 6),
    _Cmm4UpTime_Type()
)
cmm4UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4UpTime.setStatus("current")
_SatellitesVisible_Type = DisplayString
_SatellitesVisible_Object = MibScalar
satellitesVisible = _SatellitesVisible_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 7),
    _SatellitesVisible_Type()
)
satellitesVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satellitesVisible.setStatus("current")
_SatellitesTracked_Type = DisplayString
_SatellitesTracked_Object = MibScalar
satellitesTracked = _SatellitesTracked_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 8),
    _SatellitesTracked_Type()
)
satellitesTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satellitesTracked.setStatus("current")
_Latitude_Type = DisplayString
_Latitude_Object = MibScalar
latitude = _Latitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 9),
    _Latitude_Type()
)
latitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Longitude_Type = DisplayString
_Longitude_Object = MibScalar
longitude = _Longitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 10),
    _Longitude_Type()
)
longitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    longitude.setStatus("current")
_Height_Type = DisplayString
_Height_Object = MibScalar
height = _Height_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 11),
    _Height_Type()
)
height.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    height.setStatus("current")
_TrackingMode_Type = DisplayString
_TrackingMode_Object = MibScalar
trackingMode = _TrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 12),
    _TrackingMode_Type()
)
trackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackingMode.setStatus("current")
_SyncStatus_Type = DisplayString
_SyncStatus_Object = MibScalar
syncStatus = _SyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 13),
    _SyncStatus_Type()
)
syncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncStatus.setStatus("current")
_Cmm4MacAddress_Type = WhispMACAddress
_Cmm4MacAddress_Object = MibScalar
cmm4MacAddress = _Cmm4MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 14),
    _Cmm4MacAddress_Type()
)
cmm4MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4MacAddress.setStatus("current")


class _Cmm4ExtEthPwrStat_Type(Integer32):
    """Custom type cmm4ExtEthPwrStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Cmm4ExtEthPwrStat_Type.__name__ = "Integer32"
_Cmm4ExtEthPwrStat_Object = MibScalar
cmm4ExtEthPwrStat = _Cmm4ExtEthPwrStat_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 15),
    _Cmm4ExtEthPwrStat_Type()
)
cmm4ExtEthPwrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4ExtEthPwrStat.setStatus("current")
_Cmm4FPGAVersion_Type = DisplayString
_Cmm4FPGAVersion_Object = MibScalar
cmm4FPGAVersion = _Cmm4FPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 16),
    _Cmm4FPGAVersion_Type()
)
cmm4FPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4FPGAVersion.setStatus("current")
_Cmm4FPGAPlatform_Type = DisplayString
_Cmm4FPGAPlatform_Object = MibScalar
cmm4FPGAPlatform = _Cmm4FPGAPlatform_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 17),
    _Cmm4FPGAPlatform_Type()
)
cmm4FPGAPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmm4FPGAPlatform.setStatus("current")


class _DefaultStatus_Type(Integer32):
    """Custom type defaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defaultPlugInserted", 1),
          ("defaultPlugInsertedAndDefaultSwitchActive", 3),
          ("defaultSwitchActive", 2),
          ("none", 0))
    )


_DefaultStatus_Type.__name__ = "Integer32"
_DefaultStatus_Object = MibScalar
defaultStatus = _DefaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 18),
    _DefaultStatus_Type()
)
defaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultStatus.setStatus("current")
_Cmm4Gps_ObjectIdentity = ObjectIdentity
cmm4Gps = _Cmm4Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4)
)
_GpsTrackingMode_Type = DisplayString
_GpsTrackingMode_Object = MibScalar
gpsTrackingMode = _GpsTrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 1),
    _GpsTrackingMode_Type()
)
gpsTrackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTrackingMode.setStatus("current")
_GpsTime_Type = DisplayString
_GpsTime_Object = MibScalar
gpsTime = _GpsTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 2),
    _GpsTime_Type()
)
gpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTime.setStatus("current")
_GpsDate_Type = DisplayString
_GpsDate_Object = MibScalar
gpsDate = _GpsDate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 3),
    _GpsDate_Type()
)
gpsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsDate.setStatus("current")
_GpsSatellitesVisible_Type = DisplayString
_GpsSatellitesVisible_Object = MibScalar
gpsSatellitesVisible = _GpsSatellitesVisible_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 4),
    _GpsSatellitesVisible_Type()
)
gpsSatellitesVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellitesVisible.setStatus("current")
_GpsSatellitesTracked_Type = DisplayString
_GpsSatellitesTracked_Object = MibScalar
gpsSatellitesTracked = _GpsSatellitesTracked_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 5),
    _GpsSatellitesTracked_Type()
)
gpsSatellitesTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellitesTracked.setStatus("current")
_GpsHeight_Type = DisplayString
_GpsHeight_Object = MibScalar
gpsHeight = _GpsHeight_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 6),
    _GpsHeight_Type()
)
gpsHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHeight.setStatus("current")
_GpsAntennaConnection_Type = DisplayString
_GpsAntennaConnection_Object = MibScalar
gpsAntennaConnection = _GpsAntennaConnection_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 7),
    _GpsAntennaConnection_Type()
)
gpsAntennaConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAntennaConnection.setStatus("current")
_GpsLatitude_Type = DisplayString
_GpsLatitude_Object = MibScalar
gpsLatitude = _GpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 8),
    _GpsLatitude_Type()
)
gpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLatitude.setStatus("current")
_GpsLongitude_Type = DisplayString
_GpsLongitude_Object = MibScalar
gpsLongitude = _GpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 9),
    _GpsLongitude_Type()
)
gpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLongitude.setStatus("current")
_GpsInvalidMsg_Type = DisplayString
_GpsInvalidMsg_Object = MibScalar
gpsInvalidMsg = _GpsInvalidMsg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 10),
    _GpsInvalidMsg_Type()
)
gpsInvalidMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsInvalidMsg.setStatus("current")
_GpsRestartCount_Type = Integer32
_GpsRestartCount_Object = MibScalar
gpsRestartCount = _GpsRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 11),
    _GpsRestartCount_Type()
)
gpsRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRestartCount.setStatus("current")
_GpsReceiverInfo_Type = DisplayString
_GpsReceiverInfo_Object = MibScalar
gpsReceiverInfo = _GpsReceiverInfo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 12),
    _GpsReceiverInfo_Type()
)
gpsReceiverInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverInfo.setStatus("current")


class _GpsSyncStatus_Type(Integer32):
    """Custom type gpsSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 2),
          ("syncOK", 1))
    )


_GpsSyncStatus_Type.__name__ = "Integer32"
_GpsSyncStatus_Object = MibScalar
gpsSyncStatus = _GpsSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 13),
    _GpsSyncStatus_Type()
)
gpsSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSyncStatus.setStatus("current")


class _GpsSyncMasterSlave_Type(Integer32):
    """Custom type gpsSyncMasterSlave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cmmIsGPSMaster", 1),
          ("cmmIsGPSSlave", 0))
    )


_GpsSyncMasterSlave_Type.__name__ = "Integer32"
_GpsSyncMasterSlave_Object = MibScalar
gpsSyncMasterSlave = _GpsSyncMasterSlave_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 14),
    _GpsSyncMasterSlave_Type()
)
gpsSyncMasterSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSyncMasterSlave.setStatus("current")
_GpsLog_Type = EventString
_GpsLog_Object = MibScalar
gpsLog = _GpsLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 15),
    _GpsLog_Type()
)
gpsLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLog.setStatus("current")
_GpsReInitCount_Type = Integer32
_GpsReInitCount_Object = MibScalar
gpsReInitCount = _GpsReInitCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 16),
    _GpsReInitCount_Type()
)
gpsReInitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReInitCount.setStatus("current")
_Cmm4EventLog_ObjectIdentity = ObjectIdentity
cmm4EventLog = _Cmm4EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 5)
)
_EventLog_Type = EventString
_EventLog_Object = MibScalar
eventLog = _EventLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 5, 1),
    _EventLog_Type()
)
eventLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLog.setStatus("current")
_NtpLog_Type = EventString
_NtpLog_Object = MibScalar
ntpLog = _NtpLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 5, 2),
    _NtpLog_Type()
)
ntpLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLog.setStatus("current")
_Cmm4Controls_ObjectIdentity = ObjectIdentity
cmm4Controls = _Cmm4Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 6)
)


class _Cmm4Reboot_Type(Integer32):
    """Custom type cmm4Reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finishedReboot", 0),
          ("reboot", 1))
    )


_Cmm4Reboot_Type.__name__ = "Integer32"
_Cmm4Reboot_Object = MibScalar
cmm4Reboot = _Cmm4Reboot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 6, 1),
    _Cmm4Reboot_Type()
)
cmm4Reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4Reboot.setStatus("current")


class _Cmm4ClearEventLog_Type(Integer32):
    """Custom type cmm4ClearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("notClear", 0))
    )


_Cmm4ClearEventLog_Type.__name__ = "Integer32"
_Cmm4ClearEventLog_Object = MibScalar
cmm4ClearEventLog = _Cmm4ClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 6, 2),
    _Cmm4ClearEventLog_Type()
)
cmm4ClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4ClearEventLog.setStatus("current")


class _Cmm4RebootIfRequired_Type(Integer32):
    """Custom type cmm4RebootIfRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rebootcomplete", 0),
          ("rebootifrquired", 1))
    )


_Cmm4RebootIfRequired_Type.__name__ = "Integer32"
_Cmm4RebootIfRequired_Object = MibScalar
cmm4RebootIfRequired = _Cmm4RebootIfRequired_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 6, 3),
    _Cmm4RebootIfRequired_Type()
)
cmm4RebootIfRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4RebootIfRequired.setStatus("current")
_Cmm4Snmp_ObjectIdentity = ObjectIdentity
cmm4Snmp = _Cmm4Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7)
)
_Cmm4SnmpComString_Type = DisplayString
_Cmm4SnmpComString_Object = MibScalar
cmm4SnmpComString = _Cmm4SnmpComString_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 1),
    _Cmm4SnmpComString_Type()
)
cmm4SnmpComString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpComString.setStatus("current")
_Cmm4SnmpAccessSubnet_Type = DisplayString
_Cmm4SnmpAccessSubnet_Object = MibScalar
cmm4SnmpAccessSubnet = _Cmm4SnmpAccessSubnet_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 2),
    _Cmm4SnmpAccessSubnet_Type()
)
cmm4SnmpAccessSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet.setStatus("current")
_Cmm4SnmpTrapIp1_Type = IpAddress
_Cmm4SnmpTrapIp1_Object = MibScalar
cmm4SnmpTrapIp1 = _Cmm4SnmpTrapIp1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 3),
    _Cmm4SnmpTrapIp1_Type()
)
cmm4SnmpTrapIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp1.setStatus("current")
_Cmm4SnmpTrapIp2_Type = IpAddress
_Cmm4SnmpTrapIp2_Object = MibScalar
cmm4SnmpTrapIp2 = _Cmm4SnmpTrapIp2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 4),
    _Cmm4SnmpTrapIp2_Type()
)
cmm4SnmpTrapIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp2.setStatus("current")
_Cmm4SnmpTrapIp3_Type = IpAddress
_Cmm4SnmpTrapIp3_Object = MibScalar
cmm4SnmpTrapIp3 = _Cmm4SnmpTrapIp3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 5),
    _Cmm4SnmpTrapIp3_Type()
)
cmm4SnmpTrapIp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp3.setStatus("current")
_Cmm4SnmpTrapIp4_Type = IpAddress
_Cmm4SnmpTrapIp4_Object = MibScalar
cmm4SnmpTrapIp4 = _Cmm4SnmpTrapIp4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 6),
    _Cmm4SnmpTrapIp4_Type()
)
cmm4SnmpTrapIp4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp4.setStatus("current")
_Cmm4SnmpTrapIp5_Type = IpAddress
_Cmm4SnmpTrapIp5_Object = MibScalar
cmm4SnmpTrapIp5 = _Cmm4SnmpTrapIp5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 7),
    _Cmm4SnmpTrapIp5_Type()
)
cmm4SnmpTrapIp5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp5.setStatus("current")
_Cmm4SnmpTrapIp6_Type = IpAddress
_Cmm4SnmpTrapIp6_Object = MibScalar
cmm4SnmpTrapIp6 = _Cmm4SnmpTrapIp6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 8),
    _Cmm4SnmpTrapIp6_Type()
)
cmm4SnmpTrapIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp6.setStatus("current")
_Cmm4SnmpTrapIp7_Type = IpAddress
_Cmm4SnmpTrapIp7_Object = MibScalar
cmm4SnmpTrapIp7 = _Cmm4SnmpTrapIp7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 9),
    _Cmm4SnmpTrapIp7_Type()
)
cmm4SnmpTrapIp7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp7.setStatus("current")
_Cmm4SnmpTrapIp8_Type = IpAddress
_Cmm4SnmpTrapIp8_Object = MibScalar
cmm4SnmpTrapIp8 = _Cmm4SnmpTrapIp8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 10),
    _Cmm4SnmpTrapIp8_Type()
)
cmm4SnmpTrapIp8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp8.setStatus("current")
_Cmm4SnmpTrapIp9_Type = IpAddress
_Cmm4SnmpTrapIp9_Object = MibScalar
cmm4SnmpTrapIp9 = _Cmm4SnmpTrapIp9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 11),
    _Cmm4SnmpTrapIp9_Type()
)
cmm4SnmpTrapIp9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp9.setStatus("current")
_Cmm4SnmpTrapIp10_Type = IpAddress
_Cmm4SnmpTrapIp10_Object = MibScalar
cmm4SnmpTrapIp10 = _Cmm4SnmpTrapIp10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 12),
    _Cmm4SnmpTrapIp10_Type()
)
cmm4SnmpTrapIp10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpTrapIp10.setStatus("current")


class _Cmm4SnmpReadOnly_Type(Integer32):
    """Custom type cmm4SnmpReadOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readOnlyPermissions", 1),
          ("readWritePermissions", 0))
    )


_Cmm4SnmpReadOnly_Type.__name__ = "Integer32"
_Cmm4SnmpReadOnly_Object = MibScalar
cmm4SnmpReadOnly = _Cmm4SnmpReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 13),
    _Cmm4SnmpReadOnly_Type()
)
cmm4SnmpReadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpReadOnly.setStatus("current")


class _Cmm4SnmpGPSSyncTrapEnable_Type(Integer32):
    """Custom type cmm4SnmpGPSSyncTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gpsSyncTrapDisabled", 0),
          ("gpsSyncTrapEnabled", 1))
    )


_Cmm4SnmpGPSSyncTrapEnable_Type.__name__ = "Integer32"
_Cmm4SnmpGPSSyncTrapEnable_Object = MibScalar
cmm4SnmpGPSSyncTrapEnable = _Cmm4SnmpGPSSyncTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 14),
    _Cmm4SnmpGPSSyncTrapEnable_Type()
)
cmm4SnmpGPSSyncTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpGPSSyncTrapEnable.setStatus("current")
_Cmm4SnmpAccessSubnet2_Type = DisplayString
_Cmm4SnmpAccessSubnet2_Object = MibScalar
cmm4SnmpAccessSubnet2 = _Cmm4SnmpAccessSubnet2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 15),
    _Cmm4SnmpAccessSubnet2_Type()
)
cmm4SnmpAccessSubnet2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet2.setStatus("current")
_Cmm4SnmpAccessSubnet3_Type = DisplayString
_Cmm4SnmpAccessSubnet3_Object = MibScalar
cmm4SnmpAccessSubnet3 = _Cmm4SnmpAccessSubnet3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 16),
    _Cmm4SnmpAccessSubnet3_Type()
)
cmm4SnmpAccessSubnet3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet3.setStatus("current")
_Cmm4SnmpAccessSubnet4_Type = DisplayString
_Cmm4SnmpAccessSubnet4_Object = MibScalar
cmm4SnmpAccessSubnet4 = _Cmm4SnmpAccessSubnet4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 17),
    _Cmm4SnmpAccessSubnet4_Type()
)
cmm4SnmpAccessSubnet4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet4.setStatus("current")
_Cmm4SnmpAccessSubnet5_Type = DisplayString
_Cmm4SnmpAccessSubnet5_Object = MibScalar
cmm4SnmpAccessSubnet5 = _Cmm4SnmpAccessSubnet5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 18),
    _Cmm4SnmpAccessSubnet5_Type()
)
cmm4SnmpAccessSubnet5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet5.setStatus("current")
_Cmm4SnmpAccessSubnet6_Type = DisplayString
_Cmm4SnmpAccessSubnet6_Object = MibScalar
cmm4SnmpAccessSubnet6 = _Cmm4SnmpAccessSubnet6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 19),
    _Cmm4SnmpAccessSubnet6_Type()
)
cmm4SnmpAccessSubnet6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet6.setStatus("current")
_Cmm4SnmpAccessSubnet7_Type = DisplayString
_Cmm4SnmpAccessSubnet7_Object = MibScalar
cmm4SnmpAccessSubnet7 = _Cmm4SnmpAccessSubnet7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 20),
    _Cmm4SnmpAccessSubnet7_Type()
)
cmm4SnmpAccessSubnet7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet7.setStatus("current")
_Cmm4SnmpAccessSubnet8_Type = DisplayString
_Cmm4SnmpAccessSubnet8_Object = MibScalar
cmm4SnmpAccessSubnet8 = _Cmm4SnmpAccessSubnet8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 21),
    _Cmm4SnmpAccessSubnet8_Type()
)
cmm4SnmpAccessSubnet8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet8.setStatus("current")
_Cmm4SnmpAccessSubnet9_Type = DisplayString
_Cmm4SnmpAccessSubnet9_Object = MibScalar
cmm4SnmpAccessSubnet9 = _Cmm4SnmpAccessSubnet9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 22),
    _Cmm4SnmpAccessSubnet9_Type()
)
cmm4SnmpAccessSubnet9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet9.setStatus("current")
_Cmm4SnmpAccessSubnet10_Type = DisplayString
_Cmm4SnmpAccessSubnet10_Object = MibScalar
cmm4SnmpAccessSubnet10 = _Cmm4SnmpAccessSubnet10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 23),
    _Cmm4SnmpAccessSubnet10_Type()
)
cmm4SnmpAccessSubnet10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm4SnmpAccessSubnet10.setStatus("current")
_Cmm4Event_ObjectIdentity = ObjectIdentity
cmm4Event = _Cmm4Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 8)
)
_Cmm4GPSEvent_ObjectIdentity = ObjectIdentity
cmm4GPSEvent = _Cmm4GPSEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 8, 1)
)
_Cmm4UserTable_Object = MibTable
cmm4UserTable = _Cmm4UserTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9)
)
if mibBuilder.loadTexts:
    cmm4UserTable.setStatus("current")
_Cmm4UserEntry_Object = MibTableRow
cmm4UserEntry = _Cmm4UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1)
)
cmm4UserEntry.setIndexNames(
    (0, "CMM4-MIB", "entryIndex"),
)
if mibBuilder.loadTexts:
    cmm4UserEntry.setStatus("current")


class _EntryIndex_Type(Integer32):
    """Custom type entryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_EntryIndex_Type.__name__ = "Integer32"
_EntryIndex_Object = MibTableColumn
entryIndex = _EntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1, 1),
    _EntryIndex_Type()
)
entryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entryIndex.setStatus("current")
_UserLoginName_Type = DisplayString
_UserLoginName_Object = MibTableColumn
userLoginName = _UserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1, 2),
    _UserLoginName_Type()
)
userLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLoginName.setStatus("current")
_UserPswd_Type = DisplayString
_UserPswd_Object = MibTableColumn
userPswd = _UserPswd_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1, 3),
    _UserPswd_Type()
)
userPswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPswd.setStatus("current")


class _AccessLevel_Type(Integer32):
    """Custom type accessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 3),
          ("engineering", 5),
          ("guest", 1),
          ("installer", 2),
          ("noAdmin", 0),
          ("technician", 4))
    )


_AccessLevel_Type.__name__ = "Integer32"
_AccessLevel_Object = MibTableColumn
accessLevel = _AccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1, 4),
    _AccessLevel_Type()
)
accessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessLevel.setStatus("current")

# Managed Objects groups

cmm4PortCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 1)
)
cmm4PortCfgGroup.setObjects(
      *(("CMM4-MIB", "portCfgIndex"),
        ("CMM4-MIB", "cmm4PortText"),
        ("CMM4-MIB", "cmm4PortDevType"),
        ("CMM4-MIB", "cmm4PortPowerCfg"),
        ("CMM4-MIB", "cmm4PortResetCfg"))
)
if mibBuilder.loadTexts:
    cmm4PortCfgGroup.setStatus("current")

cmm4ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 2)
)
cmm4ConfigGroup.setObjects(
      *(("CMM4-MIB", "gpsTimingPulse"),
        ("CMM4-MIB", "lan1Ip"),
        ("CMM4-MIB", "lan1SubnetMask"),
        ("CMM4-MIB", "defaultGateway"),
        ("CMM4-MIB", "cmm4WebAutoUpdate"),
        ("CMM4-MIB", "cmm4ExtEthPowerReset"),
        ("CMM4-MIB", "cmm4IpAccessFilter"),
        ("CMM4-MIB", "cmm4IpAccess1"),
        ("CMM4-MIB", "cmm4IpAccess2"),
        ("CMM4-MIB", "cmm4IpAccess3"),
        ("CMM4-MIB", "cmm4MgmtPortSpeed"),
        ("CMM4-MIB", "cmm4NTPServerIp"),
        ("CMM4-MIB", "sessionTimeout"),
        ("CMM4-MIB", "vlanEnable"),
        ("CMM4-MIB", "managementVID"),
        ("CMM4-MIB", "siteInfoViewable"))
)
if mibBuilder.loadTexts:
    cmm4ConfigGroup.setStatus("current")

cmm4PortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 3)
)
cmm4PortStatusGroup.setObjects(
      *(("CMM4-MIB", "portStatusIndex"),
        ("CMM4-MIB", "cmm4PortPowerStatus"))
)
if mibBuilder.loadTexts:
    cmm4PortStatusGroup.setStatus("current")

cmm4StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 4)
)
cmm4StatusGroup.setObjects(
      *(("CMM4-MIB", "deviceType"),
        ("CMM4-MIB", "cmm4pldVersion"),
        ("CMM4-MIB", "cmm4SoftwareVersion"),
        ("CMM4-MIB", "cmm4SystemTime"),
        ("CMM4-MIB", "cmm4UpTime"),
        ("CMM4-MIB", "satellitesVisible"),
        ("CMM4-MIB", "satellitesTracked"),
        ("CMM4-MIB", "latitude"),
        ("CMM4-MIB", "longitude"),
        ("CMM4-MIB", "height"),
        ("CMM4-MIB", "trackingMode"),
        ("CMM4-MIB", "syncStatus"),
        ("CMM4-MIB", "cmm4MacAddress"),
        ("CMM4-MIB", "cmm4ExtEthPwrStat"),
        ("CMM4-MIB", "cmm4FPGAVersion"),
        ("CMM4-MIB", "cmm4FPGAPlatform"),
        ("CMM4-MIB", "defaultStatus"))
)
if mibBuilder.loadTexts:
    cmm4StatusGroup.setStatus("current")

cmm4GPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 5)
)
cmm4GPSGroup.setObjects(
      *(("CMM4-MIB", "gpsTrackingMode"),
        ("CMM4-MIB", "gpsTime"),
        ("CMM4-MIB", "gpsDate"),
        ("CMM4-MIB", "gpsSatellitesVisible"),
        ("CMM4-MIB", "gpsSatellitesTracked"),
        ("CMM4-MIB", "gpsHeight"),
        ("CMM4-MIB", "gpsAntennaConnection"),
        ("CMM4-MIB", "gpsLatitude"),
        ("CMM4-MIB", "gpsLongitude"),
        ("CMM4-MIB", "gpsInvalidMsg"),
        ("CMM4-MIB", "gpsRestartCount"),
        ("CMM4-MIB", "gpsReceiverInfo"),
        ("CMM4-MIB", "gpsSyncStatus"),
        ("CMM4-MIB", "gpsSyncMasterSlave"),
        ("CMM4-MIB", "gpsLog"),
        ("CMM4-MIB", "gpsReInitCount"))
)
if mibBuilder.loadTexts:
    cmm4GPSGroup.setStatus("current")

cmm4ControlsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 6)
)
cmm4ControlsGroup.setObjects(
      *(("CMM4-MIB", "cmm4Reboot"),
        ("CMM4-MIB", "cmm4ClearEventLog"),
        ("CMM4-MIB", "cmm4RebootIfRequired"))
)
if mibBuilder.loadTexts:
    cmm4ControlsGroup.setStatus("current")

cmm4SNMPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 7)
)
cmm4SNMPGroup.setObjects(
      *(("CMM4-MIB", "cmm4SnmpComString"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet"),
        ("CMM4-MIB", "cmm4SnmpTrapIp1"),
        ("CMM4-MIB", "cmm4SnmpTrapIp2"),
        ("CMM4-MIB", "cmm4SnmpTrapIp3"),
        ("CMM4-MIB", "cmm4SnmpTrapIp4"),
        ("CMM4-MIB", "cmm4SnmpTrapIp5"),
        ("CMM4-MIB", "cmm4SnmpTrapIp6"),
        ("CMM4-MIB", "cmm4SnmpTrapIp7"),
        ("CMM4-MIB", "cmm4SnmpTrapIp8"),
        ("CMM4-MIB", "cmm4SnmpTrapIp9"),
        ("CMM4-MIB", "cmm4SnmpTrapIp10"),
        ("CMM4-MIB", "cmm4SnmpReadOnly"),
        ("CMM4-MIB", "cmm4SnmpGPSSyncTrapEnable"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet2"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet3"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet4"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet5"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet6"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet7"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet8"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet9"),
        ("CMM4-MIB", "cmm4SnmpAccessSubnet10"))
)
if mibBuilder.loadTexts:
    cmm4SNMPGroup.setStatus("current")

cmm4UserTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 8)
)
cmm4UserTableGroup.setObjects(
      *(("CMM4-MIB", "entryIndex"),
        ("CMM4-MIB", "userLoginName"),
        ("CMM4-MIB", "userPswd"),
        ("CMM4-MIB", "accessLevel"))
)
if mibBuilder.loadTexts:
    cmm4UserTableGroup.setStatus("current")


# Notification objects

cmm4GPSInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 8, 1, 1)
)
cmm4GPSInSync.setObjects(
      *(("CMM4-MIB", "gpsSyncStatus"),
        ("CMM4-MIB", "cmm4MacAddress"))
)
if mibBuilder.loadTexts:
    cmm4GPSInSync.setStatus(
        "current"
    )

cmm4GPSNoSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 8, 1, 2)
)
cmm4GPSNoSync.setObjects(
      *(("CMM4-MIB", "gpsSyncStatus"),
        ("CMM4-MIB", "cmm4MacAddress"))
)
if mibBuilder.loadTexts:
    cmm4GPSNoSync.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CMM4-MIB",
    **{"cmm4MibModule": cmm4MibModule,
       "cmm4Groups": cmm4Groups,
       "cmm4PortCfgGroup": cmm4PortCfgGroup,
       "cmm4ConfigGroup": cmm4ConfigGroup,
       "cmm4PortStatusGroup": cmm4PortStatusGroup,
       "cmm4StatusGroup": cmm4StatusGroup,
       "cmm4GPSGroup": cmm4GPSGroup,
       "cmm4ControlsGroup": cmm4ControlsGroup,
       "cmm4SNMPGroup": cmm4SNMPGroup,
       "cmm4UserTableGroup": cmm4UserTableGroup,
       "cmm4Config": cmm4Config,
       "gpsTimingPulse": gpsTimingPulse,
       "lan1Ip": lan1Ip,
       "lan1SubnetMask": lan1SubnetMask,
       "defaultGateway": defaultGateway,
       "cmm4WebAutoUpdate": cmm4WebAutoUpdate,
       "cmm4ExtEthPowerReset": cmm4ExtEthPowerReset,
       "cmm4PortCfgTable": cmm4PortCfgTable,
       "cmm4PortCfgEntry": cmm4PortCfgEntry,
       "portCfgIndex": portCfgIndex,
       "cmm4PortText": cmm4PortText,
       "cmm4PortDevType": cmm4PortDevType,
       "cmm4PortPowerCfg": cmm4PortPowerCfg,
       "cmm4PortResetCfg": cmm4PortResetCfg,
       "cmm4IpAccessFilter": cmm4IpAccessFilter,
       "cmm4IpAccess1": cmm4IpAccess1,
       "cmm4IpAccess2": cmm4IpAccess2,
       "cmm4IpAccess3": cmm4IpAccess3,
       "cmm4MgmtPortSpeed": cmm4MgmtPortSpeed,
       "cmm4NTPServerIp": cmm4NTPServerIp,
       "sessionTimeout": sessionTimeout,
       "vlanEnable": vlanEnable,
       "managementVID": managementVID,
       "siteInfoViewable": siteInfoViewable,
       "cmm4Status": cmm4Status,
       "cmm4PortStatusTable": cmm4PortStatusTable,
       "cmm4PortStatusEntry": cmm4PortStatusEntry,
       "portStatusIndex": portStatusIndex,
       "cmm4PortPowerStatus": cmm4PortPowerStatus,
       "deviceType": deviceType,
       "cmm4pldVersion": cmm4pldVersion,
       "cmm4SoftwareVersion": cmm4SoftwareVersion,
       "cmm4SystemTime": cmm4SystemTime,
       "cmm4UpTime": cmm4UpTime,
       "satellitesVisible": satellitesVisible,
       "satellitesTracked": satellitesTracked,
       "latitude": latitude,
       "longitude": longitude,
       "height": height,
       "trackingMode": trackingMode,
       "syncStatus": syncStatus,
       "cmm4MacAddress": cmm4MacAddress,
       "cmm4ExtEthPwrStat": cmm4ExtEthPwrStat,
       "cmm4FPGAVersion": cmm4FPGAVersion,
       "cmm4FPGAPlatform": cmm4FPGAPlatform,
       "defaultStatus": defaultStatus,
       "cmm4Gps": cmm4Gps,
       "gpsTrackingMode": gpsTrackingMode,
       "gpsTime": gpsTime,
       "gpsDate": gpsDate,
       "gpsSatellitesVisible": gpsSatellitesVisible,
       "gpsSatellitesTracked": gpsSatellitesTracked,
       "gpsHeight": gpsHeight,
       "gpsAntennaConnection": gpsAntennaConnection,
       "gpsLatitude": gpsLatitude,
       "gpsLongitude": gpsLongitude,
       "gpsInvalidMsg": gpsInvalidMsg,
       "gpsRestartCount": gpsRestartCount,
       "gpsReceiverInfo": gpsReceiverInfo,
       "gpsSyncStatus": gpsSyncStatus,
       "gpsSyncMasterSlave": gpsSyncMasterSlave,
       "gpsLog": gpsLog,
       "gpsReInitCount": gpsReInitCount,
       "cmm4EventLog": cmm4EventLog,
       "eventLog": eventLog,
       "ntpLog": ntpLog,
       "cmm4Controls": cmm4Controls,
       "cmm4Reboot": cmm4Reboot,
       "cmm4ClearEventLog": cmm4ClearEventLog,
       "cmm4RebootIfRequired": cmm4RebootIfRequired,
       "cmm4Snmp": cmm4Snmp,
       "cmm4SnmpComString": cmm4SnmpComString,
       "cmm4SnmpAccessSubnet": cmm4SnmpAccessSubnet,
       "cmm4SnmpTrapIp1": cmm4SnmpTrapIp1,
       "cmm4SnmpTrapIp2": cmm4SnmpTrapIp2,
       "cmm4SnmpTrapIp3": cmm4SnmpTrapIp3,
       "cmm4SnmpTrapIp4": cmm4SnmpTrapIp4,
       "cmm4SnmpTrapIp5": cmm4SnmpTrapIp5,
       "cmm4SnmpTrapIp6": cmm4SnmpTrapIp6,
       "cmm4SnmpTrapIp7": cmm4SnmpTrapIp7,
       "cmm4SnmpTrapIp8": cmm4SnmpTrapIp8,
       "cmm4SnmpTrapIp9": cmm4SnmpTrapIp9,
       "cmm4SnmpTrapIp10": cmm4SnmpTrapIp10,
       "cmm4SnmpReadOnly": cmm4SnmpReadOnly,
       "cmm4SnmpGPSSyncTrapEnable": cmm4SnmpGPSSyncTrapEnable,
       "cmm4SnmpAccessSubnet2": cmm4SnmpAccessSubnet2,
       "cmm4SnmpAccessSubnet3": cmm4SnmpAccessSubnet3,
       "cmm4SnmpAccessSubnet4": cmm4SnmpAccessSubnet4,
       "cmm4SnmpAccessSubnet5": cmm4SnmpAccessSubnet5,
       "cmm4SnmpAccessSubnet6": cmm4SnmpAccessSubnet6,
       "cmm4SnmpAccessSubnet7": cmm4SnmpAccessSubnet7,
       "cmm4SnmpAccessSubnet8": cmm4SnmpAccessSubnet8,
       "cmm4SnmpAccessSubnet9": cmm4SnmpAccessSubnet9,
       "cmm4SnmpAccessSubnet10": cmm4SnmpAccessSubnet10,
       "cmm4Event": cmm4Event,
       "cmm4GPSEvent": cmm4GPSEvent,
       "cmm4GPSInSync": cmm4GPSInSync,
       "cmm4GPSNoSync": cmm4GPSNoSync,
       "cmm4UserTable": cmm4UserTable,
       "cmm4UserEntry": cmm4UserEntry,
       "entryIndex": entryIndex,
       "userLoginName": userLoginName,
       "userPswd": userPswd,
       "accessLevel": accessLevel}
)
