# SNMP MIB module (Nortel-Magellan-Passport-VnsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VnsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:39 2024
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

(rtg,
 rtgIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-BaseRoutingMIB",
    "rtg",
    "rtgIndex")

(DisplayString,
 Integer32,
 InterfaceIndex,
 PassportCounter64,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "PassportCounter64",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 Link) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiStringIndex",
    "Link")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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

_RtgVns_ObjectIdentity = ObjectIdentity
rtgVns = _RtgVns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3)
)
_RtgVnsRowStatusTable_Object = MibTable
rtgVnsRowStatusTable = _RtgVnsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 1)
)
if mibBuilder.loadTexts:
    rtgVnsRowStatusTable.setStatus("mandatory")
_RtgVnsRowStatusEntry_Object = MibTableRow
rtgVnsRowStatusEntry = _RtgVnsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 1, 1)
)
rtgVnsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsRowStatusEntry.setStatus("mandatory")
_RtgVnsRowStatus_Type = RowStatus
_RtgVnsRowStatus_Object = MibTableColumn
rtgVnsRowStatus = _RtgVnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 1, 1, 1),
    _RtgVnsRowStatus_Type()
)
rtgVnsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsRowStatus.setStatus("mandatory")
_RtgVnsComponentName_Type = DisplayString
_RtgVnsComponentName_Object = MibTableColumn
rtgVnsComponentName = _RtgVnsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 1, 1, 2),
    _RtgVnsComponentName_Type()
)
rtgVnsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsComponentName.setStatus("mandatory")
_RtgVnsStorageType_Type = StorageType
_RtgVnsStorageType_Object = MibTableColumn
rtgVnsStorageType = _RtgVnsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 1, 1, 4),
    _RtgVnsStorageType_Type()
)
rtgVnsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsStorageType.setStatus("mandatory")


class _RtgVnsIndex_Type(AsciiStringIndex):
    """Custom type rtgVnsIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_RtgVnsIndex_Type.__name__ = "AsciiStringIndex"
_RtgVnsIndex_Object = MibTableColumn
rtgVnsIndex = _RtgVnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 1, 1, 10),
    _RtgVnsIndex_Type()
)
rtgVnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgVnsIndex.setStatus("mandatory")
_RtgVnsNode_ObjectIdentity = ObjectIdentity
rtgVnsNode = _RtgVnsNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2)
)
_RtgVnsNodeRowStatusTable_Object = MibTable
rtgVnsNodeRowStatusTable = _RtgVnsNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 1)
)
if mibBuilder.loadTexts:
    rtgVnsNodeRowStatusTable.setStatus("mandatory")
_RtgVnsNodeRowStatusEntry_Object = MibTableRow
rtgVnsNodeRowStatusEntry = _RtgVnsNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 1, 1)
)
rtgVnsNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsNodeIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsNodeRowStatusEntry.setStatus("mandatory")
_RtgVnsNodeRowStatus_Type = RowStatus
_RtgVnsNodeRowStatus_Object = MibTableColumn
rtgVnsNodeRowStatus = _RtgVnsNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 1, 1, 1),
    _RtgVnsNodeRowStatus_Type()
)
rtgVnsNodeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsNodeRowStatus.setStatus("mandatory")
_RtgVnsNodeComponentName_Type = DisplayString
_RtgVnsNodeComponentName_Object = MibTableColumn
rtgVnsNodeComponentName = _RtgVnsNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 1, 1, 2),
    _RtgVnsNodeComponentName_Type()
)
rtgVnsNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsNodeComponentName.setStatus("mandatory")
_RtgVnsNodeStorageType_Type = StorageType
_RtgVnsNodeStorageType_Object = MibTableColumn
rtgVnsNodeStorageType = _RtgVnsNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 1, 1, 4),
    _RtgVnsNodeStorageType_Type()
)
rtgVnsNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsNodeStorageType.setStatus("mandatory")


class _RtgVnsNodeIndex_Type(Integer32):
    """Custom type rtgVnsNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RtgVnsNodeIndex_Type.__name__ = "Integer32"
_RtgVnsNodeIndex_Object = MibTableColumn
rtgVnsNodeIndex = _RtgVnsNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 1, 1, 10),
    _RtgVnsNodeIndex_Type()
)
rtgVnsNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgVnsNodeIndex.setStatus("mandatory")
_RtgVnsNodeOperTable_Object = MibTable
rtgVnsNodeOperTable = _RtgVnsNodeOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 10)
)
if mibBuilder.loadTexts:
    rtgVnsNodeOperTable.setStatus("mandatory")
_RtgVnsNodeOperEntry_Object = MibTableRow
rtgVnsNodeOperEntry = _RtgVnsNodeOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 10, 1)
)
rtgVnsNodeOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsNodeIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsNodeOperEntry.setStatus("mandatory")


