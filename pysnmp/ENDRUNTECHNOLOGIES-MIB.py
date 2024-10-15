# SNMP MIB module (ENDRUNTECHNOLOGIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENDRUNTECHNOLOGIES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:30 2024
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

endRunTechnologies = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EndRunTechnologiesMIB_ObjectIdentity = ObjectIdentity
endRunTechnologiesMIB = _EndRunTechnologiesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827)
)
_PraecisCntp_ObjectIdentity = ObjectIdentity
praecisCntp = _PraecisCntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 1)
)
_Cntp_ObjectIdentity = ObjectIdentity
cntp = _Cntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0)
)
_Cntptrap_ObjectIdentity = ObjectIdentity
cntptrap = _Cntptrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 0)
)
_CntpRxPkts_Type = Counter32
_CntpRxPkts_Object = MibScalar
cntpRxPkts = _CntpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 1),
    _CntpRxPkts_Type()
)
cntpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpRxPkts.setStatus("current")
_CntpTxPkts_Type = Counter32
_CntpTxPkts_Object = MibScalar
cntpTxPkts = _CntpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 2),
    _CntpTxPkts_Type()
)
cntpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpTxPkts.setStatus("current")
_CntpIgnoredPkts_Type = Counter32
_CntpIgnoredPkts_Object = MibScalar
cntpIgnoredPkts = _CntpIgnoredPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 3),
    _CntpIgnoredPkts_Type()
)
cntpIgnoredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpIgnoredPkts.setStatus("current")
_CntpDroppedPkts_Type = Counter32
_CntpDroppedPkts_Object = MibScalar
cntpDroppedPkts = _CntpDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 4),
    _CntpDroppedPkts_Type()
)
cntpDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpDroppedPkts.setStatus("current")
_CntpAuthFail_Type = Counter32
_CntpAuthFail_Object = MibScalar
cntpAuthFail = _CntpAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 5),
    _CntpAuthFail_Type()
)
cntpAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpAuthFail.setStatus("current")


class _CntpTimeFigureOfMerit_Type(Integer32):
    """Custom type cntpTimeFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("greaterthan10ms", 9),
          ("lessthan100us", 6),
          ("lessthan10ms", 8),
          ("lessthan1ms", 7))
    )


_CntpTimeFigureOfMerit_Type.__name__ = "Integer32"
_CntpTimeFigureOfMerit_Object = MibScalar
cntpTimeFigureOfMerit = _CntpTimeFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 6),
    _CntpTimeFigureOfMerit_Type()
)
cntpTimeFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpTimeFigureOfMerit.setStatus("current")


class _CntpLeapIndBits_Type(Integer32):
    """Custom type cntpLeapIndBits based on Integer32"""
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
        *(("leapDelWarning", 2),
          ("leapInsWarning", 1),
          ("noFaultorLeap", 0),
          ("unSynchronized", 3))
    )


_CntpLeapIndBits_Type.__name__ = "Integer32"
_CntpLeapIndBits_Object = MibScalar
cntpLeapIndBits = _CntpLeapIndBits_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 7),
    _CntpLeapIndBits_Type()
)
cntpLeapIndBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpLeapIndBits.setStatus("current")


class _CntpSyncSource_Type(DisplayString):
    """Custom type cntpSyncSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CntpSyncSource_Type.__name__ = "DisplayString"
_CntpSyncSource_Object = MibScalar
cntpSyncSource = _CntpSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 8),
    _CntpSyncSource_Type()
)
cntpSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSyncSource.setStatus("current")


class _CntpOffsetToCDMAReference_Type(DisplayString):
    """Custom type cntpOffsetToCDMAReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CntpOffsetToCDMAReference_Type.__name__ = "DisplayString"
_CntpOffsetToCDMAReference_Object = MibScalar
cntpOffsetToCDMAReference = _CntpOffsetToCDMAReference_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 9),
    _CntpOffsetToCDMAReference_Type()
)
cntpOffsetToCDMAReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpOffsetToCDMAReference.setStatus("current")


class _CntpStratum_Type(Integer32):
    """Custom type cntpStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              16)
        )
    )
    namedValues = NamedValues(
        *(("cntpStratumFlywheeling", 11),
          ("cntpStratumOne", 1),
          ("cntpStratumUnsync", 16))
    )


_CntpStratum_Type.__name__ = "Integer32"
_CntpStratum_Object = MibScalar
cntpStratum = _CntpStratum_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 10),
    _CntpStratum_Type()
)
cntpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpStratum.setStatus("current")


