# SNMP MIB module (ACD-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:20 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

acdFilter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2)
)
acdFilter.setRevisions(
        ("2011-10-10 01:00",
         "2010-11-10 01:00",
         "2008-05-01 01:00",
         "2006-08-06 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcdFilterOperator(Integer32, TextualConvention):
    status = "current"
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
        *(("equalTo", 3),
          ("greaterThan", 2),
          ("lessThan", 1),
          ("range", 4))
    )



class AcdFilterVlanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("cvlan", 1),
          ("svlan", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AcdL2FilterTable_Object = MibTable
acdL2FilterTable = _AcdL2FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1)
)
if mibBuilder.loadTexts:
    acdL2FilterTable.setStatus("deprecated")
_AcdL2FilterEntry_Object = MibTableRow
acdL2FilterEntry = _AcdL2FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1)
)
acdL2FilterEntry.setIndexNames(
    (0, "ACD-FILTER-MIB", "acdL2FilterID"),
)
if mibBuilder.loadTexts:
    acdL2FilterEntry.setStatus("current")
_AcdL2FilterID_Type = Unsigned32
_AcdL2FilterID_Object = MibTableColumn
acdL2FilterID = _AcdL2FilterID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 1),
    _AcdL2FilterID_Type()
)
acdL2FilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdL2FilterID.setStatus("current")


class _AcdL2FilterName_Type(DisplayString):
    """Custom type acdL2FilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdL2FilterName_Type.__name__ = "DisplayString"
_AcdL2FilterName_Object = MibTableColumn
acdL2FilterName = _AcdL2FilterName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 2),
    _AcdL2FilterName_Type()
)
acdL2FilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterName.setStatus("current")


class _AcdL2FilterMacDstEn_Type(TruthValue):
    """Custom type acdL2FilterMacDstEn based on TruthValue"""


_AcdL2FilterMacDstEn_Object = MibTableColumn
acdL2FilterMacDstEn = _AcdL2FilterMacDstEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 3),
    _AcdL2FilterMacDstEn_Type()
)
acdL2FilterMacDstEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterMacDstEn.setStatus("current")


class _AcdL2FilterMacDst_Type(MacAddress):
    """Custom type acdL2FilterMacDst based on MacAddress"""
    defaultHexValue = "000000000000"


_AcdL2FilterMacDst_Object = MibTableColumn
acdL2FilterMacDst = _AcdL2FilterMacDst_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 4),
    _AcdL2FilterMacDst_Type()
)
acdL2FilterMacDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterMacDst.setStatus("current")


class _AcdL2FilterMacDstMask_Type(Unsigned32):
    """Custom type acdL2FilterMacDstMask based on Unsigned32"""
    defaultValue = 48

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_AcdL2FilterMacDstMask_Type.__name__ = "Unsigned32"
_AcdL2FilterMacDstMask_Object = MibTableColumn
acdL2FilterMacDstMask = _AcdL2FilterMacDstMask_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 5),
    _AcdL2FilterMacDstMask_Type()
)
acdL2FilterMacDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterMacDstMask.setStatus("current")


class _AcdL2FilterMacSrcEn_Type(TruthValue):
    """Custom type acdL2FilterMacSrcEn based on TruthValue"""


_AcdL2FilterMacSrcEn_Object = MibTableColumn
acdL2FilterMacSrcEn = _AcdL2FilterMacSrcEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 6),
    _AcdL2FilterMacSrcEn_Type()
)
acdL2FilterMacSrcEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterMacSrcEn.setStatus("current")


class _AcdL2FilterMacSrc_Type(MacAddress):
    """Custom type acdL2FilterMacSrc based on MacAddress"""
    defaultHexValue = "000000000000"


_AcdL2FilterMacSrc_Object = MibTableColumn
acdL2FilterMacSrc = _AcdL2FilterMacSrc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 7),
    _AcdL2FilterMacSrc_Type()
)
acdL2FilterMacSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterMacSrc.setStatus("current")


class _AcdL2FilterMacSrcMask_Type(Unsigned32):
    """Custom type acdL2FilterMacSrcMask based on Unsigned32"""
    defaultValue = 48

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_AcdL2FilterMacSrcMask_Type.__name__ = "Unsigned32"
_AcdL2FilterMacSrcMask_Object = MibTableColumn
acdL2FilterMacSrcMask = _AcdL2FilterMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 8),
    _AcdL2FilterMacSrcMask_Type()
)
acdL2FilterMacSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterMacSrcMask.setStatus("current")


class _AcdL2FilterEtypeEn_Type(TruthValue):
    """Custom type acdL2FilterEtypeEn based on TruthValue"""


_AcdL2FilterEtypeEn_Object = MibTableColumn
acdL2FilterEtypeEn = _AcdL2FilterEtypeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 9),
    _AcdL2FilterEtypeEn_Type()
)
acdL2FilterEtypeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterEtypeEn.setStatus("current")


class _AcdL2FilterEtype_Type(Unsigned32):
    """Custom type acdL2FilterEtype based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdL2FilterEtype_Type.__name__ = "Unsigned32"
_AcdL2FilterEtype_Object = MibTableColumn
acdL2FilterEtype = _AcdL2FilterEtype_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 10),
    _AcdL2FilterEtype_Type()
)
acdL2FilterEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterEtype.setStatus("current")


class _AcdL2FilterVlan1PriorEn_Type(TruthValue):
    """Custom type acdL2FilterVlan1PriorEn based on TruthValue"""


_AcdL2FilterVlan1PriorEn_Object = MibTableColumn
acdL2FilterVlan1PriorEn = _AcdL2FilterVlan1PriorEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 11),
    _AcdL2FilterVlan1PriorEn_Type()
)
acdL2FilterVlan1PriorEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan1PriorEn.setStatus("current")


class _AcdL2FilterVlan1Prior_Type(Unsigned32):
    """Custom type acdL2FilterVlan1Prior based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdL2FilterVlan1Prior_Type.__name__ = "Unsigned32"
_AcdL2FilterVlan1Prior_Object = MibTableColumn
acdL2FilterVlan1Prior = _AcdL2FilterVlan1Prior_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 12),
    _AcdL2FilterVlan1Prior_Type()
)
acdL2FilterVlan1Prior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan1Prior.setStatus("current")


class _AcdL2FilterVlan1CfiEn_Type(TruthValue):
    """Custom type acdL2FilterVlan1CfiEn based on TruthValue"""


_AcdL2FilterVlan1CfiEn_Object = MibTableColumn
acdL2FilterVlan1CfiEn = _AcdL2FilterVlan1CfiEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 13),
    _AcdL2FilterVlan1CfiEn_Type()
)
acdL2FilterVlan1CfiEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan1CfiEn.setStatus("current")


class _AcdL2FilterVlan1Cfi_Type(Unsigned32):
    """Custom type acdL2FilterVlan1Cfi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcdL2FilterVlan1Cfi_Type.__name__ = "Unsigned32"
_AcdL2FilterVlan1Cfi_Object = MibTableColumn
acdL2FilterVlan1Cfi = _AcdL2FilterVlan1Cfi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 14),
    _AcdL2FilterVlan1Cfi_Type()
)
acdL2FilterVlan1Cfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan1Cfi.setStatus("current")


class _AcdL2FilterVlan1IdEn_Type(TruthValue):
    """Custom type acdL2FilterVlan1IdEn based on TruthValue"""


_AcdL2FilterVlan1IdEn_Object = MibTableColumn
acdL2FilterVlan1IdEn = _AcdL2FilterVlan1IdEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 15),
    _AcdL2FilterVlan1IdEn_Type()
)
acdL2FilterVlan1IdEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan1IdEn.setStatus("current")


class _AcdL2FilterVlan1Id_Type(Unsigned32):
    """Custom type acdL2FilterVlan1Id based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdL2FilterVlan1Id_Type.__name__ = "Unsigned32"
_AcdL2FilterVlan1Id_Object = MibTableColumn
acdL2FilterVlan1Id = _AcdL2FilterVlan1Id_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 16),
    _AcdL2FilterVlan1Id_Type()
)
acdL2FilterVlan1Id.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan1Id.setStatus("current")


class _AcdL2FilterVlan2PriorEn_Type(TruthValue):
    """Custom type acdL2FilterVlan2PriorEn based on TruthValue"""


_AcdL2FilterVlan2PriorEn_Object = MibTableColumn
acdL2FilterVlan2PriorEn = _AcdL2FilterVlan2PriorEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 17),
    _AcdL2FilterVlan2PriorEn_Type()
)
acdL2FilterVlan2PriorEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan2PriorEn.setStatus("current")


class _AcdL2FilterVlan2Prior_Type(Unsigned32):
    """Custom type acdL2FilterVlan2Prior based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdL2FilterVlan2Prior_Type.__name__ = "Unsigned32"
_AcdL2FilterVlan2Prior_Object = MibTableColumn
acdL2FilterVlan2Prior = _AcdL2FilterVlan2Prior_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 18),
    _AcdL2FilterVlan2Prior_Type()
)
acdL2FilterVlan2Prior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan2Prior.setStatus("current")


class _AcdL2FilterVlan2CfiEn_Type(TruthValue):
    """Custom type acdL2FilterVlan2CfiEn based on TruthValue"""


_AcdL2FilterVlan2CfiEn_Object = MibTableColumn
acdL2FilterVlan2CfiEn = _AcdL2FilterVlan2CfiEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 19),
    _AcdL2FilterVlan2CfiEn_Type()
)
acdL2FilterVlan2CfiEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan2CfiEn.setStatus("current")


class _AcdL2FilterVlan2Cfi_Type(Unsigned32):
    """Custom type acdL2FilterVlan2Cfi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcdL2FilterVlan2Cfi_Type.__name__ = "Unsigned32"
_AcdL2FilterVlan2Cfi_Object = MibTableColumn
acdL2FilterVlan2Cfi = _AcdL2FilterVlan2Cfi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 20),
    _AcdL2FilterVlan2Cfi_Type()
)
acdL2FilterVlan2Cfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan2Cfi.setStatus("current")


class _AcdL2FilterVlan2IdEn_Type(TruthValue):
    """Custom type acdL2FilterVlan2IdEn based on TruthValue"""


_AcdL2FilterVlan2IdEn_Object = MibTableColumn
acdL2FilterVlan2IdEn = _AcdL2FilterVlan2IdEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 21),
    _AcdL2FilterVlan2IdEn_Type()
)
acdL2FilterVlan2IdEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan2IdEn.setStatus("current")


class _AcdL2FilterVlan2Id_Type(Unsigned32):
    """Custom type acdL2FilterVlan2Id based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4065),
    )


_AcdL2FilterVlan2Id_Type.__name__ = "Unsigned32"
_AcdL2FilterVlan2Id_Object = MibTableColumn
acdL2FilterVlan2Id = _AcdL2FilterVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 22),
    _AcdL2FilterVlan2Id_Type()
)
acdL2FilterVlan2Id.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterVlan2Id.setStatus("current")
_AcdL2FilterRowStatus_Type = RowStatus
_AcdL2FilterRowStatus_Object = MibTableColumn
acdL2FilterRowStatus = _AcdL2FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 1, 1, 23),
    _AcdL2FilterRowStatus_Type()
)
acdL2FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdL2FilterRowStatus.setStatus("current")
_AcdIPv4FilterTable_Object = MibTable
acdIPv4FilterTable = _AcdIPv4FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2)
)
if mibBuilder.loadTexts:
    acdIPv4FilterTable.setStatus("deprecated")
