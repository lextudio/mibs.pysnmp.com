# SNMP MIB module (PEPVPN-SPEEDFUSION) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PEPVPN-SPEEDFUSION
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:23 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pepvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pepwave_ObjectIdentity = ObjectIdentity
pepwave = _Pepwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662)
)
_ProductMib_ObjectIdentity = ObjectIdentity
productMib = _ProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200)
)
_GeneralMib_ObjectIdentity = ObjectIdentity
generalMib = _GeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1)
)
_PepvpnMib_ObjectIdentity = ObjectIdentity
pepvpnMib = _PepvpnMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10)
)
_PepVpnInfo_ObjectIdentity = ObjectIdentity
pepVpnInfo = _PepVpnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1)
)
_PepVpnStatusTable_Object = MibTable
pepVpnStatusTable = _PepVpnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pepVpnStatusTable.setStatus("current")
_PepVpnStatusEntry_Object = MibTableRow
pepVpnStatusEntry = _PepVpnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1)
)
pepVpnStatusEntry.setIndexNames(
    (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"),
    (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"),
)
if mibBuilder.loadTexts:
    pepVpnStatusEntry.setStatus("current")
_PepVpnStatusId_Type = Integer32
_PepVpnStatusId_Object = MibTableColumn
pepVpnStatusId = _PepVpnStatusId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 1),
    _PepVpnStatusId_Type()
)
pepVpnStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusId.setStatus("current")


class _PepVpnStatusProfileName_Type(OctetString):
    """Custom type pepVpnStatusProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PepVpnStatusProfileName_Type.__name__ = "OctetString"
_PepVpnStatusProfileName_Object = MibTableColumn
pepVpnStatusProfileName = _PepVpnStatusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 2),
    _PepVpnStatusProfileName_Type()
)
pepVpnStatusProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusProfileName.setStatus("current")


class _PepVpnStatusConnectionState_Type(Integer32):
    """Custom type pepVpnStatusConnectionState based on Integer32"""
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
        *(("authen", 1),
          ("connected", 4),
          ("route", 3),
          ("start", 0),
          ("tunnel", 2))
    )


_PepVpnStatusConnectionState_Type.__name__ = "Integer32"
_PepVpnStatusConnectionState_Object = MibTableColumn
pepVpnStatusConnectionState = _PepVpnStatusConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 3),
    _PepVpnStatusConnectionState_Type()
)
pepVpnStatusConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusConnectionState.setStatus("current")


class _PepVpnStatusEncryption_Type(Integer32):
    """Custom type pepVpnStatusEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes256", 2),
          ("na", 0),
          ("off", 1))
    )


_PepVpnStatusEncryption_Type.__name__ = "Integer32"
_PepVpnStatusEncryption_Object = MibTableColumn
pepVpnStatusEncryption = _PepVpnStatusEncryption_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 4),
    _PepVpnStatusEncryption_Type()
)
pepVpnStatusEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusEncryption.setStatus("current")


class _PepVpnStatusL2Bridging_Type(Integer32):
    """Custom type pepVpnStatusL2Bridging based on Integer32"""
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


_PepVpnStatusL2Bridging_Type.__name__ = "Integer32"
_PepVpnStatusL2Bridging_Object = MibTableColumn
pepVpnStatusL2Bridging = _PepVpnStatusL2Bridging_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 5),
    _PepVpnStatusL2Bridging_Type()
)
pepVpnStatusL2Bridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusL2Bridging.setStatus("current")


class _PepVpnStatusL2Vlan_Type(Integer32):
    """Custom type pepVpnStatusL2Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PepVpnStatusL2Vlan_Type.__name__ = "Integer32"
_PepVpnStatusL2Vlan_Object = MibTableColumn
pepVpnStatusL2Vlan = _PepVpnStatusL2Vlan_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 6),
    _PepVpnStatusL2Vlan_Type()
)
pepVpnStatusL2Vlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusL2Vlan.setStatus("current")
_PepVpnRemotePeerId_Type = Integer32
_PepVpnRemotePeerId_Object = MibTableColumn
pepVpnRemotePeerId = _PepVpnRemotePeerId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 7),
    _PepVpnRemotePeerId_Type()
)
pepVpnRemotePeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnRemotePeerId.setStatus("current")
_PepVpnRemotePeer_Type = OctetString
_PepVpnRemotePeer_Object = MibTableColumn
pepVpnRemotePeer = _PepVpnRemotePeer_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 8),
    _PepVpnRemotePeer_Type()
)
pepVpnRemotePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnRemotePeer.setStatus("current")
_PepVpnStatusWanTable_Object = MibTable
pepVpnStatusWanTable = _PepVpnStatusWanTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pepVpnStatusWanTable.setStatus("current")
_PepVpnStatusWanEntry_Object = MibTableRow
pepVpnStatusWanEntry = _PepVpnStatusWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1)
)
pepVpnStatusWanEntry.setIndexNames(
    (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"),
    (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"),
    (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusWanId"),
)
if mibBuilder.loadTexts:
    pepVpnStatusWanEntry.setStatus("current")
_PepVpnStatusWanId_Type = Integer32
_PepVpnStatusWanId_Object = MibTableColumn
pepVpnStatusWanId = _PepVpnStatusWanId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 1),
    _PepVpnStatusWanId_Type()
)
pepVpnStatusWanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusWanId.setStatus("current")


class _PepVpnStatusWanName_Type(OctetString):
    """Custom type pepVpnStatusWanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PepVpnStatusWanName_Type.__name__ = "OctetString"
