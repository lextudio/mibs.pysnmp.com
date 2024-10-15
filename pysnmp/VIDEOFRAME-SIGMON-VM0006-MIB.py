# SNMP MIB module (VIDEOFRAME-SIGMON-VM0006-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIDEOFRAME-SIGMON-VM0006-MIB
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

videoframeSigmonVm0006MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1, 6)
)
videoframeSigmonVm0006MIB.setRevisions(
        ("1901-09-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vm0006GPIInterface_ObjectIdentity = ObjectIdentity
vm0006GPIInterface = _Vm0006GPIInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6)
)
_Vm0006Table_Object = MibTable
vm0006Table = _Vm0006Table_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    vm0006Table.setStatus("current")
_Vm0006Entry_Object = MibTableRow
vm0006Entry = _Vm0006Entry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 1, 1)
)
vm0006Entry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
)
if mibBuilder.loadTexts:
    vm0006Entry.setStatus("current")


class _Vm0006SlotNumber_Type(Integer32):
    """Custom type vm0006SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0006SlotNumber_Type.__name__ = "Integer32"
_Vm0006SlotNumber_Object = MibTableColumn
vm0006SlotNumber = _Vm0006SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 1, 1, 1),
    _Vm0006SlotNumber_Type()
)
vm0006SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0006SlotNumber.setStatus("current")


class _Vm0006Active_Type(Integer32):
    """Custom type vm0006Active based on Integer32"""
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


_Vm0006Active_Type.__name__ = "Integer32"
_Vm0006Active_Object = MibTableColumn
vm0006Active = _Vm0006Active_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 1, 1, 2),
    _Vm0006Active_Type()
)
vm0006Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0006Active.setStatus("current")


class _Vm0006Locate_Type(Integer32):
    """Custom type vm0006Locate based on Integer32"""
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


_Vm0006Locate_Type.__name__ = "Integer32"
_Vm0006Locate_Object = MibTableColumn
vm0006Locate = _Vm0006Locate_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 1, 1, 3),
    _Vm0006Locate_Type()
)
vm0006Locate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0006Locate.setStatus("current")
_Vm0006GPISignalTable_Object = MibTable
vm0006GPISignalTable = _Vm0006GPISignalTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    vm0006GPISignalTable.setStatus("current")
_Vm0006GPISignalEntry_Object = MibTableRow
vm0006GPISignalEntry = _Vm0006GPISignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2, 1)
)
vm0006GPISignalEntry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
    (0, "VIDEOFRAME-SIGMON-VM0006-MIB", "vm0006GPISignalNumber"),
)
if mibBuilder.loadTexts:
    vm0006GPISignalEntry.setStatus("current")


class _Vm0006GPISignalSlotNumber_Type(Integer32):
    """Custom type vm0006GPISignalSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0006GPISignalSlotNumber_Type.__name__ = "Integer32"
_Vm0006GPISignalSlotNumber_Object = MibTableColumn
vm0006GPISignalSlotNumber = _Vm0006GPISignalSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2, 1, 1),
    _Vm0006GPISignalSlotNumber_Type()
)
vm0006GPISignalSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0006GPISignalSlotNumber.setStatus("current")


class _Vm0006GPISignalNumber_Type(Integer32):
    """Custom type vm0006GPISignalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Vm0006GPISignalNumber_Type.__name__ = "Integer32"
_Vm0006GPISignalNumber_Object = MibTableColumn
vm0006GPISignalNumber = _Vm0006GPISignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2, 1, 2),
    _Vm0006GPISignalNumber_Type()
)
vm0006GPISignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0006GPISignalNumber.setStatus("current")


class _Vm0006GPISignalState_Type(Integer32):
    """Custom type vm0006GPISignalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_Vm0006GPISignalState_Type.__name__ = "Integer32"
_Vm0006GPISignalState_Object = MibTableColumn
vm0006GPISignalState = _Vm0006GPISignalState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2, 1, 3),
    _Vm0006GPISignalState_Type()
)
vm0006GPISignalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0006GPISignalState.setStatus("current")


class _Vm0007GPIChandedAck_Type(Integer32):
    """Custom type vm0007GPIChandedAck based on Integer32"""
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


