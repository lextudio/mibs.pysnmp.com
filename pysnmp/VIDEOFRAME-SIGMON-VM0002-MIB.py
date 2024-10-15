# SNMP MIB module (VIDEOFRAME-SIGMON-VM0002-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIDEOFRAME-SIGMON-VM0002-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:32 2024
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

videoframeSigmonVm0002MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1, 5)
)
videoframeSigmonVm0002MIB.setRevisions(
        ("1901-08-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vm0002AnalogVideo_ObjectIdentity = ObjectIdentity
vm0002AnalogVideo = _Vm0002AnalogVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2)
)
_Vm0002Table_Object = MibTable
vm0002Table = _Vm0002Table_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vm0002Table.setStatus("current")
_Vm0002Entry_Object = MibTableRow
vm0002Entry = _Vm0002Entry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 1, 1)
)
vm0002Entry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
)
if mibBuilder.loadTexts:
    vm0002Entry.setStatus("current")


class _Vm0002SlotNumber_Type(Integer32):
    """Custom type vm0002SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0002SlotNumber_Type.__name__ = "Integer32"
_Vm0002SlotNumber_Object = MibTableColumn
vm0002SlotNumber = _Vm0002SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 1, 1, 1),
    _Vm0002SlotNumber_Type()
)
vm0002SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002SlotNumber.setStatus("current")


class _Vm0002Active_Type(Integer32):
    """Custom type vm0002Active based on Integer32"""
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


_Vm0002Active_Type.__name__ = "Integer32"
_Vm0002Active_Object = MibTableColumn
vm0002Active = _Vm0002Active_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 1, 1, 2),
    _Vm0002Active_Type()
)
vm0002Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002Active.setStatus("current")


class _Vm0002FirmwareRev_Type(DisplayString):
    """Custom type vm0002FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0002FirmwareRev_Type.__name__ = "DisplayString"
_Vm0002FirmwareRev_Object = MibTableColumn
vm0002FirmwareRev = _Vm0002FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 1, 1, 3),
    _Vm0002FirmwareRev_Type()
)
vm0002FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002FirmwareRev.setStatus("current")


class _Vm0002Locate_Type(Integer32):
    """Custom type vm0002Locate based on Integer32"""
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


_Vm0002Locate_Type.__name__ = "Integer32"
_Vm0002Locate_Object = MibTableColumn
vm0002Locate = _Vm0002Locate_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 1, 1, 4),
    _Vm0002Locate_Type()
)
vm0002Locate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002Locate.setStatus("current")
_Vm0002SignalTable_Object = MibTable
vm0002SignalTable = _Vm0002SignalTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vm0002SignalTable.setStatus("current")
_Vm0002SignalEntry_Object = MibTableRow
vm0002SignalEntry = _Vm0002SignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1)
)
vm0002SignalEntry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
    (0, "VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalNumber"),
)
if mibBuilder.loadTexts:
    vm0002SignalEntry.setStatus("current")


class _Vm0002SignalSlotNumber_Type(Integer32):
    """Custom type vm0002SignalSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0002SignalSlotNumber_Type.__name__ = "Integer32"
_Vm0002SignalSlotNumber_Object = MibTableColumn
vm0002SignalSlotNumber = _Vm0002SignalSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 1),
    _Vm0002SignalSlotNumber_Type()
)
vm0002SignalSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002SignalSlotNumber.setStatus("current")


class _Vm0002SignalNumber_Type(Integer32):
    """Custom type vm0002SignalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Vm0002SignalNumber_Type.__name__ = "Integer32"
_Vm0002SignalNumber_Object = MibTableColumn
vm0002SignalNumber = _Vm0002SignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 2),
    _Vm0002SignalNumber_Type()
)
vm0002SignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002SignalNumber.setStatus("current")


class _Vm0002SignalName_Type(DisplayString):
    """Custom type vm0002SignalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0002SignalName_Type.__name__ = "DisplayString"
_Vm0002SignalName_Object = MibTableColumn
vm0002SignalName = _Vm0002SignalName_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 3),
    _Vm0002SignalName_Type()
)
vm0002SignalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002SignalName.setStatus("current")


class _Vm0002SignalDescription_Type(DisplayString):
    """Custom type vm0002SignalDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0002SignalDescription_Type.__name__ = "DisplayString"