_PepVpnStatusWanName_Object = MibTableColumn
pepVpnStatusWanName = _PepVpnStatusWanName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 2),
    _PepVpnStatusWanName_Type()
)
pepVpnStatusWanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusWanName.setStatus("current")
_PepVpnStatusWanTxBytes_Type = Counter64
_PepVpnStatusWanTxBytes_Object = MibTableColumn
pepVpnStatusWanTxBytes = _PepVpnStatusWanTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 3),
    _PepVpnStatusWanTxBytes_Type()
)
pepVpnStatusWanTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusWanTxBytes.setStatus("current")
_PepVpnStatusWanRxBytes_Type = Counter64
_PepVpnStatusWanRxBytes_Object = MibTableColumn
pepVpnStatusWanRxBytes = _PepVpnStatusWanRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 4),
    _PepVpnStatusWanRxBytes_Type()
)
pepVpnStatusWanRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusWanRxBytes.setStatus("current")
_PepVpnStatusWanDropPackets_Type = Integer32
_PepVpnStatusWanDropPackets_Object = MibTableColumn
pepVpnStatusWanDropPackets = _PepVpnStatusWanDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 5),
    _PepVpnStatusWanDropPackets_Type()
)
pepVpnStatusWanDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusWanDropPackets.setStatus("current")
_PepVpnStatusWanLatency_Type = Integer32
_PepVpnStatusWanLatency_Object = MibTableColumn
pepVpnStatusWanLatency = _PepVpnStatusWanLatency_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 6),
    _PepVpnStatusWanLatency_Type()
)
pepVpnStatusWanLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusWanLatency.setStatus("current")
_PepVpnStatusRemoteNetworkTable_Object = MibTable
pepVpnStatusRemoteNetworkTable = _PepVpnStatusRemoteNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pepVpnStatusRemoteNetworkTable.setStatus("current")
_PepVpnStatusRemoteNetworkEntry_Object = MibTableRow
pepVpnStatusRemoteNetworkEntry = _PepVpnStatusRemoteNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1)
)
pepVpnStatusRemoteNetworkEntry.setIndexNames(
    (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"),
    (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"),
    (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusRemoteNetowrkId"),
)
if mibBuilder.loadTexts:
    pepVpnStatusRemoteNetworkEntry.setStatus("current")
_PepVpnStatusRemoteNetowrkId_Type = Integer32
_PepVpnStatusRemoteNetowrkId_Object = MibTableColumn
pepVpnStatusRemoteNetowrkId = _PepVpnStatusRemoteNetowrkId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 1),
    _PepVpnStatusRemoteNetowrkId_Type()
)
pepVpnStatusRemoteNetowrkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusRemoteNetowrkId.setStatus("current")
_PepVpnStatusRemoteNetwork_Type = IpAddress
_PepVpnStatusRemoteNetwork_Object = MibTableColumn
pepVpnStatusRemoteNetwork = _PepVpnStatusRemoteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 2),
    _PepVpnStatusRemoteNetwork_Type()
)
pepVpnStatusRemoteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusRemoteNetwork.setStatus("current")
_PepVpnStatusRemoteSubnet_Type = IpAddress
_PepVpnStatusRemoteSubnet_Object = MibTableColumn
pepVpnStatusRemoteSubnet = _PepVpnStatusRemoteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 3),
    _PepVpnStatusRemoteSubnet_Type()
)
pepVpnStatusRemoteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pepVpnStatusRemoteSubnet.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEPVPN-SPEEDFUSION",
    **{"pepwave": pepwave,
       "productMib": productMib,
       "generalMib": generalMib,
       "pepvpnMib": pepvpnMib,
       "pepvpn": pepvpn,
       "pepVpnInfo": pepVpnInfo,
       "pepVpnStatusTable": pepVpnStatusTable,
       "pepVpnStatusEntry": pepVpnStatusEntry,
       "pepVpnStatusId": pepVpnStatusId,
       "pepVpnStatusProfileName": pepVpnStatusProfileName,
       "pepVpnStatusConnectionState": pepVpnStatusConnectionState,
       "pepVpnStatusEncryption": pepVpnStatusEncryption,
       "pepVpnStatusL2Bridging": pepVpnStatusL2Bridging,
       "pepVpnStatusL2Vlan": pepVpnStatusL2Vlan,
       "pepVpnRemotePeerId": pepVpnRemotePeerId,
       "pepVpnRemotePeer": pepVpnRemotePeer,
       "pepVpnStatusWanTable": pepVpnStatusWanTable,
       "pepVpnStatusWanEntry": pepVpnStatusWanEntry,
       "pepVpnStatusWanId": pepVpnStatusWanId,
       "pepVpnStatusWanName": pepVpnStatusWanName,
       "pepVpnStatusWanTxBytes": pepVpnStatusWanTxBytes,
       "pepVpnStatusWanRxBytes": pepVpnStatusWanRxBytes,
       "pepVpnStatusWanDropPackets": pepVpnStatusWanDropPackets,
       "pepVpnStatusWanLatency": pepVpnStatusWanLatency,
       "pepVpnStatusRemoteNetworkTable": pepVpnStatusRemoteNetworkTable,
       "pepVpnStatusRemoteNetworkEntry": pepVpnStatusRemoteNetworkEntry,
       "pepVpnStatusRemoteNetowrkId": pepVpnStatusRemoteNetowrkId,
       "pepVpnStatusRemoteNetwork": pepVpnStatusRemoteNetwork,
       "pepVpnStatusRemoteSubnet": pepVpnStatusRemoteSubnet}
)
