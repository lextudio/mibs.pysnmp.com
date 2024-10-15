# SNMP MIB module (HH3C-VXLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VXLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:22 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hh3cVxlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150)
)
hh3cVxlan.setRevisions(
        ("2013-11-21 09:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVxlanObjects_ObjectIdentity = ObjectIdentity
hh3cVxlanObjects = _Hh3cVxlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1)
)
_Hh3cVxlanScalarGroup_ObjectIdentity = ObjectIdentity
hh3cVxlanScalarGroup = _Hh3cVxlanScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 1)
)


class _Hh3cVxlanLocalMacNotify_Type(TruthValue):
    """Custom type hh3cVxlanLocalMacNotify based on TruthValue"""


_Hh3cVxlanLocalMacNotify_Object = MibScalar
hh3cVxlanLocalMacNotify = _Hh3cVxlanLocalMacNotify_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 1, 1),
    _Hh3cVxlanLocalMacNotify_Type()
)
hh3cVxlanLocalMacNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVxlanLocalMacNotify.setStatus("current")


class _Hh3cVxlanRemoteMacLearn_Type(TruthValue):
    """Custom type hh3cVxlanRemoteMacLearn based on TruthValue"""


_Hh3cVxlanRemoteMacLearn_Object = MibScalar
hh3cVxlanRemoteMacLearn = _Hh3cVxlanRemoteMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 1, 2),
    _Hh3cVxlanRemoteMacLearn_Type()
)
hh3cVxlanRemoteMacLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVxlanRemoteMacLearn.setStatus("current")
_Hh3cVxlanNextVxlanID_Type = Unsigned32
_Hh3cVxlanNextVxlanID_Object = MibScalar
hh3cVxlanNextVxlanID = _Hh3cVxlanNextVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 1, 3),
    _Hh3cVxlanNextVxlanID_Type()
)
hh3cVxlanNextVxlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVxlanNextVxlanID.setStatus("current")
_Hh3cVxlanConfigured_Type = Unsigned32
_Hh3cVxlanConfigured_Object = MibScalar
hh3cVxlanConfigured = _Hh3cVxlanConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 1, 4),
    _Hh3cVxlanConfigured_Type()
)
hh3cVxlanConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVxlanConfigured.setStatus("current")
_Hh3cVxlanTable_Object = MibTable
hh3cVxlanTable = _Hh3cVxlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVxlanTable.setStatus("current")
_Hh3cVxlanEntry_Object = MibTableRow
hh3cVxlanEntry = _Hh3cVxlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2, 1)
)
hh3cVxlanEntry.setIndexNames(
    (0, "HH3C-VXLAN-MIB", "hh3cVxlanID"),
)
if mibBuilder.loadTexts:
    hh3cVxlanEntry.setStatus("current")
_Hh3cVxlanID_Type = Unsigned32
_Hh3cVxlanID_Object = MibTableColumn
hh3cVxlanID = _Hh3cVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2, 1, 1),
    _Hh3cVxlanID_Type()
)
hh3cVxlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVxlanID.setStatus("current")
_Hh3cVxlanAddrType_Type = InetAddressType
_Hh3cVxlanAddrType_Object = MibTableColumn
hh3cVxlanAddrType = _Hh3cVxlanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2, 1, 2),
    _Hh3cVxlanAddrType_Type()
)
hh3cVxlanAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVxlanAddrType.setStatus("current")
_Hh3cVxlanGroupAddr_Type = InetAddress
_Hh3cVxlanGroupAddr_Object = MibTableColumn
hh3cVxlanGroupAddr = _Hh3cVxlanGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2, 1, 3),
    _Hh3cVxlanGroupAddr_Type()
)
hh3cVxlanGroupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVxlanGroupAddr.setStatus("current")
_Hh3cVxlanSourceAddr_Type = InetAddress
_Hh3cVxlanSourceAddr_Object = MibTableColumn
hh3cVxlanSourceAddr = _Hh3cVxlanSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2, 1, 4),
    _Hh3cVxlanSourceAddr_Type()
)
hh3cVxlanSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVxlanSourceAddr.setStatus("current")
_Hh3cVxlanVsiIndex_Type = Unsigned32
_Hh3cVxlanVsiIndex_Object = MibTableColumn
hh3cVxlanVsiIndex = _Hh3cVxlanVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2, 1, 5),
    _Hh3cVxlanVsiIndex_Type()
)
hh3cVxlanVsiIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVxlanVsiIndex.setStatus("current")
_Hh3cVxlanRemoteMacCount_Type = Unsigned32
_Hh3cVxlanRemoteMacCount_Object = MibTableColumn
hh3cVxlanRemoteMacCount = _Hh3cVxlanRemoteMacCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2, 1, 6),
    _Hh3cVxlanRemoteMacCount_Type()
)
hh3cVxlanRemoteMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVxlanRemoteMacCount.setStatus("current")
_Hh3cVxlanRowStatus_Type = RowStatus
_Hh3cVxlanRowStatus_Object = MibTableColumn
hh3cVxlanRowStatus = _Hh3cVxlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 2, 1, 7),
    _Hh3cVxlanRowStatus_Type()
)
hh3cVxlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVxlanRowStatus.setStatus("current")
_Hh3cVxlanTunnelTable_Object = MibTable
hh3cVxlanTunnelTable = _Hh3cVxlanTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cVxlanTunnelTable.setStatus("current")
_Hh3cVxlanTunnelEntry_Object = MibTableRow
hh3cVxlanTunnelEntry = _Hh3cVxlanTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 3, 1)
)
hh3cVxlanTunnelEntry.setIndexNames(
    (0, "HH3C-VXLAN-MIB", "hh3cVxlanID"),
    (0, "HH3C-VXLAN-MIB", "hh3cVxlanTunnelID"),
)
if mibBuilder.loadTexts:
    hh3cVxlanTunnelEntry.setStatus("current")
