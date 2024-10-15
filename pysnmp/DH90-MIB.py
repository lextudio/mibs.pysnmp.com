# SNMP MIB module (DH90-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DH90-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:57 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecExp_ObjectIdentity = ObjectIdentity
decExp = _DecExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3)
)
_Dh90_ObjectIdentity = ObjectIdentity
dh90 = _Dh90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1)
)


class _Dh90Type_Type(Integer32):
    """Custom type dh90Type based on Integer32"""
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
        *(("dechub90", 4),
          ("invalid", 2),
          ("standAloneCommunity", 3),
          ("unknown", 1))
    )


_Dh90Type_Type.__name__ = "Integer32"
_Dh90Type_Object = MibScalar
dh90Type = _Dh90Type_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 1),
    _Dh90Type_Type()
)
dh90Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90Type.setStatus("mandatory")


class _Dh90Backplane_Type(Integer32):
    """Custom type dh90Backplane based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("unknown", 1))
    )


_Dh90Backplane_Type.__name__ = "Integer32"
_Dh90Backplane_Object = MibScalar
dh90Backplane = _Dh90Backplane_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 2),
    _Dh90Backplane_Type()
)
dh90Backplane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90Backplane.setStatus("mandatory")
_Dh90LastChange_Type = TimeTicks
_Dh90LastChange_Object = MibScalar
dh90LastChange = _Dh90LastChange_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 3),
    _Dh90LastChange_Type()
)
dh90LastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90LastChange.setStatus("mandatory")


class _Dh90NumberSlots_Type(Integer32):
    """Custom type dh90NumberSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dh90NumberSlots_Type.__name__ = "Integer32"
_Dh90NumberSlots_Object = MibScalar
dh90NumberSlots = _Dh90NumberSlots_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 4),
    _Dh90NumberSlots_Type()
)
dh90NumberSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90NumberSlots.setStatus("mandatory")
_Dh90SlotTable_Object = MibTable
dh90SlotTable = _Dh90SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5)
)
if mibBuilder.loadTexts:
    dh90SlotTable.setStatus("mandatory")
_Dh90SlotEntry_Object = MibTableRow
dh90SlotEntry = _Dh90SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1)
)
dh90SlotEntry.setIndexNames(
    (0, "DH90-MIB", "dh90SlotIndex"),
)
if mibBuilder.loadTexts:
    dh90SlotEntry.setStatus("mandatory")


class _Dh90SlotIndex_Type(Integer32):
    """Custom type dh90SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dh90SlotIndex_Type.__name__ = "Integer32"
_Dh90SlotIndex_Object = MibTableColumn
dh90SlotIndex = _Dh90SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 1),
    _Dh90SlotIndex_Type()
)
dh90SlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90SlotIndex.setStatus("mandatory")


class _Dh90SlotModuleType_Type(Integer32):
    """Custom type dh90SlotModuleType based on Integer32"""
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
        *(("decagent90", 7),
          ("decbridge90", 4),
          ("decrepeater90C", 5),
          ("decrepeater90T", 6),
          ("decserver90L", 3),
          ("decserver90LT", 9),
          ("decserver90Lplus", 8),
          ("empty", 2),
          ("unknown", 1))
    )


_Dh90SlotModuleType_Type.__name__ = "Integer32"
_Dh90SlotModuleType_Object = MibTableColumn
dh90SlotModuleType = _Dh90SlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 2),
    _Dh90SlotModuleType_Type()
)
dh90SlotModuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90SlotModuleType.setStatus("mandatory")


class _Dh90SlotModuleName_Type(DisplayString):
    """Custom type dh90SlotModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Dh90SlotModuleName_Type.__name__ = "DisplayString"
_Dh90SlotModuleName_Object = MibTableColumn
dh90SlotModuleName = _Dh90SlotModuleName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 3),
    _Dh90SlotModuleName_Type()
)
dh90SlotModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90SlotModuleName.setStatus("mandatory")


class _Dh90SlotModuleVersion_Type(DisplayString):
    """Custom type dh90SlotModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dh90SlotModuleVersion_Type.__name__ = "DisplayString"
_Dh90SlotModuleVersion_Object = MibTableColumn
dh90SlotModuleVersion = _Dh90SlotModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 4),
    _Dh90SlotModuleVersion_Type()
)
dh90SlotModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90SlotModuleVersion.setStatus("mandatory")
_Dh90SlotCounterTime_Type = Counter32
_Dh90SlotCounterTime_Object = MibTableColumn
dh90SlotCounterTime = _Dh90SlotCounterTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 5),
    _Dh90SlotCounterTime_Type()
)
dh90SlotCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90SlotCounterTime.setStatus("mandatory")


class _Dh90SlotIfBase_Type(Integer32):
    """Custom type dh90SlotIfBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 17),
    )


_Dh90SlotIfBase_Type.__name__ = "Integer32"
_Dh90SlotIfBase_Object = MibTableColumn
dh90SlotIfBase = _Dh90SlotIfBase_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 6),
    _Dh90SlotIfBase_Type()
)
dh90SlotIfBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90SlotIfBase.setStatus("mandatory")


class _Dh90SlotIfNumber_Type(Integer32):
    """Custom type dh90SlotIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Dh90SlotIfNumber_Type.__name__ = "Integer32"
_Dh90SlotIfNumber_Object = MibTableColumn
dh90SlotIfNumber = _Dh90SlotIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 7),
    _Dh90SlotIfNumber_Type()
)
dh90SlotIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90SlotIfNumber.setStatus("mandatory")
_Dh90SlotPhysicalAddress_Type = PhysAddress
_Dh90SlotPhysicalAddress_Object = MibTableColumn
dh90SlotPhysicalAddress = _Dh90SlotPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 8),
    _Dh90SlotPhysicalAddress_Type()
)
dh90SlotPhysicalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90SlotPhysicalAddress.setStatus("mandatory")


class _Dh90SlotNumberOfPorts_Type(Integer32):
    """Custom type dh90SlotNumberOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Dh90SlotNumberOfPorts_Type.__name__ = "Integer32"
_Dh90SlotNumberOfPorts_Object = MibTableColumn
dh90SlotNumberOfPorts = _Dh90SlotNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 9),
    _Dh90SlotNumberOfPorts_Type()
)
dh90SlotNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90SlotNumberOfPorts.setStatus("mandatory")


class _Dh90SlotPassword_Type(DisplayString):
    """Custom type dh90SlotPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Dh90SlotPassword_Type.__name__ = "DisplayString"
_Dh90SlotPassword_Object = MibTableColumn
dh90SlotPassword = _Dh90SlotPassword_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 10),
    _Dh90SlotPassword_Type()
)
dh90SlotPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90SlotPassword.setStatus("mandatory")


class _Dh90SlotNewPassword_Type(DisplayString):
    """Custom type dh90SlotNewPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Dh90SlotNewPassword_Type.__name__ = "DisplayString"
_Dh90SlotNewPassword_Object = MibTableColumn
dh90SlotNewPassword = _Dh90SlotNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 11),
    _Dh90SlotNewPassword_Type()
)
dh90SlotNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90SlotNewPassword.setStatus("mandatory")


class _Dh90SlotPolling_Type(Integer32):
    """Custom type dh90SlotPolling based on Integer32"""
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


_Dh90SlotPolling_Type.__name__ = "Integer32"
_Dh90SlotPolling_Object = MibTableColumn
dh90SlotPolling = _Dh90SlotPolling_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 12),
    _Dh90SlotPolling_Type()
)
dh90SlotPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90SlotPolling.setStatus("mandatory")
_Dh90SlotPrimarySpecific_Type = ObjectIdentifier
_Dh90SlotPrimarySpecific_Object = MibTableColumn
dh90SlotPrimarySpecific = _Dh90SlotPrimarySpecific_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 13),
    _Dh90SlotPrimarySpecific_Type()
)
dh90SlotPrimarySpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90SlotPrimarySpecific.setStatus("mandatory")
_Dh90SlotSecondarySpecific_Type = ObjectIdentifier
_Dh90SlotSecondarySpecific_Object = MibTableColumn
dh90SlotSecondarySpecific = _Dh90SlotSecondarySpecific_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 5, 1, 14),
    _Dh90SlotSecondarySpecific_Type()
)
dh90SlotSecondarySpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dh90SlotSecondarySpecific.setStatus("mandatory")
_Dh90TrapAddressTable_Object = MibTable
dh90TrapAddressTable = _Dh90TrapAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 6)
)
if mibBuilder.loadTexts:
    dh90TrapAddressTable.setStatus("mandatory")
