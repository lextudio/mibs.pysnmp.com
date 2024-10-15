# SNMP MIB module (HPN-ICF-DOT11-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-RRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:54 2024
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

(HpnicfDot11ChannelScopeType,
 HpnicfDot11ObjectIDType,
 HpnicfDot11RadioElementIndex,
 HpnicfDot11RadioScopeType,
 HpnicfDot11RadioType,
 HpnicfDot11SSIDStringType,
 hpnicfDot11,
 hpnicfDot11APElementIndex) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11ChannelScopeType",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11RadioElementIndex",
    "HpnicfDot11RadioScopeType",
    "HpnicfDot11RadioType",
    "HpnicfDot11SSIDStringType",
    "hpnicfDot11",
    "hpnicfDot11APElementIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfDot11RRM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8)
)
hpnicfDot11RRM.setRevisions(
        ("2010-09-25 18:00",
         "2010-02-23 18:00",
         "2009-08-01 20:00",
         "2009-05-07 20:00",
         "2009-04-17 20:00",
         "2008-07-14 14:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11RRMConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMConfigGroup = _HpnicfDot11RRMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1)
)
_HpnicfDot11RRMGlobalCfgPara_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMGlobalCfgPara = _HpnicfDot11RRMGlobalCfgPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1)
)


class _HpnicfDot11RRM11nMadtMaxMcs_Type(Integer32):
    """Custom type hpnicfDot11RRM11nMadtMaxMcs based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
        ValueRangeConstraint(255, 255),
    )


_HpnicfDot11RRM11nMadtMaxMcs_Type.__name__ = "Integer32"
_HpnicfDot11RRM11nMadtMaxMcs_Object = MibScalar
hpnicfDot11RRM11nMadtMaxMcs = _HpnicfDot11RRM11nMadtMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 1),
    _HpnicfDot11RRM11nMadtMaxMcs_Type()
)
hpnicfDot11RRM11nMadtMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11nMadtMaxMcs.setStatus("current")


class _HpnicfDot11RRM11nSuptMaxMcs_Type(Integer32):
    """Custom type hpnicfDot11RRM11nSuptMaxMcs based on Integer32"""
    defaultValue = 76

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_HpnicfDot11RRM11nSuptMaxMcs_Type.__name__ = "Integer32"
_HpnicfDot11RRM11nSuptMaxMcs_Object = MibScalar
hpnicfDot11RRM11nSuptMaxMcs = _HpnicfDot11RRM11nSuptMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 2),
    _HpnicfDot11RRM11nSuptMaxMcs_Type()
)
hpnicfDot11RRM11nSuptMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11nSuptMaxMcs.setStatus("current")


class _HpnicfDot11RRM11gProtect_Type(TruthValue):
    """Custom type hpnicfDot11RRM11gProtect based on TruthValue"""


_HpnicfDot11RRM11gProtect_Object = MibScalar
hpnicfDot11RRM11gProtect = _HpnicfDot11RRM11gProtect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 3),
    _HpnicfDot11RRM11gProtect_Type()
)
hpnicfDot11RRM11gProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11gProtect.setStatus("current")


class _HpnicfDot11RRM11aPwrConstrt_Type(Integer32):
    """Custom type hpnicfDot11RRM11aPwrConstrt based on Integer32"""
    defaultValue = 0


_HpnicfDot11RRM11aPwrConstrt_Object = MibScalar
hpnicfDot11RRM11aPwrConstrt = _HpnicfDot11RRM11aPwrConstrt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 4),
    _HpnicfDot11RRM11aPwrConstrt_Type()
)
hpnicfDot11RRM11aPwrConstrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11aPwrConstrt.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11aPwrConstrt.setUnits("dBm")


class _HpnicfDot11RRM11aSpectrumManag_Type(TruthValue):
    """Custom type hpnicfDot11RRM11aSpectrumManag based on TruthValue"""


_HpnicfDot11RRM11aSpectrumManag_Object = MibScalar
hpnicfDot11RRM11aSpectrumManag = _HpnicfDot11RRM11aSpectrumManag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 5),
    _HpnicfDot11RRM11aSpectrumManag_Type()
)
hpnicfDot11RRM11aSpectrumManag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11aSpectrumManag.setStatus("current")


class _HpnicfDot11RRMAutoChlAvoid11h_Type(TruthValue):
    """Custom type hpnicfDot11RRMAutoChlAvoid11h based on TruthValue"""


_HpnicfDot11RRMAutoChlAvoid11h_Object = MibScalar
hpnicfDot11RRMAutoChlAvoid11h = _HpnicfDot11RRMAutoChlAvoid11h_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 6),
    _HpnicfDot11RRMAutoChlAvoid11h_Type()
)
hpnicfDot11RRMAutoChlAvoid11h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMAutoChlAvoid11h.setStatus("current")


class _HpnicfDot11RRMScanChl_Type(Integer32):
    """Custom type hpnicfDot11RRMScanChl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("auto", 1))
    )


_HpnicfDot11RRMScanChl_Type.__name__ = "Integer32"
_HpnicfDot11RRMScanChl_Object = MibScalar
hpnicfDot11RRMScanChl = _HpnicfDot11RRMScanChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 7),
    _HpnicfDot11RRMScanChl_Type()
)
hpnicfDot11RRMScanChl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMScanChl.setStatus("current")


class _HpnicfDot11RRMScanRptIntvel_Type(Integer32):
    """Custom type hpnicfDot11RRMScanRptIntvel based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_HpnicfDot11RRMScanRptIntvel_Type.__name__ = "Integer32"
_HpnicfDot11RRMScanRptIntvel_Object = MibScalar
hpnicfDot11RRMScanRptIntvel = _HpnicfDot11RRMScanRptIntvel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 8),
    _HpnicfDot11RRMScanRptIntvel_Type()
)
hpnicfDot11RRMScanRptIntvel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMScanRptIntvel.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMScanRptIntvel.setUnits("second")


class _HpnicfDot11APInterfNumThreshhd_Type(Integer32):
    """Custom type hpnicfDot11APInterfNumThreshhd based on Integer32"""
    defaultValue = 0


_HpnicfDot11APInterfNumThreshhd_Object = MibScalar
hpnicfDot11APInterfNumThreshhd = _HpnicfDot11APInterfNumThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 9),
    _HpnicfDot11APInterfNumThreshhd_Type()
)
hpnicfDot11APInterfNumThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APInterfNumThreshhd.setStatus("current")


class _HpnicfDot11StaInterfNumThreshhd_Type(Integer32):
    """Custom type hpnicfDot11StaInterfNumThreshhd based on Integer32"""
    defaultValue = 0


_HpnicfDot11StaInterfNumThreshhd_Object = MibScalar
hpnicfDot11StaInterfNumThreshhd = _HpnicfDot11StaInterfNumThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 10),
    _HpnicfDot11StaInterfNumThreshhd_Type()
)
hpnicfDot11StaInterfNumThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StaInterfNumThreshhd.setStatus("current")


class _HpnicfDot11RRM11nMultiCastMcs_Type(Unsigned32):
    """Custom type hpnicfDot11RRM11nMultiCastMcs based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_HpnicfDot11RRM11nMultiCastMcs_Type.__name__ = "Unsigned32"
_HpnicfDot11RRM11nMultiCastMcs_Object = MibScalar
hpnicfDot11RRM11nMultiCastMcs = _HpnicfDot11RRM11nMultiCastMcs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 11),
    _HpnicfDot11RRM11nMultiCastMcs_Type()
)
hpnicfDot11RRM11nMultiCastMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11nMultiCastMcs.setStatus("current")


class _HpnicfDot11RRM11acMadtMaxNss_Type(Integer32):
    """Custom type hpnicfDot11RRM11acMadtMaxNss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HpnicfDot11RRM11acMadtMaxNss_Type.__name__ = "Integer32"
_HpnicfDot11RRM11acMadtMaxNss_Object = MibScalar
hpnicfDot11RRM11acMadtMaxNss = _HpnicfDot11RRM11acMadtMaxNss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 12),
    _HpnicfDot11RRM11acMadtMaxNss_Type()
)
hpnicfDot11RRM11acMadtMaxNss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11acMadtMaxNss.setStatus("current")


class _HpnicfDot11RRM11acSuptMaxNss_Type(Integer32):
    """Custom type hpnicfDot11RRM11acSuptMaxNss based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpnicfDot11RRM11acSuptMaxNss_Type.__name__ = "Integer32"
