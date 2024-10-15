# SNMP MIB module (ZYXEL-VLAN-COUNTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-VLAN-COUNTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:01 2024
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelVlanCounter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelVlanCounterSetup_ObjectIdentity = ObjectIdentity
zyxelVlanCounterSetup = _ZyxelVlanCounterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1)
)
_ZyxelVlanCounterTable_Object = MibTable
zyxelVlanCounterTable = _ZyxelVlanCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelVlanCounterTable.setStatus("current")
_ZyxelVlanCounterEntry_Object = MibTableRow
zyxelVlanCounterEntry = _ZyxelVlanCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1)
)
zyxelVlanCounterEntry.setIndexNames(
    (0, "ZYXEL-VLAN-COUNTER-MIB", "zyVlanCounterVid"),
)
if mibBuilder.loadTexts:
    zyxelVlanCounterEntry.setStatus("current")
_ZyVlanCounterVid_Type = Integer32
_ZyVlanCounterVid_Object = MibTableColumn
zyVlanCounterVid = _ZyVlanCounterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1, 1),
    _ZyVlanCounterVid_Type()
)
zyVlanCounterVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVlanCounterVid.setStatus("current")
_ZyVlanCounterTimeout_Type = Unsigned32
_ZyVlanCounterTimeout_Object = MibTableColumn
zyVlanCounterTimeout = _ZyVlanCounterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1, 2),
    _ZyVlanCounterTimeout_Type()
)
zyVlanCounterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanCounterTimeout.setStatus("current")
_ZyVlanCounterPorts_Type = PortList
_ZyVlanCounterPorts_Object = MibTableColumn
zyVlanCounterPorts = _ZyVlanCounterPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1, 3),
    _ZyVlanCounterPorts_Type()
)
zyVlanCounterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanCounterPorts.setStatus("current")
_ZyVlanCounterRowStatus_Type = RowStatus
_ZyVlanCounterRowStatus_Object = MibTableColumn
zyVlanCounterRowStatus = _ZyVlanCounterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1, 4),
    _ZyVlanCounterRowStatus_Type()
)
zyVlanCounterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyVlanCounterRowStatus.setStatus("current")
_ZyxelVlanCounterStatus_ObjectIdentity = ObjectIdentity
zyxelVlanCounterStatus = _ZyxelVlanCounterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2)
)
_ZyxelVlanCounterInfoTable_Object = MibTable
zyxelVlanCounterInfoTable = _ZyxelVlanCounterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelVlanCounterInfoTable.setStatus("current")
_ZyxelVlanCounterInfoEntry_Object = MibTableRow
zyxelVlanCounterInfoEntry = _ZyxelVlanCounterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1)
)
zyxelVlanCounterInfoEntry.setIndexNames(
    (0, "ZYXEL-VLAN-COUNTER-MIB", "zyVlanCounterInfoVid"),
)
if mibBuilder.loadTexts:
    zyxelVlanCounterInfoEntry.setStatus("current")
