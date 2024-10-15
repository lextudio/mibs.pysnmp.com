# SNMP MIB module (DECHUB900-CHASSIS-MIB-V3-0) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECHUB900-CHASSIS-MIB-V3-0
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:38 2024
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
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecHub900_ObjectIdentity = ObjectIdentity
decHub900 = _DecHub900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11)
)
_MgmtAgent_ObjectIdentity = ObjectIdentity
mgmtAgent = _MgmtAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1)
)
_MgmtAgentVersion1_ObjectIdentity = ObjectIdentity
mgmtAgentVersion1 = _MgmtAgentVersion1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1)
)
_ChasSlot_ObjectIdentity = ObjectIdentity
chasSlot = _ChasSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1)
)


class _ChasNumSlots_Type(Integer32):
    """Custom type chasNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasNumSlots_Type.__name__ = "Integer32"
_ChasNumSlots_Object = MibScalar
chasNumSlots = _ChasNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 1),
    _ChasNumSlots_Type()
)
chasNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNumSlots.setStatus("mandatory")


class _ChasNumSlotsOccupied_Type(Integer32):
    """Custom type chasNumSlotsOccupied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasNumSlotsOccupied_Type.__name__ = "Integer32"
_ChasNumSlotsOccupied_Object = MibScalar
chasNumSlotsOccupied = _ChasNumSlotsOccupied_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 2),
    _ChasNumSlotsOccupied_Type()
)
chasNumSlotsOccupied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNumSlotsOccupied.setStatus("mandatory")


class _ChasMaxExtendedSlots_Type(Integer32):
    """Custom type chasMaxExtendedSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasMaxExtendedSlots_Type.__name__ = "Integer32"
_ChasMaxExtendedSlots_Object = MibScalar
chasMaxExtendedSlots = _ChasMaxExtendedSlots_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 3),
    _ChasMaxExtendedSlots_Type()
)
chasMaxExtendedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasMaxExtendedSlots.setStatus("mandatory")


class _ChasExtendedSlotsOccupied_Type(Integer32):
    """Custom type chasExtendedSlotsOccupied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasExtendedSlotsOccupied_Type.__name__ = "Integer32"
_ChasExtendedSlotsOccupied_Object = MibScalar
chasExtendedSlotsOccupied = _ChasExtendedSlotsOccupied_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 4),
    _ChasExtendedSlotsOccupied_Type()
)
chasExtendedSlotsOccupied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasExtendedSlotsOccupied.setStatus("mandatory")
_ChasPopulationChanges_Type = Counter32
_ChasPopulationChanges_Object = MibScalar
chasPopulationChanges = _ChasPopulationChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 5),
    _ChasPopulationChanges_Type()
)
chasPopulationChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPopulationChanges.setStatus("mandatory")
_ChasSlotTable_Object = MibTable
chasSlotTable = _ChasSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    chasSlotTable.setStatus("mandatory")
_ChasSlotEntry_Object = MibTableRow
chasSlotEntry = _ChasSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1)
)
chasSlotEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasSlotIndex"),
)
if mibBuilder.loadTexts:
    chasSlotEntry.setStatus("mandatory")


class _ChasSlotIndex_Type(Integer32):
    """Custom type chasSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 899999999),
    )


_ChasSlotIndex_Type.__name__ = "Integer32"
_ChasSlotIndex_Object = MibTableColumn
chasSlotIndex = _ChasSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 1),
    _ChasSlotIndex_Type()
)
chasSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotIndex.setStatus("mandatory")
_ChasSlotModuleType_Type = ObjectIdentifier
_ChasSlotModuleType_Object = MibTableColumn
chasSlotModuleType = _ChasSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 2),
    _ChasSlotModuleType_Type()
)
chasSlotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotModuleType.setStatus("mandatory")
_ChasSlotLastChange_Type = TimeTicks
_ChasSlotLastChange_Object = MibTableColumn
chasSlotLastChange = _ChasSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 3),
    _ChasSlotLastChange_Type()
)
chasSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotLastChange.setStatus("mandatory")


class _ChasSlotModuleDescr_Type(DisplayString):
    """Custom type chasSlotModuleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSlotModuleDescr_Type.__name__ = "DisplayString"
_ChasSlotModuleDescr_Object = MibTableColumn
chasSlotModuleDescr = _ChasSlotModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 4),
    _ChasSlotModuleDescr_Type()
)
chasSlotModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotModuleDescr.setStatus("mandatory")


class _ChasSlotModuleVersion_Type(DisplayString):
    """Custom type chasSlotModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasSlotModuleVersion_Type.__name__ = "DisplayString"
_ChasSlotModuleVersion_Object = MibTableColumn
chasSlotModuleVersion = _ChasSlotModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 5),
    _ChasSlotModuleVersion_Type()
)
chasSlotModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotModuleVersion.setStatus("mandatory")


class _ChasSlotModuleSerialNumber_Type(DisplayString):
    """Custom type chasSlotModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasSlotModuleSerialNumber_Type.__name__ = "DisplayString"
_ChasSlotModuleSerialNumber_Object = MibTableColumn
chasSlotModuleSerialNumber = _ChasSlotModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 6),
    _ChasSlotModuleSerialNumber_Type()
)
chasSlotModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotModuleSerialNumber.setStatus("mandatory")


class _ChasSlotModuleSize_Type(Integer32):
    """Custom type chasSlotModuleSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("max", 2),
          ("min", 1),
          ("system", 3))
    )


_ChasSlotModuleSize_Type.__name__ = "Integer32"
_ChasSlotModuleSize_Object = MibTableColumn
chasSlotModuleSize = _ChasSlotModuleSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 7),
    _ChasSlotModuleSize_Type()
)
chasSlotModuleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotModuleSize.setStatus("mandatory")


class _ChasSlotModuleOperStatus_Type(Integer32):
    """Custom type chasSlotModuleOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("fatal-error", 4),
          ("insufficient-power", 3),
          ("non-fatal-error", 5),
          ("up", 1))
    )


_ChasSlotModuleOperStatus_Type.__name__ = "Integer32"
_ChasSlotModuleOperStatus_Object = MibTableColumn
chasSlotModuleOperStatus = _ChasSlotModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 8),
    _ChasSlotModuleOperStatus_Type()
)
chasSlotModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotModuleOperStatus.setStatus("mandatory")


class _ChasSlotModuleAdminStatus_Type(Integer32):
    """Custom type chasSlotModuleAdminStatus based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 2),
          ("reset", 4),
          ("restore-to-defaults", 5),
          ("unknown", 1))
    )


_ChasSlotModuleAdminStatus_Type.__name__ = "Integer32"
_ChasSlotModuleAdminStatus_Object = MibTableColumn
chasSlotModuleAdminStatus = _ChasSlotModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 9),
    _ChasSlotModuleAdminStatus_Type()
)
chasSlotModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSlotModuleAdminStatus.setStatus("mandatory")


class _ChasSlotModuleNonFatalError_Type(Integer32):
    """Custom type chasSlotModuleNonFatalError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChasSlotModuleNonFatalError_Type.__name__ = "Integer32"
_ChasSlotModuleNonFatalError_Object = MibTableColumn
chasSlotModuleNonFatalError = _ChasSlotModuleNonFatalError_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 6, 1, 10),
    _ChasSlotModuleNonFatalError_Type()
)
chasSlotModuleNonFatalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSlotModuleNonFatalError.setStatus("mandatory")


class _ChasSlotResetAll_Type(Integer32):
    """Custom type chasSlotResetAll based on Integer32"""
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
        *(("resetAllModules", 2),
          ("resetAllModulesAndMgr", 3),
          ("resetAllModulesAndMgrToDefaults", 5),
          ("resetAllModulesToDefaults", 4),
          ("unknown", 1))
    )


_ChasSlotResetAll_Type.__name__ = "Integer32"
_ChasSlotResetAll_Object = MibScalar
chasSlotResetAll = _ChasSlotResetAll_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 1, 7),
    _ChasSlotResetAll_Type()
)
chasSlotResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSlotResetAll.setStatus("mandatory")
_ChasEntity_ObjectIdentity = ObjectIdentity
chasEntity = _ChasEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2)
)
_ChasEntityChanges_Type = Counter32
_ChasEntityChanges_Object = MibScalar
chasEntityChanges = _ChasEntityChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 1),
    _ChasEntityChanges_Type()
)
chasEntityChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityChanges.setStatus("mandatory")
_ChasEntityTable_Object = MibTable
chasEntityTable = _ChasEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    chasEntityTable.setStatus("mandatory")
_ChasEntityEntry_Object = MibTableRow
chasEntityEntry = _ChasEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1)
)
chasEntityEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasEntitySlotNumber"),
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasEntityIndex"),
)
if mibBuilder.loadTexts:
    chasEntityEntry.setStatus("mandatory")


class _ChasEntityIndex_Type(Integer32):
    """Custom type chasEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasEntityIndex_Type.__name__ = "Integer32"
_ChasEntityIndex_Object = MibTableColumn
chasEntityIndex = _ChasEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 1),
    _ChasEntityIndex_Type()
)
chasEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityIndex.setStatus("mandatory")


class _ChasEntityFunction_Type(Integer32):
    """Custom type chasEntityFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_ChasEntityFunction_Type.__name__ = "Integer32"
_ChasEntityFunction_Object = MibTableColumn
chasEntityFunction = _ChasEntityFunction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 2),
    _ChasEntityFunction_Type()
)
chasEntityFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityFunction.setStatus("deprecated")
_ChasEntityObjectID_Type = ObjectIdentifier
_ChasEntityObjectID_Object = MibTableColumn
chasEntityObjectID = _ChasEntityObjectID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 3),
    _ChasEntityObjectID_Type()
)
chasEntityObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityObjectID.setStatus("deprecated")


class _ChasEntityDescr_Type(DisplayString):
    """Custom type chasEntityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasEntityDescr_Type.__name__ = "DisplayString"
_ChasEntityDescr_Object = MibTableColumn
chasEntityDescr = _ChasEntityDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 4),
    _ChasEntityDescr_Type()
)
chasEntityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityDescr.setStatus("deprecated")


class _ChasEntityVersion_Type(DisplayString):
    """Custom type chasEntityVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasEntityVersion_Type.__name__ = "DisplayString"
