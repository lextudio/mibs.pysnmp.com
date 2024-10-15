# SNMP MIB module (DEC-ELAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEC-ELAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:34 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_Sysobjid_ObjectIdentity = ObjectIdentity
sysobjid = _Sysobjid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15)
)
_Bridges_ObjectIdentity = ObjectIdentity
bridges = _Bridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3)
)
_Gigaswitch_ObjectIdentity = ObjectIdentity
gigaswitch = _Gigaswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3)
)
_MinimumGIGAswitchMIBVersionSupported_Type = Integer32
_MinimumGIGAswitchMIBVersionSupported_Object = MibScalar
minimumGIGAswitchMIBVersionSupported = _MinimumGIGAswitchMIBVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 1),
    _MinimumGIGAswitchMIBVersionSupported_Type()
)
minimumGIGAswitchMIBVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minimumGIGAswitchMIBVersionSupported.setStatus("mandatory")
_MaximumGIGAswitchMIBVersionSupported_Type = Integer32
_MaximumGIGAswitchMIBVersionSupported_Object = MibScalar
maximumGIGAswitchMIBVersionSupported = _MaximumGIGAswitchMIBVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 2),
    _MaximumGIGAswitchMIBVersionSupported_Type()
)
maximumGIGAswitchMIBVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumGIGAswitchMIBVersionSupported.setStatus("mandatory")
_Gigaversion1_ObjectIdentity = ObjectIdentity
gigaversion1 = _Gigaversion1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3)
)
_GigaBox_ObjectIdentity = ObjectIdentity
gigaBox = _GigaBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1)
)
_ClockCard_ObjectIdentity = ObjectIdentity
clockCard = _ClockCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 1)
)
_MgmtMemoryAvail_Type = Integer32
_MgmtMemoryAvail_Object = MibScalar
mgmtMemoryAvail = _MgmtMemoryAvail_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 1, 1),
    _MgmtMemoryAvail_Type()
)
mgmtMemoryAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtMemoryAvail.setStatus("mandatory")


class _MgmtMemoryAction_Type(Integer32):
    """Custom type mgmtMemoryAction based on Integer32"""
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
        *(("clearAndLock", 4),
          ("locked", 5),
          ("other", 1),
          ("rewrite", 2),
          ("rewriting", 3))
    )


_MgmtMemoryAction_Type.__name__ = "Integer32"
_MgmtMemoryAction_Object = MibScalar
mgmtMemoryAction = _MgmtMemoryAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 1, 2),
    _MgmtMemoryAction_Type()
)
mgmtMemoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtMemoryAction.setStatus("mandatory")
_MgmtMemoryTable_Object = MibTable
mgmtMemoryTable = _MgmtMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mgmtMemoryTable.setStatus("mandatory")
_MgmtMemoryEntry_Object = MibTableRow
mgmtMemoryEntry = _MgmtMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 1, 3, 1)
)
mgmtMemoryEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "mgmtMemoryIndex"),
)
if mibBuilder.loadTexts:
    mgmtMemoryEntry.setStatus("mandatory")
_MgmtMemoryIndex_Type = Integer32
_MgmtMemoryIndex_Object = MibTableColumn
mgmtMemoryIndex = _MgmtMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 1, 3, 1, 1),
    _MgmtMemoryIndex_Type()
)
mgmtMemoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtMemoryIndex.setStatus("mandatory")


class _MgmtMemoryData_Type(OctetString):
    """Custom type mgmtMemoryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MgmtMemoryData_Type.__name__ = "OctetString"
_MgmtMemoryData_Object = MibTableColumn
mgmtMemoryData = _MgmtMemoryData_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 1, 3, 1, 2),
    _MgmtMemoryData_Type()
)
mgmtMemoryData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtMemoryData.setStatus("mandatory")
_Psc_ObjectIdentity = ObjectIdentity
psc = _Psc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2)
)


class _PscStatus_Type(Integer32):
    """Custom type pscStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2))
    )


_PscStatus_Type.__name__ = "Integer32"
_PscStatus_Object = MibScalar
pscStatus = _PscStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2, 1),
    _PscStatus_Type()
)
pscStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscStatus.setStatus("mandatory")
_PscFwRev_Type = DisplayString
_PscFwRev_Object = MibScalar
pscFwRev = _PscFwRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2, 2),
    _PscFwRev_Type()
)
pscFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscFwRev.setStatus("mandatory")
_PscHwRev_Type = DisplayString
_PscHwRev_Object = MibScalar
pscHwRev = _PscHwRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2, 3),
    _PscHwRev_Type()
)
pscHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscHwRev.setStatus("mandatory")


class _KeyswitchPosition_Type(Integer32):
    """Custom type keyswitchPosition based on Integer32"""
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
        *(("fault", 1),
          ("local", 3),
          ("remote", 4),
          ("secure", 2),
          ("worldAccess", 5))
    )


_KeyswitchPosition_Type.__name__ = "Integer32"
_KeyswitchPosition_Object = MibScalar
keyswitchPosition = _KeyswitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2, 4),
    _KeyswitchPosition_Type()
)
keyswitchPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyswitchPosition.setStatus("mandatory")


class _PscFwImageStatus_Type(Integer32):
    """Custom type pscFwImageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downloadRequired", 2),
          ("okay", 1))
    )


_PscFwImageStatus_Type.__name__ = "Integer32"
_PscFwImageStatus_Object = MibScalar
pscFwImageStatus = _PscFwImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2, 5),
    _PscFwImageStatus_Type()
)
pscFwImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscFwImageStatus.setStatus("mandatory")


class _PscBackplaneStatus_Type(Integer32):
    """Custom type pscBackplaneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("okay", 1))
    )


_PscBackplaneStatus_Type.__name__ = "Integer32"
_PscBackplaneStatus_Object = MibScalar
pscBackplaneStatus = _PscBackplaneStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2, 6),
    _PscBackplaneStatus_Type()
)
pscBackplaneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscBackplaneStatus.setStatus("mandatory")


class _CabinetTemperature_Type(Integer32):
    """Custom type cabinetTemperature based on Integer32"""
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
        *(("excessivelyHigh", 3),
          ("excessivelyLow", 5),
          ("high", 2),
          ("low", 4),
          ("normal", 1))
    )


_CabinetTemperature_Type.__name__ = "Integer32"
_CabinetTemperature_Object = MibScalar
cabinetTemperature = _CabinetTemperature_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2, 7),
    _CabinetTemperature_Type()
)
cabinetTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabinetTemperature.setStatus("mandatory")


class _TemperatureWarning_Type(Integer32):
    """Custom type temperatureWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("heedWarning", 1),
          ("ignoreWarning", 2))
    )


_TemperatureWarning_Type.__name__ = "Integer32"
_TemperatureWarning_Object = MibScalar
temperatureWarning = _TemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 2, 8),
    _TemperatureWarning_Type()
)
temperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureWarning.setStatus("mandatory")
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 3)
)


class _RightPowerStatus_Type(Integer32):
    """Custom type rightPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2))
    )


_RightPowerStatus_Type.__name__ = "Integer32"
_RightPowerStatus_Object = MibScalar
rightPowerStatus = _RightPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 3, 1),
    _RightPowerStatus_Type()
)
rightPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rightPowerStatus.setStatus("mandatory")


class _RightPowerInputSource_Type(Integer32):
    """Custom type rightPowerInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acLine", 1),
          ("dc48V", 2),
          ("none", 3))
    )


_RightPowerInputSource_Type.__name__ = "Integer32"
_RightPowerInputSource_Object = MibScalar
rightPowerInputSource = _RightPowerInputSource_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 3, 2),
    _RightPowerInputSource_Type()
)
rightPowerInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rightPowerInputSource.setStatus("mandatory")
_RightPowerOutputPower_Type = Integer32
_RightPowerOutputPower_Object = MibScalar
rightPowerOutputPower = _RightPowerOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 3, 3),
    _RightPowerOutputPower_Type()
)
rightPowerOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rightPowerOutputPower.setStatus("mandatory")


class _LeftPowerStatus_Type(Integer32):
    """Custom type leftPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2))
    )


_LeftPowerStatus_Type.__name__ = "Integer32"
_LeftPowerStatus_Object = MibScalar
leftPowerStatus = _LeftPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 3, 4),
    _LeftPowerStatus_Type()
)
leftPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leftPowerStatus.setStatus("mandatory")


class _LeftPowerInputSource_Type(Integer32):
    """Custom type leftPowerInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acLine", 1),
          ("dc48V", 2),
          ("none", 3))
    )


_LeftPowerInputSource_Type.__name__ = "Integer32"
_LeftPowerInputSource_Object = MibScalar
leftPowerInputSource = _LeftPowerInputSource_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 3, 5),
    _LeftPowerInputSource_Type()
)
leftPowerInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leftPowerInputSource.setStatus("mandatory")
_LeftPowerOutputPower_Type = Integer32
_LeftPowerOutputPower_Object = MibScalar
leftPowerOutputPower = _LeftPowerOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 3, 6),
    _LeftPowerOutputPower_Type()
)
leftPowerOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leftPowerOutputPower.setStatus("mandatory")
_Slot_ObjectIdentity = ObjectIdentity
slot = _Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4)
)
_SlotNumber_Type = Integer32
_SlotNumber_Object = MibScalar
slotNumber = _SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 1),
    _SlotNumber_Type()
)
slotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotNumber.setStatus("mandatory")
_ScpSlot_Type = Integer32
_ScpSlot_Object = MibScalar
scpSlot = _ScpSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 2),
    _ScpSlot_Type()
)
scpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpSlot.setStatus("mandatory")
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("mandatory")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 3, 1)
)
slotEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("mandatory")
_SlotIndex_Type = Integer32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 3, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("mandatory")


class _SlotCardStatus_Type(Integer32):
    """Custom type slotCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fault", 5),
          ("notPresent", 1),
          ("powerDown", 2),
          ("powerDownThenUp", 4),
          ("powerUp", 3),
          ("revisionMismatch", 6),
          ("selfTestInProgress", 7))
    )


_SlotCardStatus_Type.__name__ = "Integer32"
_SlotCardStatus_Object = MibTableColumn
slotCardStatus = _SlotCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 3, 1, 2),
    _SlotCardStatus_Type()
)
slotCardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotCardStatus.setStatus("mandatory")


class _SlotCardType_Type(Integer32):
    """Custom type slotCardType based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("agl-2", 6),
          ("agl-2-plus", 8),
          ("cbs36", 3),
          ("clockCard", 5),
          ("fgl2", 2),
          ("fgl4", 7),
          ("gs2000", 11),
          ("gs2000-plus", 12),
          ("other", 1),
          ("switchEngine", 4),
          ("xgl2", 9),
          ("xgl4", 10))
    )


_SlotCardType_Type.__name__ = "Integer32"
_SlotCardType_Object = MibTableColumn
slotCardType = _SlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 3, 1, 3),
    _SlotCardType_Type()
)
slotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardType.setStatus("mandatory")
_SlotCardHwRev_Type = DisplayString
_SlotCardHwRev_Object = MibTableColumn
slotCardHwRev = _SlotCardHwRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 3, 1, 4),
    _SlotCardHwRev_Type()
)
slotCardHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardHwRev.setStatus("mandatory")
_SlotCardFwRev_Type = DisplayString
_SlotCardFwRev_Object = MibTableColumn
slotCardFwRev = _SlotCardFwRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 3, 1, 5),
    _SlotCardFwRev_Type()
)
slotCardFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCardFwRev.setStatus("mandatory")
_HostSlotTable_Object = MibTable
hostSlotTable = _HostSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hostSlotTable.setStatus("mandatory")
_HostSlotEntry_Object = MibTableRow
hostSlotEntry = _HostSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 4, 1)
)
hostSlotEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "hostSlotIndex"),
)
if mibBuilder.loadTexts:
    hostSlotEntry.setStatus("mandatory")
_HostSlotIndex_Type = Integer32
_HostSlotIndex_Object = MibTableColumn
hostSlotIndex = _HostSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 4, 1, 1),
    _HostSlotIndex_Type()
)
hostSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSlotIndex.setStatus("mandatory")
_HostIP_Type = IpAddress
_HostIP_Object = MibTableColumn
hostIP = _HostIP_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 4, 4, 1, 2),
    _HostIP_Type()
)
hostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIP.setStatus("mandatory")
_Fan_ObjectIdentity = ObjectIdentity
fan = _Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 5)
)


class _FanSpeed_Type(Integer32):
    """Custom type fanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1),
          ("normal", 2))
    )


_FanSpeed_Type.__name__ = "Integer32"
_FanSpeed_Object = MibScalar
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 5, 1),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("mandatory")


class _RightFanStatus_Type(Integer32):
    """Custom type rightFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2))
    )


_RightFanStatus_Type.__name__ = "Integer32"
_RightFanStatus_Object = MibScalar
rightFanStatus = _RightFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 5, 2),
    _RightFanStatus_Type()
)
rightFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rightFanStatus.setStatus("mandatory")


class _LeftFanStatus_Type(Integer32):
    """Custom type leftFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2))
    )


_LeftFanStatus_Type.__name__ = "Integer32"
_LeftFanStatus_Object = MibScalar
leftFanStatus = _LeftFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 5, 3),
    _LeftFanStatus_Type()
)
leftFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leftFanStatus.setStatus("mandatory")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 6)
)


class _BatteryStatus_Type(Integer32):
    """Custom type batteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2))
    )


_BatteryStatus_Type.__name__ = "Integer32"
_BatteryStatus_Object = MibScalar
batteryStatus = _BatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 6, 1),
    _BatteryStatus_Type()
)
batteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryStatus.setStatus("mandatory")


class _BatteryUsing_Type(Integer32):
    """Custom type batteryUsing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryPower", 1),
          ("externalPower", 2))
    )


_BatteryUsing_Type.__name__ = "Integer32"
_BatteryUsing_Object = MibScalar
batteryUsing = _BatteryUsing_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 6, 2),
    _BatteryUsing_Type()
)
batteryUsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryUsing.setStatus("mandatory")


class _BatteryCharge_Type(Integer32):
    """Custom type batteryCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullyCharged", 1),
          ("low", 3),
          ("okay", 2))
    )


_BatteryCharge_Type.__name__ = "Integer32"
_BatteryCharge_Object = MibScalar
batteryCharge = _BatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 6, 3),
    _BatteryCharge_Type()
)
batteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCharge.setStatus("mandatory")


class _BatteryTest_Type(Integer32):
    """Custom type batteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("pass", 1),
          ("test", 3))
    )


_BatteryTest_Type.__name__ = "Integer32"
_BatteryTest_Object = MibScalar
batteryTest = _BatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 6, 4),
    _BatteryTest_Type()
)
batteryTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTest.setStatus("mandatory")
_Fppn_ObjectIdentity = ObjectIdentity
fppn = _Fppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 7)
)
_FppnTable_Object = MibTable
fppnTable = _FppnTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    fppnTable.setStatus("mandatory")
_FppnEntry_Object = MibTableRow
fppnEntry = _FppnEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 7, 1, 1)
)
fppnEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "fppnSlotNumber"),
    (0, "DEC-ELAN-MIB", "fppnPortOfThatSlot"),
)
if mibBuilder.loadTexts:
    fppnEntry.setStatus("mandatory")
_FppnSlotNumber_Type = Integer32
_FppnSlotNumber_Object = MibTableColumn
fppnSlotNumber = _FppnSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 7, 1, 1, 1),
    _FppnSlotNumber_Type()
)
fppnSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fppnSlotNumber.setStatus("mandatory")
_FppnPortOfThatSlot_Type = Integer32
_FppnPortOfThatSlot_Object = MibTableColumn
fppnPortOfThatSlot = _FppnPortOfThatSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 7, 1, 1, 2),
    _FppnPortOfThatSlot_Type()
)
fppnPortOfThatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fppnPortOfThatSlot.setStatus("mandatory")
_FppnIfIndex_Type = Integer32
_FppnIfIndex_Object = MibTableColumn
fppnIfIndex = _FppnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 7, 1, 1, 3),
    _FppnIfIndex_Type()
)
fppnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fppnIfIndex.setStatus("mandatory")
_FppnBridgePortNumber_Type = Integer32
_FppnBridgePortNumber_Object = MibTableColumn
fppnBridgePortNumber = _FppnBridgePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 7, 1, 1, 4),
    _FppnBridgePortNumber_Type()
)
fppnBridgePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fppnBridgePortNumber.setStatus("mandatory")
_LineCard_ObjectIdentity = ObjectIdentity
lineCard = _LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 8)
)
_MPortTable_Object = MibTable
mPortTable = _MPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mPortTable.setStatus("mandatory")
_MPortEntry_Object = MibTableRow
mPortEntry = _MPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 8, 1, 1)
)
mPortEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "mPortSMTIndex"),
    (0, "DEC-ELAN-MIB", "mPortMACIndex"),
)
if mibBuilder.loadTexts:
    mPortEntry.setStatus("mandatory")
_MPortSMTIndex_Type = Integer32
_MPortSMTIndex_Object = MibTableColumn
mPortSMTIndex = _MPortSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 8, 1, 1, 1),
    _MPortSMTIndex_Type()
)
mPortSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPortSMTIndex.setStatus("mandatory")
_MPortMACIndex_Type = Integer32
_MPortMACIndex_Object = MibTableColumn
mPortMACIndex = _MPortMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 8, 1, 1, 2),
    _MPortMACIndex_Type()
)
mPortMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPortMACIndex.setStatus("mandatory")


class _MPortEnable_Type(Integer32):
    """Custom type mPortEnable based on Integer32"""
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


_MPortEnable_Type.__name__ = "Integer32"
_MPortEnable_Object = MibTableColumn
mPortEnable = _MPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 8, 1, 1, 3),
    _MPortEnable_Type()
)
mPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mPortEnable.setStatus("mandatory")
_Led_ObjectIdentity = ObjectIdentity
led = _Led_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9)
)
_LedTable_Object = MibTable
ledTable = _LedTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ledTable.setStatus("mandatory")
_LedTableEntry_Object = MibTableRow
ledTableEntry = _LedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 1, 1)
)
ledTableEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ledTableIndex"),
)
if mibBuilder.loadTexts:
    ledTableEntry.setStatus("mandatory")
_LedTableIndex_Type = Integer32
_LedTableIndex_Object = MibTableColumn
ledTableIndex = _LedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 1, 1, 1),
    _LedTableIndex_Type()
)
ledTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledTableIndex.setStatus("mandatory")
_LedCount_Type = Integer32
_LedCount_Object = MibTableColumn
ledCount = _LedCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 1, 1, 2),
    _LedCount_Type()
)
ledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledCount.setStatus("mandatory")
_LedSlotTable_Object = MibTable
ledSlotTable = _LedSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ledSlotTable.setStatus("mandatory")
_LedEntry_Object = MibTableRow
ledEntry = _LedEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 2, 1)
)
ledEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ledSlotIndex"),
    (0, "DEC-ELAN-MIB", "ledLedIndex"),
)
if mibBuilder.loadTexts:
    ledEntry.setStatus("mandatory")
_LedSlotIndex_Type = Integer32
_LedSlotIndex_Object = MibTableColumn
ledSlotIndex = _LedSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 2, 1, 1),
    _LedSlotIndex_Type()
)
ledSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledSlotIndex.setStatus("mandatory")
_LedLedIndex_Type = Integer32
_LedLedIndex_Object = MibTableColumn
ledLedIndex = _LedLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 2, 1, 2),
    _LedLedIndex_Type()
)
ledLedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledLedIndex.setStatus("mandatory")


class _LedDescr_Type(DisplayString):
    """Custom type ledDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LedDescr_Type.__name__ = "DisplayString"
_LedDescr_Object = MibTableColumn
ledDescr = _LedDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 2, 1, 3),
    _LedDescr_Type()
)
ledDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledDescr.setStatus("mandatory")


class _LedProgram_Type(OctetString):
    """Custom type ledProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_LedProgram_Type.__name__ = "OctetString"
_LedProgram_Object = MibTableColumn
ledProgram = _LedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 1, 9, 2, 1, 4),
    _LedProgram_Type()
)
ledProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledProgram.setStatus("mandatory")
_GigaBridge_ObjectIdentity = ObjectIdentity
gigaBridge = _GigaBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2)
)
_FilterByReferencedExpression_ObjectIdentity = ObjectIdentity
filterByReferencedExpression = _FilterByReferencedExpression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1)
)
_EbrNportMatrixNameTable_Object = MibTable
ebrNportMatrixNameTable = _EbrNportMatrixNameTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ebrNportMatrixNameTable.setStatus("mandatory")
_EbrNportMatrixNameEntry_Object = MibTableRow
ebrNportMatrixNameEntry = _EbrNportMatrixNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 1, 1)
)
ebrNportMatrixNameEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportMatrixName"),
)
if mibBuilder.loadTexts:
    ebrNportMatrixNameEntry.setStatus("mandatory")


class _EbrNportMatrixName_Type(DisplayString):
    """Custom type ebrNportMatrixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportMatrixName_Type.__name__ = "DisplayString"
_EbrNportMatrixName_Object = MibTableColumn
ebrNportMatrixName = _EbrNportMatrixName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 1, 1, 1),
    _EbrNportMatrixName_Type()
)
ebrNportMatrixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportMatrixName.setStatus("mandatory")


class _EbrNportMatrixValue_Type(DisplayString):
    """Custom type ebrNportMatrixValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportMatrixValue_Type.__name__ = "DisplayString"
_EbrNportMatrixValue_Object = MibTableColumn
ebrNportMatrixValue = _EbrNportMatrixValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 1, 1, 2),
    _EbrNportMatrixValue_Type()
)
ebrNportMatrixValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportMatrixValue.setStatus("mandatory")


class _EbrNportMatrixStatus_Type(Integer32):
    """Custom type ebrNportMatrixStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportMatrixStatus_Type.__name__ = "Integer32"
_EbrNportMatrixStatus_Object = MibTableColumn
ebrNportMatrixStatus = _EbrNportMatrixStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 1, 1, 3),
    _EbrNportMatrixStatus_Type()
)
ebrNportMatrixStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportMatrixStatus.setStatus("mandatory")


class _EbrNportMatrixFppnValue_Type(DisplayString):
    """Custom type ebrNportMatrixFppnValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportMatrixFppnValue_Type.__name__ = "DisplayString"
_EbrNportMatrixFppnValue_Object = MibTableColumn
ebrNportMatrixFppnValue = _EbrNportMatrixFppnValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 1, 1, 4),
    _EbrNportMatrixFppnValue_Type()
)
ebrNportMatrixFppnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportMatrixFppnValue.setStatus("mandatory")
_EbrNportSapNameTable_Object = MibTable
ebrNportSapNameTable = _EbrNportSapNameTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ebrNportSapNameTable.setStatus("mandatory")
_EbrNportSapNameEntry_Object = MibTableRow
ebrNportSapNameEntry = _EbrNportSapNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 2, 1)
)
ebrNportSapNameEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSapName"),
)
if mibBuilder.loadTexts:
    ebrNportSapNameEntry.setStatus("mandatory")


class _EbrNportSapName_Type(DisplayString):
    """Custom type ebrNportSapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportSapName_Type.__name__ = "DisplayString"
_EbrNportSapName_Object = MibTableColumn
ebrNportSapName = _EbrNportSapName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 2, 1, 1),
    _EbrNportSapName_Type()
)
ebrNportSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportSapName.setStatus("mandatory")


class _EbrNportSapNameSap_Type(OctetString):
    """Custom type ebrNportSapNameSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EbrNportSapNameSap_Type.__name__ = "OctetString"
_EbrNportSapNameSap_Object = MibTableColumn
ebrNportSapNameSap = _EbrNportSapNameSap_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 2, 1, 2),
    _EbrNportSapNameSap_Type()
)
ebrNportSapNameSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapNameSap.setStatus("mandatory")


class _EbrNportSapMatrixName_Type(DisplayString):
    """Custom type ebrNportSapMatrixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportSapMatrixName_Type.__name__ = "DisplayString"
_EbrNportSapMatrixName_Object = MibTableColumn
ebrNportSapMatrixName = _EbrNportSapMatrixName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 2, 1, 3),
    _EbrNportSapMatrixName_Type()
)
ebrNportSapMatrixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapMatrixName.setStatus("mandatory")


class _EbrNportSapNameDisp_Type(Integer32):
    """Custom type ebrNportSapNameDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysFilter", 2),
          ("alwaysForward", 3),
          ("filter", 1))
    )


_EbrNportSapNameDisp_Type.__name__ = "Integer32"
_EbrNportSapNameDisp_Object = MibTableColumn
ebrNportSapNameDisp = _EbrNportSapNameDisp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 2, 1, 4),
    _EbrNportSapNameDisp_Type()
)
ebrNportSapNameDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapNameDisp.setStatus("mandatory")


class _EbrNportSapNameStatus_Type(Integer32):
    """Custom type ebrNportSapNameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportSapNameStatus_Type.__name__ = "Integer32"
_EbrNportSapNameStatus_Object = MibTableColumn
ebrNportSapNameStatus = _EbrNportSapNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 2, 1, 5),
    _EbrNportSapNameStatus_Type()
)
ebrNportSapNameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapNameStatus.setStatus("mandatory")
_EbrNportSnapNameTable_Object = MibTable
ebrNportSnapNameTable = _EbrNportSnapNameTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ebrNportSnapNameTable.setStatus("mandatory")
_EbrNportSnapNameEntry_Object = MibTableRow
ebrNportSnapNameEntry = _EbrNportSnapNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 3, 1)
)
ebrNportSnapNameEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSnapName"),
)
if mibBuilder.loadTexts:
    ebrNportSnapNameEntry.setStatus("mandatory")


class _EbrNportSnapName_Type(DisplayString):
    """Custom type ebrNportSnapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportSnapName_Type.__name__ = "DisplayString"
_EbrNportSnapName_Object = MibTableColumn
ebrNportSnapName = _EbrNportSnapName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 3, 1, 1),
    _EbrNportSnapName_Type()
)
ebrNportSnapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportSnapName.setStatus("mandatory")


class _EbrNportSnapNameSnap_Type(OctetString):
    """Custom type ebrNportSnapNameSnap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_EbrNportSnapNameSnap_Type.__name__ = "OctetString"
_EbrNportSnapNameSnap_Object = MibTableColumn
ebrNportSnapNameSnap = _EbrNportSnapNameSnap_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 3, 1, 2),
    _EbrNportSnapNameSnap_Type()
)
ebrNportSnapNameSnap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapNameSnap.setStatus("mandatory")


class _EbrNportSnapMatrixName_Type(DisplayString):
    """Custom type ebrNportSnapMatrixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportSnapMatrixName_Type.__name__ = "DisplayString"
_EbrNportSnapMatrixName_Object = MibTableColumn
ebrNportSnapMatrixName = _EbrNportSnapMatrixName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 3, 1, 3),
    _EbrNportSnapMatrixName_Type()
)
ebrNportSnapMatrixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapMatrixName.setStatus("mandatory")


class _EbrNportSnapNameDisp_Type(Integer32):
    """Custom type ebrNportSnapNameDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysFilter", 2),
          ("alwaysForward", 3),
          ("filter", 1))
    )


_EbrNportSnapNameDisp_Type.__name__ = "Integer32"
_EbrNportSnapNameDisp_Object = MibTableColumn
ebrNportSnapNameDisp = _EbrNportSnapNameDisp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 3, 1, 4),
    _EbrNportSnapNameDisp_Type()
)
ebrNportSnapNameDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapNameDisp.setStatus("mandatory")


class _EbrNportSnapNameStatus_Type(Integer32):
    """Custom type ebrNportSnapNameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportSnapNameStatus_Type.__name__ = "Integer32"
_EbrNportSnapNameStatus_Object = MibTableColumn
ebrNportSnapNameStatus = _EbrNportSnapNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 3, 1, 5),
    _EbrNportSnapNameStatus_Type()
)
ebrNportSnapNameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapNameStatus.setStatus("mandatory")
_EbrNportDANameTable_Object = MibTable
ebrNportDANameTable = _EbrNportDANameTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ebrNportDANameTable.setStatus("mandatory")
_EbrNportDANameEntry_Object = MibTableRow
ebrNportDANameEntry = _EbrNportDANameEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 4, 1)
)
ebrNportDANameEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportDAName"),
)
if mibBuilder.loadTexts:
    ebrNportDANameEntry.setStatus("mandatory")


class _EbrNportDAName_Type(DisplayString):
    """Custom type ebrNportDAName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportDAName_Type.__name__ = "DisplayString"
_EbrNportDAName_Object = MibTableColumn
ebrNportDAName = _EbrNportDAName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 4, 1, 1),
    _EbrNportDAName_Type()
)
ebrNportDAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportDAName.setStatus("mandatory")


class _EbrNportDANameDA_Type(OctetString):
    """Custom type ebrNportDANameDA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrNportDANameDA_Type.__name__ = "OctetString"
_EbrNportDANameDA_Object = MibTableColumn
ebrNportDANameDA = _EbrNportDANameDA_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 4, 1, 2),
    _EbrNportDANameDA_Type()
)
ebrNportDANameDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDANameDA.setStatus("mandatory")


class _EbrNportDAMatrixName_Type(DisplayString):
    """Custom type ebrNportDAMatrixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportDAMatrixName_Type.__name__ = "DisplayString"
_EbrNportDAMatrixName_Object = MibTableColumn
ebrNportDAMatrixName = _EbrNportDAMatrixName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 4, 1, 3),
    _EbrNportDAMatrixName_Type()
)
ebrNportDAMatrixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDAMatrixName.setStatus("mandatory")


class _EbrNportDANameDisp_Type(Integer32):
    """Custom type ebrNportDANameDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysFilter", 2),
          ("alwaysForward", 3),
          ("filter", 1))
    )


_EbrNportDANameDisp_Type.__name__ = "Integer32"
_EbrNportDANameDisp_Object = MibTableColumn
ebrNportDANameDisp = _EbrNportDANameDisp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 4, 1, 4),
    _EbrNportDANameDisp_Type()
)
ebrNportDANameDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDANameDisp.setStatus("mandatory")


class _EbrNportDANameStatus_Type(Integer32):
    """Custom type ebrNportDANameStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_EbrNportDANameStatus_Type.__name__ = "Integer32"
_EbrNportDANameStatus_Object = MibTableColumn
ebrNportDANameStatus = _EbrNportDANameStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 4, 1, 5),
    _EbrNportDANameStatus_Type()
)
ebrNportDANameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDANameStatus.setStatus("mandatory")
_EbrNportSANameTable_Object = MibTable
ebrNportSANameTable = _EbrNportSANameTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ebrNportSANameTable.setStatus("mandatory")
_EbrNportSANameEntry_Object = MibTableRow
ebrNportSANameEntry = _EbrNportSANameEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 5, 1)
)
ebrNportSANameEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSAName"),
)
if mibBuilder.loadTexts:
    ebrNportSANameEntry.setStatus("mandatory")


class _EbrNportSAName_Type(DisplayString):
    """Custom type ebrNportSAName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportSAName_Type.__name__ = "DisplayString"
_EbrNportSAName_Object = MibTableColumn
ebrNportSAName = _EbrNportSAName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 5, 1, 1),
    _EbrNportSAName_Type()
)
ebrNportSAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportSAName.setStatus("mandatory")


class _EbrNportSANameSA_Type(OctetString):
    """Custom type ebrNportSANameSA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrNportSANameSA_Type.__name__ = "OctetString"
_EbrNportSANameSA_Object = MibTableColumn
ebrNportSANameSA = _EbrNportSANameSA_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 5, 1, 2),
    _EbrNportSANameSA_Type()
)
ebrNportSANameSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSANameSA.setStatus("mandatory")


class _EbrNportSAMatrixName_Type(DisplayString):
    """Custom type ebrNportSAMatrixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportSAMatrixName_Type.__name__ = "DisplayString"
_EbrNportSAMatrixName_Object = MibTableColumn
ebrNportSAMatrixName = _EbrNportSAMatrixName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 5, 1, 3),
    _EbrNportSAMatrixName_Type()
)
ebrNportSAMatrixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSAMatrixName.setStatus("mandatory")


class _EbrNportSANameDisp_Type(Integer32):
    """Custom type ebrNportSANameDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alwaysFilter", 2),
          ("alwaysForward", 3),
          ("filter", 6),
          ("lockdown", 4),
          ("lockdownportmask", 5),
          ("portMask", 1))
    )


_EbrNportSANameDisp_Type.__name__ = "Integer32"
_EbrNportSANameDisp_Object = MibTableColumn
ebrNportSANameDisp = _EbrNportSANameDisp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 5, 1, 4),
    _EbrNportSANameDisp_Type()
)
ebrNportSANameDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSANameDisp.setStatus("mandatory")


class _EbrNportSANameStatus_Type(Integer32):
    """Custom type ebrNportSANameStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_EbrNportSANameStatus_Type.__name__ = "Integer32"
_EbrNportSANameStatus_Object = MibTableColumn
ebrNportSANameStatus = _EbrNportSANameStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 5, 1, 5),
    _EbrNportSANameStatus_Type()
)
ebrNportSANameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSANameStatus.setStatus("mandatory")


class _EbrNportDefaultMatrixValue_Type(DisplayString):
    """Custom type ebrNportDefaultMatrixValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportDefaultMatrixValue_Type.__name__ = "DisplayString"
_EbrNportDefaultMatrixValue_Object = MibScalar
ebrNportDefaultMatrixValue = _EbrNportDefaultMatrixValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 6),
    _EbrNportDefaultMatrixValue_Type()
)
ebrNportDefaultMatrixValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDefaultMatrixValue.setStatus("mandatory")


class _EbrNportManualFilter_Type(DisplayString):
    """Custom type ebrNportManualFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportManualFilter_Type.__name__ = "DisplayString"
_EbrNportManualFilter_Object = MibScalar
ebrNportManualFilter = _EbrNportManualFilter_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 7),
    _EbrNportManualFilter_Type()
)
ebrNportManualFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportManualFilter.setStatus("mandatory")
_EbrNportMatrixNameRowTable_Object = MibTable
ebrNportMatrixNameRowTable = _EbrNportMatrixNameRowTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ebrNportMatrixNameRowTable.setStatus("mandatory")
_EbrNportMatrixNameRowEntry_Object = MibTableRow
ebrNportMatrixNameRowEntry = _EbrNportMatrixNameRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 8, 1)
)
ebrNportMatrixNameRowEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportmatrixName"),
    (0, "DEC-ELAN-MIB", "ebrNportMatrixReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportMatrixNameRowEntry.setStatus("mandatory")


class _EbrNportmatrixName_Type(DisplayString):
    """Custom type ebrNportmatrixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportmatrixName_Type.__name__ = "DisplayString"
_EbrNportmatrixName_Object = MibTableColumn
ebrNportmatrixName = _EbrNportmatrixName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 8, 1, 1),
    _EbrNportmatrixName_Type()
)
ebrNportmatrixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportmatrixName.setStatus("mandatory")
_EbrNportMatrixReceivePort_Type = Integer32
_EbrNportMatrixReceivePort_Object = MibTableColumn
ebrNportMatrixReceivePort = _EbrNportMatrixReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 8, 1, 2),
    _EbrNportMatrixReceivePort_Type()
)
ebrNportMatrixReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportMatrixReceivePort.setStatus("mandatory")


class _EbrNportMatrixAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportMatrixAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportMatrixAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportMatrixAllowedToGoTo_Object = MibTableColumn
ebrNportMatrixAllowedToGoTo = _EbrNportMatrixAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 8, 1, 3),
    _EbrNportMatrixAllowedToGoTo_Type()
)
ebrNportMatrixAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportMatrixAllowedToGoTo.setStatus("mandatory")


class _EbrNportMatrixNameRowStatus_Type(Integer32):
    """Custom type ebrNportMatrixNameRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportMatrixNameRowStatus_Type.__name__ = "Integer32"
_EbrNportMatrixNameRowStatus_Object = MibTableColumn
ebrNportMatrixNameRowStatus = _EbrNportMatrixNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 8, 1, 4),
    _EbrNportMatrixNameRowStatus_Type()
)
ebrNportMatrixNameRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportMatrixNameRowStatus.setStatus("mandatory")


class _EbrNportDefaultMatrixFppnValue_Type(DisplayString):
    """Custom type ebrNportDefaultMatrixFppnValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportDefaultMatrixFppnValue_Type.__name__ = "DisplayString"
_EbrNportDefaultMatrixFppnValue_Object = MibScalar
ebrNportDefaultMatrixFppnValue = _EbrNportDefaultMatrixFppnValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 9),
    _EbrNportDefaultMatrixFppnValue_Type()
)
ebrNportDefaultMatrixFppnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDefaultMatrixFppnValue.setStatus("mandatory")


class _EbrNportFppnManualFilter_Type(DisplayString):
    """Custom type ebrNportFppnManualFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportFppnManualFilter_Type.__name__ = "DisplayString"
