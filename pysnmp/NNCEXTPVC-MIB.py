# SNMP MIB module (NNCEXTPVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCEXTPVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:20 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nncExtPvc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtPvcObjects_ObjectIdentity = ObjectIdentity
nncExtPvcObjects = _NncExtPvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1)
)
_NncCrPvpcTable_Object = MibTable
nncCrPvpcTable = _NncCrPvpcTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1)
)
if mibBuilder.loadTexts:
    nncCrPvpcTable.setStatus("current")
_NncCrPvpcTableEntry_Object = MibTableRow
nncCrPvpcTableEntry = _NncCrPvpcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1)
)
nncCrPvpcTableEntry.setIndexNames(
    (0, "NNCEXTPVC-MIB", "nncCrPvpcSrcIfIndex"),
    (0, "NNCEXTPVC-MIB", "nncCrPvpcSrcVpi"),
    (0, "NNCEXTPVC-MIB", "nncCrPvpcDstIfIndex"),
    (0, "NNCEXTPVC-MIB", "nncCrPvpcDstVpi"),
)
if mibBuilder.loadTexts:
    nncCrPvpcTableEntry.setStatus("current")
_NncCrPvpcSrcIfIndex_Type = InterfaceIndex
_NncCrPvpcSrcIfIndex_Object = MibTableColumn
nncCrPvpcSrcIfIndex = _NncCrPvpcSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 1),
    _NncCrPvpcSrcIfIndex_Type()
)
nncCrPvpcSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvpcSrcIfIndex.setStatus("current")


class _NncCrPvpcSrcVpi_Type(Integer32):
    """Custom type nncCrPvpcSrcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NncCrPvpcSrcVpi_Type.__name__ = "Integer32"
_NncCrPvpcSrcVpi_Object = MibTableColumn
nncCrPvpcSrcVpi = _NncCrPvpcSrcVpi_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 2),
    _NncCrPvpcSrcVpi_Type()
)
nncCrPvpcSrcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvpcSrcVpi.setStatus("current")
_NncCrPvpcDstIfIndex_Type = InterfaceIndex
_NncCrPvpcDstIfIndex_Object = MibTableColumn
nncCrPvpcDstIfIndex = _NncCrPvpcDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 3),
    _NncCrPvpcDstIfIndex_Type()
)
nncCrPvpcDstIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvpcDstIfIndex.setStatus("current")


class _NncCrPvpcDstVpi_Type(Integer32):
    """Custom type nncCrPvpcDstVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NncCrPvpcDstVpi_Type.__name__ = "Integer32"
_NncCrPvpcDstVpi_Object = MibTableColumn
nncCrPvpcDstVpi = _NncCrPvpcDstVpi_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 4),
    _NncCrPvpcDstVpi_Type()
)
nncCrPvpcDstVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvpcDstVpi.setStatus("current")


class _NncCrPvpcCastType_Type(Integer32):
    """Custom type nncCrPvpcCastType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2mp", 2),
          ("p2p", 1))
    )


_NncCrPvpcCastType_Type.__name__ = "Integer32"
_NncCrPvpcCastType_Object = MibTableColumn
nncCrPvpcCastType = _NncCrPvpcCastType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 5),
    _NncCrPvpcCastType_Type()
)
nncCrPvpcCastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcCastType.setStatus("current")


class _NncCrPvpcFwdServiceCategory_Type(Integer32):
    """Custom type nncCrPvpcFwdServiceCategory based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 3),
          ("cbr", 1),
          ("nrtvbr", 2),
          ("rtvbr", 6),
          ("ubr", 4))
    )


_NncCrPvpcFwdServiceCategory_Type.__name__ = "Integer32"
_NncCrPvpcFwdServiceCategory_Object = MibTableColumn
nncCrPvpcFwdServiceCategory = _NncCrPvpcFwdServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 6),
    _NncCrPvpcFwdServiceCategory_Type()
)
nncCrPvpcFwdServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdServiceCategory.setStatus("current")


class _NncCrPvpcBwdServiceCategory_Type(Integer32):
    """Custom type nncCrPvpcBwdServiceCategory based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 3),
          ("cbr", 1),
          ("nrtvbr", 2),
          ("rtvbr", 6),
          ("ubr", 4))
    )


_NncCrPvpcBwdServiceCategory_Type.__name__ = "Integer32"
_NncCrPvpcBwdServiceCategory_Object = MibTableColumn
nncCrPvpcBwdServiceCategory = _NncCrPvpcBwdServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 7),
    _NncCrPvpcBwdServiceCategory_Type()
)
nncCrPvpcBwdServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdServiceCategory.setStatus("current")


class _NncCrPvpcFwdAbrDynTrfcIcr_Type(Integer32):
    """Custom type nncCrPvpcFwdAbrDynTrfcIcr based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvpcFwdAbrDynTrfcIcr_Type.__name__ = "Integer32"
_NncCrPvpcFwdAbrDynTrfcIcr_Object = MibTableColumn
nncCrPvpcFwdAbrDynTrfcIcr = _NncCrPvpcFwdAbrDynTrfcIcr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 8),
    _NncCrPvpcFwdAbrDynTrfcIcr_Type()
)
nncCrPvpcFwdAbrDynTrfcIcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdAbrDynTrfcIcr.setStatus("current")


class _NncCrPvpcFwdAbrDynTrfcRif_Type(Integer32):
    """Custom type nncCrPvpcFwdAbrDynTrfcRif based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrPvpcFwdAbrDynTrfcRif_Type.__name__ = "Integer32"
_NncCrPvpcFwdAbrDynTrfcRif_Object = MibTableColumn
nncCrPvpcFwdAbrDynTrfcRif = _NncCrPvpcFwdAbrDynTrfcRif_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 9),
    _NncCrPvpcFwdAbrDynTrfcRif_Type()
)
nncCrPvpcFwdAbrDynTrfcRif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdAbrDynTrfcRif.setStatus("current")


class _NncCrPvpcFwdAbrDynTrfcRdf_Type(Integer32):
    """Custom type nncCrPvpcFwdAbrDynTrfcRdf based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrPvpcFwdAbrDynTrfcRdf_Type.__name__ = "Integer32"
_NncCrPvpcFwdAbrDynTrfcRdf_Object = MibTableColumn
nncCrPvpcFwdAbrDynTrfcRdf = _NncCrPvpcFwdAbrDynTrfcRdf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 10),
    _NncCrPvpcFwdAbrDynTrfcRdf_Type()
)
nncCrPvpcFwdAbrDynTrfcRdf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdAbrDynTrfcRdf.setStatus("current")


