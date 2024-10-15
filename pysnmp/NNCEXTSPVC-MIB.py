# SNMP MIB module (NNCEXTSPVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCEXTSPVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:21 2024
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

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

nncExtSpvc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 82)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmFormatDisplay(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x-2x-10x-6x-1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_NncExtSpvcObjects_ObjectIdentity = ObjectIdentity
nncExtSpvcObjects = _NncExtSpvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1)
)
_NncCrSpvpcTable_Object = MibTable
nncCrSpvpcTable = _NncCrSpvpcTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1)
)
if mibBuilder.loadTexts:
    nncCrSpvpcTable.setStatus("current")
_NncCrSpvpcTableEntry_Object = MibTableRow
nncCrSpvpcTableEntry = _NncCrSpvpcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1)
)
nncCrSpvpcTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    nncCrSpvpcTableEntry.setStatus("current")


class _NncCrSpvpcServiceCategory_Type(Integer32):
    """Custom type nncCrSpvpcServiceCategory based on Integer32"""
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


_NncCrSpvpcServiceCategory_Type.__name__ = "Integer32"
_NncCrSpvpcServiceCategory_Object = MibTableColumn
nncCrSpvpcServiceCategory = _NncCrSpvpcServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 1),
    _NncCrSpvpcServiceCategory_Type()
)
nncCrSpvpcServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcServiceCategory.setStatus("current")
_NncCrSpvpcTargEpAddr_Type = AtmFormatDisplay
_NncCrSpvpcTargEpAddr_Object = MibTableColumn
nncCrSpvpcTargEpAddr = _NncCrSpvpcTargEpAddr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 2),
    _NncCrSpvpcTargEpAddr_Type()
)
nncCrSpvpcTargEpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcTargEpAddr.setStatus("current")


class _NncCrSpvpcTargVpi_Type(Integer32):
    """Custom type nncCrSpvpcTargVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NncCrSpvpcTargVpi_Type.__name__ = "Integer32"
_NncCrSpvpcTargVpi_Object = MibTableColumn
nncCrSpvpcTargVpi = _NncCrSpvpcTargVpi_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 3),
    _NncCrSpvpcTargVpi_Type()
)
nncCrSpvpcTargVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcTargVpi.setStatus("current")


class _NncCrSpvpcAdminStatus_Type(Integer32):
    """Custom type nncCrSpvpcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NncCrSpvpcAdminStatus_Type.__name__ = "Integer32"
_NncCrSpvpcAdminStatus_Object = MibTableColumn
nncCrSpvpcAdminStatus = _NncCrSpvpcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 4),
    _NncCrSpvpcAdminStatus_Type()
)
nncCrSpvpcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcAdminStatus.setStatus("current")


class _NncCrSpvpcPriority_Type(Integer32):
    """Custom type nncCrSpvpcPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NncCrSpvpcPriority_Type.__name__ = "Integer32"
_NncCrSpvpcPriority_Object = MibTableColumn
nncCrSpvpcPriority = _NncCrSpvpcPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 5),
    _NncCrSpvpcPriority_Type()
)
nncCrSpvpcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcPriority.setStatus("current")


class _NncCrSpvpcMaxAdminWeight_Type(Integer32):
    """Custom type nncCrSpvpcMaxAdminWeight based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NncCrSpvpcMaxAdminWeight_Type.__name__ = "Integer32"
_NncCrSpvpcMaxAdminWeight_Object = MibTableColumn
nncCrSpvpcMaxAdminWeight = _NncCrSpvpcMaxAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 6),
    _NncCrSpvpcMaxAdminWeight_Type()
)
nncCrSpvpcMaxAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcMaxAdminWeight.setStatus("current")


class _NncCrSpvpcOperation_Type(Integer32):
    """Custom type nncCrSpvpcOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("reRouteDualEp", 7)
    )


_NncCrSpvpcOperation_Type.__name__ = "Integer32"
_NncCrSpvpcOperation_Object = MibTableColumn
nncCrSpvpcOperation = _NncCrSpvpcOperation_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 7),
    _NncCrSpvpcOperation_Type()
)
nncCrSpvpcOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcOperation.setStatus("current")


class _NncCrSpvpcCallStatus_Type(Integer32):
    """Custom type nncCrSpvpcCallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("readyToConnect", 7),
          ("waitingForResources", 4))
    )


_NncCrSpvpcCallStatus_Type.__name__ = "Integer32"
_NncCrSpvpcCallStatus_Object = MibTableColumn
nncCrSpvpcCallStatus = _NncCrSpvpcCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 8),
    _NncCrSpvpcCallStatus_Type()
)
nncCrSpvpcCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCrSpvpcCallStatus.setStatus("current")


class _NncCrSpvpcLocRerouteConfig_Type(Integer32):
    """Custom type nncCrSpvpcLocRerouteConfig based on Integer32"""
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
        *(("disabled", 1),
          ("enabledNniSide", 3),
          ("enabledUniSide", 2))
    )


_NncCrSpvpcLocRerouteConfig_Type.__name__ = "Integer32"
_NncCrSpvpcLocRerouteConfig_Object = MibTableColumn
nncCrSpvpcLocRerouteConfig = _NncCrSpvpcLocRerouteConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 9),
    _NncCrSpvpcLocRerouteConfig_Type()
)
nncCrSpvpcLocRerouteConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcLocRerouteConfig.setStatus("current")


class _NncCrSpvpcFwdAbrDynTrfcIcr_Type(Integer32):
    """Custom type nncCrSpvpcFwdAbrDynTrfcIcr based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvpcFwdAbrDynTrfcIcr_Type.__name__ = "Integer32"
_NncCrSpvpcFwdAbrDynTrfcIcr_Object = MibTableColumn
nncCrSpvpcFwdAbrDynTrfcIcr = _NncCrSpvpcFwdAbrDynTrfcIcr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 10),
    _NncCrSpvpcFwdAbrDynTrfcIcr_Type()
)
nncCrSpvpcFwdAbrDynTrfcIcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdAbrDynTrfcIcr.setStatus("current")


class _NncCrSpvpcFwdAbrDynTrfcRif_Type(Integer32):
    """Custom type nncCrSpvpcFwdAbrDynTrfcRif based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrSpvpcFwdAbrDynTrfcRif_Type.__name__ = "Integer32"
_NncCrSpvpcFwdAbrDynTrfcRif_Object = MibTableColumn
nncCrSpvpcFwdAbrDynTrfcRif = _NncCrSpvpcFwdAbrDynTrfcRif_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 11),
    _NncCrSpvpcFwdAbrDynTrfcRif_Type()
)
nncCrSpvpcFwdAbrDynTrfcRif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdAbrDynTrfcRif.setStatus("current")


class _NncCrSpvpcFwdAbrDynTrfcRdf_Type(Integer32):
    """Custom type nncCrSpvpcFwdAbrDynTrfcRdf based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrSpvpcFwdAbrDynTrfcRdf_Type.__name__ = "Integer32"
_NncCrSpvpcFwdAbrDynTrfcRdf_Object = MibTableColumn
nncCrSpvpcFwdAbrDynTrfcRdf = _NncCrSpvpcFwdAbrDynTrfcRdf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 12),
    _NncCrSpvpcFwdAbrDynTrfcRdf_Type()
)
nncCrSpvpcFwdAbrDynTrfcRdf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdAbrDynTrfcRdf.setStatus("current")


class _NncCrSpvpcBwdAbrDynTrfcIcr_Type(Integer32):
    """Custom type nncCrSpvpcBwdAbrDynTrfcIcr based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvpcBwdAbrDynTrfcIcr_Type.__name__ = "Integer32"
_NncCrSpvpcBwdAbrDynTrfcIcr_Object = MibTableColumn
nncCrSpvpcBwdAbrDynTrfcIcr = _NncCrSpvpcBwdAbrDynTrfcIcr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 13),
    _NncCrSpvpcBwdAbrDynTrfcIcr_Type()
)
nncCrSpvpcBwdAbrDynTrfcIcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdAbrDynTrfcIcr.setStatus("current")


class _NncCrSpvpcBwdAbrDynTrfcRif_Type(Integer32):
    """Custom type nncCrSpvpcBwdAbrDynTrfcRif based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrSpvpcBwdAbrDynTrfcRif_Type.__name__ = "Integer32"
_NncCrSpvpcBwdAbrDynTrfcRif_Object = MibTableColumn
nncCrSpvpcBwdAbrDynTrfcRif = _NncCrSpvpcBwdAbrDynTrfcRif_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 14),
    _NncCrSpvpcBwdAbrDynTrfcRif_Type()
)
nncCrSpvpcBwdAbrDynTrfcRif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdAbrDynTrfcRif.setStatus("current")


class _NncCrSpvpcBwdAbrDynTrfcRdf_Type(Integer32):
    """Custom type nncCrSpvpcBwdAbrDynTrfcRdf based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrSpvpcBwdAbrDynTrfcRdf_Type.__name__ = "Integer32"
_NncCrSpvpcBwdAbrDynTrfcRdf_Object = MibTableColumn
nncCrSpvpcBwdAbrDynTrfcRdf = _NncCrSpvpcBwdAbrDynTrfcRdf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 15),
    _NncCrSpvpcBwdAbrDynTrfcRdf_Type()
)
nncCrSpvpcBwdAbrDynTrfcRdf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdAbrDynTrfcRdf.setStatus("current")


class _NncCrSpvpcSrcBillingFlag_Type(Integer32):
    """Custom type nncCrSpvpcSrcBillingFlag based on Integer32"""
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


_NncCrSpvpcSrcBillingFlag_Type.__name__ = "Integer32"
_NncCrSpvpcSrcBillingFlag_Object = MibTableColumn
nncCrSpvpcSrcBillingFlag = _NncCrSpvpcSrcBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 16),
    _NncCrSpvpcSrcBillingFlag_Type()
)
nncCrSpvpcSrcBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcSrcBillingFlag.setStatus("current")


class _NncCrSpvpcFwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncCrSpvpcFwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

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
        *(("p0Plus1", 2),
          ("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncCrSpvpcFwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncCrSpvpcFwdTmTrafficDescriptor_Object = MibTableColumn
nncCrSpvpcFwdTmTrafficDescriptor = _NncCrSpvpcFwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 17),
    _NncCrSpvpcFwdTmTrafficDescriptor_Type()
)
nncCrSpvpcFwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdTmTrafficDescriptor.setStatus("current")


class _NncCrSpvpcFwdTmPolicingOption_Type(Integer32):
    """Custom type nncCrSpvpcFwdTmPolicingOption based on Integer32"""
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
        *(("disabled", 1),
          ("discard", 3),
          ("tag", 2))
    )


_NncCrSpvpcFwdTmPolicingOption_Type.__name__ = "Integer32"
_NncCrSpvpcFwdTmPolicingOption_Object = MibTableColumn
nncCrSpvpcFwdTmPolicingOption = _NncCrSpvpcFwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 18),
    _NncCrSpvpcFwdTmPolicingOption_Type()
)
nncCrSpvpcFwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdTmPolicingOption.setStatus("current")


class _NncCrSpvpcFwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCrSpvpcFwdTmBucketOneRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvpcFwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCrSpvpcFwdTmBucketOneRate_Object = MibTableColumn
nncCrSpvpcFwdTmBucketOneRate = _NncCrSpvpcFwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 19),
    _NncCrSpvpcFwdTmBucketOneRate_Type()
)
nncCrSpvpcFwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdTmBucketOneRate.setStatus("current")


class _NncCrSpvpcFwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCrSpvpcFwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrSpvpcFwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCrSpvpcFwdTmBucketOneCdvt_Object = MibTableColumn
nncCrSpvpcFwdTmBucketOneCdvt = _NncCrSpvpcFwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 20),
    _NncCrSpvpcFwdTmBucketOneCdvt_Type()
)
nncCrSpvpcFwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdTmBucketOneCdvt.setStatus("current")


class _NncCrSpvpcFwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncCrSpvpcFwdTmBucketTwoRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvpcFwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncCrSpvpcFwdTmBucketTwoRate_Object = MibTableColumn
nncCrSpvpcFwdTmBucketTwoRate = _NncCrSpvpcFwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 21),
    _NncCrSpvpcFwdTmBucketTwoRate_Type()
)
nncCrSpvpcFwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdTmBucketTwoRate.setStatus("current")


class _NncCrSpvpcFwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncCrSpvpcFwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncCrSpvpcFwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncCrSpvpcFwdTmBucketTwoMbs_Object = MibTableColumn
nncCrSpvpcFwdTmBucketTwoMbs = _NncCrSpvpcFwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 22),
    _NncCrSpvpcFwdTmBucketTwoMbs_Type()
)
nncCrSpvpcFwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdTmBucketTwoMbs.setStatus("current")


class _NncCrSpvpcFwdTmCdv_Type(Integer32):
    """Custom type nncCrSpvpcFwdTmCdv based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncCrSpvpcFwdTmCdv_Type.__name__ = "Integer32"
_NncCrSpvpcFwdTmCdv_Object = MibTableColumn
nncCrSpvpcFwdTmCdv = _NncCrSpvpcFwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 23),
    _NncCrSpvpcFwdTmCdv_Type()
)
nncCrSpvpcFwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdTmCdv.setStatus("current")


class _NncCrSpvpcFwdTmClr_Type(Integer32):
    """Custom type nncCrSpvpcFwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncCrSpvpcFwdTmClr_Type.__name__ = "Integer32"
_NncCrSpvpcFwdTmClr_Object = MibTableColumn
nncCrSpvpcFwdTmClr = _NncCrSpvpcFwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 24),
    _NncCrSpvpcFwdTmClr_Type()
)
nncCrSpvpcFwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcFwdTmClr.setStatus("current")


class _NncCrSpvpcBwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncCrSpvpcBwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

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
        *(("p0Plus1", 2),
          ("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncCrSpvpcBwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncCrSpvpcBwdTmTrafficDescriptor_Object = MibTableColumn
nncCrSpvpcBwdTmTrafficDescriptor = _NncCrSpvpcBwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 25),
    _NncCrSpvpcBwdTmTrafficDescriptor_Type()
)
nncCrSpvpcBwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdTmTrafficDescriptor.setStatus("current")


class _NncCrSpvpcBwdTmPolicingOption_Type(Integer32):
    """Custom type nncCrSpvpcBwdTmPolicingOption based on Integer32"""
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
        *(("disabled", 1),
          ("discard", 3),
          ("tag", 2))
    )


_NncCrSpvpcBwdTmPolicingOption_Type.__name__ = "Integer32"
_NncCrSpvpcBwdTmPolicingOption_Object = MibTableColumn
nncCrSpvpcBwdTmPolicingOption = _NncCrSpvpcBwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 26),
    _NncCrSpvpcBwdTmPolicingOption_Type()
)
nncCrSpvpcBwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdTmPolicingOption.setStatus("current")


class _NncCrSpvpcBwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCrSpvpcBwdTmBucketOneRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvpcBwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCrSpvpcBwdTmBucketOneRate_Object = MibTableColumn
nncCrSpvpcBwdTmBucketOneRate = _NncCrSpvpcBwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 27),
    _NncCrSpvpcBwdTmBucketOneRate_Type()
)
nncCrSpvpcBwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdTmBucketOneRate.setStatus("current")


class _NncCrSpvpcBwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCrSpvpcBwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrSpvpcBwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCrSpvpcBwdTmBucketOneCdvt_Object = MibTableColumn
nncCrSpvpcBwdTmBucketOneCdvt = _NncCrSpvpcBwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 28),
    _NncCrSpvpcBwdTmBucketOneCdvt_Type()
)
nncCrSpvpcBwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdTmBucketOneCdvt.setStatus("current")


