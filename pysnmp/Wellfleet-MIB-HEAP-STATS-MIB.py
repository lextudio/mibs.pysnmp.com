# SNMP MIB module (Wellfleet-MIB-HEAP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-MIB-HEAP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:39 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfMibHeapGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfMibHeapGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfMibHeapTable_Object = MibTable
wfMibHeapTable = _WfMibHeapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    wfMibHeapTable.setStatus("mandatory")
_WfMibHeapEntry_Object = MibTableRow
wfMibHeapEntry = _WfMibHeapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1)
)
wfMibHeapEntry.setIndexNames(
    (0, "Wellfleet-MIB-HEAP-STATS-MIB", "wfMibHeapSlot"),
)
if mibBuilder.loadTexts:
    wfMibHeapEntry.setStatus("mandatory")
_WfMibHeapSlot_Type = Integer32
_WfMibHeapSlot_Object = MibTableColumn
wfMibHeapSlot = _WfMibHeapSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 1),
    _WfMibHeapSlot_Type()
)
wfMibHeapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSlot.setStatus("mandatory")
_WfMibHeapMemorySize_Type = Integer32
_WfMibHeapMemorySize_Object = MibTableColumn
wfMibHeapMemorySize = _WfMibHeapMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 2),
    _WfMibHeapMemorySize_Type()
)
wfMibHeapMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapMemorySize.setStatus("mandatory")


class _WfMibHeapBoundrySize_Type(Integer32):
    """Custom type wfMibHeapBoundrySize based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 512),
    )


_WfMibHeapBoundrySize_Type.__name__ = "Integer32"
_WfMibHeapBoundrySize_Object = MibTableColumn
wfMibHeapBoundrySize = _WfMibHeapBoundrySize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 3),
    _WfMibHeapBoundrySize_Type()
)
wfMibHeapBoundrySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMibHeapBoundrySize.setStatus("mandatory")


class _WfMibHeapPageSize_Type(Integer32):
    """Custom type wfMibHeapPageSize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_WfMibHeapPageSize_Type.__name__ = "Integer32"
_WfMibHeapPageSize_Object = MibTableColumn
wfMibHeapPageSize = _WfMibHeapPageSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 4),
    _WfMibHeapPageSize_Type()
)
wfMibHeapPageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMibHeapPageSize.setStatus("mandatory")
_WfMibHeapTotalPages_Type = Integer32
_WfMibHeapTotalPages_Object = MibTableColumn
wfMibHeapTotalPages = _WfMibHeapTotalPages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 5),
    _WfMibHeapTotalPages_Type()
)
wfMibHeapTotalPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapTotalPages.setStatus("mandatory")
_WfMibHeapTotalSegs_Type = Integer32
_WfMibHeapTotalSegs_Object = MibTableColumn
wfMibHeapTotalSegs = _WfMibHeapTotalSegs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 6),
    _WfMibHeapTotalSegs_Type()
)
wfMibHeapTotalSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapTotalSegs.setStatus("mandatory")
_WfMibHeapSegsFree_Type = Integer32
_WfMibHeapSegsFree_Object = MibTableColumn
wfMibHeapSegsFree = _WfMibHeapSegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 7),
    _WfMibHeapSegsFree_Type()
)
wfMibHeapSegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSegsFree.setStatus("mandatory")
_WfMibHeapSmlstSeg_Type = Integer32
_WfMibHeapSmlstSeg_Object = MibTableColumn
wfMibHeapSmlstSeg = _WfMibHeapSmlstSeg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 8),
    _WfMibHeapSmlstSeg_Type()
)
wfMibHeapSmlstSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSmlstSeg.setStatus("mandatory")
_WfMibHeapLrgstSeg_Type = Integer32
_WfMibHeapLrgstSeg_Object = MibTableColumn
wfMibHeapLrgstSeg = _WfMibHeapLrgstSeg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 9),
    _WfMibHeapLrgstSeg_Type()
)
wfMibHeapLrgstSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapLrgstSeg.setStatus("mandatory")