_HpnicfDot11RRM11acSuptMaxNss_Object = MibScalar
hpnicfDot11RRM11acSuptMaxNss = _HpnicfDot11RRM11acSuptMaxNss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 13),
    _HpnicfDot11RRM11acSuptMaxNss_Type()
)
hpnicfDot11RRM11acSuptMaxNss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11acSuptMaxNss.setStatus("current")


class _HpnicfDot11RRM11acMultiCastNss_Type(Integer32):
    """Custom type hpnicfDot11RRM11acMultiCastNss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HpnicfDot11RRM11acMultiCastNss_Type.__name__ = "Integer32"
_HpnicfDot11RRM11acMultiCastNss_Object = MibScalar
hpnicfDot11RRM11acMultiCastNss = _HpnicfDot11RRM11acMultiCastNss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 14),
    _HpnicfDot11RRM11acMultiCastNss_Type()
)
hpnicfDot11RRM11acMultiCastNss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11acMultiCastNss.setStatus("current")


class _HpnicfDot11RRM11acMultiCastVhtMcs_Type(Integer32):
    """Custom type hpnicfDot11RRM11acMultiCastVhtMcs based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
        ValueRangeConstraint(255, 255),
    )


_HpnicfDot11RRM11acMultiCastVhtMcs_Type.__name__ = "Integer32"
_HpnicfDot11RRM11acMultiCastVhtMcs_Object = MibScalar
hpnicfDot11RRM11acMultiCastVhtMcs = _HpnicfDot11RRM11acMultiCastVhtMcs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 1, 15),
    _HpnicfDot11RRM11acMultiCastVhtMcs_Type()
)
hpnicfDot11RRM11acMultiCastVhtMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRM11acMultiCastVhtMcs.setStatus("current")
_HpnicfDot11RRMRadioCfgTable_Object = MibTable
hpnicfDot11RRMRadioCfgTable = _HpnicfDot11RRMRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioCfgTable.setStatus("current")
_HpnicfDot11RRMRadioCfgEntry_Object = MibTableRow
hpnicfDot11RRMRadioCfgEntry = _HpnicfDot11RRMRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1)
)
hpnicfDot11RRMRadioCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMRadioType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioCfgEntry.setStatus("current")
_HpnicfDot11RRMRadioType_Type = HpnicfDot11RadioType
_HpnicfDot11RRMRadioType_Object = MibTableColumn
hpnicfDot11RRMRadioType = _HpnicfDot11RRMRadioType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 1),
    _HpnicfDot11RRMRadioType_Type()
)
hpnicfDot11RRMRadioType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioType.setStatus("current")


class _HpnicfDot11RRMCfgChlState_Type(TruthValue):
    """Custom type hpnicfDot11RRMCfgChlState based on TruthValue"""


_HpnicfDot11RRMCfgChlState_Object = MibTableColumn
hpnicfDot11RRMCfgChlState = _HpnicfDot11RRMCfgChlState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 2),
    _HpnicfDot11RRMCfgChlState_Type()
)
hpnicfDot11RRMCfgChlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgChlState.setStatus("current")


class _HpnicfDot11RRMCfgChlMode_Type(Integer32):
    """Custom type hpnicfDot11RRMCfgChlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("selfDecisive", 1),
          ("userTriggered", 2))
    )


_HpnicfDot11RRMCfgChlMode_Type.__name__ = "Integer32"
_HpnicfDot11RRMCfgChlMode_Object = MibTableColumn
hpnicfDot11RRMCfgChlMode = _HpnicfDot11RRMCfgChlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 3),
    _HpnicfDot11RRMCfgChlMode_Type()
)
hpnicfDot11RRMCfgChlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgChlMode.setStatus("current")


class _HpnicfDot11RRMChlProntoRadioElmt_Type(Unsigned32):
    """Custom type hpnicfDot11RRMChlProntoRadioElmt based on Unsigned32"""
    defaultValue = 0


_HpnicfDot11RRMChlProntoRadioElmt_Object = MibTableColumn
hpnicfDot11RRMChlProntoRadioElmt = _HpnicfDot11RRMChlProntoRadioElmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 4),
    _HpnicfDot11RRMChlProntoRadioElmt_Type()
)
hpnicfDot11RRMChlProntoRadioElmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlProntoRadioElmt.setStatus("current")


class _HpnicfDot11RRMCfgPwrState_Type(TruthValue):
    """Custom type hpnicfDot11RRMCfgPwrState based on TruthValue"""


_HpnicfDot11RRMCfgPwrState_Object = MibTableColumn
hpnicfDot11RRMCfgPwrState = _HpnicfDot11RRMCfgPwrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 5),
    _HpnicfDot11RRMCfgPwrState_Type()
)
hpnicfDot11RRMCfgPwrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgPwrState.setStatus("current")


class _HpnicfDot11RRMCfgPwrMode_Type(Integer32):
    """Custom type hpnicfDot11RRMCfgPwrMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("selfDecisive", 1),
          ("userTriggered", 2))
    )


_HpnicfDot11RRMCfgPwrMode_Type.__name__ = "Integer32"
_HpnicfDot11RRMCfgPwrMode_Object = MibTableColumn
hpnicfDot11RRMCfgPwrMode = _HpnicfDot11RRMCfgPwrMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 6),
    _HpnicfDot11RRMCfgPwrMode_Type()
)
hpnicfDot11RRMCfgPwrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgPwrMode.setStatus("current")


class _HpnicfDot11RRMPwrProntoRadioElmt_Type(Unsigned32):
    """Custom type hpnicfDot11RRMPwrProntoRadioElmt based on Unsigned32"""
    defaultValue = 0


_HpnicfDot11RRMPwrProntoRadioElmt_Object = MibTableColumn
hpnicfDot11RRMPwrProntoRadioElmt = _HpnicfDot11RRMPwrProntoRadioElmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 7),
    _HpnicfDot11RRMPwrProntoRadioElmt_Type()
)
hpnicfDot11RRMPwrProntoRadioElmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMPwrProntoRadioElmt.setStatus("current")


class _HpnicfDot11RRMCfgIntrvl_Type(Integer32):
    """Custom type hpnicfDot11RRMCfgIntrvl based on Integer32"""
    defaultValue = 8


_HpnicfDot11RRMCfgIntrvl_Object = MibTableColumn
hpnicfDot11RRMCfgIntrvl = _HpnicfDot11RRMCfgIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 8),
    _HpnicfDot11RRMCfgIntrvl_Type()
)
hpnicfDot11RRMCfgIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgIntrvl.setUnits("minute")


class _HpnicfDot11RRMCfgIntrfThres_Type(Integer32):
    """Custom type hpnicfDot11RRMCfgIntrfThres based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_HpnicfDot11RRMCfgIntrfThres_Type.__name__ = "Integer32"
_HpnicfDot11RRMCfgIntrfThres_Object = MibTableColumn
hpnicfDot11RRMCfgIntrfThres = _HpnicfDot11RRMCfgIntrfThres_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 9),
    _HpnicfDot11RRMCfgIntrfThres_Type()
)
hpnicfDot11RRMCfgIntrfThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgIntrfThres.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgIntrfThres.setUnits("percent")


class _HpnicfDot11RRMCfgNoiseThres_Type(Integer32):
    """Custom type hpnicfDot11RRMCfgNoiseThres based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_HpnicfDot11RRMCfgNoiseThres_Type.__name__ = "Integer32"
_HpnicfDot11RRMCfgNoiseThres_Object = MibTableColumn
hpnicfDot11RRMCfgNoiseThres = _HpnicfDot11RRMCfgNoiseThres_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 10),
    _HpnicfDot11RRMCfgNoiseThres_Type()
)
hpnicfDot11RRMCfgNoiseThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgNoiseThres.setStatus("current")