_Dh90TrapEntry_Object = MibTableRow
dh90TrapEntry = _Dh90TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 6, 1)
)
dh90TrapEntry.setIndexNames(
    (0, "DH90-MIB", "dh90TrapAddress"),
)
if mibBuilder.loadTexts:
    dh90TrapEntry.setStatus("mandatory")
_Dh90TrapAddress_Type = IpAddress
_Dh90TrapAddress_Object = MibTableColumn
dh90TrapAddress = _Dh90TrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 1, 6, 1, 1),
    _Dh90TrapAddress_Type()
)
dh90TrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dh90TrapAddress.setStatus("mandatory")
_Da90_ObjectIdentity = ObjectIdentity
da90 = _Da90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2)
)
_Da90FlashErasures_Type = Counter32
_Da90FlashErasures_Object = MibScalar
da90FlashErasures = _Da90FlashErasures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 1),
    _Da90FlashErasures_Type()
)
da90FlashErasures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    da90FlashErasures.setStatus("mandatory")


class _Da90Maintenance_Type(Integer32):
    """Custom type da90Maintenance based on Integer32"""
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
        *(("ready", 1),
          ("reset", 3),
          ("resetToFactory", 4),
          ("unused", 2))
    )


_Da90Maintenance_Type.__name__ = "Integer32"
_Da90Maintenance_Object = MibScalar
da90Maintenance = _Da90Maintenance_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 2),
    _Da90Maintenance_Type()
)
da90Maintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    da90Maintenance.setStatus("mandatory")


class _Da90CommunityNumber_Type(Integer32):
    """Custom type da90CommunityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Da90CommunityNumber_Type.__name__ = "Integer32"
_Da90CommunityNumber_Object = MibScalar
da90CommunityNumber = _Da90CommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 3),
    _Da90CommunityNumber_Type()
)
da90CommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    da90CommunityNumber.setStatus("mandatory")
_Da90CommunityTable_Object = MibTable
da90CommunityTable = _Da90CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 4)
)
if mibBuilder.loadTexts:
    da90CommunityTable.setStatus("mandatory")
_Da90CommunityEntry_Object = MibTableRow
da90CommunityEntry = _Da90CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 4, 1)
)
da90CommunityEntry.setIndexNames(
    (0, "DH90-MIB", "da90CommunityIndex"),
)
if mibBuilder.loadTexts:
    da90CommunityEntry.setStatus("mandatory")


class _Da90CommunityIndex_Type(Integer32):
    """Custom type da90CommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Da90CommunityIndex_Type.__name__ = "Integer32"
_Da90CommunityIndex_Object = MibTableColumn
da90CommunityIndex = _Da90CommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 4, 1, 1),
    _Da90CommunityIndex_Type()
)
da90CommunityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    da90CommunityIndex.setStatus("mandatory")


class _Da90CommunityType_Type(Integer32):
    """Custom type da90CommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("invalid", 2),
          ("unknown", 1))
    )


_Da90CommunityType_Type.__name__ = "Integer32"
_Da90CommunityType_Object = MibTableColumn
da90CommunityType = _Da90CommunityType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 4, 1, 2),
    _Da90CommunityType_Type()
)
da90CommunityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    da90CommunityType.setStatus("mandatory")


class _Da90CommunityROString_Type(OctetString):
    """Custom type da90CommunityROString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Da90CommunityROString_Type.__name__ = "OctetString"
_Da90CommunityROString_Object = MibTableColumn
da90CommunityROString = _Da90CommunityROString_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 4, 1, 3),
    _Da90CommunityROString_Type()
)
da90CommunityROString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    da90CommunityROString.setStatus("mandatory")


class _Da90CommunityRWString_Type(OctetString):
    """Custom type da90CommunityRWString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Da90CommunityRWString_Type.__name__ = "OctetString"
_Da90CommunityRWString_Object = MibTableColumn
da90CommunityRWString = _Da90CommunityRWString_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 4, 1, 4),
    _Da90CommunityRWString_Type()
)
da90CommunityRWString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    da90CommunityRWString.setStatus("mandatory")


class _Da90CommunityTrapString_Type(OctetString):
    """Custom type da90CommunityTrapString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Da90CommunityTrapString_Type.__name__ = "OctetString"
_Da90CommunityTrapString_Object = MibTableColumn
da90CommunityTrapString = _Da90CommunityTrapString_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 2, 4, 1, 5),
    _Da90CommunityTrapString_Type()
)
da90CommunityTrapString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    da90CommunityTrapString.setStatus("mandatory")
_Ds90L_ObjectIdentity = ObjectIdentity
ds90L = _Ds90L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3)
)


class _Ds90LNumberModules_Type(Integer32):
    """Custom type ds90LNumberModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Ds90LNumberModules_Type.__name__ = "Integer32"
_Ds90LNumberModules_Object = MibScalar
ds90LNumberModules = _Ds90LNumberModules_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 1),
    _Ds90LNumberModules_Type()
)
ds90LNumberModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LNumberModules.setStatus("mandatory")
_Ds90LModuleTable_Object = MibTable
ds90LModuleTable = _Ds90LModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ds90LModuleTable.setStatus("mandatory")
_Ds90LModuleEntry_Object = MibTableRow
ds90LModuleEntry = _Ds90LModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1)
)
ds90LModuleEntry.setIndexNames(
    (0, "DH90-MIB", "ds90LSlotIndex"),
)
if mibBuilder.loadTexts:
    ds90LModuleEntry.setStatus("mandatory")


class _Ds90LSlotIndex_Type(Integer32):
    """Custom type ds90LSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ds90LSlotIndex_Type.__name__ = "Integer32"
_Ds90LSlotIndex_Object = MibTableColumn
ds90LSlotIndex = _Ds90LSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 1),
    _Ds90LSlotIndex_Type()
)
ds90LSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LSlotIndex.setStatus("mandatory")
_Ds90LDot3StatsDeferredTransmissions_Type = Counter32
_Ds90LDot3StatsDeferredTransmissions_Object = MibTableColumn
ds90LDot3StatsDeferredTransmissions = _Ds90LDot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 2),
    _Ds90LDot3StatsDeferredTransmissions_Type()
)
ds90LDot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LDot3StatsDeferredTransmissions.setStatus("mandatory")
_Ds90LDot3StatsSingleCollisionFrames_Type = Counter32
_Ds90LDot3StatsSingleCollisionFrames_Object = MibTableColumn
ds90LDot3StatsSingleCollisionFrames = _Ds90LDot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 3),
    _Ds90LDot3StatsSingleCollisionFrames_Type()
)
ds90LDot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LDot3StatsSingleCollisionFrames.setStatus("mandatory")
_Ds90LDot3StatsMultipleCollsionFrames_Type = Counter32
_Ds90LDot3StatsMultipleCollsionFrames_Object = MibTableColumn
ds90LDot3StatsMultipleCollsionFrames = _Ds90LDot3StatsMultipleCollsionFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 4),
    _Ds90LDot3StatsMultipleCollsionFrames_Type()
)
ds90LDot3StatsMultipleCollsionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LDot3StatsMultipleCollsionFrames.setStatus("mandatory")
_Ds90LEnetDataOverruns_Type = Counter32
_Ds90LEnetDataOverruns_Object = MibTableColumn
ds90LEnetDataOverruns = _Ds90LEnetDataOverruns_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 5),
    _Ds90LEnetDataOverruns_Type()
)
ds90LEnetDataOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LEnetDataOverruns.setStatus("mandatory")
_Ds90LLatCircMsgsIns_Type = Counter32
_Ds90LLatCircMsgsIns_Object = MibTableColumn
ds90LLatCircMsgsIns = _Ds90LLatCircMsgsIns_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 6),
    _Ds90LLatCircMsgsIns_Type()
)
ds90LLatCircMsgsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatCircMsgsIns.setStatus("mandatory")
_Ds90LLatCircMsgsOuts_Type = Counter32
_Ds90LLatCircMsgsOuts_Object = MibTableColumn
ds90LLatCircMsgsOuts = _Ds90LLatCircMsgsOuts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 7),
    _Ds90LLatCircMsgsOuts_Type()
)
ds90LLatCircMsgsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatCircMsgsOuts.setStatus("mandatory")
_Ds90LLatSessSolicitAccepts_Type = Counter32
_Ds90LLatSessSolicitAccepts_Object = MibTableColumn
ds90LLatSessSolicitAccepts = _Ds90LLatSessSolicitAccepts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 8),
    _Ds90LLatSessSolicitAccepts_Type()
)
ds90LLatSessSolicitAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatSessSolicitAccepts.setStatus("mandatory")
_Ds90LLatSessSolicitRejects_Type = Counter32
_Ds90LLatSessSolicitRejects_Object = MibTableColumn
ds90LLatSessSolicitRejects = _Ds90LLatSessSolicitRejects_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 9),
    _Ds90LLatSessSolicitRejects_Type()
)
ds90LLatSessSolicitRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatSessSolicitRejects.setStatus("mandatory")
_Ds90LLatCircDuplsMsgs_Type = Counter32
_Ds90LLatCircDuplsMsgs_Object = MibTableColumn
ds90LLatCircDuplsMsgs = _Ds90LLatCircDuplsMsgs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 10),
    _Ds90LLatCircDuplsMsgs_Type()
)
ds90LLatCircDuplsMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatCircDuplsMsgs.setStatus("mandatory")
_Ds90LLatCircMsgRetransmits_Type = Counter32
_Ds90LLatCircMsgRetransmits_Object = MibTableColumn
ds90LLatCircMsgRetransmits = _Ds90LLatCircMsgRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 11),
    _Ds90LLatCircMsgRetransmits_Type()
)
ds90LLatCircMsgRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatCircMsgRetransmits.setStatus("mandatory")
_Ds90LLatSessIllegalSlots_Type = Counter32
_Ds90LLatSessIllegalSlots_Object = MibTableColumn
ds90LLatSessIllegalSlots = _Ds90LLatSessIllegalSlots_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 12),
    _Ds90LLatSessIllegalSlots_Type()
)
ds90LLatSessIllegalSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatSessIllegalSlots.setStatus("mandatory")
_Ds90LIllegalMulticastRcvs_Type = Counter32
_Ds90LIllegalMulticastRcvs_Object = MibTableColumn
ds90LIllegalMulticastRcvs = _Ds90LIllegalMulticastRcvs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 13),
    _Ds90LIllegalMulticastRcvs_Type()
)
ds90LIllegalMulticastRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LIllegalMulticastRcvs.setStatus("mandatory")


