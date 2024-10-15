# SNMP MIB module (MERU-CONFIG-CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-CONTROLLER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:00 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlAlarmState,
 MwlAvailabilityStatus,
 MwlBonding,
 MwlControllerHwType,
 MwlEnableDisableOption,
 MwlOnOffSwitch,
 MwlOperationalState,
 MwlRegionSettings,
 MwlVpnConnectivityStatus) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlAlarmState",
    "MwlAvailabilityStatus",
    "MwlBonding",
    "MwlControllerHwType",
    "MwlEnableDisableOption",
    "MwlOnOffSwitch",
    "MwlOperationalState",
    "MwlRegionSettings",
    "MwlVpnConnectivityStatus")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigController = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwWncVars_ObjectIdentity = ObjectIdentity
mwWncVars = _MwWncVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1)
)
_MwWncVarsDescr_Type = DisplayString
_MwWncVarsDescr_Object = MibScalar
mwWncVarsDescr = _MwWncVarsDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 1),
    _MwWncVarsDescr_Type()
)
mwWncVarsDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsDescr.setStatus("current")


class _MwWncVarsLocation_Type(DisplayString):
    """Custom type mwWncVarsLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MwWncVarsLocation_Type.__name__ = "DisplayString"
_MwWncVarsLocation_Object = MibScalar
mwWncVarsLocation = _MwWncVarsLocation_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 2),
    _MwWncVarsLocation_Type()
)
mwWncVarsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsLocation.setStatus("current")


class _MwWncVarsContact_Type(DisplayString):
    """Custom type mwWncVarsContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MwWncVarsContact_Type.__name__ = "DisplayString"
_MwWncVarsContact_Object = MibScalar
mwWncVarsContact = _MwWncVarsContact_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 3),
    _MwWncVarsContact_Type()
)
mwWncVarsContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsContact.setStatus("current")
_MwWncVarsAutoApUpgrade_Type = MwlOnOffSwitch
_MwWncVarsAutoApUpgrade_Object = MibScalar
mwWncVarsAutoApUpgrade = _MwWncVarsAutoApUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 4),
    _MwWncVarsAutoApUpgrade_Type()
)
mwWncVarsAutoApUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsAutoApUpgrade.setStatus("current")
_MwWncVarsDhcpServer_Type = IpAddress
_MwWncVarsDhcpServer_Object = MibScalar
mwWncVarsDhcpServer = _MwWncVarsDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 5),
    _MwWncVarsDhcpServer_Type()
)
mwWncVarsDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsDhcpServer.setStatus("current")


class _MwWncVarsStatPollingPeriod_Type(Integer32):
    """Custom type mwWncVarsStatPollingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MwWncVarsStatPollingPeriod_Type.__name__ = "Integer32"
_MwWncVarsStatPollingPeriod_Object = MibScalar
mwWncVarsStatPollingPeriod = _MwWncVarsStatPollingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 6),
    _MwWncVarsStatPollingPeriod_Type()
)
mwWncVarsStatPollingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsStatPollingPeriod.setStatus("current")


class _MwWncVarsAuditPeriod_Type(Integer32):
    """Custom type mwWncVarsAuditPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MwWncVarsAuditPeriod_Type.__name__ = "Integer32"
_MwWncVarsAuditPeriod_Object = MibScalar
mwWncVarsAuditPeriod = _MwWncVarsAuditPeriod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 7),
    _MwWncVarsAuditPeriod_Type()
)
mwWncVarsAuditPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsAuditPeriod.setStatus("current")


class _MwWncVarsApInitScript_Type(DisplayString):
    """Custom type mwWncVarsApInitScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwWncVarsApInitScript_Type.__name__ = "DisplayString"
_MwWncVarsApInitScript_Object = MibScalar
mwWncVarsApInitScript = _MwWncVarsApInitScript_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 8),
    _MwWncVarsApInitScript_Type()
)
mwWncVarsApInitScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsApInitScript.setStatus("current")
_MwWncVarsDhcpRelayPassThroughFlag_Type = MwlOnOffSwitch
_MwWncVarsDhcpRelayPassThroughFlag_Object = MibScalar
mwWncVarsDhcpRelayPassThroughFlag = _MwWncVarsDhcpRelayPassThroughFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 9),
    _MwWncVarsDhcpRelayPassThroughFlag_Type()
)
mwWncVarsDhcpRelayPassThroughFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsDhcpRelayPassThroughFlag.setStatus("current")
_MwWncVarsManagementFromWirelessClients_Type = MwlOnOffSwitch
_MwWncVarsManagementFromWirelessClients_Object = MibScalar
mwWncVarsManagementFromWirelessClients = _MwWncVarsManagementFromWirelessClients_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 10),
    _MwWncVarsManagementFromWirelessClients_Type()
)
mwWncVarsManagementFromWirelessClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsManagementFromWirelessClients.setStatus("current")


class _MwWncVarsControllerIndex_Type(Integer32):
    """Custom type mwWncVarsControllerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MwWncVarsControllerIndex_Type.__name__ = "Integer32"