_AcdIPv4FilterEntry_Object = MibTableRow
acdIPv4FilterEntry = _AcdIPv4FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1)
)
acdIPv4FilterEntry.setIndexNames(
    (0, "ACD-FILTER-MIB", "acdIPv4FilterID"),
)
if mibBuilder.loadTexts:
    acdIPv4FilterEntry.setStatus("current")
_AcdIPv4FilterID_Type = Unsigned32
_AcdIPv4FilterID_Object = MibTableColumn
acdIPv4FilterID = _AcdIPv4FilterID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 1),
    _AcdIPv4FilterID_Type()
)
acdIPv4FilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdIPv4FilterID.setStatus("current")


class _AcdIPv4FilterName_Type(DisplayString):
    """Custom type acdIPv4FilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdIPv4FilterName_Type.__name__ = "DisplayString"
_AcdIPv4FilterName_Object = MibTableColumn
acdIPv4FilterName = _AcdIPv4FilterName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 2),
    _AcdIPv4FilterName_Type()
)
acdIPv4FilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterName.setStatus("current")


class _AcdIPv4FilterSrcEn_Type(TruthValue):
    """Custom type acdIPv4FilterSrcEn based on TruthValue"""


_AcdIPv4FilterSrcEn_Object = MibTableColumn
acdIPv4FilterSrcEn = _AcdIPv4FilterSrcEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 3),
    _AcdIPv4FilterSrcEn_Type()
)
acdIPv4FilterSrcEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterSrcEn.setStatus("current")


class _AcdIPv4FilterSrc_Type(IpAddress):
    """Custom type acdIPv4FilterSrc based on IpAddress"""
    defaultHexValue = "00000000"


_AcdIPv4FilterSrc_Object = MibTableColumn
acdIPv4FilterSrc = _AcdIPv4FilterSrc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 4),
    _AcdIPv4FilterSrc_Type()
)
acdIPv4FilterSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterSrc.setStatus("current")


class _AcdIPv4FilterSrcMask_Type(IpAddress):
    """Custom type acdIPv4FilterSrcMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AcdIPv4FilterSrcMask_Object = MibTableColumn
acdIPv4FilterSrcMask = _AcdIPv4FilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 5),
    _AcdIPv4FilterSrcMask_Type()
)
acdIPv4FilterSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterSrcMask.setStatus("current")


class _AcdIPv4FilterDstEn_Type(TruthValue):
    """Custom type acdIPv4FilterDstEn based on TruthValue"""


_AcdIPv4FilterDstEn_Object = MibTableColumn
acdIPv4FilterDstEn = _AcdIPv4FilterDstEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 6),
    _AcdIPv4FilterDstEn_Type()
)
acdIPv4FilterDstEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterDstEn.setStatus("current")


class _AcdIPv4FilterDst_Type(IpAddress):
    """Custom type acdIPv4FilterDst based on IpAddress"""
    defaultHexValue = "00000000"


_AcdIPv4FilterDst_Object = MibTableColumn
acdIPv4FilterDst = _AcdIPv4FilterDst_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 7),
    _AcdIPv4FilterDst_Type()
)
acdIPv4FilterDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterDst.setStatus("current")


class _AcdIPv4FilterDstMask_Type(IpAddress):
    """Custom type acdIPv4FilterDstMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AcdIPv4FilterDstMask_Object = MibTableColumn
acdIPv4FilterDstMask = _AcdIPv4FilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 8),
    _AcdIPv4FilterDstMask_Type()
)
acdIPv4FilterDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterDstMask.setStatus("current")


class _AcdIPv4FilterProtoEn_Type(TruthValue):
    """Custom type acdIPv4FilterProtoEn based on TruthValue"""


_AcdIPv4FilterProtoEn_Object = MibTableColumn
acdIPv4FilterProtoEn = _AcdIPv4FilterProtoEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 9),
    _AcdIPv4FilterProtoEn_Type()
)
acdIPv4FilterProtoEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterProtoEn.setStatus("current")


class _AcdIPv4FilterProto_Type(Unsigned32):
    """Custom type acdIPv4FilterProto based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcdIPv4FilterProto_Type.__name__ = "Unsigned32"
_AcdIPv4FilterProto_Object = MibTableColumn
acdIPv4FilterProto = _AcdIPv4FilterProto_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 10),
    _AcdIPv4FilterProto_Type()
)
acdIPv4FilterProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterProto.setStatus("current")


class _AcdIPv4FilterTTLEn_Type(TruthValue):
    """Custom type acdIPv4FilterTTLEn based on TruthValue"""


_AcdIPv4FilterTTLEn_Object = MibTableColumn
acdIPv4FilterTTLEn = _AcdIPv4FilterTTLEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 11),
    _AcdIPv4FilterTTLEn_Type()
)
acdIPv4FilterTTLEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterTTLEn.setStatus("current")


class _AcdIPv4FilterTTL_Type(Unsigned32):
    """Custom type acdIPv4FilterTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcdIPv4FilterTTL_Type.__name__ = "Unsigned32"
_AcdIPv4FilterTTL_Object = MibTableColumn
acdIPv4FilterTTL = _AcdIPv4FilterTTL_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 12),
    _AcdIPv4FilterTTL_Type()
)
acdIPv4FilterTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterTTL.setStatus("current")


class _AcdIPv4FilterIHLEn_Type(TruthValue):
    """Custom type acdIPv4FilterIHLEn based on TruthValue"""


_AcdIPv4FilterIHLEn_Object = MibTableColumn
acdIPv4FilterIHLEn = _AcdIPv4FilterIHLEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 13),
    _AcdIPv4FilterIHLEn_Type()
)
acdIPv4FilterIHLEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterIHLEn.setStatus("current")


class _AcdIPv4FilterIHL_Type(Unsigned32):
    """Custom type acdIPv4FilterIHL based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_AcdIPv4FilterIHL_Type.__name__ = "Unsigned32"
_AcdIPv4FilterIHL_Object = MibTableColumn
acdIPv4FilterIHL = _AcdIPv4FilterIHL_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 14),
    _AcdIPv4FilterIHL_Type()
)
acdIPv4FilterIHL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterIHL.setStatus("current")


class _AcdIPv4FilterDscpEn_Type(TruthValue):
    """Custom type acdIPv4FilterDscpEn based on TruthValue"""


_AcdIPv4FilterDscpEn_Object = MibTableColumn
acdIPv4FilterDscpEn = _AcdIPv4FilterDscpEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 15),
    _AcdIPv4FilterDscpEn_Type()
)
acdIPv4FilterDscpEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterDscpEn.setStatus("current")


class _AcdIPv4FilterDscp_Type(Unsigned32):
    """Custom type acdIPv4FilterDscp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdIPv4FilterDscp_Type.__name__ = "Unsigned32"
_AcdIPv4FilterDscp_Object = MibTableColumn
acdIPv4FilterDscp = _AcdIPv4FilterDscp_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 16),
    _AcdIPv4FilterDscp_Type()
)
acdIPv4FilterDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterDscp.setStatus("current")


class _AcdIPv4FilterECNEn_Type(TruthValue):
    """Custom type acdIPv4FilterECNEn based on TruthValue"""


_AcdIPv4FilterECNEn_Object = MibTableColumn
acdIPv4FilterECNEn = _AcdIPv4FilterECNEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 17),
    _AcdIPv4FilterECNEn_Type()
)
acdIPv4FilterECNEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterECNEn.setStatus("current")


class _AcdIPv4FilterECN_Type(Unsigned32):
    """Custom type acdIPv4FilterECN based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcdIPv4FilterECN_Type.__name__ = "Unsigned32"
_AcdIPv4FilterECN_Object = MibTableColumn
acdIPv4FilterECN = _AcdIPv4FilterECN_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 18),
    _AcdIPv4FilterECN_Type()
)
acdIPv4FilterECN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterECN.setStatus("current")


class _AcdIPv4FilterSrcPortEn_Type(TruthValue):
    """Custom type acdIPv4FilterSrcPortEn based on TruthValue"""


_AcdIPv4FilterSrcPortEn_Object = MibTableColumn
acdIPv4FilterSrcPortEn = _AcdIPv4FilterSrcPortEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 19),
    _AcdIPv4FilterSrcPortEn_Type()
)
acdIPv4FilterSrcPortEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterSrcPortEn.setStatus("current")


class _AcdIPv4FilterSrcPort_Type(Unsigned32):
    """Custom type acdIPv4FilterSrcPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdIPv4FilterSrcPort_Type.__name__ = "Unsigned32"
_AcdIPv4FilterSrcPort_Object = MibTableColumn
acdIPv4FilterSrcPort = _AcdIPv4FilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 20),
    _AcdIPv4FilterSrcPort_Type()
)
acdIPv4FilterSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterSrcPort.setStatus("current")


class _AcdIPv4FilterDstPortEn_Type(TruthValue):
    """Custom type acdIPv4FilterDstPortEn based on TruthValue"""


_AcdIPv4FilterDstPortEn_Object = MibTableColumn
acdIPv4FilterDstPortEn = _AcdIPv4FilterDstPortEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 21),
    _AcdIPv4FilterDstPortEn_Type()
)
acdIPv4FilterDstPortEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterDstPortEn.setStatus("current")


class _AcdIPv4FilterDstPort_Type(Unsigned32):
    """Custom type acdIPv4FilterDstPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdIPv4FilterDstPort_Type.__name__ = "Unsigned32"
_AcdIPv4FilterDstPort_Object = MibTableColumn
acdIPv4FilterDstPort = _AcdIPv4FilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 22),
    _AcdIPv4FilterDstPort_Type()
)
acdIPv4FilterDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterDstPort.setStatus("current")


class _AcdIPv4FilterIcmpTypeEn_Type(TruthValue):
    """Custom type acdIPv4FilterIcmpTypeEn based on TruthValue"""


_AcdIPv4FilterIcmpTypeEn_Object = MibTableColumn
acdIPv4FilterIcmpTypeEn = _AcdIPv4FilterIcmpTypeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 23),
    _AcdIPv4FilterIcmpTypeEn_Type()
)
acdIPv4FilterIcmpTypeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterIcmpTypeEn.setStatus("current")


class _AcdIPv4FilterIcmpType_Type(Unsigned32):
    """Custom type acdIPv4FilterIcmpType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcdIPv4FilterIcmpType_Type.__name__ = "Unsigned32"
_AcdIPv4FilterIcmpType_Object = MibTableColumn
acdIPv4FilterIcmpType = _AcdIPv4FilterIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 24),
    _AcdIPv4FilterIcmpType_Type()
)
acdIPv4FilterIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterIcmpType.setStatus("current")


class _AcdIPv4FilterIcmpCodeEn_Type(TruthValue):
    """Custom type acdIPv4FilterIcmpCodeEn based on TruthValue"""


_AcdIPv4FilterIcmpCodeEn_Object = MibTableColumn
acdIPv4FilterIcmpCodeEn = _AcdIPv4FilterIcmpCodeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 25),
    _AcdIPv4FilterIcmpCodeEn_Type()
)
acdIPv4FilterIcmpCodeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterIcmpCodeEn.setStatus("current")


class _AcdIPv4FilterIcmpCode_Type(Unsigned32):
    """Custom type acdIPv4FilterIcmpCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcdIPv4FilterIcmpCode_Type.__name__ = "Unsigned32"
