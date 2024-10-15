# SNMP MIB module (VIDEOFRAME-SIGMON-VM0007-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIDEOFRAME-SIGMON-VM0007-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:33 2024
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

videoframeSigmonVm0007MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1, 7)
)
videoframeSigmonVm0007MIB.setRevisions(
        ("1901-08-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vm0007TransferSwitch_ObjectIdentity = ObjectIdentity
vm0007TransferSwitch = _Vm0007TransferSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7)
)
_Vm0007Table_Object = MibTable
vm0007Table = _Vm0007Table_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    vm0007Table.setStatus("current")
_Vm0007Entry_Object = MibTableRow
vm0007Entry = _Vm0007Entry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1)
)
vm0007Entry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
)
if mibBuilder.loadTexts:
    vm0007Entry.setStatus("current")


class _Vm0007SlotNumber_Type(Integer32):
    """Custom type vm0007SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0007SlotNumber_Type.__name__ = "Integer32"
_Vm0007SlotNumber_Object = MibTableColumn
vm0007SlotNumber = _Vm0007SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 1),
    _Vm0007SlotNumber_Type()
)
vm0007SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0007SlotNumber.setStatus("current")


class _Vm0007Active_Type(Integer32):
    """Custom type vm0007Active based on Integer32"""
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


_Vm0007Active_Type.__name__ = "Integer32"
_Vm0007Active_Object = MibTableColumn
vm0007Active = _Vm0007Active_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 2),
    _Vm0007Active_Type()
)
vm0007Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0007Active.setStatus("current")


class _Vm0007Locate_Type(Integer32):
    """Custom type vm0007Locate based on Integer32"""
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


_Vm0007Locate_Type.__name__ = "Integer32"
_Vm0007Locate_Object = MibTableColumn
vm0007Locate = _Vm0007Locate_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 3),
    _Vm0007Locate_Type()
)
vm0007Locate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007Locate.setStatus("current")


class _Vm0007VideoSignalSwitchState_Type(Integer32):
    """Custom type vm0007VideoSignalSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 1),
          ("straightThrough", 2))
    )


_Vm0007VideoSignalSwitchState_Type.__name__ = "Integer32"
_Vm0007VideoSignalSwitchState_Object = MibTableColumn
vm0007VideoSignalSwitchState = _Vm0007VideoSignalSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 4),
    _Vm0007VideoSignalSwitchState_Type()
)
vm0007VideoSignalSwitchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoSignalSwitchState.setStatus("current")


class _Vm0007TransferSwitchAlarmAck_Type(Integer32):
    """Custom type vm0007TransferSwitchAlarmAck based on Integer32"""
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


_Vm0007TransferSwitchAlarmAck_Type.__name__ = "Integer32"
_Vm0007TransferSwitchAlarmAck_Object = MibTableColumn
vm0007TransferSwitchAlarmAck = _Vm0007TransferSwitchAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 5),
    _Vm0007TransferSwitchAlarmAck_Type()
)
vm0007TransferSwitchAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007TransferSwitchAlarmAck.setStatus("current")


class _Vm0007CPUOverride_Type(Integer32):
    """Custom type vm0007CPUOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Vm0007CPUOverride_Type.__name__ = "Integer32"
_Vm0007CPUOverride_Object = MibTableColumn
vm0007CPUOverride = _Vm0007CPUOverride_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 6),
    _Vm0007CPUOverride_Type()
)
vm0007CPUOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007CPUOverride.setStatus("current")


class _Vm0007VideoSource1Name_Type(DisplayString):
    """Custom type vm0007VideoSource1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0007VideoSource1Name_Type.__name__ = "DisplayString"
_Vm0007VideoSource1Name_Object = MibTableColumn
vm0007VideoSource1Name = _Vm0007VideoSource1Name_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 7),
    _Vm0007VideoSource1Name_Type()
)
vm0007VideoSource1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoSource1Name.setStatus("current")


class _Vm0007VideoSource1Description_Type(DisplayString):
    """Custom type vm0007VideoSource1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0007VideoSource1Description_Type.__name__ = "DisplayString"
_Vm0007VideoSource1Description_Object = MibTableColumn
vm0007VideoSource1Description = _Vm0007VideoSource1Description_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 8),
    _Vm0007VideoSource1Description_Type()
)
vm0007VideoSource1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoSource1Description.setStatus("current")


class _Vm0007VideoSource2Name_Type(DisplayString):
    """Custom type vm0007VideoSource2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0007VideoSource2Name_Type.__name__ = "DisplayString"
