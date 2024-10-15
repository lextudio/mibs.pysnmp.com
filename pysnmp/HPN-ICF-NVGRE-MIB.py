# SNMP MIB module (HPN-ICF-NVGRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-NVGRE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:22 2024
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

hpnicfNvgre = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156)
)
hpnicfNvgre.setRevisions(
        ("2014-03-11 09:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfNvgreObjects_ObjectIdentity = ObjectIdentity
hpnicfNvgreObjects = _HpnicfNvgreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1)
)
_HpnicfNvgreScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfNvgreScalarGroup = _HpnicfNvgreScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 1)
)
_HpnicfNvgreNextNvgreID_Type = Unsigned32
_HpnicfNvgreNextNvgreID_Object = MibScalar
hpnicfNvgreNextNvgreID = _HpnicfNvgreNextNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 1, 1),
    _HpnicfNvgreNextNvgreID_Type()
)
hpnicfNvgreNextNvgreID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNvgreNextNvgreID.setStatus("current")
_HpnicfNvgreConfigured_Type = Unsigned32
_HpnicfNvgreConfigured_Object = MibScalar
hpnicfNvgreConfigured = _HpnicfNvgreConfigured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 1, 2),
    _HpnicfNvgreConfigured_Type()
)
hpnicfNvgreConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNvgreConfigured.setStatus("current")
_HpnicfNvgreTable_Object = MibTable
hpnicfNvgreTable = _HpnicfNvgreTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfNvgreTable.setStatus("current")
_HpnicfNvgreEntry_Object = MibTableRow
hpnicfNvgreEntry = _HpnicfNvgreEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1)
)
hpnicfNvgreEntry.setIndexNames(
    (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreID"),
)
if mibBuilder.loadTexts:
    hpnicfNvgreEntry.setStatus("current")
_HpnicfNvgreID_Type = Unsigned32
_HpnicfNvgreID_Object = MibTableColumn
hpnicfNvgreID = _HpnicfNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1, 1),
    _HpnicfNvgreID_Type()
)
hpnicfNvgreID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNvgreID.setStatus("current")
_HpnicfNvgreVsiIndex_Type = Unsigned32
_HpnicfNvgreVsiIndex_Object = MibTableColumn
hpnicfNvgreVsiIndex = _HpnicfNvgreVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1, 2),
    _HpnicfNvgreVsiIndex_Type()
)
hpnicfNvgreVsiIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNvgreVsiIndex.setStatus("current")
_HpnicfNvgreRemoteMacCount_Type = Unsigned32
_HpnicfNvgreRemoteMacCount_Object = MibTableColumn
hpnicfNvgreRemoteMacCount = _HpnicfNvgreRemoteMacCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1, 3),
    _HpnicfNvgreRemoteMacCount_Type()
)
hpnicfNvgreRemoteMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNvgreRemoteMacCount.setStatus("current")
_HpnicfNvgreRowStatus_Type = RowStatus
_HpnicfNvgreRowStatus_Object = MibTableColumn
hpnicfNvgreRowStatus = _HpnicfNvgreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 2, 1, 4),
    _HpnicfNvgreRowStatus_Type()
)
hpnicfNvgreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNvgreRowStatus.setStatus("current")
_HpnicfNvgreTunnelTable_Object = MibTable
hpnicfNvgreTunnelTable = _HpnicfNvgreTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelTable.setStatus("current")
_HpnicfNvgreTunnelEntry_Object = MibTableRow
hpnicfNvgreTunnelEntry = _HpnicfNvgreTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1)
)
hpnicfNvgreTunnelEntry.setIndexNames(
    (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreID"),
    (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreTunnelID"),
)
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelEntry.setStatus("current")
_HpnicfNvgreTunnelID_Type = Unsigned32
_HpnicfNvgreTunnelID_Object = MibTableColumn
hpnicfNvgreTunnelID = _HpnicfNvgreTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1, 1),
    _HpnicfNvgreTunnelID_Type()
)
hpnicfNvgreTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelID.setStatus("current")
_HpnicfNvgreTunnelRowStatus_Type = RowStatus
_HpnicfNvgreTunnelRowStatus_Object = MibTableColumn
hpnicfNvgreTunnelRowStatus = _HpnicfNvgreTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1, 2),
    _HpnicfNvgreTunnelRowStatus_Type()
)
hpnicfNvgreTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelRowStatus.setStatus("current")
_HpnicfNvgreTunnelOctets_Type = Counter64
_HpnicfNvgreTunnelOctets_Object = MibTableColumn
hpnicfNvgreTunnelOctets = _HpnicfNvgreTunnelOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1, 3),
    _HpnicfNvgreTunnelOctets_Type()
)
hpnicfNvgreTunnelOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelOctets.setStatus("current")
_HpnicfNvgreTunnelPackets_Type = Counter64
_HpnicfNvgreTunnelPackets_Object = MibTableColumn
hpnicfNvgreTunnelPackets = _HpnicfNvgreTunnelPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 3, 1, 4),
    _HpnicfNvgreTunnelPackets_Type()
)
hpnicfNvgreTunnelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelPackets.setStatus("current")
_HpnicfNvgreTunnelBoundTable_Object = MibTable
hpnicfNvgreTunnelBoundTable = _HpnicfNvgreTunnelBoundTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelBoundTable.setStatus("current")
_HpnicfNvgreTunnelBoundEntry_Object = MibTableRow
hpnicfNvgreTunnelBoundEntry = _HpnicfNvgreTunnelBoundEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 4, 1)
)
hpnicfNvgreTunnelBoundEntry.setIndexNames(
    (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreTunnelID"),
)
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelBoundEntry.setStatus("current")
_HpnicfNvgreTunnelBoundNvgreNum_Type = Unsigned32
_HpnicfNvgreTunnelBoundNvgreNum_Object = MibTableColumn
hpnicfNvgreTunnelBoundNvgreNum = _HpnicfNvgreTunnelBoundNvgreNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 4, 1, 1),
    _HpnicfNvgreTunnelBoundNvgreNum_Type()
)
hpnicfNvgreTunnelBoundNvgreNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNvgreTunnelBoundNvgreNum.setStatus("current")
_HpnicfNvgreMacTable_Object = MibTable
hpnicfNvgreMacTable = _HpnicfNvgreMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfNvgreMacTable.setStatus("current")
_HpnicfNvgreMacEntry_Object = MibTableRow
hpnicfNvgreMacEntry = _HpnicfNvgreMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5, 1)
)
hpnicfNvgreMacEntry.setIndexNames(
    (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreVsiIndex"),
    (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfNvgreMacEntry.setStatus("current")
_HpnicfNvgreMacAddr_Type = MacAddress
_HpnicfNvgreMacAddr_Object = MibTableColumn
hpnicfNvgreMacAddr = _HpnicfNvgreMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5, 1, 1),
    _HpnicfNvgreMacAddr_Type()
)
hpnicfNvgreMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNvgreMacAddr.setStatus("current")
_HpnicfNvgreMacTunnelID_Type = Unsigned32
_HpnicfNvgreMacTunnelID_Object = MibTableColumn
hpnicfNvgreMacTunnelID = _HpnicfNvgreMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5, 1, 2),
    _HpnicfNvgreMacTunnelID_Type()
)
hpnicfNvgreMacTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNvgreMacTunnelID.setStatus("current")