class _Ds90LLatCircKeepAlive_Type(Integer32):
    """Custom type ds90LLatCircKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_Ds90LLatCircKeepAlive_Type.__name__ = "Integer32"
_Ds90LLatCircKeepAlive_Object = MibTableColumn
ds90LLatCircKeepAlive = _Ds90LLatCircKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 14),
    _Ds90LLatCircKeepAlive_Type()
)
ds90LLatCircKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatCircKeepAlive.setStatus("mandatory")


class _Ds90LLatCircRetransmitLimit_Type(Integer32):
    """Custom type ds90LLatCircRetransmitLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 120),
    )


_Ds90LLatCircRetransmitLimit_Type.__name__ = "Integer32"
_Ds90LLatCircRetransmitLimit_Object = MibTableColumn
ds90LLatCircRetransmitLimit = _Ds90LLatCircRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 15),
    _Ds90LLatCircRetransmitLimit_Type()
)
ds90LLatCircRetransmitLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatCircRetransmitLimit.setStatus("mandatory")
_Ds90LLatCircInvalidMsgs_Type = Counter32
_Ds90LLatCircInvalidMsgs_Object = MibTableColumn
ds90LLatCircInvalidMsgs = _Ds90LLatCircInvalidMsgs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 16),
    _Ds90LLatCircInvalidMsgs_Type()
)
ds90LLatCircInvalidMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LLatCircInvalidMsgs.setStatus("mandatory")


class _Ds90LAuthorizeMode_Type(Integer32):
    """Custom type ds90LAuthorizeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ds90LAuthorizeMode_Type.__name__ = "Integer32"
_Ds90LAuthorizeMode_Object = MibScalar
ds90LAuthorizeMode = _Ds90LAuthorizeMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 17),
    _Ds90LAuthorizeMode_Type()
)
ds90LAuthorizeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LAuthorizeMode.setStatus("mandatory")


class _Ds90LMaintenance_Type(Integer32):
    """Custom type ds90LMaintenance based on Integer32"""
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
        *(("ready", 1),
          ("reset", 3),
          ("resetToFactory", 4),
          ("zeroCounters", 2))
    )


_Ds90LMaintenance_Type.__name__ = "Integer32"
_Ds90LMaintenance_Object = MibTableColumn
ds90LMaintenance = _Ds90LMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 18),
    _Ds90LMaintenance_Type()
)
ds90LMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LMaintenance.setStatus("mandatory")


class _Ds90LPrompt_Type(DisplayString):
    """Custom type ds90LPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ds90LPrompt_Type.__name__ = "DisplayString"
_Ds90LPrompt_Object = MibTableColumn
ds90LPrompt = _Ds90LPrompt_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 2, 1, 19),
    _Ds90LPrompt_Type()
)
ds90LPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LPrompt.setStatus("mandatory")
_Ds90LPortTable_Object = MibTable
ds90LPortTable = _Ds90LPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3)
)
if mibBuilder.loadTexts:
    ds90LPortTable.setStatus("mandatory")
_Ds90LPortEntry_Object = MibTableRow
ds90LPortEntry = _Ds90LPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3, 1)
)
ds90LPortEntry.setIndexNames(
    (0, "DH90-MIB", "ds90LPortIndex"),
)
if mibBuilder.loadTexts:
    ds90LPortEntry.setStatus("mandatory")


class _Ds90LPortIndex_Type(Integer32):
    """Custom type ds90LPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1608),
    )


_Ds90LPortIndex_Type.__name__ = "Integer32"
_Ds90LPortIndex_Object = MibTableColumn
ds90LPortIndex = _Ds90LPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3, 1, 1),
    _Ds90LPortIndex_Type()
)
ds90LPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LPortIndex.setStatus("mandatory")


class _Ds90LPortRemoteModification_Type(Integer32):
    """Custom type ds90LPortRemoteModification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ds90LPortRemoteModification_Type.__name__ = "Integer32"
_Ds90LPortRemoteModification_Object = MibTableColumn
ds90LPortRemoteModification = _Ds90LPortRemoteModification_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3, 1, 2),
    _Ds90LPortRemoteModification_Type()
)
ds90LPortRemoteModification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LPortRemoteModification.setStatus("mandatory")


class _Ds90LPortType_Type(Integer32):
    """Custom type ds90LPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("printer", 2),
          ("terminal", 1))
    )


_Ds90LPortType_Type.__name__ = "Integer32"
_Ds90LPortType_Object = MibTableColumn
ds90LPortType = _Ds90LPortType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3, 1, 3),
    _Ds90LPortType_Type()
)
ds90LPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LPortType.setStatus("mandatory")


class _Ds90LPortBreak_Type(Integer32):
    """Custom type ds90LPortBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_Ds90LPortBreak_Type.__name__ = "Integer32"
_Ds90LPortBreak_Object = MibTableColumn
ds90LPortBreak = _Ds90LPortBreak_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3, 1, 4),
    _Ds90LPortBreak_Type()
)
ds90LPortBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LPortBreak.setStatus("mandatory")


class _Ds90LPortTest_Type(Integer32):
    """Custom type ds90LPortTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ds90LPortTest_Type.__name__ = "Integer32"
_Ds90LPortTest_Object = MibTableColumn
ds90LPortTest = _Ds90LPortTest_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3, 1, 5),
    _Ds90LPortTest_Type()
)
ds90LPortTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LPortTest.setStatus("mandatory")


class _Ds90LPortAutoConfigure_Type(Integer32):
    """Custom type ds90LPortAutoConfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Ds90LPortAutoConfigure_Type.__name__ = "Integer32"
_Ds90LPortAutoConfigure_Object = MibTableColumn
ds90LPortAutoConfigure = _Ds90LPortAutoConfigure_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3, 1, 6),
    _Ds90LPortAutoConfigure_Type()
)
ds90LPortAutoConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LPortAutoConfigure.setStatus("mandatory")


class _Ds90LPortOnDemandLoading_Type(Integer32):
    """Custom type ds90LPortOnDemandLoading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Ds90LPortOnDemandLoading_Type.__name__ = "Integer32"
_Ds90LPortOnDemandLoading_Object = MibTableColumn
ds90LPortOnDemandLoading = _Ds90LPortOnDemandLoading_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 3, 1, 7),
    _Ds90LPortOnDemandLoading_Type()
)
ds90LPortOnDemandLoading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds90LPortOnDemandLoading.setStatus("mandatory")
_Ds90LSessionTable_Object = MibTable
ds90LSessionTable = _Ds90LSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 4)
)
if mibBuilder.loadTexts:
    ds90LSessionTable.setStatus("mandatory")
_Ds90LSessionEntry_Object = MibTableRow
ds90LSessionEntry = _Ds90LSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 4, 1)
)
ds90LSessionEntry.setIndexNames(
    (0, "DH90-MIB", "ds90LSessionPort"),
    (0, "DH90-MIB", "ds90LSessionIndex"),
)
if mibBuilder.loadTexts:
    ds90LSessionEntry.setStatus("mandatory")


class _Ds90LSessionPort_Type(Integer32):
    """Custom type ds90LSessionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1608),
    )