_EbrNportFppnManualFilter_Object = MibScalar
ebrNportFppnManualFilter = _EbrNportFppnManualFilter_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 10),
    _EbrNportFppnManualFilter_Type()
)
ebrNportFppnManualFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportFppnManualFilter.setStatus("mandatory")
_EbrNportMatrixFppnRowTable_Object = MibTable
ebrNportMatrixFppnRowTable = _EbrNportMatrixFppnRowTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ebrNportMatrixFppnRowTable.setStatus("mandatory")
_EbrNportMatrixFppnRowEntry_Object = MibTableRow
ebrNportMatrixFppnRowEntry = _EbrNportMatrixFppnRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 11, 1)
)
ebrNportMatrixFppnRowEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportmatrixname"),
    (0, "DEC-ELAN-MIB", "ebrNportMatrixFppnReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportMatrixFppnRowEntry.setStatus("mandatory")


class _EbrNportmatrixname_Type(DisplayString):
    """Custom type ebrNportmatrixname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportmatrixname_Type.__name__ = "DisplayString"
_EbrNportmatrixname_Object = MibTableColumn
ebrNportmatrixname = _EbrNportmatrixname_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 11, 1, 1),
    _EbrNportmatrixname_Type()
)
ebrNportmatrixname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportmatrixname.setStatus("mandatory")
_EbrNportMatrixFppnReceivePort_Type = DisplayString
_EbrNportMatrixFppnReceivePort_Object = MibTableColumn
ebrNportMatrixFppnReceivePort = _EbrNportMatrixFppnReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 11, 1, 2),
    _EbrNportMatrixFppnReceivePort_Type()
)
ebrNportMatrixFppnReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportMatrixFppnReceivePort.setStatus("mandatory")


class _EbrNportMatrixFppnAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportMatrixFppnAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportMatrixFppnAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportMatrixFppnAllowedToGoTo_Object = MibTableColumn
ebrNportMatrixFppnAllowedToGoTo = _EbrNportMatrixFppnAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 11, 1, 3),
    _EbrNportMatrixFppnAllowedToGoTo_Type()
)
ebrNportMatrixFppnAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportMatrixFppnAllowedToGoTo.setStatus("mandatory")


class _EbrNportMatrixFppnRowStatus_Type(Integer32):
    """Custom type ebrNportMatrixFppnRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportMatrixFppnRowStatus_Type.__name__ = "Integer32"
_EbrNportMatrixFppnRowStatus_Object = MibTableColumn
ebrNportMatrixFppnRowStatus = _EbrNportMatrixFppnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 11, 1, 4),
    _EbrNportMatrixFppnRowStatus_Type()
)
ebrNportMatrixFppnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportMatrixFppnRowStatus.setStatus("mandatory")


class _EbrNportNamedDefaultMatrix_Type(DisplayString):
    """Custom type ebrNportNamedDefaultMatrix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportNamedDefaultMatrix_Type.__name__ = "DisplayString"
_EbrNportNamedDefaultMatrix_Object = MibScalar
ebrNportNamedDefaultMatrix = _EbrNportNamedDefaultMatrix_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 12),
    _EbrNportNamedDefaultMatrix_Type()
)
ebrNportNamedDefaultMatrix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportNamedDefaultMatrix.setStatus("mandatory")
_EbrNportDefaultMatrixRowTable_Object = MibTable
ebrNportDefaultMatrixRowTable = _EbrNportDefaultMatrixRowTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 13)
)
if mibBuilder.loadTexts:
    ebrNportDefaultMatrixRowTable.setStatus("mandatory")
_EbrNportDefaultMatrixRowEntry_Object = MibTableRow
ebrNportDefaultMatrixRowEntry = _EbrNportDefaultMatrixRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 13, 1)
)
ebrNportDefaultMatrixRowEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportDefaultMatrixReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportDefaultMatrixRowEntry.setStatus("mandatory")
_EbrNportDefaultMatrixReceivePort_Type = Integer32
_EbrNportDefaultMatrixReceivePort_Object = MibTableColumn
ebrNportDefaultMatrixReceivePort = _EbrNportDefaultMatrixReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 13, 1, 1),
    _EbrNportDefaultMatrixReceivePort_Type()
)
ebrNportDefaultMatrixReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportDefaultMatrixReceivePort.setStatus("mandatory")


class _EbrNportDefaultMatrixAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportDefaultMatrixAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportDefaultMatrixAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportDefaultMatrixAllowedToGoTo_Object = MibTableColumn
ebrNportDefaultMatrixAllowedToGoTo = _EbrNportDefaultMatrixAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 13, 1, 2),
    _EbrNportDefaultMatrixAllowedToGoTo_Type()
)
ebrNportDefaultMatrixAllowedToGoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportDefaultMatrixAllowedToGoTo.setStatus("mandatory")


class _EbrNportFloodMatrixValue_Type(DisplayString):
    """Custom type ebrNportFloodMatrixValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportFloodMatrixValue_Type.__name__ = "DisplayString"
_EbrNportFloodMatrixValue_Object = MibScalar
ebrNportFloodMatrixValue = _EbrNportFloodMatrixValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 14),
    _EbrNportFloodMatrixValue_Type()
)
ebrNportFloodMatrixValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportFloodMatrixValue.setStatus("mandatory")


class _EbrNportFloodMatrixFppnValue_Type(DisplayString):
    """Custom type ebrNportFloodMatrixFppnValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportFloodMatrixFppnValue_Type.__name__ = "DisplayString"
_EbrNportFloodMatrixFppnValue_Object = MibScalar
ebrNportFloodMatrixFppnValue = _EbrNportFloodMatrixFppnValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 15),
    _EbrNportFloodMatrixFppnValue_Type()
)
ebrNportFloodMatrixFppnValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportFloodMatrixFppnValue.setStatus("mandatory")


class _EbrNportNamedFloodMatrix_Type(DisplayString):
    """Custom type ebrNportNamedFloodMatrix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EbrNportNamedFloodMatrix_Type.__name__ = "DisplayString"
_EbrNportNamedFloodMatrix_Object = MibScalar
ebrNportNamedFloodMatrix = _EbrNportNamedFloodMatrix_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 16),
    _EbrNportNamedFloodMatrix_Type()
)
ebrNportNamedFloodMatrix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportNamedFloodMatrix.setStatus("mandatory")
_EbrNportFloodMatrixRowTable_Object = MibTable
ebrNportFloodMatrixRowTable = _EbrNportFloodMatrixRowTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 17)
)
if mibBuilder.loadTexts:
    ebrNportFloodMatrixRowTable.setStatus("mandatory")
_EbrNportFloodMatrixRowEntry_Object = MibTableRow
ebrNportFloodMatrixRowEntry = _EbrNportFloodMatrixRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 17, 1)
)
ebrNportFloodMatrixRowEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportFloodMatrixReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportFloodMatrixRowEntry.setStatus("mandatory")
_EbrNportFloodMatrixReceivePort_Type = Integer32
_EbrNportFloodMatrixReceivePort_Object = MibTableColumn
ebrNportFloodMatrixReceivePort = _EbrNportFloodMatrixReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 17, 1, 1),
    _EbrNportFloodMatrixReceivePort_Type()
)
ebrNportFloodMatrixReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportFloodMatrixReceivePort.setStatus("mandatory")


class _EbrNportFloodMatrixAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportFloodMatrixAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportFloodMatrixAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportFloodMatrixAllowedToGoTo_Object = MibTableColumn
ebrNportFloodMatrixAllowedToGoTo = _EbrNportFloodMatrixAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 1, 17, 1, 2),
    _EbrNportFloodMatrixAllowedToGoTo_Type()
)
ebrNportFloodMatrixAllowedToGoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrNportFloodMatrixAllowedToGoTo.setStatus("mandatory")
_FilterByBitmapValue_ObjectIdentity = ObjectIdentity
filterByBitmapValue = _FilterByBitmapValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2)
)
_EbrNportSapProtoTable_Object = MibTable
ebrNportSapProtoTable = _EbrNportSapProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ebrNportSapProtoTable.setStatus("mandatory")
_EbrNportSapProtoEntry_Object = MibTableRow
ebrNportSapProtoEntry = _EbrNportSapProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 1, 1)
)
ebrNportSapProtoEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSapValue"),
    (0, "DEC-ELAN-MIB", "ebrNportSapReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportSapProtoEntry.setStatus("mandatory")


class _EbrNportSapValue_Type(OctetString):
    """Custom type ebrNportSapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EbrNportSapValue_Type.__name__ = "OctetString"
_EbrNportSapValue_Object = MibTableColumn
ebrNportSapValue = _EbrNportSapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 1, 1, 1),
    _EbrNportSapValue_Type()
)
ebrNportSapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapValue.setStatus("mandatory")
_EbrNportSapReceivePort_Type = Integer32
_EbrNportSapReceivePort_Object = MibTableColumn
ebrNportSapReceivePort = _EbrNportSapReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 1, 1, 2),
    _EbrNportSapReceivePort_Type()
)
ebrNportSapReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapReceivePort.setStatus("mandatory")


class _EbrNportSapAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportSapAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportSapAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportSapAllowedToGoTo_Object = MibTableColumn
ebrNportSapAllowedToGoTo = _EbrNportSapAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 1, 1, 3),
    _EbrNportSapAllowedToGoTo_Type()
)
ebrNportSapAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapAllowedToGoTo.setStatus("mandatory")
_EbrNportSapFilterCharacteristicsTable_Object = MibTable
ebrNportSapFilterCharacteristicsTable = _EbrNportSapFilterCharacteristicsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ebrNportSapFilterCharacteristicsTable.setStatus("mandatory")
_EbrNportSapFilterCharacteristicsEntry_Object = MibTableRow
ebrNportSapFilterCharacteristicsEntry = _EbrNportSapFilterCharacteristicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 2, 1)
)
ebrNportSapFilterCharacteristicsEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSapFilterCharacteristicsSapValue"),
)
if mibBuilder.loadTexts:
    ebrNportSapFilterCharacteristicsEntry.setStatus("mandatory")


class _EbrNportSapFilterCharacteristicsSapValue_Type(OctetString):
    """Custom type ebrNportSapFilterCharacteristicsSapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EbrNportSapFilterCharacteristicsSapValue_Type.__name__ = "OctetString"
_EbrNportSapFilterCharacteristicsSapValue_Object = MibTableColumn
ebrNportSapFilterCharacteristicsSapValue = _EbrNportSapFilterCharacteristicsSapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 2, 1, 1),
    _EbrNportSapFilterCharacteristicsSapValue_Type()
)
ebrNportSapFilterCharacteristicsSapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapFilterCharacteristicsSapValue.setStatus("mandatory")


class _EbrNportSapDisp_Type(Integer32):
    """Custom type ebrNportSapDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysFilter", 2),
          ("alwaysForward", 3),
          ("filter", 1))
    )


_EbrNportSapDisp_Type.__name__ = "Integer32"
_EbrNportSapDisp_Object = MibTableColumn
ebrNportSapDisp = _EbrNportSapDisp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 2, 1, 2),
    _EbrNportSapDisp_Type()
)
ebrNportSapDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapDisp.setStatus("mandatory")


class _EbrNportSapStatus_Type(Integer32):
    """Custom type ebrNportSapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportSapStatus_Type.__name__ = "Integer32"
_EbrNportSapStatus_Object = MibTableColumn
ebrNportSapStatus = _EbrNportSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 2, 1, 3),
    _EbrNportSapStatus_Type()
)
ebrNportSapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapStatus.setStatus("mandatory")
_EbrNportSnapProtoTable_Object = MibTable
ebrNportSnapProtoTable = _EbrNportSnapProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    ebrNportSnapProtoTable.setStatus("mandatory")
_EbrNportSnapProtoEntry_Object = MibTableRow
ebrNportSnapProtoEntry = _EbrNportSnapProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 3, 1)
)
ebrNportSnapProtoEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSnapValue"),
    (0, "DEC-ELAN-MIB", "ebrNportSnapReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportSnapProtoEntry.setStatus("mandatory")


class _EbrNportSnapValue_Type(OctetString):
    """Custom type ebrNportSnapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_EbrNportSnapValue_Type.__name__ = "OctetString"
_EbrNportSnapValue_Object = MibTableColumn
ebrNportSnapValue = _EbrNportSnapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 3, 1, 1),
    _EbrNportSnapValue_Type()
)
ebrNportSnapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapValue.setStatus("mandatory")
_EbrNportSnapReceivePort_Type = Integer32
_EbrNportSnapReceivePort_Object = MibTableColumn
ebrNportSnapReceivePort = _EbrNportSnapReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 3, 1, 2),
    _EbrNportSnapReceivePort_Type()
)
ebrNportSnapReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapReceivePort.setStatus("mandatory")


class _EbrNportSnapAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportSnapAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportSnapAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportSnapAllowedToGoTo_Object = MibTableColumn
ebrNportSnapAllowedToGoTo = _EbrNportSnapAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 3, 1, 3),
    _EbrNportSnapAllowedToGoTo_Type()
)
ebrNportSnapAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapAllowedToGoTo.setStatus("mandatory")
_EbrNportSnapFilterCharacteristicsTable_Object = MibTable
ebrNportSnapFilterCharacteristicsTable = _EbrNportSnapFilterCharacteristicsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ebrNportSnapFilterCharacteristicsTable.setStatus("mandatory")
_EbrNportSnapFilterCharacteristicsEntry_Object = MibTableRow
ebrNportSnapFilterCharacteristicsEntry = _EbrNportSnapFilterCharacteristicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 4, 1)
)
ebrNportSnapFilterCharacteristicsEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSnapFilterCharacteristicsSnapValue"),
)
if mibBuilder.loadTexts:
    ebrNportSnapFilterCharacteristicsEntry.setStatus("mandatory")


class _EbrNportSnapFilterCharacteristicsSnapValue_Type(OctetString):
    """Custom type ebrNportSnapFilterCharacteristicsSnapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EbrNportSnapFilterCharacteristicsSnapValue_Type.__name__ = "OctetString"
_EbrNportSnapFilterCharacteristicsSnapValue_Object = MibTableColumn
ebrNportSnapFilterCharacteristicsSnapValue = _EbrNportSnapFilterCharacteristicsSnapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 4, 1, 1),
    _EbrNportSnapFilterCharacteristicsSnapValue_Type()
)
ebrNportSnapFilterCharacteristicsSnapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapFilterCharacteristicsSnapValue.setStatus("mandatory")


class _EbrNportSnapDisp_Type(Integer32):
    """Custom type ebrNportSnapDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysFilter", 2),
          ("alwaysForward", 3),
          ("filter", 1))
    )


_EbrNportSnapDisp_Type.__name__ = "Integer32"
_EbrNportSnapDisp_Object = MibTableColumn
ebrNportSnapDisp = _EbrNportSnapDisp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 4, 1, 2),
    _EbrNportSnapDisp_Type()
)
ebrNportSnapDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapDisp.setStatus("mandatory")


class _EbrNportSnapStatus_Type(Integer32):
    """Custom type ebrNportSnapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportSnapStatus_Type.__name__ = "Integer32"
_EbrNportSnapStatus_Object = MibTableColumn
ebrNportSnapStatus = _EbrNportSnapStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 4, 1, 3),
    _EbrNportSnapStatus_Type()
)
ebrNportSnapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapStatus.setStatus("mandatory")
_EbrNportStaticDATable_Object = MibTable
ebrNportStaticDATable = _EbrNportStaticDATable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    ebrNportStaticDATable.setStatus("mandatory")
_EbrNportStaticDAEntry_Object = MibTableRow
ebrNportStaticDAEntry = _EbrNportStaticDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 5, 1)
)
ebrNportStaticDAEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportDAAddress"),
    (0, "DEC-ELAN-MIB", "ebrNportDAReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportStaticDAEntry.setStatus("mandatory")


class _EbrNportDAAddress_Type(OctetString):
    """Custom type ebrNportDAAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrNportDAAddress_Type.__name__ = "OctetString"
_EbrNportDAAddress_Object = MibTableColumn
ebrNportDAAddress = _EbrNportDAAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 5, 1, 1),
    _EbrNportDAAddress_Type()
)
ebrNportDAAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDAAddress.setStatus("mandatory")
_EbrNportDAReceivePort_Type = Integer32
_EbrNportDAReceivePort_Object = MibTableColumn
ebrNportDAReceivePort = _EbrNportDAReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 5, 1, 2),
    _EbrNportDAReceivePort_Type()
)
ebrNportDAReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDAReceivePort.setStatus("mandatory")


class _EbrNportDAAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportDAAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportDAAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportDAAllowedToGoTo_Object = MibTableColumn
ebrNportDAAllowedToGoTo = _EbrNportDAAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 5, 1, 3),
    _EbrNportDAAllowedToGoTo_Type()
)
ebrNportDAAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDAAllowedToGoTo.setStatus("mandatory")
_EbrNportStaticDAFilterCharacteristicsTable_Object = MibTable
ebrNportStaticDAFilterCharacteristicsTable = _EbrNportStaticDAFilterCharacteristicsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    ebrNportStaticDAFilterCharacteristicsTable.setStatus("mandatory")
_EbrNportStaticDAFilterCharacteristicsEntry_Object = MibTableRow
ebrNportStaticDAFilterCharacteristicsEntry = _EbrNportStaticDAFilterCharacteristicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 6, 1)
)
ebrNportStaticDAFilterCharacteristicsEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportDestinationAddress"),
)
if mibBuilder.loadTexts:
    ebrNportStaticDAFilterCharacteristicsEntry.setStatus("mandatory")


class _EbrNportDestinationAddress_Type(OctetString):
    """Custom type ebrNportDestinationAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrNportDestinationAddress_Type.__name__ = "OctetString"
_EbrNportDestinationAddress_Object = MibTableColumn
ebrNportDestinationAddress = _EbrNportDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 6, 1, 1),
    _EbrNportDestinationAddress_Type()
)
ebrNportDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDestinationAddress.setStatus("mandatory")


class _EbrNportDADisp_Type(Integer32):
    """Custom type ebrNportDADisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysFilter", 2),
          ("alwaysForward", 3),
          ("filter", 1))
    )


_EbrNportDADisp_Type.__name__ = "Integer32"
_EbrNportDADisp_Object = MibTableColumn
ebrNportDADisp = _EbrNportDADisp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 6, 1, 2),
    _EbrNportDADisp_Type()
)
ebrNportDADisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDADisp.setStatus("mandatory")


class _EbrNportDAStatus_Type(Integer32):
    """Custom type ebrNportDAStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_EbrNportDAStatus_Type.__name__ = "Integer32"
_EbrNportDAStatus_Object = MibTableColumn
ebrNportDAStatus = _EbrNportDAStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 6, 1, 3),
    _EbrNportDAStatus_Type()
)
ebrNportDAStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportDAStatus.setStatus("mandatory")
_EbrNportStaticSATable_Object = MibTable
ebrNportStaticSATable = _EbrNportStaticSATable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 7)
)
if mibBuilder.loadTexts:
    ebrNportStaticSATable.setStatus("mandatory")
_EbrNportStaticSAEntry_Object = MibTableRow
ebrNportStaticSAEntry = _EbrNportStaticSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 7, 1)
)
ebrNportStaticSAEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSAAddress"),
    (0, "DEC-ELAN-MIB", "ebrNportSAReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportStaticSAEntry.setStatus("mandatory")


class _EbrNportSAAddress_Type(OctetString):
    """Custom type ebrNportSAAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrNportSAAddress_Type.__name__ = "OctetString"
_EbrNportSAAddress_Object = MibTableColumn
ebrNportSAAddress = _EbrNportSAAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 7, 1, 1),
    _EbrNportSAAddress_Type()
)
ebrNportSAAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSAAddress.setStatus("mandatory")
_EbrNportSAReceivePort_Type = Integer32
_EbrNportSAReceivePort_Object = MibTableColumn
ebrNportSAReceivePort = _EbrNportSAReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 7, 1, 2),
    _EbrNportSAReceivePort_Type()
)
ebrNportSAReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSAReceivePort.setStatus("mandatory")


class _EbrNportSAAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportSAAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportSAAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportSAAllowedToGoTo_Object = MibTableColumn
ebrNportSAAllowedToGoTo = _EbrNportSAAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 7, 1, 3),
    _EbrNportSAAllowedToGoTo_Type()
)
ebrNportSAAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSAAllowedToGoTo.setStatus("mandatory")
_EbrNportStaticSAFilterCharacteristicsTable_Object = MibTable
ebrNportStaticSAFilterCharacteristicsTable = _EbrNportStaticSAFilterCharacteristicsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 8)
)
if mibBuilder.loadTexts:
    ebrNportStaticSAFilterCharacteristicsTable.setStatus("mandatory")
_EbrNportStaticSAFilterCharacteristicsEntry_Object = MibTableRow
ebrNportStaticSAFilterCharacteristicsEntry = _EbrNportStaticSAFilterCharacteristicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 8, 1)
)
ebrNportStaticSAFilterCharacteristicsEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSourceAddress"),
)
if mibBuilder.loadTexts:
    ebrNportStaticSAFilterCharacteristicsEntry.setStatus("mandatory")


class _EbrNportSourceAddress_Type(OctetString):
    """Custom type ebrNportSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrNportSourceAddress_Type.__name__ = "OctetString"
_EbrNportSourceAddress_Object = MibTableColumn
ebrNportSourceAddress = _EbrNportSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 8, 1, 1),
    _EbrNportSourceAddress_Type()
)
ebrNportSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSourceAddress.setStatus("mandatory")


class _EbrNportSADisp_Type(Integer32):
    """Custom type ebrNportSADisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alwaysFilter", 2),
          ("alwaysForward", 3),
          ("filter", 6),
          ("lockdown", 4),
          ("lockdownportmask", 5),
          ("portMask", 1))
    )


_EbrNportSADisp_Type.__name__ = "Integer32"
_EbrNportSADisp_Object = MibTableColumn
ebrNportSADisp = _EbrNportSADisp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 8, 1, 2),
    _EbrNportSADisp_Type()
)
ebrNportSADisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSADisp.setStatus("mandatory")


class _EbrNportSAStatus_Type(Integer32):
    """Custom type ebrNportSAStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_EbrNportSAStatus_Type.__name__ = "Integer32"
_EbrNportSAStatus_Object = MibTableColumn
ebrNportSAStatus = _EbrNportSAStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 8, 1, 3),
    _EbrNportSAStatus_Type()
)
ebrNportSAStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSAStatus.setStatus("mandatory")
_EbrNportSwTable_Object = MibTable
ebrNportSwTable = _EbrNportSwTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 9)
)
if mibBuilder.loadTexts:
    ebrNportSwTable.setStatus("mandatory")
_EbrNportSwEntry_Object = MibTableRow
ebrNportSwEntry = _EbrNportSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 9, 1)
)
ebrNportSwEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSwReceivePort"),
)
if mibBuilder.loadTexts:
    ebrNportSwEntry.setStatus("mandatory")
_EbrNportSwReceivePort_Type = Integer32
_EbrNportSwReceivePort_Object = MibTableColumn
ebrNportSwReceivePort = _EbrNportSwReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 9, 1, 1),
    _EbrNportSwReceivePort_Type()
)
ebrNportSwReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSwReceivePort.setStatus("mandatory")


class _EbrNportSwAllowedToGoTo_Type(OctetString):
    """Custom type ebrNportSwAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportSwAllowedToGoTo_Type.__name__ = "OctetString"
_EbrNportSwAllowedToGoTo_Object = MibTableColumn
ebrNportSwAllowedToGoTo = _EbrNportSwAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 9, 1, 2),
    _EbrNportSwAllowedToGoTo_Type()
)
ebrNportSwAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSwAllowedToGoTo.setStatus("mandatory")


class _EbrNportSwManualFilter_Type(OctetString):
    """Custom type ebrNportSwManualFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbrNportSwManualFilter_Type.__name__ = "OctetString"
_EbrNportSwManualFilter_Object = MibScalar
ebrNportSwManualFilter = _EbrNportSwManualFilter_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 2, 10),
    _EbrNportSwManualFilter_Type()
)
ebrNportSwManualFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSwManualFilter.setStatus("mandatory")
_EbrNportPortNumTable_Object = MibTable
ebrNportPortNumTable = _EbrNportPortNumTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ebrNportPortNumTable.setStatus("mandatory")
_EbrNportPortNumEntry_Object = MibTableRow
ebrNportPortNumEntry = _EbrNportPortNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 3, 1)
)
ebrNportPortNumEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportPortNumAddress"),
)
if mibBuilder.loadTexts:
    ebrNportPortNumEntry.setStatus("mandatory")


class _EbrNportPortNumAddress_Type(OctetString):
    """Custom type ebrNportPortNumAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrNportPortNumAddress_Type.__name__ = "OctetString"
_EbrNportPortNumAddress_Object = MibTableColumn
ebrNportPortNumAddress = _EbrNportPortNumAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 3, 1, 1),
    _EbrNportPortNumAddress_Type()
)
ebrNportPortNumAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportPortNumAddress.setStatus("mandatory")
_EbrNportPortNum_Type = Integer32
_EbrNportPortNum_Object = MibTableColumn
ebrNportPortNum = _EbrNportPortNum_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 3, 1, 2),
    _EbrNportPortNum_Type()
)
ebrNportPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportPortNum.setStatus("mandatory")


class _EbrNportPortNumStatus_Type(Integer32):
    """Custom type ebrNportPortNumStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportPortNumStatus_Type.__name__ = "Integer32"
_EbrNportPortNumStatus_Object = MibTableColumn
ebrNportPortNumStatus = _EbrNportPortNumStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 3, 1, 3),
    _EbrNportPortNumStatus_Type()
)
ebrNportPortNumStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportPortNumStatus.setStatus("mandatory")
_EbrNportFppnPortNum_Type = DisplayString
_EbrNportFppnPortNum_Object = MibTableColumn
ebrNportFppnPortNum = _EbrNportFppnPortNum_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 3, 1, 4),
    _EbrNportFppnPortNum_Type()
)
ebrNportFppnPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportFppnPortNum.setStatus("mandatory")
_ServiceClassAssignments_ObjectIdentity = ObjectIdentity
serviceClassAssignments = _ServiceClassAssignments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5)
)
_EbrNportSapSvcTable_Object = MibTable
ebrNportSapSvcTable = _EbrNportSapSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ebrNportSapSvcTable.setStatus("mandatory")
_EbrNportSapSvcEntry_Object = MibTableRow
ebrNportSapSvcEntry = _EbrNportSapSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 1, 1)
)
ebrNportSapSvcEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSapSvcSapValue"),
)
if mibBuilder.loadTexts:
    ebrNportSapSvcEntry.setStatus("mandatory")
_EbrNportSapSvcSapValue_Type = Integer32
_EbrNportSapSvcSapValue_Object = MibTableColumn
ebrNportSapSvcSapValue = _EbrNportSapSvcSapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 1, 1, 1),
    _EbrNportSapSvcSapValue_Type()
)
ebrNportSapSvcSapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapSvcSapValue.setStatus("mandatory")
_EbrNportSapSvc_Type = Integer32
_EbrNportSapSvc_Object = MibTableColumn
ebrNportSapSvc = _EbrNportSapSvc_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 1, 1, 2),
    _EbrNportSapSvc_Type()
)
ebrNportSapSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapSvc.setStatus("mandatory")


class _EbrNportSapSvcStatus_Type(Integer32):
    """Custom type ebrNportSapSvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportSapSvcStatus_Type.__name__ = "Integer32"
_EbrNportSapSvcStatus_Object = MibTableColumn
ebrNportSapSvcStatus = _EbrNportSapSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 1, 1, 3),
    _EbrNportSapSvcStatus_Type()
)
ebrNportSapSvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapSvcStatus.setStatus("mandatory")
_EbrNportSapSinglePath_Type = DisplayString
_EbrNportSapSinglePath_Object = MibTableColumn
ebrNportSapSinglePath = _EbrNportSapSinglePath_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 1, 1, 4),
    _EbrNportSapSinglePath_Type()
)
ebrNportSapSinglePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSapSinglePath.setStatus("mandatory")
_EbrNportSnapSvcTable_Object = MibTable
ebrNportSnapSvcTable = _EbrNportSnapSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ebrNportSnapSvcTable.setStatus("mandatory")
_EbrNportSnapSvcEntry_Object = MibTableRow
ebrNportSnapSvcEntry = _EbrNportSnapSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 2, 1)
)
ebrNportSnapSvcEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSnapSvcSnapValue"),
)
if mibBuilder.loadTexts:
    ebrNportSnapSvcEntry.setStatus("mandatory")


class _EbrNportSnapSvcSnapValue_Type(OctetString):
    """Custom type ebrNportSnapSvcSnapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EbrNportSnapSvcSnapValue_Type.__name__ = "OctetString"
_EbrNportSnapSvcSnapValue_Object = MibTableColumn
ebrNportSnapSvcSnapValue = _EbrNportSnapSvcSnapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 2, 1, 1),
    _EbrNportSnapSvcSnapValue_Type()
)
ebrNportSnapSvcSnapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapSvcSnapValue.setStatus("mandatory")
_EbrNportSnapSvc_Type = Integer32
_EbrNportSnapSvc_Object = MibTableColumn
ebrNportSnapSvc = _EbrNportSnapSvc_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 2, 1, 2),
    _EbrNportSnapSvc_Type()
)
ebrNportSnapSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapSvc.setStatus("mandatory")


class _EbrNportSnapSvcStatus_Type(Integer32):
    """Custom type ebrNportSnapSvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportSnapSvcStatus_Type.__name__ = "Integer32"
_EbrNportSnapSvcStatus_Object = MibTableColumn
ebrNportSnapSvcStatus = _EbrNportSnapSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 2, 1, 3),
    _EbrNportSnapSvcStatus_Type()
)
ebrNportSnapSvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapSvcStatus.setStatus("mandatory")
_EbrNportSnapSinglePath_Type = DisplayString
_EbrNportSnapSinglePath_Object = MibTableColumn
ebrNportSnapSinglePath = _EbrNportSnapSinglePath_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 2, 1, 4),
    _EbrNportSnapSinglePath_Type()
)
ebrNportSnapSinglePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSnapSinglePath.setStatus("mandatory")
_EbrNportDASvcTable_Object = MibTable
ebrNportDASvcTable = _EbrNportDASvcTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 3)
)
if mibBuilder.loadTexts:
    ebrNportDASvcTable.setStatus("mandatory")
_EbrNportDASvcEntry_Object = MibTableRow
ebrNportDASvcEntry = _EbrNportDASvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 3, 1)
)
ebrNportDASvcEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNportSvcAddress"),
)
if mibBuilder.loadTexts:
    ebrNportDASvcEntry.setStatus("mandatory")


class _EbrNportSvcAddress_Type(OctetString):
    """Custom type ebrNportSvcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrNportSvcAddress_Type.__name__ = "OctetString"
_EbrNportSvcAddress_Object = MibTableColumn
ebrNportSvcAddress = _EbrNportSvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 3, 1, 1),
    _EbrNportSvcAddress_Type()
)
ebrNportSvcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSvcAddress.setStatus("mandatory")
_EbrNportSvc_Type = Integer32
_EbrNportSvc_Object = MibTableColumn
ebrNportSvc = _EbrNportSvc_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 3, 1, 2),
    _EbrNportSvc_Type()
)
ebrNportSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSvc.setStatus("mandatory")


class _EbrNportSvcStatus_Type(Integer32):
    """Custom type ebrNportSvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("permanent", 2))
    )


_EbrNportSvcStatus_Type.__name__ = "Integer32"
_EbrNportSvcStatus_Object = MibTableColumn
ebrNportSvcStatus = _EbrNportSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 5, 3, 1, 3),
    _EbrNportSvcStatus_Type()
)
ebrNportSvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNportSvcStatus.setStatus("mandatory")
_Flooding_ObjectIdentity = ObjectIdentity
flooding = _Flooding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6)
)
_FloodUnknownUnicastRate_Type = Integer32
_FloodUnknownUnicastRate_Object = MibScalar
floodUnknownUnicastRate = _FloodUnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 1),
    _FloodUnknownUnicastRate_Type()
)
floodUnknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    floodUnknownUnicastRate.setStatus("mandatory")
_FloodMulticastRate_Type = Integer32
_FloodMulticastRate_Object = MibScalar
floodMulticastRate = _FloodMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 2),
    _FloodMulticastRate_Type()
)
floodMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    floodMulticastRate.setStatus("mandatory")
_FloodTable_Object = MibTable
floodTable = _FloodTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    floodTable.setStatus("mandatory")
_FloodEntry_Object = MibTableRow
floodEntry = _FloodEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1)
)
floodEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "floodQuotaQualifier"),
    (0, "DEC-ELAN-MIB", "floodQuotaClass"),
)
if mibBuilder.loadTexts:
    floodEntry.setStatus("mandatory")
_FloodQuotaQualifier_Type = Integer32
_FloodQuotaQualifier_Object = MibTableColumn
floodQuotaQualifier = _FloodQuotaQualifier_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 1),
    _FloodQuotaQualifier_Type()
)
floodQuotaQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodQuotaQualifier.setStatus("mandatory")
_FloodQuotaClass_Type = Integer32
_FloodQuotaClass_Object = MibTableColumn
floodQuotaClass = _FloodQuotaClass_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 2),
    _FloodQuotaClass_Type()
)
floodQuotaClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodQuotaClass.setStatus("mandatory")
_FloodBytesSent_Type = Counter32
_FloodBytesSent_Object = MibTableColumn
floodBytesSent = _FloodBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 3),
    _FloodBytesSent_Type()
)
floodBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodBytesSent.setStatus("mandatory")
_FloodPacketsSent_Type = Counter32
_FloodPacketsSent_Object = MibTableColumn
floodPacketsSent = _FloodPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 4),
    _FloodPacketsSent_Type()
)
floodPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodPacketsSent.setStatus("mandatory")
_FloodGeezers_Type = Counter32
_FloodGeezers_Object = MibTableColumn
floodGeezers = _FloodGeezers_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 5),
    _FloodGeezers_Type()
)
floodGeezers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodGeezers.setStatus("mandatory")
_FloodLosers_Type = Counter32
_FloodLosers_Object = MibTableColumn
floodLosers = _FloodLosers_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 6),
    _FloodLosers_Type()
)
floodLosers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodLosers.setStatus("mandatory")
_FloodHogs_Type = Counter32
_FloodHogs_Object = MibTableColumn
floodHogs = _FloodHogs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 7),
    _FloodHogs_Type()
)
floodHogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodHogs.setStatus("mandatory")
_FloodSinglePathDiscards_Type = Counter32
_FloodSinglePathDiscards_Object = MibTableColumn
floodSinglePathDiscards = _FloodSinglePathDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 8),
    _FloodSinglePathDiscards_Type()
)
floodSinglePathDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodSinglePathDiscards.setStatus("mandatory")
_FloodPacketsFiltered_Type = Counter32
_FloodPacketsFiltered_Object = MibTableColumn
floodPacketsFiltered = _FloodPacketsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 9),
    _FloodPacketsFiltered_Type()
)
floodPacketsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodPacketsFiltered.setStatus("mandatory")
_FloodPacketsPurged_Type = Counter32
_FloodPacketsPurged_Object = MibTableColumn
floodPacketsPurged = _FloodPacketsPurged_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 10),
    _FloodPacketsPurged_Type()
)
floodPacketsPurged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodPacketsPurged.setStatus("mandatory")
_FloodBytesPurged_Type = Counter32
_FloodBytesPurged_Object = MibTableColumn
floodBytesPurged = _FloodBytesPurged_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 11),
    _FloodBytesPurged_Type()
)
floodBytesPurged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodBytesPurged.setStatus("mandatory")
_FloodLocalCopyPacketsDelivered_Type = Counter32
_FloodLocalCopyPacketsDelivered_Object = MibTableColumn
floodLocalCopyPacketsDelivered = _FloodLocalCopyPacketsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 12),
    _FloodLocalCopyPacketsDelivered_Type()
)
floodLocalCopyPacketsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodLocalCopyPacketsDelivered.setStatus("mandatory")
_FloodLocalCopyPacketsDiscarded_Type = Counter32
_FloodLocalCopyPacketsDiscarded_Object = MibTableColumn
floodLocalCopyPacketsDiscarded = _FloodLocalCopyPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 6, 3, 1, 13),
    _FloodLocalCopyPacketsDiscarded_Type()
)
floodLocalCopyPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floodLocalCopyPacketsDiscarded.setStatus("mandatory")
_CutThrough_ObjectIdentity = ObjectIdentity
cutThrough = _CutThrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7)
)
_CutThroughTable_Object = MibTable
cutThroughTable = _CutThroughTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cutThroughTable.setStatus("mandatory")
_CutThroughEntry_Object = MibTableRow
cutThroughEntry = _CutThroughEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 1, 1)
)
cutThroughEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "cutThroughBridgePort"),
)
if mibBuilder.loadTexts:
    cutThroughEntry.setStatus("mandatory")
_CutThroughBridgePort_Type = Integer32
_CutThroughBridgePort_Object = MibTableColumn
cutThroughBridgePort = _CutThroughBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 1, 1, 1),
    _CutThroughBridgePort_Type()
)
cutThroughBridgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cutThroughBridgePort.setStatus("mandatory")


class _CutThroughInbound_Type(Integer32):
    """Custom type cutThroughInbound based on Integer32"""
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


_CutThroughInbound_Type.__name__ = "Integer32"
_CutThroughInbound_Object = MibTableColumn
cutThroughInbound = _CutThroughInbound_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 1, 1, 2),
    _CutThroughInbound_Type()
)
cutThroughInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cutThroughInbound.setStatus("mandatory")


class _CutThroughOutbound_Type(Integer32):
    """Custom type cutThroughOutbound based on Integer32"""
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


_CutThroughOutbound_Type.__name__ = "Integer32"
_CutThroughOutbound_Object = MibTableColumn
cutThroughOutbound = _CutThroughOutbound_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 1, 1, 3),
    _CutThroughOutbound_Type()
)
cutThroughOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cutThroughOutbound.setStatus("mandatory")
_CutThroughFppnTable_Object = MibTable
cutThroughFppnTable = _CutThroughFppnTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    cutThroughFppnTable.setStatus("mandatory")
_CutThroughFppnEntry_Object = MibTableRow
cutThroughFppnEntry = _CutThroughFppnEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 2, 1)
)
cutThroughFppnEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "cutThroughFppnPort"),
)
if mibBuilder.loadTexts:
    cutThroughFppnEntry.setStatus("mandatory")
_CutThroughFppnPort_Type = DisplayString
_CutThroughFppnPort_Object = MibTableColumn
cutThroughFppnPort = _CutThroughFppnPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 2, 1, 1),
    _CutThroughFppnPort_Type()
)
cutThroughFppnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cutThroughFppnPort.setStatus("mandatory")


class _CutThroughFppnInbound_Type(Integer32):
    """Custom type cutThroughFppnInbound based on Integer32"""
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


_CutThroughFppnInbound_Type.__name__ = "Integer32"
_CutThroughFppnInbound_Object = MibTableColumn
cutThroughFppnInbound = _CutThroughFppnInbound_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 2, 1, 2),
    _CutThroughFppnInbound_Type()
)
cutThroughFppnInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cutThroughFppnInbound.setStatus("mandatory")


class _CutThroughFppnOutbound_Type(Integer32):
    """Custom type cutThroughFppnOutbound based on Integer32"""
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


_CutThroughFppnOutbound_Type.__name__ = "Integer32"
_CutThroughFppnOutbound_Object = MibTableColumn
cutThroughFppnOutbound = _CutThroughFppnOutbound_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 7, 2, 1, 3),
    _CutThroughFppnOutbound_Type()
)
cutThroughFppnOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cutThroughFppnOutbound.setStatus("mandatory")
_GigaStp_ObjectIdentity = ObjectIdentity
gigaStp = _GigaStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 8)
)
_GigaStpPortTable_Object = MibTable
gigaStpPortTable = _GigaStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 8, 1)
)
if mibBuilder.loadTexts:
    gigaStpPortTable.setStatus("mandatory")
_GigaStpPortEntry_Object = MibTableRow
gigaStpPortEntry = _GigaStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 8, 1, 1)
)
gigaStpPortEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "gigaStpPortIfIndex"),
)
if mibBuilder.loadTexts:
    gigaStpPortEntry.setStatus("mandatory")
_GigaStpPortIfIndex_Type = Integer32
_GigaStpPortIfIndex_Object = MibTableColumn
gigaStpPortIfIndex = _GigaStpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 8, 1, 1, 1),
    _GigaStpPortIfIndex_Type()
)
gigaStpPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigaStpPortIfIndex.setStatus("mandatory")


class _GigaStpPortSpanningTreeEnable_Type(Integer32):
    """Custom type gigaStpPortSpanningTreeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("trueNoDelay", 3))
    )


