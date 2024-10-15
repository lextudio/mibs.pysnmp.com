# SNMP MIB module (HH3C-DOT11-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-RRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:54 2024
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

(Hh3cDot11ChannelScopeType,
 Hh3cDot11ObjectIDType,
 Hh3cDot11RadioElementIndex,
 Hh3cDot11RadioScopeType,
 Hh3cDot11RadioType,
 Hh3cDot11SSIDStringType,
 hh3cDot11,
 hh3cDot11APElementIndex) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11ChannelScopeType",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11RadioElementIndex",
    "Hh3cDot11RadioScopeType",
    "Hh3cDot11RadioType",
    "Hh3cDot11SSIDStringType",
    "hh3cDot11",
    "hh3cDot11APElementIndex")

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

hh3cDot11RRM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8)
)
hh3cDot11RRM.setRevisions(
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

_Hh3cDot11RRMConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RRMConfigGroup = _Hh3cDot11RRMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1)
)
_Hh3cDot11RRMGlobalCfgPara_ObjectIdentity = ObjectIdentity
hh3cDot11RRMGlobalCfgPara = _Hh3cDot11RRMGlobalCfgPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1)
)


class _Hh3cDot11RRM11nMadtMaxMcs_Type(Integer32):
    """Custom type hh3cDot11RRM11nMadtMaxMcs based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
        ValueRangeConstraint(255, 255),
    )


_Hh3cDot11RRM11nMadtMaxMcs_Type.__name__ = "Integer32"
_Hh3cDot11RRM11nMadtMaxMcs_Object = MibScalar
hh3cDot11RRM11nMadtMaxMcs = _Hh3cDot11RRM11nMadtMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 1),
    _Hh3cDot11RRM11nMadtMaxMcs_Type()
)
hh3cDot11RRM11nMadtMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRM11nMadtMaxMcs.setStatus("current")


class _Hh3cDot11RRM11nSuptMaxMcs_Type(Integer32):
    """Custom type hh3cDot11RRM11nSuptMaxMcs based on Integer32"""
    defaultValue = 76

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_Hh3cDot11RRM11nSuptMaxMcs_Type.__name__ = "Integer32"
_Hh3cDot11RRM11nSuptMaxMcs_Object = MibScalar
hh3cDot11RRM11nSuptMaxMcs = _Hh3cDot11RRM11nSuptMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 2),
    _Hh3cDot11RRM11nSuptMaxMcs_Type()
)
hh3cDot11RRM11nSuptMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRM11nSuptMaxMcs.setStatus("current")


class _Hh3cDot11RRM11gProtect_Type(TruthValue):
    """Custom type hh3cDot11RRM11gProtect based on TruthValue"""


_Hh3cDot11RRM11gProtect_Object = MibScalar
hh3cDot11RRM11gProtect = _Hh3cDot11RRM11gProtect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 3),
    _Hh3cDot11RRM11gProtect_Type()
)
hh3cDot11RRM11gProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRM11gProtect.setStatus("current")


class _Hh3cDot11RRM11aPwrConstrt_Type(Integer32):
    """Custom type hh3cDot11RRM11aPwrConstrt based on Integer32"""
    defaultValue = 0


_Hh3cDot11RRM11aPwrConstrt_Object = MibScalar
hh3cDot11RRM11aPwrConstrt = _Hh3cDot11RRM11aPwrConstrt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 4),
    _Hh3cDot11RRM11aPwrConstrt_Type()
)
hh3cDot11RRM11aPwrConstrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRM11aPwrConstrt.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRM11aPwrConstrt.setUnits("dBm")


class _Hh3cDot11RRM11aSpectrumManag_Type(TruthValue):
    """Custom type hh3cDot11RRM11aSpectrumManag based on TruthValue"""


_Hh3cDot11RRM11aSpectrumManag_Object = MibScalar
hh3cDot11RRM11aSpectrumManag = _Hh3cDot11RRM11aSpectrumManag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 5),
    _Hh3cDot11RRM11aSpectrumManag_Type()
)
hh3cDot11RRM11aSpectrumManag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRM11aSpectrumManag.setStatus("current")


class _Hh3cDot11RRMAutoChlAvoid11h_Type(TruthValue):
    """Custom type hh3cDot11RRMAutoChlAvoid11h based on TruthValue"""


_Hh3cDot11RRMAutoChlAvoid11h_Object = MibScalar
hh3cDot11RRMAutoChlAvoid11h = _Hh3cDot11RRMAutoChlAvoid11h_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 6),
    _Hh3cDot11RRMAutoChlAvoid11h_Type()
)
hh3cDot11RRMAutoChlAvoid11h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMAutoChlAvoid11h.setStatus("current")


class _Hh3cDot11RRMScanChl_Type(Integer32):
    """Custom type hh3cDot11RRMScanChl based on Integer32"""
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


_Hh3cDot11RRMScanChl_Type.__name__ = "Integer32"
_Hh3cDot11RRMScanChl_Object = MibScalar
hh3cDot11RRMScanChl = _Hh3cDot11RRMScanChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 7),
    _Hh3cDot11RRMScanChl_Type()
)
hh3cDot11RRMScanChl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMScanChl.setStatus("current")


class _Hh3cDot11RRMScanRptIntvel_Type(Integer32):
    """Custom type hh3cDot11RRMScanRptIntvel based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_Hh3cDot11RRMScanRptIntvel_Type.__name__ = "Integer32"
_Hh3cDot11RRMScanRptIntvel_Object = MibScalar
hh3cDot11RRMScanRptIntvel = _Hh3cDot11RRMScanRptIntvel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 8),
    _Hh3cDot11RRMScanRptIntvel_Type()
)
hh3cDot11RRMScanRptIntvel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMScanRptIntvel.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMScanRptIntvel.setUnits("second")


class _Hh3cDot11APInterfNumThreshhd_Type(Integer32):
    """Custom type hh3cDot11APInterfNumThreshhd based on Integer32"""
    defaultValue = 0


_Hh3cDot11APInterfNumThreshhd_Object = MibScalar
hh3cDot11APInterfNumThreshhd = _Hh3cDot11APInterfNumThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 9),
    _Hh3cDot11APInterfNumThreshhd_Type()
)
hh3cDot11APInterfNumThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APInterfNumThreshhd.setStatus("current")


class _Hh3cDot11StaInterfNumThreshhd_Type(Integer32):
    """Custom type hh3cDot11StaInterfNumThreshhd based on Integer32"""
    defaultValue = 0


_Hh3cDot11StaInterfNumThreshhd_Object = MibScalar
hh3cDot11StaInterfNumThreshhd = _Hh3cDot11StaInterfNumThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 1, 10),
    _Hh3cDot11StaInterfNumThreshhd_Type()
)
hh3cDot11StaInterfNumThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StaInterfNumThreshhd.setStatus("current")
_Hh3cDot11RRMRadioCfgTable_Object = MibTable
hh3cDot11RRMRadioCfgTable = _Hh3cDot11RRMRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RRMRadioCfgTable.setStatus("current")
_Hh3cDot11RRMRadioCfgEntry_Object = MibTableRow
hh3cDot11RRMRadioCfgEntry = _Hh3cDot11RRMRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1)
)
hh3cDot11RRMRadioCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMRadioType"),
)
if mibBuilder.loadTexts:
    hh3cDot11RRMRadioCfgEntry.setStatus("current")
