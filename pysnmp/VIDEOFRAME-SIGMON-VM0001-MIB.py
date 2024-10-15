# SNMP MIB module (VIDEOFRAME-SIGMON-VM0001-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIDEOFRAME-SIGMON-VM0001-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:31 2024
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

(vfBoxId,) = mibBuilder.importSymbols(
    "VIDEOFRAME-GENERIC-MIB",
    "vfBoxId")

(vfMIBModules,) = mibBuilder.importSymbols(
    "VIDEOFRAME-REGISTRATIONS-MIB",
    "vfMIBModules")

(vfFrameSlotNumber,
 vfProductsVF200Reg,
 vfSigmonFrameModuleTypes) = mibBuilder.importSymbols(
    "VIDEOFRAME-SIGMON-MIB",
    "vfFrameSlotNumber",
    "vfProductsVF200Reg",
    "vfSigmonFrameModuleTypes")


# MODULE-IDENTITY

videoframeSigmonVm0001MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1, 4)
)
videoframeSigmonVm0001MIB.setRevisions(
        ("1901-08-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vm0001AnalogAudio_ObjectIdentity = ObjectIdentity
vm0001AnalogAudio = _Vm0001AnalogAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1)
)
_Vm0001Table_Object = MibTable
vm0001Table = _Vm0001Table_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vm0001Table.setStatus("current")
_Vm0001Entry_Object = MibTableRow
vm0001Entry = _Vm0001Entry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1)
)
vm0001Entry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
)
if mibBuilder.loadTexts:
    vm0001Entry.setStatus("current")


class _Vm0001SlotNumber_Type(Integer32):
    """Custom type vm0001SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0001SlotNumber_Type.__name__ = "Integer32"
_Vm0001SlotNumber_Object = MibTableColumn
vm0001SlotNumber = _Vm0001SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 1),
    _Vm0001SlotNumber_Type()
)
vm0001SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001SlotNumber.setStatus("current")


class _Vm0001Active_Type(Integer32):
    """Custom type vm0001Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Vm0001Active_Type.__name__ = "Integer32"
_Vm0001Active_Object = MibTableColumn
vm0001Active = _Vm0001Active_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 2),
    _Vm0001Active_Type()
)
vm0001Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001Active.setStatus("current")


class _Vm0001FirmwareRev_Type(DisplayString):
    """Custom type vm0001FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0001FirmwareRev_Type.__name__ = "DisplayString"
_Vm0001FirmwareRev_Object = MibTableColumn
vm0001FirmwareRev = _Vm0001FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 3),
    _Vm0001FirmwareRev_Type()
)
vm0001FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001FirmwareRev.setStatus("current")


class _Vm0001Locate_Type(Integer32):
    """Custom type vm0001Locate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("off", 2))
    )


_Vm0001Locate_Type.__name__ = "Integer32"
_Vm0001Locate_Object = MibTableColumn
vm0001Locate = _Vm0001Locate_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 4),
    _Vm0001Locate_Type()
)
vm0001Locate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001Locate.setStatus("current")
_Vm0001SignalTable_Object = MibTable
vm0001SignalTable = _Vm0001SignalTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vm0001SignalTable.setStatus("current")
_Vm0001SignalEntry_Object = MibTableRow
vm0001SignalEntry = _Vm0001SignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1)
)
vm0001SignalEntry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
    (0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"),
)
if mibBuilder.loadTexts:
    vm0001SignalEntry.setStatus("current")


class _Vm0001SignalSlotNumber_Type(Integer32):
    """Custom type vm0001SignalSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0001SignalSlotNumber_Type.__name__ = "Integer32"
_Vm0001SignalSlotNumber_Object = MibTableColumn
vm0001SignalSlotNumber = _Vm0001SignalSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 1),
    _Vm0001SignalSlotNumber_Type()
)
vm0001SignalSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001SignalSlotNumber.setStatus("current")


class _Vm0001SignalNumber_Type(Integer32):
    """Custom type vm0001SignalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Vm0001SignalNumber_Type.__name__ = "Integer32"
_Vm0001SignalNumber_Object = MibTableColumn
vm0001SignalNumber = _Vm0001SignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 2),
    _Vm0001SignalNumber_Type()
)
vm0001SignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001SignalNumber.setStatus("current")


