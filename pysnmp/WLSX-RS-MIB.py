# SNMP MIB module (WLSX-RS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-RS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:11 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaAPDot1dState,
 ArubaActiveState,
 ArubaDot3azStatus,
 ArubaEnableValue,
 ArubaEnet1Mode,
 ArubaOperStateValue,
 ArubaPoeState,
 ArubaPortDuplex,
 ArubaPortSpeed,
 ArubaPortType) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaAPDot1dState",
    "ArubaActiveState",
    "ArubaDot3azStatus",
    "ArubaEnableValue",
    "ArubaEnet1Mode",
    "ArubaOperStateValue",
    "ArubaPoeState",
    "ArubaPortDuplex",
    "ArubaPortSpeed",
    "ArubaPortType")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpManAddress,
 LldpPortId,
 LldpPortIdSubtype,
 LldpSystemCapabilitiesMap) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpManAddress",
    "LldpPortId",
    "LldpPortIdSubtype",
    "LldpSystemCapabilitiesMap")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")

(wlanAPMacAddress,) = mibBuilder.importSymbols(
    "WLSX-WLAN-MIB",
    "wlanAPMacAddress")


# MODULE-IDENTITY

wlsxRSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16)
)
wlsxRSMIB.setRevisions(
        ("1911-06-01 20:12",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxRemoteWiredGroup_ObjectIdentity = ObjectIdentity
wlsxRemoteWiredGroup = _WlsxRemoteWiredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1)
)
_WlsxRemoteAccessPointPortGroup_ObjectIdentity = ObjectIdentity
wlsxRemoteAccessPointPortGroup = _WlsxRemoteAccessPointPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1)
)
_WlsxRemoteWiredPortTable_Object = MibTable
wlsxRemoteWiredPortTable = _WlsxRemoteWiredPortTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxRemoteWiredPortTable.setStatus("current")
_WlsxRemotePortEntry_Object = MibTableRow
wlsxRemotePortEntry = _WlsxRemotePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1)
)
wlsxRemotePortEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-RS-MIB", "remotePortNumber"),
)
if mibBuilder.loadTexts:
    wlsxRemotePortEntry.setStatus("current")