class _NncCrPvpcBwdAbrDynTrfcIcr_Type(Integer32):
    """Custom type nncCrPvpcBwdAbrDynTrfcIcr based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvpcBwdAbrDynTrfcIcr_Type.__name__ = "Integer32"
_NncCrPvpcBwdAbrDynTrfcIcr_Object = MibTableColumn
nncCrPvpcBwdAbrDynTrfcIcr = _NncCrPvpcBwdAbrDynTrfcIcr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 11),
    _NncCrPvpcBwdAbrDynTrfcIcr_Type()
)
nncCrPvpcBwdAbrDynTrfcIcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdAbrDynTrfcIcr.setStatus("current")


class _NncCrPvpcBwdAbrDynTrfcRif_Type(Integer32):
    """Custom type nncCrPvpcBwdAbrDynTrfcRif based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrPvpcBwdAbrDynTrfcRif_Type.__name__ = "Integer32"
_NncCrPvpcBwdAbrDynTrfcRif_Object = MibTableColumn
nncCrPvpcBwdAbrDynTrfcRif = _NncCrPvpcBwdAbrDynTrfcRif_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 12),
    _NncCrPvpcBwdAbrDynTrfcRif_Type()
)
nncCrPvpcBwdAbrDynTrfcRif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdAbrDynTrfcRif.setStatus("current")


class _NncCrPvpcBwdAbrDynTrfcRdf_Type(Integer32):
    """Custom type nncCrPvpcBwdAbrDynTrfcRdf based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrPvpcBwdAbrDynTrfcRdf_Type.__name__ = "Integer32"
_NncCrPvpcBwdAbrDynTrfcRdf_Object = MibTableColumn
nncCrPvpcBwdAbrDynTrfcRdf = _NncCrPvpcBwdAbrDynTrfcRdf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 13),
    _NncCrPvpcBwdAbrDynTrfcRdf_Type()
)
nncCrPvpcBwdAbrDynTrfcRdf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdAbrDynTrfcRdf.setStatus("current")


class _NncCrPvpcSrcBillingFlag_Type(Integer32):
    """Custom type nncCrPvpcSrcBillingFlag based on Integer32"""
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


_NncCrPvpcSrcBillingFlag_Type.__name__ = "Integer32"
_NncCrPvpcSrcBillingFlag_Object = MibTableColumn
nncCrPvpcSrcBillingFlag = _NncCrPvpcSrcBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 14),
    _NncCrPvpcSrcBillingFlag_Type()
)
nncCrPvpcSrcBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcSrcBillingFlag.setStatus("current")


class _NncCrPvpcDstBillingFlag_Type(Integer32):
    """Custom type nncCrPvpcDstBillingFlag based on Integer32"""
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


_NncCrPvpcDstBillingFlag_Type.__name__ = "Integer32"
_NncCrPvpcDstBillingFlag_Object = MibTableColumn
nncCrPvpcDstBillingFlag = _NncCrPvpcDstBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 15),
    _NncCrPvpcDstBillingFlag_Type()
)
nncCrPvpcDstBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcDstBillingFlag.setStatus("current")


class _NncCrPvpcFwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncCrPvpcFwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("p0Plus1", 2),
          ("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncCrPvpcFwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncCrPvpcFwdTmTrafficDescriptor_Object = MibTableColumn
nncCrPvpcFwdTmTrafficDescriptor = _NncCrPvpcFwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 16),
    _NncCrPvpcFwdTmTrafficDescriptor_Type()
)
nncCrPvpcFwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdTmTrafficDescriptor.setStatus("current")


class _NncCrPvpcFwdTmPolicingOption_Type(Integer32):
    """Custom type nncCrPvpcFwdTmPolicingOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discard", 3),
          ("none", 0),
          ("tag", 2))
    )


_NncCrPvpcFwdTmPolicingOption_Type.__name__ = "Integer32"
_NncCrPvpcFwdTmPolicingOption_Object = MibTableColumn
nncCrPvpcFwdTmPolicingOption = _NncCrPvpcFwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 17),
    _NncCrPvpcFwdTmPolicingOption_Type()
)
nncCrPvpcFwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdTmPolicingOption.setStatus("current")


class _NncCrPvpcFwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCrPvpcFwdTmBucketOneRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvpcFwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCrPvpcFwdTmBucketOneRate_Object = MibTableColumn
nncCrPvpcFwdTmBucketOneRate = _NncCrPvpcFwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 18),
    _NncCrPvpcFwdTmBucketOneRate_Type()
)
nncCrPvpcFwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdTmBucketOneRate.setStatus("current")


class _NncCrPvpcFwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCrPvpcFwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrPvpcFwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCrPvpcFwdTmBucketOneCdvt_Object = MibTableColumn
nncCrPvpcFwdTmBucketOneCdvt = _NncCrPvpcFwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 19),
    _NncCrPvpcFwdTmBucketOneCdvt_Type()
)
nncCrPvpcFwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdTmBucketOneCdvt.setStatus("current")


class _NncCrPvpcFwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncCrPvpcFwdTmBucketTwoRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvpcFwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncCrPvpcFwdTmBucketTwoRate_Object = MibTableColumn
nncCrPvpcFwdTmBucketTwoRate = _NncCrPvpcFwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 20),
    _NncCrPvpcFwdTmBucketTwoRate_Type()
)
nncCrPvpcFwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdTmBucketTwoRate.setStatus("current")


class _NncCrPvpcFwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncCrPvpcFwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncCrPvpcFwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncCrPvpcFwdTmBucketTwoMbs_Object = MibTableColumn
nncCrPvpcFwdTmBucketTwoMbs = _NncCrPvpcFwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 21),
    _NncCrPvpcFwdTmBucketTwoMbs_Type()
)
nncCrPvpcFwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdTmBucketTwoMbs.setStatus("current")


class _NncCrPvpcFwdTmCdv_Type(Integer32):
    """Custom type nncCrPvpcFwdTmCdv based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncCrPvpcFwdTmCdv_Type.__name__ = "Integer32"
_NncCrPvpcFwdTmCdv_Object = MibTableColumn
nncCrPvpcFwdTmCdv = _NncCrPvpcFwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 22),
    _NncCrPvpcFwdTmCdv_Type()
)
nncCrPvpcFwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdTmCdv.setStatus("current")


class _NncCrPvpcFwdTmClr_Type(Integer32):
    """Custom type nncCrPvpcFwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncCrPvpcFwdTmClr_Type.__name__ = "Integer32"