_Ds90LSessionPort_Type.__name__ = "Integer32"
_Ds90LSessionPort_Object = MibTableColumn
ds90LSessionPort = _Ds90LSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 4, 1, 1),
    _Ds90LSessionPort_Type()
)
ds90LSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LSessionPort.setStatus("mandatory")


class _Ds90LSessionIndex_Type(Integer32):
    """Custom type ds90LSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ds90LSessionIndex_Type.__name__ = "Integer32"
_Ds90LSessionIndex_Object = MibTableColumn
ds90LSessionIndex = _Ds90LSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 4, 1, 2),
    _Ds90LSessionIndex_Type()
)
ds90LSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LSessionIndex.setStatus("mandatory")


class _Ds90LSessionRemoteNode_Type(DisplayString):
    """Custom type ds90LSessionRemoteNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Ds90LSessionRemoteNode_Type.__name__ = "DisplayString"
_Ds90LSessionRemoteNode_Object = MibTableColumn
ds90LSessionRemoteNode = _Ds90LSessionRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 4, 1, 3),
    _Ds90LSessionRemoteNode_Type()
)
ds90LSessionRemoteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LSessionRemoteNode.setStatus("mandatory")


class _Ds90LSessionService_Type(DisplayString):
    """Custom type ds90LSessionService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Ds90LSessionService_Type.__name__ = "DisplayString"
_Ds90LSessionService_Object = MibTableColumn
ds90LSessionService = _Ds90LSessionService_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 4, 1, 4),
    _Ds90LSessionService_Type()
)
ds90LSessionService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LSessionService.setStatus("mandatory")


class _Ds90LSessionRemotePortId_Type(DisplayString):
    """Custom type ds90LSessionRemotePortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Ds90LSessionRemotePortId_Type.__name__ = "DisplayString"
_Ds90LSessionRemotePortId_Object = MibTableColumn
ds90LSessionRemotePortId = _Ds90LSessionRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 3, 4, 1, 5),
    _Ds90LSessionRemotePortId_Type()
)
ds90LSessionRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds90LSessionRemotePortId.setStatus("mandatory")
_Drpt90_ObjectIdentity = ObjectIdentity
drpt90 = _Drpt90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4)
)
_Drpt90PortTable_Object = MibTable
drpt90PortTable = _Drpt90PortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1)
)
if mibBuilder.loadTexts:
    drpt90PortTable.setStatus("mandatory")
_Drpt90PortEntry_Object = MibTableRow
drpt90PortEntry = _Drpt90PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1)
)
drpt90PortEntry.setIndexNames(
    (0, "DH90-MIB", "drpt90PortIndex"),
)
if mibBuilder.loadTexts:
    drpt90PortEntry.setStatus("mandatory")


class _Drpt90PortIndex_Type(Integer32):
    """Custom type drpt90PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1608),
    )


_Drpt90PortIndex_Type.__name__ = "Integer32"
_Drpt90PortIndex_Object = MibTableColumn
drpt90PortIndex = _Drpt90PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1, 1),
    _Drpt90PortIndex_Type()
)
drpt90PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drpt90PortIndex.setStatus("mandatory")


class _Drpt90PortName_Type(DisplayString):
    """Custom type drpt90PortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Drpt90PortName_Type.__name__ = "DisplayString"
_Drpt90PortName_Object = MibTableColumn
drpt90PortName = _Drpt90PortName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1, 2),
    _Drpt90PortName_Type()
)
drpt90PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drpt90PortName.setStatus("mandatory")


class _Drpt90PortAdminStatus_Type(Integer32):
    """Custom type drpt90PortAdminStatus based on Integer32"""
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


_Drpt90PortAdminStatus_Type.__name__ = "Integer32"
_Drpt90PortAdminStatus_Object = MibTableColumn
drpt90PortAdminStatus = _Drpt90PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1, 3),
    _Drpt90PortAdminStatus_Type()
)
drpt90PortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drpt90PortAdminStatus.setStatus("mandatory")


class _Drpt90PortState_Type(Integer32):
    """Custom type drpt90PortState based on Integer32"""
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
        *(("active", 4),
          ("autoPartitioned", 2),
          ("managementPartitioned", 3),
          ("unknown", 1))
    )


_Drpt90PortState_Type.__name__ = "Integer32"
_Drpt90PortState_Object = MibTableColumn
drpt90PortState = _Drpt90PortState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1, 4),
    _Drpt90PortState_Type()
)
drpt90PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drpt90PortState.setStatus("mandatory")


class _Drpt90PortType_Type(Integer32):
    """Custom type drpt90PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("thinWire", 3),
          ("twistedPair", 2),
          ("unknown", 1))
    )


_Drpt90PortType_Type.__name__ = "Integer32"
_Drpt90PortType_Object = MibTableColumn
drpt90PortType = _Drpt90PortType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1, 5),
    _Drpt90PortType_Type()
)
drpt90PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drpt90PortType.setStatus("mandatory")
_Drpt90PortPartitionCount_Type = Counter32
_Drpt90PortPartitionCount_Object = MibTableColumn
drpt90PortPartitionCount = _Drpt90PortPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1, 6),
    _Drpt90PortPartitionCount_Type()
)
drpt90PortPartitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drpt90PortPartitionCount.setStatus("mandatory")


class _Drpt90PortAutoPartitionReason_Type(Integer32):
    """Custom type drpt90PortAutoPartitionReason based on Integer32"""
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("excessiveCollisions", 4),
          ("excessiveCollisionsAndMgmtPart", 5),
          ("excessiveLength", 2),
          ("excessiveLengthAndMgmtPart", 3),
          ("jabber", 6),
          ("jabberAndMgmtPart", 7),
          ("managementPartitioned", 1),
          ("nocarrierLoopback", 8),
          ("nocarrierLoopbackAndMgmtPart", 9),
          ("notPartitioned", 0),
          ("transmitCarrierDropout", 10),
          ("transmitCarrierDropoutAndMgmtPart", 11))
    )


_Drpt90PortAutoPartitionReason_Type.__name__ = "Integer32"
_Drpt90PortAutoPartitionReason_Object = MibTableColumn
drpt90PortAutoPartitionReason = _Drpt90PortAutoPartitionReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1, 7),
    _Drpt90PortAutoPartitionReason_Type()
)
drpt90PortAutoPartitionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drpt90PortAutoPartitionReason.setStatus("mandatory")


class _Drpt90PortJamBits_Type(Integer32):
    """Custom type drpt90PortJamBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("jb128", 3),
          ("jb96", 2),
          ("unknown", 1))
    )


_Drpt90PortJamBits_Type.__name__ = "Integer32"
_Drpt90PortJamBits_Object = MibTableColumn
drpt90PortJamBits = _Drpt90PortJamBits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 1, 1, 8),
    _Drpt90PortJamBits_Type()
)
drpt90PortJamBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drpt90PortJamBits.setStatus("mandatory")
_Drpt90PortAddrTable_Object = MibTable
drpt90PortAddrTable = _Drpt90PortAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 2)
)
if mibBuilder.loadTexts:
    drpt90PortAddrTable.setStatus("mandatory")
_Drpt90PortAddrEntry_Object = MibTableRow
drpt90PortAddrEntry = _Drpt90PortAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 2, 1)
)
drpt90PortAddrEntry.setIndexNames(
    (0, "DH90-MIB", "drpt90PortPhyAddr"),
)
if mibBuilder.loadTexts:
    drpt90PortAddrEntry.setStatus("mandatory")
_Drpt90PortPhyAddr_Type = PhysAddress
_Drpt90PortPhyAddr_Object = MibTableColumn
drpt90PortPhyAddr = _Drpt90PortPhyAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 2, 1, 1),
    _Drpt90PortPhyAddr_Type()
)
drpt90PortPhyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drpt90PortPhyAddr.setStatus("mandatory")


