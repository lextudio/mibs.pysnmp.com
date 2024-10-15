# SNMP MIB module (H3C-DOT11-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-DOT11-RRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:14 2024
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

(H3cDot11ChannelScopeType,
 H3cDot11ObjectIDType,
 H3cDot11RadioElementIndex,
 H3cDot11RadioScopeType,
 H3cDot11RadioType,
 H3cDot11SSIDStringType,
 h3cDot11,
 h3cDot11APElementIndex) = mibBuilder.importSymbols(
    "H3C-DOT11-REF-MIB",
    "H3cDot11ChannelScopeType",
    "H3cDot11ObjectIDType",
    "H3cDot11RadioElementIndex",
    "H3cDot11RadioScopeType",
    "H3cDot11RadioType",
    "H3cDot11SSIDStringType",
    "h3cDot11",
    "h3cDot11APElementIndex")

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

h3cDot11RRM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8)
)
h3cDot11RRM.setRevisions(
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

_H3cDot11RRMConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11RRMConfigGroup = _H3cDot11RRMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1)
)
_H3cDot11RRMGlobalCfgPara_ObjectIdentity = ObjectIdentity
h3cDot11RRMGlobalCfgPara = _H3cDot11RRMGlobalCfgPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1)
)


class _H3cDot11RRM11nMadtMaxMcs_Type(Integer32):
    """Custom type h3cDot11RRM11nMadtMaxMcs based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
        ValueRangeConstraint(255, 255),
    )


_H3cDot11RRM11nMadtMaxMcs_Type.__name__ = "Integer32"
_H3cDot11RRM11nMadtMaxMcs_Object = MibScalar
h3cDot11RRM11nMadtMaxMcs = _H3cDot11RRM11nMadtMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 1),
    _H3cDot11RRM11nMadtMaxMcs_Type()
)
h3cDot11RRM11nMadtMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRM11nMadtMaxMcs.setStatus("current")


class _H3cDot11RRM11nSuptMaxMcs_Type(Integer32):
    """Custom type h3cDot11RRM11nSuptMaxMcs based on Integer32"""
    defaultValue = 76

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_H3cDot11RRM11nSuptMaxMcs_Type.__name__ = "Integer32"
_H3cDot11RRM11nSuptMaxMcs_Object = MibScalar
h3cDot11RRM11nSuptMaxMcs = _H3cDot11RRM11nSuptMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 2),
    _H3cDot11RRM11nSuptMaxMcs_Type()
)
h3cDot11RRM11nSuptMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRM11nSuptMaxMcs.setStatus("current")


class _H3cDot11RRM11gProtect_Type(TruthValue):
    """Custom type h3cDot11RRM11gProtect based on TruthValue"""


_H3cDot11RRM11gProtect_Object = MibScalar
h3cDot11RRM11gProtect = _H3cDot11RRM11gProtect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 3),
    _H3cDot11RRM11gProtect_Type()
)
h3cDot11RRM11gProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRM11gProtect.setStatus("current")


class _H3cDot11RRM11aPwrConstrt_Type(Integer32):
    """Custom type h3cDot11RRM11aPwrConstrt based on Integer32"""
    defaultValue = 0


_H3cDot11RRM11aPwrConstrt_Object = MibScalar
h3cDot11RRM11aPwrConstrt = _H3cDot11RRM11aPwrConstrt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 4),
    _H3cDot11RRM11aPwrConstrt_Type()
)
h3cDot11RRM11aPwrConstrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRM11aPwrConstrt.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRM11aPwrConstrt.setUnits("dBm")


class _H3cDot11RRM11aSpectrumManag_Type(TruthValue):
    """Custom type h3cDot11RRM11aSpectrumManag based on TruthValue"""


_H3cDot11RRM11aSpectrumManag_Object = MibScalar
h3cDot11RRM11aSpectrumManag = _H3cDot11RRM11aSpectrumManag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 5),
    _H3cDot11RRM11aSpectrumManag_Type()
)
h3cDot11RRM11aSpectrumManag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRM11aSpectrumManag.setStatus("current")


class _H3cDot11RRMAutoChlAvoid11h_Type(TruthValue):
    """Custom type h3cDot11RRMAutoChlAvoid11h based on TruthValue"""


_H3cDot11RRMAutoChlAvoid11h_Object = MibScalar
h3cDot11RRMAutoChlAvoid11h = _H3cDot11RRMAutoChlAvoid11h_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 6),
    _H3cDot11RRMAutoChlAvoid11h_Type()
)
h3cDot11RRMAutoChlAvoid11h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMAutoChlAvoid11h.setStatus("current")


class _H3cDot11RRMScanChl_Type(Integer32):
    """Custom type h3cDot11RRMScanChl based on Integer32"""
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


_H3cDot11RRMScanChl_Type.__name__ = "Integer32"
_H3cDot11RRMScanChl_Object = MibScalar
h3cDot11RRMScanChl = _H3cDot11RRMScanChl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 7),
    _H3cDot11RRMScanChl_Type()
)
h3cDot11RRMScanChl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMScanChl.setStatus("current")


class _H3cDot11RRMScanRptIntvel_Type(Integer32):
    """Custom type h3cDot11RRMScanRptIntvel based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_H3cDot11RRMScanRptIntvel_Type.__name__ = "Integer32"
_H3cDot11RRMScanRptIntvel_Object = MibScalar
h3cDot11RRMScanRptIntvel = _H3cDot11RRMScanRptIntvel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 8),
    _H3cDot11RRMScanRptIntvel_Type()
)
h3cDot11RRMScanRptIntvel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMScanRptIntvel.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMScanRptIntvel.setUnits("second")


class _H3cDot11APInterfNumThreshhd_Type(Integer32):
    """Custom type h3cDot11APInterfNumThreshhd based on Integer32"""
    defaultValue = 0


_H3cDot11APInterfNumThreshhd_Object = MibScalar
h3cDot11APInterfNumThreshhd = _H3cDot11APInterfNumThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 9),
    _H3cDot11APInterfNumThreshhd_Type()
)
h3cDot11APInterfNumThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APInterfNumThreshhd.setStatus("current")


class _H3cDot11StaInterfNumThreshhd_Type(Integer32):
    """Custom type h3cDot11StaInterfNumThreshhd based on Integer32"""
    defaultValue = 0


_H3cDot11StaInterfNumThreshhd_Object = MibScalar
h3cDot11StaInterfNumThreshhd = _H3cDot11StaInterfNumThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 1, 10),
    _H3cDot11StaInterfNumThreshhd_Type()
)
h3cDot11StaInterfNumThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StaInterfNumThreshhd.setStatus("current")
_H3cDot11RRMRadioCfgTable_Object = MibTable
h3cDot11RRMRadioCfgTable = _H3cDot11RRMRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot11RRMRadioCfgTable.setStatus("current")
_H3cDot11RRMRadioCfgEntry_Object = MibTableRow
h3cDot11RRMRadioCfgEntry = _H3cDot11RRMRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1)
)
h3cDot11RRMRadioCfgEntry.setIndexNames(
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMRadioType"),
)
if mibBuilder.loadTexts:
    h3cDot11RRMRadioCfgEntry.setStatus("current")