_Vm0002SignalDescription_Object = MibTableColumn
vm0002SignalDescription = _Vm0002SignalDescription_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 4),
    _Vm0002SignalDescription_Type()
)
vm0002SignalDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002SignalDescription.setStatus("current")


class _Vm0002VSyncLossThreshold_Type(Integer32):
    """Custom type vm0002VSyncLossThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65075262),
    )


_Vm0002VSyncLossThreshold_Type.__name__ = "Integer32"
_Vm0002VSyncLossThreshold_Object = MibTableColumn
vm0002VSyncLossThreshold = _Vm0002VSyncLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 5),
    _Vm0002VSyncLossThreshold_Type()
)
vm0002VSyncLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002VSyncLossThreshold.setStatus("current")


class _Vm0002VSyncLossPeriod_Type(Integer32):
    """Custom type vm0002VSyncLossPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0002VSyncLossPeriod_Type.__name__ = "Integer32"
_Vm0002VSyncLossPeriod_Object = MibTableColumn
vm0002VSyncLossPeriod = _Vm0002VSyncLossPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 6),
    _Vm0002VSyncLossPeriod_Type()
)
vm0002VSyncLossPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002VSyncLossPeriod.setStatus("current")


class _Vm0002VSyncLossAlarmState_Type(Integer32):
    """Custom type vm0002VSyncLossAlarmState based on Integer32"""
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


_Vm0002VSyncLossAlarmState_Type.__name__ = "Integer32"
_Vm0002VSyncLossAlarmState_Object = MibTableColumn
vm0002VSyncLossAlarmState = _Vm0002VSyncLossAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 7),
    _Vm0002VSyncLossAlarmState_Type()
)
vm0002VSyncLossAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002VSyncLossAlarmState.setStatus("current")


class _Vm0002VSyncLossAlarmAck_Type(Integer32):
    """Custom type vm0002VSyncLossAlarmAck based on Integer32"""
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


_Vm0002VSyncLossAlarmAck_Type.__name__ = "Integer32"
_Vm0002VSyncLossAlarmAck_Object = MibTableColumn
vm0002VSyncLossAlarmAck = _Vm0002VSyncLossAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 8),
    _Vm0002VSyncLossAlarmAck_Type()
)
vm0002VSyncLossAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002VSyncLossAlarmAck.setStatus("current")


class _Vm0002VSyncLossTrapEnable_Type(Integer32):
    """Custom type vm0002VSyncLossTrapEnable based on Integer32"""
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


_Vm0002VSyncLossTrapEnable_Type.__name__ = "Integer32"
_Vm0002VSyncLossTrapEnable_Object = MibTableColumn
vm0002VSyncLossTrapEnable = _Vm0002VSyncLossTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 9),
    _Vm0002VSyncLossTrapEnable_Type()
)
vm0002VSyncLossTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002VSyncLossTrapEnable.setStatus("current")


class _Vm0002HSyncLossThreshold_Type(Integer32):
    """Custom type vm0002HSyncLossThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65075262),
    )


_Vm0002HSyncLossThreshold_Type.__name__ = "Integer32"
_Vm0002HSyncLossThreshold_Object = MibTableColumn
vm0002HSyncLossThreshold = _Vm0002HSyncLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 10),
    _Vm0002HSyncLossThreshold_Type()
)
vm0002HSyncLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002HSyncLossThreshold.setStatus("current")


class _Vm0002HSyncLossPeriod_Type(Integer32):
    """Custom type vm0002HSyncLossPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0002HSyncLossPeriod_Type.__name__ = "Integer32"
_Vm0002HSyncLossPeriod_Object = MibTableColumn
vm0002HSyncLossPeriod = _Vm0002HSyncLossPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 11),
    _Vm0002HSyncLossPeriod_Type()
)
vm0002HSyncLossPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002HSyncLossPeriod.setStatus("current")


class _Vm0002HSyncLossAlarmState_Type(Integer32):
    """Custom type vm0002HSyncLossAlarmState based on Integer32"""
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