_Hh3cDot11RRMRadioType_Type = Hh3cDot11RadioType
_Hh3cDot11RRMRadioType_Object = MibTableColumn
hh3cDot11RRMRadioType = _Hh3cDot11RRMRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 1),
    _Hh3cDot11RRMRadioType_Type()
)
hh3cDot11RRMRadioType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RRMRadioType.setStatus("current")


class _Hh3cDot11RRMCfgChlState_Type(TruthValue):
    """Custom type hh3cDot11RRMCfgChlState based on TruthValue"""


_Hh3cDot11RRMCfgChlState_Object = MibTableColumn
hh3cDot11RRMCfgChlState = _Hh3cDot11RRMCfgChlState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 2),
    _Hh3cDot11RRMCfgChlState_Type()
)
hh3cDot11RRMCfgChlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgChlState.setStatus("current")


class _Hh3cDot11RRMCfgChlMode_Type(Integer32):
    """Custom type hh3cDot11RRMCfgChlMode based on Integer32"""
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


_Hh3cDot11RRMCfgChlMode_Type.__name__ = "Integer32"
_Hh3cDot11RRMCfgChlMode_Object = MibTableColumn
hh3cDot11RRMCfgChlMode = _Hh3cDot11RRMCfgChlMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 3),
    _Hh3cDot11RRMCfgChlMode_Type()
)
hh3cDot11RRMCfgChlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgChlMode.setStatus("current")


class _Hh3cDot11RRMChlProntoRadioElmt_Type(Unsigned32):
    """Custom type hh3cDot11RRMChlProntoRadioElmt based on Unsigned32"""
    defaultValue = 0


_Hh3cDot11RRMChlProntoRadioElmt_Object = MibTableColumn
hh3cDot11RRMChlProntoRadioElmt = _Hh3cDot11RRMChlProntoRadioElmt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 4),
    _Hh3cDot11RRMChlProntoRadioElmt_Type()
)
hh3cDot11RRMChlProntoRadioElmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlProntoRadioElmt.setStatus("current")


class _Hh3cDot11RRMCfgPwrState_Type(TruthValue):
    """Custom type hh3cDot11RRMCfgPwrState based on TruthValue"""


_Hh3cDot11RRMCfgPwrState_Object = MibTableColumn
hh3cDot11RRMCfgPwrState = _Hh3cDot11RRMCfgPwrState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 5),
    _Hh3cDot11RRMCfgPwrState_Type()
)
hh3cDot11RRMCfgPwrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgPwrState.setStatus("current")


class _Hh3cDot11RRMCfgPwrMode_Type(Integer32):
    """Custom type hh3cDot11RRMCfgPwrMode based on Integer32"""
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


_Hh3cDot11RRMCfgPwrMode_Type.__name__ = "Integer32"
_Hh3cDot11RRMCfgPwrMode_Object = MibTableColumn
hh3cDot11RRMCfgPwrMode = _Hh3cDot11RRMCfgPwrMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 6),
    _Hh3cDot11RRMCfgPwrMode_Type()
)
hh3cDot11RRMCfgPwrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgPwrMode.setStatus("current")


class _Hh3cDot11RRMPwrProntoRadioElmt_Type(Unsigned32):
    """Custom type hh3cDot11RRMPwrProntoRadioElmt based on Unsigned32"""
    defaultValue = 0


_Hh3cDot11RRMPwrProntoRadioElmt_Object = MibTableColumn
hh3cDot11RRMPwrProntoRadioElmt = _Hh3cDot11RRMPwrProntoRadioElmt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 7),
    _Hh3cDot11RRMPwrProntoRadioElmt_Type()
)
hh3cDot11RRMPwrProntoRadioElmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMPwrProntoRadioElmt.setStatus("current")


class _Hh3cDot11RRMCfgIntrvl_Type(Integer32):
    """Custom type hh3cDot11RRMCfgIntrvl based on Integer32"""
    defaultValue = 8


_Hh3cDot11RRMCfgIntrvl_Object = MibTableColumn
hh3cDot11RRMCfgIntrvl = _Hh3cDot11RRMCfgIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 8),
    _Hh3cDot11RRMCfgIntrvl_Type()
)
hh3cDot11RRMCfgIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgIntrvl.setUnits("minute")


class _Hh3cDot11RRMCfgIntrfThres_Type(Integer32):
    """Custom type hh3cDot11RRMCfgIntrfThres based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_Hh3cDot11RRMCfgIntrfThres_Type.__name__ = "Integer32"
_Hh3cDot11RRMCfgIntrfThres_Object = MibTableColumn
hh3cDot11RRMCfgIntrfThres = _Hh3cDot11RRMCfgIntrfThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 9),
    _Hh3cDot11RRMCfgIntrfThres_Type()
)
hh3cDot11RRMCfgIntrfThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgIntrfThres.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgIntrfThres.setUnits("percent")


class _Hh3cDot11RRMCfgNoiseThres_Type(Integer32):
    """Custom type hh3cDot11RRMCfgNoiseThres based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_Hh3cDot11RRMCfgNoiseThres_Type.__name__ = "Integer32"
_Hh3cDot11RRMCfgNoiseThres_Object = MibTableColumn
hh3cDot11RRMCfgNoiseThres = _Hh3cDot11RRMCfgNoiseThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 10),
    _Hh3cDot11RRMCfgNoiseThres_Type()
)
hh3cDot11RRMCfgNoiseThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgNoiseThres.setStatus("current")


class _Hh3cDot11RRMCfgPERThres_Type(Integer32):
    """Custom type hh3cDot11RRMCfgPERThres based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_Hh3cDot11RRMCfgPERThres_Type.__name__ = "Integer32"
_Hh3cDot11RRMCfgPERThres_Object = MibTableColumn
hh3cDot11RRMCfgPERThres = _Hh3cDot11RRMCfgPERThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 11),
    _Hh3cDot11RRMCfgPERThres_Type()
)
hh3cDot11RRMCfgPERThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgPERThres.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgPERThres.setUnits("percent")


class _Hh3cDot11RRMCfgToleranceFctr_Type(Integer32):
    """Custom type hh3cDot11RRMCfgToleranceFctr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 45),
    )


_Hh3cDot11RRMCfgToleranceFctr_Type.__name__ = "Integer32"
_Hh3cDot11RRMCfgToleranceFctr_Object = MibTableColumn
hh3cDot11RRMCfgToleranceFctr = _Hh3cDot11RRMCfgToleranceFctr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 12),
    _Hh3cDot11RRMCfgToleranceFctr_Type()
)
hh3cDot11RRMCfgToleranceFctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgToleranceFctr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgToleranceFctr.setUnits("percent")


