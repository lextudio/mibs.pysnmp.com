# SNMP MIB module (PHION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PHION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:38 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

phion = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10704)
)
phion.setRevisions(
        ("2014-01-08 00:00",
         "2014-01-07 00:00",
         "2013-12-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ServiceState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("removed", 4),
          ("started", 1),
          ("stopped", 0),
          ("unknown", -1))
    )



class SensorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fan", 1),
          ("psu-status", 3),
          ("temperature", 2),
          ("unknown", -1),
          ("voltage", 0))
    )



class RaidEventSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("debug", 4),
          ("error", 1),
          ("information", 3),
          ("unknown", 0),
          ("warning", 2))
    )



class VpnStates(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", -1),
          ("down-disabled", 0))
    )



# MIB Managed Objects in the order of their OIDs

_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 1)
)
_BoxServices_Object = MibTable
boxServices = _BoxServices_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 0)
)
if mibBuilder.loadTexts:
    boxServices.setStatus("current")
_BoxServicesEntry_Object = MibTableRow
boxServicesEntry = _BoxServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 0, 1)
)
boxServicesEntry.setIndexNames(
    (0, "PHION-MIB", "boxServiceName"),
)
if mibBuilder.loadTexts:
    boxServicesEntry.setStatus("current")


class _BoxServiceName_Type(DisplayString):
    """Custom type boxServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BoxServiceName_Type.__name__ = "DisplayString"
_BoxServiceName_Object = MibTableColumn
boxServiceName = _BoxServiceName_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 0, 1, 1),
    _BoxServiceName_Type()
)
boxServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServiceName.setStatus("current")
_BoxServiceState_Type = ServiceState
_BoxServiceState_Object = MibTableColumn
boxServiceState = _BoxServiceState_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 0, 1, 2),
    _BoxServiceState_Type()
)
boxServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServiceState.setStatus("current")
_ServerServices_Object = MibTable
serverServices = _ServerServices_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 1)
)
if mibBuilder.loadTexts:
    serverServices.setStatus("current")
_ServerServicesEntry_Object = MibTableRow
serverServicesEntry = _ServerServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 1, 1)
)
serverServicesEntry.setIndexNames(
    (0, "PHION-MIB", "serverServiceName"),
)
if mibBuilder.loadTexts:
    serverServicesEntry.setStatus("current")


class _ServerServiceName_Type(DisplayString):
    """Custom type serverServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ServerServiceName_Type.__name__ = "DisplayString"
_ServerServiceName_Object = MibTableColumn
serverServiceName = _ServerServiceName_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 1, 1, 1),
    _ServerServiceName_Type()
)
serverServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverServiceName.setStatus("current")
_ServerServiceState_Type = ServiceState
_ServerServiceState_Object = MibTableColumn
serverServiceState = _ServerServiceState_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 1, 1, 2),
    _ServerServiceState_Type()
)
serverServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverServiceState.setStatus("current")
_PhionRelease_Type = DisplayString
_PhionRelease_Object = MibScalar
phionRelease = _PhionRelease_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 2),
    _PhionRelease_Type()
)
phionRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phionRelease.setStatus("current")
_PhionHotfixes_Object = MibTable
phionHotfixes = _PhionHotfixes_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 3)
)
if mibBuilder.loadTexts:
    phionHotfixes.setStatus("current")
_PhionHotfixesEntry_Object = MibTableRow
phionHotfixesEntry = _PhionHotfixesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 3, 1)
)
phionHotfixesEntry.setIndexNames(
    (0, "PHION-MIB", "hotfixName"),
)
if mibBuilder.loadTexts:
    phionHotfixesEntry.setStatus("current")