class _NncCrSpvpcBwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncCrSpvpcBwdTmBucketTwoRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvpcBwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncCrSpvpcBwdTmBucketTwoRate_Object = MibTableColumn
nncCrSpvpcBwdTmBucketTwoRate = _NncCrSpvpcBwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 29),
    _NncCrSpvpcBwdTmBucketTwoRate_Type()
)
nncCrSpvpcBwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdTmBucketTwoRate.setStatus("current")


class _NncCrSpvpcBwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncCrSpvpcBwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncCrSpvpcBwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncCrSpvpcBwdTmBucketTwoMbs_Object = MibTableColumn
nncCrSpvpcBwdTmBucketTwoMbs = _NncCrSpvpcBwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 30),
    _NncCrSpvpcBwdTmBucketTwoMbs_Type()
)
nncCrSpvpcBwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdTmBucketTwoMbs.setStatus("current")


class _NncCrSpvpcBwdTmCdv_Type(Integer32):
    """Custom type nncCrSpvpcBwdTmCdv based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncCrSpvpcBwdTmCdv_Type.__name__ = "Integer32"
_NncCrSpvpcBwdTmCdv_Object = MibTableColumn
nncCrSpvpcBwdTmCdv = _NncCrSpvpcBwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 31),
    _NncCrSpvpcBwdTmCdv_Type()
)
nncCrSpvpcBwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdTmCdv.setStatus("current")


class _NncCrSpvpcBwdTmClr_Type(Integer32):
    """Custom type nncCrSpvpcBwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncCrSpvpcBwdTmClr_Type.__name__ = "Integer32"
_NncCrSpvpcBwdTmClr_Object = MibTableColumn
nncCrSpvpcBwdTmClr = _NncCrSpvpcBwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 32),
    _NncCrSpvpcBwdTmClr_Type()
)
nncCrSpvpcBwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcBwdTmClr.setStatus("current")


class _NncCrSpvpcCreator_Type(Integer32):
    """Custom type nncCrSpvpcCreator based on Integer32"""
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


_NncCrSpvpcCreator_Type.__name__ = "Integer32"
_NncCrSpvpcCreator_Object = MibTableColumn
nncCrSpvpcCreator = _NncCrSpvpcCreator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 33),
    _NncCrSpvpcCreator_Type()
)
nncCrSpvpcCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCrSpvpcCreator.setStatus("current")
_NncCrSpvpcRowStatus_Type = RowStatus
_NncCrSpvpcRowStatus_Object = MibTableColumn
nncCrSpvpcRowStatus = _NncCrSpvpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 1, 1, 34),
    _NncCrSpvpcRowStatus_Type()
)
nncCrSpvpcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcRowStatus.setStatus("current")
_NncCrSpvpcDstCfgTable_Object = MibTable
nncCrSpvpcDstCfgTable = _NncCrSpvpcDstCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 2)
)
if mibBuilder.loadTexts:
    nncCrSpvpcDstCfgTable.setStatus("current")
_NncCrSpvpcDstCfgTableEntry_Object = MibTableRow
nncCrSpvpcDstCfgTableEntry = _NncCrSpvpcDstCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 2, 1)
)
nncCrSpvpcDstCfgTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    nncCrSpvpcDstCfgTableEntry.setStatus("current")


class _NncCrSpvpcDstCfgCdvt_Type(Integer32):
    """Custom type nncCrSpvpcDstCfgCdvt based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrSpvpcDstCfgCdvt_Type.__name__ = "Integer32"
_NncCrSpvpcDstCfgCdvt_Object = MibTableColumn
nncCrSpvpcDstCfgCdvt = _NncCrSpvpcDstCfgCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 2, 1, 1),
    _NncCrSpvpcDstCfgCdvt_Type()
)
nncCrSpvpcDstCfgCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcDstCfgCdvt.setStatus("current")


class _NncCrSpvpcDstCfgPolicing_Type(Integer32):
    """Custom type nncCrSpvpcDstCfgPolicing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discard", 3),
          ("nullPolicing", 0),
          ("tag", 2),
          ("useSignalled", 4))
    )


_NncCrSpvpcDstCfgPolicing_Type.__name__ = "Integer32"
_NncCrSpvpcDstCfgPolicing_Object = MibTableColumn
nncCrSpvpcDstCfgPolicing = _NncCrSpvpcDstCfgPolicing_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 2, 1, 2),
    _NncCrSpvpcDstCfgPolicing_Type()
)
nncCrSpvpcDstCfgPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcDstCfgPolicing.setStatus("current")


class _NncCrSpvpcDstCfgBillingFlag_Type(Integer32):
    """Custom type nncCrSpvpcDstCfgBillingFlag based on Integer32"""
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


_NncCrSpvpcDstCfgBillingFlag_Type.__name__ = "Integer32"
_NncCrSpvpcDstCfgBillingFlag_Object = MibTableColumn
nncCrSpvpcDstCfgBillingFlag = _NncCrSpvpcDstCfgBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 2, 1, 3),
    _NncCrSpvpcDstCfgBillingFlag_Type()
)
nncCrSpvpcDstCfgBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcDstCfgBillingFlag.setStatus("current")


class _NncCrSpvpcDstCfgLocRerouteConfig_Type(Integer32):
    """Custom type nncCrSpvpcDstCfgLocRerouteConfig based on Integer32"""
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
        *(("disabled", 1),
          ("enabledNniSide", 3),
          ("enabledUniSide", 2))
    )


_NncCrSpvpcDstCfgLocRerouteConfig_Type.__name__ = "Integer32"
_NncCrSpvpcDstCfgLocRerouteConfig_Object = MibTableColumn
nncCrSpvpcDstCfgLocRerouteConfig = _NncCrSpvpcDstCfgLocRerouteConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 2, 1, 4),
    _NncCrSpvpcDstCfgLocRerouteConfig_Type()
)
nncCrSpvpcDstCfgLocRerouteConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcDstCfgLocRerouteConfig.setStatus("current")
_NncCrSpvpcDstCfgRowStatus_Type = RowStatus
_NncCrSpvpcDstCfgRowStatus_Object = MibTableColumn
nncCrSpvpcDstCfgRowStatus = _NncCrSpvpcDstCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 2, 1, 5),
    _NncCrSpvpcDstCfgRowStatus_Type()
)
nncCrSpvpcDstCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvpcDstCfgRowStatus.setStatus("current")
_NncCrSpvccTable_Object = MibTable
nncCrSpvccTable = _NncCrSpvccTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3)
)
if mibBuilder.loadTexts:
    nncCrSpvccTable.setStatus("current")
_NncCrSpvccTableEntry_Object = MibTableRow
nncCrSpvccTableEntry = _NncCrSpvccTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1)
)
nncCrSpvccTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    nncCrSpvccTableEntry.setStatus("current")


class _NncCrSpvccServiceCategory_Type(Integer32):
    """Custom type nncCrSpvccServiceCategory based on Integer32"""
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


_NncCrSpvccServiceCategory_Type.__name__ = "Integer32"
_NncCrSpvccServiceCategory_Object = MibTableColumn
nncCrSpvccServiceCategory = _NncCrSpvccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 1),
    _NncCrSpvccServiceCategory_Type()
)
nncCrSpvccServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccServiceCategory.setStatus("current")
_NncCrSpvccTargEpAddr_Type = AtmFormatDisplay
_NncCrSpvccTargEpAddr_Object = MibTableColumn
nncCrSpvccTargEpAddr = _NncCrSpvccTargEpAddr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 2),
    _NncCrSpvccTargEpAddr_Type()
)
nncCrSpvccTargEpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccTargEpAddr.setStatus("current")


class _NncCrSpvccTargVpi_Type(Integer32):
    """Custom type nncCrSpvccTargVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NncCrSpvccTargVpi_Type.__name__ = "Integer32"
_NncCrSpvccTargVpi_Object = MibTableColumn
nncCrSpvccTargVpi = _NncCrSpvccTargVpi_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 3),
    _NncCrSpvccTargVpi_Type()
)
nncCrSpvccTargVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccTargVpi.setStatus("current")


class _NncCrSpvccTargVci_Type(Integer32):
    """Custom type nncCrSpvccTargVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NncCrSpvccTargVci_Type.__name__ = "Integer32"
_NncCrSpvccTargVci_Object = MibTableColumn
nncCrSpvccTargVci = _NncCrSpvccTargVci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 4),
    _NncCrSpvccTargVci_Type()
)
nncCrSpvccTargVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccTargVci.setStatus("current")


class _NncCrSpvccTargDlci_Type(Integer32):
    """Custom type nncCrSpvccTargDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1023),
    )


_NncCrSpvccTargDlci_Type.__name__ = "Integer32"
_NncCrSpvccTargDlci_Object = MibTableColumn
nncCrSpvccTargDlci = _NncCrSpvccTargDlci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 5),
    _NncCrSpvccTargDlci_Type()
)
nncCrSpvccTargDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrSpvccTargDlci.setStatus("current")


class _NncCrSpvccTargCeNumber_Type(Integer32):
    """Custom type nncCrSpvccTargCeNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NncCrSpvccTargCeNumber_Type.__name__ = "Integer32"
_NncCrSpvccTargCeNumber_Object = MibTableColumn
nncCrSpvccTargCeNumber = _NncCrSpvccTargCeNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 6),
    _NncCrSpvccTargCeNumber_Type()
)
nncCrSpvccTargCeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncCrSpvccTargCeNumber.setStatus("current")


class _NncCrSpvccTargEpType_Type(Integer32):
    """Custom type nncCrSpvccTargEpType based on Integer32"""
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
        *(("cellRelay", 1),
          ("circuitEmulation", 3),
          ("frameRelay", 2))
    )


_NncCrSpvccTargEpType_Type.__name__ = "Integer32"
_NncCrSpvccTargEpType_Object = MibTableColumn
nncCrSpvccTargEpType = _NncCrSpvccTargEpType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 7),
    _NncCrSpvccTargEpType_Type()
)
nncCrSpvccTargEpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccTargEpType.setStatus("current")


class _NncCrSpvccAdminStatus_Type(Integer32):
    """Custom type nncCrSpvccAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NncCrSpvccAdminStatus_Type.__name__ = "Integer32"
_NncCrSpvccAdminStatus_Object = MibTableColumn
nncCrSpvccAdminStatus = _NncCrSpvccAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 8),
    _NncCrSpvccAdminStatus_Type()
)
nncCrSpvccAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccAdminStatus.setStatus("current")


class _NncCrSpvccPriority_Type(Integer32):
    """Custom type nncCrSpvccPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NncCrSpvccPriority_Type.__name__ = "Integer32"
_NncCrSpvccPriority_Object = MibTableColumn
nncCrSpvccPriority = _NncCrSpvccPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 9),
    _NncCrSpvccPriority_Type()
)
nncCrSpvccPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccPriority.setStatus("current")


class _NncCrSpvccMaxAdminWeight_Type(Integer32):
    """Custom type nncCrSpvccMaxAdminWeight based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NncCrSpvccMaxAdminWeight_Type.__name__ = "Integer32"
_NncCrSpvccMaxAdminWeight_Object = MibTableColumn
nncCrSpvccMaxAdminWeight = _NncCrSpvccMaxAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 10),
    _NncCrSpvccMaxAdminWeight_Type()
)
nncCrSpvccMaxAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccMaxAdminWeight.setStatus("current")


class _NncCrSpvccOperation_Type(Integer32):
    """Custom type nncCrSpvccOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("reRouteDualEp", 7)
    )


_NncCrSpvccOperation_Type.__name__ = "Integer32"
_NncCrSpvccOperation_Object = MibTableColumn
nncCrSpvccOperation = _NncCrSpvccOperation_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 11),
    _NncCrSpvccOperation_Type()
)
nncCrSpvccOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccOperation.setStatus("current")


class _NncCrSpvccCallStatus_Type(Integer32):
    """Custom type nncCrSpvccCallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("readyToConnect", 7),
          ("waitingForResources", 4))
    )


_NncCrSpvccCallStatus_Type.__name__ = "Integer32"
_NncCrSpvccCallStatus_Object = MibTableColumn
nncCrSpvccCallStatus = _NncCrSpvccCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 12),
    _NncCrSpvccCallStatus_Type()
)
nncCrSpvccCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCrSpvccCallStatus.setStatus("current")


class _NncCrSpvccLocRerouteConfig_Type(Integer32):
    """Custom type nncCrSpvccLocRerouteConfig based on Integer32"""
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
        *(("disabled", 1),
          ("enabledNniSide", 3),
          ("enabledUniSide", 2))
    )


_NncCrSpvccLocRerouteConfig_Type.__name__ = "Integer32"
_NncCrSpvccLocRerouteConfig_Object = MibTableColumn
nncCrSpvccLocRerouteConfig = _NncCrSpvccLocRerouteConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 13),
    _NncCrSpvccLocRerouteConfig_Type()
)
nncCrSpvccLocRerouteConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccLocRerouteConfig.setStatus("current")


class _NncCrSpvccFwdAbrDynTrfcIcr_Type(Integer32):
    """Custom type nncCrSpvccFwdAbrDynTrfcIcr based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvccFwdAbrDynTrfcIcr_Type.__name__ = "Integer32"
_NncCrSpvccFwdAbrDynTrfcIcr_Object = MibTableColumn
nncCrSpvccFwdAbrDynTrfcIcr = _NncCrSpvccFwdAbrDynTrfcIcr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 14),
    _NncCrSpvccFwdAbrDynTrfcIcr_Type()
)
nncCrSpvccFwdAbrDynTrfcIcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdAbrDynTrfcIcr.setStatus("current")


class _NncCrSpvccFwdAbrDynTrfcRif_Type(Integer32):
    """Custom type nncCrSpvccFwdAbrDynTrfcRif based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrSpvccFwdAbrDynTrfcRif_Type.__name__ = "Integer32"
_NncCrSpvccFwdAbrDynTrfcRif_Object = MibTableColumn
nncCrSpvccFwdAbrDynTrfcRif = _NncCrSpvccFwdAbrDynTrfcRif_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 15),
    _NncCrSpvccFwdAbrDynTrfcRif_Type()
)
nncCrSpvccFwdAbrDynTrfcRif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdAbrDynTrfcRif.setStatus("current")


class _NncCrSpvccFwdAbrDynTrfcRdf_Type(Integer32):
    """Custom type nncCrSpvccFwdAbrDynTrfcRdf based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrSpvccFwdAbrDynTrfcRdf_Type.__name__ = "Integer32"
_NncCrSpvccFwdAbrDynTrfcRdf_Object = MibTableColumn
nncCrSpvccFwdAbrDynTrfcRdf = _NncCrSpvccFwdAbrDynTrfcRdf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 16),
    _NncCrSpvccFwdAbrDynTrfcRdf_Type()
)
nncCrSpvccFwdAbrDynTrfcRdf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdAbrDynTrfcRdf.setStatus("current")


class _NncCrSpvccBwdAbrDynTrfcIcr_Type(Integer32):
    """Custom type nncCrSpvccBwdAbrDynTrfcIcr based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvccBwdAbrDynTrfcIcr_Type.__name__ = "Integer32"
_NncCrSpvccBwdAbrDynTrfcIcr_Object = MibTableColumn
nncCrSpvccBwdAbrDynTrfcIcr = _NncCrSpvccBwdAbrDynTrfcIcr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 17),
    _NncCrSpvccBwdAbrDynTrfcIcr_Type()
)
nncCrSpvccBwdAbrDynTrfcIcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdAbrDynTrfcIcr.setStatus("current")


class _NncCrSpvccBwdAbrDynTrfcRif_Type(Integer32):
    """Custom type nncCrSpvccBwdAbrDynTrfcRif based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrSpvccBwdAbrDynTrfcRif_Type.__name__ = "Integer32"
