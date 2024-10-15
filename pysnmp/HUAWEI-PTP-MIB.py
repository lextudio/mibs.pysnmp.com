# SNMP MIB module (HUAWEI-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:37 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hwPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



class VlanIdOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_HwPtpGlobalObjects_ObjectIdentity = ObjectIdentity
hwPtpGlobalObjects = _HwPtpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1)
)


class _HwPtpEnable_Type(EnabledStatus):
    """Custom type hwPtpEnable based on EnabledStatus"""


_HwPtpEnable_Object = MibScalar
hwPtpEnable = _HwPtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 1),
    _HwPtpEnable_Type()
)
hwPtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpEnable.setStatus("current")


class _HwPtpDomain_Type(Integer32):
    """Custom type hwPtpDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPtpDomain_Type.__name__ = "Integer32"
_HwPtpDomain_Object = MibScalar
hwPtpDomain = _HwPtpDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 2),
    _HwPtpDomain_Type()
)
hwPtpDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpDomain.setStatus("current")


class _HwPtpDeviceType_Type(Integer32):
    """Custom type hwPtpDeviceType based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("bc", 2),
          ("e2etc", 4),
          ("e2etcoc", 6),
          ("invalid", 99),
          ("oc", 1),
          ("p2ptc", 3),
          ("p2ptcoc", 5),
          ("tcandbc", 7))
    )


_HwPtpDeviceType_Type.__name__ = "Integer32"
_HwPtpDeviceType_Object = MibScalar
hwPtpDeviceType = _HwPtpDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 3),
    _HwPtpDeviceType_Type()
)
hwPtpDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpDeviceType.setStatus("current")


class _HwPtpSlaveOnly_Type(TruthValue):
    """Custom type hwPtpSlaveOnly based on TruthValue"""


_HwPtpSlaveOnly_Object = MibScalar
hwPtpSlaveOnly = _HwPtpSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 4),
    _HwPtpSlaveOnly_Type()
)
hwPtpSlaveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpSlaveOnly.setStatus("current")
_HwPtpLocalClockId_Type = OctetString
_HwPtpLocalClockId_Object = MibScalar
hwPtpLocalClockId = _HwPtpLocalClockId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 5),
    _HwPtpLocalClockId_Type()
)
hwPtpLocalClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpLocalClockId.setStatus("current")


class _HwPtpLocalClockAccuracy_Type(Integer32):
    """Custom type hwPtpLocalClockAccuracy based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPtpLocalClockAccuracy_Type.__name__ = "Integer32"
_HwPtpLocalClockAccuracy_Object = MibScalar
hwPtpLocalClockAccuracy = _HwPtpLocalClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 6),
    _HwPtpLocalClockAccuracy_Type()
)
hwPtpLocalClockAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpLocalClockAccuracy.setStatus("current")


class _HwPtpLocalClockClass_Type(Integer32):
    """Custom type hwPtpLocalClockClass based on Integer32"""
    defaultValue = 187

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwPtpLocalClockClass_Type.__name__ = "Integer32"
_HwPtpLocalClockClass_Object = MibScalar
hwPtpLocalClockClass = _HwPtpLocalClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 7),
    _HwPtpLocalClockClass_Type()
)
hwPtpLocalClockClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpLocalClockClass.setStatus("current")


class _HwPtpLocalClockPriority1_Type(Integer32):
    """Custom type hwPtpLocalClockPriority1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPtpLocalClockPriority1_Type.__name__ = "Integer32"
_HwPtpLocalClockPriority1_Object = MibScalar
hwPtpLocalClockPriority1 = _HwPtpLocalClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 8),
    _HwPtpLocalClockPriority1_Type()
)
hwPtpLocalClockPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpLocalClockPriority1.setStatus("current")


class _HwPtpLocalClockPriority2_Type(Integer32):
    """Custom type hwPtpLocalClockPriority2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPtpLocalClockPriority2_Type.__name__ = "Integer32"
_HwPtpLocalClockPriority2_Object = MibScalar
hwPtpLocalClockPriority2 = _HwPtpLocalClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 9),
    _HwPtpLocalClockPriority2_Type()
)
hwPtpLocalClockPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpLocalClockPriority2.setStatus("current")


class _HwPtpLocalClockTimeSource_Type(Integer32):
    """Custom type hwPtpLocalClockTimeSource based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("atomicclock", 1),
          ("gps", 2),
          ("handset", 6),
          ("internaloscillator", 8),
          ("ntp", 5),
          ("other", 7),
          ("ptp", 4),
          ("terrestrialradio", 3))
    )


_HwPtpLocalClockTimeSource_Type.__name__ = "Integer32"
_HwPtpLocalClockTimeSource_Object = MibScalar
hwPtpLocalClockTimeSource = _HwPtpLocalClockTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 10),
    _HwPtpLocalClockTimeSource_Type()
)
hwPtpLocalClockTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpLocalClockTimeSource.setStatus("current")
_HwPtpUtc_Type = OctetString
_HwPtpUtc_Object = MibScalar
hwPtpUtc = _HwPtpUtc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 11),
    _HwPtpUtc_Type()
)
hwPtpUtc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpUtc.setStatus("current")
_HwPtpCurrentUtcOffset_Type = Integer32
_HwPtpCurrentUtcOffset_Object = MibScalar
hwPtpCurrentUtcOffset = _HwPtpCurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 12),
    _HwPtpCurrentUtcOffset_Type()
)
hwPtpCurrentUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCurrentUtcOffset.setStatus("current")


class _HwCurrentUtcOffsetValid_Type(TruthValue):
    """Custom type hwCurrentUtcOffsetValid based on TruthValue"""


_HwCurrentUtcOffsetValid_Object = MibScalar
hwCurrentUtcOffsetValid = _HwCurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 13),
    _HwCurrentUtcOffsetValid_Type()
)
hwCurrentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCurrentUtcOffsetValid.setStatus("current")


class _HwPtpLeap59orLeap61Valid_Type(Integer32):
    """Custom type hwPtpLeap59orLeap61Valid based on Integer32"""
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
        *(("leap59Valid", 1),
          ("leap61Valid", 2),
          ("none", 3))
    )


_HwPtpLeap59orLeap61Valid_Type.__name__ = "Integer32"
_HwPtpLeap59orLeap61Valid_Object = MibScalar
hwPtpLeap59orLeap61Valid = _HwPtpLeap59orLeap61Valid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 14),
    _HwPtpLeap59orLeap61Valid_Type()
)
hwPtpLeap59orLeap61Valid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpLeap59orLeap61Valid.setStatus("current")


class _HwPtpLeapEmendationTime_Type(DateAndTime):
    """Custom type hwPtpLeapEmendationTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwPtpLeapEmendationTime_Type.__name__ = "DateAndTime"
_HwPtpLeapEmendationTime_Object = MibScalar
hwPtpLeapEmendationTime = _HwPtpLeapEmendationTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 15),
    _HwPtpLeapEmendationTime_Type()
)
hwPtpLeapEmendationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpLeapEmendationTime.setStatus("current")
_HwPtpCurrentMasterClockId_Type = OctetString
_HwPtpCurrentMasterClockId_Object = MibScalar
hwPtpCurrentMasterClockId = _HwPtpCurrentMasterClockId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 16),
    _HwPtpCurrentMasterClockId_Type()
)
hwPtpCurrentMasterClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpCurrentMasterClockId.setStatus("current")
_HwPtpCurrentMasterClockReceivePort_Type = OctetString
_HwPtpCurrentMasterClockReceivePort_Object = MibScalar
hwPtpCurrentMasterClockReceivePort = _HwPtpCurrentMasterClockReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 17),
    _HwPtpCurrentMasterClockReceivePort_Type()
)
hwPtpCurrentMasterClockReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpCurrentMasterClockReceivePort.setStatus("current")


class _HwPtpCurrentMasterClockStepRemoved_Type(Integer32):
    """Custom type hwPtpCurrentMasterClockStepRemoved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwPtpCurrentMasterClockStepRemoved_Type.__name__ = "Integer32"
_HwPtpCurrentMasterClockStepRemoved_Object = MibScalar
hwPtpCurrentMasterClockStepRemoved = _HwPtpCurrentMasterClockStepRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 18),
    _HwPtpCurrentMasterClockStepRemoved_Type()
)
hwPtpCurrentMasterClockStepRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpCurrentMasterClockStepRemoved.setStatus("current")