_ChasEntityVersion_Object = MibTableColumn
chasEntityVersion = _ChasEntityVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 5),
    _ChasEntityVersion_Type()
)
chasEntityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityVersion.setStatus("deprecated")


class _ChasEntityAdminStatus_Type(Integer32):
    """Custom type chasEntityAdminStatus based on Integer32"""
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
        *(("disable", 3),
          ("enable", 2),
          ("programload", 5),
          ("reset", 4),
          ("test", 6),
          ("unknown", 1))
    )


_ChasEntityAdminStatus_Type.__name__ = "Integer32"
_ChasEntityAdminStatus_Object = MibTableColumn
chasEntityAdminStatus = _ChasEntityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 6),
    _ChasEntityAdminStatus_Type()
)
chasEntityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasEntityAdminStatus.setStatus("deprecated")


class _ChasEntityOperStatus_Type(Integer32):
    """Custom type chasEntityOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("fatalError", 8),
          ("invalid", 2),
          ("loading", 10),
          ("nonFatalError", 7),
          ("operational", 4),
          ("other", 1),
          ("resetInProgress", 5),
          ("testing", 3),
          ("warning", 6))
    )


_ChasEntityOperStatus_Type.__name__ = "Integer32"
_ChasEntityOperStatus_Object = MibTableColumn
chasEntityOperStatus = _ChasEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 7),
    _ChasEntityOperStatus_Type()
)
chasEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityOperStatus.setStatus("deprecated")
_ChasEntityTimeStamp_Type = TimeTicks
_ChasEntityTimeStamp_Object = MibTableColumn
chasEntityTimeStamp = _ChasEntityTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 8),
    _ChasEntityTimeStamp_Type()
)
chasEntityTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityTimeStamp.setStatus("deprecated")
_ChasEntityParty_Type = ObjectIdentifier
_ChasEntityParty_Object = MibTableColumn
chasEntityParty = _ChasEntityParty_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 9),
    _ChasEntityParty_Type()
)
chasEntityParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityParty.setStatus("deprecated")


class _ChasEntityCommunity_Type(OctetString):
    """Custom type chasEntityCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ChasEntityCommunity_Type.__name__ = "OctetString"
_ChasEntityCommunity_Object = MibTableColumn
chasEntityCommunity = _ChasEntityCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 10),
    _ChasEntityCommunity_Type()
)
chasEntityCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityCommunity.setStatus("mandatory")
_ChasEntityIpAddress_Type = IpAddress
_ChasEntityIpAddress_Object = MibTableColumn
chasEntityIpAddress = _ChasEntityIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 11),
    _ChasEntityIpAddress_Type()
)
chasEntityIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityIpAddress.setStatus("mandatory")


class _ChasEntityComAccessRights_Type(Integer32):
    """Custom type chasEntityComAccessRights based on Integer32"""
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
        *(("other", 4),
          ("readOnly", 1),
          ("readWrite", 2),
          ("traps", 3))
    )


_ChasEntityComAccessRights_Type.__name__ = "Integer32"
_ChasEntityComAccessRights_Object = MibTableColumn
chasEntityComAccessRights = _ChasEntityComAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 12),
    _ChasEntityComAccessRights_Type()
)
chasEntityComAccessRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityComAccessRights.setStatus("mandatory")


class _ChasEntityAccessMethod_Type(OctetString):
    """Custom type chasEntityAccessMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasEntityAccessMethod_Type.__name__ = "OctetString"
_ChasEntityAccessMethod_Object = MibTableColumn
chasEntityAccessMethod = _ChasEntityAccessMethod_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 13),
    _ChasEntityAccessMethod_Type()
)
chasEntityAccessMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityAccessMethod.setStatus("mandatory")


class _ChasEntitySlotNumber_Type(Integer32):
    """Custom type chasEntitySlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChasEntitySlotNumber_Type.__name__ = "Integer32"
_ChasEntitySlotNumber_Object = MibTableColumn
chasEntitySlotNumber = _ChasEntitySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 14),
    _ChasEntitySlotNumber_Type()
)
chasEntitySlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntitySlotNumber.setStatus("mandatory")
_ChasEntitySrcIpAddress_Type = IpAddress
_ChasEntitySrcIpAddress_Object = MibTableColumn
chasEntitySrcIpAddress = _ChasEntitySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 15),
    _ChasEntitySrcIpAddress_Type()
)
chasEntitySrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntitySrcIpAddress.setStatus("mandatory")
_ChasEntitySrcSubnetMask_Type = IpAddress
_ChasEntitySrcSubnetMask_Object = MibTableColumn
chasEntitySrcSubnetMask = _ChasEntitySrcSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 16),
    _ChasEntitySrcSubnetMask_Type()
)
chasEntitySrcSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntitySrcSubnetMask.setStatus("mandatory")


class _ChasEntityAccessCharacteristics_Type(Integer32):
    """Custom type chasEntityAccessCharacteristics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_ChasEntityAccessCharacteristics_Type.__name__ = "Integer32"
_ChasEntityAccessCharacteristics_Object = MibTableColumn
chasEntityAccessCharacteristics = _ChasEntityAccessCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 2, 1, 17),
    _ChasEntityAccessCharacteristics_Type()
)
chasEntityAccessCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityAccessCharacteristics.setStatus("mandatory")
_ChasEntityAccessLoadTable_Object = MibTable
chasEntityAccessLoadTable = _ChasEntityAccessLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    chasEntityAccessLoadTable.setStatus("mandatory")
_ChasEntityAccessLoadEntry_Object = MibTableRow
chasEntityAccessLoadEntry = _ChasEntityAccessLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 3, 1)
)
chasEntityAccessLoadEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasEntityAccessLoadSlot"),
)
if mibBuilder.loadTexts:
    chasEntityAccessLoadEntry.setStatus("mandatory")


class _ChasEntityAccessLoadSlot_Type(Integer32):
    """Custom type chasEntityAccessLoadSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChasEntityAccessLoadSlot_Type.__name__ = "Integer32"
_ChasEntityAccessLoadSlot_Object = MibTableColumn
chasEntityAccessLoadSlot = _ChasEntityAccessLoadSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 3, 1, 1),
    _ChasEntityAccessLoadSlot_Type()
)
chasEntityAccessLoadSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityAccessLoadSlot.setStatus("mandatory")


class _ChasEntityAccessLoadMethod_Type(OctetString):
    """Custom type chasEntityAccessLoadMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChasEntityAccessLoadMethod_Type.__name__ = "OctetString"
_ChasEntityAccessLoadMethod_Object = MibTableColumn
chasEntityAccessLoadMethod = _ChasEntityAccessLoadMethod_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 3, 1, 2),
    _ChasEntityAccessLoadMethod_Type()
)
chasEntityAccessLoadMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasEntityAccessLoadMethod.setStatus("mandatory")
_ChasEntityChangeTable_Object = MibTable
chasEntityChangeTable = _ChasEntityChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    chasEntityChangeTable.setStatus("mandatory")
_ChasEntityChangeEntry_Object = MibTableRow
chasEntityChangeEntry = _ChasEntityChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 4, 1)
)
chasEntityChangeEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasEntityChangeSlot"),
)
if mibBuilder.loadTexts:
    chasEntityChangeEntry.setStatus("mandatory")


class _ChasEntityChangeSlot_Type(Integer32):
    """Custom type chasEntityChangeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChasEntityChangeSlot_Type.__name__ = "Integer32"
_ChasEntityChangeSlot_Object = MibTableColumn
chasEntityChangeSlot = _ChasEntityChangeSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 4, 1, 1),
    _ChasEntityChangeSlot_Type()
)
chasEntityChangeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityChangeSlot.setStatus("mandatory")
_ChasEntityChangeCounter_Type = Counter32
_ChasEntityChangeCounter_Object = MibTableColumn
chasEntityChangeCounter = _ChasEntityChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 2, 4, 1, 2),
    _ChasEntityChangeCounter_Type()
)
chasEntityChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntityChangeCounter.setStatus("mandatory")
_ChasBackplane_ObjectIdentity = ObjectIdentity
chasBackplane = _ChasBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 3)
)
_ChasBackplaneTable_Object = MibTable
chasBackplaneTable = _ChasBackplaneTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    chasBackplaneTable.setStatus("mandatory")
_ChasBackplaneEntry_Object = MibTableRow
chasBackplaneEntry = _ChasBackplaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 3, 1, 1)
)
chasBackplaneEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasBackplaneIndex"),
)
if mibBuilder.loadTexts:
    chasBackplaneEntry.setStatus("mandatory")


class _ChasBackplaneIndex_Type(Integer32):
    """Custom type chasBackplaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChasBackplaneIndex_Type.__name__ = "Integer32"
_ChasBackplaneIndex_Object = MibTableColumn
chasBackplaneIndex = _ChasBackplaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 3, 1, 1, 1),
    _ChasBackplaneIndex_Type()
)
chasBackplaneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBackplaneIndex.setStatus("mandatory")


class _ChasBackplaneDescr_Type(DisplayString):
    """Custom type chasBackplaneDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasBackplaneDescr_Type.__name__ = "DisplayString"
_ChasBackplaneDescr_Object = MibTableColumn
chasBackplaneDescr = _ChasBackplaneDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 3, 1, 1, 2),
    _ChasBackplaneDescr_Type()
)
chasBackplaneDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBackplaneDescr.setStatus("mandatory")


class _ChasBackplaneRev_Type(DisplayString):
    """Custom type chasBackplaneRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasBackplaneRev_Type.__name__ = "DisplayString"
_ChasBackplaneRev_Object = MibTableColumn
chasBackplaneRev = _ChasBackplaneRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 3, 1, 1, 3),
    _ChasBackplaneRev_Type()
)
chasBackplaneRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBackplaneRev.setStatus("mandatory")


class _ChasBackplaneNumSlots_Type(Integer32):
    """Custom type chasBackplaneNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ChasBackplaneNumSlots_Type.__name__ = "Integer32"
