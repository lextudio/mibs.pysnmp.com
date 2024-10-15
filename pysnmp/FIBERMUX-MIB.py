# SNMP MIB module (FIBERMUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FIBERMUX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:50 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibermux_ObjectIdentity = ObjectIdentity
fibermux = _Fibermux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 120)
)
_FmxProducts_ObjectIdentity = ObjectIdentity
fmxProducts = _FmxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 120, 1)
)
_FmxCrossbow_ObjectIdentity = ObjectIdentity
fmxCrossbow = _FmxCrossbow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 120, 1, 1)
)
_FmxVariables_ObjectIdentity = ObjectIdentity
fmxVariables = _FmxVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 120, 2)
)
_FmxHubs_ObjectIdentity = ObjectIdentity
fmxHubs = _FmxHubs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 120, 2, 1)
)
_FmxSystemGrp_ObjectIdentity = ObjectIdentity
fmxSystemGrp = _FmxSystemGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1)
)
_FmxHubHwVer_Type = OctetString
_FmxHubHwVer_Object = MibScalar
fmxHubHwVer = _FmxHubHwVer_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 1),
    _FmxHubHwVer_Type()
)
fmxHubHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubHwVer.setStatus("mandatory")
_FmxHubFwVer_Type = OctetString
_FmxHubFwVer_Object = MibScalar
fmxHubFwVer = _FmxHubFwVer_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 2),
    _FmxHubFwVer_Type()
)
fmxHubFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubFwVer.setStatus("mandatory")
_FmxHubAddress_Type = OctetString
_FmxHubAddress_Object = MibScalar
fmxHubAddress = _FmxHubAddress_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 3),
    _FmxHubAddress_Type()
)
fmxHubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubAddress.setStatus("mandatory")
_FmxHubDate_Type = ObjectIdentifier
_FmxHubDate_Object = MibScalar
fmxHubDate = _FmxHubDate_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 4),
    _FmxHubDate_Type()
)
fmxHubDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxHubDate.setStatus("mandatory")
_FmxHubElapsetick_Type = TimeTicks
_FmxHubElapsetick_Object = MibScalar
fmxHubElapsetick = _FmxHubElapsetick_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 5),
    _FmxHubElapsetick_Type()
)
fmxHubElapsetick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubElapsetick.setStatus("mandatory")
_FmxHubSamplingRate_Type = Gauge32
_FmxHubSamplingRate_Object = MibScalar
fmxHubSamplingRate = _FmxHubSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 6),
    _FmxHubSamplingRate_Type()
)
fmxHubSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxHubSamplingRate.setStatus("mandatory")
_FmxHubPeakTraffic_Type = Gauge32
_FmxHubPeakTraffic_Object = MibScalar
fmxHubPeakTraffic = _FmxHubPeakTraffic_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 7),
    _FmxHubPeakTraffic_Type()
)
fmxHubPeakTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubPeakTraffic.setStatus("mandatory")
_FmxHubAverageTraffic_Type = Gauge32
_FmxHubAverageTraffic_Object = MibScalar
fmxHubAverageTraffic = _FmxHubAverageTraffic_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 8),
    _FmxHubAverageTraffic_Type()
)
fmxHubAverageTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubAverageTraffic.setStatus("mandatory")
_FmxHubCurrentTraffic_Type = Gauge32
_FmxHubCurrentTraffic_Object = MibScalar
fmxHubCurrentTraffic = _FmxHubCurrentTraffic_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 9),
    _FmxHubCurrentTraffic_Type()
)
fmxHubCurrentTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubCurrentTraffic.setStatus("mandatory")
_FmxHubTotalFrameRx_Type = Counter32
_FmxHubTotalFrameRx_Object = MibScalar
fmxHubTotalFrameRx = _FmxHubTotalFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 10),
    _FmxHubTotalFrameRx_Type()
)
fmxHubTotalFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubTotalFrameRx.setStatus("mandatory")
_FmxHubAverageByte_Type = Gauge32
_FmxHubAverageByte_Object = MibScalar
fmxHubAverageByte = _FmxHubAverageByte_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 11),
    _FmxHubAverageByte_Type()
)
fmxHubAverageByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubAverageByte.setStatus("mandatory")
_FmxHubCRCErrors_Type = Counter32
_FmxHubCRCErrors_Object = MibScalar
fmxHubCRCErrors = _FmxHubCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 12),
    _FmxHubCRCErrors_Type()
)
fmxHubCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubCRCErrors.setStatus("mandatory")
_FmxHubAlignErrors_Type = Counter32
_FmxHubAlignErrors_Object = MibScalar
fmxHubAlignErrors = _FmxHubAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 13),
    _FmxHubAlignErrors_Type()
)
fmxHubAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubAlignErrors.setStatus("mandatory")
_FmxHubMissedErrors_Type = Counter32
_FmxHubMissedErrors_Object = MibScalar
fmxHubMissedErrors = _FmxHubMissedErrors_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 14),
    _FmxHubMissedErrors_Type()
)
fmxHubMissedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubMissedErrors.setStatus("mandatory")