class _WfMibHeapStartSize_Type(Integer32):
    """Custom type wfMibHeapStartSize based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_WfMibHeapStartSize_Type.__name__ = "Integer32"
_WfMibHeapStartSize_Object = MibTableColumn
wfMibHeapStartSize = _WfMibHeapStartSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 10),
    _WfMibHeapStartSize_Type()
)
wfMibHeapStartSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMibHeapStartSize.setStatus("mandatory")
_WfMibHeapSize1_Type = Integer32
_WfMibHeapSize1_Object = MibTableColumn
wfMibHeapSize1 = _WfMibHeapSize1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 11),
    _WfMibHeapSize1_Type()
)
wfMibHeapSize1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize1.setStatus("mandatory")
_WfMibHeapSize1SegsFree_Type = Integer32
_WfMibHeapSize1SegsFree_Object = MibTableColumn
wfMibHeapSize1SegsFree = _WfMibHeapSize1SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 12),
    _WfMibHeapSize1SegsFree_Type()
)
wfMibHeapSize1SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize1SegsFree.setStatus("mandatory")
_WfMibHeapSize1SegsTotal_Type = Integer32
_WfMibHeapSize1SegsTotal_Object = MibTableColumn
wfMibHeapSize1SegsTotal = _WfMibHeapSize1SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 13),
    _WfMibHeapSize1SegsTotal_Type()
)
wfMibHeapSize1SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize1SegsTotal.setStatus("mandatory")
_WfMibHeapSize1Pages_Type = Integer32
_WfMibHeapSize1Pages_Object = MibTableColumn
wfMibHeapSize1Pages = _WfMibHeapSize1Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 14),
    _WfMibHeapSize1Pages_Type()
)
wfMibHeapSize1Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize1Pages.setStatus("mandatory")
_WfMibHeapSize2_Type = Integer32
_WfMibHeapSize2_Object = MibTableColumn
wfMibHeapSize2 = _WfMibHeapSize2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 15),
    _WfMibHeapSize2_Type()
)
wfMibHeapSize2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize2.setStatus("mandatory")
_WfMibHeapSize2SegsFree_Type = Integer32
_WfMibHeapSize2SegsFree_Object = MibTableColumn
wfMibHeapSize2SegsFree = _WfMibHeapSize2SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 16),
    _WfMibHeapSize2SegsFree_Type()
)
wfMibHeapSize2SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize2SegsFree.setStatus("mandatory")
_WfMibHeapSize2SegsTotal_Type = Integer32
_WfMibHeapSize2SegsTotal_Object = MibTableColumn
wfMibHeapSize2SegsTotal = _WfMibHeapSize2SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 17),
    _WfMibHeapSize2SegsTotal_Type()
)
wfMibHeapSize2SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize2SegsTotal.setStatus("mandatory")
_WfMibHeapSize2Pages_Type = Integer32
_WfMibHeapSize2Pages_Object = MibTableColumn
wfMibHeapSize2Pages = _WfMibHeapSize2Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 18),
    _WfMibHeapSize2Pages_Type()
)
wfMibHeapSize2Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize2Pages.setStatus("mandatory")
_WfMibHeapSize3_Type = Integer32
_WfMibHeapSize3_Object = MibTableColumn
wfMibHeapSize3 = _WfMibHeapSize3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 19),
    _WfMibHeapSize3_Type()
)
wfMibHeapSize3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize3.setStatus("mandatory")
_WfMibHeapSize3SegsFree_Type = Integer32
_WfMibHeapSize3SegsFree_Object = MibTableColumn
wfMibHeapSize3SegsFree = _WfMibHeapSize3SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 20),
    _WfMibHeapSize3SegsFree_Type()
)
wfMibHeapSize3SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize3SegsFree.setStatus("mandatory")
_WfMibHeapSize3SegsTotal_Type = Integer32
_WfMibHeapSize3SegsTotal_Object = MibTableColumn
wfMibHeapSize3SegsTotal = _WfMibHeapSize3SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 21),
    _WfMibHeapSize3SegsTotal_Type()
)
wfMibHeapSize3SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize3SegsTotal.setStatus("mandatory")
_WfMibHeapSize3Pages_Type = Integer32
_WfMibHeapSize3Pages_Object = MibTableColumn
wfMibHeapSize3Pages = _WfMibHeapSize3Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 22),
    _WfMibHeapSize3Pages_Type()
)
wfMibHeapSize3Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize3Pages.setStatus("mandatory")
_WfMibHeapSize4_Type = Integer32
_WfMibHeapSize4_Object = MibTableColumn
wfMibHeapSize4 = _WfMibHeapSize4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 23),
    _WfMibHeapSize4_Type()
)
wfMibHeapSize4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize4.setStatus("mandatory")
_WfMibHeapSize4SegsFree_Type = Integer32
_WfMibHeapSize4SegsFree_Object = MibTableColumn
wfMibHeapSize4SegsFree = _WfMibHeapSize4SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 24),
    _WfMibHeapSize4SegsFree_Type()
)
wfMibHeapSize4SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize4SegsFree.setStatus("mandatory")
_WfMibHeapSize4SegsTotal_Type = Integer32
_WfMibHeapSize4SegsTotal_Object = MibTableColumn
wfMibHeapSize4SegsTotal = _WfMibHeapSize4SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 25),
    _WfMibHeapSize4SegsTotal_Type()
)
wfMibHeapSize4SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize4SegsTotal.setStatus("mandatory")
_WfMibHeapSize4Pages_Type = Integer32
_WfMibHeapSize4Pages_Object = MibTableColumn
wfMibHeapSize4Pages = _WfMibHeapSize4Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 26),
    _WfMibHeapSize4Pages_Type()
)
wfMibHeapSize4Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize4Pages.setStatus("mandatory")
_WfMibHeapSize5_Type = Integer32
_WfMibHeapSize5_Object = MibTableColumn
wfMibHeapSize5 = _WfMibHeapSize5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 27),
    _WfMibHeapSize5_Type()
)
wfMibHeapSize5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize5.setStatus("mandatory")
_WfMibHeapSize5SegsFree_Type = Integer32
_WfMibHeapSize5SegsFree_Object = MibTableColumn
wfMibHeapSize5SegsFree = _WfMibHeapSize5SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 28),
    _WfMibHeapSize5SegsFree_Type()
)
wfMibHeapSize5SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize5SegsFree.setStatus("mandatory")
_WfMibHeapSize5SegsTotal_Type = Integer32
_WfMibHeapSize5SegsTotal_Object = MibTableColumn
wfMibHeapSize5SegsTotal = _WfMibHeapSize5SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 29),
    _WfMibHeapSize5SegsTotal_Type()
)
wfMibHeapSize5SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize5SegsTotal.setStatus("mandatory")
_WfMibHeapSize5Pages_Type = Integer32
_WfMibHeapSize5Pages_Object = MibTableColumn
wfMibHeapSize5Pages = _WfMibHeapSize5Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 30),
    _WfMibHeapSize5Pages_Type()
)
wfMibHeapSize5Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize5Pages.setStatus("mandatory")
_WfMibHeapSize6_Type = Integer32
_WfMibHeapSize6_Object = MibTableColumn
wfMibHeapSize6 = _WfMibHeapSize6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 31),
    _WfMibHeapSize6_Type()
)
wfMibHeapSize6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize6.setStatus("mandatory")
_WfMibHeapSize6SegsFree_Type = Integer32
_WfMibHeapSize6SegsFree_Object = MibTableColumn
wfMibHeapSize6SegsFree = _WfMibHeapSize6SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 32),
    _WfMibHeapSize6SegsFree_Type()
)
wfMibHeapSize6SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize6SegsFree.setStatus("mandatory")
_WfMibHeapSize6SegsTotal_Type = Integer32
_WfMibHeapSize6SegsTotal_Object = MibTableColumn
wfMibHeapSize6SegsTotal = _WfMibHeapSize6SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 33),
    _WfMibHeapSize6SegsTotal_Type()
)
wfMibHeapSize6SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize6SegsTotal.setStatus("mandatory")
_WfMibHeapSize6Pages_Type = Integer32
_WfMibHeapSize6Pages_Object = MibTableColumn
wfMibHeapSize6Pages = _WfMibHeapSize6Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 34),
    _WfMibHeapSize6Pages_Type()
)
wfMibHeapSize6Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize6Pages.setStatus("mandatory")
_WfMibHeapSize7_Type = Integer32
_WfMibHeapSize7_Object = MibTableColumn
wfMibHeapSize7 = _WfMibHeapSize7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 35),
    _WfMibHeapSize7_Type()
)
wfMibHeapSize7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize7.setStatus("mandatory")
_WfMibHeapSize7SegsFree_Type = Integer32
_WfMibHeapSize7SegsFree_Object = MibTableColumn
wfMibHeapSize7SegsFree = _WfMibHeapSize7SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 36),
    _WfMibHeapSize7SegsFree_Type()
)
wfMibHeapSize7SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize7SegsFree.setStatus("mandatory")
_WfMibHeapSize7SegsTotal_Type = Integer32
_WfMibHeapSize7SegsTotal_Object = MibTableColumn
wfMibHeapSize7SegsTotal = _WfMibHeapSize7SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 37),
    _WfMibHeapSize7SegsTotal_Type()
)
wfMibHeapSize7SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize7SegsTotal.setStatus("mandatory")
_WfMibHeapSize7Pages_Type = Integer32
_WfMibHeapSize7Pages_Object = MibTableColumn
wfMibHeapSize7Pages = _WfMibHeapSize7Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 38),
    _WfMibHeapSize7Pages_Type()
)
wfMibHeapSize7Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize7Pages.setStatus("mandatory")
_WfMibHeapSize8_Type = Integer32
_WfMibHeapSize8_Object = MibTableColumn
wfMibHeapSize8 = _WfMibHeapSize8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 39),
    _WfMibHeapSize8_Type()
)
wfMibHeapSize8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize8.setStatus("mandatory")
_WfMibHeapSize8SegsFree_Type = Integer32
_WfMibHeapSize8SegsFree_Object = MibTableColumn
wfMibHeapSize8SegsFree = _WfMibHeapSize8SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 40),
    _WfMibHeapSize8SegsFree_Type()
)
wfMibHeapSize8SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize8SegsFree.setStatus("mandatory")
_WfMibHeapSize8SegsTotal_Type = Integer32
_WfMibHeapSize8SegsTotal_Object = MibTableColumn
wfMibHeapSize8SegsTotal = _WfMibHeapSize8SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 41),
    _WfMibHeapSize8SegsTotal_Type()
)
wfMibHeapSize8SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize8SegsTotal.setStatus("mandatory")
_WfMibHeapSize8Pages_Type = Integer32
_WfMibHeapSize8Pages_Object = MibTableColumn
wfMibHeapSize8Pages = _WfMibHeapSize8Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 42),
    _WfMibHeapSize8Pages_Type()
)
wfMibHeapSize8Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize8Pages.setStatus("mandatory")
_WfMibHeapSize9_Type = Integer32
_WfMibHeapSize9_Object = MibTableColumn
wfMibHeapSize9 = _WfMibHeapSize9_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 43),
    _WfMibHeapSize9_Type()
)
wfMibHeapSize9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize9.setStatus("mandatory")
_WfMibHeapSize9SegsFree_Type = Integer32
_WfMibHeapSize9SegsFree_Object = MibTableColumn
wfMibHeapSize9SegsFree = _WfMibHeapSize9SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 44),
    _WfMibHeapSize9SegsFree_Type()
)
wfMibHeapSize9SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize9SegsFree.setStatus("mandatory")
_WfMibHeapSize9SegsTotal_Type = Integer32
_WfMibHeapSize9SegsTotal_Object = MibTableColumn
wfMibHeapSize9SegsTotal = _WfMibHeapSize9SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 45),
    _WfMibHeapSize9SegsTotal_Type()
)
wfMibHeapSize9SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize9SegsTotal.setStatus("mandatory")
_WfMibHeapSize9Pages_Type = Integer32
_WfMibHeapSize9Pages_Object = MibTableColumn
wfMibHeapSize9Pages = _WfMibHeapSize9Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 46),
    _WfMibHeapSize9Pages_Type()
)
wfMibHeapSize9Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize9Pages.setStatus("mandatory")
_WfMibHeapSize10_Type = Integer32
_WfMibHeapSize10_Object = MibTableColumn
wfMibHeapSize10 = _WfMibHeapSize10_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 47),
    _WfMibHeapSize10_Type()
)
wfMibHeapSize10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize10.setStatus("mandatory")
_WfMibHeapSize10SegsFree_Type = Integer32
_WfMibHeapSize10SegsFree_Object = MibTableColumn
wfMibHeapSize10SegsFree = _WfMibHeapSize10SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 48),
    _WfMibHeapSize10SegsFree_Type()
)
wfMibHeapSize10SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize10SegsFree.setStatus("mandatory")
_WfMibHeapSize10SegsTotal_Type = Integer32
_WfMibHeapSize10SegsTotal_Object = MibTableColumn
wfMibHeapSize10SegsTotal = _WfMibHeapSize10SegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 49),
    _WfMibHeapSize10SegsTotal_Type()
)
wfMibHeapSize10SegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize10SegsTotal.setStatus("mandatory")
_WfMibHeapSize10Pages_Type = Integer32
_WfMibHeapSize10Pages_Object = MibTableColumn
wfMibHeapSize10Pages = _WfMibHeapSize10Pages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 1, 1, 50),
    _WfMibHeapSize10Pages_Type()
)
wfMibHeapSize10Pages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapSize10Pages.setStatus("mandatory")
_WfMibHeapPageTable_Object = MibTable
wfMibHeapPageTable = _WfMibHeapPageTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    wfMibHeapPageTable.setStatus("mandatory")
_WfMibHeapPageEntry_Object = MibTableRow
wfMibHeapPageEntry = _WfMibHeapPageEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1)
)
wfMibHeapPageEntry.setIndexNames(
    (0, "Wellfleet-MIB-HEAP-STATS-MIB", "wfMibHeapPageSlot"),
)
if mibBuilder.loadTexts:
    wfMibHeapPageEntry.setStatus("mandatory")
_WfMibHeapPageSlot_Type = Integer32
_WfMibHeapPageSlot_Object = MibTableColumn
wfMibHeapPageSlot = _WfMibHeapPageSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 1),
    _WfMibHeapPageSlot_Type()
)
wfMibHeapPageSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPageSlot.setStatus("mandatory")
_WfMibHeapPageListOffset_Type = Integer32
_WfMibHeapPageListOffset_Object = MibTableColumn
wfMibHeapPageListOffset = _WfMibHeapPageListOffset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 2),
    _WfMibHeapPageListOffset_Type()
)
wfMibHeapPageListOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMibHeapPageListOffset.setStatus("mandatory")


class _WfMibHeapPageSegSize_Type(Integer32):
    """Custom type wfMibHeapPageSegSize based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_WfMibHeapPageSegSize_Type.__name__ = "Integer32"