_H3cDot11RRMRadioType_Type = H3cDot11RadioType
_H3cDot11RRMRadioType_Object = MibTableColumn
h3cDot11RRMRadioType = _H3cDot11RRMRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 1),
    _H3cDot11RRMRadioType_Type()
)
h3cDot11RRMRadioType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RRMRadioType.setStatus("current")


class _H3cDot11RRMCfgChlState_Type(TruthValue):
    """Custom type h3cDot11RRMCfgChlState based on TruthValue"""


_H3cDot11RRMCfgChlState_Object = MibTableColumn
h3cDot11RRMCfgChlState = _H3cDot11RRMCfgChlState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 2),
    _H3cDot11RRMCfgChlState_Type()
)
h3cDot11RRMCfgChlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgChlState.setStatus("current")


class _H3cDot11RRMCfgChlMode_Type(Integer32):
    """Custom type h3cDot11RRMCfgChlMode based on Integer32"""
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


_H3cDot11RRMCfgChlMode_Type.__name__ = "Integer32"
_H3cDot11RRMCfgChlMode_Object = MibTableColumn
h3cDot11RRMCfgChlMode = _H3cDot11RRMCfgChlMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 3),
    _H3cDot11RRMCfgChlMode_Type()
)
h3cDot11RRMCfgChlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgChlMode.setStatus("current")


class _H3cDot11RRMChlProntoRadioElmt_Type(Unsigned32):
    """Custom type h3cDot11RRMChlProntoRadioElmt based on Unsigned32"""
    defaultValue = 0


_H3cDot11RRMChlProntoRadioElmt_Object = MibTableColumn
h3cDot11RRMChlProntoRadioElmt = _H3cDot11RRMChlProntoRadioElmt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 4),
    _H3cDot11RRMChlProntoRadioElmt_Type()
)
h3cDot11RRMChlProntoRadioElmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMChlProntoRadioElmt.setStatus("current")


class _H3cDot11RRMCfgPwrState_Type(TruthValue):
    """Custom type h3cDot11RRMCfgPwrState based on TruthValue"""


_H3cDot11RRMCfgPwrState_Object = MibTableColumn
h3cDot11RRMCfgPwrState = _H3cDot11RRMCfgPwrState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 5),
    _H3cDot11RRMCfgPwrState_Type()
)
h3cDot11RRMCfgPwrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgPwrState.setStatus("current")


class _H3cDot11RRMCfgPwrMode_Type(Integer32):
    """Custom type h3cDot11RRMCfgPwrMode based on Integer32"""
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


_H3cDot11RRMCfgPwrMode_Type.__name__ = "Integer32"
_H3cDot11RRMCfgPwrMode_Object = MibTableColumn
h3cDot11RRMCfgPwrMode = _H3cDot11RRMCfgPwrMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 6),
    _H3cDot11RRMCfgPwrMode_Type()
)
h3cDot11RRMCfgPwrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgPwrMode.setStatus("current")


class _H3cDot11RRMPwrProntoRadioElmt_Type(Unsigned32):
    """Custom type h3cDot11RRMPwrProntoRadioElmt based on Unsigned32"""
    defaultValue = 0


_H3cDot11RRMPwrProntoRadioElmt_Object = MibTableColumn
h3cDot11RRMPwrProntoRadioElmt = _H3cDot11RRMPwrProntoRadioElmt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 7),
    _H3cDot11RRMPwrProntoRadioElmt_Type()
)
h3cDot11RRMPwrProntoRadioElmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMPwrProntoRadioElmt.setStatus("current")


class _H3cDot11RRMCfgIntrvl_Type(Integer32):
    """Custom type h3cDot11RRMCfgIntrvl based on Integer32"""
    defaultValue = 8


_H3cDot11RRMCfgIntrvl_Object = MibTableColumn
h3cDot11RRMCfgIntrvl = _H3cDot11RRMCfgIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 8),
    _H3cDot11RRMCfgIntrvl_Type()
)
h3cDot11RRMCfgIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgIntrvl.setUnits("minute")


class _H3cDot11RRMCfgIntrfThres_Type(Integer32):
    """Custom type h3cDot11RRMCfgIntrfThres based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_H3cDot11RRMCfgIntrfThres_Type.__name__ = "Integer32"
_H3cDot11RRMCfgIntrfThres_Object = MibTableColumn
h3cDot11RRMCfgIntrfThres = _H3cDot11RRMCfgIntrfThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 9),
    _H3cDot11RRMCfgIntrfThres_Type()
)
h3cDot11RRMCfgIntrfThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgIntrfThres.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgIntrfThres.setUnits("percent")


class _H3cDot11RRMCfgNoiseThres_Type(Integer32):
    """Custom type h3cDot11RRMCfgNoiseThres based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_H3cDot11RRMCfgNoiseThres_Type.__name__ = "Integer32"
_H3cDot11RRMCfgNoiseThres_Object = MibTableColumn
h3cDot11RRMCfgNoiseThres = _H3cDot11RRMCfgNoiseThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 10),
    _H3cDot11RRMCfgNoiseThres_Type()
)
h3cDot11RRMCfgNoiseThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgNoiseThres.setStatus("current")


class _H3cDot11RRMCfgPERThres_Type(Integer32):
    """Custom type h3cDot11RRMCfgPERThres based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_H3cDot11RRMCfgPERThres_Type.__name__ = "Integer32"
_H3cDot11RRMCfgPERThres_Object = MibTableColumn
h3cDot11RRMCfgPERThres = _H3cDot11RRMCfgPERThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 11),
    _H3cDot11RRMCfgPERThres_Type()
)
h3cDot11RRMCfgPERThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgPERThres.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgPERThres.setUnits("percent")


class _H3cDot11RRMCfgToleranceFctr_Type(Integer32):
    """Custom type h3cDot11RRMCfgToleranceFctr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 45),
    )


_H3cDot11RRMCfgToleranceFctr_Type.__name__ = "Integer32"
_H3cDot11RRMCfgToleranceFctr_Object = MibTableColumn
h3cDot11RRMCfgToleranceFctr = _H3cDot11RRMCfgToleranceFctr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 12),
    _H3cDot11RRMCfgToleranceFctr_Type()
)
h3cDot11RRMCfgToleranceFctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgToleranceFctr.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgToleranceFctr.setUnits("percent")