class _FmxHubStatus_Type(Integer32):
    """Custom type fmxHubStatus based on Integer32"""
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
        *(("pwrA-OK", 2),
          ("pwrAB-OK", 3),
          ("pwrAB-bad", 0),
          ("pwrB-OK", 1))
    )


_FmxHubStatus_Type.__name__ = "Integer32"
_FmxHubStatus_Object = MibScalar
fmxHubStatus = _FmxHubStatus_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 15),
    _FmxHubStatus_Type()
)
fmxHubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxHubStatus.setStatus("mandatory")


class _FmxHubClear_Type(Integer32):
    """Custom type fmxHubClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_FmxHubClear_Type.__name__ = "Integer32"
_FmxHubClear_Object = MibScalar
fmxHubClear = _FmxHubClear_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 1, 16),
    _FmxHubClear_Type()
)
fmxHubClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fmxHubClear.setStatus("mandatory")
_FmxCrossbowGrp_ObjectIdentity = ObjectIdentity
fmxCrossbowGrp = _FmxCrossbowGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2)
)
_FmxCbCardTable_Object = MibTable
fmxCbCardTable = _FmxCbCardTable_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fmxCbCardTable.setStatus("mandatory")
_FmxCbCardEntry_Object = MibTableRow
fmxCbCardEntry = _FmxCbCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fmxCbCardEntry.setStatus("mandatory")
_FmxCbCIndex_Type = Integer32
_FmxCbCIndex_Object = MibTableColumn
fmxCbCIndex = _FmxCbCIndex_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 1),
    _FmxCbCIndex_Type()
)
fmxCbCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCIndex.setStatus("mandatory")
_FmxCbCType_Type = Integer32
_FmxCbCType_Object = MibTableColumn
fmxCbCType = _FmxCbCType_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 2),
    _FmxCbCType_Type()
)
fmxCbCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCType.setStatus("mandatory")


class _FmxCbCReset_Type(Integer32):
    """Custom type fmxCbCReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_FmxCbCReset_Type.__name__ = "Integer32"
_FmxCbCReset_Object = MibTableColumn
fmxCbCReset = _FmxCbCReset_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 3),
    _FmxCbCReset_Type()
)
fmxCbCReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fmxCbCReset.setStatus("mandatory")


class _FmxCbCEnable_Type(Integer32):
    """Custom type fmxCbCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCEnable_Type.__name__ = "Integer32"
_FmxCbCEnable_Object = MibTableColumn
fmxCbCEnable = _FmxCbCEnable_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 4),
    _FmxCbCEnable_Type()
)
fmxCbCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxCbCEnable.setStatus("mandatory")


class _FmxCbCFIFOError_Type(Integer32):
    """Custom type fmxCbCFIFOError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCFIFOError_Type.__name__ = "Integer32"
_FmxCbCFIFOError_Object = MibTableColumn
fmxCbCFIFOError = _FmxCbCFIFOError_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 5),
    _FmxCbCFIFOError_Type()
)
fmxCbCFIFOError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCFIFOError.setStatus("mandatory")


class _FmxCbCJabberError_Type(Integer32):
    """Custom type fmxCbCJabberError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCJabberError_Type.__name__ = "Integer32"
_FmxCbCJabberError_Object = MibTableColumn
fmxCbCJabberError = _FmxCbCJabberError_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 6),
    _FmxCbCJabberError_Type()
)
fmxCbCJabberError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCJabberError.setStatus("mandatory")


class _FmxCbCLockup_Type(Integer32):
    """Custom type fmxCbCLockup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCLockup_Type.__name__ = "Integer32"