_ChasBackplaneNumSlots_Object = MibTableColumn
chasBackplaneNumSlots = _ChasBackplaneNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 3, 1, 1, 4),
    _ChasBackplaneNumSlots_Type()
)
chasBackplaneNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBackplaneNumSlots.setStatus("mandatory")
_ChasSegment_ObjectIdentity = ObjectIdentity
chasSegment = _ChasSegment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4)
)
_ChasSegmentTable_Object = MibTable
chasSegmentTable = _ChasSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    chasSegmentTable.setStatus("mandatory")
_ChasSegmentEntry_Object = MibTableRow
chasSegmentEntry = _ChasSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 1, 1)
)
chasSegmentEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasSegmentIndex"),
)
if mibBuilder.loadTexts:
    chasSegmentEntry.setStatus("mandatory")


class _ChasSegmentIndex_Type(Integer32):
    """Custom type chasSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasSegmentIndex_Type.__name__ = "Integer32"
_ChasSegmentIndex_Object = MibTableColumn
chasSegmentIndex = _ChasSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 1, 1, 1),
    _ChasSegmentIndex_Type()
)
chasSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSegmentIndex.setStatus("mandatory")


class _ChasSegmentName_Type(DisplayString):
    """Custom type chasSegmentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasSegmentName_Type.__name__ = "DisplayString"
_ChasSegmentName_Object = MibTableColumn
chasSegmentName = _ChasSegmentName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 1, 1, 2),
    _ChasSegmentName_Type()
)
chasSegmentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSegmentName.setStatus("mandatory")


class _ChasSegmentType_Type(Integer32):
    """Custom type chasSegmentType based on Integer32"""
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
        *(("async", 5),
          ("atm", 4),
          ("ethernet", 2),
          ("fddi", 1),
          ("pebus", 6),
          ("tr", 3))
    )


_ChasSegmentType_Type.__name__ = "Integer32"
_ChasSegmentType_Object = MibTableColumn
chasSegmentType = _ChasSegmentType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 1, 1, 3),
    _ChasSegmentType_Type()
)
chasSegmentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSegmentType.setStatus("mandatory")


class _ChasSegmentSubtypeSelect_Type(Integer32):
    """Custom type chasSegmentSubtypeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasSegmentSubtypeSelect_Type.__name__ = "Integer32"
_ChasSegmentSubtypeSelect_Object = MibTableColumn
chasSegmentSubtypeSelect = _ChasSegmentSubtypeSelect_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 1, 1, 4),
    _ChasSegmentSubtypeSelect_Type()
)
chasSegmentSubtypeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSegmentSubtypeSelect.setStatus("mandatory")


class _ChasSegmentEntryStatus_Type(Integer32):
    """Custom type chasSegmentEntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_ChasSegmentEntryStatus_Type.__name__ = "Integer32"
_ChasSegmentEntryStatus_Object = MibTableColumn
chasSegmentEntryStatus = _ChasSegmentEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 1, 1, 5),
    _ChasSegmentEntryStatus_Type()
)
chasSegmentEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSegmentEntryStatus.setStatus("mandatory")
_ChasSegSubtypeTable_Object = MibTable
chasSegSubtypeTable = _ChasSegSubtypeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    chasSegSubtypeTable.setStatus("mandatory")
_ChasSegSubtypeEntry_Object = MibTableRow
chasSegSubtypeEntry = _ChasSegSubtypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 2, 1)
)
chasSegSubtypeEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasSegSubtypeIndex"),
)
if mibBuilder.loadTexts:
    chasSegSubtypeEntry.setStatus("mandatory")


class _ChasSegSubtypeIndex_Type(Integer32):
    """Custom type chasSegSubtypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasSegSubtypeIndex_Type.__name__ = "Integer32"
_ChasSegSubtypeIndex_Object = MibTableColumn
chasSegSubtypeIndex = _ChasSegSubtypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 2, 1, 1),
    _ChasSegSubtypeIndex_Type()
)
chasSegSubtypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSegSubtypeIndex.setStatus("mandatory")


class _ChasSegSubtypeFlavor_Type(Integer32):
    """Custom type chasSegSubtypeFlavor based on Integer32"""
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
        *(("default", 1),
          ("imb", 3),
          ("imb2", 4),
          ("thinwire", 2))
    )


_ChasSegSubtypeFlavor_Type.__name__ = "Integer32"
_ChasSegSubtypeFlavor_Object = MibTableColumn
chasSegSubtypeFlavor = _ChasSegSubtypeFlavor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 2, 1, 2),
    _ChasSegSubtypeFlavor_Type()
)
chasSegSubtypeFlavor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSegSubtypeFlavor.setStatus("mandatory")


class _ChasSegSubtypeSpeed_Type(Integer32):
    """Custom type chasSegSubtypeSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChasSegSubtypeSpeed_Type.__name__ = "Integer32"
_ChasSegSubtypeSpeed_Object = MibTableColumn
chasSegSubtypeSpeed = _ChasSegSubtypeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 2, 1, 3),
    _ChasSegSubtypeSpeed_Type()
)
chasSegSubtypeSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSegSubtypeSpeed.setStatus("mandatory")


class _ChasSegSubtypeEntryStatus_Type(Integer32):
    """Custom type chasSegSubtypeEntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_ChasSegSubtypeEntryStatus_Type.__name__ = "Integer32"
_ChasSegSubtypeEntryStatus_Object = MibTableColumn
chasSegSubtypeEntryStatus = _ChasSegSubtypeEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 2, 1, 4),
    _ChasSegSubtypeEntryStatus_Type()
)
chasSegSubtypeEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSegSubtypeEntryStatus.setStatus("mandatory")


class _ChasSegDefVNbusState_Type(Integer32):
    """Custom type chasSegDefVNbusState based on Integer32"""
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


_ChasSegDefVNbusState_Type.__name__ = "Integer32"
_ChasSegDefVNbusState_Object = MibScalar
chasSegDefVNbusState = _ChasSegDefVNbusState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 4, 3),
    _ChasSegDefVNbusState_Type()
)
chasSegDefVNbusState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSegDefVNbusState.setStatus("mandatory")
_ChasConfig_ObjectIdentity = ObjectIdentity
chasConfig = _ChasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5)
)


class _ChasChassisSerialNumber_Type(DisplayString):
    """Custom type chasChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ChasChassisSerialNumber_Type.__name__ = "DisplayString"
_ChasChassisSerialNumber_Object = MibScalar
chasChassisSerialNumber = _ChasChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 1),
    _ChasChassisSerialNumber_Type()
)
chasChassisSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasChassisSerialNumber.setStatus("mandatory")
_ChasConnChanges_Type = Counter32
_ChasConnChanges_Object = MibScalar
chasConnChanges = _ChasConnChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 2),
    _ChasConnChanges_Type()
)
chasConnChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasConnChanges.setStatus("mandatory")
_ChasConnTable_Object = MibTable
chasConnTable = _ChasConnTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    chasConnTable.setStatus("mandatory")
_ChasConnEntry_Object = MibTableRow
chasConnEntry = _ChasConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 3, 1)
)
chasConnEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasConnIndex"),
)
if mibBuilder.loadTexts:
    chasConnEntry.setStatus("mandatory")


class _ChasConnIndex_Type(Integer32):
    """Custom type chasConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasConnIndex_Type.__name__ = "Integer32"
_ChasConnIndex_Object = MibTableColumn
chasConnIndex = _ChasConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 3, 1, 1),
    _ChasConnIndex_Type()
)
chasConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasConnIndex.setStatus("mandatory")


class _ChasConnSegment_Type(Integer32):
    """Custom type chasConnSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasConnSegment_Type.__name__ = "Integer32"
_ChasConnSegment_Object = MibTableColumn
chasConnSegment = _ChasConnSegment_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 3, 1, 2),
    _ChasConnSegment_Type()
)
chasConnSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasConnSegment.setStatus("mandatory")


class _ChasConnPort_Type(Integer32):
    """Custom type chasConnPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasConnPort_Type.__name__ = "Integer32"
_ChasConnPort_Object = MibTableColumn
chasConnPort = _ChasConnPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 3, 1, 3),
    _ChasConnPort_Type()
)
chasConnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasConnPort.setStatus("mandatory")


class _ChasConnNextPortIndex_Type(Integer32):
    """Custom type chasConnNextPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasConnNextPortIndex_Type.__name__ = "Integer32"
_ChasConnNextPortIndex_Object = MibTableColumn
chasConnNextPortIndex = _ChasConnNextPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 3, 1, 4),
    _ChasConnNextPortIndex_Type()
)
chasConnNextPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasConnNextPortIndex.setStatus("mandatory")


class _ChasConnEntryStatus_Type(Integer32):
    """Custom type chasConnEntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_ChasConnEntryStatus_Type.__name__ = "Integer32"
_ChasConnEntryStatus_Object = MibTableColumn
chasConnEntryStatus = _ChasConnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 5, 3, 1, 5),
    _ChasConnEntryStatus_Type()
)
chasConnEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasConnEntryStatus.setStatus("mandatory")
_ChasPort_ObjectIdentity = ObjectIdentity
chasPort = _ChasPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6)
)
_ChasPortLastChange_Type = TimeTicks
_ChasPortLastChange_Object = MibScalar
chasPortLastChange = _ChasPortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 1),
    _ChasPortLastChange_Type()
)
chasPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortLastChange.setStatus("mandatory")
_ChasPortTable_Object = MibTable
chasPortTable = _ChasPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    chasPortTable.setStatus("mandatory")
_ChasPortEntry_Object = MibTableRow
chasPortEntry = _ChasPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 2, 1)
)
chasPortEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasPortIndex"),
)
if mibBuilder.loadTexts:
    chasPortEntry.setStatus("mandatory")


class _ChasPortIndex_Type(Integer32):
    """Custom type chasPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPortIndex_Type.__name__ = "Integer32"