_GigaStpPortSpanningTreeEnable_Type.__name__ = "Integer32"
_GigaStpPortSpanningTreeEnable_Object = MibTableColumn
gigaStpPortSpanningTreeEnable = _GigaStpPortSpanningTreeEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 8, 1, 1, 2),
    _GigaStpPortSpanningTreeEnable_Type()
)
gigaStpPortSpanningTreeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigaStpPortSpanningTreeEnable.setStatus("mandatory")


class _GigaStpDemandLearningEnable_Type(Integer32):
    """Custom type gigaStpDemandLearningEnable based on Integer32"""
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


_GigaStpDemandLearningEnable_Type.__name__ = "Integer32"
_GigaStpDemandLearningEnable_Object = MibScalar
gigaStpDemandLearningEnable = _GigaStpDemandLearningEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 8, 2),
    _GigaStpDemandLearningEnable_Type()
)
gigaStpDemandLearningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigaStpDemandLearningEnable.setStatus("mandatory")
_TranslationTableParams_ObjectIdentity = ObjectIdentity
translationTableParams = _TranslationTableParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 9)
)
_TtSize_Type = Integer32
_TtSize_Object = MibScalar
ttSize = _TtSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 9, 1),
    _TtSize_Type()
)
ttSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttSize.setStatus("mandatory")
_XacInDiscardCounters_ObjectIdentity = ObjectIdentity
xacInDiscardCounters = _XacInDiscardCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 10)
)
_XacInDiscardUnknownDAUCast_Type = Counter32
_XacInDiscardUnknownDAUCast_Object = MibScalar
xacInDiscardUnknownDAUCast = _XacInDiscardUnknownDAUCast_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 10, 1),
    _XacInDiscardUnknownDAUCast_Type()
)
xacInDiscardUnknownDAUCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xacInDiscardUnknownDAUCast.setStatus("mandatory")
_XacInDiscardMulticast_Type = Counter32
_XacInDiscardMulticast_Object = MibScalar
xacInDiscardMulticast = _XacInDiscardMulticast_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 10, 2),
    _XacInDiscardMulticast_Type()
)
xacInDiscardMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xacInDiscardMulticast.setStatus("mandatory")
_XacInDiscardIPForwarding_Type = Counter32
_XacInDiscardIPForwarding_Object = MibScalar
xacInDiscardIPForwarding = _XacInDiscardIPForwarding_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 10, 3),
    _XacInDiscardIPForwarding_Type()
)
xacInDiscardIPForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xacInDiscardIPForwarding.setStatus("mandatory")
_CommunityString_ObjectIdentity = ObjectIdentity
communityString = _CommunityString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 11)
)


class _CommunityStringDelimiter_Type(OctetString):
    """Custom type communityStringDelimiter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CommunityStringDelimiter_Type.__name__ = "OctetString"
_CommunityStringDelimiter_Object = MibScalar
communityStringDelimiter = _CommunityStringDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 2, 11, 1),
    _CommunityStringDelimiter_Type()
)
communityStringDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityStringDelimiter.setStatus("mandatory")
_GigaUpgradeSoftware_ObjectIdentity = ObjectIdentity
gigaUpgradeSoftware = _GigaUpgradeSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3)
)
_DoTransfer_ObjectIdentity = ObjectIdentity
doTransfer = _DoTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 1)
)
_TftpDestination_Type = IpAddress
_TftpDestination_Object = MibScalar
tftpDestination = _TftpDestination_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 1, 1),
    _TftpDestination_Type()
)
tftpDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDestination.setStatus("mandatory")


class _MopDestination_Type(OctetString):
    """Custom type mopDestination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MopDestination_Type.__name__ = "OctetString"
_MopDestination_Object = MibScalar
mopDestination = _MopDestination_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 1, 2),
    _MopDestination_Type()
)
mopDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mopDestination.setStatus("mandatory")
_TransferFileName_Type = DisplayString
_TransferFileName_Object = MibScalar
transferFileName = _TransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 1, 3),
    _TransferFileName_Type()
)
transferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferFileName.setStatus("mandatory")


class _TransferAction_Type(Integer32):
    """Custom type transferAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doMOP", 2),
          ("doTFTP", 3),
          ("none", 1))
    )


_TransferAction_Type.__name__ = "Integer32"
_TransferAction_Object = MibScalar
transferAction = _TransferAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 1, 4),
    _TransferAction_Type()
)
transferAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferAction.setStatus("mandatory")


class _TransferStatus_Type(Integer32):
    """Custom type transferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("failedDueToCheckSum", 6),
          ("inProgress", 3),
          ("none", 1),
          ("requested", 2),
          ("success", 5))
    )


_TransferStatus_Type.__name__ = "Integer32"
_TransferStatus_Object = MibScalar
transferStatus = _TransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 1, 5),
    _TransferStatus_Type()
)
transferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatus.setStatus("mandatory")
_TransferSize_Type = Integer32
_TransferSize_Object = MibScalar
transferSize = _TransferSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 1, 6),
    _TransferSize_Type()
)
transferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSize.setStatus("mandatory")
_UseTransfer_ObjectIdentity = ObjectIdentity
useTransfer = _UseTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 2)
)
_CopyToSlot_Type = Integer32
_CopyToSlot_Object = MibScalar
copyToSlot = _CopyToSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 2, 1),
    _CopyToSlot_Type()
)
copyToSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyToSlot.setStatus("mandatory")


class _CopyType_Type(Integer32):
    """Custom type copyType based on Integer32"""
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
        *(("agl-2", 6),
          ("agl-2-plus", 8),
          ("clock", 4),
          ("fgl2", 3),
          ("fgl4", 7),
          ("none", 1),
          ("powerSystemController", 5),
          ("scp", 2))
    )


_CopyType_Type.__name__ = "Integer32"
_CopyType_Object = MibScalar
copyType = _CopyType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 2, 2),
    _CopyType_Type()
)
copyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyType.setStatus("mandatory")


class _CopyAction_Type(Integer32):
    """Custom type copyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doUpgrade", 2),
          ("none", 1))
    )


_CopyAction_Type.__name__ = "Integer32"
_CopyAction_Object = MibScalar
copyAction = _CopyAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 2, 3),
    _CopyAction_Type()
)
copyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyAction.setStatus("mandatory")


class _CopyStatus_Type(Integer32):
    """Custom type copyStatus based on Integer32"""
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
        *(("failed", 4),
          ("failedDueToBadImage", 9),
          ("failedDueToCardType", 6),
          ("failedDueToFwRev", 8),
          ("failedDueToHwRev", 7),
          ("inProgress", 3),
          ("none", 1),
          ("requested", 2),
          ("success", 5))
    )


_CopyStatus_Type.__name__ = "Integer32"
_CopyStatus_Object = MibScalar
copyStatus = _CopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 2, 4),
    _CopyStatus_Type()
)
copyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyStatus.setStatus("mandatory")


class _DeleteTransfer_Type(Integer32):
    """Custom type deleteTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("notExist", 2))
    )


_DeleteTransfer_Type.__name__ = "Integer32"
_DeleteTransfer_Object = MibScalar
deleteTransfer = _DeleteTransfer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 3, 3),
    _DeleteTransfer_Type()
)
deleteTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deleteTransfer.setStatus("mandatory")
_GigaIP_ObjectIdentity = ObjectIdentity
gigaIP = _GigaIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4)
)
_ArpTimingMechanism_ObjectIdentity = ObjectIdentity
arpTimingMechanism = _ArpTimingMechanism_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 1)
)
_ArpTimeoutInSeconds_Type = Integer32
_ArpTimeoutInSeconds_Object = MibScalar
arpTimeoutInSeconds = _ArpTimeoutInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 1, 1),
    _ArpTimeoutInSeconds_Type()
)
arpTimeoutInSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpTimeoutInSeconds.setStatus("mandatory")
_ArpPeriodBetweenRequests_Type = Integer32
_ArpPeriodBetweenRequests_Object = MibScalar
arpPeriodBetweenRequests = _ArpPeriodBetweenRequests_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 1, 2),
    _ArpPeriodBetweenRequests_Type()
)
arpPeriodBetweenRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpPeriodBetweenRequests.setStatus("mandatory")
_ArpRequestRetries_Type = Integer32
_ArpRequestRetries_Object = MibScalar
arpRequestRetries = _ArpRequestRetries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 1, 3),
    _ArpRequestRetries_Type()
)
arpRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpRequestRetries.setStatus("mandatory")
_SnmpParameters_ObjectIdentity = ObjectIdentity
snmpParameters = _SnmpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 2)
)
_SnmpDuplicateDiscardInterval_Type = Integer32
_SnmpDuplicateDiscardInterval_Object = MibScalar
snmpDuplicateDiscardInterval = _SnmpDuplicateDiscardInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 2, 1),
    _SnmpDuplicateDiscardInterval_Type()
)
snmpDuplicateDiscardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDuplicateDiscardInterval.setStatus("mandatory")
_ArpControlParams_ObjectIdentity = ObjectIdentity
arpControlParams = _ArpControlParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 3)
)


class _ArpAgent_Type(Integer32):
    """Custom type arpAgent based on Integer32"""
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


_ArpAgent_Type.__name__ = "Integer32"
_ArpAgent_Object = MibScalar
arpAgent = _ArpAgent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 3, 1),
    _ArpAgent_Type()
)
arpAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpAgent.setStatus("mandatory")
_ArpStatisticalCounters_ObjectIdentity = ObjectIdentity
arpStatisticalCounters = _ArpStatisticalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4)
)
_ArpStatisticalTable_Object = MibTable
arpStatisticalTable = _ArpStatisticalTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    arpStatisticalTable.setStatus("mandatory")
_ArpStatisticalEntry_Object = MibTableRow
arpStatisticalEntry = _ArpStatisticalEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4, 1, 1)
)
arpStatisticalEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "arpStatisticalIfIndex"),
)
if mibBuilder.loadTexts:
    arpStatisticalEntry.setStatus("mandatory")
_ArpStatisticalIfIndex_Type = Integer32
_ArpStatisticalIfIndex_Object = MibTableColumn
arpStatisticalIfIndex = _ArpStatisticalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4, 1, 1, 1),
    _ArpStatisticalIfIndex_Type()
)
arpStatisticalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatisticalIfIndex.setStatus("mandatory")
_ArpUnicastReceived_Type = Counter32
_ArpUnicastReceived_Object = MibTableColumn
arpUnicastReceived = _ArpUnicastReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4, 1, 1, 2),
    _ArpUnicastReceived_Type()
)
arpUnicastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpUnicastReceived.setStatus("mandatory")
_ArpBroadcastReceived_Type = Counter32
_ArpBroadcastReceived_Object = MibTableColumn
arpBroadcastReceived = _ArpBroadcastReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4, 1, 1, 3),
    _ArpBroadcastReceived_Type()
)
arpBroadcastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpBroadcastReceived.setStatus("mandatory")
_ArpRepliesTransmitted_Type = Counter32
_ArpRepliesTransmitted_Object = MibTableColumn
arpRepliesTransmitted = _ArpRepliesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4, 1, 1, 4),
    _ArpRepliesTransmitted_Type()
)
arpRepliesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpRepliesTransmitted.setStatus("mandatory")
_ArpFramesFlooded_Type = Counter32
_ArpFramesFlooded_Object = MibTableColumn
arpFramesFlooded = _ArpFramesFlooded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4, 1, 1, 5),
    _ArpFramesFlooded_Type()
)
arpFramesFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpFramesFlooded.setStatus("mandatory")
_ArpFramesDiscarded_Type = Counter32
_ArpFramesDiscarded_Object = MibTableColumn
arpFramesDiscarded = _ArpFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 4, 1, 1, 6),
    _ArpFramesDiscarded_Type()
)
arpFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpFramesDiscarded.setStatus("mandatory")
_IpSwitching_ObjectIdentity = ObjectIdentity
ipSwitching = _IpSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5)
)


class _IpSwitchEnable_Type(Integer32):
    """Custom type ipSwitchEnable based on Integer32"""
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


_IpSwitchEnable_Type.__name__ = "Integer32"
_IpSwitchEnable_Object = MibScalar
ipSwitchEnable = _IpSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 1),
    _IpSwitchEnable_Type()
)
ipSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSwitchEnable.setStatus("mandatory")
_IpSwitchPortsTable_Object = MibTable
ipSwitchPortsTable = _IpSwitchPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ipSwitchPortsTable.setStatus("mandatory")
_IpSwitchPortsEntry_Object = MibTableRow
ipSwitchPortsEntry = _IpSwitchPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 2, 1)
)
ipSwitchPortsEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ipRangeStartAddr"),
    (0, "DEC-ELAN-MIB", "ipRangeEndAddr"),
)
if mibBuilder.loadTexts:
    ipSwitchPortsEntry.setStatus("mandatory")
_IpRangeStartAddr_Type = IpAddress
_IpRangeStartAddr_Object = MibTableColumn
ipRangeStartAddr = _IpRangeStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 2, 1, 1),
    _IpRangeStartAddr_Type()
)
ipRangeStartAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRangeStartAddr.setStatus("mandatory")
_IpRangeEndAddr_Type = IpAddress
_IpRangeEndAddr_Object = MibTableColumn
ipRangeEndAddr = _IpRangeEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 2, 1, 2),
    _IpRangeEndAddr_Type()
)
ipRangeEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRangeEndAddr.setStatus("mandatory")
_IpIPAddr_Type = IpAddress
_IpIPAddr_Object = MibTableColumn
ipIPAddr = _IpIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 2, 1, 3),
    _IpIPAddr_Type()
)
ipIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIPAddr.setStatus("mandatory")
_IpStaticPorts_Type = DisplayString
_IpStaticPorts_Object = MibTableColumn
ipStaticPorts = _IpStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 2, 1, 4),
    _IpStaticPorts_Type()
)
ipStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticPorts.setStatus("mandatory")
_IpDynamicPorts_Type = DisplayString
_IpDynamicPorts_Object = MibTableColumn
ipDynamicPorts = _IpDynamicPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 2, 1, 5),
    _IpDynamicPorts_Type()
)
ipDynamicPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicPorts.setStatus("mandatory")
_IpPrimaryPorts_Type = DisplayString
_IpPrimaryPorts_Object = MibScalar
ipPrimaryPorts = _IpPrimaryPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 3),
    _IpPrimaryPorts_Type()
)
ipPrimaryPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPrimaryPorts.setStatus("mandatory")
_IpDynamicPrimaryPorts_Type = DisplayString
_IpDynamicPrimaryPorts_Object = MibScalar
ipDynamicPrimaryPorts = _IpDynamicPrimaryPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 4),
    _IpDynamicPrimaryPorts_Type()
)
ipDynamicPrimaryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicPrimaryPorts.setStatus("mandatory")
_IpDynamicEnabledPorts_Type = DisplayString
_IpDynamicEnabledPorts_Object = MibScalar
ipDynamicEnabledPorts = _IpDynamicEnabledPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 4, 5, 5),
    _IpDynamicEnabledPorts_Type()
)
ipDynamicEnabledPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDynamicEnabledPorts.setStatus("mandatory")
_GigaSets_ObjectIdentity = ObjectIdentity
gigaSets = _GigaSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5)
)
_PortGroupMembershipTable_Object = MibTable
portGroupMembershipTable = _PortGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    portGroupMembershipTable.setStatus("mandatory")
_PortGroupMembershipEntry_Object = MibTableRow
portGroupMembershipEntry = _PortGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 1, 1)
)
portGroupMembershipEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "portGroupBridgePort"),
)
if mibBuilder.loadTexts:
    portGroupMembershipEntry.setStatus("mandatory")
_PortGroupBridgePort_Type = Integer32
_PortGroupBridgePort_Object = MibTableColumn
portGroupBridgePort = _PortGroupBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 1, 1, 1),
    _PortGroupBridgePort_Type()
)
portGroupBridgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupBridgePort.setStatus("mandatory")
_PortGroupMembership_Type = DisplayString
_PortGroupMembership_Object = MibTableColumn
portGroupMembership = _PortGroupMembership_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 1, 1, 2),
    _PortGroupMembership_Type()
)
portGroupMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupMembership.setStatus("mandatory")
_PortGroupMembershipWorkBuf_Type = DisplayString
_PortGroupMembershipWorkBuf_Object = MibTableColumn
portGroupMembershipWorkBuf = _PortGroupMembershipWorkBuf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 1, 1, 3),
    _PortGroupMembershipWorkBuf_Type()
)
portGroupMembershipWorkBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupMembershipWorkBuf.setStatus("mandatory")


class _PortGroupPortType_Type(Integer32):
    """Custom type portGroupPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("huntGroup", 1),
          ("reliabilityGroup", 2))
    )


_PortGroupPortType_Type.__name__ = "Integer32"
_PortGroupPortType_Object = MibTableColumn
portGroupPortType = _PortGroupPortType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 1, 1, 4),
    _PortGroupPortType_Type()
)
portGroupPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupPortType.setStatus("mandatory")


class _PortGroupPortTypeWorkBuf_Type(Integer32):
    """Custom type portGroupPortTypeWorkBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("huntGroup", 1),
          ("reliabilityGroup", 2))
    )


_PortGroupPortTypeWorkBuf_Type.__name__ = "Integer32"
_PortGroupPortTypeWorkBuf_Object = MibTableColumn
portGroupPortTypeWorkBuf = _PortGroupPortTypeWorkBuf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 1, 1, 5),
    _PortGroupPortTypeWorkBuf_Type()
)
portGroupPortTypeWorkBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupPortTypeWorkBuf.setStatus("mandatory")


class _PortGroupPortOperStatus_Type(Integer32):
    """Custom type portGroupPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 3),
          ("preBridging", 2),
          ("uninitializedPort", 1))
    )


_PortGroupPortOperStatus_Type.__name__ = "Integer32"
_PortGroupPortOperStatus_Object = MibTableColumn
portGroupPortOperStatus = _PortGroupPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 1, 1, 6),
    _PortGroupPortOperStatus_Type()
)
portGroupPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupPortOperStatus.setStatus("mandatory")
_PortGroupFppnMembershipTable_Object = MibTable
portGroupFppnMembershipTable = _PortGroupFppnMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    portGroupFppnMembershipTable.setStatus("mandatory")
_PortGroupFppnMembershipEntry_Object = MibTableRow
portGroupFppnMembershipEntry = _PortGroupFppnMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 2, 1)
)
portGroupFppnMembershipEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "portGroupFppnPort"),
)
if mibBuilder.loadTexts:
    portGroupFppnMembershipEntry.setStatus("mandatory")
_PortGroupFppnPort_Type = DisplayString
_PortGroupFppnPort_Object = MibTableColumn
portGroupFppnPort = _PortGroupFppnPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 2, 1, 1),
    _PortGroupFppnPort_Type()
)
portGroupFppnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupFppnPort.setStatus("mandatory")
_PortGroupFppnMembership_Type = DisplayString
_PortGroupFppnMembership_Object = MibTableColumn
portGroupFppnMembership = _PortGroupFppnMembership_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 2, 1, 2),
    _PortGroupFppnMembership_Type()
)
portGroupFppnMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupFppnMembership.setStatus("mandatory")
_PortGroupFppnMembershipWorkBuf_Type = DisplayString
_PortGroupFppnMembershipWorkBuf_Object = MibTableColumn
portGroupFppnMembershipWorkBuf = _PortGroupFppnMembershipWorkBuf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 2, 1, 3),
    _PortGroupFppnMembershipWorkBuf_Type()
)
portGroupFppnMembershipWorkBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupFppnMembershipWorkBuf.setStatus("mandatory")


class _PortGroupFppnPortType_Type(Integer32):
    """Custom type portGroupFppnPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("huntGroup", 1),
          ("reliabilityGroup", 2))
    )


_PortGroupFppnPortType_Type.__name__ = "Integer32"
_PortGroupFppnPortType_Object = MibTableColumn
portGroupFppnPortType = _PortGroupFppnPortType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 2, 1, 4),
    _PortGroupFppnPortType_Type()
)
portGroupFppnPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupFppnPortType.setStatus("mandatory")


class _PortGroupFppnPortTypeWorkBuf_Type(Integer32):
    """Custom type portGroupFppnPortTypeWorkBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("huntGroup", 1),
          ("reliabilityGroup", 2))
    )


_PortGroupFppnPortTypeWorkBuf_Type.__name__ = "Integer32"
_PortGroupFppnPortTypeWorkBuf_Object = MibTableColumn
portGroupFppnPortTypeWorkBuf = _PortGroupFppnPortTypeWorkBuf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 2, 1, 5),
    _PortGroupFppnPortTypeWorkBuf_Type()
)
portGroupFppnPortTypeWorkBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupFppnPortTypeWorkBuf.setStatus("mandatory")


class _PortGroupFppnPortOperStatus_Type(Integer32):
    """Custom type portGroupFppnPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 3),
          ("preBridging", 2),
          ("uninitializedPort", 1))
    )


_PortGroupFppnPortOperStatus_Type.__name__ = "Integer32"
_PortGroupFppnPortOperStatus_Object = MibTableColumn
portGroupFppnPortOperStatus = _PortGroupFppnPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 2, 1, 6),
    _PortGroupFppnPortOperStatus_Type()
)
portGroupFppnPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupFppnPortOperStatus.setStatus("mandatory")
_PortGroupStatusTable_Object = MibTable
portGroupStatusTable = _PortGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 3)
)
if mibBuilder.loadTexts:
    portGroupStatusTable.setStatus("mandatory")
_PortGroupStatusEntry_Object = MibTableRow
portGroupStatusEntry = _PortGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 3, 1)
)
portGroupStatusEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "portGroupStatusBridgePort"),
)
if mibBuilder.loadTexts:
    portGroupStatusEntry.setStatus("mandatory")
_PortGroupStatusBridgePort_Type = Integer32
_PortGroupStatusBridgePort_Object = MibTableColumn
portGroupStatusBridgePort = _PortGroupStatusBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 3, 1, 1),
    _PortGroupStatusBridgePort_Type()
)
portGroupStatusBridgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupStatusBridgePort.setStatus("mandatory")
_PortGroupStatusPortNumber_Type = Integer32
_PortGroupStatusPortNumber_Object = MibTableColumn
portGroupStatusPortNumber = _PortGroupStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 3, 1, 2),
    _PortGroupStatusPortNumber_Type()
)
portGroupStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupStatusPortNumber.setStatus("mandatory")


class _PortGroupStatusPortType_Type(Integer32):
    """Custom type portGroupStatusPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("huntGroupMember", 2),
          ("reliabilityGroupMember", 3),
          ("singleton", 1))
    )


_PortGroupStatusPortType_Type.__name__ = "Integer32"
_PortGroupStatusPortType_Object = MibTableColumn
portGroupStatusPortType = _PortGroupStatusPortType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 3, 1, 3),
    _PortGroupStatusPortType_Type()
)
portGroupStatusPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupStatusPortType.setStatus("mandatory")


class _PortGroupStatusOperStatus_Type(Integer32):
    """Custom type portGroupStatusOperStatus based on Integer32"""
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
        *(("bridging", 4),
          ("portInitializing", 2),
          ("preBridging", 3),
          ("uninitializedPort", 1))
    )


_PortGroupStatusOperStatus_Type.__name__ = "Integer32"
_PortGroupStatusOperStatus_Object = MibTableColumn
portGroupStatusOperStatus = _PortGroupStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 3, 1, 4),
    _PortGroupStatusOperStatus_Type()
)
portGroupStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupStatusOperStatus.setStatus("mandatory")
_LearningDomainMembershipTable_Object = MibTable
learningDomainMembershipTable = _LearningDomainMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 4)
)
if mibBuilder.loadTexts:
    learningDomainMembershipTable.setStatus("mandatory")
_LearningDomainMembershipEntry_Object = MibTableRow
learningDomainMembershipEntry = _LearningDomainMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 4, 1)
)
learningDomainMembershipEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "learningDomainNumber"),
)
if mibBuilder.loadTexts:
    learningDomainMembershipEntry.setStatus("mandatory")
_LearningDomainNumber_Type = Integer32
_LearningDomainNumber_Object = MibTableColumn
learningDomainNumber = _LearningDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 4, 1, 1),
    _LearningDomainNumber_Type()
)
learningDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learningDomainNumber.setStatus("mandatory")
_LearningDomainMembership_Type = DisplayString
_LearningDomainMembership_Object = MibTableColumn
learningDomainMembership = _LearningDomainMembership_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 4, 1, 2),
    _LearningDomainMembership_Type()
)
learningDomainMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learningDomainMembership.setStatus("mandatory")
_LearningDomainMembershipWorkBuf_Type = DisplayString
_LearningDomainMembershipWorkBuf_Object = MibTableColumn
learningDomainMembershipWorkBuf = _LearningDomainMembershipWorkBuf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 4, 1, 3),
    _LearningDomainMembershipWorkBuf_Type()
)
learningDomainMembershipWorkBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    learningDomainMembershipWorkBuf.setStatus("mandatory")
_PortTargetDomainListMembershipTable_Object = MibTable
portTargetDomainListMembershipTable = _PortTargetDomainListMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 5)
)
if mibBuilder.loadTexts:
    portTargetDomainListMembershipTable.setStatus("mandatory")
_PortTargetDomainListMembershipEntry_Object = MibTableRow
portTargetDomainListMembershipEntry = _PortTargetDomainListMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 5, 1)
)
portTargetDomainListMembershipEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "portTargetDomainListIndex"),
)
if mibBuilder.loadTexts:
    portTargetDomainListMembershipEntry.setStatus("mandatory")
_PortTargetDomainListIndex_Type = Integer32
_PortTargetDomainListIndex_Object = MibTableColumn
portTargetDomainListIndex = _PortTargetDomainListIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 5, 1, 1),
    _PortTargetDomainListIndex_Type()
)
portTargetDomainListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTargetDomainListIndex.setStatus("mandatory")
_PortTargetDomainListMembership_Type = DisplayString
_PortTargetDomainListMembership_Object = MibTableColumn
portTargetDomainListMembership = _PortTargetDomainListMembership_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 5, 1, 2),
    _PortTargetDomainListMembership_Type()
)
portTargetDomainListMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTargetDomainListMembership.setStatus("mandatory")
_PortTargetDomainListMembershipWorkBuf_Type = DisplayString
_PortTargetDomainListMembershipWorkBuf_Object = MibTableColumn
portTargetDomainListMembershipWorkBuf = _PortTargetDomainListMembershipWorkBuf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 5, 1, 3),
    _PortTargetDomainListMembershipWorkBuf_Type()
)
portTargetDomainListMembershipWorkBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTargetDomainListMembershipWorkBuf.setStatus("mandatory")
_LBDomainMembershipTable_Object = MibTable
lBDomainMembershipTable = _LBDomainMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 6)
)
if mibBuilder.loadTexts:
    lBDomainMembershipTable.setStatus("mandatory")
_LBDomainMembershipEntry_Object = MibTableRow
lBDomainMembershipEntry = _LBDomainMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 6, 1)
)
lBDomainMembershipEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "lBDomainNumber"),
)
if mibBuilder.loadTexts:
    lBDomainMembershipEntry.setStatus("mandatory")
_LBDomainNumber_Type = Integer32
_LBDomainNumber_Object = MibTableColumn
lBDomainNumber = _LBDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 6, 1, 1),
    _LBDomainNumber_Type()
)
lBDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lBDomainNumber.setStatus("mandatory")
_LBDomainMembership_Type = DisplayString
_LBDomainMembership_Object = MibTableColumn
lBDomainMembership = _LBDomainMembership_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 6, 1, 2),
    _LBDomainMembership_Type()
)
lBDomainMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lBDomainMembership.setStatus("mandatory")
_LBDomainMembershipWorkBuf_Type = DisplayString
_LBDomainMembershipWorkBuf_Object = MibTableColumn
lBDomainMembershipWorkBuf = _LBDomainMembershipWorkBuf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 6, 1, 3),
    _LBDomainMembershipWorkBuf_Type()
)
lBDomainMembershipWorkBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lBDomainMembershipWorkBuf.setStatus("mandatory")


class _PortGroupAction_Type(Integer32):
    """Custom type portGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doUpdate", 2),
          ("none", 1))
    )


_PortGroupAction_Type.__name__ = "Integer32"
_PortGroupAction_Object = MibScalar
portGroupAction = _PortGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 7),
    _PortGroupAction_Type()
)
portGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupAction.setStatus("mandatory")


class _PortGroupActionStatus_Type(Integer32):
    """Custom type portGroupActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failedDueToLBDSpec", 6),
          ("failedDueToLDSpec", 4),
          ("failedDueToOthers", 2),
          ("failedDueToPGSpec", 3),
          ("failedDueToTLDSpec", 5),
          ("success", 1))
    )


_PortGroupActionStatus_Type.__name__ = "Integer32"
_PortGroupActionStatus_Object = MibScalar
portGroupActionStatus = _PortGroupActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 8),
    _PortGroupActionStatus_Type()
)
portGroupActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupActionStatus.setStatus("mandatory")
_TrafficGroupMembershipTable_Object = MibTable
trafficGroupMembershipTable = _TrafficGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 9)
)
if mibBuilder.loadTexts:
    trafficGroupMembershipTable.setStatus("mandatory")
_TrafficGroupMembershipEntry_Object = MibTableRow
trafficGroupMembershipEntry = _TrafficGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 9, 1)
)
trafficGroupMembershipEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "trafficGroupNumber"),
)
if mibBuilder.loadTexts:
    trafficGroupMembershipEntry.setStatus("mandatory")
_TrafficGroupNumber_Type = Integer32
_TrafficGroupNumber_Object = MibTableColumn
trafficGroupNumber = _TrafficGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 9, 1, 1),
    _TrafficGroupNumber_Type()
)
trafficGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficGroupNumber.setStatus("mandatory")
_TrafficGroupMembership_Type = DisplayString
_TrafficGroupMembership_Object = MibTableColumn
trafficGroupMembership = _TrafficGroupMembership_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 9, 1, 2),
    _TrafficGroupMembership_Type()
)
trafficGroupMembership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficGroupMembership.setStatus("mandatory")
_TrafficGroupAttributeTable_Object = MibTable
trafficGroupAttributeTable = _TrafficGroupAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 10)
)
if mibBuilder.loadTexts:
    trafficGroupAttributeTable.setStatus("mandatory")
_TrafficGroupAttributeEntry_Object = MibTableRow
trafficGroupAttributeEntry = _TrafficGroupAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 10, 1)
)
trafficGroupAttributeEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "trafficGroupNum"),
    (0, "DEC-ELAN-MIB", "trafficGroupHgNumber"),
)
if mibBuilder.loadTexts:
    trafficGroupAttributeEntry.setStatus("mandatory")
_TrafficGroupNum_Type = Integer32
_TrafficGroupNum_Object = MibTableColumn
trafficGroupNum = _TrafficGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 10, 1, 1),
    _TrafficGroupNum_Type()
)
trafficGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficGroupNum.setStatus("mandatory")
_TrafficGroupHgNumber_Type = Integer32
_TrafficGroupHgNumber_Object = MibTableColumn
trafficGroupHgNumber = _TrafficGroupHgNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 10, 1, 2),
    _TrafficGroupHgNumber_Type()
)
trafficGroupHgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficGroupHgNumber.setStatus("mandatory")
_TrafficGroupHgMember_Type = Integer32
_TrafficGroupHgMember_Object = MibTableColumn
trafficGroupHgMember = _TrafficGroupHgMember_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 10, 1, 3),
    _TrafficGroupHgMember_Type()
)
trafficGroupHgMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficGroupHgMember.setStatus("mandatory")


class _TrafficGroupCategory_Type(Integer32):
    """Custom type trafficGroupCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("reconfig", 2))
    )


_TrafficGroupCategory_Type.__name__ = "Integer32"
_TrafficGroupCategory_Object = MibTableColumn
trafficGroupCategory = _TrafficGroupCategory_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 10, 1, 4),
    _TrafficGroupCategory_Type()
)
trafficGroupCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficGroupCategory.setStatus("mandatory")
_LearningQuotaTable_Object = MibTable
learningQuotaTable = _LearningQuotaTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 11)
)
if mibBuilder.loadTexts:
    learningQuotaTable.setStatus("mandatory")
_LearningQuotaEntry_Object = MibTableRow
learningQuotaEntry = _LearningQuotaEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 11, 1)
)
learningQuotaEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "learningQuotaNumber"),
)
if mibBuilder.loadTexts:
    learningQuotaEntry.setStatus("mandatory")
_LearningQuotaNumber_Type = Integer32
_LearningQuotaNumber_Object = MibTableColumn
learningQuotaNumber = _LearningQuotaNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 11, 1, 1),
    _LearningQuotaNumber_Type()
)
learningQuotaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learningQuotaNumber.setStatus("mandatory")
_LearningQuota_Type = Integer32
_LearningQuota_Object = MibTableColumn
learningQuota = _LearningQuota_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 5, 11, 1, 2),
    _LearningQuota_Type()
)
learningQuota.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    learningQuota.setStatus("mandatory")
_GigaSnmpDebug_ObjectIdentity = ObjectIdentity
gigaSnmpDebug = _GigaSnmpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 6)
)
_CommitFails_Type = Integer32
_CommitFails_Object = MibScalar
commitFails = _CommitFails_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 6, 1),
    _CommitFails_Type()
)
commitFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitFails.setStatus("mandatory")
_GigaXglEthernetGroup_ObjectIdentity = ObjectIdentity
gigaXglEthernetGroup = _GigaXglEthernetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7)
)
_XglTable_Object = MibTable
xglTable = _XglTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    xglTable.setStatus("mandatory")
_XglEntry_Object = MibTableRow
xglEntry = _XglEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7, 1, 1)
)
xglEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xglEntry.setStatus("mandatory")


class _XglCompliantMtu_Type(Integer32):
    """Custom type xglCompliantMtu based on Integer32"""
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


_XglCompliantMtu_Type.__name__ = "Integer32"
_XglCompliantMtu_Object = MibTableColumn
xglCompliantMtu = _XglCompliantMtu_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7, 1, 1, 1),
    _XglCompliantMtu_Type()
)
xglCompliantMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xglCompliantMtu.setStatus("mandatory")


class _XglDisableIcmpErrors_Type(Integer32):
    """Custom type xglDisableIcmpErrors based on Integer32"""
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


_XglDisableIcmpErrors_Type.__name__ = "Integer32"
_XglDisableIcmpErrors_Object = MibTableColumn
xglDisableIcmpErrors = _XglDisableIcmpErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7, 1, 1, 2),
    _XglDisableIcmpErrors_Type()
)
xglDisableIcmpErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xglDisableIcmpErrors.setStatus("mandatory")


class _XglTxErrorsToIcmpFifo_Type(Integer32):
    """Custom type xglTxErrorsToIcmpFifo based on Integer32"""
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


_XglTxErrorsToIcmpFifo_Type.__name__ = "Integer32"
_XglTxErrorsToIcmpFifo_Object = MibTableColumn
xglTxErrorsToIcmpFifo = _XglTxErrorsToIcmpFifo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7, 1, 1, 3),
    _XglTxErrorsToIcmpFifo_Type()
)
xglTxErrorsToIcmpFifo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xglTxErrorsToIcmpFifo.setStatus("mandatory")