class _HwPtpVersion_Type(Integer32):
    """Custom type hwPtpVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ieee1588v2", 1),
          ("invalid", 10))
    )


_HwPtpVersion_Type.__name__ = "Integer32"
_HwPtpVersion_Object = MibScalar
hwPtpVersion = _HwPtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 19),
    _HwPtpVersion_Type()
)
hwPtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpVersion.setStatus("current")


class _HwPtpTimeScale_Type(Integer32):
    """Custom type hwPtpTimeScale based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arb", 2),
          ("ptp", 1))
    )


_HwPtpTimeScale_Type.__name__ = "Integer32"
_HwPtpTimeScale_Object = MibScalar
hwPtpTimeScale = _HwPtpTimeScale_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 20),
    _HwPtpTimeScale_Type()
)
hwPtpTimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpTimeScale.setStatus("current")


class _HwPtpFrequencyTraceable_Type(TruthValue):
    """Custom type hwPtpFrequencyTraceable based on TruthValue"""


_HwPtpFrequencyTraceable_Object = MibScalar
hwPtpFrequencyTraceable = _HwPtpFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 21),
    _HwPtpFrequencyTraceable_Type()
)
hwPtpFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpFrequencyTraceable.setStatus("current")


class _HwPtpTimeTraceable_Type(TruthValue):
    """Custom type hwPtpTimeTraceable based on TruthValue"""


_HwPtpTimeTraceable_Object = MibScalar
hwPtpTimeTraceable = _HwPtpTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 22),
    _HwPtpTimeTraceable_Type()
)
hwPtpTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpTimeTraceable.setStatus("current")


class _HwPtpTimeSynchronizationStatus_Type(Integer32):
    """Custom type hwPtpTimeSynchronizationStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("synchronization", 2),
          ("unsynchronization", 1))
    )


_HwPtpTimeSynchronizationStatus_Type.__name__ = "Integer32"
_HwPtpTimeSynchronizationStatus_Object = MibScalar
hwPtpTimeSynchronizationStatus = _HwPtpTimeSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 1, 23),
    _HwPtpTimeSynchronizationStatus_Type()
)
hwPtpTimeSynchronizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpTimeSynchronizationStatus.setStatus("current")
_HwPtpPortObjects_ObjectIdentity = ObjectIdentity
hwPtpPortObjects = _HwPtpPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2)
)
_HwPtpPortTable_Object = MibTable
hwPtpPortTable = _HwPtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1)
)
if mibBuilder.loadTexts:
    hwPtpPortTable.setStatus("current")
_HwPtpPortEntry_Object = MibTableRow
hwPtpPortEntry = _HwPtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1)
)
hwPtpPortEntry.setIndexNames(
    (0, "HUAWEI-PTP-MIB", "hwPtpPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwPtpPortEntry.setStatus("current")
_HwPtpPortIfIndex_Type = InterfaceIndex
_HwPtpPortIfIndex_Object = MibTableColumn
hwPtpPortIfIndex = _HwPtpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 1),
    _HwPtpPortIfIndex_Type()
)
hwPtpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPtpPortIfIndex.setStatus("current")


class _HwPtpPortEnable_Type(EnabledStatus):
    """Custom type hwPtpPortEnable based on EnabledStatus"""


_HwPtpPortEnable_Object = MibTableColumn
hwPtpPortEnable = _HwPtpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 2),
    _HwPtpPortEnable_Type()
)
hwPtpPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortEnable.setStatus("current")


class _HwPtpPortDelayMechanism_Type(Integer32):
    """Custom type hwPtpPortDelayMechanism based on Integer32"""
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
        *(("delay", 2),
          ("none", 1),
          ("pdelay", 3))
    )


_HwPtpPortDelayMechanism_Type.__name__ = "Integer32"
_HwPtpPortDelayMechanism_Object = MibTableColumn
hwPtpPortDelayMechanism = _HwPtpPortDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 3),
    _HwPtpPortDelayMechanism_Type()
)
hwPtpPortDelayMechanism.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortDelayMechanism.setStatus("current")


class _HwPtpPortType_Type(Integer32):
    """Custom type hwPtpPortType based on Integer32"""
    defaultValue = 1

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
        *(("bc", 3),
          ("none", 1),
          ("oc", 5),
          ("tc", 2),
          ("tcoc", 4))
    )


_HwPtpPortType_Type.__name__ = "Integer32"
_HwPtpPortType_Object = MibTableColumn
hwPtpPortType = _HwPtpPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 4),
    _HwPtpPortType_Type()
)
hwPtpPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortType.setStatus("current")


class _HwPtpPortDomain_Type(Integer32):
    """Custom type hwPtpPortDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPtpPortDomain_Type.__name__ = "Integer32"
_HwPtpPortDomain_Object = MibTableColumn
hwPtpPortDomain = _HwPtpPortDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 5),
    _HwPtpPortDomain_Type()
)
hwPtpPortDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortDomain.setStatus("current")
_HwPtpPortTcOcStaticClockId_Type = OctetString
_HwPtpPortTcOcStaticClockId_Object = MibTableColumn
hwPtpPortTcOcStaticClockId = _HwPtpPortTcOcStaticClockId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 6),
    _HwPtpPortTcOcStaticClockId_Type()
)
hwPtpPortTcOcStaticClockId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortTcOcStaticClockId.setStatus("current")


class _HwPtpPortTcOcStaticClockPortNum_Type(Integer32):
    """Custom type hwPtpPortTcOcStaticClockPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPtpPortTcOcStaticClockPortNum_Type.__name__ = "Integer32"
_HwPtpPortTcOcStaticClockPortNum_Object = MibTableColumn
hwPtpPortTcOcStaticClockPortNum = _HwPtpPortTcOcStaticClockPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 7),
    _HwPtpPortTcOcStaticClockPortNum_Type()
)
hwPtpPortTcOcStaticClockPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortTcOcStaticClockPortNum.setStatus("current")


class _HwPtpPortAnnounceInterval_Type(Integer32):
    """Custom type hwPtpPortAnnounceInterval based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HwPtpPortAnnounceInterval_Type.__name__ = "Integer32"
_HwPtpPortAnnounceInterval_Object = MibTableColumn
hwPtpPortAnnounceInterval = _HwPtpPortAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 8),
    _HwPtpPortAnnounceInterval_Type()
)
hwPtpPortAnnounceInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortAnnounceInterval.setStatus("current")


class _HwPtpPortAnnounceReceipTimeout_Type(Integer32):
    """Custom type hwPtpPortAnnounceReceipTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HwPtpPortAnnounceReceipTimeout_Type.__name__ = "Integer32"
_HwPtpPortAnnounceReceipTimeout_Object = MibTableColumn
hwPtpPortAnnounceReceipTimeout = _HwPtpPortAnnounceReceipTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 9),
    _HwPtpPortAnnounceReceipTimeout_Type()
)
hwPtpPortAnnounceReceipTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortAnnounceReceipTimeout.setStatus("current")


class _HwPtpPortSyncInterval_Type(Integer32):
    """Custom type hwPtpPortSyncInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HwPtpPortSyncInterval_Type.__name__ = "Integer32"
_HwPtpPortSyncInterval_Object = MibTableColumn
hwPtpPortSyncInterval = _HwPtpPortSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 10),
    _HwPtpPortSyncInterval_Type()
)
hwPtpPortSyncInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortSyncInterval.setStatus("current")


class _HwPtpPortMinDelayReqInterval_Type(Integer32):
    """Custom type hwPtpPortMinDelayReqInterval based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HwPtpPortMinDelayReqInterval_Type.__name__ = "Integer32"
_HwPtpPortMinDelayReqInterval_Object = MibTableColumn
hwPtpPortMinDelayReqInterval = _HwPtpPortMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 11),
    _HwPtpPortMinDelayReqInterval_Type()
)
hwPtpPortMinDelayReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortMinDelayReqInterval.setStatus("current")


class _HwPtpPortMinPdelayReqInterval_Type(Integer32):
    """Custom type hwPtpPortMinPdelayReqInterval based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HwPtpPortMinPdelayReqInterval_Type.__name__ = "Integer32"
_HwPtpPortMinPdelayReqInterval_Object = MibTableColumn
hwPtpPortMinPdelayReqInterval = _HwPtpPortMinPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 12),
    _HwPtpPortMinPdelayReqInterval_Type()
)
hwPtpPortMinPdelayReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortMinPdelayReqInterval.setStatus("current")