_ChasPortIndex_Object = MibTableColumn
chasPortIndex = _ChasPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 2, 1, 1),
    _ChasPortIndex_Type()
)
chasPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortIndex.setStatus("mandatory")


class _ChasPortSlot_Type(Integer32):
    """Custom type chasPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChasPortSlot_Type.__name__ = "Integer32"
_ChasPortSlot_Object = MibTableColumn
chasPortSlot = _ChasPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 2, 1, 2),
    _ChasPortSlot_Type()
)
chasPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortSlot.setStatus("mandatory")


class _ChasPortName_Type(DisplayString):
    """Custom type chasPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasPortName_Type.__name__ = "DisplayString"
_ChasPortName_Object = MibTableColumn
chasPortName = _ChasPortName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 2, 1, 3),
    _ChasPortName_Type()
)
chasPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasPortName.setStatus("mandatory")


class _ChasPortType_Type(Integer32):
    """Custom type chasPortType based on Integer32"""
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
        *(("async", 5),
          ("atm", 4),
          ("ethernet", 2),
          ("fddi", 1),
          ("pebus", 6),
          ("tr", 3))
    )


_ChasPortType_Type.__name__ = "Integer32"
_ChasPortType_Object = MibTableColumn
chasPortType = _ChasPortType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 2, 1, 4),
    _ChasPortType_Type()
)
chasPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortType.setStatus("mandatory")


class _ChasPortSubtypeSelect_Type(Integer32):
    """Custom type chasPortSubtypeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasPortSubtypeSelect_Type.__name__ = "Integer32"
_ChasPortSubtypeSelect_Object = MibTableColumn
chasPortSubtypeSelect = _ChasPortSubtypeSelect_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 2, 1, 5),
    _ChasPortSubtypeSelect_Type()
)
chasPortSubtypeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasPortSubtypeSelect.setStatus("mandatory")


class _ChasPortOperStatus_Type(Integer32):
    """Custom type chasPortOperStatus based on Integer32"""
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
        *(("broken", 1),
          ("configured", 3),
          ("connected", 5),
          ("testing", 4),
          ("unconfigured", 2))
    )


_ChasPortOperStatus_Type.__name__ = "Integer32"
_ChasPortOperStatus_Object = MibTableColumn
chasPortOperStatus = _ChasPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 2, 1, 6),
    _ChasPortOperStatus_Type()
)
chasPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortOperStatus.setStatus("mandatory")
_ChasPortDescrTable_Object = MibTable
chasPortDescrTable = _ChasPortDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    chasPortDescrTable.setStatus("mandatory")
_ChasPortDescrEntry_Object = MibTableRow
chasPortDescrEntry = _ChasPortDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 3, 1)
)
chasPortDescrEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasPortDescrIndex"),
)
if mibBuilder.loadTexts:
    chasPortDescrEntry.setStatus("mandatory")


class _ChasPortDescrIndex_Type(Integer32):
    """Custom type chasPortDescrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPortDescrIndex_Type.__name__ = "Integer32"
_ChasPortDescrIndex_Object = MibTableColumn
chasPortDescrIndex = _ChasPortDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 3, 1, 1),
    _ChasPortDescrIndex_Type()
)
chasPortDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortDescrIndex.setStatus("mandatory")


class _ChasPortDescr_Type(DisplayString):
    """Custom type chasPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasPortDescr_Type.__name__ = "DisplayString"
_ChasPortDescr_Object = MibTableColumn
chasPortDescr = _ChasPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 3, 1, 2),
    _ChasPortDescr_Type()
)
chasPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortDescr.setStatus("mandatory")
_ChasPortSubtypeTable_Object = MibTable
chasPortSubtypeTable = _ChasPortSubtypeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    chasPortSubtypeTable.setStatus("mandatory")
_ChasPortSubtypeEntry_Object = MibTableRow
chasPortSubtypeEntry = _ChasPortSubtypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 4, 1)
)
chasPortSubtypeEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasPortSubtypeIndex"),
)
if mibBuilder.loadTexts:
    chasPortSubtypeEntry.setStatus("mandatory")


class _ChasPortSubtypeIndex_Type(Integer32):
    """Custom type chasPortSubtypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPortSubtypeIndex_Type.__name__ = "Integer32"
_ChasPortSubtypeIndex_Object = MibTableColumn
chasPortSubtypeIndex = _ChasPortSubtypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 4, 1, 1),
    _ChasPortSubtypeIndex_Type()
)
chasPortSubtypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortSubtypeIndex.setStatus("mandatory")


class _ChasPortSubtypePortIndex_Type(Integer32):
    """Custom type chasPortSubtypePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPortSubtypePortIndex_Type.__name__ = "Integer32"
_ChasPortSubtypePortIndex_Object = MibTableColumn
chasPortSubtypePortIndex = _ChasPortSubtypePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 4, 1, 2),
    _ChasPortSubtypePortIndex_Type()
)
chasPortSubtypePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortSubtypePortIndex.setStatus("mandatory")


class _ChasPortSubtypeFlavor_Type(Integer32):
    """Custom type chasPortSubtypeFlavor based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("atmMaster", 13),
          ("atmSlave", 14),
          ("default", 1),
          ("fddiA", 6),
          ("fddiB", 7),
          ("fddiM", 8),
          ("fddiS", 9),
          ("imb2EndStation", 12),
          ("imb2FlexRepeater", 16),
          ("imb2Repeater", 15),
          ("imbEndStation", 4),
          ("imbFlexRepeater", 11),
          ("imbRepeater", 5),
          ("thinwireEndStation", 2),
          ("thinwireFlexRepeater", 10),
          ("thinwireRepeater", 3))
    )


_ChasPortSubtypeFlavor_Type.__name__ = "Integer32"
_ChasPortSubtypeFlavor_Object = MibTableColumn
chasPortSubtypeFlavor = _ChasPortSubtypeFlavor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 4, 1, 3),
    _ChasPortSubtypeFlavor_Type()
)
chasPortSubtypeFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortSubtypeFlavor.setStatus("mandatory")


class _ChasPortSubtypeSpeed_Type(Integer32):
    """Custom type chasPortSubtypeSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChasPortSubtypeSpeed_Type.__name__ = "Integer32"
_ChasPortSubtypeSpeed_Object = MibTableColumn
chasPortSubtypeSpeed = _ChasPortSubtypeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 6, 4, 1, 4),
    _ChasPortSubtypeSpeed_Type()
)
chasPortSubtypeSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPortSubtypeSpeed.setStatus("mandatory")
_ChasPowerConfig_ObjectIdentity = ObjectIdentity
chasPowerConfig = _ChasPowerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7)
)


class _ChasPowerConfigMaxSupplies_Type(Integer32):
    """Custom type chasPowerConfigMaxSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPowerConfigMaxSupplies_Type.__name__ = "Integer32"
_ChasPowerConfigMaxSupplies_Object = MibScalar
chasPowerConfigMaxSupplies = _ChasPowerConfigMaxSupplies_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 1),
    _ChasPowerConfigMaxSupplies_Type()
)
chasPowerConfigMaxSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigMaxSupplies.setStatus("mandatory")


class _ChasPowerConfigNumSupplies_Type(Integer32):
    """Custom type chasPowerConfigNumSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPowerConfigNumSupplies_Type.__name__ = "Integer32"
_ChasPowerConfigNumSupplies_Object = MibScalar
chasPowerConfigNumSupplies = _ChasPowerConfigNumSupplies_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 2),
    _ChasPowerConfigNumSupplies_Type()
)
chasPowerConfigNumSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigNumSupplies.setStatus("mandatory")
_ChasPowerConfigChanges_Type = Counter32
_ChasPowerConfigChanges_Object = MibScalar
chasPowerConfigChanges = _ChasPowerConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 3),
    _ChasPowerConfigChanges_Type()
)
chasPowerConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigChanges.setStatus("mandatory")


class _ChasPowerConfigRedundancyState_Type(Integer32):
    """Custom type chasPowerConfigRedundancyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundantPowerAvailable", 1),
          ("redundantPowerNotAvailable", 2))
    )


_ChasPowerConfigRedundancyState_Type.__name__ = "Integer32"
_ChasPowerConfigRedundancyState_Object = MibScalar
chasPowerConfigRedundancyState = _ChasPowerConfigRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 4),
    _ChasPowerConfigRedundancyState_Type()
)
chasPowerConfigRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigRedundancyState.setStatus("mandatory")
_ChasPowerConfigTable_Object = MibTable
chasPowerConfigTable = _ChasPowerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5)
)
if mibBuilder.loadTexts:
    chasPowerConfigTable.setStatus("mandatory")
_ChasPowerConfigEntry_Object = MibTableRow
chasPowerConfigEntry = _ChasPowerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5, 1)
)
chasPowerConfigEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasPowerConfigIndex"),
)
if mibBuilder.loadTexts:
    chasPowerConfigEntry.setStatus("mandatory")


class _ChasPowerConfigIndex_Type(Integer32):
    """Custom type chasPowerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPowerConfigIndex_Type.__name__ = "Integer32"
_ChasPowerConfigIndex_Object = MibTableColumn
chasPowerConfigIndex = _ChasPowerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5, 1, 1),
    _ChasPowerConfigIndex_Type()
)
chasPowerConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigIndex.setStatus("mandatory")


class _ChasPowerConfigDescr_Type(DisplayString):
    """Custom type chasPowerConfigDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasPowerConfigDescr_Type.__name__ = "DisplayString"
_ChasPowerConfigDescr_Object = MibTableColumn
chasPowerConfigDescr = _ChasPowerConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5, 1, 2),
    _ChasPowerConfigDescr_Type()
)
chasPowerConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigDescr.setStatus("mandatory")