_MwWncVarsControllerIndex_Object = MibScalar
mwWncVarsControllerIndex = _MwWncVarsControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 11),
    _MwWncVarsControllerIndex_Type()
)
mwWncVarsControllerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsControllerIndex.setStatus("current")
_MwWncVarsTopoUpdate_Type = MwlOnOffSwitch
_MwWncVarsTopoUpdate_Object = MibScalar
mwWncVarsTopoUpdate = _MwWncVarsTopoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 12),
    _MwWncVarsTopoUpdate_Type()
)
mwWncVarsTopoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsTopoUpdate.setStatus("current")
_MwWncVarsFastPath_Type = MwlOnOffSwitch
_MwWncVarsFastPath_Object = MibScalar
mwWncVarsFastPath = _MwWncVarsFastPath_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 14),
    _MwWncVarsFastPath_Type()
)
mwWncVarsFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsFastPath.setStatus("current")
_MwWncVarsBonding_Type = MwlBonding
_MwWncVarsBonding_Object = MibScalar
mwWncVarsBonding = _MwWncVarsBonding_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 15),
    _MwWncVarsBonding_Type()
)
mwWncVarsBonding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsBonding.setStatus("current")
_MwWncVarsNodeId_Type = Integer32
_MwWncVarsNodeId_Object = MibScalar
mwWncVarsNodeId = _MwWncVarsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 18),
    _MwWncVarsNodeId_Type()
)
mwWncVarsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsNodeId.setStatus("current")
_MwWncVarsHostName_Type = DisplayString
_MwWncVarsHostName_Object = MibScalar
mwWncVarsHostName = _MwWncVarsHostName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 19),
    _MwWncVarsHostName_Type()
)
mwWncVarsHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsHostName.setStatus("current")
_MwWncVarsUpTime_Type = TimeTicks
_MwWncVarsUpTime_Object = MibScalar
mwWncVarsUpTime = _MwWncVarsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 20),
    _MwWncVarsUpTime_Type()
)
mwWncVarsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsUpTime.setStatus("current")
_MwWncVarsOperationalState_Type = MwlOperationalState
_MwWncVarsOperationalState_Object = MibScalar
mwWncVarsOperationalState = _MwWncVarsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 21),
    _MwWncVarsOperationalState_Type()
)
mwWncVarsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsOperationalState.setStatus("current")
_MwWncVarsAvailabilityStatus_Type = MwlAvailabilityStatus
_MwWncVarsAvailabilityStatus_Object = MibScalar
mwWncVarsAvailabilityStatus = _MwWncVarsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 22),
    _MwWncVarsAvailabilityStatus_Type()
)
mwWncVarsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsAvailabilityStatus.setStatus("current")
_MwWncVarsAlarmState_Type = MwlAlarmState
_MwWncVarsAlarmState_Object = MibScalar
mwWncVarsAlarmState = _MwWncVarsAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 23),
    _MwWncVarsAlarmState_Type()
)
mwWncVarsAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsAlarmState.setStatus("current")
_MwWncVarsVirtualIpAddress_Type = IpAddress
_MwWncVarsVirtualIpAddress_Object = MibScalar
mwWncVarsVirtualIpAddress = _MwWncVarsVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 24),
    _MwWncVarsVirtualIpAddress_Type()
)
mwWncVarsVirtualIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsVirtualIpAddress.setStatus("current")
_MwWncVarsVirtualNetMask_Type = IpAddress
_MwWncVarsVirtualNetMask_Object = MibScalar
mwWncVarsVirtualNetMask = _MwWncVarsVirtualNetMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 25),
    _MwWncVarsVirtualNetMask_Type()
)
mwWncVarsVirtualNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsVirtualNetMask.setStatus("current")
_MwWncVarsDefaultGatewayAddr_Type = IpAddress
_MwWncVarsDefaultGatewayAddr_Object = MibScalar
mwWncVarsDefaultGatewayAddr = _MwWncVarsDefaultGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 26),
    _MwWncVarsDefaultGatewayAddr_Type()
)
mwWncVarsDefaultGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsDefaultGatewayAddr.setStatus("current")
_MwWncVarsSoftwareVersion_Type = DisplayString
_MwWncVarsSoftwareVersion_Object = MibScalar
mwWncVarsSoftwareVersion = _MwWncVarsSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 27),
    _MwWncVarsSoftwareVersion_Type()
)
mwWncVarsSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsSoftwareVersion.setStatus("current")
_MwWncVarsSerialNumber_Type = DisplayString
_MwWncVarsSerialNumber_Object = MibScalar
mwWncVarsSerialNumber = _MwWncVarsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 28),
    _MwWncVarsSerialNumber_Type()
)
mwWncVarsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsSerialNumber.setStatus("current")
_MwWncVarsSystemId_Type = DisplayString
_MwWncVarsSystemId_Object = MibScalar
mwWncVarsSystemId = _MwWncVarsSystemId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 29),
    _MwWncVarsSystemId_Type()
)
mwWncVarsSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsSystemId.setStatus("current")
_MwWncVarsHardwareType_Type = MwlControllerHwType
_MwWncVarsHardwareType_Object = MibScalar
mwWncVarsHardwareType = _MwWncVarsHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 30),
    _MwWncVarsHardwareType_Type()
)
mwWncVarsHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsHardwareType.setStatus("current")
_MwWncVarsCountry_Type = DisplayString
_MwWncVarsCountry_Object = MibScalar
mwWncVarsCountry = _MwWncVarsCountry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 31),
    _MwWncVarsCountry_Type()
)
mwWncVarsCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsCountry.setStatus("current")
_MwWncVarsManSerialNumber_Type = DisplayString
_MwWncVarsManSerialNumber_Object = MibScalar
mwWncVarsManSerialNumber = _MwWncVarsManSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 32),
    _MwWncVarsManSerialNumber_Type()
)
mwWncVarsManSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsManSerialNumber.setStatus("current")


class _MwWncVarsStationAgingOutPeriod_Type(Integer32):
    """Custom type mwWncVarsStationAgingOutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MwWncVarsStationAgingOutPeriod_Type.__name__ = "Integer32"
_MwWncVarsStationAgingOutPeriod_Object = MibScalar
mwWncVarsStationAgingOutPeriod = _MwWncVarsStationAgingOutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 33),
    _MwWncVarsStationAgingOutPeriod_Type()
)
mwWncVarsStationAgingOutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsStationAgingOutPeriod.setStatus("current")
_MwWncVarsRoamingDomainState_Type = MwlEnableDisableOption
_MwWncVarsRoamingDomainState_Object = MibScalar
mwWncVarsRoamingDomainState = _MwWncVarsRoamingDomainState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 34),
    _MwWncVarsRoamingDomainState_Type()
)
mwWncVarsRoamingDomainState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsRoamingDomainState.setStatus("current")
_MwWncVarsAssocStationMaxIdlePeriod_Type = Unsigned32
_MwWncVarsAssocStationMaxIdlePeriod_Object = MibScalar
mwWncVarsAssocStationMaxIdlePeriod = _MwWncVarsAssocStationMaxIdlePeriod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 36),
    _MwWncVarsAssocStationMaxIdlePeriod_Type()
)
mwWncVarsAssocStationMaxIdlePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwWncVarsAssocStationMaxIdlePeriod.setStatus("current")
_MwWncVarsL3RoutingMode_Type = MwlOnOffSwitch
_MwWncVarsL3RoutingMode_Object = MibScalar
mwWncVarsL3RoutingMode = _MwWncVarsL3RoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 37),
    _MwWncVarsL3RoutingMode_Type()
)
mwWncVarsL3RoutingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsL3RoutingMode.setStatus("current")
_MwWncVarsRegion_Type = MwlRegionSettings
_MwWncVarsRegion_Object = MibScalar
mwWncVarsRegion = _MwWncVarsRegion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 1, 38),
    _MwWncVarsRegion_Type()
)
mwWncVarsRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwWncVarsRegion.setStatus("current")
_MwSystemFileVars_ObjectIdentity = ObjectIdentity
mwSystemFileVars = _MwSystemFileVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 3)
)


class _MwSystemFileVarspHostName_Type(DisplayString):
    """Custom type mwSystemFileVarspHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwSystemFileVarspHostName_Type.__name__ = "DisplayString"