class _HwPtpPortAsymmetryNegativeCorrection_Type(Unsigned32):
    """Custom type hwPtpPortAsymmetryNegativeCorrection based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_HwPtpPortAsymmetryNegativeCorrection_Type.__name__ = "Unsigned32"
_HwPtpPortAsymmetryNegativeCorrection_Object = MibTableColumn
hwPtpPortAsymmetryNegativeCorrection = _HwPtpPortAsymmetryNegativeCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 13),
    _HwPtpPortAsymmetryNegativeCorrection_Type()
)
hwPtpPortAsymmetryNegativeCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortAsymmetryNegativeCorrection.setStatus("current")


class _HwPtpPortAsymmetryPositiveCorrection_Type(Unsigned32):
    """Custom type hwPtpPortAsymmetryPositiveCorrection based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_HwPtpPortAsymmetryPositiveCorrection_Type.__name__ = "Unsigned32"
_HwPtpPortAsymmetryPositiveCorrection_Object = MibTableColumn
hwPtpPortAsymmetryPositiveCorrection = _HwPtpPortAsymmetryPositiveCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 14),
    _HwPtpPortAsymmetryPositiveCorrection_Type()
)
hwPtpPortAsymmetryPositiveCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortAsymmetryPositiveCorrection.setStatus("current")


class _HwPtpPortMacEgressDestinationMac_Type(MacAddress):
    """Custom type hwPtpPortMacEgressDestinationMac based on MacAddress"""
    defaultHexValue = ""


_HwPtpPortMacEgressDestinationMac_Object = MibTableColumn
hwPtpPortMacEgressDestinationMac = _HwPtpPortMacEgressDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 15),
    _HwPtpPortMacEgressDestinationMac_Type()
)
hwPtpPortMacEgressDestinationMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortMacEgressDestinationMac.setStatus("current")


class _HwPtpPortMacEgressVlanId_Type(VlanIdOrNone):
    """Custom type hwPtpPortMacEgressVlanId based on VlanIdOrNone"""
    defaultValue = 0


_HwPtpPortMacEgressVlanId_Object = MibTableColumn
hwPtpPortMacEgressVlanId = _HwPtpPortMacEgressVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 16),
    _HwPtpPortMacEgressVlanId_Type()
)
hwPtpPortMacEgressVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortMacEgressVlanId.setStatus("current")


class _HwPtpPortMacEgressPacketPriority_Type(Integer32):
    """Custom type hwPtpPortMacEgressPacketPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwPtpPortMacEgressPacketPriority_Type.__name__ = "Integer32"
_HwPtpPortMacEgressPacketPriority_Object = MibTableColumn
hwPtpPortMacEgressPacketPriority = _HwPtpPortMacEgressPacketPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 17),
    _HwPtpPortMacEgressPacketPriority_Type()
)
hwPtpPortMacEgressPacketPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortMacEgressPacketPriority.setStatus("current")
_HwPtpPortUdpEgressSourceIp_Type = IpAddress
_HwPtpPortUdpEgressSourceIp_Object = MibTableColumn
hwPtpPortUdpEgressSourceIp = _HwPtpPortUdpEgressSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 18),
    _HwPtpPortUdpEgressSourceIp_Type()
)
hwPtpPortUdpEgressSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortUdpEgressSourceIp.setStatus("current")
_HwPtpPortUdpEgressDestinationIp_Type = IpAddress
_HwPtpPortUdpEgressDestinationIp_Object = MibTableColumn
hwPtpPortUdpEgressDestinationIp = _HwPtpPortUdpEgressDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 19),
    _HwPtpPortUdpEgressDestinationIp_Type()
)
hwPtpPortUdpEgressDestinationIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortUdpEgressDestinationIp.setStatus("current")


class _HwPtpPortUdpEgressDestinationMac_Type(MacAddress):
    """Custom type hwPtpPortUdpEgressDestinationMac based on MacAddress"""
    defaultHexValue = ""


_HwPtpPortUdpEgressDestinationMac_Object = MibTableColumn
hwPtpPortUdpEgressDestinationMac = _HwPtpPortUdpEgressDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 20),
    _HwPtpPortUdpEgressDestinationMac_Type()
)
hwPtpPortUdpEgressDestinationMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortUdpEgressDestinationMac.setStatus("current")


class _HwPtpPortUdpEgressDscp_Type(Integer32):
    """Custom type hwPtpPortUdpEgressDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwPtpPortUdpEgressDscp_Type.__name__ = "Integer32"
_HwPtpPortUdpEgressDscp_Object = MibTableColumn
hwPtpPortUdpEgressDscp = _HwPtpPortUdpEgressDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 21),
    _HwPtpPortUdpEgressDscp_Type()
)
hwPtpPortUdpEgressDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortUdpEgressDscp.setStatus("current")


class _HwPtpPortUdpEgressVlanId_Type(VlanIdOrNone):
    """Custom type hwPtpPortUdpEgressVlanId based on VlanIdOrNone"""
    defaultValue = 0


_HwPtpPortUdpEgressVlanId_Object = MibTableColumn
hwPtpPortUdpEgressVlanId = _HwPtpPortUdpEgressVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 22),
    _HwPtpPortUdpEgressVlanId_Type()
)
hwPtpPortUdpEgressVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortUdpEgressVlanId.setStatus("current")


class _HwPtpPortUdpEgressPacketPriority_Type(Integer32):
    """Custom type hwPtpPortUdpEgressPacketPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwPtpPortUdpEgressPacketPriority_Type.__name__ = "Integer32"
_HwPtpPortUdpEgressPacketPriority_Object = MibTableColumn
hwPtpPortUdpEgressPacketPriority = _HwPtpPortUdpEgressPacketPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 23),
    _HwPtpPortUdpEgressPacketPriority_Type()
)
hwPtpPortUdpEgressPacketPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortUdpEgressPacketPriority.setStatus("current")


class _HwPtpPortAnnounceDrop_Type(EnabledStatus):
    """Custom type hwPtpPortAnnounceDrop based on EnabledStatus"""


_HwPtpPortAnnounceDrop_Object = MibTableColumn
hwPtpPortAnnounceDrop = _HwPtpPortAnnounceDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 24),
    _HwPtpPortAnnounceDrop_Type()
)
hwPtpPortAnnounceDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortAnnounceDrop.setStatus("current")


class _HwPtpPortState_Type(Integer32):
    """Custom type hwPtpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 8),
          ("faulty", 5),
          ("initializing", 6),
          ("listening", 4),
          ("master", 1),
          ("passive", 3),
          ("premaster", 7),
          ("slave", 2),
          ("uncalibrated", 9))
    )


_HwPtpPortState_Type.__name__ = "Integer32"
_HwPtpPortState_Object = MibTableColumn
hwPtpPortState = _HwPtpPortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 25),
    _HwPtpPortState_Type()
)
hwPtpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortState.setStatus("current")
_HwPtpPortSourcePortClockId_Type = OctetString
_HwPtpPortSourcePortClockId_Object = MibTableColumn
hwPtpPortSourcePortClockId = _HwPtpPortSourcePortClockId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 26),
    _HwPtpPortSourcePortClockId_Type()
)
hwPtpPortSourcePortClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortSourcePortClockId.setStatus("current")


class _HwPtpPortSourcePortNum_Type(Integer32):
    """Custom type hwPtpPortSourcePortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPtpPortSourcePortNum_Type.__name__ = "Integer32"
_HwPtpPortSourcePortNum_Object = MibTableColumn
hwPtpPortSourcePortNum = _HwPtpPortSourcePortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 27),
    _HwPtpPortSourcePortNum_Type()
)
hwPtpPortSourcePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortSourcePortNum.setStatus("current")
_HwPtpPortPortVlan_Type = Integer32
_HwPtpPortPortVlan_Object = MibTableColumn
hwPtpPortPortVlan = _HwPtpPortPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 28),
    _HwPtpPortPortVlan_Type()
)
hwPtpPortPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortPortVlan.setStatus("current")


class _HwPtpPortCfgLinkStatus_Type(Integer32):
    """Custom type hwPtpPortCfgLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HwPtpPortCfgLinkStatus_Type.__name__ = "Integer32"