_WfMibHeapPageSegSize_Object = MibTableColumn
wfMibHeapPageSegSize = _WfMibHeapPageSegSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 3),
    _WfMibHeapPageSegSize_Type()
)
wfMibHeapPageSegSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMibHeapPageSegSize.setStatus("mandatory")
_WfMibHeapPageTotal_Type = Integer32
_WfMibHeapPageTotal_Object = MibTableColumn
wfMibHeapPageTotal = _WfMibHeapPageTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 4),
    _WfMibHeapPageTotal_Type()
)
wfMibHeapPageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPageTotal.setStatus("mandatory")
_WfMibHeapPageMemoryTotal_Type = Integer32
_WfMibHeapPageMemoryTotal_Object = MibTableColumn
wfMibHeapPageMemoryTotal = _WfMibHeapPageMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 5),
    _WfMibHeapPageMemoryTotal_Type()
)
wfMibHeapPageMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPageMemoryTotal.setStatus("mandatory")
_WfMibHeapPageSegsTotal_Type = Integer32
_WfMibHeapPageSegsTotal_Object = MibTableColumn
wfMibHeapPageSegsTotal = _WfMibHeapPageSegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 6),
    _WfMibHeapPageSegsTotal_Type()
)
wfMibHeapPageSegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPageSegsTotal.setStatus("mandatory")
_WfMibHeapPageSegsAllocd_Type = Integer32
_WfMibHeapPageSegsAllocd_Object = MibTableColumn
wfMibHeapPageSegsAllocd = _WfMibHeapPageSegsAllocd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 7),
    _WfMibHeapPageSegsAllocd_Type()
)
wfMibHeapPageSegsAllocd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPageSegsAllocd.setStatus("mandatory")
_WfMibHeapPageSegsFree_Type = Integer32
_WfMibHeapPageSegsFree_Object = MibTableColumn
wfMibHeapPageSegsFree = _WfMibHeapPageSegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 8),
    _WfMibHeapPageSegsFree_Type()
)
wfMibHeapPageSegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPageSegsFree.setStatus("mandatory")
_WfMibHeapPage1Size_Type = Integer32
_WfMibHeapPage1Size_Object = MibTableColumn
wfMibHeapPage1Size = _WfMibHeapPage1Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 9),
    _WfMibHeapPage1Size_Type()
)
wfMibHeapPage1Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage1Size.setStatus("mandatory")
_WfMibHeapPage1SegsFree_Type = Integer32
_WfMibHeapPage1SegsFree_Object = MibTableColumn
wfMibHeapPage1SegsFree = _WfMibHeapPage1SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 10),
    _WfMibHeapPage1SegsFree_Type()
)
wfMibHeapPage1SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage1SegsFree.setStatus("mandatory")
_WfMibHeapPage1SegsMax_Type = Integer32
_WfMibHeapPage1SegsMax_Object = MibTableColumn
wfMibHeapPage1SegsMax = _WfMibHeapPage1SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 11),
    _WfMibHeapPage1SegsMax_Type()
)
wfMibHeapPage1SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage1SegsMax.setStatus("mandatory")
_WfMibHeapPage2Size_Type = Integer32
_WfMibHeapPage2Size_Object = MibTableColumn
wfMibHeapPage2Size = _WfMibHeapPage2Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 12),
    _WfMibHeapPage2Size_Type()
)
wfMibHeapPage2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage2Size.setStatus("mandatory")
_WfMibHeapPage2SegsFree_Type = Integer32
_WfMibHeapPage2SegsFree_Object = MibTableColumn
wfMibHeapPage2SegsFree = _WfMibHeapPage2SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 13),
    _WfMibHeapPage2SegsFree_Type()
)
wfMibHeapPage2SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage2SegsFree.setStatus("mandatory")
_WfMibHeapPage2SegsMax_Type = Integer32
_WfMibHeapPage2SegsMax_Object = MibTableColumn
wfMibHeapPage2SegsMax = _WfMibHeapPage2SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 14),
    _WfMibHeapPage2SegsMax_Type()
)
wfMibHeapPage2SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage2SegsMax.setStatus("mandatory")
_WfMibHeapPage3Size_Type = Integer32
_WfMibHeapPage3Size_Object = MibTableColumn
wfMibHeapPage3Size = _WfMibHeapPage3Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 15),
    _WfMibHeapPage3Size_Type()
)
wfMibHeapPage3Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage3Size.setStatus("mandatory")
_WfMibHeapPage3SegsFree_Type = Integer32
_WfMibHeapPage3SegsFree_Object = MibTableColumn
wfMibHeapPage3SegsFree = _WfMibHeapPage3SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 16),
    _WfMibHeapPage3SegsFree_Type()
)
wfMibHeapPage3SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage3SegsFree.setStatus("mandatory")
_WfMibHeapPage3SegsMax_Type = Integer32
_WfMibHeapPage3SegsMax_Object = MibTableColumn
wfMibHeapPage3SegsMax = _WfMibHeapPage3SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 17),
    _WfMibHeapPage3SegsMax_Type()
)
wfMibHeapPage3SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage3SegsMax.setStatus("mandatory")
_WfMibHeapPage4Size_Type = Integer32
_WfMibHeapPage4Size_Object = MibTableColumn
wfMibHeapPage4Size = _WfMibHeapPage4Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 18),
    _WfMibHeapPage4Size_Type()
)
wfMibHeapPage4Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage4Size.setStatus("mandatory")
_WfMibHeapPage4SegsFree_Type = Integer32
_WfMibHeapPage4SegsFree_Object = MibTableColumn
wfMibHeapPage4SegsFree = _WfMibHeapPage4SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 19),
    _WfMibHeapPage4SegsFree_Type()
)
wfMibHeapPage4SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage4SegsFree.setStatus("mandatory")
_WfMibHeapPage4SegsMax_Type = Integer32
_WfMibHeapPage4SegsMax_Object = MibTableColumn
wfMibHeapPage4SegsMax = _WfMibHeapPage4SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 20),
    _WfMibHeapPage4SegsMax_Type()
)
wfMibHeapPage4SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage4SegsMax.setStatus("mandatory")
_WfMibHeapPage5Size_Type = Integer32
_WfMibHeapPage5Size_Object = MibTableColumn
wfMibHeapPage5Size = _WfMibHeapPage5Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 21),
    _WfMibHeapPage5Size_Type()
)
wfMibHeapPage5Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage5Size.setStatus("mandatory")
_WfMibHeapPage5SegsFree_Type = Integer32
_WfMibHeapPage5SegsFree_Object = MibTableColumn
wfMibHeapPage5SegsFree = _WfMibHeapPage5SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 22),
    _WfMibHeapPage5SegsFree_Type()
)
wfMibHeapPage5SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage5SegsFree.setStatus("mandatory")
_WfMibHeapPage5SegsMax_Type = Integer32
_WfMibHeapPage5SegsMax_Object = MibTableColumn
wfMibHeapPage5SegsMax = _WfMibHeapPage5SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 23),
    _WfMibHeapPage5SegsMax_Type()
)
wfMibHeapPage5SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage5SegsMax.setStatus("mandatory")
_WfMibHeapPage6PageSize_Type = Integer32
_WfMibHeapPage6PageSize_Object = MibTableColumn
wfMibHeapPage6PageSize = _WfMibHeapPage6PageSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 24),
    _WfMibHeapPage6PageSize_Type()
)
wfMibHeapPage6PageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage6PageSize.setStatus("mandatory")
_WfMibHeapPage6SegsFree_Type = Integer32
_WfMibHeapPage6SegsFree_Object = MibTableColumn
wfMibHeapPage6SegsFree = _WfMibHeapPage6SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 25),
    _WfMibHeapPage6SegsFree_Type()
)
wfMibHeapPage6SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage6SegsFree.setStatus("mandatory")
_WfMibHeapPage6SegsMax_Type = Integer32
_WfMibHeapPage6SegsMax_Object = MibTableColumn
wfMibHeapPage6SegsMax = _WfMibHeapPage6SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 26),
    _WfMibHeapPage6SegsMax_Type()
)
wfMibHeapPage6SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage6SegsMax.setStatus("mandatory")
_WfMibHeapPage7Size_Type = Integer32
_WfMibHeapPage7Size_Object = MibTableColumn
wfMibHeapPage7Size = _WfMibHeapPage7Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 27),
    _WfMibHeapPage7Size_Type()
)
wfMibHeapPage7Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage7Size.setStatus("mandatory")
_WfMibHeapPage7SegsFree_Type = Integer32
_WfMibHeapPage7SegsFree_Object = MibTableColumn
wfMibHeapPage7SegsFree = _WfMibHeapPage7SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 28),
    _WfMibHeapPage7SegsFree_Type()
)
wfMibHeapPage7SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage7SegsFree.setStatus("mandatory")
_WfMibHeapPage7SegsMax_Type = Integer32
_WfMibHeapPage7SegsMax_Object = MibTableColumn
wfMibHeapPage7SegsMax = _WfMibHeapPage7SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 29),
    _WfMibHeapPage7SegsMax_Type()
)
wfMibHeapPage7SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage7SegsMax.setStatus("mandatory")
_WfMibHeapPage8Size_Type = Integer32
_WfMibHeapPage8Size_Object = MibTableColumn
wfMibHeapPage8Size = _WfMibHeapPage8Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 30),
    _WfMibHeapPage8Size_Type()
)
wfMibHeapPage8Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage8Size.setStatus("mandatory")
_WfMibHeapPage8SegsFree_Type = Integer32
_WfMibHeapPage8SegsFree_Object = MibTableColumn
wfMibHeapPage8SegsFree = _WfMibHeapPage8SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 31),
    _WfMibHeapPage8SegsFree_Type()
)
wfMibHeapPage8SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage8SegsFree.setStatus("mandatory")
_WfMibHeapPage8SegsMax_Type = Integer32
_WfMibHeapPage8SegsMax_Object = MibTableColumn
wfMibHeapPage8SegsMax = _WfMibHeapPage8SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 32),
    _WfMibHeapPage8SegsMax_Type()
)
wfMibHeapPage8SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage8SegsMax.setStatus("mandatory")
_WfMibHeapPage9Size_Type = Integer32
_WfMibHeapPage9Size_Object = MibTableColumn
wfMibHeapPage9Size = _WfMibHeapPage9Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 33),
    _WfMibHeapPage9Size_Type()
)
wfMibHeapPage9Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage9Size.setStatus("mandatory")
_WfMibHeapPage9SegsFree_Type = Integer32
_WfMibHeapPage9SegsFree_Object = MibTableColumn
wfMibHeapPage9SegsFree = _WfMibHeapPage9SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 34),
    _WfMibHeapPage9SegsFree_Type()
)
wfMibHeapPage9SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage9SegsFree.setStatus("mandatory")
_WfMibHeapPage9SegsMax_Type = Integer32
_WfMibHeapPage9SegsMax_Object = MibTableColumn
wfMibHeapPage9SegsMax = _WfMibHeapPage9SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 35),
    _WfMibHeapPage9SegsMax_Type()
)
wfMibHeapPage9SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage9SegsMax.setStatus("mandatory")
_WfMibHeapPage10Size_Type = Integer32
_WfMibHeapPage10Size_Object = MibTableColumn
wfMibHeapPage10Size = _WfMibHeapPage10Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 36),
    _WfMibHeapPage10Size_Type()
)
wfMibHeapPage10Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage10Size.setStatus("mandatory")
_WfMibHeapPage10SegsFree_Type = Integer32
_WfMibHeapPage10SegsFree_Object = MibTableColumn
wfMibHeapPage10SegsFree = _WfMibHeapPage10SegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 37),
    _WfMibHeapPage10SegsFree_Type()
)
wfMibHeapPage10SegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage10SegsFree.setStatus("mandatory")
_WfMibHeapPage10SegsMax_Type = Integer32
_WfMibHeapPage10SegsMax_Object = MibTableColumn
wfMibHeapPage10SegsMax = _WfMibHeapPage10SegsMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7, 2, 1, 38),
    _WfMibHeapPage10SegsMax_Type()
)
wfMibHeapPage10SegsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMibHeapPage10SegsMax.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-MIB-HEAP-STATS-MIB",
    **{"wfMibHeapTable": wfMibHeapTable,
       "wfMibHeapEntry": wfMibHeapEntry,
       "wfMibHeapSlot": wfMibHeapSlot,
       "wfMibHeapMemorySize": wfMibHeapMemorySize,
       "wfMibHeapBoundrySize": wfMibHeapBoundrySize,
       "wfMibHeapPageSize": wfMibHeapPageSize,
       "wfMibHeapTotalPages": wfMibHeapTotalPages,
       "wfMibHeapTotalSegs": wfMibHeapTotalSegs,
       "wfMibHeapSegsFree": wfMibHeapSegsFree,
       "wfMibHeapSmlstSeg": wfMibHeapSmlstSeg,
       "wfMibHeapLrgstSeg": wfMibHeapLrgstSeg,
       "wfMibHeapStartSize": wfMibHeapStartSize,
       "wfMibHeapSize1": wfMibHeapSize1,
       "wfMibHeapSize1SegsFree": wfMibHeapSize1SegsFree,
       "wfMibHeapSize1SegsTotal": wfMibHeapSize1SegsTotal,
       "wfMibHeapSize1Pages": wfMibHeapSize1Pages,
       "wfMibHeapSize2": wfMibHeapSize2,
       "wfMibHeapSize2SegsFree": wfMibHeapSize2SegsFree,
       "wfMibHeapSize2SegsTotal": wfMibHeapSize2SegsTotal,
       "wfMibHeapSize2Pages": wfMibHeapSize2Pages,
       "wfMibHeapSize3": wfMibHeapSize3,
       "wfMibHeapSize3SegsFree": wfMibHeapSize3SegsFree,
       "wfMibHeapSize3SegsTotal": wfMibHeapSize3SegsTotal,
       "wfMibHeapSize3Pages": wfMibHeapSize3Pages,
       "wfMibHeapSize4": wfMibHeapSize4,
       "wfMibHeapSize4SegsFree": wfMibHeapSize4SegsFree,
       "wfMibHeapSize4SegsTotal": wfMibHeapSize4SegsTotal,
       "wfMibHeapSize4Pages": wfMibHeapSize4Pages,
       "wfMibHeapSize5": wfMibHeapSize5,
       "wfMibHeapSize5SegsFree": wfMibHeapSize5SegsFree,
       "wfMibHeapSize5SegsTotal": wfMibHeapSize5SegsTotal,
       "wfMibHeapSize5Pages": wfMibHeapSize5Pages,
       "wfMibHeapSize6": wfMibHeapSize6,
       "wfMibHeapSize6SegsFree": wfMibHeapSize6SegsFree,
       "wfMibHeapSize6SegsTotal": wfMibHeapSize6SegsTotal,
       "wfMibHeapSize6Pages": wfMibHeapSize6Pages,
       "wfMibHeapSize7": wfMibHeapSize7,
       "wfMibHeapSize7SegsFree": wfMibHeapSize7SegsFree,
       "wfMibHeapSize7SegsTotal": wfMibHeapSize7SegsTotal,
       "wfMibHeapSize7Pages": wfMibHeapSize7Pages,
       "wfMibHeapSize8": wfMibHeapSize8,
       "wfMibHeapSize8SegsFree": wfMibHeapSize8SegsFree,
       "wfMibHeapSize8SegsTotal": wfMibHeapSize8SegsTotal,
       "wfMibHeapSize8Pages": wfMibHeapSize8Pages,
       "wfMibHeapSize9": wfMibHeapSize9,
       "wfMibHeapSize9SegsFree": wfMibHeapSize9SegsFree,
       "wfMibHeapSize9SegsTotal": wfMibHeapSize9SegsTotal,
       "wfMibHeapSize9Pages": wfMibHeapSize9Pages,
       "wfMibHeapSize10": wfMibHeapSize10,
       "wfMibHeapSize10SegsFree": wfMibHeapSize10SegsFree,
       "wfMibHeapSize10SegsTotal": wfMibHeapSize10SegsTotal,
       "wfMibHeapSize10Pages": wfMibHeapSize10Pages,
       "wfMibHeapPageTable": wfMibHeapPageTable,
       "wfMibHeapPageEntry": wfMibHeapPageEntry,
       "wfMibHeapPageSlot": wfMibHeapPageSlot,
       "wfMibHeapPageListOffset": wfMibHeapPageListOffset,
       "wfMibHeapPageSegSize": wfMibHeapPageSegSize,
       "wfMibHeapPageTotal": wfMibHeapPageTotal,
       "wfMibHeapPageMemoryTotal": wfMibHeapPageMemoryTotal,
       "wfMibHeapPageSegsTotal": wfMibHeapPageSegsTotal,
       "wfMibHeapPageSegsAllocd": wfMibHeapPageSegsAllocd,
       "wfMibHeapPageSegsFree": wfMibHeapPageSegsFree,
       "wfMibHeapPage1Size": wfMibHeapPage1Size,
       "wfMibHeapPage1SegsFree": wfMibHeapPage1SegsFree,
       "wfMibHeapPage1SegsMax": wfMibHeapPage1SegsMax,
       "wfMibHeapPage2Size": wfMibHeapPage2Size,
       "wfMibHeapPage2SegsFree": wfMibHeapPage2SegsFree,
       "wfMibHeapPage2SegsMax": wfMibHeapPage2SegsMax,
       "wfMibHeapPage3Size": wfMibHeapPage3Size,
       "wfMibHeapPage3SegsFree": wfMibHeapPage3SegsFree,
       "wfMibHeapPage3SegsMax": wfMibHeapPage3SegsMax,
       "wfMibHeapPage4Size": wfMibHeapPage4Size,
       "wfMibHeapPage4SegsFree": wfMibHeapPage4SegsFree,
       "wfMibHeapPage4SegsMax": wfMibHeapPage4SegsMax,
       "wfMibHeapPage5Size": wfMibHeapPage5Size,
       "wfMibHeapPage5SegsFree": wfMibHeapPage5SegsFree,
       "wfMibHeapPage5SegsMax": wfMibHeapPage5SegsMax,
       "wfMibHeapPage6PageSize": wfMibHeapPage6PageSize,
       "wfMibHeapPage6SegsFree": wfMibHeapPage6SegsFree,
       "wfMibHeapPage6SegsMax": wfMibHeapPage6SegsMax,
       "wfMibHeapPage7Size": wfMibHeapPage7Size,
       "wfMibHeapPage7SegsFree": wfMibHeapPage7SegsFree,
       "wfMibHeapPage7SegsMax": wfMibHeapPage7SegsMax,
       "wfMibHeapPage8Size": wfMibHeapPage8Size,
       "wfMibHeapPage8SegsFree": wfMibHeapPage8SegsFree,
       "wfMibHeapPage8SegsMax": wfMibHeapPage8SegsMax,
       "wfMibHeapPage9Size": wfMibHeapPage9Size,
       "wfMibHeapPage9SegsFree": wfMibHeapPage9SegsFree,
       "wfMibHeapPage9SegsMax": wfMibHeapPage9SegsMax,
       "wfMibHeapPage10Size": wfMibHeapPage10Size,
       "wfMibHeapPage10SegsFree": wfMibHeapPage10SegsFree,
       "wfMibHeapPage10SegsMax": wfMibHeapPage10SegsMax}
)
