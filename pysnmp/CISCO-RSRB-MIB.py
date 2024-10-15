# SNMP MIB module (CISCO-RSRB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RSRB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:43 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoRsrbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29)
)
ciscoRsrbMIB.setRevisions(
        ("1995-08-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsrbObjects_ObjectIdentity = ObjectIdentity
rsrbObjects = _RsrbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1)
)
_RsrbVirtualRings_ObjectIdentity = ObjectIdentity
rsrbVirtualRings = _RsrbVirtualRings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1)
)
_RsrbVirtRingTable_Object = MibTable
rsrbVirtRingTable = _RsrbVirtRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsrbVirtRingTable.setStatus("current")
_RsrbVirtRingEntry_Object = MibTableRow
rsrbVirtRingEntry = _RsrbVirtRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1, 1)
)
rsrbVirtRingEntry.setIndexNames(
    (0, "CISCO-RSRB-MIB", "rsrbVirtRingIndex"),
)
if mibBuilder.loadTexts:
    rsrbVirtRingEntry.setStatus("current")


class _RsrbVirtRingIndex_Type(Integer32):
    """Custom type rsrbVirtRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsrbVirtRingIndex_Type.__name__ = "Integer32"
_RsrbVirtRingIndex_Object = MibTableColumn
rsrbVirtRingIndex = _RsrbVirtRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1, 1, 1),
    _RsrbVirtRingIndex_Type()
)
rsrbVirtRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsrbVirtRingIndex.setStatus("current")
_RsrbVirtRingIPAddr_Type = IpAddress
_RsrbVirtRingIPAddr_Object = MibTableColumn
rsrbVirtRingIPAddr = _RsrbVirtRingIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1, 1, 2),
    _RsrbVirtRingIPAddr_Type()
)
rsrbVirtRingIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbVirtRingIPAddr.setStatus("current")
_RsrbVirtRingMaxTcpQSize_Type = Integer32
_RsrbVirtRingMaxTcpQSize_Object = MibTableColumn
rsrbVirtRingMaxTcpQSize = _RsrbVirtRingMaxTcpQSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1, 1, 3),
    _RsrbVirtRingMaxTcpQSize_Type()
)
rsrbVirtRingMaxTcpQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbVirtRingMaxTcpQSize.setStatus("current")
_RsrbRemotePeers_ObjectIdentity = ObjectIdentity
rsrbRemotePeers = _RsrbRemotePeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2)
)
_RsrbRemotePeerTable_Object = MibTable
rsrbRemotePeerTable = _RsrbRemotePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rsrbRemotePeerTable.setStatus("current")
_RsrbRemotePeerEntry_Object = MibTableRow
rsrbRemotePeerEntry = _RsrbRemotePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1)
)
rsrbRemotePeerEntry.setIndexNames(
    (0, "CISCO-RSRB-MIB", "rsrbVirtRingIndex"),
    (0, "CISCO-RSRB-MIB", "rsrbRemotePeerIndex"),
)
if mibBuilder.loadTexts:
    rsrbRemotePeerEntry.setStatus("current")


class _RsrbRemotePeerIndex_Type(Integer32):
    """Custom type rsrbRemotePeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsrbRemotePeerIndex_Type.__name__ = "Integer32"
_RsrbRemotePeerIndex_Object = MibTableColumn
rsrbRemotePeerIndex = _RsrbRemotePeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 1),
    _RsrbRemotePeerIndex_Type()
)
rsrbRemotePeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsrbRemotePeerIndex.setStatus("current")


class _RsrbRemotePeerEncapsulation_Type(Integer32):
    """Custom type rsrbRemotePeerEncapsulation based on Integer32"""
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
        *(("frameRelay", 5),
          ("fst", 4),
          ("lan", 3),
          ("serial", 2),
          ("tcp", 1))
    )


_RsrbRemotePeerEncapsulation_Type.__name__ = "Integer32"
_RsrbRemotePeerEncapsulation_Object = MibTableColumn
rsrbRemotePeerEncapsulation = _RsrbRemotePeerEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 2),
    _RsrbRemotePeerEncapsulation_Type()
)
rsrbRemotePeerEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerEncapsulation.setStatus("current")
_RsrbRemotePeerIPAddr_Type = IpAddress
_RsrbRemotePeerIPAddr_Object = MibTableColumn
rsrbRemotePeerIPAddr = _RsrbRemotePeerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 3),
    _RsrbRemotePeerIPAddr_Type()
)
rsrbRemotePeerIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerIPAddr.setStatus("current")
_RsrbRemotePeerLocalIfIndex_Type = InterfaceIndex
_RsrbRemotePeerLocalIfIndex_Object = MibTableColumn
rsrbRemotePeerLocalIfIndex = _RsrbRemotePeerLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 4),
    _RsrbRemotePeerLocalIfIndex_Type()
)
rsrbRemotePeerLocalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerLocalIfIndex.setStatus("current")