class _HotfixName_Type(DisplayString):
    """Custom type hotfixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HotfixName_Type.__name__ = "DisplayString"
_HotfixName_Object = MibTableColumn
hotfixName = _HotfixName_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 3, 1, 1),
    _HotfixName_Type()
)
hotfixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotfixName.setStatus("current")
_HotfixInstallTime_Type = DateAndTime
_HotfixInstallTime_Object = MibTableColumn
hotfixInstallTime = _HotfixInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 3, 1, 2),
    _HotfixInstallTime_Type()
)
hotfixInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotfixInstallTime.setStatus("current")
_HwSensors_Object = MibTable
hwSensors = _HwSensors_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 4)
)
if mibBuilder.loadTexts:
    hwSensors.setStatus("current")
_HwSensorsEntry_Object = MibTableRow
hwSensorsEntry = _HwSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 4, 1)
)
hwSensorsEntry.setIndexNames(
    (0, "PHION-MIB", "hwSensorName"),
)
if mibBuilder.loadTexts:
    hwSensorsEntry.setStatus("current")


class _HwSensorName_Type(DisplayString):
    """Custom type hwSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwSensorName_Type.__name__ = "DisplayString"
_HwSensorName_Object = MibTableColumn
hwSensorName = _HwSensorName_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 1),
    _HwSensorName_Type()
)
hwSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensorName.setStatus("current")
_HwSensorType_Type = SensorType
_HwSensorType_Object = MibTableColumn
hwSensorType = _HwSensorType_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 2),
    _HwSensorType_Type()
)
hwSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensorType.setStatus("current")
_HwSensorValue_Type = Integer32
_HwSensorValue_Object = MibTableColumn
hwSensorValue = _HwSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 4, 1, 3),
    _HwSensorValue_Type()
)
hwSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensorValue.setStatus("current")
_RaidEvents_Object = MibTable
raidEvents = _RaidEvents_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 5)
)
if mibBuilder.loadTexts:
    raidEvents.setStatus("current")
_RaidEventsEntry_Object = MibTableRow
raidEventsEntry = _RaidEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 5, 1)
)
raidEventsEntry.setIndexNames(
    (0, "PHION-MIB", "raidEventIndex"),
)
if mibBuilder.loadTexts:
    raidEventsEntry.setStatus("current")


class _RaidEventIndex_Type(Integer32):
    """Custom type raidEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaidEventIndex_Type.__name__ = "Integer32"
_RaidEventIndex_Object = MibTableColumn
raidEventIndex = _RaidEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 1),
    _RaidEventIndex_Type()
)
raidEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidEventIndex.setStatus("current")
_RaidEventSev_Type = RaidEventSeverity
_RaidEventSev_Object = MibTableColumn
raidEventSev = _RaidEventSev_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 2),
    _RaidEventSev_Type()
)
raidEventSev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidEventSev.setStatus("current")
_RaidEventTime_Type = DateAndTime
_RaidEventTime_Object = MibTableColumn
raidEventTime = _RaidEventTime_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 3),
    _RaidEventTime_Type()
)
raidEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidEventTime.setStatus("current")
_RaidEventText_Type = DisplayString
_RaidEventText_Object = MibTableColumn
raidEventText = _RaidEventText_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 5, 1, 4),
    _RaidEventText_Type()
)
raidEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidEventText.setStatus("current")
_VpnTunnels_Object = MibTable
vpnTunnels = _VpnTunnels_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 6)
)
if mibBuilder.loadTexts:
    vpnTunnels.setStatus("current")
_VpnTunnelsEntry_Object = MibTableRow
vpnTunnelsEntry = _VpnTunnelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 6, 1)
)
vpnTunnelsEntry.setIndexNames(
    (0, "PHION-MIB", "vpnName"),
)
if mibBuilder.loadTexts:
    vpnTunnelsEntry.setStatus("current")


class _VpnName_Type(DisplayString):
    """Custom type vpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VpnName_Type.__name__ = "DisplayString"