_RemotePortNumber_Type = Unsigned32
_RemotePortNumber_Object = MibTableColumn
remotePortNumber = _RemotePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 1),
    _RemotePortNumber_Type()
)
remotePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remotePortNumber.setStatus("current")
_RemotePortMAC_Type = MacAddress
_RemotePortMAC_Object = MibTableColumn
remotePortMAC = _RemotePortMAC_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 2),
    _RemotePortMAC_Type()
)
remotePortMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortMAC.setStatus("current")
_RemotePortMode_Type = ArubaEnet1Mode
_RemotePortMode_Object = MibTableColumn
remotePortMode = _RemotePortMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 3),
    _RemotePortMode_Type()
)
remotePortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortMode.setStatus("current")
_RemotePortSlotNumber_Type = Unsigned32
_RemotePortSlotNumber_Object = MibTableColumn
remotePortSlotNumber = _RemotePortSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 4),
    _RemotePortSlotNumber_Type()
)
remotePortSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortSlotNumber.setStatus("current")
_RemotePortPortNumber_Type = Unsigned32
_RemotePortPortNumber_Object = MibTableColumn
remotePortPortNumber = _RemotePortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 5),
    _RemotePortPortNumber_Type()
)
remotePortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortPortNumber.setStatus("current")
_RemotePortType_Type = ArubaPortType
_RemotePortType_Object = MibTableColumn
remotePortType = _RemotePortType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 6),
    _RemotePortType_Type()
)
remotePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortType.setStatus("current")
_RemotePortAdminState_Type = ArubaEnableValue
_RemotePortAdminState_Object = MibTableColumn
remotePortAdminState = _RemotePortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 7),
    _RemotePortAdminState_Type()
)
remotePortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortAdminState.setStatus("current")
_RemotePortOperState_Type = ArubaOperStateValue
_RemotePortOperState_Object = MibTableColumn
remotePortOperState = _RemotePortOperState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 8),
    _RemotePortOperState_Type()
)
remotePortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortOperState.setStatus("current")
_RemotePortSpeed_Type = ArubaPortSpeed
_RemotePortSpeed_Object = MibTableColumn
remotePortSpeed = _RemotePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 9),
    _RemotePortSpeed_Type()
)
remotePortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortSpeed.setStatus("current")
_RemotePortDuplex_Type = ArubaPortDuplex
_RemotePortDuplex_Object = MibTableColumn
remotePortDuplex = _RemotePortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 10),
    _RemotePortDuplex_Type()
)
remotePortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortDuplex.setStatus("current")
_RemotePortTxPackets_Type = Counter64
_RemotePortTxPackets_Object = MibTableColumn
remotePortTxPackets = _RemotePortTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 11),
    _RemotePortTxPackets_Type()
)
remotePortTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortTxPackets.setStatus("current")
_RemotePortTxBytes_Type = Counter64
_RemotePortTxBytes_Object = MibTableColumn
remotePortTxBytes = _RemotePortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 12),
    _RemotePortTxBytes_Type()
)
remotePortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortTxBytes.setStatus("current")
_RemotePortRxPackets_Type = Counter64
_RemotePortRxPackets_Object = MibTableColumn
remotePortRxPackets = _RemotePortRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 13),
    _RemotePortRxPackets_Type()
)
remotePortRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortRxPackets.setStatus("current")
_RemotePortRxBytes_Type = Counter64
_RemotePortRxBytes_Object = MibTableColumn
remotePortRxBytes = _RemotePortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 14),
    _RemotePortRxBytes_Type()
)
remotePortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortRxBytes.setStatus("current")
_RemotePortDot3azStatus_Type = ArubaDot3azStatus
_RemotePortDot3azStatus_Object = MibTableColumn
remotePortDot3azStatus = _RemotePortDot3azStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 15),
    _RemotePortDot3azStatus_Type()
)
remotePortDot3azStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortDot3azStatus.setStatus("current")
_RemotePortName_Type = DisplayString
_RemotePortName_Object = MibTableColumn
remotePortName = _RemotePortName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 16),
    _RemotePortName_Type()
)
remotePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortName.setStatus("current")
_RemotePortPoEState_Type = ArubaPoeState
_RemotePortPoEState_Object = MibTableColumn
remotePortPoEState = _RemotePortPoEState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 17),
    _RemotePortPoEState_Type()
)
remotePortPoEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortPoEState.setStatus("current")
_RemotePortSTPState_Type = ArubaAPDot1dState
_RemotePortSTPState_Object = MibTableColumn
remotePortSTPState = _RemotePortSTPState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 1, 1, 18),
    _RemotePortSTPState_Type()
)
remotePortSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePortSTPState.setStatus("current")
_WlsxRemoteWiredUserStatsTable_Object = MibTable
wlsxRemoteWiredUserStatsTable = _WlsxRemoteWiredUserStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxRemoteWiredUserStatsTable.setStatus("current")
_WlsxRemoteWiredUserStatsEntry_Object = MibTableRow
wlsxRemoteWiredUserStatsEntry = _WlsxRemoteWiredUserStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1)
)
wlsxRemoteWiredUserStatsEntry.setIndexNames(
    (0, "WLSX-RS-MIB", "remoteWiredUserPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxRemoteWiredUserStatsEntry.setStatus("current")
_RemoteWiredUserPhyAddress_Type = MacAddress
_RemoteWiredUserPhyAddress_Object = MibTableColumn
remoteWiredUserPhyAddress = _RemoteWiredUserPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 1),
    _RemoteWiredUserPhyAddress_Type()
)
remoteWiredUserPhyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteWiredUserPhyAddress.setStatus("current")
_RemoteWiredUserSlot_Type = Unsigned32
_RemoteWiredUserSlot_Object = MibTableColumn
remoteWiredUserSlot = _RemoteWiredUserSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 2),
    _RemoteWiredUserSlot_Type()
)
remoteWiredUserSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserSlot.setStatus("current")
_RemoteWiredUserPort_Type = Unsigned32
_RemoteWiredUserPort_Object = MibTableColumn
remoteWiredUserPort = _RemoteWiredUserPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 3),
    _RemoteWiredUserPort_Type()
)
remoteWiredUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserPort.setStatus("current")
_RemoteWiredUserVlan_Type = Unsigned32
_RemoteWiredUserVlan_Object = MibTableColumn
remoteWiredUserVlan = _RemoteWiredUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 4),
    _RemoteWiredUserVlan_Type()
)
remoteWiredUserVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserVlan.setStatus("current")
_RemoteWiredUserTxPkts_Type = Counter32
_RemoteWiredUserTxPkts_Object = MibTableColumn
remoteWiredUserTxPkts = _RemoteWiredUserTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 5),
    _RemoteWiredUserTxPkts_Type()
)
remoteWiredUserTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserTxPkts.setStatus("current")
_RemoteWiredUserTxBytes_Type = Counter32
_RemoteWiredUserTxBytes_Object = MibTableColumn
remoteWiredUserTxBytes = _RemoteWiredUserTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 6),
    _RemoteWiredUserTxBytes_Type()
)
remoteWiredUserTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserTxBytes.setStatus("current")
_RemoteWiredUserRxPkts_Type = Counter32
_RemoteWiredUserRxPkts_Object = MibTableColumn
remoteWiredUserRxPkts = _RemoteWiredUserRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 7),
    _RemoteWiredUserRxPkts_Type()
)
remoteWiredUserRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserRxPkts.setStatus("current")
_RemoteWiredUserRxBytes_Type = Counter32
_RemoteWiredUserRxBytes_Object = MibTableColumn
remoteWiredUserRxBytes = _RemoteWiredUserRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 8),
    _RemoteWiredUserRxBytes_Type()
)
remoteWiredUserRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserRxBytes.setStatus("current")
_RemoteWiredUserTxBCastPkts_Type = Counter32
_RemoteWiredUserTxBCastPkts_Object = MibTableColumn
remoteWiredUserTxBCastPkts = _RemoteWiredUserTxBCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 9),
    _RemoteWiredUserTxBCastPkts_Type()
)
remoteWiredUserTxBCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserTxBCastPkts.setStatus("current")
_RemoteWiredUserTxBCastBytes_Type = Counter32
_RemoteWiredUserTxBCastBytes_Object = MibTableColumn
remoteWiredUserTxBCastBytes = _RemoteWiredUserTxBCastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 10),
    _RemoteWiredUserTxBCastBytes_Type()
)
remoteWiredUserTxBCastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserTxBCastBytes.setStatus("current")
_RemoteWiredUserTxMCastPkts_Type = Counter32
_RemoteWiredUserTxMCastPkts_Object = MibTableColumn
remoteWiredUserTxMCastPkts = _RemoteWiredUserTxMCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 11),
    _RemoteWiredUserTxMCastPkts_Type()
)
remoteWiredUserTxMCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserTxMCastPkts.setStatus("current")
_RemoteWiredUserTxMCastBytes_Type = Counter32
_RemoteWiredUserTxMCastBytes_Object = MibTableColumn
remoteWiredUserTxMCastBytes = _RemoteWiredUserTxMCastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 2, 1, 12),
    _RemoteWiredUserTxMCastBytes_Type()
)
remoteWiredUserTxMCastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteWiredUserTxMCastBytes.setStatus("current")
_WlsxLldpNeighborTable_Object = MibTable
wlsxLldpNeighborTable = _WlsxLldpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxLldpNeighborTable.setStatus("current")
_WlsxLldpNeighborEntry_Object = MibTableRow
wlsxLldpNeighborEntry = _WlsxLldpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1)
)
wlsxLldpNeighborEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-RS-MIB", "remotePortNumber"),
    (0, "WLSX-RS-MIB", "lldpNeighborIndex"),
)
if mibBuilder.loadTexts:
    wlsxLldpNeighborEntry.setStatus("current")
