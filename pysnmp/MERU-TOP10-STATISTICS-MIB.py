# SNMP MIB module (MERU-TOP10-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-TOP10-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:15 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwStatistics,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwStatistics")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwTop10Statistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwTop10ApStationProblemTable_Object = MibTable
mwTop10ApStationProblemTable = _MwTop10ApStationProblemTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mwTop10ApStationProblemTable.setStatus("current")
_MwTop10ApStationProblemEntry_Object = MibTableRow
mwTop10ApStationProblemEntry = _MwTop10ApStationProblemEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1, 1)
)
mwTop10ApStationProblemEntry.setIndexNames(
    (0, "MERU-TOP10-STATISTICS-MIB", "mwTop10ApStationProblemTableIndex"),
)
if mibBuilder.loadTexts:
    mwTop10ApStationProblemEntry.setStatus("current")
_MwTop10ApStationProblemTableIndex_Type = Integer32
_MwTop10ApStationProblemTableIndex_Object = MibTableColumn
mwTop10ApStationProblemTableIndex = _MwTop10ApStationProblemTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1, 1, 1),
    _MwTop10ApStationProblemTableIndex_Type()
)
mwTop10ApStationProblemTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTop10ApStationProblemTableIndex.setStatus("current")
_MwTop10ApStationProblemApName_Type = DisplayString
_MwTop10ApStationProblemApName_Object = MibTableColumn
mwTop10ApStationProblemApName = _MwTop10ApStationProblemApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1, 1, 2),
    _MwTop10ApStationProblemApName_Type()
)
mwTop10ApStationProblemApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationProblemApName.setStatus("current")
_MwTop10ApStationProblemIfIndex_Type = Integer32
_MwTop10ApStationProblemIfIndex_Object = MibTableColumn
mwTop10ApStationProblemIfIndex = _MwTop10ApStationProblemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1, 1, 3),
    _MwTop10ApStationProblemIfIndex_Type()
)
mwTop10ApStationProblemIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationProblemIfIndex.setStatus("current")
_MwTop10ApStationProblemWepErrors_Type = Unsigned32
_MwTop10ApStationProblemWepErrors_Object = MibTableColumn
mwTop10ApStationProblemWepErrors = _MwTop10ApStationProblemWepErrors_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1, 1, 4),
    _MwTop10ApStationProblemWepErrors_Type()
)
mwTop10ApStationProblemWepErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationProblemWepErrors.setStatus("current")
_MwTop10ApStationProblemNmsApNodeId_Type = Integer32
_MwTop10ApStationProblemNmsApNodeId_Object = MibTableColumn
mwTop10ApStationProblemNmsApNodeId = _MwTop10ApStationProblemNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1, 1, 5),
    _MwTop10ApStationProblemNmsApNodeId_Type()
)
mwTop10ApStationProblemNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationProblemNmsApNodeId.setStatus("current")
_MwTop10ApStationProblemStationIPAddress_Type = IpAddress
_MwTop10ApStationProblemStationIPAddress_Object = MibTableColumn
mwTop10ApStationProblemStationIPAddress = _MwTop10ApStationProblemStationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1, 1, 6),
    _MwTop10ApStationProblemStationIPAddress_Type()
)
mwTop10ApStationProblemStationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationProblemStationIPAddress.setStatus("current")
_MwTop10ApStationProblemStationMacAddress_Type = MacAddress
_MwTop10ApStationProblemStationMacAddress_Object = MibTableColumn
mwTop10ApStationProblemStationMacAddress = _MwTop10ApStationProblemStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 1, 1, 7),
    _MwTop10ApStationProblemStationMacAddress_Type()
)
mwTop10ApStationProblemStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationProblemStationMacAddress.setStatus("current")
_MwTop10ApStationRxtxTable_Object = MibTable
mwTop10ApStationRxtxTable = _MwTop10ApStationRxtxTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxTable.setStatus("current")
_MwTop10ApStationRxtxEntry_Object = MibTableRow
mwTop10ApStationRxtxEntry = _MwTop10ApStationRxtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1)
)
mwTop10ApStationRxtxEntry.setIndexNames(
    (0, "MERU-TOP10-STATISTICS-MIB", "mwTop10ApStationRxtxTableIndex"),
)
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxEntry.setStatus("current")
_MwTop10ApStationRxtxTableIndex_Type = Integer32
_MwTop10ApStationRxtxTableIndex_Object = MibTableColumn
mwTop10ApStationRxtxTableIndex = _MwTop10ApStationRxtxTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1, 1),
    _MwTop10ApStationRxtxTableIndex_Type()
)
mwTop10ApStationRxtxTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxTableIndex.setStatus("current")
_MwTop10ApStationRxtxApName_Type = DisplayString
_MwTop10ApStationRxtxApName_Object = MibTableColumn
mwTop10ApStationRxtxApName = _MwTop10ApStationRxtxApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1, 2),
    _MwTop10ApStationRxtxApName_Type()
)
mwTop10ApStationRxtxApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxApName.setStatus("current")
_MwTop10ApStationRxtxIfIndex_Type = Integer32
_MwTop10ApStationRxtxIfIndex_Object = MibTableColumn
mwTop10ApStationRxtxIfIndex = _MwTop10ApStationRxtxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1, 3),
    _MwTop10ApStationRxtxIfIndex_Type()
)
mwTop10ApStationRxtxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxIfIndex.setStatus("current")
_MwTop10ApStationRxtxNmsApNodeId_Type = Integer32
_MwTop10ApStationRxtxNmsApNodeId_Object = MibTableColumn
mwTop10ApStationRxtxNmsApNodeId = _MwTop10ApStationRxtxNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1, 4),
    _MwTop10ApStationRxtxNmsApNodeId_Type()
)
mwTop10ApStationRxtxNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxNmsApNodeId.setStatus("current")
_MwTop10ApStationRxtxRxPacketCount_Type = Unsigned32
_MwTop10ApStationRxtxRxPacketCount_Object = MibTableColumn
mwTop10ApStationRxtxRxPacketCount = _MwTop10ApStationRxtxRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1, 5),
    _MwTop10ApStationRxtxRxPacketCount_Type()
)
mwTop10ApStationRxtxRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxRxPacketCount.setStatus("current")
_MwTop10ApStationRxtxTxPacketCount_Type = Unsigned32
_MwTop10ApStationRxtxTxPacketCount_Object = MibTableColumn
mwTop10ApStationRxtxTxPacketCount = _MwTop10ApStationRxtxTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1, 6),
    _MwTop10ApStationRxtxTxPacketCount_Type()
)
mwTop10ApStationRxtxTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxTxPacketCount.setStatus("current")
_MwTop10ApStationRxtxStationIPAddress_Type = IpAddress
_MwTop10ApStationRxtxStationIPAddress_Object = MibTableColumn
mwTop10ApStationRxtxStationIPAddress = _MwTop10ApStationRxtxStationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1, 7),
    _MwTop10ApStationRxtxStationIPAddress_Type()
)
mwTop10ApStationRxtxStationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxStationIPAddress.setStatus("current")
_MwTop10ApStationRxtxStationMacAddress_Type = MacAddress
_MwTop10ApStationRxtxStationMacAddress_Object = MibTableColumn
mwTop10ApStationRxtxStationMacAddress = _MwTop10ApStationRxtxStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 2, 1, 8),
    _MwTop10ApStationRxtxStationMacAddress_Type()
)
mwTop10ApStationRxtxStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApStationRxtxStationMacAddress.setStatus("current")
_MwTop10ApProblemTable_Object = MibTable
mwTop10ApProblemTable = _MwTop10ApProblemTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    mwTop10ApProblemTable.setStatus("current")
_MwTop10ApProblemEntry_Object = MibTableRow
mwTop10ApProblemEntry = _MwTop10ApProblemEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 3, 1)
)
mwTop10ApProblemEntry.setIndexNames(
    (0, "MERU-TOP10-STATISTICS-MIB", "mwTop10ApProblemTableIndex"),
)
if mibBuilder.loadTexts:
    mwTop10ApProblemEntry.setStatus("current")