class _RtgVnsNodeMetric_Type(Unsigned32):
    """Custom type rtgVnsNodeMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgVnsNodeMetric_Type.__name__ = "Unsigned32"
_RtgVnsNodeMetric_Object = MibTableColumn
rtgVnsNodeMetric = _RtgVnsNodeMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 10, 1, 1),
    _RtgVnsNodeMetric_Type()
)
rtgVnsNodeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsNodeMetric.setStatus("mandatory")
_RtgVnsNodeNextHopLinkGroup1_Type = RowPointer
_RtgVnsNodeNextHopLinkGroup1_Object = MibTableColumn
rtgVnsNodeNextHopLinkGroup1 = _RtgVnsNodeNextHopLinkGroup1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 10, 1, 2),
    _RtgVnsNodeNextHopLinkGroup1_Type()
)
rtgVnsNodeNextHopLinkGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsNodeNextHopLinkGroup1.setStatus("mandatory")
_RtgVnsNodeNextHopLinkGroup2_Type = RowPointer
_RtgVnsNodeNextHopLinkGroup2_Object = MibTableColumn
rtgVnsNodeNextHopLinkGroup2 = _RtgVnsNodeNextHopLinkGroup2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 2, 10, 1, 3),
    _RtgVnsNodeNextHopLinkGroup2_Type()
)
rtgVnsNodeNextHopLinkGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsNodeNextHopLinkGroup2.setStatus("mandatory")
_RtgVnsLpStats_ObjectIdentity = ObjectIdentity
rtgVnsLpStats = _RtgVnsLpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3)
)
_RtgVnsLpStatsRowStatusTable_Object = MibTable
rtgVnsLpStatsRowStatusTable = _RtgVnsLpStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 1)
)
if mibBuilder.loadTexts:
    rtgVnsLpStatsRowStatusTable.setStatus("mandatory")
_RtgVnsLpStatsRowStatusEntry_Object = MibTableRow
rtgVnsLpStatsRowStatusEntry = _RtgVnsLpStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 1, 1)
)
rtgVnsLpStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsLpStatsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsLpStatsRowStatusEntry.setStatus("mandatory")
_RtgVnsLpStatsRowStatus_Type = RowStatus
_RtgVnsLpStatsRowStatus_Object = MibTableColumn
rtgVnsLpStatsRowStatus = _RtgVnsLpStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 1, 1, 1),
    _RtgVnsLpStatsRowStatus_Type()
)
rtgVnsLpStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsRowStatus.setStatus("mandatory")
_RtgVnsLpStatsComponentName_Type = DisplayString
_RtgVnsLpStatsComponentName_Object = MibTableColumn
rtgVnsLpStatsComponentName = _RtgVnsLpStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 1, 1, 2),
    _RtgVnsLpStatsComponentName_Type()
)
rtgVnsLpStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsComponentName.setStatus("mandatory")
_RtgVnsLpStatsStorageType_Type = StorageType
_RtgVnsLpStatsStorageType_Object = MibTableColumn
rtgVnsLpStatsStorageType = _RtgVnsLpStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 1, 1, 4),
    _RtgVnsLpStatsStorageType_Type()
)
rtgVnsLpStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsStorageType.setStatus("mandatory")


class _RtgVnsLpStatsIndex_Type(Integer32):
    """Custom type rtgVnsLpStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RtgVnsLpStatsIndex_Type.__name__ = "Integer32"
_RtgVnsLpStatsIndex_Object = MibTableColumn
rtgVnsLpStatsIndex = _RtgVnsLpStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 1, 1, 10),
    _RtgVnsLpStatsIndex_Type()
)
rtgVnsLpStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgVnsLpStatsIndex.setStatus("mandatory")
_RtgVnsLpStatsFwdStatsTable_Object = MibTable
rtgVnsLpStatsFwdStatsTable = _RtgVnsLpStatsFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2)
)
if mibBuilder.loadTexts:
    rtgVnsLpStatsFwdStatsTable.setStatus("mandatory")