class _Hh3cDot11RRMCfgAdjacencyFctr_Type(Integer32):
    """Custom type hh3cDot11RRMCfgAdjacencyFctr based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cDot11RRMCfgAdjacencyFctr_Type.__name__ = "Integer32"
_Hh3cDot11RRMCfgAdjacencyFctr_Object = MibTableColumn
hh3cDot11RRMCfgAdjacencyFctr = _Hh3cDot11RRMCfgAdjacencyFctr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 2, 1, 13),
    _Hh3cDot11RRMCfgAdjacencyFctr_Type()
)
hh3cDot11RRMCfgAdjacencyFctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCfgAdjacencyFctr.setStatus("current")
_Hh3cDot11RRMAPCfgTable_Object = MibTable
hh3cDot11RRMAPCfgTable = _Hh3cDot11RRMAPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11RRMAPCfgTable.setStatus("current")
_Hh3cDot11RRMAPCfgEntry_Object = MibTableRow
hh3cDot11RRMAPCfgEntry = _Hh3cDot11RRMAPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 3, 1)
)
hh3cDot11RRMAPCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11RRMAPCfgEntry.setStatus("current")


class _Hh3cDot11RRMAPWorkMode_Type(Integer32):
    """Custom type hh3cDot11RRMAPWorkMode based on Integer32"""
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


_Hh3cDot11RRMAPWorkMode_Type.__name__ = "Integer32"
_Hh3cDot11RRMAPWorkMode_Object = MibTableColumn
hh3cDot11RRMAPWorkMode = _Hh3cDot11RRMAPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 3, 1, 1),
    _Hh3cDot11RRMAPWorkMode_Type()
)
hh3cDot11RRMAPWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMAPWorkMode.setStatus("current")
_Hh3cDot11RRMSDRadioGroupTable_Object = MibTable
hh3cDot11RRMSDRadioGroupTable = _Hh3cDot11RRMSDRadioGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRadioGroupTable.setStatus("current")
_Hh3cDot11RRMSDRadioGroupEntry_Object = MibTableRow
hh3cDot11RRMSDRadioGroupEntry = _Hh3cDot11RRMSDRadioGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 4, 1)
)
hh3cDot11RRMSDRadioGroupEntry.setIndexNames(
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMSDRadioGroupId"),
)
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRadioGroupEntry.setStatus("current")
_Hh3cDot11RRMSDRadioGroupId_Type = Unsigned32
_Hh3cDot11RRMSDRadioGroupId_Object = MibTableColumn
hh3cDot11RRMSDRadioGroupId = _Hh3cDot11RRMSDRadioGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 4, 1, 1),
    _Hh3cDot11RRMSDRadioGroupId_Type()
)
hh3cDot11RRMSDRadioGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRadioGroupId.setStatus("current")
_Hh3cDot11RRMSDRadioGroupDesc_Type = OctetString
_Hh3cDot11RRMSDRadioGroupDesc_Object = MibTableColumn
hh3cDot11RRMSDRadioGroupDesc = _Hh3cDot11RRMSDRadioGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 4, 1, 2),
    _Hh3cDot11RRMSDRadioGroupDesc_Type()
)
hh3cDot11RRMSDRadioGroupDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRadioGroupDesc.setStatus("current")
_Hh3cDot11RRMSDRdGrpChlHolddownTm_Type = Unsigned32
_Hh3cDot11RRMSDRdGrpChlHolddownTm_Object = MibTableColumn
hh3cDot11RRMSDRdGrpChlHolddownTm = _Hh3cDot11RRMSDRdGrpChlHolddownTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 4, 1, 3),
    _Hh3cDot11RRMSDRdGrpChlHolddownTm_Type()
)
hh3cDot11RRMSDRdGrpChlHolddownTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRdGrpChlHolddownTm.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRdGrpChlHolddownTm.setUnits("minute")
_Hh3cDot11RRMSDRdGrpPwrHolddownTm_Type = Unsigned32
_Hh3cDot11RRMSDRdGrpPwrHolddownTm_Object = MibTableColumn
hh3cDot11RRMSDRdGrpPwrHolddownTm = _Hh3cDot11RRMSDRdGrpPwrHolddownTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 4, 1, 4),
    _Hh3cDot11RRMSDRdGrpPwrHolddownTm_Type()
)
hh3cDot11RRMSDRdGrpPwrHolddownTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRdGrpPwrHolddownTm.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRdGrpPwrHolddownTm.setUnits("minute")
_Hh3cDot11RRMSDRdGroupRowStatus_Type = RowStatus
_Hh3cDot11RRMSDRdGroupRowStatus_Object = MibTableColumn
hh3cDot11RRMSDRdGroupRowStatus = _Hh3cDot11RRMSDRdGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 4, 1, 5),
    _Hh3cDot11RRMSDRdGroupRowStatus_Type()
)
hh3cDot11RRMSDRdGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RRMSDRdGroupRowStatus.setStatus("current")
_Hh3cDot11RRMAPCfg2Table_Object = MibTable
hh3cDot11RRMAPCfg2Table = _Hh3cDot11RRMAPCfg2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11RRMAPCfg2Table.setStatus("current")
_Hh3cDot11RRMAPCfg2Entry_Object = MibTableRow
hh3cDot11RRMAPCfg2Entry = _Hh3cDot11RRMAPCfg2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 5, 1)
)
hh3cDot11RRMAPCfg2Entry.setIndexNames(
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RRMAPCfg2Entry.setStatus("current")
_Hh3cDot11RRMAPSerialID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11RRMAPSerialID_Object = MibTableColumn
hh3cDot11RRMAPSerialID = _Hh3cDot11RRMAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 5, 1, 1),
    _Hh3cDot11RRMAPSerialID_Type()
)
hh3cDot11RRMAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RRMAPSerialID.setStatus("current")
_Hh3cDot11RRMAPIntfThreshold_Type = Integer32
_Hh3cDot11RRMAPIntfThreshold_Object = MibTableColumn
hh3cDot11RRMAPIntfThreshold = _Hh3cDot11RRMAPIntfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 5, 1, 2),
    _Hh3cDot11RRMAPIntfThreshold_Type()
)
hh3cDot11RRMAPIntfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMAPIntfThreshold.setStatus("current")
_Hh3cDot11RRMStaIntfThreshold_Type = Integer32
_Hh3cDot11RRMStaIntfThreshold_Object = MibTableColumn
hh3cDot11RRMStaIntfThreshold = _Hh3cDot11RRMStaIntfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 5, 1, 3),
    _Hh3cDot11RRMStaIntfThreshold_Type()
)
hh3cDot11RRMStaIntfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMStaIntfThreshold.setStatus("current")
_Hh3cDot11RRMCoChlIntfTrapThhd_Type = Integer32
_Hh3cDot11RRMCoChlIntfTrapThhd_Object = MibTableColumn
hh3cDot11RRMCoChlIntfTrapThhd = _Hh3cDot11RRMCoChlIntfTrapThhd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 5, 1, 4),
    _Hh3cDot11RRMCoChlIntfTrapThhd_Type()
)
hh3cDot11RRMCoChlIntfTrapThhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMCoChlIntfTrapThhd.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMCoChlIntfTrapThhd.setUnits("dbm")
_Hh3cDot11RRMAdjChlIntfTrapThhd_Type = Integer32
_Hh3cDot11RRMAdjChlIntfTrapThhd_Object = MibTableColumn
hh3cDot11RRMAdjChlIntfTrapThhd = _Hh3cDot11RRMAdjChlIntfTrapThhd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 1, 5, 1, 5),
    _Hh3cDot11RRMAdjChlIntfTrapThhd_Type()
)
hh3cDot11RRMAdjChlIntfTrapThhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMAdjChlIntfTrapThhd.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMAdjChlIntfTrapThhd.setUnits("dbm")
_Hh3cDot11RRMDetectGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RRMDetectGroup = _Hh3cDot11RRMDetectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2)
)
_Hh3cDot11RRMChlRptTable_Object = MibTable
hh3cDot11RRMChlRptTable = _Hh3cDot11RRMChlRptTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptTable.setStatus("current")
_Hh3cDot11RRMChlRptEntry_Object = MibTableRow
hh3cDot11RRMChlRptEntry = _Hh3cDot11RRMChlRptEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1)
)
hh3cDot11RRMChlRptEntry.setIndexNames(
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMRadioIndex"),
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMChlRptChlNum"),
)
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptEntry.setStatus("current")
_Hh3cDot11RRMRadioIndex_Type = Hh3cDot11RadioElementIndex
_Hh3cDot11RRMRadioIndex_Object = MibTableColumn
hh3cDot11RRMRadioIndex = _Hh3cDot11RRMRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 1),
    _Hh3cDot11RRMRadioIndex_Type()
)
hh3cDot11RRMRadioIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11RRMRadioIndex.setStatus("current")
_Hh3cDot11RRMChlRptChlNum_Type = Integer32
_Hh3cDot11RRMChlRptChlNum_Object = MibTableColumn
hh3cDot11RRMChlRptChlNum = _Hh3cDot11RRMChlRptChlNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 2),
    _Hh3cDot11RRMChlRptChlNum_Type()
)
hh3cDot11RRMChlRptChlNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptChlNum.setStatus("current")


class _Hh3cDot11RRMChlRptChlType_Type(Integer32):
    """Custom type hh3cDot11RRMChlRptChlType based on Integer32"""
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


_Hh3cDot11RRMChlRptChlType_Type.__name__ = "Integer32"
_Hh3cDot11RRMChlRptChlType_Object = MibTableColumn
hh3cDot11RRMChlRptChlType = _Hh3cDot11RRMChlRptChlType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 3),
    _Hh3cDot11RRMChlRptChlType_Type()
)
hh3cDot11RRMChlRptChlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptChlType.setStatus("current")


class _Hh3cDot11RRMChlRptChlQlty_Type(Integer32):
    """Custom type hh3cDot11RRMChlRptChlQlty based on Integer32"""
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


_Hh3cDot11RRMChlRptChlQlty_Type.__name__ = "Integer32"
_Hh3cDot11RRMChlRptChlQlty_Object = MibTableColumn
hh3cDot11RRMChlRptChlQlty = _Hh3cDot11RRMChlRptChlQlty_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 4),
    _Hh3cDot11RRMChlRptChlQlty_Type()
)
hh3cDot11RRMChlRptChlQlty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptChlQlty.setStatus("current")
_Hh3cDot11RRMChlRptNbrCnt_Type = Integer32
_Hh3cDot11RRMChlRptNbrCnt_Object = MibTableColumn
hh3cDot11RRMChlRptNbrCnt = _Hh3cDot11RRMChlRptNbrCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 5),
    _Hh3cDot11RRMChlRptNbrCnt_Type()
)
hh3cDot11RRMChlRptNbrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptNbrCnt.setStatus("current")


class _Hh3cDot11RRMChlRptLoad_Type(Integer32):
    """Custom type hh3cDot11RRMChlRptLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMChlRptLoad_Type.__name__ = "Integer32"