class _HpnicfDot11RRMCfgPERThres_Type(Integer32):
    """Custom type hpnicfDot11RRMCfgPERThres based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfDot11RRMCfgPERThres_Type.__name__ = "Integer32"
_HpnicfDot11RRMCfgPERThres_Object = MibTableColumn
hpnicfDot11RRMCfgPERThres = _HpnicfDot11RRMCfgPERThres_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 11),
    _HpnicfDot11RRMCfgPERThres_Type()
)
hpnicfDot11RRMCfgPERThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgPERThres.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgPERThres.setUnits("percent")


class _HpnicfDot11RRMCfgToleranceFctr_Type(Integer32):
    """Custom type hpnicfDot11RRMCfgToleranceFctr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45),
    )


_HpnicfDot11RRMCfgToleranceFctr_Type.__name__ = "Integer32"
_HpnicfDot11RRMCfgToleranceFctr_Object = MibTableColumn
hpnicfDot11RRMCfgToleranceFctr = _HpnicfDot11RRMCfgToleranceFctr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 12),
    _HpnicfDot11RRMCfgToleranceFctr_Type()
)
hpnicfDot11RRMCfgToleranceFctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgToleranceFctr.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgToleranceFctr.setUnits("percent")


class _HpnicfDot11RRMCfgAdjacencyFctr_Type(Integer32):
    """Custom type hpnicfDot11RRMCfgAdjacencyFctr based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfDot11RRMCfgAdjacencyFctr_Type.__name__ = "Integer32"
_HpnicfDot11RRMCfgAdjacencyFctr_Object = MibTableColumn
hpnicfDot11RRMCfgAdjacencyFctr = _HpnicfDot11RRMCfgAdjacencyFctr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 2, 1, 13),
    _HpnicfDot11RRMCfgAdjacencyFctr_Type()
)
hpnicfDot11RRMCfgAdjacencyFctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCfgAdjacencyFctr.setStatus("current")
_HpnicfDot11RRMAPCfgTable_Object = MibTable
hpnicfDot11RRMAPCfgTable = _HpnicfDot11RRMAPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMAPCfgTable.setStatus("current")
_HpnicfDot11RRMAPCfgEntry_Object = MibTableRow
hpnicfDot11RRMAPCfgEntry = _HpnicfDot11RRMAPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 3, 1)
)
hpnicfDot11RRMAPCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMAPCfgEntry.setStatus("current")


class _HpnicfDot11RRMAPWorkMode_Type(Integer32):
    """Custom type hpnicfDot11RRMAPWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 3),
          ("monitor", 2),
          ("normal", 1))
    )


_HpnicfDot11RRMAPWorkMode_Type.__name__ = "Integer32"
_HpnicfDot11RRMAPWorkMode_Object = MibTableColumn
hpnicfDot11RRMAPWorkMode = _HpnicfDot11RRMAPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 3, 1, 1),
    _HpnicfDot11RRMAPWorkMode_Type()
)
hpnicfDot11RRMAPWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMAPWorkMode.setStatus("current")
_HpnicfDot11RRMSDRadioGroupTable_Object = MibTable
hpnicfDot11RRMSDRadioGroupTable = _HpnicfDot11RRMSDRadioGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRadioGroupTable.setStatus("current")
_HpnicfDot11RRMSDRadioGroupEntry_Object = MibTableRow
hpnicfDot11RRMSDRadioGroupEntry = _HpnicfDot11RRMSDRadioGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 4, 1)
)
hpnicfDot11RRMSDRadioGroupEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMSDRadioGroupId"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRadioGroupEntry.setStatus("current")
_HpnicfDot11RRMSDRadioGroupId_Type = Unsigned32
_HpnicfDot11RRMSDRadioGroupId_Object = MibTableColumn
hpnicfDot11RRMSDRadioGroupId = _HpnicfDot11RRMSDRadioGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 4, 1, 1),
    _HpnicfDot11RRMSDRadioGroupId_Type()
)
hpnicfDot11RRMSDRadioGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRadioGroupId.setStatus("current")
_HpnicfDot11RRMSDRadioGroupDesc_Type = OctetString
_HpnicfDot11RRMSDRadioGroupDesc_Object = MibTableColumn
hpnicfDot11RRMSDRadioGroupDesc = _HpnicfDot11RRMSDRadioGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 4, 1, 2),
    _HpnicfDot11RRMSDRadioGroupDesc_Type()
)
hpnicfDot11RRMSDRadioGroupDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRadioGroupDesc.setStatus("current")
_HpnicfDot11RRMSDRdGrpChlHolddownTm_Type = Unsigned32
_HpnicfDot11RRMSDRdGrpChlHolddownTm_Object = MibTableColumn
hpnicfDot11RRMSDRdGrpChlHolddownTm = _HpnicfDot11RRMSDRdGrpChlHolddownTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 4, 1, 3),
    _HpnicfDot11RRMSDRdGrpChlHolddownTm_Type()
)
hpnicfDot11RRMSDRdGrpChlHolddownTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRdGrpChlHolddownTm.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRdGrpChlHolddownTm.setUnits("minute")
_HpnicfDot11RRMSDRdGrpPwrHolddownTm_Type = Unsigned32
_HpnicfDot11RRMSDRdGrpPwrHolddownTm_Object = MibTableColumn
hpnicfDot11RRMSDRdGrpPwrHolddownTm = _HpnicfDot11RRMSDRdGrpPwrHolddownTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 4, 1, 4),
    _HpnicfDot11RRMSDRdGrpPwrHolddownTm_Type()
)
hpnicfDot11RRMSDRdGrpPwrHolddownTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRdGrpPwrHolddownTm.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRdGrpPwrHolddownTm.setUnits("minute")
_HpnicfDot11RRMSDRdGroupRowStatus_Type = RowStatus
_HpnicfDot11RRMSDRdGroupRowStatus_Object = MibTableColumn
hpnicfDot11RRMSDRdGroupRowStatus = _HpnicfDot11RRMSDRdGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 4, 1, 5),
    _HpnicfDot11RRMSDRdGroupRowStatus_Type()
)
hpnicfDot11RRMSDRdGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RRMSDRdGroupRowStatus.setStatus("current")
_HpnicfDot11RRMAPCfg2Table_Object = MibTable
hpnicfDot11RRMAPCfg2Table = _HpnicfDot11RRMAPCfg2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMAPCfg2Table.setStatus("current")
_HpnicfDot11RRMAPCfg2Entry_Object = MibTableRow
hpnicfDot11RRMAPCfg2Entry = _HpnicfDot11RRMAPCfg2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 5, 1)
)
hpnicfDot11RRMAPCfg2Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMAPSerialID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMAPCfg2Entry.setStatus("current")
_HpnicfDot11RRMAPSerialID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11RRMAPSerialID_Object = MibTableColumn
hpnicfDot11RRMAPSerialID = _HpnicfDot11RRMAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 5, 1, 1),
    _HpnicfDot11RRMAPSerialID_Type()
)
hpnicfDot11RRMAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RRMAPSerialID.setStatus("current")
_HpnicfDot11RRMAPIntfThreshold_Type = Integer32
_HpnicfDot11RRMAPIntfThreshold_Object = MibTableColumn
hpnicfDot11RRMAPIntfThreshold = _HpnicfDot11RRMAPIntfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 5, 1, 2),
    _HpnicfDot11RRMAPIntfThreshold_Type()
)
hpnicfDot11RRMAPIntfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMAPIntfThreshold.setStatus("current")
_HpnicfDot11RRMStaIntfThreshold_Type = Integer32
_HpnicfDot11RRMStaIntfThreshold_Object = MibTableColumn
hpnicfDot11RRMStaIntfThreshold = _HpnicfDot11RRMStaIntfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 5, 1, 3),
    _HpnicfDot11RRMStaIntfThreshold_Type()
)
hpnicfDot11RRMStaIntfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMStaIntfThreshold.setStatus("current")
_HpnicfDot11RRMCoChlIntfTrapThhd_Type = Integer32
_HpnicfDot11RRMCoChlIntfTrapThhd_Object = MibTableColumn
hpnicfDot11RRMCoChlIntfTrapThhd = _HpnicfDot11RRMCoChlIntfTrapThhd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 5, 1, 4),
    _HpnicfDot11RRMCoChlIntfTrapThhd_Type()
)
hpnicfDot11RRMCoChlIntfTrapThhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCoChlIntfTrapThhd.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMCoChlIntfTrapThhd.setUnits("dbm")
_HpnicfDot11RRMAdjChlIntfTrapThhd_Type = Integer32
_HpnicfDot11RRMAdjChlIntfTrapThhd_Object = MibTableColumn
hpnicfDot11RRMAdjChlIntfTrapThhd = _HpnicfDot11RRMAdjChlIntfTrapThhd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 1, 5, 1, 5),
    _HpnicfDot11RRMAdjChlIntfTrapThhd_Type()
)
hpnicfDot11RRMAdjChlIntfTrapThhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMAdjChlIntfTrapThhd.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMAdjChlIntfTrapThhd.setUnits("dbm")
_HpnicfDot11RRMDetectGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMDetectGroup = _HpnicfDot11RRMDetectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2)
)
_HpnicfDot11RRMChlRptTable_Object = MibTable
hpnicfDot11RRMChlRptTable = _HpnicfDot11RRMChlRptTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptTable.setStatus("current")
_HpnicfDot11RRMChlRptEntry_Object = MibTableRow
hpnicfDot11RRMChlRptEntry = _HpnicfDot11RRMChlRptEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1)
)
hpnicfDot11RRMChlRptEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMRadioIndex"),
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMChlRptChlNum"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptEntry.setStatus("current")
_HpnicfDot11RRMRadioIndex_Type = HpnicfDot11RadioElementIndex
_HpnicfDot11RRMRadioIndex_Object = MibTableColumn
hpnicfDot11RRMRadioIndex = _HpnicfDot11RRMRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 1),
    _HpnicfDot11RRMRadioIndex_Type()
)
hpnicfDot11RRMRadioIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioIndex.setStatus("current")
_HpnicfDot11RRMChlRptChlNum_Type = Integer32
_HpnicfDot11RRMChlRptChlNum_Object = MibTableColumn
hpnicfDot11RRMChlRptChlNum = _HpnicfDot11RRMChlRptChlNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 2),
    _HpnicfDot11RRMChlRptChlNum_Type()
)
hpnicfDot11RRMChlRptChlNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptChlNum.setStatus("current")