_Vm0007VideoSource2Name_Object = MibTableColumn
vm0007VideoSource2Name = _Vm0007VideoSource2Name_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 9),
    _Vm0007VideoSource2Name_Type()
)
vm0007VideoSource2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoSource2Name.setStatus("current")


class _Vm0007VideoSource2Description_Type(DisplayString):
    """Custom type vm0007VideoSource2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0007VideoSource2Description_Type.__name__ = "DisplayString"
_Vm0007VideoSource2Description_Object = MibTableColumn
vm0007VideoSource2Description = _Vm0007VideoSource2Description_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 10),
    _Vm0007VideoSource2Description_Type()
)
vm0007VideoSource2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoSource2Description.setStatus("current")


class _Vm0007VideoDest1Name_Type(DisplayString):
    """Custom type vm0007VideoDest1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0007VideoDest1Name_Type.__name__ = "DisplayString"
_Vm0007VideoDest1Name_Object = MibTableColumn
vm0007VideoDest1Name = _Vm0007VideoDest1Name_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 11),
    _Vm0007VideoDest1Name_Type()
)
vm0007VideoDest1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoDest1Name.setStatus("current")


class _Vm0007VideoDest1Description_Type(DisplayString):
    """Custom type vm0007VideoDest1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0007VideoDest1Description_Type.__name__ = "DisplayString"
_Vm0007VideoDest1Description_Object = MibTableColumn
vm0007VideoDest1Description = _Vm0007VideoDest1Description_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 12),
    _Vm0007VideoDest1Description_Type()
)
vm0007VideoDest1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoDest1Description.setStatus("current")


class _Vm0007VideoDest2Name_Type(DisplayString):
    """Custom type vm0007VideoDest2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0007VideoDest2Name_Type.__name__ = "DisplayString"
_Vm0007VideoDest2Name_Object = MibTableColumn
vm0007VideoDest2Name = _Vm0007VideoDest2Name_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 13),
    _Vm0007VideoDest2Name_Type()
)
vm0007VideoDest2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoDest2Name.setStatus("current")


class _Vm0007VideoDest2Description_Type(DisplayString):
    """Custom type vm0007VideoDest2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0007VideoDest2Description_Type.__name__ = "DisplayString"
_Vm0007VideoDest2Description_Object = MibTableColumn
vm0007VideoDest2Description = _Vm0007VideoDest2Description_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 1, 1, 14),
    _Vm0007VideoDest2Description_Type()
)
vm0007VideoDest2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007VideoDest2Description.setStatus("current")
_Vm0007AudioChannelTable_Object = MibTable
vm0007AudioChannelTable = _Vm0007AudioChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    vm0007AudioChannelTable.setStatus("current")
_Vm0007AudioChannelEntry_Object = MibTableRow
vm0007AudioChannelEntry = _Vm0007AudioChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1)
)
vm0007AudioChannelEntry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
    (0, "VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007AudioChannelNumber"),
)
if mibBuilder.loadTexts:
    vm0007AudioChannelEntry.setStatus("current")


class _Vm0007AudioChannelSlotNumber_Type(Integer32):
    """Custom type vm0007AudioChannelSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0007AudioChannelSlotNumber_Type.__name__ = "Integer32"
_Vm0007AudioChannelSlotNumber_Object = MibTableColumn
vm0007AudioChannelSlotNumber = _Vm0007AudioChannelSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 1),
    _Vm0007AudioChannelSlotNumber_Type()
)
vm0007AudioChannelSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0007AudioChannelSlotNumber.setStatus("current")


class _Vm0007AudioChannelNumber_Type(Integer32):
    """Custom type vm0007AudioChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Vm0007AudioChannelNumber_Type.__name__ = "Integer32"
_Vm0007AudioChannelNumber_Object = MibTableColumn
vm0007AudioChannelNumber = _Vm0007AudioChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 2),
    _Vm0007AudioChannelNumber_Type()
)
vm0007AudioChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0007AudioChannelNumber.setStatus("current")


class _Vm0007AudioChannelSwitchState_Type(Integer32):
    """Custom type vm0007AudioChannelSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 1),
          ("straightThrough", 2))
    )