class _ChasPowerConfigAdminStatus_Type(Integer32):
    """Custom type chasPowerConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("unknown", 1))
    )


_ChasPowerConfigAdminStatus_Type.__name__ = "Integer32"
_ChasPowerConfigAdminStatus_Object = MibTableColumn
chasPowerConfigAdminStatus = _ChasPowerConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5, 1, 3),
    _ChasPowerConfigAdminStatus_Type()
)
chasPowerConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasPowerConfigAdminStatus.setStatus("mandatory")


class _ChasPowerConfigOperStatus_Type(Integer32):
    """Custom type chasPowerConfigOperStatus based on Integer32"""
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
        *(("bad", 4),
          ("disabled", 3),
          ("empty", 2),
          ("engaged", 7),
          ("redundant", 8),
          ("standby", 6),
          ("unknown", 1),
          ("warning", 5))
    )


_ChasPowerConfigOperStatus_Type.__name__ = "Integer32"
_ChasPowerConfigOperStatus_Object = MibTableColumn
chasPowerConfigOperStatus = _ChasPowerConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5, 1, 4),
    _ChasPowerConfigOperStatus_Type()
)
chasPowerConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigOperStatus.setStatus("mandatory")


class _ChasPowerConfigHealthText_Type(DisplayString):
    """Custom type chasPowerConfigHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasPowerConfigHealthText_Type.__name__ = "DisplayString"
_ChasPowerConfigHealthText_Object = MibTableColumn
chasPowerConfigHealthText = _ChasPowerConfigHealthText_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5, 1, 5),
    _ChasPowerConfigHealthText_Type()
)
chasPowerConfigHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigHealthText.setStatus("mandatory")
_ChasPowerConfigWarnings_Type = Counter32
_ChasPowerConfigWarnings_Object = MibTableColumn
chasPowerConfigWarnings = _ChasPowerConfigWarnings_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5, 1, 6),
    _ChasPowerConfigWarnings_Type()
)
chasPowerConfigWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigWarnings.setStatus("mandatory")
_ChasPowerConfigFailures_Type = Counter32
_ChasPowerConfigFailures_Object = MibTableColumn
chasPowerConfigFailures = _ChasPowerConfigFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 7, 5, 1, 7),
    _ChasPowerConfigFailures_Type()
)
chasPowerConfigFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerConfigFailures.setStatus("mandatory")
_ChasPowerSource_ObjectIdentity = ObjectIdentity
chasPowerSource = _ChasPowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8)
)


class _ChasPowerSourceTotalPowerAvailable_Type(Integer32):
    """Custom type chasPowerSourceTotalPowerAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChasPowerSourceTotalPowerAvailable_Type.__name__ = "Integer32"
_ChasPowerSourceTotalPowerAvailable_Object = MibScalar
chasPowerSourceTotalPowerAvailable = _ChasPowerSourceTotalPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8, 1),
    _ChasPowerSourceTotalPowerAvailable_Type()
)
chasPowerSourceTotalPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSourceTotalPowerAvailable.setStatus("mandatory")


class _ChasPowerSourceTotalCurrentAvailable_Type(Integer32):
    """Custom type chasPowerSourceTotalCurrentAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChasPowerSourceTotalCurrentAvailable_Type.__name__ = "Integer32"
_ChasPowerSourceTotalCurrentAvailable_Object = MibScalar
chasPowerSourceTotalCurrentAvailable = _ChasPowerSourceTotalCurrentAvailable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8, 2),
    _ChasPowerSourceTotalCurrentAvailable_Type()
)
chasPowerSourceTotalCurrentAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSourceTotalCurrentAvailable.setStatus("mandatory")
_ChasPowerSourceTable_Object = MibTable
chasPowerSourceTable = _ChasPowerSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    chasPowerSourceTable.setStatus("mandatory")
_ChasPowerSourceEntry_Object = MibTableRow
chasPowerSourceEntry = _ChasPowerSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8, 3, 1)
)
chasPowerSourceEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasPowerSourceSupplyIndex"),
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasPowerSourceIndex"),
)
if mibBuilder.loadTexts:
    chasPowerSourceEntry.setStatus("mandatory")


class _ChasPowerSourceSupplyIndex_Type(Integer32):
    """Custom type chasPowerSourceSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPowerSourceSupplyIndex_Type.__name__ = "Integer32"
_ChasPowerSourceSupplyIndex_Object = MibTableColumn
chasPowerSourceSupplyIndex = _ChasPowerSourceSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8, 3, 1, 1),
    _ChasPowerSourceSupplyIndex_Type()
)
chasPowerSourceSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSourceSupplyIndex.setStatus("mandatory")


class _ChasPowerSourceIndex_Type(Integer32):
    """Custom type chasPowerSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPowerSourceIndex_Type.__name__ = "Integer32"
_ChasPowerSourceIndex_Object = MibTableColumn
chasPowerSourceIndex = _ChasPowerSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8, 3, 1, 2),
    _ChasPowerSourceIndex_Type()
)
chasPowerSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSourceIndex.setStatus("mandatory")


class _ChasPowerSourceNominalVoltage_Type(Integer32):
    """Custom type chasPowerSourceNominalVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChasPowerSourceNominalVoltage_Type.__name__ = "Integer32"
_ChasPowerSourceNominalVoltage_Object = MibTableColumn
chasPowerSourceNominalVoltage = _ChasPowerSourceNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8, 3, 1, 3),
    _ChasPowerSourceNominalVoltage_Type()
)
chasPowerSourceNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSourceNominalVoltage.setStatus("mandatory")


class _ChasPowerSourcePower_Type(Integer32):
    """Custom type chasPowerSourcePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChasPowerSourcePower_Type.__name__ = "Integer32"
_ChasPowerSourcePower_Object = MibTableColumn
chasPowerSourcePower = _ChasPowerSourcePower_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 8, 3, 1, 4),
    _ChasPowerSourcePower_Type()
)
chasPowerSourcePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSourcePower.setStatus("mandatory")
_ChasPowerSink_ObjectIdentity = ObjectIdentity
chasPowerSink = _ChasPowerSink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 9)
)
_ChasPowerSinkTable_Object = MibTable
chasPowerSinkTable = _ChasPowerSinkTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    chasPowerSinkTable.setStatus("mandatory")
_ChasPowerSinkEntry_Object = MibTableRow
chasPowerSinkEntry = _ChasPowerSinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 9, 1, 1)
)
chasPowerSinkEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasPowerSinkSlotIndex"),
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasPowerSinkIndex"),
)
if mibBuilder.loadTexts:
    chasPowerSinkEntry.setStatus("mandatory")


class _ChasPowerSinkSlotIndex_Type(Integer32):
    """Custom type chasPowerSinkSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPowerSinkSlotIndex_Type.__name__ = "Integer32"
_ChasPowerSinkSlotIndex_Object = MibTableColumn
chasPowerSinkSlotIndex = _ChasPowerSinkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 9, 1, 1, 1),
    _ChasPowerSinkSlotIndex_Type()
)
chasPowerSinkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSinkSlotIndex.setStatus("mandatory")


class _ChasPowerSinkIndex_Type(Integer32):
    """Custom type chasPowerSinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasPowerSinkIndex_Type.__name__ = "Integer32"
_ChasPowerSinkIndex_Object = MibTableColumn
chasPowerSinkIndex = _ChasPowerSinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 9, 1, 1, 2),
    _ChasPowerSinkIndex_Type()
)
chasPowerSinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSinkIndex.setStatus("mandatory")
_ChasPowerSinkVoltage_Type = Gauge32
_ChasPowerSinkVoltage_Object = MibTableColumn
chasPowerSinkVoltage = _ChasPowerSinkVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 9, 1, 1, 3),
    _ChasPowerSinkVoltage_Type()
)
chasPowerSinkVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSinkVoltage.setStatus("mandatory")
_ChasPowerSinkWattage_Type = Gauge32
_ChasPowerSinkWattage_Object = MibTableColumn
chasPowerSinkWattage = _ChasPowerSinkWattage_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 9, 1, 1, 4),
    _ChasPowerSinkWattage_Type()
)
chasPowerSinkWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSinkWattage.setStatus("mandatory")


class _ChasPowerSinkOperStatus_Type(Integer32):
    """Custom type chasPowerSinkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 2),
          ("notInUse", 3),
          ("unknown", 1))
    )


_ChasPowerSinkOperStatus_Type.__name__ = "Integer32"
_ChasPowerSinkOperStatus_Object = MibTableColumn
chasPowerSinkOperStatus = _ChasPowerSinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 9, 1, 1, 5),
    _ChasPowerSinkOperStatus_Type()
)
chasPowerSinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSinkOperStatus.setStatus("mandatory")
_ChasEnviron_ObjectIdentity = ObjectIdentity
chasEnviron = _ChasEnviron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10)
)
_ChasEnvironChanges_Type = Counter32
_ChasEnvironChanges_Object = MibScalar
chasEnvironChanges = _ChasEnvironChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 1),
    _ChasEnvironChanges_Type()
)
chasEnvironChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvironChanges.setStatus("mandatory")
_ChasEnvironTable_Object = MibTable
chasEnvironTable = _ChasEnvironTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    chasEnvironTable.setStatus("mandatory")
_ChasEnvironEntry_Object = MibTableRow
chasEnvironEntry = _ChasEnvironEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2, 1)
)
chasEnvironEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasEnvironSlotIndex"),
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasEnvironSensorIndex"),
)
if mibBuilder.loadTexts:
    chasEnvironEntry.setStatus("mandatory")


class _ChasEnvironSlotIndex_Type(Integer32):
    """Custom type chasEnvironSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasEnvironSlotIndex_Type.__name__ = "Integer32"
_ChasEnvironSlotIndex_Object = MibTableColumn
chasEnvironSlotIndex = _ChasEnvironSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2, 1, 1),
    _ChasEnvironSlotIndex_Type()
)
chasEnvironSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvironSlotIndex.setStatus("mandatory")


class _ChasEnvironSensorIndex_Type(Integer32):
    """Custom type chasEnvironSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasEnvironSensorIndex_Type.__name__ = "Integer32"
_ChasEnvironSensorIndex_Object = MibTableColumn
chasEnvironSensorIndex = _ChasEnvironSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2, 1, 2),
    _ChasEnvironSensorIndex_Type()
)
chasEnvironSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvironSensorIndex.setStatus("mandatory")


class _ChasEnvironSensor_Type(Integer32):
    """Custom type chasEnvironSensor based on Integer32"""
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
        *(("dc-power", 5),
          ("fan", 3),
          ("humidity", 4),
          ("other", 1),
          ("temperature", 2))
    )


_ChasEnvironSensor_Type.__name__ = "Integer32"
_ChasEnvironSensor_Object = MibTableColumn
chasEnvironSensor = _ChasEnvironSensor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2, 1, 3),
    _ChasEnvironSensor_Type()
)
chasEnvironSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvironSensor.setStatus("mandatory")


class _ChasEnvironAdminStatus_Type(Integer32):
    """Custom type chasEnvironAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("unknown", 1))
    )