class _Vm0001SignalName_Type(DisplayString):
    """Custom type vm0001SignalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0001SignalName_Type.__name__ = "DisplayString"
_Vm0001SignalName_Object = MibTableColumn
vm0001SignalName = _Vm0001SignalName_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 3),
    _Vm0001SignalName_Type()
)
vm0001SignalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001SignalName.setStatus("current")


class _Vm0001SignalDescription_Type(DisplayString):
    """Custom type vm0001SignalDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0001SignalDescription_Type.__name__ = "DisplayString"
_Vm0001SignalDescription_Object = MibTableColumn
vm0001SignalDescription = _Vm0001SignalDescription_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 4),
    _Vm0001SignalDescription_Type()
)
vm0001SignalDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001SignalDescription.setStatus("current")


class _Vm0001CurrentAplRaw_Type(Integer32):
    """Custom type vm0001CurrentAplRaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )


_Vm0001CurrentAplRaw_Type.__name__ = "Integer32"
_Vm0001CurrentAplRaw_Object = MibTableColumn
vm0001CurrentAplRaw = _Vm0001CurrentAplRaw_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 5),
    _Vm0001CurrentAplRaw_Type()
)
vm0001CurrentAplRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001CurrentAplRaw.setStatus("current")


class _Vm0001ZerodBCalibrationSet_Type(Integer32):
    """Custom type vm0001ZerodBCalibrationSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("go", 2),
          ("notReady", 3),
          ("ready", 1))
    )


_Vm0001ZerodBCalibrationSet_Type.__name__ = "Integer32"
_Vm0001ZerodBCalibrationSet_Object = MibTableColumn
vm0001ZerodBCalibrationSet = _Vm0001ZerodBCalibrationSet_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 6),
    _Vm0001ZerodBCalibrationSet_Type()
)
vm0001ZerodBCalibrationSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001ZerodBCalibrationSet.setStatus("current")


class _Vm0001ZerodBCalibrationValue_Type(Integer32):
    """Custom type vm0001ZerodBCalibrationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )


_Vm0001ZerodBCalibrationValue_Type.__name__ = "Integer32"
_Vm0001ZerodBCalibrationValue_Object = MibTableColumn
vm0001ZerodBCalibrationValue = _Vm0001ZerodBCalibrationValue_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 7),
    _Vm0001ZerodBCalibrationValue_Type()
)
vm0001ZerodBCalibrationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001ZerodBCalibrationValue.setStatus("current")


class _Vm0001AplHighThreshold_Type(Integer32):
    """Custom type vm0001AplHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 30),
    )


_Vm0001AplHighThreshold_Type.__name__ = "Integer32"
_Vm0001AplHighThreshold_Object = MibTableColumn
vm0001AplHighThreshold = _Vm0001AplHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 8),
    _Vm0001AplHighThreshold_Type()
)
vm0001AplHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001AplHighThreshold.setStatus("current")


class _Vm0001AplHighDuration_Type(Integer32):
    """Custom type vm0001AplHighDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0001AplHighDuration_Type.__name__ = "Integer32"
_Vm0001AplHighDuration_Object = MibTableColumn
vm0001AplHighDuration = _Vm0001AplHighDuration_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 9),
    _Vm0001AplHighDuration_Type()
)
vm0001AplHighDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001AplHighDuration.setStatus("current")


class _Vm0001AplHighAlarmState_Type(Integer32):
    """Custom type vm0001AplHighAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("triggered", 2))
    )


_Vm0001AplHighAlarmState_Type.__name__ = "Integer32"
_Vm0001AplHighAlarmState_Object = MibTableColumn
vm0001AplHighAlarmState = _Vm0001AplHighAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 10),
    _Vm0001AplHighAlarmState_Type()
)
vm0001AplHighAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001AplHighAlarmState.setStatus("current")


class _Vm0001AplHighAlarmAck_Type(Integer32):
    """Custom type vm0001AplHighAlarmAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 3),
          ("idle", 1),
          ("unacknowledged", 2))
    )


_Vm0001AplHighAlarmAck_Type.__name__ = "Integer32"
_Vm0001AplHighAlarmAck_Object = MibTableColumn
vm0001AplHighAlarmAck = _Vm0001AplHighAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 11),
    _Vm0001AplHighAlarmAck_Type()
)
vm0001AplHighAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001AplHighAlarmAck.setStatus("current")


class _Vm0001AplHighTrapEnable_Type(Integer32):
    """Custom type vm0001AplHighTrapEnable based on Integer32"""
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


_Vm0001AplHighTrapEnable_Type.__name__ = "Integer32"
_Vm0001AplHighTrapEnable_Object = MibTableColumn
vm0001AplHighTrapEnable = _Vm0001AplHighTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 12),
    _Vm0001AplHighTrapEnable_Type()
)
vm0001AplHighTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001AplHighTrapEnable.setStatus("current")


class _Vm0001AplLowThreshold_Type(Integer32):
    """Custom type vm0001AplLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 30),
    )