class _XglRxErrorsToIcmpFifo_Type(Integer32):
    """Custom type xglRxErrorsToIcmpFifo based on Integer32"""
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


_XglRxErrorsToIcmpFifo_Type.__name__ = "Integer32"
_XglRxErrorsToIcmpFifo_Object = MibTableColumn
xglRxErrorsToIcmpFifo = _XglRxErrorsToIcmpFifo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7, 1, 1, 4),
    _XglRxErrorsToIcmpFifo_Type()
)
xglRxErrorsToIcmpFifo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xglRxErrorsToIcmpFifo.setStatus("mandatory")


class _XglEnableAppletalkArpII_Type(Integer32):
    """Custom type xglEnableAppletalkArpII based on Integer32"""
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


_XglEnableAppletalkArpII_Type.__name__ = "Integer32"
_XglEnableAppletalkArpII_Object = MibTableColumn
xglEnableAppletalkArpII = _XglEnableAppletalkArpII_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7, 1, 1, 5),
    _XglEnableAppletalkArpII_Type()
)
xglEnableAppletalkArpII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xglEnableAppletalkArpII.setStatus("mandatory")


class _XglEnableRawIPX_Type(Integer32):
    """Custom type xglEnableRawIPX based on Integer32"""
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


_XglEnableRawIPX_Type.__name__ = "Integer32"
_XglEnableRawIPX_Object = MibTableColumn
xglEnableRawIPX = _XglEnableRawIPX_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 3, 7, 1, 1, 6),
    _XglEnableRawIPX_Type()
)
xglEnableRawIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xglEnableRawIPX.setStatus("mandatory")
_Agl_ObjectIdentity = ObjectIdentity
agl = _Agl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4)
)
_AglConfig_ObjectIdentity = ObjectIdentity
aglConfig = _AglConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 1)
)
_AglInterfaceConfTable_Object = MibTable
aglInterfaceConfTable = _AglInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aglInterfaceConfTable.setStatus("mandatory")
_AglInterfaceConfEntry_Object = MibTableRow
aglInterfaceConfEntry = _AglInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 1, 1, 1)
)
aglInterfaceConfEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglInterfaceIndex"),
)
if mibBuilder.loadTexts:
    aglInterfaceConfEntry.setStatus("mandatory")
_AglInterfaceIndex_Type = Integer32
_AglInterfaceIndex_Object = MibTableColumn
aglInterfaceIndex = _AglInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 1, 1, 1, 1),
    _AglInterfaceIndex_Type()
)
aglInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglInterfaceIndex.setStatus("mandatory")


class _AglInterfacePhyType_Type(Integer32):
    """Custom type aglInterfacePhyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds3e3", 2),
          ("sts3cStm1", 1),
          ("unKnown", 3))
    )


_AglInterfacePhyType_Type.__name__ = "Integer32"
_AglInterfacePhyType_Object = MibTableColumn
aglInterfacePhyType = _AglInterfacePhyType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 1, 1, 1, 2),
    _AglInterfacePhyType_Type()
)
aglInterfacePhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglInterfacePhyType.setStatus("mandatory")
_AglInterfaceTrafficRateGranularity_Type = Integer32
_AglInterfaceTrafficRateGranularity_Object = MibTableColumn
aglInterfaceTrafficRateGranularity = _AglInterfaceTrafficRateGranularity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 1, 1, 1, 3),
    _AglInterfaceTrafficRateGranularity_Type()
)
aglInterfaceTrafficRateGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglInterfaceTrafficRateGranularity.setStatus("mandatory")
_AglSonet_ObjectIdentity = ObjectIdentity
aglSonet = _AglSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 2)
)
_AglInterfaceSonetTable_Object = MibTable
aglInterfaceSonetTable = _AglInterfaceSonetTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    aglInterfaceSonetTable.setStatus("mandatory")
_AglInterfaceSonetEntry_Object = MibTableRow
aglInterfaceSonetEntry = _AglInterfaceSonetEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 2, 1, 1)
)
aglInterfaceSonetEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglInterfaceSonetIndex"),
)
if mibBuilder.loadTexts:
    aglInterfaceSonetEntry.setStatus("mandatory")
_AglInterfaceSonetIndex_Type = Integer32
_AglInterfaceSonetIndex_Object = MibTableColumn
aglInterfaceSonetIndex = _AglInterfaceSonetIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 2, 1, 1, 1),
    _AglInterfaceSonetIndex_Type()
)
aglInterfaceSonetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglInterfaceSonetIndex.setStatus("mandatory")


class _AglInterfaceSonetMode_Type(Integer32):
    """Custom type aglInterfaceSonetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdhSTM1", 2),
          ("sonetSTS3c", 1))
    )


_AglInterfaceSonetMode_Type.__name__ = "Integer32"
_AglInterfaceSonetMode_Object = MibTableColumn
aglInterfaceSonetMode = _AglInterfaceSonetMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 2, 1, 1, 2),
    _AglInterfaceSonetMode_Type()
)
aglInterfaceSonetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglInterfaceSonetMode.setStatus("mandatory")


class _AglInterfaceSonetTiming_Type(Integer32):
    """Custom type aglInterfaceSonetTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1))
    )


_AglInterfaceSonetTiming_Type.__name__ = "Integer32"
_AglInterfaceSonetTiming_Object = MibTableColumn
aglInterfaceSonetTiming = _AglInterfaceSonetTiming_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 2, 1, 1, 3),
    _AglInterfaceSonetTiming_Type()
)
aglInterfaceSonetTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglInterfaceSonetTiming.setStatus("mandatory")
_AglDS3E3_ObjectIdentity = ObjectIdentity
aglDS3E3 = _AglDS3E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 3)
)
_AglInterfaceDS3E3Table_Object = MibTable
aglInterfaceDS3E3Table = _AglInterfaceDS3E3Table_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    aglInterfaceDS3E3Table.setStatus("mandatory")
_AglInterfaceDS3E3Entry_Object = MibTableRow
aglInterfaceDS3E3Entry = _AglInterfaceDS3E3Entry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 3, 1, 1)
)
aglInterfaceDS3E3Entry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglInterfaceDS3E3Index"),
)
if mibBuilder.loadTexts:
    aglInterfaceDS3E3Entry.setStatus("mandatory")
_AglInterfaceDS3E3Index_Type = Integer32
_AglInterfaceDS3E3Index_Object = MibTableColumn
aglInterfaceDS3E3Index = _AglInterfaceDS3E3Index_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 3, 1, 1, 1),
    _AglInterfaceDS3E3Index_Type()
)
aglInterfaceDS3E3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglInterfaceDS3E3Index.setStatus("mandatory")


class _AglInterfaceDS3E3Mode_Type(Integer32):
    """Custom type aglInterfaceDS3E3Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-power", 2),
          ("low-power", 1))
    )


_AglInterfaceDS3E3Mode_Type.__name__ = "Integer32"
_AglInterfaceDS3E3Mode_Object = MibTableColumn
aglInterfaceDS3E3Mode = _AglInterfaceDS3E3Mode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 3, 1, 1, 2),
    _AglInterfaceDS3E3Mode_Type()
)
aglInterfaceDS3E3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglInterfaceDS3E3Mode.setStatus("mandatory")


class _AglInterfaceDS3E3Plcp_Type(Integer32):
    """Custom type aglInterfaceDS3E3Plcp based on Integer32"""
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


_AglInterfaceDS3E3Plcp_Type.__name__ = "Integer32"
_AglInterfaceDS3E3Plcp_Object = MibTableColumn
aglInterfaceDS3E3Plcp = _AglInterfaceDS3E3Plcp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 3, 1, 1, 3),
    _AglInterfaceDS3E3Plcp_Type()
)
aglInterfaceDS3E3Plcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglInterfaceDS3E3Plcp.setStatus("mandatory")
_AglAtm_ObjectIdentity = ObjectIdentity
aglAtm = _AglAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4)
)
_AglVCConnectionTable_Object = MibTable
aglVCConnectionTable = _AglVCConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    aglVCConnectionTable.setStatus("mandatory")
_AglVCConnectionTableEntry_Object = MibTableRow
aglVCConnectionTableEntry = _AglVCConnectionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1)
)
aglVCConnectionTableEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglVCConnectionPortA"),
    (0, "DEC-ELAN-MIB", "aglVCConnectionPortAVpi"),
    (0, "DEC-ELAN-MIB", "aglVCConnectionPortAVci"),
    (0, "DEC-ELAN-MIB", "aglVCConnectionPortB"),
    (0, "DEC-ELAN-MIB", "aglVCConnectionPortBVpi"),
    (0, "DEC-ELAN-MIB", "aglVCConnectionPortBVci"),
)
if mibBuilder.loadTexts:
    aglVCConnectionTableEntry.setStatus("mandatory")
_AglVCConnectionPortA_Type = Integer32
_AglVCConnectionPortA_Object = MibTableColumn
aglVCConnectionPortA = _AglVCConnectionPortA_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 1),
    _AglVCConnectionPortA_Type()
)
aglVCConnectionPortA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglVCConnectionPortA.setStatus("mandatory")


class _AglVCConnectionPortAVpi_Type(Integer32):
    """Custom type aglVCConnectionPortAVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AglVCConnectionPortAVpi_Type.__name__ = "Integer32"
_AglVCConnectionPortAVpi_Object = MibTableColumn
aglVCConnectionPortAVpi = _AglVCConnectionPortAVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 2),
    _AglVCConnectionPortAVpi_Type()
)
aglVCConnectionPortAVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglVCConnectionPortAVpi.setStatus("mandatory")


class _AglVCConnectionPortAVci_Type(Integer32):
    """Custom type aglVCConnectionPortAVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_AglVCConnectionPortAVci_Type.__name__ = "Integer32"
_AglVCConnectionPortAVci_Object = MibTableColumn
aglVCConnectionPortAVci = _AglVCConnectionPortAVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 3),
    _AglVCConnectionPortAVci_Type()
)
aglVCConnectionPortAVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglVCConnectionPortAVci.setStatus("mandatory")
_AglVCConnectionPortB_Type = Integer32
_AglVCConnectionPortB_Object = MibTableColumn
aglVCConnectionPortB = _AglVCConnectionPortB_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 4),
    _AglVCConnectionPortB_Type()
)
aglVCConnectionPortB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglVCConnectionPortB.setStatus("mandatory")


class _AglVCConnectionPortBVpi_Type(Integer32):
    """Custom type aglVCConnectionPortBVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AglVCConnectionPortBVpi_Type.__name__ = "Integer32"
_AglVCConnectionPortBVpi_Object = MibTableColumn
aglVCConnectionPortBVpi = _AglVCConnectionPortBVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 5),
    _AglVCConnectionPortBVpi_Type()
)
aglVCConnectionPortBVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglVCConnectionPortBVpi.setStatus("mandatory")


class _AglVCConnectionPortBVci_Type(Integer32):
    """Custom type aglVCConnectionPortBVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_AglVCConnectionPortBVci_Type.__name__ = "Integer32"
_AglVCConnectionPortBVci_Object = MibTableColumn
aglVCConnectionPortBVci = _AglVCConnectionPortBVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 6),
    _AglVCConnectionPortBVci_Type()
)
aglVCConnectionPortBVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglVCConnectionPortBVci.setStatus("mandatory")


class _AglVCConnectionTableEntryStatus_Type(Integer32):
    """Custom type aglVCConnectionTableEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_AglVCConnectionTableEntryStatus_Type.__name__ = "Integer32"
_AglVCConnectionTableEntryStatus_Object = MibTableColumn
aglVCConnectionTableEntryStatus = _AglVCConnectionTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 7),
    _AglVCConnectionTableEntryStatus_Type()
)
aglVCConnectionTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglVCConnectionTableEntryStatus.setStatus("mandatory")


class _AglVCConnectionTrafficType_Type(Integer32):
    """Custom type aglVCConnectionTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm-to-atm", 2),
          ("fddi-bridged", 1))
    )


_AglVCConnectionTrafficType_Type.__name__ = "Integer32"
_AglVCConnectionTrafficType_Object = MibTableColumn
aglVCConnectionTrafficType = _AglVCConnectionTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 8),
    _AglVCConnectionTrafficType_Type()
)
aglVCConnectionTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglVCConnectionTrafficType.setStatus("mandatory")


class _AglVCConnectionAALType_Type(Integer32):
    """Custom type aglVCConnectionAALType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal34", 1),
          ("aal5", 2))
    )


_AglVCConnectionAALType_Type.__name__ = "Integer32"
_AglVCConnectionAALType_Object = MibTableColumn
aglVCConnectionAALType = _AglVCConnectionAALType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 9),
    _AglVCConnectionAALType_Type()
)
aglVCConnectionAALType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglVCConnectionAALType.setStatus("mandatory")


class _AglVCConnectionOperStatus_Type(Integer32):
    """Custom type aglVCConnectionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AglVCConnectionOperStatus_Type.__name__ = "Integer32"
_AglVCConnectionOperStatus_Object = MibTableColumn
aglVCConnectionOperStatus = _AglVCConnectionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 10),
    _AglVCConnectionOperStatus_Type()
)
aglVCConnectionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglVCConnectionOperStatus.setStatus("mandatory")


class _AglVCConnectionAdminStatus_Type(Integer32):
    """Custom type aglVCConnectionAdminStatus based on Integer32"""
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


_AglVCConnectionAdminStatus_Type.__name__ = "Integer32"
_AglVCConnectionAdminStatus_Object = MibTableColumn
aglVCConnectionAdminStatus = _AglVCConnectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 11),
    _AglVCConnectionAdminStatus_Type()
)
aglVCConnectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglVCConnectionAdminStatus.setStatus("mandatory")
_AglVCConnectionTrafficShaperPeakRate_Type = Integer32
_AglVCConnectionTrafficShaperPeakRate_Object = MibTableColumn
aglVCConnectionTrafficShaperPeakRate = _AglVCConnectionTrafficShaperPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 12),
    _AglVCConnectionTrafficShaperPeakRate_Type()
)
aglVCConnectionTrafficShaperPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglVCConnectionTrafficShaperPeakRate.setStatus("mandatory")
_AglVCConnectionTrafficShaperAvgRate_Type = Integer32
_AglVCConnectionTrafficShaperAvgRate_Object = MibTableColumn
aglVCConnectionTrafficShaperAvgRate = _AglVCConnectionTrafficShaperAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 13),
    _AglVCConnectionTrafficShaperAvgRate_Type()
)
aglVCConnectionTrafficShaperAvgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglVCConnectionTrafficShaperAvgRate.setStatus("mandatory")
_AglVCConnectionTrafficShaperMinGuaranteedRate_Type = Integer32
_AglVCConnectionTrafficShaperMinGuaranteedRate_Object = MibTableColumn
aglVCConnectionTrafficShaperMinGuaranteedRate = _AglVCConnectionTrafficShaperMinGuaranteedRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 14),
    _AglVCConnectionTrafficShaperMinGuaranteedRate_Type()
)
aglVCConnectionTrafficShaperMinGuaranteedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglVCConnectionTrafficShaperMinGuaranteedRate.setStatus("mandatory")


class _AglVCConnectionTrafficShaperPriority_Type(Integer32):
    """Custom type aglVCConnectionTrafficShaperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AglVCConnectionTrafficShaperPriority_Type.__name__ = "Integer32"
_AglVCConnectionTrafficShaperPriority_Object = MibTableColumn
aglVCConnectionTrafficShaperPriority = _AglVCConnectionTrafficShaperPriority_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 1, 1, 15),
    _AglVCConnectionTrafficShaperPriority_Type()
)
aglVCConnectionTrafficShaperPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglVCConnectionTrafficShaperPriority.setStatus("mandatory")
_AglInterfaceATMTable_Object = MibTable
aglInterfaceATMTable = _AglInterfaceATMTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 2)
)
if mibBuilder.loadTexts:
    aglInterfaceATMTable.setStatus("mandatory")
_AglInterfaceATMTableEntry_Object = MibTableRow
aglInterfaceATMTableEntry = _AglInterfaceATMTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 2, 1)
)
aglInterfaceATMTableEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglInterfaceATMIndex"),
)
if mibBuilder.loadTexts:
    aglInterfaceATMTableEntry.setStatus("mandatory")
_AglInterfaceATMIndex_Type = Integer32
_AglInterfaceATMIndex_Object = MibTableColumn
aglInterfaceATMIndex = _AglInterfaceATMIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 2, 1, 1),
    _AglInterfaceATMIndex_Type()
)
aglInterfaceATMIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglInterfaceATMIndex.setStatus("mandatory")


class _AglInterfaceATMScrambeStatus_Type(Integer32):
    """Custom type aglInterfaceATMScrambeStatus based on Integer32"""
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


_AglInterfaceATMScrambeStatus_Type.__name__ = "Integer32"
_AglInterfaceATMScrambeStatus_Object = MibTableColumn
aglInterfaceATMScrambeStatus = _AglInterfaceATMScrambeStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 2, 1, 2),
    _AglInterfaceATMScrambeStatus_Type()
)
aglInterfaceATMScrambeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglInterfaceATMScrambeStatus.setStatus("mandatory")


class _AglInterfaceATMOAMStatus_Type(Integer32):
    """Custom type aglInterfaceATMOAMStatus based on Integer32"""
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


_AglInterfaceATMOAMStatus_Type.__name__ = "Integer32"
_AglInterfaceATMOAMStatus_Object = MibTableColumn
aglInterfaceATMOAMStatus = _AglInterfaceATMOAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 4, 4, 2, 1, 3),
    _AglInterfaceATMOAMStatus_Type()
)
aglInterfaceATMOAMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglInterfaceATMOAMStatus.setStatus("mandatory")
_AglatmMIB_ObjectIdentity = ObjectIdentity
aglatmMIB = _AglatmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5)
)
_AglatmMIBObjects_ObjectIdentity = ObjectIdentity
aglatmMIBObjects = _AglatmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1)
)
_AglatmInterfaceTrafficEnforcementTypes_ObjectIdentity = ObjectIdentity
aglatmInterfaceTrafficEnforcementTypes = _AglatmInterfaceTrafficEnforcementTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1)
)
_AglatmInterfaceNoTrafficEnforcement_Type = ObjectIdentifier
_AglatmInterfaceNoTrafficEnforcement_Object = MibScalar
aglatmInterfaceNoTrafficEnforcement = _AglatmInterfaceNoTrafficEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1, 1),
    _AglatmInterfaceNoTrafficEnforcement_Type()
)
aglatmInterfaceNoTrafficEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceNoTrafficEnforcement.setStatus("mandatory")
_AglatmInterfaceTrafficEnforcementType1_Type = ObjectIdentifier
_AglatmInterfaceTrafficEnforcementType1_Object = MibScalar
aglatmInterfaceTrafficEnforcementType1 = _AglatmInterfaceTrafficEnforcementType1_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1, 2),
    _AglatmInterfaceTrafficEnforcementType1_Type()
)
aglatmInterfaceTrafficEnforcementType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceTrafficEnforcementType1.setStatus("mandatory")
_AglatmInterfaceTrafficEnforcementType2_Type = ObjectIdentifier
_AglatmInterfaceTrafficEnforcementType2_Object = MibScalar
aglatmInterfaceTrafficEnforcementType2 = _AglatmInterfaceTrafficEnforcementType2_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1, 3),
    _AglatmInterfaceTrafficEnforcementType2_Type()
)
aglatmInterfaceTrafficEnforcementType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceTrafficEnforcementType2.setStatus("mandatory")
_AglatmInterfaceTrafficEnforcementType3_Type = ObjectIdentifier
_AglatmInterfaceTrafficEnforcementType3_Object = MibScalar
aglatmInterfaceTrafficEnforcementType3 = _AglatmInterfaceTrafficEnforcementType3_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1, 4),
    _AglatmInterfaceTrafficEnforcementType3_Type()
)
aglatmInterfaceTrafficEnforcementType3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceTrafficEnforcementType3.setStatus("mandatory")
_AglatmInterfaceTrafficEnforcementType4_Type = ObjectIdentifier
_AglatmInterfaceTrafficEnforcementType4_Object = MibScalar
aglatmInterfaceTrafficEnforcementType4 = _AglatmInterfaceTrafficEnforcementType4_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1, 5),
    _AglatmInterfaceTrafficEnforcementType4_Type()
)
aglatmInterfaceTrafficEnforcementType4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceTrafficEnforcementType4.setStatus("mandatory")
_AglatmInterfaceTrafficEnforcementType5_Type = ObjectIdentifier
_AglatmInterfaceTrafficEnforcementType5_Object = MibScalar
aglatmInterfaceTrafficEnforcementType5 = _AglatmInterfaceTrafficEnforcementType5_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1, 6),
    _AglatmInterfaceTrafficEnforcementType5_Type()
)
aglatmInterfaceTrafficEnforcementType5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceTrafficEnforcementType5.setStatus("mandatory")
_AglatmInterfaceTrafficEnforcementType6_Type = ObjectIdentifier
_AglatmInterfaceTrafficEnforcementType6_Object = MibScalar
aglatmInterfaceTrafficEnforcementType6 = _AglatmInterfaceTrafficEnforcementType6_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1, 7),
    _AglatmInterfaceTrafficEnforcementType6_Type()
)
aglatmInterfaceTrafficEnforcementType6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceTrafficEnforcementType6.setStatus("mandatory")
_AglatmInterfaceTrafficEnforcementType7_Type = ObjectIdentifier
_AglatmInterfaceTrafficEnforcementType7_Object = MibScalar
aglatmInterfaceTrafficEnforcementType7 = _AglatmInterfaceTrafficEnforcementType7_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 1, 8),
    _AglatmInterfaceTrafficEnforcementType7_Type()
)
aglatmInterfaceTrafficEnforcementType7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceTrafficEnforcementType7.setStatus("mandatory")
_AglatmInterfaceConfTable_Object = MibTable
aglatmInterfaceConfTable = _AglatmInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    aglatmInterfaceConfTable.setStatus("mandatory")
_AglatmInterfaceConfEntry_Object = MibTableRow
aglatmInterfaceConfEntry = _AglatmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1)
)
aglatmInterfaceConfEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglatmInterfaceIndex"),
)
if mibBuilder.loadTexts:
    aglatmInterfaceConfEntry.setStatus("mandatory")
_AglatmInterfaceIndex_Type = Integer32
_AglatmInterfaceIndex_Object = MibTableColumn
aglatmInterfaceIndex = _AglatmInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 1),
    _AglatmInterfaceIndex_Type()
)
aglatmInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aglatmInterfaceIndex.setStatus("mandatory")
_AglatmInterfaceMaxVpcs_Type = Integer32
_AglatmInterfaceMaxVpcs_Object = MibTableColumn
aglatmInterfaceMaxVpcs = _AglatmInterfaceMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 2),
    _AglatmInterfaceMaxVpcs_Type()
)
aglatmInterfaceMaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceMaxVpcs.setStatus("mandatory")
_AglatmInterfaceMaxVccs_Type = Integer32
_AglatmInterfaceMaxVccs_Object = MibTableColumn
aglatmInterfaceMaxVccs = _AglatmInterfaceMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 3),
    _AglatmInterfaceMaxVccs_Type()
)
aglatmInterfaceMaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceMaxVccs.setStatus("mandatory")
_AglatmInterfaceConfVpcs_Type = Integer32
_AglatmInterfaceConfVpcs_Object = MibTableColumn
aglatmInterfaceConfVpcs = _AglatmInterfaceConfVpcs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 4),
    _AglatmInterfaceConfVpcs_Type()
)
aglatmInterfaceConfVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceConfVpcs.setStatus("mandatory")
_AglatmInterfaceConfVccs_Type = Integer32
_AglatmInterfaceConfVccs_Object = MibTableColumn
aglatmInterfaceConfVccs = _AglatmInterfaceConfVccs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 5),
    _AglatmInterfaceConfVccs_Type()
)
aglatmInterfaceConfVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceConfVccs.setStatus("mandatory")
_AglatmInterfaceMaxActiveVpiBits_Type = Integer32
_AglatmInterfaceMaxActiveVpiBits_Object = MibTableColumn
aglatmInterfaceMaxActiveVpiBits = _AglatmInterfaceMaxActiveVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 6),
    _AglatmInterfaceMaxActiveVpiBits_Type()
)
aglatmInterfaceMaxActiveVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceMaxActiveVpiBits.setStatus("mandatory")
_AglatmInterfaceMaxActiveVciBits_Type = Integer32
_AglatmInterfaceMaxActiveVciBits_Object = MibTableColumn
aglatmInterfaceMaxActiveVciBits = _AglatmInterfaceMaxActiveVciBits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 7),
    _AglatmInterfaceMaxActiveVciBits_Type()
)
aglatmInterfaceMaxActiveVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceMaxActiveVciBits.setStatus("mandatory")
_AglatmInterfaceIlmiVpiVci_Type = Integer32
_AglatmInterfaceIlmiVpiVci_Object = MibTableColumn
aglatmInterfaceIlmiVpiVci = _AglatmInterfaceIlmiVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 8),
    _AglatmInterfaceIlmiVpiVci_Type()
)
aglatmInterfaceIlmiVpiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceIlmiVpiVci.setStatus("mandatory")
_AglatmInterfaceSpecific_Type = ObjectIdentifier
_AglatmInterfaceSpecific_Object = MibTableColumn
aglatmInterfaceSpecific = _AglatmInterfaceSpecific_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 2, 1, 9),
    _AglatmInterfaceSpecific_Type()
)
aglatmInterfaceSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceSpecific.setStatus("mandatory")
_AglatmInterfaceDs3PlcpTable_Object = MibTable
aglatmInterfaceDs3PlcpTable = _AglatmInterfaceDs3PlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    aglatmInterfaceDs3PlcpTable.setStatus("mandatory")
_AglatmInterfaceDs3PlcpEntry_Object = MibTableRow
aglatmInterfaceDs3PlcpEntry = _AglatmInterfaceDs3PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 3, 1)
)
aglatmInterfaceDs3PlcpEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglatmInterfaceDs3PlcpIndex"),
)
if mibBuilder.loadTexts:
    aglatmInterfaceDs3PlcpEntry.setStatus("mandatory")
_AglatmInterfaceDs3PlcpIndex_Type = Integer32
_AglatmInterfaceDs3PlcpIndex_Object = MibTableColumn
aglatmInterfaceDs3PlcpIndex = _AglatmInterfaceDs3PlcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 3, 1, 1),
    _AglatmInterfaceDs3PlcpIndex_Type()
)
aglatmInterfaceDs3PlcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aglatmInterfaceDs3PlcpIndex.setStatus("mandatory")
_AglatmInterfaceDs3PlcpSEFSs_Type = Counter32
_AglatmInterfaceDs3PlcpSEFSs_Object = MibTableColumn
aglatmInterfaceDs3PlcpSEFSs = _AglatmInterfaceDs3PlcpSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 3, 1, 2),
    _AglatmInterfaceDs3PlcpSEFSs_Type()
)
aglatmInterfaceDs3PlcpSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceDs3PlcpSEFSs.setStatus("mandatory")


class _AglatmInterfaceDs3PlcpAlarmState_Type(Integer32):
    """Custom type aglatmInterfaceDs3PlcpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incomingLOF", 3),
          ("noAlarm", 1),
          ("receivedFarEndAlarm", 2))
    )


_AglatmInterfaceDs3PlcpAlarmState_Type.__name__ = "Integer32"
_AglatmInterfaceDs3PlcpAlarmState_Object = MibTableColumn
aglatmInterfaceDs3PlcpAlarmState = _AglatmInterfaceDs3PlcpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 3, 1, 3),
    _AglatmInterfaceDs3PlcpAlarmState_Type()
)
aglatmInterfaceDs3PlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceDs3PlcpAlarmState.setStatus("mandatory")
_AglatmInterfaceDs3PlcpUASs_Type = Counter32
_AglatmInterfaceDs3PlcpUASs_Object = MibTableColumn
aglatmInterfaceDs3PlcpUASs = _AglatmInterfaceDs3PlcpUASs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 3, 1, 4),
    _AglatmInterfaceDs3PlcpUASs_Type()
)
aglatmInterfaceDs3PlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceDs3PlcpUASs.setStatus("mandatory")
_AglatmInterfaceSonetTCTable_Object = MibTable
aglatmInterfaceSonetTCTable = _AglatmInterfaceSonetTCTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    aglatmInterfaceSonetTCTable.setStatus("mandatory")
_AglatmInterfaceSonetTCEntry_Object = MibTableRow
aglatmInterfaceSonetTCEntry = _AglatmInterfaceSonetTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 4, 1)
)
aglatmInterfaceSonetTCEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglatmInterfaceSonetTCIndex"),
)
if mibBuilder.loadTexts:
    aglatmInterfaceSonetTCEntry.setStatus("mandatory")
_AglatmInterfaceSonetTCIndex_Type = Integer32
_AglatmInterfaceSonetTCIndex_Object = MibTableColumn
aglatmInterfaceSonetTCIndex = _AglatmInterfaceSonetTCIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 4, 1, 1),
    _AglatmInterfaceSonetTCIndex_Type()
)
aglatmInterfaceSonetTCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aglatmInterfaceSonetTCIndex.setStatus("mandatory")
_AglatmInterfaceSonetTCOCDEvents_Type = Counter32
_AglatmInterfaceSonetTCOCDEvents_Object = MibTableColumn
aglatmInterfaceSonetTCOCDEvents = _AglatmInterfaceSonetTCOCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 4, 1, 2),
    _AglatmInterfaceSonetTCOCDEvents_Type()
)
aglatmInterfaceSonetTCOCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceSonetTCOCDEvents.setStatus("mandatory")


class _AglatmInterfaceSonetTCAlarmState_Type(Integer32):
    """Custom type aglatmInterfaceSonetTCAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lcdFailure", 2),
          ("noAlarm", 1))
    )


_AglatmInterfaceSonetTCAlarmState_Type.__name__ = "Integer32"
_AglatmInterfaceSonetTCAlarmState_Object = MibTableColumn
aglatmInterfaceSonetTCAlarmState = _AglatmInterfaceSonetTCAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 5, 1, 4, 1, 3),
    _AglatmInterfaceSonetTCAlarmState_Type()
)
aglatmInterfaceSonetTCAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglatmInterfaceSonetTCAlarmState.setStatus("mandatory")
_AglsonetMIB_ObjectIdentity = ObjectIdentity
aglsonetMIB = _AglsonetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6)
)
_AglsonetObjects_ObjectIdentity = ObjectIdentity
aglsonetObjects = _AglsonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1)
)
_AglsonetMedium_ObjectIdentity = ObjectIdentity
aglsonetMedium = _AglsonetMedium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1)
)
_AglsonetMediumTable_Object = MibTable
aglsonetMediumTable = _AglsonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aglsonetMediumTable.setStatus("mandatory")
_AglsonetMediumEntry_Object = MibTableRow
aglsonetMediumEntry = _AglsonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1, 1)
)
aglsonetMediumEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglsonetMediumIfIndex"),
)
if mibBuilder.loadTexts:
    aglsonetMediumEntry.setStatus("mandatory")
_AglsonetMediumIfIndex_Type = Integer32
_AglsonetMediumIfIndex_Object = MibTableColumn
aglsonetMediumIfIndex = _AglsonetMediumIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1, 1, 1),
    _AglsonetMediumIfIndex_Type()
)
aglsonetMediumIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aglsonetMediumIfIndex.setStatus("mandatory")


class _AglsonetMediumType_Type(Integer32):
    """Custom type aglsonetMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_AglsonetMediumType_Type.__name__ = "Integer32"
_AglsonetMediumType_Object = MibTableColumn
aglsonetMediumType = _AglsonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1, 1, 2),
    _AglsonetMediumType_Type()
)
aglsonetMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetMediumType.setStatus("mandatory")
_AglsonetMediumTimeElapsed_Type = Integer32
_AglsonetMediumTimeElapsed_Object = MibTableColumn
aglsonetMediumTimeElapsed = _AglsonetMediumTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1, 1, 3),
    _AglsonetMediumTimeElapsed_Type()
)
aglsonetMediumTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetMediumTimeElapsed.setStatus("mandatory")
_AglsonetMediumValidIntervals_Type = Integer32
_AglsonetMediumValidIntervals_Object = MibTableColumn
aglsonetMediumValidIntervals = _AglsonetMediumValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1, 1, 4),
    _AglsonetMediumValidIntervals_Type()
)
aglsonetMediumValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetMediumValidIntervals.setStatus("mandatory")


class _AglsonetMediumLineCoding_Type(Integer32):
    """Custom type aglsonetMediumLineCoding based on Integer32"""
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
        *(("sonetMediumB3ZS", 2),
          ("sonetMediumCMI", 3),
          ("sonetMediumNRZ", 4),
          ("sonetMediumOther", 1),
          ("sonetMediumRZ", 5))
    )


_AglsonetMediumLineCoding_Type.__name__ = "Integer32"
_AglsonetMediumLineCoding_Object = MibTableColumn
aglsonetMediumLineCoding = _AglsonetMediumLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1, 1, 5),
    _AglsonetMediumLineCoding_Type()
)
aglsonetMediumLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetMediumLineCoding.setStatus("mandatory")