_RtgVnsLpStatsFwdStatsEntry_Object = MibTableRow
rtgVnsLpStatsFwdStatsEntry = _RtgVnsLpStatsFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1)
)
rtgVnsLpStatsFwdStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsLpStatsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsLpStatsFwdStatsEntry.setStatus("mandatory")
_RtgVnsLpStatsUniRxPkts_Type = PassportCounter64
_RtgVnsLpStatsUniRxPkts_Object = MibTableColumn
rtgVnsLpStatsUniRxPkts = _RtgVnsLpStatsUniRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 1),
    _RtgVnsLpStatsUniRxPkts_Type()
)
rtgVnsLpStatsUniRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsUniRxPkts.setStatus("mandatory")
_RtgVnsLpStatsUniRxBytes_Type = PassportCounter64
_RtgVnsLpStatsUniRxBytes_Object = MibTableColumn
rtgVnsLpStatsUniRxBytes = _RtgVnsLpStatsUniRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 2),
    _RtgVnsLpStatsUniRxBytes_Type()
)
rtgVnsLpStatsUniRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsUniRxBytes.setStatus("mandatory")
_RtgVnsLpStatsUniRxDiscPkts_Type = PassportCounter64
_RtgVnsLpStatsUniRxDiscPkts_Object = MibTableColumn
rtgVnsLpStatsUniRxDiscPkts = _RtgVnsLpStatsUniRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 3),
    _RtgVnsLpStatsUniRxDiscPkts_Type()
)
rtgVnsLpStatsUniRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsUniRxDiscPkts.setStatus("mandatory")
_RtgVnsLpStatsUniTxPkts_Type = PassportCounter64
_RtgVnsLpStatsUniTxPkts_Object = MibTableColumn
rtgVnsLpStatsUniTxPkts = _RtgVnsLpStatsUniTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 4),
    _RtgVnsLpStatsUniTxPkts_Type()
)
rtgVnsLpStatsUniTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsUniTxPkts.setStatus("mandatory")
_RtgVnsLpStatsUniTxBytes_Type = PassportCounter64
_RtgVnsLpStatsUniTxBytes_Object = MibTableColumn
rtgVnsLpStatsUniTxBytes = _RtgVnsLpStatsUniTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 5),
    _RtgVnsLpStatsUniTxBytes_Type()
)
rtgVnsLpStatsUniTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsUniTxBytes.setStatus("mandatory")
_RtgVnsLpStatsUniTxDiscPkts_Type = PassportCounter64
_RtgVnsLpStatsUniTxDiscPkts_Object = MibTableColumn
rtgVnsLpStatsUniTxDiscPkts = _RtgVnsLpStatsUniTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 6),
    _RtgVnsLpStatsUniTxDiscPkts_Type()
)
rtgVnsLpStatsUniTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsUniTxDiscPkts.setStatus("mandatory")
_RtgVnsLpStatsMultiRxPkts_Type = PassportCounter64
_RtgVnsLpStatsMultiRxPkts_Object = MibTableColumn
rtgVnsLpStatsMultiRxPkts = _RtgVnsLpStatsMultiRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 7),
    _RtgVnsLpStatsMultiRxPkts_Type()
)
rtgVnsLpStatsMultiRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsMultiRxPkts.setStatus("mandatory")
_RtgVnsLpStatsMultiRxBytes_Type = PassportCounter64
_RtgVnsLpStatsMultiRxBytes_Object = MibTableColumn
rtgVnsLpStatsMultiRxBytes = _RtgVnsLpStatsMultiRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 8),
    _RtgVnsLpStatsMultiRxBytes_Type()
)
rtgVnsLpStatsMultiRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsMultiRxBytes.setStatus("mandatory")
_RtgVnsLpStatsMultiRxDiscPkts_Type = PassportCounter64
_RtgVnsLpStatsMultiRxDiscPkts_Object = MibTableColumn
rtgVnsLpStatsMultiRxDiscPkts = _RtgVnsLpStatsMultiRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 9),
    _RtgVnsLpStatsMultiRxDiscPkts_Type()
)
rtgVnsLpStatsMultiRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsMultiRxDiscPkts.setStatus("mandatory")
_RtgVnsLpStatsMultiTxPkts_Type = PassportCounter64
_RtgVnsLpStatsMultiTxPkts_Object = MibTableColumn
rtgVnsLpStatsMultiTxPkts = _RtgVnsLpStatsMultiTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 10),
    _RtgVnsLpStatsMultiTxPkts_Type()
)
rtgVnsLpStatsMultiTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsMultiTxPkts.setStatus("mandatory")
_RtgVnsLpStatsMultiTxBytes_Type = PassportCounter64
_RtgVnsLpStatsMultiTxBytes_Object = MibTableColumn
rtgVnsLpStatsMultiTxBytes = _RtgVnsLpStatsMultiTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 11),
    _RtgVnsLpStatsMultiTxBytes_Type()
)
rtgVnsLpStatsMultiTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsMultiTxBytes.setStatus("mandatory")
_RtgVnsLpStatsMultiTxDiscPkts_Type = PassportCounter64
_RtgVnsLpStatsMultiTxDiscPkts_Object = MibTableColumn
rtgVnsLpStatsMultiTxDiscPkts = _RtgVnsLpStatsMultiTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 12),
    _RtgVnsLpStatsMultiTxDiscPkts_Type()
)
rtgVnsLpStatsMultiTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsMultiTxDiscPkts.setStatus("mandatory")
_RtgVnsLpStatsTotalRxPkts_Type = PassportCounter64
_RtgVnsLpStatsTotalRxPkts_Object = MibTableColumn
rtgVnsLpStatsTotalRxPkts = _RtgVnsLpStatsTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 13),
    _RtgVnsLpStatsTotalRxPkts_Type()
)
rtgVnsLpStatsTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsTotalRxPkts.setStatus("mandatory")
_RtgVnsLpStatsTotalRxBytes_Type = PassportCounter64
_RtgVnsLpStatsTotalRxBytes_Object = MibTableColumn
rtgVnsLpStatsTotalRxBytes = _RtgVnsLpStatsTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 14),
    _RtgVnsLpStatsTotalRxBytes_Type()
)
rtgVnsLpStatsTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsTotalRxBytes.setStatus("mandatory")
_RtgVnsLpStatsTotalRxDiscPkts_Type = PassportCounter64
_RtgVnsLpStatsTotalRxDiscPkts_Object = MibTableColumn
rtgVnsLpStatsTotalRxDiscPkts = _RtgVnsLpStatsTotalRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 15),
    _RtgVnsLpStatsTotalRxDiscPkts_Type()
)
rtgVnsLpStatsTotalRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsTotalRxDiscPkts.setStatus("mandatory")
_RtgVnsLpStatsTotalTxPkts_Type = PassportCounter64
_RtgVnsLpStatsTotalTxPkts_Object = MibTableColumn
rtgVnsLpStatsTotalTxPkts = _RtgVnsLpStatsTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 16),
    _RtgVnsLpStatsTotalTxPkts_Type()
)
rtgVnsLpStatsTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsTotalTxPkts.setStatus("mandatory")
_RtgVnsLpStatsTotalTxBytes_Type = PassportCounter64
_RtgVnsLpStatsTotalTxBytes_Object = MibTableColumn
rtgVnsLpStatsTotalTxBytes = _RtgVnsLpStatsTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 17),
    _RtgVnsLpStatsTotalTxBytes_Type()
)
rtgVnsLpStatsTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsTotalTxBytes.setStatus("mandatory")
_RtgVnsLpStatsTotalTxDiscPkts_Type = PassportCounter64
_RtgVnsLpStatsTotalTxDiscPkts_Object = MibTableColumn
rtgVnsLpStatsTotalTxDiscPkts = _RtgVnsLpStatsTotalTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 3, 2, 1, 18),
    _RtgVnsLpStatsTotalTxDiscPkts_Type()
)
rtgVnsLpStatsTotalTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsLpStatsTotalTxDiscPkts.setStatus("mandatory")
_RtgVnsProvTable_Object = MibTable
rtgVnsProvTable = _RtgVnsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 10)
)
if mibBuilder.loadTexts:
    rtgVnsProvTable.setStatus("mandatory")
