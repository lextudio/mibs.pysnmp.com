# SNMP MIB module (HH3C-EOC-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EOC-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:07 2024
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

(hh3cHPEOCDownLoadCNUFWResult,) = mibBuilder.importSymbols(
    "HH3C-HPEOC-MIB",
    "hh3cHPEOCDownLoadCNUFWResult")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cEOCCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEOCCommonSysMan_ObjectIdentity = ObjectIdentity
hh3cEOCCommonSysMan = _Hh3cEOCCommonSysMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 1)
)
_Hh3cEOCCommonSysScalarObjects_ObjectIdentity = ObjectIdentity
hh3cEOCCommonSysScalarObjects = _Hh3cEOCCommonSysScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 1, 1)
)
_Hh3cEOCCommonSysVersion_Type = OctetString
_Hh3cEOCCommonSysVersion_Object = MibScalar
hh3cEOCCommonSysVersion = _Hh3cEOCCommonSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 1, 1, 1),
    _Hh3cEOCCommonSysVersion_Type()
)
hh3cEOCCommonSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCCommonSysVersion.setStatus("current")
_Hh3cEOCCommonUpLinkMacAddress_Type = MacAddress
_Hh3cEOCCommonUpLinkMacAddress_Object = MibScalar
hh3cEOCCommonUpLinkMacAddress = _Hh3cEOCCommonUpLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 1, 1, 2),
    _Hh3cEOCCommonUpLinkMacAddress_Type()
)
hh3cEOCCommonUpLinkMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCCommonUpLinkMacAddress.setStatus("current")
_Hh3cEOCCommonCltMan_ObjectIdentity = ObjectIdentity
hh3cEOCCommonCltMan = _Hh3cEOCCommonCltMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 2)
)
_Hh3cEOCCommonCltManTable_Object = MibTable
hh3cEOCCommonCltManTable = _Hh3cEOCCommonCltManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cEOCCommonCltManTable.setStatus("current")
_Hh3cEOCCommonCltManEntry_Object = MibTableRow
hh3cEOCCommonCltManEntry = _Hh3cEOCCommonCltManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 2, 1, 1)
)
hh3cEOCCommonCltManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEOCCommonCltManEntry.setStatus("current")


class _Hh3cEOCCommonCltAutoAuthorize_Type(TruthValue):
    """Custom type hh3cEOCCommonCltAutoAuthorize based on TruthValue"""


_Hh3cEOCCommonCltAutoAuthorize_Object = MibTableColumn
hh3cEOCCommonCltAutoAuthorize = _Hh3cEOCCommonCltAutoAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 2, 1, 1, 1),
    _Hh3cEOCCommonCltAutoAuthorize_Type()
)
hh3cEOCCommonCltAutoAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCCommonCltAutoAuthorize.setStatus("current")


class _Hh3cEOCCommonCltMaxAllowToAccess_Type(Integer32):
    """Custom type hh3cEOCCommonCltMaxAllowToAccess based on Integer32"""
    defaultValue = 253


_Hh3cEOCCommonCltMaxAllowToAccess_Object = MibTableColumn
hh3cEOCCommonCltMaxAllowToAccess = _Hh3cEOCCommonCltMaxAllowToAccess_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 2, 1, 1, 2),
    _Hh3cEOCCommonCltMaxAllowToAccess_Type()
)
hh3cEOCCommonCltMaxAllowToAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCCommonCltMaxAllowToAccess.setStatus("current")
_Hh3cEOCComCnuMan_ObjectIdentity = ObjectIdentity
hh3cEOCComCnuMan = _Hh3cEOCComCnuMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3)
)
_Hh3cEOCComCnuScalarObjects_ObjectIdentity = ObjectIdentity
hh3cEOCComCnuScalarObjects = _Hh3cEOCComCnuScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1)
)
_Hh3cEOCComCnuMaxDownBWMinVal_Type = Integer32
_Hh3cEOCComCnuMaxDownBWMinVal_Object = MibScalar
hh3cEOCComCnuMaxDownBWMinVal = _Hh3cEOCComCnuMaxDownBWMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 1),
    _Hh3cEOCComCnuMaxDownBWMinVal_Type()
)
hh3cEOCComCnuMaxDownBWMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuMaxDownBWMinVal.setStatus("current")
_Hh3cEOCComCnuMaxDownBWMaxVal_Type = Integer32
_Hh3cEOCComCnuMaxDownBWMaxVal_Object = MibScalar
hh3cEOCComCnuMaxDownBWMaxVal = _Hh3cEOCComCnuMaxDownBWMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 2),
    _Hh3cEOCComCnuMaxDownBWMaxVal_Type()
)
hh3cEOCComCnuMaxDownBWMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuMaxDownBWMaxVal.setStatus("current")
_Hh3cEOCComCnuSlaHighPriBWMinVal_Type = Integer32
_Hh3cEOCComCnuSlaHighPriBWMinVal_Object = MibScalar
hh3cEOCComCnuSlaHighPriBWMinVal = _Hh3cEOCComCnuSlaHighPriBWMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 3),
    _Hh3cEOCComCnuSlaHighPriBWMinVal_Type()
)
hh3cEOCComCnuSlaHighPriBWMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuSlaHighPriBWMinVal.setStatus("current")
_Hh3cEOCComCnuSlaHighPriBWMaxVal_Type = Integer32
_Hh3cEOCComCnuSlaHighPriBWMaxVal_Object = MibScalar
hh3cEOCComCnuSlaHighPriBWMaxVal = _Hh3cEOCComCnuSlaHighPriBWMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 4),
    _Hh3cEOCComCnuSlaHighPriBWMaxVal_Type()
)
hh3cEOCComCnuSlaHighPriBWMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuSlaHighPriBWMaxVal.setStatus("current")
_Hh3cEOCComCnuMaxUpBWMinVal_Type = Integer32
_Hh3cEOCComCnuMaxUpBWMinVal_Object = MibScalar
hh3cEOCComCnuMaxUpBWMinVal = _Hh3cEOCComCnuMaxUpBWMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 5),
    _Hh3cEOCComCnuMaxUpBWMinVal_Type()
)
hh3cEOCComCnuMaxUpBWMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuMaxUpBWMinVal.setStatus("current")
_Hh3cEOCComCnuMaxUpBWMaxVal_Type = Integer32
_Hh3cEOCComCnuMaxUpBWMaxVal_Object = MibScalar
hh3cEOCComCnuMaxUpBWMaxVal = _Hh3cEOCComCnuMaxUpBWMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 6),
    _Hh3cEOCComCnuMaxUpBWMaxVal_Type()
)
hh3cEOCComCnuMaxUpBWMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuMaxUpBWMaxVal.setStatus("current")
_Hh3cEOCComCnuAttenThrA_Type = Integer32
_Hh3cEOCComCnuAttenThrA_Object = MibScalar
hh3cEOCComCnuAttenThrA = _Hh3cEOCComCnuAttenThrA_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 7),
    _Hh3cEOCComCnuAttenThrA_Type()
)
hh3cEOCComCnuAttenThrA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuAttenThrA.setStatus("current")
_Hh3cEOCComCnuAttenThrB_Type = Integer32
_Hh3cEOCComCnuAttenThrB_Object = MibScalar
hh3cEOCComCnuAttenThrB = _Hh3cEOCComCnuAttenThrB_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 8),
    _Hh3cEOCComCnuAttenThrB_Type()
)
hh3cEOCComCnuAttenThrB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuAttenThrB.setStatus("current")
_Hh3cEOCComCnuRateDropThr_Type = Integer32
_Hh3cEOCComCnuRateDropThr_Object = MibScalar
hh3cEOCComCnuRateDropThr = _Hh3cEOCComCnuRateDropThr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 1, 9),
    _Hh3cEOCComCnuRateDropThr_Type()
)
hh3cEOCComCnuRateDropThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuRateDropThr.setStatus("current")
_Hh3cEOCComCnuSysManTable_Object = MibTable
hh3cEOCComCnuSysManTable = _Hh3cEOCComCnuSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuSysManTable.setStatus("current")
_Hh3cEOCComCnuSysManEntry_Object = MibTableRow
hh3cEOCComCnuSysManEntry = _Hh3cEOCComCnuSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1)
)
hh3cEOCComCnuSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuSysManEntry.setStatus("current")
_Hh3cEOCComCnuCableIfindex_Type = Integer32
_Hh3cEOCComCnuCableIfindex_Object = MibTableColumn
hh3cEOCComCnuCableIfindex = _Hh3cEOCComCnuCableIfindex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 1),
    _Hh3cEOCComCnuCableIfindex_Type()
)
hh3cEOCComCnuCableIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuCableIfindex.setStatus("current")
_Hh3cEOCComCnuDeviceType_Type = DisplayString
_Hh3cEOCComCnuDeviceType_Object = MibTableColumn
hh3cEOCComCnuDeviceType = _Hh3cEOCComCnuDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 2),
    _Hh3cEOCComCnuDeviceType_Type()
)
hh3cEOCComCnuDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuDeviceType.setStatus("current")
_Hh3cEOCComCnuDeviceAlias_Type = DisplayString
_Hh3cEOCComCnuDeviceAlias_Object = MibTableColumn
hh3cEOCComCnuDeviceAlias = _Hh3cEOCComCnuDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 3),
    _Hh3cEOCComCnuDeviceAlias_Type()
)
hh3cEOCComCnuDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuDeviceAlias.setStatus("current")
_Hh3cEOCComCnuDescr_Type = DisplayString
_Hh3cEOCComCnuDescr_Object = MibTableColumn
hh3cEOCComCnuDescr = _Hh3cEOCComCnuDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 4),
    _Hh3cEOCComCnuDescr_Type()
)
hh3cEOCComCnuDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuDescr.setStatus("current")
_Hh3cEOCComCnuUpTime_Type = TimeTicks
_Hh3cEOCComCnuUpTime_Object = MibTableColumn
hh3cEOCComCnuUpTime = _Hh3cEOCComCnuUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 5),
    _Hh3cEOCComCnuUpTime_Type()
)
hh3cEOCComCnuUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuUpTime.setStatus("current")