class _Drpt90PortAddrIndex_Type(Integer32):
    """Custom type drpt90PortAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1608),
    )


_Drpt90PortAddrIndex_Type.__name__ = "Integer32"
_Drpt90PortAddrIndex_Object = MibTableColumn
drpt90PortAddrIndex = _Drpt90PortAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 4, 2, 1, 2),
    _Drpt90PortAddrIndex_Type()
)
drpt90PortAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drpt90PortAddrIndex.setStatus("mandatory")
_Db90ext_ObjectIdentity = ObjectIdentity
db90ext = _Db90ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5)
)
_Db90system_ObjectIdentity = ObjectIdentity
db90system = _Db90system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 1)
)
_DbSysChar_ObjectIdentity = ObjectIdentity
dbSysChar = _DbSysChar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 1, 1)
)
_DbSysRomVersion_Type = Integer32
_DbSysRomVersion_Object = MibScalar
dbSysRomVersion = _DbSysRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 1, 1, 1),
    _DbSysRomVersion_Type()
)
dbSysRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbSysRomVersion.setStatus("mandatory")


class _DbSysInitSwitch_Type(Integer32):
    """Custom type dbSysInitSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2),
          ("resetToFactory", 3))
    )


_DbSysInitSwitch_Type.__name__ = "Integer32"
_DbSysInitSwitch_Object = MibScalar
dbSysInitSwitch = _DbSysInitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 1, 1, 2),
    _DbSysInitSwitch_Type()
)
dbSysInitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbSysInitSwitch.setStatus("mandatory")
_DbSysStatus_ObjectIdentity = ObjectIdentity
dbSysStatus = _DbSysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 1, 2)
)


class _DbSysDeviceState_Type(Integer32):
    """Custom type dbSysDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("init", 1),
          ("operate", 2))
    )


_DbSysDeviceState_Type.__name__ = "Integer32"
_DbSysDeviceState_Object = MibScalar
dbSysDeviceState = _DbSysDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 1, 2, 1),
    _DbSysDeviceState_Type()
)
dbSysDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbSysDeviceState.setStatus("mandatory")


class _DbSysNvramFailed_Type(Integer32):
    """Custom type dbSysNvramFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DbSysNvramFailed_Type.__name__ = "Integer32"
_DbSysNvramFailed_Object = MibScalar
dbSysNvramFailed = _DbSysNvramFailed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 1, 2, 2),
    _DbSysNvramFailed_Type()
)
dbSysNvramFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbSysNvramFailed.setStatus("mandatory")
_Db90interfaces_ObjectIdentity = ObjectIdentity
db90interfaces = _Db90interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 2)
)
_DbIfTable_Object = MibTable
dbIfTable = _DbIfTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    dbIfTable.setStatus("mandatory")
_DbIfEntry_Object = MibTableRow
dbIfEntry = _DbIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 2, 1, 1)
)
dbIfEntry.setIndexNames(
    (0, "DH90-MIB", "dbIfIndex"),
)
if mibBuilder.loadTexts:
    dbIfEntry.setStatus("mandatory")


class _DbIfIndex_Type(Integer32):
    """Custom type dbIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_DbIfIndex_Type.__name__ = "Integer32"
_DbIfIndex_Object = MibTableColumn
dbIfIndex = _DbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 2, 1, 1, 1),
    _DbIfIndex_Type()
)
dbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbIfIndex.setStatus("mandatory")
_DbIfBadFramesReceived_Type = Counter32
_DbIfBadFramesReceived_Object = MibTableColumn
dbIfBadFramesReceived = _DbIfBadFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 2, 1, 1, 2),
    _DbIfBadFramesReceived_Type()
)
dbIfBadFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbIfBadFramesReceived.setStatus("mandatory")
_DbIfTransmitFramesError_Type = Counter32
_DbIfTransmitFramesError_Object = MibTableColumn
dbIfTransmitFramesError = _DbIfTransmitFramesError_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 2, 1, 1, 3),
    _DbIfTransmitFramesError_Type()
)
dbIfTransmitFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbIfTransmitFramesError.setStatus("mandatory")
_Db90bridge_ObjectIdentity = ObjectIdentity
db90bridge = _Db90bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3)
)
_Db90Char_ObjectIdentity = ObjectIdentity
db90Char = _Db90Char_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 1)
)
_Db90LB100SpanningTreeVer_Type = Integer32
_Db90LB100SpanningTreeVer_Object = MibScalar
db90LB100SpanningTreeVer = _Db90LB100SpanningTreeVer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 1, 1),
    _Db90LB100SpanningTreeVer_Type()
)
db90LB100SpanningTreeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90LB100SpanningTreeVer.setStatus("mandatory")
_Db90802SpanningTreeVer_Type = Integer32
_Db90802SpanningTreeVer_Object = MibScalar
db90802SpanningTreeVer = _Db90802SpanningTreeVer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 1, 2),
    _Db90802SpanningTreeVer_Type()
)
db90802SpanningTreeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90802SpanningTreeVer.setStatus("mandatory")
_Db90MaxForwardingDBEntries_Type = Integer32
_Db90MaxForwardingDBEntries_Object = MibScalar
db90MaxForwardingDBEntries = _Db90MaxForwardingDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 1, 3),
    _Db90MaxForwardingDBEntries_Type()
)
db90MaxForwardingDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90MaxForwardingDBEntries.setStatus("mandatory")
_Db90MaxNVForwardingDBEntries_Type = Integer32
_Db90MaxNVForwardingDBEntries_Object = MibScalar
db90MaxNVForwardingDBEntries = _Db90MaxNVForwardingDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 1, 4),
    _Db90MaxNVForwardingDBEntries_Type()
)
db90MaxNVForwardingDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90MaxNVForwardingDBEntries.setStatus("mandatory")
_Db90MaxProtocolDBEntries_Type = Integer32
_Db90MaxProtocolDBEntries_Object = MibScalar
db90MaxProtocolDBEntries = _Db90MaxProtocolDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 1, 5),
    _Db90MaxProtocolDBEntries_Type()
)
db90MaxProtocolDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90MaxProtocolDBEntries.setStatus("mandatory")
_Db90MaxNVProtocolDBEntries_Type = Integer32
_Db90MaxNVProtocolDBEntries_Object = MibScalar
db90MaxNVProtocolDBEntries = _Db90MaxNVProtocolDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 1, 6),
    _Db90MaxNVProtocolDBEntries_Type()
)
db90MaxNVProtocolDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90MaxNVProtocolDBEntries.setStatus("mandatory")
_Db90Stat_ObjectIdentity = ObjectIdentity
db90Stat = _Db90Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 2)
)
_Db90CurrProtocolDBEntries_Type = Integer32
_Db90CurrProtocolDBEntries_Object = MibScalar
db90CurrProtocolDBEntries = _Db90CurrProtocolDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 2, 1),
    _Db90CurrProtocolDBEntries_Type()
)
db90CurrProtocolDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90CurrProtocolDBEntries.setStatus("mandatory")
_Db90CurrNVProtocolDBEntries_Type = Integer32
_Db90CurrNVProtocolDBEntries_Object = MibScalar
db90CurrNVProtocolDBEntries = _Db90CurrNVProtocolDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 2, 2),
    _Db90CurrNVProtocolDBEntries_Type()
)
db90CurrNVProtocolDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90CurrNVProtocolDBEntries.setStatus("mandatory")


class _Db90MgmtHeardPort_Type(Integer32):
    """Custom type db90MgmtHeardPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backbone", 1),
          ("workgroup", 2))
    )


_Db90MgmtHeardPort_Type.__name__ = "Integer32"
_Db90MgmtHeardPort_Object = MibScalar
db90MgmtHeardPort = _Db90MgmtHeardPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 2, 3),
    _Db90MgmtHeardPort_Type()
)
db90MgmtHeardPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90MgmtHeardPort.setStatus("mandatory")


class _Db90LB100BeingPolled_Type(OctetString):
    """Custom type db90LB100BeingPolled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Db90LB100BeingPolled_Type.__name__ = "OctetString"
_Db90LB100BeingPolled_Object = MibScalar
db90LB100BeingPolled = _Db90LB100BeingPolled_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 2, 4),
    _Db90LB100BeingPolled_Type()
)
db90LB100BeingPolled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90LB100BeingPolled.setStatus("mandatory")
_Db90TimeSinceLastHello_Type = Integer32
_Db90TimeSinceLastHello_Object = MibScalar
db90TimeSinceLastHello = _Db90TimeSinceLastHello_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 2, 5),
    _Db90TimeSinceLastHello_Type()
)
db90TimeSinceLastHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90TimeSinceLastHello.setStatus("mandatory")


class _Db90HubManagement_Type(Integer32):
    """Custom type db90HubManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Db90HubManagement_Type.__name__ = "Integer32"