_RtgVnsProvEntry_Object = MibTableRow
rtgVnsProvEntry = _RtgVnsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 10, 1)
)
rtgVnsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsProvEntry.setStatus("mandatory")


class _RtgVnsLogicalNetworkNumber_Type(Unsigned32):
    """Custom type rtgVnsLogicalNetworkNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2047),
    )


_RtgVnsLogicalNetworkNumber_Type.__name__ = "Unsigned32"
_RtgVnsLogicalNetworkNumber_Object = MibTableColumn
rtgVnsLogicalNetworkNumber = _RtgVnsLogicalNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 10, 1, 1),
    _RtgVnsLogicalNetworkNumber_Type()
)
rtgVnsLogicalNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsLogicalNetworkNumber.setStatus("mandatory")
_RtgVnsLinkToProtocolPort_Type = Link
_RtgVnsLinkToProtocolPort_Object = MibTableColumn
rtgVnsLinkToProtocolPort = _RtgVnsLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 10, 1, 2),
    _RtgVnsLinkToProtocolPort_Type()
)
rtgVnsLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsLinkToProtocolPort.setStatus("mandatory")


class _RtgVnsMaximumTransmissionUnit_Type(Unsigned32):
    """Custom type rtgVnsMaximumTransmissionUnit based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 65535),
    )


_RtgVnsMaximumTransmissionUnit_Type.__name__ = "Unsigned32"
_RtgVnsMaximumTransmissionUnit_Object = MibTableColumn
rtgVnsMaximumTransmissionUnit = _RtgVnsMaximumTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 10, 1, 3),
    _RtgVnsMaximumTransmissionUnit_Type()
)
rtgVnsMaximumTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsMaximumTransmissionUnit.setStatus("mandatory")


class _RtgVnsLoadSharing_Type(Integer32):
    """Custom type rtgVnsLoadSharing based on Integer32"""
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


_RtgVnsLoadSharing_Type.__name__ = "Integer32"
_RtgVnsLoadSharing_Object = MibTableColumn
rtgVnsLoadSharing = _RtgVnsLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 10, 1, 4),
    _RtgVnsLoadSharing_Type()
)
rtgVnsLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsLoadSharing.setStatus("mandatory")


class _RtgVnsDiscardPriority_Type(Unsigned32):
    """Custom type rtgVnsDiscardPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_RtgVnsDiscardPriority_Type.__name__ = "Unsigned32"
_RtgVnsDiscardPriority_Object = MibTableColumn
rtgVnsDiscardPriority = _RtgVnsDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 10, 1, 5),
    _RtgVnsDiscardPriority_Type()
)
rtgVnsDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsDiscardPriority.setStatus("obsolete")
_RtgVnsIlsForwarder_Type = Link
_RtgVnsIlsForwarder_Object = MibTableColumn
rtgVnsIlsForwarder = _RtgVnsIlsForwarder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 10, 1, 6),
    _RtgVnsIlsForwarder_Type()
)
rtgVnsIlsForwarder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsIlsForwarder.setStatus("mandatory")
_RtgVnsIfEntryTable_Object = MibTable
rtgVnsIfEntryTable = _RtgVnsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 11)
)
if mibBuilder.loadTexts:
    rtgVnsIfEntryTable.setStatus("mandatory")
_RtgVnsIfEntryEntry_Object = MibTableRow
rtgVnsIfEntryEntry = _RtgVnsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 11, 1)
)
rtgVnsIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsIfEntryEntry.setStatus("mandatory")


class _RtgVnsIfAdminStatus_Type(Integer32):
    """Custom type rtgVnsIfAdminStatus based on Integer32"""
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


_RtgVnsIfAdminStatus_Type.__name__ = "Integer32"
_RtgVnsIfAdminStatus_Object = MibTableColumn
rtgVnsIfAdminStatus = _RtgVnsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 11, 1, 1),
    _RtgVnsIfAdminStatus_Type()
)
rtgVnsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsIfAdminStatus.setStatus("mandatory")


class _RtgVnsIfIndex_Type(InterfaceIndex):
    """Custom type rtgVnsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtgVnsIfIndex_Type.__name__ = "InterfaceIndex"