_MwTop10ApProblemTableIndex_Type = Integer32
_MwTop10ApProblemTableIndex_Object = MibTableColumn
mwTop10ApProblemTableIndex = _MwTop10ApProblemTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 3, 1, 1),
    _MwTop10ApProblemTableIndex_Type()
)
mwTop10ApProblemTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTop10ApProblemTableIndex.setStatus("current")
_MwTop10ApProblemApName_Type = DisplayString
_MwTop10ApProblemApName_Object = MibTableColumn
mwTop10ApProblemApName = _MwTop10ApProblemApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 3, 1, 2),
    _MwTop10ApProblemApName_Type()
)
mwTop10ApProblemApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApProblemApName.setStatus("current")
_MwTop10ApProblemTxLoss_Type = Unsigned32
_MwTop10ApProblemTxLoss_Object = MibTableColumn
mwTop10ApProblemTxLoss = _MwTop10ApProblemTxLoss_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 3, 1, 3),
    _MwTop10ApProblemTxLoss_Type()
)
mwTop10ApProblemTxLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApProblemTxLoss.setStatus("current")
_MwTop10ApProblemIfIndex_Type = Integer32
_MwTop10ApProblemIfIndex_Object = MibTableColumn
mwTop10ApProblemIfIndex = _MwTop10ApProblemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 3, 1, 4),
    _MwTop10ApProblemIfIndex_Type()
)
mwTop10ApProblemIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApProblemIfIndex.setStatus("current")
_MwTop10ApProblemNmsApNodeId_Type = Integer32
_MwTop10ApProblemNmsApNodeId_Object = MibTableColumn
mwTop10ApProblemNmsApNodeId = _MwTop10ApProblemNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 3, 1, 5),
    _MwTop10ApProblemNmsApNodeId_Type()
)
mwTop10ApProblemNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApProblemNmsApNodeId.setStatus("current")
_MwTop10ApRxtxTable_Object = MibTable
mwTop10ApRxtxTable = _MwTop10ApRxtxTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    mwTop10ApRxtxTable.setStatus("current")
_MwTop10ApRxtxEntry_Object = MibTableRow
mwTop10ApRxtxEntry = _MwTop10ApRxtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 4, 1)
)
mwTop10ApRxtxEntry.setIndexNames(
    (0, "MERU-TOP10-STATISTICS-MIB", "mwTop10ApRxtxTableIndex"),
)
if mibBuilder.loadTexts:
    mwTop10ApRxtxEntry.setStatus("current")
