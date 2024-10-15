# SNMP MIB module (IEEE8021-AS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-AS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:11 2024
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

(IEEE8021BridgePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber")

(InterfaceIndexOrZero,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifGeneralInformationGroup")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ieee8021AsTimeSyncMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20)
)
ieee8021AsTimeSyncMib.setRevisions(
        ("2012-12-12 00:00",
         "2010-11-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClockIdentity(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class IEEE8021ASClockClassValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              13,
              14,
              52,
              58,
              187,
              193,
              248,
              255)
        )
    )
    namedValues = NamedValues(
        *(("applicationSpecficAlternativeB", 193),
          ("applicationSpecficSyncLost", 14),
          ("applicationSpecificAlternativeA", 58),
          ("applicationSpecificSync", 13),
          ("defaultClock", 248),
          ("primarySync", 6),
          ("primarySyncAlternativeA", 52),
          ("primarySyncAlternativeB", 187),
          ("primarySyncLost", 7),
          ("slaveOnlyClock", 255))
    )



class IEEE8021ASClockAccuracyValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              254)
        )
    )
    namedValues = NamedValues(
        *(("timeAccurateTo100ms", 45),
          ("timeAccurateTo100ns", 33),
          ("timeAccurateTo100us", 39),
          ("timeAccurateTo10ms", 43),
          ("timeAccurateTo10s", 48),
          ("timeAccurateTo10us", 37),
          ("timeAccurateTo1ms", 41),
          ("timeAccurateTo1s", 47),
          ("timeAccurateTo1us", 35),
          ("timeAccurateTo250ms", 46),
          ("timeAccurateTo250ns", 34),
          ("timeAccurateTo250us", 40),
          ("timeAccurateTo25ms", 44),
          ("timeAccurateTo25ns", 32),
          ("timeAccurateTo25us", 38),
          ("timeAccurateTo2dot5ms", 42),
          ("timeAccurateTo2dot5us", 36),
          ("timeAccurateToGT10s", 49),
          ("timeAccurateToUnknown", 254))
    )



class IEEE8021ASTimeSourceValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("handSet", 96),
          ("internalOscillator", 160),
          ("ntp", 80),
          ("other", 144),
          ("ptp", 64),
          ("terrestrialRadio", 48))
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021AsMIBObjects_ObjectIdentity = ObjectIdentity
ieee8021AsMIBObjects = _Ieee8021AsMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 1)
)
_Ieee8021AsDefaultDS_ObjectIdentity = ObjectIdentity
ieee8021AsDefaultDS = _Ieee8021AsDefaultDS_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1)
)
_Ieee8021AsDefaultDSClockIdentity_Type = ClockIdentity
_Ieee8021AsDefaultDSClockIdentity_Object = MibScalar
ieee8021AsDefaultDSClockIdentity = _Ieee8021AsDefaultDSClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 1),
    _Ieee8021AsDefaultDSClockIdentity_Type()
)
ieee8021AsDefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSClockIdentity.setStatus("current")


class _Ieee8021AsDefaultDSNumberPorts_Type(Unsigned32):
    """Custom type ieee8021AsDefaultDSNumberPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsDefaultDSNumberPorts_Type.__name__ = "Unsigned32"
_Ieee8021AsDefaultDSNumberPorts_Object = MibScalar
ieee8021AsDefaultDSNumberPorts = _Ieee8021AsDefaultDSNumberPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 2),
    _Ieee8021AsDefaultDSNumberPorts_Type()
)
ieee8021AsDefaultDSNumberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSNumberPorts.setStatus("current")


class _Ieee8021AsDefaultDSClockClass_Type(IEEE8021ASClockClassValue):
    """Custom type ieee8021AsDefaultDSClockClass based on IEEE8021ASClockClassValue"""


_Ieee8021AsDefaultDSClockClass_Object = MibScalar
ieee8021AsDefaultDSClockClass = _Ieee8021AsDefaultDSClockClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 3),
    _Ieee8021AsDefaultDSClockClass_Type()
)
ieee8021AsDefaultDSClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSClockClass.setStatus("current")
_Ieee8021AsDefaultDSClockAccuracy_Type = IEEE8021ASClockAccuracyValue
_Ieee8021AsDefaultDSClockAccuracy_Object = MibScalar
ieee8021AsDefaultDSClockAccuracy = _Ieee8021AsDefaultDSClockAccuracy_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 4),
    _Ieee8021AsDefaultDSClockAccuracy_Type()
)
ieee8021AsDefaultDSClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSClockAccuracy.setStatus("current")


class _Ieee8021AsDefaultDSOffsetScaledLogVariance_Type(Unsigned32):
    """Custom type ieee8021AsDefaultDSOffsetScaledLogVariance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsDefaultDSOffsetScaledLogVariance_Type.__name__ = "Unsigned32"
_Ieee8021AsDefaultDSOffsetScaledLogVariance_Object = MibScalar
ieee8021AsDefaultDSOffsetScaledLogVariance = _Ieee8021AsDefaultDSOffsetScaledLogVariance_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 5),
    _Ieee8021AsDefaultDSOffsetScaledLogVariance_Type()
)
ieee8021AsDefaultDSOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSOffsetScaledLogVariance.setStatus("current")


class _Ieee8021AsDefaultDSPriority1_Type(Unsigned32):
    """Custom type ieee8021AsDefaultDSPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsDefaultDSPriority1_Type.__name__ = "Unsigned32"
_Ieee8021AsDefaultDSPriority1_Object = MibScalar
ieee8021AsDefaultDSPriority1 = _Ieee8021AsDefaultDSPriority1_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 6),
    _Ieee8021AsDefaultDSPriority1_Type()
)
ieee8021AsDefaultDSPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSPriority1.setStatus("current")


class _Ieee8021AsDefaultDSPriority2_Type(Unsigned32):
    """Custom type ieee8021AsDefaultDSPriority2 based on Unsigned32"""
    defaultValue = 248

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsDefaultDSPriority2_Type.__name__ = "Unsigned32"
_Ieee8021AsDefaultDSPriority2_Object = MibScalar
ieee8021AsDefaultDSPriority2 = _Ieee8021AsDefaultDSPriority2_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 7),
    _Ieee8021AsDefaultDSPriority2_Type()
)
ieee8021AsDefaultDSPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSPriority2.setStatus("current")
_Ieee8021AsDefaultDSGmCapable_Type = TruthValue
_Ieee8021AsDefaultDSGmCapable_Object = MibScalar
ieee8021AsDefaultDSGmCapable = _Ieee8021AsDefaultDSGmCapable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 8),
    _Ieee8021AsDefaultDSGmCapable_Type()
)
ieee8021AsDefaultDSGmCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSGmCapable.setStatus("current")


class _Ieee8021AsDefaultDSCurrentUTCOffset_Type(Integer32):
    """Custom type ieee8021AsDefaultDSCurrentUTCOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Ieee8021AsDefaultDSCurrentUTCOffset_Type.__name__ = "Integer32"
_Ieee8021AsDefaultDSCurrentUTCOffset_Object = MibScalar
ieee8021AsDefaultDSCurrentUTCOffset = _Ieee8021AsDefaultDSCurrentUTCOffset_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 9),
    _Ieee8021AsDefaultDSCurrentUTCOffset_Type()
)
ieee8021AsDefaultDSCurrentUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSCurrentUTCOffset.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSCurrentUTCOffset.setUnits("seconds")
_Ieee8021AsDefaultDSCurrentUTCOffsetValid_Type = TruthValue
_Ieee8021AsDefaultDSCurrentUTCOffsetValid_Object = MibScalar
ieee8021AsDefaultDSCurrentUTCOffsetValid = _Ieee8021AsDefaultDSCurrentUTCOffsetValid_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 10),
    _Ieee8021AsDefaultDSCurrentUTCOffsetValid_Type()
)
ieee8021AsDefaultDSCurrentUTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSCurrentUTCOffsetValid.setStatus("current")
_Ieee8021AsDefaultDSLeap59_Type = TruthValue
_Ieee8021AsDefaultDSLeap59_Object = MibScalar
ieee8021AsDefaultDSLeap59 = _Ieee8021AsDefaultDSLeap59_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 11),
    _Ieee8021AsDefaultDSLeap59_Type()
)
ieee8021AsDefaultDSLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSLeap59.setStatus("current")
_Ieee8021AsDefaultDSLeap61_Type = TruthValue
_Ieee8021AsDefaultDSLeap61_Object = MibScalar
ieee8021AsDefaultDSLeap61 = _Ieee8021AsDefaultDSLeap61_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 12),
    _Ieee8021AsDefaultDSLeap61_Type()
)
ieee8021AsDefaultDSLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSLeap61.setStatus("current")
_Ieee8021AsDefaultDSTimeTraceable_Type = TruthValue
_Ieee8021AsDefaultDSTimeTraceable_Object = MibScalar
ieee8021AsDefaultDSTimeTraceable = _Ieee8021AsDefaultDSTimeTraceable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 13),
    _Ieee8021AsDefaultDSTimeTraceable_Type()
)
ieee8021AsDefaultDSTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSTimeTraceable.setStatus("current")
_Ieee8021AsDefaultDSFrequencyTraceable_Type = TruthValue
_Ieee8021AsDefaultDSFrequencyTraceable_Object = MibScalar
ieee8021AsDefaultDSFrequencyTraceable = _Ieee8021AsDefaultDSFrequencyTraceable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 14),
    _Ieee8021AsDefaultDSFrequencyTraceable_Type()
)
ieee8021AsDefaultDSFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSFrequencyTraceable.setStatus("current")
_Ieee8021AsDefaultDSTimeSource_Type = IEEE8021ASTimeSourceValue
_Ieee8021AsDefaultDSTimeSource_Object = MibScalar
ieee8021AsDefaultDSTimeSource = _Ieee8021AsDefaultDSTimeSource_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 1, 15),
    _Ieee8021AsDefaultDSTimeSource_Type()
)
ieee8021AsDefaultDSTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsDefaultDSTimeSource.setStatus("current")
_Ieee8021AsCurrentDS_ObjectIdentity = ObjectIdentity
ieee8021AsCurrentDS = _Ieee8021AsCurrentDS_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2)
)