class _HpnicfNvgreMacType_Type(Integer32):
    """Custom type hpnicfNvgreMacType based on Integer32"""
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


_HpnicfNvgreMacType_Type.__name__ = "Integer32"
_HpnicfNvgreMacType_Object = MibTableColumn
hpnicfNvgreMacType = _HpnicfNvgreMacType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 5, 1, 3),
    _HpnicfNvgreMacType_Type()
)
hpnicfNvgreMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNvgreMacType.setStatus("current")
_HpnicfNvgreStaticMacTable_Object = MibTable
hpnicfNvgreStaticMacTable = _HpnicfNvgreStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfNvgreStaticMacTable.setStatus("current")
_HpnicfNvgreStaticMacEntry_Object = MibTableRow
hpnicfNvgreStaticMacEntry = _HpnicfNvgreStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6, 1)
)
hpnicfNvgreStaticMacEntry.setIndexNames(
    (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreVsiIndex"),
    (0, "HPN-ICF-NVGRE-MIB", "hpnicfNvgreStaticMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfNvgreStaticMacEntry.setStatus("current")
_HpnicfNvgreStaticMacAddr_Type = MacAddress
_HpnicfNvgreStaticMacAddr_Object = MibTableColumn
hpnicfNvgreStaticMacAddr = _HpnicfNvgreStaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6, 1, 1),
    _HpnicfNvgreStaticMacAddr_Type()
)
hpnicfNvgreStaticMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNvgreStaticMacAddr.setStatus("current")
_HpnicfNvgreStaticMacTunnelID_Type = Unsigned32
_HpnicfNvgreStaticMacTunnelID_Object = MibTableColumn
hpnicfNvgreStaticMacTunnelID = _HpnicfNvgreStaticMacTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6, 1, 2),
    _HpnicfNvgreStaticMacTunnelID_Type()
)
hpnicfNvgreStaticMacTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNvgreStaticMacTunnelID.setStatus("current")
_HpnicfNvgreStaticMacRowStatus_Type = RowStatus
_HpnicfNvgreStaticMacRowStatus_Object = MibTableColumn
hpnicfNvgreStaticMacRowStatus = _HpnicfNvgreStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 156, 1, 6, 1, 3),
    _HpnicfNvgreStaticMacRowStatus_Type()
)
hpnicfNvgreStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNvgreStaticMacRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-NVGRE-MIB",
    **{"hpnicfNvgre": hpnicfNvgre,
       "hpnicfNvgreObjects": hpnicfNvgreObjects,
       "hpnicfNvgreScalarGroup": hpnicfNvgreScalarGroup,
       "hpnicfNvgreNextNvgreID": hpnicfNvgreNextNvgreID,
       "hpnicfNvgreConfigured": hpnicfNvgreConfigured,
       "hpnicfNvgreTable": hpnicfNvgreTable,
       "hpnicfNvgreEntry": hpnicfNvgreEntry,
       "hpnicfNvgreID": hpnicfNvgreID,
       "hpnicfNvgreVsiIndex": hpnicfNvgreVsiIndex,
       "hpnicfNvgreRemoteMacCount": hpnicfNvgreRemoteMacCount,
       "hpnicfNvgreRowStatus": hpnicfNvgreRowStatus,
       "hpnicfNvgreTunnelTable": hpnicfNvgreTunnelTable,
       "hpnicfNvgreTunnelEntry": hpnicfNvgreTunnelEntry,
       "hpnicfNvgreTunnelID": hpnicfNvgreTunnelID,
       "hpnicfNvgreTunnelRowStatus": hpnicfNvgreTunnelRowStatus,
       "hpnicfNvgreTunnelOctets": hpnicfNvgreTunnelOctets,
       "hpnicfNvgreTunnelPackets": hpnicfNvgreTunnelPackets,
       "hpnicfNvgreTunnelBoundTable": hpnicfNvgreTunnelBoundTable,
       "hpnicfNvgreTunnelBoundEntry": hpnicfNvgreTunnelBoundEntry,
       "hpnicfNvgreTunnelBoundNvgreNum": hpnicfNvgreTunnelBoundNvgreNum,
       "hpnicfNvgreMacTable": hpnicfNvgreMacTable,
       "hpnicfNvgreMacEntry": hpnicfNvgreMacEntry,
       "hpnicfNvgreMacAddr": hpnicfNvgreMacAddr,
       "hpnicfNvgreMacTunnelID": hpnicfNvgreMacTunnelID,
       "hpnicfNvgreMacType": hpnicfNvgreMacType,
       "hpnicfNvgreStaticMacTable": hpnicfNvgreStaticMacTable,
       "hpnicfNvgreStaticMacEntry": hpnicfNvgreStaticMacEntry,
       "hpnicfNvgreStaticMacAddr": hpnicfNvgreStaticMacAddr,
       "hpnicfNvgreStaticMacTunnelID": hpnicfNvgreStaticMacTunnelID,
       "hpnicfNvgreStaticMacRowStatus": hpnicfNvgreStaticMacRowStatus}
)
