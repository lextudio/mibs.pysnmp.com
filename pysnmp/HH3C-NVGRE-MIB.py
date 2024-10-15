# SNMP MIB module (HH3C-NVGRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-NVGRE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:24 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cNvgre = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156)
)
hh3cNvgre.setRevisions(
        ("2014-03-11 09:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cNvgreObjects_ObjectIdentity = ObjectIdentity
hh3cNvgreObjects = _Hh3cNvgreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1)
)
_Hh3cNvgreScalarGroup_ObjectIdentity = ObjectIdentity
hh3cNvgreScalarGroup = _Hh3cNvgreScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 1)
)
_Hh3cNvgreNextNvgreID_Type = Unsigned32
_Hh3cNvgreNextNvgreID_Object = MibScalar
hh3cNvgreNextNvgreID = _Hh3cNvgreNextNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 1, 1),
    _Hh3cNvgreNextNvgreID_Type()
)
hh3cNvgreNextNvgreID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNvgreNextNvgreID.setStatus("current")
_Hh3cNvgreConfigured_Type = Unsigned32
_Hh3cNvgreConfigured_Object = MibScalar
hh3cNvgreConfigured = _Hh3cNvgreConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 1, 2),
    _Hh3cNvgreConfigured_Type()
)
hh3cNvgreConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNvgreConfigured.setStatus("current")
_Hh3cNvgreTable_Object = MibTable
hh3cNvgreTable = _Hh3cNvgreTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cNvgreTable.setStatus("current")
_Hh3cNvgreEntry_Object = MibTableRow
hh3cNvgreEntry = _Hh3cNvgreEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 2, 1)
)
hh3cNvgreEntry.setIndexNames(
    (0, "HH3C-NVGRE-MIB", "hh3cNvgreID"),
)
if mibBuilder.loadTexts:
    hh3cNvgreEntry.setStatus("current")
_Hh3cNvgreID_Type = Unsigned32
_Hh3cNvgreID_Object = MibTableColumn
hh3cNvgreID = _Hh3cNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 2, 1, 1),
    _Hh3cNvgreID_Type()
)
hh3cNvgreID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNvgreID.setStatus("current")
_Hh3cNvgreVsiIndex_Type = Unsigned32
_Hh3cNvgreVsiIndex_Object = MibTableColumn
hh3cNvgreVsiIndex = _Hh3cNvgreVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 2, 1, 2),
    _Hh3cNvgreVsiIndex_Type()
)
hh3cNvgreVsiIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNvgreVsiIndex.setStatus("current")
_Hh3cNvgreRemoteMacCount_Type = Unsigned32
_Hh3cNvgreRemoteMacCount_Object = MibTableColumn
hh3cNvgreRemoteMacCount = _Hh3cNvgreRemoteMacCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 2, 1, 3),
    _Hh3cNvgreRemoteMacCount_Type()
)
hh3cNvgreRemoteMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNvgreRemoteMacCount.setStatus("current")
_Hh3cNvgreRowStatus_Type = RowStatus
_Hh3cNvgreRowStatus_Object = MibTableColumn
hh3cNvgreRowStatus = _Hh3cNvgreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 2, 1, 4),
    _Hh3cNvgreRowStatus_Type()
)
hh3cNvgreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNvgreRowStatus.setStatus("current")
_Hh3cNvgreTunnelTable_Object = MibTable
hh3cNvgreTunnelTable = _Hh3cNvgreTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cNvgreTunnelTable.setStatus("current")
_Hh3cNvgreTunnelEntry_Object = MibTableRow
hh3cNvgreTunnelEntry = _Hh3cNvgreTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 3, 1)
)
hh3cNvgreTunnelEntry.setIndexNames(
    (0, "HH3C-NVGRE-MIB", "hh3cNvgreID"),
    (0, "HH3C-NVGRE-MIB", "hh3cNvgreTunnelID"),
)
if mibBuilder.loadTexts:
    hh3cNvgreTunnelEntry.setStatus("current")