_HwPtpPortCfgLinkStatus_Object = MibTableColumn
hwPtpPortCfgLinkStatus = _HwPtpPortCfgLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 30),
    _HwPtpPortCfgLinkStatus_Type()
)
hwPtpPortCfgLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortCfgLinkStatus.setStatus("current")


class _HwPtpPortCfgExtInterfaceMode_Type(Integer32):
    """Custom type hwPtpPortCfgExtInterfaceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extclock", 1),
          ("exttime", 2))
    )


_HwPtpPortCfgExtInterfaceMode_Type.__name__ = "Integer32"
_HwPtpPortCfgExtInterfaceMode_Object = MibTableColumn
hwPtpPortCfgExtInterfaceMode = _HwPtpPortCfgExtInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 31),
    _HwPtpPortCfgExtInterfaceMode_Type()
)
hwPtpPortCfgExtInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortCfgExtInterfaceMode.setStatus("current")


class _HwPtpPortCfgMsgFormat_Type(Integer32):
    """Custom type hwPtpPortCfgMsgFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptpeth", 1),
          ("ptpip", 2))
    )


_HwPtpPortCfgMsgFormat_Type.__name__ = "Integer32"
_HwPtpPortCfgMsgFormat_Object = MibTableColumn
hwPtpPortCfgMsgFormat = _HwPtpPortCfgMsgFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 32),
    _HwPtpPortCfgMsgFormat_Type()
)
hwPtpPortCfgMsgFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortCfgMsgFormat.setStatus("current")
_HwPtpPortRowStatus_Type = RowStatus
_HwPtpPortRowStatus_Object = MibTableColumn
hwPtpPortRowStatus = _HwPtpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 1, 1, 51),
    _HwPtpPortRowStatus_Type()
)
hwPtpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpPortRowStatus.setStatus("current")
_HwPtpPortStatisticTable_Object = MibTable
hwPtpPortStatisticTable = _HwPtpPortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2)
)
if mibBuilder.loadTexts:
    hwPtpPortStatisticTable.setStatus("current")
_HwPtpPortStatisticEntry_Object = MibTableRow
hwPtpPortStatisticEntry = _HwPtpPortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1)
)
hwPtpPortStatisticEntry.setIndexNames(
    (0, "HUAWEI-PTP-MIB", "hwPtpPortStatisticIfIndex"),
)
if mibBuilder.loadTexts:
    hwPtpPortStatisticEntry.setStatus("current")
_HwPtpPortStatisticIfIndex_Type = InterfaceIndex
_HwPtpPortStatisticIfIndex_Object = MibTableColumn
hwPtpPortStatisticIfIndex = _HwPtpPortStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 1),
    _HwPtpPortStatisticIfIndex_Type()
)
hwPtpPortStatisticIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPtpPortStatisticIfIndex.setStatus("current")
_HwPtpPortRxPtpTrsprnsPktCnt_Type = Unsigned32
_HwPtpPortRxPtpTrsprnsPktCnt_Object = MibTableColumn
hwPtpPortRxPtpTrsprnsPktCnt = _HwPtpPortRxPtpTrsprnsPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 2),
    _HwPtpPortRxPtpTrsprnsPktCnt_Type()
)
hwPtpPortRxPtpTrsprnsPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortRxPtpTrsprnsPktCnt.setStatus("current")
_HwPtpPortRxPtpDiscardTrsprnsPktCnt_Type = Unsigned32
_HwPtpPortRxPtpDiscardTrsprnsPktCnt_Object = MibTableColumn
hwPtpPortRxPtpDiscardTrsprnsPktCnt = _HwPtpPortRxPtpDiscardTrsprnsPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 3),
    _HwPtpPortRxPtpDiscardTrsprnsPktCnt_Type()
)
hwPtpPortRxPtpDiscardTrsprnsPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortRxPtpDiscardTrsprnsPktCnt.setStatus("current")
_HwPtpPortRxPtpEndPktCnt_Type = Unsigned32
_HwPtpPortRxPtpEndPktCnt_Object = MibTableColumn
hwPtpPortRxPtpEndPktCnt = _HwPtpPortRxPtpEndPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 4),
    _HwPtpPortRxPtpEndPktCnt_Type()
)
hwPtpPortRxPtpEndPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortRxPtpEndPktCnt.setStatus("current")
_HwPtpPortRxPtpDiscardEndPktCnt_Type = Unsigned32
_HwPtpPortRxPtpDiscardEndPktCnt_Object = MibTableColumn
hwPtpPortRxPtpDiscardEndPktCnt = _HwPtpPortRxPtpDiscardEndPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 5),
    _HwPtpPortRxPtpDiscardEndPktCnt_Type()
)
hwPtpPortRxPtpDiscardEndPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortRxPtpDiscardEndPktCnt.setStatus("current")
_HwPtpPortRxPtpAnnouncePktCnt_Type = Unsigned32
_HwPtpPortRxPtpAnnouncePktCnt_Object = MibTableColumn
hwPtpPortRxPtpAnnouncePktCnt = _HwPtpPortRxPtpAnnouncePktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 6),
    _HwPtpPortRxPtpAnnouncePktCnt_Type()
)
hwPtpPortRxPtpAnnouncePktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortRxPtpAnnouncePktCnt.setStatus("current")
_HwPtpPortRxPtpSyncPktCnt_Type = Unsigned32
_HwPtpPortRxPtpSyncPktCnt_Object = MibTableColumn
hwPtpPortRxPtpSyncPktCnt = _HwPtpPortRxPtpSyncPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 7),
    _HwPtpPortRxPtpSyncPktCnt_Type()
)
hwPtpPortRxPtpSyncPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortRxPtpSyncPktCnt.setStatus("current")
_HwPtpPortTxPtpDiscardReqCnt_Type = Unsigned32
_HwPtpPortTxPtpDiscardReqCnt_Object = MibTableColumn
hwPtpPortTxPtpDiscardReqCnt = _HwPtpPortTxPtpDiscardReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 8),
    _HwPtpPortTxPtpDiscardReqCnt_Type()
)
hwPtpPortTxPtpDiscardReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortTxPtpDiscardReqCnt.setStatus("current")
_HwPtpPortTxFifoDiscardPktCn_Type = Unsigned32
_HwPtpPortTxFifoDiscardPktCn_Object = MibTableColumn
hwPtpPortTxFifoDiscardPktCn = _HwPtpPortTxFifoDiscardPktCn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 9),
    _HwPtpPortTxFifoDiscardPktCn_Type()
)
hwPtpPortTxFifoDiscardPktCn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpPortTxFifoDiscardPktCn.setStatus("current")


class _HwPtpPortStaticPktReset_Type(Integer32):
    """Custom type hwPtpPortStaticPktReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 2))
    )


_HwPtpPortStaticPktReset_Type.__name__ = "Integer32"
_HwPtpPortStaticPktReset_Object = MibTableColumn
hwPtpPortStaticPktReset = _HwPtpPortStaticPktReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 2, 1, 20),
    _HwPtpPortStaticPktReset_Type()
)
hwPtpPortStaticPktReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpPortStaticPktReset.setStatus("current")
_HwPtpBitsClockSourceTable_Object = MibTable
hwPtpBitsClockSourceTable = _HwPtpBitsClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3)
)
if mibBuilder.loadTexts:
    hwPtpBitsClockSourceTable.setStatus("current")
_HwPtpBitsClockSourceEntry_Object = MibTableRow
hwPtpBitsClockSourceEntry = _HwPtpBitsClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1)
)
hwPtpBitsClockSourceEntry.setIndexNames(
    (0, "HUAWEI-PTP-MIB", "hwPtpBitsPortIndex"),
)
if mibBuilder.loadTexts:
    hwPtpBitsClockSourceEntry.setStatus("current")


class _HwPtpBitsPortIndex_Type(Integer32):
    """Custom type hwPtpBitsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwPtpBitsPortIndex_Type.__name__ = "Integer32"
_HwPtpBitsPortIndex_Object = MibTableColumn
hwPtpBitsPortIndex = _HwPtpBitsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 1),
    _HwPtpBitsPortIndex_Type()
)
hwPtpBitsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPtpBitsPortIndex.setStatus("current")