_Db90HubManagement_Object = MibScalar
db90HubManagement = _Db90HubManagement_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 2, 6),
    _Db90HubManagement_Type()
)
db90HubManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    db90HubManagement.setStatus("mandatory")
_Db90CurrFdbEntries_Type = Counter32
_Db90CurrFdbEntries_Object = MibScalar
db90CurrFdbEntries = _Db90CurrFdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 2, 7),
    _Db90CurrFdbEntries_Type()
)
db90CurrFdbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90CurrFdbEntries.setStatus("mandatory")
_Db90Coun_ObjectIdentity = ObjectIdentity
db90Coun = _Db90Coun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 3)
)
_Db90SpanningTreeModeChanges_Type = Counter32
_Db90SpanningTreeModeChanges_Object = MibScalar
db90SpanningTreeModeChanges = _Db90SpanningTreeModeChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 3, 1),
    _Db90SpanningTreeModeChanges_Type()
)
db90SpanningTreeModeChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90SpanningTreeModeChanges.setStatus("mandatory")
_Db90Span_ObjectIdentity = ObjectIdentity
db90Span = _Db90Span_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4)
)
_Db90BestRootAge_Type = Integer32
_Db90BestRootAge_Object = MibScalar
db90BestRootAge = _Db90BestRootAge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 1),
    _Db90BestRootAge_Type()
)
db90BestRootAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90BestRootAge.setStatus("mandatory")


class _Db90TopologyChangeFlag_Type(Integer32):
    """Custom type db90TopologyChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Db90TopologyChangeFlag_Type.__name__ = "Integer32"
_Db90TopologyChangeFlag_Object = MibScalar
db90TopologyChangeFlag = _Db90TopologyChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 2),
    _Db90TopologyChangeFlag_Type()
)
db90TopologyChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90TopologyChangeFlag.setStatus("mandatory")


class _Db90TellParentFlag_Type(Integer32):
    """Custom type db90TellParentFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Db90TellParentFlag_Type.__name__ = "Integer32"
_Db90TellParentFlag_Object = MibScalar
db90TellParentFlag = _Db90TellParentFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 3),
    _Db90TellParentFlag_Type()
)
db90TellParentFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90TellParentFlag.setStatus("mandatory")
_Db90ForwardingDBShortAgingTime_Type = Integer32
_Db90ForwardingDBShortAgingTime_Object = MibScalar
db90ForwardingDBShortAgingTime = _Db90ForwardingDBShortAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 4),
    _Db90ForwardingDBShortAgingTime_Type()
)
db90ForwardingDBShortAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90ForwardingDBShortAgingTime.setStatus("mandatory")
_Db90BadHelloLimit_Type = Integer32
_Db90BadHelloLimit_Object = MibScalar
db90BadHelloLimit = _Db90BadHelloLimit_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 5),
    _Db90BadHelloLimit_Type()
)
db90BadHelloLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90BadHelloLimit.setStatus("mandatory")
_Db90BadHelloResetTimer_Type = Integer32
_Db90BadHelloResetTimer_Object = MibScalar
db90BadHelloResetTimer = _Db90BadHelloResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 6),
    _Db90BadHelloResetTimer_Type()
)
db90BadHelloResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    db90BadHelloResetTimer.setStatus("mandatory")
_Db90NoFrameInterval_Type = Integer32
_Db90NoFrameInterval_Object = MibScalar
db90NoFrameInterval = _Db90NoFrameInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 7),
    _Db90NoFrameInterval_Type()
)
db90NoFrameInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90NoFrameInterval.setStatus("mandatory")
_Db90LB100PollTime_Type = Integer32
_Db90LB100PollTime_Object = MibScalar
db90LB100PollTime = _Db90LB100PollTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 8),
    _Db90LB100PollTime_Type()
)
db90LB100PollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90LB100PollTime.setStatus("mandatory")
_Db90LB100ResponseTimeout_Type = Integer32
_Db90LB100ResponseTimeout_Object = MibScalar
db90LB100ResponseTimeout = _Db90LB100ResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 9),
    _Db90LB100ResponseTimeout_Type()
)
db90LB100ResponseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90LB100ResponseTimeout.setStatus("mandatory")


class _Db90LB100SpanningTreeCompat_Type(Integer32):
    """Custom type db90LB100SpanningTreeCompat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoSelect", 1),
          ("ieee802", 2))
    )


_Db90LB100SpanningTreeCompat_Type.__name__ = "Integer32"
_Db90LB100SpanningTreeCompat_Object = MibScalar
db90LB100SpanningTreeCompat = _Db90LB100SpanningTreeCompat_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 4, 10),
    _Db90LB100SpanningTreeCompat_Type()
)
db90LB100SpanningTreeCompat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90LB100SpanningTreeCompat.setStatus("mandatory")
_Db90PortInterfaces_ObjectIdentity = ObjectIdentity
db90PortInterfaces = _Db90PortInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5)
)
_Db90IfTable_Object = MibTable
db90IfTable = _Db90IfTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 1)
)
if mibBuilder.loadTexts:
    db90IfTable.setStatus("mandatory")
_Db90IfEntry_Object = MibTableRow
db90IfEntry = _Db90IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 1, 1)
)
db90IfEntry.setIndexNames(
    (0, "DH90-MIB", "db90IfIndex"),
)
if mibBuilder.loadTexts:
    db90IfEntry.setStatus("mandatory")


class _Db90IfIndex_Type(Integer32):
    """Custom type db90IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_Db90IfIndex_Type.__name__ = "Integer32"
_Db90IfIndex_Object = MibTableColumn
db90IfIndex = _Db90IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 1, 1, 1),
    _Db90IfIndex_Type()
)
db90IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfIndex.setStatus("mandatory")
_Db90IfDeviceFramesReceived_Type = Counter32
_Db90IfDeviceFramesReceived_Object = MibTableColumn
db90IfDeviceFramesReceived = _Db90IfDeviceFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 1, 1, 2),
    _Db90IfDeviceFramesReceived_Type()
)
db90IfDeviceFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfDeviceFramesReceived.setStatus("mandatory")
_Db90IfBadHelloLimitExceeded_Type = Counter32
_Db90IfBadHelloLimitExceeded_Object = MibTableColumn
db90IfBadHelloLimitExceeded = _Db90IfBadHelloLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 1, 1, 3),
    _Db90IfBadHelloLimitExceeded_Type()
)
db90IfBadHelloLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfBadHelloLimitExceeded.setStatus("mandatory")
_Db90IfEtherTable_Object = MibTable
db90IfEtherTable = _Db90IfEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 2)
)
if mibBuilder.loadTexts:
    db90IfEtherTable.setStatus("optional")
_Db90IfEtherEntry_Object = MibTableRow
db90IfEtherEntry = _Db90IfEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 2, 1)
)
db90IfEtherEntry.setIndexNames(
    (0, "DH90-MIB", "db90IfIndex"),
)
if mibBuilder.loadTexts:
    db90IfEtherEntry.setStatus("mandatory")


class _Db90IfEthIndex_Type(Integer32):
    """Custom type db90IfEthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Db90IfEthIndex_Type.__name__ = "Integer32"
_Db90IfEthIndex_Object = MibTableColumn
db90IfEthIndex = _Db90IfEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 2, 1, 1),
    _Db90IfEthIndex_Type()
)
db90IfEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfEthIndex.setStatus("mandatory")
_Db90IfEthFramingError_Type = Counter32
_Db90IfEthFramingError_Object = MibTableColumn
db90IfEthFramingError = _Db90IfEthFramingError_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 2, 1, 2),
    _Db90IfEthFramingError_Type()
)
db90IfEthFramingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfEthFramingError.setStatus("mandatory")
_Db90IfEthCarrierLoss_Type = Counter32
_Db90IfEthCarrierLoss_Object = MibTableColumn
db90IfEthCarrierLoss = _Db90IfEthCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 2, 1, 3),
    _Db90IfEthCarrierLoss_Type()
)
db90IfEthCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfEthCarrierLoss.setStatus("mandatory")
_Db90IfEthCollisionLimitExceeded_Type = Counter32
_Db90IfEthCollisionLimitExceeded_Object = MibTableColumn
db90IfEthCollisionLimitExceeded = _Db90IfEthCollisionLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 2, 1, 4),
    _Db90IfEthCollisionLimitExceeded_Type()
)
db90IfEthCollisionLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfEthCollisionLimitExceeded.setStatus("mandatory")
_Db90IfSpanTable_Object = MibTable
db90IfSpanTable = _Db90IfSpanTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 3)
)
if mibBuilder.loadTexts:
    db90IfSpanTable.setStatus("mandatory")
_Db90IfSpanEntry_Object = MibTableRow
db90IfSpanEntry = _Db90IfSpanEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 3, 1)
)
db90IfSpanEntry.setIndexNames(
    (0, "DH90-MIB", "db90IfIndex"),
)
if mibBuilder.loadTexts:
    db90IfSpanEntry.setStatus("mandatory")


class _Db90IfSpIndex_Type(Integer32):
    """Custom type db90IfSpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_Db90IfSpIndex_Type.__name__ = "Integer32"
