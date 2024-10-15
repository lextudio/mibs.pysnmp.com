# SNMP MIB module (CHS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:51 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Chs_ObjectIdentity = ObjectIdentity
chs = _Chs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1)
)
_UchasSlot_ObjectIdentity = ObjectIdentity
uchasSlot = _UchasSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1)
)
_UchasSlotTable_Object = MibTable
uchasSlotTable = _UchasSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    uchasSlotTable.setStatus("mandatory")
_UchasSlotEntry_Object = MibTableRow
uchasSlotEntry = _UchasSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1)
)
uchasSlotEntry.setIndexNames(
    (0, "CHS-MIB", "uchasSlotIndex"),
)
if mibBuilder.loadTexts:
    uchasSlotEntry.setStatus("mandatory")


class _UchasSlotIndex_Type(Integer32):
    """Custom type uchasSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 37),
    )


_UchasSlotIndex_Type.__name__ = "Integer32"
_UchasSlotIndex_Object = MibTableColumn
uchasSlotIndex = _UchasSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 1),
    _UchasSlotIndex_Type()
)
uchasSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotIndex.setStatus("mandatory")
_UchasSlotModuleType_Type = ObjectIdentifier
_UchasSlotModuleType_Object = MibTableColumn
uchasSlotModuleType = _UchasSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 2),
    _UchasSlotModuleType_Type()
)
uchasSlotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotModuleType.setStatus("mandatory")
_UchasSlotLastChange_Type = TimeTicks
_UchasSlotLastChange_Object = MibTableColumn
uchasSlotLastChange = _UchasSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 3),
    _UchasSlotLastChange_Type()
)
uchasSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotLastChange.setStatus("mandatory")


class _UchasSlotModuleDescr_Type(DisplayString):
    """Custom type uchasSlotModuleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_UchasSlotModuleDescr_Type.__name__ = "DisplayString"
_UchasSlotModuleDescr_Object = MibTableColumn
uchasSlotModuleDescr = _UchasSlotModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 4),
    _UchasSlotModuleDescr_Type()
)
uchasSlotModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotModuleDescr.setStatus("mandatory")


class _UchasSlotModuleVersion_Type(DisplayString):
    """Custom type uchasSlotModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_UchasSlotModuleVersion_Type.__name__ = "DisplayString"
_UchasSlotModuleVersion_Object = MibTableColumn
uchasSlotModuleVersion = _UchasSlotModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 5),
    _UchasSlotModuleVersion_Type()
)
uchasSlotModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotModuleVersion.setStatus("mandatory")


class _UchasSlotModuleSerialNumber_Type(DisplayString):
    """Custom type uchasSlotModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UchasSlotModuleSerialNumber_Type.__name__ = "DisplayString"
_UchasSlotModuleSerialNumber_Object = MibTableColumn
uchasSlotModuleSerialNumber = _UchasSlotModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 6),
    _UchasSlotModuleSerialNumber_Type()
)
uchasSlotModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotModuleSerialNumber.setStatus("mandatory")


class _UchasSlotModuleProductCode_Type(DisplayString):
    """Custom type uchasSlotModuleProductCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UchasSlotModuleProductCode_Type.__name__ = "DisplayString"
_UchasSlotModuleProductCode_Object = MibTableColumn
uchasSlotModuleProductCode = _UchasSlotModuleProductCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 7),
    _UchasSlotModuleProductCode_Type()
)
uchasSlotModuleProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotModuleProductCode.setStatus("mandatory")
_UchasSlotStatFeEna_Type = Integer32
_UchasSlotStatFeEna_Object = MibTableColumn
uchasSlotStatFeEna = _UchasSlotStatFeEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 8),
    _UchasSlotStatFeEna_Type()
)
uchasSlotStatFeEna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotStatFeEna.setStatus("optional")


class _UchasSlotFeKey_Type(DisplayString):
    """Custom type uchasSlotFeKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_UchasSlotFeKey_Type.__name__ = "DisplayString"
_UchasSlotFeKey_Object = MibTableColumn
uchasSlotFeKey = _UchasSlotFeKey_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 9),
    _UchasSlotFeKey_Type()
)
uchasSlotFeKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasSlotFeKey.setStatus("optional")


class _UchasSlotNacConfig_Type(OctetString):
    """Custom type uchasSlotNacConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_UchasSlotNacConfig_Type.__name__ = "OctetString"
_UchasSlotNacConfig_Object = MibTableColumn
uchasSlotNacConfig = _UchasSlotNacConfig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 10),
    _UchasSlotNacConfig_Type()
)
uchasSlotNacConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotNacConfig.setStatus("optional")
_UchasSlotSwitchSettings_Type = Integer32
_UchasSlotSwitchSettings_Object = MibTableColumn
uchasSlotSwitchSettings = _UchasSlotSwitchSettings_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 11),
    _UchasSlotSwitchSettings_Type()
)
uchasSlotSwitchSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotSwitchSettings.setStatus("mandatory")
_UchasSlotRamInstalled_Type = Integer32
_UchasSlotRamInstalled_Object = MibTableColumn
uchasSlotRamInstalled = _UchasSlotRamInstalled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 12),
    _UchasSlotRamInstalled_Type()
)
uchasSlotRamInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotRamInstalled.setStatus("mandatory")
_UchasSlotFlashInstalled_Type = Integer32
_UchasSlotFlashInstalled_Object = MibTableColumn
uchasSlotFlashInstalled = _UchasSlotFlashInstalled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 1, 1, 1, 13),
    _UchasSlotFlashInstalled_Type()
)
uchasSlotFlashInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasSlotFlashInstalled.setStatus("mandatory")
_UchasEntity_ObjectIdentity = ObjectIdentity
uchasEntity = _UchasEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2)
)
_UchasEntityTable_Object = MibTable
uchasEntityTable = _UchasEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    uchasEntityTable.setStatus("mandatory")
_UchasEntityEntry_Object = MibTableRow
uchasEntityEntry = _UchasEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2, 1, 1)
)
uchasEntityEntry.setIndexNames(
    (0, "CHS-MIB", "uchasEntityIndex"),
)
if mibBuilder.loadTexts:
    uchasEntityEntry.setStatus("mandatory")


class _UchasEntityIndex_Type(Integer32):
    """Custom type uchasEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UchasEntityIndex_Type.__name__ = "Integer32"
_UchasEntityIndex_Object = MibTableColumn
uchasEntityIndex = _UchasEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2, 1, 1, 1),
    _UchasEntityIndex_Type()
)
uchasEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEntityIndex.setStatus("mandatory")
_UchasEntityObjectID_Type = ObjectIdentifier
_UchasEntityObjectID_Object = MibTableColumn
uchasEntityObjectID = _UchasEntityObjectID_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2, 1, 1, 2),
    _UchasEntityObjectID_Type()
)
uchasEntityObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEntityObjectID.setStatus("mandatory")


class _UchasEntityDescr_Type(DisplayString):
    """Custom type uchasEntityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_UchasEntityDescr_Type.__name__ = "DisplayString"
_UchasEntityDescr_Object = MibTableColumn
uchasEntityDescr = _UchasEntityDescr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2, 1, 1, 3),
    _UchasEntityDescr_Type()
)
uchasEntityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEntityDescr.setStatus("mandatory")


class _UchasEntityVersion_Type(DisplayString):
    """Custom type uchasEntityVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_UchasEntityVersion_Type.__name__ = "DisplayString"
_UchasEntityVersion_Object = MibTableColumn
uchasEntityVersion = _UchasEntityVersion_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2, 1, 1, 4),
    _UchasEntityVersion_Type()
)
uchasEntityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEntityVersion.setStatus("mandatory")


class _UchasEntityOperStatus_Type(Integer32):
    """Custom type uchasEntityOperStatus based on Integer32"""
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
        *(("failed", 5),
          ("loading", 6),
          ("operational", 4),
          ("other", 1),
          ("outOfService", 2),
          ("testing", 3))
    )


_UchasEntityOperStatus_Type.__name__ = "Integer32"
_UchasEntityOperStatus_Object = MibTableColumn
uchasEntityOperStatus = _UchasEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2, 1, 1, 5),
    _UchasEntityOperStatus_Type()
)
uchasEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEntityOperStatus.setStatus("mandatory")
_UchasEntityTimeStamp_Type = TimeTicks
_UchasEntityTimeStamp_Object = MibTableColumn
uchasEntityTimeStamp = _UchasEntityTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 2, 1, 1, 6),
    _UchasEntityTimeStamp_Type()
)
uchasEntityTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEntityTimeStamp.setStatus("mandatory")
_UchasConfig_ObjectIdentity = ObjectIdentity
uchasConfig = _UchasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 3)
)
_UchasType_Type = ObjectIdentifier
_UchasType_Object = MibScalar
uchasType = _UchasType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 3, 1),
    _UchasType_Type()
)
uchasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasType.setStatus("mandatory")