class _AglsonetMediumLineType_Type(Integer32):
    """Custom type aglsonetMediumLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sonetCoax", 5),
          ("sonetLongSingleMode", 3),
          ("sonetMultiMode", 4),
          ("sonetOther", 1),
          ("sonetShortSingleMode", 2),
          ("sonetUTP", 6))
    )


_AglsonetMediumLineType_Type.__name__ = "Integer32"
_AglsonetMediumLineType_Object = MibTableColumn
aglsonetMediumLineType = _AglsonetMediumLineType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1, 1, 6),
    _AglsonetMediumLineType_Type()
)
aglsonetMediumLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetMediumLineType.setStatus("mandatory")
_AglsonetMediumCircuitIdentifier_Type = DisplayString
_AglsonetMediumCircuitIdentifier_Object = MibTableColumn
aglsonetMediumCircuitIdentifier = _AglsonetMediumCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 1, 1, 1, 7),
    _AglsonetMediumCircuitIdentifier_Type()
)
aglsonetMediumCircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetMediumCircuitIdentifier.setStatus("mandatory")
_AglsonetSection_ObjectIdentity = ObjectIdentity
aglsonetSection = _AglsonetSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2)
)
_AglsonetSectionCurrentTable_Object = MibTable
aglsonetSectionCurrentTable = _AglsonetSectionCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aglsonetSectionCurrentTable.setStatus("mandatory")
_AglsonetSectionCurrentEntry_Object = MibTableRow
aglsonetSectionCurrentEntry = _AglsonetSectionCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2, 1, 1)
)
aglsonetSectionCurrentEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglsonetSectionCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    aglsonetSectionCurrentEntry.setStatus("mandatory")
_AglsonetSectionCurrentIfIndex_Type = Integer32
_AglsonetSectionCurrentIfIndex_Object = MibTableColumn
aglsonetSectionCurrentIfIndex = _AglsonetSectionCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2, 1, 1, 1),
    _AglsonetSectionCurrentIfIndex_Type()
)
aglsonetSectionCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aglsonetSectionCurrentIfIndex.setStatus("mandatory")
_AglsonetSectionCurrentStatus_Type = Integer32
_AglsonetSectionCurrentStatus_Object = MibTableColumn
aglsonetSectionCurrentStatus = _AglsonetSectionCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2, 1, 1, 2),
    _AglsonetSectionCurrentStatus_Type()
)
aglsonetSectionCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetSectionCurrentStatus.setStatus("mandatory")
_AglsonetSectionCurrentESs_Type = Gauge32
_AglsonetSectionCurrentESs_Object = MibTableColumn
aglsonetSectionCurrentESs = _AglsonetSectionCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2, 1, 1, 3),
    _AglsonetSectionCurrentESs_Type()
)
aglsonetSectionCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetSectionCurrentESs.setStatus("mandatory")
_AglsonetSectionCurrentSESs_Type = Gauge32
_AglsonetSectionCurrentSESs_Object = MibTableColumn
aglsonetSectionCurrentSESs = _AglsonetSectionCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2, 1, 1, 4),
    _AglsonetSectionCurrentSESs_Type()
)
aglsonetSectionCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetSectionCurrentSESs.setStatus("mandatory")
_AglsonetSectionCurrentSEFSs_Type = Gauge32
_AglsonetSectionCurrentSEFSs_Object = MibTableColumn
aglsonetSectionCurrentSEFSs = _AglsonetSectionCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2, 1, 1, 5),
    _AglsonetSectionCurrentSEFSs_Type()
)
aglsonetSectionCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetSectionCurrentSEFSs.setStatus("mandatory")
_AglsonetSectionCurrentCVs_Type = Gauge32
_AglsonetSectionCurrentCVs_Object = MibTableColumn
aglsonetSectionCurrentCVs = _AglsonetSectionCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 2, 1, 1, 6),
    _AglsonetSectionCurrentCVs_Type()
)
aglsonetSectionCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetSectionCurrentCVs.setStatus("mandatory")
_AglsonetLine_ObjectIdentity = ObjectIdentity
aglsonetLine = _AglsonetLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3)
)
_AglsonetLineCurrentTable_Object = MibTable
aglsonetLineCurrentTable = _AglsonetLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aglsonetLineCurrentTable.setStatus("mandatory")
_AglsonetLineCurrentEntry_Object = MibTableRow
aglsonetLineCurrentEntry = _AglsonetLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3, 1, 1)
)
aglsonetLineCurrentEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglsonetLineCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    aglsonetLineCurrentEntry.setStatus("mandatory")
_AglsonetLineCurrentIfIndex_Type = Integer32
_AglsonetLineCurrentIfIndex_Object = MibTableColumn
aglsonetLineCurrentIfIndex = _AglsonetLineCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3, 1, 1, 1),
    _AglsonetLineCurrentIfIndex_Type()
)
aglsonetLineCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aglsonetLineCurrentIfIndex.setStatus("mandatory")
_AglsonetLineCurrentStatus_Type = Integer32
_AglsonetLineCurrentStatus_Object = MibTableColumn
aglsonetLineCurrentStatus = _AglsonetLineCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3, 1, 1, 2),
    _AglsonetLineCurrentStatus_Type()
)
aglsonetLineCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetLineCurrentStatus.setStatus("mandatory")
_AglsonetLineCurrentESs_Type = Gauge32
_AglsonetLineCurrentESs_Object = MibTableColumn
aglsonetLineCurrentESs = _AglsonetLineCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3, 1, 1, 3),
    _AglsonetLineCurrentESs_Type()
)
aglsonetLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetLineCurrentESs.setStatus("mandatory")
_AglsonetLineCurrentSESs_Type = Gauge32
_AglsonetLineCurrentSESs_Object = MibTableColumn
aglsonetLineCurrentSESs = _AglsonetLineCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3, 1, 1, 4),
    _AglsonetLineCurrentSESs_Type()
)
aglsonetLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetLineCurrentSESs.setStatus("mandatory")
_AglsonetLineCurrentCVs_Type = Gauge32
_AglsonetLineCurrentCVs_Object = MibTableColumn
aglsonetLineCurrentCVs = _AglsonetLineCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3, 1, 1, 5),
    _AglsonetLineCurrentCVs_Type()
)
aglsonetLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetLineCurrentCVs.setStatus("mandatory")
_AglsonetLineCurrentUASs_Type = Gauge32
_AglsonetLineCurrentUASs_Object = MibTableColumn
aglsonetLineCurrentUASs = _AglsonetLineCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 1, 3, 1, 1, 6),
    _AglsonetLineCurrentUASs_Type()
)
aglsonetLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetLineCurrentUASs.setStatus("mandatory")
_AglsonetObjectsPath_ObjectIdentity = ObjectIdentity
aglsonetObjectsPath = _AglsonetObjectsPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2)
)
_AglsonetPath_ObjectIdentity = ObjectIdentity
aglsonetPath = _AglsonetPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1)
)
_AglsonetPathCurrentTable_Object = MibTable
aglsonetPathCurrentTable = _AglsonetPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aglsonetPathCurrentTable.setStatus("mandatory")
_AglsonetPathCurrentEntry_Object = MibTableRow
aglsonetPathCurrentEntry = _AglsonetPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1, 1)
)
aglsonetPathCurrentEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "aglsonetPathCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    aglsonetPathCurrentEntry.setStatus("mandatory")
_AglsonetPathCurrentIfIndex_Type = Integer32
_AglsonetPathCurrentIfIndex_Object = MibTableColumn
aglsonetPathCurrentIfIndex = _AglsonetPathCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1, 1, 1),
    _AglsonetPathCurrentIfIndex_Type()
)
aglsonetPathCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aglsonetPathCurrentIfIndex.setStatus("mandatory")


class _AglsonetPathCurrentWidth_Type(Integer32):
    """Custom type aglsonetPathCurrentWidth based on Integer32"""
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
        *(("sts1", 1),
          ("sts12cSTM4", 3),
          ("sts24c", 4),
          ("sts3cSTM1", 2),
          ("sts48cSTM16", 5))
    )


_AglsonetPathCurrentWidth_Type.__name__ = "Integer32"
_AglsonetPathCurrentWidth_Object = MibTableColumn
aglsonetPathCurrentWidth = _AglsonetPathCurrentWidth_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1, 1, 2),
    _AglsonetPathCurrentWidth_Type()
)
aglsonetPathCurrentWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aglsonetPathCurrentWidth.setStatus("mandatory")
_AglsonetPathCurrentStatus_Type = Integer32
_AglsonetPathCurrentStatus_Object = MibTableColumn
aglsonetPathCurrentStatus = _AglsonetPathCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1, 1, 3),
    _AglsonetPathCurrentStatus_Type()
)
aglsonetPathCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetPathCurrentStatus.setStatus("mandatory")
_AglsonetPathCurrentESs_Type = Gauge32
_AglsonetPathCurrentESs_Object = MibTableColumn
aglsonetPathCurrentESs = _AglsonetPathCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1, 1, 4),
    _AglsonetPathCurrentESs_Type()
)
aglsonetPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetPathCurrentESs.setStatus("mandatory")
_AglsonetPathCurrentSESs_Type = Gauge32
_AglsonetPathCurrentSESs_Object = MibTableColumn
aglsonetPathCurrentSESs = _AglsonetPathCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1, 1, 5),
    _AglsonetPathCurrentSESs_Type()
)
aglsonetPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetPathCurrentSESs.setStatus("mandatory")
_AglsonetPathCurrentCVs_Type = Gauge32
_AglsonetPathCurrentCVs_Object = MibTableColumn
aglsonetPathCurrentCVs = _AglsonetPathCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1, 1, 6),
    _AglsonetPathCurrentCVs_Type()
)
aglsonetPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetPathCurrentCVs.setStatus("mandatory")
_AglsonetPathCurrentUASs_Type = Gauge32
_AglsonetPathCurrentUASs_Object = MibTableColumn
aglsonetPathCurrentUASs = _AglsonetPathCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 3, 3, 6, 2, 1, 1, 1, 7),
    _AglsonetPathCurrentUASs_Type()
)
aglsonetPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aglsonetPathCurrentUASs.setStatus("mandatory")
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_Elanext_ObjectIdentity = ObjectIdentity
elanext = _Elanext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1)
)
_Efddi_ObjectIdentity = ObjectIdentity
efddi = _Efddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1)
)
_EfddiSMT_ObjectIdentity = ObjectIdentity
efddiSMT = _EfddiSMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 1)
)
_EfddiSMTTable_Object = MibTable
efddiSMTTable = _EfddiSMTTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    efddiSMTTable.setStatus("mandatory")
_EfddiSMTEntry_Object = MibTableRow
efddiSMTEntry = _EfddiSMTEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 1, 1, 1)
)
efddiSMTEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "eSMTIndex"),
)
if mibBuilder.loadTexts:
    efddiSMTEntry.setStatus("mandatory")
_ESMTIndex_Type = Integer32
_ESMTIndex_Object = MibTableColumn
eSMTIndex = _ESMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 1, 1, 1, 1),
    _ESMTIndex_Type()
)
eSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSMTIndex.setStatus("mandatory")


class _ESMTStationType_Type(Integer32):
    """Custom type eSMTStationType based on Integer32"""
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
        *(("dac", 2),
          ("das", 5),
          ("nac", 4),
          ("sac", 3),
          ("sas", 1))
    )


_ESMTStationType_Type.__name__ = "Integer32"
_ESMTStationType_Object = MibTableColumn
eSMTStationType = _ESMTStationType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 1, 1, 1, 2),
    _ESMTStationType_Type()
)
eSMTStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSMTStationType.setStatus("mandatory")
_ESMTTracesReceived_Type = Counter32
_ESMTTracesReceived_Object = MibTableColumn
eSMTTracesReceived = _ESMTTracesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 1, 1, 1, 3),
    _ESMTTracesReceived_Type()
)
eSMTTracesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSMTTracesReceived.setStatus("mandatory")
_EfddiMAC_ObjectIdentity = ObjectIdentity
efddiMAC = _EfddiMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2)
)
_EfddiMACTable_Object = MibTable
efddiMACTable = _EfddiMACTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    efddiMACTable.setStatus("mandatory")
_EfddiMACEntry_Object = MibTableRow
efddiMACEntry = _EfddiMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1)
)
efddiMACEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "eMACSMTIndex"),
    (0, "DEC-ELAN-MIB", "eMACIndex"),
)
if mibBuilder.loadTexts:
    efddiMACEntry.setStatus("mandatory")
_EMACSMTIndex_Type = Integer32
_EMACSMTIndex_Object = MibTableColumn
eMACSMTIndex = _EMACSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 1),
    _EMACSMTIndex_Type()
)
eMACSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACSMTIndex.setStatus("mandatory")
_EMACIndex_Type = Integer32
_EMACIndex_Object = MibTableColumn
eMACIndex = _EMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 2),
    _EMACIndex_Type()
)
eMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACIndex.setStatus("mandatory")
_EMACLinkIndex_Type = Integer32
_EMACLinkIndex_Object = MibTableColumn
eMACLinkIndex = _EMACLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 3),
    _EMACLinkIndex_Type()
)
eMACLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACLinkIndex.setStatus("mandatory")


class _EMACLinkState_Type(Integer32):
    """Custom type eMACLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("broken", 6),
          ("offFaultRecovery", 3),
          ("offMaint", 1),
          ("offReady", 2),
          ("onRingInit", 4),
          ("onRingRun", 5))
    )


_EMACLinkState_Type.__name__ = "Integer32"
_EMACLinkState_Object = MibTableColumn
eMACLinkState = _EMACLinkState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 4),
    _EMACLinkState_Type()
)
eMACLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACLinkState.setStatus("mandatory")


class _EMACRingPurgerState_Type(Integer32):
    """Custom type eMACRingPurgerState based on Integer32"""
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
        *(("candidate", 2),
          ("nonPurger", 3),
          ("purger", 4),
          ("purgerOff", 1))
    )


_EMACRingPurgerState_Type.__name__ = "Integer32"
_EMACRingPurgerState_Object = MibTableColumn
eMACRingPurgerState = _EMACRingPurgerState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 5),
    _EMACRingPurgerState_Type()
)
eMACRingPurgerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACRingPurgerState.setStatus("mandatory")


class _EMACRingPurgerEnable_Type(Integer32):
    """Custom type eMACRingPurgerEnable based on Integer32"""
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


_EMACRingPurgerEnable_Type.__name__ = "Integer32"
_EMACRingPurgerEnable_Object = MibTableColumn
eMACRingPurgerEnable = _EMACRingPurgerEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 6),
    _EMACRingPurgerEnable_Type()
)
eMACRingPurgerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMACRingPurgerEnable.setStatus("mandatory")
_EMACRingPurgeErrors_Type = Counter32
_EMACRingPurgeErrors_Object = MibTableColumn
eMACRingPurgeErrors = _EMACRingPurgeErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 7),
    _EMACRingPurgeErrors_Type()
)
eMACRingPurgeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACRingPurgeErrors.setStatus("mandatory")


class _EMACFrameStripMode_Type(Integer32):
    """Custom type eMACFrameStripMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridgeStrip", 2),
          ("saMatch", 1))
    )


_EMACFrameStripMode_Type.__name__ = "Integer32"
_EMACFrameStripMode_Object = MibTableColumn
eMACFrameStripMode = _EMACFrameStripMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 8),
    _EMACFrameStripMode_Type()
)
eMACFrameStripMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACFrameStripMode.setStatus("mandatory")
_EMACFCIStripErrors_Type = Counter32
_EMACFCIStripErrors_Object = MibTableColumn
eMACFCIStripErrors = _EMACFCIStripErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 9),
    _EMACFCIStripErrors_Type()
)
eMACFCIStripErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACFCIStripErrors.setStatus("mandatory")


class _EMACRingErrorReason_Type(Integer32):
    """Custom type eMACRingErrorReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bridgeStripError", 12),
          ("daDetected", 9),
          ("directedBeaconReceived", 14),
          ("duplicateTokenDetected", 10),
          ("noReason", 1),
          ("pcTraceInitiated", 15),
          ("pcTraceReceived", 16),
          ("ringBeaconingInitiated", 8),
          ("ringInitInitiated", 6),
          ("ringInitReceived", 7),
          ("ringOpOscillation", 13),
          ("ringPurgeError", 11))
    )


_EMACRingErrorReason_Type.__name__ = "Integer32"
_EMACRingErrorReason_Object = MibTableColumn
eMACRingErrorReason = _EMACRingErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 10),
    _EMACRingErrorReason_Type()
)
eMACRingErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACRingErrorReason.setStatus("mandatory")
_EMACRingInitializationsInitiated_Type = Counter32
_EMACRingInitializationsInitiated_Object = MibTableColumn
eMACRingInitializationsInitiated = _EMACRingInitializationsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 11),
    _EMACRingInitializationsInitiated_Type()
)
eMACRingInitializationsInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACRingInitializationsInitiated.setStatus("mandatory")
_EMACRingInitializationsReceived_Type = Counter32
_EMACRingInitializationsReceived_Object = MibTableColumn
eMACRingInitializationsReceived = _EMACRingInitializationsReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 12),
    _EMACRingInitializationsReceived_Type()
)
eMACRingInitializationsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACRingInitializationsReceived.setStatus("mandatory")
_EMACRingBeaconingInitiated_Type = Counter32
_EMACRingBeaconingInitiated_Object = MibTableColumn
eMACRingBeaconingInitiated = _EMACRingBeaconingInitiated_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 13),
    _EMACRingBeaconingInitiated_Type()
)
eMACRingBeaconingInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACRingBeaconingInitiated.setStatus("mandatory")
_EMACDuplicateAddressTestFailures_Type = Counter32
_EMACDuplicateAddressTestFailures_Object = MibTableColumn
eMACDuplicateAddressTestFailures = _EMACDuplicateAddressTestFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 14),
    _EMACDuplicateAddressTestFailures_Type()
)
eMACDuplicateAddressTestFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACDuplicateAddressTestFailures.setStatus("mandatory")
_EMACDuplicateTokensDetected_Type = Counter32
_EMACDuplicateTokensDetected_Object = MibTableColumn
eMACDuplicateTokensDetected = _EMACDuplicateTokensDetected_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 15),
    _EMACDuplicateTokensDetected_Type()
)
eMACDuplicateTokensDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACDuplicateTokensDetected.setStatus("mandatory")


class _EMACUpstreamNbrDuplAddressFlag_Type(Integer32):
    """Custom type eMACUpstreamNbrDuplAddressFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 3))
    )


_EMACUpstreamNbrDuplAddressFlag_Type.__name__ = "Integer32"
_EMACUpstreamNbrDuplAddressFlag_Object = MibTableColumn
eMACUpstreamNbrDuplAddressFlag = _EMACUpstreamNbrDuplAddressFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 16),
    _EMACUpstreamNbrDuplAddressFlag_Type()
)
eMACUpstreamNbrDuplAddressFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACUpstreamNbrDuplAddressFlag.setStatus("mandatory")
_EMACTracesInitiated_Type = Counter32
_EMACTracesInitiated_Object = MibTableColumn
eMACTracesInitiated = _EMACTracesInitiated_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 17),
    _EMACTracesInitiated_Type()
)
eMACTracesInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACTracesInitiated.setStatus("mandatory")
_EMACRestrictedTokenTimeout_Type = Integer32
_EMACRestrictedTokenTimeout_Object = MibTableColumn
eMACRestrictedTokenTimeout = _EMACRestrictedTokenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 18),
    _EMACRestrictedTokenTimeout_Type()
)
eMACRestrictedTokenTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMACRestrictedTokenTimeout.setStatus("mandatory")
_EMACFrameStatusErrors_Type = Counter32
_EMACFrameStatusErrors_Object = MibTableColumn
eMACFrameStatusErrors = _EMACFrameStatusErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 19),
    _EMACFrameStatusErrors_Type()
)
eMACFrameStatusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACFrameStatusErrors.setStatus("mandatory")
_EMACFrameAlignmentErrors_Type = Counter32
_EMACFrameAlignmentErrors_Object = MibTableColumn
eMACFrameAlignmentErrors = _EMACFrameAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 20),
    _EMACFrameAlignmentErrors_Type()
)
eMACFrameAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACFrameAlignmentErrors.setStatus("mandatory")
_EMACTransmitUnderruns_Type = Counter32
_EMACTransmitUnderruns_Object = MibTableColumn
eMACTransmitUnderruns = _EMACTransmitUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 2, 1, 1, 21),
    _EMACTransmitUnderruns_Type()
)
eMACTransmitUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMACTransmitUnderruns.setStatus("mandatory")
_EfddiPORT_ObjectIdentity = ObjectIdentity
efddiPORT = _EfddiPORT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3)
)
_EfddiPORTTable_Object = MibTable
efddiPORTTable = _EfddiPORTTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    efddiPORTTable.setStatus("mandatory")
_EfddiPORTEntry_Object = MibTableRow
efddiPORTEntry = _EfddiPORTEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1)
)
efddiPORTEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ePORTSMTIndex"),
    (0, "DEC-ELAN-MIB", "ePORTIndex"),
)
if mibBuilder.loadTexts:
    efddiPORTEntry.setStatus("mandatory")
_EPORTSMTIndex_Type = Integer32
_EPORTSMTIndex_Object = MibTableColumn
ePORTSMTIndex = _EPORTSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 1),
    _EPORTSMTIndex_Type()
)
ePORTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTSMTIndex.setStatus("mandatory")
_EPORTIndex_Type = Integer32
_EPORTIndex_Object = MibTableColumn
ePORTIndex = _EPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 2),
    _EPORTIndex_Type()
)
ePORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTIndex.setStatus("mandatory")
_EPORTPHYIndex_Type = Integer32
_EPORTPHYIndex_Object = MibTableColumn
ePORTPHYIndex = _EPORTPHYIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 3),
    _EPORTPHYIndex_Type()
)
ePORTPHYIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTPHYIndex.setStatus("mandatory")


class _EPORTPMDType_Type(Integer32):
    """Custom type ePORTPMDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("pmdLC", 4),
          ("pmdMM", 2),
          ("pmdNone", 1),
          ("pmdSM", 3),
          ("pmdSTP", 6),
          ("pmdTHN", 5),
          ("pmdUTP", 7))
    )


_EPORTPMDType_Type.__name__ = "Integer32"
_EPORTPMDType_Object = MibTableColumn
ePORTPMDType = _EPORTPMDType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 4),
    _EPORTPMDType_Type()
)
ePORTPMDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTPMDType.setStatus("mandatory")


class _EPORTPHYState_Type(Integer32):
    """Custom type ePORTPHYState based on Integer32"""
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
        *(("broken", 2),
          ("failed", 6),
          ("inuse", 8),
          ("offmaintenance", 1),
          ("offready", 3),
          ("starting", 5),
          ("wait", 4),
          ("watch", 7))
    )


_EPORTPHYState_Type.__name__ = "Integer32"
_EPORTPHYState_Object = MibTableColumn
ePORTPHYState = _EPORTPHYState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 5),
    _EPORTPHYState_Type()
)
ePORTPHYState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTPHYState.setStatus("mandatory")


class _EPORTRejectReason_Type(Integer32):
    """Custom type ePORTRejectReason based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("lctBoth", 4),
          ("lctLocal", 2),
          ("lctProtocol", 12),
          ("lctRemote", 3),
          ("lemFailure", 5),
          ("noReason", 1),
          ("remoteReject", 8),
          ("standby", 11),
          ("tneExpired", 7),
          ("topologyRules", 6),
          ("tracesInProgress", 9),
          ("tracesReceived", 10))
    )


_EPORTRejectReason_Type.__name__ = "Integer32"
_EPORTRejectReason_Object = MibTableColumn
ePORTRejectReason = _EPORTRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 6),
    _EPORTRejectReason_Type()
)
ePORTRejectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTRejectReason.setStatus("mandatory")
_EPORTConnectionsCompleted_Type = Counter32
_EPORTConnectionsCompleted_Object = MibTableColumn
ePORTConnectionsCompleted = _EPORTConnectionsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 7),
    _EPORTConnectionsCompleted_Type()
)
ePORTConnectionsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTConnectionsCompleted.setStatus("mandatory")
_EPORTTNEExpRejects_Type = Counter32
_EPORTTNEExpRejects_Object = MibTableColumn
ePORTTNEExpRejects = _EPORTTNEExpRejects_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 8),
    _EPORTTNEExpRejects_Type()
)
ePORTTNEExpRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTTNEExpRejects.setStatus("mandatory")
_EPORTElasticityBufferErrors_Type = Counter32
_EPORTElasticityBufferErrors_Object = MibTableColumn
ePORTElasticityBufferErrors = _EPORTElasticityBufferErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 3, 1, 1, 9),
    _EPORTElasticityBufferErrors_Type()
)
ePORTElasticityBufferErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePORTElasticityBufferErrors.setStatus("mandatory")
_EfddiFDX_ObjectIdentity = ObjectIdentity
efddiFDX = _EfddiFDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 4)
)
_EfddiFDXTable_Object = MibTable
efddiFDXTable = _EfddiFDXTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    efddiFDXTable.setStatus("mandatory")
_EfddiFDXEntry_Object = MibTableRow
efddiFDXEntry = _EfddiFDXEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 4, 1, 1)
)
efddiFDXEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "eFDXSMTIndex"),
    (0, "DEC-ELAN-MIB", "eFDXMACIndex"),
)
if mibBuilder.loadTexts:
    efddiFDXEntry.setStatus("mandatory")
_EFDXSMTIndex_Type = Integer32
_EFDXSMTIndex_Object = MibTableColumn
eFDXSMTIndex = _EFDXSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 4, 1, 1, 1),
    _EFDXSMTIndex_Type()
)
eFDXSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFDXSMTIndex.setStatus("mandatory")
_EFDXMACIndex_Type = Integer32
_EFDXMACIndex_Object = MibTableColumn
eFDXMACIndex = _EFDXMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 4, 1, 1, 2),
    _EFDXMACIndex_Type()
)
eFDXMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFDXMACIndex.setStatus("mandatory")


class _EFDXEnable_Type(Integer32):
    """Custom type eFDXEnable based on Integer32"""
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


_EFDXEnable_Type.__name__ = "Integer32"
_EFDXEnable_Object = MibTableColumn
eFDXEnable = _EFDXEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 4, 1, 1, 3),
    _EFDXEnable_Type()
)
eFDXEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eFDXEnable.setStatus("mandatory")


class _EFDXOp_Type(Integer32):
    """Custom type eFDXOp based on Integer32"""
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


_EFDXOp_Type.__name__ = "Integer32"
_EFDXOp_Object = MibTableColumn
eFDXOp = _EFDXOp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 4, 1, 1, 4),
    _EFDXOp_Type()
)
eFDXOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFDXOp.setStatus("mandatory")


class _EFDXState_Type(Integer32):
    """Custom type eFDXState based on Integer32"""
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
        *(("fdxConfirm", 3),
          ("fdxIdle", 1),
          ("fdxOperation", 4),
          ("fdxRequest", 2))
    )


_EFDXState_Type.__name__ = "Integer32"
_EFDXState_Object = MibTableColumn
eFDXState = _EFDXState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 1, 4, 1, 1, 5),
    _EFDXState_Type()
)
eFDXState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFDXState.setStatus("mandatory")
_Esystem_ObjectIdentity = ObjectIdentity
esystem = _Esystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2)
)
_EsysChar_ObjectIdentity = ObjectIdentity
esysChar = _EsysChar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1)
)
_EsysRomVersion_Type = Integer32
_EsysRomVersion_Object = MibScalar
esysRomVersion = _EsysRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 1),
    _EsysRomVersion_Type()
)
esysRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysRomVersion.setStatus("mandatory")


class _EsysInitSwitch_Type(Integer32):
    """Custom type esysInitSwitch based on Integer32"""
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
          ("resetWithDefaults", 3))
    )


_EsysInitSwitch_Type.__name__ = "Integer32"
_EsysInitSwitch_Object = MibScalar
esysInitSwitch = _EsysInitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 2),
    _EsysInitSwitch_Type()
)
esysInitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esysInitSwitch.setStatus("mandatory")


class _EsysResetDefaultsSwitch_Type(Integer32):
    """Custom type esysResetDefaultsSwitch based on Integer32"""
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


_EsysResetDefaultsSwitch_Type.__name__ = "Integer32"
_EsysResetDefaultsSwitch_Object = MibScalar
esysResetDefaultsSwitch = _EsysResetDefaultsSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 3),
    _EsysResetDefaultsSwitch_Type()
)
esysResetDefaultsSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysResetDefaultsSwitch.setStatus("mandatory")
_EsysGatewayAddress_Type = IpAddress
_EsysGatewayAddress_Object = MibScalar
esysGatewayAddress = _EsysGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 4),
    _EsysGatewayAddress_Type()
)
esysGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esysGatewayAddress.setStatus("mandatory")
_EsysTrapAddressTable_Object = MibTable
esysTrapAddressTable = _EsysTrapAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    esysTrapAddressTable.setStatus("mandatory")
_EsysTrapEntry_Object = MibTableRow
esysTrapEntry = _EsysTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 5, 1)
)
esysTrapEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "esysTrapAddress"),
)
if mibBuilder.loadTexts:
    esysTrapEntry.setStatus("mandatory")
_EsysTrapAddress_Type = IpAddress
_EsysTrapAddress_Object = MibTableColumn
esysTrapAddress = _EsysTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 5, 1, 1),
    _EsysTrapAddress_Type()
)
esysTrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esysTrapAddress.setStatus("mandatory")


class _EsysUpdateSwitch_Type(Integer32):
    """Custom type esysUpdateSwitch based on Integer32"""
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


_EsysUpdateSwitch_Type.__name__ = "Integer32"
_EsysUpdateSwitch_Object = MibScalar
esysUpdateSwitch = _EsysUpdateSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 6),
    _EsysUpdateSwitch_Type()
)
esysUpdateSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esysUpdateSwitch.setStatus("mandatory")


class _EsysLastLoadHost_Type(OctetString):
    """Custom type esysLastLoadHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EsysLastLoadHost_Type.__name__ = "OctetString"
_EsysLastLoadHost_Object = MibScalar
esysLastLoadHost = _EsysLastLoadHost_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 1, 7),
    _EsysLastLoadHost_Type()
)
esysLastLoadHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysLastLoadHost.setStatus("mandatory")
_EsysStatus_ObjectIdentity = ObjectIdentity
esysStatus = _EsysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 2)
)


class _EsysDeviceState_Type(Integer32):
    """Custom type esysDeviceState based on Integer32"""
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


_EsysDeviceState_Type.__name__ = "Integer32"
_EsysDeviceState_Object = MibScalar
esysDeviceState = _EsysDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 2, 1),
    _EsysDeviceState_Type()
)
esysDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysDeviceState.setStatus("mandatory")


class _EsysDeviceBrokenReason_Type(Integer32):
    """Custom type esysDeviceBrokenReason based on Integer32"""
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
        *(("firmwareFail", 4),
          ("none", 1),
          ("onlineDiagFail", 3),
          ("selftestFail", 2))
    )


_EsysDeviceBrokenReason_Type.__name__ = "Integer32"
_EsysDeviceBrokenReason_Object = MibScalar
esysDeviceBrokenReason = _EsysDeviceBrokenReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 2, 2),
    _EsysDeviceBrokenReason_Type()
)
esysDeviceBrokenReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysDeviceBrokenReason.setStatus("mandatory")


class _EsysNvramFailed_Type(Integer32):
    """Custom type esysNvramFailed based on Integer32"""
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


_EsysNvramFailed_Type.__name__ = "Integer32"
_EsysNvramFailed_Object = MibScalar
esysNvramFailed = _EsysNvramFailed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 2, 3),
    _EsysNvramFailed_Type()
)
esysNvramFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysNvramFailed.setStatus("mandatory")
_EsysCounters_ObjectIdentity = ObjectIdentity
esysCounters = _EsysCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 3)
)
_EsysPowerups_Type = Counter32
_EsysPowerups_Object = MibScalar
esysPowerups = _EsysPowerups_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 3, 1),
    _EsysPowerups_Type()
)
esysPowerups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysPowerups.setStatus("mandatory")
_EsysMgmtResets_Type = Counter32
_EsysMgmtResets_Object = MibScalar
esysMgmtResets = _EsysMgmtResets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 3, 2),
    _EsysMgmtResets_Type()
)
esysMgmtResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysMgmtResets.setStatus("mandatory")
_EsysUnsolicitedResets_Type = Counter32
_EsysUnsolicitedResets_Object = MibScalar
esysUnsolicitedResets = _EsysUnsolicitedResets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 3, 3),
    _EsysUnsolicitedResets_Type()
)
esysUnsolicitedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysUnsolicitedResets.setStatus("mandatory")
_EsysConcConfig_ObjectIdentity = ObjectIdentity
esysConcConfig = _EsysConcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4)
)
_EsysFRUConfigTable_Object = MibTable
esysFRUConfigTable = _EsysFRUConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    esysFRUConfigTable.setStatus("mandatory")
_EsysFRUConfigEntry_Object = MibTableRow
esysFRUConfigEntry = _EsysFRUConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 1, 1)
)
esysFRUConfigEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "esysFRUIndex"),
)
if mibBuilder.loadTexts:
    esysFRUConfigEntry.setStatus("mandatory")
_EsysFRUIndex_Type = Integer32
_EsysFRUIndex_Object = MibTableColumn
esysFRUIndex = _EsysFRUIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 1, 1, 1),
    _EsysFRUIndex_Type()
)
esysFRUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysFRUIndex.setStatus("mandatory")
_EsysFRUSlot_Type = Integer32
_EsysFRUSlot_Object = MibTableColumn
esysFRUSlot = _EsysFRUSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 1, 1, 2),
    _EsysFRUSlot_Type()
)
esysFRUSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysFRUSlot.setStatus("mandatory")
_EsysFRUDesc_Type = DisplayString
_EsysFRUDesc_Object = MibTableColumn
esysFRUDesc = _EsysFRUDesc_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 1, 1, 3),
    _EsysFRUDesc_Type()
)
esysFRUDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysFRUDesc.setStatus("mandatory")


class _EsysFRUType_Type(Integer32):
    """Custom type esysFRUType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              29)
        )
    )
    namedValues = NamedValues(
        *(("ansi-SingleModeMgmtCard", 16),
          ("ansiMgmtCard", 2),
          ("ansiPortCard4line", 3),
          ("ansiPortCard6line", 29),
          ("apCard", 5),
          ("controllerBackplane", 8),
          ("dasAnsiASingleModeBfiCard", 22),
          ("dasAnsiFddiCard", 21),
          ("dasSingleModeAAnsiBfiCard", 23),
          ("dasSingleModeFddiCard", 24),
          ("empty", 1),
          ("fan", 4),
          ("fddiCard", 7),
          ("lowPowerPortCard4line", 10),
          ("lowPowerPortCard6line", 13),
          ("niCard", 6),
          ("obmUartCard", 27),
          ("opticalBypass", 26),
          ("qmCard", 9),
          ("sasSingleModeFddiCard", 25),
          ("singleMode-ANSIMgmtCard", 17),
          ("singleModeAnsiPortCard4line", 11),
          ("singleModeMgmtCard", 15),
          ("stpCopperPortCard6line", 14),
          ("thinwirePortCard6line", 12),
          ("threeNiCard", 20),
          ("upgradeApCard", 19))
    )


_EsysFRUType_Type.__name__ = "Integer32"
_EsysFRUType_Object = MibTableColumn
esysFRUType = _EsysFRUType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 1, 1, 4),
    _EsysFRUType_Type()
)
esysFRUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysFRUType.setStatus("mandatory")
_EsysFRURev_Type = Integer32
_EsysFRURev_Object = MibTableColumn
esysFRURev = _EsysFRURev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 1, 1, 5),
    _EsysFRURev_Type()
)
esysFRURev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysFRURev.setStatus("mandatory")


class _EsysFRUState_Type(Integer32):
    """Custom type esysFRUState based on Integer32"""
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
        *(("broken", 4),
          ("empty", 1),
          ("marginal", 3),
          ("obrNotSupported", 5),
          ("working", 2))
    )


_EsysFRUState_Type.__name__ = "Integer32"
_EsysFRUState_Object = MibTableColumn
esysFRUState = _EsysFRUState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 1, 1, 6),
    _EsysFRUState_Type()
)
esysFRUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esysFRUState.setStatus("mandatory")


class _EsysFddiPortTrapSwitch_Type(Integer32):
    """Custom type esysFddiPortTrapSwitch based on Integer32"""
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


_EsysFddiPortTrapSwitch_Type.__name__ = "Integer32"
_EsysFddiPortTrapSwitch_Object = MibScalar
esysFddiPortTrapSwitch = _EsysFddiPortTrapSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 2, 4, 2),
    _EsysFddiPortTrapSwitch_Type()
)
esysFddiPortTrapSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esysFddiPortTrapSwitch.setStatus("mandatory")
_Einterfaces_ObjectIdentity = ObjectIdentity
einterfaces = _Einterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3)
)
_EifTable_Object = MibTable
eifTable = _EifTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eifTable.setStatus("mandatory")
_EifEntry_Object = MibTableRow
eifEntry = _EifEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3, 1, 1)
)
eifEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "eifIndex"),
)
if mibBuilder.loadTexts:
    eifEntry.setStatus("mandatory")
_EifIndex_Type = Integer32
_EifIndex_Object = MibTableColumn
eifIndex = _EifIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3, 1, 1, 1),
    _EifIndex_Type()
)
eifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eifIndex.setStatus("mandatory")
_EifBadFramesReceived_Type = Counter32
_EifBadFramesReceived_Object = MibTableColumn
eifBadFramesReceived = _EifBadFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3, 1, 1, 2),
    _EifBadFramesReceived_Type()
)
eifBadFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eifBadFramesReceived.setStatus("mandatory")
_EifReceiveOverrun_Type = Counter32
_EifReceiveOverrun_Object = MibTableColumn
eifReceiveOverrun = _EifReceiveOverrun_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3, 1, 1, 3),
    _EifReceiveOverrun_Type()
)
eifReceiveOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eifReceiveOverrun.setStatus("mandatory")
_EifOversizeFrames_Type = Counter32
_EifOversizeFrames_Object = MibTableColumn
eifOversizeFrames = _EifOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3, 1, 1, 4),
    _EifOversizeFrames_Type()
)
eifOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eifOversizeFrames.setStatus("mandatory")
_EifTransmitFramesError_Type = Counter32
_EifTransmitFramesError_Object = MibTableColumn
eifTransmitFramesError = _EifTransmitFramesError_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3, 1, 1, 5),
    _EifTransmitFramesError_Type()
)
eifTransmitFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eifTransmitFramesError.setStatus("mandatory")


class _EifMgmtSetsAllowedSwitch_Type(Integer32):
    """Custom type eifMgmtSetsAllowedSwitch based on Integer32"""
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


_EifMgmtSetsAllowedSwitch_Type.__name__ = "Integer32"
_EifMgmtSetsAllowedSwitch_Object = MibTableColumn
eifMgmtSetsAllowedSwitch = _EifMgmtSetsAllowedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 3, 1, 1, 6),
    _EifMgmtSetsAllowedSwitch_Type()
)
eifMgmtSetsAllowedSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eifMgmtSetsAllowedSwitch.setStatus("mandatory")
_Ebridge_ObjectIdentity = ObjectIdentity
ebridge = _Ebridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4)
)
_EbrChar_ObjectIdentity = ObjectIdentity
ebrChar = _EbrChar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1)
)
_EbrLB100SpanningTreeVer_Type = Integer32
_EbrLB100SpanningTreeVer_Object = MibScalar
ebrLB100SpanningTreeVer = _EbrLB100SpanningTreeVer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 1),
    _EbrLB100SpanningTreeVer_Type()
)
ebrLB100SpanningTreeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrLB100SpanningTreeVer.setStatus("mandatory")
_Ebr802SpanningTreeVer_Type = Integer32
_Ebr802SpanningTreeVer_Object = MibScalar
ebr802SpanningTreeVer = _Ebr802SpanningTreeVer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 2),
    _Ebr802SpanningTreeVer_Type()
)
ebr802SpanningTreeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebr802SpanningTreeVer.setStatus("mandatory")
_EbrMaxForwardingDBEntries_Type = Integer32
_EbrMaxForwardingDBEntries_Object = MibScalar
ebrMaxForwardingDBEntries = _EbrMaxForwardingDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 3),
    _EbrMaxForwardingDBEntries_Type()
)
ebrMaxForwardingDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrMaxForwardingDBEntries.setStatus("mandatory")
_EbrMaxNVForwardingDBEntries_Type = Integer32
_EbrMaxNVForwardingDBEntries_Object = MibScalar
ebrMaxNVForwardingDBEntries = _EbrMaxNVForwardingDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 4),
    _EbrMaxNVForwardingDBEntries_Type()
)
ebrMaxNVForwardingDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrMaxNVForwardingDBEntries.setStatus("mandatory")
_EbrMaxProtocolDBEntries_Type = Integer32
_EbrMaxProtocolDBEntries_Object = MibScalar
ebrMaxProtocolDBEntries = _EbrMaxProtocolDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 5),
    _EbrMaxProtocolDBEntries_Type()
)
ebrMaxProtocolDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrMaxProtocolDBEntries.setStatus("mandatory")
_EbrMaxNVProtocolDBEntries_Type = Integer32
_EbrMaxNVProtocolDBEntries_Object = MibScalar
ebrMaxNVProtocolDBEntries = _EbrMaxNVProtocolDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 6),
    _EbrMaxNVProtocolDBEntries_Type()
)
ebrMaxNVProtocolDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrMaxNVProtocolDBEntries.setStatus("mandatory")
_EbrForwardingDBPurgeThreshold_Type = Integer32
_EbrForwardingDBPurgeThreshold_Object = MibScalar
ebrForwardingDBPurgeThreshold = _EbrForwardingDBPurgeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 7),
    _EbrForwardingDBPurgeThreshold_Type()
)
ebrForwardingDBPurgeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrForwardingDBPurgeThreshold.setStatus("mandatory")
_EbrPortTestPassedThreshold_Type = Integer32
_EbrPortTestPassedThreshold_Object = MibScalar
ebrPortTestPassedThreshold = _EbrPortTestPassedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 8),
    _EbrPortTestPassedThreshold_Type()
)
ebrPortTestPassedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrPortTestPassedThreshold.setStatus("mandatory")
_EbrPortTestInterval_Type = Integer32
_EbrPortTestInterval_Object = MibScalar
ebrPortTestInterval = _EbrPortTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 9),
    _EbrPortTestInterval_Type()
)
ebrPortTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrPortTestInterval.setStatus("mandatory")
_EbrTopologyChangeTimer_Type = Integer32
_EbrTopologyChangeTimer_Object = MibScalar
ebrTopologyChangeTimer = _EbrTopologyChangeTimer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 10),
    _EbrTopologyChangeTimer_Type()
)
ebrTopologyChangeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrTopologyChangeTimer.setStatus("mandatory")


class _EbrManualFilterSwitch_Type(Integer32):
    """Custom type ebrManualFilterSwitch based on Integer32"""
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


_EbrManualFilterSwitch_Type.__name__ = "Integer32"
_EbrManualFilterSwitch_Object = MibScalar
ebrManualFilterSwitch = _EbrManualFilterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 11),
    _EbrManualFilterSwitch_Type()
)
ebrManualFilterSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrManualFilterSwitch.setStatus("mandatory")


class _EbrFragmentationSwitch_Type(Integer32):
    """Custom type ebrFragmentationSwitch based on Integer32"""
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


_EbrFragmentationSwitch_Type.__name__ = "Integer32"
_EbrFragmentationSwitch_Object = MibScalar
ebrFragmentationSwitch = _EbrFragmentationSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 12),
    _EbrFragmentationSwitch_Type()
)
ebrFragmentationSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrFragmentationSwitch.setStatus("mandatory")


class _EbrRemoveMgmtAddress_Type(Integer32):
    """Custom type ebrRemoveMgmtAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("true", 2))
    )