class _Ieee8021AsCurrentDSStepsRemoved_Type(Integer32):
    """Custom type ieee8021AsCurrentDSStepsRemoved based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Ieee8021AsCurrentDSStepsRemoved_Type.__name__ = "Integer32"
_Ieee8021AsCurrentDSStepsRemoved_Object = MibScalar
ieee8021AsCurrentDSStepsRemoved = _Ieee8021AsCurrentDSStepsRemoved_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 1),
    _Ieee8021AsCurrentDSStepsRemoved_Type()
)
ieee8021AsCurrentDSStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSStepsRemoved.setStatus("current")
_Ieee8021AsCurrentDSOffsetFromMasterHs_Type = Integer32
_Ieee8021AsCurrentDSOffsetFromMasterHs_Object = MibScalar
ieee8021AsCurrentDSOffsetFromMasterHs = _Ieee8021AsCurrentDSOffsetFromMasterHs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 2),
    _Ieee8021AsCurrentDSOffsetFromMasterHs_Type()
)
ieee8021AsCurrentDSOffsetFromMasterHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSOffsetFromMasterHs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSOffsetFromMasterHs.setUnits("2**-16 ns * 2**64")
_Ieee8021AsCurrentDSOffsetFromMasterMs_Type = Integer32
_Ieee8021AsCurrentDSOffsetFromMasterMs_Object = MibScalar
ieee8021AsCurrentDSOffsetFromMasterMs = _Ieee8021AsCurrentDSOffsetFromMasterMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 3),
    _Ieee8021AsCurrentDSOffsetFromMasterMs_Type()
)
ieee8021AsCurrentDSOffsetFromMasterMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSOffsetFromMasterMs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSOffsetFromMasterMs.setUnits("2**-16 ns * 2**32")
_Ieee8021AsCurrentDSOffsetFromMasterLs_Type = Integer32
_Ieee8021AsCurrentDSOffsetFromMasterLs_Object = MibScalar
ieee8021AsCurrentDSOffsetFromMasterLs = _Ieee8021AsCurrentDSOffsetFromMasterLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 4),
    _Ieee8021AsCurrentDSOffsetFromMasterLs_Type()
)
ieee8021AsCurrentDSOffsetFromMasterLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSOffsetFromMasterLs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSOffsetFromMasterLs.setUnits("2**-16 ns")
_Ieee8021AsCurrentDSLastGmPhaseChangeHs_Type = Integer32
_Ieee8021AsCurrentDSLastGmPhaseChangeHs_Object = MibScalar
ieee8021AsCurrentDSLastGmPhaseChangeHs = _Ieee8021AsCurrentDSLastGmPhaseChangeHs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 5),
    _Ieee8021AsCurrentDSLastGmPhaseChangeHs_Type()
)
ieee8021AsCurrentDSLastGmPhaseChangeHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSLastGmPhaseChangeHs.setStatus("current")
_Ieee8021AsCurrentDSLastGmPhaseChangeMs_Type = Unsigned32
_Ieee8021AsCurrentDSLastGmPhaseChangeMs_Object = MibScalar
ieee8021AsCurrentDSLastGmPhaseChangeMs = _Ieee8021AsCurrentDSLastGmPhaseChangeMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 6),
    _Ieee8021AsCurrentDSLastGmPhaseChangeMs_Type()
)
ieee8021AsCurrentDSLastGmPhaseChangeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSLastGmPhaseChangeMs.setStatus("current")
_Ieee8021AsCurrentDSLastGmPhaseChangeLs_Type = Unsigned32
_Ieee8021AsCurrentDSLastGmPhaseChangeLs_Object = MibScalar
ieee8021AsCurrentDSLastGmPhaseChangeLs = _Ieee8021AsCurrentDSLastGmPhaseChangeLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 7),
    _Ieee8021AsCurrentDSLastGmPhaseChangeLs_Type()
)
ieee8021AsCurrentDSLastGmPhaseChangeLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSLastGmPhaseChangeLs.setStatus("current")
_Ieee8021AsCurrentDSLastGmFreqChangeMs_Type = Integer32
_Ieee8021AsCurrentDSLastGmFreqChangeMs_Object = MibScalar
ieee8021AsCurrentDSLastGmFreqChangeMs = _Ieee8021AsCurrentDSLastGmFreqChangeMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 8),
    _Ieee8021AsCurrentDSLastGmFreqChangeMs_Type()
)
ieee8021AsCurrentDSLastGmFreqChangeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSLastGmFreqChangeMs.setStatus("current")
_Ieee8021AsCurrentDSLastGmFreqChangeLs_Type = Unsigned32
_Ieee8021AsCurrentDSLastGmFreqChangeLs_Object = MibScalar
ieee8021AsCurrentDSLastGmFreqChangeLs = _Ieee8021AsCurrentDSLastGmFreqChangeLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 9),
    _Ieee8021AsCurrentDSLastGmFreqChangeLs_Type()
)
ieee8021AsCurrentDSLastGmFreqChangeLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSLastGmFreqChangeLs.setStatus("current")


class _Ieee8021AsCurrentDSGmTimebaseIndicator_Type(Unsigned32):
    """Custom type ieee8021AsCurrentDSGmTimebaseIndicator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsCurrentDSGmTimebaseIndicator_Type.__name__ = "Unsigned32"
_Ieee8021AsCurrentDSGmTimebaseIndicator_Object = MibScalar
ieee8021AsCurrentDSGmTimebaseIndicator = _Ieee8021AsCurrentDSGmTimebaseIndicator_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 10),
    _Ieee8021AsCurrentDSGmTimebaseIndicator_Type()
)
ieee8021AsCurrentDSGmTimebaseIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSGmTimebaseIndicator.setStatus("current")
_Ieee8021AsCurrentDSGmChangeCount_Type = Counter32
_Ieee8021AsCurrentDSGmChangeCount_Object = MibScalar
ieee8021AsCurrentDSGmChangeCount = _Ieee8021AsCurrentDSGmChangeCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 11),
    _Ieee8021AsCurrentDSGmChangeCount_Type()
)
ieee8021AsCurrentDSGmChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSGmChangeCount.setStatus("current")
_Ieee8021AsCurrentDSTimeOfLastGmChangeEvent_Type = TimeStamp
_Ieee8021AsCurrentDSTimeOfLastGmChangeEvent_Object = MibScalar
ieee8021AsCurrentDSTimeOfLastGmChangeEvent = _Ieee8021AsCurrentDSTimeOfLastGmChangeEvent_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 12),
    _Ieee8021AsCurrentDSTimeOfLastGmChangeEvent_Type()
)
ieee8021AsCurrentDSTimeOfLastGmChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSTimeOfLastGmChangeEvent.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSTimeOfLastGmChangeEvent.setUnits("0.01 seconds")
_Ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent_Type = TimeStamp
_Ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent_Object = MibScalar
ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent = _Ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 13),
    _Ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent_Type()
)
ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent.setUnits("0.01 seconds")
_Ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent_Type = TimeStamp
_Ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent_Object = MibScalar
ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent = _Ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 2, 14),
    _Ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent_Type()
)
ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent.setUnits("0.01 seconds")
_Ieee8021AsParentDS_ObjectIdentity = ObjectIdentity
ieee8021AsParentDS = _Ieee8021AsParentDS_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3)
)
_Ieee8021AsParentDSParentClockIdentity_Type = ClockIdentity
_Ieee8021AsParentDSParentClockIdentity_Object = MibScalar
ieee8021AsParentDSParentClockIdentity = _Ieee8021AsParentDSParentClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 1),
    _Ieee8021AsParentDSParentClockIdentity_Type()
)
ieee8021AsParentDSParentClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsParentDSParentClockIdentity.setStatus("current")


class _Ieee8021AsParentDSParentPortNumber_Type(Unsigned32):
    """Custom type ieee8021AsParentDSParentPortNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsParentDSParentPortNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsParentDSParentPortNumber_Object = MibScalar
ieee8021AsParentDSParentPortNumber = _Ieee8021AsParentDSParentPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 2),
    _Ieee8021AsParentDSParentPortNumber_Type()
)
ieee8021AsParentDSParentPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsParentDSParentPortNumber.setStatus("current")
_Ieee8021AsParentDSCumlativeRateRatio_Type = Integer32
_Ieee8021AsParentDSCumlativeRateRatio_Object = MibScalar
ieee8021AsParentDSCumlativeRateRatio = _Ieee8021AsParentDSCumlativeRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 3),
    _Ieee8021AsParentDSCumlativeRateRatio_Type()
)
ieee8021AsParentDSCumlativeRateRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsParentDSCumlativeRateRatio.setStatus("current")
_Ieee8021AsParentDSGrandmasterIdentity_Type = ClockIdentity
_Ieee8021AsParentDSGrandmasterIdentity_Object = MibScalar
ieee8021AsParentDSGrandmasterIdentity = _Ieee8021AsParentDSGrandmasterIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 4),
    _Ieee8021AsParentDSGrandmasterIdentity_Type()
)
ieee8021AsParentDSGrandmasterIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsParentDSGrandmasterIdentity.setStatus("current")
_Ieee8021AsParentDSGrandmasterClockClass_Type = IEEE8021ASClockClassValue
_Ieee8021AsParentDSGrandmasterClockClass_Object = MibScalar
ieee8021AsParentDSGrandmasterClockClass = _Ieee8021AsParentDSGrandmasterClockClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 5),
    _Ieee8021AsParentDSGrandmasterClockClass_Type()
)
ieee8021AsParentDSGrandmasterClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsParentDSGrandmasterClockClass.setStatus("current")
_Ieee8021AsParentDSGrandmasterClockAccuracy_Type = IEEE8021ASClockAccuracyValue
_Ieee8021AsParentDSGrandmasterClockAccuracy_Object = MibScalar
ieee8021AsParentDSGrandmasterClockAccuracy = _Ieee8021AsParentDSGrandmasterClockAccuracy_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 6),
    _Ieee8021AsParentDSGrandmasterClockAccuracy_Type()
)
ieee8021AsParentDSGrandmasterClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsParentDSGrandmasterClockAccuracy.setStatus("current")


class _Ieee8021AsParentDSGrandmasterOffsetScaledLogVariance_Type(Unsigned32):
    """Custom type ieee8021AsParentDSGrandmasterOffsetScaledLogVariance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsParentDSGrandmasterOffsetScaledLogVariance_Type.__name__ = "Unsigned32"