class _HwPtpBitsClockAccuracy_Type(Integer32):
    """Custom type hwPtpBitsClockAccuracy based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPtpBitsClockAccuracy_Type.__name__ = "Integer32"
_HwPtpBitsClockAccuracy_Object = MibTableColumn
hwPtpBitsClockAccuracy = _HwPtpBitsClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 2),
    _HwPtpBitsClockAccuracy_Type()
)
hwPtpBitsClockAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpBitsClockAccuracy.setStatus("current")


class _HwPtpBitsClockClass_Type(Integer32):
    """Custom type hwPtpBitsClockClass based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwPtpBitsClockClass_Type.__name__ = "Integer32"
_HwPtpBitsClockClass_Object = MibTableColumn
hwPtpBitsClockClass = _HwPtpBitsClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 3),
    _HwPtpBitsClockClass_Type()
)
hwPtpBitsClockClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpBitsClockClass.setStatus("current")


class _HwPtpBitsPriority1_Type(Integer32):
    """Custom type hwPtpBitsPriority1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPtpBitsPriority1_Type.__name__ = "Integer32"
_HwPtpBitsPriority1_Object = MibTableColumn
hwPtpBitsPriority1 = _HwPtpBitsPriority1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 4),
    _HwPtpBitsPriority1_Type()
)
hwPtpBitsPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpBitsPriority1.setStatus("current")


class _HwPtpBitsPriority2_Type(Integer32):
    """Custom type hwPtpBitsPriority2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPtpBitsPriority2_Type.__name__ = "Integer32"
_HwPtpBitsPriority2_Object = MibTableColumn
hwPtpBitsPriority2 = _HwPtpBitsPriority2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 5),
    _HwPtpBitsPriority2_Type()
)
hwPtpBitsPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpBitsPriority2.setStatus("current")


class _HwPtpBitsTimeSource_Type(Integer32):
    """Custom type hwPtpBitsTimeSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("atomicclock", 1),
          ("gps", 2),
          ("handset", 6),
          ("internaloscillator", 8),
          ("ntp", 5),
          ("other", 7),
          ("ptp", 4),
          ("terrestrialradio", 3))
    )


_HwPtpBitsTimeSource_Type.__name__ = "Integer32"
_HwPtpBitsTimeSource_Object = MibTableColumn
hwPtpBitsTimeSource = _HwPtpBitsTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 6),
    _HwPtpBitsTimeSource_Type()
)
hwPtpBitsTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpBitsTimeSource.setStatus("current")


class _HwPtpBitsSignal_Type(Integer32):
    """Custom type hwPtpBitsSignal based on Integer32"""
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
        *(("dcls", 4),
          ("none", 5),
          ("oneppsandrs232", 1),
          ("twombps", 3),
          ("twomhz", 2))
    )


_HwPtpBitsSignal_Type.__name__ = "Integer32"
_HwPtpBitsSignal_Object = MibTableColumn
hwPtpBitsSignal = _HwPtpBitsSignal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 7),
    _HwPtpBitsSignal_Type()
)
hwPtpBitsSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpBitsSignal.setStatus("current")


class _HwPtpBitsSwitch_Type(Integer32):
    """Custom type hwPtpBitsSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HwPtpBitsSwitch_Type.__name__ = "Integer32"
_HwPtpBitsSwitch_Object = MibTableColumn
hwPtpBitsSwitch = _HwPtpBitsSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 8),
    _HwPtpBitsSwitch_Type()
)
hwPtpBitsSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpBitsSwitch.setStatus("current")


class _HwPtpBitsDirection_Type(Integer32):
    """Custom type hwPtpBitsDirection based on Integer32"""
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
        *(("both", 3),
          ("in", 1),
          ("none", 4),
          ("out", 2))
    )


_HwPtpBitsDirection_Type.__name__ = "Integer32"
_HwPtpBitsDirection_Object = MibTableColumn
hwPtpBitsDirection = _HwPtpBitsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 9),
    _HwPtpBitsDirection_Type()
)
hwPtpBitsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpBitsDirection.setStatus("current")


class _HwPtpBitsNormalStatus_Type(Integer32):
    """Custom type hwPtpBitsNormalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_HwPtpBitsNormalStatus_Type.__name__ = "Integer32"
_HwPtpBitsNormalStatus_Object = MibTableColumn
hwPtpBitsNormalStatus = _HwPtpBitsNormalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 10),
    _HwPtpBitsNormalStatus_Type()
)
hwPtpBitsNormalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPtpBitsNormalStatus.setStatus("current")


class _HwPtpReceiveDelay_Type(Integer32):
    """Custom type hwPtpReceiveDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_HwPtpReceiveDelay_Type.__name__ = "Integer32"
_HwPtpReceiveDelay_Object = MibTableColumn
hwPtpReceiveDelay = _HwPtpReceiveDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 11),
    _HwPtpReceiveDelay_Type()
)
hwPtpReceiveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpReceiveDelay.setStatus("current")


class _HwPtpSendDelay_Type(Integer32):
    """Custom type hwPtpSendDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1600),
    )


_HwPtpSendDelay_Type.__name__ = "Integer32"
_HwPtpSendDelay_Object = MibTableColumn
hwPtpSendDelay = _HwPtpSendDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 2, 3, 1, 12),
    _HwPtpSendDelay_Type()
)
hwPtpSendDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpSendDelay.setStatus("current")
_HwPtpExtInterfaceTable_Object = MibTable
hwPtpExtInterfaceTable = _HwPtpExtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 3)
)
if mibBuilder.loadTexts:
    hwPtpExtInterfaceTable.setStatus("current")
_HwPtpExtInterfaceEntry_Object = MibTableRow
hwPtpExtInterfaceEntry = _HwPtpExtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 3, 1)
)
hwPtpExtInterfaceEntry.setIndexNames(
    (0, "HUAWEI-PTP-MIB", "hwPtpExtInterfaceOperateIndex"),
)
if mibBuilder.loadTexts:
    hwPtpExtInterfaceEntry.setStatus("current")


class _HwPtpExtInterfaceOperateIndex_Type(Integer32):
    """Custom type hwPtpExtInterfaceOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HwPtpExtInterfaceOperateIndex_Type.__name__ = "Integer32"
_HwPtpExtInterfaceOperateIndex_Object = MibTableColumn
hwPtpExtInterfaceOperateIndex = _HwPtpExtInterfaceOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 3, 1, 1),
    _HwPtpExtInterfaceOperateIndex_Type()
)
hwPtpExtInterfaceOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPtpExtInterfaceOperateIndex.setStatus("current")


class _HwPtpExtInterfaceOperateType_Type(Integer32):
    """Custom type hwPtpExtInterfaceOperateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setelectriclevel", 2),
          ("setprotocltype", 1))
    )


_HwPtpExtInterfaceOperateType_Type.__name__ = "Integer32"
_HwPtpExtInterfaceOperateType_Object = MibTableColumn
hwPtpExtInterfaceOperateType = _HwPtpExtInterfaceOperateType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 3, 1, 2),
    _HwPtpExtInterfaceOperateType_Type()
)
hwPtpExtInterfaceOperateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpExtInterfaceOperateType.setStatus("current")
_HwPtpExtInterfaceIfIndex_Type = InterfaceIndex
_HwPtpExtInterfaceIfIndex_Object = MibTableColumn
hwPtpExtInterfaceIfIndex = _HwPtpExtInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 3, 1, 3),
    _HwPtpExtInterfaceIfIndex_Type()
)
hwPtpExtInterfaceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpExtInterfaceIfIndex.setStatus("current")


class _HwPtpExtInterfaceDirect_Type(Integer32):
    """Custom type hwPtpExtInterfaceDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_HwPtpExtInterfaceDirect_Type.__name__ = "Integer32"
_HwPtpExtInterfaceDirect_Object = MibTableColumn
hwPtpExtInterfaceDirect = _HwPtpExtInterfaceDirect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 3, 1, 4),
    _HwPtpExtInterfaceDirect_Type()
)
hwPtpExtInterfaceDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpExtInterfaceDirect.setStatus("current")


class _HwPtpExtInterfaceProtocoltype_Type(Integer32):
    """Custom type hwPtpExtInterfaceProtocoltype based on Integer32"""
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
        *(("dcls", 1),
          ("j211", 3),
          ("time1pps", 2))
    )


_HwPtpExtInterfaceProtocoltype_Type.__name__ = "Integer32"
_HwPtpExtInterfaceProtocoltype_Object = MibTableColumn
hwPtpExtInterfaceProtocoltype = _HwPtpExtInterfaceProtocoltype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 3, 1, 5),
    _HwPtpExtInterfaceProtocoltype_Type()
)
hwPtpExtInterfaceProtocoltype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpExtInterfaceProtocoltype.setStatus("current")