_Hh3cDot11RRMChlRptLoad_Object = MibTableColumn
hh3cDot11RRMChlRptLoad = _Hh3cDot11RRMChlRptLoad_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 6),
    _Hh3cDot11RRMChlRptLoad_Type()
)
hh3cDot11RRMChlRptLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptLoad.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptLoad.setUnits("percent")


class _Hh3cDot11RRMChlRptUtlz_Type(Integer32):
    """Custom type hh3cDot11RRMChlRptUtlz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMChlRptUtlz_Type.__name__ = "Integer32"
_Hh3cDot11RRMChlRptUtlz_Object = MibTableColumn
hh3cDot11RRMChlRptUtlz = _Hh3cDot11RRMChlRptUtlz_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 7),
    _Hh3cDot11RRMChlRptUtlz_Type()
)
hh3cDot11RRMChlRptUtlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptUtlz.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptUtlz.setUnits("percent")


class _Hh3cDot11RRMChlRptIntrf_Type(Integer32):
    """Custom type hh3cDot11RRMChlRptIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMChlRptIntrf_Type.__name__ = "Integer32"
_Hh3cDot11RRMChlRptIntrf_Object = MibTableColumn
hh3cDot11RRMChlRptIntrf = _Hh3cDot11RRMChlRptIntrf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 8),
    _Hh3cDot11RRMChlRptIntrf_Type()
)
hh3cDot11RRMChlRptIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptIntrf.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptIntrf.setUnits("percent")


class _Hh3cDot11RRMChlRptPER_Type(Integer32):
    """Custom type hh3cDot11RRMChlRptPER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMChlRptPER_Type.__name__ = "Integer32"
_Hh3cDot11RRMChlRptPER_Object = MibTableColumn
hh3cDot11RRMChlRptPER = _Hh3cDot11RRMChlRptPER_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 9),
    _Hh3cDot11RRMChlRptPER_Type()
)
hh3cDot11RRMChlRptPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptPER.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptPER.setUnits("percent")


class _Hh3cDot11RRMChlRptRetryRate_Type(Integer32):
    """Custom type hh3cDot11RRMChlRptRetryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMChlRptRetryRate_Type.__name__ = "Integer32"
_Hh3cDot11RRMChlRptRetryRate_Object = MibTableColumn
hh3cDot11RRMChlRptRetryRate = _Hh3cDot11RRMChlRptRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 10),
    _Hh3cDot11RRMChlRptRetryRate_Type()
)
hh3cDot11RRMChlRptRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptRetryRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptRetryRate.setUnits("percent")
_Hh3cDot11RRMChlRptNoise_Type = Integer32
_Hh3cDot11RRMChlRptNoise_Object = MibTableColumn
hh3cDot11RRMChlRptNoise = _Hh3cDot11RRMChlRptNoise_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 11),
    _Hh3cDot11RRMChlRptNoise_Type()
)
hh3cDot11RRMChlRptNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptNoise.setStatus("current")


class _Hh3cDot11RRMChlRptRadarIndtcr_Type(Integer32):
    """Custom type hh3cDot11RRMChlRptRadarIndtcr based on Integer32"""
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


_Hh3cDot11RRMChlRptRadarIndtcr_Type.__name__ = "Integer32"
_Hh3cDot11RRMChlRptRadarIndtcr_Object = MibTableColumn
hh3cDot11RRMChlRptRadarIndtcr = _Hh3cDot11RRMChlRptRadarIndtcr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 1, 1, 12),
    _Hh3cDot11RRMChlRptRadarIndtcr_Type()
)
hh3cDot11RRMChlRptRadarIndtcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RRMChlRptRadarIndtcr.setStatus("current")
_Hh3cDot11RRMNbrInfoTable_Object = MibTable
hh3cDot11RRMNbrInfoTable = _Hh3cDot11RRMNbrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RRMNbrInfoTable.setStatus("current")
_Hh3cDot11RRMNbrInfoEntry_Object = MibTableRow
hh3cDot11RRMNbrInfoEntry = _Hh3cDot11RRMNbrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 2, 1)
)
hh3cDot11RRMNbrInfoEntry.setIndexNames(
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMRadioIndex"),
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RrmNbrBSSID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RRMNbrInfoEntry.setStatus("current")
_Hh3cDot11RrmNbrBSSID_Type = MacAddress
_Hh3cDot11RrmNbrBSSID_Object = MibTableColumn
hh3cDot11RrmNbrBSSID = _Hh3cDot11RrmNbrBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 2, 1, 1),
    _Hh3cDot11RrmNbrBSSID_Type()
)
hh3cDot11RrmNbrBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RrmNbrBSSID.setStatus("current")
_Hh3cDot11RrmNbrChl_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11RrmNbrChl_Object = MibTableColumn
hh3cDot11RrmNbrChl = _Hh3cDot11RrmNbrChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 2, 1, 2),
    _Hh3cDot11RrmNbrChl_Type()
)
hh3cDot11RrmNbrChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RrmNbrChl.setStatus("current")