_Ieee8021AsParentDSGrandmasterOffsetScaledLogVariance_Object = MibScalar
ieee8021AsParentDSGrandmasterOffsetScaledLogVariance = _Ieee8021AsParentDSGrandmasterOffsetScaledLogVariance_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 7),
    _Ieee8021AsParentDSGrandmasterOffsetScaledLogVariance_Type()
)
ieee8021AsParentDSGrandmasterOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsParentDSGrandmasterOffsetScaledLogVariance.setStatus("current")


class _Ieee8021AsParentDSGrandmasterPriority1_Type(Unsigned32):
    """Custom type ieee8021AsParentDSGrandmasterPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsParentDSGrandmasterPriority1_Type.__name__ = "Unsigned32"
_Ieee8021AsParentDSGrandmasterPriority1_Object = MibScalar
ieee8021AsParentDSGrandmasterPriority1 = _Ieee8021AsParentDSGrandmasterPriority1_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 8),
    _Ieee8021AsParentDSGrandmasterPriority1_Type()
)
ieee8021AsParentDSGrandmasterPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsParentDSGrandmasterPriority1.setStatus("current")


class _Ieee8021AsParentDSGrandmasterPriority2_Type(Unsigned32):
    """Custom type ieee8021AsParentDSGrandmasterPriority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsParentDSGrandmasterPriority2_Type.__name__ = "Unsigned32"
_Ieee8021AsParentDSGrandmasterPriority2_Object = MibScalar
ieee8021AsParentDSGrandmasterPriority2 = _Ieee8021AsParentDSGrandmasterPriority2_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 3, 9),
    _Ieee8021AsParentDSGrandmasterPriority2_Type()
)
ieee8021AsParentDSGrandmasterPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsParentDSGrandmasterPriority2.setStatus("current")
_Ieee8021AsTimePropertiesDS_ObjectIdentity = ObjectIdentity
ieee8021AsTimePropertiesDS = _Ieee8021AsTimePropertiesDS_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 4)
)


class _Ieee8021AsTimePropertiesDSCurrentUtcOffset_Type(Integer32):
    """Custom type ieee8021AsTimePropertiesDSCurrentUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Ieee8021AsTimePropertiesDSCurrentUtcOffset_Type.__name__ = "Integer32"
_Ieee8021AsTimePropertiesDSCurrentUtcOffset_Object = MibScalar
ieee8021AsTimePropertiesDSCurrentUtcOffset = _Ieee8021AsTimePropertiesDSCurrentUtcOffset_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 4, 1),
    _Ieee8021AsTimePropertiesDSCurrentUtcOffset_Type()
)
ieee8021AsTimePropertiesDSCurrentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsTimePropertiesDSCurrentUtcOffset.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsTimePropertiesDSCurrentUtcOffset.setUnits("seconds")
_Ieee8021AsTimePropertiesDSCurrentUtcOffsetValid_Type = TruthValue
_Ieee8021AsTimePropertiesDSCurrentUtcOffsetValid_Object = MibScalar
ieee8021AsTimePropertiesDSCurrentUtcOffsetValid = _Ieee8021AsTimePropertiesDSCurrentUtcOffsetValid_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 4, 2),
    _Ieee8021AsTimePropertiesDSCurrentUtcOffsetValid_Type()
)
ieee8021AsTimePropertiesDSCurrentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsTimePropertiesDSCurrentUtcOffsetValid.setStatus("current")
_Ieee8021AsTimePropertiesDSLeap59_Type = TruthValue
_Ieee8021AsTimePropertiesDSLeap59_Object = MibScalar
ieee8021AsTimePropertiesDSLeap59 = _Ieee8021AsTimePropertiesDSLeap59_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 4, 3),
    _Ieee8021AsTimePropertiesDSLeap59_Type()
)
ieee8021AsTimePropertiesDSLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsTimePropertiesDSLeap59.setStatus("current")
_Ieee8021AsTimePropertiesDSLeap61_Type = TruthValue
_Ieee8021AsTimePropertiesDSLeap61_Object = MibScalar
ieee8021AsTimePropertiesDSLeap61 = _Ieee8021AsTimePropertiesDSLeap61_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 4, 4),
    _Ieee8021AsTimePropertiesDSLeap61_Type()
)
ieee8021AsTimePropertiesDSLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsTimePropertiesDSLeap61.setStatus("current")
_Ieee8021AsTimePropertiesDSTimeTraceable_Type = TruthValue
_Ieee8021AsTimePropertiesDSTimeTraceable_Object = MibScalar
ieee8021AsTimePropertiesDSTimeTraceable = _Ieee8021AsTimePropertiesDSTimeTraceable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 4, 5),
    _Ieee8021AsTimePropertiesDSTimeTraceable_Type()
)
ieee8021AsTimePropertiesDSTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsTimePropertiesDSTimeTraceable.setStatus("current")
_Ieee8021AsTimePropertiesDSFrequencyTraceable_Type = TruthValue
_Ieee8021AsTimePropertiesDSFrequencyTraceable_Object = MibScalar
ieee8021AsTimePropertiesDSFrequencyTraceable = _Ieee8021AsTimePropertiesDSFrequencyTraceable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 4, 6),
    _Ieee8021AsTimePropertiesDSFrequencyTraceable_Type()
)
ieee8021AsTimePropertiesDSFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsTimePropertiesDSFrequencyTraceable.setStatus("current")
_Ieee8021AsTimePropertiesDSTimeSource_Type = IEEE8021ASTimeSourceValue
_Ieee8021AsTimePropertiesDSTimeSource_Object = MibScalar
ieee8021AsTimePropertiesDSTimeSource = _Ieee8021AsTimePropertiesDSTimeSource_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 4, 7),
    _Ieee8021AsTimePropertiesDSTimeSource_Type()
)
ieee8021AsTimePropertiesDSTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsTimePropertiesDSTimeSource.setStatus("current")
_Ieee8021AsPortDSIfTable_Object = MibTable
ieee8021AsPortDSIfTable = _Ieee8021AsPortDSIfTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021AsPortDSIfTable.setStatus("current")
_Ieee8021AsPortDSIfEntry_Object = MibTableRow
ieee8021AsPortDSIfEntry = _Ieee8021AsPortDSIfEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1)
)
ieee8021AsPortDSIfEntry.setIndexNames(
    (0, "IEEE8021-AS-MIB", "ieee8021AsBridgeBasePort"),
    (0, "IEEE8021-AS-MIB", "ieee8021AsPortDSAsIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsPortDSIfEntry.setStatus("current")
_Ieee8021AsBridgeBasePort_Type = IEEE8021BridgePortNumber
_Ieee8021AsBridgeBasePort_Object = MibTableColumn
ieee8021AsBridgeBasePort = _Ieee8021AsBridgeBasePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 1),
    _Ieee8021AsBridgeBasePort_Type()
)
ieee8021AsBridgeBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsBridgeBasePort.setStatus("current")
_Ieee8021AsPortDSAsIfIndex_Type = InterfaceIndexOrZero
_Ieee8021AsPortDSAsIfIndex_Object = MibTableColumn
ieee8021AsPortDSAsIfIndex = _Ieee8021AsPortDSAsIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 2),
    _Ieee8021AsPortDSAsIfIndex_Type()
)
ieee8021AsPortDSAsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsPortDSAsIfIndex.setStatus("current")
_Ieee8021AsPortDSClockIdentity_Type = ClockIdentity
_Ieee8021AsPortDSClockIdentity_Object = MibTableColumn
ieee8021AsPortDSClockIdentity = _Ieee8021AsPortDSClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 3),
    _Ieee8021AsPortDSClockIdentity_Type()
)
ieee8021AsPortDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSClockIdentity.setStatus("current")


class _Ieee8021AsPortDSPortNumber_Type(Unsigned32):
    """Custom type ieee8021AsPortDSPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsPortDSPortNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsPortDSPortNumber_Object = MibTableColumn
ieee8021AsPortDSPortNumber = _Ieee8021AsPortDSPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 4),
    _Ieee8021AsPortDSPortNumber_Type()
)
ieee8021AsPortDSPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSPortNumber.setStatus("current")