_MwSystemFileVarspHostName_Object = MibScalar
mwSystemFileVarspHostName = _MwSystemFileVarspHostName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 3, 1),
    _MwSystemFileVarspHostName_Type()
)
mwSystemFileVarspHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwSystemFileVarspHostName.setStatus("current")


class _MwSystemFileVarspDnsDomainName_Type(DisplayString):
    """Custom type mwSystemFileVarspDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwSystemFileVarspDnsDomainName_Type.__name__ = "DisplayString"
_MwSystemFileVarspDnsDomainName_Object = MibScalar
mwSystemFileVarspDnsDomainName = _MwSystemFileVarspDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 3, 2),
    _MwSystemFileVarspDnsDomainName_Type()
)
mwSystemFileVarspDnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwSystemFileVarspDnsDomainName.setStatus("current")
_MwUdpBcastUpstreamTable_Object = MibTable
mwUdpBcastUpstreamTable = _MwUdpBcastUpstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamTable.setStatus("current")
_MwUdpBcastUpstreamEntry_Object = MibTableRow
mwUdpBcastUpstreamEntry = _MwUdpBcastUpstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 4, 1)
)
mwUdpBcastUpstreamEntry.setIndexNames(
    (0, "MERU-CONFIG-CONTROLLER-MIB", "mwUdpBcastUpstreamTableIndex"),
)
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamEntry.setStatus("current")
_MwUdpBcastUpstreamTableIndex_Type = Integer32
_MwUdpBcastUpstreamTableIndex_Object = MibTableColumn
mwUdpBcastUpstreamTableIndex = _MwUdpBcastUpstreamTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 4, 1, 1),
    _MwUdpBcastUpstreamTableIndex_Type()
)
mwUdpBcastUpstreamTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamTableIndex.setStatus("current")
_MwUdpBcastUpstreamPort_Type = Unsigned32
_MwUdpBcastUpstreamPort_Object = MibTableColumn
mwUdpBcastUpstreamPort = _MwUdpBcastUpstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 4, 1, 2),
    _MwUdpBcastUpstreamPort_Type()
)
mwUdpBcastUpstreamPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamPort.setStatus("current")
_MwUdpBcastUpstreamRowStatus_Type = RowStatus
_MwUdpBcastUpstreamRowStatus_Object = MibTableColumn
mwUdpBcastUpstreamRowStatus = _MwUdpBcastUpstreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 4, 1, 3),
    _MwUdpBcastUpstreamRowStatus_Type()
)
mwUdpBcastUpstreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamRowStatus.setStatus("current")
_MwUdpBcastDownstreamTable_Object = MibTable
mwUdpBcastDownstreamTable = _MwUdpBcastDownstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamTable.setStatus("current")
_MwUdpBcastDownstreamEntry_Object = MibTableRow
mwUdpBcastDownstreamEntry = _MwUdpBcastDownstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 5, 1)
)
mwUdpBcastDownstreamEntry.setIndexNames(
    (0, "MERU-CONFIG-CONTROLLER-MIB", "mwUdpBcastDownstreamTableIndex"),
)
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamEntry.setStatus("current")
_MwUdpBcastDownstreamTableIndex_Type = Integer32
_MwUdpBcastDownstreamTableIndex_Object = MibTableColumn
mwUdpBcastDownstreamTableIndex = _MwUdpBcastDownstreamTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 5, 1, 1),
    _MwUdpBcastDownstreamTableIndex_Type()
)
mwUdpBcastDownstreamTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamTableIndex.setStatus("current")
_MwUdpBcastDownstreamPort_Type = Unsigned32
_MwUdpBcastDownstreamPort_Object = MibTableColumn
mwUdpBcastDownstreamPort = _MwUdpBcastDownstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 5, 1, 2),
    _MwUdpBcastDownstreamPort_Type()
)
mwUdpBcastDownstreamPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamPort.setStatus("current")
_MwUdpBcastDownstreamRowStatus_Type = RowStatus
_MwUdpBcastDownstreamRowStatus_Object = MibTableColumn
mwUdpBcastDownstreamRowStatus = _MwUdpBcastDownstreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 5, 1, 3),
    _MwUdpBcastDownstreamRowStatus_Type()
)
mwUdpBcastDownstreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamRowStatus.setStatus("current")
_MwDnsServerTable_Object = MibTable
mwDnsServerTable = _MwDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    mwDnsServerTable.setStatus("current")
_MwDnsServerEntry_Object = MibTableRow
mwDnsServerEntry = _MwDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 6, 1)
)
mwDnsServerEntry.setIndexNames(
    (0, "MERU-CONFIG-CONTROLLER-MIB", "mwDnsServerTableIndex"),
)
if mibBuilder.loadTexts:
    mwDnsServerEntry.setStatus("current")
_MwDnsServerTableIndex_Type = Integer32
_MwDnsServerTableIndex_Object = MibTableColumn
mwDnsServerTableIndex = _MwDnsServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 6, 1, 1),
    _MwDnsServerTableIndex_Type()
)
mwDnsServerTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwDnsServerTableIndex.setStatus("current")
_MwDnsServer_Type = IpAddress
_MwDnsServer_Object = MibTableColumn
mwDnsServer = _MwDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 6, 1, 2),
    _MwDnsServer_Type()
)
mwDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDnsServer.setStatus("current")
_MwDnsServerRowStatus_Type = RowStatus
_MwDnsServerRowStatus_Object = MibTableColumn
mwDnsServerRowStatus = _MwDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 6, 1, 3),
    _MwDnsServerRowStatus_Type()
)
mwDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDnsServerRowStatus.setStatus("current")
_MwWncNetworkConfigTable_Object = MibTable
mwWncNetworkConfigTable = _MwWncNetworkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 7)
)
if mibBuilder.loadTexts:
    mwWncNetworkConfigTable.setStatus("current")
_MwWncNetworkConfigEntry_Object = MibTableRow
mwWncNetworkConfigEntry = _MwWncNetworkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 7, 1)
)
mwWncNetworkConfigEntry.setIndexNames(
    (0, "MERU-CONFIG-CONTROLLER-MIB", "mwWncNetworkConfigTableIndex"),
)
if mibBuilder.loadTexts:
    mwWncNetworkConfigEntry.setStatus("current")
_MwWncNetworkConfigTableIndex_Type = Integer32
_MwWncNetworkConfigTableIndex_Object = MibTableColumn
mwWncNetworkConfigTableIndex = _MwWncNetworkConfigTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 7, 1, 1),
    _MwWncNetworkConfigTableIndex_Type()
)
mwWncNetworkConfigTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwWncNetworkConfigTableIndex.setStatus("current")
_MwWncNetworkConfigFastPath_Type = MwlOnOffSwitch
_MwWncNetworkConfigFastPath_Object = MibTableColumn
mwWncNetworkConfigFastPath = _MwWncNetworkConfigFastPath_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 7, 1, 2),
    _MwWncNetworkConfigFastPath_Type()
)
mwWncNetworkConfigFastPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncNetworkConfigFastPath.setStatus("current")
_MwWncNetworkConfigBonding_Type = MwlBonding
_MwWncNetworkConfigBonding_Object = MibTableColumn
mwWncNetworkConfigBonding = _MwWncNetworkConfigBonding_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 7, 1, 3),
    _MwWncNetworkConfigBonding_Type()
)
mwWncNetworkConfigBonding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncNetworkConfigBonding.setStatus("current")
_MwWncNetworkConfigTenGigModule_Type = MwlEnableDisableOption
_MwWncNetworkConfigTenGigModule_Object = MibTableColumn
mwWncNetworkConfigTenGigModule = _MwWncNetworkConfigTenGigModule_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 7, 1, 4),
    _MwWncNetworkConfigTenGigModule_Type()
)
mwWncNetworkConfigTenGigModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncNetworkConfigTenGigModule.setStatus("current")
_MwWncNetworkConfigRowStatus_Type = RowStatus
_MwWncNetworkConfigRowStatus_Object = MibTableColumn
mwWncNetworkConfigRowStatus = _MwWncNetworkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 7, 1, 5),
    _MwWncNetworkConfigRowStatus_Type()
)
mwWncNetworkConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncNetworkConfigRowStatus.setStatus("current")
_MwVirtualInterfaceProfileTable_Object = MibTable
mwVirtualInterfaceProfileTable = _MwVirtualInterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8)
)
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileTable.setStatus("current")
_MwVirtualInterfaceProfileEntry_Object = MibTableRow
mwVirtualInterfaceProfileEntry = _MwVirtualInterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1)
)
mwVirtualInterfaceProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-CONTROLLER-MIB", "mwVirtualInterfaceProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileEntry.setStatus("current")
_MwVirtualInterfaceProfileTableIndex_Type = Integer32
_MwVirtualInterfaceProfileTableIndex_Object = MibTableColumn
mwVirtualInterfaceProfileTableIndex = _MwVirtualInterfaceProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1, 1),
    _MwVirtualInterfaceProfileTableIndex_Type()
)
mwVirtualInterfaceProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileTableIndex.setStatus("current")


class _MwVirtualInterfaceProfileName_Type(DisplayString):
    """Custom type mwVirtualInterfaceProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwVirtualInterfaceProfileName_Type.__name__ = "DisplayString"