class _CntpVersion_Type(DisplayString):
    """Custom type cntpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CntpVersion_Type.__name__ = "DisplayString"
_CntpVersion_Object = MibScalar
cntpVersion = _CntpVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 11),
    _CntpVersion_Type()
)
cntpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpVersion.setStatus("current")
_Cdma_ObjectIdentity = ObjectIdentity
cdma = _Cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1)
)
_Cdmatrap_ObjectIdentity = ObjectIdentity
cdmatrap = _Cdmatrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 0)
)


class _CdmaFaultStatus_Type(Bits):
    """Custom type cdmaFaultStatus based on Bits"""
    namedValues = NamedValues(
        *(("cdmaDACNearLimit", 7),
          ("cdmaFLASHWriteFlt", 4),
          ("cdmaFPGACfgFlt", 5),
          ("cdmaLOFailure", 2),
          ("cdmaLOPLLFlt", 3),
          ("cdmaNTPNotPolling", 1),
          ("cdmaNoSignalTimeout", 6),
          ("cdmaNotUsed", 0))
    )

_CdmaFaultStatus_Type.__name__ = "Bits"
_CdmaFaultStatus_Object = MibScalar
cdmaFaultStatus = _CdmaFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 1),
    _CdmaFaultStatus_Type()
)
cdmaFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFaultStatus.setStatus("current")


class _CdmaTimeFigureOfMerit_Type(Integer32):
    """Custom type cdmaTimeFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("greaterthan10ms", 9),
          ("lessthan100us", 6),
          ("lessthan10ms", 8),
          ("lessthan1ms", 7))
    )


_CdmaTimeFigureOfMerit_Type.__name__ = "Integer32"
_CdmaTimeFigureOfMerit_Object = MibScalar
cdmaTimeFigureOfMerit = _CdmaTimeFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 2),
    _CdmaTimeFigureOfMerit_Type()
)
cdmaTimeFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaTimeFigureOfMerit.setStatus("current")


class _CdmaSigProcState_Type(Integer32):
    """Custom type cdmaSigProcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cdmaAcquiring", 0),
          ("cdmaCarrierLocking", 4),
          ("cdmaCodeLocking", 2),
          ("cdmaDetected", 1),
          ("cdmaLocked", 8))
    )


_CdmaSigProcState_Type.__name__ = "Integer32"
_CdmaSigProcState_Object = MibScalar
cdmaSigProcState = _CdmaSigProcState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 3),
    _CdmaSigProcState_Type()
)
cdmaSigProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaSigProcState.setStatus("current")


class _CdmaChannel_Type(Integer32):
    """Custom type cdmaChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priAbandclass0subclass0", 0),
          ("priAbandclass0subclass1", 4),
          ("priBbandclass0subclass0", 1),
          ("priBbandclass0subclass1", 5),
          ("secAbandclass0subclass0", 2),
          ("secAbandclass0subclass1", 6),
          ("secBbandclass0subclass0", 3),
          ("secBbandclass0subclass1", 7))
    )


_CdmaChannel_Type.__name__ = "Integer32"
_CdmaChannel_Object = MibScalar
cdmaChannel = _CdmaChannel_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 4),
    _CdmaChannel_Type()
)
cdmaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaChannel.setStatus("current")


class _CdmaPNO_Type(Integer32):
    """Custom type cdmaPNO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CdmaPNO_Type.__name__ = "Integer32"
_CdmaPNO_Object = MibScalar
cdmaPNO = _CdmaPNO_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 5),
    _CdmaPNO_Type()
)
cdmaPNO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaPNO.setStatus("current")


class _CdmaAGC_Type(Integer32):
    """Custom type cdmaAGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdmaAGC_Type.__name__ = "Integer32"
_CdmaAGC_Object = MibScalar
cdmaAGC = _CdmaAGC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 6),
    _CdmaAGC_Type()
)
cdmaAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaAGC.setStatus("current")


class _CdmaVCDAC_Type(Integer32):
    """Custom type cdmaVCDAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdmaVCDAC_Type.__name__ = "Integer32"
_CdmaVCDAC_Object = MibScalar
cdmaVCDAC = _CdmaVCDAC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 7),
    _CdmaVCDAC_Type()
)
cdmaVCDAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaVCDAC.setStatus("current")


class _CdmaCarrierToNoiseRatio_Type(DisplayString):
    """Custom type cdmaCarrierToNoiseRatio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CdmaCarrierToNoiseRatio_Type.__name__ = "DisplayString"
