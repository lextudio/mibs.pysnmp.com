# SNMP MIB module (Nortel-MsCarrier-MscPassport-VnsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VnsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:20 2024
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

(mscRtg,
 mscRtgIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-BaseRoutingMIB",
    "mscRtg",
    "mscRtgIndex")

(DisplayString,
 Integer32,
 InterfaceIndex,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 Link,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiStringIndex",
    "Link",
    "PassportCounter64")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscRtgVns_ObjectIdentity = ObjectIdentity
mscRtgVns = _MscRtgVns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3)
)
_MscRtgVnsRowStatusTable_Object = MibTable
mscRtgVnsRowStatusTable = _MscRtgVnsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1)
)
if mibBuilder.loadTexts:
    mscRtgVnsRowStatusTable.setStatus("mandatory")
_MscRtgVnsRowStatusEntry_Object = MibTableRow
mscRtgVnsRowStatusEntry = _MscRtgVnsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1)
)
mscRtgVnsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsRowStatusEntry.setStatus("mandatory")
_MscRtgVnsRowStatus_Type = RowStatus
_MscRtgVnsRowStatus_Object = MibTableColumn
mscRtgVnsRowStatus = _MscRtgVnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1, 1),
    _MscRtgVnsRowStatus_Type()
)
mscRtgVnsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsRowStatus.setStatus("mandatory")
_MscRtgVnsComponentName_Type = DisplayString
_MscRtgVnsComponentName_Object = MibTableColumn
mscRtgVnsComponentName = _MscRtgVnsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1, 2),
    _MscRtgVnsComponentName_Type()
)
mscRtgVnsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsComponentName.setStatus("mandatory")
_MscRtgVnsStorageType_Type = StorageType
_MscRtgVnsStorageType_Object = MibTableColumn
mscRtgVnsStorageType = _MscRtgVnsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1, 4),
    _MscRtgVnsStorageType_Type()
)
mscRtgVnsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsStorageType.setStatus("mandatory")


class _MscRtgVnsIndex_Type(AsciiStringIndex):
    """Custom type mscRtgVnsIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscRtgVnsIndex_Type.__name__ = "AsciiStringIndex"
_MscRtgVnsIndex_Object = MibTableColumn
mscRtgVnsIndex = _MscRtgVnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1, 10),
    _MscRtgVnsIndex_Type()
)
mscRtgVnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgVnsIndex.setStatus("mandatory")
_MscRtgVnsNode_ObjectIdentity = ObjectIdentity
mscRtgVnsNode = _MscRtgVnsNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2)
)
_MscRtgVnsNodeRowStatusTable_Object = MibTable
mscRtgVnsNodeRowStatusTable = _MscRtgVnsNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscRtgVnsNodeRowStatusTable.setStatus("mandatory")
_MscRtgVnsNodeRowStatusEntry_Object = MibTableRow
mscRtgVnsNodeRowStatusEntry = _MscRtgVnsNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1)
)
mscRtgVnsNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsNodeIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsNodeRowStatusEntry.setStatus("mandatory")
_MscRtgVnsNodeRowStatus_Type = RowStatus
_MscRtgVnsNodeRowStatus_Object = MibTableColumn
mscRtgVnsNodeRowStatus = _MscRtgVnsNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1, 1),
    _MscRtgVnsNodeRowStatus_Type()
)
mscRtgVnsNodeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsNodeRowStatus.setStatus("mandatory")
_MscRtgVnsNodeComponentName_Type = DisplayString
_MscRtgVnsNodeComponentName_Object = MibTableColumn
mscRtgVnsNodeComponentName = _MscRtgVnsNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1, 2),
    _MscRtgVnsNodeComponentName_Type()
)
mscRtgVnsNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsNodeComponentName.setStatus("mandatory")
_MscRtgVnsNodeStorageType_Type = StorageType
_MscRtgVnsNodeStorageType_Object = MibTableColumn
mscRtgVnsNodeStorageType = _MscRtgVnsNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1, 4),
    _MscRtgVnsNodeStorageType_Type()
)
mscRtgVnsNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsNodeStorageType.setStatus("mandatory")


class _MscRtgVnsNodeIndex_Type(Integer32):
    """Custom type mscRtgVnsNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscRtgVnsNodeIndex_Type.__name__ = "Integer32"
_MscRtgVnsNodeIndex_Object = MibTableColumn
mscRtgVnsNodeIndex = _MscRtgVnsNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1, 10),
    _MscRtgVnsNodeIndex_Type()
)
mscRtgVnsNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgVnsNodeIndex.setStatus("mandatory")
_MscRtgVnsNodeOperTable_Object = MibTable
mscRtgVnsNodeOperTable = _MscRtgVnsNodeOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscRtgVnsNodeOperTable.setStatus("mandatory")
_MscRtgVnsNodeOperEntry_Object = MibTableRow
mscRtgVnsNodeOperEntry = _MscRtgVnsNodeOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10, 1)
)
mscRtgVnsNodeOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsNodeIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsNodeOperEntry.setStatus("mandatory")