_MwTop10ApRxtxTableIndex_Type = Integer32
_MwTop10ApRxtxTableIndex_Object = MibTableColumn
mwTop10ApRxtxTableIndex = _MwTop10ApRxtxTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 4, 1, 1),
    _MwTop10ApRxtxTableIndex_Type()
)
mwTop10ApRxtxTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTop10ApRxtxTableIndex.setStatus("current")
_MwTop10ApRxtxApName_Type = DisplayString
_MwTop10ApRxtxApName_Object = MibTableColumn
mwTop10ApRxtxApName = _MwTop10ApRxtxApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 4, 1, 2),
    _MwTop10ApRxtxApName_Type()
)
mwTop10ApRxtxApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApRxtxApName.setStatus("current")
_MwTop10ApRxtxIfIndex_Type = Integer32
_MwTop10ApRxtxIfIndex_Object = MibTableColumn
mwTop10ApRxtxIfIndex = _MwTop10ApRxtxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 4, 1, 3),
    _MwTop10ApRxtxIfIndex_Type()
)
mwTop10ApRxtxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApRxtxIfIndex.setStatus("current")
_MwTop10ApRxtxNmsApNodeId_Type = Integer32
_MwTop10ApRxtxNmsApNodeId_Object = MibTableColumn
mwTop10ApRxtxNmsApNodeId = _MwTop10ApRxtxNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 4, 1, 4),
    _MwTop10ApRxtxNmsApNodeId_Type()
)
mwTop10ApRxtxNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApRxtxNmsApNodeId.setStatus("current")
_MwTop10ApRxtxTxFrameCount_Type = Unsigned32
_MwTop10ApRxtxTxFrameCount_Object = MibTableColumn
mwTop10ApRxtxTxFrameCount = _MwTop10ApRxtxTxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 4, 1, 5),
    _MwTop10ApRxtxTxFrameCount_Type()
)
mwTop10ApRxtxTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApRxtxTxFrameCount.setStatus("current")
_MwTop10ApRxtxRxUnicastFrameCount_Type = Unsigned32
_MwTop10ApRxtxRxUnicastFrameCount_Object = MibTableColumn
mwTop10ApRxtxRxUnicastFrameCount = _MwTop10ApRxtxRxUnicastFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 2, 4, 1, 6),
    _MwTop10ApRxtxRxUnicastFrameCount_Type()
)
mwTop10ApRxtxRxUnicastFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTop10ApRxtxRxUnicastFrameCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-TOP10-STATISTICS-MIB",
    **{"mwTop10Statistics": mwTop10Statistics,
       "mwTop10ApStationProblemTable": mwTop10ApStationProblemTable,
       "mwTop10ApStationProblemEntry": mwTop10ApStationProblemEntry,
       "mwTop10ApStationProblemTableIndex": mwTop10ApStationProblemTableIndex,
       "mwTop10ApStationProblemApName": mwTop10ApStationProblemApName,
       "mwTop10ApStationProblemIfIndex": mwTop10ApStationProblemIfIndex,
       "mwTop10ApStationProblemWepErrors": mwTop10ApStationProblemWepErrors,
       "mwTop10ApStationProblemNmsApNodeId": mwTop10ApStationProblemNmsApNodeId,
       "mwTop10ApStationProblemStationIPAddress": mwTop10ApStationProblemStationIPAddress,
       "mwTop10ApStationProblemStationMacAddress": mwTop10ApStationProblemStationMacAddress,
       "mwTop10ApStationRxtxTable": mwTop10ApStationRxtxTable,
       "mwTop10ApStationRxtxEntry": mwTop10ApStationRxtxEntry,
       "mwTop10ApStationRxtxTableIndex": mwTop10ApStationRxtxTableIndex,
       "mwTop10ApStationRxtxApName": mwTop10ApStationRxtxApName,
       "mwTop10ApStationRxtxIfIndex": mwTop10ApStationRxtxIfIndex,
       "mwTop10ApStationRxtxNmsApNodeId": mwTop10ApStationRxtxNmsApNodeId,
       "mwTop10ApStationRxtxRxPacketCount": mwTop10ApStationRxtxRxPacketCount,
       "mwTop10ApStationRxtxTxPacketCount": mwTop10ApStationRxtxTxPacketCount,
       "mwTop10ApStationRxtxStationIPAddress": mwTop10ApStationRxtxStationIPAddress,
       "mwTop10ApStationRxtxStationMacAddress": mwTop10ApStationRxtxStationMacAddress,
       "mwTop10ApProblemTable": mwTop10ApProblemTable,
       "mwTop10ApProblemEntry": mwTop10ApProblemEntry,
       "mwTop10ApProblemTableIndex": mwTop10ApProblemTableIndex,
       "mwTop10ApProblemApName": mwTop10ApProblemApName,
       "mwTop10ApProblemTxLoss": mwTop10ApProblemTxLoss,
       "mwTop10ApProblemIfIndex": mwTop10ApProblemIfIndex,
       "mwTop10ApProblemNmsApNodeId": mwTop10ApProblemNmsApNodeId,
       "mwTop10ApRxtxTable": mwTop10ApRxtxTable,
       "mwTop10ApRxtxEntry": mwTop10ApRxtxEntry,
       "mwTop10ApRxtxTableIndex": mwTop10ApRxtxTableIndex,
       "mwTop10ApRxtxApName": mwTop10ApRxtxApName,
       "mwTop10ApRxtxIfIndex": mwTop10ApRxtxIfIndex,
       "mwTop10ApRxtxNmsApNodeId": mwTop10ApRxtxNmsApNodeId,
       "mwTop10ApRxtxTxFrameCount": mwTop10ApRxtxTxFrameCount,
       "mwTop10ApRxtxRxUnicastFrameCount": mwTop10ApRxtxRxUnicastFrameCount}
)