_Vm0001AplLowThreshold_Type.__name__ = "Integer32"
_Vm0001AplLowThreshold_Object = MibTableColumn
vm0001AplLowThreshold = _Vm0001AplLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 13),
    _Vm0001AplLowThreshold_Type()
)
vm0001AplLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001AplLowThreshold.setStatus("current")


class _Vm0001AplLowDuration_Type(Integer32):
    """Custom type vm0001AplLowDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0001AplLowDuration_Type.__name__ = "Integer32"
_Vm0001AplLowDuration_Object = MibTableColumn
vm0001AplLowDuration = _Vm0001AplLowDuration_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 14),
    _Vm0001AplLowDuration_Type()
)
vm0001AplLowDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001AplLowDuration.setStatus("current")


class _Vm0001AplLowAlarmState_Type(Integer32):
    """Custom type vm0001AplLowAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("triggered", 2))
    )


_Vm0001AplLowAlarmState_Type.__name__ = "Integer32"
_Vm0001AplLowAlarmState_Object = MibTableColumn
vm0001AplLowAlarmState = _Vm0001AplLowAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 15),
    _Vm0001AplLowAlarmState_Type()
)
vm0001AplLowAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001AplLowAlarmState.setStatus("current")


class _Vm0001AplLowAlarmAck_Type(Integer32):
    """Custom type vm0001AplLowAlarmAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 3),
          ("idle", 1),
          ("unacknowledged", 2))
    )


_Vm0001AplLowAlarmAck_Type.__name__ = "Integer32"
_Vm0001AplLowAlarmAck_Object = MibTableColumn
vm0001AplLowAlarmAck = _Vm0001AplLowAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 16),
    _Vm0001AplLowAlarmAck_Type()
)
vm0001AplLowAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001AplLowAlarmAck.setStatus("current")


class _Vm0001AplLowTrapEnable_Type(Integer32):
    """Custom type vm0001AplLowTrapEnable based on Integer32"""
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


_Vm0001AplLowTrapEnable_Type.__name__ = "Integer32"
_Vm0001AplLowTrapEnable_Object = MibTableColumn
vm0001AplLowTrapEnable = _Vm0001AplLowTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 17),
    _Vm0001AplLowTrapEnable_Type()
)
vm0001AplLowTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001AplLowTrapEnable.setStatus("current")


class _Vm0001PeakThreshold_Type(Integer32):
    """Custom type vm0001PeakThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 30),
    )


_Vm0001PeakThreshold_Type.__name__ = "Integer32"
_Vm0001PeakThreshold_Object = MibTableColumn
vm0001PeakThreshold = _Vm0001PeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 18),
    _Vm0001PeakThreshold_Type()
)
vm0001PeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001PeakThreshold.setStatus("current")


class _Vm0001PeakPeriod_Type(Integer32):
    """Custom type vm0001PeakPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0001PeakPeriod_Type.__name__ = "Integer32"
_Vm0001PeakPeriod_Object = MibTableColumn
vm0001PeakPeriod = _Vm0001PeakPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 19),
    _Vm0001PeakPeriod_Type()
)
vm0001PeakPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001PeakPeriod.setStatus("current")


class _Vm0001PeakAlarmState_Type(Integer32):
    """Custom type vm0001PeakAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("triggered", 2))
    )


_Vm0001PeakAlarmState_Type.__name__ = "Integer32"
_Vm0001PeakAlarmState_Object = MibTableColumn
vm0001PeakAlarmState = _Vm0001PeakAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 20),
    _Vm0001PeakAlarmState_Type()
)
vm0001PeakAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001PeakAlarmState.setStatus("current")