_NncCrSpvccBwdAbrDynTrfcRif_Object = MibTableColumn
nncCrSpvccBwdAbrDynTrfcRif = _NncCrSpvccBwdAbrDynTrfcRif_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 18),
    _NncCrSpvccBwdAbrDynTrfcRif_Type()
)
nncCrSpvccBwdAbrDynTrfcRif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdAbrDynTrfcRif.setStatus("current")


class _NncCrSpvccBwdAbrDynTrfcRdf_Type(Integer32):
    """Custom type nncCrSpvccBwdAbrDynTrfcRdf based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_NncCrSpvccBwdAbrDynTrfcRdf_Type.__name__ = "Integer32"
_NncCrSpvccBwdAbrDynTrfcRdf_Object = MibTableColumn
nncCrSpvccBwdAbrDynTrfcRdf = _NncCrSpvccBwdAbrDynTrfcRdf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 19),
    _NncCrSpvccBwdAbrDynTrfcRdf_Type()
)
nncCrSpvccBwdAbrDynTrfcRdf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdAbrDynTrfcRdf.setStatus("current")


class _NncCrSpvccSrcBillingFlag_Type(Integer32):
    """Custom type nncCrSpvccSrcBillingFlag based on Integer32"""
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


_NncCrSpvccSrcBillingFlag_Type.__name__ = "Integer32"
_NncCrSpvccSrcBillingFlag_Object = MibTableColumn
nncCrSpvccSrcBillingFlag = _NncCrSpvccSrcBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 20),
    _NncCrSpvccSrcBillingFlag_Type()
)
nncCrSpvccSrcBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccSrcBillingFlag.setStatus("current")


class _NncCrSpvccFwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncCrSpvccFwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

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
        *(("p0Plus1", 2),
          ("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncCrSpvccFwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmTrafficDescriptor_Object = MibTableColumn
nncCrSpvccFwdTmTrafficDescriptor = _NncCrSpvccFwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 21),
    _NncCrSpvccFwdTmTrafficDescriptor_Type()
)
nncCrSpvccFwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmTrafficDescriptor.setStatus("current")


class _NncCrSpvccFwdTmPolicingOption_Type(Integer32):
    """Custom type nncCrSpvccFwdTmPolicingOption based on Integer32"""
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
        *(("disabled", 1),
          ("discard", 3),
          ("tag", 2))
    )


_NncCrSpvccFwdTmPolicingOption_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmPolicingOption_Object = MibTableColumn
nncCrSpvccFwdTmPolicingOption = _NncCrSpvccFwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 22),
    _NncCrSpvccFwdTmPolicingOption_Type()
)
nncCrSpvccFwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmPolicingOption.setStatus("current")


class _NncCrSpvccFwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCrSpvccFwdTmBucketOneRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvccFwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmBucketOneRate_Object = MibTableColumn
nncCrSpvccFwdTmBucketOneRate = _NncCrSpvccFwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 23),
    _NncCrSpvccFwdTmBucketOneRate_Type()
)
nncCrSpvccFwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmBucketOneRate.setStatus("current")


class _NncCrSpvccFwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCrSpvccFwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrSpvccFwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmBucketOneCdvt_Object = MibTableColumn
nncCrSpvccFwdTmBucketOneCdvt = _NncCrSpvccFwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 24),
    _NncCrSpvccFwdTmBucketOneCdvt_Type()
)
nncCrSpvccFwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmBucketOneCdvt.setStatus("current")


class _NncCrSpvccFwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncCrSpvccFwdTmBucketTwoRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvccFwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmBucketTwoRate_Object = MibTableColumn
nncCrSpvccFwdTmBucketTwoRate = _NncCrSpvccFwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 25),
    _NncCrSpvccFwdTmBucketTwoRate_Type()
)
nncCrSpvccFwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmBucketTwoRate.setStatus("current")


class _NncCrSpvccFwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncCrSpvccFwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncCrSpvccFwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmBucketTwoMbs_Object = MibTableColumn
nncCrSpvccFwdTmBucketTwoMbs = _NncCrSpvccFwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 26),
    _NncCrSpvccFwdTmBucketTwoMbs_Type()
)
nncCrSpvccFwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmBucketTwoMbs.setStatus("current")


class _NncCrSpvccFwdTmCdv_Type(Integer32):
    """Custom type nncCrSpvccFwdTmCdv based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncCrSpvccFwdTmCdv_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmCdv_Object = MibTableColumn
nncCrSpvccFwdTmCdv = _NncCrSpvccFwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 27),
    _NncCrSpvccFwdTmCdv_Type()
)
nncCrSpvccFwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmCdv.setStatus("current")


class _NncCrSpvccFwdTmClr_Type(Integer32):
    """Custom type nncCrSpvccFwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncCrSpvccFwdTmClr_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmClr_Object = MibTableColumn
nncCrSpvccFwdTmClr = _NncCrSpvccFwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 28),
    _NncCrSpvccFwdTmClr_Type()
)
nncCrSpvccFwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmClr.setStatus("current")


class _NncCrSpvccFwdTmFrameDiscard_Type(Integer32):
    """Custom type nncCrSpvccFwdTmFrameDiscard based on Integer32"""
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


_NncCrSpvccFwdTmFrameDiscard_Type.__name__ = "Integer32"
_NncCrSpvccFwdTmFrameDiscard_Object = MibTableColumn
nncCrSpvccFwdTmFrameDiscard = _NncCrSpvccFwdTmFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 29),
    _NncCrSpvccFwdTmFrameDiscard_Type()
)
nncCrSpvccFwdTmFrameDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFwdTmFrameDiscard.setStatus("current")


class _NncCrSpvccBwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncCrSpvccBwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

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
        *(("p0Plus1", 2),
          ("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncCrSpvccBwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmTrafficDescriptor_Object = MibTableColumn
nncCrSpvccBwdTmTrafficDescriptor = _NncCrSpvccBwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 30),
    _NncCrSpvccBwdTmTrafficDescriptor_Type()
)
nncCrSpvccBwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmTrafficDescriptor.setStatus("current")


class _NncCrSpvccBwdTmPolicingOption_Type(Integer32):
    """Custom type nncCrSpvccBwdTmPolicingOption based on Integer32"""
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
        *(("disabled", 1),
          ("discard", 3),
          ("tag", 2))
    )


_NncCrSpvccBwdTmPolicingOption_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmPolicingOption_Object = MibTableColumn
nncCrSpvccBwdTmPolicingOption = _NncCrSpvccBwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 31),
    _NncCrSpvccBwdTmPolicingOption_Type()
)
nncCrSpvccBwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmPolicingOption.setStatus("current")


class _NncCrSpvccBwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCrSpvccBwdTmBucketOneRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvccBwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmBucketOneRate_Object = MibTableColumn
nncCrSpvccBwdTmBucketOneRate = _NncCrSpvccBwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 32),
    _NncCrSpvccBwdTmBucketOneRate_Type()
)
nncCrSpvccBwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmBucketOneRate.setStatus("current")


class _NncCrSpvccBwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCrSpvccBwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrSpvccBwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmBucketOneCdvt_Object = MibTableColumn
nncCrSpvccBwdTmBucketOneCdvt = _NncCrSpvccBwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 33),
    _NncCrSpvccBwdTmBucketOneCdvt_Type()
)
nncCrSpvccBwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmBucketOneCdvt.setStatus("current")


class _NncCrSpvccBwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncCrSpvccBwdTmBucketTwoRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCrSpvccBwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmBucketTwoRate_Object = MibTableColumn
nncCrSpvccBwdTmBucketTwoRate = _NncCrSpvccBwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 34),
    _NncCrSpvccBwdTmBucketTwoRate_Type()
)
nncCrSpvccBwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmBucketTwoRate.setStatus("current")


class _NncCrSpvccBwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncCrSpvccBwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncCrSpvccBwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmBucketTwoMbs_Object = MibTableColumn
nncCrSpvccBwdTmBucketTwoMbs = _NncCrSpvccBwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 35),
    _NncCrSpvccBwdTmBucketTwoMbs_Type()
)
nncCrSpvccBwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmBucketTwoMbs.setStatus("current")


class _NncCrSpvccBwdTmCdv_Type(Integer32):
    """Custom type nncCrSpvccBwdTmCdv based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncCrSpvccBwdTmCdv_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmCdv_Object = MibTableColumn
nncCrSpvccBwdTmCdv = _NncCrSpvccBwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 36),
    _NncCrSpvccBwdTmCdv_Type()
)
nncCrSpvccBwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmCdv.setStatus("current")


class _NncCrSpvccBwdTmClr_Type(Integer32):
    """Custom type nncCrSpvccBwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncCrSpvccBwdTmClr_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmClr_Object = MibTableColumn
nncCrSpvccBwdTmClr = _NncCrSpvccBwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 37),
    _NncCrSpvccBwdTmClr_Type()
)
nncCrSpvccBwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmClr.setStatus("current")


class _NncCrSpvccBwdTmFrameDiscard_Type(Integer32):
    """Custom type nncCrSpvccBwdTmFrameDiscard based on Integer32"""
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


_NncCrSpvccBwdTmFrameDiscard_Type.__name__ = "Integer32"
_NncCrSpvccBwdTmFrameDiscard_Object = MibTableColumn
nncCrSpvccBwdTmFrameDiscard = _NncCrSpvccBwdTmFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 38),
    _NncCrSpvccBwdTmFrameDiscard_Type()
)
nncCrSpvccBwdTmFrameDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccBwdTmFrameDiscard.setStatus("current")


class _NncCrSpvccFrBwdTmAr_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmAr based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncCrSpvccFrBwdTmAr_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmAr_Object = MibTableColumn
nncCrSpvccFrBwdTmAr = _NncCrSpvccFrBwdTmAr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 39),
    _NncCrSpvccFrBwdTmAr_Type()
)
nncCrSpvccFrBwdTmAr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmAr.setStatus("current")


class _NncCrSpvccFrBwdTmCir_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmCir based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncCrSpvccFrBwdTmCir_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmCir_Object = MibTableColumn
nncCrSpvccFrBwdTmCir = _NncCrSpvccFrBwdTmCir_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 40),
    _NncCrSpvccFrBwdTmCir_Type()
)
nncCrSpvccFrBwdTmCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmCir.setStatus("current")


class _NncCrSpvccFrBwdTmBc_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmBc based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_NncCrSpvccFrBwdTmBc_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmBc_Object = MibTableColumn
nncCrSpvccFrBwdTmBc = _NncCrSpvccFrBwdTmBc_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 41),
    _NncCrSpvccFrBwdTmBc_Type()
)
nncCrSpvccFrBwdTmBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmBc.setStatus("current")


class _NncCrSpvccFrBwdTmBe_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmBe based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_NncCrSpvccFrBwdTmBe_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmBe_Object = MibTableColumn
nncCrSpvccFrBwdTmBe = _NncCrSpvccFrBwdTmBe_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 42),
    _NncCrSpvccFrBwdTmBe_Type()
)
nncCrSpvccFrBwdTmBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmBe.setStatus("current")


class _NncCrSpvccFrBwdTmIwf_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmIwf based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fFwdInterworking", 4),
          ("networkInterworking", 2),
          ("none", 0),
          ("serviceInterworking", 3))
    )


_NncCrSpvccFrBwdTmIwf_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmIwf_Object = MibTableColumn
nncCrSpvccFrBwdTmIwf = _NncCrSpvccFrBwdTmIwf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 43),
    _NncCrSpvccFrBwdTmIwf_Type()
)
nncCrSpvccFrBwdTmIwf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmIwf.setStatus("current")


class _NncCrSpvccFrBwdTmPo_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmPo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 3))
    )


_NncCrSpvccFrBwdTmPo_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmPo_Object = MibTableColumn
nncCrSpvccFrBwdTmPo = _NncCrSpvccFrBwdTmPo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 44),
    _NncCrSpvccFrBwdTmPo_Type()
)
nncCrSpvccFrBwdTmPo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmPo.setStatus("current")


class _NncCrSpvccFrBwdTmPacing_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmPacing based on Integer32"""
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


_NncCrSpvccFrBwdTmPacing_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmPacing_Object = MibTableColumn
nncCrSpvccFrBwdTmPacing = _NncCrSpvccFrBwdTmPacing_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 45),
    _NncCrSpvccFrBwdTmPacing_Type()
)
nncCrSpvccFrBwdTmPacing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmPacing.setStatus("current")


class _NncCrSpvccFrBwdTmPtclMapping_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmPtclMapping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("translated", 1),
          ("transparent", 0))
    )


_NncCrSpvccFrBwdTmPtclMapping_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmPtclMapping_Object = MibTableColumn
nncCrSpvccFrBwdTmPtclMapping = _NncCrSpvccFrBwdTmPtclMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 46),
    _NncCrSpvccFrBwdTmPtclMapping_Type()
)
nncCrSpvccFrBwdTmPtclMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmPtclMapping.setStatus("current")


class _NncCrSpvccFrBwdTmClpMapping_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmClpMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cLPEquals0", 1),
          ("cLPEquals1", 2),
          ("cLPEqualsDE", 0))
    )


_NncCrSpvccFrBwdTmClpMapping_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmClpMapping_Object = MibTableColumn
nncCrSpvccFrBwdTmClpMapping = _NncCrSpvccFrBwdTmClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 47),
    _NncCrSpvccFrBwdTmClpMapping_Type()
)
nncCrSpvccFrBwdTmClpMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmClpMapping.setStatus("current")


class _NncCrSpvccFrBwdTmDeMapping_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmDeMapping based on Integer32"""
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
        *(("dEEquals1", 2),
          ("dEEqualsCLP", 0),
          ("dESSCSor0", 1))
    )


_NncCrSpvccFrBwdTmDeMapping_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmDeMapping_Object = MibTableColumn
nncCrSpvccFrBwdTmDeMapping = _NncCrSpvccFrBwdTmDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 48),
    _NncCrSpvccFrBwdTmDeMapping_Type()
)
nncCrSpvccFrBwdTmDeMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmDeMapping.setStatus("current")


class _NncCrSpvccFrBwdTmEfciMapping_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmEfciMapping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eFCIEquals0", 1),
          ("eFCIEqualsFECN", 0))
    )


_NncCrSpvccFrBwdTmEfciMapping_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmEfciMapping_Object = MibTableColumn
nncCrSpvccFrBwdTmEfciMapping = _NncCrSpvccFrBwdTmEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 49),
    _NncCrSpvccFrBwdTmEfciMapping_Type()
)
nncCrSpvccFrBwdTmEfciMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmEfciMapping.setStatus("current")


class _NncCrSpvccFrBwdTmPvcMgntProfile_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmPvcMgntProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_NncCrSpvccFrBwdTmPvcMgntProfile_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmPvcMgntProfile_Object = MibTableColumn
nncCrSpvccFrBwdTmPvcMgntProfile = _NncCrSpvccFrBwdTmPvcMgntProfile_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 50),
    _NncCrSpvccFrBwdTmPvcMgntProfile_Type()
)
nncCrSpvccFrBwdTmPvcMgntProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmPvcMgntProfile.setStatus("current")


class _NncCrSpvccFrBwdTmSIWProfile_Type(Integer32):
    """Custom type nncCrSpvccFrBwdTmSIWProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NncCrSpvccFrBwdTmSIWProfile_Type.__name__ = "Integer32"
_NncCrSpvccFrBwdTmSIWProfile_Object = MibTableColumn
nncCrSpvccFrBwdTmSIWProfile = _NncCrSpvccFrBwdTmSIWProfile_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 51),
    _NncCrSpvccFrBwdTmSIWProfile_Type()
)
nncCrSpvccFrBwdTmSIWProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccFrBwdTmSIWProfile.setStatus("current")