class _MscRtgVnsNodeMetric_Type(Unsigned32):
    """Custom type mscRtgVnsNodeMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgVnsNodeMetric_Type.__name__ = "Unsigned32"
_MscRtgVnsNodeMetric_Object = MibTableColumn
mscRtgVnsNodeMetric = _MscRtgVnsNodeMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10, 1, 1),
    _MscRtgVnsNodeMetric_Type()
)
mscRtgVnsNodeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsNodeMetric.setStatus("mandatory")
_MscRtgVnsNodeNextHopLinkGroup1_Type = RowPointer
_MscRtgVnsNodeNextHopLinkGroup1_Object = MibTableColumn
mscRtgVnsNodeNextHopLinkGroup1 = _MscRtgVnsNodeNextHopLinkGroup1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10, 1, 2),
    _MscRtgVnsNodeNextHopLinkGroup1_Type()
)
mscRtgVnsNodeNextHopLinkGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsNodeNextHopLinkGroup1.setStatus("mandatory")
_MscRtgVnsNodeNextHopLinkGroup2_Type = RowPointer
_MscRtgVnsNodeNextHopLinkGroup2_Object = MibTableColumn
mscRtgVnsNodeNextHopLinkGroup2 = _MscRtgVnsNodeNextHopLinkGroup2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10, 1, 3),
    _MscRtgVnsNodeNextHopLinkGroup2_Type()
)
mscRtgVnsNodeNextHopLinkGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsNodeNextHopLinkGroup2.setStatus("mandatory")
_MscRtgVnsLpStats_ObjectIdentity = ObjectIdentity
mscRtgVnsLpStats = _MscRtgVnsLpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3)
)
_MscRtgVnsLpStatsRowStatusTable_Object = MibTable
mscRtgVnsLpStatsRowStatusTable = _MscRtgVnsLpStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsRowStatusTable.setStatus("mandatory")
_MscRtgVnsLpStatsRowStatusEntry_Object = MibTableRow
mscRtgVnsLpStatsRowStatusEntry = _MscRtgVnsLpStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1)
)
mscRtgVnsLpStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsLpStatsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsRowStatusEntry.setStatus("mandatory")
_MscRtgVnsLpStatsRowStatus_Type = RowStatus
_MscRtgVnsLpStatsRowStatus_Object = MibTableColumn
mscRtgVnsLpStatsRowStatus = _MscRtgVnsLpStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1, 1),
    _MscRtgVnsLpStatsRowStatus_Type()
)
mscRtgVnsLpStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsRowStatus.setStatus("mandatory")
_MscRtgVnsLpStatsComponentName_Type = DisplayString
_MscRtgVnsLpStatsComponentName_Object = MibTableColumn
mscRtgVnsLpStatsComponentName = _MscRtgVnsLpStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1, 2),
    _MscRtgVnsLpStatsComponentName_Type()
)
mscRtgVnsLpStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsComponentName.setStatus("mandatory")
_MscRtgVnsLpStatsStorageType_Type = StorageType
_MscRtgVnsLpStatsStorageType_Object = MibTableColumn
mscRtgVnsLpStatsStorageType = _MscRtgVnsLpStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1, 4),
    _MscRtgVnsLpStatsStorageType_Type()
)
mscRtgVnsLpStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsStorageType.setStatus("mandatory")


class _MscRtgVnsLpStatsIndex_Type(Integer32):
    """Custom type mscRtgVnsLpStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscRtgVnsLpStatsIndex_Type.__name__ = "Integer32"