class _H3cDot11RRMCfgAdjacencyFctr_Type(Integer32):
    """Custom type h3cDot11RRMCfgAdjacencyFctr based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cDot11RRMCfgAdjacencyFctr_Type.__name__ = "Integer32"
_H3cDot11RRMCfgAdjacencyFctr_Object = MibTableColumn
h3cDot11RRMCfgAdjacencyFctr = _H3cDot11RRMCfgAdjacencyFctr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 2, 1, 13),
    _H3cDot11RRMCfgAdjacencyFctr_Type()
)
h3cDot11RRMCfgAdjacencyFctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCfgAdjacencyFctr.setStatus("current")
_H3cDot11RRMAPCfgTable_Object = MibTable
h3cDot11RRMAPCfgTable = _H3cDot11RRMAPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDot11RRMAPCfgTable.setStatus("current")
_H3cDot11RRMAPCfgEntry_Object = MibTableRow
h3cDot11RRMAPCfgEntry = _H3cDot11RRMAPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 3, 1)
)
h3cDot11RRMAPCfgEntry.setIndexNames(
    (0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11RRMAPCfgEntry.setStatus("current")


class _H3cDot11RRMAPWorkMode_Type(Integer32):
    """Custom type h3cDot11RRMAPWorkMode based on Integer32"""
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


_H3cDot11RRMAPWorkMode_Type.__name__ = "Integer32"
_H3cDot11RRMAPWorkMode_Object = MibTableColumn
h3cDot11RRMAPWorkMode = _H3cDot11RRMAPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 3, 1, 1),
    _H3cDot11RRMAPWorkMode_Type()
)
h3cDot11RRMAPWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMAPWorkMode.setStatus("current")
_H3cDot11RRMSDRadioGroupTable_Object = MibTable
h3cDot11RRMSDRadioGroupTable = _H3cDot11RRMSDRadioGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDot11RRMSDRadioGroupTable.setStatus("current")
_H3cDot11RRMSDRadioGroupEntry_Object = MibTableRow
h3cDot11RRMSDRadioGroupEntry = _H3cDot11RRMSDRadioGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 4, 1)
)
h3cDot11RRMSDRadioGroupEntry.setIndexNames(
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMSDRadioGroupId"),
)
if mibBuilder.loadTexts:
    h3cDot11RRMSDRadioGroupEntry.setStatus("current")
_H3cDot11RRMSDRadioGroupId_Type = Unsigned32
_H3cDot11RRMSDRadioGroupId_Object = MibTableColumn
h3cDot11RRMSDRadioGroupId = _H3cDot11RRMSDRadioGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 4, 1, 1),
    _H3cDot11RRMSDRadioGroupId_Type()
)
h3cDot11RRMSDRadioGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RRMSDRadioGroupId.setStatus("current")
_H3cDot11RRMSDRadioGroupDesc_Type = OctetString
_H3cDot11RRMSDRadioGroupDesc_Object = MibTableColumn
h3cDot11RRMSDRadioGroupDesc = _H3cDot11RRMSDRadioGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 4, 1, 2),
    _H3cDot11RRMSDRadioGroupDesc_Type()
)
h3cDot11RRMSDRadioGroupDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RRMSDRadioGroupDesc.setStatus("current")
_H3cDot11RRMSDRdGrpChlHolddownTm_Type = Unsigned32
_H3cDot11RRMSDRdGrpChlHolddownTm_Object = MibTableColumn
h3cDot11RRMSDRdGrpChlHolddownTm = _H3cDot11RRMSDRdGrpChlHolddownTm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 4, 1, 3),
    _H3cDot11RRMSDRdGrpChlHolddownTm_Type()
)
h3cDot11RRMSDRdGrpChlHolddownTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RRMSDRdGrpChlHolddownTm.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMSDRdGrpChlHolddownTm.setUnits("minute")
_H3cDot11RRMSDRdGrpPwrHolddownTm_Type = Unsigned32
_H3cDot11RRMSDRdGrpPwrHolddownTm_Object = MibTableColumn
h3cDot11RRMSDRdGrpPwrHolddownTm = _H3cDot11RRMSDRdGrpPwrHolddownTm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 4, 1, 4),
    _H3cDot11RRMSDRdGrpPwrHolddownTm_Type()
)
h3cDot11RRMSDRdGrpPwrHolddownTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RRMSDRdGrpPwrHolddownTm.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMSDRdGrpPwrHolddownTm.setUnits("minute")
_H3cDot11RRMSDRdGroupRowStatus_Type = RowStatus
_H3cDot11RRMSDRdGroupRowStatus_Object = MibTableColumn
h3cDot11RRMSDRdGroupRowStatus = _H3cDot11RRMSDRdGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 4, 1, 5),
    _H3cDot11RRMSDRdGroupRowStatus_Type()
)
h3cDot11RRMSDRdGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RRMSDRdGroupRowStatus.setStatus("current")
_H3cDot11RRMAPCfg2Table_Object = MibTable
h3cDot11RRMAPCfg2Table = _H3cDot11RRMAPCfg2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 5)
)
if mibBuilder.loadTexts:
    h3cDot11RRMAPCfg2Table.setStatus("current")
_H3cDot11RRMAPCfg2Entry_Object = MibTableRow
h3cDot11RRMAPCfg2Entry = _H3cDot11RRMAPCfg2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 5, 1)
)
h3cDot11RRMAPCfg2Entry.setIndexNames(
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cDot11RRMAPCfg2Entry.setStatus("current")
_H3cDot11RRMAPSerialID_Type = H3cDot11ObjectIDType
_H3cDot11RRMAPSerialID_Object = MibTableColumn
h3cDot11RRMAPSerialID = _H3cDot11RRMAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 5, 1, 1),
    _H3cDot11RRMAPSerialID_Type()
)
h3cDot11RRMAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RRMAPSerialID.setStatus("current")
_H3cDot11RRMAPIntfThreshold_Type = Integer32
_H3cDot11RRMAPIntfThreshold_Object = MibTableColumn
h3cDot11RRMAPIntfThreshold = _H3cDot11RRMAPIntfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 5, 1, 2),
    _H3cDot11RRMAPIntfThreshold_Type()
)
h3cDot11RRMAPIntfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMAPIntfThreshold.setStatus("current")
_H3cDot11RRMStaIntfThreshold_Type = Integer32
_H3cDot11RRMStaIntfThreshold_Object = MibTableColumn
h3cDot11RRMStaIntfThreshold = _H3cDot11RRMStaIntfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 5, 1, 3),
    _H3cDot11RRMStaIntfThreshold_Type()
)
h3cDot11RRMStaIntfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMStaIntfThreshold.setStatus("current")
_H3cDot11RRMCoChlIntfTrapThhd_Type = Integer32
_H3cDot11RRMCoChlIntfTrapThhd_Object = MibTableColumn
h3cDot11RRMCoChlIntfTrapThhd = _H3cDot11RRMCoChlIntfTrapThhd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 5, 1, 4),
    _H3cDot11RRMCoChlIntfTrapThhd_Type()
)
h3cDot11RRMCoChlIntfTrapThhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMCoChlIntfTrapThhd.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMCoChlIntfTrapThhd.setUnits("dbm")
_H3cDot11RRMAdjChlIntfTrapThhd_Type = Integer32
_H3cDot11RRMAdjChlIntfTrapThhd_Object = MibTableColumn
h3cDot11RRMAdjChlIntfTrapThhd = _H3cDot11RRMAdjChlIntfTrapThhd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 1, 5, 1, 5),
    _H3cDot11RRMAdjChlIntfTrapThhd_Type()
)
h3cDot11RRMAdjChlIntfTrapThhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMAdjChlIntfTrapThhd.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMAdjChlIntfTrapThhd.setUnits("dbm")
_H3cDot11RRMDetectGroup_ObjectIdentity = ObjectIdentity
h3cDot11RRMDetectGroup = _H3cDot11RRMDetectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2)
)
_H3cDot11RRMChlRptTable_Object = MibTable
h3cDot11RRMChlRptTable = _H3cDot11RRMChlRptTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptTable.setStatus("current")
_H3cDot11RRMChlRptEntry_Object = MibTableRow
h3cDot11RRMChlRptEntry = _H3cDot11RRMChlRptEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1)
)
h3cDot11RRMChlRptEntry.setIndexNames(
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMRadioIndex"),
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMChlRptChlNum"),
)
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptEntry.setStatus("current")
_H3cDot11RRMRadioIndex_Type = H3cDot11RadioElementIndex
_H3cDot11RRMRadioIndex_Object = MibTableColumn
h3cDot11RRMRadioIndex = _H3cDot11RRMRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 1),
    _H3cDot11RRMRadioIndex_Type()
)
h3cDot11RRMRadioIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11RRMRadioIndex.setStatus("current")
_H3cDot11RRMChlRptChlNum_Type = Integer32
_H3cDot11RRMChlRptChlNum_Object = MibTableColumn
h3cDot11RRMChlRptChlNum = _H3cDot11RRMChlRptChlNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 2),
    _H3cDot11RRMChlRptChlNum_Type()
)
h3cDot11RRMChlRptChlNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptChlNum.setStatus("current")


class _H3cDot11RRMChlRptChlType_Type(Integer32):
    """Custom type h3cDot11RRMChlRptChlType based on Integer32"""
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


_H3cDot11RRMChlRptChlType_Type.__name__ = "Integer32"
_H3cDot11RRMChlRptChlType_Object = MibTableColumn
h3cDot11RRMChlRptChlType = _H3cDot11RRMChlRptChlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 3),
    _H3cDot11RRMChlRptChlType_Type()
)
h3cDot11RRMChlRptChlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptChlType.setStatus("current")


class _H3cDot11RRMChlRptChlQlty_Type(Integer32):
    """Custom type h3cDot11RRMChlRptChlQlty based on Integer32"""
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


_H3cDot11RRMChlRptChlQlty_Type.__name__ = "Integer32"
_H3cDot11RRMChlRptChlQlty_Object = MibTableColumn
h3cDot11RRMChlRptChlQlty = _H3cDot11RRMChlRptChlQlty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 4),
    _H3cDot11RRMChlRptChlQlty_Type()
)
h3cDot11RRMChlRptChlQlty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptChlQlty.setStatus("current")
_H3cDot11RRMChlRptNbrCnt_Type = Integer32
_H3cDot11RRMChlRptNbrCnt_Object = MibTableColumn
h3cDot11RRMChlRptNbrCnt = _H3cDot11RRMChlRptNbrCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 5),
    _H3cDot11RRMChlRptNbrCnt_Type()
)
h3cDot11RRMChlRptNbrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptNbrCnt.setStatus("current")


class _H3cDot11RRMChlRptLoad_Type(Integer32):
    """Custom type h3cDot11RRMChlRptLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMChlRptLoad_Type.__name__ = "Integer32"