class _NncCrSpvccCreator_Type(Integer32):
    """Custom type nncCrSpvccCreator based on Integer32"""
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


_NncCrSpvccCreator_Type.__name__ = "Integer32"
_NncCrSpvccCreator_Object = MibTableColumn
nncCrSpvccCreator = _NncCrSpvccCreator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 52),
    _NncCrSpvccCreator_Type()
)
nncCrSpvccCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCrSpvccCreator.setStatus("current")
_NncCrSpvccRowStatus_Type = RowStatus
_NncCrSpvccRowStatus_Object = MibTableColumn
nncCrSpvccRowStatus = _NncCrSpvccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 3, 1, 53),
    _NncCrSpvccRowStatus_Type()
)
nncCrSpvccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccRowStatus.setStatus("current")
_NncCrSpvccDstCfgTable_Object = MibTable
nncCrSpvccDstCfgTable = _NncCrSpvccDstCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 4)
)
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgTable.setStatus("current")
_NncCrSpvccDstCfgTableEntry_Object = MibTableRow
nncCrSpvccDstCfgTableEntry = _NncCrSpvccDstCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 4, 1)
)
nncCrSpvccDstCfgTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgTableEntry.setStatus("current")


class _NncCrSpvccDstCfgCdvt_Type(Integer32):
    """Custom type nncCrSpvccDstCfgCdvt based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCrSpvccDstCfgCdvt_Type.__name__ = "Integer32"
_NncCrSpvccDstCfgCdvt_Object = MibTableColumn
nncCrSpvccDstCfgCdvt = _NncCrSpvccDstCfgCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 4, 1, 1),
    _NncCrSpvccDstCfgCdvt_Type()
)
nncCrSpvccDstCfgCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgCdvt.setStatus("current")


class _NncCrSpvccDstCfgPolicing_Type(Integer32):
    """Custom type nncCrSpvccDstCfgPolicing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discard", 3),
          ("nullPolicing", 0),
          ("tag", 2),
          ("useSignalled", 4))
    )


_NncCrSpvccDstCfgPolicing_Type.__name__ = "Integer32"
_NncCrSpvccDstCfgPolicing_Object = MibTableColumn
nncCrSpvccDstCfgPolicing = _NncCrSpvccDstCfgPolicing_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 4, 1, 2),
    _NncCrSpvccDstCfgPolicing_Type()
)
nncCrSpvccDstCfgPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgPolicing.setStatus("current")


class _NncCrSpvccDstCfgBillingFlag_Type(Integer32):
    """Custom type nncCrSpvccDstCfgBillingFlag based on Integer32"""
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


_NncCrSpvccDstCfgBillingFlag_Type.__name__ = "Integer32"
_NncCrSpvccDstCfgBillingFlag_Object = MibTableColumn
nncCrSpvccDstCfgBillingFlag = _NncCrSpvccDstCfgBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 4, 1, 3),
    _NncCrSpvccDstCfgBillingFlag_Type()
)
nncCrSpvccDstCfgBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgBillingFlag.setStatus("current")


class _NncCrSpvccDstCfgFrVsvdCongestionControl_Type(Integer32):
    """Custom type nncCrSpvccDstCfgFrVsvdCongestionControl based on Integer32"""
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


_NncCrSpvccDstCfgFrVsvdCongestionControl_Type.__name__ = "Integer32"
_NncCrSpvccDstCfgFrVsvdCongestionControl_Object = MibTableColumn
nncCrSpvccDstCfgFrVsvdCongestionControl = _NncCrSpvccDstCfgFrVsvdCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 4, 1, 4),
    _NncCrSpvccDstCfgFrVsvdCongestionControl_Type()
)
nncCrSpvccDstCfgFrVsvdCongestionControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgFrVsvdCongestionControl.setStatus("current")


class _NncCrSpvccDstCfgLocRerouteConfig_Type(Integer32):
    """Custom type nncCrSpvccDstCfgLocRerouteConfig based on Integer32"""
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
        *(("disabled", 1),
          ("enabledNniSide", 3),
          ("enabledUniSide", 2))
    )


_NncCrSpvccDstCfgLocRerouteConfig_Type.__name__ = "Integer32"
_NncCrSpvccDstCfgLocRerouteConfig_Object = MibTableColumn
nncCrSpvccDstCfgLocRerouteConfig = _NncCrSpvccDstCfgLocRerouteConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 4, 1, 5),
    _NncCrSpvccDstCfgLocRerouteConfig_Type()
)
nncCrSpvccDstCfgLocRerouteConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgLocRerouteConfig.setStatus("current")
_NncCrSpvccDstCfgRowStatus_Type = RowStatus
_NncCrSpvccDstCfgRowStatus_Object = MibTableColumn
nncCrSpvccDstCfgRowStatus = _NncCrSpvccDstCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 4, 1, 6),
    _NncCrSpvccDstCfgRowStatus_Type()
)
nncCrSpvccDstCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgRowStatus.setStatus("current")
_NncFrSpvcTable_Object = MibTable
nncFrSpvcTable = _NncFrSpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5)
)
if mibBuilder.loadTexts:
    nncFrSpvcTable.setStatus("current")
_NncFrSpvcTableEntry_Object = MibTableRow
nncFrSpvcTableEntry = _NncFrSpvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1)
)
nncFrSpvcTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCEXTSPVC-MIB", "nncFrSpvcSrcDlci"),
)
if mibBuilder.loadTexts:
    nncFrSpvcTableEntry.setStatus("current")


class _NncFrSpvcSrcDlci_Type(Integer32):
    """Custom type nncFrSpvcSrcDlci based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1023),
    )


_NncFrSpvcSrcDlci_Type.__name__ = "Integer32"
_NncFrSpvcSrcDlci_Object = MibTableColumn
nncFrSpvcSrcDlci = _NncFrSpvcSrcDlci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 1),
    _NncFrSpvcSrcDlci_Type()
)
nncFrSpvcSrcDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncFrSpvcSrcDlci.setStatus("current")
_NncFrSpvcTargEpAddr_Type = AtmFormatDisplay
_NncFrSpvcTargEpAddr_Object = MibTableColumn
nncFrSpvcTargEpAddr = _NncFrSpvcTargEpAddr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 2),
    _NncFrSpvcTargEpAddr_Type()
)
nncFrSpvcTargEpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTargEpAddr.setStatus("current")


class _NncFrSpvcTargDlci_Type(Integer32):
    """Custom type nncFrSpvcTargDlci based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1023),
    )


_NncFrSpvcTargDlci_Type.__name__ = "Integer32"
_NncFrSpvcTargDlci_Object = MibTableColumn
nncFrSpvcTargDlci = _NncFrSpvcTargDlci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 3),
    _NncFrSpvcTargDlci_Type()
)
nncFrSpvcTargDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTargDlci.setStatus("current")


class _NncFrSpvcTargVpi_Type(Integer32):
    """Custom type nncFrSpvcTargVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NncFrSpvcTargVpi_Type.__name__ = "Integer32"
_NncFrSpvcTargVpi_Object = MibTableColumn
nncFrSpvcTargVpi = _NncFrSpvcTargVpi_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 4),
    _NncFrSpvcTargVpi_Type()
)
nncFrSpvcTargVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTargVpi.setStatus("current")


class _NncFrSpvcTargVci_Type(Integer32):
    """Custom type nncFrSpvcTargVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NncFrSpvcTargVci_Type.__name__ = "Integer32"
_NncFrSpvcTargVci_Object = MibTableColumn
nncFrSpvcTargVci = _NncFrSpvcTargVci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 5),
    _NncFrSpvcTargVci_Type()
)
nncFrSpvcTargVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTargVci.setStatus("current")


class _NncFrSpvcTargEpType_Type(Integer32):
    """Custom type nncFrSpvcTargEpType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cellRelay", 1),
          ("frameRelay", 2))
    )


_NncFrSpvcTargEpType_Type.__name__ = "Integer32"
_NncFrSpvcTargEpType_Object = MibTableColumn
nncFrSpvcTargEpType = _NncFrSpvcTargEpType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 6),
    _NncFrSpvcTargEpType_Type()
)
nncFrSpvcTargEpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTargEpType.setStatus("current")


class _NncFrSpvcAdminStatus_Type(Integer32):
    """Custom type nncFrSpvcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NncFrSpvcAdminStatus_Type.__name__ = "Integer32"
_NncFrSpvcAdminStatus_Object = MibTableColumn
nncFrSpvcAdminStatus = _NncFrSpvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 7),
    _NncFrSpvcAdminStatus_Type()
)
nncFrSpvcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcAdminStatus.setStatus("current")


class _NncFrSpvcPriority_Type(Integer32):
    """Custom type nncFrSpvcPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NncFrSpvcPriority_Type.__name__ = "Integer32"
_NncFrSpvcPriority_Object = MibTableColumn
nncFrSpvcPriority = _NncFrSpvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 8),
    _NncFrSpvcPriority_Type()
)
nncFrSpvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcPriority.setStatus("current")


class _NncFrSpvcMaxAdminWeight_Type(Integer32):
    """Custom type nncFrSpvcMaxAdminWeight based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NncFrSpvcMaxAdminWeight_Type.__name__ = "Integer32"
_NncFrSpvcMaxAdminWeight_Object = MibTableColumn
nncFrSpvcMaxAdminWeight = _NncFrSpvcMaxAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 9),
    _NncFrSpvcMaxAdminWeight_Type()
)
nncFrSpvcMaxAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcMaxAdminWeight.setStatus("current")


class _NncFrSpvcOperation_Type(Integer32):
    """Custom type nncFrSpvcOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("reRouteDualEp", 7)
    )


_NncFrSpvcOperation_Type.__name__ = "Integer32"
_NncFrSpvcOperation_Object = MibTableColumn
nncFrSpvcOperation = _NncFrSpvcOperation_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 10),
    _NncFrSpvcOperation_Type()
)
nncFrSpvcOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcOperation.setStatus("current")


class _NncFrSpvcCallStatus_Type(Integer32):
    """Custom type nncFrSpvcCallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("readyToConnect", 7),
          ("waitingForResources", 4))
    )


_NncFrSpvcCallStatus_Type.__name__ = "Integer32"
_NncFrSpvcCallStatus_Object = MibTableColumn
nncFrSpvcCallStatus = _NncFrSpvcCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 11),
    _NncFrSpvcCallStatus_Type()
)
nncFrSpvcCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrSpvcCallStatus.setStatus("current")


class _NncFrSpvcLocRerouteConfig_Type(Integer32):
    """Custom type nncFrSpvcLocRerouteConfig based on Integer32"""
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
        *(("disabled", 1),
          ("enabledNniSide", 3),
          ("enabledUniSide", 2))
    )


_NncFrSpvcLocRerouteConfig_Type.__name__ = "Integer32"
_NncFrSpvcLocRerouteConfig_Object = MibTableColumn
nncFrSpvcLocRerouteConfig = _NncFrSpvcLocRerouteConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 12),
    _NncFrSpvcLocRerouteConfig_Type()
)
nncFrSpvcLocRerouteConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcLocRerouteConfig.setStatus("current")


class _NncFrSpvcSrcBillingFlag_Type(Integer32):
    """Custom type nncFrSpvcSrcBillingFlag based on Integer32"""
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


_NncFrSpvcSrcBillingFlag_Type.__name__ = "Integer32"
_NncFrSpvcSrcBillingFlag_Object = MibTableColumn
nncFrSpvcSrcBillingFlag = _NncFrSpvcSrcBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 13),
    _NncFrSpvcSrcBillingFlag_Type()
)
nncFrSpvcSrcBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcSrcBillingFlag.setStatus("current")


class _NncFrSpvcFrPriority_Type(Integer32):
    """Custom type nncFrSpvcFrPriority based on Integer32"""
    defaultValue = 1

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
        *(("bestEffort", 1),
          ("committedThroughput", 2),
          ("lowLatency", 3),
          ("realTime", 4))
    )


_NncFrSpvcFrPriority_Type.__name__ = "Integer32"
_NncFrSpvcFrPriority_Object = MibTableColumn
nncFrSpvcFrPriority = _NncFrSpvcFrPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 14),
    _NncFrSpvcFrPriority_Type()
)
nncFrSpvcFrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFrPriority.setStatus("current")


class _NncFrSpvcFrVsvdCongestionControl_Type(Integer32):
    """Custom type nncFrSpvcFrVsvdCongestionControl based on Integer32"""
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


_NncFrSpvcFrVsvdCongestionControl_Type.__name__ = "Integer32"
_NncFrSpvcFrVsvdCongestionControl_Object = MibTableColumn
nncFrSpvcFrVsvdCongestionControl = _NncFrSpvcFrVsvdCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 15),
    _NncFrSpvcFrVsvdCongestionControl_Type()
)
nncFrSpvcFrVsvdCongestionControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFrVsvdCongestionControl.setStatus("current")


class _NncFrSpvcFwdFrMir_Type(Integer32):
    """Custom type nncFrSpvcFwdFrMir based on Integer32"""
    defaultValue = 72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncFrSpvcFwdFrMir_Type.__name__ = "Integer32"
_NncFrSpvcFwdFrMir_Object = MibTableColumn
nncFrSpvcFwdFrMir = _NncFrSpvcFwdFrMir_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 16),
    _NncFrSpvcFwdFrMir_Type()
)
nncFrSpvcFwdFrMir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFwdFrMir.setStatus("current")


class _NncFrSpvcFwdTmAr_Type(Integer32):
    """Custom type nncFrSpvcFwdTmAr based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncFrSpvcFwdTmAr_Type.__name__ = "Integer32"
_NncFrSpvcFwdTmAr_Object = MibTableColumn
nncFrSpvcFwdTmAr = _NncFrSpvcFwdTmAr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 17),
    _NncFrSpvcFwdTmAr_Type()
)
nncFrSpvcFwdTmAr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFwdTmAr.setStatus("current")


class _NncFrSpvcFwdTmCir_Type(Integer32):
    """Custom type nncFrSpvcFwdTmCir based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncFrSpvcFwdTmCir_Type.__name__ = "Integer32"
_NncFrSpvcFwdTmCir_Object = MibTableColumn
nncFrSpvcFwdTmCir = _NncFrSpvcFwdTmCir_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 18),
    _NncFrSpvcFwdTmCir_Type()
)
nncFrSpvcFwdTmCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFwdTmCir.setStatus("current")


class _NncFrSpvcFwdTmBc_Type(Integer32):
    """Custom type nncFrSpvcFwdTmBc based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_NncFrSpvcFwdTmBc_Type.__name__ = "Integer32"
_NncFrSpvcFwdTmBc_Object = MibTableColumn
nncFrSpvcFwdTmBc = _NncFrSpvcFwdTmBc_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 19),
    _NncFrSpvcFwdTmBc_Type()
)
nncFrSpvcFwdTmBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFwdTmBc.setStatus("current")


class _NncFrSpvcFwdTmBe_Type(Integer32):
    """Custom type nncFrSpvcFwdTmBe based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_NncFrSpvcFwdTmBe_Type.__name__ = "Integer32"
_NncFrSpvcFwdTmBe_Object = MibTableColumn
nncFrSpvcFwdTmBe = _NncFrSpvcFwdTmBe_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 20),
    _NncFrSpvcFwdTmBe_Type()
)
nncFrSpvcFwdTmBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFwdTmBe.setStatus("current")


class _NncFrSpvcTmIwf_Type(Integer32):
    """Custom type nncFrSpvcTmIwf based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fFwdInterworking", 4),
          ("networkInterworking", 2),
          ("none", 0),
          ("serviceInterworking", 3))
    )


_NncFrSpvcTmIwf_Type.__name__ = "Integer32"
_NncFrSpvcTmIwf_Object = MibTableColumn
nncFrSpvcTmIwf = _NncFrSpvcTmIwf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 21),
    _NncFrSpvcTmIwf_Type()
)
nncFrSpvcTmIwf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTmIwf.setStatus("current")


class _NncFrSpvcFwdTmPo_Type(Integer32):
    """Custom type nncFrSpvcFwdTmPo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 3))
    )