_MscRtgVnsLpStatsIndex_Object = MibTableColumn
mscRtgVnsLpStatsIndex = _MscRtgVnsLpStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1, 10),
    _MscRtgVnsLpStatsIndex_Type()
)
mscRtgVnsLpStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsIndex.setStatus("mandatory")
_MscRtgVnsLpStatsFwdStatsTable_Object = MibTable
mscRtgVnsLpStatsFwdStatsTable = _MscRtgVnsLpStatsFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsFwdStatsTable.setStatus("mandatory")
_MscRtgVnsLpStatsFwdStatsEntry_Object = MibTableRow
mscRtgVnsLpStatsFwdStatsEntry = _MscRtgVnsLpStatsFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1)
)
mscRtgVnsLpStatsFwdStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsLpStatsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsFwdStatsEntry.setStatus("mandatory")
_MscRtgVnsLpStatsUniRxPkts_Type = PassportCounter64
_MscRtgVnsLpStatsUniRxPkts_Object = MibTableColumn
mscRtgVnsLpStatsUniRxPkts = _MscRtgVnsLpStatsUniRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 1),
    _MscRtgVnsLpStatsUniRxPkts_Type()
)
mscRtgVnsLpStatsUniRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsUniRxPkts.setStatus("mandatory")
_MscRtgVnsLpStatsUniRxBytes_Type = PassportCounter64
_MscRtgVnsLpStatsUniRxBytes_Object = MibTableColumn
mscRtgVnsLpStatsUniRxBytes = _MscRtgVnsLpStatsUniRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 2),
    _MscRtgVnsLpStatsUniRxBytes_Type()
)
mscRtgVnsLpStatsUniRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsUniRxBytes.setStatus("mandatory")
_MscRtgVnsLpStatsUniRxDiscPkts_Type = PassportCounter64
_MscRtgVnsLpStatsUniRxDiscPkts_Object = MibTableColumn
mscRtgVnsLpStatsUniRxDiscPkts = _MscRtgVnsLpStatsUniRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 3),
    _MscRtgVnsLpStatsUniRxDiscPkts_Type()
)
mscRtgVnsLpStatsUniRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsUniRxDiscPkts.setStatus("mandatory")
_MscRtgVnsLpStatsUniTxPkts_Type = PassportCounter64
_MscRtgVnsLpStatsUniTxPkts_Object = MibTableColumn
mscRtgVnsLpStatsUniTxPkts = _MscRtgVnsLpStatsUniTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 4),
    _MscRtgVnsLpStatsUniTxPkts_Type()
)
mscRtgVnsLpStatsUniTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsUniTxPkts.setStatus("mandatory")
_MscRtgVnsLpStatsUniTxBytes_Type = PassportCounter64
_MscRtgVnsLpStatsUniTxBytes_Object = MibTableColumn
mscRtgVnsLpStatsUniTxBytes = _MscRtgVnsLpStatsUniTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 5),
    _MscRtgVnsLpStatsUniTxBytes_Type()
)
mscRtgVnsLpStatsUniTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsUniTxBytes.setStatus("mandatory")
_MscRtgVnsLpStatsUniTxDiscPkts_Type = PassportCounter64
_MscRtgVnsLpStatsUniTxDiscPkts_Object = MibTableColumn
mscRtgVnsLpStatsUniTxDiscPkts = _MscRtgVnsLpStatsUniTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 6),
    _MscRtgVnsLpStatsUniTxDiscPkts_Type()
)
mscRtgVnsLpStatsUniTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsUniTxDiscPkts.setStatus("mandatory")
_MscRtgVnsLpStatsMultiRxPkts_Type = PassportCounter64
_MscRtgVnsLpStatsMultiRxPkts_Object = MibTableColumn
mscRtgVnsLpStatsMultiRxPkts = _MscRtgVnsLpStatsMultiRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 7),
    _MscRtgVnsLpStatsMultiRxPkts_Type()
)
mscRtgVnsLpStatsMultiRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsMultiRxPkts.setStatus("mandatory")
_MscRtgVnsLpStatsMultiRxBytes_Type = PassportCounter64
_MscRtgVnsLpStatsMultiRxBytes_Object = MibTableColumn
mscRtgVnsLpStatsMultiRxBytes = _MscRtgVnsLpStatsMultiRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 8),
    _MscRtgVnsLpStatsMultiRxBytes_Type()
)
mscRtgVnsLpStatsMultiRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsMultiRxBytes.setStatus("mandatory")
_MscRtgVnsLpStatsMultiRxDiscPkts_Type = PassportCounter64
_MscRtgVnsLpStatsMultiRxDiscPkts_Object = MibTableColumn
mscRtgVnsLpStatsMultiRxDiscPkts = _MscRtgVnsLpStatsMultiRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 9),
    _MscRtgVnsLpStatsMultiRxDiscPkts_Type()
)
mscRtgVnsLpStatsMultiRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsMultiRxDiscPkts.setStatus("mandatory")
_MscRtgVnsLpStatsMultiTxPkts_Type = PassportCounter64
_MscRtgVnsLpStatsMultiTxPkts_Object = MibTableColumn
mscRtgVnsLpStatsMultiTxPkts = _MscRtgVnsLpStatsMultiTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 10),
    _MscRtgVnsLpStatsMultiTxPkts_Type()
)
mscRtgVnsLpStatsMultiTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsMultiTxPkts.setStatus("mandatory")
_MscRtgVnsLpStatsMultiTxBytes_Type = PassportCounter64
_MscRtgVnsLpStatsMultiTxBytes_Object = MibTableColumn
mscRtgVnsLpStatsMultiTxBytes = _MscRtgVnsLpStatsMultiTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 11),
    _MscRtgVnsLpStatsMultiTxBytes_Type()
)
mscRtgVnsLpStatsMultiTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsMultiTxBytes.setStatus("mandatory")
_MscRtgVnsLpStatsMultiTxDiscPkts_Type = PassportCounter64
_MscRtgVnsLpStatsMultiTxDiscPkts_Object = MibTableColumn
mscRtgVnsLpStatsMultiTxDiscPkts = _MscRtgVnsLpStatsMultiTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 12),
    _MscRtgVnsLpStatsMultiTxDiscPkts_Type()
)
mscRtgVnsLpStatsMultiTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsMultiTxDiscPkts.setStatus("mandatory")
_MscRtgVnsLpStatsTotalRxPkts_Type = PassportCounter64
_MscRtgVnsLpStatsTotalRxPkts_Object = MibTableColumn
mscRtgVnsLpStatsTotalRxPkts = _MscRtgVnsLpStatsTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 13),
    _MscRtgVnsLpStatsTotalRxPkts_Type()
)
mscRtgVnsLpStatsTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsTotalRxPkts.setStatus("mandatory")
_MscRtgVnsLpStatsTotalRxBytes_Type = PassportCounter64
_MscRtgVnsLpStatsTotalRxBytes_Object = MibTableColumn
mscRtgVnsLpStatsTotalRxBytes = _MscRtgVnsLpStatsTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 14),
    _MscRtgVnsLpStatsTotalRxBytes_Type()
)
mscRtgVnsLpStatsTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsTotalRxBytes.setStatus("mandatory")
_MscRtgVnsLpStatsTotalRxDiscPkts_Type = PassportCounter64
_MscRtgVnsLpStatsTotalRxDiscPkts_Object = MibTableColumn
mscRtgVnsLpStatsTotalRxDiscPkts = _MscRtgVnsLpStatsTotalRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 15),
    _MscRtgVnsLpStatsTotalRxDiscPkts_Type()
)
mscRtgVnsLpStatsTotalRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsTotalRxDiscPkts.setStatus("mandatory")
_MscRtgVnsLpStatsTotalTxPkts_Type = PassportCounter64
_MscRtgVnsLpStatsTotalTxPkts_Object = MibTableColumn
mscRtgVnsLpStatsTotalTxPkts = _MscRtgVnsLpStatsTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 16),
    _MscRtgVnsLpStatsTotalTxPkts_Type()
)
mscRtgVnsLpStatsTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsTotalTxPkts.setStatus("mandatory")
_MscRtgVnsLpStatsTotalTxBytes_Type = PassportCounter64
_MscRtgVnsLpStatsTotalTxBytes_Object = MibTableColumn
mscRtgVnsLpStatsTotalTxBytes = _MscRtgVnsLpStatsTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 17),
    _MscRtgVnsLpStatsTotalTxBytes_Type()
)
mscRtgVnsLpStatsTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsTotalTxBytes.setStatus("mandatory")
_MscRtgVnsLpStatsTotalTxDiscPkts_Type = PassportCounter64
_MscRtgVnsLpStatsTotalTxDiscPkts_Object = MibTableColumn
mscRtgVnsLpStatsTotalTxDiscPkts = _MscRtgVnsLpStatsTotalTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 18),
    _MscRtgVnsLpStatsTotalTxDiscPkts_Type()
)
mscRtgVnsLpStatsTotalTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsLpStatsTotalTxDiscPkts.setStatus("mandatory")
_MscRtgVnsProvTable_Object = MibTable
mscRtgVnsProvTable = _MscRtgVnsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10)
)
if mibBuilder.loadTexts:
    mscRtgVnsProvTable.setStatus("mandatory")