_NncCrPvpcFwdTmClr_Object = MibTableColumn
nncCrPvpcFwdTmClr = _NncCrPvpcFwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 23),
    _NncCrPvpcFwdTmClr_Type()
)
nncCrPvpcFwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcFwdTmClr.setStatus("current")


class _NncCrPvpcBwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncCrPvpcBwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("p0Plus1", 2),
          ("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncCrPvpcBwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncCrPvpcBwdTmTrafficDescriptor_Object = MibTableColumn
nncCrPvpcBwdTmTrafficDescriptor = _NncCrPvpcBwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 24),
    _NncCrPvpcBwdTmTrafficDescriptor_Type()
)
nncCrPvpcBwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdTmTrafficDescriptor.setStatus("current")


class _NncCrPvpcBwdTmPolicingOption_Type(Integer32):
    """Custom type nncCrPvpcBwdTmPolicingOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discard", 3),
          ("none", 0),
          ("tag", 2))
    )


_NncCrPvpcBwdTmPolicingOption_Type.__name__ = "Integer32"
_NncCrPvpcBwdTmPolicingOption_Object = MibTableColumn
nncCrPvpcBwdTmPolicingOption = _NncCrPvpcBwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 25),
    _NncCrPvpcBwdTmPolicingOption_Type()
)
nncCrPvpcBwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdTmPolicingOption.setStatus("current")


class _NncCrPvpcBwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCrPvpcBwdTmBucketOneRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvpcBwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCrPvpcBwdTmBucketOneRate_Object = MibTableColumn
nncCrPvpcBwdTmBucketOneRate = _NncCrPvpcBwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 26),
    _NncCrPvpcBwdTmBucketOneRate_Type()
)
nncCrPvpcBwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdTmBucketOneRate.setStatus("current")


class _NncCrPvpcBwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCrPvpcBwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrPvpcBwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCrPvpcBwdTmBucketOneCdvt_Object = MibTableColumn
nncCrPvpcBwdTmBucketOneCdvt = _NncCrPvpcBwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 27),
    _NncCrPvpcBwdTmBucketOneCdvt_Type()
)
nncCrPvpcBwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdTmBucketOneCdvt.setStatus("current")


class _NncCrPvpcBwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncCrPvpcBwdTmBucketTwoRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvpcBwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncCrPvpcBwdTmBucketTwoRate_Object = MibTableColumn
nncCrPvpcBwdTmBucketTwoRate = _NncCrPvpcBwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 28),
    _NncCrPvpcBwdTmBucketTwoRate_Type()
)
nncCrPvpcBwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdTmBucketTwoRate.setStatus("current")


class _NncCrPvpcBwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncCrPvpcBwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncCrPvpcBwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncCrPvpcBwdTmBucketTwoMbs_Object = MibTableColumn
nncCrPvpcBwdTmBucketTwoMbs = _NncCrPvpcBwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 29),
    _NncCrPvpcBwdTmBucketTwoMbs_Type()
)
nncCrPvpcBwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdTmBucketTwoMbs.setStatus("current")


class _NncCrPvpcBwdTmCdv_Type(Integer32):
    """Custom type nncCrPvpcBwdTmCdv based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncCrPvpcBwdTmCdv_Type.__name__ = "Integer32"
_NncCrPvpcBwdTmCdv_Object = MibTableColumn
nncCrPvpcBwdTmCdv = _NncCrPvpcBwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 30),
    _NncCrPvpcBwdTmCdv_Type()
)
nncCrPvpcBwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdTmCdv.setStatus("current")


class _NncCrPvpcBwdTmClr_Type(Integer32):
    """Custom type nncCrPvpcBwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncCrPvpcBwdTmClr_Type.__name__ = "Integer32"
_NncCrPvpcBwdTmClr_Object = MibTableColumn
nncCrPvpcBwdTmClr = _NncCrPvpcBwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 31),
    _NncCrPvpcBwdTmClr_Type()
)
nncCrPvpcBwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcBwdTmClr.setStatus("current")


class _NncCrPvpcSrcAlsConfig_Type(Integer32):
    """Custom type nncCrPvpcSrcAlsConfig based on Integer32"""
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


_NncCrPvpcSrcAlsConfig_Type.__name__ = "Integer32"
_NncCrPvpcSrcAlsConfig_Object = MibTableColumn
nncCrPvpcSrcAlsConfig = _NncCrPvpcSrcAlsConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 32),
    _NncCrPvpcSrcAlsConfig_Type()
)
nncCrPvpcSrcAlsConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcSrcAlsConfig.setStatus("current")


class _NncCrPvpcDstAlsConfig_Type(Integer32):
    """Custom type nncCrPvpcDstAlsConfig based on Integer32"""
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


_NncCrPvpcDstAlsConfig_Type.__name__ = "Integer32"
_NncCrPvpcDstAlsConfig_Object = MibTableColumn
nncCrPvpcDstAlsConfig = _NncCrPvpcDstAlsConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 33),
    _NncCrPvpcDstAlsConfig_Type()
)
nncCrPvpcDstAlsConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcDstAlsConfig.setStatus("current")


class _NncCrPvpcCreator_Type(Integer32):
    """Custom type nncCrPvpcCreator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nm5620", 2),
          ("nmti", 1),
          ("snmp", 9),
          ("unknown", 0))
    )


_NncCrPvpcCreator_Type.__name__ = "Integer32"
_NncCrPvpcCreator_Object = MibTableColumn
nncCrPvpcCreator = _NncCrPvpcCreator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 34),
    _NncCrPvpcCreator_Type()
)
nncCrPvpcCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCrPvpcCreator.setStatus("current")
_NncCrPvpcRowStatus_Type = RowStatus
_NncCrPvpcRowStatus_Object = MibTableColumn
nncCrPvpcRowStatus = _NncCrPvpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 1, 1, 35),
    _NncCrPvpcRowStatus_Type()
)
nncCrPvpcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvpcRowStatus.setStatus("current")
_NncCrPvccTable_Object = MibTable
nncCrPvccTable = _NncCrPvccTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2)
)
if mibBuilder.loadTexts:
    nncCrPvccTable.setStatus("current")