class _Ieee8021AsPortDSPortRole_Type(Integer32):
    """Custom type ieee8021AsPortDSPortRole based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 3),
          ("masterPort", 6),
          ("passivePort", 7),
          ("slavePort", 9))
    )


_Ieee8021AsPortDSPortRole_Type.__name__ = "Integer32"
_Ieee8021AsPortDSPortRole_Object = MibTableColumn
ieee8021AsPortDSPortRole = _Ieee8021AsPortDSPortRole_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 5),
    _Ieee8021AsPortDSPortRole_Type()
)
ieee8021AsPortDSPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSPortRole.setStatus("current")


class _Ieee8021AsPortDSPttPortEnabled_Type(TruthValue):
    """Custom type ieee8021AsPortDSPttPortEnabled based on TruthValue"""
    defaultValue = 1


_Ieee8021AsPortDSPttPortEnabled_Object = MibTableColumn
ieee8021AsPortDSPttPortEnabled = _Ieee8021AsPortDSPttPortEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 6),
    _Ieee8021AsPortDSPttPortEnabled_Type()
)
ieee8021AsPortDSPttPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSPttPortEnabled.setStatus("current")


class _Ieee8021AsPortDSIsMeasuringDelay_Type(TruthValue):
    """Custom type ieee8021AsPortDSIsMeasuringDelay based on TruthValue"""
    defaultValue = 2


_Ieee8021AsPortDSIsMeasuringDelay_Object = MibTableColumn
ieee8021AsPortDSIsMeasuringDelay = _Ieee8021AsPortDSIsMeasuringDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 7),
    _Ieee8021AsPortDSIsMeasuringDelay_Type()
)
ieee8021AsPortDSIsMeasuringDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSIsMeasuringDelay.setStatus("current")
_Ieee8021AsPortDSAsCapable_Type = TruthValue
_Ieee8021AsPortDSAsCapable_Object = MibTableColumn
ieee8021AsPortDSAsCapable = _Ieee8021AsPortDSAsCapable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 8),
    _Ieee8021AsPortDSAsCapable_Type()
)
ieee8021AsPortDSAsCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSAsCapable.setStatus("current")


class _Ieee8021AsPortDSNeighborPropDelayHs_Type(Unsigned32):
    """Custom type ieee8021AsPortDSNeighborPropDelayHs based on Unsigned32"""
    defaultValue = 0


_Ieee8021AsPortDSNeighborPropDelayHs_Object = MibTableColumn
ieee8021AsPortDSNeighborPropDelayHs = _Ieee8021AsPortDSNeighborPropDelayHs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 9),
    _Ieee8021AsPortDSNeighborPropDelayHs_Type()
)
ieee8021AsPortDSNeighborPropDelayHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayHs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayHs.setUnits("2**-16 ns * 2**64")


class _Ieee8021AsPortDSNeighborPropDelayMs_Type(Unsigned32):
    """Custom type ieee8021AsPortDSNeighborPropDelayMs based on Unsigned32"""
    defaultValue = 0


_Ieee8021AsPortDSNeighborPropDelayMs_Object = MibTableColumn
ieee8021AsPortDSNeighborPropDelayMs = _Ieee8021AsPortDSNeighborPropDelayMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 10),
    _Ieee8021AsPortDSNeighborPropDelayMs_Type()
)
ieee8021AsPortDSNeighborPropDelayMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayMs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayMs.setUnits("2**-16 ns * 2**32")


class _Ieee8021AsPortDSNeighborPropDelayLs_Type(Unsigned32):
    """Custom type ieee8021AsPortDSNeighborPropDelayLs based on Unsigned32"""
    defaultValue = 0


_Ieee8021AsPortDSNeighborPropDelayLs_Object = MibTableColumn
ieee8021AsPortDSNeighborPropDelayLs = _Ieee8021AsPortDSNeighborPropDelayLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 11),
    _Ieee8021AsPortDSNeighborPropDelayLs_Type()
)
ieee8021AsPortDSNeighborPropDelayLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayLs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayLs.setUnits("2**-16 ns")
_Ieee8021AsPortDSNeighborPropDelayThreshHs_Type = Unsigned32
_Ieee8021AsPortDSNeighborPropDelayThreshHs_Object = MibTableColumn
ieee8021AsPortDSNeighborPropDelayThreshHs = _Ieee8021AsPortDSNeighborPropDelayThreshHs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 12),
    _Ieee8021AsPortDSNeighborPropDelayThreshHs_Type()
)
ieee8021AsPortDSNeighborPropDelayThreshHs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayThreshHs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayThreshHs.setUnits("2**-16 ns * 2 ** 64")
_Ieee8021AsPortDSNeighborPropDelayThreshMs_Type = Unsigned32
_Ieee8021AsPortDSNeighborPropDelayThreshMs_Object = MibTableColumn
ieee8021AsPortDSNeighborPropDelayThreshMs = _Ieee8021AsPortDSNeighborPropDelayThreshMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 13),
    _Ieee8021AsPortDSNeighborPropDelayThreshMs_Type()
)
ieee8021AsPortDSNeighborPropDelayThreshMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayThreshMs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayThreshMs.setUnits("2**-16 ns * 2 ** 32")
_Ieee8021AsPortDSNeighborPropDelayThreshLs_Type = Unsigned32
_Ieee8021AsPortDSNeighborPropDelayThreshLs_Object = MibTableColumn
ieee8021AsPortDSNeighborPropDelayThreshLs = _Ieee8021AsPortDSNeighborPropDelayThreshLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 14),
    _Ieee8021AsPortDSNeighborPropDelayThreshLs_Type()
)
ieee8021AsPortDSNeighborPropDelayThreshLs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayThreshLs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborPropDelayThreshLs.setUnits("2**-16 ns")
_Ieee8021AsPortDSDelayAsymmetryHs_Type = Integer32
_Ieee8021AsPortDSDelayAsymmetryHs_Object = MibTableColumn
ieee8021AsPortDSDelayAsymmetryHs = _Ieee8021AsPortDSDelayAsymmetryHs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 15),
    _Ieee8021AsPortDSDelayAsymmetryHs_Type()
)
ieee8021AsPortDSDelayAsymmetryHs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSDelayAsymmetryHs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSDelayAsymmetryHs.setUnits("2**-16 ns * 2**64")
_Ieee8021AsPortDSDelayAsymmetryMs_Type = Unsigned32
_Ieee8021AsPortDSDelayAsymmetryMs_Object = MibTableColumn
ieee8021AsPortDSDelayAsymmetryMs = _Ieee8021AsPortDSDelayAsymmetryMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 16),
    _Ieee8021AsPortDSDelayAsymmetryMs_Type()
)
ieee8021AsPortDSDelayAsymmetryMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSDelayAsymmetryMs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSDelayAsymmetryMs.setUnits("2**-16 ns * 2**32")
_Ieee8021AsPortDSDelayAsymmetryLs_Type = Unsigned32
_Ieee8021AsPortDSDelayAsymmetryLs_Object = MibTableColumn
ieee8021AsPortDSDelayAsymmetryLs = _Ieee8021AsPortDSDelayAsymmetryLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 17),
    _Ieee8021AsPortDSDelayAsymmetryLs_Type()
)
ieee8021AsPortDSDelayAsymmetryLs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSDelayAsymmetryLs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSDelayAsymmetryLs.setUnits("2**-16 ns")
_Ieee8021AsPortDSNeighborRateRatio_Type = Integer32
_Ieee8021AsPortDSNeighborRateRatio_Object = MibTableColumn
ieee8021AsPortDSNeighborRateRatio = _Ieee8021AsPortDSNeighborRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 18),
    _Ieee8021AsPortDSNeighborRateRatio_Type()
)
ieee8021AsPortDSNeighborRateRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNeighborRateRatio.setStatus("current")


class _Ieee8021AsPortDSInitialLogAnnounceInterval_Type(Integer32):
    """Custom type ieee8021AsPortDSInitialLogAnnounceInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsPortDSInitialLogAnnounceInterval_Type.__name__ = "Integer32"
_Ieee8021AsPortDSInitialLogAnnounceInterval_Object = MibTableColumn
ieee8021AsPortDSInitialLogAnnounceInterval = _Ieee8021AsPortDSInitialLogAnnounceInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 19),
    _Ieee8021AsPortDSInitialLogAnnounceInterval_Type()
)
ieee8021AsPortDSInitialLogAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSInitialLogAnnounceInterval.setStatus("current")


class _Ieee8021AsPortDSCurrentLogAnnounceInterval_Type(Integer32):
    """Custom type ieee8021AsPortDSCurrentLogAnnounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsPortDSCurrentLogAnnounceInterval_Type.__name__ = "Integer32"
_Ieee8021AsPortDSCurrentLogAnnounceInterval_Object = MibTableColumn
ieee8021AsPortDSCurrentLogAnnounceInterval = _Ieee8021AsPortDSCurrentLogAnnounceInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 20),
    _Ieee8021AsPortDSCurrentLogAnnounceInterval_Type()
)
ieee8021AsPortDSCurrentLogAnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSCurrentLogAnnounceInterval.setStatus("current")


class _Ieee8021AsPortDSAnnounceReceiptTimeout_Type(Unsigned32):
    """Custom type ieee8021AsPortDSAnnounceReceiptTimeout based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsPortDSAnnounceReceiptTimeout_Type.__name__ = "Unsigned32"
_Ieee8021AsPortDSAnnounceReceiptTimeout_Object = MibTableColumn
ieee8021AsPortDSAnnounceReceiptTimeout = _Ieee8021AsPortDSAnnounceReceiptTimeout_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 21),
    _Ieee8021AsPortDSAnnounceReceiptTimeout_Type()
)
ieee8021AsPortDSAnnounceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSAnnounceReceiptTimeout.setStatus("current")


class _Ieee8021AsPortDSInitialLogSyncInterval_Type(Integer32):
    """Custom type ieee8021AsPortDSInitialLogSyncInterval based on Integer32"""
    defaultValue = -3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsPortDSInitialLogSyncInterval_Type.__name__ = "Integer32"
_Ieee8021AsPortDSInitialLogSyncInterval_Object = MibTableColumn
ieee8021AsPortDSInitialLogSyncInterval = _Ieee8021AsPortDSInitialLogSyncInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 22),
    _Ieee8021AsPortDSInitialLogSyncInterval_Type()
)
ieee8021AsPortDSInitialLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSInitialLogSyncInterval.setStatus("current")


class _Ieee8021AsPortDSCurrentLogSyncInterval_Type(Integer32):
    """Custom type ieee8021AsPortDSCurrentLogSyncInterval based on Integer32"""
    defaultValue = -3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsPortDSCurrentLogSyncInterval_Type.__name__ = "Integer32"
_Ieee8021AsPortDSCurrentLogSyncInterval_Object = MibTableColumn
ieee8021AsPortDSCurrentLogSyncInterval = _Ieee8021AsPortDSCurrentLogSyncInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 23),
    _Ieee8021AsPortDSCurrentLogSyncInterval_Type()
)
ieee8021AsPortDSCurrentLogSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSCurrentLogSyncInterval.setStatus("current")


class _Ieee8021AsPortDSSyncReceiptTimeout_Type(Unsigned32):
    """Custom type ieee8021AsPortDSSyncReceiptTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsPortDSSyncReceiptTimeout_Type.__name__ = "Unsigned32"
_Ieee8021AsPortDSSyncReceiptTimeout_Object = MibTableColumn
ieee8021AsPortDSSyncReceiptTimeout = _Ieee8021AsPortDSSyncReceiptTimeout_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 24),
    _Ieee8021AsPortDSSyncReceiptTimeout_Type()
)
ieee8021AsPortDSSyncReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSSyncReceiptTimeout.setStatus("current")


class _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs_Type(Unsigned32):
    """Custom type ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs based on Unsigned32"""
    defaultHexValue = 0


_Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs_Object = MibTableColumn
ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs = _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 25),
    _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs_Type()
)
ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs.setUnits("2**-16 ns")


class _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs_Type(Unsigned32):
    """Custom type ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs based on Unsigned32"""
    defaultHexValue = 5722


_Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs_Object = MibTableColumn
ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs = _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 26),
    _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs_Type()
)
ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs.setUnits("2**-16 ns * 2**32")


class _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs_Type(Unsigned32):
    """Custom type ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs based on Unsigned32"""
    defaultHexValue = 197132288


_Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs_Object = MibTableColumn
ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs = _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 27),
    _Ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs_Type()
)
ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs.setUnits("2**-16 ns")


class _Ieee8021AsPortDSInitialLogPdelayReqInterval_Type(Integer32):
    """Custom type ieee8021AsPortDSInitialLogPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsPortDSInitialLogPdelayReqInterval_Type.__name__ = "Integer32"
