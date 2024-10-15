# SNMP MIB module (VIPRINET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIPRINET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:36 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

viprinet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35424)
)
viprinet.setRevisions(
        ("2015-09-28 16:20",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VpnRouter_ObjectIdentity = ObjectIdentity
vpnRouter = _VpnRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1)
)
_VpnRouterInfo_ObjectIdentity = ObjectIdentity
vpnRouterInfo = _VpnRouterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 1)
)


class _VpnRouterName_Type(OctetString):
    """Custom type vpnRouterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_VpnRouterName_Type.__name__ = "OctetString"
_VpnRouterName_Object = MibScalar
vpnRouterName = _VpnRouterName_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 1, 1),
    _VpnRouterName_Type()
)
vpnRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterName.setStatus("current")


class _VpnRouterSerial_Type(OctetString):
    """Custom type vpnRouterSerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_VpnRouterSerial_Type.__name__ = "OctetString"
_VpnRouterSerial_Object = MibScalar
vpnRouterSerial = _VpnRouterSerial_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 1, 2),
    _VpnRouterSerial_Type()
)
vpnRouterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterSerial.setStatus("current")


class _VpnRouterModel_Type(OctetString):
    """Custom type vpnRouterModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VpnRouterModel_Type.__name__ = "OctetString"
_VpnRouterModel_Object = MibScalar
vpnRouterModel = _VpnRouterModel_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 1, 3),
    _VpnRouterModel_Type()
)
vpnRouterModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterModel.setStatus("current")


class _VpnRouterFirmware_Type(OctetString):
    """Custom type vpnRouterFirmware based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_VpnRouterFirmware_Type.__name__ = "OctetString"
_VpnRouterFirmware_Object = MibScalar
vpnRouterFirmware = _VpnRouterFirmware_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 1, 4),
    _VpnRouterFirmware_Type()
)
vpnRouterFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterFirmware.setStatus("current")


class _VpnRouterMode_Type(Integer32):
    """Custom type vpnRouterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VpnRouterMode_Type.__name__ = "Integer32"
_VpnRouterMode_Object = MibScalar
vpnRouterMode = _VpnRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 1, 5),
    _VpnRouterMode_Type()
)
vpnRouterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterMode.setStatus("current")
_VpnRouteruptime_Type = TimeTicks
_VpnRouteruptime_Object = MibScalar
vpnRouteruptime = _VpnRouteruptime_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 1, 6),
    _VpnRouteruptime_Type()
)
vpnRouteruptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouteruptime.setStatus("current")


class _VpnRouterFirmwareStatus_Type(Integer32):
    """Custom type vpnRouterFirmwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VpnRouterFirmwareStatus_Type.__name__ = "Integer32"
_VpnRouterFirmwareStatus_Object = MibScalar
vpnRouterFirmwareStatus = _VpnRouterFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 1, 7),
    _VpnRouterFirmwareStatus_Type()
)
vpnRouterFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterFirmwareStatus.setStatus("current")
_VpnRouterHealth_ObjectIdentity = ObjectIdentity
vpnRouterHealth = _VpnRouterHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 2)
)


class _VpnRouterCPULoad_Type(OctetString):
    """Custom type vpnRouterCPULoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_VpnRouterCPULoad_Type.__name__ = "OctetString"
_VpnRouterCPULoad_Object = MibScalar
vpnRouterCPULoad = _VpnRouterCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 2, 1),
    _VpnRouterCPULoad_Type()
)
vpnRouterCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterCPULoad.setStatus("current")
_VpnRouterMemoryUsage_Type = Integer32
_VpnRouterMemoryUsage_Object = MibScalar
vpnRouterMemoryUsage = _VpnRouterMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 2, 2),
    _VpnRouterMemoryUsage_Type()
)
vpnRouterMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterMemoryUsage.setStatus("current")


class _VpnRouterSystemTemperature_Type(Integer32):
    """Custom type vpnRouterSystemTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VpnRouterSystemTemperature_Type.__name__ = "Integer32"
_VpnRouterSystemTemperature_Object = MibScalar
vpnRouterSystemTemperature = _VpnRouterSystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 2, 3),
    _VpnRouterSystemTemperature_Type()
)
vpnRouterSystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterSystemTemperature.setStatus("current")


class _VpnRouterCPUTemperature_Type(Integer32):
    """Custom type vpnRouterCPUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VpnRouterCPUTemperature_Type.__name__ = "Integer32"
_VpnRouterCPUTemperature_Object = MibScalar
vpnRouterCPUTemperature = _VpnRouterCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 2, 4),
    _VpnRouterCPUTemperature_Type()
)
vpnRouterCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterCPUTemperature.setStatus("current")


class _VpnRouterPowerSupplyFailure_Type(Integer32):
    """Custom type vpnRouterPowerSupplyFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpnRouterPowerSupplyFailure_Type.__name__ = "Integer32"
_VpnRouterPowerSupplyFailure_Object = MibScalar
vpnRouterPowerSupplyFailure = _VpnRouterPowerSupplyFailure_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 2, 5),
    _VpnRouterPowerSupplyFailure_Type()
)
vpnRouterPowerSupplyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterPowerSupplyFailure.setStatus("current")
_VpnRouterFans_ObjectIdentity = ObjectIdentity
vpnRouterFans = _VpnRouterFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 3)
)
_VpnRouterFanCount_Type = Integer32
_VpnRouterFanCount_Object = MibScalar
vpnRouterFanCount = _VpnRouterFanCount_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 3, 1),
    _VpnRouterFanCount_Type()
)
vpnRouterFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterFanCount.setStatus("current")
_VpnRouterFanTable_Object = MibTable
vpnRouterFanTable = _VpnRouterFanTable_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 3, 2)
)
if mibBuilder.loadTexts:
    vpnRouterFanTable.setStatus("current")