_CdmaCarrierToNoiseRatio_Object = MibScalar
cdmaCarrierToNoiseRatio = _CdmaCarrierToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 8),
    _CdmaCarrierToNoiseRatio_Type()
)
cdmaCarrierToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaCarrierToNoiseRatio.setStatus("current")


class _CdmaFrameErrorRate_Type(DisplayString):
    """Custom type cdmaFrameErrorRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CdmaFrameErrorRate_Type.__name__ = "DisplayString"
_CdmaFrameErrorRate_Object = MibScalar
cdmaFrameErrorRate = _CdmaFrameErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 9),
    _CdmaFrameErrorRate_Type()
)
cdmaFrameErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFrameErrorRate.setStatus("current")


class _CdmaLeapMode_Type(DisplayString):
    """Custom type cdmaLeapMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CdmaLeapMode_Type.__name__ = "DisplayString"
_CdmaLeapMode_Object = MibScalar
cdmaLeapMode = _CdmaLeapMode_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 10),
    _CdmaLeapMode_Type()
)
cdmaLeapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaLeapMode.setStatus("current")
_CdmaCurrentLeapSeconds_Type = Integer32
_CdmaCurrentLeapSeconds_Object = MibScalar
cdmaCurrentLeapSeconds = _CdmaCurrentLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 11),
    _CdmaCurrentLeapSeconds_Type()
)
cdmaCurrentLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaCurrentLeapSeconds.setStatus("current")
_CdmaFutureLeapSeconds_Type = Integer32
_CdmaFutureLeapSeconds_Object = MibScalar
cdmaFutureLeapSeconds = _CdmaFutureLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 12),
    _CdmaFutureLeapSeconds_Type()
)
cdmaFutureLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaFutureLeapSeconds.setStatus("current")


class _CdmaVersion_Type(DisplayString):
    """Custom type cdmaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdmaVersion_Type.__name__ = "DisplayString"
_CdmaVersion_Object = MibScalar
cdmaVersion = _CdmaVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 13),
    _CdmaVersion_Type()
)
cdmaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdmaVersion.setStatus("current")
_PraecisGntp_ObjectIdentity = ObjectIdentity
praecisGntp = _PraecisGntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 2)
)
_Gntp_ObjectIdentity = ObjectIdentity
gntp = _Gntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0)
)
_Gntptrap_ObjectIdentity = ObjectIdentity
gntptrap = _Gntptrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 0)
)
_GntpRxPkts_Type = Counter32
_GntpRxPkts_Object = MibScalar
gntpRxPkts = _GntpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 1),
    _GntpRxPkts_Type()
)
gntpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpRxPkts.setStatus("current")
_GntpTxPkts_Type = Counter32
_GntpTxPkts_Object = MibScalar
gntpTxPkts = _GntpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 2),
    _GntpTxPkts_Type()
)
gntpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTxPkts.setStatus("current")
_GntpIgnoredPkts_Type = Counter32
_GntpIgnoredPkts_Object = MibScalar
gntpIgnoredPkts = _GntpIgnoredPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 3),
    _GntpIgnoredPkts_Type()
)
gntpIgnoredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpIgnoredPkts.setStatus("current")
_GntpDroppedPkts_Type = Counter32
_GntpDroppedPkts_Object = MibScalar
gntpDroppedPkts = _GntpDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 4),
    _GntpDroppedPkts_Type()
)
gntpDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpDroppedPkts.setStatus("current")
_GntpAuthFail_Type = Counter32
_GntpAuthFail_Object = MibScalar
gntpAuthFail = _GntpAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 5),
    _GntpAuthFail_Type()
)
gntpAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpAuthFail.setStatus("current")


class _GntpTimeFigureOfMerit_Type(Integer32):
    """Custom type gntpTimeFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("greaterthan10ms", 9),
          ("lessthan100us", 6),
          ("lessthan10ms", 8),
          ("lessthan10us", 5),
          ("lessthan1ms", 7),
          ("lessthan1us", 4))
    )


_GntpTimeFigureOfMerit_Type.__name__ = "Integer32"
_GntpTimeFigureOfMerit_Object = MibScalar
gntpTimeFigureOfMerit = _GntpTimeFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 6),
    _GntpTimeFigureOfMerit_Type()
)
gntpTimeFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpTimeFigureOfMerit.setStatus("current")