_FmxCbCLockup_Object = MibTableColumn
fmxCbCLockup = _FmxCbCLockup_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 7),
    _FmxCbCLockup_Type()
)
fmxCbCLockup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCLockup.setStatus("mandatory")


class _FmxCbCTraffic_Type(Integer32):
    """Custom type fmxCbCTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCTraffic_Type.__name__ = "Integer32"
_FmxCbCTraffic_Object = MibTableColumn
fmxCbCTraffic = _FmxCbCTraffic_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 8),
    _FmxCbCTraffic_Type()
)
fmxCbCTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCTraffic.setStatus("mandatory")
_FmxCbCTimeslot_Type = Integer32
_FmxCbCTimeslot_Object = MibTableColumn
fmxCbCTimeslot = _FmxCbCTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 9),
    _FmxCbCTimeslot_Type()
)
fmxCbCTimeslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxCbCTimeslot.setStatus("mandatory")
_FmxCbCAddress_Type = Integer32
_FmxCbCAddress_Object = MibTableColumn
fmxCbCAddress = _FmxCbCAddress_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 1, 1, 10),
    _FmxCbCAddress_Type()
)
fmxCbCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCAddress.setStatus("mandatory")
_FmxCbCPortTable_Object = MibTable
fmxCbCPortTable = _FmxCbCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fmxCbCPortTable.setStatus("mandatory")
_FmxCbCPortEntry_Object = MibTableRow
fmxCbCPortEntry = _FmxCbCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fmxCbCPortEntry.setStatus("mandatory")
_FmxCbCPIndex_Type = Integer32
_FmxCbCPIndex_Object = MibTableColumn
fmxCbCPIndex = _FmxCbCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 1),
    _FmxCbCPIndex_Type()
)
fmxCbCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCPIndex.setStatus("mandatory")


class _FmxCbCPEnable_Type(Integer32):
    """Custom type fmxCbCPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCPEnable_Type.__name__ = "Integer32"
_FmxCbCPEnable_Object = MibTableColumn
fmxCbCPEnable = _FmxCbCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 2),
    _FmxCbCPEnable_Type()
)
fmxCbCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxCbCPEnable.setStatus("mandatory")


class _FmxCbCPIntegrity_Type(Integer32):
    """Custom type fmxCbCPIntegrity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCPIntegrity_Type.__name__ = "Integer32"
_FmxCbCPIntegrity_Object = MibTableColumn
fmxCbCPIntegrity = _FmxCbCPIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 3),
    _FmxCbCPIntegrity_Type()
)
fmxCbCPIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCPIntegrity.setStatus("mandatory")


class _FmxCbCPJabberError_Type(Integer32):
    """Custom type fmxCbCPJabberError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCPJabberError_Type.__name__ = "Integer32"
_FmxCbCPJabberError_Object = MibTableColumn
fmxCbCPJabberError = _FmxCbCPJabberError_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 4),
    _FmxCbCPJabberError_Type()
)
fmxCbCPJabberError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCPJabberError.setStatus("mandatory")


class _FmxCbCPRedundCtrl_Type(Integer32):
    """Custom type fmxCbCPRedundCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCPRedundCtrl_Type.__name__ = "Integer32"
_FmxCbCPRedundCtrl_Object = MibTableColumn
fmxCbCPRedundCtrl = _FmxCbCPRedundCtrl_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 5),
    _FmxCbCPRedundCtrl_Type()
)
fmxCbCPRedundCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxCbCPRedundCtrl.setStatus("mandatory")


class _FmxCbCPRedundPrimary_Type(Integer32):
    """Custom type fmxCbCPRedundPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCPRedundPrimary_Type.__name__ = "Integer32"
_FmxCbCPRedundPrimary_Object = MibTableColumn
fmxCbCPRedundPrimary = _FmxCbCPRedundPrimary_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 6),
    _FmxCbCPRedundPrimary_Type()
)
fmxCbCPRedundPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxCbCPRedundPrimary.setStatus("mandatory")