_VpnRouterFanEntry_Object = MibTableRow
vpnRouterFanEntry = _VpnRouterFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1)
)
vpnRouterFanEntry.setIndexNames(
    (0, "VIPRINET-MIB", "vpnRouterFanIndex"),
)
if mibBuilder.loadTexts:
    vpnRouterFanEntry.setStatus("current")


class _VpnRouterFanIndex_Type(Integer32):
    """Custom type vpnRouterFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VpnRouterFanIndex_Type.__name__ = "Integer32"
_VpnRouterFanIndex_Object = MibTableColumn
vpnRouterFanIndex = _VpnRouterFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1, 1),
    _VpnRouterFanIndex_Type()
)
vpnRouterFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpnRouterFanIndex.setStatus("current")


class _VpnRouterFanAdminStatus_Type(Integer32):
    """Custom type vpnRouterFanAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpnRouterFanAdminStatus_Type.__name__ = "Integer32"
_VpnRouterFanAdminStatus_Object = MibTableColumn
vpnRouterFanAdminStatus = _VpnRouterFanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1, 2),
    _VpnRouterFanAdminStatus_Type()
)
vpnRouterFanAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterFanAdminStatus.setStatus("current")


class _VpnRouterFanOperativeStatus_Type(Integer32):
    """Custom type vpnRouterFanOperativeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VpnRouterFanOperativeStatus_Type.__name__ = "Integer32"
_VpnRouterFanOperativeStatus_Object = MibTableColumn
vpnRouterFanOperativeStatus = _VpnRouterFanOperativeStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1, 3),
    _VpnRouterFanOperativeStatus_Type()
)
vpnRouterFanOperativeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterFanOperativeStatus.setStatus("current")


class _VpnRouterFanRPM_Type(Integer32):
    """Custom type vpnRouterFanRPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VpnRouterFanRPM_Type.__name__ = "Integer32"
_VpnRouterFanRPM_Object = MibTableColumn
vpnRouterFanRPM = _VpnRouterFanRPM_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1, 4),
    _VpnRouterFanRPM_Type()
)
vpnRouterFanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterFanRPM.setStatus("current")
_VpnRouterInterfaces_ObjectIdentity = ObjectIdentity
vpnRouterInterfaces = _VpnRouterInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4)
)
_VpnRouterInterfaceCount_Type = Integer32
_VpnRouterInterfaceCount_Object = MibScalar
vpnRouterInterfaceCount = _VpnRouterInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 1),
    _VpnRouterInterfaceCount_Type()
)
vpnRouterInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceCount.setStatus("current")
_VpnRouterInterfaceTable_Object = MibTable
vpnRouterInterfaceTable = _VpnRouterInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2)
)
if mibBuilder.loadTexts:
    vpnRouterInterfaceTable.setStatus("current")
_VpnRouterInterfaceEntry_Object = MibTableRow
vpnRouterInterfaceEntry = _VpnRouterInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1)
)
vpnRouterInterfaceEntry.setIndexNames(
    (0, "VIPRINET-MIB", "vpnRouterInterfaceIndex"),
)
if mibBuilder.loadTexts:
    vpnRouterInterfaceEntry.setStatus("current")


class _VpnRouterInterfaceIndex_Type(Integer32):
    """Custom type vpnRouterInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VpnRouterInterfaceIndex_Type.__name__ = "Integer32"
_VpnRouterInterfaceIndex_Object = MibTableColumn
vpnRouterInterfaceIndex = _VpnRouterInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 1),
    _VpnRouterInterfaceIndex_Type()
)
vpnRouterInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpnRouterInterfaceIndex.setStatus("current")
_VpnRouterInterfaceName_Type = DisplayString
_VpnRouterInterfaceName_Object = MibTableColumn
vpnRouterInterfaceName = _VpnRouterInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 2),
    _VpnRouterInterfaceName_Type()
)
vpnRouterInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceName.setStatus("current")


class _VpnRouterInterfaceAdminStatus_Type(Integer32):
    """Custom type vpnRouterInterfaceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpnRouterInterfaceAdminStatus_Type.__name__ = "Integer32"
_VpnRouterInterfaceAdminStatus_Object = MibTableColumn
vpnRouterInterfaceAdminStatus = _VpnRouterInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 3),
    _VpnRouterInterfaceAdminStatus_Type()
)
vpnRouterInterfaceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceAdminStatus.setStatus("current")