class _RsrbRemotePeerState_Type(Integer32):
    """Custom type rsrbRemotePeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("connected", 9),
          ("dead", 1),
          ("draining", 8),
          ("openWaitXport", 4),
          ("opening", 3),
          ("remoteOpened", 7),
          ("remoteResponded", 6),
          ("waitRemoteRsp", 5))
    )


_RsrbRemotePeerState_Type.__name__ = "Integer32"
_RsrbRemotePeerState_Object = MibTableColumn
rsrbRemotePeerState = _RsrbRemotePeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 5),
    _RsrbRemotePeerState_Type()
)
rsrbRemotePeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerState.setStatus("current")
_RsrbRemotePeerPacketsRx_Type = Counter32
_RsrbRemotePeerPacketsRx_Object = MibTableColumn
rsrbRemotePeerPacketsRx = _RsrbRemotePeerPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 6),
    _RsrbRemotePeerPacketsRx_Type()
)
rsrbRemotePeerPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerPacketsRx.setStatus("current")
_RsrbRemotePeerPacketsTx_Type = Counter32
_RsrbRemotePeerPacketsTx_Object = MibTableColumn
rsrbRemotePeerPacketsTx = _RsrbRemotePeerPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 7),
    _RsrbRemotePeerPacketsTx_Type()
)
rsrbRemotePeerPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerPacketsTx.setStatus("current")
_RsrbRemotePeerBytesRx_Type = Counter32
_RsrbRemotePeerBytesRx_Object = MibTableColumn
rsrbRemotePeerBytesRx = _RsrbRemotePeerBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 8),
    _RsrbRemotePeerBytesRx_Type()
)
rsrbRemotePeerBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerBytesRx.setStatus("current")
_RsrbRemotePeerBytesTx_Type = Counter32
_RsrbRemotePeerBytesTx_Object = MibTableColumn
rsrbRemotePeerBytesTx = _RsrbRemotePeerBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 9),
    _RsrbRemotePeerBytesTx_Type()
)
rsrbRemotePeerBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerBytesTx.setStatus("current")
_RsrbRemotePeerExplorersRx_Type = Counter32
_RsrbRemotePeerExplorersRx_Object = MibTableColumn
rsrbRemotePeerExplorersRx = _RsrbRemotePeerExplorersRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 10),
    _RsrbRemotePeerExplorersRx_Type()
)
rsrbRemotePeerExplorersRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerExplorersRx.setStatus("current")
_RsrbRemotePeerTcpQueue_Type = Gauge32
_RsrbRemotePeerTcpQueue_Object = MibTableColumn
rsrbRemotePeerTcpQueue = _RsrbRemotePeerTcpQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 11),
    _RsrbRemotePeerTcpQueue_Type()
)
rsrbRemotePeerTcpQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerTcpQueue.setStatus("current")
_RsrbRemotePeerDrops_Type = Counter32
_RsrbRemotePeerDrops_Object = MibTableColumn
rsrbRemotePeerDrops = _RsrbRemotePeerDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 12),
    _RsrbRemotePeerDrops_Type()
)
rsrbRemotePeerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerDrops.setStatus("current")
_RsrbRemotePeerLocalAck_Type = TruthValue
_RsrbRemotePeerLocalAck_Object = MibTableColumn
rsrbRemotePeerLocalAck = _RsrbRemotePeerLocalAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 13),
    _RsrbRemotePeerLocalAck_Type()
)
rsrbRemotePeerLocalAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerLocalAck.setStatus("current")
_RsrbRemotePeerVersion_Type = Integer32
_RsrbRemotePeerVersion_Object = MibTableColumn
rsrbRemotePeerVersion = _RsrbRemotePeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 14),
    _RsrbRemotePeerVersion_Type()
)
rsrbRemotePeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRemotePeerVersion.setStatus("current")
_RsrbPhysicalRings_ObjectIdentity = ObjectIdentity
rsrbPhysicalRings = _RsrbPhysicalRings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3)
)
_RsrbRingTable_Object = MibTable
rsrbRingTable = _RsrbRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rsrbRingTable.setStatus("current")
_RsrbRingEntry_Object = MibTableRow
rsrbRingEntry = _RsrbRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1)
)
rsrbRingEntry.setIndexNames(
    (0, "CISCO-RSRB-MIB", "rsrbVirtRingIndex"),
    (0, "CISCO-RSRB-MIB", "rsrbRingIndex"),
)
if mibBuilder.loadTexts:
    rsrbRingEntry.setStatus("current")


class _RsrbRingIndex_Type(Integer32):
    """Custom type rsrbRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsrbRingIndex_Type.__name__ = "Integer32"