_AcdIPv4FilterIcmpCode_Object = MibTableColumn
acdIPv4FilterIcmpCode = _AcdIPv4FilterIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 26),
    _AcdIPv4FilterIcmpCode_Type()
)
acdIPv4FilterIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterIcmpCode.setStatus("current")
_AcdIPv4FilterRowStatus_Type = RowStatus
_AcdIPv4FilterRowStatus_Object = MibTableColumn
acdIPv4FilterRowStatus = _AcdIPv4FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 2, 1, 27),
    _AcdIPv4FilterRowStatus_Type()
)
acdIPv4FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdIPv4FilterRowStatus.setStatus("current")
_AcdSmapL2FilterTable_Object = MibTable
acdSmapL2FilterTable = _AcdSmapL2FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3)
)
if mibBuilder.loadTexts:
    acdSmapL2FilterTable.setStatus("current")
_AcdSmapL2FilterEntry_Object = MibTableRow
acdSmapL2FilterEntry = _AcdSmapL2FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1)
)
acdSmapL2FilterEntry.setIndexNames(
    (0, "ACD-FILTER-MIB", "acdSmapL2FilterID"),
)
if mibBuilder.loadTexts:
    acdSmapL2FilterEntry.setStatus("current")
_AcdSmapL2FilterID_Type = Unsigned32
_AcdSmapL2FilterID_Object = MibTableColumn
acdSmapL2FilterID = _AcdSmapL2FilterID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 1),
    _AcdSmapL2FilterID_Type()
)
acdSmapL2FilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapL2FilterID.setStatus("current")


class _AcdSmapL2FilterName_Type(DisplayString):
    """Custom type acdSmapL2FilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSmapL2FilterName_Type.__name__ = "DisplayString"
_AcdSmapL2FilterName_Object = MibTableColumn
acdSmapL2FilterName = _AcdSmapL2FilterName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 2),
    _AcdSmapL2FilterName_Type()
)
acdSmapL2FilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterName.setStatus("current")
_AcdSmapL2FilterRowStatus_Type = RowStatus
_AcdSmapL2FilterRowStatus_Object = MibTableColumn
acdSmapL2FilterRowStatus = _AcdSmapL2FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 3),
    _AcdSmapL2FilterRowStatus_Type()
)
acdSmapL2FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterRowStatus.setStatus("current")


class _AcdSmapL2FilterVlan1PriorEn_Type(TruthValue):
    """Custom type acdSmapL2FilterVlan1PriorEn based on TruthValue"""


_AcdSmapL2FilterVlan1PriorEn_Object = MibTableColumn
acdSmapL2FilterVlan1PriorEn = _AcdSmapL2FilterVlan1PriorEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 4),
    _AcdSmapL2FilterVlan1PriorEn_Type()
)
acdSmapL2FilterVlan1PriorEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1PriorEn.setStatus("current")


class _AcdSmapL2FilterVlan1Prior_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan1Prior based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapL2FilterVlan1Prior_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan1Prior_Object = MibTableColumn
acdSmapL2FilterVlan1Prior = _AcdSmapL2FilterVlan1Prior_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 5),
    _AcdSmapL2FilterVlan1Prior_Type()
)
acdSmapL2FilterVlan1Prior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1Prior.setStatus("current")


class _AcdSmapL2FilterVlan1PriorLast_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan1PriorLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapL2FilterVlan1PriorLast_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan1PriorLast_Object = MibTableColumn
acdSmapL2FilterVlan1PriorLast = _AcdSmapL2FilterVlan1PriorLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 6),
    _AcdSmapL2FilterVlan1PriorLast_Type()
)
acdSmapL2FilterVlan1PriorLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1PriorLast.setStatus("current")


class _AcdSmapL2FilterVlan1PriorOper_Type(AcdFilterOperator):
    """Custom type acdSmapL2FilterVlan1PriorOper based on AcdFilterOperator"""


_AcdSmapL2FilterVlan1PriorOper_Object = MibTableColumn
acdSmapL2FilterVlan1PriorOper = _AcdSmapL2FilterVlan1PriorOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 7),
    _AcdSmapL2FilterVlan1PriorOper_Type()
)
acdSmapL2FilterVlan1PriorOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1PriorOper.setStatus("current")


class _AcdSmapL2FilterVlan1IdEn_Type(TruthValue):
    """Custom type acdSmapL2FilterVlan1IdEn based on TruthValue"""


_AcdSmapL2FilterVlan1IdEn_Object = MibTableColumn
acdSmapL2FilterVlan1IdEn = _AcdSmapL2FilterVlan1IdEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 8),
    _AcdSmapL2FilterVlan1IdEn_Type()
)
acdSmapL2FilterVlan1IdEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1IdEn.setStatus("current")


class _AcdSmapL2FilterVlan1Id_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan1Id based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdSmapL2FilterVlan1Id_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan1Id_Object = MibTableColumn
acdSmapL2FilterVlan1Id = _AcdSmapL2FilterVlan1Id_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 9),
    _AcdSmapL2FilterVlan1Id_Type()
)
acdSmapL2FilterVlan1Id.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1Id.setStatus("current")


class _AcdSmapL2FilterVlan1IdLast_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan1IdLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdSmapL2FilterVlan1IdLast_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan1IdLast_Object = MibTableColumn
acdSmapL2FilterVlan1IdLast = _AcdSmapL2FilterVlan1IdLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 10),
    _AcdSmapL2FilterVlan1IdLast_Type()
)
acdSmapL2FilterVlan1IdLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1IdLast.setStatus("current")


class _AcdSmapL2FilterVlan1IdOper_Type(AcdFilterOperator):
    """Custom type acdSmapL2FilterVlan1IdOper based on AcdFilterOperator"""


_AcdSmapL2FilterVlan1IdOper_Object = MibTableColumn
acdSmapL2FilterVlan1IdOper = _AcdSmapL2FilterVlan1IdOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 11),
    _AcdSmapL2FilterVlan1IdOper_Type()
)
acdSmapL2FilterVlan1IdOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1IdOper.setStatus("current")


class _AcdSmapL2FilterVlan1CfiEn_Type(TruthValue):
    """Custom type acdSmapL2FilterVlan1CfiEn based on TruthValue"""


_AcdSmapL2FilterVlan1CfiEn_Object = MibTableColumn
acdSmapL2FilterVlan1CfiEn = _AcdSmapL2FilterVlan1CfiEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 12),
    _AcdSmapL2FilterVlan1CfiEn_Type()
)
acdSmapL2FilterVlan1CfiEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1CfiEn.setStatus("current")


class _AcdSmapL2FilterVlan1Cfi_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan1Cfi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcdSmapL2FilterVlan1Cfi_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan1Cfi_Object = MibTableColumn
acdSmapL2FilterVlan1Cfi = _AcdSmapL2FilterVlan1Cfi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 13),
    _AcdSmapL2FilterVlan1Cfi_Type()
)
acdSmapL2FilterVlan1Cfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1Cfi.setStatus("current")


class _AcdSmapL2FilterVlan1TypeEn_Type(TruthValue):
    """Custom type acdSmapL2FilterVlan1TypeEn based on TruthValue"""


_AcdSmapL2FilterVlan1TypeEn_Object = MibTableColumn
acdSmapL2FilterVlan1TypeEn = _AcdSmapL2FilterVlan1TypeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 14),
    _AcdSmapL2FilterVlan1TypeEn_Type()
)
acdSmapL2FilterVlan1TypeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1TypeEn.setStatus("current")


class _AcdSmapL2FilterVlan1Type_Type(AcdFilterVlanType):
    """Custom type acdSmapL2FilterVlan1Type based on AcdFilterVlanType"""


_AcdSmapL2FilterVlan1Type_Object = MibTableColumn
acdSmapL2FilterVlan1Type = _AcdSmapL2FilterVlan1Type_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 15),
    _AcdSmapL2FilterVlan1Type_Type()
)
acdSmapL2FilterVlan1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan1Type.setStatus("current")


class _AcdSmapL2FilterVlan2PriorEn_Type(TruthValue):
    """Custom type acdSmapL2FilterVlan2PriorEn based on TruthValue"""


_AcdSmapL2FilterVlan2PriorEn_Object = MibTableColumn
acdSmapL2FilterVlan2PriorEn = _AcdSmapL2FilterVlan2PriorEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 16),
    _AcdSmapL2FilterVlan2PriorEn_Type()
)
acdSmapL2FilterVlan2PriorEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2PriorEn.setStatus("current")


class _AcdSmapL2FilterVlan2Prior_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan2Prior based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapL2FilterVlan2Prior_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan2Prior_Object = MibTableColumn
acdSmapL2FilterVlan2Prior = _AcdSmapL2FilterVlan2Prior_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 17),
    _AcdSmapL2FilterVlan2Prior_Type()
)
acdSmapL2FilterVlan2Prior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2Prior.setStatus("current")


class _AcdSmapL2FilterVlan2PriorLast_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan2PriorLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapL2FilterVlan2PriorLast_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan2PriorLast_Object = MibTableColumn
acdSmapL2FilterVlan2PriorLast = _AcdSmapL2FilterVlan2PriorLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 18),
    _AcdSmapL2FilterVlan2PriorLast_Type()
)
acdSmapL2FilterVlan2PriorLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2PriorLast.setStatus("current")


class _AcdSmapL2FilterVlan2PriorOper_Type(AcdFilterOperator):
    """Custom type acdSmapL2FilterVlan2PriorOper based on AcdFilterOperator"""


_AcdSmapL2FilterVlan2PriorOper_Object = MibTableColumn
acdSmapL2FilterVlan2PriorOper = _AcdSmapL2FilterVlan2PriorOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 19),
    _AcdSmapL2FilterVlan2PriorOper_Type()
)
acdSmapL2FilterVlan2PriorOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2PriorOper.setStatus("current")


class _AcdSmapL2FilterVlan2IdEn_Type(TruthValue):
    """Custom type acdSmapL2FilterVlan2IdEn based on TruthValue"""


_AcdSmapL2FilterVlan2IdEn_Object = MibTableColumn
acdSmapL2FilterVlan2IdEn = _AcdSmapL2FilterVlan2IdEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 20),
    _AcdSmapL2FilterVlan2IdEn_Type()
)
acdSmapL2FilterVlan2IdEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2IdEn.setStatus("current")


class _AcdSmapL2FilterVlan2Id_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan2Id based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdSmapL2FilterVlan2Id_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan2Id_Object = MibTableColumn
acdSmapL2FilterVlan2Id = _AcdSmapL2FilterVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 21),
    _AcdSmapL2FilterVlan2Id_Type()
)
acdSmapL2FilterVlan2Id.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2Id.setStatus("current")


class _AcdSmapL2FilterVlan2IdLast_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan2IdLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdSmapL2FilterVlan2IdLast_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan2IdLast_Object = MibTableColumn
acdSmapL2FilterVlan2IdLast = _AcdSmapL2FilterVlan2IdLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 22),
    _AcdSmapL2FilterVlan2IdLast_Type()
)
acdSmapL2FilterVlan2IdLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2IdLast.setStatus("current")


class _AcdSmapL2FilterVlan2IdOper_Type(AcdFilterOperator):
    """Custom type acdSmapL2FilterVlan2IdOper based on AcdFilterOperator"""


_AcdSmapL2FilterVlan2IdOper_Object = MibTableColumn
acdSmapL2FilterVlan2IdOper = _AcdSmapL2FilterVlan2IdOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 23),
    _AcdSmapL2FilterVlan2IdOper_Type()
)
acdSmapL2FilterVlan2IdOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2IdOper.setStatus("current")


class _AcdSmapL2FilterVlan2CfiEn_Type(TruthValue):
    """Custom type acdSmapL2FilterVlan2CfiEn based on TruthValue"""


_AcdSmapL2FilterVlan2CfiEn_Object = MibTableColumn
acdSmapL2FilterVlan2CfiEn = _AcdSmapL2FilterVlan2CfiEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 24),
    _AcdSmapL2FilterVlan2CfiEn_Type()
)
acdSmapL2FilterVlan2CfiEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2CfiEn.setStatus("current")


class _AcdSmapL2FilterVlan2Cfi_Type(Unsigned32):
    """Custom type acdSmapL2FilterVlan2Cfi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcdSmapL2FilterVlan2Cfi_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterVlan2Cfi_Object = MibTableColumn