_NncCrPvccTableEntry_Object = MibTableRow
nncCrPvccTableEntry = _NncCrPvccTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1)
)
nncCrPvccTableEntry.setIndexNames(
    (0, "NNCEXTPVC-MIB", "nncCrPvccSrcIfIndex"),
    (0, "NNCEXTPVC-MIB", "nncCrPvccSrcVpi"),
    (0, "NNCEXTPVC-MIB", "nncCrPvccSrcVci"),
    (0, "NNCEXTPVC-MIB", "nncCrPvccDstIfIndex"),
    (0, "NNCEXTPVC-MIB", "nncCrPvccDstVpi"),
    (0, "NNCEXTPVC-MIB", "nncCrPvccDstVci"),
)
if mibBuilder.loadTexts:
    nncCrPvccTableEntry.setStatus("current")
_NncCrPvccSrcIfIndex_Type = InterfaceIndex
_NncCrPvccSrcIfIndex_Object = MibTableColumn
nncCrPvccSrcIfIndex = _NncCrPvccSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 1),
    _NncCrPvccSrcIfIndex_Type()
)
nncCrPvccSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvccSrcIfIndex.setStatus("current")


class _NncCrPvccSrcVpi_Type(Integer32):
    """Custom type nncCrPvccSrcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NncCrPvccSrcVpi_Type.__name__ = "Integer32"
_NncCrPvccSrcVpi_Object = MibTableColumn
nncCrPvccSrcVpi = _NncCrPvccSrcVpi_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 2),
    _NncCrPvccSrcVpi_Type()
)
nncCrPvccSrcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvccSrcVpi.setStatus("current")


class _NncCrPvccSrcVci_Type(Integer32):
    """Custom type nncCrPvccSrcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NncCrPvccSrcVci_Type.__name__ = "Integer32"
_NncCrPvccSrcVci_Object = MibTableColumn
nncCrPvccSrcVci = _NncCrPvccSrcVci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 3),
    _NncCrPvccSrcVci_Type()
)
nncCrPvccSrcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvccSrcVci.setStatus("current")
_NncCrPvccDstIfIndex_Type = InterfaceIndex
_NncCrPvccDstIfIndex_Object = MibTableColumn
nncCrPvccDstIfIndex = _NncCrPvccDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 4),
    _NncCrPvccDstIfIndex_Type()
)
nncCrPvccDstIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvccDstIfIndex.setStatus("current")


class _NncCrPvccDstVpi_Type(Integer32):
    """Custom type nncCrPvccDstVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NncCrPvccDstVpi_Type.__name__ = "Integer32"
_NncCrPvccDstVpi_Object = MibTableColumn
nncCrPvccDstVpi = _NncCrPvccDstVpi_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 5),
    _NncCrPvccDstVpi_Type()
)
nncCrPvccDstVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvccDstVpi.setStatus("current")


class _NncCrPvccDstVci_Type(Integer32):
    """Custom type nncCrPvccDstVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NncCrPvccDstVci_Type.__name__ = "Integer32"
_NncCrPvccDstVci_Object = MibTableColumn
nncCrPvccDstVci = _NncCrPvccDstVci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 6),
    _NncCrPvccDstVci_Type()
)
nncCrPvccDstVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrPvccDstVci.setStatus("current")


class _NncCrPvccCastType_Type(Integer32):
    """Custom type nncCrPvccCastType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2mp", 2),
          ("p2p", 1))
    )


_NncCrPvccCastType_Type.__name__ = "Integer32"
_NncCrPvccCastType_Object = MibTableColumn
nncCrPvccCastType = _NncCrPvccCastType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 7),
    _NncCrPvccCastType_Type()
)
nncCrPvccCastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccCastType.setStatus("current")


class _NncCrPvccFwdServiceCategory_Type(Integer32):
    """Custom type nncCrPvccFwdServiceCategory based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 3),
          ("cbr", 1),
          ("nrtvbr", 2),
          ("rtvbr", 6),
          ("ubr", 4))
    )


_NncCrPvccFwdServiceCategory_Type.__name__ = "Integer32"
_NncCrPvccFwdServiceCategory_Object = MibTableColumn
nncCrPvccFwdServiceCategory = _NncCrPvccFwdServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 8),
    _NncCrPvccFwdServiceCategory_Type()
)
nncCrPvccFwdServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdServiceCategory.setStatus("current")


class _NncCrPvccBwdServiceCategory_Type(Integer32):
    """Custom type nncCrPvccBwdServiceCategory based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 3),
          ("cbr", 1),
          ("nrtvbr", 2),
          ("rtvbr", 6),
          ("ubr", 4))
    )


_NncCrPvccBwdServiceCategory_Type.__name__ = "Integer32"
_NncCrPvccBwdServiceCategory_Object = MibTableColumn
nncCrPvccBwdServiceCategory = _NncCrPvccBwdServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 9),
    _NncCrPvccBwdServiceCategory_Type()
)
nncCrPvccBwdServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdServiceCategory.setStatus("current")


class _NncCrPvccFwdAbrDynTrfcIcr_Type(Integer32):
    """Custom type nncCrPvccFwdAbrDynTrfcIcr based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvccFwdAbrDynTrfcIcr_Type.__name__ = "Integer32"
_NncCrPvccFwdAbrDynTrfcIcr_Object = MibTableColumn
nncCrPvccFwdAbrDynTrfcIcr = _NncCrPvccFwdAbrDynTrfcIcr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 10),
    _NncCrPvccFwdAbrDynTrfcIcr_Type()
)
nncCrPvccFwdAbrDynTrfcIcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdAbrDynTrfcIcr.setStatus("current")


class _NncCrPvccFwdAbrDynTrfcRif_Type(Integer32):
    """Custom type nncCrPvccFwdAbrDynTrfcRif based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrPvccFwdAbrDynTrfcRif_Type.__name__ = "Integer32"
_NncCrPvccFwdAbrDynTrfcRif_Object = MibTableColumn
nncCrPvccFwdAbrDynTrfcRif = _NncCrPvccFwdAbrDynTrfcRif_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 11),
    _NncCrPvccFwdAbrDynTrfcRif_Type()
)
nncCrPvccFwdAbrDynTrfcRif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdAbrDynTrfcRif.setStatus("current")


class _NncCrPvccFwdAbrDynTrfcRdf_Type(Integer32):
    """Custom type nncCrPvccFwdAbrDynTrfcRdf based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrPvccFwdAbrDynTrfcRdf_Type.__name__ = "Integer32"
_NncCrPvccFwdAbrDynTrfcRdf_Object = MibTableColumn
nncCrPvccFwdAbrDynTrfcRdf = _NncCrPvccFwdAbrDynTrfcRdf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 12),
    _NncCrPvccFwdAbrDynTrfcRdf_Type()
)
nncCrPvccFwdAbrDynTrfcRdf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdAbrDynTrfcRdf.setStatus("current")