_Db90IfSpIndex_Object = MibTableColumn
db90IfSpIndex = _Db90IfSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 3, 1, 1),
    _Db90IfSpIndex_Type()
)
db90IfSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfSpIndex.setStatus("mandatory")
_Db90IfSpDesigRootAge_Type = Integer32
_Db90IfSpDesigRootAge_Object = MibTableColumn
db90IfSpDesigRootAge = _Db90IfSpDesigRootAge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 3, 1, 2),
    _Db90IfSpDesigRootAge_Type()
)
db90IfSpDesigRootAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfSpDesigRootAge.setStatus("mandatory")
_Db90IfSpForwardDelayTimer_Type = Integer32
_Db90IfSpForwardDelayTimer_Object = MibTableColumn
db90IfSpForwardDelayTimer = _Db90IfSpForwardDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 3, 1, 3),
    _Db90IfSpForwardDelayTimer_Type()
)
db90IfSpForwardDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfSpForwardDelayTimer.setStatus("mandatory")
_Db90IfSpBadHelloCount_Type = Counter32
_Db90IfSpBadHelloCount_Object = MibTableColumn
db90IfSpBadHelloCount = _Db90IfSpBadHelloCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 3, 1, 4),
    _Db90IfSpBadHelloCount_Type()
)
db90IfSpBadHelloCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfSpBadHelloCount.setStatus("mandatory")


class _Db90IfSpTopologyChangeAckFlag_Type(Integer32):
    """Custom type db90IfSpTopologyChangeAckFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Db90IfSpTopologyChangeAckFlag_Type.__name__ = "Integer32"
_Db90IfSpTopologyChangeAckFlag_Object = MibTableColumn
db90IfSpTopologyChangeAckFlag = _Db90IfSpTopologyChangeAckFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 5, 3, 1, 5),
    _Db90IfSpTopologyChangeAckFlag_Type()
)
db90IfSpTopologyChangeAckFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90IfSpTopologyChangeAckFlag.setStatus("mandatory")
_Db90ProtoFilt_ObjectIdentity = ObjectIdentity
db90ProtoFilt = _Db90ProtoFilt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6)
)


class _Db90ProtoFilterOther_Type(Integer32):
    """Custom type db90ProtoFilterOther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("forward", 1))
    )


_Db90ProtoFilterOther_Type.__name__ = "Integer32"
_Db90ProtoFilterOther_Object = MibScalar
db90ProtoFilterOther = _Db90ProtoFilterOther_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6, 1),
    _Db90ProtoFilterOther_Type()
)
db90ProtoFilterOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    db90ProtoFilterOther.setStatus("mandatory")
_Db90ProtoFilterTable_Object = MibTable
db90ProtoFilterTable = _Db90ProtoFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6, 2)
)
if mibBuilder.loadTexts:
    db90ProtoFilterTable.setStatus("mandatory")
_Db90ProtoFilterEntry_Object = MibTableRow
db90ProtoFilterEntry = _Db90ProtoFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6, 2, 1)
)
db90ProtoFilterEntry.setIndexNames(
    (0, "DH90-MIB", "db90ProtoFilterProtocol"),
)
if mibBuilder.loadTexts:
    db90ProtoFilterEntry.setStatus("mandatory")


class _Db90ProtoFilterProtocol_Type(OctetString):
    """Custom type db90ProtoFilterProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 5),
    )


_Db90ProtoFilterProtocol_Type.__name__ = "OctetString"
_Db90ProtoFilterProtocol_Object = MibTableColumn
db90ProtoFilterProtocol = _Db90ProtoFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6, 2, 1, 1),
    _Db90ProtoFilterProtocol_Type()
)
db90ProtoFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    db90ProtoFilterProtocol.setStatus("mandatory")


class _Db90ProtoFilterType_Type(Integer32):
    """Custom type db90ProtoFilterType based on Integer32"""
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
        *(("ethernet", 3),
          ("invalid", 2),
          ("snap-sap", 4),
          ("unknown", 1))
    )


_Db90ProtoFilterType_Type.__name__ = "Integer32"
_Db90ProtoFilterType_Object = MibTableColumn
db90ProtoFilterType = _Db90ProtoFilterType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6, 2, 1, 2),
    _Db90ProtoFilterType_Type()
)
db90ProtoFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    db90ProtoFilterType.setStatus("mandatory")


class _Db90ProtoFilterStatus_Type(Integer32):
    """Custom type db90ProtoFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("forward", 1))
    )


_Db90ProtoFilterStatus_Type.__name__ = "Integer32"
_Db90ProtoFilterStatus_Object = MibTableColumn
db90ProtoFilterStatus = _Db90ProtoFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6, 2, 1, 3),
    _Db90ProtoFilterStatus_Type()
)
db90ProtoFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    db90ProtoFilterStatus.setStatus("mandatory")


class _Db90ProtoFilterMulticastFlag_Type(Integer32):
    """Custom type db90ProtoFilterMulticastFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allFrames", 1),
          ("multicastOnly", 2))
    )


_Db90ProtoFilterMulticastFlag_Type.__name__ = "Integer32"
_Db90ProtoFilterMulticastFlag_Object = MibTableColumn
db90ProtoFilterMulticastFlag = _Db90ProtoFilterMulticastFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6, 2, 1, 4),
    _Db90ProtoFilterMulticastFlag_Type()
)
db90ProtoFilterMulticastFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    db90ProtoFilterMulticastFlag.setStatus("mandatory")


class _Db90ProtoFilterPortMask_Type(Integer32):
    """Custom type db90ProtoFilterPortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allPorts", 3),
          ("backbone", 1),
          ("workGroup", 2))
    )