_MscRtgVnsProvEntry_Object = MibTableRow
mscRtgVnsProvEntry = _MscRtgVnsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1)
)
mscRtgVnsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsProvEntry.setStatus("mandatory")


class _MscRtgVnsLogicalNetworkNumber_Type(Unsigned32):
    """Custom type mscRtgVnsLogicalNetworkNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2047),
    )


_MscRtgVnsLogicalNetworkNumber_Type.__name__ = "Unsigned32"
_MscRtgVnsLogicalNetworkNumber_Object = MibTableColumn
mscRtgVnsLogicalNetworkNumber = _MscRtgVnsLogicalNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 1),
    _MscRtgVnsLogicalNetworkNumber_Type()
)
mscRtgVnsLogicalNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsLogicalNetworkNumber.setStatus("mandatory")
_MscRtgVnsLinkToProtocolPort_Type = Link
_MscRtgVnsLinkToProtocolPort_Object = MibTableColumn
mscRtgVnsLinkToProtocolPort = _MscRtgVnsLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 2),
    _MscRtgVnsLinkToProtocolPort_Type()
)
mscRtgVnsLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsLinkToProtocolPort.setStatus("mandatory")


class _MscRtgVnsMaximumTransmissionUnit_Type(Unsigned32):
    """Custom type mscRtgVnsMaximumTransmissionUnit based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 65535),
    )


_MscRtgVnsMaximumTransmissionUnit_Type.__name__ = "Unsigned32"
_MscRtgVnsMaximumTransmissionUnit_Object = MibTableColumn
mscRtgVnsMaximumTransmissionUnit = _MscRtgVnsMaximumTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 3),
    _MscRtgVnsMaximumTransmissionUnit_Type()
)
mscRtgVnsMaximumTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsMaximumTransmissionUnit.setStatus("mandatory")


class _MscRtgVnsLoadSharing_Type(Integer32):
    """Custom type mscRtgVnsLoadSharing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscRtgVnsLoadSharing_Type.__name__ = "Integer32"
_MscRtgVnsLoadSharing_Object = MibTableColumn
mscRtgVnsLoadSharing = _MscRtgVnsLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 4),
    _MscRtgVnsLoadSharing_Type()
)
mscRtgVnsLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsLoadSharing.setStatus("mandatory")


class _MscRtgVnsDiscardPriority_Type(Unsigned32):
    """Custom type mscRtgVnsDiscardPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscRtgVnsDiscardPriority_Type.__name__ = "Unsigned32"
_MscRtgVnsDiscardPriority_Object = MibTableColumn
mscRtgVnsDiscardPriority = _MscRtgVnsDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 5),
    _MscRtgVnsDiscardPriority_Type()
)
mscRtgVnsDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsDiscardPriority.setStatus("obsolete")
_MscRtgVnsIlsForwarder_Type = Link
_MscRtgVnsIlsForwarder_Object = MibTableColumn
mscRtgVnsIlsForwarder = _MscRtgVnsIlsForwarder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 6),
    _MscRtgVnsIlsForwarder_Type()
)
mscRtgVnsIlsForwarder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsIlsForwarder.setStatus("mandatory")
_MscRtgVnsIfEntryTable_Object = MibTable
mscRtgVnsIfEntryTable = _MscRtgVnsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 11)
)
if mibBuilder.loadTexts:
    mscRtgVnsIfEntryTable.setStatus("mandatory")
_MscRtgVnsIfEntryEntry_Object = MibTableRow
mscRtgVnsIfEntryEntry = _MscRtgVnsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 11, 1)
)
mscRtgVnsIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsIfEntryEntry.setStatus("mandatory")


class _MscRtgVnsIfAdminStatus_Type(Integer32):
    """Custom type mscRtgVnsIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscRtgVnsIfAdminStatus_Type.__name__ = "Integer32"
_MscRtgVnsIfAdminStatus_Object = MibTableColumn
mscRtgVnsIfAdminStatus = _MscRtgVnsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 11, 1, 1),
    _MscRtgVnsIfAdminStatus_Type()
)
mscRtgVnsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsIfAdminStatus.setStatus("mandatory")


class _MscRtgVnsIfIndex_Type(InterfaceIndex):
    """Custom type mscRtgVnsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscRtgVnsIfIndex_Type.__name__ = "InterfaceIndex"