_ChasEnvironAdminStatus_Type.__name__ = "Integer32"
_ChasEnvironAdminStatus_Object = MibTableColumn
chasEnvironAdminStatus = _ChasEnvironAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2, 1, 4),
    _ChasEnvironAdminStatus_Type()
)
chasEnvironAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasEnvironAdminStatus.setStatus("mandatory")


class _ChasEnvironOperStatus_Type(Integer32):
    """Custom type chasEnvironOperStatus based on Integer32"""
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
        *(("bad", 2),
          ("disabled", 5),
          ("good", 4),
          ("unknown", 1),
          ("warning", 3))
    )


_ChasEnvironOperStatus_Type.__name__ = "Integer32"
_ChasEnvironOperStatus_Object = MibTableColumn
chasEnvironOperStatus = _ChasEnvironOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2, 1, 5),
    _ChasEnvironOperStatus_Type()
)
chasEnvironOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvironOperStatus.setStatus("mandatory")
_ChasEnvironWarnings_Type = Counter32
_ChasEnvironWarnings_Object = MibTableColumn
chasEnvironWarnings = _ChasEnvironWarnings_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2, 1, 6),
    _ChasEnvironWarnings_Type()
)
chasEnvironWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvironWarnings.setStatus("mandatory")
_ChasEnvironFailures_Type = Counter32
_ChasEnvironFailures_Object = MibTableColumn
chasEnvironFailures = _ChasEnvironFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 10, 2, 1, 7),
    _ChasEnvironFailures_Type()
)
chasEnvironFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvironFailures.setStatus("mandatory")
_ChasLoad_ObjectIdentity = ObjectIdentity
chasLoad = _ChasLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11)
)
_ChasLoadTable_Object = MibTable
chasLoadTable = _ChasLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    chasLoadTable.setStatus("mandatory")
_ChasLoadEntry_Object = MibTableRow
chasLoadEntry = _ChasLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1, 1)
)
chasLoadEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasLoadSlotIndex"),
)
if mibBuilder.loadTexts:
    chasLoadEntry.setStatus("mandatory")


class _ChasLoadSlotIndex_Type(Integer32):
    """Custom type chasLoadSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChasLoadSlotIndex_Type.__name__ = "Integer32"
_ChasLoadSlotIndex_Object = MibTableColumn
chasLoadSlotIndex = _ChasLoadSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1, 1, 1),
    _ChasLoadSlotIndex_Type()
)
chasLoadSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLoadSlotIndex.setStatus("mandatory")


class _ChasLoadAdminStatus_Type(Integer32):
    """Custom type chasLoadAdminStatus based on Integer32"""
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
        *(("cancel", 4),
          ("other", 1),
          ("start-read", 2),
          ("start-write", 3))
    )


_ChasLoadAdminStatus_Type.__name__ = "Integer32"
_ChasLoadAdminStatus_Object = MibTableColumn
chasLoadAdminStatus = _ChasLoadAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1, 1, 2),
    _ChasLoadAdminStatus_Type()
)
chasLoadAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasLoadAdminStatus.setStatus("mandatory")


class _ChasLoadOperStatus_Type(Integer32):
    """Custom type chasLoadOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("none", 1),
          ("success", 2))
    )


_ChasLoadOperStatus_Type.__name__ = "Integer32"
_ChasLoadOperStatus_Object = MibTableColumn
chasLoadOperStatus = _ChasLoadOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1, 1, 3),
    _ChasLoadOperStatus_Type()
)
chasLoadOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLoadOperStatus.setStatus("mandatory")


class _ChasLoadFileName_Type(DisplayString):
    """Custom type chasLoadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ChasLoadFileName_Type.__name__ = "DisplayString"
_ChasLoadFileName_Object = MibTableColumn
chasLoadFileName = _ChasLoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1, 1, 4),
    _ChasLoadFileName_Type()
)
chasLoadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasLoadFileName.setStatus("mandatory")
_ChasLoadIpHostAddr_Type = IpAddress
_ChasLoadIpHostAddr_Object = MibTableColumn
chasLoadIpHostAddr = _ChasLoadIpHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1, 1, 5),
    _ChasLoadIpHostAddr_Type()
)
chasLoadIpHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasLoadIpHostAddr.setStatus("mandatory")


class _ChasLoadDevSpecific_Type(Integer32):
    """Custom type chasLoadDevSpecific based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChasLoadDevSpecific_Type.__name__ = "Integer32"
_ChasLoadDevSpecific_Object = MibTableColumn
chasLoadDevSpecific = _ChasLoadDevSpecific_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1, 1, 6),
    _ChasLoadDevSpecific_Type()
)
chasLoadDevSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLoadDevSpecific.setStatus("mandatory")


class _ChasLoadEntryStatus_Type(Integer32):
    """Custom type chasLoadEntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_ChasLoadEntryStatus_Type.__name__ = "Integer32"
_ChasLoadEntryStatus_Object = MibTableColumn
chasLoadEntryStatus = _ChasLoadEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 11, 1, 1, 7),
    _ChasLoadEntryStatus_Type()
)
chasLoadEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasLoadEntryStatus.setStatus("mandatory")
_ChasLigo_ObjectIdentity = ObjectIdentity
chasLigo = _ChasLigo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13)
)


class _ChasLigoNumEntries_Type(Integer32):
    """Custom type chasLigoNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasLigoNumEntries_Type.__name__ = "Integer32"
_ChasLigoNumEntries_Object = MibScalar
chasLigoNumEntries = _ChasLigoNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 1),
    _ChasLigoNumEntries_Type()
)
chasLigoNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoNumEntries.setStatus("mandatory")
_ChasLigoTable_Object = MibTable
chasLigoTable = _ChasLigoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    chasLigoTable.setStatus("mandatory")
_ChasLigoEntry_Object = MibTableRow
chasLigoEntry = _ChasLigoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 2, 1)
)
chasLigoEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasLigoIndex"),
)
if mibBuilder.loadTexts:
    chasLigoEntry.setStatus("mandatory")


class _ChasLigoIndex_Type(Integer32):
    """Custom type chasLigoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasLigoIndex_Type.__name__ = "Integer32"
_ChasLigoIndex_Object = MibTableColumn
chasLigoIndex = _ChasLigoIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 2, 1, 1),
    _ChasLigoIndex_Type()
)
chasLigoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoIndex.setStatus("mandatory")


class _ChasLigoSlot_Type(Integer32):
    """Custom type chasLigoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChasLigoSlot_Type.__name__ = "Integer32"
_ChasLigoSlot_Object = MibTableColumn
chasLigoSlot = _ChasLigoSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 2, 1, 2),
    _ChasLigoSlot_Type()
)
chasLigoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSlot.setStatus("mandatory")


class _ChasLigoType_Type(Integer32):
    """Custom type chasLigoType based on Integer32"""
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
        *(("atm", 4),
          ("ethernet", 3),
          ("fddi", 2),
          ("other", 1))
    )


_ChasLigoType_Type.__name__ = "Integer32"
_ChasLigoType_Object = MibTableColumn
chasLigoType = _ChasLigoType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 2, 1, 3),
    _ChasLigoType_Type()
)
chasLigoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoType.setStatus("mandatory")


class _ChasLigoSubtypeSelect_Type(Integer32):
    """Custom type chasLigoSubtypeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasLigoSubtypeSelect_Type.__name__ = "Integer32"
_ChasLigoSubtypeSelect_Object = MibTableColumn
chasLigoSubtypeSelect = _ChasLigoSubtypeSelect_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 2, 1, 4),
    _ChasLigoSubtypeSelect_Type()
)
chasLigoSubtypeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasLigoSubtypeSelect.setStatus("mandatory")


class _ChasLigoSubtypeNumEntries_Type(Integer32):
    """Custom type chasLigoSubtypeNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasLigoSubtypeNumEntries_Type.__name__ = "Integer32"
_ChasLigoSubtypeNumEntries_Object = MibScalar
chasLigoSubtypeNumEntries = _ChasLigoSubtypeNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 3),
    _ChasLigoSubtypeNumEntries_Type()
)
chasLigoSubtypeNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSubtypeNumEntries.setStatus("mandatory")
_ChasLigoSubtypeTable_Object = MibTable
chasLigoSubtypeTable = _ChasLigoSubtypeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4)
)
if mibBuilder.loadTexts:
    chasLigoSubtypeTable.setStatus("mandatory")
_ChasLigoSubtypeEntry_Object = MibTableRow
chasLigoSubtypeEntry = _ChasLigoSubtypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4, 1)
)
chasLigoSubtypeEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasLigoSubtypeIndex"),
)
if mibBuilder.loadTexts:
    chasLigoSubtypeEntry.setStatus("mandatory")


class _ChasLigoSubtypeIndex_Type(Integer32):
    """Custom type chasLigoSubtypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasLigoSubtypeIndex_Type.__name__ = "Integer32"
_ChasLigoSubtypeIndex_Object = MibTableColumn
chasLigoSubtypeIndex = _ChasLigoSubtypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4, 1, 1),
    _ChasLigoSubtypeIndex_Type()
)
chasLigoSubtypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSubtypeIndex.setStatus("mandatory")


class _ChasLigoSubtypeLigoIndex_Type(Integer32):
    """Custom type chasLigoSubtypeLigoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasLigoSubtypeLigoIndex_Type.__name__ = "Integer32"
_ChasLigoSubtypeLigoIndex_Object = MibTableColumn
chasLigoSubtypeLigoIndex = _ChasLigoSubtypeLigoIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4, 1, 2),
    _ChasLigoSubtypeLigoIndex_Type()
)
chasLigoSubtypeLigoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSubtypeLigoIndex.setStatus("mandatory")