_RsrbRingIndex_Object = MibTableColumn
rsrbRingIndex = _RsrbRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 1),
    _RsrbRingIndex_Type()
)
rsrbRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsrbRingIndex.setStatus("current")
_RsrbRingBridge_Type = Integer32
_RsrbRingBridge_Object = MibTableColumn
rsrbRingBridge = _RsrbRingBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 2),
    _RsrbRingBridge_Type()
)
rsrbRingBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRingBridge.setStatus("current")
_RsrbRingLocal_Type = TruthValue
_RsrbRingLocal_Object = MibTableColumn
rsrbRingLocal = _RsrbRingLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 3),
    _RsrbRingLocal_Type()
)
rsrbRingLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRingLocal.setStatus("current")


class _RsrbRingType_Type(Integer32):
    """Custom type rsrbRingType based on Integer32"""
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
        *(("dynamic", 2),
          ("qllc", 4),
          ("sdllc", 3),
          ("static", 1),
          ("virtual", 5))
    )


_RsrbRingType_Type.__name__ = "Integer32"
_RsrbRingType_Object = MibTableColumn
rsrbRingType = _RsrbRingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 4),
    _RsrbRingType_Type()
)
rsrbRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRingType.setStatus("current")
_RsrbRingMacAddr_Type = MacAddress
_RsrbRingMacAddr_Object = MibTableColumn
rsrbRingMacAddr = _RsrbRingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 5),
    _RsrbRingMacAddr_Type()
)
rsrbRingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRingMacAddr.setStatus("current")
_RsrbRingLocalIfIndex_Type = InterfaceIndex
_RsrbRingLocalIfIndex_Object = MibTableColumn
rsrbRingLocalIfIndex = _RsrbRingLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 6),
    _RsrbRingLocalIfIndex_Type()
)
rsrbRingLocalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRingLocalIfIndex.setStatus("current")
_RsrbRingRemoteIpAddress_Type = IpAddress
_RsrbRingRemoteIpAddress_Object = MibTableColumn
rsrbRingRemoteIpAddress = _RsrbRingRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 7),
    _RsrbRingRemoteIpAddress_Type()
)
rsrbRingRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRingRemoteIpAddress.setStatus("current")
_RsrbRingNbrPacketsFwd_Type = Counter32
_RsrbRingNbrPacketsFwd_Object = MibTableColumn
rsrbRingNbrPacketsFwd = _RsrbRingNbrPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 8),
    _RsrbRingNbrPacketsFwd_Type()
)
rsrbRingNbrPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrbRingNbrPacketsFwd.setStatus("current")
_RsrbNotificationPrefix_ObjectIdentity = ObjectIdentity
rsrbNotificationPrefix = _RsrbNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 2)
)
_RsrbNotifications_ObjectIdentity = ObjectIdentity
rsrbNotifications = _RsrbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 2, 0)
)
_RsrbMibConformance_ObjectIdentity = ObjectIdentity
rsrbMibConformance = _RsrbMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 3)
)
_RsrbMibCompliances_ObjectIdentity = ObjectIdentity
rsrbMibCompliances = _RsrbMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 1)
)
_RsrbMibGroups_ObjectIdentity = ObjectIdentity
rsrbMibGroups = _RsrbMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 2)
)

# Managed Objects groups

rsrbVirtRingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 2, 1)
)
rsrbVirtRingGroup.setObjects(
      *(("CISCO-RSRB-MIB", "rsrbVirtRingIPAddr"),
        ("CISCO-RSRB-MIB", "rsrbVirtRingMaxTcpQSize"))
)
if mibBuilder.loadTexts:
    rsrbVirtRingGroup.setStatus("current")

rsrbRemotePeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 2, 2)
)
rsrbRemotePeerGroup.setObjects(
      *(("CISCO-RSRB-MIB", "rsrbRemotePeerEncapsulation"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerIPAddr"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerLocalIfIndex"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerState"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerPacketsRx"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerPacketsTx"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerBytesRx"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerBytesTx"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerExplorersRx"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerTcpQueue"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerDrops"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerLocalAck"),
        ("CISCO-RSRB-MIB", "rsrbRemotePeerVersion"))
)
if mibBuilder.loadTexts:
    rsrbRemotePeerGroup.setStatus("current")

rsrbRingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 2, 3)
)
rsrbRingGroup.setObjects(
      *(("CISCO-RSRB-MIB", "rsrbRingBridge"),
        ("CISCO-RSRB-MIB", "rsrbRingLocal"),
        ("CISCO-RSRB-MIB", "rsrbRingType"),
        ("CISCO-RSRB-MIB", "rsrbRingMacAddr"),
        ("CISCO-RSRB-MIB", "rsrbRingLocalIfIndex"),
        ("CISCO-RSRB-MIB", "rsrbRingRemoteIpAddress"),
        ("CISCO-RSRB-MIB", "rsrbRingNbrPacketsFwd"))
)
if mibBuilder.loadTexts:
    rsrbRingGroup.setStatus("current")


# Notification objects

rsrbPeerStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 2, 0, 1)
)
rsrbPeerStateChangeNotification.setObjects(
    ("CISCO-RSRB-MIB", "rsrbRemotePeerState")
)
if mibBuilder.loadTexts:
    rsrbPeerStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

rsrbMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rsrbMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RSRB-MIB",
    **{"ciscoRsrbMIB": ciscoRsrbMIB,
       "rsrbObjects": rsrbObjects,
       "rsrbVirtualRings": rsrbVirtualRings,
       "rsrbVirtRingTable": rsrbVirtRingTable,
       "rsrbVirtRingEntry": rsrbVirtRingEntry,
       "rsrbVirtRingIndex": rsrbVirtRingIndex,
       "rsrbVirtRingIPAddr": rsrbVirtRingIPAddr,
       "rsrbVirtRingMaxTcpQSize": rsrbVirtRingMaxTcpQSize,
       "rsrbRemotePeers": rsrbRemotePeers,
       "rsrbRemotePeerTable": rsrbRemotePeerTable,
       "rsrbRemotePeerEntry": rsrbRemotePeerEntry,
       "rsrbRemotePeerIndex": rsrbRemotePeerIndex,
       "rsrbRemotePeerEncapsulation": rsrbRemotePeerEncapsulation,
       "rsrbRemotePeerIPAddr": rsrbRemotePeerIPAddr,
       "rsrbRemotePeerLocalIfIndex": rsrbRemotePeerLocalIfIndex,
       "rsrbRemotePeerState": rsrbRemotePeerState,
       "rsrbRemotePeerPacketsRx": rsrbRemotePeerPacketsRx,
       "rsrbRemotePeerPacketsTx": rsrbRemotePeerPacketsTx,
       "rsrbRemotePeerBytesRx": rsrbRemotePeerBytesRx,
       "rsrbRemotePeerBytesTx": rsrbRemotePeerBytesTx,
       "rsrbRemotePeerExplorersRx": rsrbRemotePeerExplorersRx,
       "rsrbRemotePeerTcpQueue": rsrbRemotePeerTcpQueue,
       "rsrbRemotePeerDrops": rsrbRemotePeerDrops,
       "rsrbRemotePeerLocalAck": rsrbRemotePeerLocalAck,
       "rsrbRemotePeerVersion": rsrbRemotePeerVersion,
       "rsrbPhysicalRings": rsrbPhysicalRings,
       "rsrbRingTable": rsrbRingTable,
       "rsrbRingEntry": rsrbRingEntry,
       "rsrbRingIndex": rsrbRingIndex,
       "rsrbRingBridge": rsrbRingBridge,
       "rsrbRingLocal": rsrbRingLocal,
       "rsrbRingType": rsrbRingType,
       "rsrbRingMacAddr": rsrbRingMacAddr,
       "rsrbRingLocalIfIndex": rsrbRingLocalIfIndex,
       "rsrbRingRemoteIpAddress": rsrbRingRemoteIpAddress,
       "rsrbRingNbrPacketsFwd": rsrbRingNbrPacketsFwd,
       "rsrbNotificationPrefix": rsrbNotificationPrefix,
       "rsrbNotifications": rsrbNotifications,
       "rsrbPeerStateChangeNotification": rsrbPeerStateChangeNotification,
       "rsrbMibConformance": rsrbMibConformance,
       "rsrbMibCompliances": rsrbMibCompliances,
       "rsrbMibCompliance": rsrbMibCompliance,
       "rsrbMibGroups": rsrbMibGroups,
       "rsrbVirtRingGroup": rsrbVirtRingGroup,
       "rsrbRemotePeerGroup": rsrbRemotePeerGroup,
       "rsrbRingGroup": rsrbRingGroup}
)