class _HpnicfDot11RRMChlRptChlType_Type(Integer32):
    """Custom type hpnicfDot11RRMChlRptChlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offChannel", 2),
          ("primeChannel", 1))
    )


_HpnicfDot11RRMChlRptChlType_Type.__name__ = "Integer32"
_HpnicfDot11RRMChlRptChlType_Object = MibTableColumn
hpnicfDot11RRMChlRptChlType = _HpnicfDot11RRMChlRptChlType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 3),
    _HpnicfDot11RRMChlRptChlType_Type()
)
hpnicfDot11RRMChlRptChlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptChlType.setStatus("current")


class _HpnicfDot11RRMChlRptChlQlty_Type(Integer32):
    """Custom type hpnicfDot11RRMChlRptChlQlty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_HpnicfDot11RRMChlRptChlQlty_Type.__name__ = "Integer32"
_HpnicfDot11RRMChlRptChlQlty_Object = MibTableColumn
hpnicfDot11RRMChlRptChlQlty = _HpnicfDot11RRMChlRptChlQlty_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 4),
    _HpnicfDot11RRMChlRptChlQlty_Type()
)
hpnicfDot11RRMChlRptChlQlty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptChlQlty.setStatus("current")
_HpnicfDot11RRMChlRptNbrCnt_Type = Integer32
_HpnicfDot11RRMChlRptNbrCnt_Object = MibTableColumn
hpnicfDot11RRMChlRptNbrCnt = _HpnicfDot11RRMChlRptNbrCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 5),
    _HpnicfDot11RRMChlRptNbrCnt_Type()
)
hpnicfDot11RRMChlRptNbrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptNbrCnt.setStatus("current")


class _HpnicfDot11RRMChlRptLoad_Type(Integer32):
    """Custom type hpnicfDot11RRMChlRptLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMChlRptLoad_Type.__name__ = "Integer32"
_HpnicfDot11RRMChlRptLoad_Object = MibTableColumn
hpnicfDot11RRMChlRptLoad = _HpnicfDot11RRMChlRptLoad_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 6),
    _HpnicfDot11RRMChlRptLoad_Type()
)
hpnicfDot11RRMChlRptLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptLoad.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptLoad.setUnits("percent")


class _HpnicfDot11RRMChlRptUtlz_Type(Integer32):
    """Custom type hpnicfDot11RRMChlRptUtlz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMChlRptUtlz_Type.__name__ = "Integer32"
_HpnicfDot11RRMChlRptUtlz_Object = MibTableColumn
hpnicfDot11RRMChlRptUtlz = _HpnicfDot11RRMChlRptUtlz_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 7),
    _HpnicfDot11RRMChlRptUtlz_Type()
)
hpnicfDot11RRMChlRptUtlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptUtlz.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptUtlz.setUnits("percent")


class _HpnicfDot11RRMChlRptIntrf_Type(Integer32):
    """Custom type hpnicfDot11RRMChlRptIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMChlRptIntrf_Type.__name__ = "Integer32"
_HpnicfDot11RRMChlRptIntrf_Object = MibTableColumn
hpnicfDot11RRMChlRptIntrf = _HpnicfDot11RRMChlRptIntrf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 8),
    _HpnicfDot11RRMChlRptIntrf_Type()
)
hpnicfDot11RRMChlRptIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptIntrf.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptIntrf.setUnits("percent")


class _HpnicfDot11RRMChlRptPER_Type(Integer32):
    """Custom type hpnicfDot11RRMChlRptPER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMChlRptPER_Type.__name__ = "Integer32"
_HpnicfDot11RRMChlRptPER_Object = MibTableColumn
hpnicfDot11RRMChlRptPER = _HpnicfDot11RRMChlRptPER_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 9),
    _HpnicfDot11RRMChlRptPER_Type()
)
hpnicfDot11RRMChlRptPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptPER.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptPER.setUnits("percent")


class _HpnicfDot11RRMChlRptRetryRate_Type(Integer32):
    """Custom type hpnicfDot11RRMChlRptRetryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMChlRptRetryRate_Type.__name__ = "Integer32"
_HpnicfDot11RRMChlRptRetryRate_Object = MibTableColumn
hpnicfDot11RRMChlRptRetryRate = _HpnicfDot11RRMChlRptRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 10),
    _HpnicfDot11RRMChlRptRetryRate_Type()
)
hpnicfDot11RRMChlRptRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptRetryRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptRetryRate.setUnits("percent")
_HpnicfDot11RRMChlRptNoise_Type = Integer32
_HpnicfDot11RRMChlRptNoise_Object = MibTableColumn
hpnicfDot11RRMChlRptNoise = _HpnicfDot11RRMChlRptNoise_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 11),
    _HpnicfDot11RRMChlRptNoise_Type()
)
hpnicfDot11RRMChlRptNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptNoise.setStatus("current")


class _HpnicfDot11RRMChlRptRadarIndtcr_Type(Integer32):
    """Custom type hpnicfDot11RRMChlRptRadarIndtcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notDetected", 2))
    )


_HpnicfDot11RRMChlRptRadarIndtcr_Type.__name__ = "Integer32"
_HpnicfDot11RRMChlRptRadarIndtcr_Object = MibTableColumn
hpnicfDot11RRMChlRptRadarIndtcr = _HpnicfDot11RRMChlRptRadarIndtcr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 1, 1, 12),
    _HpnicfDot11RRMChlRptRadarIndtcr_Type()
)
hpnicfDot11RRMChlRptRadarIndtcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RRMChlRptRadarIndtcr.setStatus("current")
_HpnicfDot11RRMNbrInfoTable_Object = MibTable
hpnicfDot11RRMNbrInfoTable = _HpnicfDot11RRMNbrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMNbrInfoTable.setStatus("current")
_HpnicfDot11RRMNbrInfoEntry_Object = MibTableRow
hpnicfDot11RRMNbrInfoEntry = _HpnicfDot11RRMNbrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 2, 1)
)
hpnicfDot11RRMNbrInfoEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMRadioIndex"),
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RrmNbrBSSID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMNbrInfoEntry.setStatus("current")
_HpnicfDot11RrmNbrBSSID_Type = MacAddress
_HpnicfDot11RrmNbrBSSID_Object = MibTableColumn
hpnicfDot11RrmNbrBSSID = _HpnicfDot11RrmNbrBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 2, 1, 1),
    _HpnicfDot11RrmNbrBSSID_Type()
)
hpnicfDot11RrmNbrBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RrmNbrBSSID.setStatus("current")
_HpnicfDot11RrmNbrChl_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11RrmNbrChl_Object = MibTableColumn
hpnicfDot11RrmNbrChl = _HpnicfDot11RrmNbrChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 2, 1, 2),
    _HpnicfDot11RrmNbrChl_Type()
)
hpnicfDot11RrmNbrChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RrmNbrChl.setStatus("current")