class _GntpLeapIndBits_Type(Integer32):
    """Custom type gntpLeapIndBits based on Integer32"""
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
        *(("leapDelWarning", 2),
          ("leapInsWarning", 1),
          ("noFaultorLeap", 0),
          ("unSynchronized", 3))
    )


_GntpLeapIndBits_Type.__name__ = "Integer32"
_GntpLeapIndBits_Object = MibScalar
gntpLeapIndBits = _GntpLeapIndBits_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 7),
    _GntpLeapIndBits_Type()
)
gntpLeapIndBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpLeapIndBits.setStatus("current")


class _GntpSyncSource_Type(DisplayString):
    """Custom type gntpSyncSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GntpSyncSource_Type.__name__ = "DisplayString"
_GntpSyncSource_Object = MibScalar
gntpSyncSource = _GntpSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 8),
    _GntpSyncSource_Type()
)
gntpSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpSyncSource.setStatus("current")


class _GntpOffsetToGPSReference_Type(DisplayString):
    """Custom type gntpOffsetToGPSReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GntpOffsetToGPSReference_Type.__name__ = "DisplayString"
_GntpOffsetToGPSReference_Object = MibScalar
gntpOffsetToGPSReference = _GntpOffsetToGPSReference_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 9),
    _GntpOffsetToGPSReference_Type()
)
gntpOffsetToGPSReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpOffsetToGPSReference.setStatus("current")


class _GntpStratum_Type(Integer32):
    """Custom type gntpStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              16)
        )
    )
    namedValues = NamedValues(
        *(("gntpStratumFlywheeling", 11),
          ("gntpStratumOne", 1),
          ("gntpStratumUnsync", 16))
    )


_GntpStratum_Type.__name__ = "Integer32"
_GntpStratum_Object = MibScalar
gntpStratum = _GntpStratum_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 10),
    _GntpStratum_Type()
)
gntpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpStratum.setStatus("current")


class _GntpVersion_Type(DisplayString):
    """Custom type gntpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GntpVersion_Type.__name__ = "DisplayString"
_GntpVersion_Object = MibScalar
gntpVersion = _GntpVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 11),
    _GntpVersion_Type()
)
gntpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gntpVersion.setStatus("current")
_Gps_ObjectIdentity = ObjectIdentity
gps = _Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1)
)
_Gpstrap_ObjectIdentity = ObjectIdentity
gpstrap = _Gpstrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 0)
)


class _GpsFaultStatus_Type(Bits):
    """Custom type gpsFaultStatus based on Bits"""
    namedValues = NamedValues(
        *(("gpsAntennaFlt", 0),
          ("gpsDACNearLimit", 7),
          ("gpsFLASHWriteFlt", 4),
          ("gpsFPGACfgFlt", 5),
          ("gpsNTPNotPolling", 1),
          ("gpsNoSignalTimeout", 6),
          ("gpsnotused0", 2),
          ("gpsnotused1", 3))
    )

_GpsFaultStatus_Type.__name__ = "Bits"
_GpsFaultStatus_Object = MibScalar
gpsFaultStatus = _GpsFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 1),
    _GpsFaultStatus_Type()
)
gpsFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFaultStatus.setStatus("current")


class _GpsTimeFigureOfMerit_Type(Integer32):
    """Custom type gpsTimeFigureOfMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("greaterthan10ms", 9),
          ("lessthan100us", 6),
          ("lessthan10ms", 8),
          ("lessthan10us", 5),
          ("lessthan1ms", 7),
          ("lessthan1us", 4))
    )


_GpsTimeFigureOfMerit_Type.__name__ = "Integer32"
_GpsTimeFigureOfMerit_Object = MibScalar
gpsTimeFigureOfMerit = _GpsTimeFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 2),
    _GpsTimeFigureOfMerit_Type()
)
gpsTimeFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTimeFigureOfMerit.setStatus("current")


class _GpsSigProcState_Type(Integer32):
    """Custom type gpsSigProcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gpsAcquiring", 0),
          ("gpsLocked", 2),
          ("gpsLocking", 1))
    )


_GpsSigProcState_Type.__name__ = "Integer32"
_GpsSigProcState_Object = MibScalar
gpsSigProcState = _GpsSigProcState_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 3),
    _GpsSigProcState_Type()
)
gpsSigProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSigProcState.setStatus("current")