_VpnName_Object = MibTableColumn
vpnName = _VpnName_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 6, 1, 1),
    _VpnName_Type()
)
vpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnName.setStatus("current")
_VpnState_Type = VpnStates
_VpnState_Object = MibTableColumn
vpnState = _VpnState_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 6, 1, 2),
    _VpnState_Type()
)
vpnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnState.setStatus("current")
_BgpNeighbors_Object = MibTable
bgpNeighbors = _BgpNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 7)
)
if mibBuilder.loadTexts:
    bgpNeighbors.setStatus("current")
_BgpNeighborsEntry_Object = MibTableRow
bgpNeighborsEntry = _BgpNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 7, 1)
)
bgpNeighborsEntry.setIndexNames(
    (0, "PHION-MIB", "bgpNeighborAddress"),
)
if mibBuilder.loadTexts:
    bgpNeighborsEntry.setStatus("current")


class _BgpNeighborAddress_Type(DisplayString):
    """Custom type bgpNeighborAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BgpNeighborAddress_Type.__name__ = "DisplayString"
_BgpNeighborAddress_Object = MibTableColumn
bgpNeighborAddress = _BgpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 7, 1, 1),
    _BgpNeighborAddress_Type()
)
bgpNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNeighborAddress.setStatus("current")
_BgpNeighborState_Type = Integer32
_BgpNeighborState_Object = MibTableColumn
bgpNeighborState = _BgpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 7, 1, 2),
    _BgpNeighborState_Type()
)
bgpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNeighborState.setStatus("current")
_OspfNeighbors_Object = MibTable
ospfNeighbors = _OspfNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 8)
)
if mibBuilder.loadTexts:
    ospfNeighbors.setStatus("current")
_OspfNeighborsEntry_Object = MibTableRow
ospfNeighborsEntry = _OspfNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 8, 1)
)
ospfNeighborsEntry.setIndexNames(
    (0, "PHION-MIB", "ospfNeighborId"),
)
if mibBuilder.loadTexts:
    ospfNeighborsEntry.setStatus("current")


class _OspfNeighborId_Type(DisplayString):
    """Custom type ospfNeighborId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OspfNeighborId_Type.__name__ = "DisplayString"
_OspfNeighborId_Object = MibTableColumn
ospfNeighborId = _OspfNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 1),
    _OspfNeighborId_Type()
)
ospfNeighborId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborId.setStatus("current")


class _OspfNeighborAddress_Type(DisplayString):
    """Custom type ospfNeighborAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OspfNeighborAddress_Type.__name__ = "DisplayString"
_OspfNeighborAddress_Object = MibTableColumn
ospfNeighborAddress = _OspfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 2),
    _OspfNeighborAddress_Type()
)
ospfNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborAddress.setStatus("current")


class _OspfNeighborInterface_Type(DisplayString):
    """Custom type ospfNeighborInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OspfNeighborInterface_Type.__name__ = "DisplayString"
_OspfNeighborInterface_Object = MibTableColumn
ospfNeighborInterface = _OspfNeighborInterface_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 3),
    _OspfNeighborInterface_Type()
)
ospfNeighborInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborInterface.setStatus("current")


class _OspfNeighborStatus_Type(DisplayString):
    """Custom type ospfNeighborStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OspfNeighborStatus_Type.__name__ = "DisplayString"
_OspfNeighborStatus_Object = MibTableColumn
ospfNeighborStatus = _OspfNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 8, 1, 4),
    _OspfNeighborStatus_Type()
)
ospfNeighborStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborStatus.setStatus("current")
_RipNeighbors_Object = MibTable
ripNeighbors = _RipNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 9)
)
if mibBuilder.loadTexts:
    ripNeighbors.setStatus("current")
_RipNeighborsEntry_Object = MibTableRow
ripNeighborsEntry = _RipNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 9, 1)
)
ripNeighborsEntry.setIndexNames(
    (0, "PHION-MIB", "ripNeighborAddress"),
)
if mibBuilder.loadTexts:
    ripNeighborsEntry.setStatus("current")


class _RipNeighborAddress_Type(DisplayString):
    """Custom type ripNeighborAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RipNeighborAddress_Type.__name__ = "DisplayString"
