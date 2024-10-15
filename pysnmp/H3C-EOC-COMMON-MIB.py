# SNMP MIB module (H3C-EOC-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-EOC-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:27 2024
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

(h3cHPEOCDownLoadCNUFWResult,) = mibBuilder.importSymbols(
    "H3C-HPEOC-MIB",
    "h3cHPEOCDownLoadCNUFWResult")

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cEOCCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEOCCommonSysMan_ObjectIdentity = ObjectIdentity
h3cEOCCommonSysMan = _H3cEOCCommonSysMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 1)
)
_H3cEOCCommonSysScalarObjects_ObjectIdentity = ObjectIdentity
h3cEOCCommonSysScalarObjects = _H3cEOCCommonSysScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 1, 1)
)
_H3cEOCCommonSysVersion_Type = OctetString
_H3cEOCCommonSysVersion_Object = MibScalar
h3cEOCCommonSysVersion = _H3cEOCCommonSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 1, 1, 1),
    _H3cEOCCommonSysVersion_Type()
)
h3cEOCCommonSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCCommonSysVersion.setStatus("current")
_H3cEOCCommonUpLinkMacAddress_Type = MacAddress
_H3cEOCCommonUpLinkMacAddress_Object = MibScalar
h3cEOCCommonUpLinkMacAddress = _H3cEOCCommonUpLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 1, 1, 2),
    _H3cEOCCommonUpLinkMacAddress_Type()
)
h3cEOCCommonUpLinkMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCCommonUpLinkMacAddress.setStatus("current")
_H3cEOCCommonCltMan_ObjectIdentity = ObjectIdentity
h3cEOCCommonCltMan = _H3cEOCCommonCltMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 2)
)
_H3cEOCCommonCltManTable_Object = MibTable
h3cEOCCommonCltManTable = _H3cEOCCommonCltManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 2, 1)
)
if mibBuilder.loadTexts:
    h3cEOCCommonCltManTable.setStatus("current")
_H3cEOCCommonCltManEntry_Object = MibTableRow
h3cEOCCommonCltManEntry = _H3cEOCCommonCltManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 2, 1, 1)
)
h3cEOCCommonCltManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEOCCommonCltManEntry.setStatus("current")


class _H3cEOCCommonCltAutoAuthorize_Type(TruthValue):
    """Custom type h3cEOCCommonCltAutoAuthorize based on TruthValue"""


_H3cEOCCommonCltAutoAuthorize_Object = MibTableColumn
h3cEOCCommonCltAutoAuthorize = _H3cEOCCommonCltAutoAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 2, 1, 1, 1),
    _H3cEOCCommonCltAutoAuthorize_Type()
)
h3cEOCCommonCltAutoAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCCommonCltAutoAuthorize.setStatus("current")


class _H3cEOCCommonCltMaxAllowToAccess_Type(Integer32):
    """Custom type h3cEOCCommonCltMaxAllowToAccess based on Integer32"""
    defaultValue = 253


_H3cEOCCommonCltMaxAllowToAccess_Object = MibTableColumn
h3cEOCCommonCltMaxAllowToAccess = _H3cEOCCommonCltMaxAllowToAccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 2, 1, 1, 2),
    _H3cEOCCommonCltMaxAllowToAccess_Type()
)
h3cEOCCommonCltMaxAllowToAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCCommonCltMaxAllowToAccess.setStatus("current")
_H3cEOCComCnuMan_ObjectIdentity = ObjectIdentity
h3cEOCComCnuMan = _H3cEOCComCnuMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3)
)
_H3cEOCComCnuScalarObjects_ObjectIdentity = ObjectIdentity
h3cEOCComCnuScalarObjects = _H3cEOCComCnuScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1)
)
_H3cEOCComCnuMaxDownBWMinVal_Type = Integer32
_H3cEOCComCnuMaxDownBWMinVal_Object = MibScalar
h3cEOCComCnuMaxDownBWMinVal = _H3cEOCComCnuMaxDownBWMinVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 1),
    _H3cEOCComCnuMaxDownBWMinVal_Type()
)
h3cEOCComCnuMaxDownBWMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuMaxDownBWMinVal.setStatus("current")
_H3cEOCComCnuMaxDownBWMaxVal_Type = Integer32
_H3cEOCComCnuMaxDownBWMaxVal_Object = MibScalar
h3cEOCComCnuMaxDownBWMaxVal = _H3cEOCComCnuMaxDownBWMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 2),
    _H3cEOCComCnuMaxDownBWMaxVal_Type()
)
h3cEOCComCnuMaxDownBWMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuMaxDownBWMaxVal.setStatus("current")
_H3cEOCComCnuSlaHighPriBWMinVal_Type = Integer32
_H3cEOCComCnuSlaHighPriBWMinVal_Object = MibScalar
h3cEOCComCnuSlaHighPriBWMinVal = _H3cEOCComCnuSlaHighPriBWMinVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 3),
    _H3cEOCComCnuSlaHighPriBWMinVal_Type()
)
h3cEOCComCnuSlaHighPriBWMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuSlaHighPriBWMinVal.setStatus("current")
_H3cEOCComCnuSlaHighPriBWMaxVal_Type = Integer32
_H3cEOCComCnuSlaHighPriBWMaxVal_Object = MibScalar
h3cEOCComCnuSlaHighPriBWMaxVal = _H3cEOCComCnuSlaHighPriBWMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 4),
    _H3cEOCComCnuSlaHighPriBWMaxVal_Type()
)
h3cEOCComCnuSlaHighPriBWMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuSlaHighPriBWMaxVal.setStatus("current")
_H3cEOCComCnuMaxUpBWMinVal_Type = Integer32
_H3cEOCComCnuMaxUpBWMinVal_Object = MibScalar
h3cEOCComCnuMaxUpBWMinVal = _H3cEOCComCnuMaxUpBWMinVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 5),
    _H3cEOCComCnuMaxUpBWMinVal_Type()
)
h3cEOCComCnuMaxUpBWMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuMaxUpBWMinVal.setStatus("current")
_H3cEOCComCnuMaxUpBWMaxVal_Type = Integer32
_H3cEOCComCnuMaxUpBWMaxVal_Object = MibScalar
h3cEOCComCnuMaxUpBWMaxVal = _H3cEOCComCnuMaxUpBWMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 6),
    _H3cEOCComCnuMaxUpBWMaxVal_Type()
)
h3cEOCComCnuMaxUpBWMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuMaxUpBWMaxVal.setStatus("current")
_H3cEOCComCnuAttenThrA_Type = Integer32
_H3cEOCComCnuAttenThrA_Object = MibScalar
h3cEOCComCnuAttenThrA = _H3cEOCComCnuAttenThrA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 7),
    _H3cEOCComCnuAttenThrA_Type()
)
h3cEOCComCnuAttenThrA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuAttenThrA.setStatus("current")
_H3cEOCComCnuAttenThrB_Type = Integer32
_H3cEOCComCnuAttenThrB_Object = MibScalar
h3cEOCComCnuAttenThrB = _H3cEOCComCnuAttenThrB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 8),
    _H3cEOCComCnuAttenThrB_Type()
)
h3cEOCComCnuAttenThrB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuAttenThrB.setStatus("current")
_H3cEOCComCnuRateDropThr_Type = Integer32
_H3cEOCComCnuRateDropThr_Object = MibScalar
h3cEOCComCnuRateDropThr = _H3cEOCComCnuRateDropThr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 1, 9),
    _H3cEOCComCnuRateDropThr_Type()
)
h3cEOCComCnuRateDropThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuRateDropThr.setStatus("current")
_H3cEOCComCnuSysManTable_Object = MibTable
h3cEOCComCnuSysManTable = _H3cEOCComCnuSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2)
)
if mibBuilder.loadTexts:
    h3cEOCComCnuSysManTable.setStatus("current")