class _HwPtpExtInterfaceElectricLevel_Type(Integer32):
    """Custom type hwPtpExtInterfaceElectricLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 2),
          ("rs422", 3),
          ("ttl", 1))
    )


_HwPtpExtInterfaceElectricLevel_Type.__name__ = "Integer32"
_HwPtpExtInterfaceElectricLevel_Object = MibTableColumn
hwPtpExtInterfaceElectricLevel = _HwPtpExtInterfaceElectricLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 3, 1, 6),
    _HwPtpExtInterfaceElectricLevel_Type()
)
hwPtpExtInterfaceElectricLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPtpExtInterfaceElectricLevel.setStatus("current")
_HwPtpCableLengthTable_ObjectIdentity = ObjectIdentity
hwPtpCableLengthTable = _HwPtpCableLengthTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 4)
)
_HwPtpCableLengthIfindex_Type = InterfaceIndex
_HwPtpCableLengthIfindex_Object = MibScalar
hwPtpCableLengthIfindex = _HwPtpCableLengthIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 4, 1),
    _HwPtpCableLengthIfindex_Type()
)
hwPtpCableLengthIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCableLengthIfindex.setStatus("current")


class _HwPtpCableLengthTransDirect_Type(Integer32):
    """Custom type hwPtpCableLengthTransDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("receive", 0),
          ("send", 1))
    )


_HwPtpCableLengthTransDirect_Type.__name__ = "Integer32"
_HwPtpCableLengthTransDirect_Object = MibScalar
hwPtpCableLengthTransDirect = _HwPtpCableLengthTransDirect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 4, 2),
    _HwPtpCableLengthTransDirect_Type()
)
hwPtpCableLengthTransDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCableLengthTransDirect.setStatus("current")


class _HwPtpCableLengthMode_Type(Integer32):
    """Custom type hwPtpCableLengthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("length", 0),
          ("time", 1))
    )


_HwPtpCableLengthMode_Type.__name__ = "Integer32"
_HwPtpCableLengthMode_Object = MibScalar
hwPtpCableLengthMode = _HwPtpCableLengthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 4, 3),
    _HwPtpCableLengthMode_Type()
)
hwPtpCableLengthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCableLengthMode.setStatus("current")
_HwPtpCableLengthTransDistance_Type = Integer32
_HwPtpCableLengthTransDistance_Object = MibScalar
hwPtpCableLengthTransDistance = _HwPtpCableLengthTransDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 4, 4),
    _HwPtpCableLengthTransDistance_Type()
)
hwPtpCableLengthTransDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCableLengthTransDistance.setStatus("current")
_HwPtpCableTransTable_ObjectIdentity = ObjectIdentity
hwPtpCableTransTable = _HwPtpCableTransTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 5)
)
_HwPtpCableTransIfindex_Type = InterfaceIndex
_HwPtpCableTransIfindex_Object = MibScalar
hwPtpCableTransIfindex = _HwPtpCableTransIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 5, 1),
    _HwPtpCableTransIfindex_Type()
)
hwPtpCableTransIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCableTransIfindex.setStatus("current")


class _HwPtpCableTransWarpMode_Type(Integer32):
    """Custom type hwPtpCableTransWarpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("length", 0),
          ("time", 1))
    )


_HwPtpCableTransWarpMode_Type.__name__ = "Integer32"
_HwPtpCableTransWarpMode_Object = MibScalar
hwPtpCableTransWarpMode = _HwPtpCableTransWarpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 5, 2),
    _HwPtpCableTransWarpMode_Type()
)
hwPtpCableTransWarpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCableTransWarpMode.setStatus("current")