_Hh3cVxlanTunnelID_Type = Unsigned32
_Hh3cVxlanTunnelID_Object = MibTableColumn
hh3cVxlanTunnelID = _Hh3cVxlanTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 3, 1, 1),
    _Hh3cVxlanTunnelID_Type()
)
hh3cVxlanTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVxlanTunnelID.setStatus("current")
_Hh3cVxlanTunnelRowStatus_Type = RowStatus
_Hh3cVxlanTunnelRowStatus_Object = MibTableColumn
hh3cVxlanTunnelRowStatus = _Hh3cVxlanTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 3, 1, 2),
    _Hh3cVxlanTunnelRowStatus_Type()
)
hh3cVxlanTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVxlanTunnelRowStatus.setStatus("current")
_Hh3cVxlanTunnelOctets_Type = Counter64
_Hh3cVxlanTunnelOctets_Object = MibTableColumn
hh3cVxlanTunnelOctets = _Hh3cVxlanTunnelOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 3, 1, 3),
    _Hh3cVxlanTunnelOctets_Type()
)
hh3cVxlanTunnelOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVxlanTunnelOctets.setStatus("current")
_Hh3cVxlanTunnelPackets_Type = Counter64
_Hh3cVxlanTunnelPackets_Object = MibTableColumn
hh3cVxlanTunnelPackets = _Hh3cVxlanTunnelPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 3, 1, 4),
    _Hh3cVxlanTunnelPackets_Type()
)
hh3cVxlanTunnelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVxlanTunnelPackets.setStatus("current")
_Hh3cVxlanTunnelBoundTable_Object = MibTable
hh3cVxlanTunnelBoundTable = _Hh3cVxlanTunnelBoundTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cVxlanTunnelBoundTable.setStatus("current")
_Hh3cVxlanTunnelBoundEntry_Object = MibTableRow
hh3cVxlanTunnelBoundEntry = _Hh3cVxlanTunnelBoundEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 4, 1)
)
hh3cVxlanTunnelBoundEntry.setIndexNames(
    (0, "HH3C-VXLAN-MIB", "hh3cVxlanTunnelID"),
)
if mibBuilder.loadTexts:
    hh3cVxlanTunnelBoundEntry.setStatus("current")
_Hh3cVxlanTunnelBoundVxlanNum_Type = Unsigned32
_Hh3cVxlanTunnelBoundVxlanNum_Object = MibTableColumn
hh3cVxlanTunnelBoundVxlanNum = _Hh3cVxlanTunnelBoundVxlanNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 4, 1, 1),
    _Hh3cVxlanTunnelBoundVxlanNum_Type()
)
hh3cVxlanTunnelBoundVxlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVxlanTunnelBoundVxlanNum.setStatus("current")
_Hh3cVxlanMacTable_Object = MibTable
hh3cVxlanMacTable = _Hh3cVxlanMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cVxlanMacTable.setStatus("current")
_Hh3cVxlanMacEntry_Object = MibTableRow
hh3cVxlanMacEntry = _Hh3cVxlanMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 5, 1)
)
hh3cVxlanMacEntry.setIndexNames(
    (0, "HH3C-VXLAN-MIB", "hh3cVxlanVsiIndex"),
    (0, "HH3C-VXLAN-MIB", "hh3cVxlanMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cVxlanMacEntry.setStatus("current")
_Hh3cVxlanMacAddr_Type = MacAddress
_Hh3cVxlanMacAddr_Object = MibTableColumn
hh3cVxlanMacAddr = _Hh3cVxlanMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 5, 1, 1),
    _Hh3cVxlanMacAddr_Type()
)
hh3cVxlanMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVxlanMacAddr.setStatus("current")
_Hh3cVxlanMacTunnelID_Type = Unsigned32
_Hh3cVxlanMacTunnelID_Object = MibTableColumn
hh3cVxlanMacTunnelID = _Hh3cVxlanMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 5, 1, 2),
    _Hh3cVxlanMacTunnelID_Type()
)
hh3cVxlanMacTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVxlanMacTunnelID.setStatus("current")