class _HpnicfDot11RRMNbrIntrf_Type(Integer32):
    """Custom type hpnicfDot11RRMNbrIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMNbrIntrf_Type.__name__ = "Integer32"
_HpnicfDot11RRMNbrIntrf_Object = MibTableColumn
hpnicfDot11RRMNbrIntrf = _HpnicfDot11RRMNbrIntrf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 2, 1, 3),
    _HpnicfDot11RRMNbrIntrf_Type()
)
hpnicfDot11RRMNbrIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMNbrIntrf.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMNbrIntrf.setUnits("percent")
_HpnicfDot11RrmNbrRSSI_Type = Integer32
_HpnicfDot11RrmNbrRSSI_Object = MibTableColumn
hpnicfDot11RrmNbrRSSI = _HpnicfDot11RrmNbrRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 2, 1, 4),
    _HpnicfDot11RrmNbrRSSI_Type()
)
hpnicfDot11RrmNbrRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RrmNbrRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RrmNbrRSSI.setUnits("dBm")


class _HpnicfDot11RrmNbrType_Type(Integer32):
    """Custom type hpnicfDot11RrmNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("managed", 1),
          ("unmanaged", 2))
    )


_HpnicfDot11RrmNbrType_Type.__name__ = "Integer32"
_HpnicfDot11RrmNbrType_Object = MibTableColumn
hpnicfDot11RrmNbrType = _HpnicfDot11RrmNbrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 2, 1, 5),
    _HpnicfDot11RrmNbrType_Type()
)
hpnicfDot11RrmNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RrmNbrType.setStatus("current")
_HpnicfDot11RrmNbrSSID_Type = HpnicfDot11SSIDStringType
_HpnicfDot11RrmNbrSSID_Object = MibTableColumn
hpnicfDot11RrmNbrSSID = _HpnicfDot11RrmNbrSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 2, 1, 6),
    _HpnicfDot11RrmNbrSSID_Type()
)
hpnicfDot11RrmNbrSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RrmNbrSSID.setStatus("current")
_HpnicfDot11RRMHistoryTable_Object = MibTable
hpnicfDot11RRMHistoryTable = _HpnicfDot11RRMHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryTable.setStatus("current")
_HpnicfDot11RRMHistoryEntry_Object = MibTableRow
hpnicfDot11RRMHistoryEntry = _HpnicfDot11RRMHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1)
)
hpnicfDot11RRMHistoryEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMRadioIndex"),
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMHistoryId"),
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMHistoryRecIndctr"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryEntry.setStatus("current")
_HpnicfDot11RRMHistoryId_Type = Integer32
_HpnicfDot11RRMHistoryId_Object = MibTableColumn
hpnicfDot11RRMHistoryId = _HpnicfDot11RRMHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 1),
    _HpnicfDot11RRMHistoryId_Type()
)
hpnicfDot11RRMHistoryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryId.setStatus("current")


class _HpnicfDot11RRMHistoryRecIndctr_Type(Integer32):
    """Custom type hpnicfDot11RRMHistoryRecIndctr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("after", 2),
          ("before", 1))
    )


_HpnicfDot11RRMHistoryRecIndctr_Type.__name__ = "Integer32"
_HpnicfDot11RRMHistoryRecIndctr_Object = MibTableColumn
hpnicfDot11RRMHistoryRecIndctr = _HpnicfDot11RRMHistoryRecIndctr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 2),
    _HpnicfDot11RRMHistoryRecIndctr_Type()
)
hpnicfDot11RRMHistoryRecIndctr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryRecIndctr.setStatus("current")
_HpnicfDot11RRMHistoryChl_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11RRMHistoryChl_Object = MibTableColumn
hpnicfDot11RRMHistoryChl = _HpnicfDot11RRMHistoryChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 3),
    _HpnicfDot11RRMHistoryChl_Type()
)
hpnicfDot11RRMHistoryChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryChl.setStatus("current")
_HpnicfDot11RRMHistoryPwr_Type = Integer32
_HpnicfDot11RRMHistoryPwr_Object = MibTableColumn
hpnicfDot11RRMHistoryPwr = _HpnicfDot11RRMHistoryPwr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 4),
    _HpnicfDot11RRMHistoryPwr_Type()
)
hpnicfDot11RRMHistoryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryPwr.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryPwr.setUnits("dBm")


class _HpnicfDot11RRMHistoryLoad_Type(Integer32):
    """Custom type hpnicfDot11RRMHistoryLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMHistoryLoad_Type.__name__ = "Integer32"
_HpnicfDot11RRMHistoryLoad_Object = MibTableColumn
hpnicfDot11RRMHistoryLoad = _HpnicfDot11RRMHistoryLoad_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 5),
    _HpnicfDot11RRMHistoryLoad_Type()
)
hpnicfDot11RRMHistoryLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryLoad.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryLoad.setUnits("percent")


class _HpnicfDot11RRMHistoryUtlz_Type(Integer32):
    """Custom type hpnicfDot11RRMHistoryUtlz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMHistoryUtlz_Type.__name__ = "Integer32"
_HpnicfDot11RRMHistoryUtlz_Object = MibTableColumn
hpnicfDot11RRMHistoryUtlz = _HpnicfDot11RRMHistoryUtlz_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 6),
    _HpnicfDot11RRMHistoryUtlz_Type()
)
hpnicfDot11RRMHistoryUtlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryUtlz.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryUtlz.setUnits("percent")


class _HpnicfDot11RRMHistoryIntrf_Type(Integer32):
    """Custom type hpnicfDot11RRMHistoryIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMHistoryIntrf_Type.__name__ = "Integer32"
_HpnicfDot11RRMHistoryIntrf_Object = MibTableColumn
hpnicfDot11RRMHistoryIntrf = _HpnicfDot11RRMHistoryIntrf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 7),
    _HpnicfDot11RRMHistoryIntrf_Type()
)
hpnicfDot11RRMHistoryIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryIntrf.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryIntrf.setUnits("percent")
_HpnicfDot11RRMHistoryNoise_Type = Integer32
_HpnicfDot11RRMHistoryNoise_Object = MibTableColumn
hpnicfDot11RRMHistoryNoise = _HpnicfDot11RRMHistoryNoise_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 8),
    _HpnicfDot11RRMHistoryNoise_Type()
)
hpnicfDot11RRMHistoryNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryNoise.setStatus("current")


class _HpnicfDot11RRMHistoryPER_Type(Integer32):
    """Custom type hpnicfDot11RRMHistoryPER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMHistoryPER_Type.__name__ = "Integer32"
_HpnicfDot11RRMHistoryPER_Object = MibTableColumn
hpnicfDot11RRMHistoryPER = _HpnicfDot11RRMHistoryPER_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 9),
    _HpnicfDot11RRMHistoryPER_Type()
)
hpnicfDot11RRMHistoryPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryPER.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryPER.setUnits("percent")


class _HpnicfDot11RRMHistoryRetryRate_Type(Integer32):
    """Custom type hpnicfDot11RRMHistoryRetryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11RRMHistoryRetryRate_Type.__name__ = "Integer32"
_HpnicfDot11RRMHistoryRetryRate_Object = MibTableColumn
hpnicfDot11RRMHistoryRetryRate = _HpnicfDot11RRMHistoryRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 10),
    _HpnicfDot11RRMHistoryRetryRate_Type()
)
hpnicfDot11RRMHistoryRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryRetryRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryRetryRate.setUnits("percent")