class _Hh3cDot11RRMNbrIntrf_Type(Integer32):
    """Custom type hh3cDot11RRMNbrIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMNbrIntrf_Type.__name__ = "Integer32"
_Hh3cDot11RRMNbrIntrf_Object = MibTableColumn
hh3cDot11RRMNbrIntrf = _Hh3cDot11RRMNbrIntrf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 2, 1, 3),
    _Hh3cDot11RRMNbrIntrf_Type()
)
hh3cDot11RRMNbrIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMNbrIntrf.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMNbrIntrf.setUnits("percent")
_Hh3cDot11RrmNbrRSSI_Type = Integer32
_Hh3cDot11RrmNbrRSSI_Object = MibTableColumn
hh3cDot11RrmNbrRSSI = _Hh3cDot11RrmNbrRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 2, 1, 4),
    _Hh3cDot11RrmNbrRSSI_Type()
)
hh3cDot11RrmNbrRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RrmNbrRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RrmNbrRSSI.setUnits("dBm")


class _Hh3cDot11RrmNbrType_Type(Integer32):
    """Custom type hh3cDot11RrmNbrType based on Integer32"""
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


_Hh3cDot11RrmNbrType_Type.__name__ = "Integer32"
_Hh3cDot11RrmNbrType_Object = MibTableColumn
hh3cDot11RrmNbrType = _Hh3cDot11RrmNbrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 2, 1, 5),
    _Hh3cDot11RrmNbrType_Type()
)
hh3cDot11RrmNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RrmNbrType.setStatus("current")
_Hh3cDot11RrmNbrSSID_Type = Hh3cDot11SSIDStringType
_Hh3cDot11RrmNbrSSID_Object = MibTableColumn
hh3cDot11RrmNbrSSID = _Hh3cDot11RrmNbrSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 2, 1, 6),
    _Hh3cDot11RrmNbrSSID_Type()
)
hh3cDot11RrmNbrSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RrmNbrSSID.setStatus("current")
_Hh3cDot11RRMHistoryTable_Object = MibTable
hh3cDot11RRMHistoryTable = _Hh3cDot11RRMHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryTable.setStatus("current")
_Hh3cDot11RRMHistoryEntry_Object = MibTableRow
hh3cDot11RRMHistoryEntry = _Hh3cDot11RRMHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1)
)
hh3cDot11RRMHistoryEntry.setIndexNames(
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMRadioIndex"),
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMHistoryId"),
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11RRMHistoryRecIndctr"),
)
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryEntry.setStatus("current")
_Hh3cDot11RRMHistoryId_Type = Integer32
_Hh3cDot11RRMHistoryId_Object = MibTableColumn
hh3cDot11RRMHistoryId = _Hh3cDot11RRMHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 1),
    _Hh3cDot11RRMHistoryId_Type()
)
hh3cDot11RRMHistoryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryId.setStatus("current")


class _Hh3cDot11RRMHistoryRecIndctr_Type(Integer32):
    """Custom type hh3cDot11RRMHistoryRecIndctr based on Integer32"""
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


_Hh3cDot11RRMHistoryRecIndctr_Type.__name__ = "Integer32"
_Hh3cDot11RRMHistoryRecIndctr_Object = MibTableColumn
hh3cDot11RRMHistoryRecIndctr = _Hh3cDot11RRMHistoryRecIndctr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 2),
    _Hh3cDot11RRMHistoryRecIndctr_Type()
)
hh3cDot11RRMHistoryRecIndctr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryRecIndctr.setStatus("current")
_Hh3cDot11RRMHistoryChl_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11RRMHistoryChl_Object = MibTableColumn
hh3cDot11RRMHistoryChl = _Hh3cDot11RRMHistoryChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 3),
    _Hh3cDot11RRMHistoryChl_Type()
)
hh3cDot11RRMHistoryChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryChl.setStatus("current")
_Hh3cDot11RRMHistoryPwr_Type = Integer32
_Hh3cDot11RRMHistoryPwr_Object = MibTableColumn
hh3cDot11RRMHistoryPwr = _Hh3cDot11RRMHistoryPwr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 4),
    _Hh3cDot11RRMHistoryPwr_Type()
)
hh3cDot11RRMHistoryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryPwr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryPwr.setUnits("dBm")


class _Hh3cDot11RRMHistoryLoad_Type(Integer32):
    """Custom type hh3cDot11RRMHistoryLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMHistoryLoad_Type.__name__ = "Integer32"
_Hh3cDot11RRMHistoryLoad_Object = MibTableColumn
hh3cDot11RRMHistoryLoad = _Hh3cDot11RRMHistoryLoad_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 5),
    _Hh3cDot11RRMHistoryLoad_Type()
)
hh3cDot11RRMHistoryLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryLoad.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryLoad.setUnits("percent")


class _Hh3cDot11RRMHistoryUtlz_Type(Integer32):
    """Custom type hh3cDot11RRMHistoryUtlz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMHistoryUtlz_Type.__name__ = "Integer32"
_Hh3cDot11RRMHistoryUtlz_Object = MibTableColumn
hh3cDot11RRMHistoryUtlz = _Hh3cDot11RRMHistoryUtlz_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 6),
    _Hh3cDot11RRMHistoryUtlz_Type()
)
hh3cDot11RRMHistoryUtlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryUtlz.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryUtlz.setUnits("percent")


class _Hh3cDot11RRMHistoryIntrf_Type(Integer32):
    """Custom type hh3cDot11RRMHistoryIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMHistoryIntrf_Type.__name__ = "Integer32"
_Hh3cDot11RRMHistoryIntrf_Object = MibTableColumn
hh3cDot11RRMHistoryIntrf = _Hh3cDot11RRMHistoryIntrf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 7),
    _Hh3cDot11RRMHistoryIntrf_Type()
)
hh3cDot11RRMHistoryIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryIntrf.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryIntrf.setUnits("percent")
_Hh3cDot11RRMHistoryNoise_Type = Integer32
_Hh3cDot11RRMHistoryNoise_Object = MibTableColumn
hh3cDot11RRMHistoryNoise = _Hh3cDot11RRMHistoryNoise_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 8),
    _Hh3cDot11RRMHistoryNoise_Type()
)
hh3cDot11RRMHistoryNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryNoise.setStatus("current")


class _Hh3cDot11RRMHistoryPER_Type(Integer32):
    """Custom type hh3cDot11RRMHistoryPER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMHistoryPER_Type.__name__ = "Integer32"
_Hh3cDot11RRMHistoryPER_Object = MibTableColumn
hh3cDot11RRMHistoryPER = _Hh3cDot11RRMHistoryPER_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 9),
    _Hh3cDot11RRMHistoryPER_Type()
)
hh3cDot11RRMHistoryPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryPER.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryPER.setUnits("percent")


class _Hh3cDot11RRMHistoryRetryRate_Type(Integer32):
    """Custom type hh3cDot11RRMHistoryRetryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11RRMHistoryRetryRate_Type.__name__ = "Integer32"