_Vm0007AudioChannelSwitchState_Type.__name__ = "Integer32"
_Vm0007AudioChannelSwitchState_Object = MibTableColumn
vm0007AudioChannelSwitchState = _Vm0007AudioChannelSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 3),
    _Vm0007AudioChannelSwitchState_Type()
)
vm0007AudioChannelSwitchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChannelSwitchState.setStatus("current")


class _Vm0007AudioChanSource1Name_Type(DisplayString):
    """Custom type vm0007AudioChanSource1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0007AudioChanSource1Name_Type.__name__ = "DisplayString"
_Vm0007AudioChanSource1Name_Object = MibTableColumn
vm0007AudioChanSource1Name = _Vm0007AudioChanSource1Name_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 4),
    _Vm0007AudioChanSource1Name_Type()
)
vm0007AudioChanSource1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChanSource1Name.setStatus("current")


class _Vm0007AudioChanSource1Description_Type(DisplayString):
    """Custom type vm0007AudioChanSource1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0007AudioChanSource1Description_Type.__name__ = "DisplayString"
_Vm0007AudioChanSource1Description_Object = MibTableColumn
vm0007AudioChanSource1Description = _Vm0007AudioChanSource1Description_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 5),
    _Vm0007AudioChanSource1Description_Type()
)
vm0007AudioChanSource1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChanSource1Description.setStatus("current")


class _Vm0007AudioChanSource2Name_Type(DisplayString):
    """Custom type vm0007AudioChanSource2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0007AudioChanSource2Name_Type.__name__ = "DisplayString"
_Vm0007AudioChanSource2Name_Object = MibTableColumn
vm0007AudioChanSource2Name = _Vm0007AudioChanSource2Name_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 6),
    _Vm0007AudioChanSource2Name_Type()
)
vm0007AudioChanSource2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChanSource2Name.setStatus("current")


class _Vm0007AudioChanSource2Description_Type(DisplayString):
    """Custom type vm0007AudioChanSource2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0007AudioChanSource2Description_Type.__name__ = "DisplayString"
_Vm0007AudioChanSource2Description_Object = MibTableColumn
vm0007AudioChanSource2Description = _Vm0007AudioChanSource2Description_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 7),
    _Vm0007AudioChanSource2Description_Type()
)
vm0007AudioChanSource2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChanSource2Description.setStatus("current")


class _Vm0007AudioChanDest1Name_Type(DisplayString):
    """Custom type vm0007AudioChanDest1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0007AudioChanDest1Name_Type.__name__ = "DisplayString"
_Vm0007AudioChanDest1Name_Object = MibTableColumn
vm0007AudioChanDest1Name = _Vm0007AudioChanDest1Name_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 8),
    _Vm0007AudioChanDest1Name_Type()
)
vm0007AudioChanDest1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChanDest1Name.setStatus("current")


class _Vm0007AudioChanDest1Description_Type(DisplayString):
    """Custom type vm0007AudioChanDest1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0007AudioChanDest1Description_Type.__name__ = "DisplayString"
_Vm0007AudioChanDest1Description_Object = MibTableColumn
vm0007AudioChanDest1Description = _Vm0007AudioChanDest1Description_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 9),
    _Vm0007AudioChanDest1Description_Type()
)
vm0007AudioChanDest1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChanDest1Description.setStatus("current")


class _Vm0007AudioChanDest2Name_Type(DisplayString):
    """Custom type vm0007AudioChanDest2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0007AudioChanDest2Name_Type.__name__ = "DisplayString"
_Vm0007AudioChanDest2Name_Object = MibTableColumn
vm0007AudioChanDest2Name = _Vm0007AudioChanDest2Name_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 10),
    _Vm0007AudioChanDest2Name_Type()
)
vm0007AudioChanDest2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChanDest2Name.setStatus("current")


class _Vm0007AudioChanDest2Description_Type(DisplayString):
    """Custom type vm0007AudioChanDest2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0007AudioChanDest2Description_Type.__name__ = "DisplayString"