acdSmapL2FilterVlan2Cfi = _AcdSmapL2FilterVlan2Cfi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 25),
    _AcdSmapL2FilterVlan2Cfi_Type()
)
acdSmapL2FilterVlan2Cfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2Cfi.setStatus("current")


class _AcdSmapL2FilterVlan2TypeEn_Type(TruthValue):
    """Custom type acdSmapL2FilterVlan2TypeEn based on TruthValue"""


_AcdSmapL2FilterVlan2TypeEn_Object = MibTableColumn
acdSmapL2FilterVlan2TypeEn = _AcdSmapL2FilterVlan2TypeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 26),
    _AcdSmapL2FilterVlan2TypeEn_Type()
)
acdSmapL2FilterVlan2TypeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2TypeEn.setStatus("current")


class _AcdSmapL2FilterVlan2Type_Type(AcdFilterVlanType):
    """Custom type acdSmapL2FilterVlan2Type based on AcdFilterVlanType"""


_AcdSmapL2FilterVlan2Type_Object = MibTableColumn
acdSmapL2FilterVlan2Type = _AcdSmapL2FilterVlan2Type_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 27),
    _AcdSmapL2FilterVlan2Type_Type()
)
acdSmapL2FilterVlan2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterVlan2Type.setStatus("current")


class _AcdSmapL2FilterMacDstEn_Type(TruthValue):
    """Custom type acdSmapL2FilterMacDstEn based on TruthValue"""


_AcdSmapL2FilterMacDstEn_Object = MibTableColumn
acdSmapL2FilterMacDstEn = _AcdSmapL2FilterMacDstEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 28),
    _AcdSmapL2FilterMacDstEn_Type()
)
acdSmapL2FilterMacDstEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterMacDstEn.setStatus("current")


class _AcdSmapL2FilterMacDst_Type(MacAddress):
    """Custom type acdSmapL2FilterMacDst based on MacAddress"""
    defaultHexValue = "000000000000"


_AcdSmapL2FilterMacDst_Object = MibTableColumn
acdSmapL2FilterMacDst = _AcdSmapL2FilterMacDst_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 29),
    _AcdSmapL2FilterMacDst_Type()
)
acdSmapL2FilterMacDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterMacDst.setStatus("current")


class _AcdSmapL2FilterMacDstMask_Type(Unsigned32):
    """Custom type acdSmapL2FilterMacDstMask based on Unsigned32"""
    defaultValue = 48


_AcdSmapL2FilterMacDstMask_Object = MibTableColumn
acdSmapL2FilterMacDstMask = _AcdSmapL2FilterMacDstMask_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 30),
    _AcdSmapL2FilterMacDstMask_Type()
)
acdSmapL2FilterMacDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterMacDstMask.setStatus("current")


class _AcdSmapL2FilterMacSrcEn_Type(TruthValue):
    """Custom type acdSmapL2FilterMacSrcEn based on TruthValue"""


_AcdSmapL2FilterMacSrcEn_Object = MibTableColumn
acdSmapL2FilterMacSrcEn = _AcdSmapL2FilterMacSrcEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 31),
    _AcdSmapL2FilterMacSrcEn_Type()
)
acdSmapL2FilterMacSrcEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterMacSrcEn.setStatus("current")


class _AcdSmapL2FilterMacSrc_Type(MacAddress):
    """Custom type acdSmapL2FilterMacSrc based on MacAddress"""
    defaultHexValue = "000000000000"


_AcdSmapL2FilterMacSrc_Object = MibTableColumn
acdSmapL2FilterMacSrc = _AcdSmapL2FilterMacSrc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 32),
    _AcdSmapL2FilterMacSrc_Type()
)
acdSmapL2FilterMacSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterMacSrc.setStatus("current")


class _AcdSmapL2FilterMacSrcMask_Type(Unsigned32):
    """Custom type acdSmapL2FilterMacSrcMask based on Unsigned32"""
    defaultValue = 48


_AcdSmapL2FilterMacSrcMask_Object = MibTableColumn
acdSmapL2FilterMacSrcMask = _AcdSmapL2FilterMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 33),
    _AcdSmapL2FilterMacSrcMask_Type()
)
acdSmapL2FilterMacSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterMacSrcMask.setStatus("current")


class _AcdSmapL2FilterEtypeEn_Type(TruthValue):
    """Custom type acdSmapL2FilterEtypeEn based on TruthValue"""


_AcdSmapL2FilterEtypeEn_Object = MibTableColumn
acdSmapL2FilterEtypeEn = _AcdSmapL2FilterEtypeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 34),
    _AcdSmapL2FilterEtypeEn_Type()
)
acdSmapL2FilterEtypeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterEtypeEn.setStatus("current")


class _AcdSmapL2FilterEtype_Type(Unsigned32):
    """Custom type acdSmapL2FilterEtype based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdSmapL2FilterEtype_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterEtype_Object = MibTableColumn
acdSmapL2FilterEtype = _AcdSmapL2FilterEtype_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 35),
    _AcdSmapL2FilterEtype_Type()
)
acdSmapL2FilterEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterEtype.setStatus("current")


class _AcdSmapL2FilterIpCosEn_Type(TruthValue):
    """Custom type acdSmapL2FilterIpCosEn based on TruthValue"""


_AcdSmapL2FilterIpCosEn_Object = MibTableColumn
acdSmapL2FilterIpCosEn = _AcdSmapL2FilterIpCosEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 36),
    _AcdSmapL2FilterIpCosEn_Type()
)
acdSmapL2FilterIpCosEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterIpCosEn.setStatus("current")


class _AcdSmapL2FilterIpCosMode_Type(Integer32):
    """Custom type acdSmapL2FilterIpCosMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 1),
          ("pre", 2))
    )


_AcdSmapL2FilterIpCosMode_Type.__name__ = "Integer32"
_AcdSmapL2FilterIpCosMode_Object = MibTableColumn
acdSmapL2FilterIpCosMode = _AcdSmapL2FilterIpCosMode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 37),
    _AcdSmapL2FilterIpCosMode_Type()
)
acdSmapL2FilterIpCosMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterIpCosMode.setStatus("current")


class _AcdSmapL2FilterDscp_Type(Unsigned32):
    """Custom type acdSmapL2FilterDscp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdSmapL2FilterDscp_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterDscp_Object = MibTableColumn
acdSmapL2FilterDscp = _AcdSmapL2FilterDscp_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 38),
    _AcdSmapL2FilterDscp_Type()
)
acdSmapL2FilterDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterDscp.setStatus("current")


class _AcdSmapL2FilterDscpLast_Type(Unsigned32):
    """Custom type acdSmapL2FilterDscpLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdSmapL2FilterDscpLast_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterDscpLast_Object = MibTableColumn
acdSmapL2FilterDscpLast = _AcdSmapL2FilterDscpLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 39),
    _AcdSmapL2FilterDscpLast_Type()
)
acdSmapL2FilterDscpLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterDscpLast.setStatus("current")


class _AcdSmapL2FilterDscpOper_Type(AcdFilterOperator):
    """Custom type acdSmapL2FilterDscpOper based on AcdFilterOperator"""


_AcdSmapL2FilterDscpOper_Object = MibTableColumn
acdSmapL2FilterDscpOper = _AcdSmapL2FilterDscpOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 40),
    _AcdSmapL2FilterDscpOper_Type()
)
acdSmapL2FilterDscpOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterDscpOper.setStatus("current")


class _AcdSmapL2FilterPre_Type(Unsigned32):
    """Custom type acdSmapL2FilterPre based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapL2FilterPre_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterPre_Object = MibTableColumn
acdSmapL2FilterPre = _AcdSmapL2FilterPre_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 41),
    _AcdSmapL2FilterPre_Type()
)
acdSmapL2FilterPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterPre.setStatus("current")


class _AcdSmapL2FilterPreLast_Type(Unsigned32):
    """Custom type acdSmapL2FilterPreLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapL2FilterPreLast_Type.__name__ = "Unsigned32"
_AcdSmapL2FilterPreLast_Object = MibTableColumn
acdSmapL2FilterPreLast = _AcdSmapL2FilterPreLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 42),
    _AcdSmapL2FilterPreLast_Type()
)
acdSmapL2FilterPreLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterPreLast.setStatus("current")


class _AcdSmapL2FilterPreOper_Type(AcdFilterOperator):
    """Custom type acdSmapL2FilterPreOper based on AcdFilterOperator"""


_AcdSmapL2FilterPreOper_Object = MibTableColumn
acdSmapL2FilterPreOper = _AcdSmapL2FilterPreOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 3, 1, 43),
    _AcdSmapL2FilterPreOper_Type()
)
acdSmapL2FilterPreOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapL2FilterPreOper.setStatus("current")
_AcdSmapIPv4FilterTable_Object = MibTable
acdSmapIPv4FilterTable = _AcdSmapIPv4FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4)
)
if mibBuilder.loadTexts:
    acdSmapIPv4FilterTable.setStatus("current")
_AcdSmapIPv4FilterEntry_Object = MibTableRow
acdSmapIPv4FilterEntry = _AcdSmapIPv4FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1)
)
acdSmapIPv4FilterEntry.setIndexNames(
    (0, "ACD-FILTER-MIB", "acdSmapIPv4FilterID"),
)
if mibBuilder.loadTexts:
    acdSmapIPv4FilterEntry.setStatus("current")
_AcdSmapIPv4FilterID_Type = Unsigned32
_AcdSmapIPv4FilterID_Object = MibTableColumn
acdSmapIPv4FilterID = _AcdSmapIPv4FilterID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 1),
    _AcdSmapIPv4FilterID_Type()
)
acdSmapIPv4FilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterID.setStatus("current")


class _AcdSmapIPv4FilterName_Type(DisplayString):
    """Custom type acdSmapIPv4FilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSmapIPv4FilterName_Type.__name__ = "DisplayString"
_AcdSmapIPv4FilterName_Object = MibTableColumn
acdSmapIPv4FilterName = _AcdSmapIPv4FilterName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 2),
    _AcdSmapIPv4FilterName_Type()
)
acdSmapIPv4FilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterName.setStatus("current")
_AcdSmapIPv4FilterRowStatus_Type = RowStatus
_AcdSmapIPv4FilterRowStatus_Object = MibTableColumn
acdSmapIPv4FilterRowStatus = _AcdSmapIPv4FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 3),
    _AcdSmapIPv4FilterRowStatus_Type()
)
acdSmapIPv4FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterRowStatus.setStatus("current")


class _AcdSmapIPv4FilterVlan1PriorEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterVlan1PriorEn based on TruthValue"""


_AcdSmapIPv4FilterVlan1PriorEn_Object = MibTableColumn
acdSmapIPv4FilterVlan1PriorEn = _AcdSmapIPv4FilterVlan1PriorEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 4),
    _AcdSmapIPv4FilterVlan1PriorEn_Type()
)
acdSmapIPv4FilterVlan1PriorEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1PriorEn.setStatus("current")


class _AcdSmapIPv4FilterVlan1Prior_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan1Prior based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapIPv4FilterVlan1Prior_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan1Prior_Object = MibTableColumn
acdSmapIPv4FilterVlan1Prior = _AcdSmapIPv4FilterVlan1Prior_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 5),
    _AcdSmapIPv4FilterVlan1Prior_Type()
)
acdSmapIPv4FilterVlan1Prior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1Prior.setStatus("current")