_Vm0002HSyncLossAlarmState_Type.__name__ = "Integer32"
_Vm0002HSyncLossAlarmState_Object = MibTableColumn
vm0002HSyncLossAlarmState = _Vm0002HSyncLossAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 12),
    _Vm0002HSyncLossAlarmState_Type()
)
vm0002HSyncLossAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002HSyncLossAlarmState.setStatus("current")


class _Vm0002HSyncLossAlarmAck_Type(Integer32):
    """Custom type vm0002HSyncLossAlarmAck based on Integer32"""
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


_Vm0002HSyncLossAlarmAck_Type.__name__ = "Integer32"
_Vm0002HSyncLossAlarmAck_Object = MibTableColumn
vm0002HSyncLossAlarmAck = _Vm0002HSyncLossAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 13),
    _Vm0002HSyncLossAlarmAck_Type()
)
vm0002HSyncLossAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002HSyncLossAlarmAck.setStatus("current")


class _Vm0002HSyncLossTrapEnable_Type(Integer32):
    """Custom type vm0002HSyncLossTrapEnable based on Integer32"""
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


_Vm0002HSyncLossTrapEnable_Type.__name__ = "Integer32"
_Vm0002HSyncLossTrapEnable_Object = MibTableColumn
vm0002HSyncLossTrapEnable = _Vm0002HSyncLossTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 14),
    _Vm0002HSyncLossTrapEnable_Type()
)
vm0002HSyncLossTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002HSyncLossTrapEnable.setStatus("current")


class _Vm0002PedestalHighThreshold_Type(Integer32):
    """Custom type vm0002PedestalHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Vm0002PedestalHighThreshold_Type.__name__ = "Integer32"
_Vm0002PedestalHighThreshold_Object = MibTableColumn
vm0002PedestalHighThreshold = _Vm0002PedestalHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 15),
    _Vm0002PedestalHighThreshold_Type()
)
vm0002PedestalHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002PedestalHighThreshold.setStatus("current")


class _Vm0002PedestalHighPeriod_Type(Integer32):
    """Custom type vm0002PedestalHighPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0002PedestalHighPeriod_Type.__name__ = "Integer32"
_Vm0002PedestalHighPeriod_Object = MibTableColumn
vm0002PedestalHighPeriod = _Vm0002PedestalHighPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 16),
    _Vm0002PedestalHighPeriod_Type()
)
vm0002PedestalHighPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002PedestalHighPeriod.setStatus("current")


class _Vm0002MeasuredPedestal_Type(Integer32):
    """Custom type vm0002MeasuredPedestal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Vm0002MeasuredPedestal_Type.__name__ = "Integer32"
_Vm0002MeasuredPedestal_Object = MibTableColumn
vm0002MeasuredPedestal = _Vm0002MeasuredPedestal_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 17),
    _Vm0002MeasuredPedestal_Type()
)
vm0002MeasuredPedestal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002MeasuredPedestal.setStatus("current")


class _Vm0002PedestalHighAlarmState_Type(Integer32):
    """Custom type vm0002PedestalHighAlarmState based on Integer32"""
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


_Vm0002PedestalHighAlarmState_Type.__name__ = "Integer32"
_Vm0002PedestalHighAlarmState_Object = MibTableColumn
vm0002PedestalHighAlarmState = _Vm0002PedestalHighAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 18),
    _Vm0002PedestalHighAlarmState_Type()
)
vm0002PedestalHighAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002PedestalHighAlarmState.setStatus("current")


class _Vm0002PedestalHighAlarmAck_Type(Integer32):
    """Custom type vm0002PedestalHighAlarmAck based on Integer32"""
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


_Vm0002PedestalHighAlarmAck_Type.__name__ = "Integer32"
_Vm0002PedestalHighAlarmAck_Object = MibTableColumn
vm0002PedestalHighAlarmAck = _Vm0002PedestalHighAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 19),
    _Vm0002PedestalHighAlarmAck_Type()
)
vm0002PedestalHighAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002PedestalHighAlarmAck.setStatus("current")


class _Vm0002PedestalHighTrapEnable_Type(Integer32):
    """Custom type vm0002PedestalHighTrapEnable based on Integer32"""
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


_Vm0002PedestalHighTrapEnable_Type.__name__ = "Integer32"
_Vm0002PedestalHighTrapEnable_Object = MibTableColumn
vm0002PedestalHighTrapEnable = _Vm0002PedestalHighTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 20),
    _Vm0002PedestalHighTrapEnable_Type()
)
vm0002PedestalHighTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002PedestalHighTrapEnable.setStatus("current")


class _Vm0002CurrentAplRaw_Type(Integer32):
    """Custom type vm0002CurrentAplRaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_Vm0002CurrentAplRaw_Type.__name__ = "Integer32"