_Vm0007AudioChanDest2Description_Object = MibTableColumn
vm0007AudioChanDest2Description = _Vm0007AudioChanDest2Description_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 2, 1, 11),
    _Vm0007AudioChanDest2Description_Type()
)
vm0007AudioChanDest2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007AudioChanDest2Description.setStatus("current")
_Vm0007TransferSwitchEvents_ObjectIdentity = ObjectIdentity
vm0007TransferSwitchEvents = _Vm0007TransferSwitchEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 3)
)
_Vm0007TransferSwitchEventsV2_ObjectIdentity = ObjectIdentity
vm0007TransferSwitchEventsV2 = _Vm0007TransferSwitchEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 3, 0)
)
_VfProductsVM0007Reg_ObjectIdentity = ObjectIdentity
vfProductsVM0007Reg = _VfProductsVM0007Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 5, 7)
)
if mibBuilder.loadTexts:
    vfProductsVM0007Reg.setStatus("current")

# Managed Objects groups


# Notification objects

transferSwitchActivatedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 3, 0, 1)
)
transferSwitchActivatedAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007VideoSource1Name"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007VideoSource2Name"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007VideoDest1Name"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007VideoDest2Name"))
)
if mibBuilder.loadTexts:
    transferSwitchActivatedAlarm.setStatus(
        "current"
    )

transferSwitchNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 7, 3, 0, 2)
)
transferSwitchNormalAlarm.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007VideoSource1Name"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007VideoSource2Name"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007VideoDest1Name"),
        ("VIDEOFRAME-SIGMON-VM0007-MIB", "vm0007VideoDest2Name"))
)
if mibBuilder.loadTexts:
    transferSwitchNormalAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEOFRAME-SIGMON-VM0007-MIB",
    **{"vm0007TransferSwitch": vm0007TransferSwitch,
       "vm0007Table": vm0007Table,
       "vm0007Entry": vm0007Entry,
       "vm0007SlotNumber": vm0007SlotNumber,
       "vm0007Active": vm0007Active,
       "vm0007Locate": vm0007Locate,
       "vm0007VideoSignalSwitchState": vm0007VideoSignalSwitchState,
       "vm0007TransferSwitchAlarmAck": vm0007TransferSwitchAlarmAck,
       "vm0007CPUOverride": vm0007CPUOverride,
       "vm0007VideoSource1Name": vm0007VideoSource1Name,
       "vm0007VideoSource1Description": vm0007VideoSource1Description,
       "vm0007VideoSource2Name": vm0007VideoSource2Name,
       "vm0007VideoSource2Description": vm0007VideoSource2Description,
       "vm0007VideoDest1Name": vm0007VideoDest1Name,
       "vm0007VideoDest1Description": vm0007VideoDest1Description,
       "vm0007VideoDest2Name": vm0007VideoDest2Name,
       "vm0007VideoDest2Description": vm0007VideoDest2Description,
       "vm0007AudioChannelTable": vm0007AudioChannelTable,
       "vm0007AudioChannelEntry": vm0007AudioChannelEntry,
       "vm0007AudioChannelSlotNumber": vm0007AudioChannelSlotNumber,
       "vm0007AudioChannelNumber": vm0007AudioChannelNumber,
       "vm0007AudioChannelSwitchState": vm0007AudioChannelSwitchState,
       "vm0007AudioChanSource1Name": vm0007AudioChanSource1Name,
       "vm0007AudioChanSource1Description": vm0007AudioChanSource1Description,
       "vm0007AudioChanSource2Name": vm0007AudioChanSource2Name,
       "vm0007AudioChanSource2Description": vm0007AudioChanSource2Description,
       "vm0007AudioChanDest1Name": vm0007AudioChanDest1Name,
       "vm0007AudioChanDest1Description": vm0007AudioChanDest1Description,
       "vm0007AudioChanDest2Name": vm0007AudioChanDest2Name,
       "vm0007AudioChanDest2Description": vm0007AudioChanDest2Description,
       "vm0007TransferSwitchEvents": vm0007TransferSwitchEvents,
       "vm0007TransferSwitchEventsV2": vm0007TransferSwitchEventsV2,
       "transferSwitchActivatedAlarm": transferSwitchActivatedAlarm,
       "transferSwitchNormalAlarm": transferSwitchNormalAlarm,
       "videoframeSigmonVm0007MIB": videoframeSigmonVm0007MIB,
       "vfProductsVM0007Reg": vfProductsVM0007Reg}
)