class _AcdSmapIPv4FilterVlan1PriorLast_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan1PriorLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapIPv4FilterVlan1PriorLast_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan1PriorLast_Object = MibTableColumn
acdSmapIPv4FilterVlan1PriorLast = _AcdSmapIPv4FilterVlan1PriorLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 6),
    _AcdSmapIPv4FilterVlan1PriorLast_Type()
)
acdSmapIPv4FilterVlan1PriorLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1PriorLast.setStatus("current")


class _AcdSmapIPv4FilterVlan1PriorOper_Type(AcdFilterOperator):
    """Custom type acdSmapIPv4FilterVlan1PriorOper based on AcdFilterOperator"""


_AcdSmapIPv4FilterVlan1PriorOper_Object = MibTableColumn
acdSmapIPv4FilterVlan1PriorOper = _AcdSmapIPv4FilterVlan1PriorOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 7),
    _AcdSmapIPv4FilterVlan1PriorOper_Type()
)
acdSmapIPv4FilterVlan1PriorOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1PriorOper.setStatus("current")


class _AcdSmapIPv4FilterVlan1IdEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterVlan1IdEn based on TruthValue"""


_AcdSmapIPv4FilterVlan1IdEn_Object = MibTableColumn
acdSmapIPv4FilterVlan1IdEn = _AcdSmapIPv4FilterVlan1IdEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 8),
    _AcdSmapIPv4FilterVlan1IdEn_Type()
)
acdSmapIPv4FilterVlan1IdEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1IdEn.setStatus("current")


class _AcdSmapIPv4FilterVlan1Id_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan1Id based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdSmapIPv4FilterVlan1Id_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan1Id_Object = MibTableColumn
acdSmapIPv4FilterVlan1Id = _AcdSmapIPv4FilterVlan1Id_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 9),
    _AcdSmapIPv4FilterVlan1Id_Type()
)
acdSmapIPv4FilterVlan1Id.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1Id.setStatus("current")


class _AcdSmapIPv4FilterVlan1IdLast_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan1IdLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdSmapIPv4FilterVlan1IdLast_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan1IdLast_Object = MibTableColumn
acdSmapIPv4FilterVlan1IdLast = _AcdSmapIPv4FilterVlan1IdLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 10),
    _AcdSmapIPv4FilterVlan1IdLast_Type()
)
acdSmapIPv4FilterVlan1IdLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1IdLast.setStatus("current")


class _AcdSmapIPv4FilterVlan1IdOper_Type(AcdFilterOperator):
    """Custom type acdSmapIPv4FilterVlan1IdOper based on AcdFilterOperator"""


_AcdSmapIPv4FilterVlan1IdOper_Object = MibTableColumn
acdSmapIPv4FilterVlan1IdOper = _AcdSmapIPv4FilterVlan1IdOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 11),
    _AcdSmapIPv4FilterVlan1IdOper_Type()
)
acdSmapIPv4FilterVlan1IdOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1IdOper.setStatus("current")


class _AcdSmapIPv4FilterVlan1CfiEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterVlan1CfiEn based on TruthValue"""


_AcdSmapIPv4FilterVlan1CfiEn_Object = MibTableColumn
acdSmapIPv4FilterVlan1CfiEn = _AcdSmapIPv4FilterVlan1CfiEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 12),
    _AcdSmapIPv4FilterVlan1CfiEn_Type()
)
acdSmapIPv4FilterVlan1CfiEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1CfiEn.setStatus("current")


class _AcdSmapIPv4FilterVlan1Cfi_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan1Cfi based on Unsigned32"""
    defaultValue = 0


_AcdSmapIPv4FilterVlan1Cfi_Object = MibTableColumn
acdSmapIPv4FilterVlan1Cfi = _AcdSmapIPv4FilterVlan1Cfi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 13),
    _AcdSmapIPv4FilterVlan1Cfi_Type()
)
acdSmapIPv4FilterVlan1Cfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1Cfi.setStatus("current")


class _AcdSmapIPv4FilterVlan1TypeEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterVlan1TypeEn based on TruthValue"""


_AcdSmapIPv4FilterVlan1TypeEn_Object = MibTableColumn
acdSmapIPv4FilterVlan1TypeEn = _AcdSmapIPv4FilterVlan1TypeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 14),
    _AcdSmapIPv4FilterVlan1TypeEn_Type()
)
acdSmapIPv4FilterVlan1TypeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1TypeEn.setStatus("current")


class _AcdSmapIPv4FilterVlan1Type_Type(AcdFilterVlanType):
    """Custom type acdSmapIPv4FilterVlan1Type based on AcdFilterVlanType"""


_AcdSmapIPv4FilterVlan1Type_Object = MibTableColumn
acdSmapIPv4FilterVlan1Type = _AcdSmapIPv4FilterVlan1Type_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 15),
    _AcdSmapIPv4FilterVlan1Type_Type()
)
acdSmapIPv4FilterVlan1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan1Type.setStatus("current")


class _AcdSmapIPv4FilterVlan2PriorEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterVlan2PriorEn based on TruthValue"""


_AcdSmapIPv4FilterVlan2PriorEn_Object = MibTableColumn
acdSmapIPv4FilterVlan2PriorEn = _AcdSmapIPv4FilterVlan2PriorEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 16),
    _AcdSmapIPv4FilterVlan2PriorEn_Type()
)
acdSmapIPv4FilterVlan2PriorEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2PriorEn.setStatus("current")


class _AcdSmapIPv4FilterVlan2Prior_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan2Prior based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapIPv4FilterVlan2Prior_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan2Prior_Object = MibTableColumn
acdSmapIPv4FilterVlan2Prior = _AcdSmapIPv4FilterVlan2Prior_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 17),
    _AcdSmapIPv4FilterVlan2Prior_Type()
)
acdSmapIPv4FilterVlan2Prior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2Prior.setStatus("current")


class _AcdSmapIPv4FilterVlan2PriorLast_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan2PriorLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapIPv4FilterVlan2PriorLast_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan2PriorLast_Object = MibTableColumn
acdSmapIPv4FilterVlan2PriorLast = _AcdSmapIPv4FilterVlan2PriorLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 18),
    _AcdSmapIPv4FilterVlan2PriorLast_Type()
)
acdSmapIPv4FilterVlan2PriorLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2PriorLast.setStatus("current")


class _AcdSmapIPv4FilterVlan2PriorOper_Type(AcdFilterOperator):
    """Custom type acdSmapIPv4FilterVlan2PriorOper based on AcdFilterOperator"""


_AcdSmapIPv4FilterVlan2PriorOper_Object = MibTableColumn
acdSmapIPv4FilterVlan2PriorOper = _AcdSmapIPv4FilterVlan2PriorOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 19),
    _AcdSmapIPv4FilterVlan2PriorOper_Type()
)
acdSmapIPv4FilterVlan2PriorOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2PriorOper.setStatus("current")


class _AcdSmapIPv4FilterVlan2IdEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterVlan2IdEn based on TruthValue"""


_AcdSmapIPv4FilterVlan2IdEn_Object = MibTableColumn
acdSmapIPv4FilterVlan2IdEn = _AcdSmapIPv4FilterVlan2IdEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 20),
    _AcdSmapIPv4FilterVlan2IdEn_Type()
)
acdSmapIPv4FilterVlan2IdEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2IdEn.setStatus("current")


class _AcdSmapIPv4FilterVlan2Id_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan2Id based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdSmapIPv4FilterVlan2Id_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan2Id_Object = MibTableColumn
acdSmapIPv4FilterVlan2Id = _AcdSmapIPv4FilterVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 21),
    _AcdSmapIPv4FilterVlan2Id_Type()
)
acdSmapIPv4FilterVlan2Id.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2Id.setStatus("current")


class _AcdSmapIPv4FilterVlan2IdLast_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan2IdLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdSmapIPv4FilterVlan2IdLast_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan2IdLast_Object = MibTableColumn
acdSmapIPv4FilterVlan2IdLast = _AcdSmapIPv4FilterVlan2IdLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 22),
    _AcdSmapIPv4FilterVlan2IdLast_Type()
)
acdSmapIPv4FilterVlan2IdLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2IdLast.setStatus("current")


class _AcdSmapIPv4FilterVlan2IdOper_Type(AcdFilterOperator):
    """Custom type acdSmapIPv4FilterVlan2IdOper based on AcdFilterOperator"""


_AcdSmapIPv4FilterVlan2IdOper_Object = MibTableColumn
acdSmapIPv4FilterVlan2IdOper = _AcdSmapIPv4FilterVlan2IdOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 23),
    _AcdSmapIPv4FilterVlan2IdOper_Type()
)
acdSmapIPv4FilterVlan2IdOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2IdOper.setStatus("current")


class _AcdSmapIPv4FilterVlan2CfiEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterVlan2CfiEn based on TruthValue"""


_AcdSmapIPv4FilterVlan2CfiEn_Object = MibTableColumn
acdSmapIPv4FilterVlan2CfiEn = _AcdSmapIPv4FilterVlan2CfiEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 24),
    _AcdSmapIPv4FilterVlan2CfiEn_Type()
)
acdSmapIPv4FilterVlan2CfiEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2CfiEn.setStatus("current")


class _AcdSmapIPv4FilterVlan2Cfi_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterVlan2Cfi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcdSmapIPv4FilterVlan2Cfi_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterVlan2Cfi_Object = MibTableColumn
acdSmapIPv4FilterVlan2Cfi = _AcdSmapIPv4FilterVlan2Cfi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 25),
    _AcdSmapIPv4FilterVlan2Cfi_Type()
)
acdSmapIPv4FilterVlan2Cfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2Cfi.setStatus("current")


class _AcdSmapIPv4FilterVlan2TypeEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterVlan2TypeEn based on TruthValue"""


_AcdSmapIPv4FilterVlan2TypeEn_Object = MibTableColumn
acdSmapIPv4FilterVlan2TypeEn = _AcdSmapIPv4FilterVlan2TypeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 26),
    _AcdSmapIPv4FilterVlan2TypeEn_Type()
)
acdSmapIPv4FilterVlan2TypeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2TypeEn.setStatus("current")


class _AcdSmapIPv4FilterVlan2Type_Type(AcdFilterVlanType):
    """Custom type acdSmapIPv4FilterVlan2Type based on AcdFilterVlanType"""


_AcdSmapIPv4FilterVlan2Type_Object = MibTableColumn
acdSmapIPv4FilterVlan2Type = _AcdSmapIPv4FilterVlan2Type_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 27),
    _AcdSmapIPv4FilterVlan2Type_Type()
)
acdSmapIPv4FilterVlan2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterVlan2Type.setStatus("current")


class _AcdSmapIPv4FilterSrcEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterSrcEn based on TruthValue"""


_AcdSmapIPv4FilterSrcEn_Object = MibTableColumn
acdSmapIPv4FilterSrcEn = _AcdSmapIPv4FilterSrcEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 28),
    _AcdSmapIPv4FilterSrcEn_Type()
)
acdSmapIPv4FilterSrcEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterSrcEn.setStatus("current")


class _AcdSmapIPv4FilterSrc_Type(IpAddress):
    """Custom type acdSmapIPv4FilterSrc based on IpAddress"""
    defaultHexValue = "00000000"


_AcdSmapIPv4FilterSrc_Object = MibTableColumn
acdSmapIPv4FilterSrc = _AcdSmapIPv4FilterSrc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 29),
    _AcdSmapIPv4FilterSrc_Type()
)
acdSmapIPv4FilterSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterSrc.setStatus("current")


class _AcdSmapIPv4FilterSrcMask_Type(IpAddress):
    """Custom type acdSmapIPv4FilterSrcMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AcdSmapIPv4FilterSrcMask_Object = MibTableColumn