_RtgVnsIfIndex_Object = MibTableColumn
rtgVnsIfIndex = _RtgVnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 11, 1, 2),
    _RtgVnsIfIndex_Type()
)
rtgVnsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsIfIndex.setStatus("mandatory")
_RtgVnsCidDataTable_Object = MibTable
rtgVnsCidDataTable = _RtgVnsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 12)
)
if mibBuilder.loadTexts:
    rtgVnsCidDataTable.setStatus("mandatory")
_RtgVnsCidDataEntry_Object = MibTableRow
rtgVnsCidDataEntry = _RtgVnsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 12, 1)
)
rtgVnsCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsCidDataEntry.setStatus("mandatory")


class _RtgVnsCustomerIdentifier_Type(Unsigned32):
    """Custom type rtgVnsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_RtgVnsCustomerIdentifier_Type.__name__ = "Unsigned32"
_RtgVnsCustomerIdentifier_Object = MibTableColumn
rtgVnsCustomerIdentifier = _RtgVnsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 12, 1, 1),
    _RtgVnsCustomerIdentifier_Type()
)
rtgVnsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgVnsCustomerIdentifier.setStatus("mandatory")
_RtgVnsStateTable_Object = MibTable
rtgVnsStateTable = _RtgVnsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 14)
)
if mibBuilder.loadTexts:
    rtgVnsStateTable.setStatus("mandatory")
_RtgVnsStateEntry_Object = MibTableRow
rtgVnsStateEntry = _RtgVnsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 14, 1)
)
rtgVnsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsStateEntry.setStatus("mandatory")


class _RtgVnsAdminState_Type(Integer32):
    """Custom type rtgVnsAdminState based on Integer32"""
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


_RtgVnsAdminState_Type.__name__ = "Integer32"
_RtgVnsAdminState_Object = MibTableColumn
rtgVnsAdminState = _RtgVnsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 14, 1, 1),
    _RtgVnsAdminState_Type()
)
rtgVnsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsAdminState.setStatus("mandatory")


class _RtgVnsOperationalState_Type(Integer32):
    """Custom type rtgVnsOperationalState based on Integer32"""
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


_RtgVnsOperationalState_Type.__name__ = "Integer32"
_RtgVnsOperationalState_Object = MibTableColumn
rtgVnsOperationalState = _RtgVnsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 14, 1, 2),
    _RtgVnsOperationalState_Type()
)
rtgVnsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsOperationalState.setStatus("mandatory")


class _RtgVnsUsageState_Type(Integer32):
    """Custom type rtgVnsUsageState based on Integer32"""
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


_RtgVnsUsageState_Type.__name__ = "Integer32"
_RtgVnsUsageState_Object = MibTableColumn
rtgVnsUsageState = _RtgVnsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 14, 1, 3),
    _RtgVnsUsageState_Type()
)
rtgVnsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsUsageState.setStatus("mandatory")
_RtgVnsOperTable_Object = MibTable
rtgVnsOperTable = _RtgVnsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 15)
)
if mibBuilder.loadTexts:
    rtgVnsOperTable.setStatus("mandatory")
_RtgVnsOperEntry_Object = MibTableRow
rtgVnsOperEntry = _RtgVnsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 15, 1)
)
rtgVnsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsOperEntry.setStatus("mandatory")


class _RtgVnsReportedThroughputMetric_Type(Unsigned32):
    """Custom type rtgVnsReportedThroughputMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgVnsReportedThroughputMetric_Type.__name__ = "Unsigned32"
_RtgVnsReportedThroughputMetric_Object = MibTableColumn
rtgVnsReportedThroughputMetric = _RtgVnsReportedThroughputMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 15, 1, 1),
    _RtgVnsReportedThroughputMetric_Type()
)
rtgVnsReportedThroughputMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsReportedThroughputMetric.setStatus("mandatory")
_RtgVnsFwdStatsTable_Object = MibTable
rtgVnsFwdStatsTable = _RtgVnsFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16)
)
if mibBuilder.loadTexts:
    rtgVnsFwdStatsTable.setStatus("mandatory")
_RtgVnsFwdStatsEntry_Object = MibTableRow
rtgVnsFwdStatsEntry = _RtgVnsFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1)
)
rtgVnsFwdStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-VnsMIB", "rtgVnsIndex"),
)
if mibBuilder.loadTexts:
    rtgVnsFwdStatsEntry.setStatus("mandatory")