_H3cDot11RRMChlRptLoad_Object = MibTableColumn
h3cDot11RRMChlRptLoad = _H3cDot11RRMChlRptLoad_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 6),
    _H3cDot11RRMChlRptLoad_Type()
)
h3cDot11RRMChlRptLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptLoad.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptLoad.setUnits("percent")


class _H3cDot11RRMChlRptUtlz_Type(Integer32):
    """Custom type h3cDot11RRMChlRptUtlz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMChlRptUtlz_Type.__name__ = "Integer32"
_H3cDot11RRMChlRptUtlz_Object = MibTableColumn
h3cDot11RRMChlRptUtlz = _H3cDot11RRMChlRptUtlz_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 7),
    _H3cDot11RRMChlRptUtlz_Type()
)
h3cDot11RRMChlRptUtlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptUtlz.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptUtlz.setUnits("percent")


class _H3cDot11RRMChlRptIntrf_Type(Integer32):
    """Custom type h3cDot11RRMChlRptIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMChlRptIntrf_Type.__name__ = "Integer32"
_H3cDot11RRMChlRptIntrf_Object = MibTableColumn
h3cDot11RRMChlRptIntrf = _H3cDot11RRMChlRptIntrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 8),
    _H3cDot11RRMChlRptIntrf_Type()
)
h3cDot11RRMChlRptIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptIntrf.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptIntrf.setUnits("percent")


class _H3cDot11RRMChlRptPER_Type(Integer32):
    """Custom type h3cDot11RRMChlRptPER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMChlRptPER_Type.__name__ = "Integer32"
_H3cDot11RRMChlRptPER_Object = MibTableColumn
h3cDot11RRMChlRptPER = _H3cDot11RRMChlRptPER_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 9),
    _H3cDot11RRMChlRptPER_Type()
)
h3cDot11RRMChlRptPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptPER.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptPER.setUnits("percent")


class _H3cDot11RRMChlRptRetryRate_Type(Integer32):
    """Custom type h3cDot11RRMChlRptRetryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMChlRptRetryRate_Type.__name__ = "Integer32"
_H3cDot11RRMChlRptRetryRate_Object = MibTableColumn
h3cDot11RRMChlRptRetryRate = _H3cDot11RRMChlRptRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 10),
    _H3cDot11RRMChlRptRetryRate_Type()
)
h3cDot11RRMChlRptRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptRetryRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptRetryRate.setUnits("percent")
_H3cDot11RRMChlRptNoise_Type = Integer32
_H3cDot11RRMChlRptNoise_Object = MibTableColumn
h3cDot11RRMChlRptNoise = _H3cDot11RRMChlRptNoise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 11),
    _H3cDot11RRMChlRptNoise_Type()
)
h3cDot11RRMChlRptNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptNoise.setStatus("current")


class _H3cDot11RRMChlRptRadarIndtcr_Type(Integer32):
    """Custom type h3cDot11RRMChlRptRadarIndtcr based on Integer32"""
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


_H3cDot11RRMChlRptRadarIndtcr_Type.__name__ = "Integer32"
_H3cDot11RRMChlRptRadarIndtcr_Object = MibTableColumn
h3cDot11RRMChlRptRadarIndtcr = _H3cDot11RRMChlRptRadarIndtcr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 1, 1, 12),
    _H3cDot11RRMChlRptRadarIndtcr_Type()
)
h3cDot11RRMChlRptRadarIndtcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RRMChlRptRadarIndtcr.setStatus("current")
_H3cDot11RRMNbrInfoTable_Object = MibTable
h3cDot11RRMNbrInfoTable = _H3cDot11RRMNbrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDot11RRMNbrInfoTable.setStatus("current")
_H3cDot11RRMNbrInfoEntry_Object = MibTableRow
h3cDot11RRMNbrInfoEntry = _H3cDot11RRMNbrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 2, 1)
)
h3cDot11RRMNbrInfoEntry.setIndexNames(
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMRadioIndex"),
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RrmNbrBSSID"),
)
if mibBuilder.loadTexts:
    h3cDot11RRMNbrInfoEntry.setStatus("current")