class _Vm0001PeakAlarmAck_Type(Integer32):
    """Custom type vm0001PeakAlarmAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 3),
          ("idle", 1),
          ("unacknowledged", 2))
    )


_Vm0001PeakAlarmAck_Type.__name__ = "Integer32"
_Vm0001PeakAlarmAck_Object = MibTableColumn
vm0001PeakAlarmAck = _Vm0001PeakAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 21),
    _Vm0001PeakAlarmAck_Type()
)
vm0001PeakAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001PeakAlarmAck.setStatus("current")


class _Vm0001PeakTrapEnable_Type(Integer32):
    """Custom type vm0001PeakTrapEnable based on Integer32"""
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


_Vm0001PeakTrapEnable_Type.__name__ = "Integer32"
_Vm0001PeakTrapEnable_Object = MibTableColumn
vm0001PeakTrapEnable = _Vm0001PeakTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 22),
    _Vm0001PeakTrapEnable_Type()
)
vm0001PeakTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001PeakTrapEnable.setStatus("current")
_Vm0001StereoPairTable_Object = MibTable
vm0001StereoPairTable = _Vm0001StereoPairTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vm0001StereoPairTable.setStatus("current")
_Vm0001StereoPairEntry_Object = MibTableRow
vm0001StereoPairEntry = _Vm0001StereoPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1)
)
vm0001StereoPairEntry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"),
    (0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"),
)
if mibBuilder.loadTexts:
    vm0001StereoPairEntry.setStatus("current")


class _Vm0001StereoPairSlotNumber_Type(Integer32):
    """Custom type vm0001StereoPairSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0001StereoPairSlotNumber_Type.__name__ = "Integer32"
_Vm0001StereoPairSlotNumber_Object = MibTableColumn
vm0001StereoPairSlotNumber = _Vm0001StereoPairSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 1),
    _Vm0001StereoPairSlotNumber_Type()
)
vm0001StereoPairSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001StereoPairSlotNumber.setStatus("current")


class _Vm0001StereoPairNumber_Type(DisplayString):
    """Custom type vm0001StereoPairNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0001StereoPairNumber_Type.__name__ = "DisplayString"
_Vm0001StereoPairNumber_Object = MibTableColumn
vm0001StereoPairNumber = _Vm0001StereoPairNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 2),
    _Vm0001StereoPairNumber_Type()
)
vm0001StereoPairNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001StereoPairNumber.setStatus("current")


class _Vm0001StereoPairName_Type(DisplayString):
    """Custom type vm0001StereoPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0001StereoPairName_Type.__name__ = "DisplayString"
_Vm0001StereoPairName_Object = MibTableColumn
vm0001StereoPairName = _Vm0001StereoPairName_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 3),
    _Vm0001StereoPairName_Type()
)
vm0001StereoPairName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001StereoPairName.setStatus("current")


class _Vm0001StereoPairDescription_Type(DisplayString):
    """Custom type vm0001StereoPairDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0001StereoPairDescription_Type.__name__ = "DisplayString"
_Vm0001StereoPairDescription_Object = MibTableColumn
vm0001StereoPairDescription = _Vm0001StereoPairDescription_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 4),
    _Vm0001StereoPairDescription_Type()
)
vm0001StereoPairDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001StereoPairDescription.setStatus("current")


class _Vm0001MonoFilter_Type(Integer32):
    """Custom type vm0001MonoFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Vm0001MonoFilter_Type.__name__ = "Integer32"
_Vm0001MonoFilter_Object = MibTableColumn
vm0001MonoFilter = _Vm0001MonoFilter_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 5),
    _Vm0001MonoFilter_Type()
)
vm0001MonoFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001MonoFilter.setStatus("current")
_Vm0001MonoDuration_Type = Integer32
_Vm0001MonoDuration_Object = MibTableColumn
vm0001MonoDuration = _Vm0001MonoDuration_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 6),
    _Vm0001MonoDuration_Type()
)
vm0001MonoDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001MonoDuration.setStatus("current")


class _Vm0001MonoAlarmState_Type(Integer32):
    """Custom type vm0001MonoAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("triggered", 2))
    )


_Vm0001MonoAlarmState_Type.__name__ = "Integer32"
_Vm0001MonoAlarmState_Object = MibTableColumn
vm0001MonoAlarmState = _Vm0001MonoAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 7),
    _Vm0001MonoAlarmState_Type()
)
vm0001MonoAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001MonoAlarmState.setStatus("current")


class _Vm0001MonoAlarmAck_Type(Integer32):
    """Custom type vm0001MonoAlarmAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 3),
          ("idle", 1),
          ("unacknowledged", 2))
    )