class _Hh3cEOCComCnuVLANType_Type(Integer32):
    """Custom type hh3cEOCComCnuVLANType based on Integer32"""
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
        *(("access", 2),
          ("fabric", 4),
          ("hybrid", 3),
          ("vLANTrunk", 1))
    )


_Hh3cEOCComCnuVLANType_Type.__name__ = "Integer32"
_Hh3cEOCComCnuVLANType_Object = MibTableColumn
hh3cEOCComCnuVLANType = _Hh3cEOCComCnuVLANType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 6),
    _Hh3cEOCComCnuVLANType_Type()
)
hh3cEOCComCnuVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuVLANType.setStatus("current")


class _Hh3cEOCComCnuPvid_Type(Integer32):
    """Custom type hh3cEOCComCnuPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cEOCComCnuPvid_Type.__name__ = "Integer32"
_Hh3cEOCComCnuPvid_Object = MibTableColumn
hh3cEOCComCnuPvid = _Hh3cEOCComCnuPvid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 7),
    _Hh3cEOCComCnuPvid_Type()
)
hh3cEOCComCnuPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuPvid.setStatus("current")


class _Hh3cEOCComCnuVlanTag_Type(Integer32):
    """Custom type hh3cEOCComCnuVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_Hh3cEOCComCnuVlanTag_Type.__name__ = "Integer32"
_Hh3cEOCComCnuVlanTag_Object = MibTableColumn
hh3cEOCComCnuVlanTag = _Hh3cEOCComCnuVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 8),
    _Hh3cEOCComCnuVlanTag_Type()
)
hh3cEOCComCnuVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuVlanTag.setStatus("current")


class _Hh3cEOCComCnuReset_Type(Integer32):
    """Custom type hh3cEOCComCnuReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("running", 1))
    )


_Hh3cEOCComCnuReset_Type.__name__ = "Integer32"
_Hh3cEOCComCnuReset_Object = MibTableColumn
hh3cEOCComCnuReset = _Hh3cEOCComCnuReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 9),
    _Hh3cEOCComCnuReset_Type()
)
hh3cEOCComCnuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuReset.setStatus("current")


class _Hh3cEOCComCnuDeregister_Type(Integer32):
    """Custom type hh3cEOCComCnuDeregister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deregister", 1)
    )


_Hh3cEOCComCnuDeregister_Type.__name__ = "Integer32"
_Hh3cEOCComCnuDeregister_Object = MibTableColumn
hh3cEOCComCnuDeregister = _Hh3cEOCComCnuDeregister_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 10),
    _Hh3cEOCComCnuDeregister_Type()
)
hh3cEOCComCnuDeregister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuDeregister.setStatus("current")


class _Hh3cEOCComCnuSave_Type(Integer32):
    """Custom type hh3cEOCComCnuSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("save", 1))
    )


_Hh3cEOCComCnuSave_Type.__name__ = "Integer32"
_Hh3cEOCComCnuSave_Object = MibTableColumn
hh3cEOCComCnuSave = _Hh3cEOCComCnuSave_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 11),
    _Hh3cEOCComCnuSave_Type()
)
hh3cEOCComCnuSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuSave.setStatus("current")


class _Hh3cEOCComCnuAccess_Type(Integer32):
    """Custom type hh3cEOCComCnuAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("notaccess", 2))
    )