_MwVirtualInterfaceProfileName_Object = MibTableColumn
mwVirtualInterfaceProfileName = _MwVirtualInterfaceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1, 2),
    _MwVirtualInterfaceProfileName_Type()
)
mwVirtualInterfaceProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileName.setStatus("current")


class _MwVirtualInterfaceProfileId_Type(Integer32):
    """Custom type mwVirtualInterfaceProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_MwVirtualInterfaceProfileId_Type.__name__ = "Integer32"
_MwVirtualInterfaceProfileId_Object = MibTableColumn
mwVirtualInterfaceProfileId = _MwVirtualInterfaceProfileId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1, 3),
    _MwVirtualInterfaceProfileId_Type()
)
mwVirtualInterfaceProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileId.setStatus("current")
_MwVirtualInterfaceProfileState_Type = MwlEnableDisableOption
_MwVirtualInterfaceProfileState_Object = MibTableColumn
mwVirtualInterfaceProfileState = _MwVirtualInterfaceProfileState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1, 4),
    _MwVirtualInterfaceProfileState_Type()
)
mwVirtualInterfaceProfileState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileState.setStatus("current")
_MwVirtualInterfaceProfileSubnetIp_Type = IpAddress
_MwVirtualInterfaceProfileSubnetIp_Object = MibTableColumn
mwVirtualInterfaceProfileSubnetIp = _MwVirtualInterfaceProfileSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1, 5),
    _MwVirtualInterfaceProfileSubnetIp_Type()
)
mwVirtualInterfaceProfileSubnetIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileSubnetIp.setStatus("current")
_MwVirtualInterfaceProfileSubnetMask_Type = IpAddress
_MwVirtualInterfaceProfileSubnetMask_Object = MibTableColumn
mwVirtualInterfaceProfileSubnetMask = _MwVirtualInterfaceProfileSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1, 6),
    _MwVirtualInterfaceProfileSubnetMask_Type()
)
mwVirtualInterfaceProfileSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileSubnetMask.setStatus("current")
_MwVirtualInterfaceProfileGatewayIp_Type = IpAddress
_MwVirtualInterfaceProfileGatewayIp_Object = MibTableColumn
mwVirtualInterfaceProfileGatewayIp = _MwVirtualInterfaceProfileGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1, 7),
    _MwVirtualInterfaceProfileGatewayIp_Type()
)
mwVirtualInterfaceProfileGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileGatewayIp.setStatus("current")
_MwVirtualInterfaceProfileRowStatus_Type = RowStatus
_MwVirtualInterfaceProfileRowStatus_Object = MibTableColumn
mwVirtualInterfaceProfileRowStatus = _MwVirtualInterfaceProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 8, 1, 8),
    _MwVirtualInterfaceProfileRowStatus_Type()
)
mwVirtualInterfaceProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVirtualInterfaceProfileRowStatus.setStatus("current")
_MwDhcpServerTable_Object = MibTable
mwDhcpServerTable = _MwDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9)
)
if mibBuilder.loadTexts:
    mwDhcpServerTable.setStatus("current")
_MwDhcpServerEntry_Object = MibTableRow
mwDhcpServerEntry = _MwDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1)
)
mwDhcpServerEntry.setIndexNames(
    (0, "MERU-CONFIG-CONTROLLER-MIB", "mwDhcpServerTableIndex"),
)
if mibBuilder.loadTexts:
    mwDhcpServerEntry.setStatus("current")
_MwDhcpServerTableIndex_Type = Integer32
_MwDhcpServerTableIndex_Object = MibTableColumn
mwDhcpServerTableIndex = _MwDhcpServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 1),
    _MwDhcpServerTableIndex_Type()
)
mwDhcpServerTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwDhcpServerTableIndex.setStatus("current")


class _MwDhcpServerName_Type(DisplayString):
    """Custom type mwDhcpServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwDhcpServerName_Type.__name__ = "DisplayString"