_H3cEOCComCnuSysManEntry_Object = MibTableRow
h3cEOCComCnuSysManEntry = _H3cEOCComCnuSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1)
)
h3cEOCComCnuSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEOCComCnuSysManEntry.setStatus("current")
_H3cEOCComCnuCableIfindex_Type = Integer32
_H3cEOCComCnuCableIfindex_Object = MibTableColumn
h3cEOCComCnuCableIfindex = _H3cEOCComCnuCableIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 1),
    _H3cEOCComCnuCableIfindex_Type()
)
h3cEOCComCnuCableIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuCableIfindex.setStatus("current")
_H3cEOCComCnuDeviceType_Type = DisplayString
_H3cEOCComCnuDeviceType_Object = MibTableColumn
h3cEOCComCnuDeviceType = _H3cEOCComCnuDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 2),
    _H3cEOCComCnuDeviceType_Type()
)
h3cEOCComCnuDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuDeviceType.setStatus("current")
_H3cEOCComCnuDeviceAlias_Type = DisplayString
_H3cEOCComCnuDeviceAlias_Object = MibTableColumn
h3cEOCComCnuDeviceAlias = _H3cEOCComCnuDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 3),
    _H3cEOCComCnuDeviceAlias_Type()
)
h3cEOCComCnuDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuDeviceAlias.setStatus("current")
_H3cEOCComCnuDescr_Type = DisplayString
_H3cEOCComCnuDescr_Object = MibTableColumn
h3cEOCComCnuDescr = _H3cEOCComCnuDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 4),
    _H3cEOCComCnuDescr_Type()
)
h3cEOCComCnuDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuDescr.setStatus("current")
_H3cEOCComCnuUpTime_Type = TimeTicks
_H3cEOCComCnuUpTime_Object = MibTableColumn
h3cEOCComCnuUpTime = _H3cEOCComCnuUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 5),
    _H3cEOCComCnuUpTime_Type()
)
h3cEOCComCnuUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuUpTime.setStatus("current")


class _H3cEOCComCnuVLANType_Type(Integer32):
    """Custom type h3cEOCComCnuVLANType based on Integer32"""
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


_H3cEOCComCnuVLANType_Type.__name__ = "Integer32"
_H3cEOCComCnuVLANType_Object = MibTableColumn
h3cEOCComCnuVLANType = _H3cEOCComCnuVLANType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 6),
    _H3cEOCComCnuVLANType_Type()
)
h3cEOCComCnuVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuVLANType.setStatus("current")


class _H3cEOCComCnuPvid_Type(Integer32):
    """Custom type h3cEOCComCnuPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cEOCComCnuPvid_Type.__name__ = "Integer32"
_H3cEOCComCnuPvid_Object = MibTableColumn
h3cEOCComCnuPvid = _H3cEOCComCnuPvid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 7),
    _H3cEOCComCnuPvid_Type()
)
h3cEOCComCnuPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuPvid.setStatus("current")


class _H3cEOCComCnuVlanTag_Type(Integer32):
    """Custom type h3cEOCComCnuVlanTag based on Integer32"""
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


_H3cEOCComCnuVlanTag_Type.__name__ = "Integer32"
_H3cEOCComCnuVlanTag_Object = MibTableColumn
h3cEOCComCnuVlanTag = _H3cEOCComCnuVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 8),
    _H3cEOCComCnuVlanTag_Type()
)
h3cEOCComCnuVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuVlanTag.setStatus("current")


class _H3cEOCComCnuReset_Type(Integer32):
    """Custom type h3cEOCComCnuReset based on Integer32"""
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


_H3cEOCComCnuReset_Type.__name__ = "Integer32"
_H3cEOCComCnuReset_Object = MibTableColumn
h3cEOCComCnuReset = _H3cEOCComCnuReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 9),
    _H3cEOCComCnuReset_Type()
)
h3cEOCComCnuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuReset.setStatus("current")


class _H3cEOCComCnuDeregister_Type(Integer32):
    """Custom type h3cEOCComCnuDeregister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deregister", 1)
    )


_H3cEOCComCnuDeregister_Type.__name__ = "Integer32"
_H3cEOCComCnuDeregister_Object = MibTableColumn
h3cEOCComCnuDeregister = _H3cEOCComCnuDeregister_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 10),
    _H3cEOCComCnuDeregister_Type()
)
h3cEOCComCnuDeregister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuDeregister.setStatus("current")


class _H3cEOCComCnuSave_Type(Integer32):
    """Custom type h3cEOCComCnuSave based on Integer32"""
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


_H3cEOCComCnuSave_Type.__name__ = "Integer32"
_H3cEOCComCnuSave_Object = MibTableColumn
h3cEOCComCnuSave = _H3cEOCComCnuSave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 11),
    _H3cEOCComCnuSave_Type()
)
h3cEOCComCnuSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuSave.setStatus("current")


class _H3cEOCComCnuAccess_Type(Integer32):
    """Custom type h3cEOCComCnuAccess based on Integer32"""
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


_H3cEOCComCnuAccess_Type.__name__ = "Integer32"
_H3cEOCComCnuAccess_Object = MibTableColumn
h3cEOCComCnuAccess = _H3cEOCComCnuAccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 2, 1, 12),
    _H3cEOCComCnuAccess_Type()
)
h3cEOCComCnuAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuAccess.setStatus("current")
_H3cEOCComCnuMacTable_Object = MibTable
h3cEOCComCnuMacTable = _H3cEOCComCnuMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 3)
)
if mibBuilder.loadTexts:
    h3cEOCComCnuMacTable.setStatus("current")