class _HpnicfDot11RRMHistoryChgReason_Type(Bits):
    """Custom type hpnicfDot11RRMHistoryChgReason based on Bits"""
    namedValues = NamedValues(
        *(("coverage", 1),
          ("interference", 5),
          ("others", 0),
          ("packetsDiscarded", 4),
          ("radar", 2),
          ("retransmission", 3))
    )

_HpnicfDot11RRMHistoryChgReason_Type.__name__ = "Bits"
_HpnicfDot11RRMHistoryChgReason_Object = MibTableColumn
hpnicfDot11RRMHistoryChgReason = _HpnicfDot11RRMHistoryChgReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 11),
    _HpnicfDot11RRMHistoryChgReason_Type()
)
hpnicfDot11RRMHistoryChgReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryChgReason.setStatus("current")
_HpnicfDot11RRMHistoryChgDateTime_Type = DateAndTime
_HpnicfDot11RRMHistoryChgDateTime_Object = MibTableColumn
hpnicfDot11RRMHistoryChgDateTime = _HpnicfDot11RRMHistoryChgDateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 3, 1, 12),
    _HpnicfDot11RRMHistoryChgDateTime_Type()
)
hpnicfDot11RRMHistoryChgDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMHistoryChgDateTime.setStatus("current")
_HpnicfDot11RRMRadioNbrInfoTable_Object = MibTable
hpnicfDot11RRMRadioNbrInfoTable = _HpnicfDot11RRMRadioNbrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioNbrInfoTable.setStatus("current")
_HpnicfDot11RRMRadioNbrInfoEntry_Object = MibTableRow
hpnicfDot11RRMRadioNbrInfoEntry = _HpnicfDot11RRMRadioNbrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 4, 1)
)
hpnicfDot11RRMRadioNbrInfoEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMRadioNbrAPID"),
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMRadioNbrRadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioNbrInfoEntry.setStatus("current")
_HpnicfDot11RRMRadioNbrAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11RRMRadioNbrAPID_Object = MibTableColumn
hpnicfDot11RRMRadioNbrAPID = _HpnicfDot11RRMRadioNbrAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 4, 1, 1),
    _HpnicfDot11RRMRadioNbrAPID_Type()
)
hpnicfDot11RRMRadioNbrAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioNbrAPID.setStatus("current")
_HpnicfDot11RRMRadioNbrRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11RRMRadioNbrRadioID_Object = MibTableColumn
hpnicfDot11RRMRadioNbrRadioID = _HpnicfDot11RRMRadioNbrRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 4, 1, 2),
    _HpnicfDot11RRMRadioNbrRadioID_Type()
)
hpnicfDot11RRMRadioNbrRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioNbrRadioID.setStatus("current")
_HpnicfDot11RRMRadioNbrSSID_Type = OctetString
_HpnicfDot11RRMRadioNbrSSID_Object = MibTableColumn
hpnicfDot11RRMRadioNbrSSID = _HpnicfDot11RRMRadioNbrSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 2, 4, 1, 3),
    _HpnicfDot11RRMRadioNbrSSID_Type()
)
hpnicfDot11RRMRadioNbrSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RRMRadioNbrSSID.setStatus("current")
_HpnicfDot11RRMNotifyGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMNotifyGroup = _HpnicfDot11RRMNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3)
)
_HpnicfDot11RRMChlQltyNotifications_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMChlQltyNotifications = _HpnicfDot11RRMChlQltyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 1)
)
_HpnicfDot11RRMChlQltyNtfPrefix_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMChlQltyNtfPrefix = _HpnicfDot11RRMChlQltyNtfPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 1, 0)
)
_HpnicfDot11RRMResChgNotifications_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMResChgNotifications = _HpnicfDot11RRMResChgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 2)
)
_HpnicfDot11RRMResChgNtfPrefix_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMResChgNtfPrefix = _HpnicfDot11RRMResChgNtfPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 2, 0)
)
_HpnicfDot11RRMNotificationsVar_ObjectIdentity = ObjectIdentity
hpnicfDot11RRMNotificationsVar = _HpnicfDot11RRMNotificationsVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 3)
)
_HpnicfDot11NewPower_Type = Integer32
_HpnicfDot11NewPower_Object = MibScalar
hpnicfDot11NewPower = _HpnicfDot11NewPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 3, 1),
    _HpnicfDot11NewPower_Type()
)
hpnicfDot11NewPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11NewPower.setStatus("current")
_HpnicfDot11OldPower_Type = Integer32
_HpnicfDot11OldPower_Object = MibScalar
hpnicfDot11OldPower = _HpnicfDot11OldPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 3, 2),
    _HpnicfDot11OldPower_Type()
)
hpnicfDot11OldPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11OldPower.setStatus("current")
_HpnicfDot11MonitorDetectedGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11MonitorDetectedGroup = _HpnicfDot11MonitorDetectedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4)
)
_HpnicfDot11MonitorDetectedDevTable_Object = MibTable
hpnicfDot11MonitorDetectedDevTable = _HpnicfDot11MonitorDetectedDevTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDetectedDevTable.setStatus("current")
_HpnicfDot11MonitorDetectedDevEntry_Object = MibTableRow
hpnicfDot11MonitorDetectedDevEntry = _HpnicfDot11MonitorDetectedDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1)
)
hpnicfDot11MonitorDetectedDevEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11MonitorDevMAC"),
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDetectedDevEntry.setStatus("current")
_HpnicfDot11MonitorDevMAC_Type = MacAddress
_HpnicfDot11MonitorDevMAC_Object = MibTableColumn
hpnicfDot11MonitorDevMAC = _HpnicfDot11MonitorDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 1),
    _HpnicfDot11MonitorDevMAC_Type()
)
hpnicfDot11MonitorDevMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevMAC.setStatus("current")


class _HpnicfDot11MonitorDevType_Type(Integer32):
    """Custom type hpnicfDot11MonitorDevType based on Integer32"""
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
        *(("adhoc", 3),
          ("ap", 2),
          ("client", 1),
          ("unknown", 5),
          ("wirelessBridge", 4))
    )


