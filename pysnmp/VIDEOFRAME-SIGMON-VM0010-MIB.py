# SNMP MIB module (VIDEOFRAME-SIGMON-VM0010-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIDEOFRAME-SIGMON-VM0010-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:34 2024
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

videoframeSigmonVm0010MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1, 8)
)
videoframeSigmonVm0010MIB.setRevisions(
        ("1901-09-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vm0010GPOInterface_ObjectIdentity = ObjectIdentity
vm0010GPOInterface = _Vm0010GPOInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10)
)
_Vm0010Table_Object = MibTable
vm0010Table = _Vm0010Table_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    vm0010Table.setStatus("current")
_Vm0010Entry_Object = MibTableRow
vm0010Entry = _Vm0010Entry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 1, 1)
)
vm0010Entry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
)
if mibBuilder.loadTexts:
    vm0010Entry.setStatus("current")


class _Vm0010SlotNumber_Type(Integer32):
    """Custom type vm0010SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0010SlotNumber_Type.__name__ = "Integer32"
_Vm0010SlotNumber_Object = MibTableColumn
vm0010SlotNumber = _Vm0010SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 1, 1, 1),
    _Vm0010SlotNumber_Type()
)
vm0010SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0010SlotNumber.setStatus("current")


class _Vm0010Active_Type(Integer32):
    """Custom type vm0010Active based on Integer32"""
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


_Vm0010Active_Type.__name__ = "Integer32"
_Vm0010Active_Object = MibTableColumn
vm0010Active = _Vm0010Active_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 1, 1, 2),
    _Vm0010Active_Type()
)
vm0010Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0010Active.setStatus("current")


class _Vm0010Locate_Type(Integer32):
    """Custom type vm0010Locate based on Integer32"""
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


_Vm0010Locate_Type.__name__ = "Integer32"
_Vm0010Locate_Object = MibTableColumn
vm0010Locate = _Vm0010Locate_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 1, 1, 3),
    _Vm0010Locate_Type()
)
vm0010Locate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0010Locate.setStatus("current")
_Vm0010GPORelayTable_Object = MibTable
vm0010GPORelayTable = _Vm0010GPORelayTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    vm0010GPORelayTable.setStatus("current")
_Vm0010GPORelayEntry_Object = MibTableRow
vm0010GPORelayEntry = _Vm0010GPORelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 2, 1)
)
vm0010GPORelayEntry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
    (0, "VIDEOFRAME-SIGMON-VM0010-MIB", "vm0010GPORelayNumber"),
)
if mibBuilder.loadTexts:
    vm0010GPORelayEntry.setStatus("current")


class _Vm0010GPORelaySlotNumber_Type(Integer32):
    """Custom type vm0010GPORelaySlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Vm0010GPORelaySlotNumber_Type.__name__ = "Integer32"
_Vm0010GPORelaySlotNumber_Object = MibTableColumn
vm0010GPORelaySlotNumber = _Vm0010GPORelaySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 2, 1, 1),
    _Vm0010GPORelaySlotNumber_Type()
)
vm0010GPORelaySlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0010GPORelaySlotNumber.setStatus("current")


class _Vm0010GPORelayNumber_Type(Integer32):
    """Custom type vm0010GPORelayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Vm0010GPORelayNumber_Type.__name__ = "Integer32"
_Vm0010GPORelayNumber_Object = MibTableColumn
vm0010GPORelayNumber = _Vm0010GPORelayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 2, 1, 2),
    _Vm0010GPORelayNumber_Type()
)
vm0010GPORelayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vm0010GPORelayNumber.setStatus("current")


class _Vm0010GPOClosureState_Type(Integer32):
    """Custom type vm0010GPOClosureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_Vm0010GPOClosureState_Type.__name__ = "Integer32"
_Vm0010GPOClosureState_Object = MibTableColumn
vm0010GPOClosureState = _Vm0010GPOClosureState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 2, 1, 3),
    _Vm0010GPOClosureState_Type()
)
vm0010GPOClosureState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0010GPOClosureState.setStatus("current")


class _Vm0010GPOClosureName_Type(DisplayString):
    """Custom type vm0010GPOClosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Vm0010GPOClosureName_Type.__name__ = "DisplayString"
_Vm0010GPOClosureName_Object = MibTableColumn
vm0010GPOClosureName = _Vm0010GPOClosureName_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 2, 1, 4),
    _Vm0010GPOClosureName_Type()
)
vm0010GPOClosureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0010GPOClosureName.setStatus("current")


class _Vm0010GPOClosureDescription_Type(DisplayString):
    """Custom type vm0010GPOClosureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_Vm0010GPOClosureDescription_Type.__name__ = "DisplayString"
_Vm0010GPOClosureDescription_Object = MibTableColumn
vm0010GPOClosureDescription = _Vm0010GPOClosureDescription_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 10, 2, 1, 5),
    _Vm0010GPOClosureDescription_Type()
)
vm0010GPOClosureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vm0010GPOClosureDescription.setStatus("current")
_VfProductsVM0010_ObjectIdentity = ObjectIdentity
vfProductsVM0010 = _VfProductsVM0010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 5, 10)
)
if mibBuilder.loadTexts:
    vfProductsVM0010.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEOFRAME-SIGMON-VM0010-MIB",
    **{"vm0010GPOInterface": vm0010GPOInterface,
       "vm0010Table": vm0010Table,
       "vm0010Entry": vm0010Entry,
       "vm0010SlotNumber": vm0010SlotNumber,
       "vm0010Active": vm0010Active,
       "vm0010Locate": vm0010Locate,
       "vm0010GPORelayTable": vm0010GPORelayTable,
       "vm0010GPORelayEntry": vm0010GPORelayEntry,
       "vm0010GPORelaySlotNumber": vm0010GPORelaySlotNumber,
       "vm0010GPORelayNumber": vm0010GPORelayNumber,
       "vm0010GPOClosureState": vm0010GPOClosureState,
       "vm0010GPOClosureName": vm0010GPOClosureName,
       "vm0010GPOClosureDescription": vm0010GPOClosureDescription,
       "videoframeSigmonVm0010MIB": videoframeSigmonVm0010MIB,
       "vfProductsVM0010": vfProductsVM0010}
)