class _UchasDescr_Type(DisplayString):
    """Custom type uchasDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_UchasDescr_Type.__name__ = "DisplayString"
_UchasDescr_Object = MibScalar
uchasDescr = _UchasDescr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 3, 2),
    _UchasDescr_Type()
)
uchasDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasDescr.setStatus("mandatory")


class _UchasDisplayName_Type(DisplayString):
    """Custom type uchasDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_UchasDisplayName_Type.__name__ = "DisplayString"
_UchasDisplayName_Object = MibScalar
uchasDisplayName = _UchasDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 3, 3),
    _UchasDisplayName_Type()
)
uchasDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasDisplayName.setStatus("mandatory")
_UchasPhysicalChanges_Type = Counter32
_UchasPhysicalChanges_Object = MibScalar
uchasPhysicalChanges = _UchasPhysicalChanges_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 3, 4),
    _UchasPhysicalChanges_Type()
)
uchasPhysicalChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPhysicalChanges.setStatus("mandatory")


class _UchasFrontPanelLedStates_Type(OctetString):
    """Custom type uchasFrontPanelLedStates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UchasFrontPanelLedStates_Type.__name__ = "OctetString"
_UchasFrontPanelLedStates_Object = MibScalar
uchasFrontPanelLedStates = _UchasFrontPanelLedStates_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 3, 5),
    _UchasFrontPanelLedStates_Type()
)
uchasFrontPanelLedStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasFrontPanelLedStates.setStatus("mandatory")


class _UchasFrontPanelLedColor_Type(OctetString):
    """Custom type uchasFrontPanelLedColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UchasFrontPanelLedColor_Type.__name__ = "OctetString"
_UchasFrontPanelLedColor_Object = MibScalar
uchasFrontPanelLedColor = _UchasFrontPanelLedColor_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 3, 6),
    _UchasFrontPanelLedColor_Type()
)
uchasFrontPanelLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasFrontPanelLedColor.setStatus("mandatory")


class _UchasNicStates_Type(OctetString):
    """Custom type uchasNicStates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UchasNicStates_Type.__name__ = "OctetString"
_UchasNicStates_Object = MibScalar
uchasNicStates = _UchasNicStates_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 3, 7),
    _UchasNicStates_Type()
)
uchasNicStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasNicStates.setStatus("optional")
_UchasPowerSupply_ObjectIdentity = ObjectIdentity
uchasPowerSupply = _UchasPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4)
)
_UchasPowerSupplyTable_Object = MibTable
uchasPowerSupplyTable = _UchasPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    uchasPowerSupplyTable.setStatus("optional")
_UchasPowerSupplyEntry_Object = MibTableRow
uchasPowerSupplyEntry = _UchasPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 1, 1)
)
uchasPowerSupplyEntry.setIndexNames(
    (0, "CHS-MIB", "uchasPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    uchasPowerSupplyEntry.setStatus("optional")
_UchasPowerSupplyIndex_Type = Integer32
_UchasPowerSupplyIndex_Object = MibTableColumn
uchasPowerSupplyIndex = _UchasPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 1, 1, 1),
    _UchasPowerSupplyIndex_Type()
)
uchasPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyIndex.setStatus("optional")


class _UchasPowerSupplyDescr_Type(DisplayString):
    """Custom type uchasPowerSupplyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_UchasPowerSupplyDescr_Type.__name__ = "DisplayString"
_UchasPowerSupplyDescr_Object = MibTableColumn
uchasPowerSupplyDescr = _UchasPowerSupplyDescr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 1, 1, 2),
    _UchasPowerSupplyDescr_Type()
)
uchasPowerSupplyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyDescr.setStatus("optional")


class _UchasPowerSupplyOperStatus_Type(Integer32):
    """Custom type uchasPowerSupplyOperStatus based on Integer32"""
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
        *(("bad", 2),
          ("empty", 4),
          ("good", 3),
          ("unknown", 1))
    )


_UchasPowerSupplyOperStatus_Type.__name__ = "Integer32"
_UchasPowerSupplyOperStatus_Object = MibTableColumn
uchasPowerSupplyOperStatus = _UchasPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 1, 1, 3),
    _UchasPowerSupplyOperStatus_Type()
)
uchasPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyOperStatus.setStatus("optional")
_UchasPowerSupplyFailures_Type = Counter32
_UchasPowerSupplyFailures_Object = MibTableColumn
uchasPowerSupplyFailures = _UchasPowerSupplyFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 1, 1, 4),
    _UchasPowerSupplyFailures_Type()
)
uchasPowerSupplyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyFailures.setStatus("optional")
_UchasPowerSupplyOutTable_Object = MibTable
uchasPowerSupplyOutTable = _UchasPowerSupplyOutTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    uchasPowerSupplyOutTable.setStatus("optional")
_UchasPowerSupplyOutEntry_Object = MibTableRow
uchasPowerSupplyOutEntry = _UchasPowerSupplyOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 2, 1)
)
uchasPowerSupplyOutEntry.setIndexNames(
    (0, "CHS-MIB", "uchasPowerSupplyOutPSIndex"),
    (0, "CHS-MIB", "uchasPowerSupplyOutIndex"),
)
if mibBuilder.loadTexts:
    uchasPowerSupplyOutEntry.setStatus("optional")
_UchasPowerSupplyOutPSIndex_Type = Integer32
_UchasPowerSupplyOutPSIndex_Object = MibTableColumn
uchasPowerSupplyOutPSIndex = _UchasPowerSupplyOutPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 2, 1, 1),
    _UchasPowerSupplyOutPSIndex_Type()
)
uchasPowerSupplyOutPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyOutPSIndex.setStatus("optional")
_UchasPowerSupplyOutIndex_Type = Integer32
_UchasPowerSupplyOutIndex_Object = MibTableColumn
uchasPowerSupplyOutIndex = _UchasPowerSupplyOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 2, 1, 2),
    _UchasPowerSupplyOutIndex_Type()
)
uchasPowerSupplyOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyOutIndex.setStatus("optional")