_ZyVlanCounterInfoVid_Type = Integer32
_ZyVlanCounterInfoVid_Object = MibTableColumn
zyVlanCounterInfoVid = _ZyVlanCounterInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 1),
    _ZyVlanCounterInfoVid_Type()
)
zyVlanCounterInfoVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVlanCounterInfoVid.setStatus("current")
_ZyVlanCounterInfoHCOctets_Type = Counter64
_ZyVlanCounterInfoHCOctets_Object = MibTableColumn
zyVlanCounterInfoHCOctets = _ZyVlanCounterInfoHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 2),
    _ZyVlanCounterInfoHCOctets_Type()
)
zyVlanCounterInfoHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCOctets.setUnits("Octets")
_ZyVlanCounterInfoHCPackets_Type = Counter64
_ZyVlanCounterInfoHCPackets_Object = MibTableColumn
zyVlanCounterInfoHCPackets = _ZyVlanCounterInfoHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 3),
    _ZyVlanCounterInfoHCPackets_Type()
)
zyVlanCounterInfoHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCPackets.setStatus("current")
_ZyVlanCounterInfoHCMulticastPackets_Type = Counter64
_ZyVlanCounterInfoHCMulticastPackets_Object = MibTableColumn
zyVlanCounterInfoHCMulticastPackets = _ZyVlanCounterInfoHCMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 4),
    _ZyVlanCounterInfoHCMulticastPackets_Type()
)
zyVlanCounterInfoHCMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCMulticastPackets.setStatus("current")
_ZyVlanCounterInfoHCBroadcastPackets_Type = Counter64
_ZyVlanCounterInfoHCBroadcastPackets_Object = MibTableColumn
zyVlanCounterInfoHCBroadcastPackets = _ZyVlanCounterInfoHCBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 5),
    _ZyVlanCounterInfoHCBroadcastPackets_Type()
)
zyVlanCounterInfoHCBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCBroadcastPackets.setStatus("current")
_ZyVlanCounterInfoHCTaggedPackets_Type = Counter64
_ZyVlanCounterInfoHCTaggedPackets_Object = MibTableColumn
zyVlanCounterInfoHCTaggedPackets = _ZyVlanCounterInfoHCTaggedPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 6),
    _ZyVlanCounterInfoHCTaggedPackets_Type()
)
zyVlanCounterInfoHCTaggedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCTaggedPackets.setStatus("current")
_ZyVlanCounterInfoHCPackets64Octets_Type = Counter64
_ZyVlanCounterInfoHCPackets64Octets_Object = MibTableColumn
zyVlanCounterInfoHCPackets64Octets = _ZyVlanCounterInfoHCPackets64Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 7),
    _ZyVlanCounterInfoHCPackets64Octets_Type()
)
zyVlanCounterInfoHCPackets64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCPackets64Octets.setStatus("current")
_ZyVlanCounterInfoHCPackets65to127Octets_Type = Counter64
_ZyVlanCounterInfoHCPackets65to127Octets_Object = MibTableColumn
zyVlanCounterInfoHCPackets65to127Octets = _ZyVlanCounterInfoHCPackets65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 8),
    _ZyVlanCounterInfoHCPackets65to127Octets_Type()
)
zyVlanCounterInfoHCPackets65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCPackets65to127Octets.setStatus("current")
_ZyVlanCounterInfoHCPackets128to255Octets_Type = Counter64
_ZyVlanCounterInfoHCPackets128to255Octets_Object = MibTableColumn
zyVlanCounterInfoHCPackets128to255Octets = _ZyVlanCounterInfoHCPackets128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 9),
    _ZyVlanCounterInfoHCPackets128to255Octets_Type()
)
zyVlanCounterInfoHCPackets128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCPackets128to255Octets.setStatus("current")
_ZyVlanCounterInfoHCPackets256to511Octets_Type = Counter64
_ZyVlanCounterInfoHCPackets256to511Octets_Object = MibTableColumn
zyVlanCounterInfoHCPackets256to511Octets = _ZyVlanCounterInfoHCPackets256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 10),
    _ZyVlanCounterInfoHCPackets256to511Octets_Type()
)
zyVlanCounterInfoHCPackets256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCPackets256to511Octets.setStatus("current")
_ZyVlanCounterInfoHCPackets512to1023Octets_Type = Counter64
_ZyVlanCounterInfoHCPackets512to1023Octets_Object = MibTableColumn
zyVlanCounterInfoHCPackets512to1023Octets = _ZyVlanCounterInfoHCPackets512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 11),
    _ZyVlanCounterInfoHCPackets512to1023Octets_Type()
)
zyVlanCounterInfoHCPackets512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCPackets512to1023Octets.setStatus("current")
_ZyVlanCounterInfoHCPackets1024to1518Octets_Type = Counter64
_ZyVlanCounterInfoHCPackets1024to1518Octets_Object = MibTableColumn
zyVlanCounterInfoHCPackets1024to1518Octets = _ZyVlanCounterInfoHCPackets1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 12),
    _ZyVlanCounterInfoHCPackets1024to1518Octets_Type()
)
zyVlanCounterInfoHCPackets1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCPackets1024to1518Octets.setStatus("current")
_ZyVlanCounterInfoHCOversizePackets_Type = Counter64
_ZyVlanCounterInfoHCOversizePackets_Object = MibTableColumn
zyVlanCounterInfoHCOversizePackets = _ZyVlanCounterInfoHCOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 13),
    _ZyVlanCounterInfoHCOversizePackets_Type()
)
zyVlanCounterInfoHCOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanCounterInfoHCOversizePackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VLAN-COUNTER-MIB",
    **{"zyxelVlanCounter": zyxelVlanCounter,
       "zyxelVlanCounterSetup": zyxelVlanCounterSetup,
       "zyxelVlanCounterTable": zyxelVlanCounterTable,
       "zyxelVlanCounterEntry": zyxelVlanCounterEntry,
       "zyVlanCounterVid": zyVlanCounterVid,
       "zyVlanCounterTimeout": zyVlanCounterTimeout,
       "zyVlanCounterPorts": zyVlanCounterPorts,
       "zyVlanCounterRowStatus": zyVlanCounterRowStatus,
       "zyxelVlanCounterStatus": zyxelVlanCounterStatus,
       "zyxelVlanCounterInfoTable": zyxelVlanCounterInfoTable,
       "zyxelVlanCounterInfoEntry": zyxelVlanCounterInfoEntry,
       "zyVlanCounterInfoVid": zyVlanCounterInfoVid,
       "zyVlanCounterInfoHCOctets": zyVlanCounterInfoHCOctets,
       "zyVlanCounterInfoHCPackets": zyVlanCounterInfoHCPackets,
       "zyVlanCounterInfoHCMulticastPackets": zyVlanCounterInfoHCMulticastPackets,
       "zyVlanCounterInfoHCBroadcastPackets": zyVlanCounterInfoHCBroadcastPackets,
       "zyVlanCounterInfoHCTaggedPackets": zyVlanCounterInfoHCTaggedPackets,
       "zyVlanCounterInfoHCPackets64Octets": zyVlanCounterInfoHCPackets64Octets,
       "zyVlanCounterInfoHCPackets65to127Octets": zyVlanCounterInfoHCPackets65to127Octets,
       "zyVlanCounterInfoHCPackets128to255Octets": zyVlanCounterInfoHCPackets128to255Octets,
       "zyVlanCounterInfoHCPackets256to511Octets": zyVlanCounterInfoHCPackets256to511Octets,
       "zyVlanCounterInfoHCPackets512to1023Octets": zyVlanCounterInfoHCPackets512to1023Octets,
       "zyVlanCounterInfoHCPackets1024to1518Octets": zyVlanCounterInfoHCPackets1024to1518Octets,
       "zyVlanCounterInfoHCOversizePackets": zyVlanCounterInfoHCOversizePackets}
)