class _FmxCbCPRedundActive_Type(Integer32):
    """Custom type fmxCbCPRedundActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FmxCbCPRedundActive_Type.__name__ = "Integer32"
_FmxCbCPRedundActive_Object = MibTableColumn
fmxCbCPRedundActive = _FmxCbCPRedundActive_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 7),
    _FmxCbCPRedundActive_Type()
)
fmxCbCPRedundActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCPRedundActive.setStatus("mandatory")
_FmxCbCPRedundPort_Type = Integer32
_FmxCbCPRedundPort_Object = MibTableColumn
fmxCbCPRedundPort = _FmxCbCPRedundPort_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 8),
    _FmxCbCPRedundPort_Type()
)
fmxCbCPRedundPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxCbCPRedundPort.setStatus("mandatory")
_FmxCbCPRedundCard_Type = Integer32
_FmxCbCPRedundCard_Object = MibTableColumn
fmxCbCPRedundCard = _FmxCbCPRedundCard_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 9),
    _FmxCbCPRedundCard_Type()
)
fmxCbCPRedundCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxCbCPRedundCard.setStatus("mandatory")
_FmxCbCPRedundErrors_Type = Counter32
_FmxCbCPRedundErrors_Object = MibTableColumn
fmxCbCPRedundErrors = _FmxCbCPRedundErrors_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 10),
    _FmxCbCPRedundErrors_Type()
)
fmxCbCPRedundErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmxCbCPRedundErrors.setStatus("mandatory")
_FmxCbCPRedundErrorLimit_Type = Gauge32
_FmxCbCPRedundErrorLimit_Object = MibTableColumn
fmxCbCPRedundErrorLimit = _FmxCbCPRedundErrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 120, 2, 1, 2, 2, 1, 11),
    _FmxCbCPRedundErrorLimit_Type()
)
fmxCbCPRedundErrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmxCbCPRedundErrorLimit.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBERMUX-MIB",
    **{"fibermux": fibermux,
       "fmxProducts": fmxProducts,
       "fmxCrossbow": fmxCrossbow,
       "fmxVariables": fmxVariables,
       "fmxHubs": fmxHubs,
       "fmxSystemGrp": fmxSystemGrp,
       "fmxHubHwVer": fmxHubHwVer,
       "fmxHubFwVer": fmxHubFwVer,
       "fmxHubAddress": fmxHubAddress,
       "fmxHubDate": fmxHubDate,
       "fmxHubElapsetick": fmxHubElapsetick,
       "fmxHubSamplingRate": fmxHubSamplingRate,
       "fmxHubPeakTraffic": fmxHubPeakTraffic,
       "fmxHubAverageTraffic": fmxHubAverageTraffic,
       "fmxHubCurrentTraffic": fmxHubCurrentTraffic,
       "fmxHubTotalFrameRx": fmxHubTotalFrameRx,
       "fmxHubAverageByte": fmxHubAverageByte,
       "fmxHubCRCErrors": fmxHubCRCErrors,
       "fmxHubAlignErrors": fmxHubAlignErrors,
       "fmxHubMissedErrors": fmxHubMissedErrors,
       "fmxHubStatus": fmxHubStatus,
       "fmxHubClear": fmxHubClear,
       "fmxCrossbowGrp": fmxCrossbowGrp,
       "fmxCbCardTable": fmxCbCardTable,
       "fmxCbCardEntry": fmxCbCardEntry,
       "fmxCbCIndex": fmxCbCIndex,
       "fmxCbCType": fmxCbCType,
       "fmxCbCReset": fmxCbCReset,
       "fmxCbCEnable": fmxCbCEnable,
       "fmxCbCFIFOError": fmxCbCFIFOError,
       "fmxCbCJabberError": fmxCbCJabberError,
       "fmxCbCLockup": fmxCbCLockup,
       "fmxCbCTraffic": fmxCbCTraffic,
       "fmxCbCTimeslot": fmxCbCTimeslot,
       "fmxCbCAddress": fmxCbCAddress,
       "fmxCbCPortTable": fmxCbCPortTable,
       "fmxCbCPortEntry": fmxCbCPortEntry,
       "fmxCbCPIndex": fmxCbCPIndex,
       "fmxCbCPEnable": fmxCbCPEnable,
       "fmxCbCPIntegrity": fmxCbCPIntegrity,
       "fmxCbCPJabberError": fmxCbCPJabberError,
       "fmxCbCPRedundCtrl": fmxCbCPRedundCtrl,
       "fmxCbCPRedundPrimary": fmxCbCPRedundPrimary,
       "fmxCbCPRedundActive": fmxCbCPRedundActive,
       "fmxCbCPRedundPort": fmxCbCPRedundPort,
       "fmxCbCPRedundCard": fmxCbCPRedundCard,
       "fmxCbCPRedundErrors": fmxCbCPRedundErrors,
       "fmxCbCPRedundErrorLimit": fmxCbCPRedundErrorLimit}
)