class _UchasPowerSupplyOutStatus_Type(Integer32):
    """Custom type uchasPowerSupplyOutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 3),
          ("unknown", 1),
          ("warning", 2))
    )


_UchasPowerSupplyOutStatus_Type.__name__ = "Integer32"
_UchasPowerSupplyOutStatus_Object = MibTableColumn
uchasPowerSupplyOutStatus = _UchasPowerSupplyOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 2, 1, 3),
    _UchasPowerSupplyOutStatus_Type()
)
uchasPowerSupplyOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyOutStatus.setStatus("optional")
_UchasPowerSupplyOutNominalVolt_Type = Integer32
_UchasPowerSupplyOutNominalVolt_Object = MibTableColumn
uchasPowerSupplyOutNominalVolt = _UchasPowerSupplyOutNominalVolt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 2, 1, 4),
    _UchasPowerSupplyOutNominalVolt_Type()
)
uchasPowerSupplyOutNominalVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyOutNominalVolt.setStatus("optional")
_UchasPowerSupplyOutOfferedVolt_Type = Integer32
_UchasPowerSupplyOutOfferedVolt_Object = MibTableColumn
uchasPowerSupplyOutOfferedVolt = _UchasPowerSupplyOutOfferedVolt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 2, 1, 5),
    _UchasPowerSupplyOutOfferedVolt_Type()
)
uchasPowerSupplyOutOfferedVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyOutOfferedVolt.setStatus("optional")
_UchasPowerSupplyOutWarnings_Type = Counter32
_UchasPowerSupplyOutWarnings_Object = MibTableColumn
uchasPowerSupplyOutWarnings = _UchasPowerSupplyOutWarnings_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 4, 2, 1, 6),
    _UchasPowerSupplyOutWarnings_Type()
)
uchasPowerSupplyOutWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasPowerSupplyOutWarnings.setStatus("optional")
_UchasEnviron_ObjectIdentity = ObjectIdentity
uchasEnviron = _UchasEnviron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 5)
)
_UchasEnvironTable_Object = MibTable
uchasEnvironTable = _UchasEnvironTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    uchasEnvironTable.setStatus("optional")
_UchasEnvironEntry_Object = MibTableRow
uchasEnvironEntry = _UchasEnvironEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 5, 1, 1)
)
uchasEnvironEntry.setIndexNames(
    (0, "CHS-MIB", "uchasEnvironIndex"),
)
if mibBuilder.loadTexts:
    uchasEnvironEntry.setStatus("optional")
_UchasEnvironIndex_Type = Integer32
_UchasEnvironIndex_Object = MibTableColumn
uchasEnvironIndex = _UchasEnvironIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 5, 1, 1, 1),
    _UchasEnvironIndex_Type()
)
uchasEnvironIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEnvironIndex.setStatus("optional")
_UchasEnvironSensor_Type = ObjectIdentifier
_UchasEnvironSensor_Object = MibTableColumn
uchasEnvironSensor = _UchasEnvironSensor_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 5, 1, 1, 2),
    _UchasEnvironSensor_Type()
)
uchasEnvironSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEnvironSensor.setStatus("optional")


class _UchasEnvironStatus_Type(Integer32):
    """Custom type uchasEnvironStatus based on Integer32"""
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
        *(("bad", 2),
          ("good", 4),
          ("unknown", 1),
          ("warning", 3))
    )


_UchasEnvironStatus_Type.__name__ = "Integer32"
_UchasEnvironStatus_Object = MibTableColumn
uchasEnvironStatus = _UchasEnvironStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 5, 1, 1, 3),
    _UchasEnvironStatus_Type()
)
uchasEnvironStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEnvironStatus.setStatus("optional")
_UchasEnvironWarnings_Type = Counter32
_UchasEnvironWarnings_Object = MibTableColumn
uchasEnvironWarnings = _UchasEnvironWarnings_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 5, 1, 1, 4),
    _UchasEnvironWarnings_Type()
)
uchasEnvironWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEnvironWarnings.setStatus("optional")
_UchasEnvironFailures_Type = Counter32
_UchasEnvironFailures_Object = MibTableColumn
uchasEnvironFailures = _UchasEnvironFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 5, 1, 1, 5),
    _UchasEnvironFailures_Type()
)
uchasEnvironFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasEnvironFailures.setStatus("optional")
_UchasKnownTypes_ObjectIdentity = ObjectIdentity
uchasKnownTypes = _UchasKnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6)
)
_UchasKnownChassis_ObjectIdentity = ObjectIdentity
uchasKnownChassis = _UchasKnownChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 1)
)
_Uchas17SlotChassis_ObjectIdentity = ObjectIdentity
uchas17SlotChassis = _Uchas17SlotChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 1, 1)
)
_Uchas7SlotChassis_ObjectIdentity = ObjectIdentity
uchas7SlotChassis = _Uchas7SlotChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 1, 2)
)
_UchasKnownModules_ObjectIdentity = ObjectIdentity
uchasKnownModules = _UchasKnownModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2)
)
_UchasSlotEmpty_ObjectIdentity = ObjectIdentity
uchasSlotEmpty = _UchasSlotEmpty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1)
)
_UchasSlotUnknown_ObjectIdentity = ObjectIdentity
uchasSlotUnknown = _UchasSlotUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 2)
)
_UchasNetwMgtCard_ObjectIdentity = ObjectIdentity
uchasNetwMgtCard = _UchasNetwMgtCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 3)
)
_UchasDualT1NAC_ObjectIdentity = ObjectIdentity
uchasDualT1NAC = _UchasDualT1NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 4)
)
_UchasDualModemNAC_ObjectIdentity = ObjectIdentity
uchasDualModemNAC = _UchasDualModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 5)
)
_UchasQuadModemNAC_ObjectIdentity = ObjectIdentity
uchasQuadModemNAC = _UchasQuadModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 6)
)
_UchasTrGatewayNAC_ObjectIdentity = ObjectIdentity
uchasTrGatewayNAC = _UchasTrGatewayNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 7)
)
_UchasX25GatewayNAC_ObjectIdentity = ObjectIdentity
uchasX25GatewayNAC = _UchasX25GatewayNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 8)
)
_UchasDualV34ModemNAC_ObjectIdentity = ObjectIdentity
uchasDualV34ModemNAC = _UchasDualV34ModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 9)
)
_UchasQuadV32DigitalModemNAC_ObjectIdentity = ObjectIdentity
uchasQuadV32DigitalModemNAC = _UchasQuadV32DigitalModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 10)
)
_UchasQuadV32AnalogModemNAC_ObjectIdentity = ObjectIdentity
uchasQuadV32AnalogModemNAC = _UchasQuadV32AnalogModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 11)
)
_UchasQuadV32DigAnlModemNAC_ObjectIdentity = ObjectIdentity
uchasQuadV32DigAnlModemNAC = _UchasQuadV32DigAnlModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 12)
)
_UchasQuadV34DigModemNAC_ObjectIdentity = ObjectIdentity
uchasQuadV34DigModemNAC = _UchasQuadV34DigModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 13)
)
_UchasQuadV34AnlModemNAC_ObjectIdentity = ObjectIdentity
uchasQuadV34AnlModemNAC = _UchasQuadV34AnlModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 14)
)
_UchasQuadV34DigAnlModemNAC_ObjectIdentity = ObjectIdentity
uchasQuadV34DigAnlModemNAC = _UchasQuadV34DigAnlModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 15)
)
_UchasSingleT1NAC_ObjectIdentity = ObjectIdentity
uchasSingleT1NAC = _UchasSingleT1NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 16)
)
_UchasEthernetGatewayNAC_ObjectIdentity = ObjectIdentity
uchasEthernetGatewayNAC = _UchasEthernetGatewayNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 17)
)
_UchasAccessServer_ObjectIdentity = ObjectIdentity
uchasAccessServer = _UchasAccessServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 18)
)
_Uchas486TrGatewayNAC_ObjectIdentity = ObjectIdentity
uchas486TrGatewayNAC = _Uchas486TrGatewayNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 19)
)
_Uchas486EthernetGatewayNAC_ObjectIdentity = ObjectIdentity
uchas486EthernetGatewayNAC = _Uchas486EthernetGatewayNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 20)
)
_UchasDualRS232NAC_ObjectIdentity = ObjectIdentity
uchasDualRS232NAC = _UchasDualRS232NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 22)
)
_Uchas486X25GatewayNAC_ObjectIdentity = ObjectIdentity
uchas486X25GatewayNAC = _Uchas486X25GatewayNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 23)
)
_UchasApplicationServerNAC_ObjectIdentity = ObjectIdentity
uchasApplicationServerNAC = _UchasApplicationServerNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 25)
)
_UchasISDNGatewayNAC_ObjectIdentity = ObjectIdentity
uchasISDNGatewayNAC = _UchasISDNGatewayNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 26)
)
_UchasISDNpriT1NAC_ObjectIdentity = ObjectIdentity
uchasISDNpriT1NAC = _UchasISDNpriT1NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 27)
)
_UchasModemPoolManagmentNAC_ObjectIdentity = ObjectIdentity
uchasModemPoolManagmentNAC = _UchasModemPoolManagmentNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 29)
)
_UchasModemPoolNetserverNAC_ObjectIdentity = ObjectIdentity
uchasModemPoolNetserverNAC = _UchasModemPoolNetserverNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 30)
)
_UchasModemPoolV34ModemNAC_ObjectIdentity = ObjectIdentity
uchasModemPoolV34ModemNAC = _UchasModemPoolV34ModemNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 31)
)
_UchasModemPoolISDNNAC_ObjectIdentity = ObjectIdentity
uchasModemPoolISDNNAC = _UchasModemPoolISDNNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 32)
)
_UchasNTServerNAC_ObjectIdentity = ObjectIdentity
uchasNTServerNAC = _UchasNTServerNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 33)
)
_UchasQuadV34AnalogG2NAC_ObjectIdentity = ObjectIdentity
uchasQuadV34AnalogG2NAC = _UchasQuadV34AnalogG2NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 34)
)
_UchasQuadV34DigitalG2NAC_ObjectIdentity = ObjectIdentity
uchasQuadV34DigitalG2NAC = _UchasQuadV34DigitalG2NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 35)
)
_UchasQuadV34DigAnlgG2NAC_ObjectIdentity = ObjectIdentity
uchasQuadV34DigAnlgG2NAC = _UchasQuadV34DigAnlgG2NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 36)
)
_UchasNETServerFrameRelayNAC_ObjectIdentity = ObjectIdentity
uchasNETServerFrameRelayNAC = _UchasNETServerFrameRelayNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 37)
)
_UchasNETServerTokenRingNAC_ObjectIdentity = ObjectIdentity
uchasNETServerTokenRingNAC = _UchasNETServerTokenRingNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 38)
)
_UchasX2524ChannelNAC_ObjectIdentity = ObjectIdentity
uchasX2524ChannelNAC = _UchasX2524ChannelNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 39)
)
_UchasDualT1NIC_ObjectIdentity = ObjectIdentity
uchasDualT1NIC = _UchasDualT1NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1001)
)
_UchasDualAlogMdmNIC_ObjectIdentity = ObjectIdentity
uchasDualAlogMdmNIC = _UchasDualAlogMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1002)
)
_UchasQuadDgtlMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadDgtlMdmNIC = _UchasQuadDgtlMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1003)
)
_UchasQuadAlogDgtlMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadAlogDgtlMdmNIC = _UchasQuadAlogDgtlMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1004)
)
_UchasTokenRingNIC_ObjectIdentity = ObjectIdentity
uchasTokenRingNIC = _UchasTokenRingNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1005)
)
_UchasSingleT1NIC_ObjectIdentity = ObjectIdentity
uchasSingleT1NIC = _UchasSingleT1NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1006)
)
_UchasEthernetNIC_ObjectIdentity = ObjectIdentity
uchasEthernetNIC = _UchasEthernetNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1007)
)
_UchasShortHaulDualT1NIC_ObjectIdentity = ObjectIdentity
uchasShortHaulDualT1NIC = _UchasShortHaulDualT1NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1008)
)
_UchasDualAlogMgdIntlMdmNIC_ObjectIdentity = ObjectIdentity
uchasDualAlogMgdIntlMdmNIC = _UchasDualAlogMgdIntlMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1009)
)
_UchasX25NIC_ObjectIdentity = ObjectIdentity
uchasX25NIC = _UchasX25NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1010)
)
_UchasQuadAlogNonMgdMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadAlogNonMgdMdmNIC = _UchasQuadAlogNonMgdMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1011)
)
_UchasQuadAlogMgdIntlMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadAlogMgdIntlMdmNIC = _UchasQuadAlogMgdIntlMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1012)
)
_UchasQuadAlogNonMgdIntlMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadAlogNonMgdIntlMdmNIC = _UchasQuadAlogNonMgdIntlMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1013)
)
_UchasQuadLsdLiMgdMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadLsdLiMgdMdmNIC = _UchasQuadLsdLiMgdMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1014)
)
_UchasQuadLsdLiNonMgdMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadLsdLiNonMgdMdmNIC = _UchasQuadLsdLiNonMgdMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1015)
)
_UchasQuadLsdLiMgdIntlMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadLsdLiMgdIntlMdmNIC = _UchasQuadLsdLiMgdIntlMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1016)
)
_UchasQuadLsdLiNonMgdIntlMdmNIC_ObjectIdentity = ObjectIdentity
uchasQuadLsdLiNonMgdIntlMdmNIC = _UchasQuadLsdLiNonMgdIntlMdmNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1017)
)
_UchasHSEthernetWithV35NIC_ObjectIdentity = ObjectIdentity
uchasHSEthernetWithV35NIC = _UchasHSEthernetWithV35NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1018)
)
_UchasHSEthernetWithoutV35NIC_ObjectIdentity = ObjectIdentity
uchasHSEthernetWithoutV35NIC = _UchasHSEthernetWithoutV35NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1019)
)
_UchasDualHighSpeedV35NIC_ObjectIdentity = ObjectIdentity
uchasDualHighSpeedV35NIC = _UchasDualHighSpeedV35NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1020)
)
_UchasQuadV35RS232LowSpeedNIC_ObjectIdentity = ObjectIdentity
uchasQuadV35RS232LowSpeedNIC = _UchasQuadV35RS232LowSpeedNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1021)
)
_UchasDualE1NIC_ObjectIdentity = ObjectIdentity
uchasDualE1NIC = _UchasDualE1NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1022)
)
_UchasShortHaulDualE1NIC_ObjectIdentity = ObjectIdentity
uchasShortHaulDualE1NIC = _UchasShortHaulDualE1NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 2, 1023)
)
_UchasKnownEntities_ObjectIdentity = ObjectIdentity
uchasKnownEntities = _UchasKnownEntities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3)
)
_UchasNetwMgtEntity_ObjectIdentity = ObjectIdentity
uchasNetwMgtEntity = _UchasNetwMgtEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 1)
)
_UchasDualT1Entity_ObjectIdentity = ObjectIdentity
uchasDualT1Entity = _UchasDualT1Entity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 2)
)
_UchasDS1Entity_ObjectIdentity = ObjectIdentity
uchasDS1Entity = _UchasDS1Entity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 3)
)
_UchasModemEntity_ObjectIdentity = ObjectIdentity
uchasModemEntity = _UchasModemEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 4)
)
_UchasDualStandardModemEntity_ObjectIdentity = ObjectIdentity
uchasDualStandardModemEntity = _UchasDualStandardModemEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 5)
)
_UchasHSTModemEntity_ObjectIdentity = ObjectIdentity
uchasHSTModemEntity = _UchasHSTModemEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 6)
)
_UchasV32ModemEntity_ObjectIdentity = ObjectIdentity
uchasV32ModemEntity = _UchasV32ModemEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 7)
)
_UchasTokenRingEntity_ObjectIdentity = ObjectIdentity
uchasTokenRingEntity = _UchasTokenRingEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 8)
)
_UchasX25GatewayEntity_ObjectIdentity = ObjectIdentity
uchasX25GatewayEntity = _UchasX25GatewayEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 9)
)
_UchasDualStandardV32TerboMdEnt_ObjectIdentity = ObjectIdentity
uchasDualStandardV32TerboMdEnt = _UchasDualStandardV32TerboMdEnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 10)
)
_UchasV32TerboModemEntity_ObjectIdentity = ObjectIdentity
uchasV32TerboModemEntity = _UchasV32TerboModemEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 11)
)
_UchasV32TerboFaxModemEntity_ObjectIdentity = ObjectIdentity
uchasV32TerboFaxModemEntity = _UchasV32TerboFaxModemEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 12)
)
_UchasDualStandardV34Modem_ObjectIdentity = ObjectIdentity
uchasDualStandardV34Modem = _UchasDualStandardV34Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 13)
)
_UchasV34ModemEntity_ObjectIdentity = ObjectIdentity
uchasV34ModemEntity = _UchasV34ModemEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 14)
)
_UchasV34FaxModemEntity_ObjectIdentity = ObjectIdentity
uchasV34FaxModemEntity = _UchasV34FaxModemEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 15)
)
_UchasSingleT1Entity_ObjectIdentity = ObjectIdentity
uchasSingleT1Entity = _UchasSingleT1Entity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 16)
)
_UchasEthernetGatewayEntity_ObjectIdentity = ObjectIdentity
uchasEthernetGatewayEntity = _UchasEthernetGatewayEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 17)
)
_UchasX25GatewaySubnetEntity_ObjectIdentity = ObjectIdentity
uchasX25GatewaySubnetEntity = _UchasX25GatewaySubnetEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 18)
)
_UchasTokenRingAccSrvrEntity_ObjectIdentity = ObjectIdentity
uchasTokenRingAccSrvrEntity = _UchasTokenRingAccSrvrEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 19)
)
_UchasEthernetAccSrvrEntity_ObjectIdentity = ObjectIdentity
uchasEthernetAccSrvrEntity = _UchasEthernetAccSrvrEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 20)
)
_UchasDualRS232Entity_ObjectIdentity = ObjectIdentity
uchasDualRS232Entity = _UchasDualRS232Entity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 22)
)
_UchasEnetFRIsdnNetservrEntity_ObjectIdentity = ObjectIdentity
uchasEnetFRIsdnNetservrEntity = _UchasEnetFRIsdnNetservrEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 23)
)
_UchasIsdnPriT1Entity_ObjectIdentity = ObjectIdentity
uchasIsdnPriT1Entity = _UchasIsdnPriT1Entity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 24)
)
_UchasTknRngIsdnNetserverEntity_ObjectIdentity = ObjectIdentity
uchasTknRngIsdnNetserverEntity = _UchasTknRngIsdnNetserverEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 25)
)
_UchasEnetNetserverEntity_ObjectIdentity = ObjectIdentity
uchasEnetNetserverEntity = _UchasEnetNetserverEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 26)
)
_UchasIsdnPriE1Entity_ObjectIdentity = ObjectIdentity
uchasIsdnPriE1Entity = _UchasIsdnPriE1Entity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 27)
)
_UchasAnalogMdmNicEntity_ObjectIdentity = ObjectIdentity
uchasAnalogMdmNicEntity = _UchasAnalogMdmNicEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 3, 1001)
)
_UchasWellKnownSensors_ObjectIdentity = ObjectIdentity
uchasWellKnownSensors = _UchasWellKnownSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 4)
)
_UchasSensorOther_ObjectIdentity = ObjectIdentity
uchasSensorOther = _UchasSensorOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 4, 1)
)
_UchasSensorTemperature_ObjectIdentity = ObjectIdentity
uchasSensorTemperature = _UchasSensorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 4, 2)
)
_UchasSensorFans_ObjectIdentity = ObjectIdentity
uchasSensorFans = _UchasSensorFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 6, 4, 3)
)
_UchasCmd_ObjectIdentity = ObjectIdentity
uchasCmd = _UchasCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7)
)
_UchasCmdTable_Object = MibTable
uchasCmdTable = _UchasCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    uchasCmdTable.setStatus("mandatory")
_UchasCmdEntry_Object = MibTableRow
uchasCmdEntry = _UchasCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1)
)
uchasCmdEntry.setIndexNames(
    (0, "CHS-MIB", "uchasCmdSlotIndex"),
)
if mibBuilder.loadTexts:
    uchasCmdEntry.setStatus("mandatory")
_UchasCmdSlotIndex_Type = Integer32
_UchasCmdSlotIndex_Object = MibTableColumn
uchasCmdSlotIndex = _UchasCmdSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1, 1),
    _UchasCmdSlotIndex_Type()
)
uchasCmdSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasCmdSlotIndex.setStatus("mandatory")


class _UchasCmdMgtStationId_Type(OctetString):
    """Custom type uchasCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UchasCmdMgtStationId_Type.__name__ = "OctetString"