_Vm0002CurrentAplRaw_Object = MibTableColumn
vm0002CurrentAplRaw = _Vm0002CurrentAplRaw_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 21),
    _Vm0002CurrentAplRaw_Type()
)
vm0002CurrentAplRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002CurrentAplRaw.setStatus("current")


class _Vm0002n100IRECalibrationSet_Type(Integer32):
    """Custom type vm0002n100IRECalibrationSet based on Integer32"""
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


_Vm0002n100IRECalibrationSet_Type.__name__ = "Integer32"
_Vm0002n100IRECalibrationSet_Object = MibTableColumn
vm0002n100IRECalibrationSet = _Vm0002n100IRECalibrationSet_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 22),
    _Vm0002n100IRECalibrationSet_Type()
)
vm0002n100IRECalibrationSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002n100IRECalibrationSet.setStatus("current")


class _Vm0002n100IRECalibrationValue_Type(Integer32):
    """Custom type vm0002n100IRECalibrationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_Vm0002n100IRECalibrationValue_Type.__name__ = "Integer32"
_Vm0002n100IRECalibrationValue_Object = MibTableColumn
vm0002n100IRECalibrationValue = _Vm0002n100IRECalibrationValue_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 23),
    _Vm0002n100IRECalibrationValue_Type()
)
vm0002n100IRECalibrationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002n100IRECalibrationValue.setStatus("current")


class _Vm0002AplHighThreshold_Type(Integer32):
    """Custom type vm0002AplHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Vm0002AplHighThreshold_Type.__name__ = "Integer32"
_Vm0002AplHighThreshold_Object = MibTableColumn
vm0002AplHighThreshold = _Vm0002AplHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 24),
    _Vm0002AplHighThreshold_Type()
)
vm0002AplHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002AplHighThreshold.setStatus("current")


class _Vm0002AplHighDuration_Type(Integer32):
    """Custom type vm0002AplHighDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0002AplHighDuration_Type.__name__ = "Integer32"
_Vm0002AplHighDuration_Object = MibTableColumn
vm0002AplHighDuration = _Vm0002AplHighDuration_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 25),
    _Vm0002AplHighDuration_Type()
)
vm0002AplHighDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002AplHighDuration.setStatus("current")


class _Vm0002AplHighAlarmState_Type(Integer32):
    """Custom type vm0002AplHighAlarmState based on Integer32"""
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


_Vm0002AplHighAlarmState_Type.__name__ = "Integer32"
_Vm0002AplHighAlarmState_Object = MibTableColumn
vm0002AplHighAlarmState = _Vm0002AplHighAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 26),
    _Vm0002AplHighAlarmState_Type()
)
vm0002AplHighAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002AplHighAlarmState.setStatus("current")


class _Vm0002AplHighAlarmAck_Type(Integer32):
    """Custom type vm0002AplHighAlarmAck based on Integer32"""
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


_Vm0002AplHighAlarmAck_Type.__name__ = "Integer32"
_Vm0002AplHighAlarmAck_Object = MibTableColumn
vm0002AplHighAlarmAck = _Vm0002AplHighAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 27),
    _Vm0002AplHighAlarmAck_Type()
)
vm0002AplHighAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002AplHighAlarmAck.setStatus("current")


class _Vm0002AplHighTrapEnable_Type(Integer32):
    """Custom type vm0002AplHighTrapEnable based on Integer32"""
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


_Vm0002AplHighTrapEnable_Type.__name__ = "Integer32"
_Vm0002AplHighTrapEnable_Object = MibTableColumn
vm0002AplHighTrapEnable = _Vm0002AplHighTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 28),
    _Vm0002AplHighTrapEnable_Type()
)
vm0002AplHighTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002AplHighTrapEnable.setStatus("current")


class _Vm0002AplLowThreshold_Type(Integer32):
    """Custom type vm0002AplLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Vm0002AplLowThreshold_Type.__name__ = "Integer32"