class _ChasLigoSubtypePortMask_Type(OctetString):
    """Custom type chasLigoSubtypePortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ChasLigoSubtypePortMask_Type.__name__ = "OctetString"
_ChasLigoSubtypePortMask_Object = MibTableColumn
chasLigoSubtypePortMask = _ChasLigoSubtypePortMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4, 1, 3),
    _ChasLigoSubtypePortMask_Type()
)
chasLigoSubtypePortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSubtypePortMask.setStatus("mandatory")


class _ChasLigoSubtypeLabelIndexMask_Type(OctetString):
    """Custom type chasLigoSubtypeLabelIndexMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ChasLigoSubtypeLabelIndexMask_Type.__name__ = "OctetString"
_ChasLigoSubtypeLabelIndexMask_Object = MibTableColumn
chasLigoSubtypeLabelIndexMask = _ChasLigoSubtypeLabelIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4, 1, 4),
    _ChasLigoSubtypeLabelIndexMask_Type()
)
chasLigoSubtypeLabelIndexMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSubtypeLabelIndexMask.setStatus("mandatory")


class _ChasLigoSubtypeFlavor_Type(Integer32):
    """Custom type chasLigoSubtypeFlavor based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("atm-back", 18),
          ("atm-front", 17),
          ("ethernet-back", 13),
          ("ethernet-front", 12),
          ("fddiNonroot", 3),
          ("fddiNonroot-M", 14),
          ("fddiNonroot-S", 15),
          ("fddiNonroot-SM", 16),
          ("fddiRoot-Primary", 1),
          ("fddiRoot-Secondary", 2),
          ("fddiStump-Primary", 10),
          ("fddiStump-Secondary", 11),
          ("fddiTrunk-A-Primary", 4),
          ("fddiTrunk-A-Secondary", 5),
          ("fddiTrunk-AB-Primary", 8),
          ("fddiTrunk-AB-Secondary", 9),
          ("fddiTrunk-B-Primary", 6),
          ("fddiTrunk-B-Secondary", 7))
    )


_ChasLigoSubtypeFlavor_Type.__name__ = "Integer32"
_ChasLigoSubtypeFlavor_Object = MibTableColumn
chasLigoSubtypeFlavor = _ChasLigoSubtypeFlavor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4, 1, 5),
    _ChasLigoSubtypeFlavor_Type()
)
chasLigoSubtypeFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSubtypeFlavor.setStatus("mandatory")


class _ChasLigoSubtypePortMaskV2_Type(OctetString):
    """Custom type chasLigoSubtypePortMaskV2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ChasLigoSubtypePortMaskV2_Type.__name__ = "OctetString"
_ChasLigoSubtypePortMaskV2_Object = MibTableColumn
chasLigoSubtypePortMaskV2 = _ChasLigoSubtypePortMaskV2_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4, 1, 6),
    _ChasLigoSubtypePortMaskV2_Type()
)
chasLigoSubtypePortMaskV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSubtypePortMaskV2.setStatus("mandatory")


class _ChasLigoSubtypeLabelIndexMaskV2_Type(OctetString):
    """Custom type chasLigoSubtypeLabelIndexMaskV2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ChasLigoSubtypeLabelIndexMaskV2_Type.__name__ = "OctetString"
_ChasLigoSubtypeLabelIndexMaskV2_Object = MibTableColumn
chasLigoSubtypeLabelIndexMaskV2 = _ChasLigoSubtypeLabelIndexMaskV2_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 4, 1, 7),
    _ChasLigoSubtypeLabelIndexMaskV2_Type()
)
chasLigoSubtypeLabelIndexMaskV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoSubtypeLabelIndexMaskV2.setStatus("mandatory")


class _ChasLigoLabelNumEntries_Type(Integer32):
    """Custom type chasLigoLabelNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasLigoLabelNumEntries_Type.__name__ = "Integer32"
_ChasLigoLabelNumEntries_Object = MibScalar
chasLigoLabelNumEntries = _ChasLigoLabelNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 5),
    _ChasLigoLabelNumEntries_Type()
)
chasLigoLabelNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoLabelNumEntries.setStatus("mandatory")
_ChasLigoLabelTable_Object = MibTable
chasLigoLabelTable = _ChasLigoLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 6)
)
if mibBuilder.loadTexts:
    chasLigoLabelTable.setStatus("mandatory")
_ChasLigoLabelEntry_Object = MibTableRow
chasLigoLabelEntry = _ChasLigoLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 6, 1)
)
chasLigoLabelEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasLigoLabelIndex"),
)
if mibBuilder.loadTexts:
    chasLigoLabelEntry.setStatus("mandatory")


class _ChasLigoLabelIndex_Type(Integer32):
    """Custom type chasLigoLabelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasLigoLabelIndex_Type.__name__ = "Integer32"
_ChasLigoLabelIndex_Object = MibTableColumn
chasLigoLabelIndex = _ChasLigoLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 6, 1, 1),
    _ChasLigoLabelIndex_Type()
)
chasLigoLabelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoLabelIndex.setStatus("mandatory")


class _ChasLigoLabelString_Type(DisplayString):
    """Custom type chasLigoLabelString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasLigoLabelString_Type.__name__ = "DisplayString"
_ChasLigoLabelString_Object = MibTableColumn
chasLigoLabelString = _ChasLigoLabelString_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 13, 6, 1, 2),
    _ChasLigoLabelString_Type()
)
chasLigoLabelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLigoLabelString.setStatus("mandatory")
_ChasPatching_ObjectIdentity = ObjectIdentity
chasPatching = _ChasPatching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 14)
)


class _ChasRingPatching_Type(Integer32):
    """Custom type chasRingPatching based on Integer32"""
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


_ChasRingPatching_Type.__name__ = "Integer32"
_ChasRingPatching_Object = MibScalar
chasRingPatching = _ChasRingPatching_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 14, 1),
    _ChasRingPatching_Type()
)
chasRingPatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasRingPatching.setStatus("mandatory")
_ChasRingMemberTable_Object = MibTable
chasRingMemberTable = _ChasRingMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    chasRingMemberTable.setStatus("mandatory")
_ChasRingMemberEntry_Object = MibTableRow
chasRingMemberEntry = _ChasRingMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 14, 2, 1)
)
chasRingMemberEntry.setIndexNames(
    (0, "DECHUB900-CHASSIS-MIB-V3-0", "chasRingMemberSlot"),
)
if mibBuilder.loadTexts:
    chasRingMemberEntry.setStatus("mandatory")


class _ChasRingMemberSlot_Type(Integer32):
    """Custom type chasRingMemberSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ChasRingMemberSlot_Type.__name__ = "Integer32"
_ChasRingMemberSlot_Object = MibTableColumn
chasRingMemberSlot = _ChasRingMemberSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 14, 2, 1, 1),
    _ChasRingMemberSlot_Type()
)
chasRingMemberSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasRingMemberSlot.setStatus("mandatory")


class _ChasRingMemberSegment_Type(Integer32):
    """Custom type chasRingMemberSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChasRingMemberSegment_Type.__name__ = "Integer32"
_ChasRingMemberSegment_Object = MibTableColumn
chasRingMemberSegment = _ChasRingMemberSegment_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 14, 2, 1, 2),
    _ChasRingMemberSegment_Type()
)
chasRingMemberSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasRingMemberSegment.setStatus("mandatory")


class _ChasRingMemberStatus_Type(Integer32):
    """Custom type chasRingMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_ChasRingMemberStatus_Type.__name__ = "Integer32"
_ChasRingMemberStatus_Object = MibTableColumn
chasRingMemberStatus = _ChasRingMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 14, 2, 1, 3),
    _ChasRingMemberStatus_Type()
)
chasRingMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasRingMemberStatus.setStatus("mandatory")


class _ChasRingMemberSegmentMask_Type(OctetString):
    """Custom type chasRingMemberSegmentMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ChasRingMemberSegmentMask_Type.__name__ = "OctetString"