_LldpNeighborIndex_Type = Unsigned32
_LldpNeighborIndex_Object = MibTableColumn
lldpNeighborIndex = _LldpNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 1),
    _LldpNeighborIndex_Type()
)
lldpNeighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpNeighborIndex.setStatus("current")
_LldpNeighborChassisIdSubtype_Type = LldpChassisIdSubtype
_LldpNeighborChassisIdSubtype_Object = MibTableColumn
lldpNeighborChassisIdSubtype = _LldpNeighborChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 2),
    _LldpNeighborChassisIdSubtype_Type()
)
lldpNeighborChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborChassisIdSubtype.setStatus("current")
_LldpNeighborChassisId_Type = LldpChassisId
_LldpNeighborChassisId_Object = MibTableColumn
lldpNeighborChassisId = _LldpNeighborChassisId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 3),
    _LldpNeighborChassisId_Type()
)
lldpNeighborChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborChassisId.setStatus("current")
_LldpNeighborPortIdSubtype_Type = LldpPortIdSubtype
_LldpNeighborPortIdSubtype_Object = MibTableColumn
lldpNeighborPortIdSubtype = _LldpNeighborPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 4),
    _LldpNeighborPortIdSubtype_Type()
)
lldpNeighborPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortIdSubtype.setStatus("current")
_LldpNeighborPortId_Type = LldpPortId
_LldpNeighborPortId_Object = MibTableColumn
lldpNeighborPortId = _LldpNeighborPortId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 5),
    _LldpNeighborPortId_Type()
)
lldpNeighborPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortId.setStatus("current")
_LldpNeighborPortDesc_Type = SnmpAdminString
_LldpNeighborPortDesc_Object = MibTableColumn
lldpNeighborPortDesc = _LldpNeighborPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 6),
    _LldpNeighborPortDesc_Type()
)
lldpNeighborPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortDesc.setStatus("current")
_LldpNeighborSysName_Type = SnmpAdminString
_LldpNeighborSysName_Object = MibTableColumn
lldpNeighborSysName = _LldpNeighborSysName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 7),
    _LldpNeighborSysName_Type()
)
lldpNeighborSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborSysName.setStatus("current")
_LldpNeighborSysDesc_Type = SnmpAdminString
_LldpNeighborSysDesc_Object = MibTableColumn
lldpNeighborSysDesc = _LldpNeighborSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 8),
    _LldpNeighborSysDesc_Type()
)
lldpNeighborSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborSysDesc.setStatus("current")
_LldpNeighborSysCapSupported_Type = LldpSystemCapabilitiesMap
_LldpNeighborSysCapSupported_Object = MibTableColumn
lldpNeighborSysCapSupported = _LldpNeighborSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 9),
    _LldpNeighborSysCapSupported_Type()
)
lldpNeighborSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborSysCapSupported.setStatus("current")
_LldpNeighborSysCapEnabled_Type = LldpSystemCapabilitiesMap
_LldpNeighborSysCapEnabled_Object = MibTableColumn
lldpNeighborSysCapEnabled = _LldpNeighborSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 3, 1, 10),
    _LldpNeighborSysCapEnabled_Type()
)
lldpNeighborSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborSysCapEnabled.setStatus("current")
_WlsxLldpNeighborManAddrTable_Object = MibTable
wlsxLldpNeighborManAddrTable = _WlsxLldpNeighborManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wlsxLldpNeighborManAddrTable.setStatus("current")
_WlsxLldpNeighborManAddrEntry_Object = MibTableRow
wlsxLldpNeighborManAddrEntry = _WlsxLldpNeighborManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4, 1)
)
wlsxLldpNeighborManAddrEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-RS-MIB", "remotePortNumber"),
    (0, "WLSX-RS-MIB", "lldpNeighborIndex"),
    (0, "WLSX-RS-MIB", "lldpNeighborManAddrIndex"),
)
if mibBuilder.loadTexts:
    wlsxLldpNeighborManAddrEntry.setStatus("current")