class _VpnRouterInterfaceOperativeStatus_Type(Integer32):
    """Custom type vpnRouterInterfaceOperativeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VpnRouterInterfaceOperativeStatus_Type.__name__ = "Integer32"
_VpnRouterInterfaceOperativeStatus_Object = MibTableColumn
vpnRouterInterfaceOperativeStatus = _VpnRouterInterfaceOperativeStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 4),
    _VpnRouterInterfaceOperativeStatus_Type()
)
vpnRouterInterfaceOperativeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceOperativeStatus.setStatus("current")
_VpnRouterInterfaceBandwidthToWan_Type = Integer32
_VpnRouterInterfaceBandwidthToWan_Object = MibTableColumn
vpnRouterInterfaceBandwidthToWan = _VpnRouterInterfaceBandwidthToWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 5),
    _VpnRouterInterfaceBandwidthToWan_Type()
)
vpnRouterInterfaceBandwidthToWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceBandwidthToWan.setStatus("current")
_VpnRouterInterfaceBandwidthFromWan_Type = Integer32
_VpnRouterInterfaceBandwidthFromWan_Object = MibTableColumn
vpnRouterInterfaceBandwidthFromWan = _VpnRouterInterfaceBandwidthFromWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 6),
    _VpnRouterInterfaceBandwidthFromWan_Type()
)
vpnRouterInterfaceBandwidthFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceBandwidthFromWan.setStatus("current")
_VpnRouterInterfaceTrafficUp_Type = Counter32
_VpnRouterInterfaceTrafficUp_Object = MibTableColumn
vpnRouterInterfaceTrafficUp = _VpnRouterInterfaceTrafficUp_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 7),
    _VpnRouterInterfaceTrafficUp_Type()
)
vpnRouterInterfaceTrafficUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceTrafficUp.setStatus("current")
_VpnRouterInterfaceTrafficDown_Type = Counter32
_VpnRouterInterfaceTrafficDown_Object = MibTableColumn
vpnRouterInterfaceTrafficDown = _VpnRouterInterfaceTrafficDown_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 8),
    _VpnRouterInterfaceTrafficDown_Type()
)
vpnRouterInterfaceTrafficDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceTrafficDown.setStatus("current")
_VpnRouterInterfaceSignalStrength_Type = Integer32
_VpnRouterInterfaceSignalStrength_Object = MibTableColumn
vpnRouterInterfaceSignalStrength = _VpnRouterInterfaceSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 9),
    _VpnRouterInterfaceSignalStrength_Type()
)
vpnRouterInterfaceSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceSignalStrength.setStatus("current")
_VpnRouterInterfaceServiceType_Type = DisplayString
_VpnRouterInterfaceServiceType_Object = MibTableColumn
vpnRouterInterfaceServiceType = _VpnRouterInterfaceServiceType_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 10),
    _VpnRouterInterfaceServiceType_Type()
)
vpnRouterInterfaceServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceServiceType.setStatus("current")
_VpnRouterInterfaceServiceStatus_Type = DisplayString
_VpnRouterInterfaceServiceStatus_Object = MibTableColumn
vpnRouterInterfaceServiceStatus = _VpnRouterInterfaceServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 11),
    _VpnRouterInterfaceServiceStatus_Type()
)
vpnRouterInterfaceServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceServiceStatus.setStatus("current")


class _VpnRouterInterfaceRoaming_Type(Integer32):
    """Custom type vpnRouterInterfaceRoaming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpnRouterInterfaceRoaming_Type.__name__ = "Integer32"
_VpnRouterInterfaceRoaming_Object = MibTableColumn
vpnRouterInterfaceRoaming = _VpnRouterInterfaceRoaming_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 12),
    _VpnRouterInterfaceRoaming_Type()
)
vpnRouterInterfaceRoaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceRoaming.setStatus("current")
_VpnRouterInterfaceNetworkName_Type = DisplayString
_VpnRouterInterfaceNetworkName_Object = MibTableColumn
vpnRouterInterfaceNetworkName = _VpnRouterInterfaceNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 13),
    _VpnRouterInterfaceNetworkName_Type()
)
vpnRouterInterfaceNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceNetworkName.setStatus("current")
_VpnRouterInterfaceBandInfo_Type = DisplayString
_VpnRouterInterfaceBandInfo_Object = MibTableColumn
vpnRouterInterfaceBandInfo = _VpnRouterInterfaceBandInfo_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 14),
    _VpnRouterInterfaceBandInfo_Type()
)
vpnRouterInterfaceBandInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceBandInfo.setStatus("current")
_VpnRouterInterfaceIMSI_Type = DisplayString
_VpnRouterInterfaceIMSI_Object = MibTableColumn
vpnRouterInterfaceIMSI = _VpnRouterInterfaceIMSI_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 15),
    _VpnRouterInterfaceIMSI_Type()
)
vpnRouterInterfaceIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceIMSI.setStatus("current")
_VpnRouterInterfaceIMEI_Type = DisplayString
_VpnRouterInterfaceIMEI_Object = MibTableColumn
vpnRouterInterfaceIMEI = _VpnRouterInterfaceIMEI_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 16),
    _VpnRouterInterfaceIMEI_Type()
)
vpnRouterInterfaceIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceIMEI.setStatus("current")
_VpnRouterInterfacePINStatus_Type = DisplayString
_VpnRouterInterfacePINStatus_Object = MibTableColumn
vpnRouterInterfacePINStatus = _VpnRouterInterfacePINStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 17),
    _VpnRouterInterfacePINStatus_Type()
)
vpnRouterInterfacePINStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfacePINStatus.setStatus("current")
_VpnRouterInterfaceRFBand_Type = Integer32
_VpnRouterInterfaceRFBand_Object = MibTableColumn
vpnRouterInterfaceRFBand = _VpnRouterInterfaceRFBand_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 18),
    _VpnRouterInterfaceRFBand_Type()
)
vpnRouterInterfaceRFBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceRFBand.setStatus("current")
_VpnRouterInterfaceRFChannel_Type = Integer32
_VpnRouterInterfaceRFChannel_Object = MibTableColumn
vpnRouterInterfaceRFChannel = _VpnRouterInterfaceRFChannel_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 19),
    _VpnRouterInterfaceRFChannel_Type()
)
vpnRouterInterfaceRFChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceRFChannel.setStatus("current")
_VpnRouterInterfaceSyncrateUpstream_Type = Counter32
_VpnRouterInterfaceSyncrateUpstream_Object = MibTableColumn
vpnRouterInterfaceSyncrateUpstream = _VpnRouterInterfaceSyncrateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 20),
    _VpnRouterInterfaceSyncrateUpstream_Type()
)
vpnRouterInterfaceSyncrateUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceSyncrateUpstream.setStatus("current")
_VpnRouterInterfaceSyncrateDownstream_Type = Counter32
_VpnRouterInterfaceSyncrateDownstream_Object = MibTableColumn
vpnRouterInterfaceSyncrateDownstream = _VpnRouterInterfaceSyncrateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 21),
    _VpnRouterInterfaceSyncrateDownstream_Type()
)
vpnRouterInterfaceSyncrateDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterInterfaceSyncrateDownstream.setStatus("current")
_VpnRouterTunnels_ObjectIdentity = ObjectIdentity
vpnRouterTunnels = _VpnRouterTunnels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5)
)
_VpnRouterTunnelCount_Type = Integer32
_VpnRouterTunnelCount_Object = MibScalar
vpnRouterTunnelCount = _VpnRouterTunnelCount_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 1),
    _VpnRouterTunnelCount_Type()
)
vpnRouterTunnelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelCount.setStatus("current")
_VpnRouterTunnelTable_Object = MibTable
vpnRouterTunnelTable = _VpnRouterTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2)
)
if mibBuilder.loadTexts:
    vpnRouterTunnelTable.setStatus("current")