acdSmapIPv4FilterSrcMask = _AcdSmapIPv4FilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 30),
    _AcdSmapIPv4FilterSrcMask_Type()
)
acdSmapIPv4FilterSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterSrcMask.setStatus("current")


class _AcdSmapIPv4FilterDstEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterDstEn based on TruthValue"""


_AcdSmapIPv4FilterDstEn_Object = MibTableColumn
acdSmapIPv4FilterDstEn = _AcdSmapIPv4FilterDstEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 31),
    _AcdSmapIPv4FilterDstEn_Type()
)
acdSmapIPv4FilterDstEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterDstEn.setStatus("current")


class _AcdSmapIPv4FilterDst_Type(IpAddress):
    """Custom type acdSmapIPv4FilterDst based on IpAddress"""
    defaultHexValue = "00000000"


_AcdSmapIPv4FilterDst_Object = MibTableColumn
acdSmapIPv4FilterDst = _AcdSmapIPv4FilterDst_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 32),
    _AcdSmapIPv4FilterDst_Type()
)
acdSmapIPv4FilterDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterDst.setStatus("current")


class _AcdSmapIPv4FilterDstMask_Type(IpAddress):
    """Custom type acdSmapIPv4FilterDstMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AcdSmapIPv4FilterDstMask_Object = MibTableColumn
acdSmapIPv4FilterDstMask = _AcdSmapIPv4FilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 33),
    _AcdSmapIPv4FilterDstMask_Type()
)
acdSmapIPv4FilterDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterDstMask.setStatus("current")


class _AcdSmapIPv4FilterProtoEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterProtoEn based on TruthValue"""


_AcdSmapIPv4FilterProtoEn_Object = MibTableColumn
acdSmapIPv4FilterProtoEn = _AcdSmapIPv4FilterProtoEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 34),
    _AcdSmapIPv4FilterProtoEn_Type()
)
acdSmapIPv4FilterProtoEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterProtoEn.setStatus("current")


class _AcdSmapIPv4FilterProto_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterProto based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcdSmapIPv4FilterProto_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterProto_Object = MibTableColumn
acdSmapIPv4FilterProto = _AcdSmapIPv4FilterProto_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 35),
    _AcdSmapIPv4FilterProto_Type()
)
acdSmapIPv4FilterProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterProto.setStatus("current")


class _AcdSmapIPv4FilterTTLEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterTTLEn based on TruthValue"""


_AcdSmapIPv4FilterTTLEn_Object = MibTableColumn
acdSmapIPv4FilterTTLEn = _AcdSmapIPv4FilterTTLEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 36),
    _AcdSmapIPv4FilterTTLEn_Type()
)
acdSmapIPv4FilterTTLEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterTTLEn.setStatus("current")


class _AcdSmapIPv4FilterTTL_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterTTL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcdSmapIPv4FilterTTL_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterTTL_Object = MibTableColumn
acdSmapIPv4FilterTTL = _AcdSmapIPv4FilterTTL_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 37),
    _AcdSmapIPv4FilterTTL_Type()
)
acdSmapIPv4FilterTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterTTL.setStatus("current")


class _AcdSmapIPv4FilterIHLEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterIHLEn based on TruthValue"""


_AcdSmapIPv4FilterIHLEn_Object = MibTableColumn
acdSmapIPv4FilterIHLEn = _AcdSmapIPv4FilterIHLEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 38),
    _AcdSmapIPv4FilterIHLEn_Type()
)
acdSmapIPv4FilterIHLEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterIHLEn.setStatus("current")


class _AcdSmapIPv4FilterIHL_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterIHL based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_AcdSmapIPv4FilterIHL_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterIHL_Object = MibTableColumn
acdSmapIPv4FilterIHL = _AcdSmapIPv4FilterIHL_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 39),
    _AcdSmapIPv4FilterIHL_Type()
)
acdSmapIPv4FilterIHL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterIHL.setStatus("current")


class _AcdSmapIPv4FilterIpCosEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterIpCosEn based on TruthValue"""


_AcdSmapIPv4FilterIpCosEn_Object = MibTableColumn
acdSmapIPv4FilterIpCosEn = _AcdSmapIPv4FilterIpCosEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 40),
    _AcdSmapIPv4FilterIpCosEn_Type()
)
acdSmapIPv4FilterIpCosEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterIpCosEn.setStatus("current")


class _AcdSmapIPv4FilterIpCosMode_Type(Integer32):
    """Custom type acdSmapIPv4FilterIpCosMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 1),
          ("pre", 2))
    )


_AcdSmapIPv4FilterIpCosMode_Type.__name__ = "Integer32"
_AcdSmapIPv4FilterIpCosMode_Object = MibTableColumn
acdSmapIPv4FilterIpCosMode = _AcdSmapIPv4FilterIpCosMode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 41),
    _AcdSmapIPv4FilterIpCosMode_Type()
)
acdSmapIPv4FilterIpCosMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterIpCosMode.setStatus("current")


class _AcdSmapIPv4FilterDscp_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterDscp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdSmapIPv4FilterDscp_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterDscp_Object = MibTableColumn
acdSmapIPv4FilterDscp = _AcdSmapIPv4FilterDscp_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 42),
    _AcdSmapIPv4FilterDscp_Type()
)
acdSmapIPv4FilterDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterDscp.setStatus("current")


class _AcdSmapIPv4FilterDscpLast_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterDscpLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdSmapIPv4FilterDscpLast_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterDscpLast_Object = MibTableColumn
acdSmapIPv4FilterDscpLast = _AcdSmapIPv4FilterDscpLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 43),
    _AcdSmapIPv4FilterDscpLast_Type()
)
acdSmapIPv4FilterDscpLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterDscpLast.setStatus("current")


class _AcdSmapIPv4FilterDscpOper_Type(AcdFilterOperator):
    """Custom type acdSmapIPv4FilterDscpOper based on AcdFilterOperator"""


_AcdSmapIPv4FilterDscpOper_Object = MibTableColumn
acdSmapIPv4FilterDscpOper = _AcdSmapIPv4FilterDscpOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 44),
    _AcdSmapIPv4FilterDscpOper_Type()
)
acdSmapIPv4FilterDscpOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterDscpOper.setStatus("current")


class _AcdSmapIPv4FilterPre_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterPre based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapIPv4FilterPre_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterPre_Object = MibTableColumn
acdSmapIPv4FilterPre = _AcdSmapIPv4FilterPre_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 45),
    _AcdSmapIPv4FilterPre_Type()
)
acdSmapIPv4FilterPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterPre.setStatus("current")


class _AcdSmapIPv4FilterPreLast_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterPreLast based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapIPv4FilterPreLast_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterPreLast_Object = MibTableColumn
acdSmapIPv4FilterPreLast = _AcdSmapIPv4FilterPreLast_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 46),
    _AcdSmapIPv4FilterPreLast_Type()
)
acdSmapIPv4FilterPreLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterPreLast.setStatus("current")


class _AcdSmapIPv4FilterPreOper_Type(AcdFilterOperator):
    """Custom type acdSmapIPv4FilterPreOper based on AcdFilterOperator"""


_AcdSmapIPv4FilterPreOper_Object = MibTableColumn
acdSmapIPv4FilterPreOper = _AcdSmapIPv4FilterPreOper_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 47),
    _AcdSmapIPv4FilterPreOper_Type()
)
acdSmapIPv4FilterPreOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterPreOper.setStatus("current")


class _AcdSmapIPv4FilterECNEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterECNEn based on TruthValue"""


_AcdSmapIPv4FilterECNEn_Object = MibTableColumn
acdSmapIPv4FilterECNEn = _AcdSmapIPv4FilterECNEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 48),
    _AcdSmapIPv4FilterECNEn_Type()
)
acdSmapIPv4FilterECNEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterECNEn.setStatus("current")


class _AcdSmapIPv4FilterECN_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterECN based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcdSmapIPv4FilterECN_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterECN_Object = MibTableColumn
acdSmapIPv4FilterECN = _AcdSmapIPv4FilterECN_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 49),
    _AcdSmapIPv4FilterECN_Type()
)
acdSmapIPv4FilterECN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterECN.setStatus("current")


class _AcdSmapIPv4FilterSrcPortEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterSrcPortEn based on TruthValue"""


_AcdSmapIPv4FilterSrcPortEn_Object = MibTableColumn
acdSmapIPv4FilterSrcPortEn = _AcdSmapIPv4FilterSrcPortEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 50),
    _AcdSmapIPv4FilterSrcPortEn_Type()
)
acdSmapIPv4FilterSrcPortEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterSrcPortEn.setStatus("current")


class _AcdSmapIPv4FilterSrcPort_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterSrcPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdSmapIPv4FilterSrcPort_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterSrcPort_Object = MibTableColumn
acdSmapIPv4FilterSrcPort = _AcdSmapIPv4FilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 51),
    _AcdSmapIPv4FilterSrcPort_Type()
)
acdSmapIPv4FilterSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterSrcPort.setStatus("current")


class _AcdSmapIPv4FilterDstPortEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterDstPortEn based on TruthValue"""


_AcdSmapIPv4FilterDstPortEn_Object = MibTableColumn
acdSmapIPv4FilterDstPortEn = _AcdSmapIPv4FilterDstPortEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 52),
    _AcdSmapIPv4FilterDstPortEn_Type()
)
acdSmapIPv4FilterDstPortEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterDstPortEn.setStatus("current")


class _AcdSmapIPv4FilterDstPort_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterDstPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdSmapIPv4FilterDstPort_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterDstPort_Object = MibTableColumn
acdSmapIPv4FilterDstPort = _AcdSmapIPv4FilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 53),
    _AcdSmapIPv4FilterDstPort_Type()
)
acdSmapIPv4FilterDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterDstPort.setStatus("current")


class _AcdSmapIPv4FilterIcmpTypeEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterIcmpTypeEn based on TruthValue"""


_AcdSmapIPv4FilterIcmpTypeEn_Object = MibTableColumn
acdSmapIPv4FilterIcmpTypeEn = _AcdSmapIPv4FilterIcmpTypeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 54),
    _AcdSmapIPv4FilterIcmpTypeEn_Type()
)
acdSmapIPv4FilterIcmpTypeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterIcmpTypeEn.setStatus("current")


class _AcdSmapIPv4FilterIcmpType_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterIcmpType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcdSmapIPv4FilterIcmpType_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterIcmpType_Object = MibTableColumn
acdSmapIPv4FilterIcmpType = _AcdSmapIPv4FilterIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 55),
    _AcdSmapIPv4FilterIcmpType_Type()
)
acdSmapIPv4FilterIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterIcmpType.setStatus("current")


class _AcdSmapIPv4FilterIcmpCodeEn_Type(TruthValue):
    """Custom type acdSmapIPv4FilterIcmpCodeEn based on TruthValue"""


_AcdSmapIPv4FilterIcmpCodeEn_Object = MibTableColumn
acdSmapIPv4FilterIcmpCodeEn = _AcdSmapIPv4FilterIcmpCodeEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 56),
    _AcdSmapIPv4FilterIcmpCodeEn_Type()
)
acdSmapIPv4FilterIcmpCodeEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterIcmpCodeEn.setStatus("current")


class _AcdSmapIPv4FilterIcmpCode_Type(Unsigned32):
    """Custom type acdSmapIPv4FilterIcmpCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcdSmapIPv4FilterIcmpCode_Type.__name__ = "Unsigned32"