_H3cEOCComCnuMacEntry_Object = MibTableRow
h3cEOCComCnuMacEntry = _H3cEOCComCnuMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 3, 1)
)
h3cEOCComCnuMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEOCComCnuMacEntry.setStatus("current")
_H3cEOCComCnuMacAddress_Type = MacAddress
_H3cEOCComCnuMacAddress_Object = MibTableColumn
h3cEOCComCnuMacAddress = _H3cEOCComCnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 3, 1, 1),
    _H3cEOCComCnuMacAddress_Type()
)
h3cEOCComCnuMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEOCComCnuMacAddress.setStatus("current")
_H3cEOCComCnuRowStatus_Type = RowStatus
_H3cEOCComCnuRowStatus_Object = MibTableColumn
h3cEOCComCnuRowStatus = _H3cEOCComCnuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 3, 1, 2),
    _H3cEOCComCnuRowStatus_Type()
)
h3cEOCComCnuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEOCComCnuRowStatus.setStatus("current")
_H3cEOCComCnuInfoTable_Object = MibTable
h3cEOCComCnuInfoTable = _H3cEOCComCnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4)
)
if mibBuilder.loadTexts:
    h3cEOCComCnuInfoTable.setStatus("current")
_H3cEOCComCnuInfoEntry_Object = MibTableRow
h3cEOCComCnuInfoEntry = _H3cEOCComCnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1)
)
h3cEOCComCnuInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEOCComCnuInfoEntry.setStatus("current")
_H3cEOCComCnuHardwareVersion_Type = DisplayString
_H3cEOCComCnuHardwareVersion_Object = MibTableColumn
h3cEOCComCnuHardwareVersion = _H3cEOCComCnuHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 1),
    _H3cEOCComCnuHardwareVersion_Type()
)
h3cEOCComCnuHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuHardwareVersion.setStatus("current")


class _H3cEOCComCnuPCBVersion_Type(OctetString):
    """Custom type h3cEOCComCnuPCBVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEOCComCnuPCBVersion_Type.__name__ = "OctetString"
_H3cEOCComCnuPCBVersion_Object = MibTableColumn
h3cEOCComCnuPCBVersion = _H3cEOCComCnuPCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 2),
    _H3cEOCComCnuPCBVersion_Type()
)
h3cEOCComCnuPCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuPCBVersion.setStatus("current")


class _H3cEOCComCnuLinkState_Type(Integer32):
    """Custom type h3cEOCComCnuLinkState based on Integer32"""
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


_H3cEOCComCnuLinkState_Type.__name__ = "Integer32"
_H3cEOCComCnuLinkState_Object = MibTableColumn
h3cEOCComCnuLinkState = _H3cEOCComCnuLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 3),
    _H3cEOCComCnuLinkState_Type()
)
h3cEOCComCnuLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuLinkState.setStatus("current")
_H3cEOCComCnuAttenuation_Type = Integer32
_H3cEOCComCnuAttenuation_Object = MibTableColumn
h3cEOCComCnuAttenuation = _H3cEOCComCnuAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 4),
    _H3cEOCComCnuAttenuation_Type()
)
h3cEOCComCnuAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuAttenuation.setStatus("current")
_H3cEOCComCnuSoftwareVersion_Type = DisplayString
_H3cEOCComCnuSoftwareVersion_Object = MibTableColumn
h3cEOCComCnuSoftwareVersion = _H3cEOCComCnuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 5),
    _H3cEOCComCnuSoftwareVersion_Type()
)
h3cEOCComCnuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuSoftwareVersion.setStatus("current")
_H3cEOCComCnuTxRate_Type = Integer32
_H3cEOCComCnuTxRate_Object = MibTableColumn
h3cEOCComCnuTxRate = _H3cEOCComCnuTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 6),
    _H3cEOCComCnuTxRate_Type()
)
h3cEOCComCnuTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuTxRate.setStatus("current")
_H3cEOCComCnuRxRate_Type = Integer32
_H3cEOCComCnuRxRate_Object = MibTableColumn
h3cEOCComCnuRxRate = _H3cEOCComCnuRxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 7),
    _H3cEOCComCnuRxRate_Type()
)
h3cEOCComCnuRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuRxRate.setStatus("current")
_H3cEOCComCnuTxRateDrop_Type = Integer32
_H3cEOCComCnuTxRateDrop_Object = MibTableColumn
h3cEOCComCnuTxRateDrop = _H3cEOCComCnuTxRateDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 8),
    _H3cEOCComCnuTxRateDrop_Type()
)
h3cEOCComCnuTxRateDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuTxRateDrop.setStatus("current")
_H3cEOCComCnuRxRateDrop_Type = Integer32
_H3cEOCComCnuRxRateDrop_Object = MibTableColumn
h3cEOCComCnuRxRateDrop = _H3cEOCComCnuRxRateDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 4, 1, 9),
    _H3cEOCComCnuRxRateDrop_Type()
)
h3cEOCComCnuRxRateDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuRxRateDrop.setStatus("current")
_H3cEOCComCnuBandWidthTable_Object = MibTable
h3cEOCComCnuBandWidthTable = _H3cEOCComCnuBandWidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 5)
)
if mibBuilder.loadTexts:
    h3cEOCComCnuBandWidthTable.setStatus("current")
_H3cEOCComCnuBandWidthEntry_Object = MibTableRow
h3cEOCComCnuBandWidthEntry = _H3cEOCComCnuBandWidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 5, 1)
)
h3cEOCComCnuBandWidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEOCComCnuBandWidthEntry.setStatus("current")
_H3cEOCComCnuMaxDownBW_Type = Integer32
_H3cEOCComCnuMaxDownBW_Object = MibTableColumn
h3cEOCComCnuMaxDownBW = _H3cEOCComCnuMaxDownBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 5, 1, 1),
    _H3cEOCComCnuMaxDownBW_Type()
)
h3cEOCComCnuMaxDownBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuMaxDownBW.setStatus("current")
_H3cEOCComCnuSlaHighPriBW_Type = Integer32
_H3cEOCComCnuSlaHighPriBW_Object = MibTableColumn
h3cEOCComCnuSlaHighPriBW = _H3cEOCComCnuSlaHighPriBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 5, 1, 2),
    _H3cEOCComCnuSlaHighPriBW_Type()
)
h3cEOCComCnuSlaHighPriBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuSlaHighPriBW.setStatus("current")
_H3cEOCComCnuMaxUpBW_Type = Integer32
_H3cEOCComCnuMaxUpBW_Object = MibTableColumn
h3cEOCComCnuMaxUpBW = _H3cEOCComCnuMaxUpBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 3, 5, 1, 3),
    _H3cEOCComCnuMaxUpBW_Type()
)
h3cEOCComCnuMaxUpBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComCnuMaxUpBW.setStatus("current")
_H3cEOCComUniMan_ObjectIdentity = ObjectIdentity
h3cEOCComUniMan = _H3cEOCComUniMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4)
)
_H3cEOCComUniManTable_Object = MibTable
h3cEOCComUniManTable = _H3cEOCComUniManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1)
)
if mibBuilder.loadTexts:
    h3cEOCComUniManTable.setStatus("current")
_H3cEOCComUniManEntry_Object = MibTableRow
h3cEOCComUniManEntry = _H3cEOCComUniManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1)
)
h3cEOCComUniManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EOC-COMMON-MIB", "h3cEOCUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEOCComUniManEntry.setStatus("current")
_H3cEOCUniIndex_Type = Unsigned32
_H3cEOCUniIndex_Object = MibTableColumn
h3cEOCUniIndex = _H3cEOCUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 1),
    _H3cEOCUniIndex_Type()
)
h3cEOCUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEOCUniIndex.setStatus("current")
_H3cEOCComUniDescr_Type = DisplayString
_H3cEOCComUniDescr_Object = MibTableColumn
h3cEOCComUniDescr = _H3cEOCComUniDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 2),
    _H3cEOCComUniDescr_Type()
)
h3cEOCComUniDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComUniDescr.setStatus("current")


class _H3cEOCComUniStatus_Type(Integer32):
    """Custom type h3cEOCComUniStatus based on Integer32"""
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


_H3cEOCComUniStatus_Type.__name__ = "Integer32"
_H3cEOCComUniStatus_Object = MibTableColumn
h3cEOCComUniStatus = _H3cEOCComUniStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 3),
    _H3cEOCComUniStatus_Type()
)
h3cEOCComUniStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniStatus.setStatus("current")


class _H3cEOCComUniSpeed_Type(Integer32):
    """Custom type h3cEOCComUniSpeed based on Integer32"""
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


_H3cEOCComUniSpeed_Type.__name__ = "Integer32"
_H3cEOCComUniSpeed_Object = MibTableColumn
h3cEOCComUniSpeed = _H3cEOCComUniSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 4),
    _H3cEOCComUniSpeed_Type()
)
h3cEOCComUniSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniSpeed.setStatus("current")


class _H3cEOCComUniDuplex_Type(Integer32):
    """Custom type h3cEOCComUniDuplex based on Integer32"""
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


_H3cEOCComUniDuplex_Type.__name__ = "Integer32"
_H3cEOCComUniDuplex_Object = MibTableColumn
h3cEOCComUniDuplex = _H3cEOCComUniDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 5),
    _H3cEOCComUniDuplex_Type()
)
h3cEOCComUniDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniDuplex.setStatus("current")
_H3cEOCComUniCurrentSpeed_Type = Gauge32
_H3cEOCComUniCurrentSpeed_Object = MibTableColumn
h3cEOCComUniCurrentSpeed = _H3cEOCComUniCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 6),
    _H3cEOCComUniCurrentSpeed_Type()
)
h3cEOCComUniCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComUniCurrentSpeed.setStatus("current")


class _H3cEOCComUniCurrentDuplex_Type(Integer32):
    """Custom type h3cEOCComUniCurrentDuplex based on Integer32"""
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


_H3cEOCComUniCurrentDuplex_Type.__name__ = "Integer32"
_H3cEOCComUniCurrentDuplex_Object = MibTableColumn
h3cEOCComUniCurrentDuplex = _H3cEOCComUniCurrentDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 7),
    _H3cEOCComUniCurrentDuplex_Type()
)
h3cEOCComUniCurrentDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComUniCurrentDuplex.setStatus("current")


class _H3cEOCComUniMdi_Type(Integer32):
    """Custom type h3cEOCComUniMdi based on Integer32"""
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


_H3cEOCComUniMdi_Type.__name__ = "Integer32"
_H3cEOCComUniMdi_Object = MibTableColumn
h3cEOCComUniMdi = _H3cEOCComUniMdi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 8),
    _H3cEOCComUniMdi_Type()
)
h3cEOCComUniMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniMdi.setStatus("current")


class _H3cEOCComUniFlowControl_Type(TruthValue):
    """Custom type h3cEOCComUniFlowControl based on TruthValue"""


_H3cEOCComUniFlowControl_Object = MibTableColumn
h3cEOCComUniFlowControl = _H3cEOCComUniFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 9),
    _H3cEOCComUniFlowControl_Type()
)
h3cEOCComUniFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniFlowControl.setStatus("current")


class _H3cEOCComUniCountReset_Type(Integer32):
    """Custom type h3cEOCComUniCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_H3cEOCComUniCountReset_Type.__name__ = "Integer32"