_Ieee8021AsPortDSInitialLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsPortDSInitialLogPdelayReqInterval = _Ieee8021AsPortDSInitialLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 28),
    _Ieee8021AsPortDSInitialLogPdelayReqInterval_Type()
)
ieee8021AsPortDSInitialLogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSInitialLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsPortDSCurrentLogPdelayReqInterval_Type(Integer32):
    """Custom type ieee8021AsPortDSCurrentLogPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsPortDSCurrentLogPdelayReqInterval_Type.__name__ = "Integer32"
_Ieee8021AsPortDSCurrentLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsPortDSCurrentLogPdelayReqInterval = _Ieee8021AsPortDSCurrentLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 29),
    _Ieee8021AsPortDSCurrentLogPdelayReqInterval_Type()
)
ieee8021AsPortDSCurrentLogPdelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSCurrentLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsPortDSAllowedLostResponses_Type(Unsigned32):
    """Custom type ieee8021AsPortDSAllowedLostResponses based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsPortDSAllowedLostResponses_Type.__name__ = "Unsigned32"
_Ieee8021AsPortDSAllowedLostResponses_Object = MibTableColumn
ieee8021AsPortDSAllowedLostResponses = _Ieee8021AsPortDSAllowedLostResponses_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 30),
    _Ieee8021AsPortDSAllowedLostResponses_Type()
)
ieee8021AsPortDSAllowedLostResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSAllowedLostResponses.setStatus("current")


class _Ieee8021AsPortDSVersionNumber_Type(Unsigned32):
    """Custom type ieee8021AsPortDSVersionNumber based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Ieee8021AsPortDSVersionNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsPortDSVersionNumber_Object = MibTableColumn
ieee8021AsPortDSVersionNumber = _Ieee8021AsPortDSVersionNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 31),
    _Ieee8021AsPortDSVersionNumber_Type()
)
ieee8021AsPortDSVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortDSVersionNumber.setStatus("current")
_Ieee8021AsPortDSNupMs_Type = Unsigned32
_Ieee8021AsPortDSNupMs_Object = MibTableColumn
ieee8021AsPortDSNupMs = _Ieee8021AsPortDSNupMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 32),
    _Ieee8021AsPortDSNupMs_Type()
)
ieee8021AsPortDSNupMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNupMs.setStatus("current")
_Ieee8021AsPortDSNupLs_Type = Unsigned32
_Ieee8021AsPortDSNupLs_Object = MibTableColumn
ieee8021AsPortDSNupLs = _Ieee8021AsPortDSNupLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 33),
    _Ieee8021AsPortDSNupLs_Type()
)
ieee8021AsPortDSNupLs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNupLs.setStatus("current")
_Ieee8021AsPortDSNdownMs_Type = Unsigned32
_Ieee8021AsPortDSNdownMs_Object = MibTableColumn
ieee8021AsPortDSNdownMs = _Ieee8021AsPortDSNdownMs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 34),
    _Ieee8021AsPortDSNdownMs_Type()
)
ieee8021AsPortDSNdownMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNdownMs.setStatus("current")
_Ieee8021AsPortDSNdownLs_Type = Unsigned32
_Ieee8021AsPortDSNdownLs_Object = MibTableColumn
ieee8021AsPortDSNdownLs = _Ieee8021AsPortDSNdownLs_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 35),
    _Ieee8021AsPortDSNdownLs_Type()
)
ieee8021AsPortDSNdownLs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSNdownLs.setStatus("current")


class _Ieee8021AsPortDSAcceptableMasterTableEnabled_Type(TruthValue):
    """Custom type ieee8021AsPortDSAcceptableMasterTableEnabled based on TruthValue"""


_Ieee8021AsPortDSAcceptableMasterTableEnabled_Object = MibTableColumn
ieee8021AsPortDSAcceptableMasterTableEnabled = _Ieee8021AsPortDSAcceptableMasterTableEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 5, 1, 36),
    _Ieee8021AsPortDSAcceptableMasterTableEnabled_Type()
)
ieee8021AsPortDSAcceptableMasterTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsPortDSAcceptableMasterTableEnabled.setStatus("current")
_Ieee8021AsPortStatIfTable_Object = MibTable
ieee8021AsPortStatIfTable = _Ieee8021AsPortStatIfTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021AsPortStatIfTable.setStatus("current")
_Ieee8021AsPortStatIfEntry_Object = MibTableRow
ieee8021AsPortStatIfEntry = _Ieee8021AsPortStatIfEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1)
)
ieee8021AsPortStatIfEntry.setIndexNames(
    (0, "IEEE8021-AS-MIB", "ieee8021AsBridgeBasePort"),
    (0, "IEEE8021-AS-MIB", "ieee8021AsPortDSAsIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsPortStatIfEntry.setStatus("current")
_Ieee8021AsPortStatRxSyncCount_Type = Counter32
_Ieee8021AsPortStatRxSyncCount_Object = MibTableColumn
ieee8021AsPortStatRxSyncCount = _Ieee8021AsPortStatRxSyncCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 1),
    _Ieee8021AsPortStatRxSyncCount_Type()
)
ieee8021AsPortStatRxSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatRxSyncCount.setStatus("current")
_Ieee8021AsPortStatRxFollowUpCount_Type = Counter32
_Ieee8021AsPortStatRxFollowUpCount_Object = MibTableColumn
ieee8021AsPortStatRxFollowUpCount = _Ieee8021AsPortStatRxFollowUpCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 2),
    _Ieee8021AsPortStatRxFollowUpCount_Type()
)
ieee8021AsPortStatRxFollowUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatRxFollowUpCount.setStatus("current")
_Ieee8021AsPortStatRxPdelayRequest_Type = Counter32
_Ieee8021AsPortStatRxPdelayRequest_Object = MibTableColumn
ieee8021AsPortStatRxPdelayRequest = _Ieee8021AsPortStatRxPdelayRequest_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 3),
    _Ieee8021AsPortStatRxPdelayRequest_Type()
)
ieee8021AsPortStatRxPdelayRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatRxPdelayRequest.setStatus("current")
_Ieee8021AsPortStatRxPdelayResponse_Type = Counter32
_Ieee8021AsPortStatRxPdelayResponse_Object = MibTableColumn
ieee8021AsPortStatRxPdelayResponse = _Ieee8021AsPortStatRxPdelayResponse_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 4),
    _Ieee8021AsPortStatRxPdelayResponse_Type()
)
ieee8021AsPortStatRxPdelayResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatRxPdelayResponse.setStatus("current")
_Ieee8021AsPortStatRxPdelayResponseFollowUp_Type = Counter32
_Ieee8021AsPortStatRxPdelayResponseFollowUp_Object = MibTableColumn
ieee8021AsPortStatRxPdelayResponseFollowUp = _Ieee8021AsPortStatRxPdelayResponseFollowUp_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 5),
    _Ieee8021AsPortStatRxPdelayResponseFollowUp_Type()
)
ieee8021AsPortStatRxPdelayResponseFollowUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatRxPdelayResponseFollowUp.setStatus("current")
_Ieee8021AsPortStatRxAnnounce_Type = Counter32
_Ieee8021AsPortStatRxAnnounce_Object = MibTableColumn
ieee8021AsPortStatRxAnnounce = _Ieee8021AsPortStatRxAnnounce_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 6),
    _Ieee8021AsPortStatRxAnnounce_Type()
)
ieee8021AsPortStatRxAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatRxAnnounce.setStatus("current")
_Ieee8021AsPortStatRxPTPPacketDiscard_Type = Counter32
_Ieee8021AsPortStatRxPTPPacketDiscard_Object = MibTableColumn
ieee8021AsPortStatRxPTPPacketDiscard = _Ieee8021AsPortStatRxPTPPacketDiscard_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 7),
    _Ieee8021AsPortStatRxPTPPacketDiscard_Type()
)
ieee8021AsPortStatRxPTPPacketDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatRxPTPPacketDiscard.setStatus("current")
_Ieee8021AsPortStatRxSyncReceiptTimeouts_Type = Counter32
_Ieee8021AsPortStatRxSyncReceiptTimeouts_Object = MibTableColumn
ieee8021AsPortStatRxSyncReceiptTimeouts = _Ieee8021AsPortStatRxSyncReceiptTimeouts_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 8),
    _Ieee8021AsPortStatRxSyncReceiptTimeouts_Type()
)
ieee8021AsPortStatRxSyncReceiptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatRxSyncReceiptTimeouts.setStatus("current")
_Ieee8021AsPortStatAnnounceReceiptTimeouts_Type = Counter32
_Ieee8021AsPortStatAnnounceReceiptTimeouts_Object = MibTableColumn
ieee8021AsPortStatAnnounceReceiptTimeouts = _Ieee8021AsPortStatAnnounceReceiptTimeouts_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 9),
    _Ieee8021AsPortStatAnnounceReceiptTimeouts_Type()
)
ieee8021AsPortStatAnnounceReceiptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatAnnounceReceiptTimeouts.setStatus("current")
_Ieee8021AsPortStatPdelayAllowedLostResponsesExceeded_Type = Counter32
_Ieee8021AsPortStatPdelayAllowedLostResponsesExceeded_Object = MibTableColumn
ieee8021AsPortStatPdelayAllowedLostResponsesExceeded = _Ieee8021AsPortStatPdelayAllowedLostResponsesExceeded_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 10),
    _Ieee8021AsPortStatPdelayAllowedLostResponsesExceeded_Type()
)
ieee8021AsPortStatPdelayAllowedLostResponsesExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatPdelayAllowedLostResponsesExceeded.setStatus("current")
_Ieee8021AsPortStatTxSyncCount_Type = Counter32
_Ieee8021AsPortStatTxSyncCount_Object = MibTableColumn
ieee8021AsPortStatTxSyncCount = _Ieee8021AsPortStatTxSyncCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 11),
    _Ieee8021AsPortStatTxSyncCount_Type()
)
ieee8021AsPortStatTxSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatTxSyncCount.setStatus("current")
_Ieee8021AsPortStatTxFollowUpCount_Type = Counter32
_Ieee8021AsPortStatTxFollowUpCount_Object = MibTableColumn
ieee8021AsPortStatTxFollowUpCount = _Ieee8021AsPortStatTxFollowUpCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 12),
    _Ieee8021AsPortStatTxFollowUpCount_Type()
)
ieee8021AsPortStatTxFollowUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatTxFollowUpCount.setStatus("current")
_Ieee8021AsPortStatTxPdelayRequest_Type = Counter32
_Ieee8021AsPortStatTxPdelayRequest_Object = MibTableColumn
ieee8021AsPortStatTxPdelayRequest = _Ieee8021AsPortStatTxPdelayRequest_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 13),
    _Ieee8021AsPortStatTxPdelayRequest_Type()
)
ieee8021AsPortStatTxPdelayRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatTxPdelayRequest.setStatus("current")
_Ieee8021AsPortStatTxPdelayResponse_Type = Counter32
_Ieee8021AsPortStatTxPdelayResponse_Object = MibTableColumn
ieee8021AsPortStatTxPdelayResponse = _Ieee8021AsPortStatTxPdelayResponse_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 14),
    _Ieee8021AsPortStatTxPdelayResponse_Type()
)
ieee8021AsPortStatTxPdelayResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatTxPdelayResponse.setStatus("current")
_Ieee8021AsPortStatTxPdelayResponseFollowUp_Type = Counter32
_Ieee8021AsPortStatTxPdelayResponseFollowUp_Object = MibTableColumn
ieee8021AsPortStatTxPdelayResponseFollowUp = _Ieee8021AsPortStatTxPdelayResponseFollowUp_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 15),
    _Ieee8021AsPortStatTxPdelayResponseFollowUp_Type()
)
ieee8021AsPortStatTxPdelayResponseFollowUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatTxPdelayResponseFollowUp.setStatus("current")
_Ieee8021AsPortStatTxAnnounce_Type = Counter32
_Ieee8021AsPortStatTxAnnounce_Object = MibTableColumn
ieee8021AsPortStatTxAnnounce = _Ieee8021AsPortStatTxAnnounce_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 6, 1, 16),
    _Ieee8021AsPortStatTxAnnounce_Type()
)
ieee8021AsPortStatTxAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsPortStatTxAnnounce.setStatus("current")
_Ieee8021AsAcceptableMasterTableDS_ObjectIdentity = ObjectIdentity
ieee8021AsAcceptableMasterTableDS = _Ieee8021AsAcceptableMasterTableDS_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7)
)
_Ieee8021AsAcceptableMasterTableDSBase_ObjectIdentity = ObjectIdentity
ieee8021AsAcceptableMasterTableDSBase = _Ieee8021AsAcceptableMasterTableDSBase_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 1)
)


class _Ieee8021AsAcceptableMasterTableDSMaxTableSize_Type(Unsigned32):
    """Custom type ieee8021AsAcceptableMasterTableDSMaxTableSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsAcceptableMasterTableDSMaxTableSize_Type.__name__ = "Unsigned32"