_MscRtgVnsIfIndex_Object = MibTableColumn
mscRtgVnsIfIndex = _MscRtgVnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 11, 1, 2),
    _MscRtgVnsIfIndex_Type()
)
mscRtgVnsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsIfIndex.setStatus("mandatory")
_MscRtgVnsCidDataTable_Object = MibTable
mscRtgVnsCidDataTable = _MscRtgVnsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 12)
)
if mibBuilder.loadTexts:
    mscRtgVnsCidDataTable.setStatus("mandatory")
_MscRtgVnsCidDataEntry_Object = MibTableRow
mscRtgVnsCidDataEntry = _MscRtgVnsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 12, 1)
)
mscRtgVnsCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsCidDataEntry.setStatus("mandatory")


class _MscRtgVnsCustomerIdentifier_Type(Unsigned32):
    """Custom type mscRtgVnsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscRtgVnsCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscRtgVnsCustomerIdentifier_Object = MibTableColumn
mscRtgVnsCustomerIdentifier = _MscRtgVnsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 12, 1, 1),
    _MscRtgVnsCustomerIdentifier_Type()
)
mscRtgVnsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgVnsCustomerIdentifier.setStatus("mandatory")
_MscRtgVnsStateTable_Object = MibTable
mscRtgVnsStateTable = _MscRtgVnsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14)
)
if mibBuilder.loadTexts:
    mscRtgVnsStateTable.setStatus("mandatory")
_MscRtgVnsStateEntry_Object = MibTableRow
mscRtgVnsStateEntry = _MscRtgVnsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14, 1)
)
mscRtgVnsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsStateEntry.setStatus("mandatory")


class _MscRtgVnsAdminState_Type(Integer32):
    """Custom type mscRtgVnsAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscRtgVnsAdminState_Type.__name__ = "Integer32"
_MscRtgVnsAdminState_Object = MibTableColumn
mscRtgVnsAdminState = _MscRtgVnsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14, 1, 1),
    _MscRtgVnsAdminState_Type()
)
mscRtgVnsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsAdminState.setStatus("mandatory")


class _MscRtgVnsOperationalState_Type(Integer32):
    """Custom type mscRtgVnsOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscRtgVnsOperationalState_Type.__name__ = "Integer32"
_MscRtgVnsOperationalState_Object = MibTableColumn
mscRtgVnsOperationalState = _MscRtgVnsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14, 1, 2),
    _MscRtgVnsOperationalState_Type()
)
mscRtgVnsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsOperationalState.setStatus("mandatory")


class _MscRtgVnsUsageState_Type(Integer32):
    """Custom type mscRtgVnsUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscRtgVnsUsageState_Type.__name__ = "Integer32"
_MscRtgVnsUsageState_Object = MibTableColumn
mscRtgVnsUsageState = _MscRtgVnsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14, 1, 3),
    _MscRtgVnsUsageState_Type()
)
mscRtgVnsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsUsageState.setStatus("mandatory")
_MscRtgVnsOperTable_Object = MibTable
mscRtgVnsOperTable = _MscRtgVnsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 15)
)
if mibBuilder.loadTexts:
    mscRtgVnsOperTable.setStatus("mandatory")
_MscRtgVnsOperEntry_Object = MibTableRow
mscRtgVnsOperEntry = _MscRtgVnsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 15, 1)
)
mscRtgVnsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsOperEntry.setStatus("mandatory")


