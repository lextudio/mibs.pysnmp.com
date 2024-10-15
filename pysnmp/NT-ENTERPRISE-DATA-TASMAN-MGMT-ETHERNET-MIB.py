# SNMP MIB module (NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:38 2024
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

(ntEnterpriseDataTasmanInterfaces,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanInterfaces")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nnethernetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4)
)
nnethernetMib.setRevisions(
        ("1999-07-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnethernetTable_Object = MibTable
nnethernetTable = _NnethernetTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    nnethernetTable.setStatus("current")
_NnethernetTableEntry_Object = MibTableRow
nnethernetTableEntry = _NnethernetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1)
)
nnethernetTableEntry.setIndexNames(
    (0, "NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB", "nnethernetId"),
)
if mibBuilder.loadTexts:
    nnethernetTableEntry.setStatus("current")


class _NnethernetId_Type(Integer32):
    """Custom type nnethernetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NnethernetId_Type.__name__ = "Integer32"
_NnethernetId_Object = MibTableColumn
nnethernetId = _NnethernetId_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 1),
    _NnethernetId_Type()
)
nnethernetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnethernetId.setStatus("deprecated")


class _NnethernetDescr_Type(DisplayString):
    """Custom type nnethernetDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_NnethernetDescr_Type.__name__ = "DisplayString"
_NnethernetDescr_Object = MibTableColumn
nnethernetDescr = _NnethernetDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 2),
    _NnethernetDescr_Type()
)
nnethernetDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetDescr.setStatus("current")
_NnethernetDhcpRelayServerAddr_Type = IpAddress
_NnethernetDhcpRelayServerAddr_Object = MibTableColumn
nnethernetDhcpRelayServerAddr = _NnethernetDhcpRelayServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 3),
    _NnethernetDhcpRelayServerAddr_Type()
)
nnethernetDhcpRelayServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetDhcpRelayServerAddr.setStatus("current")
_NnethernetDhcpRelayGatewayAddr_Type = IpAddress
_NnethernetDhcpRelayGatewayAddr_Object = MibTableColumn
nnethernetDhcpRelayGatewayAddr = _NnethernetDhcpRelayGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 4),
    _NnethernetDhcpRelayGatewayAddr_Type()
)
nnethernetDhcpRelayGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetDhcpRelayGatewayAddr.setStatus("current")


class _NnethernetFailOverEnable_Type(TruthValue):
    """Custom type nnethernetFailOverEnable based on TruthValue"""


_NnethernetFailOverEnable_Object = MibTableColumn
nnethernetFailOverEnable = _NnethernetFailOverEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 5),
    _NnethernetFailOverEnable_Type()
)
nnethernetFailOverEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetFailOverEnable.setStatus("current")


class _NnethernetHoldDownTime_Type(Integer32):
    """Custom type nnethernetHoldDownTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 900),
    )


_NnethernetHoldDownTime_Type.__name__ = "Integer32"
_NnethernetHoldDownTime_Object = MibTableColumn
nnethernetHoldDownTime = _NnethernetHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 6),
    _NnethernetHoldDownTime_Type()
)
nnethernetHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetHoldDownTime.setStatus("current")


class _NnethernetIcmpRedirectEnable_Type(TruthValue):
    """Custom type nnethernetIcmpRedirectEnable based on TruthValue"""


_NnethernetIcmpRedirectEnable_Object = MibTableColumn
nnethernetIcmpRedirectEnable = _NnethernetIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 7),
    _NnethernetIcmpRedirectEnable_Type()
)
nnethernetIcmpRedirectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetIcmpRedirectEnable.setStatus("current")


class _NnethernetIcmpUnreachableEnable_Type(TruthValue):
    """Custom type nnethernetIcmpUnreachableEnable based on TruthValue"""


_NnethernetIcmpUnreachableEnable_Object = MibTableColumn
nnethernetIcmpUnreachableEnable = _NnethernetIcmpUnreachableEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 8),
    _NnethernetIcmpUnreachableEnable_Type()
)
nnethernetIcmpUnreachableEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetIcmpUnreachableEnable.setStatus("current")
_NnethernetIpAddr_Type = IpAddress
_NnethernetIpAddr_Object = MibTableColumn
nnethernetIpAddr = _NnethernetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 9),
    _NnethernetIpAddr_Type()
)
nnethernetIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetIpAddr.setStatus("current")
_NnethernetSubnetMask_Type = IpAddress
_NnethernetSubnetMask_Object = MibTableColumn
nnethernetSubnetMask = _NnethernetSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 10),
    _NnethernetSubnetMask_Type()
)
nnethernetSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetSubnetMask.setStatus("current")


class _NnethernetIpDirectedBroadcastEnable_Type(TruthValue):
    """Custom type nnethernetIpDirectedBroadcastEnable based on TruthValue"""


_NnethernetIpDirectedBroadcastEnable_Object = MibTableColumn
nnethernetIpDirectedBroadcastEnable = _NnethernetIpDirectedBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 11),
    _NnethernetIpDirectedBroadcastEnable_Type()
)
nnethernetIpDirectedBroadcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetIpDirectedBroadcastEnable.setStatus("current")


class _NnethernetIpMulticast_Type(Integer32):
    """Custom type nnethernetIpMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("ospfrip2", 3),
          ("pass", 1))
    )