_EbrRemoveMgmtAddress_Type.__name__ = "Integer32"
_EbrRemoveMgmtAddress_Object = MibScalar
ebrRemoveMgmtAddress = _EbrRemoveMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 13),
    _EbrRemoveMgmtAddress_Type()
)
ebrRemoveMgmtAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrRemoveMgmtAddress.setStatus("mandatory")


class _EbrRemoveMgmtProto_Type(Integer32):
    """Custom type ebrRemoveMgmtProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("true", 2))
    )


_EbrRemoveMgmtProto_Type.__name__ = "Integer32"
_EbrRemoveMgmtProto_Object = MibScalar
ebrRemoveMgmtProto = _EbrRemoveMgmtProto_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 1, 14),
    _EbrRemoveMgmtProto_Type()
)
ebrRemoveMgmtProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrRemoveMgmtProto.setStatus("mandatory")
_EbrStat_ObjectIdentity = ObjectIdentity
ebrStat = _EbrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2)
)
_EbrCurrForwardingDBEntries_Type = Integer32
_EbrCurrForwardingDBEntries_Object = MibScalar
ebrCurrForwardingDBEntries = _EbrCurrForwardingDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 1),
    _EbrCurrForwardingDBEntries_Type()
)
ebrCurrForwardingDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrCurrForwardingDBEntries.setStatus("mandatory")
_EbrCurrNVForwardingDBEntries_Type = Integer32
_EbrCurrNVForwardingDBEntries_Object = MibScalar
ebrCurrNVForwardingDBEntries = _EbrCurrNVForwardingDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 2),
    _EbrCurrNVForwardingDBEntries_Type()
)
ebrCurrNVForwardingDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrCurrNVForwardingDBEntries.setStatus("mandatory")
_EbrCurrProtocolDBEntries_Type = Integer32
_EbrCurrProtocolDBEntries_Object = MibScalar
ebrCurrProtocolDBEntries = _EbrCurrProtocolDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 3),
    _EbrCurrProtocolDBEntries_Type()
)
ebrCurrProtocolDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrCurrProtocolDBEntries.setStatus("mandatory")
_EbrCurrNVProtocolDBEntries_Type = Integer32
_EbrCurrNVProtocolDBEntries_Object = MibScalar
ebrCurrNVProtocolDBEntries = _EbrCurrNVProtocolDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 4),
    _EbrCurrNVProtocolDBEntries_Type()
)
ebrCurrNVProtocolDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrCurrNVProtocolDBEntries.setStatus("mandatory")
_EbrMgmtHeardPort_Type = Integer32
_EbrMgmtHeardPort_Object = MibScalar
ebrMgmtHeardPort = _EbrMgmtHeardPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 5),
    _EbrMgmtHeardPort_Type()
)
ebrMgmtHeardPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrMgmtHeardPort.setStatus("mandatory")


class _EbrLB100BeingPolled_Type(OctetString):
    """Custom type ebrLB100BeingPolled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrLB100BeingPolled_Type.__name__ = "OctetString"
_EbrLB100BeingPolled_Object = MibScalar
ebrLB100BeingPolled = _EbrLB100BeingPolled_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 6),
    _EbrLB100BeingPolled_Type()
)
ebrLB100BeingPolled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrLB100BeingPolled.setStatus("mandatory")
_EbrInactiveForwardingDBEntries_Type = Integer32
_EbrInactiveForwardingDBEntries_Object = MibScalar
ebrInactiveForwardingDBEntries = _EbrInactiveForwardingDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 7),
    _EbrInactiveForwardingDBEntries_Type()
)
ebrInactiveForwardingDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrInactiveForwardingDBEntries.setStatus("mandatory")
_EbrTimeSinceForwardingDBPurged_Type = Integer32
_EbrTimeSinceForwardingDBPurged_Object = MibScalar
ebrTimeSinceForwardingDBPurged = _EbrTimeSinceForwardingDBPurged_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 8),
    _EbrTimeSinceForwardingDBPurged_Type()
)
ebrTimeSinceForwardingDBPurged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrTimeSinceForwardingDBPurged.setStatus("mandatory")
_EbrTimeSinceLastHello_Type = Integer32
_EbrTimeSinceLastHello_Object = MibScalar
ebrTimeSinceLastHello = _EbrTimeSinceLastHello_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 2, 9),
    _EbrTimeSinceLastHello_Type()
)
ebrTimeSinceLastHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrTimeSinceLastHello.setStatus("mandatory")
_EbrCoun_ObjectIdentity = ObjectIdentity
ebrCoun = _EbrCoun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 3)
)
_EbrDeviceFramesLost_Type = Counter32
_EbrDeviceFramesLost_Object = MibScalar
ebrDeviceFramesLost = _EbrDeviceFramesLost_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 3, 1),
    _EbrDeviceFramesLost_Type()
)
ebrDeviceFramesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrDeviceFramesLost.setStatus("mandatory")
_EbrSpanningTreeModeChanges_Type = Counter32
_EbrSpanningTreeModeChanges_Object = MibScalar
ebrSpanningTreeModeChanges = _EbrSpanningTreeModeChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 3, 2),
    _EbrSpanningTreeModeChanges_Type()
)
ebrSpanningTreeModeChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrSpanningTreeModeChanges.setStatus("mandatory")
_EbrSpan_ObjectIdentity = ObjectIdentity
ebrSpan = _EbrSpan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4)
)
_EbrBestRootAge_Type = Integer32
_EbrBestRootAge_Object = MibScalar
ebrBestRootAge = _EbrBestRootAge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 1),
    _EbrBestRootAge_Type()
)
ebrBestRootAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrBestRootAge.setStatus("mandatory")


class _EbrTopologyChangeFlag_Type(Integer32):
    """Custom type ebrTopologyChangeFlag based on Integer32"""
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


_EbrTopologyChangeFlag_Type.__name__ = "Integer32"
_EbrTopologyChangeFlag_Object = MibScalar
ebrTopologyChangeFlag = _EbrTopologyChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 2),
    _EbrTopologyChangeFlag_Type()
)
ebrTopologyChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrTopologyChangeFlag.setStatus("mandatory")


class _EbrTellParentFlag_Type(Integer32):
    """Custom type ebrTellParentFlag based on Integer32"""
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


_EbrTellParentFlag_Type.__name__ = "Integer32"
_EbrTellParentFlag_Object = MibScalar
ebrTellParentFlag = _EbrTellParentFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 3),
    _EbrTellParentFlag_Type()
)
ebrTellParentFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrTellParentFlag.setStatus("mandatory")
_EbrForwardingDBShortAgingTime_Type = Integer32
_EbrForwardingDBShortAgingTime_Object = MibScalar
ebrForwardingDBShortAgingTime = _EbrForwardingDBShortAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 4),
    _EbrForwardingDBShortAgingTime_Type()
)
ebrForwardingDBShortAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrForwardingDBShortAgingTime.setStatus("mandatory")
_EbrBadHelloLimit_Type = Integer32
_EbrBadHelloLimit_Object = MibScalar
ebrBadHelloLimit = _EbrBadHelloLimit_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 5),
    _EbrBadHelloLimit_Type()
)
ebrBadHelloLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrBadHelloLimit.setStatus("mandatory")
_EbrBadHelloResetTimer_Type = Integer32
_EbrBadHelloResetTimer_Object = MibScalar
ebrBadHelloResetTimer = _EbrBadHelloResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 6),
    _EbrBadHelloResetTimer_Type()
)
ebrBadHelloResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrBadHelloResetTimer.setStatus("mandatory")
_EbrNoFrameInterval_Type = Integer32
_EbrNoFrameInterval_Object = MibScalar
ebrNoFrameInterval = _EbrNoFrameInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 7),
    _EbrNoFrameInterval_Type()
)
ebrNoFrameInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNoFrameInterval.setStatus("mandatory")
_EbrLB100PollTime_Type = Integer32
_EbrLB100PollTime_Object = MibScalar
ebrLB100PollTime = _EbrLB100PollTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 8),
    _EbrLB100PollTime_Type()
)
ebrLB100PollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrLB100PollTime.setStatus("mandatory")
_EbrLB100ResponseTimeout_Type = Integer32
_EbrLB100ResponseTimeout_Object = MibScalar
ebrLB100ResponseTimeout = _EbrLB100ResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 9),
    _EbrLB100ResponseTimeout_Type()
)
ebrLB100ResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrLB100ResponseTimeout.setStatus("mandatory")


class _EbrLB100SpanningTreeCompat_Type(Integer32):
    """Custom type ebrLB100SpanningTreeCompat based on Integer32"""
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


_EbrLB100SpanningTreeCompat_Type.__name__ = "Integer32"
_EbrLB100SpanningTreeCompat_Object = MibScalar
ebrLB100SpanningTreeCompat = _EbrLB100SpanningTreeCompat_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 4, 10),
    _EbrLB100SpanningTreeCompat_Type()
)
ebrLB100SpanningTreeCompat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrLB100SpanningTreeCompat.setStatus("mandatory")
_EbrInterfaces_ObjectIdentity = ObjectIdentity
ebrInterfaces = _EbrInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5)
)
_EbrIfTable_Object = MibTable
ebrIfTable = _EbrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ebrIfTable.setStatus("mandatory")
_EbrIfEntry_Object = MibTableRow
ebrIfEntry = _EbrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1)
)
ebrIfEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrIfIndex"),
)
if mibBuilder.loadTexts:
    ebrIfEntry.setStatus("mandatory")
_EbrIfIndex_Type = Integer32
_EbrIfIndex_Object = MibTableColumn
ebrIfIndex = _EbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 1),
    _EbrIfIndex_Type()
)
ebrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfIndex.setStatus("mandatory")


class _EbrIfLinkBrokenReason_Type(Integer32):
    """Custom type ebrIfLinkBrokenReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noFault", 1),
          ("possibleExternalFault", 3),
          ("possibleInternalFault", 2))
    )


_EbrIfLinkBrokenReason_Type.__name__ = "Integer32"
_EbrIfLinkBrokenReason_Object = MibTableColumn
ebrIfLinkBrokenReason = _EbrIfLinkBrokenReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 2),
    _EbrIfLinkBrokenReason_Type()
)
ebrIfLinkBrokenReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfLinkBrokenReason.setStatus("mandatory")
_EbrIfPortRestarts_Type = Counter32
_EbrIfPortRestarts_Object = MibTableColumn
ebrIfPortRestarts = _EbrIfPortRestarts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 3),
    _EbrIfPortRestarts_Type()
)
ebrIfPortRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfPortRestarts.setStatus("mandatory")
_EbrIfUnknownDAReceived_Type = Counter32
_EbrIfUnknownDAReceived_Object = MibTableColumn
ebrIfUnknownDAReceived = _EbrIfUnknownDAReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 4),
    _EbrIfUnknownDAReceived_Type()
)
ebrIfUnknownDAReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfUnknownDAReceived.setStatus("mandatory")
_EbrIfFramesAddrFiltered_Type = Counter32
_EbrIfFramesAddrFiltered_Object = MibTableColumn
ebrIfFramesAddrFiltered = _EbrIfFramesAddrFiltered_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 5),
    _EbrIfFramesAddrFiltered_Type()
)
ebrIfFramesAddrFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfFramesAddrFiltered.setStatus("mandatory")
_EbrIfMultiFramesFiltered_Type = Counter32
_EbrIfMultiFramesFiltered_Object = MibTableColumn
ebrIfMultiFramesFiltered = _EbrIfMultiFramesFiltered_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 6),
    _EbrIfMultiFramesFiltered_Type()
)
ebrIfMultiFramesFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfMultiFramesFiltered.setStatus("mandatory")
_EbrIfFramesProtocolFiltered_Type = Counter32
_EbrIfFramesProtocolFiltered_Object = MibTableColumn
ebrIfFramesProtocolFiltered = _EbrIfFramesProtocolFiltered_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 7),
    _EbrIfFramesProtocolFiltered_Type()
)
ebrIfFramesProtocolFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfFramesProtocolFiltered.setStatus("mandatory")
_EbrIfDeviceFramesSent_Type = Counter32
_EbrIfDeviceFramesSent_Object = MibTableColumn
ebrIfDeviceFramesSent = _EbrIfDeviceFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 8),
    _EbrIfDeviceFramesSent_Type()
)
ebrIfDeviceFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfDeviceFramesSent.setStatus("mandatory")
_EbrIfDeviceFramesReceived_Type = Counter32
_EbrIfDeviceFramesReceived_Object = MibTableColumn
ebrIfDeviceFramesReceived = _EbrIfDeviceFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 9),
    _EbrIfDeviceFramesReceived_Type()
)
ebrIfDeviceFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfDeviceFramesReceived.setStatus("mandatory")
_EbrIfDeviceBytesSent_Type = Counter32
_EbrIfDeviceBytesSent_Object = MibTableColumn
ebrIfDeviceBytesSent = _EbrIfDeviceBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 10),
    _EbrIfDeviceBytesSent_Type()
)
ebrIfDeviceBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfDeviceBytesSent.setStatus("mandatory")
_EbrIfDeviceBytesReceived_Type = Counter32
_EbrIfDeviceBytesReceived_Object = MibTableColumn
ebrIfDeviceBytesReceived = _EbrIfDeviceBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 11),
    _EbrIfDeviceBytesReceived_Type()
)
ebrIfDeviceBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfDeviceBytesReceived.setStatus("mandatory")
_EbrIfDeviceFramesLost_Type = Counter32
_EbrIfDeviceFramesLost_Object = MibTableColumn
ebrIfDeviceFramesLost = _EbrIfDeviceFramesLost_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 12),
    _EbrIfDeviceFramesLost_Type()
)
ebrIfDeviceFramesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfDeviceFramesLost.setStatus("mandatory")
_EbrIfMultiBytesSent_Type = Counter32
_EbrIfMultiBytesSent_Object = MibTableColumn
ebrIfMultiBytesSent = _EbrIfMultiBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 13),
    _EbrIfMultiBytesSent_Type()
)
ebrIfMultiBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfMultiBytesSent.setStatus("mandatory")
_EbrIfMultiBytesReceived_Type = Counter32
_EbrIfMultiBytesReceived_Object = MibTableColumn
ebrIfMultiBytesReceived = _EbrIfMultiBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 14),
    _EbrIfMultiBytesReceived_Type()
)
ebrIfMultiBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfMultiBytesReceived.setStatus("mandatory")
_EbrIfMultiDeviceFramesSent_Type = Counter32
_EbrIfMultiDeviceFramesSent_Object = MibTableColumn
ebrIfMultiDeviceFramesSent = _EbrIfMultiDeviceFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 15),
    _EbrIfMultiDeviceFramesSent_Type()
)
ebrIfMultiDeviceFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfMultiDeviceFramesSent.setStatus("mandatory")
_EbrIfMultiDeviceFramesReceived_Type = Counter32
_EbrIfMultiDeviceFramesReceived_Object = MibTableColumn
ebrIfMultiDeviceFramesReceived = _EbrIfMultiDeviceFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 16),
    _EbrIfMultiDeviceFramesReceived_Type()
)
ebrIfMultiDeviceFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfMultiDeviceFramesReceived.setStatus("mandatory")
_EbrIfMultiDeviceBytesSent_Type = Counter32
_EbrIfMultiDeviceBytesSent_Object = MibTableColumn
ebrIfMultiDeviceBytesSent = _EbrIfMultiDeviceBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 17),
    _EbrIfMultiDeviceBytesSent_Type()
)
ebrIfMultiDeviceBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfMultiDeviceBytesSent.setStatus("mandatory")
_EbrIfMultiDeviceBytesReceived_Type = Counter32
_EbrIfMultiDeviceBytesReceived_Object = MibTableColumn
ebrIfMultiDeviceBytesReceived = _EbrIfMultiDeviceBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 18),
    _EbrIfMultiDeviceBytesReceived_Type()
)
ebrIfMultiDeviceBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfMultiDeviceBytesReceived.setStatus("mandatory")
_EbrIfBadBytesReceived_Type = Counter32
_EbrIfBadBytesReceived_Object = MibTableColumn
ebrIfBadBytesReceived = _EbrIfBadBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 19),
    _EbrIfBadBytesReceived_Type()
)
ebrIfBadBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfBadBytesReceived.setStatus("mandatory")
_EbrIfBadHelloLimitExceeded_Type = Counter32
_EbrIfBadHelloLimitExceeded_Object = MibTableColumn
ebrIfBadHelloLimitExceeded = _EbrIfBadHelloLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 1, 1, 20),
    _EbrIfBadHelloLimitExceeded_Type()
)
ebrIfBadHelloLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfBadHelloLimitExceeded.setStatus("mandatory")
_EbrIfEtherTable_Object = MibTable
ebrIfEtherTable = _EbrIfEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ebrIfEtherTable.setStatus("mandatory")
_EbrIfEtherEntry_Object = MibTableRow
ebrIfEtherEntry = _EbrIfEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1)
)
ebrIfEtherEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrIfIndex"),
)
if mibBuilder.loadTexts:
    ebrIfEtherEntry.setStatus("mandatory")
_EbrIfEthIndex_Type = Integer32
_EbrIfEthIndex_Object = MibTableColumn
ebrIfEthIndex = _EbrIfEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 1),
    _EbrIfEthIndex_Type()
)
ebrIfEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfEthIndex.setStatus("mandatory")


class _EbrIfEthPhysicalMediumType_Type(Integer32):
    """Custom type ebrIfEthPhysicalMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7,
              8,
              9,
              10,
              11,
              24)
        )
    )
    namedValues = NamedValues(
        *(("dConnAuiIf", 9),
          ("fiberOpticLink850nmDualIdle", 8),
          ("fiberOpticLink850nmNoIdle", 7),
          ("fullDuplexFiberOptic1300nm", 24),
          ("ieeeFiberInterRepeaterLink", 6),
          ("stdAUIInterface", 1),
          ("thinwireInterface", 2),
          ("thinwireInterfaceNoLoop", 10),
          ("twistedPairInterface", 11))
    )


_EbrIfEthPhysicalMediumType_Type.__name__ = "Integer32"
_EbrIfEthPhysicalMediumType_Object = MibTableColumn
ebrIfEthPhysicalMediumType = _EbrIfEthPhysicalMediumType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 2),
    _EbrIfEthPhysicalMediumType_Type()
)
ebrIfEthPhysicalMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfEthPhysicalMediumType.setStatus("mandatory")


class _EbrIfEthCollisionPresenceTestSwitch_Type(Integer32):
    """Custom type ebrIfEthCollisionPresenceTestSwitch based on Integer32"""
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


_EbrIfEthCollisionPresenceTestSwitch_Type.__name__ = "Integer32"
_EbrIfEthCollisionPresenceTestSwitch_Object = MibTableColumn
ebrIfEthCollisionPresenceTestSwitch = _EbrIfEthCollisionPresenceTestSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 3),
    _EbrIfEthCollisionPresenceTestSwitch_Type()
)
ebrIfEthCollisionPresenceTestSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrIfEthCollisionPresenceTestSwitch.setStatus("mandatory")
_EbrIfEthCollisionTestFailed_Type = Counter32
_EbrIfEthCollisionTestFailed_Object = MibTableColumn
ebrIfEthCollisionTestFailed = _EbrIfEthCollisionTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 4),
    _EbrIfEthCollisionTestFailed_Type()
)
ebrIfEthCollisionTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfEthCollisionTestFailed.setStatus("mandatory")
_EbrIfEthFramingError_Type = Counter32
_EbrIfEthFramingError_Object = MibTableColumn
ebrIfEthFramingError = _EbrIfEthFramingError_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 5),
    _EbrIfEthFramingError_Type()
)
ebrIfEthFramingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfEthFramingError.setStatus("mandatory")
_EbrIfEthLengthError_Type = Counter32
_EbrIfEthLengthError_Object = MibTableColumn
ebrIfEthLengthError = _EbrIfEthLengthError_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 6),
    _EbrIfEthLengthError_Type()
)
ebrIfEthLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfEthLengthError.setStatus("mandatory")
_EbrIfEthTransmitMultipleCollisions_Type = Counter32
_EbrIfEthTransmitMultipleCollisions_Object = MibTableColumn
ebrIfEthTransmitMultipleCollisions = _EbrIfEthTransmitMultipleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 7),
    _EbrIfEthTransmitMultipleCollisions_Type()
)
ebrIfEthTransmitMultipleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfEthTransmitMultipleCollisions.setStatus("mandatory")
_EbrIfEthCarrierLoss_Type = Counter32
_EbrIfEthCarrierLoss_Object = MibTableColumn
ebrIfEthCarrierLoss = _EbrIfEthCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 8),
    _EbrIfEthCarrierLoss_Type()
)
ebrIfEthCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfEthCarrierLoss.setStatus("mandatory")
_EbrIfEthCollisionLimitExceeded_Type = Counter32
_EbrIfEthCollisionLimitExceeded_Object = MibTableColumn
ebrIfEthCollisionLimitExceeded = _EbrIfEthCollisionLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 2, 1, 9),
    _EbrIfEthCollisionLimitExceeded_Type()
)
ebrIfEthCollisionLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfEthCollisionLimitExceeded.setStatus("mandatory")
_EbrIfFddiTable_Object = MibTable
ebrIfFddiTable = _EbrIfFddiTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 3)
)
if mibBuilder.loadTexts:
    ebrIfFddiTable.setStatus("mandatory")
_EbrIfFddiEntry_Object = MibTableRow
ebrIfFddiEntry = _EbrIfFddiEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 3, 1)
)
ebrIfFddiEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrIfIndex"),
)
if mibBuilder.loadTexts:
    ebrIfFddiEntry.setStatus("mandatory")
_EbrIfFddiIndex_Type = Integer32
_EbrIfFddiIndex_Object = MibTableColumn
ebrIfFddiIndex = _EbrIfFddiIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 3, 1, 1),
    _EbrIfFddiIndex_Type()
)
ebrIfFddiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfFddiIndex.setStatus("mandatory")
_EbrIfFddiUnprocessedErrorPackets_Type = Counter32
_EbrIfFddiUnprocessedErrorPackets_Object = MibTableColumn
ebrIfFddiUnprocessedErrorPackets = _EbrIfFddiUnprocessedErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 3, 1, 2),
    _EbrIfFddiUnprocessedErrorPackets_Type()
)
ebrIfFddiUnprocessedErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfFddiUnprocessedErrorPackets.setStatus("mandatory")
_EbrIfFddiIpDatagramsFragmented_Type = Counter32
_EbrIfFddiIpDatagramsFragmented_Object = MibTableColumn
ebrIfFddiIpDatagramsFragmented = _EbrIfFddiIpDatagramsFragmented_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 3, 1, 3),
    _EbrIfFddiIpDatagramsFragmented_Type()
)
ebrIfFddiIpDatagramsFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfFddiIpDatagramsFragmented.setStatus("mandatory")
_EbrIfFddiIpDontFragment_Type = Counter32
_EbrIfFddiIpDontFragment_Object = MibTableColumn
ebrIfFddiIpDontFragment = _EbrIfFddiIpDontFragment_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 3, 1, 4),
    _EbrIfFddiIpDontFragment_Type()
)
ebrIfFddiIpDontFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfFddiIpDontFragment.setStatus("mandatory")
_EbrIfFddiIpIllegalHeaderLength_Type = Counter32
_EbrIfFddiIpIllegalHeaderLength_Object = MibTableColumn
ebrIfFddiIpIllegalHeaderLength = _EbrIfFddiIpIllegalHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 3, 1, 5),
    _EbrIfFddiIpIllegalHeaderLength_Type()
)
ebrIfFddiIpIllegalHeaderLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfFddiIpIllegalHeaderLength.setStatus("mandatory")
_EbrIfFddiIpIllegalSize_Type = Counter32
_EbrIfFddiIpIllegalSize_Object = MibTableColumn
ebrIfFddiIpIllegalSize = _EbrIfFddiIpIllegalSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 3, 1, 6),
    _EbrIfFddiIpIllegalSize_Type()
)
ebrIfFddiIpIllegalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfFddiIpIllegalSize.setStatus("mandatory")
_EbrIfSpanTable_Object = MibTable
ebrIfSpanTable = _EbrIfSpanTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 4)
)
if mibBuilder.loadTexts:
    ebrIfSpanTable.setStatus("mandatory")
_EbrIfSpanEntry_Object = MibTableRow
ebrIfSpanEntry = _EbrIfSpanEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 4, 1)
)
ebrIfSpanEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrIfIndex"),
)
if mibBuilder.loadTexts:
    ebrIfSpanEntry.setStatus("mandatory")
_EbrIfSpIndex_Type = Integer32
_EbrIfSpIndex_Object = MibTableColumn
ebrIfSpIndex = _EbrIfSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 4, 1, 1),
    _EbrIfSpIndex_Type()
)
ebrIfSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfSpIndex.setStatus("mandatory")
_EbrIfSpDesigRootAge_Type = Integer32
_EbrIfSpDesigRootAge_Object = MibTableColumn
ebrIfSpDesigRootAge = _EbrIfSpDesigRootAge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 4, 1, 2),
    _EbrIfSpDesigRootAge_Type()
)
ebrIfSpDesigRootAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfSpDesigRootAge.setStatus("mandatory")
_EbrIfSpForwardDelayTimer_Type = Integer32
_EbrIfSpForwardDelayTimer_Object = MibTableColumn
ebrIfSpForwardDelayTimer = _EbrIfSpForwardDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 4, 1, 3),
    _EbrIfSpForwardDelayTimer_Type()
)
ebrIfSpForwardDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfSpForwardDelayTimer.setStatus("mandatory")
_EbrIfSpBadHelloCount_Type = Counter32
_EbrIfSpBadHelloCount_Object = MibTableColumn
ebrIfSpBadHelloCount = _EbrIfSpBadHelloCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 4, 1, 4),
    _EbrIfSpBadHelloCount_Type()
)
ebrIfSpBadHelloCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfSpBadHelloCount.setStatus("mandatory")


class _EbrIfSpPossibleLoopFlag_Type(Integer32):
    """Custom type ebrIfSpPossibleLoopFlag based on Integer32"""
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


_EbrIfSpPossibleLoopFlag_Type.__name__ = "Integer32"
_EbrIfSpPossibleLoopFlag_Object = MibTableColumn
ebrIfSpPossibleLoopFlag = _EbrIfSpPossibleLoopFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 4, 1, 5),
    _EbrIfSpPossibleLoopFlag_Type()
)
ebrIfSpPossibleLoopFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfSpPossibleLoopFlag.setStatus("mandatory")


class _EbrIfSpTopologyChangeAckFlag_Type(Integer32):
    """Custom type ebrIfSpTopologyChangeAckFlag based on Integer32"""
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


_EbrIfSpTopologyChangeAckFlag_Type.__name__ = "Integer32"
_EbrIfSpTopologyChangeAckFlag_Object = MibTableColumn
ebrIfSpTopologyChangeAckFlag = _EbrIfSpTopologyChangeAckFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 5, 4, 1, 6),
    _EbrIfSpTopologyChangeAckFlag_Type()
)
ebrIfSpTopologyChangeAckFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrIfSpTopologyChangeAckFlag.setStatus("mandatory")
_EbrTwoPortStatic_ObjectIdentity = ObjectIdentity
ebrTwoPortStatic = _EbrTwoPortStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 6)
)
_EbrTwoPortStaticTable_Object = MibTable
ebrTwoPortStaticTable = _EbrTwoPortStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ebrTwoPortStaticTable.setStatus("mandatory")
_EbrTwoPortStaticEntry_Object = MibTableRow
ebrTwoPortStaticEntry = _EbrTwoPortStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 6, 1, 1)
)
ebrTwoPortStaticEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrTwoPortAddress"),
)
if mibBuilder.loadTexts:
    ebrTwoPortStaticEntry.setStatus("mandatory")


class _EbrTwoPortAddress_Type(OctetString):
    """Custom type ebrTwoPortAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrTwoPortAddress_Type.__name__ = "OctetString"
_EbrTwoPortAddress_Object = MibTableColumn
ebrTwoPortAddress = _EbrTwoPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 6, 1, 1, 1),
    _EbrTwoPortAddress_Type()
)
ebrTwoPortAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoPortAddress.setStatus("mandatory")
_EbrTwoPortPortNum_Type = Integer32
_EbrTwoPortPortNum_Object = MibTableColumn
ebrTwoPortPortNum = _EbrTwoPortPortNum_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 6, 1, 1, 2),
    _EbrTwoPortPortNum_Type()
)
ebrTwoPortPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoPortPortNum.setStatus("mandatory")


class _EbrTwoPortStatus_Type(Integer32):
    """Custom type ebrTwoPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("filter", 4),
          ("forward", 5),
          ("hello", 2),
          ("invalid", 3),
          ("lockDown", 1),
          ("rateLimit", 6))
    )


_EbrTwoPortStatus_Type.__name__ = "Integer32"
_EbrTwoPortStatus_Object = MibTableColumn
ebrTwoPortStatus = _EbrTwoPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 6, 1, 1, 3),
    _EbrTwoPortStatus_Type()
)
ebrTwoPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoPortStatus.setStatus("mandatory")
_EbrMultiPortStatic_ObjectIdentity = ObjectIdentity
ebrMultiPortStatic = _EbrMultiPortStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 7)
)
_EbrMultiPortStaticTable_Object = MibTable
ebrMultiPortStaticTable = _EbrMultiPortStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    ebrMultiPortStaticTable.setStatus("mandatory")
_EbrMultiPortStaticEntry_Object = MibTableRow
ebrMultiPortStaticEntry = _EbrMultiPortStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 7, 1, 1)
)
ebrMultiPortStaticEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrMultiPortAddress"),
    (0, "DEC-ELAN-MIB", "ebrMultiPortReceivePort"),
)
if mibBuilder.loadTexts:
    ebrMultiPortStaticEntry.setStatus("mandatory")


class _EbrMultiPortAddress_Type(OctetString):
    """Custom type ebrMultiPortAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EbrMultiPortAddress_Type.__name__ = "OctetString"
_EbrMultiPortAddress_Object = MibTableColumn
ebrMultiPortAddress = _EbrMultiPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 7, 1, 1, 1),
    _EbrMultiPortAddress_Type()
)
ebrMultiPortAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiPortAddress.setStatus("mandatory")
_EbrMultiPortReceivePort_Type = Integer32
_EbrMultiPortReceivePort_Object = MibTableColumn
ebrMultiPortReceivePort = _EbrMultiPortReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 7, 1, 1, 2),
    _EbrMultiPortReceivePort_Type()
)
ebrMultiPortReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiPortReceivePort.setStatus("mandatory")
_EbrMultiPortAllowedToGoTo_Type = OctetString
_EbrMultiPortAllowedToGoTo_Object = MibTableColumn
ebrMultiPortAllowedToGoTo = _EbrMultiPortAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 7, 1, 1, 3),
    _EbrMultiPortAllowedToGoTo_Type()
)
ebrMultiPortAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiPortAllowedToGoTo.setStatus("mandatory")
_EbrMultiPortPortNum_Type = Integer32
_EbrMultiPortPortNum_Object = MibTableColumn
ebrMultiPortPortNum = _EbrMultiPortPortNum_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 7, 1, 1, 4),
    _EbrMultiPortPortNum_Type()
)
ebrMultiPortPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiPortPortNum.setStatus("mandatory")


class _EbrMultiPortStatus_Type(Integer32):
    """Custom type ebrMultiPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("filter", 5),
          ("hello", 4),
          ("invalid", 6),
          ("lockDown", 2),
          ("maskAndLock", 3),
          ("portMask", 1),
          ("rateLimit", 7))
    )


_EbrMultiPortStatus_Type.__name__ = "Integer32"
_EbrMultiPortStatus_Object = MibTableColumn
ebrMultiPortStatus = _EbrMultiPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 7, 1, 1, 5),
    _EbrMultiPortStatus_Type()
)
ebrMultiPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiPortStatus.setStatus("mandatory")
_EbrTwoProtoFilt_ObjectIdentity = ObjectIdentity
ebrTwoProtoFilt = _EbrTwoProtoFilt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8)
)


class _EbrTwoProtoEnetFilterOther_Type(Integer32):
    """Custom type ebrTwoProtoEnetFilterOther based on Integer32"""
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


_EbrTwoProtoEnetFilterOther_Type.__name__ = "Integer32"
_EbrTwoProtoEnetFilterOther_Object = MibScalar
ebrTwoProtoEnetFilterOther = _EbrTwoProtoEnetFilterOther_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 1),
    _EbrTwoProtoEnetFilterOther_Type()
)
ebrTwoProtoEnetFilterOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoProtoEnetFilterOther.setStatus("mandatory")


class _EbrTwoProtoSapFilterOther_Type(Integer32):
    """Custom type ebrTwoProtoSapFilterOther based on Integer32"""
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


_EbrTwoProtoSapFilterOther_Type.__name__ = "Integer32"
_EbrTwoProtoSapFilterOther_Object = MibScalar
ebrTwoProtoSapFilterOther = _EbrTwoProtoSapFilterOther_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 2),
    _EbrTwoProtoSapFilterOther_Type()
)
ebrTwoProtoSapFilterOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoProtoSapFilterOther.setStatus("mandatory")


class _EbrTwoProtoSnapFilterOther_Type(Integer32):
    """Custom type ebrTwoProtoSnapFilterOther based on Integer32"""
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


_EbrTwoProtoSnapFilterOther_Type.__name__ = "Integer32"
_EbrTwoProtoSnapFilterOther_Object = MibScalar
ebrTwoProtoSnapFilterOther = _EbrTwoProtoSnapFilterOther_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 3),
    _EbrTwoProtoSnapFilterOther_Type()
)
ebrTwoProtoSnapFilterOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoProtoSnapFilterOther.setStatus("mandatory")
_EbrTwoEnetProtoTable_Object = MibTable
ebrTwoEnetProtoTable = _EbrTwoEnetProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 4)
)
if mibBuilder.loadTexts:
    ebrTwoEnetProtoTable.setStatus("mandatory")
_EbrTwoEnetProtoEntry_Object = MibTableRow
ebrTwoEnetProtoEntry = _EbrTwoEnetProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 4, 1)
)
ebrTwoEnetProtoEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrTwoEnetProtoType"),
)
if mibBuilder.loadTexts:
    ebrTwoEnetProtoEntry.setStatus("mandatory")


class _EbrTwoEnetProtoType_Type(OctetString):
    """Custom type ebrTwoEnetProtoType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_EbrTwoEnetProtoType_Type.__name__ = "OctetString"
_EbrTwoEnetProtoType_Object = MibTableColumn
ebrTwoEnetProtoType = _EbrTwoEnetProtoType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 4, 1, 1),
    _EbrTwoEnetProtoType_Type()
)
ebrTwoEnetProtoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoEnetProtoType.setStatus("mandatory")


class _EbrTwoEnetProtoStatus_Type(Integer32):
    """Custom type ebrTwoEnetProtoStatus based on Integer32"""
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
        *(("filter", 2),
          ("forward", 1),
          ("invalid", 3),
          ("rateLimit", 4))
    )


_EbrTwoEnetProtoStatus_Type.__name__ = "Integer32"
_EbrTwoEnetProtoStatus_Object = MibTableColumn
ebrTwoEnetProtoStatus = _EbrTwoEnetProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 4, 1, 2),
    _EbrTwoEnetProtoStatus_Type()
)
ebrTwoEnetProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoEnetProtoStatus.setStatus("mandatory")
_EbrTwoSapProtoTable_Object = MibTable
ebrTwoSapProtoTable = _EbrTwoSapProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 5)
)
if mibBuilder.loadTexts:
    ebrTwoSapProtoTable.setStatus("mandatory")
_EbrTwoSapProtoEntry_Object = MibTableRow
ebrTwoSapProtoEntry = _EbrTwoSapProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 5, 1)
)
ebrTwoSapProtoEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrTwoSapIndex"),
)
if mibBuilder.loadTexts:
    ebrTwoSapProtoEntry.setStatus("mandatory")


class _EbrTwoSapIndex_Type(Integer32):
    """Custom type ebrTwoSapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EbrTwoSapIndex_Type.__name__ = "Integer32"