_NncFrSpvcFwdTmPo_Type.__name__ = "Integer32"
_NncFrSpvcFwdTmPo_Object = MibTableColumn
nncFrSpvcFwdTmPo = _NncFrSpvcFwdTmPo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 22),
    _NncFrSpvcFwdTmPo_Type()
)
nncFrSpvcFwdTmPo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFwdTmPo.setStatus("current")


class _NncFrSpvcFwdTmPacing_Type(Integer32):
    """Custom type nncFrSpvcFwdTmPacing based on Integer32"""
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


_NncFrSpvcFwdTmPacing_Type.__name__ = "Integer32"
_NncFrSpvcFwdTmPacing_Object = MibTableColumn
nncFrSpvcFwdTmPacing = _NncFrSpvcFwdTmPacing_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 23),
    _NncFrSpvcFwdTmPacing_Type()
)
nncFrSpvcFwdTmPacing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcFwdTmPacing.setStatus("current")


class _NncFrSpvcTmPtclMapping_Type(Integer32):
    """Custom type nncFrSpvcTmPtclMapping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("translated", 1),
          ("transparent", 0))
    )


_NncFrSpvcTmPtclMapping_Type.__name__ = "Integer32"
_NncFrSpvcTmPtclMapping_Object = MibTableColumn
nncFrSpvcTmPtclMapping = _NncFrSpvcTmPtclMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 24),
    _NncFrSpvcTmPtclMapping_Type()
)
nncFrSpvcTmPtclMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTmPtclMapping.setStatus("current")


class _NncFrSpvcTmClpMapping_Type(Integer32):
    """Custom type nncFrSpvcTmClpMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cLPEquals0", 1),
          ("cLPEquals1", 2),
          ("cLPEqualsDE", 0))
    )


_NncFrSpvcTmClpMapping_Type.__name__ = "Integer32"
_NncFrSpvcTmClpMapping_Object = MibTableColumn
nncFrSpvcTmClpMapping = _NncFrSpvcTmClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 25),
    _NncFrSpvcTmClpMapping_Type()
)
nncFrSpvcTmClpMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTmClpMapping.setStatus("current")


class _NncFrSpvcTmDeMapping_Type(Integer32):
    """Custom type nncFrSpvcTmDeMapping based on Integer32"""
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
        *(("dEEquals1", 2),
          ("dEEqualsCLP", 0),
          ("dESSCSor0", 1))
    )


_NncFrSpvcTmDeMapping_Type.__name__ = "Integer32"
_NncFrSpvcTmDeMapping_Object = MibTableColumn
nncFrSpvcTmDeMapping = _NncFrSpvcTmDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 26),
    _NncFrSpvcTmDeMapping_Type()
)
nncFrSpvcTmDeMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTmDeMapping.setStatus("current")


class _NncFrSpvcTmEfciMapping_Type(Integer32):
    """Custom type nncFrSpvcTmEfciMapping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eFCIEquals0", 1),
          ("eFCIEqualsFECN", 0))
    )


_NncFrSpvcTmEfciMapping_Type.__name__ = "Integer32"
_NncFrSpvcTmEfciMapping_Object = MibTableColumn
nncFrSpvcTmEfciMapping = _NncFrSpvcTmEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 27),
    _NncFrSpvcTmEfciMapping_Type()
)
nncFrSpvcTmEfciMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTmEfciMapping.setStatus("current")


class _NncFrSpvcTmPvcMgntProfile_Type(Integer32):
    """Custom type nncFrSpvcTmPvcMgntProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_NncFrSpvcTmPvcMgntProfile_Type.__name__ = "Integer32"
_NncFrSpvcTmPvcMgntProfile_Object = MibTableColumn
nncFrSpvcTmPvcMgntProfile = _NncFrSpvcTmPvcMgntProfile_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 28),
    _NncFrSpvcTmPvcMgntProfile_Type()
)
nncFrSpvcTmPvcMgntProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTmPvcMgntProfile.setStatus("current")


class _NncFrSpvcTmSIWProfile_Type(Integer32):
    """Custom type nncFrSpvcTmSIWProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NncFrSpvcTmSIWProfile_Type.__name__ = "Integer32"
_NncFrSpvcTmSIWProfile_Object = MibTableColumn
nncFrSpvcTmSIWProfile = _NncFrSpvcTmSIWProfile_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 29),
    _NncFrSpvcTmSIWProfile_Type()
)
nncFrSpvcTmSIWProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTmSIWProfile.setStatus("current")


class _NncFrSpvcTmRemapDlci_Type(Integer32):
    """Custom type nncFrSpvcTmRemapDlci based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1023),
    )


_NncFrSpvcTmRemapDlci_Type.__name__ = "Integer32"
_NncFrSpvcTmRemapDlci_Object = MibTableColumn
nncFrSpvcTmRemapDlci = _NncFrSpvcTmRemapDlci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 30),
    _NncFrSpvcTmRemapDlci_Type()
)
nncFrSpvcTmRemapDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcTmRemapDlci.setStatus("current")


class _NncFrSpvcBwdFrMir_Type(Integer32):
    """Custom type nncFrSpvcBwdFrMir based on Integer32"""
    defaultValue = 72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncFrSpvcBwdFrMir_Type.__name__ = "Integer32"
_NncFrSpvcBwdFrMir_Object = MibTableColumn
nncFrSpvcBwdFrMir = _NncFrSpvcBwdFrMir_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 31),
    _NncFrSpvcBwdFrMir_Type()
)
nncFrSpvcBwdFrMir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcBwdFrMir.setStatus("current")


class _NncFrSpvcBwdTmAr_Type(Integer32):
    """Custom type nncFrSpvcBwdTmAr based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncFrSpvcBwdTmAr_Type.__name__ = "Integer32"
_NncFrSpvcBwdTmAr_Object = MibTableColumn
nncFrSpvcBwdTmAr = _NncFrSpvcBwdTmAr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 32),
    _NncFrSpvcBwdTmAr_Type()
)
nncFrSpvcBwdTmAr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcBwdTmAr.setStatus("current")


class _NncFrSpvcBwdTmCir_Type(Integer32):
    """Custom type nncFrSpvcBwdTmCir based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncFrSpvcBwdTmCir_Type.__name__ = "Integer32"
_NncFrSpvcBwdTmCir_Object = MibTableColumn
nncFrSpvcBwdTmCir = _NncFrSpvcBwdTmCir_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 33),
    _NncFrSpvcBwdTmCir_Type()
)
nncFrSpvcBwdTmCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcBwdTmCir.setStatus("current")


class _NncFrSpvcBwdTmBc_Type(Integer32):
    """Custom type nncFrSpvcBwdTmBc based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_NncFrSpvcBwdTmBc_Type.__name__ = "Integer32"
_NncFrSpvcBwdTmBc_Object = MibTableColumn
nncFrSpvcBwdTmBc = _NncFrSpvcBwdTmBc_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 34),
    _NncFrSpvcBwdTmBc_Type()
)
nncFrSpvcBwdTmBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcBwdTmBc.setStatus("current")


class _NncFrSpvcBwdTmBe_Type(Integer32):
    """Custom type nncFrSpvcBwdTmBe based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_NncFrSpvcBwdTmBe_Type.__name__ = "Integer32"
_NncFrSpvcBwdTmBe_Object = MibTableColumn
nncFrSpvcBwdTmBe = _NncFrSpvcBwdTmBe_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 35),
    _NncFrSpvcBwdTmBe_Type()
)
nncFrSpvcBwdTmBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcBwdTmBe.setStatus("current")


class _NncFrSpvcBwdTmPo_Type(Integer32):
    """Custom type nncFrSpvcBwdTmPo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 3))
    )


_NncFrSpvcBwdTmPo_Type.__name__ = "Integer32"
_NncFrSpvcBwdTmPo_Object = MibTableColumn
nncFrSpvcBwdTmPo = _NncFrSpvcBwdTmPo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 36),
    _NncFrSpvcBwdTmPo_Type()
)
nncFrSpvcBwdTmPo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcBwdTmPo.setStatus("current")


class _NncFrSpvcBwdTmPacing_Type(Integer32):
    """Custom type nncFrSpvcBwdTmPacing based on Integer32"""
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


_NncFrSpvcBwdTmPacing_Type.__name__ = "Integer32"
_NncFrSpvcBwdTmPacing_Object = MibTableColumn
nncFrSpvcBwdTmPacing = _NncFrSpvcBwdTmPacing_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 37),
    _NncFrSpvcBwdTmPacing_Type()
)
nncFrSpvcBwdTmPacing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcBwdTmPacing.setStatus("current")


class _NncFrSpvcCrTmServiceCategory_Type(Integer32):
    """Custom type nncFrSpvcCrTmServiceCategory based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 3),
          ("nrtvbr", 2),
          ("rtvbr", 6),
          ("ubr", 4))
    )


_NncFrSpvcCrTmServiceCategory_Type.__name__ = "Integer32"
_NncFrSpvcCrTmServiceCategory_Object = MibTableColumn
nncFrSpvcCrTmServiceCategory = _NncFrSpvcCrTmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 38),
    _NncFrSpvcCrTmServiceCategory_Type()
)
nncFrSpvcCrTmServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrTmServiceCategory.setStatus("current")


class _NncFrSpvcCrBwdTmTrafficDescriptor_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmTrafficDescriptor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("p0Plus1SlashM0Plus1", 5),
          ("p0Plus1SlashS0", 4),
          ("p0Plus1SlashS0Plus1", 3),
          ("tagAll", 1))
    )


_NncFrSpvcCrBwdTmTrafficDescriptor_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmTrafficDescriptor_Object = MibTableColumn
nncFrSpvcCrBwdTmTrafficDescriptor = _NncFrSpvcCrBwdTmTrafficDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 39),
    _NncFrSpvcCrBwdTmTrafficDescriptor_Type()
)
nncFrSpvcCrBwdTmTrafficDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmTrafficDescriptor.setStatus("current")


class _NncFrSpvcCrBwdTmPolicingOption_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmPolicingOption based on Integer32"""
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
        *(("disabled", 1),
          ("discard", 3),
          ("tag", 2))
    )


_NncFrSpvcCrBwdTmPolicingOption_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmPolicingOption_Object = MibTableColumn
nncFrSpvcCrBwdTmPolicingOption = _NncFrSpvcCrBwdTmPolicingOption_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 40),
    _NncFrSpvcCrBwdTmPolicingOption_Type()
)
nncFrSpvcCrBwdTmPolicingOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmPolicingOption.setStatus("current")


class _NncFrSpvcCrBwdTmBucketOneRate_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmBucketOneRate based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncFrSpvcCrBwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmBucketOneRate_Object = MibTableColumn
nncFrSpvcCrBwdTmBucketOneRate = _NncFrSpvcCrBwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 41),
    _NncFrSpvcCrBwdTmBucketOneRate_Type()
)
nncFrSpvcCrBwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmBucketOneRate.setStatus("current")


class _NncFrSpvcCrBwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncFrSpvcCrBwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmBucketOneCdvt_Object = MibTableColumn
nncFrSpvcCrBwdTmBucketOneCdvt = _NncFrSpvcCrBwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 42),
    _NncFrSpvcCrBwdTmBucketOneCdvt_Type()
)
nncFrSpvcCrBwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmBucketOneCdvt.setStatus("current")


class _NncFrSpvcCrBwdTmBucketTwoRate_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmBucketTwoRate based on Integer32"""
    defaultValue = 72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncFrSpvcCrBwdTmBucketTwoRate_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmBucketTwoRate_Object = MibTableColumn
nncFrSpvcCrBwdTmBucketTwoRate = _NncFrSpvcCrBwdTmBucketTwoRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 43),
    _NncFrSpvcCrBwdTmBucketTwoRate_Type()
)
nncFrSpvcCrBwdTmBucketTwoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmBucketTwoRate.setStatus("current")


class _NncFrSpvcCrBwdTmBucketTwoMbs_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmBucketTwoMbs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NncFrSpvcCrBwdTmBucketTwoMbs_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmBucketTwoMbs_Object = MibTableColumn
nncFrSpvcCrBwdTmBucketTwoMbs = _NncFrSpvcCrBwdTmBucketTwoMbs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 44),
    _NncFrSpvcCrBwdTmBucketTwoMbs_Type()
)
nncFrSpvcCrBwdTmBucketTwoMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmBucketTwoMbs.setStatus("current")


class _NncFrSpvcCrBwdTmCdv_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmCdv based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_NncFrSpvcCrBwdTmCdv_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmCdv_Object = MibTableColumn
nncFrSpvcCrBwdTmCdv = _NncFrSpvcCrBwdTmCdv_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 45),
    _NncFrSpvcCrBwdTmCdv_Type()
)
nncFrSpvcCrBwdTmCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmCdv.setStatus("current")


class _NncFrSpvcCrBwdTmClr_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmClr based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncFrSpvcCrBwdTmClr_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmClr_Object = MibTableColumn
nncFrSpvcCrBwdTmClr = _NncFrSpvcCrBwdTmClr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 46),
    _NncFrSpvcCrBwdTmClr_Type()
)
nncFrSpvcCrBwdTmClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmClr.setStatus("current")


class _NncFrSpvcCrBwdTmFrameDiscard_Type(Integer32):
    """Custom type nncFrSpvcCrBwdTmFrameDiscard based on Integer32"""
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


_NncFrSpvcCrBwdTmFrameDiscard_Type.__name__ = "Integer32"
_NncFrSpvcCrBwdTmFrameDiscard_Object = MibTableColumn
nncFrSpvcCrBwdTmFrameDiscard = _NncFrSpvcCrBwdTmFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 47),
    _NncFrSpvcCrBwdTmFrameDiscard_Type()
)
nncFrSpvcCrBwdTmFrameDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcCrBwdTmFrameDiscard.setStatus("current")


class _NncFrSpvcCreator_Type(Integer32):
    """Custom type nncFrSpvcCreator based on Integer32"""
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


_NncFrSpvcCreator_Type.__name__ = "Integer32"
_NncFrSpvcCreator_Object = MibTableColumn
nncFrSpvcCreator = _NncFrSpvcCreator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 48),
    _NncFrSpvcCreator_Type()
)
nncFrSpvcCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncFrSpvcCreator.setStatus("current")
_NncFrSpvcRowStatus_Type = RowStatus
_NncFrSpvcRowStatus_Object = MibTableColumn
nncFrSpvcRowStatus = _NncFrSpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 5, 1, 49),
    _NncFrSpvcRowStatus_Type()
)
nncFrSpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcRowStatus.setStatus("current")
_NncFrSpvcDstCfgTable_Object = MibTable
nncFrSpvcDstCfgTable = _NncFrSpvcDstCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6)
)
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTable.setStatus("current")
_NncFrSpvcDstCfgTableEntry_Object = MibTableRow
nncFrSpvcDstCfgTableEntry = _NncFrSpvcDstCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1)
)
nncFrSpvcDstCfgTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmRemapDlci"),
)
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTableEntry.setStatus("current")


class _NncFrSpvcDstCfgTmAr_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmAr based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncFrSpvcDstCfgTmAr_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmAr_Object = MibTableColumn
nncFrSpvcDstCfgTmAr = _NncFrSpvcDstCfgTmAr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 1),
    _NncFrSpvcDstCfgTmAr_Type()
)
nncFrSpvcDstCfgTmAr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmAr.setStatus("current")