_VpnRouterTunnelEntry_Object = MibTableRow
vpnRouterTunnelEntry = _VpnRouterTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1)
)
vpnRouterTunnelEntry.setIndexNames(
    (0, "VIPRINET-MIB", "vpnRouterTunnelIndex"),
)
if mibBuilder.loadTexts:
    vpnRouterTunnelEntry.setStatus("current")


class _VpnRouterTunnelIndex_Type(Integer32):
    """Custom type vpnRouterTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VpnRouterTunnelIndex_Type.__name__ = "Integer32"
_VpnRouterTunnelIndex_Object = MibTableColumn
vpnRouterTunnelIndex = _VpnRouterTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 1),
    _VpnRouterTunnelIndex_Type()
)
vpnRouterTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpnRouterTunnelIndex.setStatus("current")
_VpnRouterTunnelName_Type = DisplayString
_VpnRouterTunnelName_Object = MibTableColumn
vpnRouterTunnelName = _VpnRouterTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 2),
    _VpnRouterTunnelName_Type()
)
vpnRouterTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelName.setStatus("current")


class _VpnRouterTunnelAdminStatus_Type(Integer32):
    """Custom type vpnRouterTunnelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpnRouterTunnelAdminStatus_Type.__name__ = "Integer32"
_VpnRouterTunnelAdminStatus_Object = MibTableColumn
vpnRouterTunnelAdminStatus = _VpnRouterTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 3),
    _VpnRouterTunnelAdminStatus_Type()
)
vpnRouterTunnelAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelAdminStatus.setStatus("current")