_Ieee8021AsAcceptableMasterTableDSMaxTableSize_Object = MibScalar
ieee8021AsAcceptableMasterTableDSMaxTableSize = _Ieee8021AsAcceptableMasterTableDSMaxTableSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 1, 1),
    _Ieee8021AsAcceptableMasterTableDSMaxTableSize_Type()
)
ieee8021AsAcceptableMasterTableDSMaxTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterTableDSMaxTableSize.setStatus("current")


class _Ieee8021AsAcceptableMasterTableDSActualTableSize_Type(Unsigned32):
    """Custom type ieee8021AsAcceptableMasterTableDSActualTableSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsAcceptableMasterTableDSActualTableSize_Type.__name__ = "Unsigned32"
_Ieee8021AsAcceptableMasterTableDSActualTableSize_Object = MibScalar
ieee8021AsAcceptableMasterTableDSActualTableSize = _Ieee8021AsAcceptableMasterTableDSActualTableSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 1, 2),
    _Ieee8021AsAcceptableMasterTableDSActualTableSize_Type()
)
ieee8021AsAcceptableMasterTableDSActualTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterTableDSActualTableSize.setStatus("current")
_Ieee8021AsAcceptableMasterTableDSMaster_ObjectIdentity = ObjectIdentity
ieee8021AsAcceptableMasterTableDSMaster = _Ieee8021AsAcceptableMasterTableDSMaster_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 2)
)
_Ieee8021AsAcceptableMasterTableDSMasterTable_Object = MibTable
ieee8021AsAcceptableMasterTableDSMasterTable = _Ieee8021AsAcceptableMasterTableDSMasterTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterTableDSMasterTable.setStatus("current")
_Ieee8021AsAcceptableMasterTableDSMasterEntry_Object = MibTableRow
ieee8021AsAcceptableMasterTableDSMasterEntry = _Ieee8021AsAcceptableMasterTableDSMasterEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 2, 1, 1)
)
ieee8021AsAcceptableMasterTableDSMasterEntry.setIndexNames(
    (0, "IEEE8021-AS-MIB", "ieee8021AsAcceptableMasterTableDSMasterId"),
)
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterTableDSMasterEntry.setStatus("current")
_Ieee8021AsAcceptableMasterTableDSMasterId_Type = Unsigned32
_Ieee8021AsAcceptableMasterTableDSMasterId_Object = MibTableColumn
ieee8021AsAcceptableMasterTableDSMasterId = _Ieee8021AsAcceptableMasterTableDSMasterId_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 2, 1, 1, 1),
    _Ieee8021AsAcceptableMasterTableDSMasterId_Type()
)
ieee8021AsAcceptableMasterTableDSMasterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterTableDSMasterId.setStatus("current")
_Ieee8021AsAcceptableMasterClockIdentity_Type = ClockIdentity
_Ieee8021AsAcceptableMasterClockIdentity_Object = MibTableColumn
ieee8021AsAcceptableMasterClockIdentity = _Ieee8021AsAcceptableMasterClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 2, 1, 1, 2),
    _Ieee8021AsAcceptableMasterClockIdentity_Type()
)
ieee8021AsAcceptableMasterClockIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterClockIdentity.setStatus("current")


class _Ieee8021AsAcceptableMasterPortNumber_Type(Unsigned32):
    """Custom type ieee8021AsAcceptableMasterPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsAcceptableMasterPortNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsAcceptableMasterPortNumber_Object = MibTableColumn
ieee8021AsAcceptableMasterPortNumber = _Ieee8021AsAcceptableMasterPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 2, 1, 1, 3),
    _Ieee8021AsAcceptableMasterPortNumber_Type()
)
ieee8021AsAcceptableMasterPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterPortNumber.setStatus("current")


class _Ieee8021AsAcceptableMasterAlternatePriority1_Type(Unsigned32):
    """Custom type ieee8021AsAcceptableMasterAlternatePriority1 based on Unsigned32"""
    defaultValue = 244

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsAcceptableMasterAlternatePriority1_Type.__name__ = "Unsigned32"
_Ieee8021AsAcceptableMasterAlternatePriority1_Object = MibTableColumn
ieee8021AsAcceptableMasterAlternatePriority1 = _Ieee8021AsAcceptableMasterAlternatePriority1_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 2, 1, 1, 4),
    _Ieee8021AsAcceptableMasterAlternatePriority1_Type()
)
ieee8021AsAcceptableMasterAlternatePriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterAlternatePriority1.setStatus("current")
_Ieee8021AsAcceptableMasterRowStatus_Type = RowStatus
_Ieee8021AsAcceptableMasterRowStatus_Object = MibTableColumn
ieee8021AsAcceptableMasterRowStatus = _Ieee8021AsAcceptableMasterRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 20, 1, 7, 2, 1, 1, 5),
    _Ieee8021AsAcceptableMasterRowStatus_Type()
)
ieee8021AsAcceptableMasterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterRowStatus.setStatus("current")
_Ieee8021AsConformance_ObjectIdentity = ObjectIdentity
ieee8021AsConformance = _Ieee8021AsConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 2)
)
_Ieee8021AsCompliances_ObjectIdentity = ObjectIdentity
ieee8021AsCompliances = _Ieee8021AsCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 1)
)
_Ieee8021AsGroups_ObjectIdentity = ObjectIdentity
ieee8021AsGroups = _Ieee8021AsGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2)
)
_Ieee8021AsCompliancesCor1_ObjectIdentity = ObjectIdentity
ieee8021AsCompliancesCor1 = _Ieee8021AsCompliancesCor1_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 3)
)

# Managed Objects groups

ieee8021ASSystemDefaultReqdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2, 1)
)
ieee8021ASSystemDefaultReqdGroup.setObjects(
      *(("IEEE8021-AS-MIB", "ieee8021AsDefaultDSClockIdentity"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSNumberPorts"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSClockClass"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSClockAccuracy"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSOffsetScaledLogVariance"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSPriority1"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSPriority2"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSGmCapable"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSCurrentUTCOffset"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSCurrentUTCOffsetValid"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSLeap59"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSLeap61"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSTimeTraceable"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSFrequencyTraceable"),
        ("IEEE8021-AS-MIB", "ieee8021AsDefaultDSTimeSource"))
)
if mibBuilder.loadTexts:
    ieee8021ASSystemDefaultReqdGroup.setStatus("current")

ieee8021ASSystemCurrentGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2, 2)
)
ieee8021ASSystemCurrentGroup.setObjects(
      *(("IEEE8021-AS-MIB", "ieee8021AsCurrentDSStepsRemoved"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSOffsetFromMasterHs"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSOffsetFromMasterMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSOffsetFromMasterLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSLastGmPhaseChangeHs"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSLastGmPhaseChangeMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSLastGmPhaseChangeLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSLastGmFreqChangeMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSLastGmFreqChangeLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSGmTimebaseIndicator"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSGmChangeCount"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSTimeOfLastGmChangeEvent"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent"),
        ("IEEE8021-AS-MIB", "ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent"))
)
if mibBuilder.loadTexts:
    ieee8021ASSystemCurrentGroup.setStatus("current")

