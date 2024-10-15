# SNMP MIB module (VERILINK-ENTERPRISE-NCMGENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMGENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:14 2024
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

(ncm_generic,) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-generic")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcmNodeCurrTable_Object = MibTable
ncmNodeCurrTable = _NcmNodeCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1001)
)
if mibBuilder.loadTexts:
    ncmNodeCurrTable.setStatus("mandatory")
_NcmNodeCurrEntry_Object = MibTableRow
ncmNodeCurrEntry = _NcmNodeCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1001, 1)
)
ncmNodeCurrEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmNodeCurrIndex"),
)
if mibBuilder.loadTexts:
    ncmNodeCurrEntry.setStatus("mandatory")


class _NcmNodeCurrIndex_Type(Integer32):
    """Custom type ncmNodeCurrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmNodeCurrIndex_Type.__name__ = "Integer32"
_NcmNodeCurrIndex_Object = MibTableColumn
ncmNodeCurrIndex = _NcmNodeCurrIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1001, 1, 1),
    _NcmNodeCurrIndex_Type()
)
ncmNodeCurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNodeCurrIndex.setStatus("mandatory")
_NcmNodeCurrAddress_Type = DisplayString
_NcmNodeCurrAddress_Object = MibTableColumn
ncmNodeCurrAddress = _NcmNodeCurrAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1001, 1, 2),
    _NcmNodeCurrAddress_Type()
)
ncmNodeCurrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNodeCurrAddress.setStatus("mandatory")


class _NcmActiveNodeStatus_Type(Integer32):
    """Custom type ncmActiveNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_NcmActiveNodeStatus_Type.__name__ = "Integer32"
_NcmActiveNodeStatus_Object = MibTableColumn
ncmActiveNodeStatus = _NcmActiveNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1001, 1, 3),
    _NcmActiveNodeStatus_Type()
)
ncmActiveNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmActiveNodeStatus.setStatus("mandatory")
_NcmNodeInfoTable_Object = MibTable
ncmNodeInfoTable = _NcmNodeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002)
)
if mibBuilder.loadTexts:
    ncmNodeInfoTable.setStatus("mandatory")
_NcmNodeInfoEntry_Object = MibTableRow
ncmNodeInfoEntry = _NcmNodeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002, 1)
)
ncmNodeInfoEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmNodeIndex"),
)
if mibBuilder.loadTexts:
    ncmNodeInfoEntry.setStatus("mandatory")


class _NcmNodeIndex_Type(Integer32):
    """Custom type ncmNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmNodeIndex_Type.__name__ = "Integer32"
_NcmNodeIndex_Object = MibTableColumn
ncmNodeIndex = _NcmNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002, 1, 1),
    _NcmNodeIndex_Type()
)
ncmNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNodeIndex.setStatus("mandatory")
_NcmNodeAddress_Type = DisplayString
_NcmNodeAddress_Object = MibTableColumn
ncmNodeAddress = _NcmNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002, 1, 2),
    _NcmNodeAddress_Type()
)
ncmNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNodeAddress.setStatus("mandatory")
_NcmTime_Type = DisplayString
_NcmTime_Object = MibTableColumn
ncmTime = _NcmTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002, 1, 3),
    _NcmTime_Type()
)
ncmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmTime.setStatus("mandatory")


class _NcmDate_Type(DisplayString):
    """Custom type ncmDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmDate_Type.__name__ = "DisplayString"
_NcmDate_Object = MibTableColumn
ncmDate = _NcmDate_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002, 1, 4),
    _NcmDate_Type()
)
ncmDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDate.setStatus("mandatory")
_NcmNodeShelf_Type = Integer32
_NcmNodeShelf_Object = MibTableColumn
ncmNodeShelf = _NcmNodeShelf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002, 1, 5),
    _NcmNodeShelf_Type()
)
ncmNodeShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNodeShelf.setStatus("mandatory")
_NcmNodeID_Type = Integer32
_NcmNodeID_Object = MibTableColumn
ncmNodeID = _NcmNodeID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002, 1, 6),
    _NcmNodeID_Type()
)
ncmNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNodeID.setStatus("mandatory")
_NcmControllerEqID_Type = Integer32
_NcmControllerEqID_Object = MibTableColumn
ncmControllerEqID = _NcmControllerEqID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1002, 1, 7),
    _NcmControllerEqID_Type()
)
ncmControllerEqID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmControllerEqID.setStatus("mandatory")
_NcmShelfInfoTable_Object = MibTable
ncmShelfInfoTable = _NcmShelfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1003)
)
if mibBuilder.loadTexts:
    ncmShelfInfoTable.setStatus("mandatory")
_NcmShelfInfoEntry_Object = MibTableRow
ncmShelfInfoEntry = _NcmShelfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1003, 1)
)
ncmShelfInfoEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmShelfNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmShelfIndex"),
)
if mibBuilder.loadTexts:
    ncmShelfInfoEntry.setStatus("mandatory")


class _NcmShelfNIDIndex_Type(Integer32):
    """Custom type ncmShelfNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmShelfNIDIndex_Type.__name__ = "Integer32"
_NcmShelfNIDIndex_Object = MibTableColumn
ncmShelfNIDIndex = _NcmShelfNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1003, 1, 1),
    _NcmShelfNIDIndex_Type()
)
ncmShelfNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfNIDIndex.setStatus("mandatory")


class _NcmShelfIndex_Type(Integer32):
    """Custom type ncmShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmShelfIndex_Type.__name__ = "Integer32"
_NcmShelfIndex_Object = MibTableColumn
ncmShelfIndex = _NcmShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1003, 1, 2),
    _NcmShelfIndex_Type()
)
ncmShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfIndex.setStatus("mandatory")
_NcmShelfNumber_Type = Integer32
_NcmShelfNumber_Object = MibTableColumn
ncmShelfNumber = _NcmShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1003, 1, 3),
    _NcmShelfNumber_Type()
)
ncmShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfNumber.setStatus("mandatory")


class _NcmShelfHardware_Type(Integer32):
    """Custom type ncmShelfHardware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              52,
              54)
        )
    )
    namedValues = NamedValues(
        *(("duallineshelf", 2),
          ("multilineshelf", 3),
          ("nb-2200-4ilineshelf", 10),
          ("nb-2200-4iqlineshelf", 54),
          ("nb-2200lineshelf", 4),
          ("nb-2200qlineshelf", 52),
          ("uninstalled", 1))
    )


_NcmShelfHardware_Type.__name__ = "Integer32"
_NcmShelfHardware_Object = MibTableColumn
ncmShelfHardware = _NcmShelfHardware_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1003, 1, 4),
    _NcmShelfHardware_Type()
)
ncmShelfHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfHardware.setStatus("mandatory")
_NcmNumberofCards_Type = Integer32
_NcmNumberofCards_Object = MibTableColumn
ncmNumberofCards = _NcmNumberofCards_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1003, 1, 5),
    _NcmNumberofCards_Type()
)
ncmNumberofCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNumberofCards.setStatus("mandatory")
_NcmListCardsInShelf_Type = DisplayString
_NcmListCardsInShelf_Object = MibTableColumn
ncmListCardsInShelf = _NcmListCardsInShelf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1003, 1, 6),
    _NcmListCardsInShelf_Type()
)
ncmListCardsInShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListCardsInShelf.setStatus("mandatory")
_NcmCardInfoTable_Object = MibTable
ncmCardInfoTable = _NcmCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1004)
)
if mibBuilder.loadTexts:
    ncmCardInfoTable.setStatus("mandatory")
_NcmCardInfoEntry_Object = MibTableRow
ncmCardInfoEntry = _NcmCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1004, 1)
)
ncmCardInfoEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmCardNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmCardIndex"),
)
if mibBuilder.loadTexts:
    ncmCardInfoEntry.setStatus("mandatory")


class _NcmCardNIDIndex_Type(Integer32):
    """Custom type ncmCardNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmCardNIDIndex_Type.__name__ = "Integer32"
_NcmCardNIDIndex_Object = MibTableColumn
ncmCardNIDIndex = _NcmCardNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1004, 1, 1),
    _NcmCardNIDIndex_Type()
)
ncmCardNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCardNIDIndex.setStatus("mandatory")


class _NcmCardIndex_Type(Integer32):
    """Custom type ncmCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmCardIndex_Type.__name__ = "Integer32"
_NcmCardIndex_Object = MibTableColumn
ncmCardIndex = _NcmCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1004, 1, 2),
    _NcmCardIndex_Type()
)
ncmCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCardIndex.setStatus("mandatory")


class _NcmFirmwareType_Type(Integer32):
    """Custom type ncmFirmwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              60,
              61,
              62,
              63,
              64,
              77,
              80,
              81,
              82,
              83,
              85,
              86,
              87,
              88,
              96,
              97,
              98,
              112,
              113,
              114,
              115,
              116,
              117,
              119)
        )
    )
    namedValues = NamedValues(
        *(("ace-dual-e1-firmware", 87),
          ("ace-dual-t1-firmware", 86),
          ("ace-fw-isdn-E1", 113),
          ("ace-fw-isdn-T1", 112),
          ("card-ct1-csu", 57),
          ("card-ct1-dsu", 58),
          ("card-ct1-sam", 56),
          ("card-ct1-tu", 60),
          ("card-sigma-aps", 63),
          ("card-sigma-csu", 49),
          ("card-sigma-ddsu", 51),
          ("card-sigma-diu-2144", 97),
          ("card-sigma-dsu", 50),
          ("card-sigma-dsu-2131", 98),
          ("card-sigma-dsu-dds", 61),
          ("card-sigma-dsu-dsu", 62),
          ("card-sigma-idc", 55),
          ("card-sigma-idc-sam", 54),
          ("card-sigma-sam", 48),
          ("card-sigma-sam-1", 64),
          ("card-sigma-smds", 53),
          ("card-sigma-tu", 52),
          ("card-sigma-vcu", 77),
          ("ds3-cdsu-firmware", 88),
          ("dual-port-ds3", 116),
          ("e1-ace-firmware", 80),
          ("imux-2164-firmware", 119),
          ("imux-tabs-firmware", 85),
          ("m13-2113-firmware", 117),
          ("ncm-t1-firmware", 96),
          ("quad-E1-ace-firmware", 83),
          ("quad-T1-ace-firmware", 82),
          ("quad-fw-isdn-E1", 115),
          ("quad-fw-isdn-T1", 114),
          ("t1-ace-firmware", 81))
    )


_NcmFirmwareType_Type.__name__ = "Integer32"
_NcmFirmwareType_Object = MibTableColumn
ncmFirmwareType = _NcmFirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1004, 1, 3),
    _NcmFirmwareType_Type()
)
ncmFirmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmFirmwareType.setStatus("mandatory")


class _NcmCimType_Type(Integer32):
    """Custom type ncmCimType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              20,
              21,
              22,
              32,
              33,
              34,
              35,
              36,
              37,
              48,
              49,
              50,
              51,
              52,
              56,
              62,
              64,
              65,
              82,
              83,
              88,
              89,
              90,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cim-2001-e1", 16),
          ("cim-2002-e1", 17),
          ("cim-2003-e1", 18),
          ("cim-2004-e1", 19),
          ("cim-2005-e1", 20),
          ("cim-2006-e1", 21),
          ("cim-2061", 56),
          ("cim-2065", 37),
          ("cim-2101-t1", 32),
          ("cim-2102-t1", 33),
          ("cim-2162", 36),
          ("cim-2164", 34),
          ("cim-2168", 35),
          ("cim-dim-2035", 88),
          ("cim-dim-2232", 90),
          ("cim-dim-2435", 82),
          ("cim-dim-2449", 89),
          ("cim-dim-2530", 83),
          ("cim-eia530", 51),
          ("cim-eia530A", 50),
          ("cim-hsm-2113", 62),
          ("cim-hssi", 48),
          ("cim-nim-2000", 22),
          ("cim-rs449", 52),
          ("cim-uninstall", 255),
          ("cim-v35", 49),
          ("cim-vcu-2W", 65),
          ("cim-vcu-4W", 64))
    )


_NcmCimType_Type.__name__ = "Integer32"
_NcmCimType_Object = MibTableColumn
ncmCimType = _NcmCimType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1004, 1, 4),
    _NcmCimType_Type()
)
ncmCimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCimType.setStatus("mandatory")


class _NcmClearCardInfo_Type(Integer32):
    """Custom type ncmClearCardInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmClearCardInfo_Type.__name__ = "Integer32"
_NcmClearCardInfo_Object = MibTableColumn
ncmClearCardInfo = _NcmClearCardInfo_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1004, 1, 5),
    _NcmClearCardInfo_Type()
)
ncmClearCardInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmClearCardInfo.setStatus("mandatory")
_NcmShelfSyncSourceTable_Object = MibTable
ncmShelfSyncSourceTable = _NcmShelfSyncSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005)
)
if mibBuilder.loadTexts:
    ncmShelfSyncSourceTable.setStatus("mandatory")
_NcmShelfSyncSourceEntry_Object = MibTableRow
ncmShelfSyncSourceEntry = _NcmShelfSyncSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1)
)
ncmShelfSyncSourceEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmShelfSyncNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmShelfSyncSourceIndex"),
)
if mibBuilder.loadTexts:
    ncmShelfSyncSourceEntry.setStatus("mandatory")


class _NcmShelfSyncNIDIndex_Type(Integer32):
    """Custom type ncmShelfSyncNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmShelfSyncNIDIndex_Type.__name__ = "Integer32"
_NcmShelfSyncNIDIndex_Object = MibTableColumn
ncmShelfSyncNIDIndex = _NcmShelfSyncNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 1),
    _NcmShelfSyncNIDIndex_Type()
)
ncmShelfSyncNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfSyncNIDIndex.setStatus("mandatory")


class _NcmShelfSyncSourceIndex_Type(Integer32):
    """Custom type ncmShelfSyncSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmShelfSyncSourceIndex_Type.__name__ = "Integer32"
_NcmShelfSyncSourceIndex_Object = MibTableColumn
ncmShelfSyncSourceIndex = _NcmShelfSyncSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 2),
    _NcmShelfSyncSourceIndex_Type()
)
ncmShelfSyncSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfSyncSourceIndex.setStatus("mandatory")
_NcmSourceOneShelfNum_Type = Integer32
_NcmSourceOneShelfNum_Object = MibTableColumn
ncmSourceOneShelfNum = _NcmSourceOneShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 3),
    _NcmSourceOneShelfNum_Type()
)
ncmSourceOneShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceOneShelfNum.setStatus("mandatory")
_NcmSourceOneCardNum_Type = Integer32
_NcmSourceOneCardNum_Object = MibTableColumn
ncmSourceOneCardNum = _NcmSourceOneCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 4),
    _NcmSourceOneCardNum_Type()
)
ncmSourceOneCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceOneCardNum.setStatus("mandatory")


class _NcmSourceOneClockRef_Type(Integer32):
    """Custom type ncmSourceOneClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("ncmdata-port1", 9),
          ("ncmdata-port2", 10),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmSourceOneClockRef_Type.__name__ = "Integer32"
_NcmSourceOneClockRef_Object = MibTableColumn
ncmSourceOneClockRef = _NcmSourceOneClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 5),
    _NcmSourceOneClockRef_Type()
)
ncmSourceOneClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceOneClockRef.setStatus("mandatory")


class _NcmAutoRestore1_Type(Integer32):
    """Custom type ncmAutoRestore1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmAutoRestore1_Type.__name__ = "Integer32"
_NcmAutoRestore1_Object = MibTableColumn
ncmAutoRestore1 = _NcmAutoRestore1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 6),
    _NcmAutoRestore1_Type()
)
ncmAutoRestore1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAutoRestore1.setStatus("mandatory")
_NcmSourceTwoShelfNum_Type = Integer32
_NcmSourceTwoShelfNum_Object = MibTableColumn
ncmSourceTwoShelfNum = _NcmSourceTwoShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 7),
    _NcmSourceTwoShelfNum_Type()
)
ncmSourceTwoShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceTwoShelfNum.setStatus("mandatory")
_NcmSourceTwoCardNum_Type = Integer32
_NcmSourceTwoCardNum_Object = MibTableColumn
ncmSourceTwoCardNum = _NcmSourceTwoCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 8),
    _NcmSourceTwoCardNum_Type()
)
ncmSourceTwoCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceTwoCardNum.setStatus("mandatory")


class _NcmSourceTwoClockRef_Type(Integer32):
    """Custom type ncmSourceTwoClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("ncmdata-port1", 9),
          ("ncmdata-port2", 10),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmSourceTwoClockRef_Type.__name__ = "Integer32"
_NcmSourceTwoClockRef_Object = MibTableColumn
ncmSourceTwoClockRef = _NcmSourceTwoClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 9),
    _NcmSourceTwoClockRef_Type()
)
ncmSourceTwoClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceTwoClockRef.setStatus("mandatory")


class _NcmAutoRestore2_Type(Integer32):
    """Custom type ncmAutoRestore2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmAutoRestore2_Type.__name__ = "Integer32"
_NcmAutoRestore2_Object = MibTableColumn
ncmAutoRestore2 = _NcmAutoRestore2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 10),
    _NcmAutoRestore2_Type()
)
ncmAutoRestore2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAutoRestore2.setStatus("mandatory")
_NcmSourceThreeShelfNum_Type = Integer32
_NcmSourceThreeShelfNum_Object = MibTableColumn
ncmSourceThreeShelfNum = _NcmSourceThreeShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 11),
    _NcmSourceThreeShelfNum_Type()
)
ncmSourceThreeShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceThreeShelfNum.setStatus("mandatory")
_NcmSourceThreeCardNum_Type = Integer32
_NcmSourceThreeCardNum_Object = MibTableColumn
ncmSourceThreeCardNum = _NcmSourceThreeCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 12),
    _NcmSourceThreeCardNum_Type()
)
ncmSourceThreeCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceThreeCardNum.setStatus("mandatory")


class _NcmSourceThreeClockRef_Type(Integer32):
    """Custom type ncmSourceThreeClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("ncmdata-port1", 9),
          ("ncmdata-port2", 10),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmSourceThreeClockRef_Type.__name__ = "Integer32"
_NcmSourceThreeClockRef_Object = MibTableColumn
ncmSourceThreeClockRef = _NcmSourceThreeClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 13),
    _NcmSourceThreeClockRef_Type()
)
ncmSourceThreeClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceThreeClockRef.setStatus("mandatory")


class _NcmAutoRestore3_Type(Integer32):
    """Custom type ncmAutoRestore3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmAutoRestore3_Type.__name__ = "Integer32"
_NcmAutoRestore3_Object = MibTableColumn
ncmAutoRestore3 = _NcmAutoRestore3_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 14),
    _NcmAutoRestore3_Type()
)
ncmAutoRestore3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAutoRestore3.setStatus("mandatory")


class _NcmShelfCurrentSyncSource_Type(Integer32):
    """Custom type ncmShelfCurrentSyncSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source1", 1),
          ("source2", 2),
          ("source3", 3))
    )


_NcmShelfCurrentSyncSource_Type.__name__ = "Integer32"
_NcmShelfCurrentSyncSource_Object = MibTableColumn
ncmShelfCurrentSyncSource = _NcmShelfCurrentSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1005, 1, 15),
    _NcmShelfCurrentSyncSource_Type()
)
ncmShelfCurrentSyncSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmShelfCurrentSyncSource.setStatus("mandatory")
_NcmCardSyncSourceTable_Object = MibTable
ncmCardSyncSourceTable = _NcmCardSyncSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006)
)
if mibBuilder.loadTexts:
    ncmCardSyncSourceTable.setStatus("mandatory")
_NcmCardSyncSourceEntry_Object = MibTableRow
ncmCardSyncSourceEntry = _NcmCardSyncSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1)
)
ncmCardSyncSourceEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmCardSyncNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmCardSyncSourceIndex"),
)
if mibBuilder.loadTexts:
    ncmCardSyncSourceEntry.setStatus("mandatory")


class _NcmCardSyncNIDIndex_Type(Integer32):
    """Custom type ncmCardSyncNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmCardSyncNIDIndex_Type.__name__ = "Integer32"
_NcmCardSyncNIDIndex_Object = MibTableColumn
ncmCardSyncNIDIndex = _NcmCardSyncNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 1),
    _NcmCardSyncNIDIndex_Type()
)
ncmCardSyncNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCardSyncNIDIndex.setStatus("mandatory")


class _NcmCardSyncSourceIndex_Type(Integer32):
    """Custom type ncmCardSyncSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmCardSyncSourceIndex_Type.__name__ = "Integer32"
_NcmCardSyncSourceIndex_Object = MibTableColumn
ncmCardSyncSourceIndex = _NcmCardSyncSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 2),
    _NcmCardSyncSourceIndex_Type()
)
ncmCardSyncSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCardSyncSourceIndex.setStatus("mandatory")


class _NcmCardReceiveClockFromShelf_Type(Integer32):
    """Custom type ncmCardReceiveClockFromShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmCardReceiveClockFromShelf_Type.__name__ = "Integer32"
_NcmCardReceiveClockFromShelf_Object = MibTableColumn
ncmCardReceiveClockFromShelf = _NcmCardReceiveClockFromShelf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 3),
    _NcmCardReceiveClockFromShelf_Type()
)
ncmCardReceiveClockFromShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardReceiveClockFromShelf.setStatus("mandatory")
_NcmCardSourceOneShelfNum_Type = Integer32
_NcmCardSourceOneShelfNum_Object = MibTableColumn
ncmCardSourceOneShelfNum = _NcmCardSourceOneShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 4),
    _NcmCardSourceOneShelfNum_Type()
)
ncmCardSourceOneShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceOneShelfNum.setStatus("mandatory")
_NcmCardSourceOneCardNum_Type = Integer32
_NcmCardSourceOneCardNum_Object = MibTableColumn
ncmCardSourceOneCardNum = _NcmCardSourceOneCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 5),
    _NcmCardSourceOneCardNum_Type()
)
ncmCardSourceOneCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceOneCardNum.setStatus("mandatory")


class _NcmCardSourceOneClockRef_Type(Integer32):
    """Custom type ncmCardSourceOneClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("data-port1", 9),
          ("data-port2", 10),
          ("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmCardSourceOneClockRef_Type.__name__ = "Integer32"
_NcmCardSourceOneClockRef_Object = MibTableColumn
ncmCardSourceOneClockRef = _NcmCardSourceOneClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 6),
    _NcmCardSourceOneClockRef_Type()
)
ncmCardSourceOneClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceOneClockRef.setStatus("mandatory")


class _NcmCardAutoRestore1_Type(Integer32):
    """Custom type ncmCardAutoRestore1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmCardAutoRestore1_Type.__name__ = "Integer32"
_NcmCardAutoRestore1_Object = MibTableColumn
ncmCardAutoRestore1 = _NcmCardAutoRestore1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 7),
    _NcmCardAutoRestore1_Type()
)
ncmCardAutoRestore1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardAutoRestore1.setStatus("mandatory")
_NcmCardSourceTwoShelfNum_Type = Integer32
_NcmCardSourceTwoShelfNum_Object = MibTableColumn
ncmCardSourceTwoShelfNum = _NcmCardSourceTwoShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 8),
    _NcmCardSourceTwoShelfNum_Type()
)
ncmCardSourceTwoShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceTwoShelfNum.setStatus("mandatory")
_NcmCardSourceTwoCardNum_Type = Integer32
_NcmCardSourceTwoCardNum_Object = MibTableColumn
ncmCardSourceTwoCardNum = _NcmCardSourceTwoCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 9),
    _NcmCardSourceTwoCardNum_Type()
)
ncmCardSourceTwoCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceTwoCardNum.setStatus("mandatory")


class _NcmCardSourceTwoClockRef_Type(Integer32):
    """Custom type ncmCardSourceTwoClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("data-port1", 9),
          ("data-port2", 10),
          ("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmCardSourceTwoClockRef_Type.__name__ = "Integer32"
_NcmCardSourceTwoClockRef_Object = MibTableColumn
ncmCardSourceTwoClockRef = _NcmCardSourceTwoClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 10),
    _NcmCardSourceTwoClockRef_Type()
)
ncmCardSourceTwoClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceTwoClockRef.setStatus("mandatory")


class _NcmCardAutoRestore2_Type(Integer32):
    """Custom type ncmCardAutoRestore2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmCardAutoRestore2_Type.__name__ = "Integer32"
_NcmCardAutoRestore2_Object = MibTableColumn
ncmCardAutoRestore2 = _NcmCardAutoRestore2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 11),
    _NcmCardAutoRestore2_Type()
)
ncmCardAutoRestore2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardAutoRestore2.setStatus("mandatory")
_NcmCardSourceThreeShelfNum_Type = Integer32
_NcmCardSourceThreeShelfNum_Object = MibTableColumn
ncmCardSourceThreeShelfNum = _NcmCardSourceThreeShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 12),
    _NcmCardSourceThreeShelfNum_Type()
)
ncmCardSourceThreeShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceThreeShelfNum.setStatus("mandatory")
_NcmCardSourceThreeCardNum_Type = Integer32
_NcmCardSourceThreeCardNum_Object = MibTableColumn
ncmCardSourceThreeCardNum = _NcmCardSourceThreeCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 13),
    _NcmCardSourceThreeCardNum_Type()
)
ncmCardSourceThreeCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceThreeCardNum.setStatus("mandatory")


class _NcmCardSourceThreeClockRef_Type(Integer32):
    """Custom type ncmCardSourceThreeClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("data-port1", 9),
          ("data-port2", 10),
          ("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmCardSourceThreeClockRef_Type.__name__ = "Integer32"
_NcmCardSourceThreeClockRef_Object = MibTableColumn
ncmCardSourceThreeClockRef = _NcmCardSourceThreeClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 14),
    _NcmCardSourceThreeClockRef_Type()
)
ncmCardSourceThreeClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardSourceThreeClockRef.setStatus("mandatory")


class _NcmCardAutoRestore3_Type(Integer32):
    """Custom type ncmCardAutoRestore3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmCardAutoRestore3_Type.__name__ = "Integer32"
_NcmCardAutoRestore3_Object = MibTableColumn
ncmCardAutoRestore3 = _NcmCardAutoRestore3_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 15),
    _NcmCardAutoRestore3_Type()
)
ncmCardAutoRestore3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardAutoRestore3.setStatus("mandatory")


class _NcmCardCurrentSyncSource_Type(Integer32):
    """Custom type ncmCardCurrentSyncSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source1", 1),
          ("source2", 2),
          ("source3", 3))
    )


_NcmCardCurrentSyncSource_Type.__name__ = "Integer32"
_NcmCardCurrentSyncSource_Object = MibTableColumn
ncmCardCurrentSyncSource = _NcmCardCurrentSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1006, 1, 16),
    _NcmCardCurrentSyncSource_Type()
)
ncmCardCurrentSyncSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCardCurrentSyncSource.setStatus("mandatory")
_NcmIDPromTable_Object = MibTable
ncmIDPromTable = _NcmIDPromTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007)
)
if mibBuilder.loadTexts:
    ncmIDPromTable.setStatus("mandatory")
_NcmIDPromEntry_Object = MibTableRow
ncmIDPromEntry = _NcmIDPromEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1)
)
ncmIDPromEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmIDPromNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmIDPromIndex"),
)
if mibBuilder.loadTexts:
    ncmIDPromEntry.setStatus("mandatory")


class _NcmIDPromNIDIndex_Type(Integer32):
    """Custom type ncmIDPromNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmIDPromNIDIndex_Type.__name__ = "Integer32"
_NcmIDPromNIDIndex_Object = MibTableColumn
ncmIDPromNIDIndex = _NcmIDPromNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 1),
    _NcmIDPromNIDIndex_Type()
)
ncmIDPromNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmIDPromNIDIndex.setStatus("mandatory")


class _NcmIDPromIndex_Type(Integer32):
    """Custom type ncmIDPromIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmIDPromIndex_Type.__name__ = "Integer32"
_NcmIDPromIndex_Object = MibTableColumn
ncmIDPromIndex = _NcmIDPromIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 2),
    _NcmIDPromIndex_Type()
)
ncmIDPromIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmIDPromIndex.setStatus("mandatory")


class _NcmCardType_Type(Integer32):
    """Custom type ncmCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ace-card", 1),
          ("dual-csu", 3),
          ("quad-card-for-imux", 2))
    )


_NcmCardType_Type.__name__ = "Integer32"
_NcmCardType_Object = MibTableColumn
ncmCardType = _NcmCardType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 3),
    _NcmCardType_Type()
)
ncmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCardType.setStatus("mandatory")


class _NcmCardRevision_Type(DisplayString):
    """Custom type ncmCardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmCardRevision_Type.__name__ = "DisplayString"
_NcmCardRevision_Object = MibTableColumn
ncmCardRevision = _NcmCardRevision_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 4),
    _NcmCardRevision_Type()
)
ncmCardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCardRevision.setStatus("mandatory")


class _NcmCardDate_Type(DisplayString):
    """Custom type ncmCardDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmCardDate_Type.__name__ = "DisplayString"
_NcmCardDate_Object = MibTableColumn
ncmCardDate = _NcmCardDate_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 5),
    _NcmCardDate_Type()
)
ncmCardDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCardDate.setStatus("mandatory")


class _NcmCardSerialNumber_Type(DisplayString):
    """Custom type ncmCardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmCardSerialNumber_Type.__name__ = "DisplayString"
_NcmCardSerialNumber_Object = MibTableColumn
ncmCardSerialNumber = _NcmCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 6),
    _NcmCardSerialNumber_Type()
)
ncmCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCardSerialNumber.setStatus("mandatory")


class _NcmManufacturePartNumber_Type(DisplayString):
    """Custom type ncmManufacturePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmManufacturePartNumber_Type.__name__ = "DisplayString"
_NcmManufacturePartNumber_Object = MibTableColumn
ncmManufacturePartNumber = _NcmManufacturePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 7),
    _NcmManufacturePartNumber_Type()
)
ncmManufacturePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmManufacturePartNumber.setStatus("mandatory")


class _NcmVendorCageCode_Type(DisplayString):
    """Custom type ncmVendorCageCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmVendorCageCode_Type.__name__ = "DisplayString"
_NcmVendorCageCode_Object = MibTableColumn
ncmVendorCageCode = _NcmVendorCageCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 8),
    _NcmVendorCageCode_Type()
)
ncmVendorCageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmVendorCageCode.setStatus("mandatory")


class _NcmIDCimType_Type(Integer32):
    """Custom type ncmIDCimType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              20,
              21,
              22,
              32,
              33,
              34,
              35,
              36,
              37,
              56,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cIM-2164", 34),
          ("cIM-2168", 35),
          ("cIM-UNINSTALLED", 255),
          ("cIM29001", 37),
          ("cIM29002", 56),
          ("cIM29003", 36),
          ("cIM29004", 16),
          ("cIM29005", 17),
          ("cIM29006", 18),
          ("cIM29007", 19),
          ("cIM29008", 20),
          ("cIM29009", 21),
          ("cIM29010", 32),
          ("cIM29011", 33),
          ("nIM2000", 22))
    )


_NcmIDCimType_Type.__name__ = "Integer32"
_NcmIDCimType_Object = MibTableColumn
ncmIDCimType = _NcmIDCimType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 9),
    _NcmIDCimType_Type()
)
ncmIDCimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmIDCimType.setStatus("mandatory")


class _NcmCimRevision_Type(DisplayString):
    """Custom type ncmCimRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmCimRevision_Type.__name__ = "DisplayString"
_NcmCimRevision_Object = MibTableColumn
ncmCimRevision = _NcmCimRevision_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 10),
    _NcmCimRevision_Type()
)
ncmCimRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCimRevision.setStatus("mandatory")


class _NcmCimDate_Type(DisplayString):
    """Custom type ncmCimDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmCimDate_Type.__name__ = "DisplayString"
_NcmCimDate_Object = MibTableColumn
ncmCimDate = _NcmCimDate_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 11),
    _NcmCimDate_Type()
)
ncmCimDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCimDate.setStatus("mandatory")


class _NcmCimSerialNumber_Type(DisplayString):
    """Custom type ncmCimSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmCimSerialNumber_Type.__name__ = "DisplayString"
_NcmCimSerialNumber_Object = MibTableColumn
ncmCimSerialNumber = _NcmCimSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 12),
    _NcmCimSerialNumber_Type()
)
ncmCimSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCimSerialNumber.setStatus("mandatory")


class _NcmCimManufacturePartNumber_Type(DisplayString):
    """Custom type ncmCimManufacturePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmCimManufacturePartNumber_Type.__name__ = "DisplayString"
_NcmCimManufacturePartNumber_Object = MibTableColumn
ncmCimManufacturePartNumber = _NcmCimManufacturePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 13),
    _NcmCimManufacturePartNumber_Type()
)
ncmCimManufacturePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCimManufacturePartNumber.setStatus("mandatory")


class _NcmCimVendorCageCode_Type(DisplayString):
    """Custom type ncmCimVendorCageCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmCimVendorCageCode_Type.__name__ = "DisplayString"
_NcmCimVendorCageCode_Object = MibTableColumn
ncmCimVendorCageCode = _NcmCimVendorCageCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1007, 1, 14),
    _NcmCimVendorCageCode_Type()
)
ncmCimVendorCageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCimVendorCageCode.setStatus("mandatory")
_NcmE1PortConfigTable_Object = MibTable
ncmE1PortConfigTable = _NcmE1PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008)
)
if mibBuilder.loadTexts:
    ncmE1PortConfigTable.setStatus("mandatory")
_NcmE1PortConfigEntry_Object = MibTableRow
ncmE1PortConfigEntry = _NcmE1PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1)
)
ncmE1PortConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1ConfigNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1PortLineIndex"),
)
if mibBuilder.loadTexts:
    ncmE1PortConfigEntry.setStatus("mandatory")


class _NcmE1ConfigNIDIndex_Type(Integer32):
    """Custom type ncmE1ConfigNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1ConfigNIDIndex_Type.__name__ = "Integer32"
_NcmE1ConfigNIDIndex_Object = MibTableColumn
ncmE1ConfigNIDIndex = _NcmE1ConfigNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 1),
    _NcmE1ConfigNIDIndex_Type()
)
ncmE1ConfigNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1ConfigNIDIndex.setStatus("mandatory")


class _NcmE1PortLineIndex_Type(Integer32):
    """Custom type ncmE1PortLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1PortLineIndex_Type.__name__ = "Integer32"
_NcmE1PortLineIndex_Object = MibTableColumn
ncmE1PortLineIndex = _NcmE1PortLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 2),
    _NcmE1PortLineIndex_Type()
)
ncmE1PortLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLineIndex.setStatus("mandatory")


class _NcmE1PortCRC4_Type(Integer32):
    """Custom type ncmE1PortCRC4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmE1PortCRC4_Type.__name__ = "Integer32"
_NcmE1PortCRC4_Object = MibTableColumn
ncmE1PortCRC4 = _NcmE1PortCRC4_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 3),
    _NcmE1PortCRC4_Type()
)
ncmE1PortCRC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortCRC4.setStatus("mandatory")


class _NcmE1PortCarrierFailureAlarm_Type(Integer32):
    """Custom type ncmE1PortCarrierFailureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmE1PortCarrierFailureAlarm_Type.__name__ = "Integer32"
_NcmE1PortCarrierFailureAlarm_Object = MibTableColumn
ncmE1PortCarrierFailureAlarm = _NcmE1PortCarrierFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 4),
    _NcmE1PortCarrierFailureAlarm_Type()
)
ncmE1PortCarrierFailureAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortCarrierFailureAlarm.setStatus("mandatory")


class _NcmE1PortFaseAlarm_Type(Integer32):
    """Custom type ncmE1PortFaseAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_NcmE1PortFaseAlarm_Type.__name__ = "Integer32"
_NcmE1PortFaseAlarm_Object = MibTableColumn
ncmE1PortFaseAlarm = _NcmE1PortFaseAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 5),
    _NcmE1PortFaseAlarm_Type()
)
ncmE1PortFaseAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortFaseAlarm.setStatus("mandatory")


class _NcmE1PortInbandISDNEnableDisable_Type(Integer32):
    """Custom type ncmE1PortInbandISDNEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disablebothinbandisdn", 1),
          ("enableinband", 2),
          ("enableisdn", 3))
    )


_NcmE1PortInbandISDNEnableDisable_Type.__name__ = "Integer32"
_NcmE1PortInbandISDNEnableDisable_Object = MibTableColumn
ncmE1PortInbandISDNEnableDisable = _NcmE1PortInbandISDNEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 6),
    _NcmE1PortInbandISDNEnableDisable_Type()
)
ncmE1PortInbandISDNEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortInbandISDNEnableDisable.setStatus("mandatory")


class _NcmE1PortRepeaterLoopbackTimeoutEnable_Type(Integer32):
    """Custom type ncmE1PortRepeaterLoopbackTimeoutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmE1PortRepeaterLoopbackTimeoutEnable_Type.__name__ = "Integer32"
_NcmE1PortRepeaterLoopbackTimeoutEnable_Object = MibTableColumn
ncmE1PortRepeaterLoopbackTimeoutEnable = _NcmE1PortRepeaterLoopbackTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 7),
    _NcmE1PortRepeaterLoopbackTimeoutEnable_Type()
)
ncmE1PortRepeaterLoopbackTimeoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortRepeaterLoopbackTimeoutEnable.setStatus("mandatory")


class _NcmE1PortFraming_Type(Integer32):
    """Custom type ncmE1PortFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cAS", 1),
          ("cCS", 2),
          ("g703", 4),
          ("thirty-one-Ch", 3))
    )


_NcmE1PortFraming_Type.__name__ = "Integer32"
_NcmE1PortFraming_Object = MibTableColumn
ncmE1PortFraming = _NcmE1PortFraming_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 8),
    _NcmE1PortFraming_Type()
)
ncmE1PortFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortFraming.setStatus("mandatory")
_NcmE1PortRepeaterLoopbackTimeout_Type = Integer32
_NcmE1PortRepeaterLoopbackTimeout_Object = MibTableColumn
ncmE1PortRepeaterLoopbackTimeout = _NcmE1PortRepeaterLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 9),
    _NcmE1PortRepeaterLoopbackTimeout_Type()
)
ncmE1PortRepeaterLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortRepeaterLoopbackTimeout.setStatus("mandatory")
_NcmE1PortCarrierFailureAlarmDeclareTime_Type = Integer32
_NcmE1PortCarrierFailureAlarmDeclareTime_Object = MibTableColumn
ncmE1PortCarrierFailureAlarmDeclareTime = _NcmE1PortCarrierFailureAlarmDeclareTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 10),
    _NcmE1PortCarrierFailureAlarmDeclareTime_Type()
)
ncmE1PortCarrierFailureAlarmDeclareTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortCarrierFailureAlarmDeclareTime.setStatus("mandatory")


class _NcmE1PortServiceState_Type(Integer32):
    """Custom type ncmE1PortServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 2),
          ("out-of-service", 1))
    )


_NcmE1PortServiceState_Type.__name__ = "Integer32"
_NcmE1PortServiceState_Object = MibTableColumn
ncmE1PortServiceState = _NcmE1PortServiceState_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 11),
    _NcmE1PortServiceState_Type()
)
ncmE1PortServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortServiceState.setStatus("mandatory")
_NcmE1PortIdlePattern_Type = Integer32
_NcmE1PortIdlePattern_Object = MibTableColumn
ncmE1PortIdlePattern = _NcmE1PortIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 12),
    _NcmE1PortIdlePattern_Type()
)
ncmE1PortIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1PortIdlePattern.setStatus("mandatory")


class _NcmE1TimeSlot_Type(DisplayString):
    """Custom type ncmE1TimeSlot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmE1TimeSlot_Type.__name__ = "DisplayString"
_NcmE1TimeSlot_Object = MibTableColumn
ncmE1TimeSlot = _NcmE1TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 13),
    _NcmE1TimeSlot_Type()
)
ncmE1TimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TimeSlot.setStatus("mandatory")
_NcmE1TimeSlotSelect_Type = Integer32
_NcmE1TimeSlotSelect_Object = MibTableColumn
ncmE1TimeSlotSelect = _NcmE1TimeSlotSelect_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1008, 1, 14),
    _NcmE1TimeSlotSelect_Type()
)
ncmE1TimeSlotSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1TimeSlotSelect.setStatus("mandatory")
_NcmE1PortStatusTable_Object = MibTable
ncmE1PortStatusTable = _NcmE1PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009)
)
if mibBuilder.loadTexts:
    ncmE1PortStatusTable.setStatus("mandatory")
_NcmE1PortStatusEntry_Object = MibTableRow
ncmE1PortStatusEntry = _NcmE1PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1)
)
ncmE1PortStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1PortStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1PortStatusIndex"),
)
if mibBuilder.loadTexts:
    ncmE1PortStatusEntry.setStatus("mandatory")


class _NcmE1PortStatusNIDIndex_Type(Integer32):
    """Custom type ncmE1PortStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1PortStatusNIDIndex_Type.__name__ = "Integer32"
_NcmE1PortStatusNIDIndex_Object = MibTableColumn
ncmE1PortStatusNIDIndex = _NcmE1PortStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 1),
    _NcmE1PortStatusNIDIndex_Type()
)
ncmE1PortStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortStatusNIDIndex.setStatus("mandatory")


class _NcmE1PortStatusIndex_Type(Integer32):
    """Custom type ncmE1PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1PortStatusIndex_Type.__name__ = "Integer32"
_NcmE1PortStatusIndex_Object = MibTableColumn
ncmE1PortStatusIndex = _NcmE1PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 2),
    _NcmE1PortStatusIndex_Type()
)
ncmE1PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortStatusIndex.setStatus("mandatory")


class _NcmE1PortCRC4Error_Type(Integer32):
    """Custom type ncmE1PortCRC4Error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortCRC4Error_Type.__name__ = "Integer32"
_NcmE1PortCRC4Error_Object = MibTableColumn
ncmE1PortCRC4Error = _NcmE1PortCRC4Error_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 3),
    _NcmE1PortCRC4Error_Type()
)
ncmE1PortCRC4Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortCRC4Error.setStatus("mandatory")


class _NcmE1PortFramingSlip_Type(Integer32):
    """Custom type ncmE1PortFramingSlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortFramingSlip_Type.__name__ = "Integer32"
_NcmE1PortFramingSlip_Object = MibTableColumn
ncmE1PortFramingSlip = _NcmE1PortFramingSlip_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 4),
    _NcmE1PortFramingSlip_Type()
)
ncmE1PortFramingSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortFramingSlip.setStatus("mandatory")


class _NcmE1PortRAI_Type(Integer32):
    """Custom type ncmE1PortRAI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortRAI_Type.__name__ = "Integer32"
_NcmE1PortRAI_Object = MibTableColumn
ncmE1PortRAI = _NcmE1PortRAI_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 5),
    _NcmE1PortRAI_Type()
)
ncmE1PortRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortRAI.setStatus("mandatory")


class _NcmE1PortLOFA_Type(Integer32):
    """Custom type ncmE1PortLOFA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLOFA_Type.__name__ = "Integer32"
_NcmE1PortLOFA_Object = MibTableColumn
ncmE1PortLOFA = _NcmE1PortLOFA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 6),
    _NcmE1PortLOFA_Type()
)
ncmE1PortLOFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLOFA.setStatus("mandatory")


class _NcmE1PortAIS_Type(Integer32):
    """Custom type ncmE1PortAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortAIS_Type.__name__ = "Integer32"
_NcmE1PortAIS_Object = MibTableColumn
ncmE1PortAIS = _NcmE1PortAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 7),
    _NcmE1PortAIS_Type()
)
ncmE1PortAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortAIS.setStatus("mandatory")


class _NcmE1PortLOS_Type(Integer32):
    """Custom type ncmE1PortLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLOS_Type.__name__ = "Integer32"
_NcmE1PortLOS_Object = MibTableColumn
ncmE1PortLOS = _NcmE1PortLOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 8),
    _NcmE1PortLOS_Type()
)
ncmE1PortLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLOS.setStatus("mandatory")


class _NcmE1PortBPVThresholdExceeded_Type(Integer32):
    """Custom type ncmE1PortBPVThresholdExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortBPVThresholdExceeded_Type.__name__ = "Integer32"
_NcmE1PortBPVThresholdExceeded_Object = MibTableColumn
ncmE1PortBPVThresholdExceeded = _NcmE1PortBPVThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 9),
    _NcmE1PortBPVThresholdExceeded_Type()
)
ncmE1PortBPVThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortBPVThresholdExceeded.setStatus("mandatory")
_NcmE1BlockErrorCounter_Type = Gauge32
_NcmE1BlockErrorCounter_Object = MibTableColumn
ncmE1BlockErrorCounter = _NcmE1BlockErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 10),
    _NcmE1BlockErrorCounter_Type()
)
ncmE1BlockErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1BlockErrorCounter.setStatus("mandatory")


class _NcmE1CodeViolationMode_Type(Integer32):
    """Custom type ncmE1CodeViolationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("count-FEBE", 2),
          ("count-HDB3", 1))
    )


_NcmE1CodeViolationMode_Type.__name__ = "Integer32"
_NcmE1CodeViolationMode_Object = MibTableColumn
ncmE1CodeViolationMode = _NcmE1CodeViolationMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 11),
    _NcmE1CodeViolationMode_Type()
)
ncmE1CodeViolationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CodeViolationMode.setStatus("mandatory")
_NcmE1CurrentHDB3ORFEBEErrorCounts_Type = Gauge32
_NcmE1CurrentHDB3ORFEBEErrorCounts_Object = MibTableColumn
ncmE1CurrentHDB3ORFEBEErrorCounts = _NcmE1CurrentHDB3ORFEBEErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 12),
    _NcmE1CurrentHDB3ORFEBEErrorCounts_Type()
)
ncmE1CurrentHDB3ORFEBEErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentHDB3ORFEBEErrorCounts.setStatus("mandatory")
_NcmE1CurrentFrameErrorCounts_Type = Gauge32
_NcmE1CurrentFrameErrorCounts_Object = MibTableColumn
ncmE1CurrentFrameErrorCounts = _NcmE1CurrentFrameErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 13),
    _NcmE1CurrentFrameErrorCounts_Type()
)
ncmE1CurrentFrameErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentFrameErrorCounts.setStatus("mandatory")
_NcmE1CurrentCRC4ErrorCounts_Type = Gauge32
_NcmE1CurrentCRC4ErrorCounts_Object = MibTableColumn
ncmE1CurrentCRC4ErrorCounts = _NcmE1CurrentCRC4ErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 14),
    _NcmE1CurrentCRC4ErrorCounts_Type()
)
ncmE1CurrentCRC4ErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentCRC4ErrorCounts.setStatus("mandatory")


class _NcmE1ResetPerfCount_Type(Integer32):
    """Custom type ncmE1ResetPerfCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1ResetPerfCount_Type.__name__ = "Integer32"
_NcmE1ResetPerfCount_Object = MibTableColumn
ncmE1ResetPerfCount = _NcmE1ResetPerfCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 15),
    _NcmE1ResetPerfCount_Type()
)
ncmE1ResetPerfCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1ResetPerfCount.setStatus("mandatory")


class _NcmE1PortSendRAI_Type(Integer32):
    """Custom type ncmE1PortSendRAI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortSendRAI_Type.__name__ = "Integer32"
_NcmE1PortSendRAI_Object = MibTableColumn
ncmE1PortSendRAI = _NcmE1PortSendRAI_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 16),
    _NcmE1PortSendRAI_Type()
)
ncmE1PortSendRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortSendRAI.setStatus("mandatory")


class _NcmE1PortSendAIS_Type(Integer32):
    """Custom type ncmE1PortSendAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortSendAIS_Type.__name__ = "Integer32"
_NcmE1PortSendAIS_Object = MibTableColumn
ncmE1PortSendAIS = _NcmE1PortSendAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 17),
    _NcmE1PortSendAIS_Type()
)
ncmE1PortSendAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortSendAIS.setStatus("mandatory")


class _NcmE1PortRFA_Type(Integer32):
    """Custom type ncmE1PortRFA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortRFA_Type.__name__ = "Integer32"
_NcmE1PortRFA_Object = MibTableColumn
ncmE1PortRFA = _NcmE1PortRFA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 18),
    _NcmE1PortRFA_Type()
)
ncmE1PortRFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortRFA.setStatus("mandatory")


class _NcmE1PortBERThresholdExceeded_Type(Integer32):
    """Custom type ncmE1PortBERThresholdExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortBERThresholdExceeded_Type.__name__ = "Integer32"
_NcmE1PortBERThresholdExceeded_Object = MibTableColumn
ncmE1PortBERThresholdExceeded = _NcmE1PortBERThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 19),
    _NcmE1PortBERThresholdExceeded_Type()
)
ncmE1PortBERThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortBERThresholdExceeded.setStatus("mandatory")


class _NcmE1PortLLB_Type(Integer32):
    """Custom type ncmE1PortLLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLLB_Type.__name__ = "Integer32"
_NcmE1PortLLB_Object = MibTableColumn
ncmE1PortLLB = _NcmE1PortLLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 20),
    _NcmE1PortLLB_Type()
)
ncmE1PortLLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLLB.setStatus("mandatory")


class _NcmE1PortPLB_Type(Integer32):
    """Custom type ncmE1PortPLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortPLB_Type.__name__ = "Integer32"
_NcmE1PortPLB_Object = MibTableColumn
ncmE1PortPLB = _NcmE1PortPLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 21),
    _NcmE1PortPLB_Type()
)
ncmE1PortPLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortPLB.setStatus("mandatory")


class _NcmE1PortLOC_Type(Integer32):
    """Custom type ncmE1PortLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLOC_Type.__name__ = "Integer32"
_NcmE1PortLOC_Object = MibTableColumn
ncmE1PortLOC = _NcmE1PortLOC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 22),
    _NcmE1PortLOC_Type()
)
ncmE1PortLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLOC.setStatus("mandatory")


class _NcmE1PortTestPattern_Type(Integer32):
    """Custom type ncmE1PortTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all-ones", 9),
          ("all-zeros", 7),
          ("fifty-octets", 8),
          ("none", 1),
          ("one-in-8", 5),
          ("qRSS", 3),
          ("three-24", 2),
          ("two-n-15-1", 6),
          ("two-n-20-1", 4))
    )


_NcmE1PortTestPattern_Type.__name__ = "Integer32"
_NcmE1PortTestPattern_Object = MibTableColumn
ncmE1PortTestPattern = _NcmE1PortTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1009, 1, 23),
    _NcmE1PortTestPattern_Type()
)
ncmE1PortTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortTestPattern.setStatus("mandatory")
_NcmE1CurrentTable_Object = MibTable
ncmE1CurrentTable = _NcmE1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010)
)
if mibBuilder.loadTexts:
    ncmE1CurrentTable.setStatus("mandatory")
_NcmE1CurrentEntry_Object = MibTableRow
ncmE1CurrentEntry = _NcmE1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1)
)
ncmE1CurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1CurrentNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1CurrentIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1CurrentEndType"),
)
if mibBuilder.loadTexts:
    ncmE1CurrentEntry.setStatus("mandatory")


class _NcmE1CurrentNIDIndex_Type(Integer32):
    """Custom type ncmE1CurrentNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1CurrentNIDIndex_Type.__name__ = "Integer32"
_NcmE1CurrentNIDIndex_Object = MibTableColumn
ncmE1CurrentNIDIndex = _NcmE1CurrentNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 1),
    _NcmE1CurrentNIDIndex_Type()
)
ncmE1CurrentNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentNIDIndex.setStatus("mandatory")


class _NcmE1CurrentIndex_Type(Integer32):
    """Custom type ncmE1CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1CurrentIndex_Type.__name__ = "Integer32"
_NcmE1CurrentIndex_Object = MibTableColumn
ncmE1CurrentIndex = _NcmE1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 2),
    _NcmE1CurrentIndex_Type()
)
ncmE1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentIndex.setStatus("mandatory")


class _NcmE1CurrentEndType_Type(Integer32):
    """Custom type ncmE1CurrentEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmE1CurrentEndType_Type.__name__ = "Integer32"
_NcmE1CurrentEndType_Object = MibTableColumn
ncmE1CurrentEndType = _NcmE1CurrentEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 3),
    _NcmE1CurrentEndType_Type()
)
ncmE1CurrentEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentEndType.setStatus("mandatory")


class _NcmE1CRC4Status_Type(Integer32):
    """Custom type ncmE1CRC4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmE1CRC4Status_Type.__name__ = "Integer32"
_NcmE1CRC4Status_Object = MibTableColumn
ncmE1CRC4Status = _NcmE1CRC4Status_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 4),
    _NcmE1CRC4Status_Type()
)
ncmE1CRC4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CRC4Status.setStatus("mandatory")
_NcmE1Timestamp_Type = Integer32
_NcmE1Timestamp_Object = MibTableColumn
ncmE1Timestamp = _NcmE1Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 5),
    _NcmE1Timestamp_Type()
)
ncmE1Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1Timestamp.setStatus("mandatory")
_NcmE1Timestamp1_Type = Integer32
_NcmE1Timestamp1_Object = MibTableColumn
ncmE1Timestamp1 = _NcmE1Timestamp1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 6),
    _NcmE1Timestamp1_Type()
)
ncmE1Timestamp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1Timestamp1.setStatus("mandatory")
_NcmE1CurrentIntervalSec_Type = Integer32
_NcmE1CurrentIntervalSec_Object = MibTableColumn
ncmE1CurrentIntervalSec = _NcmE1CurrentIntervalSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 7),
    _NcmE1CurrentIntervalSec_Type()
)
ncmE1CurrentIntervalSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentIntervalSec.setStatus("mandatory")
_NcmE1CurrentASs_Type = Gauge32
_NcmE1CurrentASs_Object = MibTableColumn
ncmE1CurrentASs = _NcmE1CurrentASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 8),
    _NcmE1CurrentASs_Type()
)
ncmE1CurrentASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentASs.setStatus("mandatory")
_NcmE1CurrentUASs_Type = Gauge32
_NcmE1CurrentUASs_Object = MibTableColumn
ncmE1CurrentUASs = _NcmE1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 9),
    _NcmE1CurrentUASs_Type()
)
ncmE1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentUASs.setStatus("mandatory")
_NcmE1CurrentESs_Type = Gauge32
_NcmE1CurrentESs_Object = MibTableColumn
ncmE1CurrentESs = _NcmE1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 10),
    _NcmE1CurrentESs_Type()
)
ncmE1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentESs.setStatus("mandatory")
_NcmE1CurrentSESs_Type = Gauge32
_NcmE1CurrentSESs_Object = MibTableColumn
ncmE1CurrentSESs = _NcmE1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 11),
    _NcmE1CurrentSESs_Type()
)
ncmE1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentSESs.setStatus("mandatory")
_NcmE1CurrentFAE_Type = Gauge32
_NcmE1CurrentFAE_Object = MibTableColumn
ncmE1CurrentFAE = _NcmE1CurrentFAE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 12),
    _NcmE1CurrentFAE_Type()
)
ncmE1CurrentFAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentFAE.setStatus("mandatory")
_NcmE1CurrentBBE_Type = Gauge32
_NcmE1CurrentBBE_Object = MibTableColumn
ncmE1CurrentBBE = _NcmE1CurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 13),
    _NcmE1CurrentBBE_Type()
)
ncmE1CurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentBBE.setStatus("mandatory")
_NcmE1CurrentSEFSs_Type = Gauge32
_NcmE1CurrentSEFSs_Object = MibTableColumn
ncmE1CurrentSEFSs = _NcmE1CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 14),
    _NcmE1CurrentSEFSs_Type()
)
ncmE1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentSEFSs.setStatus("mandatory")
_NcmE1CurrentAISSs_Type = Gauge32
_NcmE1CurrentAISSs_Object = MibTableColumn
ncmE1CurrentAISSs = _NcmE1CurrentAISSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 15),
    _NcmE1CurrentAISSs_Type()
)
ncmE1CurrentAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentAISSs.setStatus("mandatory")
_NcmE1CurrentLOSSs_Type = Gauge32
_NcmE1CurrentLOSSs_Object = MibTableColumn
ncmE1CurrentLOSSs = _NcmE1CurrentLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 16),
    _NcmE1CurrentLOSSs_Type()
)
ncmE1CurrentLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentLOSSs.setStatus("mandatory")
_NcmE1CurrentLOFSs_Type = Gauge32
_NcmE1CurrentLOFSs_Object = MibTableColumn
ncmE1CurrentLOFSs = _NcmE1CurrentLOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 17),
    _NcmE1CurrentLOFSs_Type()
)
ncmE1CurrentLOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentLOFSs.setStatus("mandatory")
_NcmE1CurrentOOFSs_Type = Gauge32
_NcmE1CurrentOOFSs_Object = MibTableColumn
ncmE1CurrentOOFSs = _NcmE1CurrentOOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 18),
    _NcmE1CurrentOOFSs_Type()
)
ncmE1CurrentOOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentOOFSs.setStatus("mandatory")
_NcmE1CurrentCVPath_Type = Gauge32
_NcmE1CurrentCVPath_Object = MibTableColumn
ncmE1CurrentCVPath = _NcmE1CurrentCVPath_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 19),
    _NcmE1CurrentCVPath_Type()
)
ncmE1CurrentCVPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentCVPath.setStatus("mandatory")
_NcmE1CurrentCVLine_Type = Gauge32
_NcmE1CurrentCVLine_Object = MibTableColumn
ncmE1CurrentCVLine = _NcmE1CurrentCVLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 20),
    _NcmE1CurrentCVLine_Type()
)
ncmE1CurrentCVLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentCVLine.setStatus("mandatory")
_NcmE1CurrentESsLine_Type = Gauge32
_NcmE1CurrentESsLine_Object = MibTableColumn
ncmE1CurrentESsLine = _NcmE1CurrentESsLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 21),
    _NcmE1CurrentESsLine_Type()
)
ncmE1CurrentESsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentESsLine.setStatus("mandatory")
_NcmE1CurrentSESsLine_Type = Gauge32
_NcmE1CurrentSESsLine_Object = MibTableColumn
ncmE1CurrentSESsLine = _NcmE1CurrentSESsLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 22),
    _NcmE1CurrentSESsLine_Type()
)
ncmE1CurrentSESsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentSESsLine.setStatus("mandatory")
_NcmE1CurrentFECPath_Type = Gauge32
_NcmE1CurrentFECPath_Object = MibTableColumn
ncmE1CurrentFECPath = _NcmE1CurrentFECPath_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 23),
    _NcmE1CurrentFECPath_Type()
)
ncmE1CurrentFECPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentFECPath.setStatus("mandatory")
_NcmE1CurrentFECLine_Type = Gauge32
_NcmE1CurrentFECLine_Object = MibTableColumn
ncmE1CurrentFECLine = _NcmE1CurrentFECLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1010, 1, 24),
    _NcmE1CurrentFECLine_Type()
)
ncmE1CurrentFECLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CurrentFECLine.setStatus("mandatory")
_NcmE1IntervalTable_Object = MibTable
ncmE1IntervalTable = _NcmE1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011)
)
if mibBuilder.loadTexts:
    ncmE1IntervalTable.setStatus("mandatory")
_NcmE1IntervalEntry_Object = MibTableRow
ncmE1IntervalEntry = _NcmE1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1)
)
ncmE1IntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1IntervalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1IntervalIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1IntervalEndType"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1IntervalNumber"),
)
if mibBuilder.loadTexts:
    ncmE1IntervalEntry.setStatus("mandatory")


class _NcmE1IntervalNIDIndex_Type(Integer32):
    """Custom type ncmE1IntervalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1IntervalNIDIndex_Type.__name__ = "Integer32"
_NcmE1IntervalNIDIndex_Object = MibTableColumn
ncmE1IntervalNIDIndex = _NcmE1IntervalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 1),
    _NcmE1IntervalNIDIndex_Type()
)
ncmE1IntervalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalNIDIndex.setStatus("mandatory")


class _NcmE1IntervalIndex_Type(Integer32):
    """Custom type ncmE1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1IntervalIndex_Type.__name__ = "Integer32"
_NcmE1IntervalIndex_Object = MibTableColumn
ncmE1IntervalIndex = _NcmE1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 2),
    _NcmE1IntervalIndex_Type()
)
ncmE1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalIndex.setStatus("mandatory")


class _NcmE1IntervalEndType_Type(Integer32):
    """Custom type ncmE1IntervalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmE1IntervalEndType_Type.__name__ = "Integer32"
_NcmE1IntervalEndType_Object = MibTableColumn
ncmE1IntervalEndType = _NcmE1IntervalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 3),
    _NcmE1IntervalEndType_Type()
)
ncmE1IntervalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalEndType.setStatus("mandatory")


class _NcmE1IntervalNumber_Type(Integer32):
    """Custom type ncmE1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NcmE1IntervalNumber_Type.__name__ = "Integer32"
_NcmE1IntervalNumber_Object = MibTableColumn
ncmE1IntervalNumber = _NcmE1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 4),
    _NcmE1IntervalNumber_Type()
)
ncmE1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalNumber.setStatus("mandatory")
_NcmE1IntervalASs_Type = Gauge32
_NcmE1IntervalASs_Object = MibTableColumn
ncmE1IntervalASs = _NcmE1IntervalASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 5),
    _NcmE1IntervalASs_Type()
)
ncmE1IntervalASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalASs.setStatus("mandatory")
_NcmE1IntervalUASs_Type = Gauge32
_NcmE1IntervalUASs_Object = MibTableColumn
ncmE1IntervalUASs = _NcmE1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 6),
    _NcmE1IntervalUASs_Type()
)
ncmE1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalUASs.setStatus("mandatory")
_NcmE1IntervalESs_Type = Gauge32
_NcmE1IntervalESs_Object = MibTableColumn
ncmE1IntervalESs = _NcmE1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 7),
    _NcmE1IntervalESs_Type()
)
ncmE1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalESs.setStatus("mandatory")
_NcmE1IntervalSESs_Type = Gauge32
_NcmE1IntervalSESs_Object = MibTableColumn
ncmE1IntervalSESs = _NcmE1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 8),
    _NcmE1IntervalSESs_Type()
)
ncmE1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalSESs.setStatus("mandatory")
_NcmE1IntervalFAE_Type = Gauge32
_NcmE1IntervalFAE_Object = MibTableColumn
ncmE1IntervalFAE = _NcmE1IntervalFAE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 9),
    _NcmE1IntervalFAE_Type()
)
ncmE1IntervalFAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalFAE.setStatus("mandatory")
_NcmE1IntervalBBE_Type = Gauge32
_NcmE1IntervalBBE_Object = MibTableColumn
ncmE1IntervalBBE = _NcmE1IntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 10),
    _NcmE1IntervalBBE_Type()
)
ncmE1IntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalBBE.setStatus("mandatory")
_NcmE1IntervalSEFSs_Type = Gauge32
_NcmE1IntervalSEFSs_Object = MibTableColumn
ncmE1IntervalSEFSs = _NcmE1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 11),
    _NcmE1IntervalSEFSs_Type()
)
ncmE1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalSEFSs.setStatus("mandatory")
_NcmE1IntervalAISSs_Type = Gauge32
_NcmE1IntervalAISSs_Object = MibTableColumn
ncmE1IntervalAISSs = _NcmE1IntervalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 12),
    _NcmE1IntervalAISSs_Type()
)
ncmE1IntervalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalAISSs.setStatus("mandatory")
_NcmE1IntervalLOSSs_Type = Gauge32
_NcmE1IntervalLOSSs_Object = MibTableColumn
ncmE1IntervalLOSSs = _NcmE1IntervalLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 13),
    _NcmE1IntervalLOSSs_Type()
)
ncmE1IntervalLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalLOSSs.setStatus("mandatory")
_NcmE1IntervalLOFSs_Type = Gauge32
_NcmE1IntervalLOFSs_Object = MibTableColumn
ncmE1IntervalLOFSs = _NcmE1IntervalLOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 14),
    _NcmE1IntervalLOFSs_Type()
)
ncmE1IntervalLOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalLOFSs.setStatus("mandatory")
_NcmE1IntervalOOFSs_Type = Gauge32
_NcmE1IntervalOOFSs_Object = MibTableColumn
ncmE1IntervalOOFSs = _NcmE1IntervalOOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 15),
    _NcmE1IntervalOOFSs_Type()
)
ncmE1IntervalOOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalOOFSs.setStatus("mandatory")
_NcmE1IntervalCVPath_Type = Gauge32
_NcmE1IntervalCVPath_Object = MibTableColumn
ncmE1IntervalCVPath = _NcmE1IntervalCVPath_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 16),
    _NcmE1IntervalCVPath_Type()
)
ncmE1IntervalCVPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalCVPath.setStatus("mandatory")
_NcmE1IntervalCVLine_Type = Gauge32
_NcmE1IntervalCVLine_Object = MibTableColumn
ncmE1IntervalCVLine = _NcmE1IntervalCVLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 17),
    _NcmE1IntervalCVLine_Type()
)
ncmE1IntervalCVLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalCVLine.setStatus("mandatory")
_NcmE1IntervalESsLine_Type = Gauge32
_NcmE1IntervalESsLine_Object = MibTableColumn
ncmE1IntervalESsLine = _NcmE1IntervalESsLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 18),
    _NcmE1IntervalESsLine_Type()
)
ncmE1IntervalESsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalESsLine.setStatus("mandatory")
_NcmE1IntervalSESsLine_Type = Gauge32
_NcmE1IntervalSESsLine_Object = MibTableColumn
ncmE1IntervalSESsLine = _NcmE1IntervalSESsLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 19),
    _NcmE1IntervalSESsLine_Type()
)
ncmE1IntervalSESsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalSESsLine.setStatus("mandatory")
_NcmE1IntervalFECPath_Type = Gauge32
_NcmE1IntervalFECPath_Object = MibTableColumn
ncmE1IntervalFECPath = _NcmE1IntervalFECPath_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 20),
    _NcmE1IntervalFECPath_Type()
)
ncmE1IntervalFECPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalFECPath.setStatus("mandatory")
_NcmE1IntervalFECLine_Type = Gauge32
_NcmE1IntervalFECLine_Object = MibTableColumn
ncmE1IntervalFECLine = _NcmE1IntervalFECLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1011, 1, 21),
    _NcmE1IntervalFECLine_Type()
)
ncmE1IntervalFECLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1IntervalFECLine.setStatus("mandatory")
_NcmE1TotalTable_Object = MibTable
ncmE1TotalTable = _NcmE1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012)
)
if mibBuilder.loadTexts:
    ncmE1TotalTable.setStatus("mandatory")
_NcmE1TotalEntry_Object = MibTableRow
ncmE1TotalEntry = _NcmE1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1)
)
ncmE1TotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1TotalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1TotalIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1TotalEndType"),
)
if mibBuilder.loadTexts:
    ncmE1TotalEntry.setStatus("mandatory")


class _NcmE1TotalNIDIndex_Type(Integer32):
    """Custom type ncmE1TotalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1TotalNIDIndex_Type.__name__ = "Integer32"
_NcmE1TotalNIDIndex_Object = MibTableColumn
ncmE1TotalNIDIndex = _NcmE1TotalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 1),
    _NcmE1TotalNIDIndex_Type()
)
ncmE1TotalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalNIDIndex.setStatus("mandatory")


class _NcmE1TotalIndex_Type(Integer32):
    """Custom type ncmE1TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1TotalIndex_Type.__name__ = "Integer32"
_NcmE1TotalIndex_Object = MibTableColumn
ncmE1TotalIndex = _NcmE1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 2),
    _NcmE1TotalIndex_Type()
)
ncmE1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalIndex.setStatus("mandatory")


class _NcmE1TotalEndType_Type(Integer32):
    """Custom type ncmE1TotalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmE1TotalEndType_Type.__name__ = "Integer32"
_NcmE1TotalEndType_Object = MibTableColumn
ncmE1TotalEndType = _NcmE1TotalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 3),
    _NcmE1TotalEndType_Type()
)
ncmE1TotalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalEndType.setStatus("mandatory")
_NcmE1NumberOfValidInterval_Type = Integer32
_NcmE1NumberOfValidInterval_Object = MibTableColumn
ncmE1NumberOfValidInterval = _NcmE1NumberOfValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 4),
    _NcmE1NumberOfValidInterval_Type()
)
ncmE1NumberOfValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1NumberOfValidInterval.setStatus("mandatory")
_NcmE1TotalASs_Type = Gauge32
_NcmE1TotalASs_Object = MibTableColumn
ncmE1TotalASs = _NcmE1TotalASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 5),
    _NcmE1TotalASs_Type()
)
ncmE1TotalASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalASs.setStatus("mandatory")
_NcmE1TotalUASs_Type = Gauge32
_NcmE1TotalUASs_Object = MibTableColumn
ncmE1TotalUASs = _NcmE1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 6),
    _NcmE1TotalUASs_Type()
)
ncmE1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalUASs.setStatus("mandatory")
_NcmE1TotalESs_Type = Gauge32
_NcmE1TotalESs_Object = MibTableColumn
ncmE1TotalESs = _NcmE1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 7),
    _NcmE1TotalESs_Type()
)
ncmE1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalESs.setStatus("mandatory")
_NcmE1TotalSESs_Type = Gauge32
_NcmE1TotalSESs_Object = MibTableColumn
ncmE1TotalSESs = _NcmE1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 8),
    _NcmE1TotalSESs_Type()
)
ncmE1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalSESs.setStatus("mandatory")
_NcmE1TotalFAE_Type = Gauge32
_NcmE1TotalFAE_Object = MibTableColumn
ncmE1TotalFAE = _NcmE1TotalFAE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 9),
    _NcmE1TotalFAE_Type()
)
ncmE1TotalFAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalFAE.setStatus("mandatory")
_NcmE1TotalBBE_Type = Gauge32
_NcmE1TotalBBE_Object = MibTableColumn
ncmE1TotalBBE = _NcmE1TotalBBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 10),
    _NcmE1TotalBBE_Type()
)
ncmE1TotalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalBBE.setStatus("mandatory")
_NcmE1TotalSEFSs_Type = Gauge32
_NcmE1TotalSEFSs_Object = MibTableColumn
ncmE1TotalSEFSs = _NcmE1TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 11),
    _NcmE1TotalSEFSs_Type()
)
ncmE1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalSEFSs.setStatus("mandatory")
_NcmE1TotalAISSs_Type = Gauge32
_NcmE1TotalAISSs_Object = MibTableColumn
ncmE1TotalAISSs = _NcmE1TotalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 12),
    _NcmE1TotalAISSs_Type()
)
ncmE1TotalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalAISSs.setStatus("mandatory")
_NcmE1TotalLOSSs_Type = Gauge32
_NcmE1TotalLOSSs_Object = MibTableColumn
ncmE1TotalLOSSs = _NcmE1TotalLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 13),
    _NcmE1TotalLOSSs_Type()
)
ncmE1TotalLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalLOSSs.setStatus("mandatory")
_NcmE1TotalLOFSs_Type = Gauge32
_NcmE1TotalLOFSs_Object = MibTableColumn
ncmE1TotalLOFSs = _NcmE1TotalLOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 14),
    _NcmE1TotalLOFSs_Type()
)
ncmE1TotalLOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalLOFSs.setStatus("mandatory")
_NcmE1TotalOOFSs_Type = Gauge32
_NcmE1TotalOOFSs_Object = MibTableColumn
ncmE1TotalOOFSs = _NcmE1TotalOOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 15),
    _NcmE1TotalOOFSs_Type()
)
ncmE1TotalOOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalOOFSs.setStatus("mandatory")
_NcmE1TotalCVPath_Type = Gauge32
_NcmE1TotalCVPath_Object = MibTableColumn
ncmE1TotalCVPath = _NcmE1TotalCVPath_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 16),
    _NcmE1TotalCVPath_Type()
)
ncmE1TotalCVPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalCVPath.setStatus("mandatory")
_NcmE1TotalCVLine_Type = Gauge32
_NcmE1TotalCVLine_Object = MibTableColumn
ncmE1TotalCVLine = _NcmE1TotalCVLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 17),
    _NcmE1TotalCVLine_Type()
)
ncmE1TotalCVLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalCVLine.setStatus("mandatory")
_NcmE1TotalESsLine_Type = Gauge32
_NcmE1TotalESsLine_Object = MibTableColumn
ncmE1TotalESsLine = _NcmE1TotalESsLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 18),
    _NcmE1TotalESsLine_Type()
)
ncmE1TotalESsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalESsLine.setStatus("mandatory")
_NcmE1TotalSESsLine_Type = Gauge32
_NcmE1TotalSESsLine_Object = MibTableColumn
ncmE1TotalSESsLine = _NcmE1TotalSESsLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 19),
    _NcmE1TotalSESsLine_Type()
)
ncmE1TotalSESsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalSESsLine.setStatus("mandatory")
_NcmE1TotalFECPath_Type = Gauge32
_NcmE1TotalFECPath_Object = MibTableColumn
ncmE1TotalFECPath = _NcmE1TotalFECPath_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 20),
    _NcmE1TotalFECPath_Type()
)
ncmE1TotalFECPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalFECPath.setStatus("mandatory")
_NcmE1TotalFECLine_Type = Gauge32
_NcmE1TotalFECLine_Object = MibTableColumn
ncmE1TotalFECLine = _NcmE1TotalFECLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1012, 1, 21),
    _NcmE1TotalFECLine_Type()
)
ncmE1TotalFECLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TotalFECLine.setStatus("mandatory")
_NcmE1PrevTotalTable_Object = MibTable
ncmE1PrevTotalTable = _NcmE1PrevTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013)
)
if mibBuilder.loadTexts:
    ncmE1PrevTotalTable.setStatus("mandatory")
_NcmE1PrevTotalEntry_Object = MibTableRow
ncmE1PrevTotalEntry = _NcmE1PrevTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1)
)
ncmE1PrevTotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1PrevTotalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1PrevTotalIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1PrevTotalEndType"),
)
if mibBuilder.loadTexts:
    ncmE1PrevTotalEntry.setStatus("mandatory")


class _NcmE1PrevTotalNIDIndex_Type(Integer32):
    """Custom type ncmE1PrevTotalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1PrevTotalNIDIndex_Type.__name__ = "Integer32"
_NcmE1PrevTotalNIDIndex_Object = MibTableColumn
ncmE1PrevTotalNIDIndex = _NcmE1PrevTotalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 1),
    _NcmE1PrevTotalNIDIndex_Type()
)
ncmE1PrevTotalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalNIDIndex.setStatus("mandatory")


class _NcmE1PrevTotalIndex_Type(Integer32):
    """Custom type ncmE1PrevTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1PrevTotalIndex_Type.__name__ = "Integer32"
_NcmE1PrevTotalIndex_Object = MibTableColumn
ncmE1PrevTotalIndex = _NcmE1PrevTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 2),
    _NcmE1PrevTotalIndex_Type()
)
ncmE1PrevTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalIndex.setStatus("mandatory")


class _NcmE1PrevTotalEndType_Type(Integer32):
    """Custom type ncmE1PrevTotalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmE1PrevTotalEndType_Type.__name__ = "Integer32"
_NcmE1PrevTotalEndType_Object = MibTableColumn
ncmE1PrevTotalEndType = _NcmE1PrevTotalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 3),
    _NcmE1PrevTotalEndType_Type()
)
ncmE1PrevTotalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalEndType.setStatus("mandatory")
_NcmE1PrevTotalASs_Type = Gauge32
_NcmE1PrevTotalASs_Object = MibTableColumn
ncmE1PrevTotalASs = _NcmE1PrevTotalASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 4),
    _NcmE1PrevTotalASs_Type()
)
ncmE1PrevTotalASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalASs.setStatus("mandatory")
_NcmE1PrevTotalUASs_Type = Gauge32
_NcmE1PrevTotalUASs_Object = MibTableColumn
ncmE1PrevTotalUASs = _NcmE1PrevTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 5),
    _NcmE1PrevTotalUASs_Type()
)
ncmE1PrevTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalUASs.setStatus("mandatory")
_NcmE1PrevTotalESs_Type = Gauge32
_NcmE1PrevTotalESs_Object = MibTableColumn
ncmE1PrevTotalESs = _NcmE1PrevTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 6),
    _NcmE1PrevTotalESs_Type()
)
ncmE1PrevTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalESs.setStatus("mandatory")
_NcmE1PrevTotalSESs_Type = Gauge32
_NcmE1PrevTotalSESs_Object = MibTableColumn
ncmE1PrevTotalSESs = _NcmE1PrevTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 7),
    _NcmE1PrevTotalSESs_Type()
)
ncmE1PrevTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalSESs.setStatus("mandatory")
_NcmE1PrevTotalFAE_Type = Gauge32
_NcmE1PrevTotalFAE_Object = MibTableColumn
ncmE1PrevTotalFAE = _NcmE1PrevTotalFAE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 8),
    _NcmE1PrevTotalFAE_Type()
)
ncmE1PrevTotalFAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalFAE.setStatus("mandatory")
_NcmE1PrevTotalBBE_Type = Gauge32
_NcmE1PrevTotalBBE_Object = MibTableColumn
ncmE1PrevTotalBBE = _NcmE1PrevTotalBBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 9),
    _NcmE1PrevTotalBBE_Type()
)
ncmE1PrevTotalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalBBE.setStatus("mandatory")
_NcmE1PrevTotalSEFSs_Type = Gauge32
_NcmE1PrevTotalSEFSs_Object = MibTableColumn
ncmE1PrevTotalSEFSs = _NcmE1PrevTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 10),
    _NcmE1PrevTotalSEFSs_Type()
)
ncmE1PrevTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalSEFSs.setStatus("mandatory")
_NcmE1PrevTotalAISSs_Type = Gauge32
_NcmE1PrevTotalAISSs_Object = MibTableColumn
ncmE1PrevTotalAISSs = _NcmE1PrevTotalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 11),
    _NcmE1PrevTotalAISSs_Type()
)
ncmE1PrevTotalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalAISSs.setStatus("mandatory")
_NcmE1PrevTotalLOSSs_Type = Gauge32
_NcmE1PrevTotalLOSSs_Object = MibTableColumn
ncmE1PrevTotalLOSSs = _NcmE1PrevTotalLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 12),
    _NcmE1PrevTotalLOSSs_Type()
)
ncmE1PrevTotalLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalLOSSs.setStatus("mandatory")
_NcmE1PrevTotalLOFSs_Type = Gauge32
_NcmE1PrevTotalLOFSs_Object = MibTableColumn
ncmE1PrevTotalLOFSs = _NcmE1PrevTotalLOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 13),
    _NcmE1PrevTotalLOFSs_Type()
)
ncmE1PrevTotalLOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalLOFSs.setStatus("mandatory")
_NcmE1PrevTotalOOFSs_Type = Gauge32
_NcmE1PrevTotalOOFSs_Object = MibTableColumn
ncmE1PrevTotalOOFSs = _NcmE1PrevTotalOOFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 14),
    _NcmE1PrevTotalOOFSs_Type()
)
ncmE1PrevTotalOOFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalOOFSs.setStatus("mandatory")
_NcmE1PrevTotalCVPath_Type = Gauge32
_NcmE1PrevTotalCVPath_Object = MibTableColumn
ncmE1PrevTotalCVPath = _NcmE1PrevTotalCVPath_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 15),
    _NcmE1PrevTotalCVPath_Type()
)
ncmE1PrevTotalCVPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalCVPath.setStatus("mandatory")
_NcmE1PrevTotalCVLine_Type = Gauge32
_NcmE1PrevTotalCVLine_Object = MibTableColumn
ncmE1PrevTotalCVLine = _NcmE1PrevTotalCVLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 16),
    _NcmE1PrevTotalCVLine_Type()
)
ncmE1PrevTotalCVLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalCVLine.setStatus("mandatory")
_NcmE1PrevTotalESsLine_Type = Gauge32
_NcmE1PrevTotalESsLine_Object = MibTableColumn
ncmE1PrevTotalESsLine = _NcmE1PrevTotalESsLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 17),
    _NcmE1PrevTotalESsLine_Type()
)
ncmE1PrevTotalESsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalESsLine.setStatus("mandatory")
_NcmE1PrevTotalSESsLine_Type = Gauge32
_NcmE1PrevTotalSESsLine_Object = MibTableColumn
ncmE1PrevTotalSESsLine = _NcmE1PrevTotalSESsLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 18),
    _NcmE1PrevTotalSESsLine_Type()
)
ncmE1PrevTotalSESsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalSESsLine.setStatus("mandatory")
_NcmE1PrevTotalFECPath_Type = Gauge32
_NcmE1PrevTotalFECPath_Object = MibTableColumn
ncmE1PrevTotalFECPath = _NcmE1PrevTotalFECPath_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 19),
    _NcmE1PrevTotalFECPath_Type()
)
ncmE1PrevTotalFECPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalFECPath.setStatus("mandatory")
_NcmE1PrevTotalFECLine_Type = Gauge32
_NcmE1PrevTotalFECLine_Object = MibTableColumn
ncmE1PrevTotalFECLine = _NcmE1PrevTotalFECLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1013, 1, 20),
    _NcmE1PrevTotalFECLine_Type()
)
ncmE1PrevTotalFECLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PrevTotalFECLine.setStatus("mandatory")
_NcmE1PerformanceSnapShotTable_Object = MibTable
ncmE1PerformanceSnapShotTable = _NcmE1PerformanceSnapShotTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014)
)
if mibBuilder.loadTexts:
    ncmE1PerformanceSnapShotTable.setStatus("mandatory")
_NcmE1PerformanceSnapShotEntry_Object = MibTableRow
ncmE1PerformanceSnapShotEntry = _NcmE1PerformanceSnapShotEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1)
)
ncmE1PerformanceSnapShotEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1SnapShotNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1SnapShotIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1SnapShotEndType"),
)
if mibBuilder.loadTexts:
    ncmE1PerformanceSnapShotEntry.setStatus("mandatory")


class _NcmE1SnapShotNIDIndex_Type(Integer32):
    """Custom type ncmE1SnapShotNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1SnapShotNIDIndex_Type.__name__ = "Integer32"
_NcmE1SnapShotNIDIndex_Object = MibTableColumn
ncmE1SnapShotNIDIndex = _NcmE1SnapShotNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1, 1),
    _NcmE1SnapShotNIDIndex_Type()
)
ncmE1SnapShotNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1SnapShotNIDIndex.setStatus("mandatory")


class _NcmE1SnapShotIndex_Type(Integer32):
    """Custom type ncmE1SnapShotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1SnapShotIndex_Type.__name__ = "Integer32"
_NcmE1SnapShotIndex_Object = MibTableColumn
ncmE1SnapShotIndex = _NcmE1SnapShotIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1, 2),
    _NcmE1SnapShotIndex_Type()
)
ncmE1SnapShotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1SnapShotIndex.setStatus("mandatory")


class _NcmE1SnapShotEndType_Type(Integer32):
    """Custom type ncmE1SnapShotEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmE1SnapShotEndType_Type.__name__ = "Integer32"
_NcmE1SnapShotEndType_Object = MibTableColumn
ncmE1SnapShotEndType = _NcmE1SnapShotEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1, 3),
    _NcmE1SnapShotEndType_Type()
)
ncmE1SnapShotEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1SnapShotEndType.setStatus("mandatory")


class _NcmE1SnapShot_Type(Integer32):
    """Custom type ncmE1SnapShot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1SnapShot_Type.__name__ = "Integer32"
_NcmE1SnapShot_Object = MibTableColumn
ncmE1SnapShot = _NcmE1SnapShot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1, 4),
    _NcmE1SnapShot_Type()
)
ncmE1SnapShot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1SnapShot.setStatus("mandatory")
_NcmE1TimeStampSec_Type = Integer32
_NcmE1TimeStampSec_Object = MibTableColumn
ncmE1TimeStampSec = _NcmE1TimeStampSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1, 5),
    _NcmE1TimeStampSec_Type()
)
ncmE1TimeStampSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TimeStampSec.setStatus("mandatory")
_NcmE1TimeMilliSec_Type = Integer32
_NcmE1TimeMilliSec_Object = MibTableColumn
ncmE1TimeMilliSec = _NcmE1TimeMilliSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1, 6),
    _NcmE1TimeMilliSec_Type()
)
ncmE1TimeMilliSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1TimeMilliSec.setStatus("mandatory")
_NcmE1SecInCurrInterval_Type = Integer32
_NcmE1SecInCurrInterval_Object = MibTableColumn
ncmE1SecInCurrInterval = _NcmE1SecInCurrInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1, 7),
    _NcmE1SecInCurrInterval_Type()
)
ncmE1SecInCurrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1SecInCurrInterval.setStatus("mandatory")


class _NcmE1ResetPerfReg_Type(Integer32):
    """Custom type ncmE1ResetPerfReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1ResetPerfReg_Type.__name__ = "Integer32"
_NcmE1ResetPerfReg_Object = MibTableColumn
ncmE1ResetPerfReg = _NcmE1ResetPerfReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1014, 1, 8),
    _NcmE1ResetPerfReg_Type()
)
ncmE1ResetPerfReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1ResetPerfReg.setStatus("mandatory")
_NcmE1PortLatchedStatusTable_Object = MibTable
ncmE1PortLatchedStatusTable = _NcmE1PortLatchedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015)
)
if mibBuilder.loadTexts:
    ncmE1PortLatchedStatusTable.setStatus("mandatory")
_NcmE1PortLatchedStatusEntry_Object = MibTableRow
ncmE1PortLatchedStatusEntry = _NcmE1PortLatchedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1)
)
ncmE1PortLatchedStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1PortLatchedStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1PortLatchedStatusIndex"),
)
if mibBuilder.loadTexts:
    ncmE1PortLatchedStatusEntry.setStatus("mandatory")


class _NcmE1PortLatchedStatusNIDIndex_Type(Integer32):
    """Custom type ncmE1PortLatchedStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1PortLatchedStatusNIDIndex_Type.__name__ = "Integer32"
_NcmE1PortLatchedStatusNIDIndex_Object = MibTableColumn
ncmE1PortLatchedStatusNIDIndex = _NcmE1PortLatchedStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 1),
    _NcmE1PortLatchedStatusNIDIndex_Type()
)
ncmE1PortLatchedStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedStatusNIDIndex.setStatus("mandatory")


class _NcmE1PortLatchedStatusIndex_Type(Integer32):
    """Custom type ncmE1PortLatchedStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1PortLatchedStatusIndex_Type.__name__ = "Integer32"
_NcmE1PortLatchedStatusIndex_Object = MibTableColumn
ncmE1PortLatchedStatusIndex = _NcmE1PortLatchedStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 2),
    _NcmE1PortLatchedStatusIndex_Type()
)
ncmE1PortLatchedStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedStatusIndex.setStatus("mandatory")


class _NcmE1PortLatchedCRC4Error_Type(Integer32):
    """Custom type ncmE1PortLatchedCRC4Error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLatchedCRC4Error_Type.__name__ = "Integer32"
_NcmE1PortLatchedCRC4Error_Object = MibTableColumn
ncmE1PortLatchedCRC4Error = _NcmE1PortLatchedCRC4Error_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 3),
    _NcmE1PortLatchedCRC4Error_Type()
)
ncmE1PortLatchedCRC4Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedCRC4Error.setStatus("mandatory")


class _NcmE1PortLatchedFramingSlip_Type(Integer32):
    """Custom type ncmE1PortLatchedFramingSlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLatchedFramingSlip_Type.__name__ = "Integer32"
_NcmE1PortLatchedFramingSlip_Object = MibTableColumn
ncmE1PortLatchedFramingSlip = _NcmE1PortLatchedFramingSlip_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 4),
    _NcmE1PortLatchedFramingSlip_Type()
)
ncmE1PortLatchedFramingSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedFramingSlip.setStatus("mandatory")


class _NcmE1PortLatchedRAI_Type(Integer32):
    """Custom type ncmE1PortLatchedRAI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLatchedRAI_Type.__name__ = "Integer32"
_NcmE1PortLatchedRAI_Object = MibTableColumn
ncmE1PortLatchedRAI = _NcmE1PortLatchedRAI_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 5),
    _NcmE1PortLatchedRAI_Type()
)
ncmE1PortLatchedRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedRAI.setStatus("mandatory")


class _NcmE1PortLatchedLOFA_Type(Integer32):
    """Custom type ncmE1PortLatchedLOFA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLatchedLOFA_Type.__name__ = "Integer32"
_NcmE1PortLatchedLOFA_Object = MibTableColumn
ncmE1PortLatchedLOFA = _NcmE1PortLatchedLOFA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 6),
    _NcmE1PortLatchedLOFA_Type()
)
ncmE1PortLatchedLOFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedLOFA.setStatus("mandatory")


class _NcmE1PortLatchedAIS_Type(Integer32):
    """Custom type ncmE1PortLatchedAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLatchedAIS_Type.__name__ = "Integer32"
_NcmE1PortLatchedAIS_Object = MibTableColumn
ncmE1PortLatchedAIS = _NcmE1PortLatchedAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 7),
    _NcmE1PortLatchedAIS_Type()
)
ncmE1PortLatchedAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedAIS.setStatus("mandatory")


class _NcmE1PortLatchedLOS_Type(Integer32):
    """Custom type ncmE1PortLatchedLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLatchedLOS_Type.__name__ = "Integer32"
_NcmE1PortLatchedLOS_Object = MibTableColumn
ncmE1PortLatchedLOS = _NcmE1PortLatchedLOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 8),
    _NcmE1PortLatchedLOS_Type()
)
ncmE1PortLatchedLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedLOS.setStatus("mandatory")


class _NcmE1PortLatchedBPVThresholdExceeded_Type(Integer32):
    """Custom type ncmE1PortLatchedBPVThresholdExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1PortLatchedBPVThresholdExceeded_Type.__name__ = "Integer32"
_NcmE1PortLatchedBPVThresholdExceeded_Object = MibTableColumn
ncmE1PortLatchedBPVThresholdExceeded = _NcmE1PortLatchedBPVThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1015, 1, 9),
    _NcmE1PortLatchedBPVThresholdExceeded_Type()
)
ncmE1PortLatchedBPVThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1PortLatchedBPVThresholdExceeded.setStatus("mandatory")
_NcmE1ThresholdStatusTable_Object = MibTable
ncmE1ThresholdStatusTable = _NcmE1ThresholdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016)
)
if mibBuilder.loadTexts:
    ncmE1ThresholdStatusTable.setStatus("mandatory")
_NcmE1ThresholdStatusEntry_Object = MibTableRow
ncmE1ThresholdStatusEntry = _NcmE1ThresholdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1)
)
ncmE1ThresholdStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1ThresholdStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1ThresholdStatusIndex"),
)
if mibBuilder.loadTexts:
    ncmE1ThresholdStatusEntry.setStatus("mandatory")


class _NcmE1ThresholdStatusNIDIndex_Type(Integer32):
    """Custom type ncmE1ThresholdStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1ThresholdStatusNIDIndex_Type.__name__ = "Integer32"
_NcmE1ThresholdStatusNIDIndex_Object = MibTableColumn
ncmE1ThresholdStatusNIDIndex = _NcmE1ThresholdStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 1),
    _NcmE1ThresholdStatusNIDIndex_Type()
)
ncmE1ThresholdStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1ThresholdStatusNIDIndex.setStatus("mandatory")


class _NcmE1ThresholdStatusIndex_Type(Integer32):
    """Custom type ncmE1ThresholdStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1ThresholdStatusIndex_Type.__name__ = "Integer32"
_NcmE1ThresholdStatusIndex_Object = MibTableColumn
ncmE1ThresholdStatusIndex = _NcmE1ThresholdStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 2),
    _NcmE1ThresholdStatusIndex_Type()
)
ncmE1ThresholdStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1ThresholdStatusIndex.setStatus("mandatory")
_NcmE1CRCThreshold_Type = Integer32
_NcmE1CRCThreshold_Object = MibTableColumn
ncmE1CRCThreshold = _NcmE1CRCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 3),
    _NcmE1CRCThreshold_Type()
)
ncmE1CRCThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CRCThreshold.setStatus("mandatory")


class _NcmE1CRCExceeded_Type(Integer32):
    """Custom type ncmE1CRCExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1CRCExceeded_Type.__name__ = "Integer32"
_NcmE1CRCExceeded_Object = MibTableColumn
ncmE1CRCExceeded = _NcmE1CRCExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 4),
    _NcmE1CRCExceeded_Type()
)
ncmE1CRCExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1CRCExceeded.setStatus("mandatory")
_NcmE1SESThreshold_Type = Integer32
_NcmE1SESThreshold_Object = MibTableColumn
ncmE1SESThreshold = _NcmE1SESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 5),
    _NcmE1SESThreshold_Type()
)
ncmE1SESThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1SESThreshold.setStatus("mandatory")


class _NcmE1SESExceeded_Type(Integer32):
    """Custom type ncmE1SESExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1SESExceeded_Type.__name__ = "Integer32"
_NcmE1SESExceeded_Object = MibTableColumn
ncmE1SESExceeded = _NcmE1SESExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 6),
    _NcmE1SESExceeded_Type()
)
ncmE1SESExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1SESExceeded.setStatus("mandatory")
_NcmE1UASThreshold_Type = Integer32
_NcmE1UASThreshold_Object = MibTableColumn
ncmE1UASThreshold = _NcmE1UASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 7),
    _NcmE1UASThreshold_Type()
)
ncmE1UASThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1UASThreshold.setStatus("mandatory")


class _NcmE1UASExceeded_Type(Integer32):
    """Custom type ncmE1UASExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1UASExceeded_Type.__name__ = "Integer32"
_NcmE1UASExceeded_Object = MibTableColumn
ncmE1UASExceeded = _NcmE1UASExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 8),
    _NcmE1UASExceeded_Type()
)
ncmE1UASExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1UASExceeded.setStatus("mandatory")
_NcmE1BPVThresholdst_Type = Integer32
_NcmE1BPVThresholdst_Object = MibTableColumn
ncmE1BPVThresholdst = _NcmE1BPVThresholdst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 9),
    _NcmE1BPVThresholdst_Type()
)
ncmE1BPVThresholdst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1BPVThresholdst.setStatus("mandatory")


class _NcmE1BPVExceeded_Type(Integer32):
    """Custom type ncmE1BPVExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1BPVExceeded_Type.__name__ = "Integer32"
_NcmE1BPVExceeded_Object = MibTableColumn
ncmE1BPVExceeded = _NcmE1BPVExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 10),
    _NcmE1BPVExceeded_Type()
)
ncmE1BPVExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1BPVExceeded.setStatus("mandatory")
_NcmE1BERThreshold_Type = Integer32
_NcmE1BERThreshold_Object = MibTableColumn
ncmE1BERThreshold = _NcmE1BERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 11),
    _NcmE1BERThreshold_Type()
)
ncmE1BERThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1BERThreshold.setStatus("mandatory")


class _NcmE1BERExceeded_Type(Integer32):
    """Custom type ncmE1BERExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmE1BERExceeded_Type.__name__ = "Integer32"
_NcmE1BERExceeded_Object = MibTableColumn
ncmE1BERExceeded = _NcmE1BERExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 12),
    _NcmE1BERExceeded_Type()
)
ncmE1BERExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1BERExceeded.setStatus("mandatory")


class _NcmE1RestoreState_Type(Integer32):
    """Custom type ncmE1RestoreState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("in-servcie", 2),
          ("out-of-servcie", 1))
    )


_NcmE1RestoreState_Type.__name__ = "Integer32"
_NcmE1RestoreState_Object = MibTableColumn
ncmE1RestoreState = _NcmE1RestoreState_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 13),
    _NcmE1RestoreState_Type()
)
ncmE1RestoreState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1RestoreState.setStatus("mandatory")
_NcmE1LineRestoreSec_Type = Integer32
_NcmE1LineRestoreSec_Object = MibTableColumn
ncmE1LineRestoreSec = _NcmE1LineRestoreSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1016, 1, 14),
    _NcmE1LineRestoreSec_Type()
)
ncmE1LineRestoreSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1LineRestoreSec.setStatus("mandatory")
_NcmT1ConfigTable_Object = MibTable
ncmT1ConfigTable = _NcmT1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017)
)
if mibBuilder.loadTexts:
    ncmT1ConfigTable.setStatus("mandatory")
_NcmT1ConfigEntry_Object = MibTableRow
ncmT1ConfigEntry = _NcmT1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1)
)
ncmT1ConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1ConfigNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1LineIndex"),
)
if mibBuilder.loadTexts:
    ncmT1ConfigEntry.setStatus("mandatory")


class _NcmT1ConfigNIDIndex_Type(Integer32):
    """Custom type ncmT1ConfigNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1ConfigNIDIndex_Type.__name__ = "Integer32"
_NcmT1ConfigNIDIndex_Object = MibTableColumn
ncmT1ConfigNIDIndex = _NcmT1ConfigNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 1),
    _NcmT1ConfigNIDIndex_Type()
)
ncmT1ConfigNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ConfigNIDIndex.setStatus("mandatory")


class _NcmT1LineIndex_Type(Integer32):
    """Custom type ncmT1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1LineIndex_Type.__name__ = "Integer32"
_NcmT1LineIndex_Object = MibTableColumn
ncmT1LineIndex = _NcmT1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 2),
    _NcmT1LineIndex_Type()
)
ncmT1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LineIndex.setStatus("mandatory")


class _NcmT1CRC6_Type(Integer32):
    """Custom type ncmT1CRC6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmT1CRC6_Type.__name__ = "Integer32"
_NcmT1CRC6_Object = MibTableColumn
ncmT1CRC6 = _NcmT1CRC6_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 3),
    _NcmT1CRC6_Type()
)
ncmT1CRC6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1CRC6.setStatus("mandatory")


class _NcmT1FramingFormat_Type(Integer32):
    """Custom type ncmT1FramingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eSF", 2),
          ("sF", 1))
    )


_NcmT1FramingFormat_Type.__name__ = "Integer32"
_NcmT1FramingFormat_Object = MibTableColumn
ncmT1FramingFormat = _NcmT1FramingFormat_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 4),
    _NcmT1FramingFormat_Type()
)
ncmT1FramingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1FramingFormat.setStatus("mandatory")


class _NcmT1LineCoding_Type(Integer32):
    """Custom type ncmT1LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 1),
          ("b8ZS", 2))
    )


_NcmT1LineCoding_Type.__name__ = "Integer32"
_NcmT1LineCoding_Object = MibTableColumn
ncmT1LineCoding = _NcmT1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 5),
    _NcmT1LineCoding_Type()
)
ncmT1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1LineCoding.setStatus("mandatory")


class _NcmT1FramingType_Type(Integer32):
    """Custom type ncmT1FramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cAS-BR", 1),
          ("cAS-CC", 2),
          ("cCS", 3))
    )


_NcmT1FramingType_Type.__name__ = "Integer32"
_NcmT1FramingType_Object = MibTableColumn
ncmT1FramingType = _NcmT1FramingType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 6),
    _NcmT1FramingType_Type()
)
ncmT1FramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1FramingType.setStatus("mandatory")


class _NcmT1FDL_Type(Integer32):
    """Custom type ncmT1FDL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmT1FDL_Type.__name__ = "Integer32"
_NcmT1FDL_Object = MibTableColumn
ncmT1FDL = _NcmT1FDL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 7),
    _NcmT1FDL_Type()
)
ncmT1FDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1FDL.setStatus("mandatory")


class _NcmT1InbandISDNEnableDisable_Type(Integer32):
    """Custom type ncmT1InbandISDNEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disablebothinbandisdn", 1),
          ("enableinband", 2),
          ("enableisdn", 3))
    )


_NcmT1InbandISDNEnableDisable_Type.__name__ = "Integer32"
_NcmT1InbandISDNEnableDisable_Object = MibTableColumn
ncmT1InbandISDNEnableDisable = _NcmT1InbandISDNEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 8),
    _NcmT1InbandISDNEnableDisable_Type()
)
ncmT1InbandISDNEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1InbandISDNEnableDisable.setStatus("mandatory")


class _NcmT1EnableNetLoopback_Type(Integer32):
    """Custom type ncmT1EnableNetLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmT1EnableNetLoopback_Type.__name__ = "Integer32"
_NcmT1EnableNetLoopback_Object = MibTableColumn
ncmT1EnableNetLoopback = _NcmT1EnableNetLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 9),
    _NcmT1EnableNetLoopback_Type()
)
ncmT1EnableNetLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1EnableNetLoopback.setStatus("mandatory")


class _NcmT1EnableNetOnesDensity_Type(Integer32):
    """Custom type ncmT1EnableNetOnesDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmT1EnableNetOnesDensity_Type.__name__ = "Integer32"
_NcmT1EnableNetOnesDensity_Object = MibTableColumn
ncmT1EnableNetOnesDensity = _NcmT1EnableNetOnesDensity_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 10),
    _NcmT1EnableNetOnesDensity_Type()
)
ncmT1EnableNetOnesDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1EnableNetOnesDensity.setStatus("mandatory")


class _NcmT1DensityPattern_Type(Integer32):
    """Custom type ncmT1DensityPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("d12d5c80Zero", 3),
          ("d15Zeros", 2),
          ("d80Zeros", 1),
          ("tR-62411", 4))
    )


_NcmT1DensityPattern_Type.__name__ = "Integer32"
_NcmT1DensityPattern_Object = MibTableColumn
ncmT1DensityPattern = _NcmT1DensityPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 11),
    _NcmT1DensityPattern_Type()
)
ncmT1DensityPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1DensityPattern.setStatus("mandatory")


class _NcmT1EnableRepeaterLpbkTimeout_Type(Integer32):
    """Custom type ncmT1EnableRepeaterLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmT1EnableRepeaterLpbkTimeout_Type.__name__ = "Integer32"
_NcmT1EnableRepeaterLpbkTimeout_Object = MibTableColumn
ncmT1EnableRepeaterLpbkTimeout = _NcmT1EnableRepeaterLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 12),
    _NcmT1EnableRepeaterLpbkTimeout_Type()
)
ncmT1EnableRepeaterLpbkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1EnableRepeaterLpbkTimeout.setStatus("mandatory")
_NcmT1RepeaterLoopbackTimeout_Type = Integer32
_NcmT1RepeaterLoopbackTimeout_Object = MibTableColumn
ncmT1RepeaterLoopbackTimeout = _NcmT1RepeaterLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 13),
    _NcmT1RepeaterLoopbackTimeout_Type()
)
ncmT1RepeaterLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1RepeaterLoopbackTimeout.setStatus("mandatory")
_NcmT1UserAlarmDeclareTime_Type = Integer32
_NcmT1UserAlarmDeclareTime_Object = MibTableColumn
ncmT1UserAlarmDeclareTime = _NcmT1UserAlarmDeclareTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 14),
    _NcmT1UserAlarmDeclareTime_Type()
)
ncmT1UserAlarmDeclareTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1UserAlarmDeclareTime.setStatus("mandatory")


class _NcmT1State_Type(Integer32):
    """Custom type ncmT1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 2),
          ("out-of-service", 1))
    )


_NcmT1State_Type.__name__ = "Integer32"
_NcmT1State_Object = MibTableColumn
ncmT1State = _NcmT1State_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 15),
    _NcmT1State_Type()
)
ncmT1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1State.setStatus("mandatory")


class _NcmT1NetworkLBOEQLIZ_Type(Integer32):
    """Custom type ncmT1NetworkLBOEQLIZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bldLn-0db-FT-0-133", 1),
          ("bldLnNeg15db-FT-266-399", 3),
          ("bldLnNeg22d5-FT-399-533", 4),
          ("bldLnNeg7d5db-FT-133-266", 2),
          ("fT-533-655", 5))
    )


_NcmT1NetworkLBOEQLIZ_Type.__name__ = "Integer32"
_NcmT1NetworkLBOEQLIZ_Object = MibTableColumn
ncmT1NetworkLBOEQLIZ = _NcmT1NetworkLBOEQLIZ_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 16),
    _NcmT1NetworkLBOEQLIZ_Type()
)
ncmT1NetworkLBOEQLIZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1NetworkLBOEQLIZ.setStatus("mandatory")
_NcmT1TimeSlot_Type = DisplayString
_NcmT1TimeSlot_Object = MibTableColumn
ncmT1TimeSlot = _NcmT1TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 17),
    _NcmT1TimeSlot_Type()
)
ncmT1TimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TimeSlot.setStatus("mandatory")
_NcmT1TimeSlotSelect_Type = Integer32
_NcmT1TimeSlotSelect_Object = MibTableColumn
ncmT1TimeSlotSelect = _NcmT1TimeSlotSelect_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1017, 1, 18),
    _NcmT1TimeSlotSelect_Type()
)
ncmT1TimeSlotSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1TimeSlotSelect.setStatus("mandatory")
_NcmT1PortStatusTable_Object = MibTable
ncmT1PortStatusTable = _NcmT1PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018)
)
if mibBuilder.loadTexts:
    ncmT1PortStatusTable.setStatus("mandatory")
_NcmT1PortStatusEntry_Object = MibTableRow
ncmT1PortStatusEntry = _NcmT1PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1)
)
ncmT1PortStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1PortStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1PortStatusIndex"),
)
if mibBuilder.loadTexts:
    ncmT1PortStatusEntry.setStatus("mandatory")


class _NcmT1PortStatusNIDIndex_Type(Integer32):
    """Custom type ncmT1PortStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1PortStatusNIDIndex_Type.__name__ = "Integer32"
_NcmT1PortStatusNIDIndex_Object = MibTableColumn
ncmT1PortStatusNIDIndex = _NcmT1PortStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 1),
    _NcmT1PortStatusNIDIndex_Type()
)
ncmT1PortStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortStatusNIDIndex.setStatus("mandatory")


class _NcmT1PortStatusIndex_Type(Integer32):
    """Custom type ncmT1PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1PortStatusIndex_Type.__name__ = "Integer32"
_NcmT1PortStatusIndex_Object = MibTableColumn
ncmT1PortStatusIndex = _NcmT1PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 2),
    _NcmT1PortStatusIndex_Type()
)
ncmT1PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortStatusIndex.setStatus("mandatory")


class _NcmT1PortCRC6Error_Type(Integer32):
    """Custom type ncmT1PortCRC6Error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortCRC6Error_Type.__name__ = "Integer32"
_NcmT1PortCRC6Error_Object = MibTableColumn
ncmT1PortCRC6Error = _NcmT1PortCRC6Error_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 3),
    _NcmT1PortCRC6Error_Type()
)
ncmT1PortCRC6Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortCRC6Error.setStatus("mandatory")


class _NcmT1PortFramingSlip_Type(Integer32):
    """Custom type ncmT1PortFramingSlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortFramingSlip_Type.__name__ = "Integer32"
_NcmT1PortFramingSlip_Object = MibTableColumn
ncmT1PortFramingSlip = _NcmT1PortFramingSlip_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 4),
    _NcmT1PortFramingSlip_Type()
)
ncmT1PortFramingSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortFramingSlip.setStatus("mandatory")


class _NcmT1PortRAI_Type(Integer32):
    """Custom type ncmT1PortRAI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortRAI_Type.__name__ = "Integer32"
_NcmT1PortRAI_Object = MibTableColumn
ncmT1PortRAI = _NcmT1PortRAI_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 5),
    _NcmT1PortRAI_Type()
)
ncmT1PortRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortRAI.setStatus("mandatory")


class _NcmT1PortLOF_Type(Integer32):
    """Custom type ncmT1PortLOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortLOF_Type.__name__ = "Integer32"
_NcmT1PortLOF_Object = MibTableColumn
ncmT1PortLOF = _NcmT1PortLOF_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 6),
    _NcmT1PortLOF_Type()
)
ncmT1PortLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortLOF.setStatus("mandatory")


class _NcmT1PortAIS_Type(Integer32):
    """Custom type ncmT1PortAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortAIS_Type.__name__ = "Integer32"
_NcmT1PortAIS_Object = MibTableColumn
ncmT1PortAIS = _NcmT1PortAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 7),
    _NcmT1PortAIS_Type()
)
ncmT1PortAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortAIS.setStatus("mandatory")


class _NcmT1PortLOS_Type(Integer32):
    """Custom type ncmT1PortLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortLOS_Type.__name__ = "Integer32"
_NcmT1PortLOS_Object = MibTableColumn
ncmT1PortLOS = _NcmT1PortLOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 8),
    _NcmT1PortLOS_Type()
)
ncmT1PortLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortLOS.setStatus("mandatory")


class _NcmT1PortBPVThresholdExceeded_Type(Integer32):
    """Custom type ncmT1PortBPVThresholdExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortBPVThresholdExceeded_Type.__name__ = "Integer32"
_NcmT1PortBPVThresholdExceeded_Object = MibTableColumn
ncmT1PortBPVThresholdExceeded = _NcmT1PortBPVThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 9),
    _NcmT1PortBPVThresholdExceeded_Type()
)
ncmT1PortBPVThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortBPVThresholdExceeded.setStatus("mandatory")
_NcmT1BlockErrorCounter_Type = Gauge32
_NcmT1BlockErrorCounter_Object = MibTableColumn
ncmT1BlockErrorCounter = _NcmT1BlockErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 10),
    _NcmT1BlockErrorCounter_Type()
)
ncmT1BlockErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1BlockErrorCounter.setStatus("mandatory")


class _NcmT1BERExceeded_Type(Integer32):
    """Custom type ncmT1BERExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1BERExceeded_Type.__name__ = "Integer32"
_NcmT1BERExceeded_Object = MibTableColumn
ncmT1BERExceeded = _NcmT1BERExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 11),
    _NcmT1BERExceeded_Type()
)
ncmT1BERExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1BERExceeded.setStatus("mandatory")


class _NcmT1PortSendRAI_Type(Integer32):
    """Custom type ncmT1PortSendRAI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortSendRAI_Type.__name__ = "Integer32"
_NcmT1PortSendRAI_Object = MibTableColumn
ncmT1PortSendRAI = _NcmT1PortSendRAI_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 12),
    _NcmT1PortSendRAI_Type()
)
ncmT1PortSendRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortSendRAI.setStatus("mandatory")


class _NcmT1PortSendAIS_Type(Integer32):
    """Custom type ncmT1PortSendAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortSendAIS_Type.__name__ = "Integer32"
_NcmT1PortSendAIS_Object = MibTableColumn
ncmT1PortSendAIS = _NcmT1PortSendAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 13),
    _NcmT1PortSendAIS_Type()
)
ncmT1PortSendAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortSendAIS.setStatus("mandatory")


class _NcmT1PortCGA_Type(Integer32):
    """Custom type ncmT1PortCGA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortCGA_Type.__name__ = "Integer32"
_NcmT1PortCGA_Object = MibTableColumn
ncmT1PortCGA = _NcmT1PortCGA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 14),
    _NcmT1PortCGA_Type()
)
ncmT1PortCGA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortCGA.setStatus("mandatory")


class _NcmT1PortLLB_Type(Integer32):
    """Custom type ncmT1PortLLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortLLB_Type.__name__ = "Integer32"
_NcmT1PortLLB_Object = MibTableColumn
ncmT1PortLLB = _NcmT1PortLLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 15),
    _NcmT1PortLLB_Type()
)
ncmT1PortLLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortLLB.setStatus("mandatory")


class _NcmT1PortPLB_Type(Integer32):
    """Custom type ncmT1PortPLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortPLB_Type.__name__ = "Integer32"
_NcmT1PortPLB_Object = MibTableColumn
ncmT1PortPLB = _NcmT1PortPLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 16),
    _NcmT1PortPLB_Type()
)
ncmT1PortPLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortPLB.setStatus("mandatory")


class _NcmT1PortLOC_Type(Integer32):
    """Custom type ncmT1PortLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1PortLOC_Type.__name__ = "Integer32"
_NcmT1PortLOC_Object = MibTableColumn
ncmT1PortLOC = _NcmT1PortLOC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 17),
    _NcmT1PortLOC_Type()
)
ncmT1PortLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortLOC.setStatus("mandatory")


class _NcmT1PortTestPattern_Type(Integer32):
    """Custom type ncmT1PortTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all-ones", 9),
          ("all-zeros", 7),
          ("fifty-octets", 8),
          ("none", 1),
          ("one-in-8", 5),
          ("qRSS", 3),
          ("three-24", 2),
          ("two-n-15-1", 6),
          ("two-n-20-1", 4))
    )


_NcmT1PortTestPattern_Type.__name__ = "Integer32"
_NcmT1PortTestPattern_Object = MibTableColumn
ncmT1PortTestPattern = _NcmT1PortTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1018, 1, 18),
    _NcmT1PortTestPattern_Type()
)
ncmT1PortTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PortTestPattern.setStatus("mandatory")
_NcmT1CurrentTable_Object = MibTable
ncmT1CurrentTable = _NcmT1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019)
)
if mibBuilder.loadTexts:
    ncmT1CurrentTable.setStatus("mandatory")
_NcmT1CurrentEntry_Object = MibTableRow
ncmT1CurrentEntry = _NcmT1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1)
)
ncmT1CurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1CurrentNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1CurrentIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1CurrentEndType"),
)
if mibBuilder.loadTexts:
    ncmT1CurrentEntry.setStatus("mandatory")


class _NcmT1CurrentNIDIndex_Type(Integer32):
    """Custom type ncmT1CurrentNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1CurrentNIDIndex_Type.__name__ = "Integer32"
_NcmT1CurrentNIDIndex_Object = MibTableColumn
ncmT1CurrentNIDIndex = _NcmT1CurrentNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 1),
    _NcmT1CurrentNIDIndex_Type()
)
ncmT1CurrentNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentNIDIndex.setStatus("mandatory")


class _NcmT1CurrentIndex_Type(Integer32):
    """Custom type ncmT1CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1CurrentIndex_Type.__name__ = "Integer32"
_NcmT1CurrentIndex_Object = MibTableColumn
ncmT1CurrentIndex = _NcmT1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 2),
    _NcmT1CurrentIndex_Type()
)
ncmT1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentIndex.setStatus("mandatory")


class _NcmT1CurrentEndType_Type(Integer32):
    """Custom type ncmT1CurrentEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmT1CurrentEndType_Type.__name__ = "Integer32"
_NcmT1CurrentEndType_Object = MibTableColumn
ncmT1CurrentEndType = _NcmT1CurrentEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 3),
    _NcmT1CurrentEndType_Type()
)
ncmT1CurrentEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentEndType.setStatus("mandatory")
_NcmT1Timestamp_Type = Integer32
_NcmT1Timestamp_Object = MibTableColumn
ncmT1Timestamp = _NcmT1Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 4),
    _NcmT1Timestamp_Type()
)
ncmT1Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1Timestamp.setStatus("mandatory")
_NcmT1Timestamp1_Type = Integer32
_NcmT1Timestamp1_Object = MibTableColumn
ncmT1Timestamp1 = _NcmT1Timestamp1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 5),
    _NcmT1Timestamp1_Type()
)
ncmT1Timestamp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1Timestamp1.setStatus("mandatory")
_NcmT1CurrentIntervalSec_Type = Integer32
_NcmT1CurrentIntervalSec_Object = MibTableColumn
ncmT1CurrentIntervalSec = _NcmT1CurrentIntervalSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 6),
    _NcmT1CurrentIntervalSec_Type()
)
ncmT1CurrentIntervalSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentIntervalSec.setStatus("mandatory")
_NcmT1CurrentASs_Type = Gauge32
_NcmT1CurrentASs_Object = MibTableColumn
ncmT1CurrentASs = _NcmT1CurrentASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 7),
    _NcmT1CurrentASs_Type()
)
ncmT1CurrentASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentASs.setStatus("mandatory")
_NcmT1CurrentUASs_Type = Gauge32
_NcmT1CurrentUASs_Object = MibTableColumn
ncmT1CurrentUASs = _NcmT1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 8),
    _NcmT1CurrentUASs_Type()
)
ncmT1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentUASs.setStatus("mandatory")
_NcmT1CurrentESs_Type = Gauge32
_NcmT1CurrentESs_Object = MibTableColumn
ncmT1CurrentESs = _NcmT1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 9),
    _NcmT1CurrentESs_Type()
)
ncmT1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentESs.setStatus("mandatory")
_NcmT1CurrentBESs_Type = Gauge32
_NcmT1CurrentBESs_Object = MibTableColumn
ncmT1CurrentBESs = _NcmT1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 10),
    _NcmT1CurrentBESs_Type()
)
ncmT1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentBESs.setStatus("mandatory")
_NcmT1CurrentSESs_Type = Gauge32
_NcmT1CurrentSESs_Object = MibTableColumn
ncmT1CurrentSESs = _NcmT1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 11),
    _NcmT1CurrentSESs_Type()
)
ncmT1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentSESs.setStatus("mandatory")
_NcmT1CurrentSEFs_Type = Gauge32
_NcmT1CurrentSEFs_Object = MibTableColumn
ncmT1CurrentSEFs = _NcmT1CurrentSEFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 12),
    _NcmT1CurrentSEFs_Type()
)
ncmT1CurrentSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentSEFs.setStatus("mandatory")
_NcmT1CurrentLOSs_Type = Gauge32
_NcmT1CurrentLOSs_Object = MibTableColumn
ncmT1CurrentLOSs = _NcmT1CurrentLOSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 13),
    _NcmT1CurrentLOSs_Type()
)
ncmT1CurrentLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentLOSs.setStatus("mandatory")
_NcmT1CurrentAISs_Type = Gauge32
_NcmT1CurrentAISs_Object = MibTableColumn
ncmT1CurrentAISs = _NcmT1CurrentAISs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 14),
    _NcmT1CurrentAISs_Type()
)
ncmT1CurrentAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentAISs.setStatus("mandatory")
_NcmT1CurrentLOFs_Type = Gauge32
_NcmT1CurrentLOFs_Object = MibTableColumn
ncmT1CurrentLOFs = _NcmT1CurrentLOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 15),
    _NcmT1CurrentLOFs_Type()
)
ncmT1CurrentLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentLOFs.setStatus("mandatory")
_NcmT1CurrentOOFs_Type = Gauge32
_NcmT1CurrentOOFs_Object = MibTableColumn
ncmT1CurrentOOFs = _NcmT1CurrentOOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 16),
    _NcmT1CurrentOOFs_Type()
)
ncmT1CurrentOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentOOFs.setStatus("mandatory")
_NcmT1CurrentESsTypeA_Type = Gauge32
_NcmT1CurrentESsTypeA_Object = MibTableColumn
ncmT1CurrentESsTypeA = _NcmT1CurrentESsTypeA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 17),
    _NcmT1CurrentESsTypeA_Type()
)
ncmT1CurrentESsTypeA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentESsTypeA.setStatus("mandatory")
_NcmT1CurrentSASs_Type = Gauge32
_NcmT1CurrentSASs_Object = MibTableColumn
ncmT1CurrentSASs = _NcmT1CurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 18),
    _NcmT1CurrentSASs_Type()
)
ncmT1CurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentSASs.setStatus("mandatory")
_NcmT1CurrentCSSs_Type = Gauge32
_NcmT1CurrentCSSs_Object = MibTableColumn
ncmT1CurrentCSSs = _NcmT1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 19),
    _NcmT1CurrentCSSs_Type()
)
ncmT1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentCSSs.setStatus("mandatory")
_NcmT1CurrentLOFC_Type = Gauge32
_NcmT1CurrentLOFC_Object = MibTableColumn
ncmT1CurrentLOFC = _NcmT1CurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 20),
    _NcmT1CurrentLOFC_Type()
)
ncmT1CurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentLOFC.setStatus("mandatory")
_NcmT1CurrentFrameErrCount_Type = Gauge32
_NcmT1CurrentFrameErrCount_Object = MibTableColumn
ncmT1CurrentFrameErrCount = _NcmT1CurrentFrameErrCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 21),
    _NcmT1CurrentFrameErrCount_Type()
)
ncmT1CurrentFrameErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentFrameErrCount.setStatus("mandatory")
_NcmT1CurrentErrorFreeSec_Type = Gauge32
_NcmT1CurrentErrorFreeSec_Object = MibTableColumn
ncmT1CurrentErrorFreeSec = _NcmT1CurrentErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 22),
    _NcmT1CurrentErrorFreeSec_Type()
)
ncmT1CurrentErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentErrorFreeSec.setStatus("mandatory")
_NcmT1CurrentDegradedMin_Type = Gauge32
_NcmT1CurrentDegradedMin_Object = MibTableColumn
ncmT1CurrentDegradedMin = _NcmT1CurrentDegradedMin_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1019, 1, 23),
    _NcmT1CurrentDegradedMin_Type()
)
ncmT1CurrentDegradedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrentDegradedMin.setStatus("mandatory")
_NcmT1IntervalTable_Object = MibTable
ncmT1IntervalTable = _NcmT1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020)
)
if mibBuilder.loadTexts:
    ncmT1IntervalTable.setStatus("mandatory")
_NcmT1IntervalEntry_Object = MibTableRow
ncmT1IntervalEntry = _NcmT1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1)
)
ncmT1IntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1IntervalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1IntervalIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1IntervalEndType"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1IntervalNumber"),
)
if mibBuilder.loadTexts:
    ncmT1IntervalEntry.setStatus("mandatory")


class _NcmT1IntervalNIDIndex_Type(Integer32):
    """Custom type ncmT1IntervalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1IntervalNIDIndex_Type.__name__ = "Integer32"
_NcmT1IntervalNIDIndex_Object = MibTableColumn
ncmT1IntervalNIDIndex = _NcmT1IntervalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 1),
    _NcmT1IntervalNIDIndex_Type()
)
ncmT1IntervalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalNIDIndex.setStatus("mandatory")


class _NcmT1IntervalIndex_Type(Integer32):
    """Custom type ncmT1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1IntervalIndex_Type.__name__ = "Integer32"
_NcmT1IntervalIndex_Object = MibTableColumn
ncmT1IntervalIndex = _NcmT1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 2),
    _NcmT1IntervalIndex_Type()
)
ncmT1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalIndex.setStatus("mandatory")


class _NcmT1IntervalEndType_Type(Integer32):
    """Custom type ncmT1IntervalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmT1IntervalEndType_Type.__name__ = "Integer32"
_NcmT1IntervalEndType_Object = MibTableColumn
ncmT1IntervalEndType = _NcmT1IntervalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 3),
    _NcmT1IntervalEndType_Type()
)
ncmT1IntervalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalEndType.setStatus("mandatory")


class _NcmT1IntervalNumber_Type(Integer32):
    """Custom type ncmT1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NcmT1IntervalNumber_Type.__name__ = "Integer32"
_NcmT1IntervalNumber_Object = MibTableColumn
ncmT1IntervalNumber = _NcmT1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 4),
    _NcmT1IntervalNumber_Type()
)
ncmT1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalNumber.setStatus("mandatory")
_NcmT1IntervalASs_Type = Gauge32
_NcmT1IntervalASs_Object = MibTableColumn
ncmT1IntervalASs = _NcmT1IntervalASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 5),
    _NcmT1IntervalASs_Type()
)
ncmT1IntervalASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalASs.setStatus("mandatory")
_NcmT1IntervalUASs_Type = Gauge32
_NcmT1IntervalUASs_Object = MibTableColumn
ncmT1IntervalUASs = _NcmT1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 6),
    _NcmT1IntervalUASs_Type()
)
ncmT1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalUASs.setStatus("mandatory")
_NcmT1IntervalESs_Type = Gauge32
_NcmT1IntervalESs_Object = MibTableColumn
ncmT1IntervalESs = _NcmT1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 7),
    _NcmT1IntervalESs_Type()
)
ncmT1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalESs.setStatus("mandatory")
_NcmT1IntervalBESs_Type = Gauge32
_NcmT1IntervalBESs_Object = MibTableColumn
ncmT1IntervalBESs = _NcmT1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 8),
    _NcmT1IntervalBESs_Type()
)
ncmT1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalBESs.setStatus("mandatory")
_NcmT1IntervalSESs_Type = Gauge32
_NcmT1IntervalSESs_Object = MibTableColumn
ncmT1IntervalSESs = _NcmT1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 9),
    _NcmT1IntervalSESs_Type()
)
ncmT1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalSESs.setStatus("mandatory")
_NcmT1IntervalSEFs_Type = Gauge32
_NcmT1IntervalSEFs_Object = MibTableColumn
ncmT1IntervalSEFs = _NcmT1IntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 10),
    _NcmT1IntervalSEFs_Type()
)
ncmT1IntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalSEFs.setStatus("mandatory")
_NcmT1IntervalLOSs_Type = Gauge32
_NcmT1IntervalLOSs_Object = MibTableColumn
ncmT1IntervalLOSs = _NcmT1IntervalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 11),
    _NcmT1IntervalLOSs_Type()
)
ncmT1IntervalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalLOSs.setStatus("mandatory")
_NcmT1IntervalAISs_Type = Gauge32
_NcmT1IntervalAISs_Object = MibTableColumn
ncmT1IntervalAISs = _NcmT1IntervalAISs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 12),
    _NcmT1IntervalAISs_Type()
)
ncmT1IntervalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalAISs.setStatus("mandatory")
_NcmT1IntervalLOFs_Type = Gauge32
_NcmT1IntervalLOFs_Object = MibTableColumn
ncmT1IntervalLOFs = _NcmT1IntervalLOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 13),
    _NcmT1IntervalLOFs_Type()
)
ncmT1IntervalLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalLOFs.setStatus("mandatory")
_NcmT1IntervalOOFs_Type = Gauge32
_NcmT1IntervalOOFs_Object = MibTableColumn
ncmT1IntervalOOFs = _NcmT1IntervalOOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 14),
    _NcmT1IntervalOOFs_Type()
)
ncmT1IntervalOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalOOFs.setStatus("mandatory")
_NcmT1IntervalESsTypeA_Type = Gauge32
_NcmT1IntervalESsTypeA_Object = MibTableColumn
ncmT1IntervalESsTypeA = _NcmT1IntervalESsTypeA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 15),
    _NcmT1IntervalESsTypeA_Type()
)
ncmT1IntervalESsTypeA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalESsTypeA.setStatus("mandatory")
_NcmT1IntervalSASs_Type = Gauge32
_NcmT1IntervalSASs_Object = MibTableColumn
ncmT1IntervalSASs = _NcmT1IntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 16),
    _NcmT1IntervalSASs_Type()
)
ncmT1IntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalSASs.setStatus("mandatory")
_NcmT1IntervalCSSs_Type = Gauge32
_NcmT1IntervalCSSs_Object = MibTableColumn
ncmT1IntervalCSSs = _NcmT1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 17),
    _NcmT1IntervalCSSs_Type()
)
ncmT1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalCSSs.setStatus("mandatory")
_NcmT1IntervalLOFC_Type = Gauge32
_NcmT1IntervalLOFC_Object = MibTableColumn
ncmT1IntervalLOFC = _NcmT1IntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 18),
    _NcmT1IntervalLOFC_Type()
)
ncmT1IntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalLOFC.setStatus("mandatory")
_NcmT1IntervalFrameErr_Type = Gauge32
_NcmT1IntervalFrameErr_Object = MibTableColumn
ncmT1IntervalFrameErr = _NcmT1IntervalFrameErr_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 19),
    _NcmT1IntervalFrameErr_Type()
)
ncmT1IntervalFrameErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalFrameErr.setStatus("mandatory")
_NcmT1IntervalErrFreeSec_Type = Gauge32
_NcmT1IntervalErrFreeSec_Object = MibTableColumn
ncmT1IntervalErrFreeSec = _NcmT1IntervalErrFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 20),
    _NcmT1IntervalErrFreeSec_Type()
)
ncmT1IntervalErrFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalErrFreeSec.setStatus("mandatory")
_NcmT1IntervalDegradMin_Type = Gauge32
_NcmT1IntervalDegradMin_Object = MibTableColumn
ncmT1IntervalDegradMin = _NcmT1IntervalDegradMin_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1020, 1, 21),
    _NcmT1IntervalDegradMin_Type()
)
ncmT1IntervalDegradMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1IntervalDegradMin.setStatus("mandatory")
_NcmT1TotalTable_Object = MibTable
ncmT1TotalTable = _NcmT1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021)
)
if mibBuilder.loadTexts:
    ncmT1TotalTable.setStatus("mandatory")
_NcmT1TotalEntry_Object = MibTableRow
ncmT1TotalEntry = _NcmT1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1)
)
ncmT1TotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1TotalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1TotalIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1TotalEndType"),
)
if mibBuilder.loadTexts:
    ncmT1TotalEntry.setStatus("mandatory")


class _NcmT1TotalNIDIndex_Type(Integer32):
    """Custom type ncmT1TotalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1TotalNIDIndex_Type.__name__ = "Integer32"
_NcmT1TotalNIDIndex_Object = MibTableColumn
ncmT1TotalNIDIndex = _NcmT1TotalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 1),
    _NcmT1TotalNIDIndex_Type()
)
ncmT1TotalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalNIDIndex.setStatus("mandatory")


class _NcmT1TotalIndex_Type(Integer32):
    """Custom type ncmT1TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1TotalIndex_Type.__name__ = "Integer32"
_NcmT1TotalIndex_Object = MibTableColumn
ncmT1TotalIndex = _NcmT1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 2),
    _NcmT1TotalIndex_Type()
)
ncmT1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalIndex.setStatus("mandatory")


class _NcmT1TotalEndType_Type(Integer32):
    """Custom type ncmT1TotalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmT1TotalEndType_Type.__name__ = "Integer32"
_NcmT1TotalEndType_Object = MibTableColumn
ncmT1TotalEndType = _NcmT1TotalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 3),
    _NcmT1TotalEndType_Type()
)
ncmT1TotalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalEndType.setStatus("mandatory")
_NcmT1NumberOfValidIntervals_Type = Integer32
_NcmT1NumberOfValidIntervals_Object = MibTableColumn
ncmT1NumberOfValidIntervals = _NcmT1NumberOfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 4),
    _NcmT1NumberOfValidIntervals_Type()
)
ncmT1NumberOfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1NumberOfValidIntervals.setStatus("mandatory")
_NcmT1TotalASs_Type = Gauge32
_NcmT1TotalASs_Object = MibTableColumn
ncmT1TotalASs = _NcmT1TotalASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 5),
    _NcmT1TotalASs_Type()
)
ncmT1TotalASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalASs.setStatus("mandatory")
_NcmT1TotalUASs_Type = Gauge32
_NcmT1TotalUASs_Object = MibTableColumn
ncmT1TotalUASs = _NcmT1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 6),
    _NcmT1TotalUASs_Type()
)
ncmT1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalUASs.setStatus("mandatory")
_NcmT1TotalESs_Type = Gauge32
_NcmT1TotalESs_Object = MibTableColumn
ncmT1TotalESs = _NcmT1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 7),
    _NcmT1TotalESs_Type()
)
ncmT1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalESs.setStatus("mandatory")
_NcmT1TotalBESs_Type = Gauge32
_NcmT1TotalBESs_Object = MibTableColumn
ncmT1TotalBESs = _NcmT1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 8),
    _NcmT1TotalBESs_Type()
)
ncmT1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalBESs.setStatus("mandatory")
_NcmT1TotalSESs_Type = Gauge32
_NcmT1TotalSESs_Object = MibTableColumn
ncmT1TotalSESs = _NcmT1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 9),
    _NcmT1TotalSESs_Type()
)
ncmT1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalSESs.setStatus("mandatory")
_NcmT1TotalSEFs_Type = Gauge32
_NcmT1TotalSEFs_Object = MibTableColumn
ncmT1TotalSEFs = _NcmT1TotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 10),
    _NcmT1TotalSEFs_Type()
)
ncmT1TotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalSEFs.setStatus("mandatory")
_NcmT1TotalLOSs_Type = Gauge32
_NcmT1TotalLOSs_Object = MibTableColumn
ncmT1TotalLOSs = _NcmT1TotalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 11),
    _NcmT1TotalLOSs_Type()
)
ncmT1TotalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalLOSs.setStatus("mandatory")
_NcmT1TotalAISs_Type = Gauge32
_NcmT1TotalAISs_Object = MibTableColumn
ncmT1TotalAISs = _NcmT1TotalAISs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 12),
    _NcmT1TotalAISs_Type()
)
ncmT1TotalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalAISs.setStatus("mandatory")
_NcmT1TotalLOFs_Type = Gauge32
_NcmT1TotalLOFs_Object = MibTableColumn
ncmT1TotalLOFs = _NcmT1TotalLOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 13),
    _NcmT1TotalLOFs_Type()
)
ncmT1TotalLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalLOFs.setStatus("mandatory")
_NcmT1TotalOOFs_Type = Gauge32
_NcmT1TotalOOFs_Object = MibTableColumn
ncmT1TotalOOFs = _NcmT1TotalOOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 14),
    _NcmT1TotalOOFs_Type()
)
ncmT1TotalOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalOOFs.setStatus("mandatory")
_NcmT1TotalESsTypeA_Type = Gauge32
_NcmT1TotalESsTypeA_Object = MibTableColumn
ncmT1TotalESsTypeA = _NcmT1TotalESsTypeA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 15),
    _NcmT1TotalESsTypeA_Type()
)
ncmT1TotalESsTypeA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalESsTypeA.setStatus("mandatory")
_NcmT1TotalSASs_Type = Gauge32
_NcmT1TotalSASs_Object = MibTableColumn
ncmT1TotalSASs = _NcmT1TotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 16),
    _NcmT1TotalSASs_Type()
)
ncmT1TotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalSASs.setStatus("mandatory")
_NcmT1TotalCSSs_Type = Gauge32
_NcmT1TotalCSSs_Object = MibTableColumn
ncmT1TotalCSSs = _NcmT1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 17),
    _NcmT1TotalCSSs_Type()
)
ncmT1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalCSSs.setStatus("mandatory")
_NcmT1TotalLOFC_Type = Gauge32
_NcmT1TotalLOFC_Object = MibTableColumn
ncmT1TotalLOFC = _NcmT1TotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 18),
    _NcmT1TotalLOFC_Type()
)
ncmT1TotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalLOFC.setStatus("mandatory")
_NcmT1TotalFrameErrCount_Type = Gauge32
_NcmT1TotalFrameErrCount_Object = MibTableColumn
ncmT1TotalFrameErrCount = _NcmT1TotalFrameErrCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 19),
    _NcmT1TotalFrameErrCount_Type()
)
ncmT1TotalFrameErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalFrameErrCount.setStatus("mandatory")
_NcmT1TotalErrorFreeSec_Type = Gauge32
_NcmT1TotalErrorFreeSec_Object = MibTableColumn
ncmT1TotalErrorFreeSec = _NcmT1TotalErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 20),
    _NcmT1TotalErrorFreeSec_Type()
)
ncmT1TotalErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalErrorFreeSec.setStatus("mandatory")
_NcmT1TotalDegradedMin_Type = Gauge32
_NcmT1TotalDegradedMin_Object = MibTableColumn
ncmT1TotalDegradedMin = _NcmT1TotalDegradedMin_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1021, 1, 21),
    _NcmT1TotalDegradedMin_Type()
)
ncmT1TotalDegradedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TotalDegradedMin.setStatus("mandatory")
_NcmT1PrevTotalTable_Object = MibTable
ncmT1PrevTotalTable = _NcmT1PrevTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022)
)
if mibBuilder.loadTexts:
    ncmT1PrevTotalTable.setStatus("mandatory")
_NcmT1PrevTotalEntry_Object = MibTableRow
ncmT1PrevTotalEntry = _NcmT1PrevTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1)
)
ncmT1PrevTotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1PrevTotalNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1PrevTotalIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1PrevTotalEndType"),
)
if mibBuilder.loadTexts:
    ncmT1PrevTotalEntry.setStatus("mandatory")


class _NcmT1PrevTotalNIDIndex_Type(Integer32):
    """Custom type ncmT1PrevTotalNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1PrevTotalNIDIndex_Type.__name__ = "Integer32"
_NcmT1PrevTotalNIDIndex_Object = MibTableColumn
ncmT1PrevTotalNIDIndex = _NcmT1PrevTotalNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 1),
    _NcmT1PrevTotalNIDIndex_Type()
)
ncmT1PrevTotalNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalNIDIndex.setStatus("mandatory")


class _NcmT1PrevTotalIndex_Type(Integer32):
    """Custom type ncmT1PrevTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1PrevTotalIndex_Type.__name__ = "Integer32"
_NcmT1PrevTotalIndex_Object = MibTableColumn
ncmT1PrevTotalIndex = _NcmT1PrevTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 2),
    _NcmT1PrevTotalIndex_Type()
)
ncmT1PrevTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalIndex.setStatus("mandatory")


class _NcmT1PrevTotalEndType_Type(Integer32):
    """Custom type ncmT1PrevTotalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmT1PrevTotalEndType_Type.__name__ = "Integer32"
_NcmT1PrevTotalEndType_Object = MibTableColumn
ncmT1PrevTotalEndType = _NcmT1PrevTotalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 3),
    _NcmT1PrevTotalEndType_Type()
)
ncmT1PrevTotalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalEndType.setStatus("mandatory")
_NcmT1PrevTotalASs_Type = Gauge32
_NcmT1PrevTotalASs_Object = MibTableColumn
ncmT1PrevTotalASs = _NcmT1PrevTotalASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 4),
    _NcmT1PrevTotalASs_Type()
)
ncmT1PrevTotalASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalASs.setStatus("mandatory")
_NcmT1PrevTotalUASs_Type = Gauge32
_NcmT1PrevTotalUASs_Object = MibTableColumn
ncmT1PrevTotalUASs = _NcmT1PrevTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 5),
    _NcmT1PrevTotalUASs_Type()
)
ncmT1PrevTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalUASs.setStatus("mandatory")
_NcmT1PrevTotalESs_Type = Gauge32
_NcmT1PrevTotalESs_Object = MibTableColumn
ncmT1PrevTotalESs = _NcmT1PrevTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 6),
    _NcmT1PrevTotalESs_Type()
)
ncmT1PrevTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalESs.setStatus("mandatory")
_NcmT1PrevTotalBESs_Type = Gauge32
_NcmT1PrevTotalBESs_Object = MibTableColumn
ncmT1PrevTotalBESs = _NcmT1PrevTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 7),
    _NcmT1PrevTotalBESs_Type()
)
ncmT1PrevTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalBESs.setStatus("mandatory")
_NcmT1PrevTotalSESs_Type = Gauge32
_NcmT1PrevTotalSESs_Object = MibTableColumn
ncmT1PrevTotalSESs = _NcmT1PrevTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 8),
    _NcmT1PrevTotalSESs_Type()
)
ncmT1PrevTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalSESs.setStatus("mandatory")
_NcmT1PrevTotalSEFs_Type = Gauge32
_NcmT1PrevTotalSEFs_Object = MibTableColumn
ncmT1PrevTotalSEFs = _NcmT1PrevTotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 9),
    _NcmT1PrevTotalSEFs_Type()
)
ncmT1PrevTotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalSEFs.setStatus("mandatory")
_NcmT1PrevTotalLOSs_Type = Gauge32
_NcmT1PrevTotalLOSs_Object = MibTableColumn
ncmT1PrevTotalLOSs = _NcmT1PrevTotalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 10),
    _NcmT1PrevTotalLOSs_Type()
)
ncmT1PrevTotalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalLOSs.setStatus("mandatory")
_NcmT1PrevTotalAISs_Type = Gauge32
_NcmT1PrevTotalAISs_Object = MibTableColumn
ncmT1PrevTotalAISs = _NcmT1PrevTotalAISs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 11),
    _NcmT1PrevTotalAISs_Type()
)
ncmT1PrevTotalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalAISs.setStatus("mandatory")
_NcmT1PrevTotalLOFs_Type = Gauge32
_NcmT1PrevTotalLOFs_Object = MibTableColumn
ncmT1PrevTotalLOFs = _NcmT1PrevTotalLOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 12),
    _NcmT1PrevTotalLOFs_Type()
)
ncmT1PrevTotalLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalLOFs.setStatus("mandatory")
_NcmT1PrevTotalOOFs_Type = Gauge32
_NcmT1PrevTotalOOFs_Object = MibTableColumn
ncmT1PrevTotalOOFs = _NcmT1PrevTotalOOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 13),
    _NcmT1PrevTotalOOFs_Type()
)
ncmT1PrevTotalOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalOOFs.setStatus("mandatory")
_NcmT1PrevTotalESsTypeA_Type = Gauge32
_NcmT1PrevTotalESsTypeA_Object = MibTableColumn
ncmT1PrevTotalESsTypeA = _NcmT1PrevTotalESsTypeA_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 14),
    _NcmT1PrevTotalESsTypeA_Type()
)
ncmT1PrevTotalESsTypeA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalESsTypeA.setStatus("mandatory")
_NcmT1PrevTotalSASs_Type = Gauge32
_NcmT1PrevTotalSASs_Object = MibTableColumn
ncmT1PrevTotalSASs = _NcmT1PrevTotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 15),
    _NcmT1PrevTotalSASs_Type()
)
ncmT1PrevTotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalSASs.setStatus("mandatory")
_NcmT1PrevTotalCSSs_Type = Gauge32
_NcmT1PrevTotalCSSs_Object = MibTableColumn
ncmT1PrevTotalCSSs = _NcmT1PrevTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 16),
    _NcmT1PrevTotalCSSs_Type()
)
ncmT1PrevTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalCSSs.setStatus("mandatory")
_NcmT1PrevTotalLOFC_Type = Gauge32
_NcmT1PrevTotalLOFC_Object = MibTableColumn
ncmT1PrevTotalLOFC = _NcmT1PrevTotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 17),
    _NcmT1PrevTotalLOFC_Type()
)
ncmT1PrevTotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalLOFC.setStatus("mandatory")
_NcmT1PrevTotalFrameErrCount_Type = Gauge32
_NcmT1PrevTotalFrameErrCount_Object = MibTableColumn
ncmT1PrevTotalFrameErrCount = _NcmT1PrevTotalFrameErrCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 18),
    _NcmT1PrevTotalFrameErrCount_Type()
)
ncmT1PrevTotalFrameErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalFrameErrCount.setStatus("mandatory")
_NcmT1PrevTotalErrorFreeSec_Type = Gauge32
_NcmT1PrevTotalErrorFreeSec_Object = MibTableColumn
ncmT1PrevTotalErrorFreeSec = _NcmT1PrevTotalErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 19),
    _NcmT1PrevTotalErrorFreeSec_Type()
)
ncmT1PrevTotalErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalErrorFreeSec.setStatus("mandatory")
_NcmT1PrevTotalDegradedMin_Type = Gauge32
_NcmT1PrevTotalDegradedMin_Object = MibTableColumn
ncmT1PrevTotalDegradedMin = _NcmT1PrevTotalDegradedMin_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1022, 1, 20),
    _NcmT1PrevTotalDegradedMin_Type()
)
ncmT1PrevTotalDegradedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PrevTotalDegradedMin.setStatus("mandatory")
_NcmT1PreformanceSnapShotTable_Object = MibTable
ncmT1PreformanceSnapShotTable = _NcmT1PreformanceSnapShotTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023)
)
if mibBuilder.loadTexts:
    ncmT1PreformanceSnapShotTable.setStatus("mandatory")
_NcmT1PreformanceSnapShotEntry_Object = MibTableRow
ncmT1PreformanceSnapShotEntry = _NcmT1PreformanceSnapShotEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1)
)
ncmT1PreformanceSnapShotEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1SnapShotNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1SnapShotIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1SnapShotEndType"),
)
if mibBuilder.loadTexts:
    ncmT1PreformanceSnapShotEntry.setStatus("mandatory")


class _NcmT1SnapShotNIDIndex_Type(Integer32):
    """Custom type ncmT1SnapShotNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1SnapShotNIDIndex_Type.__name__ = "Integer32"
_NcmT1SnapShotNIDIndex_Object = MibTableColumn
ncmT1SnapShotNIDIndex = _NcmT1SnapShotNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1, 1),
    _NcmT1SnapShotNIDIndex_Type()
)
ncmT1SnapShotNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1SnapShotNIDIndex.setStatus("mandatory")


class _NcmT1SnapShotIndex_Type(Integer32):
    """Custom type ncmT1SnapShotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1SnapShotIndex_Type.__name__ = "Integer32"
_NcmT1SnapShotIndex_Object = MibTableColumn
ncmT1SnapShotIndex = _NcmT1SnapShotIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1, 2),
    _NcmT1SnapShotIndex_Type()
)
ncmT1SnapShotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1SnapShotIndex.setStatus("mandatory")


class _NcmT1SnapShotEndType_Type(Integer32):
    """Custom type ncmT1SnapShotEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmT1SnapShotEndType_Type.__name__ = "Integer32"
_NcmT1SnapShotEndType_Object = MibTableColumn
ncmT1SnapShotEndType = _NcmT1SnapShotEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1, 3),
    _NcmT1SnapShotEndType_Type()
)
ncmT1SnapShotEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1SnapShotEndType.setStatus("mandatory")


class _NcmT1SnapShot_Type(Integer32):
    """Custom type ncmT1SnapShot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1SnapShot_Type.__name__ = "Integer32"
_NcmT1SnapShot_Object = MibTableColumn
ncmT1SnapShot = _NcmT1SnapShot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1, 4),
    _NcmT1SnapShot_Type()
)
ncmT1SnapShot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1SnapShot.setStatus("mandatory")
_NcmT1TimeStampSec_Type = Integer32
_NcmT1TimeStampSec_Object = MibTableColumn
ncmT1TimeStampSec = _NcmT1TimeStampSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1, 5),
    _NcmT1TimeStampSec_Type()
)
ncmT1TimeStampSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TimeStampSec.setStatus("mandatory")
_NcmT1TimeStampMilliSec_Type = Integer32
_NcmT1TimeStampMilliSec_Object = MibTableColumn
ncmT1TimeStampMilliSec = _NcmT1TimeStampMilliSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1, 6),
    _NcmT1TimeStampMilliSec_Type()
)
ncmT1TimeStampMilliSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1TimeStampMilliSec.setStatus("mandatory")
_NcmT1CurrIntervalSec_Type = Integer32
_NcmT1CurrIntervalSec_Object = MibTableColumn
ncmT1CurrIntervalSec = _NcmT1CurrIntervalSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1, 7),
    _NcmT1CurrIntervalSec_Type()
)
ncmT1CurrIntervalSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1CurrIntervalSec.setStatus("mandatory")


class _NcmT1ResetPerfReg_Type(Integer32):
    """Custom type ncmT1ResetPerfReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1ResetPerfReg_Type.__name__ = "Integer32"
_NcmT1ResetPerfReg_Object = MibTableColumn
ncmT1ResetPerfReg = _NcmT1ResetPerfReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1023, 1, 8),
    _NcmT1ResetPerfReg_Type()
)
ncmT1ResetPerfReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1ResetPerfReg.setStatus("mandatory")
_NcmAdvancedT1ConfigTable_Object = MibTable
ncmAdvancedT1ConfigTable = _NcmAdvancedT1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024)
)
if mibBuilder.loadTexts:
    ncmAdvancedT1ConfigTable.setStatus("mandatory")
_NcmAdvancedT1ConfigEntry_Object = MibTableRow
ncmAdvancedT1ConfigEntry = _NcmAdvancedT1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1)
)
ncmAdvancedT1ConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmAdvancedT1NIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmAdvancedT1LineIndex"),
)
if mibBuilder.loadTexts:
    ncmAdvancedT1ConfigEntry.setStatus("mandatory")


class _NcmAdvancedT1NIDIndex_Type(Integer32):
    """Custom type ncmAdvancedT1NIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmAdvancedT1NIDIndex_Type.__name__ = "Integer32"
_NcmAdvancedT1NIDIndex_Object = MibTableColumn
ncmAdvancedT1NIDIndex = _NcmAdvancedT1NIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 1),
    _NcmAdvancedT1NIDIndex_Type()
)
ncmAdvancedT1NIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAdvancedT1NIDIndex.setStatus("mandatory")


class _NcmAdvancedT1LineIndex_Type(Integer32):
    """Custom type ncmAdvancedT1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmAdvancedT1LineIndex_Type.__name__ = "Integer32"
_NcmAdvancedT1LineIndex_Object = MibTableColumn
ncmAdvancedT1LineIndex = _NcmAdvancedT1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 2),
    _NcmAdvancedT1LineIndex_Type()
)
ncmAdvancedT1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAdvancedT1LineIndex.setStatus("mandatory")


class _NcmadvfdlMode_Type(Integer32):
    """Custom type ncmadvfdlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 2),
          ("terminated", 1))
    )


_NcmadvfdlMode_Type.__name__ = "Integer32"
_NcmadvfdlMode_Object = MibTableColumn
ncmadvfdlMode = _NcmadvfdlMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 3),
    _NcmadvfdlMode_Type()
)
ncmadvfdlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmadvfdlMode.setStatus("mandatory")


class _NcmadvfdlStandard_Type(Integer32):
    """Custom type ncmadvfdlStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type-54016", 1),
          ("type-T1-403", 2),
          ("type-both", 3))
    )


_NcmadvfdlStandard_Type.__name__ = "Integer32"
_NcmadvfdlStandard_Object = MibTableColumn
ncmadvfdlStandard = _NcmadvfdlStandard_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 4),
    _NcmadvfdlStandard_Type()
)
ncmadvfdlStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmadvfdlStandard.setStatus("mandatory")


class _NcmadvfdlPerformanceReport_Type(Integer32):
    """Custom type ncmadvfdlPerformanceReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("telco", 3),
          ("user", 2))
    )


_NcmadvfdlPerformanceReport_Type.__name__ = "Integer32"
_NcmadvfdlPerformanceReport_Object = MibTableColumn
ncmadvfdlPerformanceReport = _NcmadvfdlPerformanceReport_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 5),
    _NcmadvfdlPerformanceReport_Type()
)
ncmadvfdlPerformanceReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmadvfdlPerformanceReport.setStatus("mandatory")


class _NcmadvfdlLBEnable_Type(Integer32):
    """Custom type ncmadvfdlLBEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmadvfdlLBEnable_Type.__name__ = "Integer32"
_NcmadvfdlLBEnable_Object = MibTableColumn
ncmadvfdlLBEnable = _NcmadvfdlLBEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 6),
    _NcmadvfdlLBEnable_Type()
)
ncmadvfdlLBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmadvfdlLBEnable.setStatus("mandatory")


class _NcmadvfdlLLBT1BOPMsg_Type(Integer32):
    """Custom type ncmadvfdlLLBT1BOPMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmadvfdlLLBT1BOPMsg_Type.__name__ = "Integer32"
_NcmadvfdlLLBT1BOPMsg_Object = MibTableColumn
ncmadvfdlLLBT1BOPMsg = _NcmadvfdlLLBT1BOPMsg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 7),
    _NcmadvfdlLLBT1BOPMsg_Type()
)
ncmadvfdlLLBT1BOPMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmadvfdlLLBT1BOPMsg.setStatus("mandatory")


class _NcmadvfdlPLBT1BOPMsg_Type(Integer32):
    """Custom type ncmadvfdlPLBT1BOPMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmadvfdlPLBT1BOPMsg_Type.__name__ = "Integer32"
_NcmadvfdlPLBT1BOPMsg_Object = MibTableColumn
ncmadvfdlPLBT1BOPMsg = _NcmadvfdlPLBT1BOPMsg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 8),
    _NcmadvfdlPLBT1BOPMsg_Type()
)
ncmadvfdlPLBT1BOPMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmadvfdlPLBT1BOPMsg.setStatus("mandatory")


class _NcmadvfdlIdlePattern_Type(Integer32):
    """Custom type ncmadvfdlIdlePattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-ones", 1),
          ("flags", 2))
    )


_NcmadvfdlIdlePattern_Type.__name__ = "Integer32"
_NcmadvfdlIdlePattern_Object = MibTableColumn
ncmadvfdlIdlePattern = _NcmadvfdlIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 9),
    _NcmadvfdlIdlePattern_Type()
)
ncmadvfdlIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmadvfdlIdlePattern.setStatus("mandatory")


class _NcmadvfdlMonitoringCsuType_Type(Integer32):
    """Custom type ncmadvfdlMonitoringCsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-polling", 2),
          ("polling", 1),
          ("unsolicited-messages", 3))
    )


_NcmadvfdlMonitoringCsuType_Type.__name__ = "Integer32"
_NcmadvfdlMonitoringCsuType_Object = MibTableColumn
ncmadvfdlMonitoringCsuType = _NcmadvfdlMonitoringCsuType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1024, 1, 10),
    _NcmadvfdlMonitoringCsuType_Type()
)
ncmadvfdlMonitoringCsuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmadvfdlMonitoringCsuType.setStatus("mandatory")
_NcmT1LatchedStatusTable_Object = MibTable
ncmT1LatchedStatusTable = _NcmT1LatchedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025)
)
if mibBuilder.loadTexts:
    ncmT1LatchedStatusTable.setStatus("mandatory")
_NcmT1LatchedStatusEntry_Object = MibTableRow
ncmT1LatchedStatusEntry = _NcmT1LatchedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1)
)
ncmT1LatchedStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1LatchedStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1LatchedStatusIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1LatchedStatusEndType"),
)
if mibBuilder.loadTexts:
    ncmT1LatchedStatusEntry.setStatus("mandatory")


class _NcmT1LatchedStatusNIDIndex_Type(Integer32):
    """Custom type ncmT1LatchedStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1LatchedStatusNIDIndex_Type.__name__ = "Integer32"
_NcmT1LatchedStatusNIDIndex_Object = MibTableColumn
ncmT1LatchedStatusNIDIndex = _NcmT1LatchedStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 1),
    _NcmT1LatchedStatusNIDIndex_Type()
)
ncmT1LatchedStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusNIDIndex.setStatus("mandatory")


class _NcmT1LatchedStatusIndex_Type(Integer32):
    """Custom type ncmT1LatchedStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1LatchedStatusIndex_Type.__name__ = "Integer32"
_NcmT1LatchedStatusIndex_Object = MibTableColumn
ncmT1LatchedStatusIndex = _NcmT1LatchedStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 2),
    _NcmT1LatchedStatusIndex_Type()
)
ncmT1LatchedStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusIndex.setStatus("mandatory")


class _NcmT1LatchedStatusEndType_Type(Integer32):
    """Custom type ncmT1LatchedStatusEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmT1LatchedStatusEndType_Type.__name__ = "Integer32"
_NcmT1LatchedStatusEndType_Object = MibTableColumn
ncmT1LatchedStatusEndType = _NcmT1LatchedStatusEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 3),
    _NcmT1LatchedStatusEndType_Type()
)
ncmT1LatchedStatusEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusEndType.setStatus("mandatory")


class _NcmT1LatchedStatusCRC6Error_Type(Integer32):
    """Custom type ncmT1LatchedStatusCRC6Error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1LatchedStatusCRC6Error_Type.__name__ = "Integer32"
_NcmT1LatchedStatusCRC6Error_Object = MibTableColumn
ncmT1LatchedStatusCRC6Error = _NcmT1LatchedStatusCRC6Error_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 4),
    _NcmT1LatchedStatusCRC6Error_Type()
)
ncmT1LatchedStatusCRC6Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusCRC6Error.setStatus("mandatory")


class _NcmT1LatchedStatusFramingSlip_Type(Integer32):
    """Custom type ncmT1LatchedStatusFramingSlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1LatchedStatusFramingSlip_Type.__name__ = "Integer32"
_NcmT1LatchedStatusFramingSlip_Object = MibTableColumn
ncmT1LatchedStatusFramingSlip = _NcmT1LatchedStatusFramingSlip_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 5),
    _NcmT1LatchedStatusFramingSlip_Type()
)
ncmT1LatchedStatusFramingSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusFramingSlip.setStatus("mandatory")


class _NcmT1LatchedStatusRAI_Type(Integer32):
    """Custom type ncmT1LatchedStatusRAI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1LatchedStatusRAI_Type.__name__ = "Integer32"
_NcmT1LatchedStatusRAI_Object = MibTableColumn
ncmT1LatchedStatusRAI = _NcmT1LatchedStatusRAI_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 6),
    _NcmT1LatchedStatusRAI_Type()
)
ncmT1LatchedStatusRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusRAI.setStatus("mandatory")


class _NcmT1LatchedStatusLOF_Type(Integer32):
    """Custom type ncmT1LatchedStatusLOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1LatchedStatusLOF_Type.__name__ = "Integer32"
_NcmT1LatchedStatusLOF_Object = MibTableColumn
ncmT1LatchedStatusLOF = _NcmT1LatchedStatusLOF_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 7),
    _NcmT1LatchedStatusLOF_Type()
)
ncmT1LatchedStatusLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusLOF.setStatus("mandatory")


class _NcmT1LatchedStatusAIS_Type(Integer32):
    """Custom type ncmT1LatchedStatusAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1LatchedStatusAIS_Type.__name__ = "Integer32"
_NcmT1LatchedStatusAIS_Object = MibTableColumn
ncmT1LatchedStatusAIS = _NcmT1LatchedStatusAIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 8),
    _NcmT1LatchedStatusAIS_Type()
)
ncmT1LatchedStatusAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusAIS.setStatus("mandatory")


class _NcmT1LatchedStatusLOS_Type(Integer32):
    """Custom type ncmT1LatchedStatusLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1LatchedStatusLOS_Type.__name__ = "Integer32"
_NcmT1LatchedStatusLOS_Object = MibTableColumn
ncmT1LatchedStatusLOS = _NcmT1LatchedStatusLOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 9),
    _NcmT1LatchedStatusLOS_Type()
)
ncmT1LatchedStatusLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusLOS.setStatus("mandatory")
_NcmT1LatchedStatusBPVThreExcd_Type = Gauge32
_NcmT1LatchedStatusBPVThreExcd_Object = MibTableColumn
ncmT1LatchedStatusBPVThreExcd = _NcmT1LatchedStatusBPVThreExcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 10),
    _NcmT1LatchedStatusBPVThreExcd_Type()
)
ncmT1LatchedStatusBPVThreExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusBPVThreExcd.setStatus("mandatory")
_NcmT1LatchedStatusBERExceeded_Type = Gauge32
_NcmT1LatchedStatusBERExceeded_Object = MibTableColumn
ncmT1LatchedStatusBERExceeded = _NcmT1LatchedStatusBERExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1025, 1, 11),
    _NcmT1LatchedStatusBERExceeded_Type()
)
ncmT1LatchedStatusBERExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1LatchedStatusBERExceeded.setStatus("mandatory")
_NcmT1ThresholdStatusTable_Object = MibTable
ncmT1ThresholdStatusTable = _NcmT1ThresholdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026)
)
if mibBuilder.loadTexts:
    ncmT1ThresholdStatusTable.setStatus("mandatory")
_NcmT1ThresholdStatusEntry_Object = MibTableRow
ncmT1ThresholdStatusEntry = _NcmT1ThresholdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1)
)
ncmT1ThresholdStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1ThresholdStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1ThresholdStatusIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1ThresholdStatusEndType"),
)
if mibBuilder.loadTexts:
    ncmT1ThresholdStatusEntry.setStatus("mandatory")


class _NcmT1ThresholdStatusNIDIndex_Type(Integer32):
    """Custom type ncmT1ThresholdStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1ThresholdStatusNIDIndex_Type.__name__ = "Integer32"
_NcmT1ThresholdStatusNIDIndex_Object = MibTableColumn
ncmT1ThresholdStatusNIDIndex = _NcmT1ThresholdStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 1),
    _NcmT1ThresholdStatusNIDIndex_Type()
)
ncmT1ThresholdStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdStatusNIDIndex.setStatus("mandatory")


class _NcmT1ThresholdStatusIndex_Type(Integer32):
    """Custom type ncmT1ThresholdStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1ThresholdStatusIndex_Type.__name__ = "Integer32"
_NcmT1ThresholdStatusIndex_Object = MibTableColumn
ncmT1ThresholdStatusIndex = _NcmT1ThresholdStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 2),
    _NcmT1ThresholdStatusIndex_Type()
)
ncmT1ThresholdStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdStatusIndex.setStatus("mandatory")


class _NcmT1ThresholdStatusEndType_Type(Integer32):
    """Custom type ncmT1ThresholdStatusEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmT1ThresholdStatusEndType_Type.__name__ = "Integer32"
_NcmT1ThresholdStatusEndType_Object = MibTableColumn
ncmT1ThresholdStatusEndType = _NcmT1ThresholdStatusEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 3),
    _NcmT1ThresholdStatusEndType_Type()
)
ncmT1ThresholdStatusEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdStatusEndType.setStatus("mandatory")


class _NcmT1ThresholdRestoreState_Type(Integer32):
    """Custom type ncmT1ThresholdRestoreState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("in-service", 2),
          ("out-of-service", 1))
    )


_NcmT1ThresholdRestoreState_Type.__name__ = "Integer32"
_NcmT1ThresholdRestoreState_Object = MibTableColumn
ncmT1ThresholdRestoreState = _NcmT1ThresholdRestoreState_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 4),
    _NcmT1ThresholdRestoreState_Type()
)
ncmT1ThresholdRestoreState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdRestoreState.setStatus("mandatory")
_NcmT1ThresholdSecLineRestore_Type = Gauge32
_NcmT1ThresholdSecLineRestore_Object = MibTableColumn
ncmT1ThresholdSecLineRestore = _NcmT1ThresholdSecLineRestore_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 5),
    _NcmT1ThresholdSecLineRestore_Type()
)
ncmT1ThresholdSecLineRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdSecLineRestore.setStatus("mandatory")


class _NcmT1ThresholdBERExceeded_Type(Integer32):
    """Custom type ncmT1ThresholdBERExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1ThresholdBERExceeded_Type.__name__ = "Integer32"
_NcmT1ThresholdBERExceeded_Object = MibTableColumn
ncmT1ThresholdBERExceeded = _NcmT1ThresholdBERExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 6),
    _NcmT1ThresholdBERExceeded_Type()
)
ncmT1ThresholdBERExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdBERExceeded.setStatus("mandatory")
_NcmT1ThresholdBERCount_Type = Gauge32
_NcmT1ThresholdBERCount_Object = MibTableColumn
ncmT1ThresholdBERCount = _NcmT1ThresholdBERCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 7),
    _NcmT1ThresholdBERCount_Type()
)
ncmT1ThresholdBERCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdBERCount.setStatus("mandatory")


class _NcmT1ThresholdSESExceeded_Type(Integer32):
    """Custom type ncmT1ThresholdSESExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1ThresholdSESExceeded_Type.__name__ = "Integer32"
_NcmT1ThresholdSESExceeded_Object = MibTableColumn
ncmT1ThresholdSESExceeded = _NcmT1ThresholdSESExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 8),
    _NcmT1ThresholdSESExceeded_Type()
)
ncmT1ThresholdSESExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdSESExceeded.setStatus("mandatory")
_NcmT1ThresholdSESCount_Type = Gauge32
_NcmT1ThresholdSESCount_Object = MibTableColumn
ncmT1ThresholdSESCount = _NcmT1ThresholdSESCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 9),
    _NcmT1ThresholdSESCount_Type()
)
ncmT1ThresholdSESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdSESCount.setStatus("mandatory")


class _NcmT1ThresholdUASExceeded_Type(Integer32):
    """Custom type ncmT1ThresholdUASExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1ThresholdUASExceeded_Type.__name__ = "Integer32"
_NcmT1ThresholdUASExceeded_Object = MibTableColumn
ncmT1ThresholdUASExceeded = _NcmT1ThresholdUASExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 10),
    _NcmT1ThresholdUASExceeded_Type()
)
ncmT1ThresholdUASExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdUASExceeded.setStatus("mandatory")
_NcmT1ThresholdUASCount_Type = Gauge32
_NcmT1ThresholdUASCount_Object = MibTableColumn
ncmT1ThresholdUASCount = _NcmT1ThresholdUASCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 11),
    _NcmT1ThresholdUASCount_Type()
)
ncmT1ThresholdUASCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdUASCount.setStatus("mandatory")


class _NcmT1ThresholdCRCExceeded_Type(Integer32):
    """Custom type ncmT1ThresholdCRCExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1ThresholdCRCExceeded_Type.__name__ = "Integer32"
_NcmT1ThresholdCRCExceeded_Object = MibTableColumn
ncmT1ThresholdCRCExceeded = _NcmT1ThresholdCRCExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 12),
    _NcmT1ThresholdCRCExceeded_Type()
)
ncmT1ThresholdCRCExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdCRCExceeded.setStatus("mandatory")
_NcmT1ThresholdCRCCount_Type = Gauge32
_NcmT1ThresholdCRCCount_Object = MibTableColumn
ncmT1ThresholdCRCCount = _NcmT1ThresholdCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 13),
    _NcmT1ThresholdCRCCount_Type()
)
ncmT1ThresholdCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdCRCCount.setStatus("mandatory")


class _NcmT1ThresholdBPVExceeded_Type(Integer32):
    """Custom type ncmT1ThresholdBPVExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1ThresholdBPVExceeded_Type.__name__ = "Integer32"
_NcmT1ThresholdBPVExceeded_Object = MibTableColumn
ncmT1ThresholdBPVExceeded = _NcmT1ThresholdBPVExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 14),
    _NcmT1ThresholdBPVExceeded_Type()
)
ncmT1ThresholdBPVExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdBPVExceeded.setStatus("mandatory")
_NcmT1ThresholdBPVCount_Type = Gauge32
_NcmT1ThresholdBPVCount_Object = MibTableColumn
ncmT1ThresholdBPVCount = _NcmT1ThresholdBPVCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1026, 1, 15),
    _NcmT1ThresholdBPVCount_Type()
)
ncmT1ThresholdBPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1ThresholdBPVCount.setStatus("mandatory")
_NcmT1PerformanceCountersTable_Object = MibTable
ncmT1PerformanceCountersTable = _NcmT1PerformanceCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027)
)
if mibBuilder.loadTexts:
    ncmT1PerformanceCountersTable.setStatus("mandatory")
_NcmT1PerformanceCountersEntry_Object = MibTableRow
ncmT1PerformanceCountersEntry = _NcmT1PerformanceCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1)
)
ncmT1PerformanceCountersEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1PerfCountNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1PerfCountIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmT1PerfCountEndType"),
)
if mibBuilder.loadTexts:
    ncmT1PerformanceCountersEntry.setStatus("mandatory")


class _NcmT1PerfCountNIDIndex_Type(Integer32):
    """Custom type ncmT1PerfCountNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1PerfCountNIDIndex_Type.__name__ = "Integer32"
_NcmT1PerfCountNIDIndex_Object = MibTableColumn
ncmT1PerfCountNIDIndex = _NcmT1PerfCountNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 1),
    _NcmT1PerfCountNIDIndex_Type()
)
ncmT1PerfCountNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PerfCountNIDIndex.setStatus("mandatory")


class _NcmT1PerfCountIndex_Type(Integer32):
    """Custom type ncmT1PerfCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmT1PerfCountIndex_Type.__name__ = "Integer32"
_NcmT1PerfCountIndex_Object = MibTableColumn
ncmT1PerfCountIndex = _NcmT1PerfCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 2),
    _NcmT1PerfCountIndex_Type()
)
ncmT1PerfCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PerfCountIndex.setStatus("mandatory")


class _NcmT1PerfCountEndType_Type(Integer32):
    """Custom type ncmT1PerfCountEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmT1PerfCountEndType_Type.__name__ = "Integer32"
_NcmT1PerfCountEndType_Object = MibTableColumn
ncmT1PerfCountEndType = _NcmT1PerfCountEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 3),
    _NcmT1PerfCountEndType_Type()
)
ncmT1PerfCountEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PerfCountEndType.setStatus("mandatory")


class _NcmT1PerfCountFrameMode_Type(Integer32):
    """Custom type ncmT1PerfCountFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 2))
    )


_NcmT1PerfCountFrameMode_Type.__name__ = "Integer32"
_NcmT1PerfCountFrameMode_Object = MibTableColumn
ncmT1PerfCountFrameMode = _NcmT1PerfCountFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 4),
    _NcmT1PerfCountFrameMode_Type()
)
ncmT1PerfCountFrameMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PerfCountFrameMode.setStatus("mandatory")
_NcmT1PerfCountCurESFErrEvt_Type = Gauge32
_NcmT1PerfCountCurESFErrEvt_Object = MibTableColumn
ncmT1PerfCountCurESFErrEvt = _NcmT1PerfCountCurESFErrEvt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 5),
    _NcmT1PerfCountCurESFErrEvt_Type()
)
ncmT1PerfCountCurESFErrEvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PerfCountCurESFErrEvt.setStatus("mandatory")
_NcmT1PerfCountCurBPVErrCnt_Type = Gauge32
_NcmT1PerfCountCurBPVErrCnt_Object = MibTableColumn
ncmT1PerfCountCurBPVErrCnt = _NcmT1PerfCountCurBPVErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 6),
    _NcmT1PerfCountCurBPVErrCnt_Type()
)
ncmT1PerfCountCurBPVErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PerfCountCurBPVErrCnt.setStatus("mandatory")
_NcmT1PerfCountCurFrameErrCnt_Type = Gauge32
_NcmT1PerfCountCurFrameErrCnt_Object = MibTableColumn
ncmT1PerfCountCurFrameErrCnt = _NcmT1PerfCountCurFrameErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 7),
    _NcmT1PerfCountCurFrameErrCnt_Type()
)
ncmT1PerfCountCurFrameErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PerfCountCurFrameErrCnt.setStatus("mandatory")
_NcmT1PerfCountCurCRC6Error_Type = Gauge32
_NcmT1PerfCountCurCRC6Error_Object = MibTableColumn
ncmT1PerfCountCurCRC6Error = _NcmT1PerfCountCurCRC6Error_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 8),
    _NcmT1PerfCountCurCRC6Error_Type()
)
ncmT1PerfCountCurCRC6Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmT1PerfCountCurCRC6Error.setStatus("mandatory")


class _NcmT1ResetPerfCount_Type(Integer32):
    """Custom type ncmT1ResetPerfCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmT1ResetPerfCount_Type.__name__ = "Integer32"
_NcmT1ResetPerfCount_Object = MibTableColumn
ncmT1ResetPerfCount = _NcmT1ResetPerfCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1027, 1, 9),
    _NcmT1ResetPerfCount_Type()
)
ncmT1ResetPerfCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmT1ResetPerfCount.setStatus("mandatory")
_NcmDataPortConfigTable_Object = MibTable
ncmDataPortConfigTable = _NcmDataPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028)
)
if mibBuilder.loadTexts:
    ncmDataPortConfigTable.setStatus("mandatory")
_NcmDataPortConfigEntry_Object = MibTableRow
ncmDataPortConfigEntry = _NcmDataPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1)
)
ncmDataPortConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmDataPortConfigNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmDataPortConfigIndex"),
)
if mibBuilder.loadTexts:
    ncmDataPortConfigEntry.setStatus("mandatory")


class _NcmDataPortConfigNIDIndex_Type(Integer32):
    """Custom type ncmDataPortConfigNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmDataPortConfigNIDIndex_Type.__name__ = "Integer32"
_NcmDataPortConfigNIDIndex_Object = MibTableColumn
ncmDataPortConfigNIDIndex = _NcmDataPortConfigNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 1),
    _NcmDataPortConfigNIDIndex_Type()
)
ncmDataPortConfigNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortConfigNIDIndex.setStatus("mandatory")


class _NcmDataPortConfigIndex_Type(Integer32):
    """Custom type ncmDataPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmDataPortConfigIndex_Type.__name__ = "Integer32"
_NcmDataPortConfigIndex_Object = MibTableColumn
ncmDataPortConfigIndex = _NcmDataPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 2),
    _NcmDataPortConfigIndex_Type()
)
ncmDataPortConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortConfigIndex.setStatus("mandatory")


class _NcmDataPortConfigMode_Type(Integer32):
    """Custom type ncmDataPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_NcmDataPortConfigMode_Type.__name__ = "Integer32"
_NcmDataPortConfigMode_Object = MibTableColumn
ncmDataPortConfigMode = _NcmDataPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 3),
    _NcmDataPortConfigMode_Type()
)
ncmDataPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortConfigMode.setStatus("mandatory")


class _NcmDataPortConfigLineIndicate_Type(Integer32):
    """Custom type ncmDataPortConfigLineIndicate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active-high", 2),
          ("active-low", 1))
    )


_NcmDataPortConfigLineIndicate_Type.__name__ = "Integer32"
_NcmDataPortConfigLineIndicate_Object = MibTableColumn
ncmDataPortConfigLineIndicate = _NcmDataPortConfigLineIndicate_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 4),
    _NcmDataPortConfigLineIndicate_Type()
)
ncmDataPortConfigLineIndicate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortConfigLineIndicate.setStatus("mandatory")


class _NcmDataPortLineStatusCDCC_Type(Integer32):
    """Custom type ncmDataPortLineStatusCDCC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_NcmDataPortLineStatusCDCC_Type.__name__ = "Integer32"
_NcmDataPortLineStatusCDCC_Object = MibTableColumn
ncmDataPortLineStatusCDCC = _NcmDataPortLineStatusCDCC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 5),
    _NcmDataPortLineStatusCDCC_Type()
)
ncmDataPortLineStatusCDCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortLineStatusCDCC.setStatus("mandatory")


class _NcmDataPortLineStatusCACB_Type(Integer32):
    """Custom type ncmDataPortLineStatusCACB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_NcmDataPortLineStatusCACB_Type.__name__ = "Integer32"
_NcmDataPortLineStatusCACB_Object = MibTableColumn
ncmDataPortLineStatusCACB = _NcmDataPortLineStatusCACB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 6),
    _NcmDataPortLineStatusCACB_Type()
)
ncmDataPortLineStatusCACB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortLineStatusCACB.setStatus("mandatory")


class _NcmDataPortLineStatusLLCJ_Type(Integer32):
    """Custom type ncmDataPortLineStatusLLCJ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_NcmDataPortLineStatusLLCJ_Type.__name__ = "Integer32"
_NcmDataPortLineStatusLLCJ_Object = MibTableColumn
ncmDataPortLineStatusLLCJ = _NcmDataPortLineStatusLLCJ_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 7),
    _NcmDataPortLineStatusLLCJ_Type()
)
ncmDataPortLineStatusLLCJ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortLineStatusLLCJ.setStatus("mandatory")


class _NcmDataPortLineStatusRLTM_Type(Integer32):
    """Custom type ncmDataPortLineStatusRLTM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_NcmDataPortLineStatusRLTM_Type.__name__ = "Integer32"
_NcmDataPortLineStatusRLTM_Object = MibTableColumn
ncmDataPortLineStatusRLTM = _NcmDataPortLineStatusRLTM_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 8),
    _NcmDataPortLineStatusRLTM_Type()
)
ncmDataPortLineStatusRLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortLineStatusRLTM.setStatus("mandatory")


class _NcmDataPortConfigLOS_Type(Integer32):
    """Custom type ncmDataPortConfigLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmDataPortConfigLOS_Type.__name__ = "Integer32"
_NcmDataPortConfigLOS_Object = MibTableColumn
ncmDataPortConfigLOS = _NcmDataPortConfigLOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 9),
    _NcmDataPortConfigLOS_Type()
)
ncmDataPortConfigLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortConfigLOS.setStatus("mandatory")


class _NcmDataPortConfigServiceState_Type(Integer32):
    """Custom type ncmDataPortConfigServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 2),
          ("not-in-service", 1))
    )


_NcmDataPortConfigServiceState_Type.__name__ = "Integer32"
_NcmDataPortConfigServiceState_Object = MibTableColumn
ncmDataPortConfigServiceState = _NcmDataPortConfigServiceState_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 10),
    _NcmDataPortConfigServiceState_Type()
)
ncmDataPortConfigServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortConfigServiceState.setStatus("mandatory")


class _NcmDataPortConfigClkOpt_Type(Integer32):
    """Custom type ncmDataPortConfigClkOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invertedst", 2),
          ("st", 1),
          ("tt", 3))
    )


_NcmDataPortConfigClkOpt_Type.__name__ = "Integer32"
_NcmDataPortConfigClkOpt_Object = MibTableColumn
ncmDataPortConfigClkOpt = _NcmDataPortConfigClkOpt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1028, 1, 11),
    _NcmDataPortConfigClkOpt_Type()
)
ncmDataPortConfigClkOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDataPortConfigClkOpt.setStatus("mandatory")
_NcmDataPortStatusTable_Object = MibTable
ncmDataPortStatusTable = _NcmDataPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029)
)
if mibBuilder.loadTexts:
    ncmDataPortStatusTable.setStatus("mandatory")
_NcmDataPortStatusEntry_Object = MibTableRow
ncmDataPortStatusEntry = _NcmDataPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1)
)
ncmDataPortStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmDataPortStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmDataPortStatusIndex"),
)
if mibBuilder.loadTexts:
    ncmDataPortStatusEntry.setStatus("mandatory")


class _NcmDataPortStatusNIDIndex_Type(Integer32):
    """Custom type ncmDataPortStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmDataPortStatusNIDIndex_Type.__name__ = "Integer32"
_NcmDataPortStatusNIDIndex_Object = MibTableColumn
ncmDataPortStatusNIDIndex = _NcmDataPortStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 1),
    _NcmDataPortStatusNIDIndex_Type()
)
ncmDataPortStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusNIDIndex.setStatus("mandatory")


class _NcmDataPortStatusIndex_Type(Integer32):
    """Custom type ncmDataPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmDataPortStatusIndex_Type.__name__ = "Integer32"
_NcmDataPortStatusIndex_Object = MibTableColumn
ncmDataPortStatusIndex = _NcmDataPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 2),
    _NcmDataPortStatusIndex_Type()
)
ncmDataPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusIndex.setStatus("mandatory")


class _NcmDataPortStatusMode_Type(Integer32):
    """Custom type ncmDataPortStatusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_NcmDataPortStatusMode_Type.__name__ = "Integer32"
_NcmDataPortStatusMode_Object = MibTableColumn
ncmDataPortStatusMode = _NcmDataPortStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 3),
    _NcmDataPortStatusMode_Type()
)
ncmDataPortStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusMode.setStatus("mandatory")


class _NcmDataPortStatusLineIndicate_Type(Integer32):
    """Custom type ncmDataPortStatusLineIndicate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active-high", 2),
          ("active-low", 1))
    )


_NcmDataPortStatusLineIndicate_Type.__name__ = "Integer32"
_NcmDataPortStatusLineIndicate_Object = MibTableColumn
ncmDataPortStatusLineIndicate = _NcmDataPortStatusLineIndicate_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 4),
    _NcmDataPortStatusLineIndicate_Type()
)
ncmDataPortStatusLineIndicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusLineIndicate.setStatus("mandatory")


class _NcmDataPortStatusLineCDCC_Type(Integer32):
    """Custom type ncmDataPortStatusLineCDCC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_NcmDataPortStatusLineCDCC_Type.__name__ = "Integer32"
_NcmDataPortStatusLineCDCC_Object = MibTableColumn
ncmDataPortStatusLineCDCC = _NcmDataPortStatusLineCDCC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 5),
    _NcmDataPortStatusLineCDCC_Type()
)
ncmDataPortStatusLineCDCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusLineCDCC.setStatus("mandatory")


class _NcmDataPortStatusLineCACB_Type(Integer32):
    """Custom type ncmDataPortStatusLineCACB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_NcmDataPortStatusLineCACB_Type.__name__ = "Integer32"
_NcmDataPortStatusLineCACB_Object = MibTableColumn
ncmDataPortStatusLineCACB = _NcmDataPortStatusLineCACB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 6),
    _NcmDataPortStatusLineCACB_Type()
)
ncmDataPortStatusLineCACB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusLineCACB.setStatus("mandatory")


class _NcmDataPortStatusLineLLCJ_Type(Integer32):
    """Custom type ncmDataPortStatusLineLLCJ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_NcmDataPortStatusLineLLCJ_Type.__name__ = "Integer32"
_NcmDataPortStatusLineLLCJ_Object = MibTableColumn
ncmDataPortStatusLineLLCJ = _NcmDataPortStatusLineLLCJ_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 7),
    _NcmDataPortStatusLineLLCJ_Type()
)
ncmDataPortStatusLineLLCJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusLineLLCJ.setStatus("mandatory")


class _NcmDataPortStatusLineRLTM_Type(Integer32):
    """Custom type ncmDataPortStatusLineRLTM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_NcmDataPortStatusLineRLTM_Type.__name__ = "Integer32"
_NcmDataPortStatusLineRLTM_Object = MibTableColumn
ncmDataPortStatusLineRLTM = _NcmDataPortStatusLineRLTM_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 8),
    _NcmDataPortStatusLineRLTM_Type()
)
ncmDataPortStatusLineRLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusLineRLTM.setStatus("mandatory")


class _NcmDataPortStatusLineLOS_Type(Integer32):
    """Custom type ncmDataPortStatusLineLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmDataPortStatusLineLOS_Type.__name__ = "Integer32"
_NcmDataPortStatusLineLOS_Object = MibTableColumn
ncmDataPortStatusLineLOS = _NcmDataPortStatusLineLOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 9),
    _NcmDataPortStatusLineLOS_Type()
)
ncmDataPortStatusLineLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusLineLOS.setStatus("mandatory")


class _NcmDataPortStatusServiceState_Type(Integer32):
    """Custom type ncmDataPortStatusServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 2),
          ("not-in-service", 1))
    )


_NcmDataPortStatusServiceState_Type.__name__ = "Integer32"
_NcmDataPortStatusServiceState_Object = MibTableColumn
ncmDataPortStatusServiceState = _NcmDataPortStatusServiceState_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 10),
    _NcmDataPortStatusServiceState_Type()
)
ncmDataPortStatusServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusServiceState.setStatus("mandatory")


class _NcmDataPortStatusCimType_Type(Integer32):
    """Custom type ncmDataPortStatusCimType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              20,
              21,
              32,
              33,
              34,
              56,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cim-2000-E1", 16),
          ("cim-2002-E1", 17),
          ("cim-2003-E1", 18),
          ("cim-2004-E1", 19),
          ("cim-2005-E1", 20),
          ("cim-2006-E1", 21),
          ("cim-2061-E1", 56),
          ("cim-2101-T1", 32),
          ("cim-2102-T1", 33),
          ("cim-2164-T1", 34),
          ("cim-UNINSTALLED", 255))
    )


_NcmDataPortStatusCimType_Type.__name__ = "Integer32"
_NcmDataPortStatusCimType_Object = MibTableColumn
ncmDataPortStatusCimType = _NcmDataPortStatusCimType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 11),
    _NcmDataPortStatusCimType_Type()
)
ncmDataPortStatusCimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusCimType.setStatus("mandatory")


class _NcmDataPortStatusLoopback_Type(Integer32):
    """Custom type ncmDataPortStatusLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmDataPortStatusLoopback_Type.__name__ = "Integer32"
_NcmDataPortStatusLoopback_Object = MibTableColumn
ncmDataPortStatusLoopback = _NcmDataPortStatusLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 12),
    _NcmDataPortStatusLoopback_Type()
)
ncmDataPortStatusLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortStatusLoopback.setStatus("mandatory")


class _NcmDataPortTestPattern_Type(Integer32):
    """Custom type ncmDataPortTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d3-in-D24", 2),
          ("none", 1),
          ("qrss", 3))
    )


_NcmDataPortTestPattern_Type.__name__ = "Integer32"
_NcmDataPortTestPattern_Object = MibTableColumn
ncmDataPortTestPattern = _NcmDataPortTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 13),
    _NcmDataPortTestPattern_Type()
)
ncmDataPortTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortTestPattern.setStatus("mandatory")
_NcmDataPortTstPatErrCount_Type = Gauge32
_NcmDataPortTstPatErrCount_Object = MibTableColumn
ncmDataPortTstPatErrCount = _NcmDataPortTstPatErrCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1029, 1, 14),
    _NcmDataPortTstPatErrCount_Type()
)
ncmDataPortTstPatErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDataPortTstPatErrCount.setStatus("mandatory")
_NcmALARMConfigTable_Object = MibTable
ncmALARMConfigTable = _NcmALARMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030)
)
if mibBuilder.loadTexts:
    ncmALARMConfigTable.setStatus("mandatory")
_NcmALARMConfigEntry_Object = MibTableRow
ncmALARMConfigEntry = _NcmALARMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1)
)
ncmALARMConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmAlarmConfigNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    ncmALARMConfigEntry.setStatus("mandatory")


class _NcmAlarmConfigNIDIndex_Type(Integer32):
    """Custom type ncmAlarmConfigNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmAlarmConfigNIDIndex_Type.__name__ = "Integer32"
_NcmAlarmConfigNIDIndex_Object = MibTableColumn
ncmAlarmConfigNIDIndex = _NcmAlarmConfigNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 1),
    _NcmAlarmConfigNIDIndex_Type()
)
ncmAlarmConfigNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmConfigNIDIndex.setStatus("mandatory")


class _NcmAlarmConfigIndex_Type(Integer32):
    """Custom type ncmAlarmConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmAlarmConfigIndex_Type.__name__ = "Integer32"
_NcmAlarmConfigIndex_Object = MibTableColumn
ncmAlarmConfigIndex = _NcmAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 2),
    _NcmAlarmConfigIndex_Type()
)
ncmAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmConfigIndex.setStatus("mandatory")
_NcmAlmCfgDomain_Type = Integer32
_NcmAlmCfgDomain_Object = MibTableColumn
ncmAlmCfgDomain = _NcmAlmCfgDomain_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 3),
    _NcmAlmCfgDomain_Type()
)
ncmAlmCfgDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgDomain.setStatus("mandatory")
_NcmAlmCfgSrcAddr_Type = DisplayString
_NcmAlmCfgSrcAddr_Object = MibTableColumn
ncmAlmCfgSrcAddr = _NcmAlmCfgSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 4),
    _NcmAlmCfgSrcAddr_Type()
)
ncmAlmCfgSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgSrcAddr.setStatus("mandatory")
_NcmAlmCfgCard_Type = Integer32
_NcmAlmCfgCard_Object = MibTableColumn
ncmAlmCfgCard = _NcmAlmCfgCard_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 5),
    _NcmAlmCfgCard_Type()
)
ncmAlmCfgCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgCard.setStatus("mandatory")
_NcmAlmCfgShelf_Type = Integer32
_NcmAlmCfgShelf_Object = MibTableColumn
ncmAlmCfgShelf = _NcmAlmCfgShelf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 6),
    _NcmAlmCfgShelf_Type()
)
ncmAlmCfgShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgShelf.setStatus("mandatory")


class _NcmAlmCfgE1T1Port1EnableAlmRpt_Type(Integer32):
    """Custom type ncmAlmCfgE1T1Port1EnableAlmRpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmAlmCfgE1T1Port1EnableAlmRpt_Type.__name__ = "Integer32"
_NcmAlmCfgE1T1Port1EnableAlmRpt_Object = MibTableColumn
ncmAlmCfgE1T1Port1EnableAlmRpt = _NcmAlmCfgE1T1Port1EnableAlmRpt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 7),
    _NcmAlmCfgE1T1Port1EnableAlmRpt_Type()
)
ncmAlmCfgE1T1Port1EnableAlmRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgE1T1Port1EnableAlmRpt.setStatus("mandatory")


class _NcmAlmCfgE1T1Port2EnableAlmRpt_Type(Integer32):
    """Custom type ncmAlmCfgE1T1Port2EnableAlmRpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmAlmCfgE1T1Port2EnableAlmRpt_Type.__name__ = "Integer32"
_NcmAlmCfgE1T1Port2EnableAlmRpt_Object = MibTableColumn
ncmAlmCfgE1T1Port2EnableAlmRpt = _NcmAlmCfgE1T1Port2EnableAlmRpt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 8),
    _NcmAlmCfgE1T1Port2EnableAlmRpt_Type()
)
ncmAlmCfgE1T1Port2EnableAlmRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgE1T1Port2EnableAlmRpt.setStatus("mandatory")


class _NcmAlmCfgE1T1Port3EnableAlmRpt_Type(Integer32):
    """Custom type ncmAlmCfgE1T1Port3EnableAlmRpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmAlmCfgE1T1Port3EnableAlmRpt_Type.__name__ = "Integer32"
_NcmAlmCfgE1T1Port3EnableAlmRpt_Object = MibTableColumn
ncmAlmCfgE1T1Port3EnableAlmRpt = _NcmAlmCfgE1T1Port3EnableAlmRpt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 9),
    _NcmAlmCfgE1T1Port3EnableAlmRpt_Type()
)
ncmAlmCfgE1T1Port3EnableAlmRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgE1T1Port3EnableAlmRpt.setStatus("mandatory")


class _NcmAlmCfgE1T1Port4EnableAlmRpt_Type(Integer32):
    """Custom type ncmAlmCfgE1T1Port4EnableAlmRpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmAlmCfgE1T1Port4EnableAlmRpt_Type.__name__ = "Integer32"
_NcmAlmCfgE1T1Port4EnableAlmRpt_Object = MibTableColumn
ncmAlmCfgE1T1Port4EnableAlmRpt = _NcmAlmCfgE1T1Port4EnableAlmRpt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 10),
    _NcmAlmCfgE1T1Port4EnableAlmRpt_Type()
)
ncmAlmCfgE1T1Port4EnableAlmRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgE1T1Port4EnableAlmRpt.setStatus("mandatory")


class _NcmAlmCfgDataPort1EnableAlmRpt_Type(Integer32):
    """Custom type ncmAlmCfgDataPort1EnableAlmRpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 3))
    )


_NcmAlmCfgDataPort1EnableAlmRpt_Type.__name__ = "Integer32"
_NcmAlmCfgDataPort1EnableAlmRpt_Object = MibTableColumn
ncmAlmCfgDataPort1EnableAlmRpt = _NcmAlmCfgDataPort1EnableAlmRpt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 11),
    _NcmAlmCfgDataPort1EnableAlmRpt_Type()
)
ncmAlmCfgDataPort1EnableAlmRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgDataPort1EnableAlmRpt.setStatus("mandatory")


class _NcmAlmCfgDataPort2EnableAlmRpt_Type(Integer32):
    """Custom type ncmAlmCfgDataPort2EnableAlmRpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 3))
    )


_NcmAlmCfgDataPort2EnableAlmRpt_Type.__name__ = "Integer32"
_NcmAlmCfgDataPort2EnableAlmRpt_Object = MibTableColumn
ncmAlmCfgDataPort2EnableAlmRpt = _NcmAlmCfgDataPort2EnableAlmRpt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 12),
    _NcmAlmCfgDataPort2EnableAlmRpt_Type()
)
ncmAlmCfgDataPort2EnableAlmRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgDataPort2EnableAlmRpt.setStatus("mandatory")


class _NcmAlmCfgEnableCardAlmRpt_Type(Integer32):
    """Custom type ncmAlmCfgEnableCardAlmRpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmAlmCfgEnableCardAlmRpt_Type.__name__ = "Integer32"
_NcmAlmCfgEnableCardAlmRpt_Object = MibTableColumn
ncmAlmCfgEnableCardAlmRpt = _NcmAlmCfgEnableCardAlmRpt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 13),
    _NcmAlmCfgEnableCardAlmRpt_Type()
)
ncmAlmCfgEnableCardAlmRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgEnableCardAlmRpt.setStatus("mandatory")
_NcmAlmCfgDeclareTime_Type = Integer32
_NcmAlmCfgDeclareTime_Object = MibTableColumn
ncmAlmCfgDeclareTime = _NcmAlmCfgDeclareTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1030, 1, 14),
    _NcmAlmCfgDeclareTime_Type()
)
ncmAlmCfgDeclareTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAlmCfgDeclareTime.setStatus("mandatory")
_NcmCURRENTAlarmMsgTable_Object = MibTable
ncmCURRENTAlarmMsgTable = _NcmCURRENTAlarmMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1031)
)
if mibBuilder.loadTexts:
    ncmCURRENTAlarmMsgTable.setStatus("mandatory")
_NcmCURRENTAlarmMsgEntry_Object = MibTableRow
ncmCURRENTAlarmMsgEntry = _NcmCURRENTAlarmMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1031, 1)
)
ncmCURRENTAlarmMsgEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmCurrAlarmMsgNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmCurrAlarmMsgIndex"),
)
if mibBuilder.loadTexts:
    ncmCURRENTAlarmMsgEntry.setStatus("mandatory")


class _NcmCurrAlarmMsgNIDIndex_Type(Integer32):
    """Custom type ncmCurrAlarmMsgNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmCurrAlarmMsgNIDIndex_Type.__name__ = "Integer32"
_NcmCurrAlarmMsgNIDIndex_Object = MibTableColumn
ncmCurrAlarmMsgNIDIndex = _NcmCurrAlarmMsgNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1031, 1, 1),
    _NcmCurrAlarmMsgNIDIndex_Type()
)
ncmCurrAlarmMsgNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCurrAlarmMsgNIDIndex.setStatus("mandatory")


class _NcmCurrAlarmMsgIndex_Type(Integer32):
    """Custom type ncmCurrAlarmMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmCurrAlarmMsgIndex_Type.__name__ = "Integer32"
_NcmCurrAlarmMsgIndex_Object = MibTableColumn
ncmCurrAlarmMsgIndex = _NcmCurrAlarmMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1031, 1, 2),
    _NcmCurrAlarmMsgIndex_Type()
)
ncmCurrAlarmMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCurrAlarmMsgIndex.setStatus("mandatory")


class _NcmCurrAlarmMsgNumber_Type(Integer32):
    """Custom type ncmCurrAlarmMsgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NcmCurrAlarmMsgNumber_Type.__name__ = "Integer32"
_NcmCurrAlarmMsgNumber_Object = MibTableColumn
ncmCurrAlarmMsgNumber = _NcmCurrAlarmMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1031, 1, 3),
    _NcmCurrAlarmMsgNumber_Type()
)
ncmCurrAlarmMsgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCurrAlarmMsgNumber.setStatus("mandatory")
_NcmCurrAlarmMsgEquipID_Type = Integer32
_NcmCurrAlarmMsgEquipID_Object = MibTableColumn
ncmCurrAlarmMsgEquipID = _NcmCurrAlarmMsgEquipID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1031, 1, 4),
    _NcmCurrAlarmMsgEquipID_Type()
)
ncmCurrAlarmMsgEquipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCurrAlarmMsgEquipID.setStatus("mandatory")
_NcmPrevAlarmMsgTable_Object = MibTable
ncmPrevAlarmMsgTable = _NcmPrevAlarmMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032)
)
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgTable.setStatus("mandatory")
_NcmPrevAlarmMsgEntry_Object = MibTableRow
ncmPrevAlarmMsgEntry = _NcmPrevAlarmMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1)
)
ncmPrevAlarmMsgEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmPrevAlarmMsgNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmPrevAlarmMsgIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmPrevAlarmMsgNumber"),
)
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgEntry.setStatus("mandatory")


class _NcmPrevAlarmMsgNIDIndex_Type(Integer32):
    """Custom type ncmPrevAlarmMsgNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPrevAlarmMsgNIDIndex_Type.__name__ = "Integer32"
_NcmPrevAlarmMsgNIDIndex_Object = MibTableColumn
ncmPrevAlarmMsgNIDIndex = _NcmPrevAlarmMsgNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 1),
    _NcmPrevAlarmMsgNIDIndex_Type()
)
ncmPrevAlarmMsgNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgNIDIndex.setStatus("mandatory")


class _NcmPrevAlarmMsgIndex_Type(Integer32):
    """Custom type ncmPrevAlarmMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPrevAlarmMsgIndex_Type.__name__ = "Integer32"
_NcmPrevAlarmMsgIndex_Object = MibTableColumn
ncmPrevAlarmMsgIndex = _NcmPrevAlarmMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 2),
    _NcmPrevAlarmMsgIndex_Type()
)
ncmPrevAlarmMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgIndex.setStatus("mandatory")


class _NcmPrevAlarmMsgNumber_Type(Integer32):
    """Custom type ncmPrevAlarmMsgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NcmPrevAlarmMsgNumber_Type.__name__ = "Integer32"
_NcmPrevAlarmMsgNumber_Object = MibTableColumn
ncmPrevAlarmMsgNumber = _NcmPrevAlarmMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 3),
    _NcmPrevAlarmMsgNumber_Type()
)
ncmPrevAlarmMsgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgNumber.setStatus("mandatory")
_NcmPrevAlarmMsgTimeStampSec_Type = Integer32
_NcmPrevAlarmMsgTimeStampSec_Object = MibTableColumn
ncmPrevAlarmMsgTimeStampSec = _NcmPrevAlarmMsgTimeStampSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 4),
    _NcmPrevAlarmMsgTimeStampSec_Type()
)
ncmPrevAlarmMsgTimeStampSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgTimeStampSec.setStatus("mandatory")
_NcmPrevAlarmMsgTimeStampms_Type = Integer32
_NcmPrevAlarmMsgTimeStampms_Object = MibTableColumn
ncmPrevAlarmMsgTimeStampms = _NcmPrevAlarmMsgTimeStampms_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 5),
    _NcmPrevAlarmMsgTimeStampms_Type()
)
ncmPrevAlarmMsgTimeStampms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgTimeStampms.setStatus("mandatory")
_NcmPrevAlarmMsgAlarmCode_Type = Integer32
_NcmPrevAlarmMsgAlarmCode_Object = MibTableColumn
ncmPrevAlarmMsgAlarmCode = _NcmPrevAlarmMsgAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 6),
    _NcmPrevAlarmMsgAlarmCode_Type()
)
ncmPrevAlarmMsgAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgAlarmCode.setStatus("mandatory")


class _NcmPrevAlarmMsgAlarmInstance_Type(Integer32):
    """Custom type ncmPrevAlarmMsgAlarmInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NcmPrevAlarmMsgAlarmInstance_Type.__name__ = "Integer32"
_NcmPrevAlarmMsgAlarmInstance_Object = MibTableColumn
ncmPrevAlarmMsgAlarmInstance = _NcmPrevAlarmMsgAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 7),
    _NcmPrevAlarmMsgAlarmInstance_Type()
)
ncmPrevAlarmMsgAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgAlarmInstance.setStatus("mandatory")


class _NcmPrevAlarmMsgObjType_Type(Integer32):
    """Custom type ncmPrevAlarmMsgObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 3),
          ("clkRef", 5),
          ("dS3-Port", 16),
          ("dataPort", 2),
          ("e1-PortID", 1),
          ("equipment", 10),
          ("hssi-Port", 17),
          ("notUsed", 8),
          ("power", 4),
          ("refBus", 7),
          ("software", 9),
          ("t1-PortID", 11),
          ("timeBus", 6))
    )


_NcmPrevAlarmMsgObjType_Type.__name__ = "Integer32"
_NcmPrevAlarmMsgObjType_Object = MibTableColumn
ncmPrevAlarmMsgObjType = _NcmPrevAlarmMsgObjType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 8),
    _NcmPrevAlarmMsgObjType_Type()
)
ncmPrevAlarmMsgObjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgObjType.setStatus("mandatory")


class _NcmPrevAlarmMsgSeverity_Type(Integer32):
    """Custom type ncmPrevAlarmMsgSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("informational", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_NcmPrevAlarmMsgSeverity_Type.__name__ = "Integer32"
_NcmPrevAlarmMsgSeverity_Object = MibTableColumn
ncmPrevAlarmMsgSeverity = _NcmPrevAlarmMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1032, 1, 9),
    _NcmPrevAlarmMsgSeverity_Type()
)
ncmPrevAlarmMsgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPrevAlarmMsgSeverity.setStatus("mandatory")
_NcmEnhanAlmCfgTable_Object = MibTable
ncmEnhanAlmCfgTable = _NcmEnhanAlmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033)
)
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgTable.setStatus("mandatory")
_NcmEnhanAlmCfgEntry_Object = MibTableRow
ncmEnhanAlmCfgEntry = _NcmEnhanAlmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1)
)
ncmEnhanAlmCfgEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmEnhanAlmCfgNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmEnhanAlmCfgIndex"),
)
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgEntry.setStatus("mandatory")


class _NcmEnhanAlmCfgNIDIndex_Type(Integer32):
    """Custom type ncmEnhanAlmCfgNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmEnhanAlmCfgNIDIndex_Type.__name__ = "Integer32"
_NcmEnhanAlmCfgNIDIndex_Object = MibTableColumn
ncmEnhanAlmCfgNIDIndex = _NcmEnhanAlmCfgNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 1),
    _NcmEnhanAlmCfgNIDIndex_Type()
)
ncmEnhanAlmCfgNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgNIDIndex.setStatus("mandatory")


class _NcmEnhanAlmCfgIndex_Type(Integer32):
    """Custom type ncmEnhanAlmCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmEnhanAlmCfgIndex_Type.__name__ = "Integer32"
_NcmEnhanAlmCfgIndex_Object = MibTableColumn
ncmEnhanAlmCfgIndex = _NcmEnhanAlmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 2),
    _NcmEnhanAlmCfgIndex_Type()
)
ncmEnhanAlmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgIndex.setStatus("mandatory")
_NcmEnhanAlmCfgCRCThreshold_Type = Integer32
_NcmEnhanAlmCfgCRCThreshold_Object = MibTableColumn
ncmEnhanAlmCfgCRCThreshold = _NcmEnhanAlmCfgCRCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 3),
    _NcmEnhanAlmCfgCRCThreshold_Type()
)
ncmEnhanAlmCfgCRCThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgCRCThreshold.setStatus("mandatory")
_NcmEnhanAlmCfgSESThreshold_Type = Integer32
_NcmEnhanAlmCfgSESThreshold_Object = MibTableColumn
ncmEnhanAlmCfgSESThreshold = _NcmEnhanAlmCfgSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 4),
    _NcmEnhanAlmCfgSESThreshold_Type()
)
ncmEnhanAlmCfgSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgSESThreshold.setStatus("mandatory")
_NcmEnhanAlmCfgUASThreshold_Type = Integer32
_NcmEnhanAlmCfgUASThreshold_Object = MibTableColumn
ncmEnhanAlmCfgUASThreshold = _NcmEnhanAlmCfgUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 5),
    _NcmEnhanAlmCfgUASThreshold_Type()
)
ncmEnhanAlmCfgUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgUASThreshold.setStatus("mandatory")


class _NcmEnhanAlmCfgBERThreshold_Type(Integer32):
    """Custom type ncmEnhanAlmCfgBERThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("d10E-4", 2),
          ("d10E-5", 3),
          ("d10E-6", 4),
          ("d10E-7", 5),
          ("d10E-8", 6),
          ("d10E-9", 7),
          ("disable", 1))
    )


_NcmEnhanAlmCfgBERThreshold_Type.__name__ = "Integer32"
_NcmEnhanAlmCfgBERThreshold_Object = MibTableColumn
ncmEnhanAlmCfgBERThreshold = _NcmEnhanAlmCfgBERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 6),
    _NcmEnhanAlmCfgBERThreshold_Type()
)
ncmEnhanAlmCfgBERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgBERThreshold.setStatus("mandatory")


class _NcmEnhanAlmCfgBPVThreshold_Type(Integer32):
    """Custom type ncmEnhanAlmCfgBPVThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmEnhanAlmCfgBPVThreshold_Type.__name__ = "Integer32"
_NcmEnhanAlmCfgBPVThreshold_Object = MibTableColumn
ncmEnhanAlmCfgBPVThreshold = _NcmEnhanAlmCfgBPVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 7),
    _NcmEnhanAlmCfgBPVThreshold_Type()
)
ncmEnhanAlmCfgBPVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgBPVThreshold.setStatus("mandatory")


class _NcmEnhanAlmCfgLineRestoral_Type(Integer32):
    """Custom type ncmEnhanAlmCfgLineRestoral based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("disable", 1),
          ("manual", 3),
          ("time-of-day", 4))
    )


_NcmEnhanAlmCfgLineRestoral_Type.__name__ = "Integer32"
_NcmEnhanAlmCfgLineRestoral_Object = MibTableColumn
ncmEnhanAlmCfgLineRestoral = _NcmEnhanAlmCfgLineRestoral_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 8),
    _NcmEnhanAlmCfgLineRestoral_Type()
)
ncmEnhanAlmCfgLineRestoral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgLineRestoral.setStatus("mandatory")
_NcmEnhanAlmCfgTODHour_Type = Integer32
_NcmEnhanAlmCfgTODHour_Object = MibTableColumn
ncmEnhanAlmCfgTODHour = _NcmEnhanAlmCfgTODHour_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 9),
    _NcmEnhanAlmCfgTODHour_Type()
)
ncmEnhanAlmCfgTODHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgTODHour.setStatus("mandatory")
_NcmEnhanAlmCfgTODMinute_Type = Integer32
_NcmEnhanAlmCfgTODMinute_Object = MibTableColumn
ncmEnhanAlmCfgTODMinute = _NcmEnhanAlmCfgTODMinute_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 10),
    _NcmEnhanAlmCfgTODMinute_Type()
)
ncmEnhanAlmCfgTODMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgTODMinute.setStatus("mandatory")


class _NcmEnhanAlmCfgLinRestEvalPer_Type(Integer32):
    """Custom type ncmEnhanAlmCfgLinRestEvalPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NcmEnhanAlmCfgLinRestEvalPer_Type.__name__ = "Integer32"
_NcmEnhanAlmCfgLinRestEvalPer_Object = MibTableColumn
ncmEnhanAlmCfgLinRestEvalPer = _NcmEnhanAlmCfgLinRestEvalPer_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1033, 1, 11),
    _NcmEnhanAlmCfgLinRestEvalPer_Type()
)
ncmEnhanAlmCfgLinRestEvalPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmEnhanAlmCfgLinRestEvalPer.setStatus("mandatory")
_NcmLoopbackTable_Object = MibTable
ncmLoopbackTable = _NcmLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1034)
)
if mibBuilder.loadTexts:
    ncmLoopbackTable.setStatus("mandatory")
_NcmLoopbackEntry_Object = MibTableRow
ncmLoopbackEntry = _NcmLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1034, 1)
)
ncmLoopbackEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmLpbkNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmLpbkLineIndex"),
)
if mibBuilder.loadTexts:
    ncmLoopbackEntry.setStatus("mandatory")


class _NcmLpbkNIDIndex_Type(Integer32):
    """Custom type ncmLpbkNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmLpbkNIDIndex_Type.__name__ = "Integer32"
_NcmLpbkNIDIndex_Object = MibTableColumn
ncmLpbkNIDIndex = _NcmLpbkNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1034, 1, 1),
    _NcmLpbkNIDIndex_Type()
)
ncmLpbkNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLpbkNIDIndex.setStatus("mandatory")


class _NcmLpbkLineIndex_Type(Integer32):
    """Custom type ncmLpbkLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmLpbkLineIndex_Type.__name__ = "Integer32"
_NcmLpbkLineIndex_Object = MibTableColumn
ncmLpbkLineIndex = _NcmLpbkLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1034, 1, 2),
    _NcmLpbkLineIndex_Type()
)
ncmLpbkLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLpbkLineIndex.setStatus("mandatory")


class _NcmSetAllOnes_Type(Integer32):
    """Custom type ncmSetAllOnes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmSetAllOnes_Type.__name__ = "Integer32"
_NcmSetAllOnes_Object = MibTableColumn
ncmSetAllOnes = _NcmSetAllOnes_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1034, 1, 3),
    _NcmSetAllOnes_Type()
)
ncmSetAllOnes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSetAllOnes.setStatus("mandatory")


class _NcmTimeoutLOCSec_Type(Integer32):
    """Custom type ncmTimeoutLOCSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NcmTimeoutLOCSec_Type.__name__ = "Integer32"
_NcmTimeoutLOCSec_Object = MibTableColumn
ncmTimeoutLOCSec = _NcmTimeoutLOCSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1034, 1, 4),
    _NcmTimeoutLOCSec_Type()
)
ncmTimeoutLOCSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmTimeoutLOCSec.setStatus("mandatory")


class _NcmRemoteLB_Type(Integer32):
    """Custom type ncmRemoteLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmRemoteLB_Type.__name__ = "Integer32"
_NcmRemoteLB_Object = MibTableColumn
ncmRemoteLB = _NcmRemoteLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1034, 1, 5),
    _NcmRemoteLB_Type()
)
ncmRemoteLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmRemoteLB.setStatus("mandatory")


class _NcmActivateDeactLBType_Type(Integer32):
    """Custom type ncmActivateDeactLBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              10000,
              10016,
              10032,
              10064,
              10128)
        )
    )
    namedValues = NamedValues(
        *(("aCT-FT1-LOOP-CODE", 128),
          ("aCT-SIX-TWO-FOUR-ONE-ONE-INBAND", 64),
          ("act-LLBBOP", 16),
          ("act-PLBBOP", 32),
          ("dPLoop", 8),
          ("deact-FT1-LOOP-CODE", 10128),
          ("deact-LLBBOP", 10016),
          ("deact-PLBBOP", 10032),
          ("deact-SIX-TWO-FOUR-ONE-ONE-INBAND", 10064),
          ("deactivate", 10000),
          ("lineLoop", 1),
          ("localLoopbk", 4),
          ("payloadLoop", 2))
    )


_NcmActivateDeactLBType_Type.__name__ = "Integer32"
_NcmActivateDeactLBType_Object = MibTableColumn
ncmActivateDeactLBType = _NcmActivateDeactLBType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1034, 1, 6),
    _NcmActivateDeactLBType_Type()
)
ncmActivateDeactLBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmActivateDeactLBType.setStatus("mandatory")
_NcmTestPatternTable_Object = MibTable
ncmTestPatternTable = _NcmTestPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1035)
)
if mibBuilder.loadTexts:
    ncmTestPatternTable.setStatus("mandatory")
_NcmTestPatternEntry_Object = MibTableRow
ncmTestPatternEntry = _NcmTestPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1035, 1)
)
ncmTestPatternEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmTstpattNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmTstpattLineIndex"),
)
if mibBuilder.loadTexts:
    ncmTestPatternEntry.setStatus("mandatory")


class _NcmTstpattNIDIndex_Type(Integer32):
    """Custom type ncmTstpattNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmTstpattNIDIndex_Type.__name__ = "Integer32"
_NcmTstpattNIDIndex_Object = MibTableColumn
ncmTstpattNIDIndex = _NcmTstpattNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1035, 1, 1),
    _NcmTstpattNIDIndex_Type()
)
ncmTstpattNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmTstpattNIDIndex.setStatus("mandatory")


class _NcmTstpattLineIndex_Type(Integer32):
    """Custom type ncmTstpattLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmTstpattLineIndex_Type.__name__ = "Integer32"
_NcmTstpattLineIndex_Object = MibTableColumn
ncmTstpattLineIndex = _NcmTstpattLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1035, 1, 2),
    _NcmTstpattLineIndex_Type()
)
ncmTstpattLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmTstpattLineIndex.setStatus("mandatory")


class _NcmTstpattTestPeriod_Type(Integer32):
    """Custom type ncmTstpattTestPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NcmTstpattTestPeriod_Type.__name__ = "Integer32"
_NcmTstpattTestPeriod_Object = MibTableColumn
ncmTstpattTestPeriod = _NcmTstpattTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1035, 1, 3),
    _NcmTstpattTestPeriod_Type()
)
ncmTstpattTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmTstpattTestPeriod.setStatus("mandatory")


class _NcmStartStopTestPattern_Type(Integer32):
    """Custom type ncmStartStopTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              100)
        )
    )
    namedValues = NamedValues(
        *(("all-Ones", 8),
          ("all-Zeroes", 6),
          ("fiftyfive-Octets", 7),
          ("one-In-Eight", 4),
          ("qrss", 2),
          ("stop", 100),
          ("three-In-Twentyfour", 1),
          ("two-N-Fifteen-One", 5),
          ("two-N-Twenty-One", 3))
    )


_NcmStartStopTestPattern_Type.__name__ = "Integer32"
_NcmStartStopTestPattern_Object = MibTableColumn
ncmStartStopTestPattern = _NcmStartStopTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1035, 1, 4),
    _NcmStartStopTestPattern_Type()
)
ncmStartStopTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmStartStopTestPattern.setStatus("mandatory")


class _NcmResetTestCounter_Type(Integer32):
    """Custom type ncmResetTestCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_NcmResetTestCounter_Type.__name__ = "Integer32"
_NcmResetTestCounter_Object = MibTableColumn
ncmResetTestCounter = _NcmResetTestCounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1035, 1, 5),
    _NcmResetTestCounter_Type()
)
ncmResetTestCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmResetTestCounter.setStatus("mandatory")
_NcmCircuitInfoTable_Object = MibTable
ncmCircuitInfoTable = _NcmCircuitInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036)
)
if mibBuilder.loadTexts:
    ncmCircuitInfoTable.setStatus("mandatory")
_NcmCircuitInfoEntry_Object = MibTableRow
ncmCircuitInfoEntry = _NcmCircuitInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1)
)
ncmCircuitInfoEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmCircuitInfoNIDIndex"),
)
if mibBuilder.loadTexts:
    ncmCircuitInfoEntry.setStatus("mandatory")


class _NcmCircuitInfoNIDIndex_Type(Integer32):
    """Custom type ncmCircuitInfoNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmCircuitInfoNIDIndex_Type.__name__ = "Integer32"
_NcmCircuitInfoNIDIndex_Object = MibTableColumn
ncmCircuitInfoNIDIndex = _NcmCircuitInfoNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 1),
    _NcmCircuitInfoNIDIndex_Type()
)
ncmCircuitInfoNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCircuitInfoNIDIndex.setStatus("mandatory")


class _NcmCircuitInfoCircName_Type(DisplayString):
    """Custom type ncmCircuitInfoCircName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NcmCircuitInfoCircName_Type.__name__ = "DisplayString"
_NcmCircuitInfoCircName_Object = MibTableColumn
ncmCircuitInfoCircName = _NcmCircuitInfoCircName_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 2),
    _NcmCircuitInfoCircName_Type()
)
ncmCircuitInfoCircName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoCircName.setStatus("mandatory")


class _NcmCircuitInfoCircPriority_Type(Integer32):
    """Custom type ncmCircuitInfoCircPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CPRIO-CRIT", 4),
          ("ccb-CPRIO-HIGH", 3),
          ("ccb-CPRIO-LOW", 1),
          ("ccb-CPRIO-NRML", 2))
    )


_NcmCircuitInfoCircPriority_Type.__name__ = "Integer32"
_NcmCircuitInfoCircPriority_Object = MibTableColumn
ncmCircuitInfoCircPriority = _NcmCircuitInfoCircPriority_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 3),
    _NcmCircuitInfoCircPriority_Type()
)
ncmCircuitInfoCircPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoCircPriority.setStatus("mandatory")


class _NcmCircuitInfoCircType_Type(Integer32):
    """Custom type ncmCircuitInfoCircType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CTYPE-BACKUP", 5),
          ("ccb-CTYPE-BACKUP-ND", 6),
          ("ccb-CTYPE-PERMANENT", 2),
          ("ccb-CTYPE-PRIMARY", 4),
          ("ccb-CTYPE-RESERVED", 1),
          ("ccb-CTYPE-SWITCHED", 3))
    )


_NcmCircuitInfoCircType_Type.__name__ = "Integer32"
_NcmCircuitInfoCircType_Object = MibTableColumn
ncmCircuitInfoCircType = _NcmCircuitInfoCircType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 4),
    _NcmCircuitInfoCircType_Type()
)
ncmCircuitInfoCircType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoCircType.setStatus("mandatory")


class _NcmCircuitInfoCircMode_Type(Integer32):
    """Custom type ncmCircuitInfoCircMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CMODE-NSIG-VOICE", 4),
          ("ccb-CMODE-NX56-DATA", 1),
          ("ccb-CMODE-NX64-DATA", 2),
          ("ccb-CMODE-RESERVED", 5),
          ("ccb-CMODE-SIG-VOICE", 3))
    )


_NcmCircuitInfoCircMode_Type.__name__ = "Integer32"
_NcmCircuitInfoCircMode_Object = MibTableColumn
ncmCircuitInfoCircMode = _NcmCircuitInfoCircMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 5),
    _NcmCircuitInfoCircMode_Type()
)
ncmCircuitInfoCircMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoCircMode.setStatus("mandatory")
_NcmCircuitInfoSrcPortSite_Type = Integer32
_NcmCircuitInfoSrcPortSite_Object = MibTableColumn
ncmCircuitInfoSrcPortSite = _NcmCircuitInfoSrcPortSite_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 6),
    _NcmCircuitInfoSrcPortSite_Type()
)
ncmCircuitInfoSrcPortSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoSrcPortSite.setStatus("mandatory")


class _NcmCircuitInfoSrcCardEquipID_Type(Integer32):
    """Custom type ncmCircuitInfoSrcCardEquipID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(77,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              96,
              112,
              113,
              116)
        )
    )
    namedValues = NamedValues(
        *(("ace-FW-DUAL-E1", 87),
          ("ace-FW-DUAL-T1", 86),
          ("ace-FW-E1", 80),
          ("ace-FW-ISDN-E1", 113),
          ("ace-FW-ISDN-T1", 112),
          ("ace-FW-QUAD-E1", 83),
          ("ace-FW-QUAD-T1", 82),
          ("ace-FW-T1", 81),
          ("ace-Reserved", 84),
          ("card-SIGMA-VCU", 77),
          ("fw-DS3-CDSU", 88),
          ("fw-DS3-CDSU-CHANNEL", 89),
          ("fw-DS3-DUDS3", 116),
          ("fw-NCM", 96),
          ("tabs-IMUX", 85))
    )


_NcmCircuitInfoSrcCardEquipID_Type.__name__ = "Integer32"
_NcmCircuitInfoSrcCardEquipID_Object = MibTableColumn
ncmCircuitInfoSrcCardEquipID = _NcmCircuitInfoSrcCardEquipID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 7),
    _NcmCircuitInfoSrcCardEquipID_Type()
)
ncmCircuitInfoSrcCardEquipID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoSrcCardEquipID.setStatus("mandatory")


class _NcmCircuitInfoSrcPortID_Type(Integer32):
    """Custom type ncmCircuitInfoSrcPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DATA-PORT-1", 5),
          ("ccb-DATA-PORT-2", 6),
          ("ccb-NET-PORT-1", 1),
          ("ccb-NET-PORT-2", 2),
          ("ccb-NET-PORT-3", 3),
          ("ccb-NET-PORT-4", 4),
          ("ccb-TAC-EQP-PORT", 8),
          ("ccb-TAC-NET-PORT", 7),
          ("ccb-UNKNOWN-PORT", 9))
    )


_NcmCircuitInfoSrcPortID_Type.__name__ = "Integer32"
_NcmCircuitInfoSrcPortID_Object = MibTableColumn
ncmCircuitInfoSrcPortID = _NcmCircuitInfoSrcPortID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 8),
    _NcmCircuitInfoSrcPortID_Type()
)
ncmCircuitInfoSrcPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoSrcPortID.setStatus("mandatory")
_NcmCircuitInfoSrcTimeslotmap_Type = Integer32
_NcmCircuitInfoSrcTimeslotmap_Object = MibTableColumn
ncmCircuitInfoSrcTimeslotmap = _NcmCircuitInfoSrcTimeslotmap_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 9),
    _NcmCircuitInfoSrcTimeslotmap_Type()
)
ncmCircuitInfoSrcTimeslotmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoSrcTimeslotmap.setStatus("mandatory")
_NcmCircuitInfoDstPortSite_Type = Integer32
_NcmCircuitInfoDstPortSite_Object = MibTableColumn
ncmCircuitInfoDstPortSite = _NcmCircuitInfoDstPortSite_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 10),
    _NcmCircuitInfoDstPortSite_Type()
)
ncmCircuitInfoDstPortSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoDstPortSite.setStatus("mandatory")


class _NcmCircuitInfoDstCardEquipID_Type(Integer32):
    """Custom type ncmCircuitInfoDstCardEquipID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(77,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              96,
              112,
              113,
              116)
        )
    )
    namedValues = NamedValues(
        *(("ace-FW-DUAL-E1", 87),
          ("ace-FW-DUAL-T1", 86),
          ("ace-FW-E1", 80),
          ("ace-FW-ISDN-E1", 113),
          ("ace-FW-ISDN-T1", 112),
          ("ace-FW-QUAD-E1", 83),
          ("ace-FW-QUAD-T1", 82),
          ("ace-FW-T1", 81),
          ("ace-Reserved", 84),
          ("card-SIGMA-VCU", 77),
          ("fw-DS3-CDSU", 88),
          ("fw-DS3-CDSU-CHANNEL", 89),
          ("fw-DS3-DUDS3", 116),
          ("fw-NCM", 96),
          ("tabs-IMUX", 85))
    )


_NcmCircuitInfoDstCardEquipID_Type.__name__ = "Integer32"
_NcmCircuitInfoDstCardEquipID_Object = MibTableColumn
ncmCircuitInfoDstCardEquipID = _NcmCircuitInfoDstCardEquipID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 11),
    _NcmCircuitInfoDstCardEquipID_Type()
)
ncmCircuitInfoDstCardEquipID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoDstCardEquipID.setStatus("mandatory")


class _NcmCircuitInfoDstPortID_Type(Integer32):
    """Custom type ncmCircuitInfoDstPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DATA-PORT-1", 5),
          ("ccb-DATA-PORT-2", 6),
          ("ccb-NET-PORT-1", 1),
          ("ccb-NET-PORT-2", 2),
          ("ccb-NET-PORT-3", 3),
          ("ccb-NET-PORT-4", 4),
          ("ccb-TAC-EQP-PORT", 8),
          ("ccb-TAC-NET-PORT", 7),
          ("ccb-UNKNOWN-PORT", 9))
    )


_NcmCircuitInfoDstPortID_Type.__name__ = "Integer32"
_NcmCircuitInfoDstPortID_Object = MibTableColumn
ncmCircuitInfoDstPortID = _NcmCircuitInfoDstPortID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 12),
    _NcmCircuitInfoDstPortID_Type()
)
ncmCircuitInfoDstPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoDstPortID.setStatus("mandatory")
_NcmCircuitInfoDstTimeslotmap_Type = Integer32
_NcmCircuitInfoDstTimeslotmap_Object = MibTableColumn
ncmCircuitInfoDstTimeslotmap = _NcmCircuitInfoDstTimeslotmap_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 13),
    _NcmCircuitInfoDstTimeslotmap_Type()
)
ncmCircuitInfoDstTimeslotmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoDstTimeslotmap.setStatus("mandatory")


class _NcmCircuitInfoBackPlaneBusID_Type(Integer32):
    """Custom type ncmCircuitInfoBackPlaneBusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ccb-BKPL-BUS-A1", 1),
          ("ccb-BKPL-BUS-A2", 2),
          ("ccb-BKPL-BUS-A3", 3),
          ("ccb-BKPL-BUS-A4", 4),
          ("ccb-BKPL-BUS-A5", 5),
          ("ccb-BKPL-BUS-A6", 6),
          ("ccb-BKPL-BUS-A7", 7),
          ("ccb-BKPL-BUS-A8", 8),
          ("ccb-BKPL-BUS-AUTO", 12),
          ("ccb-BKPL-BUS-B", 9),
          ("ccb-BKPL-BUS-C", 10),
          ("ccb-BKPL-BUS-NONE", 11))
    )


_NcmCircuitInfoBackPlaneBusID_Type.__name__ = "Integer32"
_NcmCircuitInfoBackPlaneBusID_Object = MibTableColumn
ncmCircuitInfoBackPlaneBusID = _NcmCircuitInfoBackPlaneBusID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 14),
    _NcmCircuitInfoBackPlaneBusID_Type()
)
ncmCircuitInfoBackPlaneBusID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoBackPlaneBusID.setStatus("mandatory")


class _NcmCircuitInfoAssoCircName_Type(DisplayString):
    """Custom type ncmCircuitInfoAssoCircName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NcmCircuitInfoAssoCircName_Type.__name__ = "DisplayString"
_NcmCircuitInfoAssoCircName_Object = MibTableColumn
ncmCircuitInfoAssoCircName = _NcmCircuitInfoAssoCircName_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 15),
    _NcmCircuitInfoAssoCircName_Type()
)
ncmCircuitInfoAssoCircName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoAssoCircName.setStatus("mandatory")


class _NcmCircuitInfoAction_Type(Integer32):
    """Custom type ncmCircuitInfoAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("activate", 4),
          ("add", 1),
          ("deactivate", 5),
          ("delete", 3),
          ("edit", 2),
          ("getdetailinfo", 6))
    )


_NcmCircuitInfoAction_Type.__name__ = "Integer32"
_NcmCircuitInfoAction_Object = MibTableColumn
ncmCircuitInfoAction = _NcmCircuitInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 16),
    _NcmCircuitInfoAction_Type()
)
ncmCircuitInfoAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCircuitInfoAction.setStatus("mandatory")


class _NcmAddEditActDeactCircuitStatus_Type(Integer32):
    """Custom type ncmAddEditActDeactCircuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              31,
              32,
              33,
              34,
              35,
              36,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("ccb-BUILD-CIRCDBASE-OVRFLOW", 13),
          ("ccb-BUILD-CKT-EXIST", 3),
          ("ccb-BUILD-CKT-INACTIVE", 16),
          ("ccb-BUILD-CKT-NOT-EXIST", 14),
          ("ccb-BUILD-DBKCHECK-NO-BKPCIRC", 42),
          ("ccb-BUILD-DBKCHECK-NO-PRICIRC", 41),
          ("ccb-BUILD-DBKCHECK-NO-PRIPORT", 44),
          ("ccb-BUILD-DBKCHECK-NO-SHRPORT", 43),
          ("ccb-BUILD-DCHECK-BUS-DRV-CNFL", 35),
          ("ccb-BUILD-DCHECK-BUS-TS-CNFL", 34),
          ("ccb-BUILD-DCHECK-DIFFCARD", 33),
          ("ccb-BUILD-DCHECK-MISSCARD", 32),
          ("ccb-BUILD-DCHECK-OK", 31),
          ("ccb-BUILD-DCHECK-PORT-CNFL", 36),
          ("ccb-BUILD-INVALID-DATA", 4),
          ("ccb-BUILD-NO-BUS-BW", 6),
          ("ccb-BUILD-NO-PEER-CARD", 7),
          ("ccb-BUILD-NO-PORT-BW", 2),
          ("ccb-BUILD-NOT-ACT-CIRC", 17),
          ("ccb-BUILD-PEER-CKT-EXIST", 9),
          ("ccb-BUILD-PEER-INVALID-DATA", 10),
          ("ccb-BUILD-PEER-NO-BUS-BW", 12),
          ("ccb-BUILD-PEER-NO-PORT-BW", 8),
          ("ccb-BUILD-PEER-PROM-FAILURE", 11),
          ("ccb-BUILD-PORT-SETUP-FAIL", 15),
          ("ccb-BUILD-PROM-FAILURE", 5),
          ("ccb-BUILD-SCHECK-BAD-BUS", 27),
          ("ccb-BUILD-SCHECK-BAD-CARD", 22),
          ("ccb-BUILD-SCHECK-BAD-CMODE", 24),
          ("ccb-BUILD-SCHECK-BAD-CTYPE", 23),
          ("ccb-BUILD-SCHECK-DIFF-TSNUM", 26),
          ("ccb-BUILD-SCHECK-DIFF-ncmSHELF", 25),
          ("ccb-BUILD-SCHECK-OK", 21),
          ("ccb-BUILD-SUCCESS", 1))
    )


_NcmAddEditActDeactCircuitStatus_Type.__name__ = "Integer32"
_NcmAddEditActDeactCircuitStatus_Object = MibTableColumn
ncmAddEditActDeactCircuitStatus = _NcmAddEditActDeactCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 17),
    _NcmAddEditActDeactCircuitStatus_Type()
)
ncmAddEditActDeactCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAddEditActDeactCircuitStatus.setStatus("mandatory")


class _NcmDeleteCircuitStatus_Type(Integer32):
    """Custom type ncmDeleteCircuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DELETE-CANT-FIND", 3),
          ("ccb-DELETE-CKT-NOT-EXIST", 7),
          ("ccb-DELETE-NO-PEER-CARD", 4),
          ("ccb-DELETE-PEER-CANT-FIND", 6),
          ("ccb-DELETE-PEER-PROM-FAILURE", 5),
          ("ccb-DELETE-PROM-FAILURE", 2),
          ("ccb-DELETE-SUCCESS", 1))
    )


_NcmDeleteCircuitStatus_Type.__name__ = "Integer32"
_NcmDeleteCircuitStatus_Object = MibTableColumn
ncmDeleteCircuitStatus = _NcmDeleteCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 18),
    _NcmDeleteCircuitStatus_Type()
)
ncmDeleteCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDeleteCircuitStatus.setStatus("mandatory")


class _NcmGetDetailCircuitStatus_Type(Integer32):
    """Custom type ncmGetDetailCircuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CSTAT-ACTIVE", 3),
          ("ccb-CSTAT-BACKUPPED", 8),
          ("ccb-CSTAT-BROKEN", 6),
          ("ccb-CSTAT-EDITING", 2),
          ("ccb-CSTAT-INACTIVE", 4),
          ("ccb-CSTAT-LINE-ERR", 7),
          ("ccb-CSTAT-PREEMPTED", 5),
          ("ccb-CSTAT-SPARE", 1))
    )


_NcmGetDetailCircuitStatus_Type.__name__ = "Integer32"
_NcmGetDetailCircuitStatus_Object = MibTableColumn
ncmGetDetailCircuitStatus = _NcmGetDetailCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1036, 1, 19),
    _NcmGetDetailCircuitStatus_Type()
)
ncmGetDetailCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmGetDetailCircuitStatus.setStatus("mandatory")
_NcmPortTimeslotAllocTable_Object = MibTable
ncmPortTimeslotAllocTable = _NcmPortTimeslotAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1037)
)
if mibBuilder.loadTexts:
    ncmPortTimeslotAllocTable.setStatus("mandatory")
_NcmPortTimeslotAllocEntry_Object = MibTableRow
ncmPortTimeslotAllocEntry = _NcmPortTimeslotAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1037, 1)
)
ncmPortTimeslotAllocEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmPortTimeslotAllocNIDIndex"),
)
if mibBuilder.loadTexts:
    ncmPortTimeslotAllocEntry.setStatus("mandatory")


class _NcmPortTimeslotAllocNIDIndex_Type(Integer32):
    """Custom type ncmPortTimeslotAllocNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPortTimeslotAllocNIDIndex_Type.__name__ = "Integer32"
_NcmPortTimeslotAllocNIDIndex_Object = MibTableColumn
ncmPortTimeslotAllocNIDIndex = _NcmPortTimeslotAllocNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1037, 1, 1),
    _NcmPortTimeslotAllocNIDIndex_Type()
)
ncmPortTimeslotAllocNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPortTimeslotAllocNIDIndex.setStatus("mandatory")
_NcmPortTimeslotCardSite_Type = Integer32
_NcmPortTimeslotCardSite_Object = MibTableColumn
ncmPortTimeslotCardSite = _NcmPortTimeslotCardSite_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1037, 1, 2),
    _NcmPortTimeslotCardSite_Type()
)
ncmPortTimeslotCardSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPortTimeslotCardSite.setStatus("mandatory")


class _NcmPortTimeslotCardEquipID_Type(Integer32):
    """Custom type ncmPortTimeslotCardEquipID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(77,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              96,
              112,
              113,
              116)
        )
    )
    namedValues = NamedValues(
        *(("ace-FW-DUAL-E1", 87),
          ("ace-FW-DUAL-T1", 86),
          ("ace-FW-E1", 80),
          ("ace-FW-ISDN-E1", 113),
          ("ace-FW-ISDN-T1", 112),
          ("ace-FW-QUAD-E1", 83),
          ("ace-FW-QUAD-T1", 82),
          ("ace-FW-T1", 81),
          ("ace-Reserved", 84),
          ("card-SIGMA-VCU", 77),
          ("fw-DS3-CDSU", 88),
          ("fw-DS3-CDSU-CHANNEL", 89),
          ("fw-DS3-DUDS3", 116),
          ("fw-NCM", 96),
          ("tabs-IMUX", 85))
    )


_NcmPortTimeslotCardEquipID_Type.__name__ = "Integer32"
_NcmPortTimeslotCardEquipID_Object = MibTableColumn
ncmPortTimeslotCardEquipID = _NcmPortTimeslotCardEquipID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1037, 1, 3),
    _NcmPortTimeslotCardEquipID_Type()
)
ncmPortTimeslotCardEquipID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPortTimeslotCardEquipID.setStatus("mandatory")


class _NcmPortTimeslotPortID_Type(Integer32):
    """Custom type ncmPortTimeslotPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DATA-PORT-1", 5),
          ("ccb-DATA-PORT-2", 6),
          ("ccb-NET-PORT-1", 1),
          ("ccb-NET-PORT-2", 2),
          ("ccb-NET-PORT-3", 3),
          ("ccb-NET-PORT-4", 4),
          ("ccb-TAC-EQP-PORT", 8),
          ("ccb-TAC-NET-PORT", 7),
          ("ccb-UNKNOWN-PORT", 9))
    )


_NcmPortTimeslotPortID_Type.__name__ = "Integer32"
_NcmPortTimeslotPortID_Object = MibTableColumn
ncmPortTimeslotPortID = _NcmPortTimeslotPortID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1037, 1, 4),
    _NcmPortTimeslotPortID_Type()
)
ncmPortTimeslotPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPortTimeslotPortID.setStatus("mandatory")
_NcmPortAllocTimeSlotMap_Type = Integer32
_NcmPortAllocTimeSlotMap_Object = MibTableColumn
ncmPortAllocTimeSlotMap = _NcmPortAllocTimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1037, 1, 5),
    _NcmPortAllocTimeSlotMap_Type()
)
ncmPortAllocTimeSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPortAllocTimeSlotMap.setStatus("mandatory")
_NcmDialBkUpInfoTable_Object = MibTable
ncmDialBkUpInfoTable = _NcmDialBkUpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038)
)
if mibBuilder.loadTexts:
    ncmDialBkUpInfoTable.setStatus("mandatory")
_NcmDialBkUpInfoEntry_Object = MibTableRow
ncmDialBkUpInfoEntry = _NcmDialBkUpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1)
)
ncmDialBkUpInfoEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmDialBkUpInfoNIDIndex"),
)
if mibBuilder.loadTexts:
    ncmDialBkUpInfoEntry.setStatus("mandatory")


class _NcmDialBkUpInfoNIDIndex_Type(Integer32):
    """Custom type ncmDialBkUpInfoNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmDialBkUpInfoNIDIndex_Type.__name__ = "Integer32"
_NcmDialBkUpInfoNIDIndex_Object = MibTableColumn
ncmDialBkUpInfoNIDIndex = _NcmDialBkUpInfoNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 1),
    _NcmDialBkUpInfoNIDIndex_Type()
)
ncmDialBkUpInfoNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDialBkUpInfoNIDIndex.setStatus("mandatory")


class _NcmDialBkUpReqCircName_Type(DisplayString):
    """Custom type ncmDialBkUpReqCircName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NcmDialBkUpReqCircName_Type.__name__ = "DisplayString"
_NcmDialBkUpReqCircName_Object = MibTableColumn
ncmDialBkUpReqCircName = _NcmDialBkUpReqCircName_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 2),
    _NcmDialBkUpReqCircName_Type()
)
ncmDialBkUpReqCircName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDialBkUpReqCircName.setStatus("mandatory")


class _NcmPrimaryCircName_Type(DisplayString):
    """Custom type ncmPrimaryCircName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NcmPrimaryCircName_Type.__name__ = "DisplayString"
_NcmPrimaryCircName_Object = MibTableColumn
ncmPrimaryCircName = _NcmPrimaryCircName_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 3),
    _NcmPrimaryCircName_Type()
)
ncmPrimaryCircName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPrimaryCircName.setStatus("mandatory")


class _NcmBackupCircName_Type(DisplayString):
    """Custom type ncmBackupCircName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NcmBackupCircName_Type.__name__ = "DisplayString"
_NcmBackupCircName_Object = MibTableColumn
ncmBackupCircName = _NcmBackupCircName_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 4),
    _NcmBackupCircName_Type()
)
ncmBackupCircName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmBackupCircName.setStatus("mandatory")
_NcmCallReferenceNumber_Type = Integer32
_NcmCallReferenceNumber_Object = MibTableColumn
ncmCallReferenceNumber = _NcmCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 5),
    _NcmCallReferenceNumber_Type()
)
ncmCallReferenceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCallReferenceNumber.setStatus("mandatory")


class _NcmCirSrcPortErrsetupMask_Type(Integer32):
    """Custom type ncmCirSrcPortErrsetupMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DBKP-ALM-AIS-CTS", 1),
          ("ccb-DBKP-ALM-LOF", 8),
          ("ccb-DBKP-ALM-LOS-DCD", 4),
          ("ccb-DBKP-ALM-SES", 32),
          ("ccb-DBKP-ALM-UAS", 16),
          ("ccb-DBKP-ALM-YEL-DSR", 2))
    )


_NcmCirSrcPortErrsetupMask_Type.__name__ = "Integer32"
_NcmCirSrcPortErrsetupMask_Object = MibTableColumn
ncmCirSrcPortErrsetupMask = _NcmCirSrcPortErrsetupMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 6),
    _NcmCirSrcPortErrsetupMask_Type()
)
ncmCirSrcPortErrsetupMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCirSrcPortErrsetupMask.setStatus("mandatory")


class _NcmCirDstPortErrsetupMask_Type(Integer32):
    """Custom type ncmCirDstPortErrsetupMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DBKP-ALM-AIS-CTS", 1),
          ("ccb-DBKP-ALM-LOF", 8),
          ("ccb-DBKP-ALM-LOS-DCD", 4),
          ("ccb-DBKP-ALM-SES", 32),
          ("ccb-DBKP-ALM-UAS", 16),
          ("ccb-DBKP-ALM-YEL-DSR", 2))
    )


_NcmCirDstPortErrsetupMask_Type.__name__ = "Integer32"
_NcmCirDstPortErrsetupMask_Object = MibTableColumn
ncmCirDstPortErrsetupMask = _NcmCirDstPortErrsetupMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 7),
    _NcmCirDstPortErrsetupMask_Type()
)
ncmCirDstPortErrsetupMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCirDstPortErrsetupMask.setStatus("mandatory")


class _NcmCirErrClearanceMask_Type(Integer32):
    """Custom type ncmCirErrClearanceMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DBKP-ALM-AIS-CTS", 1),
          ("ccb-DBKP-ALM-LOF", 8),
          ("ccb-DBKP-ALM-LOS-DCD", 4),
          ("ccb-DBKP-ALM-SES", 32),
          ("ccb-DBKP-ALM-UAS", 16),
          ("ccb-DBKP-ALM-YEL-DSR", 2))
    )


_NcmCirErrClearanceMask_Type.__name__ = "Integer32"
_NcmCirErrClearanceMask_Object = MibTableColumn
ncmCirErrClearanceMask = _NcmCirErrClearanceMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 8),
    _NcmCirErrClearanceMask_Type()
)
ncmCirErrClearanceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCirErrClearanceMask.setStatus("mandatory")
_NcmDialBkUpTimeout_Type = Integer32
_NcmDialBkUpTimeout_Object = MibTableColumn
ncmDialBkUpTimeout = _NcmDialBkUpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 9),
    _NcmDialBkUpTimeout_Type()
)
ncmDialBkUpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDialBkUpTimeout.setStatus("mandatory")


class _NcmDialBkUpAction_Type(Integer32):
    """Custom type ncmDialBkUpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("set", 1)
    )


_NcmDialBkUpAction_Type.__name__ = "Integer32"
_NcmDialBkUpAction_Object = MibTableColumn
ncmDialBkUpAction = _NcmDialBkUpAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 10),
    _NcmDialBkUpAction_Type()
)
ncmDialBkUpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmDialBkUpAction.setStatus("mandatory")


class _NcmDialBkUpSetupStatus_Type(Integer32):
    """Custom type ncmDialBkUpSetupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              31,
              32,
              33,
              34,
              35,
              36,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("ccb-BUILD-CIRCDBASE-OVRFLOW", 13),
          ("ccb-BUILD-CKT-EXIST", 3),
          ("ccb-BUILD-CKT-INACTIVE", 16),
          ("ccb-BUILD-CKT-NOT-EXIST", 14),
          ("ccb-BUILD-DBKCHECK-NO-BKPCIRC", 42),
          ("ccb-BUILD-DBKCHECK-NO-PRICIRC", 41),
          ("ccb-BUILD-DBKCHECK-NO-PRIPORT", 44),
          ("ccb-BUILD-DBKCHECK-NO-SHRPORT", 43),
          ("ccb-BUILD-DCHECK-BUS-DRV-CNFL", 35),
          ("ccb-BUILD-DCHECK-BUS-TS-CNFL", 34),
          ("ccb-BUILD-DCHECK-DIFFCARD", 33),
          ("ccb-BUILD-DCHECK-MISSCARD", 32),
          ("ccb-BUILD-DCHECK-OK", 31),
          ("ccb-BUILD-DCHECK-PORT-CNFL", 36),
          ("ccb-BUILD-INVALID-DATA", 4),
          ("ccb-BUILD-NO-BUS-BW", 6),
          ("ccb-BUILD-NO-PEER-CARD", 7),
          ("ccb-BUILD-NO-PORT-BW", 2),
          ("ccb-BUILD-NOT-ACT-CIRC", 17),
          ("ccb-BUILD-PEER-CKT-EXIST", 9),
          ("ccb-BUILD-PEER-INVALID-DATA", 10),
          ("ccb-BUILD-PEER-NO-BUS-BW", 12),
          ("ccb-BUILD-PEER-NO-PORT-BW", 8),
          ("ccb-BUILD-PEER-PROM-FAILURE", 11),
          ("ccb-BUILD-PORT-SETUP-FAIL", 15),
          ("ccb-BUILD-PROM-FAILURE", 5),
          ("ccb-BUILD-SCHECK-BAD-BUS", 27),
          ("ccb-BUILD-SCHECK-BAD-CARD", 22),
          ("ccb-BUILD-SCHECK-BAD-CMODE", 24),
          ("ccb-BUILD-SCHECK-BAD-CTYPE", 23),
          ("ccb-BUILD-SCHECK-DIFF-TSNUM", 26),
          ("ccb-BUILD-SCHECK-DIFF-ncmSHELF", 25),
          ("ccb-BUILD-SCHECK-OK", 21),
          ("ccb-BUILD-SUCCESS", 1))
    )


_NcmDialBkUpSetupStatus_Type.__name__ = "Integer32"
_NcmDialBkUpSetupStatus_Object = MibTableColumn
ncmDialBkUpSetupStatus = _NcmDialBkUpSetupStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1038, 1, 11),
    _NcmDialBkUpSetupStatus_Type()
)
ncmDialBkUpSetupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDialBkUpSetupStatus.setStatus("mandatory")
_NcmClearCircuitGrpTable_Object = MibTable
ncmClearCircuitGrpTable = _NcmClearCircuitGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1039)
)
if mibBuilder.loadTexts:
    ncmClearCircuitGrpTable.setStatus("mandatory")
_NcmClearCircuitGrpEntry_Object = MibTableRow
ncmClearCircuitGrpEntry = _NcmClearCircuitGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1039, 1)
)
ncmClearCircuitGrpEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmClearCircuitGrpNIDIndex"),
)
if mibBuilder.loadTexts:
    ncmClearCircuitGrpEntry.setStatus("mandatory")


class _NcmClearCircuitGrpNIDIndex_Type(Integer32):
    """Custom type ncmClearCircuitGrpNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmClearCircuitGrpNIDIndex_Type.__name__ = "Integer32"
_NcmClearCircuitGrpNIDIndex_Object = MibTableColumn
ncmClearCircuitGrpNIDIndex = _NcmClearCircuitGrpNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1039, 1, 1),
    _NcmClearCircuitGrpNIDIndex_Type()
)
ncmClearCircuitGrpNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmClearCircuitGrpNIDIndex.setStatus("mandatory")


class _NcmClearCircuitGrpName_Type(Integer32):
    """Custom type ncmClearCircuitGrpName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CDEL-ALL", 1),
          ("ccb-CDEL-BUS-CKT", 5),
          ("ccb-CDEL-CARD-CKT", 3),
          ("ccb-CDEL-INACTIVE", 2),
          ("ccb-CDEL-PORT-CKT", 4))
    )


_NcmClearCircuitGrpName_Type.__name__ = "Integer32"
_NcmClearCircuitGrpName_Object = MibTableColumn
ncmClearCircuitGrpName = _NcmClearCircuitGrpName_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1039, 1, 2),
    _NcmClearCircuitGrpName_Type()
)
ncmClearCircuitGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmClearCircuitGrpName.setStatus("mandatory")
_NcmClearCircuitGrpSite_Type = Integer32
_NcmClearCircuitGrpSite_Object = MibTableColumn
ncmClearCircuitGrpSite = _NcmClearCircuitGrpSite_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1039, 1, 3),
    _NcmClearCircuitGrpSite_Type()
)
ncmClearCircuitGrpSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmClearCircuitGrpSite.setStatus("mandatory")


class _NcmClearCircuitCardEquipID_Type(Integer32):
    """Custom type ncmClearCircuitCardEquipID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(77,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              96,
              112,
              113,
              116)
        )
    )
    namedValues = NamedValues(
        *(("ace-FW-DUAL-E1", 87),
          ("ace-FW-DUAL-T1", 86),
          ("ace-FW-E1", 80),
          ("ace-FW-ISDN-E1", 113),
          ("ace-FW-ISDN-T1", 112),
          ("ace-FW-QUAD-E1", 83),
          ("ace-FW-QUAD-T1", 82),
          ("ace-FW-T1", 81),
          ("ace-Reserved", 84),
          ("card-SIGMA-VCU", 77),
          ("fw-DS3-CDSU", 88),
          ("fw-DS3-CDSU-CHANNEL", 89),
          ("fw-DS3-DUDS3", 116),
          ("fw-NCM", 96),
          ("tabs-IMUX", 85))
    )


_NcmClearCircuitCardEquipID_Type.__name__ = "Integer32"
_NcmClearCircuitCardEquipID_Object = MibTableColumn
ncmClearCircuitCardEquipID = _NcmClearCircuitCardEquipID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1039, 1, 4),
    _NcmClearCircuitCardEquipID_Type()
)
ncmClearCircuitCardEquipID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmClearCircuitCardEquipID.setStatus("mandatory")


class _NcmClearCircuitPortID_Type(Integer32):
    """Custom type ncmClearCircuitPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DATA-PORT-1", 5),
          ("ccb-DATA-PORT-2", 6),
          ("ccb-NET-PORT-1", 1),
          ("ccb-NET-PORT-2", 2),
          ("ccb-NET-PORT-3", 3),
          ("ccb-NET-PORT-4", 4),
          ("ccb-TAC-EQP-PORT", 8),
          ("ccb-TAC-NET-PORT", 7),
          ("ccb-UNKNOWN-PORT", 9))
    )


_NcmClearCircuitPortID_Type.__name__ = "Integer32"
_NcmClearCircuitPortID_Object = MibTableColumn
ncmClearCircuitPortID = _NcmClearCircuitPortID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1039, 1, 5),
    _NcmClearCircuitPortID_Type()
)
ncmClearCircuitPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmClearCircuitPortID.setStatus("mandatory")


class _NcmClearCircuitAction_Type(Integer32):
    """Custom type ncmClearCircuitAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_NcmClearCircuitAction_Type.__name__ = "Integer32"
_NcmClearCircuitAction_Object = MibTableColumn
ncmClearCircuitAction = _NcmClearCircuitAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1039, 1, 6),
    _NcmClearCircuitAction_Type()
)
ncmClearCircuitAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmClearCircuitAction.setStatus("mandatory")
_NcmListGetMsgNumTable_Object = MibTable
ncmListGetMsgNumTable = _NcmListGetMsgNumTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040)
)
if mibBuilder.loadTexts:
    ncmListGetMsgNumTable.setStatus("mandatory")
_NcmListGetMsgNumEntry_Object = MibTableRow
ncmListGetMsgNumEntry = _NcmListGetMsgNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1)
)
ncmListGetMsgNumEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmListMsgNumNIDIndex"),
)
if mibBuilder.loadTexts:
    ncmListGetMsgNumEntry.setStatus("mandatory")


class _NcmListMsgNumNIDIndex_Type(Integer32):
    """Custom type ncmListMsgNumNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmListMsgNumNIDIndex_Type.__name__ = "Integer32"
_NcmListMsgNumNIDIndex_Object = MibTableColumn
ncmListMsgNumNIDIndex = _NcmListMsgNumNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1, 1),
    _NcmListMsgNumNIDIndex_Type()
)
ncmListMsgNumNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListMsgNumNIDIndex.setStatus("mandatory")


class _NcmListMsgNumCircuitGroup_Type(Integer32):
    """Custom type ncmListMsgNumCircuitGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CLIST-ACTIVE", 2),
          ("ccb-CLIST-ALL", 1),
          ("ccb-CLIST-CARD-CKT", 4),
          ("ccb-CLIST-PORT-CKT", 3))
    )


_NcmListMsgNumCircuitGroup_Type.__name__ = "Integer32"
_NcmListMsgNumCircuitGroup_Object = MibTableColumn
ncmListMsgNumCircuitGroup = _NcmListMsgNumCircuitGroup_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1, 2),
    _NcmListMsgNumCircuitGroup_Type()
)
ncmListMsgNumCircuitGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmListMsgNumCircuitGroup.setStatus("mandatory")
_NcmListMsgNumPageNumber_Type = Integer32
_NcmListMsgNumPageNumber_Object = MibTableColumn
ncmListMsgNumPageNumber = _NcmListMsgNumPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1, 3),
    _NcmListMsgNumPageNumber_Type()
)
ncmListMsgNumPageNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmListMsgNumPageNumber.setStatus("mandatory")
_NcmListMsgNumCardSite_Type = Integer32
_NcmListMsgNumCardSite_Object = MibTableColumn
ncmListMsgNumCardSite = _NcmListMsgNumCardSite_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1, 4),
    _NcmListMsgNumCardSite_Type()
)
ncmListMsgNumCardSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmListMsgNumCardSite.setStatus("mandatory")


class _NcmListMsgNumCardEquipID_Type(Integer32):
    """Custom type ncmListMsgNumCardEquipID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(77,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              96,
              112,
              113,
              116)
        )
    )
    namedValues = NamedValues(
        *(("ace-FW-DUAL-E1", 87),
          ("ace-FW-DUAL-T1", 86),
          ("ace-FW-E1", 80),
          ("ace-FW-ISDN-E1", 113),
          ("ace-FW-ISDN-T1", 112),
          ("ace-FW-QUAD-E1", 83),
          ("ace-FW-QUAD-T1", 82),
          ("ace-FW-T1", 81),
          ("ace-Reserved", 84),
          ("card-SIGMA-VCU", 77),
          ("fw-DS3-CDSU", 88),
          ("fw-DS3-CDSU-CHANNEL", 89),
          ("fw-DS3-DUDS3", 116),
          ("fw-NCM", 96),
          ("tabs-IMUX", 85))
    )


_NcmListMsgNumCardEquipID_Type.__name__ = "Integer32"
_NcmListMsgNumCardEquipID_Object = MibTableColumn
ncmListMsgNumCardEquipID = _NcmListMsgNumCardEquipID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1, 5),
    _NcmListMsgNumCardEquipID_Type()
)
ncmListMsgNumCardEquipID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmListMsgNumCardEquipID.setStatus("mandatory")


class _NcmListMsgNumPortID_Type(Integer32):
    """Custom type ncmListMsgNumPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ccb-DATA-PORT-1", 5),
          ("ccb-DATA-PORT-2", 6),
          ("ccb-NET-PORT-1", 1),
          ("ccb-NET-PORT-2", 2),
          ("ccb-NET-PORT-3", 3),
          ("ccb-NET-PORT-4", 4),
          ("ccb-TAC-EQP-PORT", 8),
          ("ccb-TAC-NET-PORT", 7),
          ("ccb-UNKNOWN-PORT", 9))
    )


_NcmListMsgNumPortID_Type.__name__ = "Integer32"
_NcmListMsgNumPortID_Object = MibTableColumn
ncmListMsgNumPortID = _NcmListMsgNumPortID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1, 6),
    _NcmListMsgNumPortID_Type()
)
ncmListMsgNumPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmListMsgNumPortID.setStatus("mandatory")
_NcmNumofGetListMessage_Type = Integer32
_NcmNumofGetListMessage_Object = MibTableColumn
ncmNumofGetListMessage = _NcmNumofGetListMessage_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1, 7),
    _NcmNumofGetListMessage_Type()
)
ncmNumofGetListMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNumofGetListMessage.setStatus("mandatory")
_NcmTotalCircDatabase_Type = Integer32
_NcmTotalCircDatabase_Object = MibTableColumn
ncmTotalCircDatabase = _NcmTotalCircDatabase_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1040, 1, 8),
    _NcmTotalCircDatabase_Type()
)
ncmTotalCircDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmTotalCircDatabase.setStatus("mandatory")
_NcmCircListccbTable_Object = MibTable
ncmCircListccbTable = _NcmCircListccbTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041)
)
if mibBuilder.loadTexts:
    ncmCircListccbTable.setStatus("mandatory")
_NcmCircListccbEntry_Object = MibTableRow
ncmCircListccbEntry = _NcmCircListccbEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1)
)
ncmCircListccbEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmListccbNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmNumofCircListMessage"),
)
if mibBuilder.loadTexts:
    ncmCircListccbEntry.setStatus("mandatory")


class _NcmListccbNIDIndex_Type(Integer32):
    """Custom type ncmListccbNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmListccbNIDIndex_Type.__name__ = "Integer32"
_NcmListccbNIDIndex_Object = MibTableColumn
ncmListccbNIDIndex = _NcmListccbNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 1),
    _NcmListccbNIDIndex_Type()
)
ncmListccbNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListccbNIDIndex.setStatus("mandatory")
_NcmNumofCircListMessage_Type = Integer32
_NcmNumofCircListMessage_Object = MibTableColumn
ncmNumofCircListMessage = _NcmNumofCircListMessage_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 2),
    _NcmNumofCircListMessage_Type()
)
ncmNumofCircListMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmNumofCircListMessage.setStatus("mandatory")


class _NcmListccbCircName_Type(DisplayString):
    """Custom type ncmListccbCircName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NcmListccbCircName_Type.__name__ = "DisplayString"
_NcmListccbCircName_Object = MibTableColumn
ncmListccbCircName = _NcmListccbCircName_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 3),
    _NcmListccbCircName_Type()
)
ncmListccbCircName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListccbCircName.setStatus("mandatory")


class _NcmListccbCircPriority_Type(Integer32):
    """Custom type ncmListccbCircPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CPRIO-CRIT", 4),
          ("ccb-CPRIO-HIGH", 3),
          ("ccb-CPRIO-LOW", 1),
          ("ccb-CPRIO-NRML", 2))
    )


_NcmListccbCircPriority_Type.__name__ = "Integer32"
_NcmListccbCircPriority_Object = MibTableColumn
ncmListccbCircPriority = _NcmListccbCircPriority_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 4),
    _NcmListccbCircPriority_Type()
)
ncmListccbCircPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListccbCircPriority.setStatus("mandatory")


class _NcmListccbCircType_Type(Integer32):
    """Custom type ncmListccbCircType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CTYPE-BACKUP", 5),
          ("ccb-CTYPE-PERMANENT", 2),
          ("ccb-CTYPE-PRIMARY", 4),
          ("ccb-CTYPE-RESERVED", 1),
          ("ccb-CTYPE-SWITCHED", 3))
    )


_NcmListccbCircType_Type.__name__ = "Integer32"
_NcmListccbCircType_Object = MibTableColumn
ncmListccbCircType = _NcmListccbCircType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 5),
    _NcmListccbCircType_Type()
)
ncmListccbCircType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListccbCircType.setStatus("mandatory")


class _NcmListccbCircMode_Type(Integer32):
    """Custom type ncmListccbCircMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CMODE-NSIG-VOICE", 4),
          ("ccb-CMODE-NX56-DATA", 1),
          ("ccb-CMODE-NX64-DATA", 2),
          ("ccb-CMODE-RESERVED", 5),
          ("ccb-CMODE-SIG-VOICE", 3))
    )


_NcmListccbCircMode_Type.__name__ = "Integer32"
_NcmListccbCircMode_Object = MibTableColumn
ncmListccbCircMode = _NcmListccbCircMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 6),
    _NcmListccbCircMode_Type()
)
ncmListccbCircMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListccbCircMode.setStatus("mandatory")
_NcmSrcPortSite_Type = Integer32
_NcmSrcPortSite_Object = MibTableColumn
ncmSrcPortSite = _NcmSrcPortSite_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 7),
    _NcmSrcPortSite_Type()
)
ncmSrcPortSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSrcPortSite.setStatus("mandatory")


class _NcmSrcCardEquipID_Type(Integer32):
    """Custom type ncmSrcCardEquipID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(77,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              96,
              112,
              113,
              116)
        )
    )
    namedValues = NamedValues(
        *(("ace-FW-DUAL-E1", 87),
          ("ace-FW-DUAL-T1", 86),
          ("ace-FW-E1", 80),
          ("ace-FW-ISDN-E1", 113),
          ("ace-FW-ISDN-T1", 112),
          ("ace-FW-QUAD-E1", 83),
          ("ace-FW-QUAD-T1", 82),
          ("ace-FW-T1", 81),
          ("ace-Reserved", 84),
          ("card-SIGMA-VCU", 77),
          ("fw-DS3-CDSU", 88),
          ("fw-DS3-CDSU-CHANNEL", 89),
          ("fw-DS3-DUDS3", 116),
          ("fw-NCM", 96),
          ("tabs-IMUX", 85))
    )


_NcmSrcCardEquipID_Type.__name__ = "Integer32"
_NcmSrcCardEquipID_Object = MibTableColumn
ncmSrcCardEquipID = _NcmSrcCardEquipID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 8),
    _NcmSrcCardEquipID_Type()
)
ncmSrcCardEquipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSrcCardEquipID.setStatus("mandatory")


class _NcmSrcPortIdentifier_Type(Integer32):
    """Custom type ncmSrcPortIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cb-UNKNOWN-PORT", 9),
          ("ccb-DATA-PORT-1", 5),
          ("ccb-DATA-PORT-2", 6),
          ("ccb-NET-PORT-1", 1),
          ("ccb-NET-PORT-2", 2),
          ("ccb-NET-PORT-3", 3),
          ("ccb-NET-PORT-4", 4),
          ("ccb-TAC-EQP-PORT", 8),
          ("ccb-TAC-NET-PORT", 7))
    )


_NcmSrcPortIdentifier_Type.__name__ = "Integer32"
_NcmSrcPortIdentifier_Object = MibTableColumn
ncmSrcPortIdentifier = _NcmSrcPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 9),
    _NcmSrcPortIdentifier_Type()
)
ncmSrcPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSrcPortIdentifier.setStatus("mandatory")
_NcmSrcTimeslotmap_Type = Integer32
_NcmSrcTimeslotmap_Object = MibTableColumn
ncmSrcTimeslotmap = _NcmSrcTimeslotmap_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 10),
    _NcmSrcTimeslotmap_Type()
)
ncmSrcTimeslotmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSrcTimeslotmap.setStatus("mandatory")
_NcmDstPortSite_Type = Integer32
_NcmDstPortSite_Object = MibTableColumn
ncmDstPortSite = _NcmDstPortSite_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 11),
    _NcmDstPortSite_Type()
)
ncmDstPortSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDstPortSite.setStatus("mandatory")


class _NcmDstCardEquipID_Type(Integer32):
    """Custom type ncmDstCardEquipID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(77,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              96,
              112,
              113,
              116)
        )
    )
    namedValues = NamedValues(
        *(("ace-FW-DUAL-E1", 87),
          ("ace-FW-DUAL-T1", 86),
          ("ace-FW-E1", 80),
          ("ace-FW-ISDN-E1", 113),
          ("ace-FW-ISDN-T1", 112),
          ("ace-FW-QUAD-E1", 83),
          ("ace-FW-QUAD-T1", 82),
          ("ace-FW-T1", 81),
          ("ace-Reserved", 84),
          ("card-SIGMA-VCU", 77),
          ("fw-DS3-CDSU", 88),
          ("fw-DS3-CDSU-CHANNEL", 89),
          ("fw-DS3-DUDS3", 116),
          ("fw-NCM", 96),
          ("tabs-IMUX", 85))
    )


_NcmDstCardEquipID_Type.__name__ = "Integer32"
_NcmDstCardEquipID_Object = MibTableColumn
ncmDstCardEquipID = _NcmDstCardEquipID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 12),
    _NcmDstCardEquipID_Type()
)
ncmDstCardEquipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDstCardEquipID.setStatus("mandatory")


class _NcmDstPortIdentifier_Type(Integer32):
    """Custom type ncmDstPortIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cb-UNKNOWN-PORT", 9),
          ("ccb-DATA-PORT-1", 5),
          ("ccb-DATA-PORT-2", 6),
          ("ccb-NET-PORT-1", 1),
          ("ccb-NET-PORT-2", 2),
          ("ccb-NET-PORT-3", 3),
          ("ccb-NET-PORT-4", 4),
          ("ccb-TAC-EQP-PORT", 8),
          ("ccb-TAC-NET-PORT", 7))
    )


_NcmDstPortIdentifier_Type.__name__ = "Integer32"
_NcmDstPortIdentifier_Object = MibTableColumn
ncmDstPortIdentifier = _NcmDstPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 13),
    _NcmDstPortIdentifier_Type()
)
ncmDstPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDstPortIdentifier.setStatus("mandatory")
_NcmDstTimeslotmap_Type = Integer32
_NcmDstTimeslotmap_Object = MibTableColumn
ncmDstTimeslotmap = _NcmDstTimeslotmap_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 14),
    _NcmDstTimeslotmap_Type()
)
ncmDstTimeslotmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmDstTimeslotmap.setStatus("mandatory")


class _NcmListccbBackPlaneBusID_Type(Integer32):
    """Custom type ncmListccbBackPlaneBusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ccb-BKPL-BUS-A1", 1),
          ("ccb-BKPL-BUS-A2", 2),
          ("ccb-BKPL-BUS-A3", 3),
          ("ccb-BKPL-BUS-A4", 4),
          ("ccb-BKPL-BUS-A5", 5),
          ("ccb-BKPL-BUS-A6", 6),
          ("ccb-BKPL-BUS-A7", 7),
          ("ccb-BKPL-BUS-A8", 8),
          ("ccb-BKPL-BUS-AUTO", 12),
          ("ccb-BKPL-BUS-B", 9),
          ("ccb-BKPL-BUS-C", 10),
          ("ccb-BKPL-BUS-NONE", 11))
    )


_NcmListccbBackPlaneBusID_Type.__name__ = "Integer32"
_NcmListccbBackPlaneBusID_Object = MibTableColumn
ncmListccbBackPlaneBusID = _NcmListccbBackPlaneBusID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 15),
    _NcmListccbBackPlaneBusID_Type()
)
ncmListccbBackPlaneBusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListccbBackPlaneBusID.setStatus("mandatory")


class _NcmListccbCircStatus_Type(Integer32):
    """Custom type ncmListccbCircStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ccb-CSTAT-ACTIVE", 3),
          ("ccb-CSTAT-BACKUPPED", 8),
          ("ccb-CSTAT-BROKEN", 6),
          ("ccb-CSTAT-EDITING", 2),
          ("ccb-CSTAT-INACTIVE", 4),
          ("ccb-CSTAT-LINE-ERR", 7),
          ("ccb-CSTAT-PREEMPTED", 5),
          ("ccb-CSTAT-SPARE", 1))
    )


_NcmListccbCircStatus_Type.__name__ = "Integer32"
_NcmListccbCircStatus_Object = MibTableColumn
ncmListccbCircStatus = _NcmListccbCircStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1041, 1, 16),
    _NcmListccbCircStatus_Type()
)
ncmListccbCircStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmListccbCircStatus.setStatus("mandatory")
_NcmEquipmentIDTable_Object = MibTable
ncmEquipmentIDTable = _NcmEquipmentIDTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042)
)
if mibBuilder.loadTexts:
    ncmEquipmentIDTable.setStatus("mandatory")
_NcmEquipmentIDEntry_Object = MibTableRow
ncmEquipmentIDEntry = _NcmEquipmentIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1)
)
ncmEquipmentIDEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmEquipmentIDNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmEquipmentIDLineIndex"),
)
if mibBuilder.loadTexts:
    ncmEquipmentIDEntry.setStatus("mandatory")
_NcmEquipmentIDNIDIndex_Type = Integer32
_NcmEquipmentIDNIDIndex_Object = MibTableColumn
ncmEquipmentIDNIDIndex = _NcmEquipmentIDNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1, 1),
    _NcmEquipmentIDNIDIndex_Type()
)
ncmEquipmentIDNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmEquipmentIDNIDIndex.setStatus("mandatory")
_NcmEquipmentIDLineIndex_Type = Integer32
_NcmEquipmentIDLineIndex_Object = MibTableColumn
ncmEquipmentIDLineIndex = _NcmEquipmentIDLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1, 2),
    _NcmEquipmentIDLineIndex_Type()
)
ncmEquipmentIDLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmEquipmentIDLineIndex.setStatus("mandatory")
_NcmFirmwareVersion_Type = Integer32
_NcmFirmwareVersion_Object = MibTableColumn
ncmFirmwareVersion = _NcmFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1, 3),
    _NcmFirmwareVersion_Type()
)
ncmFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmFirmwareVersion.setStatus("mandatory")
_NcmFirmwareRevision_Type = Integer32
_NcmFirmwareRevision_Object = MibTableColumn
ncmFirmwareRevision = _NcmFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1, 4),
    _NcmFirmwareRevision_Type()
)
ncmFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmFirmwareRevision.setStatus("mandatory")
_NcmEquipmentType_Type = Integer32
_NcmEquipmentType_Object = MibTableColumn
ncmEquipmentType = _NcmEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1, 5),
    _NcmEquipmentType_Type()
)
ncmEquipmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmEquipmentType.setStatus("mandatory")
_NcmHardwareVersion_Type = Integer32
_NcmHardwareVersion_Object = MibTableColumn
ncmHardwareVersion = _NcmHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1, 6),
    _NcmHardwareVersion_Type()
)
ncmHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmHardwareVersion.setStatus("mandatory")
_NcmHardwareRevision_Type = Integer32
_NcmHardwareRevision_Object = MibTableColumn
ncmHardwareRevision = _NcmHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1, 7),
    _NcmHardwareRevision_Type()
)
ncmHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmHardwareRevision.setStatus("mandatory")
_NcmLocationID_Type = Integer32
_NcmLocationID_Object = MibTableColumn
ncmLocationID = _NcmLocationID_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1042, 1, 8),
    _NcmLocationID_Type()
)
ncmLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLocationID.setStatus("mandatory")
_NcmE1AlarmThresholdConfigTable_Object = MibTable
ncmE1AlarmThresholdConfigTable = _NcmE1AlarmThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043)
)
if mibBuilder.loadTexts:
    ncmE1AlarmThresholdConfigTable.setStatus("mandatory")
_NcmE1AlarmThresholdConfigEntry_Object = MibTableRow
ncmE1AlarmThresholdConfigEntry = _NcmE1AlarmThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1)
)
ncmE1AlarmThresholdConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1AlarmThresholdConfigNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1AlarmThresholdConfigIndex"),
)
if mibBuilder.loadTexts:
    ncmE1AlarmThresholdConfigEntry.setStatus("mandatory")


class _NcmE1AlarmThresholdConfigNIDIndex_Type(Integer32):
    """Custom type ncmE1AlarmThresholdConfigNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1AlarmThresholdConfigNIDIndex_Type.__name__ = "Integer32"
_NcmE1AlarmThresholdConfigNIDIndex_Object = MibTableColumn
ncmE1AlarmThresholdConfigNIDIndex = _NcmE1AlarmThresholdConfigNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 1),
    _NcmE1AlarmThresholdConfigNIDIndex_Type()
)
ncmE1AlarmThresholdConfigNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1AlarmThresholdConfigNIDIndex.setStatus("mandatory")
_NcmE1AlarmThresholdConfigIndex_Type = Integer32
_NcmE1AlarmThresholdConfigIndex_Object = MibTableColumn
ncmE1AlarmThresholdConfigIndex = _NcmE1AlarmThresholdConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 2),
    _NcmE1AlarmThresholdConfigIndex_Type()
)
ncmE1AlarmThresholdConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1AlarmThresholdConfigIndex.setStatus("mandatory")
_NcmE1LOFThreshold_Type = Integer32
_NcmE1LOFThreshold_Object = MibTableColumn
ncmE1LOFThreshold = _NcmE1LOFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 3),
    _NcmE1LOFThreshold_Type()
)
ncmE1LOFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1LOFThreshold.setStatus("mandatory")
_NcmE1LOFTimeInterval_Type = Integer32
_NcmE1LOFTimeInterval_Object = MibTableColumn
ncmE1LOFTimeInterval = _NcmE1LOFTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 4),
    _NcmE1LOFTimeInterval_Type()
)
ncmE1LOFTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1LOFTimeInterval.setStatus("mandatory")
_NcmE1LOSThreshold_Type = Integer32
_NcmE1LOSThreshold_Object = MibTableColumn
ncmE1LOSThreshold = _NcmE1LOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 5),
    _NcmE1LOSThreshold_Type()
)
ncmE1LOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1LOSThreshold.setStatus("mandatory")
_NcmE1LOSTimeInterval_Type = Integer32
_NcmE1LOSTimeInterval_Object = MibTableColumn
ncmE1LOSTimeInterval = _NcmE1LOSTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 6),
    _NcmE1LOSTimeInterval_Type()
)
ncmE1LOSTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1LOSTimeInterval.setStatus("mandatory")
_NcmE1RAIThreshold_Type = Integer32
_NcmE1RAIThreshold_Object = MibTableColumn
ncmE1RAIThreshold = _NcmE1RAIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 7),
    _NcmE1RAIThreshold_Type()
)
ncmE1RAIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1RAIThreshold.setStatus("mandatory")
_NcmE1RAITimeInterval_Type = Integer32
_NcmE1RAITimeInterval_Object = MibTableColumn
ncmE1RAITimeInterval = _NcmE1RAITimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 8),
    _NcmE1RAITimeInterval_Type()
)
ncmE1RAITimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1RAITimeInterval.setStatus("mandatory")
_NcmE1AISThreshold_Type = Integer32
_NcmE1AISThreshold_Object = MibTableColumn
ncmE1AISThreshold = _NcmE1AISThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 9),
    _NcmE1AISThreshold_Type()
)
ncmE1AISThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1AISThreshold.setStatus("mandatory")
_NcmE1AISTimeInterval_Type = Integer32
_NcmE1AISTimeInterval_Object = MibTableColumn
ncmE1AISTimeInterval = _NcmE1AISTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 10),
    _NcmE1AISTimeInterval_Type()
)
ncmE1AISTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1AISTimeInterval.setStatus("mandatory")
_NcmE1BPVThreshold_Type = Integer32
_NcmE1BPVThreshold_Object = MibTableColumn
ncmE1BPVThreshold = _NcmE1BPVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 11),
    _NcmE1BPVThreshold_Type()
)
ncmE1BPVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1BPVThreshold.setStatus("mandatory")
_NcmE1BPVTimeInterval_Type = Integer32
_NcmE1BPVTimeInterval_Object = MibTableColumn
ncmE1BPVTimeInterval = _NcmE1BPVTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 12),
    _NcmE1BPVTimeInterval_Type()
)
ncmE1BPVTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1BPVTimeInterval.setStatus("mandatory")
_NcmE1ES15MINThreshold_Type = Integer32
_NcmE1ES15MINThreshold_Object = MibTableColumn
ncmE1ES15MINThreshold = _NcmE1ES15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 13),
    _NcmE1ES15MINThreshold_Type()
)
ncmE1ES15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1ES15MINThreshold.setStatus("mandatory")
_NcmE1ES24HRThreshold_Type = Integer32
_NcmE1ES24HRThreshold_Object = MibTableColumn
ncmE1ES24HRThreshold = _NcmE1ES24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 14),
    _NcmE1ES24HRThreshold_Type()
)
ncmE1ES24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1ES24HRThreshold.setStatus("mandatory")
_NcmE1SES15MINThreshold_Type = Integer32
_NcmE1SES15MINThreshold_Object = MibTableColumn
ncmE1SES15MINThreshold = _NcmE1SES15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 15),
    _NcmE1SES15MINThreshold_Type()
)
ncmE1SES15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1SES15MINThreshold.setStatus("mandatory")
_NcmE1SES24HRThreshold_Type = Integer32
_NcmE1SES24HRThreshold_Object = MibTableColumn
ncmE1SES24HRThreshold = _NcmE1SES24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 16),
    _NcmE1SES24HRThreshold_Type()
)
ncmE1SES24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmE1SES24HRThreshold.setStatus("mandatory")
_NcmCVP15MINThreshold_Type = Integer32
_NcmCVP15MINThreshold_Object = MibTableColumn
ncmCVP15MINThreshold = _NcmCVP15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 17),
    _NcmCVP15MINThreshold_Type()
)
ncmCVP15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCVP15MINThreshold.setStatus("mandatory")
_NcmCVP24HRThreshold_Type = Integer32
_NcmCVP24HRThreshold_Object = MibTableColumn
ncmCVP24HRThreshold = _NcmCVP24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 18),
    _NcmCVP24HRThreshold_Type()
)
ncmCVP24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCVP24HRThreshold.setStatus("mandatory")
_NcmCVL15MINThreshold_Type = Integer32
_NcmCVL15MINThreshold_Object = MibTableColumn
ncmCVL15MINThreshold = _NcmCVL15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 19),
    _NcmCVL15MINThreshold_Type()
)
ncmCVL15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCVL15MINThreshold.setStatus("mandatory")
_NcmCVL24HRThreshold_Type = Integer32
_NcmCVL24HRThreshold_Object = MibTableColumn
ncmCVL24HRThreshold = _NcmCVL24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 20),
    _NcmCVL24HRThreshold_Type()
)
ncmCVL24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmCVL24HRThreshold.setStatus("mandatory")
_NcmESL15MINThreshold_Type = Integer32
_NcmESL15MINThreshold_Object = MibTableColumn
ncmESL15MINThreshold = _NcmESL15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 21),
    _NcmESL15MINThreshold_Type()
)
ncmESL15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmESL15MINThreshold.setStatus("mandatory")
_NcmESL24HRThreshold_Type = Integer32
_NcmESL24HRThreshold_Object = MibTableColumn
ncmESL24HRThreshold = _NcmESL24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 22),
    _NcmESL24HRThreshold_Type()
)
ncmESL24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmESL24HRThreshold.setStatus("mandatory")
_NcmSESL15MINThreshold_Type = Integer32
_NcmSESL15MINThreshold_Object = MibTableColumn
ncmSESL15MINThreshold = _NcmSESL15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 23),
    _NcmSESL15MINThreshold_Type()
)
ncmSESL15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSESL15MINThreshold.setStatus("mandatory")
_NcmSESL24HRThreshold_Type = Integer32
_NcmSESL24HRThreshold_Object = MibTableColumn
ncmSESL24HRThreshold = _NcmSESL24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 24),
    _NcmSESL24HRThreshold_Type()
)
ncmSESL24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSESL24HRThreshold.setStatus("mandatory")
_NcmUASP15MINThreshold_Type = Integer32
_NcmUASP15MINThreshold_Object = MibTableColumn
ncmUASP15MINThreshold = _NcmUASP15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 25),
    _NcmUASP15MINThreshold_Type()
)
ncmUASP15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmUASP15MINThreshold.setStatus("mandatory")
_NcmUASP24HRThreshold_Type = Integer32
_NcmUASP24HRThreshold_Object = MibTableColumn
ncmUASP24HRThreshold = _NcmUASP24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1043, 1, 26),
    _NcmUASP24HRThreshold_Type()
)
ncmUASP24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmUASP24HRThreshold.setStatus("mandatory")
_NcmE1AlarmThresholdStatusTable_Object = MibTable
ncmE1AlarmThresholdStatusTable = _NcmE1AlarmThresholdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044)
)
if mibBuilder.loadTexts:
    ncmE1AlarmThresholdStatusTable.setStatus("mandatory")
_NcmE1AlarmThresholdStatusEntry_Object = MibTableRow
ncmE1AlarmThresholdStatusEntry = _NcmE1AlarmThresholdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1)
)
ncmE1AlarmThresholdStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1AlarmThresholdStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmE1AlarmThresholdStatusIndex"),
)
if mibBuilder.loadTexts:
    ncmE1AlarmThresholdStatusEntry.setStatus("mandatory")


class _NcmE1AlarmThresholdStatusNIDIndex_Type(Integer32):
    """Custom type ncmE1AlarmThresholdStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmE1AlarmThresholdStatusNIDIndex_Type.__name__ = "Integer32"
_NcmE1AlarmThresholdStatusNIDIndex_Object = MibTableColumn
ncmE1AlarmThresholdStatusNIDIndex = _NcmE1AlarmThresholdStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 1),
    _NcmE1AlarmThresholdStatusNIDIndex_Type()
)
ncmE1AlarmThresholdStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1AlarmThresholdStatusNIDIndex.setStatus("mandatory")
_NcmE1AlarmThresholdStatusIndex_Type = Integer32
_NcmE1AlarmThresholdStatusIndex_Object = MibTableColumn
ncmE1AlarmThresholdStatusIndex = _NcmE1AlarmThresholdStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 2),
    _NcmE1AlarmThresholdStatusIndex_Type()
)
ncmE1AlarmThresholdStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmE1AlarmThresholdStatusIndex.setStatus("mandatory")


class _NcmLOFExceededE1_Type(Integer32):
    """Custom type ncmLOFExceededE1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmLOFExceededE1_Type.__name__ = "Integer32"
_NcmLOFExceededE1_Object = MibTableColumn
ncmLOFExceededE1 = _NcmLOFExceededE1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 3),
    _NcmLOFExceededE1_Type()
)
ncmLOFExceededE1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOFExceededE1.setStatus("mandatory")


class _NcmLOSExceededE1_Type(Integer32):
    """Custom type ncmLOSExceededE1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmLOSExceededE1_Type.__name__ = "Integer32"
_NcmLOSExceededE1_Object = MibTableColumn
ncmLOSExceededE1 = _NcmLOSExceededE1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 4),
    _NcmLOSExceededE1_Type()
)
ncmLOSExceededE1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOSExceededE1.setStatus("mandatory")


class _NcmRAIExceededE1_Type(Integer32):
    """Custom type ncmRAIExceededE1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmRAIExceededE1_Type.__name__ = "Integer32"
_NcmRAIExceededE1_Object = MibTableColumn
ncmRAIExceededE1 = _NcmRAIExceededE1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 5),
    _NcmRAIExceededE1_Type()
)
ncmRAIExceededE1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmRAIExceededE1.setStatus("mandatory")


class _NcmAISExceededE1_Type(Integer32):
    """Custom type ncmAISExceededE1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmAISExceededE1_Type.__name__ = "Integer32"
_NcmAISExceededE1_Object = MibTableColumn
ncmAISExceededE1 = _NcmAISExceededE1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 6),
    _NcmAISExceededE1_Type()
)
ncmAISExceededE1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAISExceededE1.setStatus("mandatory")


class _NcmBPVExceededE1_Type(Integer32):
    """Custom type ncmBPVExceededE1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmBPVExceededE1_Type.__name__ = "Integer32"
_NcmBPVExceededE1_Object = MibTableColumn
ncmBPVExceededE1 = _NcmBPVExceededE1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 7),
    _NcmBPVExceededE1_Type()
)
ncmBPVExceededE1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmBPVExceededE1.setStatus("mandatory")


class _NcmES15MINExceeded_Type(Integer32):
    """Custom type ncmES15MINExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmES15MINExceeded_Type.__name__ = "Integer32"
_NcmES15MINExceeded_Object = MibTableColumn
ncmES15MINExceeded = _NcmES15MINExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 8),
    _NcmES15MINExceeded_Type()
)
ncmES15MINExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmES15MINExceeded.setStatus("mandatory")


class _NcmES24HRExceeded_Type(Integer32):
    """Custom type ncmES24HRExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmES24HRExceeded_Type.__name__ = "Integer32"
_NcmES24HRExceeded_Object = MibTableColumn
ncmES24HRExceeded = _NcmES24HRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 9),
    _NcmES24HRExceeded_Type()
)
ncmES24HRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmES24HRExceeded.setStatus("mandatory")


class _NcmSES15MINExceeded_Type(Integer32):
    """Custom type ncmSES15MINExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmSES15MINExceeded_Type.__name__ = "Integer32"
_NcmSES15MINExceeded_Object = MibTableColumn
ncmSES15MINExceeded = _NcmSES15MINExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 10),
    _NcmSES15MINExceeded_Type()
)
ncmSES15MINExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSES15MINExceeded.setStatus("mandatory")


class _NcmSES24HRExceeded_Type(Integer32):
    """Custom type ncmSES24HRExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmSES24HRExceeded_Type.__name__ = "Integer32"
_NcmSES24HRExceeded_Object = MibTableColumn
ncmSES24HRExceeded = _NcmSES24HRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 11),
    _NcmSES24HRExceeded_Type()
)
ncmSES24HRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSES24HRExceeded.setStatus("mandatory")


class _NcmCVP15MINExceeded_Type(Integer32):
    """Custom type ncmCVP15MINExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmCVP15MINExceeded_Type.__name__ = "Integer32"
_NcmCVP15MINExceeded_Object = MibTableColumn
ncmCVP15MINExceeded = _NcmCVP15MINExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 12),
    _NcmCVP15MINExceeded_Type()
)
ncmCVP15MINExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCVP15MINExceeded.setStatus("mandatory")


class _NcmCVP24HRExceeded_Type(Integer32):
    """Custom type ncmCVP24HRExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmCVP24HRExceeded_Type.__name__ = "Integer32"
_NcmCVP24HRExceeded_Object = MibTableColumn
ncmCVP24HRExceeded = _NcmCVP24HRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 13),
    _NcmCVP24HRExceeded_Type()
)
ncmCVP24HRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCVP24HRExceeded.setStatus("mandatory")


class _NcmCVL15MINExceeded_Type(Integer32):
    """Custom type ncmCVL15MINExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmCVL15MINExceeded_Type.__name__ = "Integer32"
_NcmCVL15MINExceeded_Object = MibTableColumn
ncmCVL15MINExceeded = _NcmCVL15MINExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 14),
    _NcmCVL15MINExceeded_Type()
)
ncmCVL15MINExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCVL15MINExceeded.setStatus("mandatory")


class _NcmCVL24HRExceeded_Type(Integer32):
    """Custom type ncmCVL24HRExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmCVL24HRExceeded_Type.__name__ = "Integer32"
_NcmCVL24HRExceeded_Object = MibTableColumn
ncmCVL24HRExceeded = _NcmCVL24HRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 15),
    _NcmCVL24HRExceeded_Type()
)
ncmCVL24HRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCVL24HRExceeded.setStatus("mandatory")


class _NcmESL15MINExceeded_Type(Integer32):
    """Custom type ncmESL15MINExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmESL15MINExceeded_Type.__name__ = "Integer32"
_NcmESL15MINExceeded_Object = MibTableColumn
ncmESL15MINExceeded = _NcmESL15MINExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 16),
    _NcmESL15MINExceeded_Type()
)
ncmESL15MINExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmESL15MINExceeded.setStatus("mandatory")


class _NcmESL24HRExceeded_Type(Integer32):
    """Custom type ncmESL24HRExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmESL24HRExceeded_Type.__name__ = "Integer32"
_NcmESL24HRExceeded_Object = MibTableColumn
ncmESL24HRExceeded = _NcmESL24HRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 17),
    _NcmESL24HRExceeded_Type()
)
ncmESL24HRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmESL24HRExceeded.setStatus("mandatory")


class _NcmSESL15MINExceeded_Type(Integer32):
    """Custom type ncmSESL15MINExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmSESL15MINExceeded_Type.__name__ = "Integer32"
_NcmSESL15MINExceeded_Object = MibTableColumn
ncmSESL15MINExceeded = _NcmSESL15MINExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 18),
    _NcmSESL15MINExceeded_Type()
)
ncmSESL15MINExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSESL15MINExceeded.setStatus("mandatory")


class _NcmSESL24HRExceeded_Type(Integer32):
    """Custom type ncmSESL24HRExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmSESL24HRExceeded_Type.__name__ = "Integer32"
_NcmSESL24HRExceeded_Object = MibTableColumn
ncmSESL24HRExceeded = _NcmSESL24HRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 19),
    _NcmSESL24HRExceeded_Type()
)
ncmSESL24HRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSESL24HRExceeded.setStatus("mandatory")


class _NcmUASP15MINExceeded_Type(Integer32):
    """Custom type ncmUASP15MINExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmUASP15MINExceeded_Type.__name__ = "Integer32"
_NcmUASP15MINExceeded_Object = MibTableColumn
ncmUASP15MINExceeded = _NcmUASP15MINExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 20),
    _NcmUASP15MINExceeded_Type()
)
ncmUASP15MINExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmUASP15MINExceeded.setStatus("mandatory")


class _NcmUASP24HRExceeded_Type(Integer32):
    """Custom type ncmUASP24HRExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmUASP24HRExceeded_Type.__name__ = "Integer32"
_NcmUASP24HRExceeded_Object = MibTableColumn
ncmUASP24HRExceeded = _NcmUASP24HRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 21),
    _NcmUASP24HRExceeded_Type()
)
ncmUASP24HRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmUASP24HRExceeded.setStatus("mandatory")
_NcmLOFThresholdCount_Type = Integer32
_NcmLOFThresholdCount_Object = MibTableColumn
ncmLOFThresholdCount = _NcmLOFThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 22),
    _NcmLOFThresholdCount_Type()
)
ncmLOFThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOFThresholdCount.setStatus("mandatory")
_NcmLOFTimeIntervals_Type = Integer32
_NcmLOFTimeIntervals_Object = MibTableColumn
ncmLOFTimeIntervals = _NcmLOFTimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 23),
    _NcmLOFTimeIntervals_Type()
)
ncmLOFTimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOFTimeIntervals.setStatus("mandatory")
_NcmLOSThresholdCount_Type = Integer32
_NcmLOSThresholdCount_Object = MibTableColumn
ncmLOSThresholdCount = _NcmLOSThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 24),
    _NcmLOSThresholdCount_Type()
)
ncmLOSThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOSThresholdCount.setStatus("mandatory")
_NcmLOSTimeIntervals_Type = Integer32
_NcmLOSTimeIntervals_Object = MibTableColumn
ncmLOSTimeIntervals = _NcmLOSTimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 25),
    _NcmLOSTimeIntervals_Type()
)
ncmLOSTimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOSTimeIntervals.setStatus("mandatory")
_NcmRAIThresholdCount_Type = Integer32
_NcmRAIThresholdCount_Object = MibTableColumn
ncmRAIThresholdCount = _NcmRAIThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 26),
    _NcmRAIThresholdCount_Type()
)
ncmRAIThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmRAIThresholdCount.setStatus("mandatory")
_NcmRAITimeIntervals_Type = Integer32
_NcmRAITimeIntervals_Object = MibTableColumn
ncmRAITimeIntervals = _NcmRAITimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 27),
    _NcmRAITimeIntervals_Type()
)
ncmRAITimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmRAITimeIntervals.setStatus("mandatory")
_NcmAISThresholdCount_Type = Integer32
_NcmAISThresholdCount_Object = MibTableColumn
ncmAISThresholdCount = _NcmAISThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 28),
    _NcmAISThresholdCount_Type()
)
ncmAISThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAISThresholdCount.setStatus("mandatory")
_NcmAISTimeIntervals_Type = Integer32
_NcmAISTimeIntervals_Object = MibTableColumn
ncmAISTimeIntervals = _NcmAISTimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 29),
    _NcmAISTimeIntervals_Type()
)
ncmAISTimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAISTimeIntervals.setStatus("mandatory")
_NcmBPVThresholdCount_Type = Integer32
_NcmBPVThresholdCount_Object = MibTableColumn
ncmBPVThresholdCount = _NcmBPVThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 30),
    _NcmBPVThresholdCount_Type()
)
ncmBPVThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmBPVThresholdCount.setStatus("mandatory")
_NcmBPVTimeIntervals_Type = Integer32
_NcmBPVTimeIntervals_Object = MibTableColumn
ncmBPVTimeIntervals = _NcmBPVTimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 31),
    _NcmBPVTimeIntervals_Type()
)
ncmBPVTimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmBPVTimeIntervals.setStatus("mandatory")
_NcmES15MINThresholdCount_Type = Integer32
_NcmES15MINThresholdCount_Object = MibTableColumn
ncmES15MINThresholdCount = _NcmES15MINThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 32),
    _NcmES15MINThresholdCount_Type()
)
ncmES15MINThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmES15MINThresholdCount.setStatus("mandatory")
_NcmES24HRThresholdCount_Type = Integer32
_NcmES24HRThresholdCount_Object = MibTableColumn
ncmES24HRThresholdCount = _NcmES24HRThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 33),
    _NcmES24HRThresholdCount_Type()
)
ncmES24HRThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmES24HRThresholdCount.setStatus("mandatory")
_NcmSES15MINThresholdCount_Type = Integer32
_NcmSES15MINThresholdCount_Object = MibTableColumn
ncmSES15MINThresholdCount = _NcmSES15MINThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 34),
    _NcmSES15MINThresholdCount_Type()
)
ncmSES15MINThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSES15MINThresholdCount.setStatus("mandatory")
_NcmSES24HRThresholdCount_Type = Integer32
_NcmSES24HRThresholdCount_Object = MibTableColumn
ncmSES24HRThresholdCount = _NcmSES24HRThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 35),
    _NcmSES24HRThresholdCount_Type()
)
ncmSES24HRThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSES24HRThresholdCount.setStatus("mandatory")
_NcmCVP15MINThresholdCount_Type = Integer32
_NcmCVP15MINThresholdCount_Object = MibTableColumn
ncmCVP15MINThresholdCount = _NcmCVP15MINThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 36),
    _NcmCVP15MINThresholdCount_Type()
)
ncmCVP15MINThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCVP15MINThresholdCount.setStatus("mandatory")
_NcmCVP24HRThresholdCount_Type = Integer32
_NcmCVP24HRThresholdCount_Object = MibTableColumn
ncmCVP24HRThresholdCount = _NcmCVP24HRThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 37),
    _NcmCVP24HRThresholdCount_Type()
)
ncmCVP24HRThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCVP24HRThresholdCount.setStatus("mandatory")
_NcmCVL15MINThresholdCount_Type = Integer32
_NcmCVL15MINThresholdCount_Object = MibTableColumn
ncmCVL15MINThresholdCount = _NcmCVL15MINThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 38),
    _NcmCVL15MINThresholdCount_Type()
)
ncmCVL15MINThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCVL15MINThresholdCount.setStatus("mandatory")
_NcmCVL24HRThresholdCount_Type = Integer32
_NcmCVL24HRThresholdCount_Object = MibTableColumn
ncmCVL24HRThresholdCount = _NcmCVL24HRThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 39),
    _NcmCVL24HRThresholdCount_Type()
)
ncmCVL24HRThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCVL24HRThresholdCount.setStatus("mandatory")
_NcmESL15MINThresholdCount_Type = Integer32
_NcmESL15MINThresholdCount_Object = MibTableColumn
ncmESL15MINThresholdCount = _NcmESL15MINThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 40),
    _NcmESL15MINThresholdCount_Type()
)
ncmESL15MINThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmESL15MINThresholdCount.setStatus("mandatory")
_NcmESL24HRThresholdCount_Type = Integer32
_NcmESL24HRThresholdCount_Object = MibTableColumn
ncmESL24HRThresholdCount = _NcmESL24HRThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 41),
    _NcmESL24HRThresholdCount_Type()
)
ncmESL24HRThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmESL24HRThresholdCount.setStatus("mandatory")
_NcmSESL15MINThresholdCount_Type = Integer32
_NcmSESL15MINThresholdCount_Object = MibTableColumn
ncmSESL15MINThresholdCount = _NcmSESL15MINThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 42),
    _NcmSESL15MINThresholdCount_Type()
)
ncmSESL15MINThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSESL15MINThresholdCount.setStatus("mandatory")
_NcmSESL24HRThresholdCount_Type = Integer32
_NcmSESL24HRThresholdCount_Object = MibTableColumn
ncmSESL24HRThresholdCount = _NcmSESL24HRThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 43),
    _NcmSESL24HRThresholdCount_Type()
)
ncmSESL24HRThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSESL24HRThresholdCount.setStatus("mandatory")
_NcmUASP15MINThresholdCount_Type = Integer32
_NcmUASP15MINThresholdCount_Object = MibTableColumn
ncmUASP15MINThresholdCount = _NcmUASP15MINThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 44),
    _NcmUASP15MINThresholdCount_Type()
)
ncmUASP15MINThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmUASP15MINThresholdCount.setStatus("mandatory")
_NcmUASP24HRThresholdCount_Type = Integer32
_NcmUASP24HRThresholdCount_Object = MibTableColumn
ncmUASP24HRThresholdCount = _NcmUASP24HRThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1044, 1, 45),
    _NcmUASP24HRThresholdCount_Type()
)
ncmUASP24HRThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmUASP24HRThresholdCount.setStatus("mandatory")
_NcmAlarmThresholdConfigTable_Object = MibTable
ncmAlarmThresholdConfigTable = _NcmAlarmThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045)
)
if mibBuilder.loadTexts:
    ncmAlarmThresholdConfigTable.setStatus("mandatory")
_NcmAlarmThresholdConfigEntry_Object = MibTableRow
ncmAlarmThresholdConfigEntry = _NcmAlarmThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1)
)
ncmAlarmThresholdConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmAlarmThresholdConfigNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmAlarmThresholdConfigIndex"),
)
if mibBuilder.loadTexts:
    ncmAlarmThresholdConfigEntry.setStatus("mandatory")


class _NcmAlarmThresholdConfigNIDIndex_Type(Integer32):
    """Custom type ncmAlarmThresholdConfigNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmAlarmThresholdConfigNIDIndex_Type.__name__ = "Integer32"
_NcmAlarmThresholdConfigNIDIndex_Object = MibTableColumn
ncmAlarmThresholdConfigNIDIndex = _NcmAlarmThresholdConfigNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 1),
    _NcmAlarmThresholdConfigNIDIndex_Type()
)
ncmAlarmThresholdConfigNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmThresholdConfigNIDIndex.setStatus("mandatory")
_NcmAlarmThresholdConfigIndex_Type = Integer32
_NcmAlarmThresholdConfigIndex_Object = MibTableColumn
ncmAlarmThresholdConfigIndex = _NcmAlarmThresholdConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 2),
    _NcmAlarmThresholdConfigIndex_Type()
)
ncmAlarmThresholdConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmThresholdConfigIndex.setStatus("mandatory")
_NcmLOFThreshold_Type = Integer32
_NcmLOFThreshold_Object = MibTableColumn
ncmLOFThreshold = _NcmLOFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 3),
    _NcmLOFThreshold_Type()
)
ncmLOFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmLOFThreshold.setStatus("mandatory")
_NcmLOFTimeInterval_Type = Integer32
_NcmLOFTimeInterval_Object = MibTableColumn
ncmLOFTimeInterval = _NcmLOFTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 4),
    _NcmLOFTimeInterval_Type()
)
ncmLOFTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmLOFTimeInterval.setStatus("mandatory")
_NcmLOSThreshold_Type = Integer32
_NcmLOSThreshold_Object = MibTableColumn
ncmLOSThreshold = _NcmLOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 5),
    _NcmLOSThreshold_Type()
)
ncmLOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmLOSThreshold.setStatus("mandatory")
_NcmLOSTimeInterval_Type = Integer32
_NcmLOSTimeInterval_Object = MibTableColumn
ncmLOSTimeInterval = _NcmLOSTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 6),
    _NcmLOSTimeInterval_Type()
)
ncmLOSTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmLOSTimeInterval.setStatus("mandatory")
_NcmRAIThreshold_Type = Integer32
_NcmRAIThreshold_Object = MibTableColumn
ncmRAIThreshold = _NcmRAIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 7),
    _NcmRAIThreshold_Type()
)
ncmRAIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmRAIThreshold.setStatus("mandatory")
_NcmRAITimeInterval_Type = Integer32
_NcmRAITimeInterval_Object = MibTableColumn
ncmRAITimeInterval = _NcmRAITimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 8),
    _NcmRAITimeInterval_Type()
)
ncmRAITimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmRAITimeInterval.setStatus("mandatory")
_NcmAISThreshold_Type = Integer32
_NcmAISThreshold_Object = MibTableColumn
ncmAISThreshold = _NcmAISThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 9),
    _NcmAISThreshold_Type()
)
ncmAISThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAISThreshold.setStatus("mandatory")
_NcmAISTimeInterval_Type = Integer32
_NcmAISTimeInterval_Object = MibTableColumn
ncmAISTimeInterval = _NcmAISTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 10),
    _NcmAISTimeInterval_Type()
)
ncmAISTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmAISTimeInterval.setStatus("mandatory")
_NcmBPVThreshold_Type = Integer32
_NcmBPVThreshold_Object = MibTableColumn
ncmBPVThreshold = _NcmBPVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 11),
    _NcmBPVThreshold_Type()
)
ncmBPVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmBPVThreshold.setStatus("mandatory")
_NcmBPVTimeInterval_Type = Integer32
_NcmBPVTimeInterval_Object = MibTableColumn
ncmBPVTimeInterval = _NcmBPVTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 12),
    _NcmBPVTimeInterval_Type()
)
ncmBPVTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmBPVTimeInterval.setStatus("mandatory")
_NcmES15MINThreshold_Type = Integer32
_NcmES15MINThreshold_Object = MibTableColumn
ncmES15MINThreshold = _NcmES15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 13),
    _NcmES15MINThreshold_Type()
)
ncmES15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmES15MINThreshold.setStatus("mandatory")
_NcmES24HRThreshold_Type = Integer32
_NcmES24HRThreshold_Object = MibTableColumn
ncmES24HRThreshold = _NcmES24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 14),
    _NcmES24HRThreshold_Type()
)
ncmES24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmES24HRThreshold.setStatus("mandatory")
_NcmSES15MINThreshold_Type = Integer32
_NcmSES15MINThreshold_Object = MibTableColumn
ncmSES15MINThreshold = _NcmSES15MINThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 15),
    _NcmSES15MINThreshold_Type()
)
ncmSES15MINThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSES15MINThreshold.setStatus("mandatory")
_NcmSES24HRThreshold_Type = Integer32
_NcmSES24HRThreshold_Object = MibTableColumn
ncmSES24HRThreshold = _NcmSES24HRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1045, 1, 16),
    _NcmSES24HRThreshold_Type()
)
ncmSES24HRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSES24HRThreshold.setStatus("mandatory")
_NcmAlarmThresholdStatusTable_Object = MibTable
ncmAlarmThresholdStatusTable = _NcmAlarmThresholdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046)
)
if mibBuilder.loadTexts:
    ncmAlarmThresholdStatusTable.setStatus("mandatory")
_NcmAlarmThresholdStatusEntry_Object = MibTableRow
ncmAlarmThresholdStatusEntry = _NcmAlarmThresholdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1)
)
ncmAlarmThresholdStatusEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmAlarmThresholdStatusNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmAlarmThresholdStatusIndex"),
)
if mibBuilder.loadTexts:
    ncmAlarmThresholdStatusEntry.setStatus("mandatory")


class _NcmAlarmThresholdStatusNIDIndex_Type(Integer32):
    """Custom type ncmAlarmThresholdStatusNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmAlarmThresholdStatusNIDIndex_Type.__name__ = "Integer32"
_NcmAlarmThresholdStatusNIDIndex_Object = MibTableColumn
ncmAlarmThresholdStatusNIDIndex = _NcmAlarmThresholdStatusNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 1),
    _NcmAlarmThresholdStatusNIDIndex_Type()
)
ncmAlarmThresholdStatusNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmThresholdStatusNIDIndex.setStatus("mandatory")
_NcmAlarmThresholdStatusIndex_Type = Integer32
_NcmAlarmThresholdStatusIndex_Object = MibTableColumn
ncmAlarmThresholdStatusIndex = _NcmAlarmThresholdStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 2),
    _NcmAlarmThresholdStatusIndex_Type()
)
ncmAlarmThresholdStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmThresholdStatusIndex.setStatus("mandatory")


class _NcmLOFExceeded_Type(Integer32):
    """Custom type ncmLOFExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmLOFExceeded_Type.__name__ = "Integer32"
_NcmLOFExceeded_Object = MibTableColumn
ncmLOFExceeded = _NcmLOFExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 3),
    _NcmLOFExceeded_Type()
)
ncmLOFExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOFExceeded.setStatus("mandatory")


class _NcmLOSExceeded_Type(Integer32):
    """Custom type ncmLOSExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmLOSExceeded_Type.__name__ = "Integer32"
_NcmLOSExceeded_Object = MibTableColumn
ncmLOSExceeded = _NcmLOSExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 4),
    _NcmLOSExceeded_Type()
)
ncmLOSExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOSExceeded.setStatus("mandatory")


class _NcmAISExceeded_Type(Integer32):
    """Custom type ncmAISExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmAISExceeded_Type.__name__ = "Integer32"
_NcmAISExceeded_Object = MibTableColumn
ncmAISExceeded = _NcmAISExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 5),
    _NcmAISExceeded_Type()
)
ncmAISExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAISExceeded.setStatus("mandatory")


class _NcmRAIExceeded_Type(Integer32):
    """Custom type ncmRAIExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmRAIExceeded_Type.__name__ = "Integer32"
_NcmRAIExceeded_Object = MibTableColumn
ncmRAIExceeded = _NcmRAIExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 6),
    _NcmRAIExceeded_Type()
)
ncmRAIExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmRAIExceeded.setStatus("mandatory")


class _NcmBPVExceeded_Type(Integer32):
    """Custom type ncmBPVExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmBPVExceeded_Type.__name__ = "Integer32"
_NcmBPVExceeded_Object = MibTableColumn
ncmBPVExceeded = _NcmBPVExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 7),
    _NcmBPVExceeded_Type()
)
ncmBPVExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmBPVExceeded.setStatus("mandatory")


class _NcmESExceeded_Type(Integer32):
    """Custom type ncmESExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmESExceeded_Type.__name__ = "Integer32"
_NcmESExceeded_Object = MibTableColumn
ncmESExceeded = _NcmESExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 8),
    _NcmESExceeded_Type()
)
ncmESExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmESExceeded.setStatus("mandatory")


class _NcmSESExceeded_Type(Integer32):
    """Custom type ncmSESExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NcmSESExceeded_Type.__name__ = "Integer32"
_NcmSESExceeded_Object = MibTableColumn
ncmSESExceeded = _NcmSESExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 9),
    _NcmSESExceeded_Type()
)
ncmSESExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSESExceeded.setStatus("mandatory")
_NcmLOFThresholdCountst_Type = Integer32
_NcmLOFThresholdCountst_Object = MibTableColumn
ncmLOFThresholdCountst = _NcmLOFThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 10),
    _NcmLOFThresholdCountst_Type()
)
ncmLOFThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOFThresholdCountst.setStatus("mandatory")
_NcmLOFTimeIntervalst_Type = Integer32
_NcmLOFTimeIntervalst_Object = MibTableColumn
ncmLOFTimeIntervalst = _NcmLOFTimeIntervalst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 11),
    _NcmLOFTimeIntervalst_Type()
)
ncmLOFTimeIntervalst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOFTimeIntervalst.setStatus("mandatory")
_NcmLOSThresholdCountst_Type = Integer32
_NcmLOSThresholdCountst_Object = MibTableColumn
ncmLOSThresholdCountst = _NcmLOSThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 12),
    _NcmLOSThresholdCountst_Type()
)
ncmLOSThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOSThresholdCountst.setStatus("mandatory")
_NcmLOSTimeIntervalst_Type = Integer32
_NcmLOSTimeIntervalst_Object = MibTableColumn
ncmLOSTimeIntervalst = _NcmLOSTimeIntervalst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 13),
    _NcmLOSTimeIntervalst_Type()
)
ncmLOSTimeIntervalst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmLOSTimeIntervalst.setStatus("mandatory")
_NcmRAIThresholdCountst_Type = Integer32
_NcmRAIThresholdCountst_Object = MibTableColumn
ncmRAIThresholdCountst = _NcmRAIThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 14),
    _NcmRAIThresholdCountst_Type()
)
ncmRAIThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmRAIThresholdCountst.setStatus("mandatory")
_NcmRAITimeIntervalst_Type = Integer32
_NcmRAITimeIntervalst_Object = MibTableColumn
ncmRAITimeIntervalst = _NcmRAITimeIntervalst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 15),
    _NcmRAITimeIntervalst_Type()
)
ncmRAITimeIntervalst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmRAITimeIntervalst.setStatus("mandatory")
_NcmAISThresholdCountst_Type = Integer32
_NcmAISThresholdCountst_Object = MibTableColumn
ncmAISThresholdCountst = _NcmAISThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 16),
    _NcmAISThresholdCountst_Type()
)
ncmAISThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAISThresholdCountst.setStatus("mandatory")
_NcmAISTimeIntervalst_Type = Integer32
_NcmAISTimeIntervalst_Object = MibTableColumn
ncmAISTimeIntervalst = _NcmAISTimeIntervalst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 17),
    _NcmAISTimeIntervalst_Type()
)
ncmAISTimeIntervalst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAISTimeIntervalst.setStatus("mandatory")
_NcmBPVThresholdCountst_Type = Integer32
_NcmBPVThresholdCountst_Object = MibTableColumn
ncmBPVThresholdCountst = _NcmBPVThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 18),
    _NcmBPVThresholdCountst_Type()
)
ncmBPVThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmBPVThresholdCountst.setStatus("mandatory")
_NcmBPVTimeIntervalst_Type = Integer32
_NcmBPVTimeIntervalst_Object = MibTableColumn
ncmBPVTimeIntervalst = _NcmBPVTimeIntervalst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 19),
    _NcmBPVTimeIntervalst_Type()
)
ncmBPVTimeIntervalst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmBPVTimeIntervalst.setStatus("mandatory")
_NcmES15MINThresholdCountst_Type = Integer32
_NcmES15MINThresholdCountst_Object = MibTableColumn
ncmES15MINThresholdCountst = _NcmES15MINThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 20),
    _NcmES15MINThresholdCountst_Type()
)
ncmES15MINThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmES15MINThresholdCountst.setStatus("mandatory")
_NcmES24HRThresholdCountst_Type = Integer32
_NcmES24HRThresholdCountst_Object = MibTableColumn
ncmES24HRThresholdCountst = _NcmES24HRThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 21),
    _NcmES24HRThresholdCountst_Type()
)
ncmES24HRThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmES24HRThresholdCountst.setStatus("mandatory")
_NcmSES15MINThresholdCountst_Type = Integer32
_NcmSES15MINThresholdCountst_Object = MibTableColumn
ncmSES15MINThresholdCountst = _NcmSES15MINThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 22),
    _NcmSES15MINThresholdCountst_Type()
)
ncmSES15MINThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSES15MINThresholdCountst.setStatus("mandatory")
_NcmSES24HRThresholdCountst_Type = Integer32
_NcmSES24HRThresholdCountst_Object = MibTableColumn
ncmSES24HRThresholdCountst = _NcmSES24HRThresholdCountst_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 23),
    _NcmSES24HRThresholdCountst_Type()
)
ncmSES24HRThresholdCountst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmSES24HRThresholdCountst.setStatus("mandatory")


class _NcmResetAlmThresholdCount_Type(Integer32):
    """Custom type ncmResetAlmThresholdCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_NcmResetAlmThresholdCount_Type.__name__ = "Integer32"
_NcmResetAlmThresholdCount_Object = MibTableColumn
ncmResetAlmThresholdCount = _NcmResetAlmThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1046, 1, 24),
    _NcmResetAlmThresholdCount_Type()
)
ncmResetAlmThresholdCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmResetAlmThresholdCount.setStatus("mandatory")
_NcmShelfSyncSourceSegTable_Object = MibTable
ncmShelfSyncSourceSegTable = _NcmShelfSyncSourceSegTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050)
)
if mibBuilder.loadTexts:
    ncmShelfSyncSourceSegTable.setStatus("mandatory")
_NcmShelfSyncSourceSegEntry_Object = MibTableRow
ncmShelfSyncSourceSegEntry = _NcmShelfSyncSourceSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1)
)
ncmShelfSyncSourceSegEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmShelfSyncSegNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmShelfSyncSourceSegIndex"),
    (0, "VERILINK-ENTERPRISE-NCMGENERIC-MIB", "ncmShelfSyncSourceSegNum"),
)
if mibBuilder.loadTexts:
    ncmShelfSyncSourceSegEntry.setStatus("mandatory")


class _NcmShelfSyncSegNIDIndex_Type(Integer32):
    """Custom type ncmShelfSyncSegNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmShelfSyncSegNIDIndex_Type.__name__ = "Integer32"
_NcmShelfSyncSegNIDIndex_Object = MibTableColumn
ncmShelfSyncSegNIDIndex = _NcmShelfSyncSegNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 1),
    _NcmShelfSyncSegNIDIndex_Type()
)
ncmShelfSyncSegNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfSyncSegNIDIndex.setStatus("mandatory")


class _NcmShelfSyncSourceSegIndex_Type(Integer32):
    """Custom type ncmShelfSyncSourceSegIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmShelfSyncSourceSegIndex_Type.__name__ = "Integer32"
_NcmShelfSyncSourceSegIndex_Object = MibTableColumn
ncmShelfSyncSourceSegIndex = _NcmShelfSyncSourceSegIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 2),
    _NcmShelfSyncSourceSegIndex_Type()
)
ncmShelfSyncSourceSegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfSyncSourceSegIndex.setStatus("mandatory")


class _NcmShelfSyncSourceSegNum_Type(Integer32):
    """Custom type ncmShelfSyncSourceSegNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmShelfSyncSourceSegNum_Type.__name__ = "Integer32"
_NcmShelfSyncSourceSegNum_Object = MibTableColumn
ncmShelfSyncSourceSegNum = _NcmShelfSyncSourceSegNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 3),
    _NcmShelfSyncSourceSegNum_Type()
)
ncmShelfSyncSourceSegNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfSyncSourceSegNum.setStatus("mandatory")


class _NcmShelfTypeSeg_Type(Integer32):
    """Custom type ncmShelfTypeSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              52,
              54)
        )
    )
    namedValues = NamedValues(
        *(("dualLineShelf", 2),
          ("multiLineShelf", 3),
          ("nb-2200-4ILineShelf", 10),
          ("nb-2200-4IQLineShelf", 54),
          ("nb-2200LineShelf", 4),
          ("nb-2200QLineShelf", 52),
          ("uninstalled", 1))
    )


_NcmShelfTypeSeg_Type.__name__ = "Integer32"
_NcmShelfTypeSeg_Object = MibTableColumn
ncmShelfTypeSeg = _NcmShelfTypeSeg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 4),
    _NcmShelfTypeSeg_Type()
)
ncmShelfTypeSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmShelfTypeSeg.setStatus("mandatory")


class _NcmRefBusSeg_Type(Integer32):
    """Custom type ncmRefBusSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("c", 1))
    )


_NcmRefBusSeg_Type.__name__ = "Integer32"
_NcmRefBusSeg_Object = MibTableColumn
ncmRefBusSeg = _NcmRefBusSeg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 5),
    _NcmRefBusSeg_Type()
)
ncmRefBusSeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmRefBusSeg.setStatus("mandatory")
_NcmSourceSegOneShelfNum_Type = Integer32
_NcmSourceSegOneShelfNum_Object = MibTableColumn
ncmSourceSegOneShelfNum = _NcmSourceSegOneShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 6),
    _NcmSourceSegOneShelfNum_Type()
)
ncmSourceSegOneShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegOneShelfNum.setStatus("mandatory")
_NcmSourceSegOneCardNum_Type = Integer32
_NcmSourceSegOneCardNum_Object = MibTableColumn
ncmSourceSegOneCardNum = _NcmSourceSegOneCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 7),
    _NcmSourceSegOneCardNum_Type()
)
ncmSourceSegOneCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegOneCardNum.setStatus("mandatory")


class _NcmSourceSegOneClockRef_Type(Integer32):
    """Custom type ncmSourceSegOneClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmSourceSegOneClockRef_Type.__name__ = "Integer32"
_NcmSourceSegOneClockRef_Object = MibTableColumn
ncmSourceSegOneClockRef = _NcmSourceSegOneClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 8),
    _NcmSourceSegOneClockRef_Type()
)
ncmSourceSegOneClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegOneClockRef.setStatus("mandatory")


class _NcmSourceSegAutoRestore1_Type(Integer32):
    """Custom type ncmSourceSegAutoRestore1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmSourceSegAutoRestore1_Type.__name__ = "Integer32"
_NcmSourceSegAutoRestore1_Object = MibTableColumn
ncmSourceSegAutoRestore1 = _NcmSourceSegAutoRestore1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 9),
    _NcmSourceSegAutoRestore1_Type()
)
ncmSourceSegAutoRestore1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegAutoRestore1.setStatus("mandatory")
_NcmSourceSegTwoShelfNum_Type = Integer32
_NcmSourceSegTwoShelfNum_Object = MibTableColumn
ncmSourceSegTwoShelfNum = _NcmSourceSegTwoShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 10),
    _NcmSourceSegTwoShelfNum_Type()
)
ncmSourceSegTwoShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegTwoShelfNum.setStatus("mandatory")
_NcmSourceSegTwoCardNum_Type = Integer32
_NcmSourceSegTwoCardNum_Object = MibTableColumn
ncmSourceSegTwoCardNum = _NcmSourceSegTwoCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 11),
    _NcmSourceSegTwoCardNum_Type()
)
ncmSourceSegTwoCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegTwoCardNum.setStatus("mandatory")


class _NcmSourceSegTwoClockRef_Type(Integer32):
    """Custom type ncmSourceSegTwoClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmSourceSegTwoClockRef_Type.__name__ = "Integer32"
_NcmSourceSegTwoClockRef_Object = MibTableColumn
ncmSourceSegTwoClockRef = _NcmSourceSegTwoClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 12),
    _NcmSourceSegTwoClockRef_Type()
)
ncmSourceSegTwoClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegTwoClockRef.setStatus("mandatory")


class _NcmSourceSegAutoRestore2_Type(Integer32):
    """Custom type ncmSourceSegAutoRestore2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmSourceSegAutoRestore2_Type.__name__ = "Integer32"
_NcmSourceSegAutoRestore2_Object = MibTableColumn
ncmSourceSegAutoRestore2 = _NcmSourceSegAutoRestore2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 13),
    _NcmSourceSegAutoRestore2_Type()
)
ncmSourceSegAutoRestore2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegAutoRestore2.setStatus("mandatory")
_NcmSourceSegThreeShelfNum_Type = Integer32
_NcmSourceSegThreeShelfNum_Object = MibTableColumn
ncmSourceSegThreeShelfNum = _NcmSourceSegThreeShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 14),
    _NcmSourceSegThreeShelfNum_Type()
)
ncmSourceSegThreeShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegThreeShelfNum.setStatus("mandatory")
_NcmSourceSegThreeCardNum_Type = Integer32
_NcmSourceSegThreeCardNum_Object = MibTableColumn
ncmSourceSegThreeCardNum = _NcmSourceSegThreeCardNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 15),
    _NcmSourceSegThreeCardNum_Type()
)
ncmSourceSegThreeCardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegThreeCardNum.setStatus("mandatory")


class _NcmSourceSegThreeClockRef_Type(Integer32):
    """Custom type ncmSourceSegThreeClockRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("e1-t1port1", 5),
          ("e1-t1port2", 6),
          ("external-timing", 7),
          ("internal-timing", 8),
          ("quad-t1-port3", 11),
          ("quad-t1-port4", 12))
    )


_NcmSourceSegThreeClockRef_Type.__name__ = "Integer32"
_NcmSourceSegThreeClockRef_Object = MibTableColumn
ncmSourceSegThreeClockRef = _NcmSourceSegThreeClockRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 16),
    _NcmSourceSegThreeClockRef_Type()
)
ncmSourceSegThreeClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegThreeClockRef.setStatus("mandatory")


class _NcmSourceSegAutoRestore3_Type(Integer32):
    """Custom type ncmSourceSegAutoRestore3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmSourceSegAutoRestore3_Type.__name__ = "Integer32"
_NcmSourceSegAutoRestore3_Object = MibTableColumn
ncmSourceSegAutoRestore3 = _NcmSourceSegAutoRestore3_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 17),
    _NcmSourceSegAutoRestore3_Type()
)
ncmSourceSegAutoRestore3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmSourceSegAutoRestore3.setStatus("mandatory")


class _NcmShelfCurrentSyncSourceSeg_Type(Integer32):
    """Custom type ncmShelfCurrentSyncSourceSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source1", 1),
          ("source2", 2),
          ("source3", 3))
    )


_NcmShelfCurrentSyncSourceSeg_Type.__name__ = "Integer32"
_NcmShelfCurrentSyncSourceSeg_Object = MibTableColumn
ncmShelfCurrentSyncSourceSeg = _NcmShelfCurrentSyncSourceSeg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012, 1050, 1, 18),
    _NcmShelfCurrentSyncSourceSeg_Type()
)
ncmShelfCurrentSyncSourceSeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmShelfCurrentSyncSourceSeg.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMGENERIC-MIB",
    **{"ncmNodeCurrTable": ncmNodeCurrTable,
       "ncmNodeCurrEntry": ncmNodeCurrEntry,
       "ncmNodeCurrIndex": ncmNodeCurrIndex,
       "ncmNodeCurrAddress": ncmNodeCurrAddress,
       "ncmActiveNodeStatus": ncmActiveNodeStatus,
       "ncmNodeInfoTable": ncmNodeInfoTable,
       "ncmNodeInfoEntry": ncmNodeInfoEntry,
       "ncmNodeIndex": ncmNodeIndex,
       "ncmNodeAddress": ncmNodeAddress,
       "ncmTime": ncmTime,
       "ncmDate": ncmDate,
       "ncmNodeShelf": ncmNodeShelf,
       "ncmNodeID": ncmNodeID,
       "ncmControllerEqID": ncmControllerEqID,
       "ncmShelfInfoTable": ncmShelfInfoTable,
       "ncmShelfInfoEntry": ncmShelfInfoEntry,
       "ncmShelfNIDIndex": ncmShelfNIDIndex,
       "ncmShelfIndex": ncmShelfIndex,
       "ncmShelfNumber": ncmShelfNumber,
       "ncmShelfHardware": ncmShelfHardware,
       "ncmNumberofCards": ncmNumberofCards,
       "ncmListCardsInShelf": ncmListCardsInShelf,
       "ncmCardInfoTable": ncmCardInfoTable,
       "ncmCardInfoEntry": ncmCardInfoEntry,
       "ncmCardNIDIndex": ncmCardNIDIndex,
       "ncmCardIndex": ncmCardIndex,
       "ncmFirmwareType": ncmFirmwareType,
       "ncmCimType": ncmCimType,
       "ncmClearCardInfo": ncmClearCardInfo,
       "ncmShelfSyncSourceTable": ncmShelfSyncSourceTable,
       "ncmShelfSyncSourceEntry": ncmShelfSyncSourceEntry,
       "ncmShelfSyncNIDIndex": ncmShelfSyncNIDIndex,
       "ncmShelfSyncSourceIndex": ncmShelfSyncSourceIndex,
       "ncmSourceOneShelfNum": ncmSourceOneShelfNum,
       "ncmSourceOneCardNum": ncmSourceOneCardNum,
       "ncmSourceOneClockRef": ncmSourceOneClockRef,
       "ncmAutoRestore1": ncmAutoRestore1,
       "ncmSourceTwoShelfNum": ncmSourceTwoShelfNum,
       "ncmSourceTwoCardNum": ncmSourceTwoCardNum,
       "ncmSourceTwoClockRef": ncmSourceTwoClockRef,
       "ncmAutoRestore2": ncmAutoRestore2,
       "ncmSourceThreeShelfNum": ncmSourceThreeShelfNum,
       "ncmSourceThreeCardNum": ncmSourceThreeCardNum,
       "ncmSourceThreeClockRef": ncmSourceThreeClockRef,
       "ncmAutoRestore3": ncmAutoRestore3,
       "ncmShelfCurrentSyncSource": ncmShelfCurrentSyncSource,
       "ncmCardSyncSourceTable": ncmCardSyncSourceTable,
       "ncmCardSyncSourceEntry": ncmCardSyncSourceEntry,
       "ncmCardSyncNIDIndex": ncmCardSyncNIDIndex,
       "ncmCardSyncSourceIndex": ncmCardSyncSourceIndex,
       "ncmCardReceiveClockFromShelf": ncmCardReceiveClockFromShelf,
       "ncmCardSourceOneShelfNum": ncmCardSourceOneShelfNum,
       "ncmCardSourceOneCardNum": ncmCardSourceOneCardNum,
       "ncmCardSourceOneClockRef": ncmCardSourceOneClockRef,
       "ncmCardAutoRestore1": ncmCardAutoRestore1,
       "ncmCardSourceTwoShelfNum": ncmCardSourceTwoShelfNum,
       "ncmCardSourceTwoCardNum": ncmCardSourceTwoCardNum,
       "ncmCardSourceTwoClockRef": ncmCardSourceTwoClockRef,
       "ncmCardAutoRestore2": ncmCardAutoRestore2,
       "ncmCardSourceThreeShelfNum": ncmCardSourceThreeShelfNum,
       "ncmCardSourceThreeCardNum": ncmCardSourceThreeCardNum,
       "ncmCardSourceThreeClockRef": ncmCardSourceThreeClockRef,
       "ncmCardAutoRestore3": ncmCardAutoRestore3,
       "ncmCardCurrentSyncSource": ncmCardCurrentSyncSource,
       "ncmIDPromTable": ncmIDPromTable,
       "ncmIDPromEntry": ncmIDPromEntry,
       "ncmIDPromNIDIndex": ncmIDPromNIDIndex,
       "ncmIDPromIndex": ncmIDPromIndex,
       "ncmCardType": ncmCardType,
       "ncmCardRevision": ncmCardRevision,
       "ncmCardDate": ncmCardDate,
       "ncmCardSerialNumber": ncmCardSerialNumber,
       "ncmManufacturePartNumber": ncmManufacturePartNumber,
       "ncmVendorCageCode": ncmVendorCageCode,
       "ncmIDCimType": ncmIDCimType,
       "ncmCimRevision": ncmCimRevision,
       "ncmCimDate": ncmCimDate,
       "ncmCimSerialNumber": ncmCimSerialNumber,
       "ncmCimManufacturePartNumber": ncmCimManufacturePartNumber,
       "ncmCimVendorCageCode": ncmCimVendorCageCode,
       "ncmE1PortConfigTable": ncmE1PortConfigTable,
       "ncmE1PortConfigEntry": ncmE1PortConfigEntry,
       "ncmE1ConfigNIDIndex": ncmE1ConfigNIDIndex,
       "ncmE1PortLineIndex": ncmE1PortLineIndex,
       "ncmE1PortCRC4": ncmE1PortCRC4,
       "ncmE1PortCarrierFailureAlarm": ncmE1PortCarrierFailureAlarm,
       "ncmE1PortFaseAlarm": ncmE1PortFaseAlarm,
       "ncmE1PortInbandISDNEnableDisable": ncmE1PortInbandISDNEnableDisable,
       "ncmE1PortRepeaterLoopbackTimeoutEnable": ncmE1PortRepeaterLoopbackTimeoutEnable,
       "ncmE1PortFraming": ncmE1PortFraming,
       "ncmE1PortRepeaterLoopbackTimeout": ncmE1PortRepeaterLoopbackTimeout,
       "ncmE1PortCarrierFailureAlarmDeclareTime": ncmE1PortCarrierFailureAlarmDeclareTime,
       "ncmE1PortServiceState": ncmE1PortServiceState,
       "ncmE1PortIdlePattern": ncmE1PortIdlePattern,
       "ncmE1TimeSlot": ncmE1TimeSlot,
       "ncmE1TimeSlotSelect": ncmE1TimeSlotSelect,
       "ncmE1PortStatusTable": ncmE1PortStatusTable,
       "ncmE1PortStatusEntry": ncmE1PortStatusEntry,
       "ncmE1PortStatusNIDIndex": ncmE1PortStatusNIDIndex,
       "ncmE1PortStatusIndex": ncmE1PortStatusIndex,
       "ncmE1PortCRC4Error": ncmE1PortCRC4Error,
       "ncmE1PortFramingSlip": ncmE1PortFramingSlip,
       "ncmE1PortRAI": ncmE1PortRAI,
       "ncmE1PortLOFA": ncmE1PortLOFA,
       "ncmE1PortAIS": ncmE1PortAIS,
       "ncmE1PortLOS": ncmE1PortLOS,
       "ncmE1PortBPVThresholdExceeded": ncmE1PortBPVThresholdExceeded,
       "ncmE1BlockErrorCounter": ncmE1BlockErrorCounter,
       "ncmE1CodeViolationMode": ncmE1CodeViolationMode,
       "ncmE1CurrentHDB3ORFEBEErrorCounts": ncmE1CurrentHDB3ORFEBEErrorCounts,
       "ncmE1CurrentFrameErrorCounts": ncmE1CurrentFrameErrorCounts,
       "ncmE1CurrentCRC4ErrorCounts": ncmE1CurrentCRC4ErrorCounts,
       "ncmE1ResetPerfCount": ncmE1ResetPerfCount,
       "ncmE1PortSendRAI": ncmE1PortSendRAI,
       "ncmE1PortSendAIS": ncmE1PortSendAIS,
       "ncmE1PortRFA": ncmE1PortRFA,
       "ncmE1PortBERThresholdExceeded": ncmE1PortBERThresholdExceeded,
       "ncmE1PortLLB": ncmE1PortLLB,
       "ncmE1PortPLB": ncmE1PortPLB,
       "ncmE1PortLOC": ncmE1PortLOC,
       "ncmE1PortTestPattern": ncmE1PortTestPattern,
       "ncmE1CurrentTable": ncmE1CurrentTable,
       "ncmE1CurrentEntry": ncmE1CurrentEntry,
       "ncmE1CurrentNIDIndex": ncmE1CurrentNIDIndex,
       "ncmE1CurrentIndex": ncmE1CurrentIndex,
       "ncmE1CurrentEndType": ncmE1CurrentEndType,
       "ncmE1CRC4Status": ncmE1CRC4Status,
       "ncmE1Timestamp": ncmE1Timestamp,
       "ncmE1Timestamp1": ncmE1Timestamp1,
       "ncmE1CurrentIntervalSec": ncmE1CurrentIntervalSec,
       "ncmE1CurrentASs": ncmE1CurrentASs,
       "ncmE1CurrentUASs": ncmE1CurrentUASs,
       "ncmE1CurrentESs": ncmE1CurrentESs,
       "ncmE1CurrentSESs": ncmE1CurrentSESs,
       "ncmE1CurrentFAE": ncmE1CurrentFAE,
       "ncmE1CurrentBBE": ncmE1CurrentBBE,
       "ncmE1CurrentSEFSs": ncmE1CurrentSEFSs,
       "ncmE1CurrentAISSs": ncmE1CurrentAISSs,
       "ncmE1CurrentLOSSs": ncmE1CurrentLOSSs,
       "ncmE1CurrentLOFSs": ncmE1CurrentLOFSs,
       "ncmE1CurrentOOFSs": ncmE1CurrentOOFSs,
       "ncmE1CurrentCVPath": ncmE1CurrentCVPath,
       "ncmE1CurrentCVLine": ncmE1CurrentCVLine,
       "ncmE1CurrentESsLine": ncmE1CurrentESsLine,
       "ncmE1CurrentSESsLine": ncmE1CurrentSESsLine,
       "ncmE1CurrentFECPath": ncmE1CurrentFECPath,
       "ncmE1CurrentFECLine": ncmE1CurrentFECLine,
       "ncmE1IntervalTable": ncmE1IntervalTable,
       "ncmE1IntervalEntry": ncmE1IntervalEntry,
       "ncmE1IntervalNIDIndex": ncmE1IntervalNIDIndex,
       "ncmE1IntervalIndex": ncmE1IntervalIndex,
       "ncmE1IntervalEndType": ncmE1IntervalEndType,
       "ncmE1IntervalNumber": ncmE1IntervalNumber,
       "ncmE1IntervalASs": ncmE1IntervalASs,
       "ncmE1IntervalUASs": ncmE1IntervalUASs,
       "ncmE1IntervalESs": ncmE1IntervalESs,
       "ncmE1IntervalSESs": ncmE1IntervalSESs,
       "ncmE1IntervalFAE": ncmE1IntervalFAE,
       "ncmE1IntervalBBE": ncmE1IntervalBBE,
       "ncmE1IntervalSEFSs": ncmE1IntervalSEFSs,
       "ncmE1IntervalAISSs": ncmE1IntervalAISSs,
       "ncmE1IntervalLOSSs": ncmE1IntervalLOSSs,
       "ncmE1IntervalLOFSs": ncmE1IntervalLOFSs,
       "ncmE1IntervalOOFSs": ncmE1IntervalOOFSs,
       "ncmE1IntervalCVPath": ncmE1IntervalCVPath,
       "ncmE1IntervalCVLine": ncmE1IntervalCVLine,
       "ncmE1IntervalESsLine": ncmE1IntervalESsLine,
       "ncmE1IntervalSESsLine": ncmE1IntervalSESsLine,
       "ncmE1IntervalFECPath": ncmE1IntervalFECPath,
       "ncmE1IntervalFECLine": ncmE1IntervalFECLine,
       "ncmE1TotalTable": ncmE1TotalTable,
       "ncmE1TotalEntry": ncmE1TotalEntry,
       "ncmE1TotalNIDIndex": ncmE1TotalNIDIndex,
       "ncmE1TotalIndex": ncmE1TotalIndex,
       "ncmE1TotalEndType": ncmE1TotalEndType,
       "ncmE1NumberOfValidInterval": ncmE1NumberOfValidInterval,
       "ncmE1TotalASs": ncmE1TotalASs,
       "ncmE1TotalUASs": ncmE1TotalUASs,
       "ncmE1TotalESs": ncmE1TotalESs,
       "ncmE1TotalSESs": ncmE1TotalSESs,
       "ncmE1TotalFAE": ncmE1TotalFAE,
       "ncmE1TotalBBE": ncmE1TotalBBE,
       "ncmE1TotalSEFSs": ncmE1TotalSEFSs,
       "ncmE1TotalAISSs": ncmE1TotalAISSs,
       "ncmE1TotalLOSSs": ncmE1TotalLOSSs,
       "ncmE1TotalLOFSs": ncmE1TotalLOFSs,
       "ncmE1TotalOOFSs": ncmE1TotalOOFSs,
       "ncmE1TotalCVPath": ncmE1TotalCVPath,
       "ncmE1TotalCVLine": ncmE1TotalCVLine,
       "ncmE1TotalESsLine": ncmE1TotalESsLine,
       "ncmE1TotalSESsLine": ncmE1TotalSESsLine,
       "ncmE1TotalFECPath": ncmE1TotalFECPath,
       "ncmE1TotalFECLine": ncmE1TotalFECLine,
       "ncmE1PrevTotalTable": ncmE1PrevTotalTable,
       "ncmE1PrevTotalEntry": ncmE1PrevTotalEntry,
       "ncmE1PrevTotalNIDIndex": ncmE1PrevTotalNIDIndex,
       "ncmE1PrevTotalIndex": ncmE1PrevTotalIndex,
       "ncmE1PrevTotalEndType": ncmE1PrevTotalEndType,
       "ncmE1PrevTotalASs": ncmE1PrevTotalASs,
       "ncmE1PrevTotalUASs": ncmE1PrevTotalUASs,
       "ncmE1PrevTotalESs": ncmE1PrevTotalESs,
       "ncmE1PrevTotalSESs": ncmE1PrevTotalSESs,
       "ncmE1PrevTotalFAE": ncmE1PrevTotalFAE,
       "ncmE1PrevTotalBBE": ncmE1PrevTotalBBE,
       "ncmE1PrevTotalSEFSs": ncmE1PrevTotalSEFSs,
       "ncmE1PrevTotalAISSs": ncmE1PrevTotalAISSs,
       "ncmE1PrevTotalLOSSs": ncmE1PrevTotalLOSSs,
       "ncmE1PrevTotalLOFSs": ncmE1PrevTotalLOFSs,
       "ncmE1PrevTotalOOFSs": ncmE1PrevTotalOOFSs,
       "ncmE1PrevTotalCVPath": ncmE1PrevTotalCVPath,
       "ncmE1PrevTotalCVLine": ncmE1PrevTotalCVLine,
       "ncmE1PrevTotalESsLine": ncmE1PrevTotalESsLine,
       "ncmE1PrevTotalSESsLine": ncmE1PrevTotalSESsLine,
       "ncmE1PrevTotalFECPath": ncmE1PrevTotalFECPath,
       "ncmE1PrevTotalFECLine": ncmE1PrevTotalFECLine,
       "ncmE1PerformanceSnapShotTable": ncmE1PerformanceSnapShotTable,
       "ncmE1PerformanceSnapShotEntry": ncmE1PerformanceSnapShotEntry,
       "ncmE1SnapShotNIDIndex": ncmE1SnapShotNIDIndex,
       "ncmE1SnapShotIndex": ncmE1SnapShotIndex,
       "ncmE1SnapShotEndType": ncmE1SnapShotEndType,
       "ncmE1SnapShot": ncmE1SnapShot,
       "ncmE1TimeStampSec": ncmE1TimeStampSec,
       "ncmE1TimeMilliSec": ncmE1TimeMilliSec,
       "ncmE1SecInCurrInterval": ncmE1SecInCurrInterval,
       "ncmE1ResetPerfReg": ncmE1ResetPerfReg,
       "ncmE1PortLatchedStatusTable": ncmE1PortLatchedStatusTable,
       "ncmE1PortLatchedStatusEntry": ncmE1PortLatchedStatusEntry,
       "ncmE1PortLatchedStatusNIDIndex": ncmE1PortLatchedStatusNIDIndex,
       "ncmE1PortLatchedStatusIndex": ncmE1PortLatchedStatusIndex,
       "ncmE1PortLatchedCRC4Error": ncmE1PortLatchedCRC4Error,
       "ncmE1PortLatchedFramingSlip": ncmE1PortLatchedFramingSlip,
       "ncmE1PortLatchedRAI": ncmE1PortLatchedRAI,
       "ncmE1PortLatchedLOFA": ncmE1PortLatchedLOFA,
       "ncmE1PortLatchedAIS": ncmE1PortLatchedAIS,
       "ncmE1PortLatchedLOS": ncmE1PortLatchedLOS,
       "ncmE1PortLatchedBPVThresholdExceeded": ncmE1PortLatchedBPVThresholdExceeded,
       "ncmE1ThresholdStatusTable": ncmE1ThresholdStatusTable,
       "ncmE1ThresholdStatusEntry": ncmE1ThresholdStatusEntry,
       "ncmE1ThresholdStatusNIDIndex": ncmE1ThresholdStatusNIDIndex,
       "ncmE1ThresholdStatusIndex": ncmE1ThresholdStatusIndex,
       "ncmE1CRCThreshold": ncmE1CRCThreshold,
       "ncmE1CRCExceeded": ncmE1CRCExceeded,
       "ncmE1SESThreshold": ncmE1SESThreshold,
       "ncmE1SESExceeded": ncmE1SESExceeded,
       "ncmE1UASThreshold": ncmE1UASThreshold,
       "ncmE1UASExceeded": ncmE1UASExceeded,
       "ncmE1BPVThresholdst": ncmE1BPVThresholdst,
       "ncmE1BPVExceeded": ncmE1BPVExceeded,
       "ncmE1BERThreshold": ncmE1BERThreshold,
       "ncmE1BERExceeded": ncmE1BERExceeded,
       "ncmE1RestoreState": ncmE1RestoreState,
       "ncmE1LineRestoreSec": ncmE1LineRestoreSec,
       "ncmT1ConfigTable": ncmT1ConfigTable,
       "ncmT1ConfigEntry": ncmT1ConfigEntry,
       "ncmT1ConfigNIDIndex": ncmT1ConfigNIDIndex,
       "ncmT1LineIndex": ncmT1LineIndex,
       "ncmT1CRC6": ncmT1CRC6,
       "ncmT1FramingFormat": ncmT1FramingFormat,
       "ncmT1LineCoding": ncmT1LineCoding,
       "ncmT1FramingType": ncmT1FramingType,
       "ncmT1FDL": ncmT1FDL,
       "ncmT1InbandISDNEnableDisable": ncmT1InbandISDNEnableDisable,
       "ncmT1EnableNetLoopback": ncmT1EnableNetLoopback,
       "ncmT1EnableNetOnesDensity": ncmT1EnableNetOnesDensity,
       "ncmT1DensityPattern": ncmT1DensityPattern,
       "ncmT1EnableRepeaterLpbkTimeout": ncmT1EnableRepeaterLpbkTimeout,
       "ncmT1RepeaterLoopbackTimeout": ncmT1RepeaterLoopbackTimeout,
       "ncmT1UserAlarmDeclareTime": ncmT1UserAlarmDeclareTime,
       "ncmT1State": ncmT1State,
       "ncmT1NetworkLBOEQLIZ": ncmT1NetworkLBOEQLIZ,
       "ncmT1TimeSlot": ncmT1TimeSlot,
       "ncmT1TimeSlotSelect": ncmT1TimeSlotSelect,
       "ncmT1PortStatusTable": ncmT1PortStatusTable,
       "ncmT1PortStatusEntry": ncmT1PortStatusEntry,
       "ncmT1PortStatusNIDIndex": ncmT1PortStatusNIDIndex,
       "ncmT1PortStatusIndex": ncmT1PortStatusIndex,
       "ncmT1PortCRC6Error": ncmT1PortCRC6Error,
       "ncmT1PortFramingSlip": ncmT1PortFramingSlip,
       "ncmT1PortRAI": ncmT1PortRAI,
       "ncmT1PortLOF": ncmT1PortLOF,
       "ncmT1PortAIS": ncmT1PortAIS,
       "ncmT1PortLOS": ncmT1PortLOS,
       "ncmT1PortBPVThresholdExceeded": ncmT1PortBPVThresholdExceeded,
       "ncmT1BlockErrorCounter": ncmT1BlockErrorCounter,
       "ncmT1BERExceeded": ncmT1BERExceeded,
       "ncmT1PortSendRAI": ncmT1PortSendRAI,
       "ncmT1PortSendAIS": ncmT1PortSendAIS,
       "ncmT1PortCGA": ncmT1PortCGA,
       "ncmT1PortLLB": ncmT1PortLLB,
       "ncmT1PortPLB": ncmT1PortPLB,
       "ncmT1PortLOC": ncmT1PortLOC,
       "ncmT1PortTestPattern": ncmT1PortTestPattern,
       "ncmT1CurrentTable": ncmT1CurrentTable,
       "ncmT1CurrentEntry": ncmT1CurrentEntry,
       "ncmT1CurrentNIDIndex": ncmT1CurrentNIDIndex,
       "ncmT1CurrentIndex": ncmT1CurrentIndex,
       "ncmT1CurrentEndType": ncmT1CurrentEndType,
       "ncmT1Timestamp": ncmT1Timestamp,
       "ncmT1Timestamp1": ncmT1Timestamp1,
       "ncmT1CurrentIntervalSec": ncmT1CurrentIntervalSec,
       "ncmT1CurrentASs": ncmT1CurrentASs,
       "ncmT1CurrentUASs": ncmT1CurrentUASs,
       "ncmT1CurrentESs": ncmT1CurrentESs,
       "ncmT1CurrentBESs": ncmT1CurrentBESs,
       "ncmT1CurrentSESs": ncmT1CurrentSESs,
       "ncmT1CurrentSEFs": ncmT1CurrentSEFs,
       "ncmT1CurrentLOSs": ncmT1CurrentLOSs,
       "ncmT1CurrentAISs": ncmT1CurrentAISs,
       "ncmT1CurrentLOFs": ncmT1CurrentLOFs,
       "ncmT1CurrentOOFs": ncmT1CurrentOOFs,
       "ncmT1CurrentESsTypeA": ncmT1CurrentESsTypeA,
       "ncmT1CurrentSASs": ncmT1CurrentSASs,
       "ncmT1CurrentCSSs": ncmT1CurrentCSSs,
       "ncmT1CurrentLOFC": ncmT1CurrentLOFC,
       "ncmT1CurrentFrameErrCount": ncmT1CurrentFrameErrCount,
       "ncmT1CurrentErrorFreeSec": ncmT1CurrentErrorFreeSec,
       "ncmT1CurrentDegradedMin": ncmT1CurrentDegradedMin,
       "ncmT1IntervalTable": ncmT1IntervalTable,
       "ncmT1IntervalEntry": ncmT1IntervalEntry,
       "ncmT1IntervalNIDIndex": ncmT1IntervalNIDIndex,
       "ncmT1IntervalIndex": ncmT1IntervalIndex,
       "ncmT1IntervalEndType": ncmT1IntervalEndType,
       "ncmT1IntervalNumber": ncmT1IntervalNumber,
       "ncmT1IntervalASs": ncmT1IntervalASs,
       "ncmT1IntervalUASs": ncmT1IntervalUASs,
       "ncmT1IntervalESs": ncmT1IntervalESs,
       "ncmT1IntervalBESs": ncmT1IntervalBESs,
       "ncmT1IntervalSESs": ncmT1IntervalSESs,
       "ncmT1IntervalSEFs": ncmT1IntervalSEFs,
       "ncmT1IntervalLOSs": ncmT1IntervalLOSs,
       "ncmT1IntervalAISs": ncmT1IntervalAISs,
       "ncmT1IntervalLOFs": ncmT1IntervalLOFs,
       "ncmT1IntervalOOFs": ncmT1IntervalOOFs,
       "ncmT1IntervalESsTypeA": ncmT1IntervalESsTypeA,
       "ncmT1IntervalSASs": ncmT1IntervalSASs,
       "ncmT1IntervalCSSs": ncmT1IntervalCSSs,
       "ncmT1IntervalLOFC": ncmT1IntervalLOFC,
       "ncmT1IntervalFrameErr": ncmT1IntervalFrameErr,
       "ncmT1IntervalErrFreeSec": ncmT1IntervalErrFreeSec,
       "ncmT1IntervalDegradMin": ncmT1IntervalDegradMin,
       "ncmT1TotalTable": ncmT1TotalTable,
       "ncmT1TotalEntry": ncmT1TotalEntry,
       "ncmT1TotalNIDIndex": ncmT1TotalNIDIndex,
       "ncmT1TotalIndex": ncmT1TotalIndex,
       "ncmT1TotalEndType": ncmT1TotalEndType,
       "ncmT1NumberOfValidIntervals": ncmT1NumberOfValidIntervals,
       "ncmT1TotalASs": ncmT1TotalASs,
       "ncmT1TotalUASs": ncmT1TotalUASs,
       "ncmT1TotalESs": ncmT1TotalESs,
       "ncmT1TotalBESs": ncmT1TotalBESs,
       "ncmT1TotalSESs": ncmT1TotalSESs,
       "ncmT1TotalSEFs": ncmT1TotalSEFs,
       "ncmT1TotalLOSs": ncmT1TotalLOSs,
       "ncmT1TotalAISs": ncmT1TotalAISs,
       "ncmT1TotalLOFs": ncmT1TotalLOFs,
       "ncmT1TotalOOFs": ncmT1TotalOOFs,
       "ncmT1TotalESsTypeA": ncmT1TotalESsTypeA,
       "ncmT1TotalSASs": ncmT1TotalSASs,
       "ncmT1TotalCSSs": ncmT1TotalCSSs,
       "ncmT1TotalLOFC": ncmT1TotalLOFC,
       "ncmT1TotalFrameErrCount": ncmT1TotalFrameErrCount,
       "ncmT1TotalErrorFreeSec": ncmT1TotalErrorFreeSec,
       "ncmT1TotalDegradedMin": ncmT1TotalDegradedMin,
       "ncmT1PrevTotalTable": ncmT1PrevTotalTable,
       "ncmT1PrevTotalEntry": ncmT1PrevTotalEntry,
       "ncmT1PrevTotalNIDIndex": ncmT1PrevTotalNIDIndex,
       "ncmT1PrevTotalIndex": ncmT1PrevTotalIndex,
       "ncmT1PrevTotalEndType": ncmT1PrevTotalEndType,
       "ncmT1PrevTotalASs": ncmT1PrevTotalASs,
       "ncmT1PrevTotalUASs": ncmT1PrevTotalUASs,
       "ncmT1PrevTotalESs": ncmT1PrevTotalESs,
       "ncmT1PrevTotalBESs": ncmT1PrevTotalBESs,
       "ncmT1PrevTotalSESs": ncmT1PrevTotalSESs,
       "ncmT1PrevTotalSEFs": ncmT1PrevTotalSEFs,
       "ncmT1PrevTotalLOSs": ncmT1PrevTotalLOSs,
       "ncmT1PrevTotalAISs": ncmT1PrevTotalAISs,
       "ncmT1PrevTotalLOFs": ncmT1PrevTotalLOFs,
       "ncmT1PrevTotalOOFs": ncmT1PrevTotalOOFs,
       "ncmT1PrevTotalESsTypeA": ncmT1PrevTotalESsTypeA,
       "ncmT1PrevTotalSASs": ncmT1PrevTotalSASs,
       "ncmT1PrevTotalCSSs": ncmT1PrevTotalCSSs,
       "ncmT1PrevTotalLOFC": ncmT1PrevTotalLOFC,
       "ncmT1PrevTotalFrameErrCount": ncmT1PrevTotalFrameErrCount,
       "ncmT1PrevTotalErrorFreeSec": ncmT1PrevTotalErrorFreeSec,
       "ncmT1PrevTotalDegradedMin": ncmT1PrevTotalDegradedMin,
       "ncmT1PreformanceSnapShotTable": ncmT1PreformanceSnapShotTable,
       "ncmT1PreformanceSnapShotEntry": ncmT1PreformanceSnapShotEntry,
       "ncmT1SnapShotNIDIndex": ncmT1SnapShotNIDIndex,
       "ncmT1SnapShotIndex": ncmT1SnapShotIndex,
       "ncmT1SnapShotEndType": ncmT1SnapShotEndType,
       "ncmT1SnapShot": ncmT1SnapShot,
       "ncmT1TimeStampSec": ncmT1TimeStampSec,
       "ncmT1TimeStampMilliSec": ncmT1TimeStampMilliSec,
       "ncmT1CurrIntervalSec": ncmT1CurrIntervalSec,
       "ncmT1ResetPerfReg": ncmT1ResetPerfReg,
       "ncmAdvancedT1ConfigTable": ncmAdvancedT1ConfigTable,
       "ncmAdvancedT1ConfigEntry": ncmAdvancedT1ConfigEntry,
       "ncmAdvancedT1NIDIndex": ncmAdvancedT1NIDIndex,
       "ncmAdvancedT1LineIndex": ncmAdvancedT1LineIndex,
       "ncmadvfdlMode": ncmadvfdlMode,
       "ncmadvfdlStandard": ncmadvfdlStandard,
       "ncmadvfdlPerformanceReport": ncmadvfdlPerformanceReport,
       "ncmadvfdlLBEnable": ncmadvfdlLBEnable,
       "ncmadvfdlLLBT1BOPMsg": ncmadvfdlLLBT1BOPMsg,
       "ncmadvfdlPLBT1BOPMsg": ncmadvfdlPLBT1BOPMsg,
       "ncmadvfdlIdlePattern": ncmadvfdlIdlePattern,
       "ncmadvfdlMonitoringCsuType": ncmadvfdlMonitoringCsuType,
       "ncmT1LatchedStatusTable": ncmT1LatchedStatusTable,
       "ncmT1LatchedStatusEntry": ncmT1LatchedStatusEntry,
       "ncmT1LatchedStatusNIDIndex": ncmT1LatchedStatusNIDIndex,
       "ncmT1LatchedStatusIndex": ncmT1LatchedStatusIndex,
       "ncmT1LatchedStatusEndType": ncmT1LatchedStatusEndType,
       "ncmT1LatchedStatusCRC6Error": ncmT1LatchedStatusCRC6Error,
       "ncmT1LatchedStatusFramingSlip": ncmT1LatchedStatusFramingSlip,
       "ncmT1LatchedStatusRAI": ncmT1LatchedStatusRAI,
       "ncmT1LatchedStatusLOF": ncmT1LatchedStatusLOF,
       "ncmT1LatchedStatusAIS": ncmT1LatchedStatusAIS,
       "ncmT1LatchedStatusLOS": ncmT1LatchedStatusLOS,
       "ncmT1LatchedStatusBPVThreExcd": ncmT1LatchedStatusBPVThreExcd,
       "ncmT1LatchedStatusBERExceeded": ncmT1LatchedStatusBERExceeded,
       "ncmT1ThresholdStatusTable": ncmT1ThresholdStatusTable,
       "ncmT1ThresholdStatusEntry": ncmT1ThresholdStatusEntry,
       "ncmT1ThresholdStatusNIDIndex": ncmT1ThresholdStatusNIDIndex,
       "ncmT1ThresholdStatusIndex": ncmT1ThresholdStatusIndex,
       "ncmT1ThresholdStatusEndType": ncmT1ThresholdStatusEndType,
       "ncmT1ThresholdRestoreState": ncmT1ThresholdRestoreState,
       "ncmT1ThresholdSecLineRestore": ncmT1ThresholdSecLineRestore,
       "ncmT1ThresholdBERExceeded": ncmT1ThresholdBERExceeded,
       "ncmT1ThresholdBERCount": ncmT1ThresholdBERCount,
       "ncmT1ThresholdSESExceeded": ncmT1ThresholdSESExceeded,
       "ncmT1ThresholdSESCount": ncmT1ThresholdSESCount,
       "ncmT1ThresholdUASExceeded": ncmT1ThresholdUASExceeded,
       "ncmT1ThresholdUASCount": ncmT1ThresholdUASCount,
       "ncmT1ThresholdCRCExceeded": ncmT1ThresholdCRCExceeded,
       "ncmT1ThresholdCRCCount": ncmT1ThresholdCRCCount,
       "ncmT1ThresholdBPVExceeded": ncmT1ThresholdBPVExceeded,
       "ncmT1ThresholdBPVCount": ncmT1ThresholdBPVCount,
       "ncmT1PerformanceCountersTable": ncmT1PerformanceCountersTable,
       "ncmT1PerformanceCountersEntry": ncmT1PerformanceCountersEntry,
       "ncmT1PerfCountNIDIndex": ncmT1PerfCountNIDIndex,
       "ncmT1PerfCountIndex": ncmT1PerfCountIndex,
       "ncmT1PerfCountEndType": ncmT1PerfCountEndType,
       "ncmT1PerfCountFrameMode": ncmT1PerfCountFrameMode,
       "ncmT1PerfCountCurESFErrEvt": ncmT1PerfCountCurESFErrEvt,
       "ncmT1PerfCountCurBPVErrCnt": ncmT1PerfCountCurBPVErrCnt,
       "ncmT1PerfCountCurFrameErrCnt": ncmT1PerfCountCurFrameErrCnt,
       "ncmT1PerfCountCurCRC6Error": ncmT1PerfCountCurCRC6Error,
       "ncmT1ResetPerfCount": ncmT1ResetPerfCount,
       "ncmDataPortConfigTable": ncmDataPortConfigTable,
       "ncmDataPortConfigEntry": ncmDataPortConfigEntry,
       "ncmDataPortConfigNIDIndex": ncmDataPortConfigNIDIndex,
       "ncmDataPortConfigIndex": ncmDataPortConfigIndex,
       "ncmDataPortConfigMode": ncmDataPortConfigMode,
       "ncmDataPortConfigLineIndicate": ncmDataPortConfigLineIndicate,
       "ncmDataPortLineStatusCDCC": ncmDataPortLineStatusCDCC,
       "ncmDataPortLineStatusCACB": ncmDataPortLineStatusCACB,
       "ncmDataPortLineStatusLLCJ": ncmDataPortLineStatusLLCJ,
       "ncmDataPortLineStatusRLTM": ncmDataPortLineStatusRLTM,
       "ncmDataPortConfigLOS": ncmDataPortConfigLOS,
       "ncmDataPortConfigServiceState": ncmDataPortConfigServiceState,
       "ncmDataPortConfigClkOpt": ncmDataPortConfigClkOpt,
       "ncmDataPortStatusTable": ncmDataPortStatusTable,
       "ncmDataPortStatusEntry": ncmDataPortStatusEntry,
       "ncmDataPortStatusNIDIndex": ncmDataPortStatusNIDIndex,
       "ncmDataPortStatusIndex": ncmDataPortStatusIndex,
       "ncmDataPortStatusMode": ncmDataPortStatusMode,
       "ncmDataPortStatusLineIndicate": ncmDataPortStatusLineIndicate,
       "ncmDataPortStatusLineCDCC": ncmDataPortStatusLineCDCC,
       "ncmDataPortStatusLineCACB": ncmDataPortStatusLineCACB,
       "ncmDataPortStatusLineLLCJ": ncmDataPortStatusLineLLCJ,
       "ncmDataPortStatusLineRLTM": ncmDataPortStatusLineRLTM,
       "ncmDataPortStatusLineLOS": ncmDataPortStatusLineLOS,
       "ncmDataPortStatusServiceState": ncmDataPortStatusServiceState,
       "ncmDataPortStatusCimType": ncmDataPortStatusCimType,
       "ncmDataPortStatusLoopback": ncmDataPortStatusLoopback,
       "ncmDataPortTestPattern": ncmDataPortTestPattern,
       "ncmDataPortTstPatErrCount": ncmDataPortTstPatErrCount,
       "ncmALARMConfigTable": ncmALARMConfigTable,
       "ncmALARMConfigEntry": ncmALARMConfigEntry,
       "ncmAlarmConfigNIDIndex": ncmAlarmConfigNIDIndex,
       "ncmAlarmConfigIndex": ncmAlarmConfigIndex,
       "ncmAlmCfgDomain": ncmAlmCfgDomain,
       "ncmAlmCfgSrcAddr": ncmAlmCfgSrcAddr,
       "ncmAlmCfgCard": ncmAlmCfgCard,
       "ncmAlmCfgShelf": ncmAlmCfgShelf,
       "ncmAlmCfgE1T1Port1EnableAlmRpt": ncmAlmCfgE1T1Port1EnableAlmRpt,
       "ncmAlmCfgE1T1Port2EnableAlmRpt": ncmAlmCfgE1T1Port2EnableAlmRpt,
       "ncmAlmCfgE1T1Port3EnableAlmRpt": ncmAlmCfgE1T1Port3EnableAlmRpt,
       "ncmAlmCfgE1T1Port4EnableAlmRpt": ncmAlmCfgE1T1Port4EnableAlmRpt,
       "ncmAlmCfgDataPort1EnableAlmRpt": ncmAlmCfgDataPort1EnableAlmRpt,
       "ncmAlmCfgDataPort2EnableAlmRpt": ncmAlmCfgDataPort2EnableAlmRpt,
       "ncmAlmCfgEnableCardAlmRpt": ncmAlmCfgEnableCardAlmRpt,
       "ncmAlmCfgDeclareTime": ncmAlmCfgDeclareTime,
       "ncmCURRENTAlarmMsgTable": ncmCURRENTAlarmMsgTable,
       "ncmCURRENTAlarmMsgEntry": ncmCURRENTAlarmMsgEntry,
       "ncmCurrAlarmMsgNIDIndex": ncmCurrAlarmMsgNIDIndex,
       "ncmCurrAlarmMsgIndex": ncmCurrAlarmMsgIndex,
       "ncmCurrAlarmMsgNumber": ncmCurrAlarmMsgNumber,
       "ncmCurrAlarmMsgEquipID": ncmCurrAlarmMsgEquipID,
       "ncmPrevAlarmMsgTable": ncmPrevAlarmMsgTable,
       "ncmPrevAlarmMsgEntry": ncmPrevAlarmMsgEntry,
       "ncmPrevAlarmMsgNIDIndex": ncmPrevAlarmMsgNIDIndex,
       "ncmPrevAlarmMsgIndex": ncmPrevAlarmMsgIndex,
       "ncmPrevAlarmMsgNumber": ncmPrevAlarmMsgNumber,
       "ncmPrevAlarmMsgTimeStampSec": ncmPrevAlarmMsgTimeStampSec,
       "ncmPrevAlarmMsgTimeStampms": ncmPrevAlarmMsgTimeStampms,
       "ncmPrevAlarmMsgAlarmCode": ncmPrevAlarmMsgAlarmCode,
       "ncmPrevAlarmMsgAlarmInstance": ncmPrevAlarmMsgAlarmInstance,
       "ncmPrevAlarmMsgObjType": ncmPrevAlarmMsgObjType,
       "ncmPrevAlarmMsgSeverity": ncmPrevAlarmMsgSeverity,
       "ncmEnhanAlmCfgTable": ncmEnhanAlmCfgTable,
       "ncmEnhanAlmCfgEntry": ncmEnhanAlmCfgEntry,
       "ncmEnhanAlmCfgNIDIndex": ncmEnhanAlmCfgNIDIndex,
       "ncmEnhanAlmCfgIndex": ncmEnhanAlmCfgIndex,
       "ncmEnhanAlmCfgCRCThreshold": ncmEnhanAlmCfgCRCThreshold,
       "ncmEnhanAlmCfgSESThreshold": ncmEnhanAlmCfgSESThreshold,
       "ncmEnhanAlmCfgUASThreshold": ncmEnhanAlmCfgUASThreshold,
       "ncmEnhanAlmCfgBERThreshold": ncmEnhanAlmCfgBERThreshold,
       "ncmEnhanAlmCfgBPVThreshold": ncmEnhanAlmCfgBPVThreshold,
       "ncmEnhanAlmCfgLineRestoral": ncmEnhanAlmCfgLineRestoral,
       "ncmEnhanAlmCfgTODHour": ncmEnhanAlmCfgTODHour,
       "ncmEnhanAlmCfgTODMinute": ncmEnhanAlmCfgTODMinute,
       "ncmEnhanAlmCfgLinRestEvalPer": ncmEnhanAlmCfgLinRestEvalPer,
       "ncmLoopbackTable": ncmLoopbackTable,
       "ncmLoopbackEntry": ncmLoopbackEntry,
       "ncmLpbkNIDIndex": ncmLpbkNIDIndex,
       "ncmLpbkLineIndex": ncmLpbkLineIndex,
       "ncmSetAllOnes": ncmSetAllOnes,
       "ncmTimeoutLOCSec": ncmTimeoutLOCSec,
       "ncmRemoteLB": ncmRemoteLB,
       "ncmActivateDeactLBType": ncmActivateDeactLBType,
       "ncmTestPatternTable": ncmTestPatternTable,
       "ncmTestPatternEntry": ncmTestPatternEntry,
       "ncmTstpattNIDIndex": ncmTstpattNIDIndex,
       "ncmTstpattLineIndex": ncmTstpattLineIndex,
       "ncmTstpattTestPeriod": ncmTstpattTestPeriod,
       "ncmStartStopTestPattern": ncmStartStopTestPattern,
       "ncmResetTestCounter": ncmResetTestCounter,
       "ncmCircuitInfoTable": ncmCircuitInfoTable,
       "ncmCircuitInfoEntry": ncmCircuitInfoEntry,
       "ncmCircuitInfoNIDIndex": ncmCircuitInfoNIDIndex,
       "ncmCircuitInfoCircName": ncmCircuitInfoCircName,
       "ncmCircuitInfoCircPriority": ncmCircuitInfoCircPriority,
       "ncmCircuitInfoCircType": ncmCircuitInfoCircType,
       "ncmCircuitInfoCircMode": ncmCircuitInfoCircMode,
       "ncmCircuitInfoSrcPortSite": ncmCircuitInfoSrcPortSite,
       "ncmCircuitInfoSrcCardEquipID": ncmCircuitInfoSrcCardEquipID,
       "ncmCircuitInfoSrcPortID": ncmCircuitInfoSrcPortID,
       "ncmCircuitInfoSrcTimeslotmap": ncmCircuitInfoSrcTimeslotmap,
       "ncmCircuitInfoDstPortSite": ncmCircuitInfoDstPortSite,
       "ncmCircuitInfoDstCardEquipID": ncmCircuitInfoDstCardEquipID,
       "ncmCircuitInfoDstPortID": ncmCircuitInfoDstPortID,
       "ncmCircuitInfoDstTimeslotmap": ncmCircuitInfoDstTimeslotmap,
       "ncmCircuitInfoBackPlaneBusID": ncmCircuitInfoBackPlaneBusID,
       "ncmCircuitInfoAssoCircName": ncmCircuitInfoAssoCircName,
       "ncmCircuitInfoAction": ncmCircuitInfoAction,
       "ncmAddEditActDeactCircuitStatus": ncmAddEditActDeactCircuitStatus,
       "ncmDeleteCircuitStatus": ncmDeleteCircuitStatus,
       "ncmGetDetailCircuitStatus": ncmGetDetailCircuitStatus,
       "ncmPortTimeslotAllocTable": ncmPortTimeslotAllocTable,
       "ncmPortTimeslotAllocEntry": ncmPortTimeslotAllocEntry,
       "ncmPortTimeslotAllocNIDIndex": ncmPortTimeslotAllocNIDIndex,
       "ncmPortTimeslotCardSite": ncmPortTimeslotCardSite,
       "ncmPortTimeslotCardEquipID": ncmPortTimeslotCardEquipID,
       "ncmPortTimeslotPortID": ncmPortTimeslotPortID,
       "ncmPortAllocTimeSlotMap": ncmPortAllocTimeSlotMap,
       "ncmDialBkUpInfoTable": ncmDialBkUpInfoTable,
       "ncmDialBkUpInfoEntry": ncmDialBkUpInfoEntry,
       "ncmDialBkUpInfoNIDIndex": ncmDialBkUpInfoNIDIndex,
       "ncmDialBkUpReqCircName": ncmDialBkUpReqCircName,
       "ncmPrimaryCircName": ncmPrimaryCircName,
       "ncmBackupCircName": ncmBackupCircName,
       "ncmCallReferenceNumber": ncmCallReferenceNumber,
       "ncmCirSrcPortErrsetupMask": ncmCirSrcPortErrsetupMask,
       "ncmCirDstPortErrsetupMask": ncmCirDstPortErrsetupMask,
       "ncmCirErrClearanceMask": ncmCirErrClearanceMask,
       "ncmDialBkUpTimeout": ncmDialBkUpTimeout,
       "ncmDialBkUpAction": ncmDialBkUpAction,
       "ncmDialBkUpSetupStatus": ncmDialBkUpSetupStatus,
       "ncmClearCircuitGrpTable": ncmClearCircuitGrpTable,
       "ncmClearCircuitGrpEntry": ncmClearCircuitGrpEntry,
       "ncmClearCircuitGrpNIDIndex": ncmClearCircuitGrpNIDIndex,
       "ncmClearCircuitGrpName": ncmClearCircuitGrpName,
       "ncmClearCircuitGrpSite": ncmClearCircuitGrpSite,
       "ncmClearCircuitCardEquipID": ncmClearCircuitCardEquipID,
       "ncmClearCircuitPortID": ncmClearCircuitPortID,
       "ncmClearCircuitAction": ncmClearCircuitAction,
       "ncmListGetMsgNumTable": ncmListGetMsgNumTable,
       "ncmListGetMsgNumEntry": ncmListGetMsgNumEntry,
       "ncmListMsgNumNIDIndex": ncmListMsgNumNIDIndex,
       "ncmListMsgNumCircuitGroup": ncmListMsgNumCircuitGroup,
       "ncmListMsgNumPageNumber": ncmListMsgNumPageNumber,
       "ncmListMsgNumCardSite": ncmListMsgNumCardSite,
       "ncmListMsgNumCardEquipID": ncmListMsgNumCardEquipID,
       "ncmListMsgNumPortID": ncmListMsgNumPortID,
       "ncmNumofGetListMessage": ncmNumofGetListMessage,
       "ncmTotalCircDatabase": ncmTotalCircDatabase,
       "ncmCircListccbTable": ncmCircListccbTable,
       "ncmCircListccbEntry": ncmCircListccbEntry,
       "ncmListccbNIDIndex": ncmListccbNIDIndex,
       "ncmNumofCircListMessage": ncmNumofCircListMessage,
       "ncmListccbCircName": ncmListccbCircName,
       "ncmListccbCircPriority": ncmListccbCircPriority,
       "ncmListccbCircType": ncmListccbCircType,
       "ncmListccbCircMode": ncmListccbCircMode,
       "ncmSrcPortSite": ncmSrcPortSite,
       "ncmSrcCardEquipID": ncmSrcCardEquipID,
       "ncmSrcPortIdentifier": ncmSrcPortIdentifier,
       "ncmSrcTimeslotmap": ncmSrcTimeslotmap,
       "ncmDstPortSite": ncmDstPortSite,
       "ncmDstCardEquipID": ncmDstCardEquipID,
       "ncmDstPortIdentifier": ncmDstPortIdentifier,
       "ncmDstTimeslotmap": ncmDstTimeslotmap,
       "ncmListccbBackPlaneBusID": ncmListccbBackPlaneBusID,
       "ncmListccbCircStatus": ncmListccbCircStatus,
       "ncmEquipmentIDTable": ncmEquipmentIDTable,
       "ncmEquipmentIDEntry": ncmEquipmentIDEntry,
       "ncmEquipmentIDNIDIndex": ncmEquipmentIDNIDIndex,
       "ncmEquipmentIDLineIndex": ncmEquipmentIDLineIndex,
       "ncmFirmwareVersion": ncmFirmwareVersion,
       "ncmFirmwareRevision": ncmFirmwareRevision,
       "ncmEquipmentType": ncmEquipmentType,
       "ncmHardwareVersion": ncmHardwareVersion,
       "ncmHardwareRevision": ncmHardwareRevision,
       "ncmLocationID": ncmLocationID,
       "ncmE1AlarmThresholdConfigTable": ncmE1AlarmThresholdConfigTable,
       "ncmE1AlarmThresholdConfigEntry": ncmE1AlarmThresholdConfigEntry,
       "ncmE1AlarmThresholdConfigNIDIndex": ncmE1AlarmThresholdConfigNIDIndex,
       "ncmE1AlarmThresholdConfigIndex": ncmE1AlarmThresholdConfigIndex,
       "ncmE1LOFThreshold": ncmE1LOFThreshold,
       "ncmE1LOFTimeInterval": ncmE1LOFTimeInterval,
       "ncmE1LOSThreshold": ncmE1LOSThreshold,
       "ncmE1LOSTimeInterval": ncmE1LOSTimeInterval,
       "ncmE1RAIThreshold": ncmE1RAIThreshold,
       "ncmE1RAITimeInterval": ncmE1RAITimeInterval,
       "ncmE1AISThreshold": ncmE1AISThreshold,
       "ncmE1AISTimeInterval": ncmE1AISTimeInterval,
       "ncmE1BPVThreshold": ncmE1BPVThreshold,
       "ncmE1BPVTimeInterval": ncmE1BPVTimeInterval,
       "ncmE1ES15MINThreshold": ncmE1ES15MINThreshold,
       "ncmE1ES24HRThreshold": ncmE1ES24HRThreshold,
       "ncmE1SES15MINThreshold": ncmE1SES15MINThreshold,
       "ncmE1SES24HRThreshold": ncmE1SES24HRThreshold,
       "ncmCVP15MINThreshold": ncmCVP15MINThreshold,
       "ncmCVP24HRThreshold": ncmCVP24HRThreshold,
       "ncmCVL15MINThreshold": ncmCVL15MINThreshold,
       "ncmCVL24HRThreshold": ncmCVL24HRThreshold,
       "ncmESL15MINThreshold": ncmESL15MINThreshold,
       "ncmESL24HRThreshold": ncmESL24HRThreshold,
       "ncmSESL15MINThreshold": ncmSESL15MINThreshold,
       "ncmSESL24HRThreshold": ncmSESL24HRThreshold,
       "ncmUASP15MINThreshold": ncmUASP15MINThreshold,
       "ncmUASP24HRThreshold": ncmUASP24HRThreshold,
       "ncmE1AlarmThresholdStatusTable": ncmE1AlarmThresholdStatusTable,
       "ncmE1AlarmThresholdStatusEntry": ncmE1AlarmThresholdStatusEntry,
       "ncmE1AlarmThresholdStatusNIDIndex": ncmE1AlarmThresholdStatusNIDIndex,
       "ncmE1AlarmThresholdStatusIndex": ncmE1AlarmThresholdStatusIndex,
       "ncmLOFExceededE1": ncmLOFExceededE1,
       "ncmLOSExceededE1": ncmLOSExceededE1,
       "ncmRAIExceededE1": ncmRAIExceededE1,
       "ncmAISExceededE1": ncmAISExceededE1,
       "ncmBPVExceededE1": ncmBPVExceededE1,
       "ncmES15MINExceeded": ncmES15MINExceeded,
       "ncmES24HRExceeded": ncmES24HRExceeded,
       "ncmSES15MINExceeded": ncmSES15MINExceeded,
       "ncmSES24HRExceeded": ncmSES24HRExceeded,
       "ncmCVP15MINExceeded": ncmCVP15MINExceeded,
       "ncmCVP24HRExceeded": ncmCVP24HRExceeded,
       "ncmCVL15MINExceeded": ncmCVL15MINExceeded,
       "ncmCVL24HRExceeded": ncmCVL24HRExceeded,
       "ncmESL15MINExceeded": ncmESL15MINExceeded,
       "ncmESL24HRExceeded": ncmESL24HRExceeded,
       "ncmSESL15MINExceeded": ncmSESL15MINExceeded,
       "ncmSESL24HRExceeded": ncmSESL24HRExceeded,
       "ncmUASP15MINExceeded": ncmUASP15MINExceeded,
       "ncmUASP24HRExceeded": ncmUASP24HRExceeded,
       "ncmLOFThresholdCount": ncmLOFThresholdCount,
       "ncmLOFTimeIntervals": ncmLOFTimeIntervals,
       "ncmLOSThresholdCount": ncmLOSThresholdCount,
       "ncmLOSTimeIntervals": ncmLOSTimeIntervals,
       "ncmRAIThresholdCount": ncmRAIThresholdCount,
       "ncmRAITimeIntervals": ncmRAITimeIntervals,
       "ncmAISThresholdCount": ncmAISThresholdCount,
       "ncmAISTimeIntervals": ncmAISTimeIntervals,
       "ncmBPVThresholdCount": ncmBPVThresholdCount,
       "ncmBPVTimeIntervals": ncmBPVTimeIntervals,
       "ncmES15MINThresholdCount": ncmES15MINThresholdCount,
       "ncmES24HRThresholdCount": ncmES24HRThresholdCount,
       "ncmSES15MINThresholdCount": ncmSES15MINThresholdCount,
       "ncmSES24HRThresholdCount": ncmSES24HRThresholdCount,
       "ncmCVP15MINThresholdCount": ncmCVP15MINThresholdCount,
       "ncmCVP24HRThresholdCount": ncmCVP24HRThresholdCount,
       "ncmCVL15MINThresholdCount": ncmCVL15MINThresholdCount,
       "ncmCVL24HRThresholdCount": ncmCVL24HRThresholdCount,
       "ncmESL15MINThresholdCount": ncmESL15MINThresholdCount,
       "ncmESL24HRThresholdCount": ncmESL24HRThresholdCount,
       "ncmSESL15MINThresholdCount": ncmSESL15MINThresholdCount,
       "ncmSESL24HRThresholdCount": ncmSESL24HRThresholdCount,
       "ncmUASP15MINThresholdCount": ncmUASP15MINThresholdCount,
       "ncmUASP24HRThresholdCount": ncmUASP24HRThresholdCount,
       "ncmAlarmThresholdConfigTable": ncmAlarmThresholdConfigTable,
       "ncmAlarmThresholdConfigEntry": ncmAlarmThresholdConfigEntry,
       "ncmAlarmThresholdConfigNIDIndex": ncmAlarmThresholdConfigNIDIndex,
       "ncmAlarmThresholdConfigIndex": ncmAlarmThresholdConfigIndex,
       "ncmLOFThreshold": ncmLOFThreshold,
       "ncmLOFTimeInterval": ncmLOFTimeInterval,
       "ncmLOSThreshold": ncmLOSThreshold,
       "ncmLOSTimeInterval": ncmLOSTimeInterval,
       "ncmRAIThreshold": ncmRAIThreshold,
       "ncmRAITimeInterval": ncmRAITimeInterval,
       "ncmAISThreshold": ncmAISThreshold,
       "ncmAISTimeInterval": ncmAISTimeInterval,
       "ncmBPVThreshold": ncmBPVThreshold,
       "ncmBPVTimeInterval": ncmBPVTimeInterval,
       "ncmES15MINThreshold": ncmES15MINThreshold,
       "ncmES24HRThreshold": ncmES24HRThreshold,
       "ncmSES15MINThreshold": ncmSES15MINThreshold,
       "ncmSES24HRThreshold": ncmSES24HRThreshold,
       "ncmAlarmThresholdStatusTable": ncmAlarmThresholdStatusTable,
       "ncmAlarmThresholdStatusEntry": ncmAlarmThresholdStatusEntry,
       "ncmAlarmThresholdStatusNIDIndex": ncmAlarmThresholdStatusNIDIndex,
       "ncmAlarmThresholdStatusIndex": ncmAlarmThresholdStatusIndex,
       "ncmLOFExceeded": ncmLOFExceeded,
       "ncmLOSExceeded": ncmLOSExceeded,
       "ncmAISExceeded": ncmAISExceeded,
       "ncmRAIExceeded": ncmRAIExceeded,
       "ncmBPVExceeded": ncmBPVExceeded,
       "ncmESExceeded": ncmESExceeded,
       "ncmSESExceeded": ncmSESExceeded,
       "ncmLOFThresholdCountst": ncmLOFThresholdCountst,
       "ncmLOFTimeIntervalst": ncmLOFTimeIntervalst,
       "ncmLOSThresholdCountst": ncmLOSThresholdCountst,
       "ncmLOSTimeIntervalst": ncmLOSTimeIntervalst,
       "ncmRAIThresholdCountst": ncmRAIThresholdCountst,
       "ncmRAITimeIntervalst": ncmRAITimeIntervalst,
       "ncmAISThresholdCountst": ncmAISThresholdCountst,
       "ncmAISTimeIntervalst": ncmAISTimeIntervalst,
       "ncmBPVThresholdCountst": ncmBPVThresholdCountst,
       "ncmBPVTimeIntervalst": ncmBPVTimeIntervalst,
       "ncmES15MINThresholdCountst": ncmES15MINThresholdCountst,
       "ncmES24HRThresholdCountst": ncmES24HRThresholdCountst,
       "ncmSES15MINThresholdCountst": ncmSES15MINThresholdCountst,
       "ncmSES24HRThresholdCountst": ncmSES24HRThresholdCountst,
       "ncmResetAlmThresholdCount": ncmResetAlmThresholdCount,
       "ncmShelfSyncSourceSegTable": ncmShelfSyncSourceSegTable,
       "ncmShelfSyncSourceSegEntry": ncmShelfSyncSourceSegEntry,
       "ncmShelfSyncSegNIDIndex": ncmShelfSyncSegNIDIndex,
       "ncmShelfSyncSourceSegIndex": ncmShelfSyncSourceSegIndex,
       "ncmShelfSyncSourceSegNum": ncmShelfSyncSourceSegNum,
       "ncmShelfTypeSeg": ncmShelfTypeSeg,
       "ncmRefBusSeg": ncmRefBusSeg,
       "ncmSourceSegOneShelfNum": ncmSourceSegOneShelfNum,
       "ncmSourceSegOneCardNum": ncmSourceSegOneCardNum,
       "ncmSourceSegOneClockRef": ncmSourceSegOneClockRef,
       "ncmSourceSegAutoRestore1": ncmSourceSegAutoRestore1,
       "ncmSourceSegTwoShelfNum": ncmSourceSegTwoShelfNum,
       "ncmSourceSegTwoCardNum": ncmSourceSegTwoCardNum,
       "ncmSourceSegTwoClockRef": ncmSourceSegTwoClockRef,
       "ncmSourceSegAutoRestore2": ncmSourceSegAutoRestore2,
       "ncmSourceSegThreeShelfNum": ncmSourceSegThreeShelfNum,
       "ncmSourceSegThreeCardNum": ncmSourceSegThreeCardNum,
       "ncmSourceSegThreeClockRef": ncmSourceSegThreeClockRef,
       "ncmSourceSegAutoRestore3": ncmSourceSegAutoRestore3,
       "ncmShelfCurrentSyncSourceSeg": ncmShelfCurrentSyncSourceSeg}
)