_Hh3cNvgreTunnelID_Type = Unsigned32
_Hh3cNvgreTunnelID_Object = MibTableColumn
hh3cNvgreTunnelID = _Hh3cNvgreTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 3, 1, 1),
    _Hh3cNvgreTunnelID_Type()
)
hh3cNvgreTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNvgreTunnelID.setStatus("current")
_Hh3cNvgreTunnelRowStatus_Type = RowStatus
_Hh3cNvgreTunnelRowStatus_Object = MibTableColumn
hh3cNvgreTunnelRowStatus = _Hh3cNvgreTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 3, 1, 2),
    _Hh3cNvgreTunnelRowStatus_Type()
)
hh3cNvgreTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNvgreTunnelRowStatus.setStatus("current")
_Hh3cNvgreTunnelOctets_Type = Counter64
_Hh3cNvgreTunnelOctets_Object = MibTableColumn
hh3cNvgreTunnelOctets = _Hh3cNvgreTunnelOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 3, 1, 3),
    _Hh3cNvgreTunnelOctets_Type()
)
hh3cNvgreTunnelOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNvgreTunnelOctets.setStatus("current")
_Hh3cNvgreTunnelPackets_Type = Counter64
_Hh3cNvgreTunnelPackets_Object = MibTableColumn
hh3cNvgreTunnelPackets = _Hh3cNvgreTunnelPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 3, 1, 4),
    _Hh3cNvgreTunnelPackets_Type()
)
hh3cNvgreTunnelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNvgreTunnelPackets.setStatus("current")
_Hh3cNvgreTunnelBoundTable_Object = MibTable
hh3cNvgreTunnelBoundTable = _Hh3cNvgreTunnelBoundTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cNvgreTunnelBoundTable.setStatus("current")
_Hh3cNvgreTunnelBoundEntry_Object = MibTableRow
hh3cNvgreTunnelBoundEntry = _Hh3cNvgreTunnelBoundEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 4, 1)
)
hh3cNvgreTunnelBoundEntry.setIndexNames(
    (0, "HH3C-NVGRE-MIB", "hh3cNvgreTunnelID"),
)
if mibBuilder.loadTexts:
    hh3cNvgreTunnelBoundEntry.setStatus("current")
_Hh3cNvgreTunnelBoundNvgreNum_Type = Unsigned32
_Hh3cNvgreTunnelBoundNvgreNum_Object = MibTableColumn
hh3cNvgreTunnelBoundNvgreNum = _Hh3cNvgreTunnelBoundNvgreNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 4, 1, 1),
    _Hh3cNvgreTunnelBoundNvgreNum_Type()
)
hh3cNvgreTunnelBoundNvgreNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNvgreTunnelBoundNvgreNum.setStatus("current")
_Hh3cNvgreMacTable_Object = MibTable
hh3cNvgreMacTable = _Hh3cNvgreMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cNvgreMacTable.setStatus("current")
_Hh3cNvgreMacEntry_Object = MibTableRow
hh3cNvgreMacEntry = _Hh3cNvgreMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 5, 1)
)
hh3cNvgreMacEntry.setIndexNames(
    (0, "HH3C-NVGRE-MIB", "hh3cNvgreVsiIndex"),
    (0, "HH3C-NVGRE-MIB", "hh3cNvgreMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cNvgreMacEntry.setStatus("current")
_Hh3cNvgreMacAddr_Type = MacAddress
_Hh3cNvgreMacAddr_Object = MibTableColumn
hh3cNvgreMacAddr = _Hh3cNvgreMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 5, 1, 1),
    _Hh3cNvgreMacAddr_Type()
)
hh3cNvgreMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNvgreMacAddr.setStatus("current")
_Hh3cNvgreMacTunnelID_Type = Unsigned32
_Hh3cNvgreMacTunnelID_Object = MibTableColumn
hh3cNvgreMacTunnelID = _Hh3cNvgreMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 5, 1, 2),
    _Hh3cNvgreMacTunnelID_Type()
)
hh3cNvgreMacTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNvgreMacTunnelID.setStatus("current")


class _Hh3cNvgreMacType_Type(Integer32):
    """Custom type hh3cNvgreMacType based on Integer32"""
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