_UchasCmdMgtStationId_Object = MibTableColumn
uchasCmdMgtStationId = _UchasCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1, 2),
    _UchasCmdMgtStationId_Type()
)
uchasCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasCmdMgtStationId.setStatus("mandatory")
_UchasCmdReqId_Type = Integer32
_UchasCmdReqId_Object = MibTableColumn
uchasCmdReqId = _UchasCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1, 3),
    _UchasCmdReqId_Type()
)
uchasCmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasCmdReqId.setStatus("mandatory")


class _UchasCmdFunction_Type(Integer32):
    """Custom type uchasCmdFunction based on Integer32"""
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
        *(("hardwareReset", 4),
          ("noCommand", 1),
          ("removeFromService", 2),
          ("restoreToService", 3),
          ("softwareDownload", 5))
    )


_UchasCmdFunction_Type.__name__ = "Integer32"
_UchasCmdFunction_Object = MibTableColumn
uchasCmdFunction = _UchasCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1, 4),
    _UchasCmdFunction_Type()
)
uchasCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasCmdFunction.setStatus("mandatory")


class _UchasCmdForce_Type(Integer32):
    """Custom type uchasCmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_UchasCmdForce_Type.__name__ = "Integer32"
_UchasCmdForce_Object = MibTableColumn
uchasCmdForce = _UchasCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1, 5),
    _UchasCmdForce_Type()
)
uchasCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasCmdForce.setStatus("mandatory")


class _UchasCmdParam_Type(OctetString):
    """Custom type uchasCmdParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_UchasCmdParam_Type.__name__ = "OctetString"