_AcdSmapIPv4FilterIcmpCode_Object = MibTableColumn
acdSmapIPv4FilterIcmpCode = _AcdSmapIPv4FilterIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 4, 1, 57),
    _AcdSmapIPv4FilterIcmpCode_Type()
)
acdSmapIPv4FilterIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterIcmpCode.setStatus("current")
_AcdFilterNotifications_ObjectIdentity = ObjectIdentity
acdFilterNotifications = _AcdFilterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 5)
)
_AcdFilterMIBObjects_ObjectIdentity = ObjectIdentity
acdFilterMIBObjects = _AcdFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 6)
)
_AcdFilterTableTid_ObjectIdentity = ObjectIdentity
acdFilterTableTid = _AcdFilterTableTid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 6, 1)
)
_AcdSmapL2FilterTableLastChangeTid_Type = Unsigned32
_AcdSmapL2FilterTableLastChangeTid_Object = MibScalar
acdSmapL2FilterTableLastChangeTid = _AcdSmapL2FilterTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 6, 1, 1),
    _AcdSmapL2FilterTableLastChangeTid_Type()
)
acdSmapL2FilterTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSmapL2FilterTableLastChangeTid.setStatus("current")
_AcdSmapIPv4FilterTableLastChangeTid_Type = Unsigned32
_AcdSmapIPv4FilterTableLastChangeTid_Object = MibScalar
acdSmapIPv4FilterTableLastChangeTid = _AcdSmapIPv4FilterTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 6, 1, 2),
    _AcdSmapIPv4FilterTableLastChangeTid_Type()
)
acdSmapIPv4FilterTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSmapIPv4FilterTableLastChangeTid.setStatus("current")
_AcdFilterConformance_ObjectIdentity = ObjectIdentity
acdFilterConformance = _AcdFilterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7)
)
_AcdFilterCompliances_ObjectIdentity = ObjectIdentity
acdFilterCompliances = _AcdFilterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7, 1)
)
_AcdFilterGroups_ObjectIdentity = ObjectIdentity
acdFilterGroups = _AcdFilterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7, 2)
)

# Managed Objects groups

acdL2FilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7, 2, 1)
)
acdL2FilterGroup.setObjects(
      *(("ACD-FILTER-MIB", "acdL2FilterName"),
        ("ACD-FILTER-MIB", "acdL2FilterMacDstEn"),
        ("ACD-FILTER-MIB", "acdL2FilterMacDst"),
        ("ACD-FILTER-MIB", "acdL2FilterMacDstMask"),
        ("ACD-FILTER-MIB", "acdL2FilterMacSrcEn"),
        ("ACD-FILTER-MIB", "acdL2FilterMacSrc"),
        ("ACD-FILTER-MIB", "acdL2FilterMacSrcMask"),
        ("ACD-FILTER-MIB", "acdL2FilterEtypeEn"),
        ("ACD-FILTER-MIB", "acdL2FilterEtype"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan1PriorEn"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan1Prior"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan1CfiEn"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan1Cfi"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan1IdEn"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan1Id"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan2PriorEn"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan2Prior"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan2CfiEn"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan2Cfi"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan2IdEn"),
        ("ACD-FILTER-MIB", "acdL2FilterVlan2Id"),
        ("ACD-FILTER-MIB", "acdL2FilterRowStatus"))
)
if mibBuilder.loadTexts:
    acdL2FilterGroup.setStatus("current")

acdIPv4FilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7, 2, 2)
)
acdIPv4FilterGroup.setObjects(
      *(("ACD-FILTER-MIB", "acdIPv4FilterName"),
        ("ACD-FILTER-MIB", "acdIPv4FilterSrcEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterSrc"),
        ("ACD-FILTER-MIB", "acdIPv4FilterSrcMask"),
        ("ACD-FILTER-MIB", "acdIPv4FilterDstEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterDst"),
        ("ACD-FILTER-MIB", "acdIPv4FilterDstMask"),
        ("ACD-FILTER-MIB", "acdIPv4FilterProtoEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterProto"),
        ("ACD-FILTER-MIB", "acdIPv4FilterTTLEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterTTL"),
        ("ACD-FILTER-MIB", "acdIPv4FilterIHLEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterIHL"),
        ("ACD-FILTER-MIB", "acdIPv4FilterDscpEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterDscp"),
        ("ACD-FILTER-MIB", "acdIPv4FilterECNEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterECN"),
        ("ACD-FILTER-MIB", "acdIPv4FilterSrcPortEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterSrcPort"),
        ("ACD-FILTER-MIB", "acdIPv4FilterDstPortEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterDstPort"),
        ("ACD-FILTER-MIB", "acdIPv4FilterIcmpTypeEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterIcmpType"),
        ("ACD-FILTER-MIB", "acdIPv4FilterIcmpCodeEn"),
        ("ACD-FILTER-MIB", "acdIPv4FilterIcmpCode"),
        ("ACD-FILTER-MIB", "acdIPv4FilterRowStatus"))
)
if mibBuilder.loadTexts:
    acdIPv4FilterGroup.setStatus("current")