_RipNeighborAddress_Object = MibTableColumn
ripNeighborAddress = _RipNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 9, 1, 1),
    _RipNeighborAddress_Type()
)
ripNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNeighborAddress.setStatus("current")


class _RipNeighborState_Type(DisplayString):
    """Custom type ripNeighborState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RipNeighborState_Type.__name__ = "DisplayString"
_RipNeighborState_Object = MibTableColumn
ripNeighborState = _RipNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 9, 1, 2),
    _RipNeighborState_Type()
)
ripNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNeighborState.setStatus("current")
_FwStats_Object = MibTable
fwStats = _FwStats_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 10)
)
if mibBuilder.loadTexts:
    fwStats.setStatus("current")
_FwStatsEntry_Object = MibTableRow
fwStatsEntry = _FwStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 10, 1)
)
fwStatsEntry.setIndexNames(
    (0, "PHION-MIB", "firewallSessions"),
)
if mibBuilder.loadTexts:
    fwStatsEntry.setStatus("current")
_FirewallSessions_Type = Integer32
_FirewallSessions_Object = MibTableColumn
firewallSessions = _FirewallSessions_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 1),
    _FirewallSessions_Type()
)
firewallSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessions.setStatus("current")
_PacketThroughput_Type = Integer32
_PacketThroughput_Object = MibTableColumn
packetThroughput = _PacketThroughput_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 2),
    _PacketThroughput_Type()
)
packetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetThroughput.setStatus("current")
_DataThroughput_Type = Integer32
_DataThroughput_Object = MibTableColumn
dataThroughput = _DataThroughput_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 10, 1, 3),
    _DataThroughput_Type()
)
dataThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataThroughput.setStatus("current")
_VpnUsers_Type = Integer32
_VpnUsers_Object = MibScalar
vpnUsers = _VpnUsers_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 11),
    _VpnUsers_Type()
)
vpnUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnUsers.setStatus("current")
_TrafficShape_Object = MibTable
trafficShape = _TrafficShape_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12)
)
if mibBuilder.loadTexts:
    trafficShape.setStatus("current")
_TrafficShapeEntry_Object = MibTableRow
trafficShapeEntry = _TrafficShapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1)
)
trafficShapeEntry.setIndexNames(
    (0, "PHION-MIB", "connectorName"),
)
if mibBuilder.loadTexts:
    trafficShapeEntry.setStatus("current")


class _ConnectorName_Type(DisplayString):
    """Custom type connectorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConnectorName_Type.__name__ = "DisplayString"