class _VpnRouterTunnelOperativeStatus_Type(Integer32):
    """Custom type vpnRouterTunnelOperativeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpnRouterTunnelOperativeStatus_Type.__name__ = "Integer32"
_VpnRouterTunnelOperativeStatus_Object = MibTableColumn
vpnRouterTunnelOperativeStatus = _VpnRouterTunnelOperativeStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 4),
    _VpnRouterTunnelOperativeStatus_Type()
)
vpnRouterTunnelOperativeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelOperativeStatus.setStatus("current")
_VpnRouterTunnelCumulatedBandwidthToWan_Type = Integer32
_VpnRouterTunnelCumulatedBandwidthToWan_Object = MibTableColumn
vpnRouterTunnelCumulatedBandwidthToWan = _VpnRouterTunnelCumulatedBandwidthToWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 5),
    _VpnRouterTunnelCumulatedBandwidthToWan_Type()
)
vpnRouterTunnelCumulatedBandwidthToWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelCumulatedBandwidthToWan.setStatus("current")
_VpnRouterTunnelCumulatedBandwidthFromWan_Type = Integer32
_VpnRouterTunnelCumulatedBandwidthFromWan_Object = MibTableColumn
vpnRouterTunnelCumulatedBandwidthFromWan = _VpnRouterTunnelCumulatedBandwidthFromWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 6),
    _VpnRouterTunnelCumulatedBandwidthFromWan_Type()
)
vpnRouterTunnelCumulatedBandwidthFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelCumulatedBandwidthFromWan.setStatus("current")
_VpnRouterTunnelCurrentCumulatedBandwidthToWan_Type = Integer32
_VpnRouterTunnelCurrentCumulatedBandwidthToWan_Object = MibTableColumn
vpnRouterTunnelCurrentCumulatedBandwidthToWan = _VpnRouterTunnelCurrentCumulatedBandwidthToWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 7),
    _VpnRouterTunnelCurrentCumulatedBandwidthToWan_Type()
)
vpnRouterTunnelCurrentCumulatedBandwidthToWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelCurrentCumulatedBandwidthToWan.setStatus("current")
_VpnRouterTunnelCurrentCumulatedBandwidthFromWan_Type = Integer32
_VpnRouterTunnelCurrentCumulatedBandwidthFromWan_Object = MibTableColumn
vpnRouterTunnelCurrentCumulatedBandwidthFromWan = _VpnRouterTunnelCurrentCumulatedBandwidthFromWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 8),
    _VpnRouterTunnelCurrentCumulatedBandwidthFromWan_Type()
)
vpnRouterTunnelCurrentCumulatedBandwidthFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelCurrentCumulatedBandwidthFromWan.setStatus("current")
_VpnRouterTunnelTrafficUp_Type = Counter32
_VpnRouterTunnelTrafficUp_Object = MibTableColumn
vpnRouterTunnelTrafficUp = _VpnRouterTunnelTrafficUp_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 9),
    _VpnRouterTunnelTrafficUp_Type()
)
vpnRouterTunnelTrafficUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelTrafficUp.setStatus("current")
_VpnRouterTunnelTrafficDown_Type = Counter32
_VpnRouterTunnelTrafficDown_Object = MibTableColumn
vpnRouterTunnelTrafficDown = _VpnRouterTunnelTrafficDown_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 10),
    _VpnRouterTunnelTrafficDown_Type()
)
vpnRouterTunnelTrafficDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelTrafficDown.setStatus("current")
_VpnRouterTunnelRemoteRouterSerial_Type = DisplayString
_VpnRouterTunnelRemoteRouterSerial_Object = MibTableColumn
vpnRouterTunnelRemoteRouterSerial = _VpnRouterTunnelRemoteRouterSerial_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 11),
    _VpnRouterTunnelRemoteRouterSerial_Type()
)
vpnRouterTunnelRemoteRouterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelRemoteRouterSerial.setStatus("current")
_VpnRouterTunnelChannels_ObjectIdentity = ObjectIdentity
vpnRouterTunnelChannels = _VpnRouterTunnelChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6)
)
_VpnRouterTunnelChannelCount_Type = Integer32
_VpnRouterTunnelChannelCount_Object = MibScalar
vpnRouterTunnelChannelCount = _VpnRouterTunnelChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 1),
    _VpnRouterTunnelChannelCount_Type()
)
vpnRouterTunnelChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelCount.setStatus("current")
_VpnRouterTunnelChannelTable_Object = MibTable
vpnRouterTunnelChannelTable = _VpnRouterTunnelChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2)
)
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelTable.setStatus("current")
_VpnRouterTunnelChannelEntry_Object = MibTableRow
vpnRouterTunnelChannelEntry = _VpnRouterTunnelChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1)
)
vpnRouterTunnelChannelEntry.setIndexNames(
    (0, "VIPRINET-MIB", "vpnRouterTunnelChannelIndex"),
)
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelEntry.setStatus("current")


class _VpnRouterTunnelChannelIndex_Type(Integer32):
    """Custom type vpnRouterTunnelChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VpnRouterTunnelChannelIndex_Type.__name__ = "Integer32"
_VpnRouterTunnelChannelIndex_Object = MibTableColumn
vpnRouterTunnelChannelIndex = _VpnRouterTunnelChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 1),
    _VpnRouterTunnelChannelIndex_Type()
)
vpnRouterTunnelChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelIndex.setStatus("current")
_VpnRouterTunnelChannelName_Type = DisplayString
_VpnRouterTunnelChannelName_Object = MibTableColumn
vpnRouterTunnelChannelName = _VpnRouterTunnelChannelName_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 2),
    _VpnRouterTunnelChannelName_Type()
)
vpnRouterTunnelChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelName.setStatus("current")


class _VpnRouterTunnelChannelAdminStatus_Type(Integer32):
    """Custom type vpnRouterTunnelChannelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpnRouterTunnelChannelAdminStatus_Type.__name__ = "Integer32"
_VpnRouterTunnelChannelAdminStatus_Object = MibTableColumn
vpnRouterTunnelChannelAdminStatus = _VpnRouterTunnelChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 3),
    _VpnRouterTunnelChannelAdminStatus_Type()
)
vpnRouterTunnelChannelAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelAdminStatus.setStatus("current")


class _VpnRouterTunnelChannelOperativeStatus_Type(Integer32):
    """Custom type vpnRouterTunnelChannelOperativeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VpnRouterTunnelChannelOperativeStatus_Type.__name__ = "Integer32"