_NnethernetIpMulticast_Type.__name__ = "Integer32"
_NnethernetIpMulticast_Object = MibTableColumn
nnethernetIpMulticast = _NnethernetIpMulticast_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 12),
    _NnethernetIpMulticast_Type()
)
nnethernetIpMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetIpMulticast.setStatus("current")


class _NnethernetMtu_Type(Integer32):
    """Custom type nnethernetMtu based on Integer32"""
    defaultValue = 1500


_NnethernetMtu_Object = MibTableColumn
nnethernetMtu = _NnethernetMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 13),
    _NnethernetMtu_Type()
)
nnethernetMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetMtu.setStatus("current")


class _NnethernetSpeed_Type(Integer32):
    """Custom type nnethernetSpeed based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed-100MBPs", 2),
          ("speed-10MBPs", 1),
          ("speed-Auto", 3))
    )


_NnethernetSpeed_Type.__name__ = "Integer32"
_NnethernetSpeed_Object = MibTableColumn
nnethernetSpeed = _NnethernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 14),
    _NnethernetSpeed_Type()
)
nnethernetSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetSpeed.setStatus("current")


class _NnethernetMode_Type(Integer32):
    """Custom type nnethernetMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1))
    )


_NnethernetMode_Type.__name__ = "Integer32"
_NnethernetMode_Object = MibTableColumn
nnethernetMode = _NnethernetMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 15),
    _NnethernetMode_Type()
)
nnethernetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetMode.setStatus("current")


class _NnethernetShutdownEnable_Type(TruthValue):
    """Custom type nnethernetShutdownEnable based on TruthValue"""


_NnethernetShutdownEnable_Object = MibTableColumn
nnethernetShutdownEnable = _NnethernetShutdownEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 16),
    _NnethernetShutdownEnable_Type()
)
nnethernetShutdownEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetShutdownEnable.setStatus("current")


class _NnethernetVlanId_Type(Integer32):
    """Custom type nnethernetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4098),
    )


_NnethernetVlanId_Type.__name__ = "Integer32"
_NnethernetVlanId_Object = MibTableColumn
nnethernetVlanId = _NnethernetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 17),
    _NnethernetVlanId_Type()
)
nnethernetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetVlanId.setStatus("current")
_NnethernetRowStatus_Type = RowStatus
_NnethernetRowStatus_Object = MibTableColumn
nnethernetRowStatus = _NnethernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 18),
    _NnethernetRowStatus_Type()
)
nnethernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnethernetRowStatus.setStatus("current")
_NnethernetDropPackets_Type = Counter32
_NnethernetDropPackets_Object = MibTableColumn
nnethernetDropPackets = _NnethernetDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 19),
    _NnethernetDropPackets_Type()
)
nnethernetDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnethernetDropPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB",
    **{"nnethernetMib": nnethernetMib,
       "nnethernetTable": nnethernetTable,
       "nnethernetTableEntry": nnethernetTableEntry,
       "nnethernetId": nnethernetId,
       "nnethernetDescr": nnethernetDescr,
       "nnethernetDhcpRelayServerAddr": nnethernetDhcpRelayServerAddr,
       "nnethernetDhcpRelayGatewayAddr": nnethernetDhcpRelayGatewayAddr,
       "nnethernetFailOverEnable": nnethernetFailOverEnable,
       "nnethernetHoldDownTime": nnethernetHoldDownTime,
       "nnethernetIcmpRedirectEnable": nnethernetIcmpRedirectEnable,
       "nnethernetIcmpUnreachableEnable": nnethernetIcmpUnreachableEnable,
       "nnethernetIpAddr": nnethernetIpAddr,
       "nnethernetSubnetMask": nnethernetSubnetMask,
       "nnethernetIpDirectedBroadcastEnable": nnethernetIpDirectedBroadcastEnable,
       "nnethernetIpMulticast": nnethernetIpMulticast,
       "nnethernetMtu": nnethernetMtu,
       "nnethernetSpeed": nnethernetSpeed,
       "nnethernetMode": nnethernetMode,
       "nnethernetShutdownEnable": nnethernetShutdownEnable,
       "nnethernetVlanId": nnethernetVlanId,
       "nnethernetRowStatus": nnethernetRowStatus,
       "nnethernetDropPackets": nnethernetDropPackets}
)