_H3cEOCComUniCountReset_Object = MibTableColumn
h3cEOCComUniCountReset = _H3cEOCComUniCountReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 10),
    _H3cEOCComUniCountReset_Type()
)
h3cEOCComUniCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniCountReset.setStatus("current")
_H3cEOCComUniAlias_Type = DisplayString
_H3cEOCComUniAlias_Object = MibTableColumn
h3cEOCComUniAlias = _H3cEOCComUniAlias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 11),
    _H3cEOCComUniAlias_Type()
)
h3cEOCComUniAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniAlias.setStatus("current")
_H3cEOCComUniType_Type = IANAifType
_H3cEOCComUniType_Object = MibTableColumn
h3cEOCComUniType = _H3cEOCComUniType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 12),
    _H3cEOCComUniType_Type()
)
h3cEOCComUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComUniType.setStatus("current")


class _H3cEOCComUniVLANType_Type(Integer32):
    """Custom type h3cEOCComUniVLANType based on Integer32"""
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


_H3cEOCComUniVLANType_Type.__name__ = "Integer32"
_H3cEOCComUniVLANType_Object = MibTableColumn
h3cEOCComUniVLANType = _H3cEOCComUniVLANType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 13),
    _H3cEOCComUniVLANType_Type()
)
h3cEOCComUniVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniVLANType.setStatus("current")


class _H3cEOCComUniPvid_Type(Integer32):
    """Custom type h3cEOCComUniPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cEOCComUniPvid_Type.__name__ = "Integer32"
_H3cEOCComUniPvid_Object = MibTableColumn
h3cEOCComUniPvid = _H3cEOCComUniPvid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 14),
    _H3cEOCComUniPvid_Type()
)
h3cEOCComUniPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniPvid.setStatus("current")


class _H3cEOCComUniVlanTag_Type(Integer32):
    """Custom type h3cEOCComUniVlanTag based on Integer32"""
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


_H3cEOCComUniVlanTag_Type.__name__ = "Integer32"
_H3cEOCComUniVlanTag_Object = MibTableColumn
h3cEOCComUniVlanTag = _H3cEOCComUniVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 15),
    _H3cEOCComUniVlanTag_Type()
)
h3cEOCComUniVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniVlanTag.setStatus("current")


class _H3cEOCComUniPriority_Type(Integer32):
    """Custom type h3cEOCComUniPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cEOCComUniPriority_Type.__name__ = "Integer32"
_H3cEOCComUniPriority_Object = MibTableColumn
h3cEOCComUniPriority = _H3cEOCComUniPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 16),
    _H3cEOCComUniPriority_Type()
)
h3cEOCComUniPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniPriority.setStatus("current")
_H3cEOCComUniUpLineRate_Type = Unsigned32
_H3cEOCComUniUpLineRate_Object = MibTableColumn
h3cEOCComUniUpLineRate = _H3cEOCComUniUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 17),
    _H3cEOCComUniUpLineRate_Type()
)
h3cEOCComUniUpLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniUpLineRate.setStatus("current")
_H3cEOCComUniDownLineRate_Type = Unsigned32
_H3cEOCComUniDownLineRate_Object = MibTableColumn
h3cEOCComUniDownLineRate = _H3cEOCComUniDownLineRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 18),
    _H3cEOCComUniDownLineRate_Type()
)
h3cEOCComUniDownLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniDownLineRate.setStatus("current")