class _HwPtpCableTransWarpDirect_Type(Integer32):
    """Custom type hwPtpCableTransWarpDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("negative", 1),
          ("positive", 0))
    )


_HwPtpCableTransWarpDirect_Type.__name__ = "Integer32"
_HwPtpCableTransWarpDirect_Object = MibScalar
hwPtpCableTransWarpDirect = _HwPtpCableTransWarpDirect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 5, 3),
    _HwPtpCableTransWarpDirect_Type()
)
hwPtpCableTransWarpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCableTransWarpDirect.setStatus("current")
_HwPtpCableTransWarpValue_Type = Integer32
_HwPtpCableTransWarpValue_Object = MibScalar
hwPtpCableTransWarpValue = _HwPtpCableTransWarpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 5, 4),
    _HwPtpCableTransWarpValue_Type()
)
hwPtpCableTransWarpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPtpCableTransWarpValue.setStatus("current")
_HwPtpNotifications_ObjectIdentity = ObjectIdentity
hwPtpNotifications = _HwPtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 6)
)
_HwPtpConformance_ObjectIdentity = ObjectIdentity
hwPtpConformance = _HwPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7)
)
_HwPtpCompliance_ObjectIdentity = ObjectIdentity
hwPtpCompliance = _HwPtpCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 1)
)
_HwPtpGroups_ObjectIdentity = ObjectIdentity
hwPtpGroups = _HwPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 2)
)

# Managed Objects groups

hwPtpGlobalObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 2, 1)
)
hwPtpGlobalObjectsGroup.setObjects(
      *(("HUAWEI-PTP-MIB", "hwPtpEnable"),
        ("HUAWEI-PTP-MIB", "hwPtpDomain"),
        ("HUAWEI-PTP-MIB", "hwPtpSlaveOnly"),
        ("HUAWEI-PTP-MIB", "hwPtpDeviceType"),
        ("HUAWEI-PTP-MIB", "hwPtpLocalClockId"),
        ("HUAWEI-PTP-MIB", "hwPtpLocalClockClass"),
        ("HUAWEI-PTP-MIB", "hwPtpLocalClockAccuracy"),
        ("HUAWEI-PTP-MIB", "hwPtpLocalClockPriority1"),
        ("HUAWEI-PTP-MIB", "hwPtpLocalClockPriority2"),
        ("HUAWEI-PTP-MIB", "hwPtpLocalClockTimeSource"),
        ("HUAWEI-PTP-MIB", "hwPtpUtc"),
        ("HUAWEI-PTP-MIB", "hwPtpCurrentUtcOffset"),
        ("HUAWEI-PTP-MIB", "hwPtpCurrentMasterClockId"),
        ("HUAWEI-PTP-MIB", "hwPtpCurrentMasterClockReceivePort"),
        ("HUAWEI-PTP-MIB", "hwPtpCurrentMasterClockStepRemoved"),
        ("HUAWEI-PTP-MIB", "hwPtpTimeSynchronizationStatus"),
        ("HUAWEI-PTP-MIB", "hwPtpTimeTraceable"),
        ("HUAWEI-PTP-MIB", "hwPtpTimeScale"),
        ("HUAWEI-PTP-MIB", "hwPtpVersion"),
        ("HUAWEI-PTP-MIB", "hwPtpLeapEmendationTime"),
        ("HUAWEI-PTP-MIB", "hwCurrentUtcOffsetValid"),
        ("HUAWEI-PTP-MIB", "hwPtpLeap59orLeap61Valid"),
        ("HUAWEI-PTP-MIB", "hwPtpFrequencyTraceable"))
)
if mibBuilder.loadTexts:
    hwPtpGlobalObjectsGroup.setStatus("current")

hwPtpPortObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 2, 2)
)
hwPtpPortObjectsGroup.setObjects(
      *(("HUAWEI-PTP-MIB", "hwPtpPortEnable"),
        ("HUAWEI-PTP-MIB", "hwPtpPortDelayMechanism"),
        ("HUAWEI-PTP-MIB", "hwPtpPortDomain"),
        ("HUAWEI-PTP-MIB", "hwPtpPortTcOcStaticClockId"),
        ("HUAWEI-PTP-MIB", "hwPtpPortAnnounceInterval"),
        ("HUAWEI-PTP-MIB", "hwPtpPortAnnounceReceipTimeout"),
        ("HUAWEI-PTP-MIB", "hwPtpPortSyncInterval"),
        ("HUAWEI-PTP-MIB", "hwPtpPortMinDelayReqInterval"),
        ("HUAWEI-PTP-MIB", "hwPtpPortMinPdelayReqInterval"),
        ("HUAWEI-PTP-MIB", "hwPtpPortAsymmetryNegativeCorrection"),
        ("HUAWEI-PTP-MIB", "hwPtpPortAsymmetryPositiveCorrection"),
        ("HUAWEI-PTP-MIB", "hwPtpPortMacEgressDestinationMac"),
        ("HUAWEI-PTP-MIB", "hwPtpPortMacEgressVlanId"),
        ("HUAWEI-PTP-MIB", "hwPtpPortMacEgressPacketPriority"),
        ("HUAWEI-PTP-MIB", "hwPtpPortUdpEgressSourceIp"),
        ("HUAWEI-PTP-MIB", "hwPtpPortUdpEgressDestinationIp"),
        ("HUAWEI-PTP-MIB", "hwPtpPortUdpEgressDestinationMac"),
        ("HUAWEI-PTP-MIB", "hwPtpPortUdpEgressDscp"),
        ("HUAWEI-PTP-MIB", "hwPtpPortUdpEgressVlanId"),
        ("HUAWEI-PTP-MIB", "hwPtpPortUdpEgressPacketPriority"),
        ("HUAWEI-PTP-MIB", "hwPtpPortAnnounceDrop"),
        ("HUAWEI-PTP-MIB", "hwPtpPortState"),
        ("HUAWEI-PTP-MIB", "hwPtpPortSourcePortClockId"),
        ("HUAWEI-PTP-MIB", "hwPtpPortRxPtpTrsprnsPktCnt"),
        ("HUAWEI-PTP-MIB", "hwPtpPortRxPtpDiscardTrsprnsPktCnt"),
        ("HUAWEI-PTP-MIB", "hwPtpPortRxPtpEndPktCnt"),
        ("HUAWEI-PTP-MIB", "hwPtpPortRxPtpDiscardEndPktCnt"),
        ("HUAWEI-PTP-MIB", "hwPtpPortRxPtpAnnouncePktCnt"),
        ("HUAWEI-PTP-MIB", "hwPtpPortRxPtpSyncPktCnt"),
        ("HUAWEI-PTP-MIB", "hwPtpPortTxPtpDiscardReqCnt"),
        ("HUAWEI-PTP-MIB", "hwPtpPortTxFifoDiscardPktCn"),
        ("HUAWEI-PTP-MIB", "hwPtpReceiveDelay"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsDirection"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsSignal"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsSwitch"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsNormalStatus"),
        ("HUAWEI-PTP-MIB", "hwPtpSendDelay"),
        ("HUAWEI-PTP-MIB", "hwPtpPortRowStatus"),
        ("HUAWEI-PTP-MIB", "hwPtpPortStaticPktReset"),
        ("HUAWEI-PTP-MIB", "hwPtpPortType"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsClockAccuracy"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsClockClass"),
        ("HUAWEI-PTP-MIB", "hwPtpPortCfgMsgFormat"),
        ("HUAWEI-PTP-MIB", "hwPtpPortCfgExtInterfaceMode"),
        ("HUAWEI-PTP-MIB", "hwPtpPortCfgLinkStatus"),
        ("HUAWEI-PTP-MIB", "hwPtpPortPortVlan"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsPriority2"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsPriority1"),
        ("HUAWEI-PTP-MIB", "hwPtpBitsTimeSource"),
        ("HUAWEI-PTP-MIB", "hwPtpPortTcOcStaticClockPortNum"),
        ("HUAWEI-PTP-MIB", "hwPtpPortSourcePortNum"))
)
if mibBuilder.loadTexts:
    hwPtpPortObjectsGroup.setStatus("current")

hwPtpManageExtInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 2, 4)
)
hwPtpManageExtInterfaceGroup.setObjects(
      *(("HUAWEI-PTP-MIB", "hwPtpExtInterfaceOperateType"),
        ("HUAWEI-PTP-MIB", "hwPtpExtInterfaceIfIndex"),
        ("HUAWEI-PTP-MIB", "hwPtpExtInterfaceDirect"),
        ("HUAWEI-PTP-MIB", "hwPtpExtInterfaceProtocoltype"),
        ("HUAWEI-PTP-MIB", "hwPtpExtInterfaceElectricLevel"))
)
if mibBuilder.loadTexts:
    hwPtpManageExtInterfaceGroup.setStatus("current")

hwPtpManageCableLengthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 2, 5)
)
hwPtpManageCableLengthGroup.setObjects(
      *(("HUAWEI-PTP-MIB", "hwPtpCableLengthIfindex"),
        ("HUAWEI-PTP-MIB", "hwPtpCableLengthTransDirect"),
        ("HUAWEI-PTP-MIB", "hwPtpCableLengthMode"),
        ("HUAWEI-PTP-MIB", "hwPtpCableLengthTransDistance"))
)
if mibBuilder.loadTexts:
    hwPtpManageCableLengthGroup.setStatus("current")

hwPtpManageCableTransGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 2, 6)
)
hwPtpManageCableTransGroup.setObjects(
      *(("HUAWEI-PTP-MIB", "hwPtpCableTransIfindex"),
        ("HUAWEI-PTP-MIB", "hwPtpCableTransWarpMode"),
        ("HUAWEI-PTP-MIB", "hwPtpCableTransWarpDirect"),
        ("HUAWEI-PTP-MIB", "hwPtpCableTransWarpValue"))
)
if mibBuilder.loadTexts:
    hwPtpManageCableTransGroup.setStatus("current")


# Notification objects

hwPtpPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 6, 1)
)
hwPtpPortStatusChange.setObjects(
    ("HUAWEI-PTP-MIB", "hwPtpPortState")
)
if mibBuilder.loadTexts:
    hwPtpPortStatusChange.setStatus(
        "current"
    )

hwPtpClockSourceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 6, 2)
)
hwPtpClockSourceChange.setObjects(
    ("HUAWEI-PTP-MIB", "hwPtpCurrentMasterClockId")
)
if mibBuilder.loadTexts:
    hwPtpClockSourceChange.setStatus(
        "current"
    )

hwPtpTimeSynchronizationStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 6, 3)
)
hwPtpTimeSynchronizationStatusChange.setObjects(
    ("HUAWEI-PTP-MIB", "hwPtpTimeSynchronizationStatus")
)
if mibBuilder.loadTexts:
    hwPtpTimeSynchronizationStatusChange.setStatus(
        "current"
    )


# Notifications groups

hwPtpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 2, 3)
)
hwPtpNotificationsGroup.setObjects(
      *(("HUAWEI-PTP-MIB", "hwPtpPortStatusChange"),
        ("HUAWEI-PTP-MIB", "hwPtpClockSourceChange"),
        ("HUAWEI-PTP-MIB", "hwPtpTimeSynchronizationStatusChange"))
)
if mibBuilder.loadTexts:
    hwPtpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwPtpComliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 187, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hwPtpComliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "VlanIdOrNone": VlanIdOrNone,
       "hwPtpMIB": hwPtpMIB,
       "hwPtpGlobalObjects": hwPtpGlobalObjects,
       "hwPtpEnable": hwPtpEnable,
       "hwPtpDomain": hwPtpDomain,
       "hwPtpDeviceType": hwPtpDeviceType,
       "hwPtpSlaveOnly": hwPtpSlaveOnly,
       "hwPtpLocalClockId": hwPtpLocalClockId,
       "hwPtpLocalClockAccuracy": hwPtpLocalClockAccuracy,
       "hwPtpLocalClockClass": hwPtpLocalClockClass,
       "hwPtpLocalClockPriority1": hwPtpLocalClockPriority1,
       "hwPtpLocalClockPriority2": hwPtpLocalClockPriority2,
       "hwPtpLocalClockTimeSource": hwPtpLocalClockTimeSource,
       "hwPtpUtc": hwPtpUtc,
       "hwPtpCurrentUtcOffset": hwPtpCurrentUtcOffset,
       "hwCurrentUtcOffsetValid": hwCurrentUtcOffsetValid,
       "hwPtpLeap59orLeap61Valid": hwPtpLeap59orLeap61Valid,
       "hwPtpLeapEmendationTime": hwPtpLeapEmendationTime,
       "hwPtpCurrentMasterClockId": hwPtpCurrentMasterClockId,
       "hwPtpCurrentMasterClockReceivePort": hwPtpCurrentMasterClockReceivePort,
       "hwPtpCurrentMasterClockStepRemoved": hwPtpCurrentMasterClockStepRemoved,
       "hwPtpVersion": hwPtpVersion,
       "hwPtpTimeScale": hwPtpTimeScale,
       "hwPtpFrequencyTraceable": hwPtpFrequencyTraceable,
       "hwPtpTimeTraceable": hwPtpTimeTraceable,
       "hwPtpTimeSynchronizationStatus": hwPtpTimeSynchronizationStatus,
       "hwPtpPortObjects": hwPtpPortObjects,
       "hwPtpPortTable": hwPtpPortTable,
       "hwPtpPortEntry": hwPtpPortEntry,
       "hwPtpPortIfIndex": hwPtpPortIfIndex,
       "hwPtpPortEnable": hwPtpPortEnable,
       "hwPtpPortDelayMechanism": hwPtpPortDelayMechanism,
       "hwPtpPortType": hwPtpPortType,
       "hwPtpPortDomain": hwPtpPortDomain,
       "hwPtpPortTcOcStaticClockId": hwPtpPortTcOcStaticClockId,
       "hwPtpPortTcOcStaticClockPortNum": hwPtpPortTcOcStaticClockPortNum,
       "hwPtpPortAnnounceInterval": hwPtpPortAnnounceInterval,
       "hwPtpPortAnnounceReceipTimeout": hwPtpPortAnnounceReceipTimeout,
       "hwPtpPortSyncInterval": hwPtpPortSyncInterval,
       "hwPtpPortMinDelayReqInterval": hwPtpPortMinDelayReqInterval,
       "hwPtpPortMinPdelayReqInterval": hwPtpPortMinPdelayReqInterval,
       "hwPtpPortAsymmetryNegativeCorrection": hwPtpPortAsymmetryNegativeCorrection,
       "hwPtpPortAsymmetryPositiveCorrection": hwPtpPortAsymmetryPositiveCorrection,
       "hwPtpPortMacEgressDestinationMac": hwPtpPortMacEgressDestinationMac,
       "hwPtpPortMacEgressVlanId": hwPtpPortMacEgressVlanId,
       "hwPtpPortMacEgressPacketPriority": hwPtpPortMacEgressPacketPriority,
       "hwPtpPortUdpEgressSourceIp": hwPtpPortUdpEgressSourceIp,
       "hwPtpPortUdpEgressDestinationIp": hwPtpPortUdpEgressDestinationIp,
       "hwPtpPortUdpEgressDestinationMac": hwPtpPortUdpEgressDestinationMac,
       "hwPtpPortUdpEgressDscp": hwPtpPortUdpEgressDscp,
       "hwPtpPortUdpEgressVlanId": hwPtpPortUdpEgressVlanId,
       "hwPtpPortUdpEgressPacketPriority": hwPtpPortUdpEgressPacketPriority,
       "hwPtpPortAnnounceDrop": hwPtpPortAnnounceDrop,
       "hwPtpPortState": hwPtpPortState,
       "hwPtpPortSourcePortClockId": hwPtpPortSourcePortClockId,
       "hwPtpPortSourcePortNum": hwPtpPortSourcePortNum,
       "hwPtpPortPortVlan": hwPtpPortPortVlan,
       "hwPtpPortCfgLinkStatus": hwPtpPortCfgLinkStatus,
       "hwPtpPortCfgExtInterfaceMode": hwPtpPortCfgExtInterfaceMode,
       "hwPtpPortCfgMsgFormat": hwPtpPortCfgMsgFormat,
       "hwPtpPortRowStatus": hwPtpPortRowStatus,
       "hwPtpPortStatisticTable": hwPtpPortStatisticTable,
       "hwPtpPortStatisticEntry": hwPtpPortStatisticEntry,
       "hwPtpPortStatisticIfIndex": hwPtpPortStatisticIfIndex,
       "hwPtpPortRxPtpTrsprnsPktCnt": hwPtpPortRxPtpTrsprnsPktCnt,
       "hwPtpPortRxPtpDiscardTrsprnsPktCnt": hwPtpPortRxPtpDiscardTrsprnsPktCnt,
       "hwPtpPortRxPtpEndPktCnt": hwPtpPortRxPtpEndPktCnt,
       "hwPtpPortRxPtpDiscardEndPktCnt": hwPtpPortRxPtpDiscardEndPktCnt,
       "hwPtpPortRxPtpAnnouncePktCnt": hwPtpPortRxPtpAnnouncePktCnt,
       "hwPtpPortRxPtpSyncPktCnt": hwPtpPortRxPtpSyncPktCnt,
       "hwPtpPortTxPtpDiscardReqCnt": hwPtpPortTxPtpDiscardReqCnt,
       "hwPtpPortTxFifoDiscardPktCn": hwPtpPortTxFifoDiscardPktCn,
       "hwPtpPortStaticPktReset": hwPtpPortStaticPktReset,
       "hwPtpBitsClockSourceTable": hwPtpBitsClockSourceTable,
       "hwPtpBitsClockSourceEntry": hwPtpBitsClockSourceEntry,
       "hwPtpBitsPortIndex": hwPtpBitsPortIndex,
       "hwPtpBitsClockAccuracy": hwPtpBitsClockAccuracy,
       "hwPtpBitsClockClass": hwPtpBitsClockClass,
       "hwPtpBitsPriority1": hwPtpBitsPriority1,
       "hwPtpBitsPriority2": hwPtpBitsPriority2,
       "hwPtpBitsTimeSource": hwPtpBitsTimeSource,
       "hwPtpBitsSignal": hwPtpBitsSignal,
       "hwPtpBitsSwitch": hwPtpBitsSwitch,
       "hwPtpBitsDirection": hwPtpBitsDirection,
       "hwPtpBitsNormalStatus": hwPtpBitsNormalStatus,
       "hwPtpReceiveDelay": hwPtpReceiveDelay,
       "hwPtpSendDelay": hwPtpSendDelay,
       "hwPtpExtInterfaceTable": hwPtpExtInterfaceTable,
       "hwPtpExtInterfaceEntry": hwPtpExtInterfaceEntry,
       "hwPtpExtInterfaceOperateIndex": hwPtpExtInterfaceOperateIndex,
       "hwPtpExtInterfaceOperateType": hwPtpExtInterfaceOperateType,
       "hwPtpExtInterfaceIfIndex": hwPtpExtInterfaceIfIndex,
       "hwPtpExtInterfaceDirect": hwPtpExtInterfaceDirect,
       "hwPtpExtInterfaceProtocoltype": hwPtpExtInterfaceProtocoltype,
       "hwPtpExtInterfaceElectricLevel": hwPtpExtInterfaceElectricLevel,
       "hwPtpCableLengthTable": hwPtpCableLengthTable,
       "hwPtpCableLengthIfindex": hwPtpCableLengthIfindex,
       "hwPtpCableLengthTransDirect": hwPtpCableLengthTransDirect,
       "hwPtpCableLengthMode": hwPtpCableLengthMode,
       "hwPtpCableLengthTransDistance": hwPtpCableLengthTransDistance,
       "hwPtpCableTransTable": hwPtpCableTransTable,
       "hwPtpCableTransIfindex": hwPtpCableTransIfindex,
       "hwPtpCableTransWarpMode": hwPtpCableTransWarpMode,
       "hwPtpCableTransWarpDirect": hwPtpCableTransWarpDirect,
       "hwPtpCableTransWarpValue": hwPtpCableTransWarpValue,
       "hwPtpNotifications": hwPtpNotifications,
       "hwPtpPortStatusChange": hwPtpPortStatusChange,
       "hwPtpClockSourceChange": hwPtpClockSourceChange,
       "hwPtpTimeSynchronizationStatusChange": hwPtpTimeSynchronizationStatusChange,
       "hwPtpConformance": hwPtpConformance,
       "hwPtpCompliance": hwPtpCompliance,
       "hwPtpComliance": hwPtpComliance,
       "hwPtpGroups": hwPtpGroups,
       "hwPtpGlobalObjectsGroup": hwPtpGlobalObjectsGroup,
       "hwPtpPortObjectsGroup": hwPtpPortObjectsGroup,
       "hwPtpNotificationsGroup": hwPtpNotificationsGroup,
       "hwPtpManageExtInterfaceGroup": hwPtpManageExtInterfaceGroup,
       "hwPtpManageCableLengthGroup": hwPtpManageCableLengthGroup,
       "hwPtpManageCableTransGroup": hwPtpManageCableTransGroup}
)