class _NncCrPvccBwdAbrDynTrfcIcr_Type(Integer32):
    """Custom type nncCrPvccBwdAbrDynTrfcIcr based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvccBwdAbrDynTrfcIcr_Type.__name__ = "Integer32"
_NncCrPvccBwdAbrDynTrfcIcr_Object = MibTableColumn
nncCrPvccBwdAbrDynTrfcIcr = _NncCrPvccBwdAbrDynTrfcIcr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 13),
    _NncCrPvccBwdAbrDynTrfcIcr_Type()
)
nncCrPvccBwdAbrDynTrfcIcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdAbrDynTrfcIcr.setStatus("current")


class _NncCrPvccBwdAbrDynTrfcRif_Type(Integer32):
    """Custom type nncCrPvccBwdAbrDynTrfcRif based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrPvccBwdAbrDynTrfcRif_Type.__name__ = "Integer32"
_NncCrPvccBwdAbrDynTrfcRif_Object = MibTableColumn
nncCrPvccBwdAbrDynTrfcRif = _NncCrPvccBwdAbrDynTrfcRif_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 14),
    _NncCrPvccBwdAbrDynTrfcRif_Type()
)
nncCrPvccBwdAbrDynTrfcRif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdAbrDynTrfcRif.setStatus("current")


class _NncCrPvccBwdAbrDynTrfcRdf_Type(Integer32):
    """Custom type nncCrPvccBwdAbrDynTrfcRdf based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrPvccBwdAbrDynTrfcRdf_Type.__name__ = "Integer32"
_NncCrPvccBwdAbrDynTrfcRdf_Object = MibTableColumn
nncCrPvccBwdAbrDynTrfcRdf = _NncCrPvccBwdAbrDynTrfcRdf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 15),
    _NncCrPvccBwdAbrDynTrfcRdf_Type()
)
nncCrPvccBwdAbrDynTrfcRdf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdAbrDynTrfcRdf.setStatus("current")


class _NncCrPvccSrcBillingFlag_Type(Integer32):
    """Custom type nncCrPvccSrcBillingFlag based on Integer32"""
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


_NncCrPvccSrcBillingFlag_Type.__name__ = "Integer32"
_NncCrPvccSrcBillingFlag_Object = MibTableColumn
nncCrPvccSrcBillingFlag = _NncCrPvccSrcBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 16),
    _NncCrPvccSrcBillingFlag_Type()
)
nncCrPvccSrcBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccSrcBillingFlag.setStatus("current")


class _NncCrPvccDstBillingFlag_Type(Integer32):
    """Custom type nncCrPvccDstBillingFlag based on Integer32"""
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


_NncCrPvccDstBillingFlag_Type.__name__ = "Integer32"
_NncCrPvccDstBillingFlag_Object = MibTableColumn
nncCrPvccDstBillingFlag = _NncCrPvccDstBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 17),
    _NncCrPvccDstBillingFlag_Type()
)
nncCrPvccDstBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccDstBillingFlag.setStatus("current")


class _NncCrPvccFwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncCrPvccFwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("p0Plus1", 2),
          ("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncCrPvccFwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncCrPvccFwdTmTrafficDescriptor_Object = MibTableColumn
nncCrPvccFwdTmTrafficDescriptor = _NncCrPvccFwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 18),
    _NncCrPvccFwdTmTrafficDescriptor_Type()
)
nncCrPvccFwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmTrafficDescriptor.setStatus("current")


class _NncCrPvccFwdTmPolicingOption_Type(Integer32):
    """Custom type nncCrPvccFwdTmPolicingOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discard", 3),
          ("none", 0),
          ("tag", 2))
    )


_NncCrPvccFwdTmPolicingOption_Type.__name__ = "Integer32"
_NncCrPvccFwdTmPolicingOption_Object = MibTableColumn
nncCrPvccFwdTmPolicingOption = _NncCrPvccFwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 19),
    _NncCrPvccFwdTmPolicingOption_Type()
)
nncCrPvccFwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmPolicingOption.setStatus("current")


class _NncCrPvccFwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCrPvccFwdTmBucketOneRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvccFwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCrPvccFwdTmBucketOneRate_Object = MibTableColumn
nncCrPvccFwdTmBucketOneRate = _NncCrPvccFwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 20),
    _NncCrPvccFwdTmBucketOneRate_Type()
)
nncCrPvccFwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmBucketOneRate.setStatus("current")


class _NncCrPvccFwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCrPvccFwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrPvccFwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCrPvccFwdTmBucketOneCdvt_Object = MibTableColumn
nncCrPvccFwdTmBucketOneCdvt = _NncCrPvccFwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 21),
    _NncCrPvccFwdTmBucketOneCdvt_Type()
)
nncCrPvccFwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmBucketOneCdvt.setStatus("current")


class _NncCrPvccFwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncCrPvccFwdTmBucketTwoRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvccFwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncCrPvccFwdTmBucketTwoRate_Object = MibTableColumn
nncCrPvccFwdTmBucketTwoRate = _NncCrPvccFwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 22),
    _NncCrPvccFwdTmBucketTwoRate_Type()
)
nncCrPvccFwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmBucketTwoRate.setStatus("current")


class _NncCrPvccFwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncCrPvccFwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncCrPvccFwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncCrPvccFwdTmBucketTwoMbs_Object = MibTableColumn
nncCrPvccFwdTmBucketTwoMbs = _NncCrPvccFwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 23),
    _NncCrPvccFwdTmBucketTwoMbs_Type()
)
nncCrPvccFwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmBucketTwoMbs.setStatus("current")


class _NncCrPvccFwdTmCdv_Type(Integer32):
    """Custom type nncCrPvccFwdTmCdv based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncCrPvccFwdTmCdv_Type.__name__ = "Integer32"
_NncCrPvccFwdTmCdv_Object = MibTableColumn
nncCrPvccFwdTmCdv = _NncCrPvccFwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 24),
    _NncCrPvccFwdTmCdv_Type()
)
nncCrPvccFwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmCdv.setStatus("current")


class _NncCrPvccFwdTmClr_Type(Integer32):
    """Custom type nncCrPvccFwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncCrPvccFwdTmClr_Type.__name__ = "Integer32"
_NncCrPvccFwdTmClr_Object = MibTableColumn
nncCrPvccFwdTmClr = _NncCrPvccFwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 25),
    _NncCrPvccFwdTmClr_Type()
)
nncCrPvccFwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmClr.setStatus("current")