_Vm0001MonoAlarmAck_Type.__name__ = "Integer32"
_Vm0001MonoAlarmAck_Object = MibTableColumn
vm0001MonoAlarmAck = _Vm0001MonoAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 8),
    _Vm0001MonoAlarmAck_Type()
)
vm0001MonoAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001MonoAlarmAck.setStatus("current")


class _Vm0001MonoTrapEnable_Type(Integer32):
    """Custom type vm0001MonoTrapEnable based on Integer32"""
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


_Vm0001MonoTrapEnable_Type.__name__ = "Integer32"
_Vm0001MonoTrapEnable_Object = MibTableColumn
vm0001MonoTrapEnable = _Vm0001MonoTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 9),
    _Vm0001MonoTrapEnable_Type()
)
vm0001MonoTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001MonoTrapEnable.setStatus("current")


class _Vm0001StereoOutOfPhaseFilter_Type(Integer32):
    """Custom type vm0001StereoOutOfPhaseFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Vm0001StereoOutOfPhaseFilter_Type.__name__ = "Integer32"
_Vm0001StereoOutOfPhaseFilter_Object = MibTableColumn
vm0001StereoOutOfPhaseFilter = _Vm0001StereoOutOfPhaseFilter_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 10),
    _Vm0001StereoOutOfPhaseFilter_Type()
)
vm0001StereoOutOfPhaseFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001StereoOutOfPhaseFilter.setStatus("current")
_Vm0001StereoOutOfPhaseDuration_Type = Integer32
_Vm0001StereoOutOfPhaseDuration_Object = MibTableColumn
vm0001StereoOutOfPhaseDuration = _Vm0001StereoOutOfPhaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 11),
    _Vm0001StereoOutOfPhaseDuration_Type()
)
vm0001StereoOutOfPhaseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001StereoOutOfPhaseDuration.setStatus("current")


class _Vm0001StereoOutOfPhaseAlarmState_Type(Integer32):
    """Custom type vm0001StereoOutOfPhaseAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("triggered", 2))
    )


_Vm0001StereoOutOfPhaseAlarmState_Type.__name__ = "Integer32"
_Vm0001StereoOutOfPhaseAlarmState_Object = MibTableColumn
vm0001StereoOutOfPhaseAlarmState = _Vm0001StereoOutOfPhaseAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 12),
    _Vm0001StereoOutOfPhaseAlarmState_Type()
)
vm0001StereoOutOfPhaseAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0001StereoOutOfPhaseAlarmState.setStatus("current")


