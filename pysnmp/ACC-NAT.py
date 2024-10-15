# SNMP MIB module (ACC-NAT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-NAT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:38 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccNAT_ObjectIdentity = ObjectIdentity
accNAT = _AccNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61)
)
_AccNATMapTable_Object = MibTable
accNATMapTable = _AccNATMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 1)
)
if mibBuilder.loadTexts:
    accNATMapTable.setStatus("mandatory")
_AccNATMapEntry_Object = MibTableRow
accNATMapEntry = _AccNATMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 1, 1)
)
accNATMapEntry.setIndexNames(
    (0, "ACC-NAT", "accNATMapIfIndex"),
)
if mibBuilder.loadTexts:
    accNATMapEntry.setStatus("mandatory")
_AccNATMapIfIndex_Type = Integer32
_AccNATMapIfIndex_Object = MibTableColumn
accNATMapIfIndex = _AccNATMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 1, 1, 1),
    _AccNATMapIfIndex_Type()
)
accNATMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNATMapIfIndex.setStatus("mandatory")
_AccNATMapMapAddr_Type = IpAddress
_AccNATMapMapAddr_Object = MibTableColumn
accNATMapMapAddr = _AccNATMapMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 1, 1, 2),
    _AccNATMapMapAddr_Type()
)
accNATMapMapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNATMapMapAddr.setStatus("mandatory")
_AccNATMapStatTable_Object = MibTable
accNATMapStatTable = _AccNATMapStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2)
)
if mibBuilder.loadTexts:
    accNATMapStatTable.setStatus("mandatory")
_AccNATMapStatEntry_Object = MibTableRow
accNATMapStatEntry = _AccNATMapStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1)
)
accNATMapStatEntry.setIndexNames(
    (0, "ACC-NAT", "accNATMapIfIndex"),
)
if mibBuilder.loadTexts:
    accNATMapStatEntry.setStatus("mandatory")
_AccNatMapStatTblIfIndex_Type = Integer32
_AccNatMapStatTblIfIndex_Object = MibTableColumn
accNatMapStatTblIfIndex = _AccNatMapStatTblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 1),
    _AccNatMapStatTblIfIndex_Type()
)
accNatMapStatTblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblIfIndex.setStatus("mandatory")
_AccNatMapStatTblMapAddr_Type = IpAddress
_AccNatMapStatTblMapAddr_Object = MibTableColumn
accNatMapStatTblMapAddr = _AccNatMapStatTblMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 2),
    _AccNatMapStatTblMapAddr_Type()
)
accNatMapStatTblMapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblMapAddr.setStatus("mandatory")
_AccNatMapStatTblSrcAddr_Type = IpAddress
_AccNatMapStatTblSrcAddr_Object = MibTableColumn
accNatMapStatTblSrcAddr = _AccNatMapStatTblSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 3),
    _AccNatMapStatTblSrcAddr_Type()
)
accNatMapStatTblSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblSrcAddr.setStatus("mandatory")
_AccNatMapStatTblDstAddr_Type = IpAddress
_AccNatMapStatTblDstAddr_Object = MibTableColumn
accNatMapStatTblDstAddr = _AccNatMapStatTblDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 4),
    _AccNatMapStatTblDstAddr_Type()
)
accNatMapStatTblDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblDstAddr.setStatus("mandatory")
_AccNatMapStatTblMapPort_Type = Integer32
_AccNatMapStatTblMapPort_Object = MibTableColumn
accNatMapStatTblMapPort = _AccNatMapStatTblMapPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 5),
    _AccNatMapStatTblMapPort_Type()
)
accNatMapStatTblMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblMapPort.setStatus("mandatory")
_AccNatMapStatTblSrcPort_Type = Integer32
_AccNatMapStatTblSrcPort_Object = MibTableColumn
accNatMapStatTblSrcPort = _AccNatMapStatTblSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 6),
    _AccNatMapStatTblSrcPort_Type()
)
accNatMapStatTblSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblSrcPort.setStatus("mandatory")
_AccNatMapStatTblDstPort_Type = Integer32
_AccNatMapStatTblDstPort_Object = MibTableColumn
accNatMapStatTblDstPort = _AccNatMapStatTblDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 7),
    _AccNatMapStatTblDstPort_Type()
)
accNatMapStatTblDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblDstPort.setStatus("mandatory")
_AccNatMapStatTblMapCnts_Type = Counter32
_AccNatMapStatTblMapCnts_Object = MibTableColumn
accNatMapStatTblMapCnts = _AccNatMapStatTblMapCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 8),
    _AccNatMapStatTblMapCnts_Type()
)
accNatMapStatTblMapCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblMapCnts.setStatus("mandatory")
_AccNatMapStatTblUnmapCnts_Type = Counter32
_AccNatMapStatTblUnmapCnts_Object = MibTableColumn
accNatMapStatTblUnmapCnts = _AccNatMapStatTblUnmapCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 9),
    _AccNatMapStatTblUnmapCnts_Type()
)
accNatMapStatTblUnmapCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblUnmapCnts.setStatus("mandatory")
_AccNatMapStatTblProto_Type = Integer32
_AccNatMapStatTblProto_Object = MibTableColumn
accNatMapStatTblProto = _AccNatMapStatTblProto_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 2, 1, 10),
    _AccNatMapStatTblProto_Type()
)
accNatMapStatTblProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNatMapStatTblProto.setStatus("mandatory")
_AccNAVMapTable_Object = MibTable
accNAVMapTable = _AccNAVMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 3)
)
if mibBuilder.loadTexts:
    accNAVMapTable.setStatus("mandatory")