class _NncCrPvccFwdTmFrameDiscard_Type(Integer32):
    """Custom type nncCrPvccFwdTmFrameDiscard based on Integer32"""
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


_NncCrPvccFwdTmFrameDiscard_Type.__name__ = "Integer32"
_NncCrPvccFwdTmFrameDiscard_Object = MibTableColumn
nncCrPvccFwdTmFrameDiscard = _NncCrPvccFwdTmFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 26),
    _NncCrPvccFwdTmFrameDiscard_Type()
)
nncCrPvccFwdTmFrameDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccFwdTmFrameDiscard.setStatus("current")


class _NncCrPvccBwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncCrPvccBwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("p0Plus1", 2),
          ("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncCrPvccBwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncCrPvccBwdTmTrafficDescriptor_Object = MibTableColumn
nncCrPvccBwdTmTrafficDescriptor = _NncCrPvccBwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 27),
    _NncCrPvccBwdTmTrafficDescriptor_Type()
)
nncCrPvccBwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmTrafficDescriptor.setStatus("current")


class _NncCrPvccBwdTmPolicingOption_Type(Integer32):
    """Custom type nncCrPvccBwdTmPolicingOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discard", 3),
          ("none", 0),
          ("tag", 2))
    )


_NncCrPvccBwdTmPolicingOption_Type.__name__ = "Integer32"
_NncCrPvccBwdTmPolicingOption_Object = MibTableColumn
nncCrPvccBwdTmPolicingOption = _NncCrPvccBwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 28),
    _NncCrPvccBwdTmPolicingOption_Type()
)
nncCrPvccBwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmPolicingOption.setStatus("current")


class _NncCrPvccBwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCrPvccBwdTmBucketOneRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvccBwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCrPvccBwdTmBucketOneRate_Object = MibTableColumn
nncCrPvccBwdTmBucketOneRate = _NncCrPvccBwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 29),
    _NncCrPvccBwdTmBucketOneRate_Type()
)
nncCrPvccBwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmBucketOneRate.setStatus("current")


class _NncCrPvccBwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCrPvccBwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrPvccBwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCrPvccBwdTmBucketOneCdvt_Object = MibTableColumn
nncCrPvccBwdTmBucketOneCdvt = _NncCrPvccBwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 30),
    _NncCrPvccBwdTmBucketOneCdvt_Type()
)
nncCrPvccBwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmBucketOneCdvt.setStatus("current")


class _NncCrPvccBwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncCrPvccBwdTmBucketTwoRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrPvccBwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncCrPvccBwdTmBucketTwoRate_Object = MibTableColumn
nncCrPvccBwdTmBucketTwoRate = _NncCrPvccBwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 31),
    _NncCrPvccBwdTmBucketTwoRate_Type()
)
nncCrPvccBwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmBucketTwoRate.setStatus("current")


class _NncCrPvccBwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncCrPvccBwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncCrPvccBwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncCrPvccBwdTmBucketTwoMbs_Object = MibTableColumn
nncCrPvccBwdTmBucketTwoMbs = _NncCrPvccBwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 32),
    _NncCrPvccBwdTmBucketTwoMbs_Type()
)
nncCrPvccBwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmBucketTwoMbs.setStatus("current")


class _NncCrPvccBwdTmCdv_Type(Integer32):
    """Custom type nncCrPvccBwdTmCdv based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncCrPvccBwdTmCdv_Type.__name__ = "Integer32"
_NncCrPvccBwdTmCdv_Object = MibTableColumn
nncCrPvccBwdTmCdv = _NncCrPvccBwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 33),
    _NncCrPvccBwdTmCdv_Type()
)
nncCrPvccBwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmCdv.setStatus("current")


class _NncCrPvccBwdTmClr_Type(Integer32):
    """Custom type nncCrPvccBwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncCrPvccBwdTmClr_Type.__name__ = "Integer32"
_NncCrPvccBwdTmClr_Object = MibTableColumn
nncCrPvccBwdTmClr = _NncCrPvccBwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 34),
    _NncCrPvccBwdTmClr_Type()
)
nncCrPvccBwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmClr.setStatus("current")


class _NncCrPvccBwdTmFrameDiscard_Type(Integer32):
    """Custom type nncCrPvccBwdTmFrameDiscard based on Integer32"""
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


_NncCrPvccBwdTmFrameDiscard_Type.__name__ = "Integer32"
_NncCrPvccBwdTmFrameDiscard_Object = MibTableColumn
nncCrPvccBwdTmFrameDiscard = _NncCrPvccBwdTmFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 35),
    _NncCrPvccBwdTmFrameDiscard_Type()
)
nncCrPvccBwdTmFrameDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccBwdTmFrameDiscard.setStatus("current")


class _NncCrPvccSrcAlsConfig_Type(Integer32):
    """Custom type nncCrPvccSrcAlsConfig based on Integer32"""
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


_NncCrPvccSrcAlsConfig_Type.__name__ = "Integer32"
_NncCrPvccSrcAlsConfig_Object = MibTableColumn
nncCrPvccSrcAlsConfig = _NncCrPvccSrcAlsConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 36),
    _NncCrPvccSrcAlsConfig_Type()
)
nncCrPvccSrcAlsConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccSrcAlsConfig.setStatus("current")


class _NncCrPvccDstAlsConfig_Type(Integer32):
    """Custom type nncCrPvccDstAlsConfig based on Integer32"""
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


_NncCrPvccDstAlsConfig_Type.__name__ = "Integer32"
_NncCrPvccDstAlsConfig_Object = MibTableColumn
nncCrPvccDstAlsConfig = _NncCrPvccDstAlsConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 37),
    _NncCrPvccDstAlsConfig_Type()
)
nncCrPvccDstAlsConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccDstAlsConfig.setStatus("current")


class _NncCrPvccCreator_Type(Integer32):
    """Custom type nncCrPvccCreator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nm5620", 2),
          ("nmti", 1),
          ("snmp", 9),
          ("unknown", 0))
    )