_MwDhcpServerName_Object = MibTableColumn
mwDhcpServerName = _MwDhcpServerName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 2),
    _MwDhcpServerName_Type()
)
mwDhcpServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerName.setStatus("current")


class _MwDhcpServerVlanName_Type(DisplayString):
    """Custom type mwDhcpServerVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwDhcpServerVlanName_Type.__name__ = "DisplayString"
_MwDhcpServerVlanName_Object = MibTableColumn
mwDhcpServerVlanName = _MwDhcpServerVlanName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 3),
    _MwDhcpServerVlanName_Type()
)
mwDhcpServerVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerVlanName.setStatus("current")


class _MwDhcpServerVirtualInterfaceProfileName_Type(DisplayString):
    """Custom type mwDhcpServerVirtualInterfaceProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwDhcpServerVirtualInterfaceProfileName_Type.__name__ = "DisplayString"
_MwDhcpServerVirtualInterfaceProfileName_Object = MibTableColumn
mwDhcpServerVirtualInterfaceProfileName = _MwDhcpServerVirtualInterfaceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 4),
    _MwDhcpServerVirtualInterfaceProfileName_Type()
)
mwDhcpServerVirtualInterfaceProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerVirtualInterfaceProfileName.setStatus("current")
_MwDhcpServerState_Type = MwlEnableDisableOption
_MwDhcpServerState_Object = MibTableColumn
mwDhcpServerState = _MwDhcpServerState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 5),
    _MwDhcpServerState_Type()
)
mwDhcpServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerState.setStatus("current")


class _MwDhcpServerLeaseTime_Type(Integer32):
    """Custom type mwDhcpServerLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 65535),
    )


_MwDhcpServerLeaseTime_Type.__name__ = "Integer32"
_MwDhcpServerLeaseTime_Object = MibTableColumn
mwDhcpServerLeaseTime = _MwDhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 6),
    _MwDhcpServerLeaseTime_Type()
)
mwDhcpServerLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerLeaseTime.setStatus("current")
_MwDhcpServerIpPoolStart_Type = IpAddress
_MwDhcpServerIpPoolStart_Object = MibTableColumn
mwDhcpServerIpPoolStart = _MwDhcpServerIpPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 7),
    _MwDhcpServerIpPoolStart_Type()
)
mwDhcpServerIpPoolStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerIpPoolStart.setStatus("current")
_MwDhcpServerIpPoolEnd_Type = IpAddress
_MwDhcpServerIpPoolEnd_Object = MibTableColumn
mwDhcpServerIpPoolEnd = _MwDhcpServerIpPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 8),
    _MwDhcpServerIpPoolEnd_Type()
)
mwDhcpServerIpPoolEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerIpPoolEnd.setStatus("current")
_MwDhcpServerDomainName_Type = DisplayString
_MwDhcpServerDomainName_Object = MibTableColumn
mwDhcpServerDomainName = _MwDhcpServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 9),
    _MwDhcpServerDomainName_Type()
)
mwDhcpServerDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerDomainName.setStatus("current")
_MwDhcpServerDnsServer1_Type = IpAddress
_MwDhcpServerDnsServer1_Object = MibTableColumn
mwDhcpServerDnsServer1 = _MwDhcpServerDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 10),
    _MwDhcpServerDnsServer1_Type()
)
mwDhcpServerDnsServer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerDnsServer1.setStatus("current")
_MwDhcpServerDnsServer2_Type = IpAddress
_MwDhcpServerDnsServer2_Object = MibTableColumn
mwDhcpServerDnsServer2 = _MwDhcpServerDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 11),
    _MwDhcpServerDnsServer2_Type()
)
mwDhcpServerDnsServer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerDnsServer2.setStatus("current")
_MwDhcpServerNetbiosServer1_Type = IpAddress
_MwDhcpServerNetbiosServer1_Object = MibTableColumn
mwDhcpServerNetbiosServer1 = _MwDhcpServerNetbiosServer1_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 12),
    _MwDhcpServerNetbiosServer1_Type()
)
mwDhcpServerNetbiosServer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerNetbiosServer1.setStatus("current")
_MwDhcpServerNetbiosServer2_Type = IpAddress
_MwDhcpServerNetbiosServer2_Object = MibTableColumn
mwDhcpServerNetbiosServer2 = _MwDhcpServerNetbiosServer2_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 13),
    _MwDhcpServerNetbiosServer2_Type()
)
mwDhcpServerNetbiosServer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerNetbiosServer2.setStatus("current")


class _MwDhcpServerOption43_Type(DisplayString):
    """Custom type mwDhcpServerOption43 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwDhcpServerOption43_Type.__name__ = "DisplayString"
