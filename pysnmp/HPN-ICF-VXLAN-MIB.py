# SNMP MIB module (HPN-ICF-VXLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VXLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:15 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfVxlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150)
)
hpnicfVxlan.setRevisions(
        ("2013-11-21 09:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfVxlanObjects_ObjectIdentity = ObjectIdentity
hpnicfVxlanObjects = _HpnicfVxlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1)
)
_HpnicfVxlanScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfVxlanScalarGroup = _HpnicfVxlanScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1)
)


class _HpnicfVxlanLocalMacNotify_Type(TruthValue):
    """Custom type hpnicfVxlanLocalMacNotify based on TruthValue"""


_HpnicfVxlanLocalMacNotify_Object = MibScalar
hpnicfVxlanLocalMacNotify = _HpnicfVxlanLocalMacNotify_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1, 1),
    _HpnicfVxlanLocalMacNotify_Type()
)
hpnicfVxlanLocalMacNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVxlanLocalMacNotify.setStatus("current")


class _HpnicfVxlanRemoteMacLearn_Type(TruthValue):
    """Custom type hpnicfVxlanRemoteMacLearn based on TruthValue"""


_HpnicfVxlanRemoteMacLearn_Object = MibScalar
hpnicfVxlanRemoteMacLearn = _HpnicfVxlanRemoteMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1, 2),
    _HpnicfVxlanRemoteMacLearn_Type()
)
hpnicfVxlanRemoteMacLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVxlanRemoteMacLearn.setStatus("current")
_HpnicfVxlanNextVxlanID_Type = Unsigned32
_HpnicfVxlanNextVxlanID_Object = MibScalar
hpnicfVxlanNextVxlanID = _HpnicfVxlanNextVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1, 3),
    _HpnicfVxlanNextVxlanID_Type()
)
hpnicfVxlanNextVxlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVxlanNextVxlanID.setStatus("current")
_HpnicfVxlanConfigured_Type = Unsigned32
_HpnicfVxlanConfigured_Object = MibScalar
hpnicfVxlanConfigured = _HpnicfVxlanConfigured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1, 4),
    _HpnicfVxlanConfigured_Type()
)
hpnicfVxlanConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVxlanConfigured.setStatus("current")
_HpnicfVxlanTable_Object = MibTable
hpnicfVxlanTable = _HpnicfVxlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfVxlanTable.setStatus("current")
_HpnicfVxlanEntry_Object = MibTableRow
hpnicfVxlanEntry = _HpnicfVxlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1)
)
hpnicfVxlanEntry.setIndexNames(
    (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanID"),
)
if mibBuilder.loadTexts:
    hpnicfVxlanEntry.setStatus("current")
_HpnicfVxlanID_Type = Unsigned32
_HpnicfVxlanID_Object = MibTableColumn
hpnicfVxlanID = _HpnicfVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 1),
    _HpnicfVxlanID_Type()
)
hpnicfVxlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVxlanID.setStatus("current")
_HpnicfVxlanAddrType_Type = InetAddressType
_HpnicfVxlanAddrType_Object = MibTableColumn
hpnicfVxlanAddrType = _HpnicfVxlanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 2),
    _HpnicfVxlanAddrType_Type()
)
hpnicfVxlanAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVxlanAddrType.setStatus("current")
_HpnicfVxlanGroupAddr_Type = InetAddress
_HpnicfVxlanGroupAddr_Object = MibTableColumn
hpnicfVxlanGroupAddr = _HpnicfVxlanGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 3),
    _HpnicfVxlanGroupAddr_Type()
)
hpnicfVxlanGroupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVxlanGroupAddr.setStatus("current")
_HpnicfVxlanSourceAddr_Type = InetAddress
_HpnicfVxlanSourceAddr_Object = MibTableColumn
hpnicfVxlanSourceAddr = _HpnicfVxlanSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 4),
    _HpnicfVxlanSourceAddr_Type()
)
hpnicfVxlanSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVxlanSourceAddr.setStatus("current")
_HpnicfVxlanVsiIndex_Type = Unsigned32
_HpnicfVxlanVsiIndex_Object = MibTableColumn
hpnicfVxlanVsiIndex = _HpnicfVxlanVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 5),
    _HpnicfVxlanVsiIndex_Type()
)
hpnicfVxlanVsiIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVxlanVsiIndex.setStatus("current")
_HpnicfVxlanRemoteMacCount_Type = Unsigned32
_HpnicfVxlanRemoteMacCount_Object = MibTableColumn
hpnicfVxlanRemoteMacCount = _HpnicfVxlanRemoteMacCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 6),
    _HpnicfVxlanRemoteMacCount_Type()
)
hpnicfVxlanRemoteMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVxlanRemoteMacCount.setStatus("current")
_HpnicfVxlanRowStatus_Type = RowStatus
_HpnicfVxlanRowStatus_Object = MibTableColumn
hpnicfVxlanRowStatus = _HpnicfVxlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 7),
    _HpnicfVxlanRowStatus_Type()
)
hpnicfVxlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVxlanRowStatus.setStatus("current")
_HpnicfVxlanTunnelTable_Object = MibTable
hpnicfVxlanTunnelTable = _HpnicfVxlanTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelTable.setStatus("current")
_HpnicfVxlanTunnelEntry_Object = MibTableRow
hpnicfVxlanTunnelEntry = _HpnicfVxlanTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1)
)
hpnicfVxlanTunnelEntry.setIndexNames(
    (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanID"),
    (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanTunnelID"),
)
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelEntry.setStatus("current")
_HpnicfVxlanTunnelID_Type = Unsigned32
_HpnicfVxlanTunnelID_Object = MibTableColumn
hpnicfVxlanTunnelID = _HpnicfVxlanTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1, 1),
    _HpnicfVxlanTunnelID_Type()
)
hpnicfVxlanTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelID.setStatus("current")
_HpnicfVxlanTunnelRowStatus_Type = RowStatus
_HpnicfVxlanTunnelRowStatus_Object = MibTableColumn
hpnicfVxlanTunnelRowStatus = _HpnicfVxlanTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1, 2),
    _HpnicfVxlanTunnelRowStatus_Type()
)
hpnicfVxlanTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelRowStatus.setStatus("current")
_HpnicfVxlanTunnelOctets_Type = Counter64
_HpnicfVxlanTunnelOctets_Object = MibTableColumn
hpnicfVxlanTunnelOctets = _HpnicfVxlanTunnelOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1, 3),
    _HpnicfVxlanTunnelOctets_Type()
)
hpnicfVxlanTunnelOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelOctets.setStatus("current")
_HpnicfVxlanTunnelPackets_Type = Counter64
_HpnicfVxlanTunnelPackets_Object = MibTableColumn
hpnicfVxlanTunnelPackets = _HpnicfVxlanTunnelPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1, 4),
    _HpnicfVxlanTunnelPackets_Type()
)
hpnicfVxlanTunnelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelPackets.setStatus("current")
_HpnicfVxlanTunnelBoundTable_Object = MibTable
hpnicfVxlanTunnelBoundTable = _HpnicfVxlanTunnelBoundTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelBoundTable.setStatus("current")
_HpnicfVxlanTunnelBoundEntry_Object = MibTableRow
hpnicfVxlanTunnelBoundEntry = _HpnicfVxlanTunnelBoundEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 4, 1)
)
hpnicfVxlanTunnelBoundEntry.setIndexNames(
    (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanTunnelID"),
)
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelBoundEntry.setStatus("current")
_HpnicfVxlanTunnelBoundVxlanNum_Type = Unsigned32
_HpnicfVxlanTunnelBoundVxlanNum_Object = MibTableColumn
hpnicfVxlanTunnelBoundVxlanNum = _HpnicfVxlanTunnelBoundVxlanNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 4, 1, 1),
    _HpnicfVxlanTunnelBoundVxlanNum_Type()
)
hpnicfVxlanTunnelBoundVxlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVxlanTunnelBoundVxlanNum.setStatus("current")
_HpnicfVxlanMacTable_Object = MibTable
hpnicfVxlanMacTable = _HpnicfVxlanMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfVxlanMacTable.setStatus("current")
_HpnicfVxlanMacEntry_Object = MibTableRow
hpnicfVxlanMacEntry = _HpnicfVxlanMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5, 1)
)
hpnicfVxlanMacEntry.setIndexNames(
    (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanVsiIndex"),
    (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfVxlanMacEntry.setStatus("current")
_HpnicfVxlanMacAddr_Type = MacAddress
_HpnicfVxlanMacAddr_Object = MibTableColumn
hpnicfVxlanMacAddr = _HpnicfVxlanMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5, 1, 1),
    _HpnicfVxlanMacAddr_Type()
)
hpnicfVxlanMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVxlanMacAddr.setStatus("current")
_HpnicfVxlanMacTunnelID_Type = Unsigned32
_HpnicfVxlanMacTunnelID_Object = MibTableColumn
hpnicfVxlanMacTunnelID = _HpnicfVxlanMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5, 1, 2),
    _HpnicfVxlanMacTunnelID_Type()
)
hpnicfVxlanMacTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVxlanMacTunnelID.setStatus("current")