ieee8021AsSystemClockParentGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2, 3)
)
ieee8021AsSystemClockParentGroup.setObjects(
      *(("IEEE8021-AS-MIB", "ieee8021AsParentDSParentClockIdentity"),
        ("IEEE8021-AS-MIB", "ieee8021AsParentDSParentPortNumber"),
        ("IEEE8021-AS-MIB", "ieee8021AsParentDSCumlativeRateRatio"),
        ("IEEE8021-AS-MIB", "ieee8021AsParentDSGrandmasterIdentity"),
        ("IEEE8021-AS-MIB", "ieee8021AsParentDSGrandmasterClockClass"),
        ("IEEE8021-AS-MIB", "ieee8021AsParentDSGrandmasterClockAccuracy"),
        ("IEEE8021-AS-MIB", "ieee8021AsParentDSGrandmasterOffsetScaledLogVariance"),
        ("IEEE8021-AS-MIB", "ieee8021AsParentDSGrandmasterPriority1"),
        ("IEEE8021-AS-MIB", "ieee8021AsParentDSGrandmasterPriority2"))
)
if mibBuilder.loadTexts:
    ieee8021AsSystemClockParentGroup.setStatus("current")

ieee8021AsSystemTimePropertiesGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2, 4)
)
ieee8021AsSystemTimePropertiesGroup.setObjects(
      *(("IEEE8021-AS-MIB", "ieee8021AsTimePropertiesDSCurrentUtcOffset"),
        ("IEEE8021-AS-MIB", "ieee8021AsTimePropertiesDSCurrentUtcOffsetValid"),
        ("IEEE8021-AS-MIB", "ieee8021AsTimePropertiesDSLeap59"),
        ("IEEE8021-AS-MIB", "ieee8021AsTimePropertiesDSLeap61"),
        ("IEEE8021-AS-MIB", "ieee8021AsTimePropertiesDSTimeTraceable"),
        ("IEEE8021-AS-MIB", "ieee8021AsTimePropertiesDSFrequencyTraceable"),
        ("IEEE8021-AS-MIB", "ieee8021AsTimePropertiesDSTimeSource"))
)
if mibBuilder.loadTexts:
    ieee8021AsSystemTimePropertiesGroup.setStatus("current")

ieee8021AsPortDataSetGlobalGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2, 5)
)
ieee8021AsPortDataSetGlobalGroup.setObjects(
      *(("IEEE8021-AS-MIB", "ieee8021AsPortDSClockIdentity"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSPortNumber"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSPortRole"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSPttPortEnabled"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSIsMeasuringDelay"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSAsCapable"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNeighborPropDelayHs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNeighborPropDelayMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNeighborPropDelayLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNeighborPropDelayThreshHs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNeighborPropDelayThreshMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNeighborPropDelayThreshLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSDelayAsymmetryHs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSDelayAsymmetryMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSDelayAsymmetryLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNeighborRateRatio"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSInitialLogAnnounceInterval"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSCurrentLogAnnounceInterval"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSAnnounceReceiptTimeout"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSInitialLogSyncInterval"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSCurrentLogSyncInterval"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSSyncReceiptTimeout"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSInitialLogPdelayReqInterval"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSCurrentLogPdelayReqInterval"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSAllowedLostResponses"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSVersionNumber"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNupMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNupLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNdownMs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSNdownLs"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortDSAcceptableMasterTableEnabled"))
)
if mibBuilder.loadTexts:
    ieee8021AsPortDataSetGlobalGroup.setStatus("current")

ieee8021ASPortStatisticsGlobalGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2, 6)
)
ieee8021ASPortStatisticsGlobalGroup.setObjects(
      *(("IEEE8021-AS-MIB", "ieee8021AsPortStatRxSyncCount"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatRxFollowUpCount"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatRxPdelayRequest"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatRxPdelayResponse"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatRxPdelayResponseFollowUp"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatRxAnnounce"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatRxPTPPacketDiscard"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatRxSyncReceiptTimeouts"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatAnnounceReceiptTimeouts"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatPdelayAllowedLostResponsesExceeded"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatTxSyncCount"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatTxFollowUpCount"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatTxPdelayRequest"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatTxPdelayResponse"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatTxPdelayResponseFollowUp"),
        ("IEEE8021-AS-MIB", "ieee8021AsPortStatTxAnnounce"))
)
if mibBuilder.loadTexts:
    ieee8021ASPortStatisticsGlobalGroup.setStatus("current")

ieee8021AsAcceptableMasterBaseGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2, 7)
)
ieee8021AsAcceptableMasterBaseGroup.setObjects(
      *(("IEEE8021-AS-MIB", "ieee8021AsAcceptableMasterTableDSMaxTableSize"),
        ("IEEE8021-AS-MIB", "ieee8021AsAcceptableMasterTableDSActualTableSize"))
)
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterBaseGroup.setStatus("current")