_ConnectorName_Object = MibTableColumn
connectorName = _ConnectorName_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 1),
    _ConnectorName_Type()
)
connectorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectorName.setStatus("current")
_Rate_Type = Counter64
_Rate_Object = MibTableColumn
rate = _Rate_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 2),
    _Rate_Type()
)
rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rate.setStatus("current")
_Sessions_Type = Counter64
_Sessions_Object = MibTableColumn
sessions = _Sessions_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 3),
    _Sessions_Type()
)
sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessions.setStatus("current")
_Class1Total_Type = Counter64
_Class1Total_Object = MibTableColumn
class1Total = _Class1Total_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 4),
    _Class1Total_Type()
)
class1Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class1Total.setStatus("current")
_Class1Pakets_Type = Counter64
_Class1Pakets_Object = MibTableColumn
class1Pakets = _Class1Pakets_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 5),
    _Class1Pakets_Type()
)
class1Pakets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class1Pakets.setStatus("current")
_Class1Drop_Type = Counter64
_Class1Drop_Object = MibTableColumn
class1Drop = _Class1Drop_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 6),
    _Class1Drop_Type()
)
class1Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class1Drop.setStatus("current")
_Class2Total_Type = Counter64
_Class2Total_Object = MibTableColumn
class2Total = _Class2Total_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 7),
    _Class2Total_Type()
)
class2Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class2Total.setStatus("current")
_Class2Pakets_Type = Counter64
_Class2Pakets_Object = MibTableColumn
class2Pakets = _Class2Pakets_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 8),
    _Class2Pakets_Type()
)
class2Pakets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class2Pakets.setStatus("current")
_Class2Drop_Type = Counter64
_Class2Drop_Object = MibTableColumn
class2Drop = _Class2Drop_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 9),
    _Class2Drop_Type()
)
class2Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class2Drop.setStatus("current")
_Class3Total_Type = Counter64
_Class3Total_Object = MibTableColumn
class3Total = _Class3Total_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 10),
    _Class3Total_Type()
)
class3Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class3Total.setStatus("current")
_Class3Pakets_Type = Counter64
_Class3Pakets_Object = MibTableColumn
class3Pakets = _Class3Pakets_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 11),
    _Class3Pakets_Type()
)
class3Pakets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class3Pakets.setStatus("current")
_Class3Drop_Type = Counter64
_Class3Drop_Object = MibTableColumn
class3Drop = _Class3Drop_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 12),
    _Class3Drop_Type()
)
class3Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    class3Drop.setStatus("current")
_NoDelayTotal_Type = Counter64
_NoDelayTotal_Object = MibTableColumn
noDelayTotal = _NoDelayTotal_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 13),
    _NoDelayTotal_Type()
)
noDelayTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noDelayTotal.setStatus("current")
_NoDelayPakets_Type = Counter64
_NoDelayPakets_Object = MibTableColumn
noDelayPakets = _NoDelayPakets_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 14),
    _NoDelayPakets_Type()
)
noDelayPakets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noDelayPakets.setStatus("current")
_NoDelayDrop_Type = Counter64
_NoDelayDrop_Object = MibTableColumn
noDelayDrop = _NoDelayDrop_Object(
    (1, 3, 6, 1, 4, 1, 10704, 1, 12, 1, 15),
    _NoDelayDrop_Type()
)
noDelayDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noDelayDrop.setStatus("current")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 10)
)


class _EventID_Type(DisplayString):
    """Custom type eventID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_EventID_Type.__name__ = "DisplayString"
_EventID_Object = MibScalar
eventID = _EventID_Object(
    (1, 3, 6, 1, 4, 1, 10704, 10, 1),
    _EventID_Type()
)
eventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventID.setStatus("current")
_EventIDDescription_Type = DisplayString
_EventIDDescription_Object = MibScalar
eventIDDescription = _EventIDDescription_Object(
    (1, 3, 6, 1, 4, 1, 10704, 10, 2),
    _EventIDDescription_Type()
)
eventIDDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIDDescription.setStatus("current")


class _EventType_Type(DisplayString):
    """Custom type eventType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_EventType_Type.__name__ = "DisplayString"
_EventType_Object = MibScalar
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 10704, 10, 3),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("current")