class _Hh3cVxlanMacType_Type(Integer32):
    """Custom type hh3cVxlanMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protocolLearned", 3),
          ("selfLearned", 1),
          ("staticConfigured", 2))
    )


_Hh3cVxlanMacType_Type.__name__ = "Integer32"
_Hh3cVxlanMacType_Object = MibTableColumn
hh3cVxlanMacType = _Hh3cVxlanMacType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 5, 1, 3),
    _Hh3cVxlanMacType_Type()
)
hh3cVxlanMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVxlanMacType.setStatus("current")
_Hh3cVxlanStaticMacTable_Object = MibTable
hh3cVxlanStaticMacTable = _Hh3cVxlanStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cVxlanStaticMacTable.setStatus("current")
_Hh3cVxlanStaticMacEntry_Object = MibTableRow
hh3cVxlanStaticMacEntry = _Hh3cVxlanStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 6, 1)
)
hh3cVxlanStaticMacEntry.setIndexNames(
    (0, "HH3C-VXLAN-MIB", "hh3cVxlanVsiIndex"),
    (0, "HH3C-VXLAN-MIB", "hh3cVxlanStaticMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cVxlanStaticMacEntry.setStatus("current")
_Hh3cVxlanStaticMacAddr_Type = MacAddress
_Hh3cVxlanStaticMacAddr_Object = MibTableColumn
hh3cVxlanStaticMacAddr = _Hh3cVxlanStaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 6, 1, 1),
    _Hh3cVxlanStaticMacAddr_Type()
)
hh3cVxlanStaticMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVxlanStaticMacAddr.setStatus("current")
_Hh3cVxlanStaticMacTunnelID_Type = Unsigned32
_Hh3cVxlanStaticMacTunnelID_Object = MibTableColumn
hh3cVxlanStaticMacTunnelID = _Hh3cVxlanStaticMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 6, 1, 2),
    _Hh3cVxlanStaticMacTunnelID_Type()
)
hh3cVxlanStaticMacTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVxlanStaticMacTunnelID.setStatus("current")
_Hh3cVxlanStaticMacRowStatus_Type = RowStatus
_Hh3cVxlanStaticMacRowStatus_Object = MibTableColumn
hh3cVxlanStaticMacRowStatus = _Hh3cVxlanStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150, 1, 6, 1, 3),
    _Hh3cVxlanStaticMacRowStatus_Type()
)
hh3cVxlanStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVxlanStaticMacRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VXLAN-MIB",
    **{"hh3cVxlan": hh3cVxlan,
       "hh3cVxlanObjects": hh3cVxlanObjects,
       "hh3cVxlanScalarGroup": hh3cVxlanScalarGroup,
       "hh3cVxlanLocalMacNotify": hh3cVxlanLocalMacNotify,
       "hh3cVxlanRemoteMacLearn": hh3cVxlanRemoteMacLearn,
       "hh3cVxlanNextVxlanID": hh3cVxlanNextVxlanID,
       "hh3cVxlanConfigured": hh3cVxlanConfigured,
       "hh3cVxlanTable": hh3cVxlanTable,
       "hh3cVxlanEntry": hh3cVxlanEntry,
       "hh3cVxlanID": hh3cVxlanID,
       "hh3cVxlanAddrType": hh3cVxlanAddrType,
       "hh3cVxlanGroupAddr": hh3cVxlanGroupAddr,
       "hh3cVxlanSourceAddr": hh3cVxlanSourceAddr,
       "hh3cVxlanVsiIndex": hh3cVxlanVsiIndex,
       "hh3cVxlanRemoteMacCount": hh3cVxlanRemoteMacCount,
       "hh3cVxlanRowStatus": hh3cVxlanRowStatus,
       "hh3cVxlanTunnelTable": hh3cVxlanTunnelTable,
       "hh3cVxlanTunnelEntry": hh3cVxlanTunnelEntry,
       "hh3cVxlanTunnelID": hh3cVxlanTunnelID,
       "hh3cVxlanTunnelRowStatus": hh3cVxlanTunnelRowStatus,
       "hh3cVxlanTunnelOctets": hh3cVxlanTunnelOctets,
       "hh3cVxlanTunnelPackets": hh3cVxlanTunnelPackets,
       "hh3cVxlanTunnelBoundTable": hh3cVxlanTunnelBoundTable,
       "hh3cVxlanTunnelBoundEntry": hh3cVxlanTunnelBoundEntry,
       "hh3cVxlanTunnelBoundVxlanNum": hh3cVxlanTunnelBoundVxlanNum,
       "hh3cVxlanMacTable": hh3cVxlanMacTable,
       "hh3cVxlanMacEntry": hh3cVxlanMacEntry,
       "hh3cVxlanMacAddr": hh3cVxlanMacAddr,
       "hh3cVxlanMacTunnelID": hh3cVxlanMacTunnelID,
       "hh3cVxlanMacType": hh3cVxlanMacType,
       "hh3cVxlanStaticMacTable": hh3cVxlanStaticMacTable,
       "hh3cVxlanStaticMacEntry": hh3cVxlanStaticMacEntry,
       "hh3cVxlanStaticMacAddr": hh3cVxlanStaticMacAddr,
       "hh3cVxlanStaticMacTunnelID": hh3cVxlanStaticMacTunnelID,
       "hh3cVxlanStaticMacRowStatus": hh3cVxlanStaticMacRowStatus}
)