_EbrTwoSapIndex_Object = MibTableColumn
ebrTwoSapIndex = _EbrTwoSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 5, 1, 1),
    _EbrTwoSapIndex_Type()
)
ebrTwoSapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrTwoSapIndex.setStatus("mandatory")


class _EbrTwoSapValue_Type(OctetString):
    """Custom type ebrTwoSapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EbrTwoSapValue_Type.__name__ = "OctetString"
_EbrTwoSapValue_Object = MibTableColumn
ebrTwoSapValue = _EbrTwoSapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 5, 1, 2),
    _EbrTwoSapValue_Type()
)
ebrTwoSapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoSapValue.setStatus("mandatory")


class _EbrTwoSapStatus_Type(Integer32):
    """Custom type ebrTwoSapStatus based on Integer32"""
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
        *(("filter", 2),
          ("forward", 1),
          ("invalid", 3),
          ("rateLimit", 4))
    )


_EbrTwoSapStatus_Type.__name__ = "Integer32"
_EbrTwoSapStatus_Object = MibTableColumn
ebrTwoSapStatus = _EbrTwoSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 5, 1, 3),
    _EbrTwoSapStatus_Type()
)
ebrTwoSapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoSapStatus.setStatus("mandatory")
_EbrTwoSnapProtoTable_Object = MibTable
ebrTwoSnapProtoTable = _EbrTwoSnapProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 6)
)
if mibBuilder.loadTexts:
    ebrTwoSnapProtoTable.setStatus("mandatory")
_EbrTwoSnapProtoEntry_Object = MibTableRow
ebrTwoSnapProtoEntry = _EbrTwoSnapProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 6, 1)
)
ebrTwoSnapProtoEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrTwoSnapIndex"),
)
if mibBuilder.loadTexts:
    ebrTwoSnapProtoEntry.setStatus("mandatory")
_EbrTwoSnapIndex_Type = Integer32
_EbrTwoSnapIndex_Object = MibTableColumn
ebrTwoSnapIndex = _EbrTwoSnapIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 6, 1, 1),
    _EbrTwoSnapIndex_Type()
)
ebrTwoSnapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrTwoSnapIndex.setStatus("mandatory")


class _EbrTwoSnapValue_Type(OctetString):
    """Custom type ebrTwoSnapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_EbrTwoSnapValue_Type.__name__ = "OctetString"
_EbrTwoSnapValue_Object = MibTableColumn
ebrTwoSnapValue = _EbrTwoSnapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 6, 1, 2),
    _EbrTwoSnapValue_Type()
)
ebrTwoSnapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoSnapValue.setStatus("mandatory")


class _EbrTwoSnapStatus_Type(Integer32):
    """Custom type ebrTwoSnapStatus based on Integer32"""
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
        *(("filter", 2),
          ("forward", 1),
          ("invalid", 3),
          ("rateLimit", 4))
    )


_EbrTwoSnapStatus_Type.__name__ = "Integer32"
_EbrTwoSnapStatus_Object = MibTableColumn
ebrTwoSnapStatus = _EbrTwoSnapStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 8, 6, 1, 3),
    _EbrTwoSnapStatus_Type()
)
ebrTwoSnapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrTwoSnapStatus.setStatus("mandatory")
_EbrMultiProtoFilt_ObjectIdentity = ObjectIdentity
ebrMultiProtoFilt = _EbrMultiProtoFilt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9)
)
_EbrMultiEnetProtoTable_Object = MibTable
ebrMultiEnetProtoTable = _EbrMultiEnetProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 1)
)
if mibBuilder.loadTexts:
    ebrMultiEnetProtoTable.setStatus("mandatory")
_EbrMultiEnetProtoEntry_Object = MibTableRow
ebrMultiEnetProtoEntry = _EbrMultiEnetProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 1, 1)
)
ebrMultiEnetProtoEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrMultiEnetProtoType"),
    (0, "DEC-ELAN-MIB", "ebrMultiEnetReceivePort"),
)
if mibBuilder.loadTexts:
    ebrMultiEnetProtoEntry.setStatus("mandatory")


class _EbrMultiEnetProtoType_Type(OctetString):
    """Custom type ebrMultiEnetProtoType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_EbrMultiEnetProtoType_Type.__name__ = "OctetString"
_EbrMultiEnetProtoType_Object = MibTableColumn
ebrMultiEnetProtoType = _EbrMultiEnetProtoType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 1, 1, 1),
    _EbrMultiEnetProtoType_Type()
)
ebrMultiEnetProtoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiEnetProtoType.setStatus("mandatory")
_EbrMultiEnetReceivePort_Type = Integer32
_EbrMultiEnetReceivePort_Object = MibTableColumn
ebrMultiEnetReceivePort = _EbrMultiEnetReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 1, 1, 2),
    _EbrMultiEnetReceivePort_Type()
)
ebrMultiEnetReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiEnetReceivePort.setStatus("mandatory")
_EbrMultiEnetAllowedToGoTo_Type = OctetString
_EbrMultiEnetAllowedToGoTo_Object = MibTableColumn
ebrMultiEnetAllowedToGoTo = _EbrMultiEnetAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 1, 1, 3),
    _EbrMultiEnetAllowedToGoTo_Type()
)
ebrMultiEnetAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiEnetAllowedToGoTo.setStatus("mandatory")


class _EbrMultiEnetStatus_Type(Integer32):
    """Custom type ebrMultiEnetStatus based on Integer32"""
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
        *(("filter", 3),
          ("forward", 4),
          ("invalid", 2),
          ("portMask", 1),
          ("rateLimit", 5))
    )


_EbrMultiEnetStatus_Type.__name__ = "Integer32"
_EbrMultiEnetStatus_Object = MibTableColumn
ebrMultiEnetStatus = _EbrMultiEnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 1, 1, 4),
    _EbrMultiEnetStatus_Type()
)
ebrMultiEnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiEnetStatus.setStatus("mandatory")
_EbrMultiSapProtoTable_Object = MibTable
ebrMultiSapProtoTable = _EbrMultiSapProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 2)
)
if mibBuilder.loadTexts:
    ebrMultiSapProtoTable.setStatus("mandatory")
_EbrMultiSapProtoEntry_Object = MibTableRow
ebrMultiSapProtoEntry = _EbrMultiSapProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 2, 1)
)
ebrMultiSapProtoEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrMultiSapValue"),
    (0, "DEC-ELAN-MIB", "ebrMultiSapReceivePort"),
)
if mibBuilder.loadTexts:
    ebrMultiSapProtoEntry.setStatus("mandatory")


class _EbrMultiSapValue_Type(OctetString):
    """Custom type ebrMultiSapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EbrMultiSapValue_Type.__name__ = "OctetString"
_EbrMultiSapValue_Object = MibTableColumn
ebrMultiSapValue = _EbrMultiSapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 2, 1, 1),
    _EbrMultiSapValue_Type()
)
ebrMultiSapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSapValue.setStatus("mandatory")
_EbrMultiSapReceivePort_Type = Integer32
_EbrMultiSapReceivePort_Object = MibTableColumn
ebrMultiSapReceivePort = _EbrMultiSapReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 2, 1, 2),
    _EbrMultiSapReceivePort_Type()
)
ebrMultiSapReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSapReceivePort.setStatus("mandatory")
_EbrMultiSapAllowedToGoTo_Type = OctetString
_EbrMultiSapAllowedToGoTo_Object = MibTableColumn
ebrMultiSapAllowedToGoTo = _EbrMultiSapAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 2, 1, 3),
    _EbrMultiSapAllowedToGoTo_Type()
)
ebrMultiSapAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSapAllowedToGoTo.setStatus("mandatory")


class _EbrMultiSapStatus_Type(Integer32):
    """Custom type ebrMultiSapStatus based on Integer32"""
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
        *(("filter", 3),
          ("forward", 4),
          ("invalid", 2),
          ("portMask", 1),
          ("rateLimit", 5))
    )


_EbrMultiSapStatus_Type.__name__ = "Integer32"
_EbrMultiSapStatus_Object = MibTableColumn
ebrMultiSapStatus = _EbrMultiSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 2, 1, 4),
    _EbrMultiSapStatus_Type()
)
ebrMultiSapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSapStatus.setStatus("mandatory")
_EbrMultiSnapProtoTable_Object = MibTable
ebrMultiSnapProtoTable = _EbrMultiSnapProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 3)
)
if mibBuilder.loadTexts:
    ebrMultiSnapProtoTable.setStatus("mandatory")
_EbrMultiSnapProtoEntry_Object = MibTableRow
ebrMultiSnapProtoEntry = _EbrMultiSnapProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 3, 1)
)
ebrMultiSnapProtoEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrMultiSnapValue"),
    (0, "DEC-ELAN-MIB", "ebrMultiSnapReceivePort"),
)
if mibBuilder.loadTexts:
    ebrMultiSnapProtoEntry.setStatus("mandatory")


class _EbrMultiSnapValue_Type(OctetString):
    """Custom type ebrMultiSnapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_EbrMultiSnapValue_Type.__name__ = "OctetString"
_EbrMultiSnapValue_Object = MibTableColumn
ebrMultiSnapValue = _EbrMultiSnapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 3, 1, 1),
    _EbrMultiSnapValue_Type()
)
ebrMultiSnapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSnapValue.setStatus("mandatory")
_EbrMultiSnapReceivePort_Type = Integer32
_EbrMultiSnapReceivePort_Object = MibTableColumn
ebrMultiSnapReceivePort = _EbrMultiSnapReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 3, 1, 2),
    _EbrMultiSnapReceivePort_Type()
)
ebrMultiSnapReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSnapReceivePort.setStatus("mandatory")
_EbrMultiSnapAllowedToGoTo_Type = OctetString
_EbrMultiSnapAllowedToGoTo_Object = MibTableColumn
ebrMultiSnapAllowedToGoTo = _EbrMultiSnapAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 3, 1, 3),
    _EbrMultiSnapAllowedToGoTo_Type()
)
ebrMultiSnapAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSnapAllowedToGoTo.setStatus("mandatory")


class _EbrMultiSnapStatus_Type(Integer32):
    """Custom type ebrMultiSnapStatus based on Integer32"""
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
        *(("filter", 3),
          ("forward", 4),
          ("invalid", 2),
          ("portMask", 1),
          ("rateLimit", 5))
    )


_EbrMultiSnapStatus_Type.__name__ = "Integer32"
_EbrMultiSnapStatus_Object = MibTableColumn
ebrMultiSnapStatus = _EbrMultiSnapStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 9, 3, 1, 4),
    _EbrMultiSnapStatus_Type()
)
ebrMultiSnapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSnapStatus.setStatus("mandatory")
_EbrMultiFiltSw_ObjectIdentity = ObjectIdentity
ebrMultiFiltSw = _EbrMultiFiltSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 10)
)
_EbrMultiSwTable_Object = MibTable
ebrMultiSwTable = _EbrMultiSwTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 10, 1)
)
if mibBuilder.loadTexts:
    ebrMultiSwTable.setStatus("mandatory")
_EbrMultiSwEntry_Object = MibTableRow
ebrMultiSwEntry = _EbrMultiSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 10, 1, 1)
)
ebrMultiSwEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrMultiSwIndex"),
)
if mibBuilder.loadTexts:
    ebrMultiSwEntry.setStatus("mandatory")
_EbrMultiSwIndex_Type = Integer32
_EbrMultiSwIndex_Object = MibTableColumn
ebrMultiSwIndex = _EbrMultiSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 10, 1, 1, 1),
    _EbrMultiSwIndex_Type()
)
ebrMultiSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrMultiSwIndex.setStatus("mandatory")


class _EbrMultiSwManualFilter_Type(Integer32):
    """Custom type ebrMultiSwManualFilter based on Integer32"""
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


_EbrMultiSwManualFilter_Type.__name__ = "Integer32"
_EbrMultiSwManualFilter_Object = MibTableColumn
ebrMultiSwManualFilter = _EbrMultiSwManualFilter_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 10, 1, 1, 2),
    _EbrMultiSwManualFilter_Type()
)
ebrMultiSwManualFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSwManualFilter.setStatus("mandatory")


class _EbrMultiSwProtoEnetOther_Type(Integer32):
    """Custom type ebrMultiSwProtoEnetOther based on Integer32"""
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


_EbrMultiSwProtoEnetOther_Type.__name__ = "Integer32"
_EbrMultiSwProtoEnetOther_Object = MibTableColumn
ebrMultiSwProtoEnetOther = _EbrMultiSwProtoEnetOther_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 10, 1, 1, 3),
    _EbrMultiSwProtoEnetOther_Type()
)
ebrMultiSwProtoEnetOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSwProtoEnetOther.setStatus("mandatory")


class _EbrMultiSwProtoSapOther_Type(Integer32):
    """Custom type ebrMultiSwProtoSapOther based on Integer32"""
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


_EbrMultiSwProtoSapOther_Type.__name__ = "Integer32"
_EbrMultiSwProtoSapOther_Object = MibTableColumn
ebrMultiSwProtoSapOther = _EbrMultiSwProtoSapOther_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 10, 1, 1, 4),
    _EbrMultiSwProtoSapOther_Type()
)
ebrMultiSwProtoSapOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSwProtoSapOther.setStatus("mandatory")


class _EbrMultiSwProtoSnapOther_Type(Integer32):
    """Custom type ebrMultiSwProtoSnapOther based on Integer32"""
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


_EbrMultiSwProtoSnapOther_Type.__name__ = "Integer32"
_EbrMultiSwProtoSnapOther_Object = MibTableColumn
ebrMultiSwProtoSnapOther = _EbrMultiSwProtoSnapOther_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 10, 1, 1, 5),
    _EbrMultiSwProtoSnapOther_Type()
)
ebrMultiSwProtoSnapOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrMultiSwProtoSnapOther.setStatus("mandatory")
_EbrNTP_ObjectIdentity = ObjectIdentity
ebrNTP = _EbrNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 11)
)
_EbrNTPTable_Object = MibTable
ebrNTPTable = _EbrNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 11, 1)
)
if mibBuilder.loadTexts:
    ebrNTPTable.setStatus("mandatory")
_EbrNTPEntry_Object = MibTableRow
ebrNTPEntry = _EbrNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 11, 1, 1)
)
ebrNTPEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrNTPtype"),
)
if mibBuilder.loadTexts:
    ebrNTPEntry.setStatus("mandatory")


class _EbrNTPtype_Type(OctetString):
    """Custom type ebrNTPtype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_EbrNTPtype_Type.__name__ = "OctetString"
_EbrNTPtype_Object = MibTableColumn
ebrNTPtype = _EbrNTPtype_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 11, 1, 1, 1),
    _EbrNTPtype_Type()
)
ebrNTPtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNTPtype.setStatus("mandatory")


class _EbrNTPStatus_Type(Integer32):
    """Custom type ebrNTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_EbrNTPStatus_Type.__name__ = "Integer32"
_EbrNTPStatus_Object = MibTableColumn
ebrNTPStatus = _EbrNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 11, 1, 1, 2),
    _EbrNTPStatus_Type()
)
ebrNTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrNTPStatus.setStatus("mandatory")


class _EsysIPXSwitch_Type(Integer32):
    """Custom type esysIPXSwitch based on Integer32"""
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


_EsysIPXSwitch_Type.__name__ = "Integer32"
_EsysIPXSwitch_Object = MibScalar
esysIPXSwitch = _EsysIPXSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 11, 2),
    _EsysIPXSwitch_Type()
)
esysIPXSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esysIPXSwitch.setStatus("mandatory")
_EbrRateLimiting_ObjectIdentity = ObjectIdentity
ebrRateLimiting = _EbrRateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 12)
)


class _EbrRateLimitSwitch_Type(Integer32):
    """Custom type ebrRateLimitSwitch based on Integer32"""
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


_EbrRateLimitSwitch_Type.__name__ = "Integer32"
_EbrRateLimitSwitch_Object = MibScalar
ebrRateLimitSwitch = _EbrRateLimitSwitch_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 12, 1),
    _EbrRateLimitSwitch_Type()
)
ebrRateLimitSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrRateLimitSwitch.setStatus("mandatory")
_EbrRateLimit_Type = Integer32
_EbrRateLimit_Object = MibScalar
ebrRateLimit = _EbrRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 12, 2),
    _EbrRateLimit_Type()
)
ebrRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebrRateLimit.setStatus("mandatory")
_EbrRateLimitCounterTable_Object = MibTable
ebrRateLimitCounterTable = _EbrRateLimitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 12, 3)
)
if mibBuilder.loadTexts:
    ebrRateLimitCounterTable.setStatus("mandatory")
_EbrRateLimitCounterEntry_Object = MibTableRow
ebrRateLimitCounterEntry = _EbrRateLimitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 12, 3, 1)
)
ebrRateLimitCounterEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "ebrRateLimitPort"),
)
if mibBuilder.loadTexts:
    ebrRateLimitCounterEntry.setStatus("mandatory")
_EbrRateLimitPort_Type = Integer32
_EbrRateLimitPort_Object = MibTableColumn
ebrRateLimitPort = _EbrRateLimitPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 12, 3, 1, 1),
    _EbrRateLimitPort_Type()
)
ebrRateLimitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrRateLimitPort.setStatus("mandatory")
_EbrRateLimitAddressFrames_Type = Counter32
_EbrRateLimitAddressFrames_Object = MibTableColumn
ebrRateLimitAddressFrames = _EbrRateLimitAddressFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 12, 3, 1, 2),
    _EbrRateLimitAddressFrames_Type()
)
ebrRateLimitAddressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrRateLimitAddressFrames.setStatus("mandatory")
_EbrRateLimitProtocolFrames_Type = Counter32
_EbrRateLimitProtocolFrames_Object = MibTableColumn
ebrRateLimitProtocolFrames = _EbrRateLimitProtocolFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 4, 12, 3, 1, 3),
    _EbrRateLimitProtocolFrames_Type()
)
ebrRateLimitProtocolFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebrRateLimitProtocolFrames.setStatus("mandatory")
_Eauth_ObjectIdentity = ObjectIdentity
eauth = _Eauth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5)
)
_Eauth1_ObjectIdentity = ObjectIdentity
eauth1 = _Eauth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1)
)


class _EauthTrapCommunity_Type(OctetString):
    """Custom type eauthTrapCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EauthTrapCommunity_Type.__name__ = "OctetString"
_EauthTrapCommunity_Object = MibScalar
eauthTrapCommunity = _EauthTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 1),
    _EauthTrapCommunity_Type()
)
eauthTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthTrapCommunity.setStatus("mandatory")
_EauthTrapUserTable_Object = MibTable
eauthTrapUserTable = _EauthTrapUserTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    eauthTrapUserTable.setStatus("mandatory")
_EauthTrapUserEntry_Object = MibTableRow
eauthTrapUserEntry = _EauthTrapUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 2, 1)
)
eauthTrapUserEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "eauthTrapUserAddr"),
)
if mibBuilder.loadTexts:
    eauthTrapUserEntry.setStatus("mandatory")
_EauthTrapUserAddr_Type = IpAddress
_EauthTrapUserAddr_Object = MibTableColumn
eauthTrapUserAddr = _EauthTrapUserAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 2, 1, 1),
    _EauthTrapUserAddr_Type()
)
eauthTrapUserAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthTrapUserAddr.setStatus("mandatory")


class _EauthTrapUserStatus_Type(Integer32):
    """Custom type eauthTrapUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_EauthTrapUserStatus_Type.__name__ = "Integer32"
_EauthTrapUserStatus_Object = MibTableColumn
eauthTrapUserStatus = _EauthTrapUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 2, 1, 2),
    _EauthTrapUserStatus_Type()
)
eauthTrapUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthTrapUserStatus.setStatus("mandatory")


class _EauthReadOnlyCommunity_Type(OctetString):
    """Custom type eauthReadOnlyCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EauthReadOnlyCommunity_Type.__name__ = "OctetString"
_EauthReadOnlyCommunity_Object = MibScalar
eauthReadOnlyCommunity = _EauthReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 3),
    _EauthReadOnlyCommunity_Type()
)
eauthReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthReadOnlyCommunity.setStatus("mandatory")
_EauthReadOnlyUserTable_Object = MibTable
eauthReadOnlyUserTable = _EauthReadOnlyUserTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    eauthReadOnlyUserTable.setStatus("mandatory")
_EauthReadOnlyUserEntry_Object = MibTableRow
eauthReadOnlyUserEntry = _EauthReadOnlyUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 4, 1)
)
eauthReadOnlyUserEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "eauthReadOnlyUserAddr"),
)
if mibBuilder.loadTexts:
    eauthReadOnlyUserEntry.setStatus("mandatory")
_EauthReadOnlyUserAddr_Type = IpAddress
_EauthReadOnlyUserAddr_Object = MibTableColumn
eauthReadOnlyUserAddr = _EauthReadOnlyUserAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 4, 1, 1),
    _EauthReadOnlyUserAddr_Type()
)
eauthReadOnlyUserAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthReadOnlyUserAddr.setStatus("mandatory")


class _EauthReadOnlyUserMask_Type(OctetString):
    """Custom type eauthReadOnlyUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EauthReadOnlyUserMask_Type.__name__ = "OctetString"
_EauthReadOnlyUserMask_Object = MibTableColumn
eauthReadOnlyUserMask = _EauthReadOnlyUserMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 4, 1, 2),
    _EauthReadOnlyUserMask_Type()
)
eauthReadOnlyUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthReadOnlyUserMask.setStatus("mandatory")


class _EauthReadOnlyUserStatus_Type(Integer32):
    """Custom type eauthReadOnlyUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_EauthReadOnlyUserStatus_Type.__name__ = "Integer32"
_EauthReadOnlyUserStatus_Object = MibTableColumn
eauthReadOnlyUserStatus = _EauthReadOnlyUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 4, 1, 3),
    _EauthReadOnlyUserStatus_Type()
)
eauthReadOnlyUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthReadOnlyUserStatus.setStatus("mandatory")


class _EauthReadWriteCommunity_Type(OctetString):
    """Custom type eauthReadWriteCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EauthReadWriteCommunity_Type.__name__ = "OctetString"
_EauthReadWriteCommunity_Object = MibScalar
eauthReadWriteCommunity = _EauthReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 5),
    _EauthReadWriteCommunity_Type()
)
eauthReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthReadWriteCommunity.setStatus("mandatory")
_EauthReadWriteUserTable_Object = MibTable
eauthReadWriteUserTable = _EauthReadWriteUserTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    eauthReadWriteUserTable.setStatus("mandatory")
_EauthReadWriteUserEntry_Object = MibTableRow
eauthReadWriteUserEntry = _EauthReadWriteUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 6, 1)
)
eauthReadWriteUserEntry.setIndexNames(
    (0, "DEC-ELAN-MIB", "eauthReadWriteUserAddr"),
)
if mibBuilder.loadTexts:
    eauthReadWriteUserEntry.setStatus("mandatory")
_EauthReadWriteUserAddr_Type = IpAddress
_EauthReadWriteUserAddr_Object = MibTableColumn
eauthReadWriteUserAddr = _EauthReadWriteUserAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 6, 1, 1),
    _EauthReadWriteUserAddr_Type()
)
eauthReadWriteUserAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthReadWriteUserAddr.setStatus("mandatory")


class _EauthReadWriteUserMask_Type(OctetString):
    """Custom type eauthReadWriteUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EauthReadWriteUserMask_Type.__name__ = "OctetString"
_EauthReadWriteUserMask_Object = MibTableColumn
eauthReadWriteUserMask = _EauthReadWriteUserMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 6, 1, 2),
    _EauthReadWriteUserMask_Type()
)
eauthReadWriteUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthReadWriteUserMask.setStatus("mandatory")