_UchasCmdParam_Object = MibTableColumn
uchasCmdParam = _UchasCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1, 6),
    _UchasCmdParam_Type()
)
uchasCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasCmdParam.setStatus("mandatory")


class _UchasCmdResult_Type(Integer32):
    """Custom type uchasCmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_UchasCmdResult_Type.__name__ = "Integer32"
_UchasCmdResult_Object = MibTableColumn
uchasCmdResult = _UchasCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1, 7),
    _UchasCmdResult_Type()
)
uchasCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasCmdResult.setStatus("mandatory")


class _UchasCmdCode_Type(Integer32):
    """Custom type uchasCmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              14,
              20,
              21,
              22,
              58,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88)
        )
    )
    namedValues = NamedValues(
        *(("badAddressInData", 67),
          ("badFlashRomID", 61),
          ("badFlashVoltage", 62),
          ("badProgramVoltage", 68),
          ("cardIdMismatch", 84),
          ("cardIdUnknown", 85),
          ("connected", 14),
          ("crcTestingSdlFile", 78),
          ("deviceDisabled", 22),
          ("downloadingNacFile", 82),
          ("downloadingSdlFile", 77),
          ("eraseExecutionError", 65),
          ("eraseSequenceError", 64),
          ("erasingFlash", 81),
          ("executeLoadedProgram", 80),
          ("flashEraseError", 63),
          ("flashEraseTimeout", 87),
          ("invalidCodeError", 71),
          ("invalidFileHeader", 88),
          ("invalidRomId", 75),
          ("noError", 1),
          ("noResponse", 12),
          ("nonManagedDevice", 21),
          ("pendingSoftwareDownload", 73),
          ("programCodeError", 70),
          ("programmingDataError", 69),
          ("queryWorkSpaceSize", 79),
          ("ramCrcBad", 74),
          ("receiveBufferOverflow", 66),
          ("resetingNac", 83),
          ("romCrcBad", 72),
          ("sdlTrigger", 76),
          ("slotEmpty", 8),
          ("tftpTimeout", 86),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20),
          ("userInterfaceActive", 58))
    )


_UchasCmdCode_Type.__name__ = "Integer32"
_UchasCmdCode_Object = MibTableColumn
uchasCmdCode = _UchasCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 7, 1, 1, 8),
    _UchasCmdCode_Type()
)
uchasCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasCmdCode.setStatus("mandatory")
_UchasTrapEnable_ObjectIdentity = ObjectIdentity
uchasTrapEnable = _UchasTrapEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8)
)


class _UchasModuleInsertedTrapEna_Type(Integer32):
    """Custom type uchasModuleInsertedTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_UchasModuleInsertedTrapEna_Type.__name__ = "Integer32"
_UchasModuleInsertedTrapEna_Object = MibScalar
uchasModuleInsertedTrapEna = _UchasModuleInsertedTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8, 1),
    _UchasModuleInsertedTrapEna_Type()
)
uchasModuleInsertedTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasModuleInsertedTrapEna.setStatus("optional")


class _UchasModuleRemovedTrapEna_Type(Integer32):
    """Custom type uchasModuleRemovedTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_UchasModuleRemovedTrapEna_Type.__name__ = "Integer32"
_UchasModuleRemovedTrapEna_Object = MibScalar
uchasModuleRemovedTrapEna = _UchasModuleRemovedTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8, 2),
    _UchasModuleRemovedTrapEna_Type()
)
uchasModuleRemovedTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasModuleRemovedTrapEna.setStatus("optional")


class _UchasPSUWarningTrapEna_Type(Integer32):
    """Custom type uchasPSUWarningTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_UchasPSUWarningTrapEna_Type.__name__ = "Integer32"
_UchasPSUWarningTrapEna_Object = MibScalar
uchasPSUWarningTrapEna = _UchasPSUWarningTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8, 3),
    _UchasPSUWarningTrapEna_Type()
)
uchasPSUWarningTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasPSUWarningTrapEna.setStatus("optional")


class _UchasPSUFailureTrapEna_Type(Integer32):
    """Custom type uchasPSUFailureTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_UchasPSUFailureTrapEna_Type.__name__ = "Integer32"
_UchasPSUFailureTrapEna_Object = MibScalar
uchasPSUFailureTrapEna = _UchasPSUFailureTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8, 4),
    _UchasPSUFailureTrapEna_Type()
)
uchasPSUFailureTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasPSUFailureTrapEna.setStatus("optional")


class _UchasTempWarningTrapEna_Type(Integer32):
    """Custom type uchasTempWarningTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_UchasTempWarningTrapEna_Type.__name__ = "Integer32"
_UchasTempWarningTrapEna_Object = MibScalar
uchasTempWarningTrapEna = _UchasTempWarningTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8, 5),
    _UchasTempWarningTrapEna_Type()
)
uchasTempWarningTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasTempWarningTrapEna.setStatus("optional")


class _UchasFanFailureTrapEna_Type(Integer32):
    """Custom type uchasFanFailureTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_UchasFanFailureTrapEna_Type.__name__ = "Integer32"
_UchasFanFailureTrapEna_Object = MibScalar
uchasFanFailureTrapEna = _UchasFanFailureTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8, 6),
    _UchasFanFailureTrapEna_Type()
)
uchasFanFailureTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasFanFailureTrapEna.setStatus("optional")


class _UchasEntityWatchdogTrapEna_Type(Integer32):
    """Custom type uchasEntityWatchdogTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_UchasEntityWatchdogTrapEna_Type.__name__ = "Integer32"
_UchasEntityWatchdogTrapEna_Object = MibScalar
uchasEntityWatchdogTrapEna = _UchasEntityWatchdogTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8, 7),
    _UchasEntityWatchdogTrapEna_Type()
)
uchasEntityWatchdogTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasEntityWatchdogTrapEna.setStatus("mandatory")


class _UchasEntityMgtBusFailTrapEna_Type(Integer32):
    """Custom type uchasEntityMgtBusFailTrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_UchasEntityMgtBusFailTrapEna_Type.__name__ = "Integer32"