_Vm0007GPIChandedAck_Type.__name__ = "Integer32"
_Vm0007GPIChandedAck_Object = MibTableColumn
vm0007GPIChandedAck = _Vm0007GPIChandedAck_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2, 1, 4),
    _Vm0007GPIChandedAck_Type()
)
vm0007GPIChandedAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0007GPIChandedAck.setStatus("current")


class _Vm0006GPISignalName_Type(DisplayString):
    """Custom type vm0006GPISignalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0006GPISignalName_Type.__name__ = "DisplayString"
_Vm0006GPISignalName_Object = MibTableColumn
vm0006GPISignalName = _Vm0006GPISignalName_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2, 1, 5),
    _Vm0006GPISignalName_Type()
)
vm0006GPISignalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0006GPISignalName.setStatus("current")


class _Vm0006GPISignalDescription_Type(DisplayString):
    """Custom type vm0006GPISignalDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0006GPISignalDescription_Type.__name__ = "DisplayString"
_Vm0006GPISignalDescription_Object = MibTableColumn
vm0006GPISignalDescription = _Vm0006GPISignalDescription_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2, 1, 6),
    _Vm0006GPISignalDescription_Type()
)
vm0006GPISignalDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0006GPISignalDescription.setStatus("current")


class _Vm0006GPISignalTrapEnable_Type(Integer32):
    """Custom type vm0006GPISignalTrapEnable based on Integer32"""
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


_Vm0006GPISignalTrapEnable_Type.__name__ = "Integer32"
_Vm0006GPISignalTrapEnable_Object = MibTableColumn
vm0006GPISignalTrapEnable = _Vm0006GPISignalTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 2, 1, 7),
    _Vm0006GPISignalTrapEnable_Type()
)
vm0006GPISignalTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0006GPISignalTrapEnable.setStatus("current")
_Vm0006GPIInterfaceEvents_ObjectIdentity = ObjectIdentity
vm0006GPIInterfaceEvents = _Vm0006GPIInterfaceEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 3)
)
_Vm0006GPIInterfaceEventsV2_ObjectIdentity = ObjectIdentity
vm0006GPIInterfaceEventsV2 = _Vm0006GPIInterfaceEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 3, 0)
)
_VfProductsVM0006_ObjectIdentity = ObjectIdentity
vfProductsVM0006 = _VfProductsVM0006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 5, 6)
)
if mibBuilder.loadTexts:
    vfProductsVM0006.setStatus("current")

# Managed Objects groups


# Notification objects

gpiChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 6, 3, 0, 1)
)
gpiChanged.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-VM0006-MIB", "vm0006SlotNumber"),
        ("VIDEOFRAME-SIGMON-VM0006-MIB", "vm0006GPISignalNumber"),
        ("VIDEOFRAME-SIGMON-VM0006-MIB", "vm0006GPISignalName"),
        ("VIDEOFRAME-SIGMON-VM0006-MIB", "vm0006GPISignalDescription"))
)
if mibBuilder.loadTexts:
    gpiChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEOFRAME-SIGMON-VM0006-MIB",
    **{"vm0006GPIInterface": vm0006GPIInterface,
       "vm0006Table": vm0006Table,
       "vm0006Entry": vm0006Entry,
       "vm0006SlotNumber": vm0006SlotNumber,
       "vm0006Active": vm0006Active,
       "vm0006Locate": vm0006Locate,
       "vm0006GPISignalTable": vm0006GPISignalTable,
       "vm0006GPISignalEntry": vm0006GPISignalEntry,
       "vm0006GPISignalSlotNumber": vm0006GPISignalSlotNumber,
       "vm0006GPISignalNumber": vm0006GPISignalNumber,
       "vm0006GPISignalState": vm0006GPISignalState,
       "vm0007GPIChandedAck": vm0007GPIChandedAck,
       "vm0006GPISignalName": vm0006GPISignalName,
       "vm0006GPISignalDescription": vm0006GPISignalDescription,
       "vm0006GPISignalTrapEnable": vm0006GPISignalTrapEnable,
       "vm0006GPIInterfaceEvents": vm0006GPIInterfaceEvents,
       "vm0006GPIInterfaceEventsV2": vm0006GPIInterfaceEventsV2,
       "gpiChanged": gpiChanged,
       "videoframeSigmonVm0006MIB": videoframeSigmonVm0006MIB,
       "vfProductsVM0006": vfProductsVM0006}
)