_VpnRouterTunnelChannelOperativeStatus_Object = MibTableColumn
vpnRouterTunnelChannelOperativeStatus = _VpnRouterTunnelChannelOperativeStatus_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 4),
    _VpnRouterTunnelChannelOperativeStatus_Type()
)
vpnRouterTunnelChannelOperativeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelOperativeStatus.setStatus("current")
_VpnRouterTunnelChannelMaxBandwidthToWan_Type = Integer32
_VpnRouterTunnelChannelMaxBandwidthToWan_Object = MibTableColumn
vpnRouterTunnelChannelMaxBandwidthToWan = _VpnRouterTunnelChannelMaxBandwidthToWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 5),
    _VpnRouterTunnelChannelMaxBandwidthToWan_Type()
)
vpnRouterTunnelChannelMaxBandwidthToWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelMaxBandwidthToWan.setStatus("current")
_VpnRouterTunnelChannelMaxBandwidthFromWan_Type = Integer32
_VpnRouterTunnelChannelMaxBandwidthFromWan_Object = MibTableColumn
vpnRouterTunnelChannelMaxBandwidthFromWan = _VpnRouterTunnelChannelMaxBandwidthFromWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 6),
    _VpnRouterTunnelChannelMaxBandwidthFromWan_Type()
)
vpnRouterTunnelChannelMaxBandwidthFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelMaxBandwidthFromWan.setStatus("current")
_VpnRouterTunnelChannelCurrentBandwidthToWan_Type = Integer32
_VpnRouterTunnelChannelCurrentBandwidthToWan_Object = MibTableColumn
vpnRouterTunnelChannelCurrentBandwidthToWan = _VpnRouterTunnelChannelCurrentBandwidthToWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 7),
    _VpnRouterTunnelChannelCurrentBandwidthToWan_Type()
)
vpnRouterTunnelChannelCurrentBandwidthToWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelCurrentBandwidthToWan.setStatus("current")
_VpnRouterTunnelChannelCurrentBandwidthFromWan_Type = Integer32
_VpnRouterTunnelChannelCurrentBandwidthFromWan_Object = MibTableColumn
vpnRouterTunnelChannelCurrentBandwidthFromWan = _VpnRouterTunnelChannelCurrentBandwidthFromWan_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 8),
    _VpnRouterTunnelChannelCurrentBandwidthFromWan_Type()
)
vpnRouterTunnelChannelCurrentBandwidthFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelCurrentBandwidthFromWan.setStatus("current")
_VpnRouterTunnelChannelTrafficUp_Type = Counter32
_VpnRouterTunnelChannelTrafficUp_Object = MibTableColumn
vpnRouterTunnelChannelTrafficUp = _VpnRouterTunnelChannelTrafficUp_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 9),
    _VpnRouterTunnelChannelTrafficUp_Type()
)
vpnRouterTunnelChannelTrafficUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelTrafficUp.setStatus("current")
_VpnRouterTunnelChannelTrafficDown_Type = Counter32
_VpnRouterTunnelChannelTrafficDown_Object = MibTableColumn
vpnRouterTunnelChannelTrafficDown = _VpnRouterTunnelChannelTrafficDown_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 10),
    _VpnRouterTunnelChannelTrafficDown_Type()
)
vpnRouterTunnelChannelTrafficDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelTrafficDown.setStatus("current")
_VpnRouterTunnelChannelReferencedTunnel_Type = Integer32
_VpnRouterTunnelChannelReferencedTunnel_Object = MibTableColumn
vpnRouterTunnelChannelReferencedTunnel = _VpnRouterTunnelChannelReferencedTunnel_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 11),
    _VpnRouterTunnelChannelReferencedTunnel_Type()
)
vpnRouterTunnelChannelReferencedTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelReferencedTunnel.setStatus("current")


class _VpnRouterTunnelChannelIsBackup_Type(Integer32):
    """Custom type vpnRouterTunnelChannelIsBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpnRouterTunnelChannelIsBackup_Type.__name__ = "Integer32"
_VpnRouterTunnelChannelIsBackup_Object = MibTableColumn
vpnRouterTunnelChannelIsBackup = _VpnRouterTunnelChannelIsBackup_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 12),
    _VpnRouterTunnelChannelIsBackup_Type()
)
vpnRouterTunnelChannelIsBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelIsBackup.setStatus("current")


class _VpnRouterTunnelChannelModuleSlot_Type(Integer32):
    """Custom type vpnRouterTunnelChannelModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_VpnRouterTunnelChannelModuleSlot_Type.__name__ = "Integer32"
_VpnRouterTunnelChannelModuleSlot_Object = MibTableColumn
vpnRouterTunnelChannelModuleSlot = _VpnRouterTunnelChannelModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 13),
    _VpnRouterTunnelChannelModuleSlot_Type()
)
vpnRouterTunnelChannelModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelModuleSlot.setStatus("current")


class _VpnRouterTunnelChannelPacketLoss_Type(Integer32):
    """Custom type vpnRouterTunnelChannelPacketLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VpnRouterTunnelChannelPacketLoss_Type.__name__ = "Integer32"
_VpnRouterTunnelChannelPacketLoss_Object = MibTableColumn
vpnRouterTunnelChannelPacketLoss = _VpnRouterTunnelChannelPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 14),
    _VpnRouterTunnelChannelPacketLoss_Type()
)
vpnRouterTunnelChannelPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelPacketLoss.setStatus("current")


class _VpnRouterTunnelChannelLinkStability_Type(Integer32):
    """Custom type vpnRouterTunnelChannelLinkStability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VpnRouterTunnelChannelLinkStability_Type.__name__ = "Integer32"
_VpnRouterTunnelChannelLinkStability_Object = MibTableColumn
vpnRouterTunnelChannelLinkStability = _VpnRouterTunnelChannelLinkStability_Object(
    (1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 15),
    _VpnRouterTunnelChannelLinkStability_Type()
)
vpnRouterTunnelChannelLinkStability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnRouterTunnelChannelLinkStability.setStatus("current")
_VpnRouterConformance_ObjectIdentity = ObjectIdentity
vpnRouterConformance = _VpnRouterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 7)
)
_VpnRouterGroups_ObjectIdentity = ObjectIdentity
vpnRouterGroups = _VpnRouterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 7, 1)
)
_VpnRouterCompliances_ObjectIdentity = ObjectIdentity
vpnRouterCompliances = _VpnRouterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35424, 1, 7, 2)
)

# Managed Objects groups

vpnRouterObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35424, 1, 7, 1, 1)
)
vpnRouterObjects.setObjects(
      *(("VIPRINET-MIB", "vpnRouterTunnelChannelName"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelAdminStatus"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelOperativeStatus"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelMaxBandwidthToWan"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelMaxBandwidthFromWan"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelCurrentBandwidthToWan"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelCurrentBandwidthFromWan"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelTrafficUp"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelTrafficDown"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelReferencedTunnel"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelIsBackup"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelModuleSlot"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelPacketLoss"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelLinkStability"),
        ("VIPRINET-MIB", "vpnRouterTunnelName"),
        ("VIPRINET-MIB", "vpnRouterTunnelAdminStatus"),
        ("VIPRINET-MIB", "vpnRouterTunnelOperativeStatus"),
        ("VIPRINET-MIB", "vpnRouterTunnelCumulatedBandwidthToWan"),
        ("VIPRINET-MIB", "vpnRouterTunnelCumulatedBandwidthFromWan"),
        ("VIPRINET-MIB", "vpnRouterTunnelCurrentCumulatedBandwidthToWan"),
        ("VIPRINET-MIB", "vpnRouterTunnelCurrentCumulatedBandwidthFromWan"),
        ("VIPRINET-MIB", "vpnRouterTunnelTrafficUp"),
        ("VIPRINET-MIB", "vpnRouterTunnelTrafficDown"),
        ("VIPRINET-MIB", "vpnRouterTunnelRemoteRouterSerial"),
        ("VIPRINET-MIB", "vpnRouterInterfaceName"),
        ("VIPRINET-MIB", "vpnRouterInterfaceAdminStatus"),
        ("VIPRINET-MIB", "vpnRouterInterfaceOperativeStatus"),
        ("VIPRINET-MIB", "vpnRouterInterfaceBandwidthToWan"),
        ("VIPRINET-MIB", "vpnRouterInterfaceBandwidthFromWan"),
        ("VIPRINET-MIB", "vpnRouterInterfaceTrafficUp"),
        ("VIPRINET-MIB", "vpnRouterInterfaceTrafficDown"),
        ("VIPRINET-MIB", "vpnRouterFanAdminStatus"),
        ("VIPRINET-MIB", "vpnRouterFanOperativeStatus"),
        ("VIPRINET-MIB", "vpnRouterFanRPM"),
        ("VIPRINET-MIB", "vpnRouterName"),
        ("VIPRINET-MIB", "vpnRouterSerial"),
        ("VIPRINET-MIB", "vpnRouterModel"),
        ("VIPRINET-MIB", "vpnRouterFirmware"),
        ("VIPRINET-MIB", "vpnRouterMode"),
        ("VIPRINET-MIB", "vpnRouteruptime"),
        ("VIPRINET-MIB", "vpnRouterFirmwareStatus"),
        ("VIPRINET-MIB", "vpnRouterCPULoad"),
        ("VIPRINET-MIB", "vpnRouterMemoryUsage"),
        ("VIPRINET-MIB", "vpnRouterSystemTemperature"),
        ("VIPRINET-MIB", "vpnRouterCPUTemperature"),
        ("VIPRINET-MIB", "vpnRouterPowerSupplyFailure"),
        ("VIPRINET-MIB", "vpnRouterFanCount"),
        ("VIPRINET-MIB", "vpnRouterInterfaceCount"),
        ("VIPRINET-MIB", "vpnRouterTunnelCount"),
        ("VIPRINET-MIB", "vpnRouterTunnelChannelCount"))
)
if mibBuilder.loadTexts:
    vpnRouterObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vpnRouterReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35424, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vpnRouterReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPRINET-MIB",
    **{"viprinet": viprinet,
       "vpnRouter": vpnRouter,
       "vpnRouterInfo": vpnRouterInfo,
       "vpnRouterName": vpnRouterName,
       "vpnRouterSerial": vpnRouterSerial,
       "vpnRouterModel": vpnRouterModel,
       "vpnRouterFirmware": vpnRouterFirmware,
       "vpnRouterMode": vpnRouterMode,
       "vpnRouteruptime": vpnRouteruptime,
       "vpnRouterFirmwareStatus": vpnRouterFirmwareStatus,
       "vpnRouterHealth": vpnRouterHealth,
       "vpnRouterCPULoad": vpnRouterCPULoad,
       "vpnRouterMemoryUsage": vpnRouterMemoryUsage,
       "vpnRouterSystemTemperature": vpnRouterSystemTemperature,
       "vpnRouterCPUTemperature": vpnRouterCPUTemperature,
       "vpnRouterPowerSupplyFailure": vpnRouterPowerSupplyFailure,
       "vpnRouterFans": vpnRouterFans,
       "vpnRouterFanCount": vpnRouterFanCount,
       "vpnRouterFanTable": vpnRouterFanTable,
       "vpnRouterFanEntry": vpnRouterFanEntry,
       "vpnRouterFanIndex": vpnRouterFanIndex,
       "vpnRouterFanAdminStatus": vpnRouterFanAdminStatus,
       "vpnRouterFanOperativeStatus": vpnRouterFanOperativeStatus,
       "vpnRouterFanRPM": vpnRouterFanRPM,
       "vpnRouterInterfaces": vpnRouterInterfaces,
       "vpnRouterInterfaceCount": vpnRouterInterfaceCount,
       "vpnRouterInterfaceTable": vpnRouterInterfaceTable,
       "vpnRouterInterfaceEntry": vpnRouterInterfaceEntry,
       "vpnRouterInterfaceIndex": vpnRouterInterfaceIndex,
       "vpnRouterInterfaceName": vpnRouterInterfaceName,
       "vpnRouterInterfaceAdminStatus": vpnRouterInterfaceAdminStatus,
       "vpnRouterInterfaceOperativeStatus": vpnRouterInterfaceOperativeStatus,
       "vpnRouterInterfaceBandwidthToWan": vpnRouterInterfaceBandwidthToWan,
       "vpnRouterInterfaceBandwidthFromWan": vpnRouterInterfaceBandwidthFromWan,
       "vpnRouterInterfaceTrafficUp": vpnRouterInterfaceTrafficUp,
       "vpnRouterInterfaceTrafficDown": vpnRouterInterfaceTrafficDown,
       "vpnRouterInterfaceSignalStrength": vpnRouterInterfaceSignalStrength,
       "vpnRouterInterfaceServiceType": vpnRouterInterfaceServiceType,
       "vpnRouterInterfaceServiceStatus": vpnRouterInterfaceServiceStatus,
       "vpnRouterInterfaceRoaming": vpnRouterInterfaceRoaming,
       "vpnRouterInterfaceNetworkName": vpnRouterInterfaceNetworkName,
       "vpnRouterInterfaceBandInfo": vpnRouterInterfaceBandInfo,
       "vpnRouterInterfaceIMSI": vpnRouterInterfaceIMSI,
       "vpnRouterInterfaceIMEI": vpnRouterInterfaceIMEI,
       "vpnRouterInterfacePINStatus": vpnRouterInterfacePINStatus,
       "vpnRouterInterfaceRFBand": vpnRouterInterfaceRFBand,
       "vpnRouterInterfaceRFChannel": vpnRouterInterfaceRFChannel,
       "vpnRouterInterfaceSyncrateUpstream": vpnRouterInterfaceSyncrateUpstream,
       "vpnRouterInterfaceSyncrateDownstream": vpnRouterInterfaceSyncrateDownstream,
       "vpnRouterTunnels": vpnRouterTunnels,
       "vpnRouterTunnelCount": vpnRouterTunnelCount,
       "vpnRouterTunnelTable": vpnRouterTunnelTable,
       "vpnRouterTunnelEntry": vpnRouterTunnelEntry,
       "vpnRouterTunnelIndex": vpnRouterTunnelIndex,
       "vpnRouterTunnelName": vpnRouterTunnelName,
       "vpnRouterTunnelAdminStatus": vpnRouterTunnelAdminStatus,
       "vpnRouterTunnelOperativeStatus": vpnRouterTunnelOperativeStatus,
       "vpnRouterTunnelCumulatedBandwidthToWan": vpnRouterTunnelCumulatedBandwidthToWan,
       "vpnRouterTunnelCumulatedBandwidthFromWan": vpnRouterTunnelCumulatedBandwidthFromWan,
       "vpnRouterTunnelCurrentCumulatedBandwidthToWan": vpnRouterTunnelCurrentCumulatedBandwidthToWan,
       "vpnRouterTunnelCurrentCumulatedBandwidthFromWan": vpnRouterTunnelCurrentCumulatedBandwidthFromWan,
       "vpnRouterTunnelTrafficUp": vpnRouterTunnelTrafficUp,
       "vpnRouterTunnelTrafficDown": vpnRouterTunnelTrafficDown,
       "vpnRouterTunnelRemoteRouterSerial": vpnRouterTunnelRemoteRouterSerial,
       "vpnRouterTunnelChannels": vpnRouterTunnelChannels,
       "vpnRouterTunnelChannelCount": vpnRouterTunnelChannelCount,
       "vpnRouterTunnelChannelTable": vpnRouterTunnelChannelTable,
       "vpnRouterTunnelChannelEntry": vpnRouterTunnelChannelEntry,
       "vpnRouterTunnelChannelIndex": vpnRouterTunnelChannelIndex,
       "vpnRouterTunnelChannelName": vpnRouterTunnelChannelName,
       "vpnRouterTunnelChannelAdminStatus": vpnRouterTunnelChannelAdminStatus,
       "vpnRouterTunnelChannelOperativeStatus": vpnRouterTunnelChannelOperativeStatus,
       "vpnRouterTunnelChannelMaxBandwidthToWan": vpnRouterTunnelChannelMaxBandwidthToWan,
       "vpnRouterTunnelChannelMaxBandwidthFromWan": vpnRouterTunnelChannelMaxBandwidthFromWan,
       "vpnRouterTunnelChannelCurrentBandwidthToWan": vpnRouterTunnelChannelCurrentBandwidthToWan,
       "vpnRouterTunnelChannelCurrentBandwidthFromWan": vpnRouterTunnelChannelCurrentBandwidthFromWan,
       "vpnRouterTunnelChannelTrafficUp": vpnRouterTunnelChannelTrafficUp,
       "vpnRouterTunnelChannelTrafficDown": vpnRouterTunnelChannelTrafficDown,
       "vpnRouterTunnelChannelReferencedTunnel": vpnRouterTunnelChannelReferencedTunnel,
       "vpnRouterTunnelChannelIsBackup": vpnRouterTunnelChannelIsBackup,
       "vpnRouterTunnelChannelModuleSlot": vpnRouterTunnelChannelModuleSlot,
       "vpnRouterTunnelChannelPacketLoss": vpnRouterTunnelChannelPacketLoss,
       "vpnRouterTunnelChannelLinkStability": vpnRouterTunnelChannelLinkStability,
       "vpnRouterConformance": vpnRouterConformance,
       "vpnRouterGroups": vpnRouterGroups,
       "vpnRouterObjects": vpnRouterObjects,
       "vpnRouterCompliances": vpnRouterCompliances,
       "vpnRouterReadOnlyCompliance": vpnRouterReadOnlyCompliance}
)