_Hh3cNvgreMacType_Type.__name__ = "Integer32"
_Hh3cNvgreMacType_Object = MibTableColumn
hh3cNvgreMacType = _Hh3cNvgreMacType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 5, 1, 3),
    _Hh3cNvgreMacType_Type()
)
hh3cNvgreMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNvgreMacType.setStatus("current")
_Hh3cNvgreStaticMacTable_Object = MibTable
hh3cNvgreStaticMacTable = _Hh3cNvgreStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cNvgreStaticMacTable.setStatus("current")
_Hh3cNvgreStaticMacEntry_Object = MibTableRow
hh3cNvgreStaticMacEntry = _Hh3cNvgreStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 6, 1)
)
hh3cNvgreStaticMacEntry.setIndexNames(
    (0, "HH3C-NVGRE-MIB", "hh3cNvgreVsiIndex"),
    (0, "HH3C-NVGRE-MIB", "hh3cNvgreStaticMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cNvgreStaticMacEntry.setStatus("current")
_Hh3cNvgreStaticMacAddr_Type = MacAddress
_Hh3cNvgreStaticMacAddr_Object = MibTableColumn
hh3cNvgreStaticMacAddr = _Hh3cNvgreStaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 6, 1, 1),
    _Hh3cNvgreStaticMacAddr_Type()
)
hh3cNvgreStaticMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNvgreStaticMacAddr.setStatus("current")
_Hh3cNvgreStaticMacTunnelID_Type = Unsigned32
_Hh3cNvgreStaticMacTunnelID_Object = MibTableColumn
hh3cNvgreStaticMacTunnelID = _Hh3cNvgreStaticMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 6, 1, 2),
    _Hh3cNvgreStaticMacTunnelID_Type()
)
hh3cNvgreStaticMacTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNvgreStaticMacTunnelID.setStatus("current")
_Hh3cNvgreStaticMacRowStatus_Type = RowStatus
_Hh3cNvgreStaticMacRowStatus_Object = MibTableColumn
hh3cNvgreStaticMacRowStatus = _Hh3cNvgreStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156, 1, 6, 1, 3),
    _Hh3cNvgreStaticMacRowStatus_Type()
)
hh3cNvgreStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNvgreStaticMacRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NVGRE-MIB",
    **{"hh3cNvgre": hh3cNvgre,
       "hh3cNvgreObjects": hh3cNvgreObjects,
       "hh3cNvgreScalarGroup": hh3cNvgreScalarGroup,
       "hh3cNvgreNextNvgreID": hh3cNvgreNextNvgreID,
       "hh3cNvgreConfigured": hh3cNvgreConfigured,
       "hh3cNvgreTable": hh3cNvgreTable,
       "hh3cNvgreEntry": hh3cNvgreEntry,
       "hh3cNvgreID": hh3cNvgreID,
       "hh3cNvgreVsiIndex": hh3cNvgreVsiIndex,
       "hh3cNvgreRemoteMacCount": hh3cNvgreRemoteMacCount,
       "hh3cNvgreRowStatus": hh3cNvgreRowStatus,
       "hh3cNvgreTunnelTable": hh3cNvgreTunnelTable,
       "hh3cNvgreTunnelEntry": hh3cNvgreTunnelEntry,
       "hh3cNvgreTunnelID": hh3cNvgreTunnelID,
       "hh3cNvgreTunnelRowStatus": hh3cNvgreTunnelRowStatus,
       "hh3cNvgreTunnelOctets": hh3cNvgreTunnelOctets,
       "hh3cNvgreTunnelPackets": hh3cNvgreTunnelPackets,
       "hh3cNvgreTunnelBoundTable": hh3cNvgreTunnelBoundTable,
       "hh3cNvgreTunnelBoundEntry": hh3cNvgreTunnelBoundEntry,
       "hh3cNvgreTunnelBoundNvgreNum": hh3cNvgreTunnelBoundNvgreNum,
       "hh3cNvgreMacTable": hh3cNvgreMacTable,
       "hh3cNvgreMacEntry": hh3cNvgreMacEntry,
       "hh3cNvgreMacAddr": hh3cNvgreMacAddr,
       "hh3cNvgreMacTunnelID": hh3cNvgreMacTunnelID,
       "hh3cNvgreMacType": hh3cNvgreMacType,
       "hh3cNvgreStaticMacTable": hh3cNvgreStaticMacTable,
       "hh3cNvgreStaticMacEntry": hh3cNvgreStaticMacEntry,
       "hh3cNvgreStaticMacAddr": hh3cNvgreStaticMacAddr,
       "hh3cNvgreStaticMacTunnelID": hh3cNvgreStaticMacTunnelID,
       "hh3cNvgreStaticMacRowStatus": hh3cNvgreStaticMacRowStatus}
)