_Hh3cEOCComCnuAccess_Type.__name__ = "Integer32"
_Hh3cEOCComCnuAccess_Object = MibTableColumn
hh3cEOCComCnuAccess = _Hh3cEOCComCnuAccess_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 2, 1, 12),
    _Hh3cEOCComCnuAccess_Type()
)
hh3cEOCComCnuAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuAccess.setStatus("current")
_Hh3cEOCComCnuMacTable_Object = MibTable
hh3cEOCComCnuMacTable = _Hh3cEOCComCnuMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuMacTable.setStatus("current")
_Hh3cEOCComCnuMacEntry_Object = MibTableRow
hh3cEOCComCnuMacEntry = _Hh3cEOCComCnuMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 3, 1)
)
hh3cEOCComCnuMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuMacEntry.setStatus("current")
_Hh3cEOCComCnuMacAddress_Type = MacAddress
_Hh3cEOCComCnuMacAddress_Object = MibTableColumn
hh3cEOCComCnuMacAddress = _Hh3cEOCComCnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 3, 1, 1),
    _Hh3cEOCComCnuMacAddress_Type()
)
hh3cEOCComCnuMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEOCComCnuMacAddress.setStatus("current")
_Hh3cEOCComCnuRowStatus_Type = RowStatus
_Hh3cEOCComCnuRowStatus_Object = MibTableColumn
hh3cEOCComCnuRowStatus = _Hh3cEOCComCnuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 3, 1, 2),
    _Hh3cEOCComCnuRowStatus_Type()
)
hh3cEOCComCnuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEOCComCnuRowStatus.setStatus("current")
_Hh3cEOCComCnuInfoTable_Object = MibTable
hh3cEOCComCnuInfoTable = _Hh3cEOCComCnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuInfoTable.setStatus("current")
_Hh3cEOCComCnuInfoEntry_Object = MibTableRow
hh3cEOCComCnuInfoEntry = _Hh3cEOCComCnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1)
)
hh3cEOCComCnuInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuInfoEntry.setStatus("current")
_Hh3cEOCComCnuHardwareVersion_Type = DisplayString
_Hh3cEOCComCnuHardwareVersion_Object = MibTableColumn
hh3cEOCComCnuHardwareVersion = _Hh3cEOCComCnuHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 1),
    _Hh3cEOCComCnuHardwareVersion_Type()
)
hh3cEOCComCnuHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuHardwareVersion.setStatus("current")


class _Hh3cEOCComCnuPCBVersion_Type(OctetString):
    """Custom type hh3cEOCComCnuPCBVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEOCComCnuPCBVersion_Type.__name__ = "OctetString"
_Hh3cEOCComCnuPCBVersion_Object = MibTableColumn
hh3cEOCComCnuPCBVersion = _Hh3cEOCComCnuPCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 2),
    _Hh3cEOCComCnuPCBVersion_Type()
)
hh3cEOCComCnuPCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuPCBVersion.setStatus("current")


class _Hh3cEOCComCnuLinkState_Type(Integer32):
    """Custom type hh3cEOCComCnuLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 2),
          ("linkup", 3),
          ("physicaldown", 1))
    )


_Hh3cEOCComCnuLinkState_Type.__name__ = "Integer32"
_Hh3cEOCComCnuLinkState_Object = MibTableColumn
hh3cEOCComCnuLinkState = _Hh3cEOCComCnuLinkState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 3),
    _Hh3cEOCComCnuLinkState_Type()
)
hh3cEOCComCnuLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuLinkState.setStatus("current")
_Hh3cEOCComCnuAttenuation_Type = Integer32
_Hh3cEOCComCnuAttenuation_Object = MibTableColumn
hh3cEOCComCnuAttenuation = _Hh3cEOCComCnuAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 4),
    _Hh3cEOCComCnuAttenuation_Type()
)
hh3cEOCComCnuAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuAttenuation.setStatus("current")
_Hh3cEOCComCnuSoftwareVersion_Type = DisplayString
_Hh3cEOCComCnuSoftwareVersion_Object = MibTableColumn
hh3cEOCComCnuSoftwareVersion = _Hh3cEOCComCnuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 5),
    _Hh3cEOCComCnuSoftwareVersion_Type()
)
hh3cEOCComCnuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuSoftwareVersion.setStatus("current")
_Hh3cEOCComCnuTxRate_Type = Integer32
_Hh3cEOCComCnuTxRate_Object = MibTableColumn
hh3cEOCComCnuTxRate = _Hh3cEOCComCnuTxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 6),
    _Hh3cEOCComCnuTxRate_Type()
)
hh3cEOCComCnuTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuTxRate.setStatus("current")
_Hh3cEOCComCnuRxRate_Type = Integer32
_Hh3cEOCComCnuRxRate_Object = MibTableColumn
hh3cEOCComCnuRxRate = _Hh3cEOCComCnuRxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 7),
    _Hh3cEOCComCnuRxRate_Type()
)
hh3cEOCComCnuRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuRxRate.setStatus("current")
_Hh3cEOCComCnuTxRateDrop_Type = Integer32
_Hh3cEOCComCnuTxRateDrop_Object = MibTableColumn
hh3cEOCComCnuTxRateDrop = _Hh3cEOCComCnuTxRateDrop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 8),
    _Hh3cEOCComCnuTxRateDrop_Type()
)
hh3cEOCComCnuTxRateDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuTxRateDrop.setStatus("current")
_Hh3cEOCComCnuRxRateDrop_Type = Integer32
_Hh3cEOCComCnuRxRateDrop_Object = MibTableColumn
hh3cEOCComCnuRxRateDrop = _Hh3cEOCComCnuRxRateDrop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 4, 1, 9),
    _Hh3cEOCComCnuRxRateDrop_Type()
)
hh3cEOCComCnuRxRateDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuRxRateDrop.setStatus("current")
_Hh3cEOCComCnuBandWidthTable_Object = MibTable
hh3cEOCComCnuBandWidthTable = _Hh3cEOCComCnuBandWidthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 5)
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuBandWidthTable.setStatus("current")
_Hh3cEOCComCnuBandWidthEntry_Object = MibTableRow
hh3cEOCComCnuBandWidthEntry = _Hh3cEOCComCnuBandWidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 5, 1)
)
hh3cEOCComCnuBandWidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuBandWidthEntry.setStatus("current")
_Hh3cEOCComCnuMaxDownBW_Type = Integer32
_Hh3cEOCComCnuMaxDownBW_Object = MibTableColumn
hh3cEOCComCnuMaxDownBW = _Hh3cEOCComCnuMaxDownBW_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 5, 1, 1),
    _Hh3cEOCComCnuMaxDownBW_Type()
)
hh3cEOCComCnuMaxDownBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuMaxDownBW.setStatus("current")
_Hh3cEOCComCnuSlaHighPriBW_Type = Integer32
_Hh3cEOCComCnuSlaHighPriBW_Object = MibTableColumn
hh3cEOCComCnuSlaHighPriBW = _Hh3cEOCComCnuSlaHighPriBW_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 5, 1, 2),
    _Hh3cEOCComCnuSlaHighPriBW_Type()
)
hh3cEOCComCnuSlaHighPriBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuSlaHighPriBW.setStatus("current")
_Hh3cEOCComCnuMaxUpBW_Type = Integer32
_Hh3cEOCComCnuMaxUpBW_Object = MibTableColumn
hh3cEOCComCnuMaxUpBW = _Hh3cEOCComCnuMaxUpBW_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 3, 5, 1, 3),
    _Hh3cEOCComCnuMaxUpBW_Type()
)
hh3cEOCComCnuMaxUpBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComCnuMaxUpBW.setStatus("current")
_Hh3cEOCComUniMan_ObjectIdentity = ObjectIdentity
hh3cEOCComUniMan = _Hh3cEOCComUniMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4)
)
_Hh3cEOCComUniManTable_Object = MibTable
hh3cEOCComUniManTable = _Hh3cEOCComUniManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cEOCComUniManTable.setStatus("current")
_Hh3cEOCComUniManEntry_Object = MibTableRow
hh3cEOCComUniManEntry = _Hh3cEOCComUniManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1)
)
hh3cEOCComUniManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EOC-COMMON-MIB", "hh3cEOCUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEOCComUniManEntry.setStatus("current")
_Hh3cEOCUniIndex_Type = Unsigned32
_Hh3cEOCUniIndex_Object = MibTableColumn
hh3cEOCUniIndex = _Hh3cEOCUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 1),
    _Hh3cEOCUniIndex_Type()
)
hh3cEOCUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEOCUniIndex.setStatus("current")
_Hh3cEOCComUniDescr_Type = DisplayString
_Hh3cEOCComUniDescr_Object = MibTableColumn
hh3cEOCComUniDescr = _Hh3cEOCComUniDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 2),
    _Hh3cEOCComUniDescr_Type()
)
hh3cEOCComUniDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComUniDescr.setStatus("current")