_UchasEntityMgtBusFailTrapEna_Object = MibScalar
uchasEntityMgtBusFailTrapEna = _UchasEntityMgtBusFailTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 8, 8),
    _UchasEntityMgtBusFailTrapEna_Type()
)
uchasEntityMgtBusFailTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasEntityMgtBusFailTrapEna.setStatus("mandatory")
_UchasAutoResponse_ObjectIdentity = ObjectIdentity
uchasAutoResponse = _UchasAutoResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9)
)


class _UchasArPsuVoltOutOfRange_Type(OctetString):
    """Custom type uchasArPsuVoltOutOfRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArPsuVoltOutOfRange_Type.__name__ = "OctetString"
_UchasArPsuVoltOutOfRange_Object = MibScalar
uchasArPsuVoltOutOfRange = _UchasArPsuVoltOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 1),
    _UchasArPsuVoltOutOfRange_Type()
)
uchasArPsuVoltOutOfRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArPsuVoltOutOfRange.setStatus("optional")


class _UchasArPsuFailed_Type(OctetString):
    """Custom type uchasArPsuFailed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArPsuFailed_Type.__name__ = "OctetString"
_UchasArPsuFailed_Object = MibScalar
uchasArPsuFailed = _UchasArPsuFailed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 2),
    _UchasArPsuFailed_Type()
)
uchasArPsuFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArPsuFailed.setStatus("optional")


class _UchasArFanFailed_Type(OctetString):
    """Custom type uchasArFanFailed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArFanFailed_Type.__name__ = "OctetString"
_UchasArFanFailed_Object = MibScalar
uchasArFanFailed = _UchasArFanFailed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 3),
    _UchasArFanFailed_Type()
)
uchasArFanFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArFanFailed.setStatus("optional")


class _UchasArHubTempOutOfRange_Type(OctetString):
    """Custom type uchasArHubTempOutOfRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArHubTempOutOfRange_Type.__name__ = "OctetString"
_UchasArHubTempOutOfRange_Object = MibScalar
uchasArHubTempOutOfRange = _UchasArHubTempOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 4),
    _UchasArHubTempOutOfRange_Type()
)
uchasArHubTempOutOfRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArHubTempOutOfRange.setStatus("optional")


class _UchasArTimer1_Type(OctetString):
    """Custom type uchasArTimer1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArTimer1_Type.__name__ = "OctetString"
_UchasArTimer1_Object = MibScalar
uchasArTimer1 = _UchasArTimer1_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 5),
    _UchasArTimer1_Type()
)
uchasArTimer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimer1.setStatus("optional")


class _UchasArTimer2_Type(OctetString):
    """Custom type uchasArTimer2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArTimer2_Type.__name__ = "OctetString"
_UchasArTimer2_Object = MibScalar
uchasArTimer2 = _UchasArTimer2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 6),
    _UchasArTimer2_Type()
)
uchasArTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimer2.setStatus("optional")


class _UchasArTimer3_Type(OctetString):
    """Custom type uchasArTimer3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArTimer3_Type.__name__ = "OctetString"
_UchasArTimer3_Object = MibScalar
uchasArTimer3 = _UchasArTimer3_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 7),
    _UchasArTimer3_Type()
)
uchasArTimer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimer3.setStatus("optional")


class _UchasArTimer4_Type(OctetString):
    """Custom type uchasArTimer4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArTimer4_Type.__name__ = "OctetString"
_UchasArTimer4_Object = MibScalar
uchasArTimer4 = _UchasArTimer4_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 8),
    _UchasArTimer4_Type()
)
uchasArTimer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimer4.setStatus("optional")
_UchasArSlotTable_Object = MibTable
uchasArSlotTable = _UchasArSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 9)
)
if mibBuilder.loadTexts:
    uchasArSlotTable.setStatus("optional")
_UchasArSlotEntry_Object = MibTableRow
uchasArSlotEntry = _UchasArSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 9, 1)
)
uchasArSlotEntry.setIndexNames(
    (0, "CHS-MIB", "uchasArSlotIndex"),
)
if mibBuilder.loadTexts:
    uchasArSlotEntry.setStatus("optional")


class _UchasArSlotIndex_Type(Integer32):
    """Custom type uchasArSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 37),
    )


_UchasArSlotIndex_Type.__name__ = "Integer32"
_UchasArSlotIndex_Object = MibTableColumn
uchasArSlotIndex = _UchasArSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 9, 1, 1),
    _UchasArSlotIndex_Type()
)
uchasArSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasArSlotIndex.setStatus("optional")


class _UchasArModuleInserted_Type(OctetString):
    """Custom type uchasArModuleInserted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArModuleInserted_Type.__name__ = "OctetString"
_UchasArModuleInserted_Object = MibTableColumn
uchasArModuleInserted = _UchasArModuleInserted_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 9, 1, 2),
    _UchasArModuleInserted_Type()
)
uchasArModuleInserted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArModuleInserted.setStatus("optional")


class _UchasArModuleReinit_Type(OctetString):
    """Custom type uchasArModuleReinit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArModuleReinit_Type.__name__ = "OctetString"
_UchasArModuleReinit_Object = MibTableColumn
uchasArModuleReinit = _UchasArModuleReinit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 9, 1, 3),
    _UchasArModuleReinit_Type()
)
uchasArModuleReinit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArModuleReinit.setStatus("optional")


class _UchasArModuleRemoved_Type(OctetString):
    """Custom type uchasArModuleRemoved based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArModuleRemoved_Type.__name__ = "OctetString"
_UchasArModuleRemoved_Object = MibTableColumn
uchasArModuleRemoved = _UchasArModuleRemoved_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 9, 1, 4),
    _UchasArModuleRemoved_Type()
)
uchasArModuleRemoved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArModuleRemoved.setStatus("optional")


class _UchasArModuleNonoper_Type(OctetString):
    """Custom type uchasArModuleNonoper based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArModuleNonoper_Type.__name__ = "OctetString"
_UchasArModuleNonoper_Object = MibTableColumn
uchasArModuleNonoper = _UchasArModuleNonoper_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 9, 1, 5),
    _UchasArModuleNonoper_Type()
)
uchasArModuleNonoper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArModuleNonoper.setStatus("optional")


class _UchasArModuleWatchdog_Type(OctetString):
    """Custom type uchasArModuleWatchdog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UchasArModuleWatchdog_Type.__name__ = "OctetString"
_UchasArModuleWatchdog_Object = MibTableColumn
uchasArModuleWatchdog = _UchasArModuleWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 9, 9, 1, 6),
    _UchasArModuleWatchdog_Type()
)
uchasArModuleWatchdog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArModuleWatchdog.setStatus("optional")
_UchasArTimers_ObjectIdentity = ObjectIdentity
uchasArTimers = _UchasArTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10)
)
_UchasArTimerTable_Object = MibTable
uchasArTimerTable = _UchasArTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    uchasArTimerTable.setStatus("optional")
_UchasArTimerEntry_Object = MibTableRow
uchasArTimerEntry = _UchasArTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1)
)
uchasArTimerEntry.setIndexNames(
    (0, "CHS-MIB", "uchasArTimerIndex"),
)
if mibBuilder.loadTexts:
    uchasArTimerEntry.setStatus("optional")


class _UchasArTimerIndex_Type(Integer32):
    """Custom type uchasArTimerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UchasArTimerIndex_Type.__name__ = "Integer32"
_UchasArTimerIndex_Object = MibTableColumn
uchasArTimerIndex = _UchasArTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 1),
    _UchasArTimerIndex_Type()
)
uchasArTimerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasArTimerIndex.setStatus("optional")


class _UchasArTimerEna_Type(Integer32):
    """Custom type uchasArTimerEna based on Integer32"""
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


_UchasArTimerEna_Type.__name__ = "Integer32"
_UchasArTimerEna_Object = MibTableColumn
uchasArTimerEna = _UchasArTimerEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 2),
    _UchasArTimerEna_Type()
)
uchasArTimerEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimerEna.setStatus("optional")


class _UchasArTimerStartDate_Type(DisplayString):
    """Custom type uchasArTimerStartDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_UchasArTimerStartDate_Type.__name__ = "DisplayString"
_UchasArTimerStartDate_Object = MibTableColumn
uchasArTimerStartDate = _UchasArTimerStartDate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 3),
    _UchasArTimerStartDate_Type()
)
uchasArTimerStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimerStartDate.setStatus("optional")