_RtgVnsUniRxPkts_Type = PassportCounter64
_RtgVnsUniRxPkts_Object = MibTableColumn
rtgVnsUniRxPkts = _RtgVnsUniRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 1),
    _RtgVnsUniRxPkts_Type()
)
rtgVnsUniRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsUniRxPkts.setStatus("mandatory")
_RtgVnsUniRxBytes_Type = PassportCounter64
_RtgVnsUniRxBytes_Object = MibTableColumn
rtgVnsUniRxBytes = _RtgVnsUniRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 2),
    _RtgVnsUniRxBytes_Type()
)
rtgVnsUniRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsUniRxBytes.setStatus("mandatory")
_RtgVnsUniRxDiscPkts_Type = PassportCounter64
_RtgVnsUniRxDiscPkts_Object = MibTableColumn
rtgVnsUniRxDiscPkts = _RtgVnsUniRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 3),
    _RtgVnsUniRxDiscPkts_Type()
)
rtgVnsUniRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsUniRxDiscPkts.setStatus("mandatory")
_RtgVnsUniTxPkts_Type = PassportCounter64
_RtgVnsUniTxPkts_Object = MibTableColumn
rtgVnsUniTxPkts = _RtgVnsUniTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 4),
    _RtgVnsUniTxPkts_Type()
)
rtgVnsUniTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsUniTxPkts.setStatus("mandatory")
_RtgVnsUniTxBytes_Type = PassportCounter64
_RtgVnsUniTxBytes_Object = MibTableColumn
rtgVnsUniTxBytes = _RtgVnsUniTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 5),
    _RtgVnsUniTxBytes_Type()
)
rtgVnsUniTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsUniTxBytes.setStatus("mandatory")
_RtgVnsUniTxDiscPkts_Type = PassportCounter64
_RtgVnsUniTxDiscPkts_Object = MibTableColumn
rtgVnsUniTxDiscPkts = _RtgVnsUniTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 6),
    _RtgVnsUniTxDiscPkts_Type()
)
rtgVnsUniTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsUniTxDiscPkts.setStatus("mandatory")
_RtgVnsMultiRxPkts_Type = PassportCounter64
_RtgVnsMultiRxPkts_Object = MibTableColumn
rtgVnsMultiRxPkts = _RtgVnsMultiRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 7),
    _RtgVnsMultiRxPkts_Type()
)
rtgVnsMultiRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsMultiRxPkts.setStatus("mandatory")
_RtgVnsMultiRxBytes_Type = PassportCounter64
_RtgVnsMultiRxBytes_Object = MibTableColumn
rtgVnsMultiRxBytes = _RtgVnsMultiRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 8),
    _RtgVnsMultiRxBytes_Type()
)
rtgVnsMultiRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsMultiRxBytes.setStatus("mandatory")
_RtgVnsMultiRxDiscPkts_Type = PassportCounter64
_RtgVnsMultiRxDiscPkts_Object = MibTableColumn
rtgVnsMultiRxDiscPkts = _RtgVnsMultiRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 9),
    _RtgVnsMultiRxDiscPkts_Type()
)
rtgVnsMultiRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsMultiRxDiscPkts.setStatus("mandatory")
_RtgVnsMultiTxPkts_Type = PassportCounter64
_RtgVnsMultiTxPkts_Object = MibTableColumn
rtgVnsMultiTxPkts = _RtgVnsMultiTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 10),
    _RtgVnsMultiTxPkts_Type()
)
rtgVnsMultiTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsMultiTxPkts.setStatus("mandatory")
_RtgVnsMultiTxBytes_Type = PassportCounter64
_RtgVnsMultiTxBytes_Object = MibTableColumn
rtgVnsMultiTxBytes = _RtgVnsMultiTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 11),
    _RtgVnsMultiTxBytes_Type()
)
rtgVnsMultiTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsMultiTxBytes.setStatus("mandatory")
_RtgVnsMultiTxDiscPkts_Type = PassportCounter64
_RtgVnsMultiTxDiscPkts_Object = MibTableColumn
rtgVnsMultiTxDiscPkts = _RtgVnsMultiTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 12),
    _RtgVnsMultiTxDiscPkts_Type()
)
rtgVnsMultiTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsMultiTxDiscPkts.setStatus("mandatory")
_RtgVnsTotalRxPkts_Type = PassportCounter64
_RtgVnsTotalRxPkts_Object = MibTableColumn
rtgVnsTotalRxPkts = _RtgVnsTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 13),
    _RtgVnsTotalRxPkts_Type()
)
rtgVnsTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsTotalRxPkts.setStatus("mandatory")
_RtgVnsTotalRxBytes_Type = PassportCounter64
_RtgVnsTotalRxBytes_Object = MibTableColumn
rtgVnsTotalRxBytes = _RtgVnsTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 14),
    _RtgVnsTotalRxBytes_Type()
)
rtgVnsTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsTotalRxBytes.setStatus("mandatory")
_RtgVnsTotalRxDiscPkts_Type = PassportCounter64
_RtgVnsTotalRxDiscPkts_Object = MibTableColumn
rtgVnsTotalRxDiscPkts = _RtgVnsTotalRxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 15),
    _RtgVnsTotalRxDiscPkts_Type()
)
rtgVnsTotalRxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsTotalRxDiscPkts.setStatus("mandatory")
_RtgVnsTotalTxPkts_Type = PassportCounter64
_RtgVnsTotalTxPkts_Object = MibTableColumn
rtgVnsTotalTxPkts = _RtgVnsTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 16),
    _RtgVnsTotalTxPkts_Type()
)
rtgVnsTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsTotalTxPkts.setStatus("mandatory")
_RtgVnsTotalTxBytes_Type = PassportCounter64
_RtgVnsTotalTxBytes_Object = MibTableColumn
rtgVnsTotalTxBytes = _RtgVnsTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 17),
    _RtgVnsTotalTxBytes_Type()
)
rtgVnsTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsTotalTxBytes.setStatus("mandatory")
_RtgVnsTotalTxDiscPkts_Type = PassportCounter64
_RtgVnsTotalTxDiscPkts_Object = MibTableColumn
rtgVnsTotalTxDiscPkts = _RtgVnsTotalTxDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 3, 16, 1, 18),
    _RtgVnsTotalTxDiscPkts_Type()
)
rtgVnsTotalTxDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgVnsTotalTxDiscPkts.setStatus("mandatory")
_VnsMIB_ObjectIdentity = ObjectIdentity
vnsMIB = _VnsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20)
)
_VnsGroup_ObjectIdentity = ObjectIdentity
vnsGroup = _VnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20, 1)
)
_VnsGroupBD_ObjectIdentity = ObjectIdentity
vnsGroupBD = _VnsGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20, 1, 4)
)
_VnsGroupBD00_ObjectIdentity = ObjectIdentity
vnsGroupBD00 = _VnsGroupBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20, 1, 4, 1)
)
_VnsGroupBD00A_ObjectIdentity = ObjectIdentity
vnsGroupBD00A = _VnsGroupBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20, 1, 4, 1, 2)
)
_VnsCapabilities_ObjectIdentity = ObjectIdentity
vnsCapabilities = _VnsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20, 3)
)
_VnsCapabilitiesBD_ObjectIdentity = ObjectIdentity
vnsCapabilitiesBD = _VnsCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20, 3, 4)
)
_VnsCapabilitiesBD00_ObjectIdentity = ObjectIdentity
vnsCapabilitiesBD00 = _VnsCapabilitiesBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20, 3, 4, 1)
)
_VnsCapabilitiesBD00A_ObjectIdentity = ObjectIdentity
vnsCapabilitiesBD00A = _VnsCapabilitiesBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 20, 3, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VnsMIB",
    **{"rtgVns": rtgVns,
       "rtgVnsRowStatusTable": rtgVnsRowStatusTable,
       "rtgVnsRowStatusEntry": rtgVnsRowStatusEntry,
       "rtgVnsRowStatus": rtgVnsRowStatus,
       "rtgVnsComponentName": rtgVnsComponentName,
       "rtgVnsStorageType": rtgVnsStorageType,
       "rtgVnsIndex": rtgVnsIndex,
       "rtgVnsNode": rtgVnsNode,
       "rtgVnsNodeRowStatusTable": rtgVnsNodeRowStatusTable,
       "rtgVnsNodeRowStatusEntry": rtgVnsNodeRowStatusEntry,
       "rtgVnsNodeRowStatus": rtgVnsNodeRowStatus,
       "rtgVnsNodeComponentName": rtgVnsNodeComponentName,
       "rtgVnsNodeStorageType": rtgVnsNodeStorageType,
       "rtgVnsNodeIndex": rtgVnsNodeIndex,
       "rtgVnsNodeOperTable": rtgVnsNodeOperTable,
       "rtgVnsNodeOperEntry": rtgVnsNodeOperEntry,
       "rtgVnsNodeMetric": rtgVnsNodeMetric,
       "rtgVnsNodeNextHopLinkGroup1": rtgVnsNodeNextHopLinkGroup1,
       "rtgVnsNodeNextHopLinkGroup2": rtgVnsNodeNextHopLinkGroup2,
       "rtgVnsLpStats": rtgVnsLpStats,
       "rtgVnsLpStatsRowStatusTable": rtgVnsLpStatsRowStatusTable,
       "rtgVnsLpStatsRowStatusEntry": rtgVnsLpStatsRowStatusEntry,
       "rtgVnsLpStatsRowStatus": rtgVnsLpStatsRowStatus,
       "rtgVnsLpStatsComponentName": rtgVnsLpStatsComponentName,
       "rtgVnsLpStatsStorageType": rtgVnsLpStatsStorageType,
       "rtgVnsLpStatsIndex": rtgVnsLpStatsIndex,
       "rtgVnsLpStatsFwdStatsTable": rtgVnsLpStatsFwdStatsTable,
       "rtgVnsLpStatsFwdStatsEntry": rtgVnsLpStatsFwdStatsEntry,
       "rtgVnsLpStatsUniRxPkts": rtgVnsLpStatsUniRxPkts,
       "rtgVnsLpStatsUniRxBytes": rtgVnsLpStatsUniRxBytes,
       "rtgVnsLpStatsUniRxDiscPkts": rtgVnsLpStatsUniRxDiscPkts,
       "rtgVnsLpStatsUniTxPkts": rtgVnsLpStatsUniTxPkts,
       "rtgVnsLpStatsUniTxBytes": rtgVnsLpStatsUniTxBytes,
       "rtgVnsLpStatsUniTxDiscPkts": rtgVnsLpStatsUniTxDiscPkts,
       "rtgVnsLpStatsMultiRxPkts": rtgVnsLpStatsMultiRxPkts,
       "rtgVnsLpStatsMultiRxBytes": rtgVnsLpStatsMultiRxBytes,
       "rtgVnsLpStatsMultiRxDiscPkts": rtgVnsLpStatsMultiRxDiscPkts,
       "rtgVnsLpStatsMultiTxPkts": rtgVnsLpStatsMultiTxPkts,
       "rtgVnsLpStatsMultiTxBytes": rtgVnsLpStatsMultiTxBytes,
       "rtgVnsLpStatsMultiTxDiscPkts": rtgVnsLpStatsMultiTxDiscPkts,
       "rtgVnsLpStatsTotalRxPkts": rtgVnsLpStatsTotalRxPkts,
       "rtgVnsLpStatsTotalRxBytes": rtgVnsLpStatsTotalRxBytes,
       "rtgVnsLpStatsTotalRxDiscPkts": rtgVnsLpStatsTotalRxDiscPkts,
       "rtgVnsLpStatsTotalTxPkts": rtgVnsLpStatsTotalTxPkts,
       "rtgVnsLpStatsTotalTxBytes": rtgVnsLpStatsTotalTxBytes,
       "rtgVnsLpStatsTotalTxDiscPkts": rtgVnsLpStatsTotalTxDiscPkts,
       "rtgVnsProvTable": rtgVnsProvTable,
       "rtgVnsProvEntry": rtgVnsProvEntry,
       "rtgVnsLogicalNetworkNumber": rtgVnsLogicalNetworkNumber,
       "rtgVnsLinkToProtocolPort": rtgVnsLinkToProtocolPort,
       "rtgVnsMaximumTransmissionUnit": rtgVnsMaximumTransmissionUnit,
       "rtgVnsLoadSharing": rtgVnsLoadSharing,
       "rtgVnsDiscardPriority": rtgVnsDiscardPriority,
       "rtgVnsIlsForwarder": rtgVnsIlsForwarder,
       "rtgVnsIfEntryTable": rtgVnsIfEntryTable,
       "rtgVnsIfEntryEntry": rtgVnsIfEntryEntry,
       "rtgVnsIfAdminStatus": rtgVnsIfAdminStatus,
       "rtgVnsIfIndex": rtgVnsIfIndex,
       "rtgVnsCidDataTable": rtgVnsCidDataTable,
       "rtgVnsCidDataEntry": rtgVnsCidDataEntry,
       "rtgVnsCustomerIdentifier": rtgVnsCustomerIdentifier,
       "rtgVnsStateTable": rtgVnsStateTable,
       "rtgVnsStateEntry": rtgVnsStateEntry,
       "rtgVnsAdminState": rtgVnsAdminState,
       "rtgVnsOperationalState": rtgVnsOperationalState,
       "rtgVnsUsageState": rtgVnsUsageState,
       "rtgVnsOperTable": rtgVnsOperTable,
       "rtgVnsOperEntry": rtgVnsOperEntry,
       "rtgVnsReportedThroughputMetric": rtgVnsReportedThroughputMetric,
       "rtgVnsFwdStatsTable": rtgVnsFwdStatsTable,
       "rtgVnsFwdStatsEntry": rtgVnsFwdStatsEntry,
       "rtgVnsUniRxPkts": rtgVnsUniRxPkts,
       "rtgVnsUniRxBytes": rtgVnsUniRxBytes,
       "rtgVnsUniRxDiscPkts": rtgVnsUniRxDiscPkts,
       "rtgVnsUniTxPkts": rtgVnsUniTxPkts,
       "rtgVnsUniTxBytes": rtgVnsUniTxBytes,
       "rtgVnsUniTxDiscPkts": rtgVnsUniTxDiscPkts,
       "rtgVnsMultiRxPkts": rtgVnsMultiRxPkts,
       "rtgVnsMultiRxBytes": rtgVnsMultiRxBytes,
       "rtgVnsMultiRxDiscPkts": rtgVnsMultiRxDiscPkts,
       "rtgVnsMultiTxPkts": rtgVnsMultiTxPkts,
       "rtgVnsMultiTxBytes": rtgVnsMultiTxBytes,
       "rtgVnsMultiTxDiscPkts": rtgVnsMultiTxDiscPkts,
       "rtgVnsTotalRxPkts": rtgVnsTotalRxPkts,
       "rtgVnsTotalRxBytes": rtgVnsTotalRxBytes,
       "rtgVnsTotalRxDiscPkts": rtgVnsTotalRxDiscPkts,
       "rtgVnsTotalTxPkts": rtgVnsTotalTxPkts,
       "rtgVnsTotalTxBytes": rtgVnsTotalTxBytes,
       "rtgVnsTotalTxDiscPkts": rtgVnsTotalTxDiscPkts,
       "vnsMIB": vnsMIB,
       "vnsGroup": vnsGroup,
       "vnsGroupBD": vnsGroupBD,
       "vnsGroupBD00": vnsGroupBD00,
       "vnsGroupBD00A": vnsGroupBD00A,
       "vnsCapabilities": vnsCapabilities,
       "vnsCapabilitiesBD": vnsCapabilitiesBD,
       "vnsCapabilitiesBD00": vnsCapabilitiesBD00,
       "vnsCapabilitiesBD00A": vnsCapabilitiesBD00A}
)