_H3cDot11RrmNbrBSSID_Type = MacAddress
_H3cDot11RrmNbrBSSID_Object = MibTableColumn
h3cDot11RrmNbrBSSID = _H3cDot11RrmNbrBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 2, 1, 1),
    _H3cDot11RrmNbrBSSID_Type()
)
h3cDot11RrmNbrBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RrmNbrBSSID.setStatus("current")
_H3cDot11RrmNbrChl_Type = H3cDot11ChannelScopeType
_H3cDot11RrmNbrChl_Object = MibTableColumn
h3cDot11RrmNbrChl = _H3cDot11RrmNbrChl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 2, 1, 2),
    _H3cDot11RrmNbrChl_Type()
)
h3cDot11RrmNbrChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RrmNbrChl.setStatus("current")


class _H3cDot11RRMNbrIntrf_Type(Integer32):
    """Custom type h3cDot11RRMNbrIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMNbrIntrf_Type.__name__ = "Integer32"
_H3cDot11RRMNbrIntrf_Object = MibTableColumn
h3cDot11RRMNbrIntrf = _H3cDot11RRMNbrIntrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 2, 1, 3),
    _H3cDot11RRMNbrIntrf_Type()
)
h3cDot11RRMNbrIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMNbrIntrf.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMNbrIntrf.setUnits("percent")
_H3cDot11RrmNbrRSSI_Type = Integer32
_H3cDot11RrmNbrRSSI_Object = MibTableColumn
h3cDot11RrmNbrRSSI = _H3cDot11RrmNbrRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 2, 1, 4),
    _H3cDot11RrmNbrRSSI_Type()
)
h3cDot11RrmNbrRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RrmNbrRSSI.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RrmNbrRSSI.setUnits("dBm")


class _H3cDot11RrmNbrType_Type(Integer32):
    """Custom type h3cDot11RrmNbrType based on Integer32"""
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


_H3cDot11RrmNbrType_Type.__name__ = "Integer32"
_H3cDot11RrmNbrType_Object = MibTableColumn
h3cDot11RrmNbrType = _H3cDot11RrmNbrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 2, 1, 5),
    _H3cDot11RrmNbrType_Type()
)
h3cDot11RrmNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RrmNbrType.setStatus("current")
_H3cDot11RrmNbrSSID_Type = H3cDot11SSIDStringType
_H3cDot11RrmNbrSSID_Object = MibTableColumn
h3cDot11RrmNbrSSID = _H3cDot11RrmNbrSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 2, 1, 6),
    _H3cDot11RrmNbrSSID_Type()
)
h3cDot11RrmNbrSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RrmNbrSSID.setStatus("current")
_H3cDot11RRMHistoryTable_Object = MibTable
h3cDot11RRMHistoryTable = _H3cDot11RRMHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryTable.setStatus("current")
_H3cDot11RRMHistoryEntry_Object = MibTableRow
h3cDot11RRMHistoryEntry = _H3cDot11RRMHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1)
)
h3cDot11RRMHistoryEntry.setIndexNames(
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMRadioIndex"),
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMHistoryId"),
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11RRMHistoryRecIndctr"),
)
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryEntry.setStatus("current")
_H3cDot11RRMHistoryId_Type = Integer32
_H3cDot11RRMHistoryId_Object = MibTableColumn
h3cDot11RRMHistoryId = _H3cDot11RRMHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 1),
    _H3cDot11RRMHistoryId_Type()
)
h3cDot11RRMHistoryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryId.setStatus("current")


class _H3cDot11RRMHistoryRecIndctr_Type(Integer32):
    """Custom type h3cDot11RRMHistoryRecIndctr based on Integer32"""
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


_H3cDot11RRMHistoryRecIndctr_Type.__name__ = "Integer32"
_H3cDot11RRMHistoryRecIndctr_Object = MibTableColumn
h3cDot11RRMHistoryRecIndctr = _H3cDot11RRMHistoryRecIndctr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 2),
    _H3cDot11RRMHistoryRecIndctr_Type()
)
h3cDot11RRMHistoryRecIndctr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryRecIndctr.setStatus("current")
_H3cDot11RRMHistoryChl_Type = H3cDot11ChannelScopeType
_H3cDot11RRMHistoryChl_Object = MibTableColumn
h3cDot11RRMHistoryChl = _H3cDot11RRMHistoryChl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 3),
    _H3cDot11RRMHistoryChl_Type()
)
h3cDot11RRMHistoryChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryChl.setStatus("current")
_H3cDot11RRMHistoryPwr_Type = Integer32
_H3cDot11RRMHistoryPwr_Object = MibTableColumn
h3cDot11RRMHistoryPwr = _H3cDot11RRMHistoryPwr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 4),
    _H3cDot11RRMHistoryPwr_Type()
)
h3cDot11RRMHistoryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryPwr.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryPwr.setUnits("dBm")


class _H3cDot11RRMHistoryLoad_Type(Integer32):
    """Custom type h3cDot11RRMHistoryLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMHistoryLoad_Type.__name__ = "Integer32"
_H3cDot11RRMHistoryLoad_Object = MibTableColumn
h3cDot11RRMHistoryLoad = _H3cDot11RRMHistoryLoad_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 5),
    _H3cDot11RRMHistoryLoad_Type()
)
h3cDot11RRMHistoryLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryLoad.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryLoad.setUnits("percent")


class _H3cDot11RRMHistoryUtlz_Type(Integer32):
    """Custom type h3cDot11RRMHistoryUtlz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMHistoryUtlz_Type.__name__ = "Integer32"
_H3cDot11RRMHistoryUtlz_Object = MibTableColumn
h3cDot11RRMHistoryUtlz = _H3cDot11RRMHistoryUtlz_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 6),
    _H3cDot11RRMHistoryUtlz_Type()
)
h3cDot11RRMHistoryUtlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryUtlz.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryUtlz.setUnits("percent")


class _H3cDot11RRMHistoryIntrf_Type(Integer32):
    """Custom type h3cDot11RRMHistoryIntrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMHistoryIntrf_Type.__name__ = "Integer32"
_H3cDot11RRMHistoryIntrf_Object = MibTableColumn
h3cDot11RRMHistoryIntrf = _H3cDot11RRMHistoryIntrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 7),
    _H3cDot11RRMHistoryIntrf_Type()
)
h3cDot11RRMHistoryIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryIntrf.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryIntrf.setUnits("percent")
_H3cDot11RRMHistoryNoise_Type = Integer32
_H3cDot11RRMHistoryNoise_Object = MibTableColumn
h3cDot11RRMHistoryNoise = _H3cDot11RRMHistoryNoise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 8),
    _H3cDot11RRMHistoryNoise_Type()
)
h3cDot11RRMHistoryNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryNoise.setStatus("current")


class _H3cDot11RRMHistoryPER_Type(Integer32):
    """Custom type h3cDot11RRMHistoryPER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMHistoryPER_Type.__name__ = "Integer32"
_H3cDot11RRMHistoryPER_Object = MibTableColumn
h3cDot11RRMHistoryPER = _H3cDot11RRMHistoryPER_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 9),
    _H3cDot11RRMHistoryPER_Type()
)
h3cDot11RRMHistoryPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryPER.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryPER.setUnits("percent")


class _H3cDot11RRMHistoryRetryRate_Type(Integer32):
    """Custom type h3cDot11RRMHistoryRetryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11RRMHistoryRetryRate_Type.__name__ = "Integer32"