class _NncFrSpvcDstCfgTmCir_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmCir based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_NncFrSpvcDstCfgTmCir_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmCir_Object = MibTableColumn
nncFrSpvcDstCfgTmCir = _NncFrSpvcDstCfgTmCir_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 2),
    _NncFrSpvcDstCfgTmCir_Type()
)
nncFrSpvcDstCfgTmCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmCir.setStatus("current")


class _NncFrSpvcDstCfgTmBc_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmBc based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_NncFrSpvcDstCfgTmBc_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmBc_Object = MibTableColumn
nncFrSpvcDstCfgTmBc = _NncFrSpvcDstCfgTmBc_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 3),
    _NncFrSpvcDstCfgTmBc_Type()
)
nncFrSpvcDstCfgTmBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmBc.setStatus("current")


class _NncFrSpvcDstCfgTmBe_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmBe based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_NncFrSpvcDstCfgTmBe_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmBe_Object = MibTableColumn
nncFrSpvcDstCfgTmBe = _NncFrSpvcDstCfgTmBe_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 4),
    _NncFrSpvcDstCfgTmBe_Type()
)
nncFrSpvcDstCfgTmBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmBe.setStatus("current")


class _NncFrSpvcDstCfgTmIwf_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmIwf based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fFwdInterworking", 4),
          ("networkInterworking", 2),
          ("none", 0),
          ("serviceInterworking", 3))
    )


_NncFrSpvcDstCfgTmIwf_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmIwf_Object = MibTableColumn
nncFrSpvcDstCfgTmIwf = _NncFrSpvcDstCfgTmIwf_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 5),
    _NncFrSpvcDstCfgTmIwf_Type()
)
nncFrSpvcDstCfgTmIwf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmIwf.setStatus("current")


class _NncFrSpvcDstCfgTmPo_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmPo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 3))
    )


_NncFrSpvcDstCfgTmPo_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmPo_Object = MibTableColumn
nncFrSpvcDstCfgTmPo = _NncFrSpvcDstCfgTmPo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 6),
    _NncFrSpvcDstCfgTmPo_Type()
)
nncFrSpvcDstCfgTmPo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmPo.setStatus("current")


class _NncFrSpvcDstCfgTmPacing_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmPacing based on Integer32"""
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


_NncFrSpvcDstCfgTmPacing_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmPacing_Object = MibTableColumn
nncFrSpvcDstCfgTmPacing = _NncFrSpvcDstCfgTmPacing_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 7),
    _NncFrSpvcDstCfgTmPacing_Type()
)
nncFrSpvcDstCfgTmPacing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmPacing.setStatus("current")


class _NncFrSpvcDstCfgTmPtclMapping_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmPtclMapping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("translated", 1),
          ("transparent", 0))
    )


_NncFrSpvcDstCfgTmPtclMapping_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmPtclMapping_Object = MibTableColumn
nncFrSpvcDstCfgTmPtclMapping = _NncFrSpvcDstCfgTmPtclMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 8),
    _NncFrSpvcDstCfgTmPtclMapping_Type()
)
nncFrSpvcDstCfgTmPtclMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmPtclMapping.setStatus("current")


class _NncFrSpvcDstCfgTmClpMapping_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmClpMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cLPEquals0", 1),
          ("cLPEquals1", 2),
          ("cLPEqualsDE", 0))
    )


_NncFrSpvcDstCfgTmClpMapping_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmClpMapping_Object = MibTableColumn
nncFrSpvcDstCfgTmClpMapping = _NncFrSpvcDstCfgTmClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 9),
    _NncFrSpvcDstCfgTmClpMapping_Type()
)
nncFrSpvcDstCfgTmClpMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmClpMapping.setStatus("current")


class _NncFrSpvcDstCfgTmDeMapping_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmDeMapping based on Integer32"""
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
        *(("dEEquals1", 2),
          ("dEEqualsCLP", 0),
          ("dESSCSor0", 1))
    )


_NncFrSpvcDstCfgTmDeMapping_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmDeMapping_Object = MibTableColumn
nncFrSpvcDstCfgTmDeMapping = _NncFrSpvcDstCfgTmDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 10),
    _NncFrSpvcDstCfgTmDeMapping_Type()
)
nncFrSpvcDstCfgTmDeMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmDeMapping.setStatus("current")


class _NncFrSpvcDstCfgTmEfciMapping_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmEfciMapping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eFCIEquals0", 1),
          ("eFCIEqualsFECN", 0))
    )


_NncFrSpvcDstCfgTmEfciMapping_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmEfciMapping_Object = MibTableColumn
nncFrSpvcDstCfgTmEfciMapping = _NncFrSpvcDstCfgTmEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 11),
    _NncFrSpvcDstCfgTmEfciMapping_Type()
)
nncFrSpvcDstCfgTmEfciMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmEfciMapping.setStatus("current")


class _NncFrSpvcDstCfgTmPvcMgntProfile_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmPvcMgntProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_NncFrSpvcDstCfgTmPvcMgntProfile_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmPvcMgntProfile_Object = MibTableColumn
nncFrSpvcDstCfgTmPvcMgntProfile = _NncFrSpvcDstCfgTmPvcMgntProfile_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 12),
    _NncFrSpvcDstCfgTmPvcMgntProfile_Type()
)
nncFrSpvcDstCfgTmPvcMgntProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmPvcMgntProfile.setStatus("current")


class _NncFrSpvcDstCfgTmSIWProfile_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmSIWProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NncFrSpvcDstCfgTmSIWProfile_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmSIWProfile_Object = MibTableColumn
nncFrSpvcDstCfgTmSIWProfile = _NncFrSpvcDstCfgTmSIWProfile_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 13),
    _NncFrSpvcDstCfgTmSIWProfile_Type()
)
nncFrSpvcDstCfgTmSIWProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmSIWProfile.setStatus("current")


class _NncFrSpvcDstCfgTmRemapDlci_Type(Integer32):
    """Custom type nncFrSpvcDstCfgTmRemapDlci based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1023),
    )


_NncFrSpvcDstCfgTmRemapDlci_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgTmRemapDlci_Object = MibTableColumn
nncFrSpvcDstCfgTmRemapDlci = _NncFrSpvcDstCfgTmRemapDlci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 14),
    _NncFrSpvcDstCfgTmRemapDlci_Type()
)
nncFrSpvcDstCfgTmRemapDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgTmRemapDlci.setStatus("current")


class _NncFrSpvcDstCfgBillingFlag_Type(Integer32):
    """Custom type nncFrSpvcDstCfgBillingFlag based on Integer32"""
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


_NncFrSpvcDstCfgBillingFlag_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgBillingFlag_Object = MibTableColumn
nncFrSpvcDstCfgBillingFlag = _NncFrSpvcDstCfgBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 15),
    _NncFrSpvcDstCfgBillingFlag_Type()
)
nncFrSpvcDstCfgBillingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgBillingFlag.setStatus("current")


class _NncFrSpvcDstCfgFrPriority_Type(Integer32):
    """Custom type nncFrSpvcDstCfgFrPriority based on Integer32"""
    defaultValue = 1

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
        *(("bestEffort", 1),
          ("committedThroughput", 2),
          ("lowLatency", 3),
          ("realTime", 4))
    )


_NncFrSpvcDstCfgFrPriority_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgFrPriority_Object = MibTableColumn
nncFrSpvcDstCfgFrPriority = _NncFrSpvcDstCfgFrPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 16),
    _NncFrSpvcDstCfgFrPriority_Type()
)
nncFrSpvcDstCfgFrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgFrPriority.setStatus("current")


class _NncFrSpvcDstCfgLocRerouteConfig_Type(Integer32):
    """Custom type nncFrSpvcDstCfgLocRerouteConfig based on Integer32"""
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
        *(("disabled", 1),
          ("enabledNniSide", 3),
          ("enabledUniSide", 2))
    )


_NncFrSpvcDstCfgLocRerouteConfig_Type.__name__ = "Integer32"
_NncFrSpvcDstCfgLocRerouteConfig_Object = MibTableColumn
nncFrSpvcDstCfgLocRerouteConfig = _NncFrSpvcDstCfgLocRerouteConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 17),
    _NncFrSpvcDstCfgLocRerouteConfig_Type()
)
nncFrSpvcDstCfgLocRerouteConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgLocRerouteConfig.setStatus("current")
_NncFrSpvcDstCfgRowStatus_Type = RowStatus
_NncFrSpvcDstCfgRowStatus_Object = MibTableColumn
nncFrSpvcDstCfgRowStatus = _NncFrSpvcDstCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 6, 1, 18),
    _NncFrSpvcDstCfgRowStatus_Type()
)
nncFrSpvcDstCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgRowStatus.setStatus("current")
_NncCeSpvcTable_Object = MibTable
nncCeSpvcTable = _NncCeSpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7)
)
if mibBuilder.loadTexts:
    nncCeSpvcTable.setStatus("current")
_NncCeSpvcTableEntry_Object = MibTableRow
nncCeSpvcTableEntry = _NncCeSpvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1)
)
nncCeSpvcTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncCeSpvcTableEntry.setStatus("current")
_NncCeSpvcTargEpAddr_Type = AtmFormatDisplay
_NncCeSpvcTargEpAddr_Object = MibTableColumn
nncCeSpvcTargEpAddr = _NncCeSpvcTargEpAddr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 1),
    _NncCeSpvcTargEpAddr_Type()
)
nncCeSpvcTargEpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcTargEpAddr.setStatus("current")


class _NncCeSpvcTargVpi_Type(Integer32):
    """Custom type nncCeSpvcTargVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NncCeSpvcTargVpi_Type.__name__ = "Integer32"
_NncCeSpvcTargVpi_Object = MibTableColumn
nncCeSpvcTargVpi = _NncCeSpvcTargVpi_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 2),
    _NncCeSpvcTargVpi_Type()
)
nncCeSpvcTargVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcTargVpi.setStatus("current")


class _NncCeSpvcTargVci_Type(Integer32):
    """Custom type nncCeSpvcTargVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NncCeSpvcTargVci_Type.__name__ = "Integer32"
_NncCeSpvcTargVci_Object = MibTableColumn
nncCeSpvcTargVci = _NncCeSpvcTargVci_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 3),
    _NncCeSpvcTargVci_Type()
)
nncCeSpvcTargVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcTargVci.setStatus("current")


class _NncCeSpvcTargCeNumber_Type(Integer32):
    """Custom type nncCeSpvcTargCeNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NncCeSpvcTargCeNumber_Type.__name__ = "Integer32"
_NncCeSpvcTargCeNumber_Object = MibTableColumn
nncCeSpvcTargCeNumber = _NncCeSpvcTargCeNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 4),
    _NncCeSpvcTargCeNumber_Type()
)
nncCeSpvcTargCeNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcTargCeNumber.setStatus("current")


class _NncCeSpvcTargEpType_Type(Integer32):
    """Custom type nncCeSpvcTargEpType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cellRelay", 1),
          ("circuitEmulation", 3))
    )


_NncCeSpvcTargEpType_Type.__name__ = "Integer32"
_NncCeSpvcTargEpType_Object = MibTableColumn
nncCeSpvcTargEpType = _NncCeSpvcTargEpType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 5),
    _NncCeSpvcTargEpType_Type()
)
nncCeSpvcTargEpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcTargEpType.setStatus("current")


class _NncCeSpvcAdminStatus_Type(Integer32):
    """Custom type nncCeSpvcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NncCeSpvcAdminStatus_Type.__name__ = "Integer32"
_NncCeSpvcAdminStatus_Object = MibTableColumn
nncCeSpvcAdminStatus = _NncCeSpvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 6),
    _NncCeSpvcAdminStatus_Type()
)
nncCeSpvcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcAdminStatus.setStatus("current")


class _NncCeSpvcPriority_Type(Integer32):
    """Custom type nncCeSpvcPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NncCeSpvcPriority_Type.__name__ = "Integer32"
_NncCeSpvcPriority_Object = MibTableColumn
nncCeSpvcPriority = _NncCeSpvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 7),
    _NncCeSpvcPriority_Type()
)
nncCeSpvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcPriority.setStatus("current")


class _NncCeSpvcMaxAdminWeight_Type(Integer32):
    """Custom type nncCeSpvcMaxAdminWeight based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NncCeSpvcMaxAdminWeight_Type.__name__ = "Integer32"
_NncCeSpvcMaxAdminWeight_Object = MibTableColumn
nncCeSpvcMaxAdminWeight = _NncCeSpvcMaxAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 8),
    _NncCeSpvcMaxAdminWeight_Type()
)
nncCeSpvcMaxAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcMaxAdminWeight.setStatus("current")


class _NncCeSpvcOperation_Type(Integer32):
    """Custom type nncCeSpvcOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("reRouteDualEp", 7)
    )


_NncCeSpvcOperation_Type.__name__ = "Integer32"
_NncCeSpvcOperation_Object = MibTableColumn
nncCeSpvcOperation = _NncCeSpvcOperation_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 9),
    _NncCeSpvcOperation_Type()
)
nncCeSpvcOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcOperation.setStatus("current")


class _NncCeSpvcCallStatus_Type(Integer32):
    """Custom type nncCeSpvcCallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("readyToConnect", 7),
          ("waitingForResources", 4))
    )


_NncCeSpvcCallStatus_Type.__name__ = "Integer32"
_NncCeSpvcCallStatus_Object = MibTableColumn
nncCeSpvcCallStatus = _NncCeSpvcCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 10),
    _NncCeSpvcCallStatus_Type()
)
nncCeSpvcCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCeSpvcCallStatus.setStatus("current")


class _NncCeSpvcLocRerouteConfig_Type(Integer32):
    """Custom type nncCeSpvcLocRerouteConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledNniSide", 3))
    )


_NncCeSpvcLocRerouteConfig_Type.__name__ = "Integer32"
_NncCeSpvcLocRerouteConfig_Object = MibTableColumn
nncCeSpvcLocRerouteConfig = _NncCeSpvcLocRerouteConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 11),
    _NncCeSpvcLocRerouteConfig_Type()
)
nncCeSpvcLocRerouteConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcLocRerouteConfig.setStatus("current")


class _NncCeSpvcFwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCeSpvcFwdTmBucketOneRate based on Integer32"""
    defaultValue = 73

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCeSpvcFwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCeSpvcFwdTmBucketOneRate_Object = MibTableColumn
nncCeSpvcFwdTmBucketOneRate = _NncCeSpvcFwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 12),
    _NncCeSpvcFwdTmBucketOneRate_Type()
)
nncCeSpvcFwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcFwdTmBucketOneRate.setStatus("current")


class _NncCeSpvcFwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCeSpvcFwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCeSpvcFwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCeSpvcFwdTmBucketOneCdvt_Object = MibTableColumn
nncCeSpvcFwdTmBucketOneCdvt = _NncCeSpvcFwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 13),
    _NncCeSpvcFwdTmBucketOneCdvt_Type()
)
nncCeSpvcFwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcFwdTmBucketOneCdvt.setStatus("current")


class _NncCeSpvcBwdTmBucketOneRate_Type(Integer32):
    """Custom type nncCeSpvcBwdTmBucketOneRate based on Integer32"""
    defaultValue = 73

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2488320),
    )


_NncCeSpvcBwdTmBucketOneRate_Type.__name__ = "Integer32"
_NncCeSpvcBwdTmBucketOneRate_Object = MibTableColumn
nncCeSpvcBwdTmBucketOneRate = _NncCeSpvcBwdTmBucketOneRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 14),
    _NncCeSpvcBwdTmBucketOneRate_Type()
)
nncCeSpvcBwdTmBucketOneRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcBwdTmBucketOneRate.setStatus("current")