class _H3cEOCComUniAdminStatus_Type(Integer32):
    """Custom type h3cEOCComUniAdminStatus based on Integer32"""
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


_H3cEOCComUniAdminStatus_Type.__name__ = "Integer32"
_H3cEOCComUniAdminStatus_Object = MibTableColumn
h3cEOCComUniAdminStatus = _H3cEOCComUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 1, 1, 19),
    _H3cEOCComUniAdminStatus_Type()
)
h3cEOCComUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEOCComUniAdminStatus.setStatus("current")
_H3cEOCComUniCountTable_Object = MibTable
h3cEOCComUniCountTable = _H3cEOCComUniCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2)
)
if mibBuilder.loadTexts:
    h3cEOCComUniCountTable.setStatus("current")
_H3cEOCComUniCountEntry_Object = MibTableRow
h3cEOCComUniCountEntry = _H3cEOCComUniCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1)
)
h3cEOCComUniCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EOC-COMMON-MIB", "h3cEOCUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEOCComUniCountEntry.setStatus("current")
_H3cEOCUniInPkts_Type = Unsigned32
_H3cEOCUniInPkts_Object = MibTableColumn
h3cEOCUniInPkts = _H3cEOCUniInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 1),
    _H3cEOCUniInPkts_Type()
)
h3cEOCUniInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInPkts.setStatus("current")
_H3cEOCUniInUPkts_Type = Unsigned32
_H3cEOCUniInUPkts_Object = MibTableColumn
h3cEOCUniInUPkts = _H3cEOCUniInUPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 2),
    _H3cEOCUniInUPkts_Type()
)
h3cEOCUniInUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInUPkts.setStatus("current")
_H3cEOCUniInBPkts_Type = Unsigned32
_H3cEOCUniInBPkts_Object = MibTableColumn
h3cEOCUniInBPkts = _H3cEOCUniInBPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 3),
    _H3cEOCUniInBPkts_Type()
)
h3cEOCUniInBPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInBPkts.setStatus("current")
_H3cEOCUniInMPkts_Type = Unsigned32
_H3cEOCUniInMPkts_Object = MibTableColumn
h3cEOCUniInMPkts = _H3cEOCUniInMPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 4),
    _H3cEOCUniInMPkts_Type()
)
h3cEOCUniInMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInMPkts.setStatus("current")
_H3cEOCUniInPausePkts_Type = Unsigned32
_H3cEOCUniInPausePkts_Object = MibTableColumn
h3cEOCUniInPausePkts = _H3cEOCUniInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 5),
    _H3cEOCUniInPausePkts_Type()
)
h3cEOCUniInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInPausePkts.setStatus("current")
_H3cEOCUniInTotalErrors_Type = Unsigned32
_H3cEOCUniInTotalErrors_Object = MibTableColumn
h3cEOCUniInTotalErrors = _H3cEOCUniInTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 6),
    _H3cEOCUniInTotalErrors_Type()
)
h3cEOCUniInTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInTotalErrors.setStatus("current")
_H3cEOCUniInCRCErrs_Type = Unsigned32
_H3cEOCUniInCRCErrs_Object = MibTableColumn
h3cEOCUniInCRCErrs = _H3cEOCUniInCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 7),
    _H3cEOCUniInCRCErrs_Type()
)
h3cEOCUniInCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInCRCErrs.setStatus("current")
_H3cEOCUniInUndersizePkts_Type = Unsigned32
_H3cEOCUniInUndersizePkts_Object = MibTableColumn
h3cEOCUniInUndersizePkts = _H3cEOCUniInUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 8),
    _H3cEOCUniInUndersizePkts_Type()
)
h3cEOCUniInUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInUndersizePkts.setStatus("current")
_H3cEOCUniInOversizePkts_Type = Unsigned32
_H3cEOCUniInOversizePkts_Object = MibTableColumn
h3cEOCUniInOversizePkts = _H3cEOCUniInOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 9),
    _H3cEOCUniInOversizePkts_Type()
)
h3cEOCUniInOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInOversizePkts.setStatus("current")
_H3cEOCUniInErrorbyOther_Type = Unsigned32
_H3cEOCUniInErrorbyOther_Object = MibTableColumn
h3cEOCUniInErrorbyOther = _H3cEOCUniInErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 10),
    _H3cEOCUniInErrorbyOther_Type()
)
h3cEOCUniInErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInErrorbyOther.setStatus("current")
_H3cEOCUniInOctets_Type = Unsigned32
_H3cEOCUniInOctets_Object = MibTableColumn
h3cEOCUniInOctets = _H3cEOCUniInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 11),
    _H3cEOCUniInOctets_Type()
)
h3cEOCUniInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniInOctets.setStatus("current")
_H3cEOCUniOutPkts_Type = Unsigned32
_H3cEOCUniOutPkts_Object = MibTableColumn
h3cEOCUniOutPkts = _H3cEOCUniOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 12),
    _H3cEOCUniOutPkts_Type()
)
h3cEOCUniOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutPkts.setStatus("current")
_H3cEOCUniOutUPkts_Type = Unsigned32
_H3cEOCUniOutUPkts_Object = MibTableColumn
h3cEOCUniOutUPkts = _H3cEOCUniOutUPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 13),
    _H3cEOCUniOutUPkts_Type()
)
h3cEOCUniOutUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutUPkts.setStatus("current")
_H3cEOCUniOutBPkts_Type = Unsigned32
_H3cEOCUniOutBPkts_Object = MibTableColumn
h3cEOCUniOutBPkts = _H3cEOCUniOutBPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 14),
    _H3cEOCUniOutBPkts_Type()
)
h3cEOCUniOutBPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutBPkts.setStatus("current")
_H3cEOCUniOutMPkts_Type = Unsigned32
_H3cEOCUniOutMPkts_Object = MibTableColumn
h3cEOCUniOutMPkts = _H3cEOCUniOutMPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 15),
    _H3cEOCUniOutMPkts_Type()
)
h3cEOCUniOutMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutMPkts.setStatus("current")
_H3cEOCUniOutPausePkts_Type = Unsigned32
_H3cEOCUniOutPausePkts_Object = MibTableColumn
h3cEOCUniOutPausePkts = _H3cEOCUniOutPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 16),
    _H3cEOCUniOutPausePkts_Type()
)
h3cEOCUniOutPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutPausePkts.setStatus("current")
_H3cEOCUniOutTotalErrors_Type = Unsigned32
_H3cEOCUniOutTotalErrors_Object = MibTableColumn
h3cEOCUniOutTotalErrors = _H3cEOCUniOutTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 17),
    _H3cEOCUniOutTotalErrors_Type()
)
h3cEOCUniOutTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutTotalErrors.setStatus("current")
_H3cEOCUniOutCollisions_Type = Unsigned32
_H3cEOCUniOutCollisions_Object = MibTableColumn
h3cEOCUniOutCollisions = _H3cEOCUniOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 18),
    _H3cEOCUniOutCollisions_Type()
)
h3cEOCUniOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutCollisions.setStatus("current")
_H3cEOCUniOutDelayExceedDsds_Type = Unsigned32
_H3cEOCUniOutDelayExceedDsds_Object = MibTableColumn
h3cEOCUniOutDelayExceedDsds = _H3cEOCUniOutDelayExceedDsds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 19),
    _H3cEOCUniOutDelayExceedDsds_Type()
)
h3cEOCUniOutDelayExceedDsds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutDelayExceedDsds.setStatus("current")
_H3cEOCUniOutErrorbyOther_Type = Unsigned32
_H3cEOCUniOutErrorbyOther_Object = MibTableColumn
h3cEOCUniOutErrorbyOther = _H3cEOCUniOutErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 20),
    _H3cEOCUniOutErrorbyOther_Type()
)
h3cEOCUniOutErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutErrorbyOther.setStatus("current")
_H3cEOCUniOutDroppedFrames_Type = Unsigned32
_H3cEOCUniOutDroppedFrames_Object = MibTableColumn
h3cEOCUniOutDroppedFrames = _H3cEOCUniOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 21),
    _H3cEOCUniOutDroppedFrames_Type()
)
h3cEOCUniOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutDroppedFrames.setStatus("current")
_H3cEOCUniOutOctets_Type = Unsigned32
_H3cEOCUniOutOctets_Object = MibTableColumn
h3cEOCUniOutOctets = _H3cEOCUniOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 4, 2, 1, 22),
    _H3cEOCUniOutOctets_Type()
)
h3cEOCUniOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCUniOutOctets.setStatus("current")
_H3cEOCCommonTrap_ObjectIdentity = ObjectIdentity
h3cEOCCommonTrap = _H3cEOCCommonTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5)
)
_H3cEOCTrapPrefix_ObjectIdentity = ObjectIdentity
h3cEOCTrapPrefix = _H3cEOCTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0)
)
_H3cEOCComOnLineCnuMan_ObjectIdentity = ObjectIdentity
h3cEOCComOnLineCnuMan = _H3cEOCComOnLineCnuMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 6)
)
_H3cEOCComCnuTypeTable_Object = MibTable
h3cEOCComCnuTypeTable = _H3cEOCComCnuTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 6, 1)
)
if mibBuilder.loadTexts:
    h3cEOCComCnuTypeTable.setStatus("current")