_H3cDot11RRMHistoryRetryRate_Object = MibTableColumn
h3cDot11RRMHistoryRetryRate = _H3cDot11RRMHistoryRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 10),
    _H3cDot11RRMHistoryRetryRate_Type()
)
h3cDot11RRMHistoryRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryRetryRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryRetryRate.setUnits("percent")


class _H3cDot11RRMHistoryChgReason_Type(Bits):
    """Custom type h3cDot11RRMHistoryChgReason based on Bits"""
    namedValues = NamedValues(
        *(("coverage", 1),
          ("interference", 5),
          ("others", 0),
          ("packetsDiscarded", 4),
          ("radar", 2),
          ("retransmission", 3))
    )

_H3cDot11RRMHistoryChgReason_Type.__name__ = "Bits"
_H3cDot11RRMHistoryChgReason_Object = MibTableColumn
h3cDot11RRMHistoryChgReason = _H3cDot11RRMHistoryChgReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 11),
    _H3cDot11RRMHistoryChgReason_Type()
)
h3cDot11RRMHistoryChgReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryChgReason.setStatus("current")
_H3cDot11RRMHistoryChgDateTime_Type = DateAndTime
_H3cDot11RRMHistoryChgDateTime_Object = MibTableColumn
h3cDot11RRMHistoryChgDateTime = _H3cDot11RRMHistoryChgDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 2, 3, 1, 12),
    _H3cDot11RRMHistoryChgDateTime_Type()
)
h3cDot11RRMHistoryChgDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RRMHistoryChgDateTime.setStatus("current")
_H3cDot11RRMNotifyGroup_ObjectIdentity = ObjectIdentity
h3cDot11RRMNotifyGroup = _H3cDot11RRMNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3)
)
_H3cDot11RRMChlQltyNotifications_ObjectIdentity = ObjectIdentity
h3cDot11RRMChlQltyNotifications = _H3cDot11RRMChlQltyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 1)
)
_H3cDot11RRMChlQltyNtfPrefix_ObjectIdentity = ObjectIdentity
h3cDot11RRMChlQltyNtfPrefix = _H3cDot11RRMChlQltyNtfPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 1, 0)
)
_H3cDot11RRMResChgNotifications_ObjectIdentity = ObjectIdentity
h3cDot11RRMResChgNotifications = _H3cDot11RRMResChgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 2)
)
_H3cDot11RRMResChgNtfPrefix_ObjectIdentity = ObjectIdentity
h3cDot11RRMResChgNtfPrefix = _H3cDot11RRMResChgNtfPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 2, 0)
)
_H3cDot11RRMNotificationsVar_ObjectIdentity = ObjectIdentity
h3cDot11RRMNotificationsVar = _H3cDot11RRMNotificationsVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 3)
)
_H3cDot11NewPower_Type = Integer32
_H3cDot11NewPower_Object = MibScalar
h3cDot11NewPower = _H3cDot11NewPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 3, 1),
    _H3cDot11NewPower_Type()
)
h3cDot11NewPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11NewPower.setStatus("current")
_H3cDot11OldPower_Type = Integer32
_H3cDot11OldPower_Object = MibScalar
h3cDot11OldPower = _H3cDot11OldPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 3, 2),
    _H3cDot11OldPower_Type()
)
h3cDot11OldPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11OldPower.setStatus("current")
_H3cDot11MonitorDetectedGroup_ObjectIdentity = ObjectIdentity
h3cDot11MonitorDetectedGroup = _H3cDot11MonitorDetectedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4)
)
_H3cDot11MonitorDetectedDevTable_Object = MibTable
h3cDot11MonitorDetectedDevTable = _H3cDot11MonitorDetectedDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1)
)
if mibBuilder.loadTexts:
    h3cDot11MonitorDetectedDevTable.setStatus("current")
_H3cDot11MonitorDetectedDevEntry_Object = MibTableRow
h3cDot11MonitorDetectedDevEntry = _H3cDot11MonitorDetectedDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1)
)
h3cDot11MonitorDetectedDevEntry.setIndexNames(
    (0, "H3C-DOT11-RRM-MIB", "h3cDot11MonitorDevMAC"),
    (0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11MonitorDetectedDevEntry.setStatus("current")
_H3cDot11MonitorDevMAC_Type = MacAddress
_H3cDot11MonitorDevMAC_Object = MibTableColumn
h3cDot11MonitorDevMAC = _H3cDot11MonitorDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 1),
    _H3cDot11MonitorDevMAC_Type()
)
h3cDot11MonitorDevMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevMAC.setStatus("current")


class _H3cDot11MonitorDevType_Type(Integer32):
    """Custom type h3cDot11MonitorDevType based on Integer32"""
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


_H3cDot11MonitorDevType_Type.__name__ = "Integer32"
_H3cDot11MonitorDevType_Object = MibTableColumn
h3cDot11MonitorDevType = _H3cDot11MonitorDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 2),
    _H3cDot11MonitorDevType_Type()
)
h3cDot11MonitorDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevType.setStatus("current")
_H3cDot11MonitorDevVendor_Type = OctetString
_H3cDot11MonitorDevVendor_Object = MibTableColumn
h3cDot11MonitorDevVendor = _H3cDot11MonitorDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 3),
    _H3cDot11MonitorDevVendor_Type()
)
h3cDot11MonitorDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevVendor.setStatus("current")
_H3cDot11MonitorDevSSID_Type = OctetString
_H3cDot11MonitorDevSSID_Object = MibTableColumn
h3cDot11MonitorDevSSID = _H3cDot11MonitorDevSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 4),
    _H3cDot11MonitorDevSSID_Type()
)
h3cDot11MonitorDevSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevSSID.setStatus("current")
_H3cDot11MonitorDevBSSID_Type = MacAddress
_H3cDot11MonitorDevBSSID_Object = MibTableColumn
h3cDot11MonitorDevBSSID = _H3cDot11MonitorDevBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 5),
    _H3cDot11MonitorDevBSSID_Type()
)
h3cDot11MonitorDevBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevBSSID.setStatus("current")
_H3cDot11MonitorDevChannel_Type = H3cDot11ChannelScopeType
_H3cDot11MonitorDevChannel_Object = MibTableColumn
h3cDot11MonitorDevChannel = _H3cDot11MonitorDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 6),
    _H3cDot11MonitorDevChannel_Type()
)
h3cDot11MonitorDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevChannel.setStatus("current")
_H3cDot11MonitorRadioId_Type = H3cDot11RadioScopeType
_H3cDot11MonitorRadioId_Object = MibTableColumn
h3cDot11MonitorRadioId = _H3cDot11MonitorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 7),
    _H3cDot11MonitorRadioId_Type()
)
h3cDot11MonitorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorRadioId.setStatus("current")
_H3cDot11MonitorDevMaxRSSI_Type = Integer32
_H3cDot11MonitorDevMaxRSSI_Object = MibTableColumn
h3cDot11MonitorDevMaxRSSI = _H3cDot11MonitorDevMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 8),
    _H3cDot11MonitorDevMaxRSSI_Type()
)
h3cDot11MonitorDevMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevMaxRSSI.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevMaxRSSI.setUnits("dbm")
_H3cDot11MonitorDevBeaconIntvl_Type = Integer32
_H3cDot11MonitorDevBeaconIntvl_Object = MibTableColumn
h3cDot11MonitorDevBeaconIntvl = _H3cDot11MonitorDevBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 9),
    _H3cDot11MonitorDevBeaconIntvl_Type()
)
h3cDot11MonitorDevBeaconIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevBeaconIntvl.setUnits("millisecond")
_H3cDot11MonitorDevFstDctTime_Type = DateAndTime
_H3cDot11MonitorDevFstDctTime_Object = MibTableColumn
h3cDot11MonitorDevFstDctTime = _H3cDot11MonitorDevFstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 10),
    _H3cDot11MonitorDevFstDctTime_Type()
)
h3cDot11MonitorDevFstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevFstDctTime.setStatus("current")
_H3cDot11MonitorDevLstDctTime_Type = DateAndTime
_H3cDot11MonitorDevLstDctTime_Object = MibTableColumn
h3cDot11MonitorDevLstDctTime = _H3cDot11MonitorDevLstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 11),
    _H3cDot11MonitorDevLstDctTime_Type()
)
h3cDot11MonitorDevLstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevLstDctTime.setStatus("current")
_H3cDot11MonitorDevClear_Type = TruthValue
_H3cDot11MonitorDevClear_Object = MibTableColumn
h3cDot11MonitorDevClear = _H3cDot11MonitorDevClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 12),
    _H3cDot11MonitorDevClear_Type()
)
h3cDot11MonitorDevClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevClear.setStatus("current")
_H3cDot11MonitorDevSNR_Type = Integer32
_H3cDot11MonitorDevSNR_Object = MibTableColumn
h3cDot11MonitorDevSNR = _H3cDot11MonitorDevSNR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 4, 1, 1, 13),
    _H3cDot11MonitorDevSNR_Type()
)
h3cDot11MonitorDevSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MonitorDevSNR.setStatus("current")