class _Hh3cEOCComUniStatus_Type(Integer32):
    """Custom type hh3cEOCComUniStatus based on Integer32"""
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


_Hh3cEOCComUniStatus_Type.__name__ = "Integer32"
_Hh3cEOCComUniStatus_Object = MibTableColumn
hh3cEOCComUniStatus = _Hh3cEOCComUniStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 3),
    _Hh3cEOCComUniStatus_Type()
)
hh3cEOCComUniStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniStatus.setStatus("current")


class _Hh3cEOCComUniSpeed_Type(Integer32):
    """Custom type hh3cEOCComUniSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("s100M", 100),
          ("s10M", 10))
    )


_Hh3cEOCComUniSpeed_Type.__name__ = "Integer32"
_Hh3cEOCComUniSpeed_Object = MibTableColumn
hh3cEOCComUniSpeed = _Hh3cEOCComUniSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 4),
    _Hh3cEOCComUniSpeed_Type()
)
hh3cEOCComUniSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniSpeed.setStatus("current")


class _Hh3cEOCComUniDuplex_Type(Integer32):
    """Custom type hh3cEOCComUniDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 1),
          ("half", 2))
    )


_Hh3cEOCComUniDuplex_Type.__name__ = "Integer32"
_Hh3cEOCComUniDuplex_Object = MibTableColumn
hh3cEOCComUniDuplex = _Hh3cEOCComUniDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 5),
    _Hh3cEOCComUniDuplex_Type()
)
hh3cEOCComUniDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniDuplex.setStatus("current")
_Hh3cEOCComUniCurrentSpeed_Type = Gauge32
_Hh3cEOCComUniCurrentSpeed_Object = MibTableColumn
hh3cEOCComUniCurrentSpeed = _Hh3cEOCComUniCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 6),
    _Hh3cEOCComUniCurrentSpeed_Type()
)
hh3cEOCComUniCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComUniCurrentSpeed.setStatus("current")


class _Hh3cEOCComUniCurrentDuplex_Type(Integer32):
    """Custom type hh3cEOCComUniCurrentDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("unknown", 3))
    )


_Hh3cEOCComUniCurrentDuplex_Type.__name__ = "Integer32"
_Hh3cEOCComUniCurrentDuplex_Object = MibTableColumn
hh3cEOCComUniCurrentDuplex = _Hh3cEOCComUniCurrentDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 7),
    _Hh3cEOCComUniCurrentDuplex_Type()
)
hh3cEOCComUniCurrentDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComUniCurrentDuplex.setStatus("current")


class _Hh3cEOCComUniMdi_Type(Integer32):
    """Custom type hh3cEOCComUniMdi based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi-auto", 3),
          ("mdi-ii", 1),
          ("mdi-x", 2))
    )


_Hh3cEOCComUniMdi_Type.__name__ = "Integer32"
_Hh3cEOCComUniMdi_Object = MibTableColumn
hh3cEOCComUniMdi = _Hh3cEOCComUniMdi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 8),
    _Hh3cEOCComUniMdi_Type()
)
hh3cEOCComUniMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniMdi.setStatus("current")


class _Hh3cEOCComUniFlowControl_Type(TruthValue):
    """Custom type hh3cEOCComUniFlowControl based on TruthValue"""


_Hh3cEOCComUniFlowControl_Object = MibTableColumn
hh3cEOCComUniFlowControl = _Hh3cEOCComUniFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 9),
    _Hh3cEOCComUniFlowControl_Type()
)
hh3cEOCComUniFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniFlowControl.setStatus("current")


class _Hh3cEOCComUniCountReset_Type(Integer32):
    """Custom type hh3cEOCComUniCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cEOCComUniCountReset_Type.__name__ = "Integer32"
_Hh3cEOCComUniCountReset_Object = MibTableColumn
hh3cEOCComUniCountReset = _Hh3cEOCComUniCountReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 10),
    _Hh3cEOCComUniCountReset_Type()
)
hh3cEOCComUniCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniCountReset.setStatus("current")
_Hh3cEOCComUniAlias_Type = DisplayString
_Hh3cEOCComUniAlias_Object = MibTableColumn
hh3cEOCComUniAlias = _Hh3cEOCComUniAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 11),
    _Hh3cEOCComUniAlias_Type()
)
hh3cEOCComUniAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniAlias.setStatus("current")
_Hh3cEOCComUniType_Type = IANAifType
_Hh3cEOCComUniType_Object = MibTableColumn
hh3cEOCComUniType = _Hh3cEOCComUniType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 12),
    _Hh3cEOCComUniType_Type()
)
hh3cEOCComUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComUniType.setStatus("current")


class _Hh3cEOCComUniVLANType_Type(Integer32):
    """Custom type hh3cEOCComUniVLANType based on Integer32"""
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
        *(("access", 2),
          ("fabric", 4),
          ("hybrid", 3),
          ("vLANTrunk", 1))
    )


_Hh3cEOCComUniVLANType_Type.__name__ = "Integer32"
_Hh3cEOCComUniVLANType_Object = MibTableColumn
hh3cEOCComUniVLANType = _Hh3cEOCComUniVLANType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 13),
    _Hh3cEOCComUniVLANType_Type()
)
hh3cEOCComUniVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniVLANType.setStatus("current")


class _Hh3cEOCComUniPvid_Type(Integer32):
    """Custom type hh3cEOCComUniPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cEOCComUniPvid_Type.__name__ = "Integer32"
_Hh3cEOCComUniPvid_Object = MibTableColumn
hh3cEOCComUniPvid = _Hh3cEOCComUniPvid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 14),
    _Hh3cEOCComUniPvid_Type()
)
hh3cEOCComUniPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniPvid.setStatus("current")


class _Hh3cEOCComUniVlanTag_Type(Integer32):
    """Custom type hh3cEOCComUniVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_Hh3cEOCComUniVlanTag_Type.__name__ = "Integer32"
_Hh3cEOCComUniVlanTag_Object = MibTableColumn
hh3cEOCComUniVlanTag = _Hh3cEOCComUniVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 15),
    _Hh3cEOCComUniVlanTag_Type()
)
hh3cEOCComUniVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniVlanTag.setStatus("current")


class _Hh3cEOCComUniPriority_Type(Integer32):
    """Custom type hh3cEOCComUniPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cEOCComUniPriority_Type.__name__ = "Integer32"