class _UchasArTimerStartTime_Type(DisplayString):
    """Custom type uchasArTimerStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_UchasArTimerStartTime_Type.__name__ = "DisplayString"
_UchasArTimerStartTime_Object = MibTableColumn
uchasArTimerStartTime = _UchasArTimerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 4),
    _UchasArTimerStartTime_Type()
)
uchasArTimerStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimerStartTime.setStatus("optional")


class _UchasArTimerStopDate_Type(DisplayString):
    """Custom type uchasArTimerStopDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_UchasArTimerStopDate_Type.__name__ = "DisplayString"
_UchasArTimerStopDate_Object = MibTableColumn
uchasArTimerStopDate = _UchasArTimerStopDate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 5),
    _UchasArTimerStopDate_Type()
)
uchasArTimerStopDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimerStopDate.setStatus("optional")


class _UchasArTimerStopTime_Type(DisplayString):
    """Custom type uchasArTimerStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_UchasArTimerStopTime_Type.__name__ = "DisplayString"
_UchasArTimerStopTime_Object = MibTableColumn
uchasArTimerStopTime = _UchasArTimerStopTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 6),
    _UchasArTimerStopTime_Type()
)
uchasArTimerStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimerStopTime.setStatus("optional")


class _UchasArTimerInterval_Type(Integer32):
    """Custom type uchasArTimerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2678400),
    )


_UchasArTimerInterval_Type.__name__ = "Integer32"
_UchasArTimerInterval_Object = MibTableColumn
uchasArTimerInterval = _UchasArTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 7),
    _UchasArTimerInterval_Type()
)
uchasArTimerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uchasArTimerInterval.setStatus("optional")


class _UchasArTimerState_Type(Integer32):
    """Custom type uchasArTimerState based on Integer32"""
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
          ("init", 1),
          ("passive", 2))
    )