_H3cEOCComCnuTypeEntry_Object = MibTableRow
h3cEOCComCnuTypeEntry = _H3cEOCComCnuTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 6, 1, 1)
)
h3cEOCComCnuTypeEntry.setIndexNames(
    (0, "H3C-EOC-COMMON-MIB", "h3cEOCComCnuTypeIdx"),
)
if mibBuilder.loadTexts:
    h3cEOCComCnuTypeEntry.setStatus("current")
_H3cEOCComCnuTypeIdx_Type = Unsigned32
_H3cEOCComCnuTypeIdx_Object = MibTableColumn
h3cEOCComCnuTypeIdx = _H3cEOCComCnuTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 6, 1, 1, 1),
    _H3cEOCComCnuTypeIdx_Type()
)
h3cEOCComCnuTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEOCComCnuTypeIdx.setStatus("current")
_H3cEOCComCnuDescripton_Type = DisplayString
_H3cEOCComCnuDescripton_Object = MibTableColumn
h3cEOCComCnuDescripton = _H3cEOCComCnuDescripton_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 6, 1, 1, 2),
    _H3cEOCComCnuDescripton_Type()
)
h3cEOCComCnuDescripton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuDescripton.setStatus("current")
_H3cEOCComCnuNumTable_Object = MibTable
h3cEOCComCnuNumTable = _H3cEOCComCnuNumTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 6, 2)
)
if mibBuilder.loadTexts:
    h3cEOCComCnuNumTable.setStatus("current")
_H3cEOCComCnuNumEntry_Object = MibTableRow
h3cEOCComCnuNumEntry = _H3cEOCComCnuNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 6, 2, 1)
)
h3cEOCComCnuNumEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EOC-COMMON-MIB", "h3cEOCComCnuTypeIdx"),
)
if mibBuilder.loadTexts:
    h3cEOCComCnuNumEntry.setStatus("current")
_H3cEOCComCnuNumber_Type = Integer32
_H3cEOCComCnuNumber_Object = MibTableColumn
h3cEOCComCnuNumber = _H3cEOCComCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 6, 2, 1, 1),
    _H3cEOCComCnuNumber_Type()
)
h3cEOCComCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEOCComCnuNumber.setStatus("current")

# Managed Objects groups


# Notification objects

h3cEOCCnuRegExcessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 1)
)
h3cEOCCnuRegExcessTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuRegExcessTrap.setStatus(
        "current"
    )

h3cEOCCnuRegExcessRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 2)
)
h3cEOCCnuRegExcessRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuRegExcessRecoverTrap.setStatus(
        "current"
    )

h3cEOCCnuRegSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 3)
)
h3cEOCCnuRegSuccTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuRegSuccTrap.setStatus(
        "current"
    )

h3cEOCCnuOffLineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 4)
)
h3cEOCCnuOffLineTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuOffLineTrap.setStatus(
        "current"
    )

h3cEOCCnuLinkupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 5)
)
h3cEOCCnuLinkupTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuLinkupTrap.setStatus(
        "current"
    )

h3cEOCOamDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 6)
)
h3cEOCOamDisconnectTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCOamDisconnectTrap.setStatus(
        "current"
    )

h3cEOCOamDisconnectRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 7)
)
h3cEOCOamDisconnectRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCOamDisconnectRecoverTrap.setStatus(
        "current"
    )

h3cEOCBandwidthNotEnoughTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 8)
)
h3cEOCBandwidthNotEnoughTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCBandwidthNotEnoughTrap.setStatus(
        "current"
    )

h3cEOCCnuAttenuationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 9)
)
h3cEOCCnuAttenuationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuAttenuation"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuAttenuationTrap.setStatus(
        "current"
    )

h3cEOCCnuRegFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 10)
)
h3cEOCCnuRegFailTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuRegFailTrap.setStatus(
        "current"
    )

h3cEOCCLTCablePortErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 11)
)
h3cEOCCLTCablePortErrorTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCCLTCablePortErrorTrap.setStatus(
        "current"
    )

h3cEOCCLTCablePortErrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 12)
)
h3cEOCCLTCablePortErrReTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cEOCCLTCablePortErrReTrap.setStatus(
        "current"
    )

h3cEOCCnuTxRateDropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 13)
)
h3cEOCCnuTxRateDropTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuTxRateDrop"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuTxRateDropTrap.setStatus(
        "current"
    )

h3cEOCCnuTxRateDropRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 14)
)
h3cEOCCnuTxRateDropRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuTxRateDrop"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuTxRateDropRecoverTrap.setStatus(
        "current"
    )

h3cEOCCnuRxRateDropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 15)
)
h3cEOCCnuRxRateDropTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuRxRateDrop"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuRxRateDropTrap.setStatus(
        "current"
    )

h3cEOCCnuRxRateDropRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 16)
)
h3cEOCCnuRxRateDropRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuRxRateDrop"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuRxRateDropRecoverTrap.setStatus(
        "current"
    )

h3cEOCCnuFWDownLoadErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 17)
)
h3cEOCCnuFWDownLoadErrTrap.setObjects(
    ("H3C-HPEOC-MIB", "h3cHPEOCDownLoadCNUFWResult")
)
if mibBuilder.loadTexts:
    h3cEOCCnuFWDownLoadErrTrap.setStatus(
        "current"
    )

h3cEOCCnuFWDownLoadErrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 18)
)
if mibBuilder.loadTexts:
    h3cEOCCnuFWDownLoadErrReTrap.setStatus(
        "current"
    )

h3cEOCCnuDeviceTypeErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 19)
)
h3cEOCCnuDeviceTypeErrTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuDeviceType"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuDeviceTypeErrTrap.setStatus(
        "current"
    )

h3cEOCCnuDeviceTypeErrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 20)
)
h3cEOCCnuDeviceTypeErrReTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuDeviceTypeErrReTrap.setStatus(
        "current"
    )

h3cEOCCnuAutoUpdateErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 21)
)
h3cEOCCnuAutoUpdateErrTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuAutoUpdateErrTrap.setStatus(
        "current"
    )

h3cEOCCnuAutoUpdateSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 83, 5, 0, 22)
)
h3cEOCCnuAutoUpdateSuccTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-EOC-COMMON-MIB", "h3cEOCComCnuMacAddress"))
)
if mibBuilder.loadTexts:
    h3cEOCCnuAutoUpdateSuccTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-EOC-COMMON-MIB",
    **{"h3cEOCCommon": h3cEOCCommon,
       "h3cEOCCommonSysMan": h3cEOCCommonSysMan,
       "h3cEOCCommonSysScalarObjects": h3cEOCCommonSysScalarObjects,
       "h3cEOCCommonSysVersion": h3cEOCCommonSysVersion,
       "h3cEOCCommonUpLinkMacAddress": h3cEOCCommonUpLinkMacAddress,
       "h3cEOCCommonCltMan": h3cEOCCommonCltMan,
       "h3cEOCCommonCltManTable": h3cEOCCommonCltManTable,
       "h3cEOCCommonCltManEntry": h3cEOCCommonCltManEntry,
       "h3cEOCCommonCltAutoAuthorize": h3cEOCCommonCltAutoAuthorize,
       "h3cEOCCommonCltMaxAllowToAccess": h3cEOCCommonCltMaxAllowToAccess,
       "h3cEOCComCnuMan": h3cEOCComCnuMan,
       "h3cEOCComCnuScalarObjects": h3cEOCComCnuScalarObjects,
       "h3cEOCComCnuMaxDownBWMinVal": h3cEOCComCnuMaxDownBWMinVal,
       "h3cEOCComCnuMaxDownBWMaxVal": h3cEOCComCnuMaxDownBWMaxVal,
       "h3cEOCComCnuSlaHighPriBWMinVal": h3cEOCComCnuSlaHighPriBWMinVal,
       "h3cEOCComCnuSlaHighPriBWMaxVal": h3cEOCComCnuSlaHighPriBWMaxVal,
       "h3cEOCComCnuMaxUpBWMinVal": h3cEOCComCnuMaxUpBWMinVal,
       "h3cEOCComCnuMaxUpBWMaxVal": h3cEOCComCnuMaxUpBWMaxVal,
       "h3cEOCComCnuAttenThrA": h3cEOCComCnuAttenThrA,
       "h3cEOCComCnuAttenThrB": h3cEOCComCnuAttenThrB,
       "h3cEOCComCnuRateDropThr": h3cEOCComCnuRateDropThr,
       "h3cEOCComCnuSysManTable": h3cEOCComCnuSysManTable,
       "h3cEOCComCnuSysManEntry": h3cEOCComCnuSysManEntry,
       "h3cEOCComCnuCableIfindex": h3cEOCComCnuCableIfindex,
       "h3cEOCComCnuDeviceType": h3cEOCComCnuDeviceType,
       "h3cEOCComCnuDeviceAlias": h3cEOCComCnuDeviceAlias,
       "h3cEOCComCnuDescr": h3cEOCComCnuDescr,
       "h3cEOCComCnuUpTime": h3cEOCComCnuUpTime,
       "h3cEOCComCnuVLANType": h3cEOCComCnuVLANType,
       "h3cEOCComCnuPvid": h3cEOCComCnuPvid,
       "h3cEOCComCnuVlanTag": h3cEOCComCnuVlanTag,
       "h3cEOCComCnuReset": h3cEOCComCnuReset,
       "h3cEOCComCnuDeregister": h3cEOCComCnuDeregister,
       "h3cEOCComCnuSave": h3cEOCComCnuSave,
       "h3cEOCComCnuAccess": h3cEOCComCnuAccess,
       "h3cEOCComCnuMacTable": h3cEOCComCnuMacTable,
       "h3cEOCComCnuMacEntry": h3cEOCComCnuMacEntry,
       "h3cEOCComCnuMacAddress": h3cEOCComCnuMacAddress,
       "h3cEOCComCnuRowStatus": h3cEOCComCnuRowStatus,
       "h3cEOCComCnuInfoTable": h3cEOCComCnuInfoTable,
       "h3cEOCComCnuInfoEntry": h3cEOCComCnuInfoEntry,
       "h3cEOCComCnuHardwareVersion": h3cEOCComCnuHardwareVersion,
       "h3cEOCComCnuPCBVersion": h3cEOCComCnuPCBVersion,
       "h3cEOCComCnuLinkState": h3cEOCComCnuLinkState,
       "h3cEOCComCnuAttenuation": h3cEOCComCnuAttenuation,
       "h3cEOCComCnuSoftwareVersion": h3cEOCComCnuSoftwareVersion,
       "h3cEOCComCnuTxRate": h3cEOCComCnuTxRate,
       "h3cEOCComCnuRxRate": h3cEOCComCnuRxRate,
       "h3cEOCComCnuTxRateDrop": h3cEOCComCnuTxRateDrop,
       "h3cEOCComCnuRxRateDrop": h3cEOCComCnuRxRateDrop,
       "h3cEOCComCnuBandWidthTable": h3cEOCComCnuBandWidthTable,
       "h3cEOCComCnuBandWidthEntry": h3cEOCComCnuBandWidthEntry,
       "h3cEOCComCnuMaxDownBW": h3cEOCComCnuMaxDownBW,
       "h3cEOCComCnuSlaHighPriBW": h3cEOCComCnuSlaHighPriBW,
       "h3cEOCComCnuMaxUpBW": h3cEOCComCnuMaxUpBW,
       "h3cEOCComUniMan": h3cEOCComUniMan,
       "h3cEOCComUniManTable": h3cEOCComUniManTable,
       "h3cEOCComUniManEntry": h3cEOCComUniManEntry,
       "h3cEOCUniIndex": h3cEOCUniIndex,
       "h3cEOCComUniDescr": h3cEOCComUniDescr,
       "h3cEOCComUniStatus": h3cEOCComUniStatus,
       "h3cEOCComUniSpeed": h3cEOCComUniSpeed,
       "h3cEOCComUniDuplex": h3cEOCComUniDuplex,
       "h3cEOCComUniCurrentSpeed": h3cEOCComUniCurrentSpeed,
       "h3cEOCComUniCurrentDuplex": h3cEOCComUniCurrentDuplex,
       "h3cEOCComUniMdi": h3cEOCComUniMdi,
       "h3cEOCComUniFlowControl": h3cEOCComUniFlowControl,
       "h3cEOCComUniCountReset": h3cEOCComUniCountReset,
       "h3cEOCComUniAlias": h3cEOCComUniAlias,
       "h3cEOCComUniType": h3cEOCComUniType,
       "h3cEOCComUniVLANType": h3cEOCComUniVLANType,
       "h3cEOCComUniPvid": h3cEOCComUniPvid,
       "h3cEOCComUniVlanTag": h3cEOCComUniVlanTag,
       "h3cEOCComUniPriority": h3cEOCComUniPriority,
       "h3cEOCComUniUpLineRate": h3cEOCComUniUpLineRate,
       "h3cEOCComUniDownLineRate": h3cEOCComUniDownLineRate,
       "h3cEOCComUniAdminStatus": h3cEOCComUniAdminStatus,
       "h3cEOCComUniCountTable": h3cEOCComUniCountTable,
       "h3cEOCComUniCountEntry": h3cEOCComUniCountEntry,
       "h3cEOCUniInPkts": h3cEOCUniInPkts,
       "h3cEOCUniInUPkts": h3cEOCUniInUPkts,
       "h3cEOCUniInBPkts": h3cEOCUniInBPkts,
       "h3cEOCUniInMPkts": h3cEOCUniInMPkts,
       "h3cEOCUniInPausePkts": h3cEOCUniInPausePkts,
       "h3cEOCUniInTotalErrors": h3cEOCUniInTotalErrors,
       "h3cEOCUniInCRCErrs": h3cEOCUniInCRCErrs,
       "h3cEOCUniInUndersizePkts": h3cEOCUniInUndersizePkts,
       "h3cEOCUniInOversizePkts": h3cEOCUniInOversizePkts,
       "h3cEOCUniInErrorbyOther": h3cEOCUniInErrorbyOther,
       "h3cEOCUniInOctets": h3cEOCUniInOctets,
       "h3cEOCUniOutPkts": h3cEOCUniOutPkts,
       "h3cEOCUniOutUPkts": h3cEOCUniOutUPkts,
       "h3cEOCUniOutBPkts": h3cEOCUniOutBPkts,
       "h3cEOCUniOutMPkts": h3cEOCUniOutMPkts,
       "h3cEOCUniOutPausePkts": h3cEOCUniOutPausePkts,
       "h3cEOCUniOutTotalErrors": h3cEOCUniOutTotalErrors,
       "h3cEOCUniOutCollisions": h3cEOCUniOutCollisions,
       "h3cEOCUniOutDelayExceedDsds": h3cEOCUniOutDelayExceedDsds,
       "h3cEOCUniOutErrorbyOther": h3cEOCUniOutErrorbyOther,
       "h3cEOCUniOutDroppedFrames": h3cEOCUniOutDroppedFrames,
       "h3cEOCUniOutOctets": h3cEOCUniOutOctets,
       "h3cEOCCommonTrap": h3cEOCCommonTrap,
       "h3cEOCTrapPrefix": h3cEOCTrapPrefix,
       "h3cEOCCnuRegExcessTrap": h3cEOCCnuRegExcessTrap,
       "h3cEOCCnuRegExcessRecoverTrap": h3cEOCCnuRegExcessRecoverTrap,
       "h3cEOCCnuRegSuccTrap": h3cEOCCnuRegSuccTrap,
       "h3cEOCCnuOffLineTrap": h3cEOCCnuOffLineTrap,
       "h3cEOCCnuLinkupTrap": h3cEOCCnuLinkupTrap,
       "h3cEOCOamDisconnectTrap": h3cEOCOamDisconnectTrap,
       "h3cEOCOamDisconnectRecoverTrap": h3cEOCOamDisconnectRecoverTrap,
       "h3cEOCBandwidthNotEnoughTrap": h3cEOCBandwidthNotEnoughTrap,
       "h3cEOCCnuAttenuationTrap": h3cEOCCnuAttenuationTrap,
       "h3cEOCCnuRegFailTrap": h3cEOCCnuRegFailTrap,
       "h3cEOCCLTCablePortErrorTrap": h3cEOCCLTCablePortErrorTrap,
       "h3cEOCCLTCablePortErrReTrap": h3cEOCCLTCablePortErrReTrap,
       "h3cEOCCnuTxRateDropTrap": h3cEOCCnuTxRateDropTrap,
       "h3cEOCCnuTxRateDropRecoverTrap": h3cEOCCnuTxRateDropRecoverTrap,
       "h3cEOCCnuRxRateDropTrap": h3cEOCCnuRxRateDropTrap,
       "h3cEOCCnuRxRateDropRecoverTrap": h3cEOCCnuRxRateDropRecoverTrap,
       "h3cEOCCnuFWDownLoadErrTrap": h3cEOCCnuFWDownLoadErrTrap,
       "h3cEOCCnuFWDownLoadErrReTrap": h3cEOCCnuFWDownLoadErrReTrap,
       "h3cEOCCnuDeviceTypeErrTrap": h3cEOCCnuDeviceTypeErrTrap,
       "h3cEOCCnuDeviceTypeErrReTrap": h3cEOCCnuDeviceTypeErrReTrap,
       "h3cEOCCnuAutoUpdateErrTrap": h3cEOCCnuAutoUpdateErrTrap,
       "h3cEOCCnuAutoUpdateSuccTrap": h3cEOCCnuAutoUpdateSuccTrap,
       "h3cEOCComOnLineCnuMan": h3cEOCComOnLineCnuMan,
       "h3cEOCComCnuTypeTable": h3cEOCComCnuTypeTable,
       "h3cEOCComCnuTypeEntry": h3cEOCComCnuTypeEntry,
       "h3cEOCComCnuTypeIdx": h3cEOCComCnuTypeIdx,
       "h3cEOCComCnuDescripton": h3cEOCComCnuDescripton,
       "h3cEOCComCnuNumTable": h3cEOCComCnuNumTable,
       "h3cEOCComCnuNumEntry": h3cEOCComCnuNumEntry,
       "h3cEOCComCnuNumber": h3cEOCComCnuNumber}
)