_LldpNeighborManAddrIndex_Type = Unsigned32
_LldpNeighborManAddrIndex_Object = MibTableColumn
lldpNeighborManAddrIndex = _LldpNeighborManAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4, 1, 1),
    _LldpNeighborManAddrIndex_Type()
)
lldpNeighborManAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpNeighborManAddrIndex.setStatus("current")
_LldpNeighborManAddrSubtype_Type = AddressFamilyNumbers
_LldpNeighborManAddrSubtype_Object = MibTableColumn
lldpNeighborManAddrSubtype = _LldpNeighborManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4, 1, 2),
    _LldpNeighborManAddrSubtype_Type()
)
lldpNeighborManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborManAddrSubtype.setStatus("current")
_LldpNeighborManAddr_Type = LldpManAddress
_LldpNeighborManAddr_Object = MibTableColumn
lldpNeighborManAddr = _LldpNeighborManAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 1, 1, 4, 1, 3),
    _LldpNeighborManAddr_Type()
)
lldpNeighborManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborManAddr.setStatus("current")
_WlsxRemoteUSBGroup_ObjectIdentity = ObjectIdentity
wlsxRemoteUSBGroup = _WlsxRemoteUSBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2)
)
_WlsxRemoteAccessPointUSBGroup_ObjectIdentity = ObjectIdentity
wlsxRemoteAccessPointUSBGroup = _WlsxRemoteAccessPointUSBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1)
)
_WlsxRemoteUSBTable_Object = MibTable
wlsxRemoteUSBTable = _WlsxRemoteUSBTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxRemoteUSBTable.setStatus("current")
_WlsxUSBEntry_Object = MibTableRow
wlsxUSBEntry = _WlsxUSBEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1)
)
wlsxUSBEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-RS-MIB", "usbDevNumber"),
)
if mibBuilder.loadTexts:
    wlsxUSBEntry.setStatus("current")