# Managed Objects groups


# Notification objects

h3cDot11RRMIntrfLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 1, 0, 1)
)
h3cDot11RRMIntrfLimit.setObjects(
    ("H3C-DOT11-RRM-MIB", "h3cDot11RRMChlRptIntrf")
)
if mibBuilder.loadTexts:
    h3cDot11RRMIntrfLimit.setStatus(
        "current"
    )

h3cDot11RRMPERLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 1, 0, 2)
)
h3cDot11RRMPERLimit.setObjects(
    ("H3C-DOT11-RRM-MIB", "h3cDot11RRMChlRptPER")
)
if mibBuilder.loadTexts:
    h3cDot11RRMPERLimit.setStatus(
        "current"
    )

h3cDot11RRMNoiseLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 1, 0, 3)
)
h3cDot11RRMNoiseLimit.setObjects(
    ("H3C-DOT11-RRM-MIB", "h3cDot11RRMChlRptNoise")
)
if mibBuilder.loadTexts:
    h3cDot11RRMNoiseLimit.setStatus(
        "current"
    )

h3cDot11RRMPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 8, 3, 2, 0, 1)
)
h3cDot11RRMPowerChange.setObjects(
      *(("H3C-DOT11-RRM-MIB", "h3cDot11RRMRadioIndex"),
        ("H3C-DOT11-RRM-MIB", "h3cDot11NewPower"),
        ("H3C-DOT11-RRM-MIB", "h3cDot11OldPower"))
)
if mibBuilder.loadTexts:
    h3cDot11RRMPowerChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DOT11-RRM-MIB",
    **{"h3cDot11RRM": h3cDot11RRM,
       "h3cDot11RRMConfigGroup": h3cDot11RRMConfigGroup,
       "h3cDot11RRMGlobalCfgPara": h3cDot11RRMGlobalCfgPara,
       "h3cDot11RRM11nMadtMaxMcs": h3cDot11RRM11nMadtMaxMcs,
       "h3cDot11RRM11nSuptMaxMcs": h3cDot11RRM11nSuptMaxMcs,
       "h3cDot11RRM11gProtect": h3cDot11RRM11gProtect,
       "h3cDot11RRM11aPwrConstrt": h3cDot11RRM11aPwrConstrt,
       "h3cDot11RRM11aSpectrumManag": h3cDot11RRM11aSpectrumManag,
       "h3cDot11RRMAutoChlAvoid11h": h3cDot11RRMAutoChlAvoid11h,
       "h3cDot11RRMScanChl": h3cDot11RRMScanChl,
       "h3cDot11RRMScanRptIntvel": h3cDot11RRMScanRptIntvel,
       "h3cDot11APInterfNumThreshhd": h3cDot11APInterfNumThreshhd,
       "h3cDot11StaInterfNumThreshhd": h3cDot11StaInterfNumThreshhd,
       "h3cDot11RRMRadioCfgTable": h3cDot11RRMRadioCfgTable,
       "h3cDot11RRMRadioCfgEntry": h3cDot11RRMRadioCfgEntry,
       "h3cDot11RRMRadioType": h3cDot11RRMRadioType,
       "h3cDot11RRMCfgChlState": h3cDot11RRMCfgChlState,
       "h3cDot11RRMCfgChlMode": h3cDot11RRMCfgChlMode,
       "h3cDot11RRMChlProntoRadioElmt": h3cDot11RRMChlProntoRadioElmt,
       "h3cDot11RRMCfgPwrState": h3cDot11RRMCfgPwrState,
       "h3cDot11RRMCfgPwrMode": h3cDot11RRMCfgPwrMode,
       "h3cDot11RRMPwrProntoRadioElmt": h3cDot11RRMPwrProntoRadioElmt,
       "h3cDot11RRMCfgIntrvl": h3cDot11RRMCfgIntrvl,
       "h3cDot11RRMCfgIntrfThres": h3cDot11RRMCfgIntrfThres,
       "h3cDot11RRMCfgNoiseThres": h3cDot11RRMCfgNoiseThres,
       "h3cDot11RRMCfgPERThres": h3cDot11RRMCfgPERThres,
       "h3cDot11RRMCfgToleranceFctr": h3cDot11RRMCfgToleranceFctr,
       "h3cDot11RRMCfgAdjacencyFctr": h3cDot11RRMCfgAdjacencyFctr,
       "h3cDot11RRMAPCfgTable": h3cDot11RRMAPCfgTable,
       "h3cDot11RRMAPCfgEntry": h3cDot11RRMAPCfgEntry,
       "h3cDot11RRMAPWorkMode": h3cDot11RRMAPWorkMode,
       "h3cDot11RRMSDRadioGroupTable": h3cDot11RRMSDRadioGroupTable,
       "h3cDot11RRMSDRadioGroupEntry": h3cDot11RRMSDRadioGroupEntry,
       "h3cDot11RRMSDRadioGroupId": h3cDot11RRMSDRadioGroupId,
       "h3cDot11RRMSDRadioGroupDesc": h3cDot11RRMSDRadioGroupDesc,
       "h3cDot11RRMSDRdGrpChlHolddownTm": h3cDot11RRMSDRdGrpChlHolddownTm,
       "h3cDot11RRMSDRdGrpPwrHolddownTm": h3cDot11RRMSDRdGrpPwrHolddownTm,
       "h3cDot11RRMSDRdGroupRowStatus": h3cDot11RRMSDRdGroupRowStatus,
       "h3cDot11RRMAPCfg2Table": h3cDot11RRMAPCfg2Table,
       "h3cDot11RRMAPCfg2Entry": h3cDot11RRMAPCfg2Entry,
       "h3cDot11RRMAPSerialID": h3cDot11RRMAPSerialID,
       "h3cDot11RRMAPIntfThreshold": h3cDot11RRMAPIntfThreshold,
       "h3cDot11RRMStaIntfThreshold": h3cDot11RRMStaIntfThreshold,
       "h3cDot11RRMCoChlIntfTrapThhd": h3cDot11RRMCoChlIntfTrapThhd,
       "h3cDot11RRMAdjChlIntfTrapThhd": h3cDot11RRMAdjChlIntfTrapThhd,
       "h3cDot11RRMDetectGroup": h3cDot11RRMDetectGroup,
       "h3cDot11RRMChlRptTable": h3cDot11RRMChlRptTable,
       "h3cDot11RRMChlRptEntry": h3cDot11RRMChlRptEntry,
       "h3cDot11RRMRadioIndex": h3cDot11RRMRadioIndex,
       "h3cDot11RRMChlRptChlNum": h3cDot11RRMChlRptChlNum,
       "h3cDot11RRMChlRptChlType": h3cDot11RRMChlRptChlType,
       "h3cDot11RRMChlRptChlQlty": h3cDot11RRMChlRptChlQlty,
       "h3cDot11RRMChlRptNbrCnt": h3cDot11RRMChlRptNbrCnt,
       "h3cDot11RRMChlRptLoad": h3cDot11RRMChlRptLoad,
       "h3cDot11RRMChlRptUtlz": h3cDot11RRMChlRptUtlz,
       "h3cDot11RRMChlRptIntrf": h3cDot11RRMChlRptIntrf,
       "h3cDot11RRMChlRptPER": h3cDot11RRMChlRptPER,
       "h3cDot11RRMChlRptRetryRate": h3cDot11RRMChlRptRetryRate,
       "h3cDot11RRMChlRptNoise": h3cDot11RRMChlRptNoise,
       "h3cDot11RRMChlRptRadarIndtcr": h3cDot11RRMChlRptRadarIndtcr,
       "h3cDot11RRMNbrInfoTable": h3cDot11RRMNbrInfoTable,
       "h3cDot11RRMNbrInfoEntry": h3cDot11RRMNbrInfoEntry,
       "h3cDot11RrmNbrBSSID": h3cDot11RrmNbrBSSID,
       "h3cDot11RrmNbrChl": h3cDot11RrmNbrChl,
       "h3cDot11RRMNbrIntrf": h3cDot11RRMNbrIntrf,
       "h3cDot11RrmNbrRSSI": h3cDot11RrmNbrRSSI,
       "h3cDot11RrmNbrType": h3cDot11RrmNbrType,
       "h3cDot11RrmNbrSSID": h3cDot11RrmNbrSSID,
       "h3cDot11RRMHistoryTable": h3cDot11RRMHistoryTable,
       "h3cDot11RRMHistoryEntry": h3cDot11RRMHistoryEntry,
       "h3cDot11RRMHistoryId": h3cDot11RRMHistoryId,
       "h3cDot11RRMHistoryRecIndctr": h3cDot11RRMHistoryRecIndctr,
       "h3cDot11RRMHistoryChl": h3cDot11RRMHistoryChl,
       "h3cDot11RRMHistoryPwr": h3cDot11RRMHistoryPwr,
       "h3cDot11RRMHistoryLoad": h3cDot11RRMHistoryLoad,
       "h3cDot11RRMHistoryUtlz": h3cDot11RRMHistoryUtlz,
       "h3cDot11RRMHistoryIntrf": h3cDot11RRMHistoryIntrf,
       "h3cDot11RRMHistoryNoise": h3cDot11RRMHistoryNoise,
       "h3cDot11RRMHistoryPER": h3cDot11RRMHistoryPER,
       "h3cDot11RRMHistoryRetryRate": h3cDot11RRMHistoryRetryRate,
       "h3cDot11RRMHistoryChgReason": h3cDot11RRMHistoryChgReason,
       "h3cDot11RRMHistoryChgDateTime": h3cDot11RRMHistoryChgDateTime,
       "h3cDot11RRMNotifyGroup": h3cDot11RRMNotifyGroup,
       "h3cDot11RRMChlQltyNotifications": h3cDot11RRMChlQltyNotifications,
       "h3cDot11RRMChlQltyNtfPrefix": h3cDot11RRMChlQltyNtfPrefix,
       "h3cDot11RRMIntrfLimit": h3cDot11RRMIntrfLimit,
       "h3cDot11RRMPERLimit": h3cDot11RRMPERLimit,
       "h3cDot11RRMNoiseLimit": h3cDot11RRMNoiseLimit,
       "h3cDot11RRMResChgNotifications": h3cDot11RRMResChgNotifications,
       "h3cDot11RRMResChgNtfPrefix": h3cDot11RRMResChgNtfPrefix,
       "h3cDot11RRMPowerChange": h3cDot11RRMPowerChange,
       "h3cDot11RRMNotificationsVar": h3cDot11RRMNotificationsVar,
       "h3cDot11NewPower": h3cDot11NewPower,
       "h3cDot11OldPower": h3cDot11OldPower,
       "h3cDot11MonitorDetectedGroup": h3cDot11MonitorDetectedGroup,
       "h3cDot11MonitorDetectedDevTable": h3cDot11MonitorDetectedDevTable,
       "h3cDot11MonitorDetectedDevEntry": h3cDot11MonitorDetectedDevEntry,
       "h3cDot11MonitorDevMAC": h3cDot11MonitorDevMAC,
       "h3cDot11MonitorDevType": h3cDot11MonitorDevType,
       "h3cDot11MonitorDevVendor": h3cDot11MonitorDevVendor,
       "h3cDot11MonitorDevSSID": h3cDot11MonitorDevSSID,
       "h3cDot11MonitorDevBSSID": h3cDot11MonitorDevBSSID,
       "h3cDot11MonitorDevChannel": h3cDot11MonitorDevChannel,
       "h3cDot11MonitorRadioId": h3cDot11MonitorRadioId,
       "h3cDot11MonitorDevMaxRSSI": h3cDot11MonitorDevMaxRSSI,
       "h3cDot11MonitorDevBeaconIntvl": h3cDot11MonitorDevBeaconIntvl,
       "h3cDot11MonitorDevFstDctTime": h3cDot11MonitorDevFstDctTime,
       "h3cDot11MonitorDevLstDctTime": h3cDot11MonitorDevLstDctTime,
       "h3cDot11MonitorDevClear": h3cDot11MonitorDevClear,
       "h3cDot11MonitorDevSNR": h3cDot11MonitorDevSNR}
)