_AccNAVMapEntry_Object = MibTableRow
accNAVMapEntry = _AccNAVMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 3, 1)
)
accNAVMapEntry.setIndexNames(
    (0, "ACC-NAT", "accNAVMapIfIndex"),
)
if mibBuilder.loadTexts:
    accNAVMapEntry.setStatus("mandatory")
_AccNAVMapIfIndex_Type = Integer32
_AccNAVMapIfIndex_Object = MibTableColumn
accNAVMapIfIndex = _AccNAVMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 3, 1, 1),
    _AccNAVMapIfIndex_Type()
)
accNAVMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNAVMapIfIndex.setStatus("mandatory")
_AccNAVMapServerPort_Type = Integer32
_AccNAVMapServerPort_Object = MibTableColumn
accNAVMapServerPort = _AccNAVMapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 3, 1, 2),
    _AccNAVMapServerPort_Type()
)
accNAVMapServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNAVMapServerPort.setStatus("mandatory")
_AccNAVMapServerAddr_Type = IpAddress
_AccNAVMapServerAddr_Object = MibTableColumn
accNAVMapServerAddr = _AccNAVMapServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 3, 1, 3),
    _AccNAVMapServerAddr_Type()
)
accNAVMapServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNAVMapServerAddr.setStatus("mandatory")
_AccNATTable_Object = MibTable
accNATTable = _AccNATTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 4)
)
if mibBuilder.loadTexts:
    accNATTable.setStatus("mandatory")
_AccNATEntry_Object = MibTableRow
accNATEntry = _AccNATEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 4, 1)
)
accNATEntry.setIndexNames(
    (0, "ACC-NAT", "accNATIfIndex"),
)
if mibBuilder.loadTexts:
    accNATEntry.setStatus("mandatory")
_AccNATIfIndex_Type = Integer32
_AccNATIfIndex_Object = MibTableColumn
accNATIfIndex = _AccNATIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 4, 1, 1),
    _AccNATIfIndex_Type()
)
accNATIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNATIfIndex.setStatus("mandatory")
_AccNATSourceAddr_Type = IpAddress
_AccNATSourceAddr_Object = MibTableColumn
accNATSourceAddr = _AccNATSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 4, 1, 2),
    _AccNATSourceAddr_Type()
)
accNATSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNATSourceAddr.setStatus("mandatory")
_AccNATSourceSubnetMask_Type = IpAddress
_AccNATSourceSubnetMask_Object = MibTableColumn
accNATSourceSubnetMask = _AccNATSourceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 4, 1, 3),
    _AccNATSourceSubnetMask_Type()
)
accNATSourceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNATSourceSubnetMask.setStatus("mandatory")
_AccNATMapAddr_Type = IpAddress
_AccNATMapAddr_Object = MibTableColumn
accNATMapAddr = _AccNATMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 4, 1, 4),
    _AccNATMapAddr_Type()
)
accNATMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNATMapAddr.setStatus("mandatory")
_AccNATMapSubnetMask_Type = IpAddress
_AccNATMapSubnetMask_Object = MibTableColumn
accNATMapSubnetMask = _AccNATMapSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 61, 4, 1, 5),
    _AccNATMapSubnetMask_Type()
)
accNATMapSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNATMapSubnetMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-NAT",
    **{"accNAT": accNAT,
       "accNATMapTable": accNATMapTable,
       "accNATMapEntry": accNATMapEntry,
       "accNATMapIfIndex": accNATMapIfIndex,
       "accNATMapMapAddr": accNATMapMapAddr,
       "accNATMapStatTable": accNATMapStatTable,
       "accNATMapStatEntry": accNATMapStatEntry,
       "accNatMapStatTblIfIndex": accNatMapStatTblIfIndex,
       "accNatMapStatTblMapAddr": accNatMapStatTblMapAddr,
       "accNatMapStatTblSrcAddr": accNatMapStatTblSrcAddr,
       "accNatMapStatTblDstAddr": accNatMapStatTblDstAddr,
       "accNatMapStatTblMapPort": accNatMapStatTblMapPort,
       "accNatMapStatTblSrcPort": accNatMapStatTblSrcPort,
       "accNatMapStatTblDstPort": accNatMapStatTblDstPort,
       "accNatMapStatTblMapCnts": accNatMapStatTblMapCnts,
       "accNatMapStatTblUnmapCnts": accNatMapStatTblUnmapCnts,
       "accNatMapStatTblProto": accNatMapStatTblProto,
       "accNAVMapTable": accNAVMapTable,
       "accNAVMapEntry": accNAVMapEntry,
       "accNAVMapIfIndex": accNAVMapIfIndex,
       "accNAVMapServerPort": accNAVMapServerPort,
       "accNAVMapServerAddr": accNAVMapServerAddr,
       "accNATTable": accNATTable,
       "accNATEntry": accNATEntry,
       "accNATIfIndex": accNATIfIndex,
       "accNATSourceAddr": accNATSourceAddr,
       "accNATSourceSubnetMask": accNATSourceSubnetMask,
       "accNATMapAddr": accNATMapAddr,
       "accNATMapSubnetMask": accNATMapSubnetMask}
)