_UchasArTimerState_Type.__name__ = "Integer32"
_UchasArTimerState_Object = MibTableColumn
uchasArTimerState = _UchasArTimerState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 8),
    _UchasArTimerState_Type()
)
uchasArTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasArTimerState.setStatus("optional")
_UchasArTimerTriggers_Type = Counter32
_UchasArTimerTriggers_Object = MibTableColumn
uchasArTimerTriggers = _UchasArTimerTriggers_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 1, 10, 1, 1, 9),
    _UchasArTimerTriggers_Type()
)
uchasArTimerTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uchasArTimerTriggers.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHS-MIB",
    **{"usr": usr,
       "nas": nas,
       "chs": chs,
       "uchasSlot": uchasSlot,
       "uchasSlotTable": uchasSlotTable,
       "uchasSlotEntry": uchasSlotEntry,
       "uchasSlotIndex": uchasSlotIndex,
       "uchasSlotModuleType": uchasSlotModuleType,
       "uchasSlotLastChange": uchasSlotLastChange,
       "uchasSlotModuleDescr": uchasSlotModuleDescr,
       "uchasSlotModuleVersion": uchasSlotModuleVersion,
       "uchasSlotModuleSerialNumber": uchasSlotModuleSerialNumber,
       "uchasSlotModuleProductCode": uchasSlotModuleProductCode,
       "uchasSlotStatFeEna": uchasSlotStatFeEna,
       "uchasSlotFeKey": uchasSlotFeKey,
       "uchasSlotNacConfig": uchasSlotNacConfig,
       "uchasSlotSwitchSettings": uchasSlotSwitchSettings,
       "uchasSlotRamInstalled": uchasSlotRamInstalled,
       "uchasSlotFlashInstalled": uchasSlotFlashInstalled,
       "uchasEntity": uchasEntity,
       "uchasEntityTable": uchasEntityTable,
       "uchasEntityEntry": uchasEntityEntry,
       "uchasEntityIndex": uchasEntityIndex,
       "uchasEntityObjectID": uchasEntityObjectID,
       "uchasEntityDescr": uchasEntityDescr,
       "uchasEntityVersion": uchasEntityVersion,
       "uchasEntityOperStatus": uchasEntityOperStatus,
       "uchasEntityTimeStamp": uchasEntityTimeStamp,
       "uchasConfig": uchasConfig,
       "uchasType": uchasType,
       "uchasDescr": uchasDescr,
       "uchasDisplayName": uchasDisplayName,
       "uchasPhysicalChanges": uchasPhysicalChanges,
       "uchasFrontPanelLedStates": uchasFrontPanelLedStates,
       "uchasFrontPanelLedColor": uchasFrontPanelLedColor,
       "uchasNicStates": uchasNicStates,
       "uchasPowerSupply": uchasPowerSupply,
       "uchasPowerSupplyTable": uchasPowerSupplyTable,
       "uchasPowerSupplyEntry": uchasPowerSupplyEntry,
       "uchasPowerSupplyIndex": uchasPowerSupplyIndex,
       "uchasPowerSupplyDescr": uchasPowerSupplyDescr,
       "uchasPowerSupplyOperStatus": uchasPowerSupplyOperStatus,
       "uchasPowerSupplyFailures": uchasPowerSupplyFailures,
       "uchasPowerSupplyOutTable": uchasPowerSupplyOutTable,
       "uchasPowerSupplyOutEntry": uchasPowerSupplyOutEntry,
       "uchasPowerSupplyOutPSIndex": uchasPowerSupplyOutPSIndex,
       "uchasPowerSupplyOutIndex": uchasPowerSupplyOutIndex,
       "uchasPowerSupplyOutStatus": uchasPowerSupplyOutStatus,
       "uchasPowerSupplyOutNominalVolt": uchasPowerSupplyOutNominalVolt,
       "uchasPowerSupplyOutOfferedVolt": uchasPowerSupplyOutOfferedVolt,
       "uchasPowerSupplyOutWarnings": uchasPowerSupplyOutWarnings,
       "uchasEnviron": uchasEnviron,
       "uchasEnvironTable": uchasEnvironTable,
       "uchasEnvironEntry": uchasEnvironEntry,
       "uchasEnvironIndex": uchasEnvironIndex,
       "uchasEnvironSensor": uchasEnvironSensor,
       "uchasEnvironStatus": uchasEnvironStatus,
       "uchasEnvironWarnings": uchasEnvironWarnings,
       "uchasEnvironFailures": uchasEnvironFailures,
       "uchasKnownTypes": uchasKnownTypes,
       "uchasKnownChassis": uchasKnownChassis,
       "uchas17SlotChassis": uchas17SlotChassis,
       "uchas7SlotChassis": uchas7SlotChassis,
       "uchasKnownModules": uchasKnownModules,
       "uchasSlotEmpty": uchasSlotEmpty,
       "uchasSlotUnknown": uchasSlotUnknown,
       "uchasNetwMgtCard": uchasNetwMgtCard,
       "uchasDualT1NAC": uchasDualT1NAC,
       "uchasDualModemNAC": uchasDualModemNAC,
       "uchasQuadModemNAC": uchasQuadModemNAC,
       "uchasTrGatewayNAC": uchasTrGatewayNAC,
       "uchasX25GatewayNAC": uchasX25GatewayNAC,
       "uchasDualV34ModemNAC": uchasDualV34ModemNAC,
       "uchasQuadV32DigitalModemNAC": uchasQuadV32DigitalModemNAC,
       "uchasQuadV32AnalogModemNAC": uchasQuadV32AnalogModemNAC,
       "uchasQuadV32DigAnlModemNAC": uchasQuadV32DigAnlModemNAC,
       "uchasQuadV34DigModemNAC": uchasQuadV34DigModemNAC,
       "uchasQuadV34AnlModemNAC": uchasQuadV34AnlModemNAC,
       "uchasQuadV34DigAnlModemNAC": uchasQuadV34DigAnlModemNAC,
       "uchasSingleT1NAC": uchasSingleT1NAC,
       "uchasEthernetGatewayNAC": uchasEthernetGatewayNAC,
       "uchasAccessServer": uchasAccessServer,
       "uchas486TrGatewayNAC": uchas486TrGatewayNAC,
       "uchas486EthernetGatewayNAC": uchas486EthernetGatewayNAC,
       "uchasDualRS232NAC": uchasDualRS232NAC,
       "uchas486X25GatewayNAC": uchas486X25GatewayNAC,
       "uchasApplicationServerNAC": uchasApplicationServerNAC,
       "uchasISDNGatewayNAC": uchasISDNGatewayNAC,
       "uchasISDNpriT1NAC": uchasISDNpriT1NAC,
       "uchasModemPoolManagmentNAC": uchasModemPoolManagmentNAC,
       "uchasModemPoolNetserverNAC": uchasModemPoolNetserverNAC,
       "uchasModemPoolV34ModemNAC": uchasModemPoolV34ModemNAC,
       "uchasModemPoolISDNNAC": uchasModemPoolISDNNAC,
       "uchasNTServerNAC": uchasNTServerNAC,
       "uchasQuadV34AnalogG2NAC": uchasQuadV34AnalogG2NAC,
       "uchasQuadV34DigitalG2NAC": uchasQuadV34DigitalG2NAC,
       "uchasQuadV34DigAnlgG2NAC": uchasQuadV34DigAnlgG2NAC,
       "uchasNETServerFrameRelayNAC": uchasNETServerFrameRelayNAC,
       "uchasNETServerTokenRingNAC": uchasNETServerTokenRingNAC,
       "uchasX2524ChannelNAC": uchasX2524ChannelNAC,
       "uchasDualT1NIC": uchasDualT1NIC,
       "uchasDualAlogMdmNIC": uchasDualAlogMdmNIC,
       "uchasQuadDgtlMdmNIC": uchasQuadDgtlMdmNIC,
       "uchasQuadAlogDgtlMdmNIC": uchasQuadAlogDgtlMdmNIC,
       "uchasTokenRingNIC": uchasTokenRingNIC,
       "uchasSingleT1NIC": uchasSingleT1NIC,
       "uchasEthernetNIC": uchasEthernetNIC,
       "uchasShortHaulDualT1NIC": uchasShortHaulDualT1NIC,
       "uchasDualAlogMgdIntlMdmNIC": uchasDualAlogMgdIntlMdmNIC,
       "uchasX25NIC": uchasX25NIC,
       "uchasQuadAlogNonMgdMdmNIC": uchasQuadAlogNonMgdMdmNIC,
       "uchasQuadAlogMgdIntlMdmNIC": uchasQuadAlogMgdIntlMdmNIC,
       "uchasQuadAlogNonMgdIntlMdmNIC": uchasQuadAlogNonMgdIntlMdmNIC,
       "uchasQuadLsdLiMgdMdmNIC": uchasQuadLsdLiMgdMdmNIC,
       "uchasQuadLsdLiNonMgdMdmNIC": uchasQuadLsdLiNonMgdMdmNIC,
       "uchasQuadLsdLiMgdIntlMdmNIC": uchasQuadLsdLiMgdIntlMdmNIC,
       "uchasQuadLsdLiNonMgdIntlMdmNIC": uchasQuadLsdLiNonMgdIntlMdmNIC,
       "uchasHSEthernetWithV35NIC": uchasHSEthernetWithV35NIC,
       "uchasHSEthernetWithoutV35NIC": uchasHSEthernetWithoutV35NIC,
       "uchasDualHighSpeedV35NIC": uchasDualHighSpeedV35NIC,
       "uchasQuadV35RS232LowSpeedNIC": uchasQuadV35RS232LowSpeedNIC,
       "uchasDualE1NIC": uchasDualE1NIC,
       "uchasShortHaulDualE1NIC": uchasShortHaulDualE1NIC,
       "uchasKnownEntities": uchasKnownEntities,
       "uchasNetwMgtEntity": uchasNetwMgtEntity,
       "uchasDualT1Entity": uchasDualT1Entity,
       "uchasDS1Entity": uchasDS1Entity,
       "uchasModemEntity": uchasModemEntity,
       "uchasDualStandardModemEntity": uchasDualStandardModemEntity,
       "uchasHSTModemEntity": uchasHSTModemEntity,
       "uchasV32ModemEntity": uchasV32ModemEntity,
       "uchasTokenRingEntity": uchasTokenRingEntity,
       "uchasX25GatewayEntity": uchasX25GatewayEntity,
       "uchasDualStandardV32TerboMdEnt": uchasDualStandardV32TerboMdEnt,
       "uchasV32TerboModemEntity": uchasV32TerboModemEntity,
       "uchasV32TerboFaxModemEntity": uchasV32TerboFaxModemEntity,
       "uchasDualStandardV34Modem": uchasDualStandardV34Modem,
       "uchasV34ModemEntity": uchasV34ModemEntity,
       "uchasV34FaxModemEntity": uchasV34FaxModemEntity,
       "uchasSingleT1Entity": uchasSingleT1Entity,
       "uchasEthernetGatewayEntity": uchasEthernetGatewayEntity,
       "uchasX25GatewaySubnetEntity": uchasX25GatewaySubnetEntity,
       "uchasTokenRingAccSrvrEntity": uchasTokenRingAccSrvrEntity,
       "uchasEthernetAccSrvrEntity": uchasEthernetAccSrvrEntity,
       "uchasDualRS232Entity": uchasDualRS232Entity,
       "uchasEnetFRIsdnNetservrEntity": uchasEnetFRIsdnNetservrEntity,
       "uchasIsdnPriT1Entity": uchasIsdnPriT1Entity,
       "uchasTknRngIsdnNetserverEntity": uchasTknRngIsdnNetserverEntity,
       "uchasEnetNetserverEntity": uchasEnetNetserverEntity,
       "uchasIsdnPriE1Entity": uchasIsdnPriE1Entity,
       "uchasAnalogMdmNicEntity": uchasAnalogMdmNicEntity,
       "uchasWellKnownSensors": uchasWellKnownSensors,
       "uchasSensorOther": uchasSensorOther,
       "uchasSensorTemperature": uchasSensorTemperature,
       "uchasSensorFans": uchasSensorFans,
       "uchasCmd": uchasCmd,
       "uchasCmdTable": uchasCmdTable,
       "uchasCmdEntry": uchasCmdEntry,
       "uchasCmdSlotIndex": uchasCmdSlotIndex,
       "uchasCmdMgtStationId": uchasCmdMgtStationId,
       "uchasCmdReqId": uchasCmdReqId,
       "uchasCmdFunction": uchasCmdFunction,
       "uchasCmdForce": uchasCmdForce,
       "uchasCmdParam": uchasCmdParam,
       "uchasCmdResult": uchasCmdResult,
       "uchasCmdCode": uchasCmdCode,
       "uchasTrapEnable": uchasTrapEnable,
       "uchasModuleInsertedTrapEna": uchasModuleInsertedTrapEna,
       "uchasModuleRemovedTrapEna": uchasModuleRemovedTrapEna,
       "uchasPSUWarningTrapEna": uchasPSUWarningTrapEna,
       "uchasPSUFailureTrapEna": uchasPSUFailureTrapEna,
       "uchasTempWarningTrapEna": uchasTempWarningTrapEna,
       "uchasFanFailureTrapEna": uchasFanFailureTrapEna,
       "uchasEntityWatchdogTrapEna": uchasEntityWatchdogTrapEna,
       "uchasEntityMgtBusFailTrapEna": uchasEntityMgtBusFailTrapEna,
       "uchasAutoResponse": uchasAutoResponse,
       "uchasArPsuVoltOutOfRange": uchasArPsuVoltOutOfRange,
       "uchasArPsuFailed": uchasArPsuFailed,
       "uchasArFanFailed": uchasArFanFailed,
       "uchasArHubTempOutOfRange": uchasArHubTempOutOfRange,
       "uchasArTimer1": uchasArTimer1,
       "uchasArTimer2": uchasArTimer2,
       "uchasArTimer3": uchasArTimer3,
       "uchasArTimer4": uchasArTimer4,
       "uchasArSlotTable": uchasArSlotTable,
       "uchasArSlotEntry": uchasArSlotEntry,
       "uchasArSlotIndex": uchasArSlotIndex,
       "uchasArModuleInserted": uchasArModuleInserted,
       "uchasArModuleReinit": uchasArModuleReinit,
       "uchasArModuleRemoved": uchasArModuleRemoved,
       "uchasArModuleNonoper": uchasArModuleNonoper,
       "uchasArModuleWatchdog": uchasArModuleWatchdog,
       "uchasArTimers": uchasArTimers,
       "uchasArTimerTable": uchasArTimerTable,
       "uchasArTimerEntry": uchasArTimerEntry,
       "uchasArTimerIndex": uchasArTimerIndex,
       "uchasArTimerEna": uchasArTimerEna,
       "uchasArTimerStartDate": uchasArTimerStartDate,
       "uchasArTimerStartTime": uchasArTimerStartTime,
       "uchasArTimerStopDate": uchasArTimerStopDate,
       "uchasArTimerStopTime": uchasArTimerStopTime,
       "uchasArTimerInterval": uchasArTimerInterval,
       "uchasArTimerState": uchasArTimerState,
       "uchasArTimerTriggers": uchasArTimerTriggers}
)