class _GpsNumTrackSats_Type(Integer32):
    """Custom type gpsNumTrackSats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_GpsNumTrackSats_Type.__name__ = "Integer32"
_GpsNumTrackSats_Object = MibScalar
gpsNumTrackSats = _GpsNumTrackSats_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 4),
    _GpsNumTrackSats_Type()
)
gpsNumTrackSats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsNumTrackSats.setStatus("current")


class _GpsVCDAC_Type(Integer32):
    """Custom type gpsVCDAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GpsVCDAC_Type.__name__ = "Integer32"
_GpsVCDAC_Object = MibScalar
gpsVCDAC = _GpsVCDAC_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 5),
    _GpsVCDAC_Type()
)
gpsVCDAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsVCDAC.setStatus("current")


class _GpsAvgCarrierToNoiseRatiodB_Type(DisplayString):
    """Custom type gpsAvgCarrierToNoiseRatiodB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GpsAvgCarrierToNoiseRatiodB_Type.__name__ = "DisplayString"
_GpsAvgCarrierToNoiseRatiodB_Object = MibScalar
gpsAvgCarrierToNoiseRatiodB = _GpsAvgCarrierToNoiseRatiodB_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 6),
    _GpsAvgCarrierToNoiseRatiodB_Type()
)
gpsAvgCarrierToNoiseRatiodB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAvgCarrierToNoiseRatiodB.setStatus("current")


class _GpsReferencePosition_Type(DisplayString):
    """Custom type gpsReferencePosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_GpsReferencePosition_Type.__name__ = "DisplayString"
_GpsReferencePosition_Object = MibScalar
gpsReferencePosition = _GpsReferencePosition_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 7),
    _GpsReferencePosition_Type()
)
gpsReferencePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReferencePosition.setStatus("current")


class _GpsRefPosSource_Type(DisplayString):
    """Custom type gpsRefPosSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_GpsRefPosSource_Type.__name__ = "DisplayString"
_GpsRefPosSource_Object = MibScalar
gpsRefPosSource = _GpsRefPosSource_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 8),
    _GpsRefPosSource_Type()
)
gpsRefPosSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRefPosSource.setStatus("current")
_GpsCurrentLeapSeconds_Type = Integer32
_GpsCurrentLeapSeconds_Object = MibScalar
gpsCurrentLeapSeconds = _GpsCurrentLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 9),
    _GpsCurrentLeapSeconds_Type()
)
gpsCurrentLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsCurrentLeapSeconds.setStatus("current")
_GpsFutureLeapSeconds_Type = Integer32
_GpsFutureLeapSeconds_Object = MibScalar
gpsFutureLeapSeconds = _GpsFutureLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 10),
    _GpsFutureLeapSeconds_Type()
)
gpsFutureLeapSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFutureLeapSeconds.setStatus("current")


class _GpsVersion_Type(DisplayString):
    """Custom type gpsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GpsVersion_Type.__name__ = "DisplayString"
_GpsVersion_Object = MibScalar
gpsVersion = _GpsVersion_Object(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 11),
    _GpsVersion_Type()
)
gpsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsVersion.setStatus("current")

# Managed Objects groups


# Notification objects

cntpTrapLeapIndBitsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 0, 1)
)
cntpTrapLeapIndBitsChange.setObjects(
    ("ENDRUNTECHNOLOGIES-MIB", "cntpLeapIndBits")
)
if mibBuilder.loadTexts:
    cntpTrapLeapIndBitsChange.setStatus(
        "current"
    )

cntpTrapStratumChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 1, 0, 0, 2)
)
cntpTrapStratumChange.setObjects(
    ("ENDRUNTECHNOLOGIES-MIB", "cntpStratum")
)
if mibBuilder.loadTexts:
    cntpTrapStratumChange.setStatus(
        "current"
    )

cdmaTrapFaultStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 1, 1, 0, 1)
)
cdmaTrapFaultStatusChange.setObjects(
    ("ENDRUNTECHNOLOGIES-MIB", "cdmaFaultStatus")
)
if mibBuilder.loadTexts:
    cdmaTrapFaultStatusChange.setStatus(
        "current"
    )

gntpTrapLeapIndBitsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 0, 1)
)
gntpTrapLeapIndBitsChange.setObjects(
    ("ENDRUNTECHNOLOGIES-MIB", "gntpLeapIndBits")
)
if mibBuilder.loadTexts:
    gntpTrapLeapIndBitsChange.setStatus(
        "current"
    )

gntpTrapStratumChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 2, 0, 0, 2)
)
gntpTrapStratumChange.setObjects(
    ("ENDRUNTECHNOLOGIES-MIB", "gntpStratum")
)
if mibBuilder.loadTexts:
    gntpTrapStratumChange.setStatus(
        "current"
    )

gpsTrapFaultStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13827, 2, 1, 0, 1)
)
gpsTrapFaultStatusChange.setObjects(
    ("ENDRUNTECHNOLOGIES-MIB", "gpsFaultStatus")
)
if mibBuilder.loadTexts:
    gpsTrapFaultStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDRUNTECHNOLOGIES-MIB",
    **{"endRunTechnologiesMIB": endRunTechnologiesMIB,
       "endRunTechnologies": endRunTechnologies,
       "praecisCntp": praecisCntp,
       "cntp": cntp,
       "cntptrap": cntptrap,
       "cntpTrapLeapIndBitsChange": cntpTrapLeapIndBitsChange,
       "cntpTrapStratumChange": cntpTrapStratumChange,
       "cntpRxPkts": cntpRxPkts,
       "cntpTxPkts": cntpTxPkts,
       "cntpIgnoredPkts": cntpIgnoredPkts,
       "cntpDroppedPkts": cntpDroppedPkts,
       "cntpAuthFail": cntpAuthFail,
       "cntpTimeFigureOfMerit": cntpTimeFigureOfMerit,
       "cntpLeapIndBits": cntpLeapIndBits,
       "cntpSyncSource": cntpSyncSource,
       "cntpOffsetToCDMAReference": cntpOffsetToCDMAReference,
       "cntpStratum": cntpStratum,
       "cntpVersion": cntpVersion,
       "cdma": cdma,
       "cdmatrap": cdmatrap,
       "cdmaTrapFaultStatusChange": cdmaTrapFaultStatusChange,
       "cdmaFaultStatus": cdmaFaultStatus,
       "cdmaTimeFigureOfMerit": cdmaTimeFigureOfMerit,
       "cdmaSigProcState": cdmaSigProcState,
       "cdmaChannel": cdmaChannel,
       "cdmaPNO": cdmaPNO,
       "cdmaAGC": cdmaAGC,
       "cdmaVCDAC": cdmaVCDAC,
       "cdmaCarrierToNoiseRatio": cdmaCarrierToNoiseRatio,
       "cdmaFrameErrorRate": cdmaFrameErrorRate,
       "cdmaLeapMode": cdmaLeapMode,
       "cdmaCurrentLeapSeconds": cdmaCurrentLeapSeconds,
       "cdmaFutureLeapSeconds": cdmaFutureLeapSeconds,
       "cdmaVersion": cdmaVersion,
       "praecisGntp": praecisGntp,
       "gntp": gntp,
       "gntptrap": gntptrap,
       "gntpTrapLeapIndBitsChange": gntpTrapLeapIndBitsChange,
       "gntpTrapStratumChange": gntpTrapStratumChange,
       "gntpRxPkts": gntpRxPkts,
       "gntpTxPkts": gntpTxPkts,
       "gntpIgnoredPkts": gntpIgnoredPkts,
       "gntpDroppedPkts": gntpDroppedPkts,
       "gntpAuthFail": gntpAuthFail,
       "gntpTimeFigureOfMerit": gntpTimeFigureOfMerit,
       "gntpLeapIndBits": gntpLeapIndBits,
       "gntpSyncSource": gntpSyncSource,
       "gntpOffsetToGPSReference": gntpOffsetToGPSReference,
       "gntpStratum": gntpStratum,
       "gntpVersion": gntpVersion,
       "gps": gps,
       "gpstrap": gpstrap,
       "gpsTrapFaultStatusChange": gpsTrapFaultStatusChange,
       "gpsFaultStatus": gpsFaultStatus,
       "gpsTimeFigureOfMerit": gpsTimeFigureOfMerit,
       "gpsSigProcState": gpsSigProcState,
       "gpsNumTrackSats": gpsNumTrackSats,
       "gpsVCDAC": gpsVCDAC,
       "gpsAvgCarrierToNoiseRatiodB": gpsAvgCarrierToNoiseRatiodB,
       "gpsReferencePosition": gpsReferencePosition,
       "gpsRefPosSource": gpsRefPosSource,
       "gpsCurrentLeapSeconds": gpsCurrentLeapSeconds,
       "gpsFutureLeapSeconds": gpsFutureLeapSeconds,
       "gpsVersion": gpsVersion}
)