class _EauthReadWriteUserStatus_Type(Integer32):
    """Custom type eauthReadWriteUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_EauthReadWriteUserStatus_Type.__name__ = "Integer32"
_EauthReadWriteUserStatus_Object = MibTableColumn
eauthReadWriteUserStatus = _EauthReadWriteUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 1, 5, 1, 6, 1, 3),
    _EauthReadWriteUserStatus_Type()
)
eauthReadWriteUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eauthReadWriteUserStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEC-ELAN-MIB",
    **{"dec": dec,
       "ema": ema,
       "sysobjid": sysobjid,
       "bridges": bridges,
       "gigaswitch": gigaswitch,
       "minimumGIGAswitchMIBVersionSupported": minimumGIGAswitchMIBVersionSupported,
       "maximumGIGAswitchMIBVersionSupported": maximumGIGAswitchMIBVersionSupported,
       "gigaversion1": gigaversion1,
       "gigaBox": gigaBox,
       "clockCard": clockCard,
       "mgmtMemoryAvail": mgmtMemoryAvail,
       "mgmtMemoryAction": mgmtMemoryAction,
       "mgmtMemoryTable": mgmtMemoryTable,
       "mgmtMemoryEntry": mgmtMemoryEntry,
       "mgmtMemoryIndex": mgmtMemoryIndex,
       "mgmtMemoryData": mgmtMemoryData,
       "psc": psc,
       "pscStatus": pscStatus,
       "pscFwRev": pscFwRev,
       "pscHwRev": pscHwRev,
       "keyswitchPosition": keyswitchPosition,
       "pscFwImageStatus": pscFwImageStatus,
       "pscBackplaneStatus": pscBackplaneStatus,
       "cabinetTemperature": cabinetTemperature,
       "temperatureWarning": temperatureWarning,
       "powerSupply": powerSupply,
       "rightPowerStatus": rightPowerStatus,
       "rightPowerInputSource": rightPowerInputSource,
       "rightPowerOutputPower": rightPowerOutputPower,
       "leftPowerStatus": leftPowerStatus,
       "leftPowerInputSource": leftPowerInputSource,
       "leftPowerOutputPower": leftPowerOutputPower,
       "slot": slot,
       "slotNumber": slotNumber,
       "scpSlot": scpSlot,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotIndex": slotIndex,
       "slotCardStatus": slotCardStatus,
       "slotCardType": slotCardType,
       "slotCardHwRev": slotCardHwRev,
       "slotCardFwRev": slotCardFwRev,
       "hostSlotTable": hostSlotTable,
       "hostSlotEntry": hostSlotEntry,
       "hostSlotIndex": hostSlotIndex,
       "hostIP": hostIP,
       "fan": fan,
       "fanSpeed": fanSpeed,
       "rightFanStatus": rightFanStatus,
       "leftFanStatus": leftFanStatus,
       "battery": battery,
       "batteryStatus": batteryStatus,
       "batteryUsing": batteryUsing,
       "batteryCharge": batteryCharge,
       "batteryTest": batteryTest,
       "fppn": fppn,
       "fppnTable": fppnTable,
       "fppnEntry": fppnEntry,
       "fppnSlotNumber": fppnSlotNumber,
       "fppnPortOfThatSlot": fppnPortOfThatSlot,
       "fppnIfIndex": fppnIfIndex,
       "fppnBridgePortNumber": fppnBridgePortNumber,
       "lineCard": lineCard,
       "mPortTable": mPortTable,
       "mPortEntry": mPortEntry,
       "mPortSMTIndex": mPortSMTIndex,
       "mPortMACIndex": mPortMACIndex,
       "mPortEnable": mPortEnable,
       "led": led,
       "ledTable": ledTable,
       "ledTableEntry": ledTableEntry,
       "ledTableIndex": ledTableIndex,
       "ledCount": ledCount,
       "ledSlotTable": ledSlotTable,
       "ledEntry": ledEntry,
       "ledSlotIndex": ledSlotIndex,
       "ledLedIndex": ledLedIndex,
       "ledDescr": ledDescr,
       "ledProgram": ledProgram,
       "gigaBridge": gigaBridge,
       "filterByReferencedExpression": filterByReferencedExpression,
       "ebrNportMatrixNameTable": ebrNportMatrixNameTable,
       "ebrNportMatrixNameEntry": ebrNportMatrixNameEntry,
       "ebrNportMatrixName": ebrNportMatrixName,
       "ebrNportMatrixValue": ebrNportMatrixValue,
       "ebrNportMatrixStatus": ebrNportMatrixStatus,
       "ebrNportMatrixFppnValue": ebrNportMatrixFppnValue,
       "ebrNportSapNameTable": ebrNportSapNameTable,
       "ebrNportSapNameEntry": ebrNportSapNameEntry,
       "ebrNportSapName": ebrNportSapName,
       "ebrNportSapNameSap": ebrNportSapNameSap,
       "ebrNportSapMatrixName": ebrNportSapMatrixName,
       "ebrNportSapNameDisp": ebrNportSapNameDisp,
       "ebrNportSapNameStatus": ebrNportSapNameStatus,
       "ebrNportSnapNameTable": ebrNportSnapNameTable,
       "ebrNportSnapNameEntry": ebrNportSnapNameEntry,
       "ebrNportSnapName": ebrNportSnapName,
       "ebrNportSnapNameSnap": ebrNportSnapNameSnap,
       "ebrNportSnapMatrixName": ebrNportSnapMatrixName,
       "ebrNportSnapNameDisp": ebrNportSnapNameDisp,
       "ebrNportSnapNameStatus": ebrNportSnapNameStatus,
       "ebrNportDANameTable": ebrNportDANameTable,
       "ebrNportDANameEntry": ebrNportDANameEntry,
       "ebrNportDAName": ebrNportDAName,
       "ebrNportDANameDA": ebrNportDANameDA,
       "ebrNportDAMatrixName": ebrNportDAMatrixName,
       "ebrNportDANameDisp": ebrNportDANameDisp,
       "ebrNportDANameStatus": ebrNportDANameStatus,
       "ebrNportSANameTable": ebrNportSANameTable,
       "ebrNportSANameEntry": ebrNportSANameEntry,
       "ebrNportSAName": ebrNportSAName,
       "ebrNportSANameSA": ebrNportSANameSA,
       "ebrNportSAMatrixName": ebrNportSAMatrixName,
       "ebrNportSANameDisp": ebrNportSANameDisp,
       "ebrNportSANameStatus": ebrNportSANameStatus,
       "ebrNportDefaultMatrixValue": ebrNportDefaultMatrixValue,
       "ebrNportManualFilter": ebrNportManualFilter,
       "ebrNportMatrixNameRowTable": ebrNportMatrixNameRowTable,
       "ebrNportMatrixNameRowEntry": ebrNportMatrixNameRowEntry,
       "ebrNportmatrixName": ebrNportmatrixName,
       "ebrNportMatrixReceivePort": ebrNportMatrixReceivePort,
       "ebrNportMatrixAllowedToGoTo": ebrNportMatrixAllowedToGoTo,
       "ebrNportMatrixNameRowStatus": ebrNportMatrixNameRowStatus,
       "ebrNportDefaultMatrixFppnValue": ebrNportDefaultMatrixFppnValue,
       "ebrNportFppnManualFilter": ebrNportFppnManualFilter,
       "ebrNportMatrixFppnRowTable": ebrNportMatrixFppnRowTable,
       "ebrNportMatrixFppnRowEntry": ebrNportMatrixFppnRowEntry,
       "ebrNportmatrixname": ebrNportmatrixname,
       "ebrNportMatrixFppnReceivePort": ebrNportMatrixFppnReceivePort,
       "ebrNportMatrixFppnAllowedToGoTo": ebrNportMatrixFppnAllowedToGoTo,
       "ebrNportMatrixFppnRowStatus": ebrNportMatrixFppnRowStatus,
       "ebrNportNamedDefaultMatrix": ebrNportNamedDefaultMatrix,
       "ebrNportDefaultMatrixRowTable": ebrNportDefaultMatrixRowTable,
       "ebrNportDefaultMatrixRowEntry": ebrNportDefaultMatrixRowEntry,
       "ebrNportDefaultMatrixReceivePort": ebrNportDefaultMatrixReceivePort,
       "ebrNportDefaultMatrixAllowedToGoTo": ebrNportDefaultMatrixAllowedToGoTo,
       "ebrNportFloodMatrixValue": ebrNportFloodMatrixValue,
       "ebrNportFloodMatrixFppnValue": ebrNportFloodMatrixFppnValue,
       "ebrNportNamedFloodMatrix": ebrNportNamedFloodMatrix,
       "ebrNportFloodMatrixRowTable": ebrNportFloodMatrixRowTable,
       "ebrNportFloodMatrixRowEntry": ebrNportFloodMatrixRowEntry,
       "ebrNportFloodMatrixReceivePort": ebrNportFloodMatrixReceivePort,
       "ebrNportFloodMatrixAllowedToGoTo": ebrNportFloodMatrixAllowedToGoTo,
       "filterByBitmapValue": filterByBitmapValue,
       "ebrNportSapProtoTable": ebrNportSapProtoTable,
       "ebrNportSapProtoEntry": ebrNportSapProtoEntry,
       "ebrNportSapValue": ebrNportSapValue,
       "ebrNportSapReceivePort": ebrNportSapReceivePort,
       "ebrNportSapAllowedToGoTo": ebrNportSapAllowedToGoTo,
       "ebrNportSapFilterCharacteristicsTable": ebrNportSapFilterCharacteristicsTable,
       "ebrNportSapFilterCharacteristicsEntry": ebrNportSapFilterCharacteristicsEntry,
       "ebrNportSapFilterCharacteristicsSapValue": ebrNportSapFilterCharacteristicsSapValue,
       "ebrNportSapDisp": ebrNportSapDisp,
       "ebrNportSapStatus": ebrNportSapStatus,
       "ebrNportSnapProtoTable": ebrNportSnapProtoTable,
       "ebrNportSnapProtoEntry": ebrNportSnapProtoEntry,
       "ebrNportSnapValue": ebrNportSnapValue,
       "ebrNportSnapReceivePort": ebrNportSnapReceivePort,
       "ebrNportSnapAllowedToGoTo": ebrNportSnapAllowedToGoTo,
       "ebrNportSnapFilterCharacteristicsTable": ebrNportSnapFilterCharacteristicsTable,
       "ebrNportSnapFilterCharacteristicsEntry": ebrNportSnapFilterCharacteristicsEntry,
       "ebrNportSnapFilterCharacteristicsSnapValue": ebrNportSnapFilterCharacteristicsSnapValue,
       "ebrNportSnapDisp": ebrNportSnapDisp,
       "ebrNportSnapStatus": ebrNportSnapStatus,
       "ebrNportStaticDATable": ebrNportStaticDATable,
       "ebrNportStaticDAEntry": ebrNportStaticDAEntry,
       "ebrNportDAAddress": ebrNportDAAddress,
       "ebrNportDAReceivePort": ebrNportDAReceivePort,
       "ebrNportDAAllowedToGoTo": ebrNportDAAllowedToGoTo,
       "ebrNportStaticDAFilterCharacteristicsTable": ebrNportStaticDAFilterCharacteristicsTable,
       "ebrNportStaticDAFilterCharacteristicsEntry": ebrNportStaticDAFilterCharacteristicsEntry,
       "ebrNportDestinationAddress": ebrNportDestinationAddress,
       "ebrNportDADisp": ebrNportDADisp,
       "ebrNportDAStatus": ebrNportDAStatus,
       "ebrNportStaticSATable": ebrNportStaticSATable,
       "ebrNportStaticSAEntry": ebrNportStaticSAEntry,
       "ebrNportSAAddress": ebrNportSAAddress,
       "ebrNportSAReceivePort": ebrNportSAReceivePort,
       "ebrNportSAAllowedToGoTo": ebrNportSAAllowedToGoTo,
       "ebrNportStaticSAFilterCharacteristicsTable": ebrNportStaticSAFilterCharacteristicsTable,
       "ebrNportStaticSAFilterCharacteristicsEntry": ebrNportStaticSAFilterCharacteristicsEntry,
       "ebrNportSourceAddress": ebrNportSourceAddress,
       "ebrNportSADisp": ebrNportSADisp,
       "ebrNportSAStatus": ebrNportSAStatus,
       "ebrNportSwTable": ebrNportSwTable,
       "ebrNportSwEntry": ebrNportSwEntry,
       "ebrNportSwReceivePort": ebrNportSwReceivePort,
       "ebrNportSwAllowedToGoTo": ebrNportSwAllowedToGoTo,
       "ebrNportSwManualFilter": ebrNportSwManualFilter,
       "ebrNportPortNumTable": ebrNportPortNumTable,
       "ebrNportPortNumEntry": ebrNportPortNumEntry,
       "ebrNportPortNumAddress": ebrNportPortNumAddress,
       "ebrNportPortNum": ebrNportPortNum,
       "ebrNportPortNumStatus": ebrNportPortNumStatus,
       "ebrNportFppnPortNum": ebrNportFppnPortNum,
       "serviceClassAssignments": serviceClassAssignments,
       "ebrNportSapSvcTable": ebrNportSapSvcTable,
       "ebrNportSapSvcEntry": ebrNportSapSvcEntry,
       "ebrNportSapSvcSapValue": ebrNportSapSvcSapValue,
       "ebrNportSapSvc": ebrNportSapSvc,
       "ebrNportSapSvcStatus": ebrNportSapSvcStatus,
       "ebrNportSapSinglePath": ebrNportSapSinglePath,
       "ebrNportSnapSvcTable": ebrNportSnapSvcTable,
       "ebrNportSnapSvcEntry": ebrNportSnapSvcEntry,
       "ebrNportSnapSvcSnapValue": ebrNportSnapSvcSnapValue,
       "ebrNportSnapSvc": ebrNportSnapSvc,
       "ebrNportSnapSvcStatus": ebrNportSnapSvcStatus,
       "ebrNportSnapSinglePath": ebrNportSnapSinglePath,
       "ebrNportDASvcTable": ebrNportDASvcTable,
       "ebrNportDASvcEntry": ebrNportDASvcEntry,
       "ebrNportSvcAddress": ebrNportSvcAddress,
       "ebrNportSvc": ebrNportSvc,
       "ebrNportSvcStatus": ebrNportSvcStatus,
       "flooding": flooding,
       "floodUnknownUnicastRate": floodUnknownUnicastRate,
       "floodMulticastRate": floodMulticastRate,
       "floodTable": floodTable,
       "floodEntry": floodEntry,
       "floodQuotaQualifier": floodQuotaQualifier,
       "floodQuotaClass": floodQuotaClass,
       "floodBytesSent": floodBytesSent,
       "floodPacketsSent": floodPacketsSent,
       "floodGeezers": floodGeezers,
       "floodLosers": floodLosers,
       "floodHogs": floodHogs,
       "floodSinglePathDiscards": floodSinglePathDiscards,
       "floodPacketsFiltered": floodPacketsFiltered,
       "floodPacketsPurged": floodPacketsPurged,
       "floodBytesPurged": floodBytesPurged,
       "floodLocalCopyPacketsDelivered": floodLocalCopyPacketsDelivered,
       "floodLocalCopyPacketsDiscarded": floodLocalCopyPacketsDiscarded,
       "cutThrough": cutThrough,
       "cutThroughTable": cutThroughTable,
       "cutThroughEntry": cutThroughEntry,
       "cutThroughBridgePort": cutThroughBridgePort,
       "cutThroughInbound": cutThroughInbound,
       "cutThroughOutbound": cutThroughOutbound,
       "cutThroughFppnTable": cutThroughFppnTable,
       "cutThroughFppnEntry": cutThroughFppnEntry,
       "cutThroughFppnPort": cutThroughFppnPort,
       "cutThroughFppnInbound": cutThroughFppnInbound,
       "cutThroughFppnOutbound": cutThroughFppnOutbound,
       "gigaStp": gigaStp,
       "gigaStpPortTable": gigaStpPortTable,
       "gigaStpPortEntry": gigaStpPortEntry,
       "gigaStpPortIfIndex": gigaStpPortIfIndex,
       "gigaStpPortSpanningTreeEnable": gigaStpPortSpanningTreeEnable,
       "gigaStpDemandLearningEnable": gigaStpDemandLearningEnable,
       "translationTableParams": translationTableParams,
       "ttSize": ttSize,
       "xacInDiscardCounters": xacInDiscardCounters,
       "xacInDiscardUnknownDAUCast": xacInDiscardUnknownDAUCast,
       "xacInDiscardMulticast": xacInDiscardMulticast,
       "xacInDiscardIPForwarding": xacInDiscardIPForwarding,
       "communityString": communityString,
       "communityStringDelimiter": communityStringDelimiter,
       "gigaUpgradeSoftware": gigaUpgradeSoftware,
       "doTransfer": doTransfer,
       "tftpDestination": tftpDestination,
       "mopDestination": mopDestination,
       "transferFileName": transferFileName,
       "transferAction": transferAction,
       "transferStatus": transferStatus,
       "transferSize": transferSize,
       "useTransfer": useTransfer,
       "copyToSlot": copyToSlot,
       "copyType": copyType,
       "copyAction": copyAction,
       "copyStatus": copyStatus,
       "deleteTransfer": deleteTransfer,
       "gigaIP": gigaIP,
       "arpTimingMechanism": arpTimingMechanism,
       "arpTimeoutInSeconds": arpTimeoutInSeconds,
       "arpPeriodBetweenRequests": arpPeriodBetweenRequests,
       "arpRequestRetries": arpRequestRetries,
       "snmpParameters": snmpParameters,
       "snmpDuplicateDiscardInterval": snmpDuplicateDiscardInterval,
       "arpControlParams": arpControlParams,
       "arpAgent": arpAgent,
       "arpStatisticalCounters": arpStatisticalCounters,
       "arpStatisticalTable": arpStatisticalTable,
       "arpStatisticalEntry": arpStatisticalEntry,
       "arpStatisticalIfIndex": arpStatisticalIfIndex,
       "arpUnicastReceived": arpUnicastReceived,
       "arpBroadcastReceived": arpBroadcastReceived,
       "arpRepliesTransmitted": arpRepliesTransmitted,
       "arpFramesFlooded": arpFramesFlooded,
       "arpFramesDiscarded": arpFramesDiscarded,
       "ipSwitching": ipSwitching,
       "ipSwitchEnable": ipSwitchEnable,
       "ipSwitchPortsTable": ipSwitchPortsTable,
       "ipSwitchPortsEntry": ipSwitchPortsEntry,
       "ipRangeStartAddr": ipRangeStartAddr,
       "ipRangeEndAddr": ipRangeEndAddr,
       "ipIPAddr": ipIPAddr,
       "ipStaticPorts": ipStaticPorts,
       "ipDynamicPorts": ipDynamicPorts,
       "ipPrimaryPorts": ipPrimaryPorts,
       "ipDynamicPrimaryPorts": ipDynamicPrimaryPorts,
       "ipDynamicEnabledPorts": ipDynamicEnabledPorts,
       "gigaSets": gigaSets,
       "portGroupMembershipTable": portGroupMembershipTable,
       "portGroupMembershipEntry": portGroupMembershipEntry,
       "portGroupBridgePort": portGroupBridgePort,
       "portGroupMembership": portGroupMembership,
       "portGroupMembershipWorkBuf": portGroupMembershipWorkBuf,
       "portGroupPortType": portGroupPortType,
       "portGroupPortTypeWorkBuf": portGroupPortTypeWorkBuf,
       "portGroupPortOperStatus": portGroupPortOperStatus,
       "portGroupFppnMembershipTable": portGroupFppnMembershipTable,
       "portGroupFppnMembershipEntry": portGroupFppnMembershipEntry,
       "portGroupFppnPort": portGroupFppnPort,
       "portGroupFppnMembership": portGroupFppnMembership,
       "portGroupFppnMembershipWorkBuf": portGroupFppnMembershipWorkBuf,
       "portGroupFppnPortType": portGroupFppnPortType,
       "portGroupFppnPortTypeWorkBuf": portGroupFppnPortTypeWorkBuf,
       "portGroupFppnPortOperStatus": portGroupFppnPortOperStatus,
       "portGroupStatusTable": portGroupStatusTable,
       "portGroupStatusEntry": portGroupStatusEntry,
       "portGroupStatusBridgePort": portGroupStatusBridgePort,
       "portGroupStatusPortNumber": portGroupStatusPortNumber,
       "portGroupStatusPortType": portGroupStatusPortType,
       "portGroupStatusOperStatus": portGroupStatusOperStatus,
       "learningDomainMembershipTable": learningDomainMembershipTable,
       "learningDomainMembershipEntry": learningDomainMembershipEntry,
       "learningDomainNumber": learningDomainNumber,
       "learningDomainMembership": learningDomainMembership,
       "learningDomainMembershipWorkBuf": learningDomainMembershipWorkBuf,
       "portTargetDomainListMembershipTable": portTargetDomainListMembershipTable,
       "portTargetDomainListMembershipEntry": portTargetDomainListMembershipEntry,
       "portTargetDomainListIndex": portTargetDomainListIndex,
       "portTargetDomainListMembership": portTargetDomainListMembership,
       "portTargetDomainListMembershipWorkBuf": portTargetDomainListMembershipWorkBuf,
       "lBDomainMembershipTable": lBDomainMembershipTable,
       "lBDomainMembershipEntry": lBDomainMembershipEntry,
       "lBDomainNumber": lBDomainNumber,
       "lBDomainMembership": lBDomainMembership,
       "lBDomainMembershipWorkBuf": lBDomainMembershipWorkBuf,
       "portGroupAction": portGroupAction,
       "portGroupActionStatus": portGroupActionStatus,
       "trafficGroupMembershipTable": trafficGroupMembershipTable,
       "trafficGroupMembershipEntry": trafficGroupMembershipEntry,
       "trafficGroupNumber": trafficGroupNumber,
       "trafficGroupMembership": trafficGroupMembership,
       "trafficGroupAttributeTable": trafficGroupAttributeTable,
       "trafficGroupAttributeEntry": trafficGroupAttributeEntry,
       "trafficGroupNum": trafficGroupNum,
       "trafficGroupHgNumber": trafficGroupHgNumber,
       "trafficGroupHgMember": trafficGroupHgMember,
       "trafficGroupCategory": trafficGroupCategory,
       "learningQuotaTable": learningQuotaTable,
       "learningQuotaEntry": learningQuotaEntry,
       "learningQuotaNumber": learningQuotaNumber,
       "learningQuota": learningQuota,
       "gigaSnmpDebug": gigaSnmpDebug,
       "commitFails": commitFails,
       "gigaXglEthernetGroup": gigaXglEthernetGroup,
       "xglTable": xglTable,
       "xglEntry": xglEntry,
       "xglCompliantMtu": xglCompliantMtu,
       "xglDisableIcmpErrors": xglDisableIcmpErrors,
       "xglTxErrorsToIcmpFifo": xglTxErrorsToIcmpFifo,
       "xglRxErrorsToIcmpFifo": xglRxErrorsToIcmpFifo,
       "xglEnableAppletalkArpII": xglEnableAppletalkArpII,
       "xglEnableRawIPX": xglEnableRawIPX,
       "agl": agl,
       "aglConfig": aglConfig,
       "aglInterfaceConfTable": aglInterfaceConfTable,
       "aglInterfaceConfEntry": aglInterfaceConfEntry,
       "aglInterfaceIndex": aglInterfaceIndex,
       "aglInterfacePhyType": aglInterfacePhyType,
       "aglInterfaceTrafficRateGranularity": aglInterfaceTrafficRateGranularity,
       "aglSonet": aglSonet,
       "aglInterfaceSonetTable": aglInterfaceSonetTable,
       "aglInterfaceSonetEntry": aglInterfaceSonetEntry,
       "aglInterfaceSonetIndex": aglInterfaceSonetIndex,
       "aglInterfaceSonetMode": aglInterfaceSonetMode,
       "aglInterfaceSonetTiming": aglInterfaceSonetTiming,
       "aglDS3E3": aglDS3E3,
       "aglInterfaceDS3E3Table": aglInterfaceDS3E3Table,
       "aglInterfaceDS3E3Entry": aglInterfaceDS3E3Entry,
       "aglInterfaceDS3E3Index": aglInterfaceDS3E3Index,
       "aglInterfaceDS3E3Mode": aglInterfaceDS3E3Mode,
       "aglInterfaceDS3E3Plcp": aglInterfaceDS3E3Plcp,
       "aglAtm": aglAtm,
       "aglVCConnectionTable": aglVCConnectionTable,
       "aglVCConnectionTableEntry": aglVCConnectionTableEntry,
       "aglVCConnectionPortA": aglVCConnectionPortA,
       "aglVCConnectionPortAVpi": aglVCConnectionPortAVpi,
       "aglVCConnectionPortAVci": aglVCConnectionPortAVci,
       "aglVCConnectionPortB": aglVCConnectionPortB,
       "aglVCConnectionPortBVpi": aglVCConnectionPortBVpi,
       "aglVCConnectionPortBVci": aglVCConnectionPortBVci,
       "aglVCConnectionTableEntryStatus": aglVCConnectionTableEntryStatus,
       "aglVCConnectionTrafficType": aglVCConnectionTrafficType,
       "aglVCConnectionAALType": aglVCConnectionAALType,
       "aglVCConnectionOperStatus": aglVCConnectionOperStatus,
       "aglVCConnectionAdminStatus": aglVCConnectionAdminStatus,
       "aglVCConnectionTrafficShaperPeakRate": aglVCConnectionTrafficShaperPeakRate,
       "aglVCConnectionTrafficShaperAvgRate": aglVCConnectionTrafficShaperAvgRate,
       "aglVCConnectionTrafficShaperMinGuaranteedRate": aglVCConnectionTrafficShaperMinGuaranteedRate,
       "aglVCConnectionTrafficShaperPriority": aglVCConnectionTrafficShaperPriority,
       "aglInterfaceATMTable": aglInterfaceATMTable,
       "aglInterfaceATMTableEntry": aglInterfaceATMTableEntry,
       "aglInterfaceATMIndex": aglInterfaceATMIndex,
       "aglInterfaceATMScrambeStatus": aglInterfaceATMScrambeStatus,
       "aglInterfaceATMOAMStatus": aglInterfaceATMOAMStatus,
       "aglatmMIB": aglatmMIB,
       "aglatmMIBObjects": aglatmMIBObjects,
       "aglatmInterfaceTrafficEnforcementTypes": aglatmInterfaceTrafficEnforcementTypes,
       "aglatmInterfaceNoTrafficEnforcement": aglatmInterfaceNoTrafficEnforcement,
       "aglatmInterfaceTrafficEnforcementType1": aglatmInterfaceTrafficEnforcementType1,
       "aglatmInterfaceTrafficEnforcementType2": aglatmInterfaceTrafficEnforcementType2,
       "aglatmInterfaceTrafficEnforcementType3": aglatmInterfaceTrafficEnforcementType3,
       "aglatmInterfaceTrafficEnforcementType4": aglatmInterfaceTrafficEnforcementType4,
       "aglatmInterfaceTrafficEnforcementType5": aglatmInterfaceTrafficEnforcementType5,
       "aglatmInterfaceTrafficEnforcementType6": aglatmInterfaceTrafficEnforcementType6,
       "aglatmInterfaceTrafficEnforcementType7": aglatmInterfaceTrafficEnforcementType7,
       "aglatmInterfaceConfTable": aglatmInterfaceConfTable,
       "aglatmInterfaceConfEntry": aglatmInterfaceConfEntry,
       "aglatmInterfaceIndex": aglatmInterfaceIndex,
       "aglatmInterfaceMaxVpcs": aglatmInterfaceMaxVpcs,
       "aglatmInterfaceMaxVccs": aglatmInterfaceMaxVccs,
       "aglatmInterfaceConfVpcs": aglatmInterfaceConfVpcs,
       "aglatmInterfaceConfVccs": aglatmInterfaceConfVccs,
       "aglatmInterfaceMaxActiveVpiBits": aglatmInterfaceMaxActiveVpiBits,
       "aglatmInterfaceMaxActiveVciBits": aglatmInterfaceMaxActiveVciBits,
       "aglatmInterfaceIlmiVpiVci": aglatmInterfaceIlmiVpiVci,
       "aglatmInterfaceSpecific": aglatmInterfaceSpecific,
       "aglatmInterfaceDs3PlcpTable": aglatmInterfaceDs3PlcpTable,
       "aglatmInterfaceDs3PlcpEntry": aglatmInterfaceDs3PlcpEntry,
       "aglatmInterfaceDs3PlcpIndex": aglatmInterfaceDs3PlcpIndex,
       "aglatmInterfaceDs3PlcpSEFSs": aglatmInterfaceDs3PlcpSEFSs,
       "aglatmInterfaceDs3PlcpAlarmState": aglatmInterfaceDs3PlcpAlarmState,
       "aglatmInterfaceDs3PlcpUASs": aglatmInterfaceDs3PlcpUASs,
       "aglatmInterfaceSonetTCTable": aglatmInterfaceSonetTCTable,
       "aglatmInterfaceSonetTCEntry": aglatmInterfaceSonetTCEntry,
       "aglatmInterfaceSonetTCIndex": aglatmInterfaceSonetTCIndex,
       "aglatmInterfaceSonetTCOCDEvents": aglatmInterfaceSonetTCOCDEvents,
       "aglatmInterfaceSonetTCAlarmState": aglatmInterfaceSonetTCAlarmState,
       "aglsonetMIB": aglsonetMIB,
       "aglsonetObjects": aglsonetObjects,
       "aglsonetMedium": aglsonetMedium,
       "aglsonetMediumTable": aglsonetMediumTable,
       "aglsonetMediumEntry": aglsonetMediumEntry,
       "aglsonetMediumIfIndex": aglsonetMediumIfIndex,
       "aglsonetMediumType": aglsonetMediumType,
       "aglsonetMediumTimeElapsed": aglsonetMediumTimeElapsed,
       "aglsonetMediumValidIntervals": aglsonetMediumValidIntervals,
       "aglsonetMediumLineCoding": aglsonetMediumLineCoding,
       "aglsonetMediumLineType": aglsonetMediumLineType,
       "aglsonetMediumCircuitIdentifier": aglsonetMediumCircuitIdentifier,
       "aglsonetSection": aglsonetSection,
       "aglsonetSectionCurrentTable": aglsonetSectionCurrentTable,
       "aglsonetSectionCurrentEntry": aglsonetSectionCurrentEntry,
       "aglsonetSectionCurrentIfIndex": aglsonetSectionCurrentIfIndex,
       "aglsonetSectionCurrentStatus": aglsonetSectionCurrentStatus,
       "aglsonetSectionCurrentESs": aglsonetSectionCurrentESs,
       "aglsonetSectionCurrentSESs": aglsonetSectionCurrentSESs,
       "aglsonetSectionCurrentSEFSs": aglsonetSectionCurrentSEFSs,
       "aglsonetSectionCurrentCVs": aglsonetSectionCurrentCVs,
       "aglsonetLine": aglsonetLine,
       "aglsonetLineCurrentTable": aglsonetLineCurrentTable,
       "aglsonetLineCurrentEntry": aglsonetLineCurrentEntry,
       "aglsonetLineCurrentIfIndex": aglsonetLineCurrentIfIndex,
       "aglsonetLineCurrentStatus": aglsonetLineCurrentStatus,
       "aglsonetLineCurrentESs": aglsonetLineCurrentESs,
       "aglsonetLineCurrentSESs": aglsonetLineCurrentSESs,
       "aglsonetLineCurrentCVs": aglsonetLineCurrentCVs,
       "aglsonetLineCurrentUASs": aglsonetLineCurrentUASs,
       "aglsonetObjectsPath": aglsonetObjectsPath,
       "aglsonetPath": aglsonetPath,
       "aglsonetPathCurrentTable": aglsonetPathCurrentTable,
       "aglsonetPathCurrentEntry": aglsonetPathCurrentEntry,
       "aglsonetPathCurrentIfIndex": aglsonetPathCurrentIfIndex,
       "aglsonetPathCurrentWidth": aglsonetPathCurrentWidth,
       "aglsonetPathCurrentStatus": aglsonetPathCurrentStatus,
       "aglsonetPathCurrentESs": aglsonetPathCurrentESs,
       "aglsonetPathCurrentSESs": aglsonetPathCurrentSESs,
       "aglsonetPathCurrentCVs": aglsonetPathCurrentCVs,
       "aglsonetPathCurrentUASs": aglsonetPathCurrentUASs,
       "decMIBextension": decMIBextension,
       "elanext": elanext,
       "efddi": efddi,
       "efddiSMT": efddiSMT,
       "efddiSMTTable": efddiSMTTable,
       "efddiSMTEntry": efddiSMTEntry,
       "eSMTIndex": eSMTIndex,
       "eSMTStationType": eSMTStationType,
       "eSMTTracesReceived": eSMTTracesReceived,
       "efddiMAC": efddiMAC,
       "efddiMACTable": efddiMACTable,
       "efddiMACEntry": efddiMACEntry,
       "eMACSMTIndex": eMACSMTIndex,
       "eMACIndex": eMACIndex,
       "eMACLinkIndex": eMACLinkIndex,
       "eMACLinkState": eMACLinkState,
       "eMACRingPurgerState": eMACRingPurgerState,
       "eMACRingPurgerEnable": eMACRingPurgerEnable,
       "eMACRingPurgeErrors": eMACRingPurgeErrors,
       "eMACFrameStripMode": eMACFrameStripMode,
       "eMACFCIStripErrors": eMACFCIStripErrors,
       "eMACRingErrorReason": eMACRingErrorReason,
       "eMACRingInitializationsInitiated": eMACRingInitializationsInitiated,
       "eMACRingInitializationsReceived": eMACRingInitializationsReceived,
       "eMACRingBeaconingInitiated": eMACRingBeaconingInitiated,
       "eMACDuplicateAddressTestFailures": eMACDuplicateAddressTestFailures,
       "eMACDuplicateTokensDetected": eMACDuplicateTokensDetected,
       "eMACUpstreamNbrDuplAddressFlag": eMACUpstreamNbrDuplAddressFlag,
       "eMACTracesInitiated": eMACTracesInitiated,
       "eMACRestrictedTokenTimeout": eMACRestrictedTokenTimeout,
       "eMACFrameStatusErrors": eMACFrameStatusErrors,
       "eMACFrameAlignmentErrors": eMACFrameAlignmentErrors,
       "eMACTransmitUnderruns": eMACTransmitUnderruns,
       "efddiPORT": efddiPORT,
       "efddiPORTTable": efddiPORTTable,
       "efddiPORTEntry": efddiPORTEntry,
       "ePORTSMTIndex": ePORTSMTIndex,
       "ePORTIndex": ePORTIndex,
       "ePORTPHYIndex": ePORTPHYIndex,
       "ePORTPMDType": ePORTPMDType,
       "ePORTPHYState": ePORTPHYState,
       "ePORTRejectReason": ePORTRejectReason,
       "ePORTConnectionsCompleted": ePORTConnectionsCompleted,
       "ePORTTNEExpRejects": ePORTTNEExpRejects,
       "ePORTElasticityBufferErrors": ePORTElasticityBufferErrors,
       "efddiFDX": efddiFDX,
       "efddiFDXTable": efddiFDXTable,
       "efddiFDXEntry": efddiFDXEntry,
       "eFDXSMTIndex": eFDXSMTIndex,
       "eFDXMACIndex": eFDXMACIndex,
       "eFDXEnable": eFDXEnable,
       "eFDXOp": eFDXOp,
       "eFDXState": eFDXState,
       "esystem": esystem,
       "esysChar": esysChar,
       "esysRomVersion": esysRomVersion,
       "esysInitSwitch": esysInitSwitch,
       "esysResetDefaultsSwitch": esysResetDefaultsSwitch,
       "esysGatewayAddress": esysGatewayAddress,
       "esysTrapAddressTable": esysTrapAddressTable,
       "esysTrapEntry": esysTrapEntry,
       "esysTrapAddress": esysTrapAddress,
       "esysUpdateSwitch": esysUpdateSwitch,
       "esysLastLoadHost": esysLastLoadHost,
       "esysStatus": esysStatus,
       "esysDeviceState": esysDeviceState,
       "esysDeviceBrokenReason": esysDeviceBrokenReason,
       "esysNvramFailed": esysNvramFailed,
       "esysCounters": esysCounters,
       "esysPowerups": esysPowerups,
       "esysMgmtResets": esysMgmtResets,
       "esysUnsolicitedResets": esysUnsolicitedResets,
       "esysConcConfig": esysConcConfig,
       "esysFRUConfigTable": esysFRUConfigTable,
       "esysFRUConfigEntry": esysFRUConfigEntry,
       "esysFRUIndex": esysFRUIndex,
       "esysFRUSlot": esysFRUSlot,
       "esysFRUDesc": esysFRUDesc,
       "esysFRUType": esysFRUType,
       "esysFRURev": esysFRURev,
       "esysFRUState": esysFRUState,
       "esysFddiPortTrapSwitch": esysFddiPortTrapSwitch,
       "einterfaces": einterfaces,
       "eifTable": eifTable,
       "eifEntry": eifEntry,
       "eifIndex": eifIndex,
       "eifBadFramesReceived": eifBadFramesReceived,
       "eifReceiveOverrun": eifReceiveOverrun,
       "eifOversizeFrames": eifOversizeFrames,
       "eifTransmitFramesError": eifTransmitFramesError,
       "eifMgmtSetsAllowedSwitch": eifMgmtSetsAllowedSwitch,
       "ebridge": ebridge,
       "ebrChar": ebrChar,
       "ebrLB100SpanningTreeVer": ebrLB100SpanningTreeVer,
       "ebr802SpanningTreeVer": ebr802SpanningTreeVer,
       "ebrMaxForwardingDBEntries": ebrMaxForwardingDBEntries,
       "ebrMaxNVForwardingDBEntries": ebrMaxNVForwardingDBEntries,
       "ebrMaxProtocolDBEntries": ebrMaxProtocolDBEntries,
       "ebrMaxNVProtocolDBEntries": ebrMaxNVProtocolDBEntries,
       "ebrForwardingDBPurgeThreshold": ebrForwardingDBPurgeThreshold,
       "ebrPortTestPassedThreshold": ebrPortTestPassedThreshold,
       "ebrPortTestInterval": ebrPortTestInterval,
       "ebrTopologyChangeTimer": ebrTopologyChangeTimer,
       "ebrManualFilterSwitch": ebrManualFilterSwitch,
       "ebrFragmentationSwitch": ebrFragmentationSwitch,
       "ebrRemoveMgmtAddress": ebrRemoveMgmtAddress,
       "ebrRemoveMgmtProto": ebrRemoveMgmtProto,
       "ebrStat": ebrStat,
       "ebrCurrForwardingDBEntries": ebrCurrForwardingDBEntries,
       "ebrCurrNVForwardingDBEntries": ebrCurrNVForwardingDBEntries,
       "ebrCurrProtocolDBEntries": ebrCurrProtocolDBEntries,
       "ebrCurrNVProtocolDBEntries": ebrCurrNVProtocolDBEntries,
       "ebrMgmtHeardPort": ebrMgmtHeardPort,
       "ebrLB100BeingPolled": ebrLB100BeingPolled,
       "ebrInactiveForwardingDBEntries": ebrInactiveForwardingDBEntries,
       "ebrTimeSinceForwardingDBPurged": ebrTimeSinceForwardingDBPurged,
       "ebrTimeSinceLastHello": ebrTimeSinceLastHello,
       "ebrCoun": ebrCoun,
       "ebrDeviceFramesLost": ebrDeviceFramesLost,
       "ebrSpanningTreeModeChanges": ebrSpanningTreeModeChanges,
       "ebrSpan": ebrSpan,
       "ebrBestRootAge": ebrBestRootAge,
       "ebrTopologyChangeFlag": ebrTopologyChangeFlag,
       "ebrTellParentFlag": ebrTellParentFlag,
       "ebrForwardingDBShortAgingTime": ebrForwardingDBShortAgingTime,
       "ebrBadHelloLimit": ebrBadHelloLimit,
       "ebrBadHelloResetTimer": ebrBadHelloResetTimer,
       "ebrNoFrameInterval": ebrNoFrameInterval,
       "ebrLB100PollTime": ebrLB100PollTime,
       "ebrLB100ResponseTimeout": ebrLB100ResponseTimeout,
       "ebrLB100SpanningTreeCompat": ebrLB100SpanningTreeCompat,
       "ebrInterfaces": ebrInterfaces,
       "ebrIfTable": ebrIfTable,
       "ebrIfEntry": ebrIfEntry,
       "ebrIfIndex": ebrIfIndex,
       "ebrIfLinkBrokenReason": ebrIfLinkBrokenReason,
       "ebrIfPortRestarts": ebrIfPortRestarts,
       "ebrIfUnknownDAReceived": ebrIfUnknownDAReceived,
       "ebrIfFramesAddrFiltered": ebrIfFramesAddrFiltered,
       "ebrIfMultiFramesFiltered": ebrIfMultiFramesFiltered,
       "ebrIfFramesProtocolFiltered": ebrIfFramesProtocolFiltered,
       "ebrIfDeviceFramesSent": ebrIfDeviceFramesSent,
       "ebrIfDeviceFramesReceived": ebrIfDeviceFramesReceived,
       "ebrIfDeviceBytesSent": ebrIfDeviceBytesSent,
       "ebrIfDeviceBytesReceived": ebrIfDeviceBytesReceived,
       "ebrIfDeviceFramesLost": ebrIfDeviceFramesLost,
       "ebrIfMultiBytesSent": ebrIfMultiBytesSent,
       "ebrIfMultiBytesReceived": ebrIfMultiBytesReceived,
       "ebrIfMultiDeviceFramesSent": ebrIfMultiDeviceFramesSent,
       "ebrIfMultiDeviceFramesReceived": ebrIfMultiDeviceFramesReceived,
       "ebrIfMultiDeviceBytesSent": ebrIfMultiDeviceBytesSent,
       "ebrIfMultiDeviceBytesReceived": ebrIfMultiDeviceBytesReceived,
       "ebrIfBadBytesReceived": ebrIfBadBytesReceived,
       "ebrIfBadHelloLimitExceeded": ebrIfBadHelloLimitExceeded,
       "ebrIfEtherTable": ebrIfEtherTable,
       "ebrIfEtherEntry": ebrIfEtherEntry,
       "ebrIfEthIndex": ebrIfEthIndex,
       "ebrIfEthPhysicalMediumType": ebrIfEthPhysicalMediumType,
       "ebrIfEthCollisionPresenceTestSwitch": ebrIfEthCollisionPresenceTestSwitch,
       "ebrIfEthCollisionTestFailed": ebrIfEthCollisionTestFailed,
       "ebrIfEthFramingError": ebrIfEthFramingError,
       "ebrIfEthLengthError": ebrIfEthLengthError,
       "ebrIfEthTransmitMultipleCollisions": ebrIfEthTransmitMultipleCollisions,
       "ebrIfEthCarrierLoss": ebrIfEthCarrierLoss,
       "ebrIfEthCollisionLimitExceeded": ebrIfEthCollisionLimitExceeded,
       "ebrIfFddiTable": ebrIfFddiTable,
       "ebrIfFddiEntry": ebrIfFddiEntry,
       "ebrIfFddiIndex": ebrIfFddiIndex,
       "ebrIfFddiUnprocessedErrorPackets": ebrIfFddiUnprocessedErrorPackets,
       "ebrIfFddiIpDatagramsFragmented": ebrIfFddiIpDatagramsFragmented,
       "ebrIfFddiIpDontFragment": ebrIfFddiIpDontFragment,
       "ebrIfFddiIpIllegalHeaderLength": ebrIfFddiIpIllegalHeaderLength,
       "ebrIfFddiIpIllegalSize": ebrIfFddiIpIllegalSize,
       "ebrIfSpanTable": ebrIfSpanTable,
       "ebrIfSpanEntry": ebrIfSpanEntry,
       "ebrIfSpIndex": ebrIfSpIndex,
       "ebrIfSpDesigRootAge": ebrIfSpDesigRootAge,
       "ebrIfSpForwardDelayTimer": ebrIfSpForwardDelayTimer,
       "ebrIfSpBadHelloCount": ebrIfSpBadHelloCount,
       "ebrIfSpPossibleLoopFlag": ebrIfSpPossibleLoopFlag,
       "ebrIfSpTopologyChangeAckFlag": ebrIfSpTopologyChangeAckFlag,
       "ebrTwoPortStatic": ebrTwoPortStatic,
       "ebrTwoPortStaticTable": ebrTwoPortStaticTable,
       "ebrTwoPortStaticEntry": ebrTwoPortStaticEntry,
       "ebrTwoPortAddress": ebrTwoPortAddress,
       "ebrTwoPortPortNum": ebrTwoPortPortNum,
       "ebrTwoPortStatus": ebrTwoPortStatus,
       "ebrMultiPortStatic": ebrMultiPortStatic,
       "ebrMultiPortStaticTable": ebrMultiPortStaticTable,
       "ebrMultiPortStaticEntry": ebrMultiPortStaticEntry,
       "ebrMultiPortAddress": ebrMultiPortAddress,
       "ebrMultiPortReceivePort": ebrMultiPortReceivePort,
       "ebrMultiPortAllowedToGoTo": ebrMultiPortAllowedToGoTo,
       "ebrMultiPortPortNum": ebrMultiPortPortNum,
       "ebrMultiPortStatus": ebrMultiPortStatus,
       "ebrTwoProtoFilt": ebrTwoProtoFilt,
       "ebrTwoProtoEnetFilterOther": ebrTwoProtoEnetFilterOther,
       "ebrTwoProtoSapFilterOther": ebrTwoProtoSapFilterOther,
       "ebrTwoProtoSnapFilterOther": ebrTwoProtoSnapFilterOther,
       "ebrTwoEnetProtoTable": ebrTwoEnetProtoTable,
       "ebrTwoEnetProtoEntry": ebrTwoEnetProtoEntry,
       "ebrTwoEnetProtoType": ebrTwoEnetProtoType,
       "ebrTwoEnetProtoStatus": ebrTwoEnetProtoStatus,
       "ebrTwoSapProtoTable": ebrTwoSapProtoTable,
       "ebrTwoSapProtoEntry": ebrTwoSapProtoEntry,
       "ebrTwoSapIndex": ebrTwoSapIndex,
       "ebrTwoSapValue": ebrTwoSapValue,
       "ebrTwoSapStatus": ebrTwoSapStatus,
       "ebrTwoSnapProtoTable": ebrTwoSnapProtoTable,
       "ebrTwoSnapProtoEntry": ebrTwoSnapProtoEntry,
       "ebrTwoSnapIndex": ebrTwoSnapIndex,
       "ebrTwoSnapValue": ebrTwoSnapValue,
       "ebrTwoSnapStatus": ebrTwoSnapStatus,
       "ebrMultiProtoFilt": ebrMultiProtoFilt,
       "ebrMultiEnetProtoTable": ebrMultiEnetProtoTable,
       "ebrMultiEnetProtoEntry": ebrMultiEnetProtoEntry,
       "ebrMultiEnetProtoType": ebrMultiEnetProtoType,
       "ebrMultiEnetReceivePort": ebrMultiEnetReceivePort,
       "ebrMultiEnetAllowedToGoTo": ebrMultiEnetAllowedToGoTo,
       "ebrMultiEnetStatus": ebrMultiEnetStatus,
       "ebrMultiSapProtoTable": ebrMultiSapProtoTable,
       "ebrMultiSapProtoEntry": ebrMultiSapProtoEntry,
       "ebrMultiSapValue": ebrMultiSapValue,
       "ebrMultiSapReceivePort": ebrMultiSapReceivePort,
       "ebrMultiSapAllowedToGoTo": ebrMultiSapAllowedToGoTo,
       "ebrMultiSapStatus": ebrMultiSapStatus,
       "ebrMultiSnapProtoTable": ebrMultiSnapProtoTable,
       "ebrMultiSnapProtoEntry": ebrMultiSnapProtoEntry,
       "ebrMultiSnapValue": ebrMultiSnapValue,
       "ebrMultiSnapReceivePort": ebrMultiSnapReceivePort,
       "ebrMultiSnapAllowedToGoTo": ebrMultiSnapAllowedToGoTo,
       "ebrMultiSnapStatus": ebrMultiSnapStatus,
       "ebrMultiFiltSw": ebrMultiFiltSw,
       "ebrMultiSwTable": ebrMultiSwTable,
       "ebrMultiSwEntry": ebrMultiSwEntry,
       "ebrMultiSwIndex": ebrMultiSwIndex,
       "ebrMultiSwManualFilter": ebrMultiSwManualFilter,
       "ebrMultiSwProtoEnetOther": ebrMultiSwProtoEnetOther,
       "ebrMultiSwProtoSapOther": ebrMultiSwProtoSapOther,
       "ebrMultiSwProtoSnapOther": ebrMultiSwProtoSnapOther,
       "ebrNTP": ebrNTP,
       "ebrNTPTable": ebrNTPTable,
       "ebrNTPEntry": ebrNTPEntry,
       "ebrNTPtype": ebrNTPtype,
       "ebrNTPStatus": ebrNTPStatus,
       "esysIPXSwitch": esysIPXSwitch,
       "ebrRateLimiting": ebrRateLimiting,
       "ebrRateLimitSwitch": ebrRateLimitSwitch,
       "ebrRateLimit": ebrRateLimit,
       "ebrRateLimitCounterTable": ebrRateLimitCounterTable,
       "ebrRateLimitCounterEntry": ebrRateLimitCounterEntry,
       "ebrRateLimitPort": ebrRateLimitPort,
       "ebrRateLimitAddressFrames": ebrRateLimitAddressFrames,
       "ebrRateLimitProtocolFrames": ebrRateLimitProtocolFrames,
       "eauth": eauth,
       "eauth1": eauth1,
       "eauthTrapCommunity": eauthTrapCommunity,
       "eauthTrapUserTable": eauthTrapUserTable,
       "eauthTrapUserEntry": eauthTrapUserEntry,
       "eauthTrapUserAddr": eauthTrapUserAddr,
       "eauthTrapUserStatus": eauthTrapUserStatus,
       "eauthReadOnlyCommunity": eauthReadOnlyCommunity,
       "eauthReadOnlyUserTable": eauthReadOnlyUserTable,
       "eauthReadOnlyUserEntry": eauthReadOnlyUserEntry,
       "eauthReadOnlyUserAddr": eauthReadOnlyUserAddr,
       "eauthReadOnlyUserMask": eauthReadOnlyUserMask,
       "eauthReadOnlyUserStatus": eauthReadOnlyUserStatus,
       "eauthReadWriteCommunity": eauthReadWriteCommunity,
       "eauthReadWriteUserTable": eauthReadWriteUserTable,
       "eauthReadWriteUserEntry": eauthReadWriteUserEntry,
       "eauthReadWriteUserAddr": eauthReadWriteUserAddr,
       "eauthReadWriteUserMask": eauthReadWriteUserMask,
       "eauthReadWriteUserStatus": eauthReadWriteUserStatus}
)