_Hh3cEOCComUniPriority_Object = MibTableColumn
hh3cEOCComUniPriority = _Hh3cEOCComUniPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 16),
    _Hh3cEOCComUniPriority_Type()
)
hh3cEOCComUniPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniPriority.setStatus("current")
_Hh3cEOCComUniUpLineRate_Type = Unsigned32
_Hh3cEOCComUniUpLineRate_Object = MibTableColumn
hh3cEOCComUniUpLineRate = _Hh3cEOCComUniUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 17),
    _Hh3cEOCComUniUpLineRate_Type()
)
hh3cEOCComUniUpLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniUpLineRate.setStatus("current")
_Hh3cEOCComUniDownLineRate_Type = Unsigned32
_Hh3cEOCComUniDownLineRate_Object = MibTableColumn
hh3cEOCComUniDownLineRate = _Hh3cEOCComUniDownLineRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 18),
    _Hh3cEOCComUniDownLineRate_Type()
)
hh3cEOCComUniDownLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniDownLineRate.setStatus("current")


class _Hh3cEOCComUniAdminStatus_Type(Integer32):
    """Custom type hh3cEOCComUniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Hh3cEOCComUniAdminStatus_Type.__name__ = "Integer32"
_Hh3cEOCComUniAdminStatus_Object = MibTableColumn
hh3cEOCComUniAdminStatus = _Hh3cEOCComUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 1, 1, 19),
    _Hh3cEOCComUniAdminStatus_Type()
)
hh3cEOCComUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEOCComUniAdminStatus.setStatus("current")
_Hh3cEOCComUniCountTable_Object = MibTable
hh3cEOCComUniCountTable = _Hh3cEOCComUniCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cEOCComUniCountTable.setStatus("current")
_Hh3cEOCComUniCountEntry_Object = MibTableRow
hh3cEOCComUniCountEntry = _Hh3cEOCComUniCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1)
)
hh3cEOCComUniCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EOC-COMMON-MIB", "hh3cEOCUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEOCComUniCountEntry.setStatus("current")
_Hh3cEOCUniInPkts_Type = Unsigned32
_Hh3cEOCUniInPkts_Object = MibTableColumn
hh3cEOCUniInPkts = _Hh3cEOCUniInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 1),
    _Hh3cEOCUniInPkts_Type()
)
hh3cEOCUniInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInPkts.setStatus("current")
_Hh3cEOCUniInUPkts_Type = Unsigned32
_Hh3cEOCUniInUPkts_Object = MibTableColumn
hh3cEOCUniInUPkts = _Hh3cEOCUniInUPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 2),
    _Hh3cEOCUniInUPkts_Type()
)
hh3cEOCUniInUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInUPkts.setStatus("current")
_Hh3cEOCUniInBPkts_Type = Unsigned32
_Hh3cEOCUniInBPkts_Object = MibTableColumn
hh3cEOCUniInBPkts = _Hh3cEOCUniInBPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 3),
    _Hh3cEOCUniInBPkts_Type()
)
hh3cEOCUniInBPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInBPkts.setStatus("current")
_Hh3cEOCUniInMPkts_Type = Unsigned32
_Hh3cEOCUniInMPkts_Object = MibTableColumn
hh3cEOCUniInMPkts = _Hh3cEOCUniInMPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 4),
    _Hh3cEOCUniInMPkts_Type()
)
hh3cEOCUniInMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInMPkts.setStatus("current")
_Hh3cEOCUniInPausePkts_Type = Unsigned32
_Hh3cEOCUniInPausePkts_Object = MibTableColumn
hh3cEOCUniInPausePkts = _Hh3cEOCUniInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 5),
    _Hh3cEOCUniInPausePkts_Type()
)
hh3cEOCUniInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInPausePkts.setStatus("current")
_Hh3cEOCUniInTotalErrors_Type = Unsigned32
_Hh3cEOCUniInTotalErrors_Object = MibTableColumn
hh3cEOCUniInTotalErrors = _Hh3cEOCUniInTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 6),
    _Hh3cEOCUniInTotalErrors_Type()
)
hh3cEOCUniInTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInTotalErrors.setStatus("current")
_Hh3cEOCUniInCRCErrs_Type = Unsigned32
_Hh3cEOCUniInCRCErrs_Object = MibTableColumn
hh3cEOCUniInCRCErrs = _Hh3cEOCUniInCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 7),
    _Hh3cEOCUniInCRCErrs_Type()
)
hh3cEOCUniInCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInCRCErrs.setStatus("current")
_Hh3cEOCUniInUndersizePkts_Type = Unsigned32
_Hh3cEOCUniInUndersizePkts_Object = MibTableColumn
hh3cEOCUniInUndersizePkts = _Hh3cEOCUniInUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 8),
    _Hh3cEOCUniInUndersizePkts_Type()
)
hh3cEOCUniInUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInUndersizePkts.setStatus("current")
_Hh3cEOCUniInOversizePkts_Type = Unsigned32
_Hh3cEOCUniInOversizePkts_Object = MibTableColumn
hh3cEOCUniInOversizePkts = _Hh3cEOCUniInOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 9),
    _Hh3cEOCUniInOversizePkts_Type()
)
hh3cEOCUniInOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInOversizePkts.setStatus("current")
_Hh3cEOCUniInErrorbyOther_Type = Unsigned32
_Hh3cEOCUniInErrorbyOther_Object = MibTableColumn
hh3cEOCUniInErrorbyOther = _Hh3cEOCUniInErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 10),
    _Hh3cEOCUniInErrorbyOther_Type()
)
hh3cEOCUniInErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInErrorbyOther.setStatus("current")
_Hh3cEOCUniInOctets_Type = Unsigned32
_Hh3cEOCUniInOctets_Object = MibTableColumn
hh3cEOCUniInOctets = _Hh3cEOCUniInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 11),
    _Hh3cEOCUniInOctets_Type()
)
hh3cEOCUniInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniInOctets.setStatus("current")
_Hh3cEOCUniOutPkts_Type = Unsigned32
_Hh3cEOCUniOutPkts_Object = MibTableColumn
hh3cEOCUniOutPkts = _Hh3cEOCUniOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 12),
    _Hh3cEOCUniOutPkts_Type()
)
hh3cEOCUniOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutPkts.setStatus("current")
_Hh3cEOCUniOutUPkts_Type = Unsigned32
_Hh3cEOCUniOutUPkts_Object = MibTableColumn
hh3cEOCUniOutUPkts = _Hh3cEOCUniOutUPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 13),
    _Hh3cEOCUniOutUPkts_Type()
)
hh3cEOCUniOutUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutUPkts.setStatus("current")
_Hh3cEOCUniOutBPkts_Type = Unsigned32
_Hh3cEOCUniOutBPkts_Object = MibTableColumn
hh3cEOCUniOutBPkts = _Hh3cEOCUniOutBPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 14),
    _Hh3cEOCUniOutBPkts_Type()
)
hh3cEOCUniOutBPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutBPkts.setStatus("current")
_Hh3cEOCUniOutMPkts_Type = Unsigned32
_Hh3cEOCUniOutMPkts_Object = MibTableColumn
hh3cEOCUniOutMPkts = _Hh3cEOCUniOutMPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 15),
    _Hh3cEOCUniOutMPkts_Type()
)
hh3cEOCUniOutMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutMPkts.setStatus("current")
_Hh3cEOCUniOutPausePkts_Type = Unsigned32
_Hh3cEOCUniOutPausePkts_Object = MibTableColumn
hh3cEOCUniOutPausePkts = _Hh3cEOCUniOutPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 16),
    _Hh3cEOCUniOutPausePkts_Type()
)
hh3cEOCUniOutPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutPausePkts.setStatus("current")
_Hh3cEOCUniOutTotalErrors_Type = Unsigned32
_Hh3cEOCUniOutTotalErrors_Object = MibTableColumn
hh3cEOCUniOutTotalErrors = _Hh3cEOCUniOutTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 17),
    _Hh3cEOCUniOutTotalErrors_Type()
)
hh3cEOCUniOutTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutTotalErrors.setStatus("current")
_Hh3cEOCUniOutCollisions_Type = Unsigned32
_Hh3cEOCUniOutCollisions_Object = MibTableColumn
hh3cEOCUniOutCollisions = _Hh3cEOCUniOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 18),
    _Hh3cEOCUniOutCollisions_Type()
)
hh3cEOCUniOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutCollisions.setStatus("current")
_Hh3cEOCUniOutDelayExceedDsds_Type = Unsigned32
_Hh3cEOCUniOutDelayExceedDsds_Object = MibTableColumn
hh3cEOCUniOutDelayExceedDsds = _Hh3cEOCUniOutDelayExceedDsds_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 19),
    _Hh3cEOCUniOutDelayExceedDsds_Type()
)
hh3cEOCUniOutDelayExceedDsds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutDelayExceedDsds.setStatus("current")
_Hh3cEOCUniOutErrorbyOther_Type = Unsigned32
_Hh3cEOCUniOutErrorbyOther_Object = MibTableColumn
hh3cEOCUniOutErrorbyOther = _Hh3cEOCUniOutErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 20),
    _Hh3cEOCUniOutErrorbyOther_Type()
)
hh3cEOCUniOutErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutErrorbyOther.setStatus("current")
_Hh3cEOCUniOutDroppedFrames_Type = Unsigned32
_Hh3cEOCUniOutDroppedFrames_Object = MibTableColumn
hh3cEOCUniOutDroppedFrames = _Hh3cEOCUniOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 21),
    _Hh3cEOCUniOutDroppedFrames_Type()
)
hh3cEOCUniOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutDroppedFrames.setStatus("current")
_Hh3cEOCUniOutOctets_Type = Unsigned32
_Hh3cEOCUniOutOctets_Object = MibTableColumn
hh3cEOCUniOutOctets = _Hh3cEOCUniOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 4, 2, 1, 22),
    _Hh3cEOCUniOutOctets_Type()
)
hh3cEOCUniOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCUniOutOctets.setStatus("current")
_Hh3cEOCCommonTrap_ObjectIdentity = ObjectIdentity
hh3cEOCCommonTrap = _Hh3cEOCCommonTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5)
)
_Hh3cEOCTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cEOCTrapPrefix = _Hh3cEOCTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0)
)
_Hh3cEOCComOnLineCnuMan_ObjectIdentity = ObjectIdentity
hh3cEOCComOnLineCnuMan = _Hh3cEOCComOnLineCnuMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 6)
)
_Hh3cEOCComCnuTypeTable_Object = MibTable
hh3cEOCComCnuTypeTable = _Hh3cEOCComCnuTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuTypeTable.setStatus("current")
_Hh3cEOCComCnuTypeEntry_Object = MibTableRow
hh3cEOCComCnuTypeEntry = _Hh3cEOCComCnuTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 6, 1, 1)
)
hh3cEOCComCnuTypeEntry.setIndexNames(
    (0, "HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuTypeIdx"),
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuTypeEntry.setStatus("current")
_Hh3cEOCComCnuTypeIdx_Type = Unsigned32
_Hh3cEOCComCnuTypeIdx_Object = MibTableColumn
hh3cEOCComCnuTypeIdx = _Hh3cEOCComCnuTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 6, 1, 1, 1),
    _Hh3cEOCComCnuTypeIdx_Type()
)
hh3cEOCComCnuTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEOCComCnuTypeIdx.setStatus("current")
_Hh3cEOCComCnuDescripton_Type = DisplayString
_Hh3cEOCComCnuDescripton_Object = MibTableColumn
hh3cEOCComCnuDescripton = _Hh3cEOCComCnuDescripton_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 6, 1, 1, 2),
    _Hh3cEOCComCnuDescripton_Type()
)
hh3cEOCComCnuDescripton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuDescripton.setStatus("current")
_Hh3cEOCComCnuNumTable_Object = MibTable
hh3cEOCComCnuNumTable = _Hh3cEOCComCnuNumTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuNumTable.setStatus("current")
_Hh3cEOCComCnuNumEntry_Object = MibTableRow
hh3cEOCComCnuNumEntry = _Hh3cEOCComCnuNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 6, 2, 1)
)
hh3cEOCComCnuNumEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuTypeIdx"),
)
if mibBuilder.loadTexts:
    hh3cEOCComCnuNumEntry.setStatus("current")
_Hh3cEOCComCnuNumber_Type = Integer32
_Hh3cEOCComCnuNumber_Object = MibTableColumn
hh3cEOCComCnuNumber = _Hh3cEOCComCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 6, 2, 1, 1),
    _Hh3cEOCComCnuNumber_Type()
)
hh3cEOCComCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEOCComCnuNumber.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cEOCCnuRegExcessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 1)
)
hh3cEOCCnuRegExcessTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuRegExcessTrap.setStatus(
        "current"
    )

hh3cEOCCnuRegExcessRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 2)
)
hh3cEOCCnuRegExcessRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuRegExcessRecoverTrap.setStatus(
        "current"
    )

hh3cEOCCnuRegSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 3)
)
hh3cEOCCnuRegSuccTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuRegSuccTrap.setStatus(
        "current"
    )

hh3cEOCCnuOffLineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 4)
)
hh3cEOCCnuOffLineTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuOffLineTrap.setStatus(
        "current"
    )

hh3cEOCCnuLinkupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 5)
)
hh3cEOCCnuLinkupTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuLinkupTrap.setStatus(
        "current"
    )

hh3cEOCOamDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 6)
)
hh3cEOCOamDisconnectTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCOamDisconnectTrap.setStatus(
        "current"
    )

hh3cEOCOamDisconnectRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 7)
)
hh3cEOCOamDisconnectRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCOamDisconnectRecoverTrap.setStatus(
        "current"
    )

hh3cEOCBandwidthNotEnoughTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 8)
)
hh3cEOCBandwidthNotEnoughTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCBandwidthNotEnoughTrap.setStatus(
        "current"
    )

hh3cEOCCnuAttenuationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 9)
)
hh3cEOCCnuAttenuationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuAttenuation"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuAttenuationTrap.setStatus(
        "current"
    )

hh3cEOCCnuRegFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 10)
)
hh3cEOCCnuRegFailTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuRegFailTrap.setStatus(
        "current"
    )

hh3cEOCCLTCablePortErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 11)
)
hh3cEOCCLTCablePortErrorTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCCLTCablePortErrorTrap.setStatus(
        "current"
    )

hh3cEOCCLTCablePortErrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 12)
)
hh3cEOCCLTCablePortErrReTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEOCCLTCablePortErrReTrap.setStatus(
        "current"
    )

hh3cEOCCnuTxRateDropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 13)
)
hh3cEOCCnuTxRateDropTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuTxRateDrop"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuTxRateDropTrap.setStatus(
        "current"
    )

hh3cEOCCnuTxRateDropRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 14)
)
hh3cEOCCnuTxRateDropRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuTxRateDrop"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuTxRateDropRecoverTrap.setStatus(
        "current"
    )

hh3cEOCCnuRxRateDropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 15)
)
hh3cEOCCnuRxRateDropTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuRxRateDrop"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuRxRateDropTrap.setStatus(
        "current"
    )

hh3cEOCCnuRxRateDropRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 16)
)
hh3cEOCCnuRxRateDropRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuRxRateDrop"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuRxRateDropRecoverTrap.setStatus(
        "current"
    )

hh3cEOCCnuFWDownLoadErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 17)
)
hh3cEOCCnuFWDownLoadErrTrap.setObjects(
    ("HH3C-HPEOC-MIB", "hh3cHPEOCDownLoadCNUFWResult")
)
if mibBuilder.loadTexts:
    hh3cEOCCnuFWDownLoadErrTrap.setStatus(
        "current"
    )

hh3cEOCCnuFWDownLoadErrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 18)
)
if mibBuilder.loadTexts:
    hh3cEOCCnuFWDownLoadErrReTrap.setStatus(
        "current"
    )

hh3cEOCCnuDeviceTypeErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 19)
)
hh3cEOCCnuDeviceTypeErrTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuDeviceType"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuDeviceTypeErrTrap.setStatus(
        "current"
    )

hh3cEOCCnuDeviceTypeErrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 20)
)
hh3cEOCCnuDeviceTypeErrReTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuDeviceTypeErrReTrap.setStatus(
        "current"
    )

hh3cEOCCnuAutoUpdateErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 21)
)
hh3cEOCCnuAutoUpdateErrTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuAutoUpdateErrTrap.setStatus(
        "current"
    )

hh3cEOCCnuAutoUpdateSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83, 5, 0, 22)
)
hh3cEOCCnuAutoUpdateSuccTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EOC-COMMON-MIB", "hh3cEOCComCnuMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cEOCCnuAutoUpdateSuccTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EOC-COMMON-MIB",
    **{"hh3cEOCCommon": hh3cEOCCommon,
       "hh3cEOCCommonSysMan": hh3cEOCCommonSysMan,
       "hh3cEOCCommonSysScalarObjects": hh3cEOCCommonSysScalarObjects,
       "hh3cEOCCommonSysVersion": hh3cEOCCommonSysVersion,
       "hh3cEOCCommonUpLinkMacAddress": hh3cEOCCommonUpLinkMacAddress,
       "hh3cEOCCommonCltMan": hh3cEOCCommonCltMan,
       "hh3cEOCCommonCltManTable": hh3cEOCCommonCltManTable,
       "hh3cEOCCommonCltManEntry": hh3cEOCCommonCltManEntry,
       "hh3cEOCCommonCltAutoAuthorize": hh3cEOCCommonCltAutoAuthorize,
       "hh3cEOCCommonCltMaxAllowToAccess": hh3cEOCCommonCltMaxAllowToAccess,
       "hh3cEOCComCnuMan": hh3cEOCComCnuMan,
       "hh3cEOCComCnuScalarObjects": hh3cEOCComCnuScalarObjects,
       "hh3cEOCComCnuMaxDownBWMinVal": hh3cEOCComCnuMaxDownBWMinVal,
       "hh3cEOCComCnuMaxDownBWMaxVal": hh3cEOCComCnuMaxDownBWMaxVal,
       "hh3cEOCComCnuSlaHighPriBWMinVal": hh3cEOCComCnuSlaHighPriBWMinVal,
       "hh3cEOCComCnuSlaHighPriBWMaxVal": hh3cEOCComCnuSlaHighPriBWMaxVal,
       "hh3cEOCComCnuMaxUpBWMinVal": hh3cEOCComCnuMaxUpBWMinVal,
       "hh3cEOCComCnuMaxUpBWMaxVal": hh3cEOCComCnuMaxUpBWMaxVal,
       "hh3cEOCComCnuAttenThrA": hh3cEOCComCnuAttenThrA,
       "hh3cEOCComCnuAttenThrB": hh3cEOCComCnuAttenThrB,
       "hh3cEOCComCnuRateDropThr": hh3cEOCComCnuRateDropThr,
       "hh3cEOCComCnuSysManTable": hh3cEOCComCnuSysManTable,
       "hh3cEOCComCnuSysManEntry": hh3cEOCComCnuSysManEntry,
       "hh3cEOCComCnuCableIfindex": hh3cEOCComCnuCableIfindex,
       "hh3cEOCComCnuDeviceType": hh3cEOCComCnuDeviceType,
       "hh3cEOCComCnuDeviceAlias": hh3cEOCComCnuDeviceAlias,
       "hh3cEOCComCnuDescr": hh3cEOCComCnuDescr,
       "hh3cEOCComCnuUpTime": hh3cEOCComCnuUpTime,
       "hh3cEOCComCnuVLANType": hh3cEOCComCnuVLANType,
       "hh3cEOCComCnuPvid": hh3cEOCComCnuPvid,
       "hh3cEOCComCnuVlanTag": hh3cEOCComCnuVlanTag,
       "hh3cEOCComCnuReset": hh3cEOCComCnuReset,
       "hh3cEOCComCnuDeregister": hh3cEOCComCnuDeregister,
       "hh3cEOCComCnuSave": hh3cEOCComCnuSave,
       "hh3cEOCComCnuAccess": hh3cEOCComCnuAccess,
       "hh3cEOCComCnuMacTable": hh3cEOCComCnuMacTable,
       "hh3cEOCComCnuMacEntry": hh3cEOCComCnuMacEntry,
       "hh3cEOCComCnuMacAddress": hh3cEOCComCnuMacAddress,
       "hh3cEOCComCnuRowStatus": hh3cEOCComCnuRowStatus,
       "hh3cEOCComCnuInfoTable": hh3cEOCComCnuInfoTable,
       "hh3cEOCComCnuInfoEntry": hh3cEOCComCnuInfoEntry,
       "hh3cEOCComCnuHardwareVersion": hh3cEOCComCnuHardwareVersion,
       "hh3cEOCComCnuPCBVersion": hh3cEOCComCnuPCBVersion,
       "hh3cEOCComCnuLinkState": hh3cEOCComCnuLinkState,
       "hh3cEOCComCnuAttenuation": hh3cEOCComCnuAttenuation,
       "hh3cEOCComCnuSoftwareVersion": hh3cEOCComCnuSoftwareVersion,
       "hh3cEOCComCnuTxRate": hh3cEOCComCnuTxRate,
       "hh3cEOCComCnuRxRate": hh3cEOCComCnuRxRate,
       "hh3cEOCComCnuTxRateDrop": hh3cEOCComCnuTxRateDrop,
       "hh3cEOCComCnuRxRateDrop": hh3cEOCComCnuRxRateDrop,
       "hh3cEOCComCnuBandWidthTable": hh3cEOCComCnuBandWidthTable,
       "hh3cEOCComCnuBandWidthEntry": hh3cEOCComCnuBandWidthEntry,
       "hh3cEOCComCnuMaxDownBW": hh3cEOCComCnuMaxDownBW,
       "hh3cEOCComCnuSlaHighPriBW": hh3cEOCComCnuSlaHighPriBW,
       "hh3cEOCComCnuMaxUpBW": hh3cEOCComCnuMaxUpBW,
       "hh3cEOCComUniMan": hh3cEOCComUniMan,
       "hh3cEOCComUniManTable": hh3cEOCComUniManTable,
       "hh3cEOCComUniManEntry": hh3cEOCComUniManEntry,
       "hh3cEOCUniIndex": hh3cEOCUniIndex,
       "hh3cEOCComUniDescr": hh3cEOCComUniDescr,
       "hh3cEOCComUniStatus": hh3cEOCComUniStatus,
       "hh3cEOCComUniSpeed": hh3cEOCComUniSpeed,
       "hh3cEOCComUniDuplex": hh3cEOCComUniDuplex,
       "hh3cEOCComUniCurrentSpeed": hh3cEOCComUniCurrentSpeed,
       "hh3cEOCComUniCurrentDuplex": hh3cEOCComUniCurrentDuplex,
       "hh3cEOCComUniMdi": hh3cEOCComUniMdi,
       "hh3cEOCComUniFlowControl": hh3cEOCComUniFlowControl,
       "hh3cEOCComUniCountReset": hh3cEOCComUniCountReset,
       "hh3cEOCComUniAlias": hh3cEOCComUniAlias,
       "hh3cEOCComUniType": hh3cEOCComUniType,
       "hh3cEOCComUniVLANType": hh3cEOCComUniVLANType,
       "hh3cEOCComUniPvid": hh3cEOCComUniPvid,
       "hh3cEOCComUniVlanTag": hh3cEOCComUniVlanTag,
       "hh3cEOCComUniPriority": hh3cEOCComUniPriority,
       "hh3cEOCComUniUpLineRate": hh3cEOCComUniUpLineRate,
       "hh3cEOCComUniDownLineRate": hh3cEOCComUniDownLineRate,
       "hh3cEOCComUniAdminStatus": hh3cEOCComUniAdminStatus,
       "hh3cEOCComUniCountTable": hh3cEOCComUniCountTable,
       "hh3cEOCComUniCountEntry": hh3cEOCComUniCountEntry,
       "hh3cEOCUniInPkts": hh3cEOCUniInPkts,
       "hh3cEOCUniInUPkts": hh3cEOCUniInUPkts,
       "hh3cEOCUniInBPkts": hh3cEOCUniInBPkts,
       "hh3cEOCUniInMPkts": hh3cEOCUniInMPkts,
       "hh3cEOCUniInPausePkts": hh3cEOCUniInPausePkts,
       "hh3cEOCUniInTotalErrors": hh3cEOCUniInTotalErrors,
       "hh3cEOCUniInCRCErrs": hh3cEOCUniInCRCErrs,
       "hh3cEOCUniInUndersizePkts": hh3cEOCUniInUndersizePkts,
       "hh3cEOCUniInOversizePkts": hh3cEOCUniInOversizePkts,
       "hh3cEOCUniInErrorbyOther": hh3cEOCUniInErrorbyOther,
       "hh3cEOCUniInOctets": hh3cEOCUniInOctets,
       "hh3cEOCUniOutPkts": hh3cEOCUniOutPkts,
       "hh3cEOCUniOutUPkts": hh3cEOCUniOutUPkts,
       "hh3cEOCUniOutBPkts": hh3cEOCUniOutBPkts,
       "hh3cEOCUniOutMPkts": hh3cEOCUniOutMPkts,
       "hh3cEOCUniOutPausePkts": hh3cEOCUniOutPausePkts,
       "hh3cEOCUniOutTotalErrors": hh3cEOCUniOutTotalErrors,
       "hh3cEOCUniOutCollisions": hh3cEOCUniOutCollisions,
       "hh3cEOCUniOutDelayExceedDsds": hh3cEOCUniOutDelayExceedDsds,
       "hh3cEOCUniOutErrorbyOther": hh3cEOCUniOutErrorbyOther,
       "hh3cEOCUniOutDroppedFrames": hh3cEOCUniOutDroppedFrames,
       "hh3cEOCUniOutOctets": hh3cEOCUniOutOctets,
       "hh3cEOCCommonTrap": hh3cEOCCommonTrap,
       "hh3cEOCTrapPrefix": hh3cEOCTrapPrefix,
       "hh3cEOCCnuRegExcessTrap": hh3cEOCCnuRegExcessTrap,
       "hh3cEOCCnuRegExcessRecoverTrap": hh3cEOCCnuRegExcessRecoverTrap,
       "hh3cEOCCnuRegSuccTrap": hh3cEOCCnuRegSuccTrap,
       "hh3cEOCCnuOffLineTrap": hh3cEOCCnuOffLineTrap,
       "hh3cEOCCnuLinkupTrap": hh3cEOCCnuLinkupTrap,
       "hh3cEOCOamDisconnectTrap": hh3cEOCOamDisconnectTrap,
       "hh3cEOCOamDisconnectRecoverTrap": hh3cEOCOamDisconnectRecoverTrap,
       "hh3cEOCBandwidthNotEnoughTrap": hh3cEOCBandwidthNotEnoughTrap,
       "hh3cEOCCnuAttenuationTrap": hh3cEOCCnuAttenuationTrap,
       "hh3cEOCCnuRegFailTrap": hh3cEOCCnuRegFailTrap,
       "hh3cEOCCLTCablePortErrorTrap": hh3cEOCCLTCablePortErrorTrap,
       "hh3cEOCCLTCablePortErrReTrap": hh3cEOCCLTCablePortErrReTrap,
       "hh3cEOCCnuTxRateDropTrap": hh3cEOCCnuTxRateDropTrap,
       "hh3cEOCCnuTxRateDropRecoverTrap": hh3cEOCCnuTxRateDropRecoverTrap,
       "hh3cEOCCnuRxRateDropTrap": hh3cEOCCnuRxRateDropTrap,
       "hh3cEOCCnuRxRateDropRecoverTrap": hh3cEOCCnuRxRateDropRecoverTrap,
       "hh3cEOCCnuFWDownLoadErrTrap": hh3cEOCCnuFWDownLoadErrTrap,
       "hh3cEOCCnuFWDownLoadErrReTrap": hh3cEOCCnuFWDownLoadErrReTrap,
       "hh3cEOCCnuDeviceTypeErrTrap": hh3cEOCCnuDeviceTypeErrTrap,
       "hh3cEOCCnuDeviceTypeErrReTrap": hh3cEOCCnuDeviceTypeErrReTrap,
       "hh3cEOCCnuAutoUpdateErrTrap": hh3cEOCCnuAutoUpdateErrTrap,
       "hh3cEOCCnuAutoUpdateSuccTrap": hh3cEOCCnuAutoUpdateSuccTrap,
       "hh3cEOCComOnLineCnuMan": hh3cEOCComOnLineCnuMan,
       "hh3cEOCComCnuTypeTable": hh3cEOCComCnuTypeTable,
       "hh3cEOCComCnuTypeEntry": hh3cEOCComCnuTypeEntry,
       "hh3cEOCComCnuTypeIdx": hh3cEOCComCnuTypeIdx,
       "hh3cEOCComCnuDescripton": hh3cEOCComCnuDescripton,
       "hh3cEOCComCnuNumTable": hh3cEOCComCnuNumTable,
       "hh3cEOCComCnuNumEntry": hh3cEOCComCnuNumEntry,
       "hh3cEOCComCnuNumber": hh3cEOCComCnuNumber}
)