class _HpnicfVxlanMacType_Type(Integer32):
    """Custom type hpnicfVxlanMacType based on Integer32"""
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


_HpnicfVxlanMacType_Type.__name__ = "Integer32"
_HpnicfVxlanMacType_Object = MibTableColumn
hpnicfVxlanMacType = _HpnicfVxlanMacType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5, 1, 3),
    _HpnicfVxlanMacType_Type()
)
hpnicfVxlanMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVxlanMacType.setStatus("current")
_HpnicfVxlanStaticMacTable_Object = MibTable
hpnicfVxlanStaticMacTable = _HpnicfVxlanStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfVxlanStaticMacTable.setStatus("current")
_HpnicfVxlanStaticMacEntry_Object = MibTableRow
hpnicfVxlanStaticMacEntry = _HpnicfVxlanStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6, 1)
)
hpnicfVxlanStaticMacEntry.setIndexNames(
    (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanVsiIndex"),
    (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanStaticMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfVxlanStaticMacEntry.setStatus("current")
_HpnicfVxlanStaticMacAddr_Type = MacAddress
_HpnicfVxlanStaticMacAddr_Object = MibTableColumn
hpnicfVxlanStaticMacAddr = _HpnicfVxlanStaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6, 1, 1),
    _HpnicfVxlanStaticMacAddr_Type()
)
hpnicfVxlanStaticMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVxlanStaticMacAddr.setStatus("current")
_HpnicfVxlanStaticMacTunnelID_Type = Unsigned32
_HpnicfVxlanStaticMacTunnelID_Object = MibTableColumn
hpnicfVxlanStaticMacTunnelID = _HpnicfVxlanStaticMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6, 1, 2),
    _HpnicfVxlanStaticMacTunnelID_Type()
)
hpnicfVxlanStaticMacTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVxlanStaticMacTunnelID.setStatus("current")
_HpnicfVxlanStaticMacRowStatus_Type = RowStatus
_HpnicfVxlanStaticMacRowStatus_Object = MibTableColumn
hpnicfVxlanStaticMacRowStatus = _HpnicfVxlanStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6, 1, 3),
    _HpnicfVxlanStaticMacRowStatus_Type()
)
hpnicfVxlanStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVxlanStaticMacRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VXLAN-MIB",
    **{"hpnicfVxlan": hpnicfVxlan,
       "hpnicfVxlanObjects": hpnicfVxlanObjects,
       "hpnicfVxlanScalarGroup": hpnicfVxlanScalarGroup,
       "hpnicfVxlanLocalMacNotify": hpnicfVxlanLocalMacNotify,
       "hpnicfVxlanRemoteMacLearn": hpnicfVxlanRemoteMacLearn,
       "hpnicfVxlanNextVxlanID": hpnicfVxlanNextVxlanID,
       "hpnicfVxlanConfigured": hpnicfVxlanConfigured,
       "hpnicfVxlanTable": hpnicfVxlanTable,
       "hpnicfVxlanEntry": hpnicfVxlanEntry,
       "hpnicfVxlanID": hpnicfVxlanID,
       "hpnicfVxlanAddrType": hpnicfVxlanAddrType,
       "hpnicfVxlanGroupAddr": hpnicfVxlanGroupAddr,
       "hpnicfVxlanSourceAddr": hpnicfVxlanSourceAddr,
       "hpnicfVxlanVsiIndex": hpnicfVxlanVsiIndex,
       "hpnicfVxlanRemoteMacCount": hpnicfVxlanRemoteMacCount,
       "hpnicfVxlanRowStatus": hpnicfVxlanRowStatus,
       "hpnicfVxlanTunnelTable": hpnicfVxlanTunnelTable,
       "hpnicfVxlanTunnelEntry": hpnicfVxlanTunnelEntry,
       "hpnicfVxlanTunnelID": hpnicfVxlanTunnelID,
       "hpnicfVxlanTunnelRowStatus": hpnicfVxlanTunnelRowStatus,
       "hpnicfVxlanTunnelOctets": hpnicfVxlanTunnelOctets,
       "hpnicfVxlanTunnelPackets": hpnicfVxlanTunnelPackets,
       "hpnicfVxlanTunnelBoundTable": hpnicfVxlanTunnelBoundTable,
       "hpnicfVxlanTunnelBoundEntry": hpnicfVxlanTunnelBoundEntry,
       "hpnicfVxlanTunnelBoundVxlanNum": hpnicfVxlanTunnelBoundVxlanNum,
       "hpnicfVxlanMacTable": hpnicfVxlanMacTable,
       "hpnicfVxlanMacEntry": hpnicfVxlanMacEntry,
       "hpnicfVxlanMacAddr": hpnicfVxlanMacAddr,
       "hpnicfVxlanMacTunnelID": hpnicfVxlanMacTunnelID,
       "hpnicfVxlanMacType": hpnicfVxlanMacType,
       "hpnicfVxlanStaticMacTable": hpnicfVxlanStaticMacTable,
       "hpnicfVxlanStaticMacEntry": hpnicfVxlanStaticMacEntry,
       "hpnicfVxlanStaticMacAddr": hpnicfVxlanStaticMacAddr,
       "hpnicfVxlanStaticMacTunnelID": hpnicfVxlanStaticMacTunnelID,
       "hpnicfVxlanStaticMacRowStatus": hpnicfVxlanStaticMacRowStatus}
)