_Vm0002AplLowThreshold_Object = MibTableColumn
vm0002AplLowThreshold = _Vm0002AplLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 29),
    _Vm0002AplLowThreshold_Type()
)
vm0002AplLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002AplLowThreshold.setStatus("current")


class _Vm0002AplLowDuration_Type(Integer32):
    """Custom type vm0002AplLowDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0002AplLowDuration_Type.__name__ = "Integer32"
_Vm0002AplLowDuration_Object = MibTableColumn
vm0002AplLowDuration = _Vm0002AplLowDuration_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 30),
    _Vm0002AplLowDuration_Type()
)
vm0002AplLowDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002AplLowDuration.setStatus("current")


class _Vm0002AplLowAlarmState_Type(Integer32):
    """Custom type vm0002AplLowAlarmState based on Integer32"""
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


_Vm0002AplLowAlarmState_Type.__name__ = "Integer32"
_Vm0002AplLowAlarmState_Object = MibTableColumn
vm0002AplLowAlarmState = _Vm0002AplLowAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 31),
    _Vm0002AplLowAlarmState_Type()
)
vm0002AplLowAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002AplLowAlarmState.setStatus("current")


class _Vm0002AplLowAlarmAck_Type(Integer32):
    """Custom type vm0002AplLowAlarmAck based on Integer32"""
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


_Vm0002AplLowAlarmAck_Type.__name__ = "Integer32"
_Vm0002AplLowAlarmAck_Object = MibTableColumn
vm0002AplLowAlarmAck = _Vm0002AplLowAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 32),
    _Vm0002AplLowAlarmAck_Type()
)
vm0002AplLowAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002AplLowAlarmAck.setStatus("current")


class _Vm0002AplLowTrapEnable_Type(Integer32):
    """Custom type vm0002AplLowTrapEnable based on Integer32"""
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


_Vm0002AplLowTrapEnable_Type.__name__ = "Integer32"
_Vm0002AplLowTrapEnable_Object = MibTableColumn
vm0002AplLowTrapEnable = _Vm0002AplLowTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 33),
    _Vm0002AplLowTrapEnable_Type()
)
vm0002AplLowTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002AplLowTrapEnable.setStatus("current")


class _Vm0002FrozenImageFilter_Type(Integer32):
    """Custom type vm0002FrozenImageFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Vm0002FrozenImageFilter_Type.__name__ = "Integer32"
_Vm0002FrozenImageFilter_Object = MibTableColumn
vm0002FrozenImageFilter = _Vm0002FrozenImageFilter_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 34),
    _Vm0002FrozenImageFilter_Type()
)
vm0002FrozenImageFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002FrozenImageFilter.setStatus("current")