class _Vm0001StereoOutOfPhaseAlarmAck_Type(Integer32):
    """Custom type vm0001StereoOutOfPhaseAlarmAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 3),
          ("idle", 1),
          ("unacknowledged", 2))
    )


_Vm0001StereoOutOfPhaseAlarmAck_Type.__name__ = "Integer32"
_Vm0001StereoOutOfPhaseAlarmAck_Object = MibTableColumn
vm0001StereoOutOfPhaseAlarmAck = _Vm0001StereoOutOfPhaseAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 13),
    _Vm0001StereoOutOfPhaseAlarmAck_Type()
)
vm0001StereoOutOfPhaseAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0001StereoOutOfPhaseAlarmAck.setStatus("current")
_Vm0001AnalogAudioEvents_ObjectIdentity = ObjectIdentity
vm0001AnalogAudioEvents = _Vm0001AnalogAudioEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4)
)
_Vm0001AnalogAudioEventsV2_ObjectIdentity = ObjectIdentity
vm0001AnalogAudioEventsV2 = _Vm0001AnalogAudioEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0)
)
_VfProductsVM0001Reg_ObjectIdentity = ObjectIdentity
vfProductsVM0001Reg = _VfProductsVM0001Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vfProductsVM0001Reg.setStatus("current")

# Managed Objects groups


# Notification objects

analogAudioAPLHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 1)
)
analogAudioAPLHighAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
)
if mibBuilder.loadTexts:
    analogAudioAPLHighAlarm.setStatus(
        "current"
    )

analogAudioAPLLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 2)
)
analogAudioAPLLowAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
)
if mibBuilder.loadTexts:
    analogAudioAPLLowAlarm.setStatus(
        "current"
    )

analogAudioPeakAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 3)
)
analogAudioPeakAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
)
if mibBuilder.loadTexts:
    analogAudioPeakAlarm.setStatus(
        "current"
    )

analogAudioMonoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 4)
)
analogAudioMonoAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairName"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairDescription"))
)
if mibBuilder.loadTexts:
    analogAudioMonoAlarm.setStatus(
        "current"
    )

analogAudioStereoOutOfPhaseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 5)
)
analogAudioStereoOutOfPhaseAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairName"),
        ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairDescription"))
)
if mibBuilder.loadTexts:
    analogAudioStereoOutOfPhaseAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEOFRAME-SIGMON-VM0001-MIB",
    **{"vm0001AnalogAudio": vm0001AnalogAudio,
       "vm0001Table": vm0001Table,
       "vm0001Entry": vm0001Entry,
       "vm0001SlotNumber": vm0001SlotNumber,
       "vm0001Active": vm0001Active,
       "vm0001FirmwareRev": vm0001FirmwareRev,
       "vm0001Locate": vm0001Locate,
       "vm0001SignalTable": vm0001SignalTable,
       "vm0001SignalEntry": vm0001SignalEntry,
       "vm0001SignalSlotNumber": vm0001SignalSlotNumber,
       "vm0001SignalNumber": vm0001SignalNumber,
       "vm0001SignalName": vm0001SignalName,
       "vm0001SignalDescription": vm0001SignalDescription,
       "vm0001CurrentAplRaw": vm0001CurrentAplRaw,
       "vm0001ZerodBCalibrationSet": vm0001ZerodBCalibrationSet,
       "vm0001ZerodBCalibrationValue": vm0001ZerodBCalibrationValue,
       "vm0001AplHighThreshold": vm0001AplHighThreshold,
       "vm0001AplHighDuration": vm0001AplHighDuration,
       "vm0001AplHighAlarmState": vm0001AplHighAlarmState,
       "vm0001AplHighAlarmAck": vm0001AplHighAlarmAck,
       "vm0001AplHighTrapEnable": vm0001AplHighTrapEnable,
       "vm0001AplLowThreshold": vm0001AplLowThreshold,
       "vm0001AplLowDuration": vm0001AplLowDuration,
       "vm0001AplLowAlarmState": vm0001AplLowAlarmState,
       "vm0001AplLowAlarmAck": vm0001AplLowAlarmAck,
       "vm0001AplLowTrapEnable": vm0001AplLowTrapEnable,
       "vm0001PeakThreshold": vm0001PeakThreshold,
       "vm0001PeakPeriod": vm0001PeakPeriod,
       "vm0001PeakAlarmState": vm0001PeakAlarmState,
       "vm0001PeakAlarmAck": vm0001PeakAlarmAck,
       "vm0001PeakTrapEnable": vm0001PeakTrapEnable,
       "vm0001StereoPairTable": vm0001StereoPairTable,
       "vm0001StereoPairEntry": vm0001StereoPairEntry,
       "vm0001StereoPairSlotNumber": vm0001StereoPairSlotNumber,
       "vm0001StereoPairNumber": vm0001StereoPairNumber,
       "vm0001StereoPairName": vm0001StereoPairName,
       "vm0001StereoPairDescription": vm0001StereoPairDescription,
       "vm0001MonoFilter": vm0001MonoFilter,
       "vm0001MonoDuration": vm0001MonoDuration,
       "vm0001MonoAlarmState": vm0001MonoAlarmState,
       "vm0001MonoAlarmAck": vm0001MonoAlarmAck,
       "vm0001MonoTrapEnable": vm0001MonoTrapEnable,
       "vm0001StereoOutOfPhaseFilter": vm0001StereoOutOfPhaseFilter,
       "vm0001StereoOutOfPhaseDuration": vm0001StereoOutOfPhaseDuration,
       "vm0001StereoOutOfPhaseAlarmState": vm0001StereoOutOfPhaseAlarmState,
       "vm0001StereoOutOfPhaseAlarmAck": vm0001StereoOutOfPhaseAlarmAck,
       "vm0001AnalogAudioEvents": vm0001AnalogAudioEvents,
       "vm0001AnalogAudioEventsV2": vm0001AnalogAudioEventsV2,
       "analogAudioAPLHighAlarm": analogAudioAPLHighAlarm,
       "analogAudioAPLLowAlarm": analogAudioAPLLowAlarm,
       "analogAudioPeakAlarm": analogAudioPeakAlarm,
       "analogAudioMonoAlarm": analogAudioMonoAlarm,
       "analogAudioStereoOutOfPhaseAlarm": analogAudioStereoOutOfPhaseAlarm,
       "videoframeSigmonVm0001MIB": videoframeSigmonVm0001MIB,
       "vfProductsVM0001Reg": vfProductsVM0001Reg}
)