_HpnicfDot11MonitorDevType_Type.__name__ = "Integer32"
_HpnicfDot11MonitorDevType_Object = MibTableColumn
hpnicfDot11MonitorDevType = _HpnicfDot11MonitorDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 2),
    _HpnicfDot11MonitorDevType_Type()
)
hpnicfDot11MonitorDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevType.setStatus("current")
_HpnicfDot11MonitorDevVendor_Type = OctetString
_HpnicfDot11MonitorDevVendor_Object = MibTableColumn
hpnicfDot11MonitorDevVendor = _HpnicfDot11MonitorDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 3),
    _HpnicfDot11MonitorDevVendor_Type()
)
hpnicfDot11MonitorDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevVendor.setStatus("current")
_HpnicfDot11MonitorDevSSID_Type = OctetString
_HpnicfDot11MonitorDevSSID_Object = MibTableColumn
hpnicfDot11MonitorDevSSID = _HpnicfDot11MonitorDevSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 4),
    _HpnicfDot11MonitorDevSSID_Type()
)
hpnicfDot11MonitorDevSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevSSID.setStatus("current")
_HpnicfDot11MonitorDevBSSID_Type = MacAddress
_HpnicfDot11MonitorDevBSSID_Object = MibTableColumn
hpnicfDot11MonitorDevBSSID = _HpnicfDot11MonitorDevBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 5),
    _HpnicfDot11MonitorDevBSSID_Type()
)
hpnicfDot11MonitorDevBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevBSSID.setStatus("current")
_HpnicfDot11MonitorDevChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11MonitorDevChannel_Object = MibTableColumn
hpnicfDot11MonitorDevChannel = _HpnicfDot11MonitorDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 6),
    _HpnicfDot11MonitorDevChannel_Type()
)
hpnicfDot11MonitorDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevChannel.setStatus("current")
_HpnicfDot11MonitorRadioId_Type = HpnicfDot11RadioScopeType
_HpnicfDot11MonitorRadioId_Object = MibTableColumn
hpnicfDot11MonitorRadioId = _HpnicfDot11MonitorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 7),
    _HpnicfDot11MonitorRadioId_Type()
)
hpnicfDot11MonitorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorRadioId.setStatus("current")
_HpnicfDot11MonitorDevMaxRSSI_Type = Integer32
_HpnicfDot11MonitorDevMaxRSSI_Object = MibTableColumn
hpnicfDot11MonitorDevMaxRSSI = _HpnicfDot11MonitorDevMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 8),
    _HpnicfDot11MonitorDevMaxRSSI_Type()
)
hpnicfDot11MonitorDevMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevMaxRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevMaxRSSI.setUnits("dbm")
_HpnicfDot11MonitorDevBeaconIntvl_Type = Integer32
_HpnicfDot11MonitorDevBeaconIntvl_Object = MibTableColumn
hpnicfDot11MonitorDevBeaconIntvl = _HpnicfDot11MonitorDevBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 9),
    _HpnicfDot11MonitorDevBeaconIntvl_Type()
)
hpnicfDot11MonitorDevBeaconIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevBeaconIntvl.setUnits("millisecond")
_HpnicfDot11MonitorDevFstDctTime_Type = DateAndTime
_HpnicfDot11MonitorDevFstDctTime_Object = MibTableColumn
hpnicfDot11MonitorDevFstDctTime = _HpnicfDot11MonitorDevFstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 10),
    _HpnicfDot11MonitorDevFstDctTime_Type()
)
hpnicfDot11MonitorDevFstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevFstDctTime.setStatus("current")
_HpnicfDot11MonitorDevLstDctTime_Type = DateAndTime
_HpnicfDot11MonitorDevLstDctTime_Object = MibTableColumn
hpnicfDot11MonitorDevLstDctTime = _HpnicfDot11MonitorDevLstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 11),
    _HpnicfDot11MonitorDevLstDctTime_Type()
)
hpnicfDot11MonitorDevLstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevLstDctTime.setStatus("current")
_HpnicfDot11MonitorDevClear_Type = TruthValue
_HpnicfDot11MonitorDevClear_Object = MibTableColumn
hpnicfDot11MonitorDevClear = _HpnicfDot11MonitorDevClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 12),
    _HpnicfDot11MonitorDevClear_Type()
)
hpnicfDot11MonitorDevClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevClear.setStatus("current")
_HpnicfDot11MonitorDevSNR_Type = Integer32
_HpnicfDot11MonitorDevSNR_Object = MibTableColumn
hpnicfDot11MonitorDevSNR = _HpnicfDot11MonitorDevSNR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 4, 1, 1, 13),
    _HpnicfDot11MonitorDevSNR_Type()
)
hpnicfDot11MonitorDevSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorDevSNR.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDot11RRMIntrfLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 1, 0, 1)
)
hpnicfDot11RRMIntrfLimit.setObjects(
    ("HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMChlRptIntrf")
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMIntrfLimit.setStatus(
        "current"
    )

hpnicfDot11RRMPERLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 1, 0, 2)
)
hpnicfDot11RRMPERLimit.setObjects(
    ("HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMChlRptPER")
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMPERLimit.setStatus(
        "current"
    )

hpnicfDot11RRMNoiseLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 1, 0, 3)
)
hpnicfDot11RRMNoiseLimit.setObjects(
    ("HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMChlRptNoise")
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMNoiseLimit.setStatus(
        "current"
    )

hpnicfDot11RRMPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 8, 3, 2, 0, 1)
)
hpnicfDot11RRMPowerChange.setObjects(
      *(("HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11RRMRadioIndex"),
        ("HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11NewPower"),
        ("HPN-ICF-DOT11-RRM-MIB", "hpnicfDot11OldPower"))
)
if mibBuilder.loadTexts:
    hpnicfDot11RRMPowerChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-RRM-MIB",
    **{"hpnicfDot11RRM": hpnicfDot11RRM,
       "hpnicfDot11RRMConfigGroup": hpnicfDot11RRMConfigGroup,
       "hpnicfDot11RRMGlobalCfgPara": hpnicfDot11RRMGlobalCfgPara,
       "hpnicfDot11RRM11nMadtMaxMcs": hpnicfDot11RRM11nMadtMaxMcs,
       "hpnicfDot11RRM11nSuptMaxMcs": hpnicfDot11RRM11nSuptMaxMcs,
       "hpnicfDot11RRM11gProtect": hpnicfDot11RRM11gProtect,
       "hpnicfDot11RRM11aPwrConstrt": hpnicfDot11RRM11aPwrConstrt,
       "hpnicfDot11RRM11aSpectrumManag": hpnicfDot11RRM11aSpectrumManag,
       "hpnicfDot11RRMAutoChlAvoid11h": hpnicfDot11RRMAutoChlAvoid11h,
       "hpnicfDot11RRMScanChl": hpnicfDot11RRMScanChl,
       "hpnicfDot11RRMScanRptIntvel": hpnicfDot11RRMScanRptIntvel,
       "hpnicfDot11APInterfNumThreshhd": hpnicfDot11APInterfNumThreshhd,
       "hpnicfDot11StaInterfNumThreshhd": hpnicfDot11StaInterfNumThreshhd,
       "hpnicfDot11RRM11nMultiCastMcs": hpnicfDot11RRM11nMultiCastMcs,
       "hpnicfDot11RRM11acMadtMaxNss": hpnicfDot11RRM11acMadtMaxNss,
       "hpnicfDot11RRM11acSuptMaxNss": hpnicfDot11RRM11acSuptMaxNss,
       "hpnicfDot11RRM11acMultiCastNss": hpnicfDot11RRM11acMultiCastNss,
       "hpnicfDot11RRM11acMultiCastVhtMcs": hpnicfDot11RRM11acMultiCastVhtMcs,
       "hpnicfDot11RRMRadioCfgTable": hpnicfDot11RRMRadioCfgTable,
       "hpnicfDot11RRMRadioCfgEntry": hpnicfDot11RRMRadioCfgEntry,
       "hpnicfDot11RRMRadioType": hpnicfDot11RRMRadioType,
       "hpnicfDot11RRMCfgChlState": hpnicfDot11RRMCfgChlState,
       "hpnicfDot11RRMCfgChlMode": hpnicfDot11RRMCfgChlMode,
       "hpnicfDot11RRMChlProntoRadioElmt": hpnicfDot11RRMChlProntoRadioElmt,
       "hpnicfDot11RRMCfgPwrState": hpnicfDot11RRMCfgPwrState,
       "hpnicfDot11RRMCfgPwrMode": hpnicfDot11RRMCfgPwrMode,
       "hpnicfDot11RRMPwrProntoRadioElmt": hpnicfDot11RRMPwrProntoRadioElmt,
       "hpnicfDot11RRMCfgIntrvl": hpnicfDot11RRMCfgIntrvl,
       "hpnicfDot11RRMCfgIntrfThres": hpnicfDot11RRMCfgIntrfThres,
       "hpnicfDot11RRMCfgNoiseThres": hpnicfDot11RRMCfgNoiseThres,
       "hpnicfDot11RRMCfgPERThres": hpnicfDot11RRMCfgPERThres,
       "hpnicfDot11RRMCfgToleranceFctr": hpnicfDot11RRMCfgToleranceFctr,
       "hpnicfDot11RRMCfgAdjacencyFctr": hpnicfDot11RRMCfgAdjacencyFctr,
       "hpnicfDot11RRMAPCfgTable": hpnicfDot11RRMAPCfgTable,
       "hpnicfDot11RRMAPCfgEntry": hpnicfDot11RRMAPCfgEntry,
       "hpnicfDot11RRMAPWorkMode": hpnicfDot11RRMAPWorkMode,
       "hpnicfDot11RRMSDRadioGroupTable": hpnicfDot11RRMSDRadioGroupTable,
       "hpnicfDot11RRMSDRadioGroupEntry": hpnicfDot11RRMSDRadioGroupEntry,
       "hpnicfDot11RRMSDRadioGroupId": hpnicfDot11RRMSDRadioGroupId,
       "hpnicfDot11RRMSDRadioGroupDesc": hpnicfDot11RRMSDRadioGroupDesc,
       "hpnicfDot11RRMSDRdGrpChlHolddownTm": hpnicfDot11RRMSDRdGrpChlHolddownTm,
       "hpnicfDot11RRMSDRdGrpPwrHolddownTm": hpnicfDot11RRMSDRdGrpPwrHolddownTm,
       "hpnicfDot11RRMSDRdGroupRowStatus": hpnicfDot11RRMSDRdGroupRowStatus,
       "hpnicfDot11RRMAPCfg2Table": hpnicfDot11RRMAPCfg2Table,
       "hpnicfDot11RRMAPCfg2Entry": hpnicfDot11RRMAPCfg2Entry,
       "hpnicfDot11RRMAPSerialID": hpnicfDot11RRMAPSerialID,
       "hpnicfDot11RRMAPIntfThreshold": hpnicfDot11RRMAPIntfThreshold,
       "hpnicfDot11RRMStaIntfThreshold": hpnicfDot11RRMStaIntfThreshold,
       "hpnicfDot11RRMCoChlIntfTrapThhd": hpnicfDot11RRMCoChlIntfTrapThhd,
       "hpnicfDot11RRMAdjChlIntfTrapThhd": hpnicfDot11RRMAdjChlIntfTrapThhd,
       "hpnicfDot11RRMDetectGroup": hpnicfDot11RRMDetectGroup,
       "hpnicfDot11RRMChlRptTable": hpnicfDot11RRMChlRptTable,
       "hpnicfDot11RRMChlRptEntry": hpnicfDot11RRMChlRptEntry,
       "hpnicfDot11RRMRadioIndex": hpnicfDot11RRMRadioIndex,
       "hpnicfDot11RRMChlRptChlNum": hpnicfDot11RRMChlRptChlNum,
       "hpnicfDot11RRMChlRptChlType": hpnicfDot11RRMChlRptChlType,
       "hpnicfDot11RRMChlRptChlQlty": hpnicfDot11RRMChlRptChlQlty,
       "hpnicfDot11RRMChlRptNbrCnt": hpnicfDot11RRMChlRptNbrCnt,
       "hpnicfDot11RRMChlRptLoad": hpnicfDot11RRMChlRptLoad,
       "hpnicfDot11RRMChlRptUtlz": hpnicfDot11RRMChlRptUtlz,
       "hpnicfDot11RRMChlRptIntrf": hpnicfDot11RRMChlRptIntrf,
       "hpnicfDot11RRMChlRptPER": hpnicfDot11RRMChlRptPER,
       "hpnicfDot11RRMChlRptRetryRate": hpnicfDot11RRMChlRptRetryRate,
       "hpnicfDot11RRMChlRptNoise": hpnicfDot11RRMChlRptNoise,
       "hpnicfDot11RRMChlRptRadarIndtcr": hpnicfDot11RRMChlRptRadarIndtcr,
       "hpnicfDot11RRMNbrInfoTable": hpnicfDot11RRMNbrInfoTable,
       "hpnicfDot11RRMNbrInfoEntry": hpnicfDot11RRMNbrInfoEntry,
       "hpnicfDot11RrmNbrBSSID": hpnicfDot11RrmNbrBSSID,
       "hpnicfDot11RrmNbrChl": hpnicfDot11RrmNbrChl,
       "hpnicfDot11RRMNbrIntrf": hpnicfDot11RRMNbrIntrf,
       "hpnicfDot11RrmNbrRSSI": hpnicfDot11RrmNbrRSSI,
       "hpnicfDot11RrmNbrType": hpnicfDot11RrmNbrType,
       "hpnicfDot11RrmNbrSSID": hpnicfDot11RrmNbrSSID,
       "hpnicfDot11RRMHistoryTable": hpnicfDot11RRMHistoryTable,
       "hpnicfDot11RRMHistoryEntry": hpnicfDot11RRMHistoryEntry,
       "hpnicfDot11RRMHistoryId": hpnicfDot11RRMHistoryId,
       "hpnicfDot11RRMHistoryRecIndctr": hpnicfDot11RRMHistoryRecIndctr,
       "hpnicfDot11RRMHistoryChl": hpnicfDot11RRMHistoryChl,
       "hpnicfDot11RRMHistoryPwr": hpnicfDot11RRMHistoryPwr,
       "hpnicfDot11RRMHistoryLoad": hpnicfDot11RRMHistoryLoad,
       "hpnicfDot11RRMHistoryUtlz": hpnicfDot11RRMHistoryUtlz,
       "hpnicfDot11RRMHistoryIntrf": hpnicfDot11RRMHistoryIntrf,
       "hpnicfDot11RRMHistoryNoise": hpnicfDot11RRMHistoryNoise,
       "hpnicfDot11RRMHistoryPER": hpnicfDot11RRMHistoryPER,
       "hpnicfDot11RRMHistoryRetryRate": hpnicfDot11RRMHistoryRetryRate,
       "hpnicfDot11RRMHistoryChgReason": hpnicfDot11RRMHistoryChgReason,
       "hpnicfDot11RRMHistoryChgDateTime": hpnicfDot11RRMHistoryChgDateTime,
       "hpnicfDot11RRMRadioNbrInfoTable": hpnicfDot11RRMRadioNbrInfoTable,
       "hpnicfDot11RRMRadioNbrInfoEntry": hpnicfDot11RRMRadioNbrInfoEntry,
       "hpnicfDot11RRMRadioNbrAPID": hpnicfDot11RRMRadioNbrAPID,
       "hpnicfDot11RRMRadioNbrRadioID": hpnicfDot11RRMRadioNbrRadioID,
       "hpnicfDot11RRMRadioNbrSSID": hpnicfDot11RRMRadioNbrSSID,
       "hpnicfDot11RRMNotifyGroup": hpnicfDot11RRMNotifyGroup,
       "hpnicfDot11RRMChlQltyNotifications": hpnicfDot11RRMChlQltyNotifications,
       "hpnicfDot11RRMChlQltyNtfPrefix": hpnicfDot11RRMChlQltyNtfPrefix,
       "hpnicfDot11RRMIntrfLimit": hpnicfDot11RRMIntrfLimit,
       "hpnicfDot11RRMPERLimit": hpnicfDot11RRMPERLimit,
       "hpnicfDot11RRMNoiseLimit": hpnicfDot11RRMNoiseLimit,
       "hpnicfDot11RRMResChgNotifications": hpnicfDot11RRMResChgNotifications,
       "hpnicfDot11RRMResChgNtfPrefix": hpnicfDot11RRMResChgNtfPrefix,
       "hpnicfDot11RRMPowerChange": hpnicfDot11RRMPowerChange,
       "hpnicfDot11RRMNotificationsVar": hpnicfDot11RRMNotificationsVar,
       "hpnicfDot11NewPower": hpnicfDot11NewPower,
       "hpnicfDot11OldPower": hpnicfDot11OldPower,
       "hpnicfDot11MonitorDetectedGroup": hpnicfDot11MonitorDetectedGroup,
       "hpnicfDot11MonitorDetectedDevTable": hpnicfDot11MonitorDetectedDevTable,
       "hpnicfDot11MonitorDetectedDevEntry": hpnicfDot11MonitorDetectedDevEntry,
       "hpnicfDot11MonitorDevMAC": hpnicfDot11MonitorDevMAC,
       "hpnicfDot11MonitorDevType": hpnicfDot11MonitorDevType,
       "hpnicfDot11MonitorDevVendor": hpnicfDot11MonitorDevVendor,
       "hpnicfDot11MonitorDevSSID": hpnicfDot11MonitorDevSSID,
       "hpnicfDot11MonitorDevBSSID": hpnicfDot11MonitorDevBSSID,
       "hpnicfDot11MonitorDevChannel": hpnicfDot11MonitorDevChannel,
       "hpnicfDot11MonitorRadioId": hpnicfDot11MonitorRadioId,
       "hpnicfDot11MonitorDevMaxRSSI": hpnicfDot11MonitorDevMaxRSSI,
       "hpnicfDot11MonitorDevBeaconIntvl": hpnicfDot11MonitorDevBeaconIntvl,
       "hpnicfDot11MonitorDevFstDctTime": hpnicfDot11MonitorDevFstDctTime,
       "hpnicfDot11MonitorDevLstDctTime": hpnicfDot11MonitorDevLstDctTime,
       "hpnicfDot11MonitorDevClear": hpnicfDot11MonitorDevClear,
       "hpnicfDot11MonitorDevSNR": hpnicfDot11MonitorDevSNR}
)