acdSmapL2FilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7, 2, 3)
)
acdSmapL2FilterGroup.setObjects(
      *(("ACD-FILTER-MIB", "acdSmapL2FilterName"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterRowStatus"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1PriorEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1Prior"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1PriorLast"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1PriorOper"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1IdEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1Id"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1IdLast"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1IdOper"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1CfiEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1Cfi"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1TypeEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan1Type"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2PriorEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2Prior"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2PriorLast"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2PriorOper"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2IdEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2Id"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2IdLast"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2IdOper"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2CfiEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2Cfi"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2TypeEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterVlan2Type"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterMacDstEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterMacDst"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterMacDstMask"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterMacSrcEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterMacSrc"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterMacSrcMask"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterEtypeEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterEtype"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterIpCosEn"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterIpCosMode"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterDscp"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterDscpLast"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterDscpOper"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterPre"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterPreLast"),
        ("ACD-FILTER-MIB", "acdSmapL2FilterPreOper"))
)
if mibBuilder.loadTexts:
    acdSmapL2FilterGroup.setStatus("current")

acdSmapIPv4FilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7, 2, 4)
)
acdSmapIPv4FilterGroup.setObjects(
      *(("ACD-FILTER-MIB", "acdSmapIPv4FilterName"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterRowStatus"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1PriorEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1Prior"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1PriorLast"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1PriorOper"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1IdEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1Id"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1IdLast"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1IdOper"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1CfiEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1Cfi"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1TypeEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan1Type"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2PriorEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2Prior"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2PriorLast"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2PriorOper"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2IdEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2Id"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2IdLast"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2IdOper"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2CfiEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2Cfi"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2TypeEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterVlan2Type"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterSrcEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterSrc"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterSrcMask"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterDstEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterDst"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterDstMask"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterProtoEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterProto"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterTTLEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterTTL"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterIHLEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterIHL"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterIpCosEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterIpCosMode"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterDscp"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterDscpLast"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterDscpOper"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterPre"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterPreLast"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterPreOper"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterECNEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterECN"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterSrcPortEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterSrcPort"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterDstPortEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterDstPort"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterIcmpTypeEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterIcmpType"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterIcmpCodeEn"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterIcmpCode"))
)
if mibBuilder.loadTexts:
    acdSmapIPv4FilterGroup.setStatus("current")

acdFilterTidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7, 2, 5)
)
acdFilterTidGroup.setObjects(
      *(("ACD-FILTER-MIB", "acdSmapL2FilterTableLastChangeTid"),
        ("ACD-FILTER-MIB", "acdSmapIPv4FilterTableLastChangeTid"))
)
if mibBuilder.loadTexts:
    acdFilterTidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdFilterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    acdFilterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-FILTER-MIB",
    **{"AcdFilterOperator": AcdFilterOperator,
       "AcdFilterVlanType": AcdFilterVlanType,
       "acdFilter": acdFilter,
       "acdL2FilterTable": acdL2FilterTable,
       "acdL2FilterEntry": acdL2FilterEntry,
       "acdL2FilterID": acdL2FilterID,
       "acdL2FilterName": acdL2FilterName,
       "acdL2FilterMacDstEn": acdL2FilterMacDstEn,
       "acdL2FilterMacDst": acdL2FilterMacDst,
       "acdL2FilterMacDstMask": acdL2FilterMacDstMask,
       "acdL2FilterMacSrcEn": acdL2FilterMacSrcEn,
       "acdL2FilterMacSrc": acdL2FilterMacSrc,
       "acdL2FilterMacSrcMask": acdL2FilterMacSrcMask,
       "acdL2FilterEtypeEn": acdL2FilterEtypeEn,
       "acdL2FilterEtype": acdL2FilterEtype,
       "acdL2FilterVlan1PriorEn": acdL2FilterVlan1PriorEn,
       "acdL2FilterVlan1Prior": acdL2FilterVlan1Prior,
       "acdL2FilterVlan1CfiEn": acdL2FilterVlan1CfiEn,
       "acdL2FilterVlan1Cfi": acdL2FilterVlan1Cfi,
       "acdL2FilterVlan1IdEn": acdL2FilterVlan1IdEn,
       "acdL2FilterVlan1Id": acdL2FilterVlan1Id,
       "acdL2FilterVlan2PriorEn": acdL2FilterVlan2PriorEn,
       "acdL2FilterVlan2Prior": acdL2FilterVlan2Prior,
       "acdL2FilterVlan2CfiEn": acdL2FilterVlan2CfiEn,
       "acdL2FilterVlan2Cfi": acdL2FilterVlan2Cfi,
       "acdL2FilterVlan2IdEn": acdL2FilterVlan2IdEn,
       "acdL2FilterVlan2Id": acdL2FilterVlan2Id,
       "acdL2FilterRowStatus": acdL2FilterRowStatus,
       "acdIPv4FilterTable": acdIPv4FilterTable,
       "acdIPv4FilterEntry": acdIPv4FilterEntry,
       "acdIPv4FilterID": acdIPv4FilterID,
       "acdIPv4FilterName": acdIPv4FilterName,
       "acdIPv4FilterSrcEn": acdIPv4FilterSrcEn,
       "acdIPv4FilterSrc": acdIPv4FilterSrc,
       "acdIPv4FilterSrcMask": acdIPv4FilterSrcMask,
       "acdIPv4FilterDstEn": acdIPv4FilterDstEn,
       "acdIPv4FilterDst": acdIPv4FilterDst,
       "acdIPv4FilterDstMask": acdIPv4FilterDstMask,
       "acdIPv4FilterProtoEn": acdIPv4FilterProtoEn,
       "acdIPv4FilterProto": acdIPv4FilterProto,
       "acdIPv4FilterTTLEn": acdIPv4FilterTTLEn,
       "acdIPv4FilterTTL": acdIPv4FilterTTL,
       "acdIPv4FilterIHLEn": acdIPv4FilterIHLEn,
       "acdIPv4FilterIHL": acdIPv4FilterIHL,
       "acdIPv4FilterDscpEn": acdIPv4FilterDscpEn,
       "acdIPv4FilterDscp": acdIPv4FilterDscp,
       "acdIPv4FilterECNEn": acdIPv4FilterECNEn,
       "acdIPv4FilterECN": acdIPv4FilterECN,
       "acdIPv4FilterSrcPortEn": acdIPv4FilterSrcPortEn,
       "acdIPv4FilterSrcPort": acdIPv4FilterSrcPort,
       "acdIPv4FilterDstPortEn": acdIPv4FilterDstPortEn,
       "acdIPv4FilterDstPort": acdIPv4FilterDstPort,
       "acdIPv4FilterIcmpTypeEn": acdIPv4FilterIcmpTypeEn,
       "acdIPv4FilterIcmpType": acdIPv4FilterIcmpType,
       "acdIPv4FilterIcmpCodeEn": acdIPv4FilterIcmpCodeEn,
       "acdIPv4FilterIcmpCode": acdIPv4FilterIcmpCode,
       "acdIPv4FilterRowStatus": acdIPv4FilterRowStatus,
       "acdSmapL2FilterTable": acdSmapL2FilterTable,
       "acdSmapL2FilterEntry": acdSmapL2FilterEntry,
       "acdSmapL2FilterID": acdSmapL2FilterID,
       "acdSmapL2FilterName": acdSmapL2FilterName,
       "acdSmapL2FilterRowStatus": acdSmapL2FilterRowStatus,
       "acdSmapL2FilterVlan1PriorEn": acdSmapL2FilterVlan1PriorEn,
       "acdSmapL2FilterVlan1Prior": acdSmapL2FilterVlan1Prior,
       "acdSmapL2FilterVlan1PriorLast": acdSmapL2FilterVlan1PriorLast,
       "acdSmapL2FilterVlan1PriorOper": acdSmapL2FilterVlan1PriorOper,
       "acdSmapL2FilterVlan1IdEn": acdSmapL2FilterVlan1IdEn,
       "acdSmapL2FilterVlan1Id": acdSmapL2FilterVlan1Id,
       "acdSmapL2FilterVlan1IdLast": acdSmapL2FilterVlan1IdLast,
       "acdSmapL2FilterVlan1IdOper": acdSmapL2FilterVlan1IdOper,
       "acdSmapL2FilterVlan1CfiEn": acdSmapL2FilterVlan1CfiEn,
       "acdSmapL2FilterVlan1Cfi": acdSmapL2FilterVlan1Cfi,
       "acdSmapL2FilterVlan1TypeEn": acdSmapL2FilterVlan1TypeEn,
       "acdSmapL2FilterVlan1Type": acdSmapL2FilterVlan1Type,
       "acdSmapL2FilterVlan2PriorEn": acdSmapL2FilterVlan2PriorEn,
       "acdSmapL2FilterVlan2Prior": acdSmapL2FilterVlan2Prior,
       "acdSmapL2FilterVlan2PriorLast": acdSmapL2FilterVlan2PriorLast,
       "acdSmapL2FilterVlan2PriorOper": acdSmapL2FilterVlan2PriorOper,
       "acdSmapL2FilterVlan2IdEn": acdSmapL2FilterVlan2IdEn,
       "acdSmapL2FilterVlan2Id": acdSmapL2FilterVlan2Id,
       "acdSmapL2FilterVlan2IdLast": acdSmapL2FilterVlan2IdLast,
       "acdSmapL2FilterVlan2IdOper": acdSmapL2FilterVlan2IdOper,
       "acdSmapL2FilterVlan2CfiEn": acdSmapL2FilterVlan2CfiEn,
       "acdSmapL2FilterVlan2Cfi": acdSmapL2FilterVlan2Cfi,
       "acdSmapL2FilterVlan2TypeEn": acdSmapL2FilterVlan2TypeEn,
       "acdSmapL2FilterVlan2Type": acdSmapL2FilterVlan2Type,
       "acdSmapL2FilterMacDstEn": acdSmapL2FilterMacDstEn,
       "acdSmapL2FilterMacDst": acdSmapL2FilterMacDst,
       "acdSmapL2FilterMacDstMask": acdSmapL2FilterMacDstMask,
       "acdSmapL2FilterMacSrcEn": acdSmapL2FilterMacSrcEn,
       "acdSmapL2FilterMacSrc": acdSmapL2FilterMacSrc,
       "acdSmapL2FilterMacSrcMask": acdSmapL2FilterMacSrcMask,
       "acdSmapL2FilterEtypeEn": acdSmapL2FilterEtypeEn,
       "acdSmapL2FilterEtype": acdSmapL2FilterEtype,
       "acdSmapL2FilterIpCosEn": acdSmapL2FilterIpCosEn,
       "acdSmapL2FilterIpCosMode": acdSmapL2FilterIpCosMode,
       "acdSmapL2FilterDscp": acdSmapL2FilterDscp,
       "acdSmapL2FilterDscpLast": acdSmapL2FilterDscpLast,
       "acdSmapL2FilterDscpOper": acdSmapL2FilterDscpOper,
       "acdSmapL2FilterPre": acdSmapL2FilterPre,
       "acdSmapL2FilterPreLast": acdSmapL2FilterPreLast,
       "acdSmapL2FilterPreOper": acdSmapL2FilterPreOper,
       "acdSmapIPv4FilterTable": acdSmapIPv4FilterTable,
       "acdSmapIPv4FilterEntry": acdSmapIPv4FilterEntry,
       "acdSmapIPv4FilterID": acdSmapIPv4FilterID,
       "acdSmapIPv4FilterName": acdSmapIPv4FilterName,
       "acdSmapIPv4FilterRowStatus": acdSmapIPv4FilterRowStatus,
       "acdSmapIPv4FilterVlan1PriorEn": acdSmapIPv4FilterVlan1PriorEn,
       "acdSmapIPv4FilterVlan1Prior": acdSmapIPv4FilterVlan1Prior,
       "acdSmapIPv4FilterVlan1PriorLast": acdSmapIPv4FilterVlan1PriorLast,
       "acdSmapIPv4FilterVlan1PriorOper": acdSmapIPv4FilterVlan1PriorOper,
       "acdSmapIPv4FilterVlan1IdEn": acdSmapIPv4FilterVlan1IdEn,
       "acdSmapIPv4FilterVlan1Id": acdSmapIPv4FilterVlan1Id,
       "acdSmapIPv4FilterVlan1IdLast": acdSmapIPv4FilterVlan1IdLast,
       "acdSmapIPv4FilterVlan1IdOper": acdSmapIPv4FilterVlan1IdOper,
       "acdSmapIPv4FilterVlan1CfiEn": acdSmapIPv4FilterVlan1CfiEn,
       "acdSmapIPv4FilterVlan1Cfi": acdSmapIPv4FilterVlan1Cfi,
       "acdSmapIPv4FilterVlan1TypeEn": acdSmapIPv4FilterVlan1TypeEn,
       "acdSmapIPv4FilterVlan1Type": acdSmapIPv4FilterVlan1Type,
       "acdSmapIPv4FilterVlan2PriorEn": acdSmapIPv4FilterVlan2PriorEn,
       "acdSmapIPv4FilterVlan2Prior": acdSmapIPv4FilterVlan2Prior,
       "acdSmapIPv4FilterVlan2PriorLast": acdSmapIPv4FilterVlan2PriorLast,
       "acdSmapIPv4FilterVlan2PriorOper": acdSmapIPv4FilterVlan2PriorOper,
       "acdSmapIPv4FilterVlan2IdEn": acdSmapIPv4FilterVlan2IdEn,
       "acdSmapIPv4FilterVlan2Id": acdSmapIPv4FilterVlan2Id,
       "acdSmapIPv4FilterVlan2IdLast": acdSmapIPv4FilterVlan2IdLast,
       "acdSmapIPv4FilterVlan2IdOper": acdSmapIPv4FilterVlan2IdOper,
       "acdSmapIPv4FilterVlan2CfiEn": acdSmapIPv4FilterVlan2CfiEn,
       "acdSmapIPv4FilterVlan2Cfi": acdSmapIPv4FilterVlan2Cfi,
       "acdSmapIPv4FilterVlan2TypeEn": acdSmapIPv4FilterVlan2TypeEn,
       "acdSmapIPv4FilterVlan2Type": acdSmapIPv4FilterVlan2Type,
       "acdSmapIPv4FilterSrcEn": acdSmapIPv4FilterSrcEn,
       "acdSmapIPv4FilterSrc": acdSmapIPv4FilterSrc,
       "acdSmapIPv4FilterSrcMask": acdSmapIPv4FilterSrcMask,
       "acdSmapIPv4FilterDstEn": acdSmapIPv4FilterDstEn,
       "acdSmapIPv4FilterDst": acdSmapIPv4FilterDst,
       "acdSmapIPv4FilterDstMask": acdSmapIPv4FilterDstMask,
       "acdSmapIPv4FilterProtoEn": acdSmapIPv4FilterProtoEn,
       "acdSmapIPv4FilterProto": acdSmapIPv4FilterProto,
       "acdSmapIPv4FilterTTLEn": acdSmapIPv4FilterTTLEn,
       "acdSmapIPv4FilterTTL": acdSmapIPv4FilterTTL,
       "acdSmapIPv4FilterIHLEn": acdSmapIPv4FilterIHLEn,
       "acdSmapIPv4FilterIHL": acdSmapIPv4FilterIHL,
       "acdSmapIPv4FilterIpCosEn": acdSmapIPv4FilterIpCosEn,
       "acdSmapIPv4FilterIpCosMode": acdSmapIPv4FilterIpCosMode,
       "acdSmapIPv4FilterDscp": acdSmapIPv4FilterDscp,
       "acdSmapIPv4FilterDscpLast": acdSmapIPv4FilterDscpLast,
       "acdSmapIPv4FilterDscpOper": acdSmapIPv4FilterDscpOper,
       "acdSmapIPv4FilterPre": acdSmapIPv4FilterPre,
       "acdSmapIPv4FilterPreLast": acdSmapIPv4FilterPreLast,
       "acdSmapIPv4FilterPreOper": acdSmapIPv4FilterPreOper,
       "acdSmapIPv4FilterECNEn": acdSmapIPv4FilterECNEn,
       "acdSmapIPv4FilterECN": acdSmapIPv4FilterECN,
       "acdSmapIPv4FilterSrcPortEn": acdSmapIPv4FilterSrcPortEn,
       "acdSmapIPv4FilterSrcPort": acdSmapIPv4FilterSrcPort,
       "acdSmapIPv4FilterDstPortEn": acdSmapIPv4FilterDstPortEn,
       "acdSmapIPv4FilterDstPort": acdSmapIPv4FilterDstPort,
       "acdSmapIPv4FilterIcmpTypeEn": acdSmapIPv4FilterIcmpTypeEn,
       "acdSmapIPv4FilterIcmpType": acdSmapIPv4FilterIcmpType,
       "acdSmapIPv4FilterIcmpCodeEn": acdSmapIPv4FilterIcmpCodeEn,
       "acdSmapIPv4FilterIcmpCode": acdSmapIPv4FilterIcmpCode,
       "acdFilterNotifications": acdFilterNotifications,
       "acdFilterMIBObjects": acdFilterMIBObjects,
       "acdFilterTableTid": acdFilterTableTid,
       "acdSmapL2FilterTableLastChangeTid": acdSmapL2FilterTableLastChangeTid,
       "acdSmapIPv4FilterTableLastChangeTid": acdSmapIPv4FilterTableLastChangeTid,
       "acdFilterConformance": acdFilterConformance,
       "acdFilterCompliances": acdFilterCompliances,
       "acdFilterCompliance": acdFilterCompliance,
       "acdFilterGroups": acdFilterGroups,
       "acdL2FilterGroup": acdL2FilterGroup,
       "acdIPv4FilterGroup": acdIPv4FilterGroup,
       "acdSmapL2FilterGroup": acdSmapL2FilterGroup,
       "acdSmapIPv4FilterGroup": acdSmapIPv4FilterGroup,
       "acdFilterTidGroup": acdFilterTidGroup}
)