_Hh3cDot11RRMHistoryRetryRate_Object = MibTableColumn
hh3cDot11RRMHistoryRetryRate = _Hh3cDot11RRMHistoryRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 10),
    _Hh3cDot11RRMHistoryRetryRate_Type()
)
hh3cDot11RRMHistoryRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryRetryRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryRetryRate.setUnits("percent")


class _Hh3cDot11RRMHistoryChgReason_Type(Bits):
    """Custom type hh3cDot11RRMHistoryChgReason based on Bits"""
    namedValues = NamedValues(
        *(("coverage", 1),
          ("interference", 5),
          ("others", 0),
          ("packetsDiscarded", 4),
          ("radar", 2),
          ("retransmission", 3))
    )

_Hh3cDot11RRMHistoryChgReason_Type.__name__ = "Bits"
_Hh3cDot11RRMHistoryChgReason_Object = MibTableColumn
hh3cDot11RRMHistoryChgReason = _Hh3cDot11RRMHistoryChgReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 11),
    _Hh3cDot11RRMHistoryChgReason_Type()
)
hh3cDot11RRMHistoryChgReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryChgReason.setStatus("current")
_Hh3cDot11RRMHistoryChgDateTime_Type = DateAndTime
_Hh3cDot11RRMHistoryChgDateTime_Object = MibTableColumn
hh3cDot11RRMHistoryChgDateTime = _Hh3cDot11RRMHistoryChgDateTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 2, 3, 1, 12),
    _Hh3cDot11RRMHistoryChgDateTime_Type()
)
hh3cDot11RRMHistoryChgDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RRMHistoryChgDateTime.setStatus("current")
_Hh3cDot11RRMNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RRMNotifyGroup = _Hh3cDot11RRMNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3)
)
_Hh3cDot11RRMChlQltyNotifications_ObjectIdentity = ObjectIdentity
hh3cDot11RRMChlQltyNotifications = _Hh3cDot11RRMChlQltyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 1)
)
_Hh3cDot11RRMChlQltyNtfPrefix_ObjectIdentity = ObjectIdentity
hh3cDot11RRMChlQltyNtfPrefix = _Hh3cDot11RRMChlQltyNtfPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 1, 0)
)
_Hh3cDot11RRMResChgNotifications_ObjectIdentity = ObjectIdentity
hh3cDot11RRMResChgNotifications = _Hh3cDot11RRMResChgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 2)
)
_Hh3cDot11RRMResChgNtfPrefix_ObjectIdentity = ObjectIdentity
hh3cDot11RRMResChgNtfPrefix = _Hh3cDot11RRMResChgNtfPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 2, 0)
)
_Hh3cDot11RRMNotificationsVar_ObjectIdentity = ObjectIdentity
hh3cDot11RRMNotificationsVar = _Hh3cDot11RRMNotificationsVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 3)
)
_Hh3cDot11NewPower_Type = Integer32
_Hh3cDot11NewPower_Object = MibScalar
hh3cDot11NewPower = _Hh3cDot11NewPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 3, 1),
    _Hh3cDot11NewPower_Type()
)
hh3cDot11NewPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11NewPower.setStatus("current")
_Hh3cDot11OldPower_Type = Integer32
_Hh3cDot11OldPower_Object = MibScalar
hh3cDot11OldPower = _Hh3cDot11OldPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 3, 2),
    _Hh3cDot11OldPower_Type()
)
hh3cDot11OldPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11OldPower.setStatus("current")
_Hh3cDot11MonitorDetectedGroup_ObjectIdentity = ObjectIdentity
hh3cDot11MonitorDetectedGroup = _Hh3cDot11MonitorDetectedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4)
)
_Hh3cDot11MonitorDetectedDevTable_Object = MibTable
hh3cDot11MonitorDetectedDevTable = _Hh3cDot11MonitorDetectedDevTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11MonitorDetectedDevTable.setStatus("current")
_Hh3cDot11MonitorDetectedDevEntry_Object = MibTableRow
hh3cDot11MonitorDetectedDevEntry = _Hh3cDot11MonitorDetectedDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1)
)
hh3cDot11MonitorDetectedDevEntry.setIndexNames(
    (0, "HH3C-DOT11-RRM-MIB", "hh3cDot11MonitorDevMAC"),
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11MonitorDetectedDevEntry.setStatus("current")
_Hh3cDot11MonitorDevMAC_Type = MacAddress
_Hh3cDot11MonitorDevMAC_Object = MibTableColumn
hh3cDot11MonitorDevMAC = _Hh3cDot11MonitorDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 1),
    _Hh3cDot11MonitorDevMAC_Type()
)
hh3cDot11MonitorDevMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevMAC.setStatus("current")


class _Hh3cDot11MonitorDevType_Type(Integer32):
    """Custom type hh3cDot11MonitorDevType based on Integer32"""
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


_Hh3cDot11MonitorDevType_Type.__name__ = "Integer32"
_Hh3cDot11MonitorDevType_Object = MibTableColumn
hh3cDot11MonitorDevType = _Hh3cDot11MonitorDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 2),
    _Hh3cDot11MonitorDevType_Type()
)
hh3cDot11MonitorDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevType.setStatus("current")
_Hh3cDot11MonitorDevVendor_Type = OctetString
_Hh3cDot11MonitorDevVendor_Object = MibTableColumn
hh3cDot11MonitorDevVendor = _Hh3cDot11MonitorDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 3),
    _Hh3cDot11MonitorDevVendor_Type()
)
hh3cDot11MonitorDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevVendor.setStatus("current")
_Hh3cDot11MonitorDevSSID_Type = OctetString
_Hh3cDot11MonitorDevSSID_Object = MibTableColumn
hh3cDot11MonitorDevSSID = _Hh3cDot11MonitorDevSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 4),
    _Hh3cDot11MonitorDevSSID_Type()
)
hh3cDot11MonitorDevSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevSSID.setStatus("current")
_Hh3cDot11MonitorDevBSSID_Type = MacAddress
_Hh3cDot11MonitorDevBSSID_Object = MibTableColumn
hh3cDot11MonitorDevBSSID = _Hh3cDot11MonitorDevBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 5),
    _Hh3cDot11MonitorDevBSSID_Type()
)
hh3cDot11MonitorDevBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevBSSID.setStatus("current")
_Hh3cDot11MonitorDevChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11MonitorDevChannel_Object = MibTableColumn
hh3cDot11MonitorDevChannel = _Hh3cDot11MonitorDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 6),
    _Hh3cDot11MonitorDevChannel_Type()
)
hh3cDot11MonitorDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevChannel.setStatus("current")
_Hh3cDot11MonitorRadioId_Type = Hh3cDot11RadioScopeType
_Hh3cDot11MonitorRadioId_Object = MibTableColumn
hh3cDot11MonitorRadioId = _Hh3cDot11MonitorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 7),
    _Hh3cDot11MonitorRadioId_Type()
)
hh3cDot11MonitorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorRadioId.setStatus("current")
_Hh3cDot11MonitorDevMaxRSSI_Type = Integer32
_Hh3cDot11MonitorDevMaxRSSI_Object = MibTableColumn
hh3cDot11MonitorDevMaxRSSI = _Hh3cDot11MonitorDevMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 8),
    _Hh3cDot11MonitorDevMaxRSSI_Type()
)
hh3cDot11MonitorDevMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevMaxRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevMaxRSSI.setUnits("dbm")
_Hh3cDot11MonitorDevBeaconIntvl_Type = Integer32
_Hh3cDot11MonitorDevBeaconIntvl_Object = MibTableColumn
hh3cDot11MonitorDevBeaconIntvl = _Hh3cDot11MonitorDevBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 9),
    _Hh3cDot11MonitorDevBeaconIntvl_Type()
)
hh3cDot11MonitorDevBeaconIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevBeaconIntvl.setUnits("millisecond")
_Hh3cDot11MonitorDevFstDctTime_Type = DateAndTime
_Hh3cDot11MonitorDevFstDctTime_Object = MibTableColumn
hh3cDot11MonitorDevFstDctTime = _Hh3cDot11MonitorDevFstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 10),
    _Hh3cDot11MonitorDevFstDctTime_Type()
)
hh3cDot11MonitorDevFstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevFstDctTime.setStatus("current")
_Hh3cDot11MonitorDevLstDctTime_Type = DateAndTime
_Hh3cDot11MonitorDevLstDctTime_Object = MibTableColumn
hh3cDot11MonitorDevLstDctTime = _Hh3cDot11MonitorDevLstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 11),
    _Hh3cDot11MonitorDevLstDctTime_Type()
)
hh3cDot11MonitorDevLstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevLstDctTime.setStatus("current")
_Hh3cDot11MonitorDevClear_Type = TruthValue
_Hh3cDot11MonitorDevClear_Object = MibTableColumn
hh3cDot11MonitorDevClear = _Hh3cDot11MonitorDevClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 12),
    _Hh3cDot11MonitorDevClear_Type()
)
hh3cDot11MonitorDevClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevClear.setStatus("current")
_Hh3cDot11MonitorDevSNR_Type = Integer32
_Hh3cDot11MonitorDevSNR_Object = MibTableColumn
hh3cDot11MonitorDevSNR = _Hh3cDot11MonitorDevSNR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 4, 1, 1, 13),
    _Hh3cDot11MonitorDevSNR_Type()
)
hh3cDot11MonitorDevSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MonitorDevSNR.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11RRMIntrfLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 1, 0, 1)
)
hh3cDot11RRMIntrfLimit.setObjects(
    ("HH3C-DOT11-RRM-MIB", "hh3cDot11RRMChlRptIntrf")
)
if mibBuilder.loadTexts:
    hh3cDot11RRMIntrfLimit.setStatus(
        "current"
    )