_ChasRingMemberSegmentMask_Object = MibTableColumn
chasRingMemberSegmentMask = _ChasRingMemberSegmentMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 1, 1, 14, 2, 1, 4),
    _ChasRingMemberSegmentMask_Type()
)
chasRingMemberSegmentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasRingMemberSegmentMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECHUB900-CHASSIS-MIB-V3-0",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decHub900": decHub900,
       "mgmtAgent": mgmtAgent,
       "mgmtAgentVersion1": mgmtAgentVersion1,
       "chassis": chassis,
       "chasSlot": chasSlot,
       "chasNumSlots": chasNumSlots,
       "chasNumSlotsOccupied": chasNumSlotsOccupied,
       "chasMaxExtendedSlots": chasMaxExtendedSlots,
       "chasExtendedSlotsOccupied": chasExtendedSlotsOccupied,
       "chasPopulationChanges": chasPopulationChanges,
       "chasSlotTable": chasSlotTable,
       "chasSlotEntry": chasSlotEntry,
       "chasSlotIndex": chasSlotIndex,
       "chasSlotModuleType": chasSlotModuleType,
       "chasSlotLastChange": chasSlotLastChange,
       "chasSlotModuleDescr": chasSlotModuleDescr,
       "chasSlotModuleVersion": chasSlotModuleVersion,
       "chasSlotModuleSerialNumber": chasSlotModuleSerialNumber,
       "chasSlotModuleSize": chasSlotModuleSize,
       "chasSlotModuleOperStatus": chasSlotModuleOperStatus,
       "chasSlotModuleAdminStatus": chasSlotModuleAdminStatus,
       "chasSlotModuleNonFatalError": chasSlotModuleNonFatalError,
       "chasSlotResetAll": chasSlotResetAll,
       "chasEntity": chasEntity,
       "chasEntityChanges": chasEntityChanges,
       "chasEntityTable": chasEntityTable,
       "chasEntityEntry": chasEntityEntry,
       "chasEntityIndex": chasEntityIndex,
       "chasEntityFunction": chasEntityFunction,
       "chasEntityObjectID": chasEntityObjectID,
       "chasEntityDescr": chasEntityDescr,
       "chasEntityVersion": chasEntityVersion,
       "chasEntityAdminStatus": chasEntityAdminStatus,
       "chasEntityOperStatus": chasEntityOperStatus,
       "chasEntityTimeStamp": chasEntityTimeStamp,
       "chasEntityParty": chasEntityParty,
       "chasEntityCommunity": chasEntityCommunity,
       "chasEntityIpAddress": chasEntityIpAddress,
       "chasEntityComAccessRights": chasEntityComAccessRights,
       "chasEntityAccessMethod": chasEntityAccessMethod,
       "chasEntitySlotNumber": chasEntitySlotNumber,
       "chasEntitySrcIpAddress": chasEntitySrcIpAddress,
       "chasEntitySrcSubnetMask": chasEntitySrcSubnetMask,
       "chasEntityAccessCharacteristics": chasEntityAccessCharacteristics,
       "chasEntityAccessLoadTable": chasEntityAccessLoadTable,
       "chasEntityAccessLoadEntry": chasEntityAccessLoadEntry,
       "chasEntityAccessLoadSlot": chasEntityAccessLoadSlot,
       "chasEntityAccessLoadMethod": chasEntityAccessLoadMethod,
       "chasEntityChangeTable": chasEntityChangeTable,
       "chasEntityChangeEntry": chasEntityChangeEntry,
       "chasEntityChangeSlot": chasEntityChangeSlot,
       "chasEntityChangeCounter": chasEntityChangeCounter,
       "chasBackplane": chasBackplane,
       "chasBackplaneTable": chasBackplaneTable,
       "chasBackplaneEntry": chasBackplaneEntry,
       "chasBackplaneIndex": chasBackplaneIndex,
       "chasBackplaneDescr": chasBackplaneDescr,
       "chasBackplaneRev": chasBackplaneRev,
       "chasBackplaneNumSlots": chasBackplaneNumSlots,
       "chasSegment": chasSegment,
       "chasSegmentTable": chasSegmentTable,
       "chasSegmentEntry": chasSegmentEntry,
       "chasSegmentIndex": chasSegmentIndex,
       "chasSegmentName": chasSegmentName,
       "chasSegmentType": chasSegmentType,
       "chasSegmentSubtypeSelect": chasSegmentSubtypeSelect,
       "chasSegmentEntryStatus": chasSegmentEntryStatus,
       "chasSegSubtypeTable": chasSegSubtypeTable,
       "chasSegSubtypeEntry": chasSegSubtypeEntry,
       "chasSegSubtypeIndex": chasSegSubtypeIndex,
       "chasSegSubtypeFlavor": chasSegSubtypeFlavor,
       "chasSegSubtypeSpeed": chasSegSubtypeSpeed,
       "chasSegSubtypeEntryStatus": chasSegSubtypeEntryStatus,
       "chasSegDefVNbusState": chasSegDefVNbusState,
       "chasConfig": chasConfig,
       "chasChassisSerialNumber": chasChassisSerialNumber,
       "chasConnChanges": chasConnChanges,
       "chasConnTable": chasConnTable,
       "chasConnEntry": chasConnEntry,
       "chasConnIndex": chasConnIndex,
       "chasConnSegment": chasConnSegment,
       "chasConnPort": chasConnPort,
       "chasConnNextPortIndex": chasConnNextPortIndex,
       "chasConnEntryStatus": chasConnEntryStatus,
       "chasPort": chasPort,
       "chasPortLastChange": chasPortLastChange,
       "chasPortTable": chasPortTable,
       "chasPortEntry": chasPortEntry,
       "chasPortIndex": chasPortIndex,
       "chasPortSlot": chasPortSlot,
       "chasPortName": chasPortName,
       "chasPortType": chasPortType,
       "chasPortSubtypeSelect": chasPortSubtypeSelect,
       "chasPortOperStatus": chasPortOperStatus,
       "chasPortDescrTable": chasPortDescrTable,
       "chasPortDescrEntry": chasPortDescrEntry,
       "chasPortDescrIndex": chasPortDescrIndex,
       "chasPortDescr": chasPortDescr,
       "chasPortSubtypeTable": chasPortSubtypeTable,
       "chasPortSubtypeEntry": chasPortSubtypeEntry,
       "chasPortSubtypeIndex": chasPortSubtypeIndex,
       "chasPortSubtypePortIndex": chasPortSubtypePortIndex,
       "chasPortSubtypeFlavor": chasPortSubtypeFlavor,
       "chasPortSubtypeSpeed": chasPortSubtypeSpeed,
       "chasPowerConfig": chasPowerConfig,
       "chasPowerConfigMaxSupplies": chasPowerConfigMaxSupplies,
       "chasPowerConfigNumSupplies": chasPowerConfigNumSupplies,
       "chasPowerConfigChanges": chasPowerConfigChanges,
       "chasPowerConfigRedundancyState": chasPowerConfigRedundancyState,
       "chasPowerConfigTable": chasPowerConfigTable,
       "chasPowerConfigEntry": chasPowerConfigEntry,
       "chasPowerConfigIndex": chasPowerConfigIndex,
       "chasPowerConfigDescr": chasPowerConfigDescr,
       "chasPowerConfigAdminStatus": chasPowerConfigAdminStatus,
       "chasPowerConfigOperStatus": chasPowerConfigOperStatus,
       "chasPowerConfigHealthText": chasPowerConfigHealthText,
       "chasPowerConfigWarnings": chasPowerConfigWarnings,
       "chasPowerConfigFailures": chasPowerConfigFailures,
       "chasPowerSource": chasPowerSource,
       "chasPowerSourceTotalPowerAvailable": chasPowerSourceTotalPowerAvailable,
       "chasPowerSourceTotalCurrentAvailable": chasPowerSourceTotalCurrentAvailable,
       "chasPowerSourceTable": chasPowerSourceTable,
       "chasPowerSourceEntry": chasPowerSourceEntry,
       "chasPowerSourceSupplyIndex": chasPowerSourceSupplyIndex,
       "chasPowerSourceIndex": chasPowerSourceIndex,
       "chasPowerSourceNominalVoltage": chasPowerSourceNominalVoltage,
       "chasPowerSourcePower": chasPowerSourcePower,
       "chasPowerSink": chasPowerSink,
       "chasPowerSinkTable": chasPowerSinkTable,
       "chasPowerSinkEntry": chasPowerSinkEntry,
       "chasPowerSinkSlotIndex": chasPowerSinkSlotIndex,
       "chasPowerSinkIndex": chasPowerSinkIndex,
       "chasPowerSinkVoltage": chasPowerSinkVoltage,
       "chasPowerSinkWattage": chasPowerSinkWattage,
       "chasPowerSinkOperStatus": chasPowerSinkOperStatus,
       "chasEnviron": chasEnviron,
       "chasEnvironChanges": chasEnvironChanges,
       "chasEnvironTable": chasEnvironTable,
       "chasEnvironEntry": chasEnvironEntry,
       "chasEnvironSlotIndex": chasEnvironSlotIndex,
       "chasEnvironSensorIndex": chasEnvironSensorIndex,
       "chasEnvironSensor": chasEnvironSensor,
       "chasEnvironAdminStatus": chasEnvironAdminStatus,
       "chasEnvironOperStatus": chasEnvironOperStatus,
       "chasEnvironWarnings": chasEnvironWarnings,
       "chasEnvironFailures": chasEnvironFailures,
       "chasLoad": chasLoad,
       "chasLoadTable": chasLoadTable,
       "chasLoadEntry": chasLoadEntry,
       "chasLoadSlotIndex": chasLoadSlotIndex,
       "chasLoadAdminStatus": chasLoadAdminStatus,
       "chasLoadOperStatus": chasLoadOperStatus,
       "chasLoadFileName": chasLoadFileName,
       "chasLoadIpHostAddr": chasLoadIpHostAddr,
       "chasLoadDevSpecific": chasLoadDevSpecific,
       "chasLoadEntryStatus": chasLoadEntryStatus,
       "chasLigo": chasLigo,
       "chasLigoNumEntries": chasLigoNumEntries,
       "chasLigoTable": chasLigoTable,
       "chasLigoEntry": chasLigoEntry,
       "chasLigoIndex": chasLigoIndex,
       "chasLigoSlot": chasLigoSlot,
       "chasLigoType": chasLigoType,
       "chasLigoSubtypeSelect": chasLigoSubtypeSelect,
       "chasLigoSubtypeNumEntries": chasLigoSubtypeNumEntries,
       "chasLigoSubtypeTable": chasLigoSubtypeTable,
       "chasLigoSubtypeEntry": chasLigoSubtypeEntry,
       "chasLigoSubtypeIndex": chasLigoSubtypeIndex,
       "chasLigoSubtypeLigoIndex": chasLigoSubtypeLigoIndex,
       "chasLigoSubtypePortMask": chasLigoSubtypePortMask,
       "chasLigoSubtypeLabelIndexMask": chasLigoSubtypeLabelIndexMask,
       "chasLigoSubtypeFlavor": chasLigoSubtypeFlavor,
       "chasLigoSubtypePortMaskV2": chasLigoSubtypePortMaskV2,
       "chasLigoSubtypeLabelIndexMaskV2": chasLigoSubtypeLabelIndexMaskV2,
       "chasLigoLabelNumEntries": chasLigoLabelNumEntries,
       "chasLigoLabelTable": chasLigoLabelTable,
       "chasLigoLabelEntry": chasLigoLabelEntry,
       "chasLigoLabelIndex": chasLigoLabelIndex,
       "chasLigoLabelString": chasLigoLabelString,
       "chasPatching": chasPatching,
       "chasRingPatching": chasRingPatching,
       "chasRingMemberTable": chasRingMemberTable,
       "chasRingMemberEntry": chasRingMemberEntry,
       "chasRingMemberSlot": chasRingMemberSlot,
       "chasRingMemberSegment": chasRingMemberSegment,
       "chasRingMemberStatus": chasRingMemberStatus,
       "chasRingMemberSegmentMask": chasRingMemberSegmentMask}
)