_MwDhcpServerOption43_Object = MibTableColumn
mwDhcpServerOption43 = _MwDhcpServerOption43_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 14),
    _MwDhcpServerOption43_Type()
)
mwDhcpServerOption43.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerOption43.setStatus("current")
_MwDhcpServerRowStatus_Type = RowStatus
_MwDhcpServerRowStatus_Object = MibTableColumn
mwDhcpServerRowStatus = _MwDhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 9, 1, 16),
    _MwDhcpServerRowStatus_Type()
)
mwDhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwDhcpServerRowStatus.setStatus("current")
_MwVpnServer_ObjectIdentity = ObjectIdentity
mwVpnServer = _MwVpnServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 10)
)
_MwVpnServerState_Type = MwlEnableDisableOption
_MwVpnServerState_Object = MibScalar
mwVpnServerState = _MwVpnServerState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 10, 2),
    _MwVpnServerState_Type()
)
mwVpnServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVpnServerState.setStatus("current")
_MwVpnServerIp_Type = IpAddress
_MwVpnServerIp_Object = MibScalar
mwVpnServerIp = _MwVpnServerIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 10, 3),
    _MwVpnServerIp_Type()
)
mwVpnServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVpnServerIp.setStatus("current")


class _MwVpnServerHostName_Type(DisplayString):
    """Custom type mwVpnServerHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MwVpnServerHostName_Type.__name__ = "DisplayString"
_MwVpnServerHostName_Object = MibScalar
mwVpnServerHostName = _MwVpnServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 10, 4),
    _MwVpnServerHostName_Type()
)
mwVpnServerHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVpnServerHostName.setStatus("current")
_MwVpnServerPort_Type = Unsigned32
_MwVpnServerPort_Object = MibScalar
mwVpnServerPort = _MwVpnServerPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 10, 5),
    _MwVpnServerPort_Type()
)
mwVpnServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVpnServerPort.setStatus("current")
_MwVpnServerIpPool_Type = IpAddress
_MwVpnServerIpPool_Object = MibScalar
mwVpnServerIpPool = _MwVpnServerIpPool_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 10, 6),
    _MwVpnServerIpPool_Type()
)
mwVpnServerIpPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVpnServerIpPool.setStatus("current")
_MwVpnServerSubnetMask_Type = IpAddress
_MwVpnServerSubnetMask_Object = MibScalar
mwVpnServerSubnetMask = _MwVpnServerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 10, 7),
    _MwVpnServerSubnetMask_Type()
)
mwVpnServerSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVpnServerSubnetMask.setStatus("current")
_MwVpnClient_ObjectIdentity = ObjectIdentity
mwVpnClient = _MwVpnClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 11)
)
_MwVpnClientState_Type = MwlEnableDisableOption
_MwVpnClientState_Object = MibScalar
mwVpnClientState = _MwVpnClientState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 11, 2),
    _MwVpnClientState_Type()
)
mwVpnClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwVpnClientState.setStatus("current")
_MwVpnClientVpnServerIp_Type = IpAddress
_MwVpnClientVpnServerIp_Object = MibScalar
mwVpnClientVpnServerIp = _MwVpnClientVpnServerIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 11, 3),
    _MwVpnClientVpnServerIp_Type()
)
mwVpnClientVpnServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwVpnClientVpnServerIp.setStatus("current")
_MwVpnClientVpnServerPort_Type = Unsigned32
_MwVpnClientVpnServerPort_Object = MibScalar
mwVpnClientVpnServerPort = _MwVpnClientVpnServerPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 11, 4),
    _MwVpnClientVpnServerPort_Type()
)
mwVpnClientVpnServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwVpnClientVpnServerPort.setStatus("current")
_MwVpnClientStatus_Type = MwlVpnConnectivityStatus
_MwVpnClientStatus_Object = MibScalar
mwVpnClientStatus = _MwVpnClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 11, 5),
    _MwVpnClientStatus_Type()
)
mwVpnClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVpnClientStatus.setStatus("current")
_MwUdpBcastUpstreamBridgedTable_Object = MibTable
mwUdpBcastUpstreamBridgedTable = _MwUdpBcastUpstreamBridgedTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 12)
)
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamBridgedTable.setStatus("current")
_MwUdpBcastUpstreamBridgedEntry_Object = MibTableRow
mwUdpBcastUpstreamBridgedEntry = _MwUdpBcastUpstreamBridgedEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 12, 1)
)
mwUdpBcastUpstreamBridgedEntry.setIndexNames(
    (0, "MERU-CONFIG-CONTROLLER-MIB", "mwUdpBcastUpstreamBridgedTableIndex"),
)
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamBridgedEntry.setStatus("current")
_MwUdpBcastUpstreamBridgedTableIndex_Type = Integer32
_MwUdpBcastUpstreamBridgedTableIndex_Object = MibTableColumn
mwUdpBcastUpstreamBridgedTableIndex = _MwUdpBcastUpstreamBridgedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 12, 1, 1),
    _MwUdpBcastUpstreamBridgedTableIndex_Type()
)
mwUdpBcastUpstreamBridgedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamBridgedTableIndex.setStatus("current")
_MwUdpBcastUpstreamBridgedPort_Type = Unsigned32
_MwUdpBcastUpstreamBridgedPort_Object = MibTableColumn
mwUdpBcastUpstreamBridgedPort = _MwUdpBcastUpstreamBridgedPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 12, 1, 2),
    _MwUdpBcastUpstreamBridgedPort_Type()
)
mwUdpBcastUpstreamBridgedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamBridgedPort.setStatus("current")
_MwUdpBcastUpstreamBridgedRowStatus_Type = RowStatus
_MwUdpBcastUpstreamBridgedRowStatus_Object = MibTableColumn
mwUdpBcastUpstreamBridgedRowStatus = _MwUdpBcastUpstreamBridgedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 12, 1, 3),
    _MwUdpBcastUpstreamBridgedRowStatus_Type()
)
mwUdpBcastUpstreamBridgedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwUdpBcastUpstreamBridgedRowStatus.setStatus("current")
_MwUdpBcastDownstreamBridgedTable_Object = MibTable
mwUdpBcastDownstreamBridgedTable = _MwUdpBcastDownstreamBridgedTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 13)
)
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamBridgedTable.setStatus("current")
_MwUdpBcastDownstreamBridgedEntry_Object = MibTableRow
mwUdpBcastDownstreamBridgedEntry = _MwUdpBcastDownstreamBridgedEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 13, 1)
)
mwUdpBcastDownstreamBridgedEntry.setIndexNames(
    (0, "MERU-CONFIG-CONTROLLER-MIB", "mwUdpBcastDownstreamBridgedTableIndex"),
)
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamBridgedEntry.setStatus("current")
_MwUdpBcastDownstreamBridgedTableIndex_Type = Integer32
_MwUdpBcastDownstreamBridgedTableIndex_Object = MibTableColumn
mwUdpBcastDownstreamBridgedTableIndex = _MwUdpBcastDownstreamBridgedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 13, 1, 1),
    _MwUdpBcastDownstreamBridgedTableIndex_Type()
)
mwUdpBcastDownstreamBridgedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamBridgedTableIndex.setStatus("current")
_MwUdpBcastDownstreamBridgedPort_Type = Unsigned32
_MwUdpBcastDownstreamBridgedPort_Object = MibTableColumn
mwUdpBcastDownstreamBridgedPort = _MwUdpBcastDownstreamBridgedPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 13, 1, 2),
    _MwUdpBcastDownstreamBridgedPort_Type()
)
mwUdpBcastDownstreamBridgedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamBridgedPort.setStatus("current")
_MwUdpBcastDownstreamBridgedRowStatus_Type = RowStatus
_MwUdpBcastDownstreamBridgedRowStatus_Object = MibTableColumn
mwUdpBcastDownstreamBridgedRowStatus = _MwUdpBcastDownstreamBridgedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 1, 13, 1, 3),
    _MwUdpBcastDownstreamBridgedRowStatus_Type()
)
mwUdpBcastDownstreamBridgedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwUdpBcastDownstreamBridgedRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-CONTROLLER-MIB",
    **{"mwConfigController": mwConfigController,
       "mwWncVars": mwWncVars,
       "mwWncVarsDescr": mwWncVarsDescr,
       "mwWncVarsLocation": mwWncVarsLocation,
       "mwWncVarsContact": mwWncVarsContact,
       "mwWncVarsAutoApUpgrade": mwWncVarsAutoApUpgrade,
       "mwWncVarsDhcpServer": mwWncVarsDhcpServer,
       "mwWncVarsStatPollingPeriod": mwWncVarsStatPollingPeriod,
       "mwWncVarsAuditPeriod": mwWncVarsAuditPeriod,
       "mwWncVarsApInitScript": mwWncVarsApInitScript,
       "mwWncVarsDhcpRelayPassThroughFlag": mwWncVarsDhcpRelayPassThroughFlag,
       "mwWncVarsManagementFromWirelessClients": mwWncVarsManagementFromWirelessClients,
       "mwWncVarsControllerIndex": mwWncVarsControllerIndex,
       "mwWncVarsTopoUpdate": mwWncVarsTopoUpdate,
       "mwWncVarsFastPath": mwWncVarsFastPath,
       "mwWncVarsBonding": mwWncVarsBonding,
       "mwWncVarsNodeId": mwWncVarsNodeId,
       "mwWncVarsHostName": mwWncVarsHostName,
       "mwWncVarsUpTime": mwWncVarsUpTime,
       "mwWncVarsOperationalState": mwWncVarsOperationalState,
       "mwWncVarsAvailabilityStatus": mwWncVarsAvailabilityStatus,
       "mwWncVarsAlarmState": mwWncVarsAlarmState,
       "mwWncVarsVirtualIpAddress": mwWncVarsVirtualIpAddress,
       "mwWncVarsVirtualNetMask": mwWncVarsVirtualNetMask,
       "mwWncVarsDefaultGatewayAddr": mwWncVarsDefaultGatewayAddr,
       "mwWncVarsSoftwareVersion": mwWncVarsSoftwareVersion,
       "mwWncVarsSerialNumber": mwWncVarsSerialNumber,
       "mwWncVarsSystemId": mwWncVarsSystemId,
       "mwWncVarsHardwareType": mwWncVarsHardwareType,
       "mwWncVarsCountry": mwWncVarsCountry,
       "mwWncVarsManSerialNumber": mwWncVarsManSerialNumber,
       "mwWncVarsStationAgingOutPeriod": mwWncVarsStationAgingOutPeriod,
       "mwWncVarsRoamingDomainState": mwWncVarsRoamingDomainState,
       "mwWncVarsAssocStationMaxIdlePeriod": mwWncVarsAssocStationMaxIdlePeriod,
       "mwWncVarsL3RoutingMode": mwWncVarsL3RoutingMode,
       "mwWncVarsRegion": mwWncVarsRegion,
       "mwSystemFileVars": mwSystemFileVars,
       "mwSystemFileVarspHostName": mwSystemFileVarspHostName,
       "mwSystemFileVarspDnsDomainName": mwSystemFileVarspDnsDomainName,
       "mwUdpBcastUpstreamTable": mwUdpBcastUpstreamTable,
       "mwUdpBcastUpstreamEntry": mwUdpBcastUpstreamEntry,
       "mwUdpBcastUpstreamTableIndex": mwUdpBcastUpstreamTableIndex,
       "mwUdpBcastUpstreamPort": mwUdpBcastUpstreamPort,
       "mwUdpBcastUpstreamRowStatus": mwUdpBcastUpstreamRowStatus,
       "mwUdpBcastDownstreamTable": mwUdpBcastDownstreamTable,
       "mwUdpBcastDownstreamEntry": mwUdpBcastDownstreamEntry,
       "mwUdpBcastDownstreamTableIndex": mwUdpBcastDownstreamTableIndex,
       "mwUdpBcastDownstreamPort": mwUdpBcastDownstreamPort,
       "mwUdpBcastDownstreamRowStatus": mwUdpBcastDownstreamRowStatus,
       "mwDnsServerTable": mwDnsServerTable,
       "mwDnsServerEntry": mwDnsServerEntry,
       "mwDnsServerTableIndex": mwDnsServerTableIndex,
       "mwDnsServer": mwDnsServer,
       "mwDnsServerRowStatus": mwDnsServerRowStatus,
       "mwWncNetworkConfigTable": mwWncNetworkConfigTable,
       "mwWncNetworkConfigEntry": mwWncNetworkConfigEntry,
       "mwWncNetworkConfigTableIndex": mwWncNetworkConfigTableIndex,
       "mwWncNetworkConfigFastPath": mwWncNetworkConfigFastPath,
       "mwWncNetworkConfigBonding": mwWncNetworkConfigBonding,
       "mwWncNetworkConfigTenGigModule": mwWncNetworkConfigTenGigModule,
       "mwWncNetworkConfigRowStatus": mwWncNetworkConfigRowStatus,
       "mwVirtualInterfaceProfileTable": mwVirtualInterfaceProfileTable,
       "mwVirtualInterfaceProfileEntry": mwVirtualInterfaceProfileEntry,
       "mwVirtualInterfaceProfileTableIndex": mwVirtualInterfaceProfileTableIndex,
       "mwVirtualInterfaceProfileName": mwVirtualInterfaceProfileName,
       "mwVirtualInterfaceProfileId": mwVirtualInterfaceProfileId,
       "mwVirtualInterfaceProfileState": mwVirtualInterfaceProfileState,
       "mwVirtualInterfaceProfileSubnetIp": mwVirtualInterfaceProfileSubnetIp,
       "mwVirtualInterfaceProfileSubnetMask": mwVirtualInterfaceProfileSubnetMask,
       "mwVirtualInterfaceProfileGatewayIp": mwVirtualInterfaceProfileGatewayIp,
       "mwVirtualInterfaceProfileRowStatus": mwVirtualInterfaceProfileRowStatus,
       "mwDhcpServerTable": mwDhcpServerTable,
       "mwDhcpServerEntry": mwDhcpServerEntry,
       "mwDhcpServerTableIndex": mwDhcpServerTableIndex,
       "mwDhcpServerName": mwDhcpServerName,
       "mwDhcpServerVlanName": mwDhcpServerVlanName,
       "mwDhcpServerVirtualInterfaceProfileName": mwDhcpServerVirtualInterfaceProfileName,
       "mwDhcpServerState": mwDhcpServerState,
       "mwDhcpServerLeaseTime": mwDhcpServerLeaseTime,
       "mwDhcpServerIpPoolStart": mwDhcpServerIpPoolStart,
       "mwDhcpServerIpPoolEnd": mwDhcpServerIpPoolEnd,
       "mwDhcpServerDomainName": mwDhcpServerDomainName,
       "mwDhcpServerDnsServer1": mwDhcpServerDnsServer1,
       "mwDhcpServerDnsServer2": mwDhcpServerDnsServer2,
       "mwDhcpServerNetbiosServer1": mwDhcpServerNetbiosServer1,
       "mwDhcpServerNetbiosServer2": mwDhcpServerNetbiosServer2,
       "mwDhcpServerOption43": mwDhcpServerOption43,
       "mwDhcpServerRowStatus": mwDhcpServerRowStatus,
       "mwVpnServer": mwVpnServer,
       "mwVpnServerState": mwVpnServerState,
       "mwVpnServerIp": mwVpnServerIp,
       "mwVpnServerHostName": mwVpnServerHostName,
       "mwVpnServerPort": mwVpnServerPort,
       "mwVpnServerIpPool": mwVpnServerIpPool,
       "mwVpnServerSubnetMask": mwVpnServerSubnetMask,
       "mwVpnClient": mwVpnClient,
       "mwVpnClientState": mwVpnClientState,
       "mwVpnClientVpnServerIp": mwVpnClientVpnServerIp,
       "mwVpnClientVpnServerPort": mwVpnClientVpnServerPort,
       "mwVpnClientStatus": mwVpnClientStatus,
       "mwUdpBcastUpstreamBridgedTable": mwUdpBcastUpstreamBridgedTable,
       "mwUdpBcastUpstreamBridgedEntry": mwUdpBcastUpstreamBridgedEntry,
       "mwUdpBcastUpstreamBridgedTableIndex": mwUdpBcastUpstreamBridgedTableIndex,
       "mwUdpBcastUpstreamBridgedPort": mwUdpBcastUpstreamBridgedPort,
       "mwUdpBcastUpstreamBridgedRowStatus": mwUdpBcastUpstreamBridgedRowStatus,
       "mwUdpBcastDownstreamBridgedTable": mwUdpBcastDownstreamBridgedTable,
       "mwUdpBcastDownstreamBridgedEntry": mwUdpBcastDownstreamBridgedEntry,
       "mwUdpBcastDownstreamBridgedTableIndex": mwUdpBcastDownstreamBridgedTableIndex,
       "mwUdpBcastDownstreamBridgedPort": mwUdpBcastDownstreamBridgedPort,
       "mwUdpBcastDownstreamBridgedRowStatus": mwUdpBcastDownstreamBridgedRowStatus}
)