class _MscRtgVnsReportedThroughputMetric_Type(Unsigned32):
    """Custom type mscRtgVnsReportedThroughputMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgVnsReportedThroughputMetric_Type.__name__ = "Unsigned32"
_MscRtgVnsReportedThroughputMetric_Object = MibTableColumn
mscRtgVnsReportedThroughputMetric = _MscRtgVnsReportedThroughputMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 15, 1, 1),
    _MscRtgVnsReportedThroughputMetric_Type()
)
mscRtgVnsReportedThroughputMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsReportedThroughputMetric.setStatus("mandatory")
_MscRtgVnsFwdStatsTable_Object = MibTable
mscRtgVnsFwdStatsTable = _MscRtgVnsFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16)
)
if mibBuilder.loadTexts:
    mscRtgVnsFwdStatsTable.setStatus("mandatory")
_MscRtgVnsFwdStatsEntry_Object = MibTableRow
mscRtgVnsFwdStatsEntry = _MscRtgVnsFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1)
)
mscRtgVnsFwdStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgVnsFwdStatsEntry.setStatus("mandatory")
_MscRtgVnsUniRxPkts_Type = PassportCounter64
_MscRtgVnsUniRxPkts_Object = MibTableColumn
mscRtgVnsUniRxPkts = _MscRtgVnsUniRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 1),
    _MscRtgVnsUniRxPkts_Type()
)
mscRtgVnsUniRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsUniRxPkts.setStatus("mandatory")
_MscRtgVnsUniRxBytes_Type = PassportCounter64
_MscRtgVnsUniRxBytes_Object = MibTableColumn
mscRtgVnsUniRxBytes = _MscRtgVnsUniRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 2),
    _MscRtgVnsUniRxBytes_Type()
)
mscRtgVnsUniRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsUniRxBytes.setStatus("mandatory")
_MscRtgVnsUniRxDiscPkts_Type = PassportCounter64
_MscRtgVnsUniRxDiscPkts_Object = MibTableColumn
mscRtgVnsUniRxDiscPkts = _MscRtgVnsUniRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 3),
    _MscRtgVnsUniRxDiscPkts_Type()
)
mscRtgVnsUniRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsUniRxDiscPkts.setStatus("mandatory")
_MscRtgVnsUniTxPkts_Type = PassportCounter64
_MscRtgVnsUniTxPkts_Object = MibTableColumn
mscRtgVnsUniTxPkts = _MscRtgVnsUniTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 4),
    _MscRtgVnsUniTxPkts_Type()
)
mscRtgVnsUniTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsUniTxPkts.setStatus("mandatory")
_MscRtgVnsUniTxBytes_Type = PassportCounter64
_MscRtgVnsUniTxBytes_Object = MibTableColumn
mscRtgVnsUniTxBytes = _MscRtgVnsUniTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 5),
    _MscRtgVnsUniTxBytes_Type()
)
mscRtgVnsUniTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsUniTxBytes.setStatus("mandatory")
_MscRtgVnsUniTxDiscPkts_Type = PassportCounter64
_MscRtgVnsUniTxDiscPkts_Object = MibTableColumn
mscRtgVnsUniTxDiscPkts = _MscRtgVnsUniTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 6),
    _MscRtgVnsUniTxDiscPkts_Type()
)
mscRtgVnsUniTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsUniTxDiscPkts.setStatus("mandatory")
_MscRtgVnsMultiRxPkts_Type = PassportCounter64
_MscRtgVnsMultiRxPkts_Object = MibTableColumn
mscRtgVnsMultiRxPkts = _MscRtgVnsMultiRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 7),
    _MscRtgVnsMultiRxPkts_Type()
)
mscRtgVnsMultiRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsMultiRxPkts.setStatus("mandatory")
_MscRtgVnsMultiRxBytes_Type = PassportCounter64
_MscRtgVnsMultiRxBytes_Object = MibTableColumn
mscRtgVnsMultiRxBytes = _MscRtgVnsMultiRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 8),
    _MscRtgVnsMultiRxBytes_Type()
)
mscRtgVnsMultiRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsMultiRxBytes.setStatus("mandatory")
_MscRtgVnsMultiRxDiscPkts_Type = PassportCounter64
_MscRtgVnsMultiRxDiscPkts_Object = MibTableColumn
mscRtgVnsMultiRxDiscPkts = _MscRtgVnsMultiRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 9),
    _MscRtgVnsMultiRxDiscPkts_Type()
)
mscRtgVnsMultiRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsMultiRxDiscPkts.setStatus("mandatory")
_MscRtgVnsMultiTxPkts_Type = PassportCounter64
_MscRtgVnsMultiTxPkts_Object = MibTableColumn
mscRtgVnsMultiTxPkts = _MscRtgVnsMultiTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 10),
    _MscRtgVnsMultiTxPkts_Type()
)
mscRtgVnsMultiTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsMultiTxPkts.setStatus("mandatory")
_MscRtgVnsMultiTxBytes_Type = PassportCounter64
_MscRtgVnsMultiTxBytes_Object = MibTableColumn
mscRtgVnsMultiTxBytes = _MscRtgVnsMultiTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 11),
    _MscRtgVnsMultiTxBytes_Type()
)
mscRtgVnsMultiTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsMultiTxBytes.setStatus("mandatory")
_MscRtgVnsMultiTxDiscPkts_Type = PassportCounter64
_MscRtgVnsMultiTxDiscPkts_Object = MibTableColumn
mscRtgVnsMultiTxDiscPkts = _MscRtgVnsMultiTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 12),
    _MscRtgVnsMultiTxDiscPkts_Type()
)
mscRtgVnsMultiTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsMultiTxDiscPkts.setStatus("mandatory")
_MscRtgVnsTotalRxPkts_Type = PassportCounter64
_MscRtgVnsTotalRxPkts_Object = MibTableColumn
mscRtgVnsTotalRxPkts = _MscRtgVnsTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 13),
    _MscRtgVnsTotalRxPkts_Type()
)
mscRtgVnsTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsTotalRxPkts.setStatus("mandatory")
_MscRtgVnsTotalRxBytes_Type = PassportCounter64
_MscRtgVnsTotalRxBytes_Object = MibTableColumn
mscRtgVnsTotalRxBytes = _MscRtgVnsTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 14),
    _MscRtgVnsTotalRxBytes_Type()
)
mscRtgVnsTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsTotalRxBytes.setStatus("mandatory")
_MscRtgVnsTotalRxDiscPkts_Type = PassportCounter64
_MscRtgVnsTotalRxDiscPkts_Object = MibTableColumn
mscRtgVnsTotalRxDiscPkts = _MscRtgVnsTotalRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 15),
    _MscRtgVnsTotalRxDiscPkts_Type()
)
mscRtgVnsTotalRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsTotalRxDiscPkts.setStatus("mandatory")
_MscRtgVnsTotalTxPkts_Type = PassportCounter64
_MscRtgVnsTotalTxPkts_Object = MibTableColumn
mscRtgVnsTotalTxPkts = _MscRtgVnsTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 16),
    _MscRtgVnsTotalTxPkts_Type()
)
mscRtgVnsTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsTotalTxPkts.setStatus("mandatory")
_MscRtgVnsTotalTxBytes_Type = PassportCounter64
_MscRtgVnsTotalTxBytes_Object = MibTableColumn
mscRtgVnsTotalTxBytes = _MscRtgVnsTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 17),
    _MscRtgVnsTotalTxBytes_Type()
)
mscRtgVnsTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsTotalTxBytes.setStatus("mandatory")
_MscRtgVnsTotalTxDiscPkts_Type = PassportCounter64
_MscRtgVnsTotalTxDiscPkts_Object = MibTableColumn
mscRtgVnsTotalTxDiscPkts = _MscRtgVnsTotalTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 18),
    _MscRtgVnsTotalTxDiscPkts_Type()
)
mscRtgVnsTotalTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgVnsTotalTxDiscPkts.setStatus("mandatory")
_VnsMIB_ObjectIdentity = ObjectIdentity
vnsMIB = _VnsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20)
)
_VnsGroup_ObjectIdentity = ObjectIdentity
vnsGroup = _VnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 1)
)
_VnsGroupCA_ObjectIdentity = ObjectIdentity
vnsGroupCA = _VnsGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 1, 1)
)
_VnsGroupCA02_ObjectIdentity = ObjectIdentity
vnsGroupCA02 = _VnsGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 1, 1, 3)
)
_VnsGroupCA02A_ObjectIdentity = ObjectIdentity
vnsGroupCA02A = _VnsGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 1, 1, 3, 2)
)
_VnsCapabilities_ObjectIdentity = ObjectIdentity
vnsCapabilities = _VnsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 3)
)
_VnsCapabilitiesCA_ObjectIdentity = ObjectIdentity
vnsCapabilitiesCA = _VnsCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 3, 1)
)
_VnsCapabilitiesCA02_ObjectIdentity = ObjectIdentity
vnsCapabilitiesCA02 = _VnsCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 3, 1, 3)
)
_VnsCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
vnsCapabilitiesCA02A = _VnsCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VnsMIB",
    **{"mscRtgVns": mscRtgVns,
       "mscRtgVnsRowStatusTable": mscRtgVnsRowStatusTable,
       "mscRtgVnsRowStatusEntry": mscRtgVnsRowStatusEntry,
       "mscRtgVnsRowStatus": mscRtgVnsRowStatus,
       "mscRtgVnsComponentName": mscRtgVnsComponentName,
       "mscRtgVnsStorageType": mscRtgVnsStorageType,
       "mscRtgVnsIndex": mscRtgVnsIndex,
       "mscRtgVnsNode": mscRtgVnsNode,
       "mscRtgVnsNodeRowStatusTable": mscRtgVnsNodeRowStatusTable,
       "mscRtgVnsNodeRowStatusEntry": mscRtgVnsNodeRowStatusEntry,
       "mscRtgVnsNodeRowStatus": mscRtgVnsNodeRowStatus,
       "mscRtgVnsNodeComponentName": mscRtgVnsNodeComponentName,
       "mscRtgVnsNodeStorageType": mscRtgVnsNodeStorageType,
       "mscRtgVnsNodeIndex": mscRtgVnsNodeIndex,
       "mscRtgVnsNodeOperTable": mscRtgVnsNodeOperTable,
       "mscRtgVnsNodeOperEntry": mscRtgVnsNodeOperEntry,
       "mscRtgVnsNodeMetric": mscRtgVnsNodeMetric,
       "mscRtgVnsNodeNextHopLinkGroup1": mscRtgVnsNodeNextHopLinkGroup1,
       "mscRtgVnsNodeNextHopLinkGroup2": mscRtgVnsNodeNextHopLinkGroup2,
       "mscRtgVnsLpStats": mscRtgVnsLpStats,
       "mscRtgVnsLpStatsRowStatusTable": mscRtgVnsLpStatsRowStatusTable,
       "mscRtgVnsLpStatsRowStatusEntry": mscRtgVnsLpStatsRowStatusEntry,
       "mscRtgVnsLpStatsRowStatus": mscRtgVnsLpStatsRowStatus,
       "mscRtgVnsLpStatsComponentName": mscRtgVnsLpStatsComponentName,
       "mscRtgVnsLpStatsStorageType": mscRtgVnsLpStatsStorageType,
       "mscRtgVnsLpStatsIndex": mscRtgVnsLpStatsIndex,
       "mscRtgVnsLpStatsFwdStatsTable": mscRtgVnsLpStatsFwdStatsTable,
       "mscRtgVnsLpStatsFwdStatsEntry": mscRtgVnsLpStatsFwdStatsEntry,
       "mscRtgVnsLpStatsUniRxPkts": mscRtgVnsLpStatsUniRxPkts,
       "mscRtgVnsLpStatsUniRxBytes": mscRtgVnsLpStatsUniRxBytes,
       "mscRtgVnsLpStatsUniRxDiscPkts": mscRtgVnsLpStatsUniRxDiscPkts,
       "mscRtgVnsLpStatsUniTxPkts": mscRtgVnsLpStatsUniTxPkts,
       "mscRtgVnsLpStatsUniTxBytes": mscRtgVnsLpStatsUniTxBytes,
       "mscRtgVnsLpStatsUniTxDiscPkts": mscRtgVnsLpStatsUniTxDiscPkts,
       "mscRtgVnsLpStatsMultiRxPkts": mscRtgVnsLpStatsMultiRxPkts,
       "mscRtgVnsLpStatsMultiRxBytes": mscRtgVnsLpStatsMultiRxBytes,
       "mscRtgVnsLpStatsMultiRxDiscPkts": mscRtgVnsLpStatsMultiRxDiscPkts,
       "mscRtgVnsLpStatsMultiTxPkts": mscRtgVnsLpStatsMultiTxPkts,
       "mscRtgVnsLpStatsMultiTxBytes": mscRtgVnsLpStatsMultiTxBytes,
       "mscRtgVnsLpStatsMultiTxDiscPkts": mscRtgVnsLpStatsMultiTxDiscPkts,
       "mscRtgVnsLpStatsTotalRxPkts": mscRtgVnsLpStatsTotalRxPkts,
       "mscRtgVnsLpStatsTotalRxBytes": mscRtgVnsLpStatsTotalRxBytes,
       "mscRtgVnsLpStatsTotalRxDiscPkts": mscRtgVnsLpStatsTotalRxDiscPkts,
       "mscRtgVnsLpStatsTotalTxPkts": mscRtgVnsLpStatsTotalTxPkts,
       "mscRtgVnsLpStatsTotalTxBytes": mscRtgVnsLpStatsTotalTxBytes,
       "mscRtgVnsLpStatsTotalTxDiscPkts": mscRtgVnsLpStatsTotalTxDiscPkts,
       "mscRtgVnsProvTable": mscRtgVnsProvTable,
       "mscRtgVnsProvEntry": mscRtgVnsProvEntry,
       "mscRtgVnsLogicalNetworkNumber": mscRtgVnsLogicalNetworkNumber,
       "mscRtgVnsLinkToProtocolPort": mscRtgVnsLinkToProtocolPort,
       "mscRtgVnsMaximumTransmissionUnit": mscRtgVnsMaximumTransmissionUnit,
       "mscRtgVnsLoadSharing": mscRtgVnsLoadSharing,
       "mscRtgVnsDiscardPriority": mscRtgVnsDiscardPriority,
       "mscRtgVnsIlsForwarder": mscRtgVnsIlsForwarder,
       "mscRtgVnsIfEntryTable": mscRtgVnsIfEntryTable,
       "mscRtgVnsIfEntryEntry": mscRtgVnsIfEntryEntry,
       "mscRtgVnsIfAdminStatus": mscRtgVnsIfAdminStatus,
       "mscRtgVnsIfIndex": mscRtgVnsIfIndex,
       "mscRtgVnsCidDataTable": mscRtgVnsCidDataTable,
       "mscRtgVnsCidDataEntry": mscRtgVnsCidDataEntry,
       "mscRtgVnsCustomerIdentifier": mscRtgVnsCustomerIdentifier,
       "mscRtgVnsStateTable": mscRtgVnsStateTable,
       "mscRtgVnsStateEntry": mscRtgVnsStateEntry,
       "mscRtgVnsAdminState": mscRtgVnsAdminState,
       "mscRtgVnsOperationalState": mscRtgVnsOperationalState,
       "mscRtgVnsUsageState": mscRtgVnsUsageState,
       "mscRtgVnsOperTable": mscRtgVnsOperTable,
       "mscRtgVnsOperEntry": mscRtgVnsOperEntry,
       "mscRtgVnsReportedThroughputMetric": mscRtgVnsReportedThroughputMetric,
       "mscRtgVnsFwdStatsTable": mscRtgVnsFwdStatsTable,
       "mscRtgVnsFwdStatsEntry": mscRtgVnsFwdStatsEntry,
       "mscRtgVnsUniRxPkts": mscRtgVnsUniRxPkts,
       "mscRtgVnsUniRxBytes": mscRtgVnsUniRxBytes,
       "mscRtgVnsUniRxDiscPkts": mscRtgVnsUniRxDiscPkts,
       "mscRtgVnsUniTxPkts": mscRtgVnsUniTxPkts,
       "mscRtgVnsUniTxBytes": mscRtgVnsUniTxBytes,
       "mscRtgVnsUniTxDiscPkts": mscRtgVnsUniTxDiscPkts,
       "mscRtgVnsMultiRxPkts": mscRtgVnsMultiRxPkts,
       "mscRtgVnsMultiRxBytes": mscRtgVnsMultiRxBytes,
       "mscRtgVnsMultiRxDiscPkts": mscRtgVnsMultiRxDiscPkts,
       "mscRtgVnsMultiTxPkts": mscRtgVnsMultiTxPkts,
       "mscRtgVnsMultiTxBytes": mscRtgVnsMultiTxBytes,
       "mscRtgVnsMultiTxDiscPkts": mscRtgVnsMultiTxDiscPkts,
       "mscRtgVnsTotalRxPkts": mscRtgVnsTotalRxPkts,
       "mscRtgVnsTotalRxBytes": mscRtgVnsTotalRxBytes,
       "mscRtgVnsTotalRxDiscPkts": mscRtgVnsTotalRxDiscPkts,
       "mscRtgVnsTotalTxPkts": mscRtgVnsTotalTxPkts,
       "mscRtgVnsTotalTxBytes": mscRtgVnsTotalTxBytes,
       "mscRtgVnsTotalTxDiscPkts": mscRtgVnsTotalTxDiscPkts,
       "vnsMIB": vnsMIB,
       "vnsGroup": vnsGroup,
       "vnsGroupCA": vnsGroupCA,
       "vnsGroupCA02": vnsGroupCA02,
       "vnsGroupCA02A": vnsGroupCA02A,
       "vnsCapabilities": vnsCapabilities,
       "vnsCapabilitiesCA": vnsCapabilitiesCA,
       "vnsCapabilitiesCA02": vnsCapabilitiesCA02,
       "vnsCapabilitiesCA02A": vnsCapabilitiesCA02A}
)