_NncCrPvccCreator_Type.__name__ = "Integer32"
_NncCrPvccCreator_Object = MibTableColumn
nncCrPvccCreator = _NncCrPvccCreator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 38),
    _NncCrPvccCreator_Type()
)
nncCrPvccCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCrPvccCreator.setStatus("current")
_NncCrPvccRowStatus_Type = RowStatus
_NncCrPvccRowStatus_Object = MibTableColumn
nncCrPvccRowStatus = _NncCrPvccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 1, 2, 1, 39),
    _NncCrPvccRowStatus_Type()
)
nncCrPvccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrPvccRowStatus.setStatus("current")
_NncExtPvcGroups_ObjectIdentity = ObjectIdentity
nncExtPvcGroups = _NncExtPvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 3)
)
_NncExtPvcCompliances_ObjectIdentity = ObjectIdentity
nncExtPvcCompliances = _NncExtPvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 4)
)

# Managed Objects groups

nncCrPvpcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 3, 1)
)
nncCrPvpcGroup.setObjects(
      *(("NNCEXTPVC-MIB", "nncCrPvpcSrcIfIndex"),
        ("NNCEXTPVC-MIB", "nncCrPvpcSrcVpi"),
        ("NNCEXTPVC-MIB", "nncCrPvpcDstIfIndex"),
        ("NNCEXTPVC-MIB", "nncCrPvpcDstVpi"),
        ("NNCEXTPVC-MIB", "nncCrPvpcCastType"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdServiceCategory"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdServiceCategory"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdAbrDynTrfcIcr"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdAbrDynTrfcRif"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdAbrDynTrfcRdf"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdAbrDynTrfcIcr"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdAbrDynTrfcRif"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdAbrDynTrfcRdf"),
        ("NNCEXTPVC-MIB", "nncCrPvpcSrcBillingFlag"),
        ("NNCEXTPVC-MIB", "nncCrPvpcDstBillingFlag"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdTmTrafficDescriptor"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdTmPolicingOption"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdTmBucketOneRate"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdTmBucketOneCdvt"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdTmBucketTwoRate"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdTmBucketTwoMbs"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdTmCdv"),
        ("NNCEXTPVC-MIB", "nncCrPvpcFwdTmClr"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdTmTrafficDescriptor"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdTmPolicingOption"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdTmBucketOneRate"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdTmBucketOneCdvt"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdTmBucketTwoRate"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdTmBucketTwoMbs"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdTmCdv"),
        ("NNCEXTPVC-MIB", "nncCrPvpcBwdTmClr"),
        ("NNCEXTPVC-MIB", "nncCrPvpcSrcAlsConfig"),
        ("NNCEXTPVC-MIB", "nncCrPvpcDstAlsConfig"),
        ("NNCEXTPVC-MIB", "nncCrPvpcCreator"),
        ("NNCEXTPVC-MIB", "nncCrPvpcRowStatus"))
)
if mibBuilder.loadTexts:
    nncCrPvpcGroup.setStatus("current")

nncCrPvccGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 3, 2)
)
nncCrPvccGroup.setObjects(
      *(("NNCEXTPVC-MIB", "nncCrPvccSrcIfIndex"),
        ("NNCEXTPVC-MIB", "nncCrPvccSrcVpi"),
        ("NNCEXTPVC-MIB", "nncCrPvccSrcVci"),
        ("NNCEXTPVC-MIB", "nncCrPvccDstIfIndex"),
        ("NNCEXTPVC-MIB", "nncCrPvccDstVpi"),
        ("NNCEXTPVC-MIB", "nncCrPvccDstVci"),
        ("NNCEXTPVC-MIB", "nncCrPvccCastType"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdServiceCategory"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdServiceCategory"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdAbrDynTrfcIcr"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdAbrDynTrfcRif"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdAbrDynTrfcRdf"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdAbrDynTrfcIcr"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdAbrDynTrfcRif"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdAbrDynTrfcRdf"),
        ("NNCEXTPVC-MIB", "nncCrPvccSrcBillingFlag"),
        ("NNCEXTPVC-MIB", "nncCrPvccDstBillingFlag"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmTrafficDescriptor"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmPolicingOption"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmBucketOneRate"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmBucketOneCdvt"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmBucketTwoRate"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmBucketTwoMbs"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmCdv"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmClr"),
        ("NNCEXTPVC-MIB", "nncCrPvccFwdTmFrameDiscard"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmTrafficDescriptor"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmPolicingOption"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmBucketOneRate"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmBucketOneCdvt"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmBucketTwoRate"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmBucketTwoMbs"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmCdv"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmClr"),
        ("NNCEXTPVC-MIB", "nncCrPvccBwdTmFrameDiscard"),
        ("NNCEXTPVC-MIB", "nncCrPvccSrcAlsConfig"),
        ("NNCEXTPVC-MIB", "nncCrPvccDstAlsConfig"),
        ("NNCEXTPVC-MIB", "nncCrPvccCreator"),
        ("NNCEXTPVC-MIB", "nncCrPvccRowStatus"))
)
if mibBuilder.loadTexts:
    nncCrPvccGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncPvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 79, 4, 1)
)
if mibBuilder.loadTexts:
    nncPvcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCEXTPVC-MIB",
    **{"nncExtPvc": nncExtPvc,
       "nncExtPvcObjects": nncExtPvcObjects,
       "nncCrPvpcTable": nncCrPvpcTable,
       "nncCrPvpcTableEntry": nncCrPvpcTableEntry,
       "nncCrPvpcSrcIfIndex": nncCrPvpcSrcIfIndex,
       "nncCrPvpcSrcVpi": nncCrPvpcSrcVpi,
       "nncCrPvpcDstIfIndex": nncCrPvpcDstIfIndex,
       "nncCrPvpcDstVpi": nncCrPvpcDstVpi,
       "nncCrPvpcCastType": nncCrPvpcCastType,
       "nncCrPvpcFwdServiceCategory": nncCrPvpcFwdServiceCategory,
       "nncCrPvpcBwdServiceCategory": nncCrPvpcBwdServiceCategory,
       "nncCrPvpcFwdAbrDynTrfcIcr": nncCrPvpcFwdAbrDynTrfcIcr,
       "nncCrPvpcFwdAbrDynTrfcRif": nncCrPvpcFwdAbrDynTrfcRif,
       "nncCrPvpcFwdAbrDynTrfcRdf": nncCrPvpcFwdAbrDynTrfcRdf,
       "nncCrPvpcBwdAbrDynTrfcIcr": nncCrPvpcBwdAbrDynTrfcIcr,
       "nncCrPvpcBwdAbrDynTrfcRif": nncCrPvpcBwdAbrDynTrfcRif,
       "nncCrPvpcBwdAbrDynTrfcRdf": nncCrPvpcBwdAbrDynTrfcRdf,
       "nncCrPvpcSrcBillingFlag": nncCrPvpcSrcBillingFlag,
       "nncCrPvpcDstBillingFlag": nncCrPvpcDstBillingFlag,
       "nncCrPvpcFwdTmTrafficDescriptor": nncCrPvpcFwdTmTrafficDescriptor,
       "nncCrPvpcFwdTmPolicingOption": nncCrPvpcFwdTmPolicingOption,
       "nncCrPvpcFwdTmBucketOneRate": nncCrPvpcFwdTmBucketOneRate,
       "nncCrPvpcFwdTmBucketOneCdvt": nncCrPvpcFwdTmBucketOneCdvt,
       "nncCrPvpcFwdTmBucketTwoRate": nncCrPvpcFwdTmBucketTwoRate,
       "nncCrPvpcFwdTmBucketTwoMbs": nncCrPvpcFwdTmBucketTwoMbs,
       "nncCrPvpcFwdTmCdv": nncCrPvpcFwdTmCdv,
       "nncCrPvpcFwdTmClr": nncCrPvpcFwdTmClr,
       "nncCrPvpcBwdTmTrafficDescriptor": nncCrPvpcBwdTmTrafficDescriptor,
       "nncCrPvpcBwdTmPolicingOption": nncCrPvpcBwdTmPolicingOption,
       "nncCrPvpcBwdTmBucketOneRate": nncCrPvpcBwdTmBucketOneRate,
       "nncCrPvpcBwdTmBucketOneCdvt": nncCrPvpcBwdTmBucketOneCdvt,
       "nncCrPvpcBwdTmBucketTwoRate": nncCrPvpcBwdTmBucketTwoRate,
       "nncCrPvpcBwdTmBucketTwoMbs": nncCrPvpcBwdTmBucketTwoMbs,
       "nncCrPvpcBwdTmCdv": nncCrPvpcBwdTmCdv,
       "nncCrPvpcBwdTmClr": nncCrPvpcBwdTmClr,
       "nncCrPvpcSrcAlsConfig": nncCrPvpcSrcAlsConfig,
       "nncCrPvpcDstAlsConfig": nncCrPvpcDstAlsConfig,
       "nncCrPvpcCreator": nncCrPvpcCreator,
       "nncCrPvpcRowStatus": nncCrPvpcRowStatus,
       "nncCrPvccTable": nncCrPvccTable,
       "nncCrPvccTableEntry": nncCrPvccTableEntry,
       "nncCrPvccSrcIfIndex": nncCrPvccSrcIfIndex,
       "nncCrPvccSrcVpi": nncCrPvccSrcVpi,
       "nncCrPvccSrcVci": nncCrPvccSrcVci,
       "nncCrPvccDstIfIndex": nncCrPvccDstIfIndex,
       "nncCrPvccDstVpi": nncCrPvccDstVpi,
       "nncCrPvccDstVci": nncCrPvccDstVci,
       "nncCrPvccCastType": nncCrPvccCastType,
       "nncCrPvccFwdServiceCategory": nncCrPvccFwdServiceCategory,
       "nncCrPvccBwdServiceCategory": nncCrPvccBwdServiceCategory,
       "nncCrPvccFwdAbrDynTrfcIcr": nncCrPvccFwdAbrDynTrfcIcr,
       "nncCrPvccFwdAbrDynTrfcRif": nncCrPvccFwdAbrDynTrfcRif,
       "nncCrPvccFwdAbrDynTrfcRdf": nncCrPvccFwdAbrDynTrfcRdf,
       "nncCrPvccBwdAbrDynTrfcIcr": nncCrPvccBwdAbrDynTrfcIcr,
       "nncCrPvccBwdAbrDynTrfcRif": nncCrPvccBwdAbrDynTrfcRif,
       "nncCrPvccBwdAbrDynTrfcRdf": nncCrPvccBwdAbrDynTrfcRdf,
       "nncCrPvccSrcBillingFlag": nncCrPvccSrcBillingFlag,
       "nncCrPvccDstBillingFlag": nncCrPvccDstBillingFlag,
       "nncCrPvccFwdTmTrafficDescriptor": nncCrPvccFwdTmTrafficDescriptor,
       "nncCrPvccFwdTmPolicingOption": nncCrPvccFwdTmPolicingOption,
       "nncCrPvccFwdTmBucketOneRate": nncCrPvccFwdTmBucketOneRate,
       "nncCrPvccFwdTmBucketOneCdvt": nncCrPvccFwdTmBucketOneCdvt,
       "nncCrPvccFwdTmBucketTwoRate": nncCrPvccFwdTmBucketTwoRate,
       "nncCrPvccFwdTmBucketTwoMbs": nncCrPvccFwdTmBucketTwoMbs,
       "nncCrPvccFwdTmCdv": nncCrPvccFwdTmCdv,
       "nncCrPvccFwdTmClr": nncCrPvccFwdTmClr,
       "nncCrPvccFwdTmFrameDiscard": nncCrPvccFwdTmFrameDiscard,
       "nncCrPvccBwdTmTrafficDescriptor": nncCrPvccBwdTmTrafficDescriptor,
       "nncCrPvccBwdTmPolicingOption": nncCrPvccBwdTmPolicingOption,
       "nncCrPvccBwdTmBucketOneRate": nncCrPvccBwdTmBucketOneRate,
       "nncCrPvccBwdTmBucketOneCdvt": nncCrPvccBwdTmBucketOneCdvt,
       "nncCrPvccBwdTmBucketTwoRate": nncCrPvccBwdTmBucketTwoRate,
       "nncCrPvccBwdTmBucketTwoMbs": nncCrPvccBwdTmBucketTwoMbs,
       "nncCrPvccBwdTmCdv": nncCrPvccBwdTmCdv,
       "nncCrPvccBwdTmClr": nncCrPvccBwdTmClr,
       "nncCrPvccBwdTmFrameDiscard": nncCrPvccBwdTmFrameDiscard,
       "nncCrPvccSrcAlsConfig": nncCrPvccSrcAlsConfig,
       "nncCrPvccDstAlsConfig": nncCrPvccDstAlsConfig,
       "nncCrPvccCreator": nncCrPvccCreator,
       "nncCrPvccRowStatus": nncCrPvccRowStatus,
       "nncExtPvcGroups": nncExtPvcGroups,
       "nncCrPvpcGroup": nncCrPvpcGroup,
       "nncCrPvccGroup": nncCrPvccGroup,
       "nncExtPvcCompliances": nncExtPvcCompliances,
       "nncPvcCompliance": nncPvcCompliance}
)