hh3cDot11RRMPERLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 1, 0, 2)
)
hh3cDot11RRMPERLimit.setObjects(
    ("HH3C-DOT11-RRM-MIB", "hh3cDot11RRMChlRptPER")
)
if mibBuilder.loadTexts:
    hh3cDot11RRMPERLimit.setStatus(
        "current"
    )

hh3cDot11RRMNoiseLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 1, 0, 3)
)
hh3cDot11RRMNoiseLimit.setObjects(
    ("HH3C-DOT11-RRM-MIB", "hh3cDot11RRMChlRptNoise")
)
if mibBuilder.loadTexts:
    hh3cDot11RRMNoiseLimit.setStatus(
        "current"
    )

hh3cDot11RRMPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 8, 3, 2, 0, 1)
)
hh3cDot11RRMPowerChange.setObjects(
      *(("HH3C-DOT11-RRM-MIB", "hh3cDot11RRMRadioIndex"),
        ("HH3C-DOT11-RRM-MIB", "hh3cDot11NewPower"),
        ("HH3C-DOT11-RRM-MIB", "hh3cDot11OldPower"))
)
if mibBuilder.loadTexts:
    hh3cDot11RRMPowerChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-RRM-MIB",
    **{"hh3cDot11RRM": hh3cDot11RRM,
       "hh3cDot11RRMConfigGroup": hh3cDot11RRMConfigGroup,
       "hh3cDot11RRMGlobalCfgPara": hh3cDot11RRMGlobalCfgPara,
       "hh3cDot11RRM11nMadtMaxMcs": hh3cDot11RRM11nMadtMaxMcs,
       "hh3cDot11RRM11nSuptMaxMcs": hh3cDot11RRM11nSuptMaxMcs,
       "hh3cDot11RRM11gProtect": hh3cDot11RRM11gProtect,
       "hh3cDot11RRM11aPwrConstrt": hh3cDot11RRM11aPwrConstrt,
       "hh3cDot11RRM11aSpectrumManag": hh3cDot11RRM11aSpectrumManag,
       "hh3cDot11RRMAutoChlAvoid11h": hh3cDot11RRMAutoChlAvoid11h,
       "hh3cDot11RRMScanChl": hh3cDot11RRMScanChl,
       "hh3cDot11RRMScanRptIntvel": hh3cDot11RRMScanRptIntvel,
       "hh3cDot11APInterfNumThreshhd": hh3cDot11APInterfNumThreshhd,
       "hh3cDot11StaInterfNumThreshhd": hh3cDot11StaInterfNumThreshhd,
       "hh3cDot11RRMRadioCfgTable": hh3cDot11RRMRadioCfgTable,
       "hh3cDot11RRMRadioCfgEntry": hh3cDot11RRMRadioCfgEntry,
       "hh3cDot11RRMRadioType": hh3cDot11RRMRadioType,
       "hh3cDot11RRMCfgChlState": hh3cDot11RRMCfgChlState,
       "hh3cDot11RRMCfgChlMode": hh3cDot11RRMCfgChlMode,
       "hh3cDot11RRMChlProntoRadioElmt": hh3cDot11RRMChlProntoRadioElmt,
       "hh3cDot11RRMCfgPwrState": hh3cDot11RRMCfgPwrState,
       "hh3cDot11RRMCfgPwrMode": hh3cDot11RRMCfgPwrMode,
       "hh3cDot11RRMPwrProntoRadioElmt": hh3cDot11RRMPwrProntoRadioElmt,
       "hh3cDot11RRMCfgIntrvl": hh3cDot11RRMCfgIntrvl,
       "hh3cDot11RRMCfgIntrfThres": hh3cDot11RRMCfgIntrfThres,
       "hh3cDot11RRMCfgNoiseThres": hh3cDot11RRMCfgNoiseThres,
       "hh3cDot11RRMCfgPERThres": hh3cDot11RRMCfgPERThres,
       "hh3cDot11RRMCfgToleranceFctr": hh3cDot11RRMCfgToleranceFctr,
       "hh3cDot11RRMCfgAdjacencyFctr": hh3cDot11RRMCfgAdjacencyFctr,
       "hh3cDot11RRMAPCfgTable": hh3cDot11RRMAPCfgTable,
       "hh3cDot11RRMAPCfgEntry": hh3cDot11RRMAPCfgEntry,
       "hh3cDot11RRMAPWorkMode": hh3cDot11RRMAPWorkMode,
       "hh3cDot11RRMSDRadioGroupTable": hh3cDot11RRMSDRadioGroupTable,
       "hh3cDot11RRMSDRadioGroupEntry": hh3cDot11RRMSDRadioGroupEntry,
       "hh3cDot11RRMSDRadioGroupId": hh3cDot11RRMSDRadioGroupId,
       "hh3cDot11RRMSDRadioGroupDesc": hh3cDot11RRMSDRadioGroupDesc,
       "hh3cDot11RRMSDRdGrpChlHolddownTm": hh3cDot11RRMSDRdGrpChlHolddownTm,
       "hh3cDot11RRMSDRdGrpPwrHolddownTm": hh3cDot11RRMSDRdGrpPwrHolddownTm,
       "hh3cDot11RRMSDRdGroupRowStatus": hh3cDot11RRMSDRdGroupRowStatus,
       "hh3cDot11RRMAPCfg2Table": hh3cDot11RRMAPCfg2Table,
       "hh3cDot11RRMAPCfg2Entry": hh3cDot11RRMAPCfg2Entry,
       "hh3cDot11RRMAPSerialID": hh3cDot11RRMAPSerialID,
       "hh3cDot11RRMAPIntfThreshold": hh3cDot11RRMAPIntfThreshold,
       "hh3cDot11RRMStaIntfThreshold": hh3cDot11RRMStaIntfThreshold,
       "hh3cDot11RRMCoChlIntfTrapThhd": hh3cDot11RRMCoChlIntfTrapThhd,
       "hh3cDot11RRMAdjChlIntfTrapThhd": hh3cDot11RRMAdjChlIntfTrapThhd,
       "hh3cDot11RRMDetectGroup": hh3cDot11RRMDetectGroup,
       "hh3cDot11RRMChlRptTable": hh3cDot11RRMChlRptTable,
       "hh3cDot11RRMChlRptEntry": hh3cDot11RRMChlRptEntry,
       "hh3cDot11RRMRadioIndex": hh3cDot11RRMRadioIndex,
       "hh3cDot11RRMChlRptChlNum": hh3cDot11RRMChlRptChlNum,
       "hh3cDot11RRMChlRptChlType": hh3cDot11RRMChlRptChlType,
       "hh3cDot11RRMChlRptChlQlty": hh3cDot11RRMChlRptChlQlty,
       "hh3cDot11RRMChlRptNbrCnt": hh3cDot11RRMChlRptNbrCnt,
       "hh3cDot11RRMChlRptLoad": hh3cDot11RRMChlRptLoad,
       "hh3cDot11RRMChlRptUtlz": hh3cDot11RRMChlRptUtlz,
       "hh3cDot11RRMChlRptIntrf": hh3cDot11RRMChlRptIntrf,
       "hh3cDot11RRMChlRptPER": hh3cDot11RRMChlRptPER,
       "hh3cDot11RRMChlRptRetryRate": hh3cDot11RRMChlRptRetryRate,
       "hh3cDot11RRMChlRptNoise": hh3cDot11RRMChlRptNoise,
       "hh3cDot11RRMChlRptRadarIndtcr": hh3cDot11RRMChlRptRadarIndtcr,
       "hh3cDot11RRMNbrInfoTable": hh3cDot11RRMNbrInfoTable,
       "hh3cDot11RRMNbrInfoEntry": hh3cDot11RRMNbrInfoEntry,
       "hh3cDot11RrmNbrBSSID": hh3cDot11RrmNbrBSSID,
       "hh3cDot11RrmNbrChl": hh3cDot11RrmNbrChl,
       "hh3cDot11RRMNbrIntrf": hh3cDot11RRMNbrIntrf,
       "hh3cDot11RrmNbrRSSI": hh3cDot11RrmNbrRSSI,
       "hh3cDot11RrmNbrType": hh3cDot11RrmNbrType,
       "hh3cDot11RrmNbrSSID": hh3cDot11RrmNbrSSID,
       "hh3cDot11RRMHistoryTable": hh3cDot11RRMHistoryTable,
       "hh3cDot11RRMHistoryEntry": hh3cDot11RRMHistoryEntry,
       "hh3cDot11RRMHistoryId": hh3cDot11RRMHistoryId,
       "hh3cDot11RRMHistoryRecIndctr": hh3cDot11RRMHistoryRecIndctr,
       "hh3cDot11RRMHistoryChl": hh3cDot11RRMHistoryChl,
       "hh3cDot11RRMHistoryPwr": hh3cDot11RRMHistoryPwr,
       "hh3cDot11RRMHistoryLoad": hh3cDot11RRMHistoryLoad,
       "hh3cDot11RRMHistoryUtlz": hh3cDot11RRMHistoryUtlz,
       "hh3cDot11RRMHistoryIntrf": hh3cDot11RRMHistoryIntrf,
       "hh3cDot11RRMHistoryNoise": hh3cDot11RRMHistoryNoise,
       "hh3cDot11RRMHistoryPER": hh3cDot11RRMHistoryPER,
       "hh3cDot11RRMHistoryRetryRate": hh3cDot11RRMHistoryRetryRate,
       "hh3cDot11RRMHistoryChgReason": hh3cDot11RRMHistoryChgReason,
       "hh3cDot11RRMHistoryChgDateTime": hh3cDot11RRMHistoryChgDateTime,
       "hh3cDot11RRMNotifyGroup": hh3cDot11RRMNotifyGroup,
       "hh3cDot11RRMChlQltyNotifications": hh3cDot11RRMChlQltyNotifications,
       "hh3cDot11RRMChlQltyNtfPrefix": hh3cDot11RRMChlQltyNtfPrefix,
       "hh3cDot11RRMIntrfLimit": hh3cDot11RRMIntrfLimit,
       "hh3cDot11RRMPERLimit": hh3cDot11RRMPERLimit,
       "hh3cDot11RRMNoiseLimit": hh3cDot11RRMNoiseLimit,
       "hh3cDot11RRMResChgNotifications": hh3cDot11RRMResChgNotifications,
       "hh3cDot11RRMResChgNtfPrefix": hh3cDot11RRMResChgNtfPrefix,
       "hh3cDot11RRMPowerChange": hh3cDot11RRMPowerChange,
       "hh3cDot11RRMNotificationsVar": hh3cDot11RRMNotificationsVar,
       "hh3cDot11NewPower": hh3cDot11NewPower,
       "hh3cDot11OldPower": hh3cDot11OldPower,
       "hh3cDot11MonitorDetectedGroup": hh3cDot11MonitorDetectedGroup,
       "hh3cDot11MonitorDetectedDevTable": hh3cDot11MonitorDetectedDevTable,
       "hh3cDot11MonitorDetectedDevEntry": hh3cDot11MonitorDetectedDevEntry,
       "hh3cDot11MonitorDevMAC": hh3cDot11MonitorDevMAC,
       "hh3cDot11MonitorDevType": hh3cDot11MonitorDevType,
       "hh3cDot11MonitorDevVendor": hh3cDot11MonitorDevVendor,
       "hh3cDot11MonitorDevSSID": hh3cDot11MonitorDevSSID,
       "hh3cDot11MonitorDevBSSID": hh3cDot11MonitorDevBSSID,
       "hh3cDot11MonitorDevChannel": hh3cDot11MonitorDevChannel,
       "hh3cDot11MonitorRadioId": hh3cDot11MonitorRadioId,
       "hh3cDot11MonitorDevMaxRSSI": hh3cDot11MonitorDevMaxRSSI,
       "hh3cDot11MonitorDevBeaconIntvl": hh3cDot11MonitorDevBeaconIntvl,
       "hh3cDot11MonitorDevFstDctTime": hh3cDot11MonitorDevFstDctTime,
       "hh3cDot11MonitorDevLstDctTime": hh3cDot11MonitorDevLstDctTime,
       "hh3cDot11MonitorDevClear": hh3cDot11MonitorDevClear,
       "hh3cDot11MonitorDevSNR": hh3cDot11MonitorDevSNR}
)