class _NncCeSpvcBwdTmBucketOneCdvt_Type(Integer32):
    """Custom type nncCeSpvcBwdTmBucketOneCdvt based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCeSpvcBwdTmBucketOneCdvt_Type.__name__ = "Integer32"
_NncCeSpvcBwdTmBucketOneCdvt_Object = MibTableColumn
nncCeSpvcBwdTmBucketOneCdvt = _NncCeSpvcBwdTmBucketOneCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 15),
    _NncCeSpvcBwdTmBucketOneCdvt_Type()
)
nncCeSpvcBwdTmBucketOneCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcBwdTmBucketOneCdvt.setStatus("current")


class _NncCeSpvcCreator_Type(Integer32):
    """Custom type nncCeSpvcCreator based on Integer32"""
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


_NncCeSpvcCreator_Type.__name__ = "Integer32"
_NncCeSpvcCreator_Object = MibTableColumn
nncCeSpvcCreator = _NncCeSpvcCreator_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 16),
    _NncCeSpvcCreator_Type()
)
nncCeSpvcCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCeSpvcCreator.setStatus("current")
_NncCeSpvcRowStatus_Type = RowStatus
_NncCeSpvcRowStatus_Object = MibTableColumn
nncCeSpvcRowStatus = _NncCeSpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 7, 1, 17),
    _NncCeSpvcRowStatus_Type()
)
nncCeSpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcRowStatus.setStatus("current")
_NncCeSpvcDstCfgTable_Object = MibTable
nncCeSpvcDstCfgTable = _NncCeSpvcDstCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 8)
)
if mibBuilder.loadTexts:
    nncCeSpvcDstCfgTable.setStatus("current")
_NncCeSpvcDstCfgTableEntry_Object = MibTableRow
nncCeSpvcDstCfgTableEntry = _NncCeSpvcDstCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 8, 1)
)
nncCeSpvcDstCfgTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncCeSpvcDstCfgTableEntry.setStatus("current")


class _NncCeSpvcDstCfgCdvt_Type(Integer32):
    """Custom type nncCeSpvcDstCfgCdvt based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190000),
    )


_NncCeSpvcDstCfgCdvt_Type.__name__ = "Integer32"
_NncCeSpvcDstCfgCdvt_Object = MibTableColumn
nncCeSpvcDstCfgCdvt = _NncCeSpvcDstCfgCdvt_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 8, 1, 1),
    _NncCeSpvcDstCfgCdvt_Type()
)
nncCeSpvcDstCfgCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcDstCfgCdvt.setStatus("current")