class _EventAlarmTime_Type(DisplayString):
    """Custom type eventAlarmTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_EventAlarmTime_Type.__name__ = "DisplayString"
_EventAlarmTime_Object = MibScalar
eventAlarmTime = _EventAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 10704, 10, 4),
    _EventAlarmTime_Type()
)
eventAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmTime.setStatus("current")
_EventLayerDescription_Type = DisplayString
_EventLayerDescription_Object = MibScalar
eventLayerDescription = _EventLayerDescription_Object(
    (1, 3, 6, 1, 4, 1, 10704, 10, 5),
    _EventLayerDescription_Type()
)
eventLayerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLayerDescription.setStatus("current")
_EventClassification_Type = DisplayString
_EventClassification_Object = MibScalar
eventClassification = _EventClassification_Object(
    (1, 3, 6, 1, 4, 1, 10704, 10, 6),
    _EventClassification_Type()
)
eventClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventClassification.setStatus("current")
_EventRepresentation_Type = DisplayString
_EventRepresentation_Object = MibScalar
eventRepresentation = _EventRepresentation_Object(
    (1, 3, 6, 1, 4, 1, 10704, 10, 7),
    _EventRepresentation_Type()
)
eventRepresentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventRepresentation.setStatus("current")
_EventSeverity_Type = DisplayString
_EventSeverity_Object = MibScalar
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10704, 10, 8),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_FwCompliances_ObjectIdentity = ObjectIdentity
fwCompliances = _FwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 20)
)
_FwGroups_ObjectIdentity = ObjectIdentity
fwGroups = _FwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 21)
)
_ServiceGroups_ObjectIdentity = ObjectIdentity
serviceGroups = _ServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 21, 1)
)
_FirmwareGroups_ObjectIdentity = ObjectIdentity
firmwareGroups = _FirmwareGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 21, 2)
)
_HwGroups_ObjectIdentity = ObjectIdentity
hwGroups = _HwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 21, 3)
)
_NetGroups_ObjectIdentity = ObjectIdentity
netGroups = _NetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 21, 4)
)
_EventGroups_ObjectIdentity = ObjectIdentity
eventGroups = _EventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10704, 21, 5)
)

# Managed Objects groups

boxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 1, 1)
)
boxGroup.setObjects(
      *(("PHION-MIB", "boxServiceName"),
        ("PHION-MIB", "boxServiceState"))
)
if mibBuilder.loadTexts:
    boxGroup.setStatus("current")

serverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 1, 2)
)
serverGroup.setObjects(
      *(("PHION-MIB", "serverServiceName"),
        ("PHION-MIB", "serverServiceState"))
)
if mibBuilder.loadTexts:
    serverGroup.setStatus("current")

releaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 2, 1)
)
releaseGroup.setObjects(
    ("PHION-MIB", "phionRelease")
)
if mibBuilder.loadTexts:
    releaseGroup.setStatus("current")

hotfixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 2, 2)
)
hotfixGroup.setObjects(
      *(("PHION-MIB", "hotfixName"),
        ("PHION-MIB", "hotfixInstallTime"))
)
if mibBuilder.loadTexts:
    hotfixGroup.setStatus("current")

hwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 3, 1)
)
hwGroup.setObjects(
      *(("PHION-MIB", "hwSensorName"),
        ("PHION-MIB", "hwSensorType"),
        ("PHION-MIB", "hwSensorValue"))
)
if mibBuilder.loadTexts:
    hwGroup.setStatus("current")

raidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 3, 2)
)
raidGroup.setObjects(
      *(("PHION-MIB", "raidEventIndex"),
        ("PHION-MIB", "raidEventSev"),
        ("PHION-MIB", "raidEventTime"),
        ("PHION-MIB", "raidEventText"))
)
if mibBuilder.loadTexts:
    raidGroup.setStatus("current")

fwstatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 3, 3)
)
fwstatsGroup.setObjects(
      *(("PHION-MIB", "firewallSessions"),
        ("PHION-MIB", "packetThroughput"),
        ("PHION-MIB", "dataThroughput"))
)
if mibBuilder.loadTexts:
    fwstatsGroup.setStatus("current")

trafficshapeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 3, 4)
)
trafficshapeGroup.setObjects(
      *(("PHION-MIB", "connectorName"),
        ("PHION-MIB", "rate"),
        ("PHION-MIB", "sessions"),
        ("PHION-MIB", "class1Total"),
        ("PHION-MIB", "class1Pakets"),
        ("PHION-MIB", "class1Drop"),
        ("PHION-MIB", "class2Total"),
        ("PHION-MIB", "class2Pakets"),
        ("PHION-MIB", "class2Drop"),
        ("PHION-MIB", "class3Total"),
        ("PHION-MIB", "class3Pakets"),
        ("PHION-MIB", "class3Drop"),
        ("PHION-MIB", "noDelayTotal"),
        ("PHION-MIB", "noDelayPakets"),
        ("PHION-MIB", "noDelayDrop"))
)
if mibBuilder.loadTexts:
    trafficshapeGroup.setStatus("current")

vpnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 4, 1)
)
vpnGroup.setObjects(
      *(("PHION-MIB", "vpnName"),
        ("PHION-MIB", "vpnState"))
)
if mibBuilder.loadTexts:
    vpnGroup.setStatus("current")

bgpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 4, 2)
)
bgpGroup.setObjects(
      *(("PHION-MIB", "bgpNeighborAddress"),
        ("PHION-MIB", "bgpNeighborState"))
)
if mibBuilder.loadTexts:
    bgpGroup.setStatus("current")

ospfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 4, 3)
)
ospfGroup.setObjects(
      *(("PHION-MIB", "ospfNeighborId"),
        ("PHION-MIB", "ospfNeighborAddress"),
        ("PHION-MIB", "ospfNeighborInterface"),
        ("PHION-MIB", "ospfNeighborStatus"))
)
if mibBuilder.loadTexts:
    ospfGroup.setStatus("current")

ripGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 4, 4)
)
ripGroup.setObjects(
      *(("PHION-MIB", "ripNeighborAddress"),
        ("PHION-MIB", "ripNeighborState"))
)
if mibBuilder.loadTexts:
    ripGroup.setStatus("current")

vpnusersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 4, 5)
)
vpnusersGroup.setObjects(
    ("PHION-MIB", "vpnUsers")
)
if mibBuilder.loadTexts:
    vpnusersGroup.setStatus("current")

eventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 5, 1)
)
eventGroup.setObjects(
      *(("PHION-MIB", "eventID"),
        ("PHION-MIB", "eventIDDescription"),
        ("PHION-MIB", "eventType"),
        ("PHION-MIB", "eventAlarmTime"),
        ("PHION-MIB", "eventLayerDescription"),
        ("PHION-MIB", "eventClassification"),
        ("PHION-MIB", "eventRepresentation"),
        ("PHION-MIB", "eventSeverity"))
)
if mibBuilder.loadTexts:
    eventGroup.setStatus("current")


# Notification objects

eventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10704, 11)
)
eventTrap.setObjects(
      *(("PHION-MIB", "eventID"),
        ("PHION-MIB", "eventIDDescription"),
        ("PHION-MIB", "eventType"),
        ("PHION-MIB", "eventAlarmTime"),
        ("PHION-MIB", "eventLayerDescription"),
        ("PHION-MIB", "eventClassification"),
        ("PHION-MIB", "eventRepresentation"),
        ("PHION-MIB", "eventSeverity"))
)
if mibBuilder.loadTexts:
    eventTrap.setStatus(
        "current"
    )


# Notifications groups

notificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10704, 21, 5, 2)
)
notificationGroup.setObjects(
    ("PHION-MIB", "eventTrap")
)
if mibBuilder.loadTexts:
    notificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10704, 20, 1)
)
if mibBuilder.loadTexts:
    fwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PHION-MIB",
    **{"ServiceState": ServiceState,
       "SensorType": SensorType,
       "RaidEventSeverity": RaidEventSeverity,
       "VpnStates": VpnStates,
       "phion": phion,
       "firewall": firewall,
       "boxServices": boxServices,
       "boxServicesEntry": boxServicesEntry,
       "boxServiceName": boxServiceName,
       "boxServiceState": boxServiceState,
       "serverServices": serverServices,
       "serverServicesEntry": serverServicesEntry,
       "serverServiceName": serverServiceName,
       "serverServiceState": serverServiceState,
       "phionRelease": phionRelease,
       "phionHotfixes": phionHotfixes,
       "phionHotfixesEntry": phionHotfixesEntry,
       "hotfixName": hotfixName,
       "hotfixInstallTime": hotfixInstallTime,
       "hwSensors": hwSensors,
       "hwSensorsEntry": hwSensorsEntry,
       "hwSensorName": hwSensorName,
       "hwSensorType": hwSensorType,
       "hwSensorValue": hwSensorValue,
       "raidEvents": raidEvents,
       "raidEventsEntry": raidEventsEntry,
       "raidEventIndex": raidEventIndex,
       "raidEventSev": raidEventSev,
       "raidEventTime": raidEventTime,
       "raidEventText": raidEventText,
       "vpnTunnels": vpnTunnels,
       "vpnTunnelsEntry": vpnTunnelsEntry,
       "vpnName": vpnName,
       "vpnState": vpnState,
       "bgpNeighbors": bgpNeighbors,
       "bgpNeighborsEntry": bgpNeighborsEntry,
       "bgpNeighborAddress": bgpNeighborAddress,
       "bgpNeighborState": bgpNeighborState,
       "ospfNeighbors": ospfNeighbors,
       "ospfNeighborsEntry": ospfNeighborsEntry,
       "ospfNeighborId": ospfNeighborId,
       "ospfNeighborAddress": ospfNeighborAddress,
       "ospfNeighborInterface": ospfNeighborInterface,
       "ospfNeighborStatus": ospfNeighborStatus,
       "ripNeighbors": ripNeighbors,
       "ripNeighborsEntry": ripNeighborsEntry,
       "ripNeighborAddress": ripNeighborAddress,
       "ripNeighborState": ripNeighborState,
       "fwStats": fwStats,
       "fwStatsEntry": fwStatsEntry,
       "firewallSessions": firewallSessions,
       "packetThroughput": packetThroughput,
       "dataThroughput": dataThroughput,
       "vpnUsers": vpnUsers,
       "trafficShape": trafficShape,
       "trafficShapeEntry": trafficShapeEntry,
       "connectorName": connectorName,
       "rate": rate,
       "sessions": sessions,
       "class1Total": class1Total,
       "class1Pakets": class1Pakets,
       "class1Drop": class1Drop,
       "class2Total": class2Total,
       "class2Pakets": class2Pakets,
       "class2Drop": class2Drop,
       "class3Total": class3Total,
       "class3Pakets": class3Pakets,
       "class3Drop": class3Drop,
       "noDelayTotal": noDelayTotal,
       "noDelayPakets": noDelayPakets,
       "noDelayDrop": noDelayDrop,
       "event": event,
       "eventID": eventID,
       "eventIDDescription": eventIDDescription,
       "eventType": eventType,
       "eventAlarmTime": eventAlarmTime,
       "eventLayerDescription": eventLayerDescription,
       "eventClassification": eventClassification,
       "eventRepresentation": eventRepresentation,
       "eventSeverity": eventSeverity,
       "eventTrap": eventTrap,
       "fwCompliances": fwCompliances,
       "fwCompliance": fwCompliance,
       "fwGroups": fwGroups,
       "serviceGroups": serviceGroups,
       "boxGroup": boxGroup,
       "serverGroup": serverGroup,
       "firmwareGroups": firmwareGroups,
       "releaseGroup": releaseGroup,
       "hotfixGroup": hotfixGroup,
       "hwGroups": hwGroups,
       "hwGroup": hwGroup,
       "raidGroup": raidGroup,
       "fwstatsGroup": fwstatsGroup,
       "trafficshapeGroup": trafficshapeGroup,
       "netGroups": netGroups,
       "vpnGroup": vpnGroup,
       "bgpGroup": bgpGroup,
       "ospfGroup": ospfGroup,
       "ripGroup": ripGroup,
       "vpnusersGroup": vpnusersGroup,
       "eventGroups": eventGroups,
       "eventGroup": eventGroup,
       "notificationGroup": notificationGroup}
)