class _Vm0002MaxFrozenDuration_Type(Integer32):
    """Custom type vm0002MaxFrozenDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vm0002MaxFrozenDuration_Type.__name__ = "Integer32"
_Vm0002MaxFrozenDuration_Object = MibTableColumn
vm0002MaxFrozenDuration = _Vm0002MaxFrozenDuration_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 35),
    _Vm0002MaxFrozenDuration_Type()
)
vm0002MaxFrozenDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002MaxFrozenDuration.setStatus("current")


class _Vm0002FrozenAlarmState_Type(Integer32):
    """Custom type vm0002FrozenAlarmState based on Integer32"""
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


_Vm0002FrozenAlarmState_Type.__name__ = "Integer32"
_Vm0002FrozenAlarmState_Object = MibTableColumn
vm0002FrozenAlarmState = _Vm0002FrozenAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 36),
    _Vm0002FrozenAlarmState_Type()
)
vm0002FrozenAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0002FrozenAlarmState.setStatus("current")


class _Vm0002FrozenAlarmAck_Type(Integer32):
    """Custom type vm0002FrozenAlarmAck based on Integer32"""
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


_Vm0002FrozenAlarmAck_Type.__name__ = "Integer32"
_Vm0002FrozenAlarmAck_Object = MibTableColumn
vm0002FrozenAlarmAck = _Vm0002FrozenAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 37),
    _Vm0002FrozenAlarmAck_Type()
)
vm0002FrozenAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002FrozenAlarmAck.setStatus("current")


class _Vm0002FrozenTrapEnable_Type(Integer32):
    """Custom type vm0002FrozenTrapEnable based on Integer32"""
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


_Vm0002FrozenTrapEnable_Type.__name__ = "Integer32"
_Vm0002FrozenTrapEnable_Object = MibTableColumn
vm0002FrozenTrapEnable = _Vm0002FrozenTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 38),
    _Vm0002FrozenTrapEnable_Type()
)
vm0002FrozenTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002FrozenTrapEnable.setStatus("current")


class _Vm0002BurstPresent_Type(Integer32):
    """Custom type vm0002BurstPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_Vm0002BurstPresent_Type.__name__ = "Integer32"
_Vm0002BurstPresent_Object = MibTableColumn
vm0002BurstPresent = _Vm0002BurstPresent_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 2, 1, 39),
    _Vm0002BurstPresent_Type()
)
vm0002BurstPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0002BurstPresent.setStatus("current")
_Vm0002AnalogVideoEvents_ObjectIdentity = ObjectIdentity
vm0002AnalogVideoEvents = _Vm0002AnalogVideoEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 3)
)
_Vm0002AnalogVideoEventsV2_ObjectIdentity = ObjectIdentity
vm0002AnalogVideoEventsV2 = _Vm0002AnalogVideoEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 3, 0)
)
_VfProductsVM0002Reg_ObjectIdentity = ObjectIdentity
vfProductsVM0002Reg = _VfProductsVM0002Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 5, 2)
)
if mibBuilder.loadTexts:
    vfProductsVM0002Reg.setStatus("current")

# Managed Objects groups


# Notification objects

analogVideoVSyncLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 3, 0, 1)
)
analogVideoVSyncLossAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalName"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalDescription"))
)
if mibBuilder.loadTexts:
    analogVideoVSyncLossAlarm.setStatus(
        "current"
    )

analogVideoHSyncLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 3, 0, 2)
)
analogVideoHSyncLossAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalName"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalDescription"))
)
if mibBuilder.loadTexts:
    analogVideoHSyncLossAlarm.setStatus(
        "current"
    )

analogVideoPedestalHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 3, 0, 3)
)
analogVideoPedestalHighAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalName"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalDescription"))
)
if mibBuilder.loadTexts:
    analogVideoPedestalHighAlarm.setStatus(
        "current"
    )

analogVideoAPLHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 3, 0, 4)
)
analogVideoAPLHighAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalName"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalDescription"))
)
if mibBuilder.loadTexts:
    analogVideoAPLHighAlarm.setStatus(
        "current"
    )

analogVideoAPLLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 3, 0, 5)
)
analogVideoAPLLowAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalName"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalDescription"))
)
if mibBuilder.loadTexts:
    analogVideoAPLLowAlarm.setStatus(
        "current"
    )

analogVideoFrozenImageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 2, 3, 0, 6)
)
analogVideoFrozenImageAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalName"),
        ("VIDEOFRAME-SIGMON-VM0002-MIB", "vm0002SignalDescription"))
)
if mibBuilder.loadTexts:
    analogVideoFrozenImageAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEOFRAME-SIGMON-VM0002-MIB",
    **{"vm0002AnalogVideo": vm0002AnalogVideo,
       "vm0002Table": vm0002Table,
       "vm0002Entry": vm0002Entry,
       "vm0002SlotNumber": vm0002SlotNumber,
       "vm0002Active": vm0002Active,
       "vm0002FirmwareRev": vm0002FirmwareRev,
       "vm0002Locate": vm0002Locate,
       "vm0002SignalTable": vm0002SignalTable,
       "vm0002SignalEntry": vm0002SignalEntry,
       "vm0002SignalSlotNumber": vm0002SignalSlotNumber,
       "vm0002SignalNumber": vm0002SignalNumber,
       "vm0002SignalName": vm0002SignalName,
       "vm0002SignalDescription": vm0002SignalDescription,
       "vm0002VSyncLossThreshold": vm0002VSyncLossThreshold,
       "vm0002VSyncLossPeriod": vm0002VSyncLossPeriod,
       "vm0002VSyncLossAlarmState": vm0002VSyncLossAlarmState,
       "vm0002VSyncLossAlarmAck": vm0002VSyncLossAlarmAck,
       "vm0002VSyncLossTrapEnable": vm0002VSyncLossTrapEnable,
       "vm0002HSyncLossThreshold": vm0002HSyncLossThreshold,
       "vm0002HSyncLossPeriod": vm0002HSyncLossPeriod,
       "vm0002HSyncLossAlarmState": vm0002HSyncLossAlarmState,
       "vm0002HSyncLossAlarmAck": vm0002HSyncLossAlarmAck,
       "vm0002HSyncLossTrapEnable": vm0002HSyncLossTrapEnable,
       "vm0002PedestalHighThreshold": vm0002PedestalHighThreshold,
       "vm0002PedestalHighPeriod": vm0002PedestalHighPeriod,
       "vm0002MeasuredPedestal": vm0002MeasuredPedestal,
       "vm0002PedestalHighAlarmState": vm0002PedestalHighAlarmState,
       "vm0002PedestalHighAlarmAck": vm0002PedestalHighAlarmAck,
       "vm0002PedestalHighTrapEnable": vm0002PedestalHighTrapEnable,
       "vm0002CurrentAplRaw": vm0002CurrentAplRaw,
       "vm0002n100IRECalibrationSet": vm0002n100IRECalibrationSet,
       "vm0002n100IRECalibrationValue": vm0002n100IRECalibrationValue,
       "vm0002AplHighThreshold": vm0002AplHighThreshold,
       "vm0002AplHighDuration": vm0002AplHighDuration,
       "vm0002AplHighAlarmState": vm0002AplHighAlarmState,
       "vm0002AplHighAlarmAck": vm0002AplHighAlarmAck,
       "vm0002AplHighTrapEnable": vm0002AplHighTrapEnable,
       "vm0002AplLowThreshold": vm0002AplLowThreshold,
       "vm0002AplLowDuration": vm0002AplLowDuration,
       "vm0002AplLowAlarmState": vm0002AplLowAlarmState,
       "vm0002AplLowAlarmAck": vm0002AplLowAlarmAck,
       "vm0002AplLowTrapEnable": vm0002AplLowTrapEnable,
       "vm0002FrozenImageFilter": vm0002FrozenImageFilter,
       "vm0002MaxFrozenDuration": vm0002MaxFrozenDuration,
       "vm0002FrozenAlarmState": vm0002FrozenAlarmState,
       "vm0002FrozenAlarmAck": vm0002FrozenAlarmAck,
       "vm0002FrozenTrapEnable": vm0002FrozenTrapEnable,
       "vm0002BurstPresent": vm0002BurstPresent,
       "vm0002AnalogVideoEvents": vm0002AnalogVideoEvents,
       "vm0002AnalogVideoEventsV2": vm0002AnalogVideoEventsV2,
       "analogVideoVSyncLossAlarm": analogVideoVSyncLossAlarm,
       "analogVideoHSyncLossAlarm": analogVideoHSyncLossAlarm,
       "analogVideoPedestalHighAlarm": analogVideoPedestalHighAlarm,
       "analogVideoAPLHighAlarm": analogVideoAPLHighAlarm,
       "analogVideoAPLLowAlarm": analogVideoAPLLowAlarm,
       "analogVideoFrozenImageAlarm": analogVideoFrozenImageAlarm,
       "videoframeSigmonVm0002MIB": videoframeSigmonVm0002MIB,
       "vfProductsVM0002Reg": vfProductsVM0002Reg}
)