class _NncCeSpvcDstCfgLocRerouteConfig_Type(Integer32):
    """Custom type nncCeSpvcDstCfgLocRerouteConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledNniSide", 3))
    )


_NncCeSpvcDstCfgLocRerouteConfig_Type.__name__ = "Integer32"
_NncCeSpvcDstCfgLocRerouteConfig_Object = MibTableColumn
nncCeSpvcDstCfgLocRerouteConfig = _NncCeSpvcDstCfgLocRerouteConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 8, 1, 2),
    _NncCeSpvcDstCfgLocRerouteConfig_Type()
)
nncCeSpvcDstCfgLocRerouteConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcDstCfgLocRerouteConfig.setStatus("current")
_NncCeSpvcDstCfgRowStatus_Type = RowStatus
_NncCeSpvcDstCfgRowStatus_Object = MibTableColumn
nncCeSpvcDstCfgRowStatus = _NncCeSpvcDstCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 1, 8, 1, 3),
    _NncCeSpvcDstCfgRowStatus_Type()
)
nncCeSpvcDstCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nncCeSpvcDstCfgRowStatus.setStatus("current")
_NncExtSpvcGroups_ObjectIdentity = ObjectIdentity
nncExtSpvcGroups = _NncExtSpvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3)
)
_NncExtSpvcCompliances_ObjectIdentity = ObjectIdentity
nncExtSpvcCompliances = _NncExtSpvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 4)
)

# Managed Objects groups

nncCrSpvpcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3, 1)
)
nncCrSpvpcGroup.setObjects(
      *(("NNCEXTSPVC-MIB", "nncCrSpvpcServiceCategory"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcTargEpAddr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcTargVpi"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcAdminStatus"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcPriority"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcMaxAdminWeight"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcOperation"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcCallStatus"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcLocRerouteConfig"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdAbrDynTrfcIcr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdAbrDynTrfcRif"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdAbrDynTrfcRdf"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdAbrDynTrfcIcr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdAbrDynTrfcRif"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdAbrDynTrfcRdf"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcSrcBillingFlag"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdTmTrafficDescriptor"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdTmPolicingOption"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdTmBucketOneRate"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdTmBucketOneCdvt"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdTmBucketTwoRate"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdTmBucketTwoMbs"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdTmCdv"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcFwdTmClr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdTmTrafficDescriptor"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdTmPolicingOption"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdTmBucketOneRate"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdTmBucketOneCdvt"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdTmBucketTwoRate"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdTmBucketTwoMbs"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdTmCdv"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcBwdTmClr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcCreator"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcRowStatus"))
)
if mibBuilder.loadTexts:
    nncCrSpvpcGroup.setStatus("current")

nncCrSpvpcDstCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3, 2)
)
nncCrSpvpcDstCfgGroup.setObjects(
      *(("NNCEXTSPVC-MIB", "nncCrSpvpcDstCfgCdvt"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcDstCfgPolicing"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcDstCfgBillingFlag"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcDstCfgLocRerouteConfig"),
        ("NNCEXTSPVC-MIB", "nncCrSpvpcDstCfgRowStatus"))
)
if mibBuilder.loadTexts:
    nncCrSpvpcDstCfgGroup.setStatus("current")

nncCrSpvccGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3, 3)
)
nncCrSpvccGroup.setObjects(
      *(("NNCEXTSPVC-MIB", "nncCrSpvccServiceCategory"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccTargEpAddr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccTargVpi"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccTargVci"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccTargDlci"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccTargCeNumber"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccTargEpType"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccAdminStatus"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccPriority"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccMaxAdminWeight"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccOperation"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccCallStatus"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccLocRerouteConfig"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdAbrDynTrfcIcr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdAbrDynTrfcRif"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdAbrDynTrfcRdf"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdAbrDynTrfcIcr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdAbrDynTrfcRif"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdAbrDynTrfcRdf"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccSrcBillingFlag"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmTrafficDescriptor"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmPolicingOption"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmBucketOneRate"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmBucketOneCdvt"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmBucketTwoRate"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmBucketTwoMbs"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmCdv"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmClr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFwdTmFrameDiscard"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmTrafficDescriptor"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmPolicingOption"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmBucketOneRate"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmBucketOneCdvt"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmBucketTwoRate"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmBucketTwoMbs"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmCdv"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmClr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccBwdTmFrameDiscard"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmAr"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmCir"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmBc"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmBe"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmIwf"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmPo"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmPacing"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmPtclMapping"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmClpMapping"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmDeMapping"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmEfciMapping"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmPvcMgntProfile"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccFrBwdTmSIWProfile"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccCreator"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccRowStatus"))
)
if mibBuilder.loadTexts:
    nncCrSpvccGroup.setStatus("current")

nncCrSpvccDstCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3, 4)
)
nncCrSpvccDstCfgGroup.setObjects(
      *(("NNCEXTSPVC-MIB", "nncCrSpvccDstCfgCdvt"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccDstCfgPolicing"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccDstCfgBillingFlag"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccDstCfgFrVsvdCongestionControl"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccDstCfgLocRerouteConfig"),
        ("NNCEXTSPVC-MIB", "nncCrSpvccDstCfgRowStatus"))
)
if mibBuilder.loadTexts:
    nncCrSpvccDstCfgGroup.setStatus("current")

nncFrSpvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3, 5)
)
nncFrSpvcGroup.setObjects(
      *(("NNCEXTSPVC-MIB", "nncFrSpvcSrcDlci"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTargEpAddr"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTargDlci"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTargVpi"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTargVci"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTargEpType"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcAdminStatus"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcPriority"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcMaxAdminWeight"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcOperation"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCallStatus"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcLocRerouteConfig"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcSrcBillingFlag"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFrPriority"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFrVsvdCongestionControl"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFwdFrMir"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFwdTmAr"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFwdTmCir"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFwdTmBc"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFwdTmBe"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTmIwf"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFwdTmPo"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcFwdTmPacing"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTmPtclMapping"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTmClpMapping"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTmDeMapping"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTmEfciMapping"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTmPvcMgntProfile"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTmSIWProfile"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcTmRemapDlci"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcBwdTmAr"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcBwdTmCir"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcBwdTmBc"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcBwdTmBe"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcBwdTmPo"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcBwdTmPacing"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrTmServiceCategory"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmTrafficDescriptor"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmPolicingOption"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmBucketOneRate"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmBucketOneCdvt"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmBucketTwoRate"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmBucketTwoMbs"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmCdv"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmClr"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCrBwdTmFrameDiscard"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcCreator"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcRowStatus"))
)
if mibBuilder.loadTexts:
    nncFrSpvcGroup.setStatus("current")

nncFrSpvcDstCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3, 6)
)
nncFrSpvcDstCfgGroup.setObjects(
      *(("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmAr"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmCir"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmBc"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmBe"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmIwf"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmPo"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmPacing"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmPtclMapping"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmClpMapping"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmDeMapping"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmEfciMapping"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmPvcMgntProfile"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmSIWProfile"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgTmRemapDlci"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgBillingFlag"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgFrPriority"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgLocRerouteConfig"),
        ("NNCEXTSPVC-MIB", "nncFrSpvcDstCfgRowStatus"))
)
if mibBuilder.loadTexts:
    nncFrSpvcDstCfgGroup.setStatus("current")

nncCeSpvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3, 7)
)
nncCeSpvcGroup.setObjects(
      *(("NNCEXTSPVC-MIB", "nncCeSpvcTargEpAddr"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcTargVpi"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcTargVci"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcTargCeNumber"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcTargEpType"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcAdminStatus"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcPriority"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcMaxAdminWeight"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcOperation"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcCallStatus"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcLocRerouteConfig"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcFwdTmBucketOneRate"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcFwdTmBucketOneCdvt"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcBwdTmBucketOneRate"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcBwdTmBucketOneCdvt"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcCreator"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcRowStatus"))
)
if mibBuilder.loadTexts:
    nncCeSpvcGroup.setStatus("current")

nncCeSpvcDstCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 3, 8)
)
nncCeSpvcDstCfgGroup.setObjects(
      *(("NNCEXTSPVC-MIB", "nncCeSpvcDstCfgCdvt"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcDstCfgLocRerouteConfig"),
        ("NNCEXTSPVC-MIB", "nncCeSpvcDstCfgRowStatus"))
)
if mibBuilder.loadTexts:
    nncCeSpvcDstCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncSpvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 82, 4, 1)
)
if mibBuilder.loadTexts:
    nncSpvcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCEXTSPVC-MIB",
    **{"AtmFormatDisplay": AtmFormatDisplay,
       "nncExtSpvc": nncExtSpvc,
       "nncExtSpvcObjects": nncExtSpvcObjects,
       "nncCrSpvpcTable": nncCrSpvpcTable,
       "nncCrSpvpcTableEntry": nncCrSpvpcTableEntry,
       "nncCrSpvpcServiceCategory": nncCrSpvpcServiceCategory,
       "nncCrSpvpcTargEpAddr": nncCrSpvpcTargEpAddr,
       "nncCrSpvpcTargVpi": nncCrSpvpcTargVpi,
       "nncCrSpvpcAdminStatus": nncCrSpvpcAdminStatus,
       "nncCrSpvpcPriority": nncCrSpvpcPriority,
       "nncCrSpvpcMaxAdminWeight": nncCrSpvpcMaxAdminWeight,
       "nncCrSpvpcOperation": nncCrSpvpcOperation,
       "nncCrSpvpcCallStatus": nncCrSpvpcCallStatus,
       "nncCrSpvpcLocRerouteConfig": nncCrSpvpcLocRerouteConfig,
       "nncCrSpvpcFwdAbrDynTrfcIcr": nncCrSpvpcFwdAbrDynTrfcIcr,
       "nncCrSpvpcFwdAbrDynTrfcRif": nncCrSpvpcFwdAbrDynTrfcRif,
       "nncCrSpvpcFwdAbrDynTrfcRdf": nncCrSpvpcFwdAbrDynTrfcRdf,
       "nncCrSpvpcBwdAbrDynTrfcIcr": nncCrSpvpcBwdAbrDynTrfcIcr,
       "nncCrSpvpcBwdAbrDynTrfcRif": nncCrSpvpcBwdAbrDynTrfcRif,
       "nncCrSpvpcBwdAbrDynTrfcRdf": nncCrSpvpcBwdAbrDynTrfcRdf,
       "nncCrSpvpcSrcBillingFlag": nncCrSpvpcSrcBillingFlag,
       "nncCrSpvpcFwdTmTrafficDescriptor": nncCrSpvpcFwdTmTrafficDescriptor,
       "nncCrSpvpcFwdTmPolicingOption": nncCrSpvpcFwdTmPolicingOption,
       "nncCrSpvpcFwdTmBucketOneRate": nncCrSpvpcFwdTmBucketOneRate,
       "nncCrSpvpcFwdTmBucketOneCdvt": nncCrSpvpcFwdTmBucketOneCdvt,
       "nncCrSpvpcFwdTmBucketTwoRate": nncCrSpvpcFwdTmBucketTwoRate,
       "nncCrSpvpcFwdTmBucketTwoMbs": nncCrSpvpcFwdTmBucketTwoMbs,
       "nncCrSpvpcFwdTmCdv": nncCrSpvpcFwdTmCdv,
       "nncCrSpvpcFwdTmClr": nncCrSpvpcFwdTmClr,
       "nncCrSpvpcBwdTmTrafficDescriptor": nncCrSpvpcBwdTmTrafficDescriptor,
       "nncCrSpvpcBwdTmPolicingOption": nncCrSpvpcBwdTmPolicingOption,
       "nncCrSpvpcBwdTmBucketOneRate": nncCrSpvpcBwdTmBucketOneRate,
       "nncCrSpvpcBwdTmBucketOneCdvt": nncCrSpvpcBwdTmBucketOneCdvt,
       "nncCrSpvpcBwdTmBucketTwoRate": nncCrSpvpcBwdTmBucketTwoRate,
       "nncCrSpvpcBwdTmBucketTwoMbs": nncCrSpvpcBwdTmBucketTwoMbs,
       "nncCrSpvpcBwdTmCdv": nncCrSpvpcBwdTmCdv,
       "nncCrSpvpcBwdTmClr": nncCrSpvpcBwdTmClr,
       "nncCrSpvpcCreator": nncCrSpvpcCreator,
       "nncCrSpvpcRowStatus": nncCrSpvpcRowStatus,
       "nncCrSpvpcDstCfgTable": nncCrSpvpcDstCfgTable,
       "nncCrSpvpcDstCfgTableEntry": nncCrSpvpcDstCfgTableEntry,
       "nncCrSpvpcDstCfgCdvt": nncCrSpvpcDstCfgCdvt,
       "nncCrSpvpcDstCfgPolicing": nncCrSpvpcDstCfgPolicing,
       "nncCrSpvpcDstCfgBillingFlag": nncCrSpvpcDstCfgBillingFlag,
       "nncCrSpvpcDstCfgLocRerouteConfig": nncCrSpvpcDstCfgLocRerouteConfig,
       "nncCrSpvpcDstCfgRowStatus": nncCrSpvpcDstCfgRowStatus,
       "nncCrSpvccTable": nncCrSpvccTable,
       "nncCrSpvccTableEntry": nncCrSpvccTableEntry,
       "nncCrSpvccServiceCategory": nncCrSpvccServiceCategory,
       "nncCrSpvccTargEpAddr": nncCrSpvccTargEpAddr,
       "nncCrSpvccTargVpi": nncCrSpvccTargVpi,
       "nncCrSpvccTargVci": nncCrSpvccTargVci,
       "nncCrSpvccTargDlci": nncCrSpvccTargDlci,
       "nncCrSpvccTargCeNumber": nncCrSpvccTargCeNumber,
       "nncCrSpvccTargEpType": nncCrSpvccTargEpType,
       "nncCrSpvccAdminStatus": nncCrSpvccAdminStatus,
       "nncCrSpvccPriority": nncCrSpvccPriority,
       "nncCrSpvccMaxAdminWeight": nncCrSpvccMaxAdminWeight,
       "nncCrSpvccOperation": nncCrSpvccOperation,
       "nncCrSpvccCallStatus": nncCrSpvccCallStatus,
       "nncCrSpvccLocRerouteConfig": nncCrSpvccLocRerouteConfig,
       "nncCrSpvccFwdAbrDynTrfcIcr": nncCrSpvccFwdAbrDynTrfcIcr,
       "nncCrSpvccFwdAbrDynTrfcRif": nncCrSpvccFwdAbrDynTrfcRif,
       "nncCrSpvccFwdAbrDynTrfcRdf": nncCrSpvccFwdAbrDynTrfcRdf,
       "nncCrSpvccBwdAbrDynTrfcIcr": nncCrSpvccBwdAbrDynTrfcIcr,
       "nncCrSpvccBwdAbrDynTrfcRif": nncCrSpvccBwdAbrDynTrfcRif,
       "nncCrSpvccBwdAbrDynTrfcRdf": nncCrSpvccBwdAbrDynTrfcRdf,
       "nncCrSpvccSrcBillingFlag": nncCrSpvccSrcBillingFlag,
       "nncCrSpvccFwdTmTrafficDescriptor": nncCrSpvccFwdTmTrafficDescriptor,
       "nncCrSpvccFwdTmPolicingOption": nncCrSpvccFwdTmPolicingOption,
       "nncCrSpvccFwdTmBucketOneRate": nncCrSpvccFwdTmBucketOneRate,
       "nncCrSpvccFwdTmBucketOneCdvt": nncCrSpvccFwdTmBucketOneCdvt,
       "nncCrSpvccFwdTmBucketTwoRate": nncCrSpvccFwdTmBucketTwoRate,
       "nncCrSpvccFwdTmBucketTwoMbs": nncCrSpvccFwdTmBucketTwoMbs,
       "nncCrSpvccFwdTmCdv": nncCrSpvccFwdTmCdv,
       "nncCrSpvccFwdTmClr": nncCrSpvccFwdTmClr,
       "nncCrSpvccFwdTmFrameDiscard": nncCrSpvccFwdTmFrameDiscard,
       "nncCrSpvccBwdTmTrafficDescriptor": nncCrSpvccBwdTmTrafficDescriptor,
       "nncCrSpvccBwdTmPolicingOption": nncCrSpvccBwdTmPolicingOption,
       "nncCrSpvccBwdTmBucketOneRate": nncCrSpvccBwdTmBucketOneRate,
       "nncCrSpvccBwdTmBucketOneCdvt": nncCrSpvccBwdTmBucketOneCdvt,
       "nncCrSpvccBwdTmBucketTwoRate": nncCrSpvccBwdTmBucketTwoRate,
       "nncCrSpvccBwdTmBucketTwoMbs": nncCrSpvccBwdTmBucketTwoMbs,
       "nncCrSpvccBwdTmCdv": nncCrSpvccBwdTmCdv,
       "nncCrSpvccBwdTmClr": nncCrSpvccBwdTmClr,
       "nncCrSpvccBwdTmFrameDiscard": nncCrSpvccBwdTmFrameDiscard,
       "nncCrSpvccFrBwdTmAr": nncCrSpvccFrBwdTmAr,
       "nncCrSpvccFrBwdTmCir": nncCrSpvccFrBwdTmCir,
       "nncCrSpvccFrBwdTmBc": nncCrSpvccFrBwdTmBc,
       "nncCrSpvccFrBwdTmBe": nncCrSpvccFrBwdTmBe,
       "nncCrSpvccFrBwdTmIwf": nncCrSpvccFrBwdTmIwf,
       "nncCrSpvccFrBwdTmPo": nncCrSpvccFrBwdTmPo,
       "nncCrSpvccFrBwdTmPacing": nncCrSpvccFrBwdTmPacing,
       "nncCrSpvccFrBwdTmPtclMapping": nncCrSpvccFrBwdTmPtclMapping,
       "nncCrSpvccFrBwdTmClpMapping": nncCrSpvccFrBwdTmClpMapping,
       "nncCrSpvccFrBwdTmDeMapping": nncCrSpvccFrBwdTmDeMapping,
       "nncCrSpvccFrBwdTmEfciMapping": nncCrSpvccFrBwdTmEfciMapping,
       "nncCrSpvccFrBwdTmPvcMgntProfile": nncCrSpvccFrBwdTmPvcMgntProfile,
       "nncCrSpvccFrBwdTmSIWProfile": nncCrSpvccFrBwdTmSIWProfile,
       "nncCrSpvccCreator": nncCrSpvccCreator,
       "nncCrSpvccRowStatus": nncCrSpvccRowStatus,
       "nncCrSpvccDstCfgTable": nncCrSpvccDstCfgTable,
       "nncCrSpvccDstCfgTableEntry": nncCrSpvccDstCfgTableEntry,
       "nncCrSpvccDstCfgCdvt": nncCrSpvccDstCfgCdvt,
       "nncCrSpvccDstCfgPolicing": nncCrSpvccDstCfgPolicing,
       "nncCrSpvccDstCfgBillingFlag": nncCrSpvccDstCfgBillingFlag,
       "nncCrSpvccDstCfgFrVsvdCongestionControl": nncCrSpvccDstCfgFrVsvdCongestionControl,
       "nncCrSpvccDstCfgLocRerouteConfig": nncCrSpvccDstCfgLocRerouteConfig,
       "nncCrSpvccDstCfgRowStatus": nncCrSpvccDstCfgRowStatus,
       "nncFrSpvcTable": nncFrSpvcTable,
       "nncFrSpvcTableEntry": nncFrSpvcTableEntry,
       "nncFrSpvcSrcDlci": nncFrSpvcSrcDlci,
       "nncFrSpvcTargEpAddr": nncFrSpvcTargEpAddr,
       "nncFrSpvcTargDlci": nncFrSpvcTargDlci,
       "nncFrSpvcTargVpi": nncFrSpvcTargVpi,
       "nncFrSpvcTargVci": nncFrSpvcTargVci,
       "nncFrSpvcTargEpType": nncFrSpvcTargEpType,
       "nncFrSpvcAdminStatus": nncFrSpvcAdminStatus,
       "nncFrSpvcPriority": nncFrSpvcPriority,
       "nncFrSpvcMaxAdminWeight": nncFrSpvcMaxAdminWeight,
       "nncFrSpvcOperation": nncFrSpvcOperation,
       "nncFrSpvcCallStatus": nncFrSpvcCallStatus,
       "nncFrSpvcLocRerouteConfig": nncFrSpvcLocRerouteConfig,
       "nncFrSpvcSrcBillingFlag": nncFrSpvcSrcBillingFlag,
       "nncFrSpvcFrPriority": nncFrSpvcFrPriority,
       "nncFrSpvcFrVsvdCongestionControl": nncFrSpvcFrVsvdCongestionControl,
       "nncFrSpvcFwdFrMir": nncFrSpvcFwdFrMir,
       "nncFrSpvcFwdTmAr": nncFrSpvcFwdTmAr,
       "nncFrSpvcFwdTmCir": nncFrSpvcFwdTmCir,
       "nncFrSpvcFwdTmBc": nncFrSpvcFwdTmBc,
       "nncFrSpvcFwdTmBe": nncFrSpvcFwdTmBe,
       "nncFrSpvcTmIwf": nncFrSpvcTmIwf,
       "nncFrSpvcFwdTmPo": nncFrSpvcFwdTmPo,
       "nncFrSpvcFwdTmPacing": nncFrSpvcFwdTmPacing,
       "nncFrSpvcTmPtclMapping": nncFrSpvcTmPtclMapping,
       "nncFrSpvcTmClpMapping": nncFrSpvcTmClpMapping,
       "nncFrSpvcTmDeMapping": nncFrSpvcTmDeMapping,
       "nncFrSpvcTmEfciMapping": nncFrSpvcTmEfciMapping,
       "nncFrSpvcTmPvcMgntProfile": nncFrSpvcTmPvcMgntProfile,
       "nncFrSpvcTmSIWProfile": nncFrSpvcTmSIWProfile,
       "nncFrSpvcTmRemapDlci": nncFrSpvcTmRemapDlci,
       "nncFrSpvcBwdFrMir": nncFrSpvcBwdFrMir,
       "nncFrSpvcBwdTmAr": nncFrSpvcBwdTmAr,
       "nncFrSpvcBwdTmCir": nncFrSpvcBwdTmCir,
       "nncFrSpvcBwdTmBc": nncFrSpvcBwdTmBc,
       "nncFrSpvcBwdTmBe": nncFrSpvcBwdTmBe,
       "nncFrSpvcBwdTmPo": nncFrSpvcBwdTmPo,
       "nncFrSpvcBwdTmPacing": nncFrSpvcBwdTmPacing,
       "nncFrSpvcCrTmServiceCategory": nncFrSpvcCrTmServiceCategory,
       "nncFrSpvcCrBwdTmTrafficDescriptor": nncFrSpvcCrBwdTmTrafficDescriptor,
       "nncFrSpvcCrBwdTmPolicingOption": nncFrSpvcCrBwdTmPolicingOption,
       "nncFrSpvcCrBwdTmBucketOneRate": nncFrSpvcCrBwdTmBucketOneRate,
       "nncFrSpvcCrBwdTmBucketOneCdvt": nncFrSpvcCrBwdTmBucketOneCdvt,
       "nncFrSpvcCrBwdTmBucketTwoRate": nncFrSpvcCrBwdTmBucketTwoRate,
       "nncFrSpvcCrBwdTmBucketTwoMbs": nncFrSpvcCrBwdTmBucketTwoMbs,
       "nncFrSpvcCrBwdTmCdv": nncFrSpvcCrBwdTmCdv,
       "nncFrSpvcCrBwdTmClr": nncFrSpvcCrBwdTmClr,
       "nncFrSpvcCrBwdTmFrameDiscard": nncFrSpvcCrBwdTmFrameDiscard,
       "nncFrSpvcCreator": nncFrSpvcCreator,
       "nncFrSpvcRowStatus": nncFrSpvcRowStatus,
       "nncFrSpvcDstCfgTable": nncFrSpvcDstCfgTable,
       "nncFrSpvcDstCfgTableEntry": nncFrSpvcDstCfgTableEntry,
       "nncFrSpvcDstCfgTmAr": nncFrSpvcDstCfgTmAr,
       "nncFrSpvcDstCfgTmCir": nncFrSpvcDstCfgTmCir,
       "nncFrSpvcDstCfgTmBc": nncFrSpvcDstCfgTmBc,
       "nncFrSpvcDstCfgTmBe": nncFrSpvcDstCfgTmBe,
       "nncFrSpvcDstCfgTmIwf": nncFrSpvcDstCfgTmIwf,
       "nncFrSpvcDstCfgTmPo": nncFrSpvcDstCfgTmPo,
       "nncFrSpvcDstCfgTmPacing": nncFrSpvcDstCfgTmPacing,
       "nncFrSpvcDstCfgTmPtclMapping": nncFrSpvcDstCfgTmPtclMapping,
       "nncFrSpvcDstCfgTmClpMapping": nncFrSpvcDstCfgTmClpMapping,
       "nncFrSpvcDstCfgTmDeMapping": nncFrSpvcDstCfgTmDeMapping,
       "nncFrSpvcDstCfgTmEfciMapping": nncFrSpvcDstCfgTmEfciMapping,
       "nncFrSpvcDstCfgTmPvcMgntProfile": nncFrSpvcDstCfgTmPvcMgntProfile,
       "nncFrSpvcDstCfgTmSIWProfile": nncFrSpvcDstCfgTmSIWProfile,
       "nncFrSpvcDstCfgTmRemapDlci": nncFrSpvcDstCfgTmRemapDlci,
       "nncFrSpvcDstCfgBillingFlag": nncFrSpvcDstCfgBillingFlag,
       "nncFrSpvcDstCfgFrPriority": nncFrSpvcDstCfgFrPriority,
       "nncFrSpvcDstCfgLocRerouteConfig": nncFrSpvcDstCfgLocRerouteConfig,
       "nncFrSpvcDstCfgRowStatus": nncFrSpvcDstCfgRowStatus,
       "nncCeSpvcTable": nncCeSpvcTable,
       "nncCeSpvcTableEntry": nncCeSpvcTableEntry,
       "nncCeSpvcTargEpAddr": nncCeSpvcTargEpAddr,
       "nncCeSpvcTargVpi": nncCeSpvcTargVpi,
       "nncCeSpvcTargVci": nncCeSpvcTargVci,
       "nncCeSpvcTargCeNumber": nncCeSpvcTargCeNumber,
       "nncCeSpvcTargEpType": nncCeSpvcTargEpType,
       "nncCeSpvcAdminStatus": nncCeSpvcAdminStatus,
       "nncCeSpvcPriority": nncCeSpvcPriority,
       "nncCeSpvcMaxAdminWeight": nncCeSpvcMaxAdminWeight,
       "nncCeSpvcOperation": nncCeSpvcOperation,
       "nncCeSpvcCallStatus": nncCeSpvcCallStatus,
       "nncCeSpvcLocRerouteConfig": nncCeSpvcLocRerouteConfig,
       "nncCeSpvcFwdTmBucketOneRate": nncCeSpvcFwdTmBucketOneRate,
       "nncCeSpvcFwdTmBucketOneCdvt": nncCeSpvcFwdTmBucketOneCdvt,
       "nncCeSpvcBwdTmBucketOneRate": nncCeSpvcBwdTmBucketOneRate,
       "nncCeSpvcBwdTmBucketOneCdvt": nncCeSpvcBwdTmBucketOneCdvt,
       "nncCeSpvcCreator": nncCeSpvcCreator,
       "nncCeSpvcRowStatus": nncCeSpvcRowStatus,
       "nncCeSpvcDstCfgTable": nncCeSpvcDstCfgTable,
       "nncCeSpvcDstCfgTableEntry": nncCeSpvcDstCfgTableEntry,
       "nncCeSpvcDstCfgCdvt": nncCeSpvcDstCfgCdvt,
       "nncCeSpvcDstCfgLocRerouteConfig": nncCeSpvcDstCfgLocRerouteConfig,
       "nncCeSpvcDstCfgRowStatus": nncCeSpvcDstCfgRowStatus,
       "nncExtSpvcGroups": nncExtSpvcGroups,
       "nncCrSpvpcGroup": nncCrSpvpcGroup,
       "nncCrSpvpcDstCfgGroup": nncCrSpvpcDstCfgGroup,
       "nncCrSpvccGroup": nncCrSpvccGroup,
       "nncCrSpvccDstCfgGroup": nncCrSpvccDstCfgGroup,
       "nncFrSpvcGroup": nncFrSpvcGroup,
       "nncFrSpvcDstCfgGroup": nncFrSpvcDstCfgGroup,
       "nncCeSpvcGroup": nncCeSpvcGroup,
       "nncCeSpvcDstCfgGroup": nncCeSpvcDstCfgGroup,
       "nncExtSpvcCompliances": nncExtSpvcCompliances,
       "nncSpvcCompliance": nncSpvcCompliance}
)