_UsbDevNumber_Type = Unsigned32
_UsbDevNumber_Object = MibTableColumn
usbDevNumber = _UsbDevNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 1),
    _UsbDevNumber_Type()
)
usbDevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDevNumber.setStatus("current")
_UsbStatus_Type = DisplayString
_UsbStatus_Object = MibTableColumn
usbStatus = _UsbStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 2),
    _UsbStatus_Type()
)
usbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbStatus.setStatus("current")
_UsbManufacturer_Type = DisplayString
_UsbManufacturer_Object = MibTableColumn
usbManufacturer = _UsbManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 3),
    _UsbManufacturer_Type()
)
usbManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbManufacturer.setStatus("current")
_UsbProduct_Type = DisplayString
_UsbProduct_Object = MibTableColumn
usbProduct = _UsbProduct_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 4),
    _UsbProduct_Type()
)
usbProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbProduct.setStatus("current")
_UsbSerialNumber_Type = DisplayString
_UsbSerialNumber_Object = MibTableColumn
usbSerialNumber = _UsbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 5),
    _UsbSerialNumber_Type()
)
usbSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbSerialNumber.setStatus("current")
_UsbVendor_Type = DisplayString
_UsbVendor_Object = MibTableColumn
usbVendor = _UsbVendor_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 6),
    _UsbVendor_Type()
)
usbVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbVendor.setStatus("current")
_UsbProductID_Type = DisplayString
_UsbProductID_Object = MibTableColumn
usbProductID = _UsbProductID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 7),
    _UsbProductID_Type()
)
usbProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbProductID.setStatus("current")
_UsbDriver_Type = DisplayString
_UsbDriver_Object = MibTableColumn
usbDriver = _UsbDriver_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 8),
    _UsbDriver_Type()
)
usbDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDriver.setStatus("current")
_UsbRSSI_Type = DisplayString
_UsbRSSI_Object = MibTableColumn
usbRSSI = _UsbRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 9),
    _UsbRSSI_Type()
)
usbRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbRSSI.setStatus("current")
_UsbNetworkServiceLevel_Type = DisplayString
_UsbNetworkServiceLevel_Object = MibTableColumn
usbNetworkServiceLevel = _UsbNetworkServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 10),
    _UsbNetworkServiceLevel_Type()
)
usbNetworkServiceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbNetworkServiceLevel.setStatus("current")
_UsbFirmwareVersion_Type = DisplayString
_UsbFirmwareVersion_Object = MibTableColumn
usbFirmwareVersion = _UsbFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 11),
    _UsbFirmwareVersion_Type()
)
usbFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbFirmwareVersion.setStatus("current")
_UsbEsnNumber_Type = DisplayString
_UsbEsnNumber_Object = MibTableColumn
usbEsnNumber = _UsbEsnNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 12),
    _UsbEsnNumber_Type()
)
usbEsnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbEsnNumber.setStatus("current")
_UsbifOperStatus_Type = ArubaOperStateValue
_UsbifOperStatus_Object = MibTableColumn
usbifOperStatus = _UsbifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 13),
    _UsbifOperStatus_Type()
)
usbifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbifOperStatus.setStatus("current")
_UsbifInUcastPkts_Type = Counter64
_UsbifInUcastPkts_Object = MibTableColumn
usbifInUcastPkts = _UsbifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 14),
    _UsbifInUcastPkts_Type()
)
usbifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbifInUcastPkts.setStatus("current")
_UsbifInUcastOctets_Type = Counter64
_UsbifInUcastOctets_Object = MibTableColumn
usbifInUcastOctets = _UsbifInUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 15),
    _UsbifInUcastOctets_Type()
)
usbifInUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbifInUcastOctets.setStatus("current")
_UsbifOutUcastPkts_Type = Counter64
_UsbifOutUcastPkts_Object = MibTableColumn
usbifOutUcastPkts = _UsbifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 16),
    _UsbifOutUcastPkts_Type()
)
usbifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbifOutUcastPkts.setStatus("current")
_UsbifOutUcastOctets_Type = Counter64
_UsbifOutUcastOctets_Object = MibTableColumn
usbifOutUcastOctets = _UsbifOutUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 17),
    _UsbifOutUcastOctets_Type()
)
usbifOutUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbifOutUcastOctets.setStatus("current")
_UsbifInErrors_Type = Counter64
_UsbifInErrors_Object = MibTableColumn
usbifInErrors = _UsbifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 18),
    _UsbifInErrors_Type()
)
usbifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbifInErrors.setStatus("current")
_UsbifOutErrors_Type = Counter64
_UsbifOutErrors_Object = MibTableColumn
usbifOutErrors = _UsbifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 16, 2, 1, 1, 1, 19),
    _UsbifOutErrors_Type()
)
usbifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbifOutErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-RS-MIB",
    **{"wlsxRSMIB": wlsxRSMIB,
       "wlsxRemoteWiredGroup": wlsxRemoteWiredGroup,
       "wlsxRemoteAccessPointPortGroup": wlsxRemoteAccessPointPortGroup,
       "wlsxRemoteWiredPortTable": wlsxRemoteWiredPortTable,
       "wlsxRemotePortEntry": wlsxRemotePortEntry,
       "remotePortNumber": remotePortNumber,
       "remotePortMAC": remotePortMAC,
       "remotePortMode": remotePortMode,
       "remotePortSlotNumber": remotePortSlotNumber,
       "remotePortPortNumber": remotePortPortNumber,
       "remotePortType": remotePortType,
       "remotePortAdminState": remotePortAdminState,
       "remotePortOperState": remotePortOperState,
       "remotePortSpeed": remotePortSpeed,
       "remotePortDuplex": remotePortDuplex,
       "remotePortTxPackets": remotePortTxPackets,
       "remotePortTxBytes": remotePortTxBytes,
       "remotePortRxPackets": remotePortRxPackets,
       "remotePortRxBytes": remotePortRxBytes,
       "remotePortDot3azStatus": remotePortDot3azStatus,
       "remotePortName": remotePortName,
       "remotePortPoEState": remotePortPoEState,
       "remotePortSTPState": remotePortSTPState,
       "wlsxRemoteWiredUserStatsTable": wlsxRemoteWiredUserStatsTable,
       "wlsxRemoteWiredUserStatsEntry": wlsxRemoteWiredUserStatsEntry,
       "remoteWiredUserPhyAddress": remoteWiredUserPhyAddress,
       "remoteWiredUserSlot": remoteWiredUserSlot,
       "remoteWiredUserPort": remoteWiredUserPort,
       "remoteWiredUserVlan": remoteWiredUserVlan,
       "remoteWiredUserTxPkts": remoteWiredUserTxPkts,
       "remoteWiredUserTxBytes": remoteWiredUserTxBytes,
       "remoteWiredUserRxPkts": remoteWiredUserRxPkts,
       "remoteWiredUserRxBytes": remoteWiredUserRxBytes,
       "remoteWiredUserTxBCastPkts": remoteWiredUserTxBCastPkts,
       "remoteWiredUserTxBCastBytes": remoteWiredUserTxBCastBytes,
       "remoteWiredUserTxMCastPkts": remoteWiredUserTxMCastPkts,
       "remoteWiredUserTxMCastBytes": remoteWiredUserTxMCastBytes,
       "wlsxLldpNeighborTable": wlsxLldpNeighborTable,
       "wlsxLldpNeighborEntry": wlsxLldpNeighborEntry,
       "lldpNeighborIndex": lldpNeighborIndex,
       "lldpNeighborChassisIdSubtype": lldpNeighborChassisIdSubtype,
       "lldpNeighborChassisId": lldpNeighborChassisId,
       "lldpNeighborPortIdSubtype": lldpNeighborPortIdSubtype,
       "lldpNeighborPortId": lldpNeighborPortId,
       "lldpNeighborPortDesc": lldpNeighborPortDesc,
       "lldpNeighborSysName": lldpNeighborSysName,
       "lldpNeighborSysDesc": lldpNeighborSysDesc,
       "lldpNeighborSysCapSupported": lldpNeighborSysCapSupported,
       "lldpNeighborSysCapEnabled": lldpNeighborSysCapEnabled,
       "wlsxLldpNeighborManAddrTable": wlsxLldpNeighborManAddrTable,
       "wlsxLldpNeighborManAddrEntry": wlsxLldpNeighborManAddrEntry,
       "lldpNeighborManAddrIndex": lldpNeighborManAddrIndex,
       "lldpNeighborManAddrSubtype": lldpNeighborManAddrSubtype,
       "lldpNeighborManAddr": lldpNeighborManAddr,
       "wlsxRemoteUSBGroup": wlsxRemoteUSBGroup,
       "wlsxRemoteAccessPointUSBGroup": wlsxRemoteAccessPointUSBGroup,
       "wlsxRemoteUSBTable": wlsxRemoteUSBTable,
       "wlsxUSBEntry": wlsxUSBEntry,
       "usbDevNumber": usbDevNumber,
       "usbStatus": usbStatus,
       "usbManufacturer": usbManufacturer,
       "usbProduct": usbProduct,
       "usbSerialNumber": usbSerialNumber,
       "usbVendor": usbVendor,
       "usbProductID": usbProductID,
       "usbDriver": usbDriver,
       "usbRSSI": usbRSSI,
       "usbNetworkServiceLevel": usbNetworkServiceLevel,
       "usbFirmwareVersion": usbFirmwareVersion,
       "usbEsnNumber": usbEsnNumber,
       "usbifOperStatus": usbifOperStatus,
       "usbifInUcastPkts": usbifInUcastPkts,
       "usbifInUcastOctets": usbifInUcastOctets,
       "usbifOutUcastPkts": usbifOutUcastPkts,
       "usbifOutUcastOctets": usbifOutUcastOctets,
       "usbifInErrors": usbifInErrors,
       "usbifOutErrors": usbifOutErrors}
)