ieee8021AsAcceptableMasterTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 2, 8)
)
ieee8021AsAcceptableMasterTableGroup.setObjects(
      *(("IEEE8021-AS-MIB", "ieee8021AsAcceptableMasterClockIdentity"),
        ("IEEE8021-AS-MIB", "ieee8021AsAcceptableMasterPortNumber"),
        ("IEEE8021-AS-MIB", "ieee8021AsAcceptableMasterAlternatePriority1"),
        ("IEEE8021-AS-MIB", "ieee8021AsAcceptableMasterRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021AsAcceptableMasterTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021AsCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021AsCompliance.setStatus(
        "deprecated"
    )

ieee8021AsComplianceCor1 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 20, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021AsComplianceCor1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-AS-MIB",
    **{"ClockIdentity": ClockIdentity,
       "IEEE8021ASClockClassValue": IEEE8021ASClockClassValue,
       "IEEE8021ASClockAccuracyValue": IEEE8021ASClockAccuracyValue,
       "IEEE8021ASTimeSourceValue": IEEE8021ASTimeSourceValue,
       "ieee8021AsTimeSyncMib": ieee8021AsTimeSyncMib,
       "ieee8021AsMIBObjects": ieee8021AsMIBObjects,
       "ieee8021AsDefaultDS": ieee8021AsDefaultDS,
       "ieee8021AsDefaultDSClockIdentity": ieee8021AsDefaultDSClockIdentity,
       "ieee8021AsDefaultDSNumberPorts": ieee8021AsDefaultDSNumberPorts,
       "ieee8021AsDefaultDSClockClass": ieee8021AsDefaultDSClockClass,
       "ieee8021AsDefaultDSClockAccuracy": ieee8021AsDefaultDSClockAccuracy,
       "ieee8021AsDefaultDSOffsetScaledLogVariance": ieee8021AsDefaultDSOffsetScaledLogVariance,
       "ieee8021AsDefaultDSPriority1": ieee8021AsDefaultDSPriority1,
       "ieee8021AsDefaultDSPriority2": ieee8021AsDefaultDSPriority2,
       "ieee8021AsDefaultDSGmCapable": ieee8021AsDefaultDSGmCapable,
       "ieee8021AsDefaultDSCurrentUTCOffset": ieee8021AsDefaultDSCurrentUTCOffset,
       "ieee8021AsDefaultDSCurrentUTCOffsetValid": ieee8021AsDefaultDSCurrentUTCOffsetValid,
       "ieee8021AsDefaultDSLeap59": ieee8021AsDefaultDSLeap59,
       "ieee8021AsDefaultDSLeap61": ieee8021AsDefaultDSLeap61,
       "ieee8021AsDefaultDSTimeTraceable": ieee8021AsDefaultDSTimeTraceable,
       "ieee8021AsDefaultDSFrequencyTraceable": ieee8021AsDefaultDSFrequencyTraceable,
       "ieee8021AsDefaultDSTimeSource": ieee8021AsDefaultDSTimeSource,
       "ieee8021AsCurrentDS": ieee8021AsCurrentDS,
       "ieee8021AsCurrentDSStepsRemoved": ieee8021AsCurrentDSStepsRemoved,
       "ieee8021AsCurrentDSOffsetFromMasterHs": ieee8021AsCurrentDSOffsetFromMasterHs,
       "ieee8021AsCurrentDSOffsetFromMasterMs": ieee8021AsCurrentDSOffsetFromMasterMs,
       "ieee8021AsCurrentDSOffsetFromMasterLs": ieee8021AsCurrentDSOffsetFromMasterLs,
       "ieee8021AsCurrentDSLastGmPhaseChangeHs": ieee8021AsCurrentDSLastGmPhaseChangeHs,
       "ieee8021AsCurrentDSLastGmPhaseChangeMs": ieee8021AsCurrentDSLastGmPhaseChangeMs,
       "ieee8021AsCurrentDSLastGmPhaseChangeLs": ieee8021AsCurrentDSLastGmPhaseChangeLs,
       "ieee8021AsCurrentDSLastGmFreqChangeMs": ieee8021AsCurrentDSLastGmFreqChangeMs,
       "ieee8021AsCurrentDSLastGmFreqChangeLs": ieee8021AsCurrentDSLastGmFreqChangeLs,
       "ieee8021AsCurrentDSGmTimebaseIndicator": ieee8021AsCurrentDSGmTimebaseIndicator,
       "ieee8021AsCurrentDSGmChangeCount": ieee8021AsCurrentDSGmChangeCount,
       "ieee8021AsCurrentDSTimeOfLastGmChangeEvent": ieee8021AsCurrentDSTimeOfLastGmChangeEvent,
       "ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent": ieee8021AsCurrentDSTimeOfLastGmFreqChangeEvent,
       "ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent": ieee8021AsCurrentDSTimeOfLastGmPhaseChangeEvent,
       "ieee8021AsParentDS": ieee8021AsParentDS,
       "ieee8021AsParentDSParentClockIdentity": ieee8021AsParentDSParentClockIdentity,
       "ieee8021AsParentDSParentPortNumber": ieee8021AsParentDSParentPortNumber,
       "ieee8021AsParentDSCumlativeRateRatio": ieee8021AsParentDSCumlativeRateRatio,
       "ieee8021AsParentDSGrandmasterIdentity": ieee8021AsParentDSGrandmasterIdentity,
       "ieee8021AsParentDSGrandmasterClockClass": ieee8021AsParentDSGrandmasterClockClass,
       "ieee8021AsParentDSGrandmasterClockAccuracy": ieee8021AsParentDSGrandmasterClockAccuracy,
       "ieee8021AsParentDSGrandmasterOffsetScaledLogVariance": ieee8021AsParentDSGrandmasterOffsetScaledLogVariance,
       "ieee8021AsParentDSGrandmasterPriority1": ieee8021AsParentDSGrandmasterPriority1,
       "ieee8021AsParentDSGrandmasterPriority2": ieee8021AsParentDSGrandmasterPriority2,
       "ieee8021AsTimePropertiesDS": ieee8021AsTimePropertiesDS,
       "ieee8021AsTimePropertiesDSCurrentUtcOffset": ieee8021AsTimePropertiesDSCurrentUtcOffset,
       "ieee8021AsTimePropertiesDSCurrentUtcOffsetValid": ieee8021AsTimePropertiesDSCurrentUtcOffsetValid,
       "ieee8021AsTimePropertiesDSLeap59": ieee8021AsTimePropertiesDSLeap59,
       "ieee8021AsTimePropertiesDSLeap61": ieee8021AsTimePropertiesDSLeap61,
       "ieee8021AsTimePropertiesDSTimeTraceable": ieee8021AsTimePropertiesDSTimeTraceable,
       "ieee8021AsTimePropertiesDSFrequencyTraceable": ieee8021AsTimePropertiesDSFrequencyTraceable,
       "ieee8021AsTimePropertiesDSTimeSource": ieee8021AsTimePropertiesDSTimeSource,
       "ieee8021AsPortDSIfTable": ieee8021AsPortDSIfTable,
       "ieee8021AsPortDSIfEntry": ieee8021AsPortDSIfEntry,
       "ieee8021AsBridgeBasePort": ieee8021AsBridgeBasePort,
       "ieee8021AsPortDSAsIfIndex": ieee8021AsPortDSAsIfIndex,
       "ieee8021AsPortDSClockIdentity": ieee8021AsPortDSClockIdentity,
       "ieee8021AsPortDSPortNumber": ieee8021AsPortDSPortNumber,
       "ieee8021AsPortDSPortRole": ieee8021AsPortDSPortRole,
       "ieee8021AsPortDSPttPortEnabled": ieee8021AsPortDSPttPortEnabled,
       "ieee8021AsPortDSIsMeasuringDelay": ieee8021AsPortDSIsMeasuringDelay,
       "ieee8021AsPortDSAsCapable": ieee8021AsPortDSAsCapable,
       "ieee8021AsPortDSNeighborPropDelayHs": ieee8021AsPortDSNeighborPropDelayHs,
       "ieee8021AsPortDSNeighborPropDelayMs": ieee8021AsPortDSNeighborPropDelayMs,
       "ieee8021AsPortDSNeighborPropDelayLs": ieee8021AsPortDSNeighborPropDelayLs,
       "ieee8021AsPortDSNeighborPropDelayThreshHs": ieee8021AsPortDSNeighborPropDelayThreshHs,
       "ieee8021AsPortDSNeighborPropDelayThreshMs": ieee8021AsPortDSNeighborPropDelayThreshMs,
       "ieee8021AsPortDSNeighborPropDelayThreshLs": ieee8021AsPortDSNeighborPropDelayThreshLs,
       "ieee8021AsPortDSDelayAsymmetryHs": ieee8021AsPortDSDelayAsymmetryHs,
       "ieee8021AsPortDSDelayAsymmetryMs": ieee8021AsPortDSDelayAsymmetryMs,
       "ieee8021AsPortDSDelayAsymmetryLs": ieee8021AsPortDSDelayAsymmetryLs,
       "ieee8021AsPortDSNeighborRateRatio": ieee8021AsPortDSNeighborRateRatio,
       "ieee8021AsPortDSInitialLogAnnounceInterval": ieee8021AsPortDSInitialLogAnnounceInterval,
       "ieee8021AsPortDSCurrentLogAnnounceInterval": ieee8021AsPortDSCurrentLogAnnounceInterval,
       "ieee8021AsPortDSAnnounceReceiptTimeout": ieee8021AsPortDSAnnounceReceiptTimeout,
       "ieee8021AsPortDSInitialLogSyncInterval": ieee8021AsPortDSInitialLogSyncInterval,
       "ieee8021AsPortDSCurrentLogSyncInterval": ieee8021AsPortDSCurrentLogSyncInterval,
       "ieee8021AsPortDSSyncReceiptTimeout": ieee8021AsPortDSSyncReceiptTimeout,
       "ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs": ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalHs,
       "ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs": ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalMs,
       "ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs": ieee8021AsPortDSSyncReceiptTimeoutTimeIntervalLs,
       "ieee8021AsPortDSInitialLogPdelayReqInterval": ieee8021AsPortDSInitialLogPdelayReqInterval,
       "ieee8021AsPortDSCurrentLogPdelayReqInterval": ieee8021AsPortDSCurrentLogPdelayReqInterval,
       "ieee8021AsPortDSAllowedLostResponses": ieee8021AsPortDSAllowedLostResponses,
       "ieee8021AsPortDSVersionNumber": ieee8021AsPortDSVersionNumber,
       "ieee8021AsPortDSNupMs": ieee8021AsPortDSNupMs,
       "ieee8021AsPortDSNupLs": ieee8021AsPortDSNupLs,
       "ieee8021AsPortDSNdownMs": ieee8021AsPortDSNdownMs,
       "ieee8021AsPortDSNdownLs": ieee8021AsPortDSNdownLs,
       "ieee8021AsPortDSAcceptableMasterTableEnabled": ieee8021AsPortDSAcceptableMasterTableEnabled,
       "ieee8021AsPortStatIfTable": ieee8021AsPortStatIfTable,
       "ieee8021AsPortStatIfEntry": ieee8021AsPortStatIfEntry,
       "ieee8021AsPortStatRxSyncCount": ieee8021AsPortStatRxSyncCount,
       "ieee8021AsPortStatRxFollowUpCount": ieee8021AsPortStatRxFollowUpCount,
       "ieee8021AsPortStatRxPdelayRequest": ieee8021AsPortStatRxPdelayRequest,
       "ieee8021AsPortStatRxPdelayResponse": ieee8021AsPortStatRxPdelayResponse,
       "ieee8021AsPortStatRxPdelayResponseFollowUp": ieee8021AsPortStatRxPdelayResponseFollowUp,
       "ieee8021AsPortStatRxAnnounce": ieee8021AsPortStatRxAnnounce,
       "ieee8021AsPortStatRxPTPPacketDiscard": ieee8021AsPortStatRxPTPPacketDiscard,
       "ieee8021AsPortStatRxSyncReceiptTimeouts": ieee8021AsPortStatRxSyncReceiptTimeouts,
       "ieee8021AsPortStatAnnounceReceiptTimeouts": ieee8021AsPortStatAnnounceReceiptTimeouts,
       "ieee8021AsPortStatPdelayAllowedLostResponsesExceeded": ieee8021AsPortStatPdelayAllowedLostResponsesExceeded,
       "ieee8021AsPortStatTxSyncCount": ieee8021AsPortStatTxSyncCount,
       "ieee8021AsPortStatTxFollowUpCount": ieee8021AsPortStatTxFollowUpCount,
       "ieee8021AsPortStatTxPdelayRequest": ieee8021AsPortStatTxPdelayRequest,
       "ieee8021AsPortStatTxPdelayResponse": ieee8021AsPortStatTxPdelayResponse,
       "ieee8021AsPortStatTxPdelayResponseFollowUp": ieee8021AsPortStatTxPdelayResponseFollowUp,
       "ieee8021AsPortStatTxAnnounce": ieee8021AsPortStatTxAnnounce,
       "ieee8021AsAcceptableMasterTableDS": ieee8021AsAcceptableMasterTableDS,
       "ieee8021AsAcceptableMasterTableDSBase": ieee8021AsAcceptableMasterTableDSBase,
       "ieee8021AsAcceptableMasterTableDSMaxTableSize": ieee8021AsAcceptableMasterTableDSMaxTableSize,
       "ieee8021AsAcceptableMasterTableDSActualTableSize": ieee8021AsAcceptableMasterTableDSActualTableSize,
       "ieee8021AsAcceptableMasterTableDSMaster": ieee8021AsAcceptableMasterTableDSMaster,
       "ieee8021AsAcceptableMasterTableDSMasterTable": ieee8021AsAcceptableMasterTableDSMasterTable,
       "ieee8021AsAcceptableMasterTableDSMasterEntry": ieee8021AsAcceptableMasterTableDSMasterEntry,
       "ieee8021AsAcceptableMasterTableDSMasterId": ieee8021AsAcceptableMasterTableDSMasterId,
       "ieee8021AsAcceptableMasterClockIdentity": ieee8021AsAcceptableMasterClockIdentity,
       "ieee8021AsAcceptableMasterPortNumber": ieee8021AsAcceptableMasterPortNumber,
       "ieee8021AsAcceptableMasterAlternatePriority1": ieee8021AsAcceptableMasterAlternatePriority1,
       "ieee8021AsAcceptableMasterRowStatus": ieee8021AsAcceptableMasterRowStatus,
       "ieee8021AsConformance": ieee8021AsConformance,
       "ieee8021AsCompliances": ieee8021AsCompliances,
       "ieee8021AsCompliance": ieee8021AsCompliance,
       "ieee8021AsComplianceCor1": ieee8021AsComplianceCor1,
       "ieee8021AsGroups": ieee8021AsGroups,
       "ieee8021ASSystemDefaultReqdGroup": ieee8021ASSystemDefaultReqdGroup,
       "ieee8021ASSystemCurrentGroup": ieee8021ASSystemCurrentGroup,
       "ieee8021AsSystemClockParentGroup": ieee8021AsSystemClockParentGroup,
       "ieee8021AsSystemTimePropertiesGroup": ieee8021AsSystemTimePropertiesGroup,
       "ieee8021AsPortDataSetGlobalGroup": ieee8021AsPortDataSetGlobalGroup,
       "ieee8021ASPortStatisticsGlobalGroup": ieee8021ASPortStatisticsGlobalGroup,
       "ieee8021AsAcceptableMasterBaseGroup": ieee8021AsAcceptableMasterBaseGroup,
       "ieee8021AsAcceptableMasterTableGroup": ieee8021AsAcceptableMasterTableGroup,
       "ieee8021AsCompliancesCor1": ieee8021AsCompliancesCor1}
)