_Db90ProtoFilterPortMask_Type.__name__ = "Integer32"
_Db90ProtoFilterPortMask_Object = MibTableColumn
db90ProtoFilterPortMask = _Db90ProtoFilterPortMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 3, 5, 3, 6, 2, 1, 5),
    _Db90ProtoFilterPortMask_Type()
)
db90ProtoFilterPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    db90ProtoFilterPortMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DH90-MIB",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decExp": decExp,
       "dh90": dh90,
       "dh90Type": dh90Type,
       "dh90Backplane": dh90Backplane,
       "dh90LastChange": dh90LastChange,
       "dh90NumberSlots": dh90NumberSlots,
       "dh90SlotTable": dh90SlotTable,
       "dh90SlotEntry": dh90SlotEntry,
       "dh90SlotIndex": dh90SlotIndex,
       "dh90SlotModuleType": dh90SlotModuleType,
       "dh90SlotModuleName": dh90SlotModuleName,
       "dh90SlotModuleVersion": dh90SlotModuleVersion,
       "dh90SlotCounterTime": dh90SlotCounterTime,
       "dh90SlotIfBase": dh90SlotIfBase,
       "dh90SlotIfNumber": dh90SlotIfNumber,
       "dh90SlotPhysicalAddress": dh90SlotPhysicalAddress,
       "dh90SlotNumberOfPorts": dh90SlotNumberOfPorts,
       "dh90SlotPassword": dh90SlotPassword,
       "dh90SlotNewPassword": dh90SlotNewPassword,
       "dh90SlotPolling": dh90SlotPolling,
       "dh90SlotPrimarySpecific": dh90SlotPrimarySpecific,
       "dh90SlotSecondarySpecific": dh90SlotSecondarySpecific,
       "dh90TrapAddressTable": dh90TrapAddressTable,
       "dh90TrapEntry": dh90TrapEntry,
       "dh90TrapAddress": dh90TrapAddress,
       "da90": da90,
       "da90FlashErasures": da90FlashErasures,
       "da90Maintenance": da90Maintenance,
       "da90CommunityNumber": da90CommunityNumber,
       "da90CommunityTable": da90CommunityTable,
       "da90CommunityEntry": da90CommunityEntry,
       "da90CommunityIndex": da90CommunityIndex,
       "da90CommunityType": da90CommunityType,
       "da90CommunityROString": da90CommunityROString,
       "da90CommunityRWString": da90CommunityRWString,
       "da90CommunityTrapString": da90CommunityTrapString,
       "ds90L": ds90L,
       "ds90LNumberModules": ds90LNumberModules,
       "ds90LModuleTable": ds90LModuleTable,
       "ds90LModuleEntry": ds90LModuleEntry,
       "ds90LSlotIndex": ds90LSlotIndex,
       "ds90LDot3StatsDeferredTransmissions": ds90LDot3StatsDeferredTransmissions,
       "ds90LDot3StatsSingleCollisionFrames": ds90LDot3StatsSingleCollisionFrames,
       "ds90LDot3StatsMultipleCollsionFrames": ds90LDot3StatsMultipleCollsionFrames,
       "ds90LEnetDataOverruns": ds90LEnetDataOverruns,
       "ds90LLatCircMsgsIns": ds90LLatCircMsgsIns,
       "ds90LLatCircMsgsOuts": ds90LLatCircMsgsOuts,
       "ds90LLatSessSolicitAccepts": ds90LLatSessSolicitAccepts,
       "ds90LLatSessSolicitRejects": ds90LLatSessSolicitRejects,
       "ds90LLatCircDuplsMsgs": ds90LLatCircDuplsMsgs,
       "ds90LLatCircMsgRetransmits": ds90LLatCircMsgRetransmits,
       "ds90LLatSessIllegalSlots": ds90LLatSessIllegalSlots,
       "ds90LIllegalMulticastRcvs": ds90LIllegalMulticastRcvs,
       "ds90LLatCircKeepAlive": ds90LLatCircKeepAlive,
       "ds90LLatCircRetransmitLimit": ds90LLatCircRetransmitLimit,
       "ds90LLatCircInvalidMsgs": ds90LLatCircInvalidMsgs,
       "ds90LAuthorizeMode": ds90LAuthorizeMode,
       "ds90LMaintenance": ds90LMaintenance,
       "ds90LPrompt": ds90LPrompt,
       "ds90LPortTable": ds90LPortTable,
       "ds90LPortEntry": ds90LPortEntry,
       "ds90LPortIndex": ds90LPortIndex,
       "ds90LPortRemoteModification": ds90LPortRemoteModification,
       "ds90LPortType": ds90LPortType,
       "ds90LPortBreak": ds90LPortBreak,
       "ds90LPortTest": ds90LPortTest,
       "ds90LPortAutoConfigure": ds90LPortAutoConfigure,
       "ds90LPortOnDemandLoading": ds90LPortOnDemandLoading,
       "ds90LSessionTable": ds90LSessionTable,
       "ds90LSessionEntry": ds90LSessionEntry,
       "ds90LSessionPort": ds90LSessionPort,
       "ds90LSessionIndex": ds90LSessionIndex,
       "ds90LSessionRemoteNode": ds90LSessionRemoteNode,
       "ds90LSessionService": ds90LSessionService,
       "ds90LSessionRemotePortId": ds90LSessionRemotePortId,
       "drpt90": drpt90,
       "drpt90PortTable": drpt90PortTable,
       "drpt90PortEntry": drpt90PortEntry,
       "drpt90PortIndex": drpt90PortIndex,
       "drpt90PortName": drpt90PortName,
       "drpt90PortAdminStatus": drpt90PortAdminStatus,
       "drpt90PortState": drpt90PortState,
       "drpt90PortType": drpt90PortType,
       "drpt90PortPartitionCount": drpt90PortPartitionCount,
       "drpt90PortAutoPartitionReason": drpt90PortAutoPartitionReason,
       "drpt90PortJamBits": drpt90PortJamBits,
       "drpt90PortAddrTable": drpt90PortAddrTable,
       "drpt90PortAddrEntry": drpt90PortAddrEntry,
       "drpt90PortPhyAddr": drpt90PortPhyAddr,
       "drpt90PortAddrIndex": drpt90PortAddrIndex,
       "db90ext": db90ext,
       "db90system": db90system,
       "dbSysChar": dbSysChar,
       "dbSysRomVersion": dbSysRomVersion,
       "dbSysInitSwitch": dbSysInitSwitch,
       "dbSysStatus": dbSysStatus,
       "dbSysDeviceState": dbSysDeviceState,
       "dbSysNvramFailed": dbSysNvramFailed,
       "db90interfaces": db90interfaces,
       "dbIfTable": dbIfTable,
       "dbIfEntry": dbIfEntry,
       "dbIfIndex": dbIfIndex,
       "dbIfBadFramesReceived": dbIfBadFramesReceived,
       "dbIfTransmitFramesError": dbIfTransmitFramesError,
       "db90bridge": db90bridge,
       "db90Char": db90Char,
       "db90LB100SpanningTreeVer": db90LB100SpanningTreeVer,
       "db90802SpanningTreeVer": db90802SpanningTreeVer,
       "db90MaxForwardingDBEntries": db90MaxForwardingDBEntries,
       "db90MaxNVForwardingDBEntries": db90MaxNVForwardingDBEntries,
       "db90MaxProtocolDBEntries": db90MaxProtocolDBEntries,
       "db90MaxNVProtocolDBEntries": db90MaxNVProtocolDBEntries,
       "db90Stat": db90Stat,
       "db90CurrProtocolDBEntries": db90CurrProtocolDBEntries,
       "db90CurrNVProtocolDBEntries": db90CurrNVProtocolDBEntries,
       "db90MgmtHeardPort": db90MgmtHeardPort,
       "db90LB100BeingPolled": db90LB100BeingPolled,
       "db90TimeSinceLastHello": db90TimeSinceLastHello,
       "db90HubManagement": db90HubManagement,
       "db90CurrFdbEntries": db90CurrFdbEntries,
       "db90Coun": db90Coun,
       "db90SpanningTreeModeChanges": db90SpanningTreeModeChanges,
       "db90Span": db90Span,
       "db90BestRootAge": db90BestRootAge,
       "db90TopologyChangeFlag": db90TopologyChangeFlag,
       "db90TellParentFlag": db90TellParentFlag,
       "db90ForwardingDBShortAgingTime": db90ForwardingDBShortAgingTime,
       "db90BadHelloLimit": db90BadHelloLimit,
       "db90BadHelloResetTimer": db90BadHelloResetTimer,
       "db90NoFrameInterval": db90NoFrameInterval,
       "db90LB100PollTime": db90LB100PollTime,
       "db90LB100ResponseTimeout": db90LB100ResponseTimeout,
       "db90LB100SpanningTreeCompat": db90LB100SpanningTreeCompat,
       "db90PortInterfaces": db90PortInterfaces,
       "db90IfTable": db90IfTable,
       "db90IfEntry": db90IfEntry,
       "db90IfIndex": db90IfIndex,
       "db90IfDeviceFramesReceived": db90IfDeviceFramesReceived,
       "db90IfBadHelloLimitExceeded": db90IfBadHelloLimitExceeded,
       "db90IfEtherTable": db90IfEtherTable,
       "db90IfEtherEntry": db90IfEtherEntry,
       "db90IfEthIndex": db90IfEthIndex,
       "db90IfEthFramingError": db90IfEthFramingError,
       "db90IfEthCarrierLoss": db90IfEthCarrierLoss,
       "db90IfEthCollisionLimitExceeded": db90IfEthCollisionLimitExceeded,
       "db90IfSpanTable": db90IfSpanTable,
       "db90IfSpanEntry": db90IfSpanEntry,
       "db90IfSpIndex": db90IfSpIndex,
       "db90IfSpDesigRootAge": db90IfSpDesigRootAge,
       "db90IfSpForwardDelayTimer": db90IfSpForwardDelayTimer,
       "db90IfSpBadHelloCount": db90IfSpBadHelloCount,
       "db90IfSpTopologyChangeAckFlag": db90IfSpTopologyChangeAckFlag,
       "db90ProtoFilt": db90ProtoFilt,
       "db90ProtoFilterOther": db90ProtoFilterOther,
       "db90ProtoFilterTable": db90ProtoFilterTable,
       "db90ProtoFilterEntry": db90ProtoFilterEntry,
       "db90ProtoFilterProtocol": db90ProtoFilterProtocol,
       "db90ProtoFilterType": db90ProtoFilterType,
       "db90ProtoFilterStatus": db90ProtoFilterStatus,
       "db90ProtoFilterMulticastFlag": db90ProtoFilterMulticastFlag,
       "db90ProtoFilterPortMask": db90ProtoFilterPortMask}
)
