# SNMP MIB module (LC-PHYSICAL-ENTITIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LC-PHYSICAL-ENTITIES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:33 2024
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

(lancastMibModulesA,
 lancastTraps) = mibBuilder.importSymbols(
    "LANCAST-MIB",
    "lancastMibModulesA",
    "lancastTraps")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

physicalEntities = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2)
)
physicalEntities.setRevisions(
        ("1999-03-03 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChassisGroup_ObjectIdentity = ObjectIdentity
chassisGroup = _ChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2)
)
_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("current")
_ChassisTableEntry_Object = MibTableRow
chassisTableEntry = _ChassisTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1)
)
chassisTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "chassisEntityIndex"),
)
if mibBuilder.loadTexts:
    chassisTableEntry.setStatus("current")
_ChassisEntityIndex_Type = Integer32
_ChassisEntityIndex_Object = MibTableColumn
chassisEntityIndex = _ChassisEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 1),
    _ChassisEntityIndex_Type()
)
chassisEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisEntityIndex.setStatus("current")


class _ChassisDescription_Type(DisplayString):
    """Custom type chassisDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ChassisDescription_Type.__name__ = "DisplayString"
_ChassisDescription_Object = MibTableColumn
chassisDescription = _ChassisDescription_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 2),
    _ChassisDescription_Type()
)
chassisDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisDescription.setStatus("current")


class _ChassisPartNumber_Type(DisplayString):
    """Custom type chassisPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ChassisPartNumber_Type.__name__ = "DisplayString"
_ChassisPartNumber_Object = MibTableColumn
chassisPartNumber = _ChassisPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 3),
    _ChassisPartNumber_Type()
)
chassisPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPartNumber.setStatus("current")
_ChassisNumSlots_Type = Integer32
_ChassisNumSlots_Object = MibTableColumn
chassisNumSlots = _ChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 4),
    _ChassisNumSlots_Type()
)
chassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNumSlots.setStatus("current")
_ChassisCurrentTemp_Type = Integer32
_ChassisCurrentTemp_Object = MibTableColumn
chassisCurrentTemp = _ChassisCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 5),
    _ChassisCurrentTemp_Type()
)
chassisCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCurrentTemp.setStatus("current")
_ChassisMaxTemp_Type = Integer32
_ChassisMaxTemp_Object = MibTableColumn
chassisMaxTemp = _ChassisMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 6),
    _ChassisMaxTemp_Type()
)
chassisMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMaxTemp.setStatus("current")


class _ChassisReset_Type(Integer32):
    """Custom type chassisReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-resetable", 3),
          ("reset", 1),
          ("resetable", 2))
    )


_ChassisReset_Type.__name__ = "Integer32"
_ChassisReset_Object = MibTableColumn
chassisReset = _ChassisReset_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 7),
    _ChassisReset_Type()
)
chassisReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisReset.setStatus("current")


class _LastEntityResetReason_Type(Integer32):
    """Custom type lastEntityResetReason based on Integer32"""
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
        *(("cold-start", 1),
          ("download-reset", 3),
          ("nms-sw-reset", 2),
          ("watch-dog-timeout", 4))
    )


_LastEntityResetReason_Type.__name__ = "Integer32"
_LastEntityResetReason_Object = MibTableColumn
lastEntityResetReason = _LastEntityResetReason_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 8),
    _LastEntityResetReason_Type()
)
lastEntityResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastEntityResetReason.setStatus("current")
_LastEntityResetIndex_Type = Integer32
_LastEntityResetIndex_Object = MibTableColumn
lastEntityResetIndex = _LastEntityResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 9),
    _LastEntityResetIndex_Type()
)
lastEntityResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastEntityResetIndex.setStatus("current")


class _LastEntityResetTime_Type(DisplayString):
    """Custom type lastEntityResetTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LastEntityResetTime_Type.__name__ = "DisplayString"
_LastEntityResetTime_Object = MibTableColumn
lastEntityResetTime = _LastEntityResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 10),
    _LastEntityResetTime_Type()
)
lastEntityResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastEntityResetTime.setStatus("current")


class _LastEntityResetType_Type(Integer32):
    """Custom type lastEntityResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 3),
          ("module", 9),
          ("port", 10))
    )


_LastEntityResetType_Type.__name__ = "Integer32"
_LastEntityResetType_Object = MibTableColumn
lastEntityResetType = _LastEntityResetType_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 2, 1, 1, 11),
    _LastEntityResetType_Type()
)
lastEntityResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastEntityResetType.setStatus("current")
_BackPlaneGroup_ObjectIdentity = ObjectIdentity
backPlaneGroup = _BackPlaneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3)
)
_BackPlaneTable_Object = MibTable
backPlaneTable = _BackPlaneTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    backPlaneTable.setStatus("current")
_BackPlaneTableEntry_Object = MibTableRow
backPlaneTableEntry = _BackPlaneTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3, 1, 1)
)
backPlaneTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "backPlaneEntityIndex"),
)
if mibBuilder.loadTexts:
    backPlaneTableEntry.setStatus("current")
_BackPlaneEntityIndex_Type = Integer32
_BackPlaneEntityIndex_Object = MibTableColumn
backPlaneEntityIndex = _BackPlaneEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3, 1, 1, 1),
    _BackPlaneEntityIndex_Type()
)
backPlaneEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneEntityIndex.setStatus("current")


class _BackPlaneDescription_Type(DisplayString):
    """Custom type backPlaneDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BackPlaneDescription_Type.__name__ = "DisplayString"
_BackPlaneDescription_Object = MibTableColumn
backPlaneDescription = _BackPlaneDescription_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3, 1, 1, 2),
    _BackPlaneDescription_Type()
)
backPlaneDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneDescription.setStatus("current")


class _BackPlanePartNumber_Type(DisplayString):
    """Custom type backPlanePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BackPlanePartNumber_Type.__name__ = "DisplayString"
_BackPlanePartNumber_Object = MibTableColumn
backPlanePartNumber = _BackPlanePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3, 1, 1, 3),
    _BackPlanePartNumber_Type()
)
backPlanePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlanePartNumber.setStatus("current")


class _BackPlaneSerialNumber_Type(DisplayString):
    """Custom type backPlaneSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BackPlaneSerialNumber_Type.__name__ = "DisplayString"
_BackPlaneSerialNumber_Object = MibTableColumn
backPlaneSerialNumber = _BackPlaneSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3, 1, 1, 4),
    _BackPlaneSerialNumber_Type()
)
backPlaneSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneSerialNumber.setStatus("current")


class _BackPlaneManufactureDate_Type(DisplayString):
    """Custom type backPlaneManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BackPlaneManufactureDate_Type.__name__ = "DisplayString"
_BackPlaneManufactureDate_Object = MibTableColumn
backPlaneManufactureDate = _BackPlaneManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3, 1, 1, 5),
    _BackPlaneManufactureDate_Type()
)
backPlaneManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneManufactureDate.setStatus("current")


class _BackPlaneHWRevisionNumber_Type(DisplayString):
    """Custom type backPlaneHWRevisionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BackPlaneHWRevisionNumber_Type.__name__ = "DisplayString"
_BackPlaneHWRevisionNumber_Object = MibTableColumn
backPlaneHWRevisionNumber = _BackPlaneHWRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 3, 1, 1, 6),
    _BackPlaneHWRevisionNumber_Type()
)
backPlaneHWRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneHWRevisionNumber.setStatus("current")
_PowerSupplyGroup_ObjectIdentity = ObjectIdentity
powerSupplyGroup = _PowerSupplyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4)
)
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("current")
_PowerSupplyTableEntry_Object = MibTableRow
powerSupplyTableEntry = _PowerSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1, 1)
)
powerSupplyTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "powerSupplyEntityIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyTableEntry.setStatus("current")
_PowerSupplyEntityIndex_Type = Integer32
_PowerSupplyEntityIndex_Object = MibTableColumn
powerSupplyEntityIndex = _PowerSupplyEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1, 1, 1),
    _PowerSupplyEntityIndex_Type()
)
powerSupplyEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyEntityIndex.setStatus("current")


class _PowerSupplyStatus_Type(Integer32):
    """Custom type powerSupplyStatus based on Integer32"""
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


_PowerSupplyStatus_Type.__name__ = "Integer32"
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1, 1, 2),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("current")


class _PowerSupplyType_Type(Integer32):
    """Custom type powerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("universal", 3))
    )


_PowerSupplyType_Type.__name__ = "Integer32"
_PowerSupplyType_Object = MibTableColumn
powerSupplyType = _PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1, 1, 3),
    _PowerSupplyType_Type()
)
powerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyType.setStatus("current")
_PowerSupply5vCurrent_Type = Integer32
_PowerSupply5vCurrent_Object = MibTableColumn
powerSupply5vCurrent = _PowerSupply5vCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1, 1, 4),
    _PowerSupply5vCurrent_Type()
)
powerSupply5vCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply5vCurrent.setStatus("current")
_PowerSupply5vMin_Type = Integer32
_PowerSupply5vMin_Object = MibTableColumn
powerSupply5vMin = _PowerSupply5vMin_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1, 1, 5),
    _PowerSupply5vMin_Type()
)
powerSupply5vMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply5vMin.setStatus("current")
_PowerSupply5vMax_Type = Integer32
_PowerSupply5vMax_Object = MibTableColumn
powerSupply5vMax = _PowerSupply5vMax_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1, 1, 6),
    _PowerSupply5vMax_Type()
)
powerSupply5vMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply5vMax.setStatus("current")


class _PowerSupplyUnitIdentifier_Type(Integer32):
    """Custom type powerSupplyUnitIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ps-A", 1),
          ("ps-B", 2))
    )


_PowerSupplyUnitIdentifier_Type.__name__ = "Integer32"
_PowerSupplyUnitIdentifier_Object = MibTableColumn
powerSupplyUnitIdentifier = _PowerSupplyUnitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 4, 1, 1, 7),
    _PowerSupplyUnitIdentifier_Type()
)
powerSupplyUnitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyUnitIdentifier.setStatus("current")
_ModulesGroup_ObjectIdentity = ObjectIdentity
modulesGroup = _ModulesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleTableEntry_Object = MibTableRow
moduleTableEntry = _ModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1)
)
moduleTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "modEntityIndex"),
)
if mibBuilder.loadTexts:
    moduleTableEntry.setStatus("current")
_ModEntityIndex_Type = Integer32
_ModEntityIndex_Object = MibTableColumn
modEntityIndex = _ModEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 1),
    _ModEntityIndex_Type()
)
modEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modEntityIndex.setStatus("current")


class _ModAdminState_Type(Integer32):
    """Custom type modAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("not-applicable", 0),
          ("up", 1))
    )


_ModAdminState_Type.__name__ = "Integer32"
_ModAdminState_Object = MibTableColumn
modAdminState = _ModAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 2),
    _ModAdminState_Type()
)
modAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modAdminState.setStatus("current")


class _ModOperStatus_Type(Integer32):
    """Custom type modOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ModOperStatus_Type.__name__ = "Integer32"
_ModOperStatus_Object = MibTableColumn
modOperStatus = _ModOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 3),
    _ModOperStatus_Type()
)
modOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modOperStatus.setStatus("current")


class _ModType_Type(Integer32):
    """Custom type modType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("displayModule", 7),
          ("dualTwister", 5),
          ("fixedPort", 9),
          ("gigabitTwister", 11),
          ("mgmnt", 3),
          ("rateAdapter", 10),
          ("redundantTwister", 6),
          ("reserved", 2),
          ("singleTwister", 4),
          ("singleTwister2", 8),
          ("unknown", 1))
    )


_ModType_Type.__name__ = "Integer32"
_ModType_Object = MibTableColumn
modType = _ModType_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 4),
    _ModType_Type()
)
modType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modType.setStatus("current")


class _ModDescription_Type(DisplayString):
    """Custom type modDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ModDescription_Type.__name__ = "DisplayString"
_ModDescription_Object = MibTableColumn
modDescription = _ModDescription_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 5),
    _ModDescription_Type()
)
modDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modDescription.setStatus("current")


class _ModName_Type(DisplayString):
    """Custom type modName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ModName_Type.__name__ = "DisplayString"
_ModName_Object = MibTableColumn
modName = _ModName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 6),
    _ModName_Type()
)
modName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modName.setStatus("current")


class _ModPartNumber_Type(DisplayString):
    """Custom type modPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ModPartNumber_Type.__name__ = "DisplayString"
_ModPartNumber_Object = MibTableColumn
modPartNumber = _ModPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 7),
    _ModPartNumber_Type()
)
modPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modPartNumber.setStatus("current")


class _ModSerialNumber_Type(DisplayString):
    """Custom type modSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ModSerialNumber_Type.__name__ = "DisplayString"
_ModSerialNumber_Object = MibTableColumn
modSerialNumber = _ModSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 8),
    _ModSerialNumber_Type()
)
modSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modSerialNumber.setStatus("current")


class _ModManufactureDate_Type(DisplayString):
    """Custom type modManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ModManufactureDate_Type.__name__ = "DisplayString"
_ModManufactureDate_Object = MibTableColumn
modManufactureDate = _ModManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 9),
    _ModManufactureDate_Type()
)
modManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modManufactureDate.setStatus("current")


class _ModDiagnosticTestStatus_Type(DisplayString):
    """Custom type modDiagnosticTestStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ModDiagnosticTestStatus_Type.__name__ = "DisplayString"
_ModDiagnosticTestStatus_Object = MibTableColumn
modDiagnosticTestStatus = _ModDiagnosticTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 10),
    _ModDiagnosticTestStatus_Type()
)
modDiagnosticTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modDiagnosticTestStatus.setStatus("current")


class _ModHWRevisionNumber_Type(DisplayString):
    """Custom type modHWRevisionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ModHWRevisionNumber_Type.__name__ = "DisplayString"
_ModHWRevisionNumber_Object = MibTableColumn
modHWRevisionNumber = _ModHWRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 11),
    _ModHWRevisionNumber_Type()
)
modHWRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modHWRevisionNumber.setStatus("current")
_ModNumPorts_Type = Integer32
_ModNumPorts_Object = MibTableColumn
modNumPorts = _ModNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 12),
    _ModNumPorts_Type()
)
modNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modNumPorts.setStatus("current")
_ModFirstSlot_Type = Integer32
_ModFirstSlot_Object = MibTableColumn
modFirstSlot = _ModFirstSlot_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 13),
    _ModFirstSlot_Type()
)
modFirstSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFirstSlot.setStatus("current")
_ModNumSlotsOccupied_Type = Integer32
_ModNumSlotsOccupied_Object = MibTableColumn
modNumSlotsOccupied = _ModNumSlotsOccupied_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 14),
    _ModNumSlotsOccupied_Type()
)
modNumSlotsOccupied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modNumSlotsOccupied.setStatus("current")


class _ModReset_Type(Integer32):
    """Custom type modReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-resetable", 3),
          ("reset", 1),
          ("resetable", 2))
    )


_ModReset_Type.__name__ = "Integer32"
_ModReset_Object = MibTableColumn
modReset = _ModReset_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 1, 1, 15),
    _ModReset_Type()
)
modReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modReset.setStatus("current")
_MgmntTable_Object = MibTable
mgmntTable = _MgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    mgmntTable.setStatus("current")
_MgmntTableEntry_Object = MibTableRow
mgmntTableEntry = _MgmntTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1)
)
mgmntTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "mgmntEntityIndex"),
)
if mibBuilder.loadTexts:
    mgmntTableEntry.setStatus("current")
_MgmntEntityIndex_Type = Integer32
_MgmntEntityIndex_Object = MibTableColumn
mgmntEntityIndex = _MgmntEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 1),
    _MgmntEntityIndex_Type()
)
mgmntEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntEntityIndex.setStatus("current")


class _MgmntBootImageName_Type(DisplayString):
    """Custom type mgmntBootImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgmntBootImageName_Type.__name__ = "DisplayString"
_MgmntBootImageName_Object = MibTableColumn
mgmntBootImageName = _MgmntBootImageName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 2),
    _MgmntBootImageName_Type()
)
mgmntBootImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntBootImageName.setStatus("current")


class _MgmntBootImageVersion_Type(DisplayString):
    """Custom type mgmntBootImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgmntBootImageVersion_Type.__name__ = "DisplayString"
_MgmntBootImageVersion_Object = MibTableColumn
mgmntBootImageVersion = _MgmntBootImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 3),
    _MgmntBootImageVersion_Type()
)
mgmntBootImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntBootImageVersion.setStatus("current")


class _MgmntCoreImageName_Type(DisplayString):
    """Custom type mgmntCoreImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgmntCoreImageName_Type.__name__ = "DisplayString"
_MgmntCoreImageName_Object = MibTableColumn
mgmntCoreImageName = _MgmntCoreImageName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 4),
    _MgmntCoreImageName_Type()
)
mgmntCoreImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntCoreImageName.setStatus("current")


class _MgmntCoreImageVersion_Type(DisplayString):
    """Custom type mgmntCoreImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgmntCoreImageVersion_Type.__name__ = "DisplayString"
_MgmntCoreImageVersion_Object = MibTableColumn
mgmntCoreImageVersion = _MgmntCoreImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 5),
    _MgmntCoreImageVersion_Type()
)
mgmntCoreImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntCoreImageVersion.setStatus("current")


class _MgmntAppImageName_Type(DisplayString):
    """Custom type mgmntAppImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgmntAppImageName_Type.__name__ = "DisplayString"
_MgmntAppImageName_Object = MibTableColumn
mgmntAppImageName = _MgmntAppImageName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 6),
    _MgmntAppImageName_Type()
)
mgmntAppImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntAppImageName.setStatus("current")


class _MgmntAppImageVersion_Type(DisplayString):
    """Custom type mgmntAppImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MgmntAppImageVersion_Type.__name__ = "DisplayString"
_MgmntAppImageVersion_Object = MibTableColumn
mgmntAppImageVersion = _MgmntAppImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 7),
    _MgmntAppImageVersion_Type()
)
mgmntAppImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntAppImageVersion.setStatus("current")
_MgmntRamMemorySize_Type = Integer32
_MgmntRamMemorySize_Object = MibTableColumn
mgmntRamMemorySize = _MgmntRamMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 8),
    _MgmntRamMemorySize_Type()
)
mgmntRamMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntRamMemorySize.setStatus("current")
_MgmntFlashMemorySize_Type = Integer32
_MgmntFlashMemorySize_Object = MibTableColumn
mgmntFlashMemorySize = _MgmntFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 9),
    _MgmntFlashMemorySize_Type()
)
mgmntFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntFlashMemorySize.setStatus("current")
_MgmntNVRamMemorySize_Type = Integer32
_MgmntNVRamMemorySize_Object = MibTableColumn
mgmntNVRamMemorySize = _MgmntNVRamMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 10),
    _MgmntNVRamMemorySize_Type()
)
mgmntNVRamMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntNVRamMemorySize.setStatus("current")
_Mgmnt5vCurrent_Type = Integer32
_Mgmnt5vCurrent_Object = MibTableColumn
mgmnt5vCurrent = _Mgmnt5vCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 11),
    _Mgmnt5vCurrent_Type()
)
mgmnt5vCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmnt5vCurrent.setStatus("current")
_Mgmnt5vMin_Type = Integer32
_Mgmnt5vMin_Object = MibTableColumn
mgmnt5vMin = _Mgmnt5vMin_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 12),
    _Mgmnt5vMin_Type()
)
mgmnt5vMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmnt5vMin.setStatus("current")
_Mgmnt5vMax_Type = Integer32
_Mgmnt5vMax_Object = MibTableColumn
mgmnt5vMax = _Mgmnt5vMax_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 13),
    _Mgmnt5vMax_Type()
)
mgmnt5vMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmnt5vMax.setStatus("current")
_Mgmnt3pt3vCurrent_Type = Integer32
_Mgmnt3pt3vCurrent_Object = MibTableColumn
mgmnt3pt3vCurrent = _Mgmnt3pt3vCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 14),
    _Mgmnt3pt3vCurrent_Type()
)
mgmnt3pt3vCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmnt3pt3vCurrent.setStatus("current")
_Mgmnt3pt3vMin_Type = Integer32
_Mgmnt3pt3vMin_Object = MibTableColumn
mgmnt3pt3vMin = _Mgmnt3pt3vMin_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 15),
    _Mgmnt3pt3vMin_Type()
)
mgmnt3pt3vMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmnt3pt3vMin.setStatus("current")
_Mgmnt3pt3vMax_Type = Integer32
_Mgmnt3pt3vMax_Object = MibTableColumn
mgmnt3pt3vMax = _Mgmnt3pt3vMax_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 16),
    _Mgmnt3pt3vMax_Type()
)
mgmnt3pt3vMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmnt3pt3vMax.setStatus("current")


class _MgmntDiagnosticBootError_Type(Integer32):
    """Custom type mgmntDiagnosticBootError based on Integer32"""
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


_MgmntDiagnosticBootError_Type.__name__ = "Integer32"
_MgmntDiagnosticBootError_Object = MibTableColumn
mgmntDiagnosticBootError = _MgmntDiagnosticBootError_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 2, 1, 17),
    _MgmntDiagnosticBootError_Type()
)
mgmntDiagnosticBootError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmntDiagnosticBootError.setStatus("current")
_SingleTwisterTable_Object = MibTable
singleTwisterTable = _SingleTwisterTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    singleTwisterTable.setStatus("current")
_SingleTwisterTableEntry_Object = MibTableRow
singleTwisterTableEntry = _SingleTwisterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 3, 1)
)
singleTwisterTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "stwEntityIndex"),
)
if mibBuilder.loadTexts:
    singleTwisterTableEntry.setStatus("current")
_StwEntityIndex_Type = Integer32
_StwEntityIndex_Object = MibTableColumn
stwEntityIndex = _StwEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 3, 1, 1),
    _StwEntityIndex_Type()
)
stwEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stwEntityIndex.setStatus("current")


class _StwLinkLossCarryForward_Type(Integer32):
    """Custom type stwLinkLossCarryForward based on Integer32"""
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


_StwLinkLossCarryForward_Type.__name__ = "Integer32"
_StwLinkLossCarryForward_Object = MibTableColumn
stwLinkLossCarryForward = _StwLinkLossCarryForward_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 3, 1, 2),
    _StwLinkLossCarryForward_Type()
)
stwLinkLossCarryForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stwLinkLossCarryForward.setStatus("current")
_DualTwisterTable_Object = MibTable
dualTwisterTable = _DualTwisterTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    dualTwisterTable.setStatus("current")
_DualTwisterTableEntry_Object = MibTableRow
dualTwisterTableEntry = _DualTwisterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 4, 1)
)
dualTwisterTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "stwEntityIndex"),
)
if mibBuilder.loadTexts:
    dualTwisterTableEntry.setStatus("current")
_DtwEntityIndex_Type = Integer32
_DtwEntityIndex_Object = MibTableColumn
dtwEntityIndex = _DtwEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 4, 1, 1),
    _DtwEntityIndex_Type()
)
dtwEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtwEntityIndex.setStatus("current")


class _DtwLinkLossCarryForward_Type(Integer32):
    """Custom type dtwLinkLossCarryForward based on Integer32"""
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


_DtwLinkLossCarryForward_Type.__name__ = "Integer32"
_DtwLinkLossCarryForward_Object = MibTableColumn
dtwLinkLossCarryForward = _DtwLinkLossCarryForward_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 4, 1, 2),
    _DtwLinkLossCarryForward_Type()
)
dtwLinkLossCarryForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtwLinkLossCarryForward.setStatus("current")
_RedundantTwisterTable_Object = MibTable
redundantTwisterTable = _RedundantTwisterTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    redundantTwisterTable.setStatus("current")
_RedundantTwisterTableEntry_Object = MibTableRow
redundantTwisterTableEntry = _RedundantTwisterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1)
)
redundantTwisterTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "rtwEntityIndex"),
)
if mibBuilder.loadTexts:
    redundantTwisterTableEntry.setStatus("current")
_RtwEntityIndex_Type = Integer32
_RtwEntityIndex_Object = MibTableColumn
rtwEntityIndex = _RtwEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 1),
    _RtwEntityIndex_Type()
)
rtwEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtwEntityIndex.setStatus("current")


class _RtwAutoRestorePrimary_Type(Integer32):
    """Custom type rtwAutoRestorePrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-selectable", 3))
    )


_RtwAutoRestorePrimary_Type.__name__ = "Integer32"
_RtwAutoRestorePrimary_Object = MibTableColumn
rtwAutoRestorePrimary = _RtwAutoRestorePrimary_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 2),
    _RtwAutoRestorePrimary_Type()
)
rtwAutoRestorePrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtwAutoRestorePrimary.setStatus("current")


class _RtwLinkLossCarryForward_Type(Integer32):
    """Custom type rtwLinkLossCarryForward based on Integer32"""
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


_RtwLinkLossCarryForward_Type.__name__ = "Integer32"
_RtwLinkLossCarryForward_Object = MibTableColumn
rtwLinkLossCarryForward = _RtwLinkLossCarryForward_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 3),
    _RtwLinkLossCarryForward_Type()
)
rtwLinkLossCarryForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtwLinkLossCarryForward.setStatus("current")


class _RtwActivePort_Type(Integer32):
    """Custom type rtwActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_RtwActivePort_Type.__name__ = "Integer32"
_RtwActivePort_Object = MibTableColumn
rtwActivePort = _RtwActivePort_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 4),
    _RtwActivePort_Type()
)
rtwActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtwActivePort.setStatus("current")


class _RtwRedundantTransmission_Type(Integer32):
    """Custom type rtwRedundantTransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-applicable", 0))
    )


_RtwRedundantTransmission_Type.__name__ = "Integer32"
_RtwRedundantTransmission_Object = MibTableColumn
rtwRedundantTransmission = _RtwRedundantTransmission_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 5),
    _RtwRedundantTransmission_Type()
)
rtwRedundantTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtwRedundantTransmission.setStatus("current")


class _RtwSecondarySwitchOver_Type(Integer32):
    """Custom type rtwSecondarySwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_RtwSecondarySwitchOver_Type.__name__ = "Integer32"
_RtwSecondarySwitchOver_Object = MibTableColumn
rtwSecondarySwitchOver = _RtwSecondarySwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 6),
    _RtwSecondarySwitchOver_Type()
)
rtwSecondarySwitchOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtwSecondarySwitchOver.setStatus("current")


class _RtwLinkPulseControl_Type(Integer32):
    """Custom type rtwLinkPulseControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active-port", 2),
          ("both-ports", 1),
          ("not-applicable", 0))
    )


_RtwLinkPulseControl_Type.__name__ = "Integer32"
_RtwLinkPulseControl_Object = MibTableColumn
rtwLinkPulseControl = _RtwLinkPulseControl_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 7),
    _RtwLinkPulseControl_Type()
)
rtwLinkPulseControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtwLinkPulseControl.setStatus("current")


class _RtwModeControl_Type(Integer32):
    """Custom type rtwModeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundant", 1),
          ("selectAB", 2))
    )


_RtwModeControl_Type.__name__ = "Integer32"
_RtwModeControl_Object = MibTableColumn
rtwModeControl = _RtwModeControl_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 8),
    _RtwModeControl_Type()
)
rtwModeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtwModeControl.setStatus("current")


class _RtwABSelect_Type(Integer32):
    """Custom type rtwABSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-selectable", 3),
          ("selectA", 1),
          ("selectB", 2))
    )


_RtwABSelect_Type.__name__ = "Integer32"
_RtwABSelect_Object = MibTableColumn
rtwABSelect = _RtwABSelect_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 5, 5, 1, 9),
    _RtwABSelect_Type()
)
rtwABSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtwABSelect.setStatus("current")
_EPortGroup_ObjectIdentity = ObjectIdentity
ePortGroup = _EPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6)
)
_EPortTable_Object = MibTable
ePortTable = _EPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ePortTable.setStatus("current")
_EPortTableEntry_Object = MibTableRow
ePortTableEntry = _EPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1)
)
ePortTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "ePortEntityIndex"),
)
if mibBuilder.loadTexts:
    ePortTableEntry.setStatus("current")
_EPortEntityIndex_Type = Integer32
_EPortEntityIndex_Object = MibTableColumn
ePortEntityIndex = _EPortEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 1),
    _EPortEntityIndex_Type()
)
ePortEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortEntityIndex.setStatus("current")
_EPortIfIndex_Type = Integer32
_EPortIfIndex_Object = MibTableColumn
ePortIfIndex = _EPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 2),
    _EPortIfIndex_Type()
)
ePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortIfIndex.setStatus("current")


class _EPortType_Type(Integer32):
    """Custom type ePortType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("e10-100Base-TX", 8),
          ("e1000Base-FX", 11),
          ("e1000Base-LX", 9),
          ("e1000Base-SX", 10),
          ("e100Base-SX", 13),
          ("e100BaseFX-MM", 6),
          ("e100BaseFX-SM", 7),
          ("e100BaseTX", 5),
          ("e10Base-SX", 12),
          ("e10BaseFL-MM", 3),
          ("e10BaseFL-SM", 4),
          ("e10BaseT", 2),
          ("other", 1))
    )


_EPortType_Type.__name__ = "Integer32"
_EPortType_Object = MibTableColumn
ePortType = _EPortType_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 3),
    _EPortType_Type()
)
ePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortType.setStatus("current")


class _EPortDescription_Type(DisplayString):
    """Custom type ePortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EPortDescription_Type.__name__ = "DisplayString"
_EPortDescription_Object = MibTableColumn
ePortDescription = _EPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 4),
    _EPortDescription_Type()
)
ePortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortDescription.setStatus("current")


class _EPortName_Type(DisplayString):
    """Custom type ePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EPortName_Type.__name__ = "DisplayString"
_EPortName_Object = MibTableColumn
ePortName = _EPortName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 5),
    _EPortName_Type()
)
ePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortName.setStatus("current")


class _EPortLinkStatus_Type(Integer32):
    """Custom type ePortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-detected", 1),
          ("no-link", 2))
    )


_EPortLinkStatus_Type.__name__ = "Integer32"
_EPortLinkStatus_Object = MibTableColumn
ePortLinkStatus = _EPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 6),
    _EPortLinkStatus_Type()
)
ePortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortLinkStatus.setStatus("current")


class _EPortAdminState_Type(Integer32):
    """Custom type ePortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-applicable", 0))
    )


_EPortAdminState_Type.__name__ = "Integer32"
_EPortAdminState_Object = MibTableColumn
ePortAdminState = _EPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 7),
    _EPortAdminState_Type()
)
ePortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortAdminState.setStatus("current")


class _EPortOperStatus_Type(Integer32):
    """Custom type ePortOperStatus based on Integer32"""
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


_EPortOperStatus_Type.__name__ = "Integer32"
_EPortOperStatus_Object = MibTableColumn
ePortOperStatus = _EPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 8),
    _EPortOperStatus_Type()
)
ePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortOperStatus.setStatus("current")


class _EPortDuplexAdmin_Type(Integer32):
    """Custom type ePortDuplexAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("not-applicable", 0))
    )


_EPortDuplexAdmin_Type.__name__ = "Integer32"
_EPortDuplexAdmin_Object = MibTableColumn
ePortDuplexAdmin = _EPortDuplexAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 9),
    _EPortDuplexAdmin_Type()
)
ePortDuplexAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortDuplexAdmin.setStatus("current")


class _EPortDuplexOper_Type(Integer32):
    """Custom type ePortDuplexOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_EPortDuplexOper_Type.__name__ = "Integer32"
_EPortDuplexOper_Object = MibTableColumn
ePortDuplexOper = _EPortDuplexOper_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 10),
    _EPortDuplexOper_Type()
)
ePortDuplexOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortDuplexOper.setStatus("current")


class _EPortSpeedAdmin_Type(Integer32):
    """Custom type ePortSpeedAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gigabit", 3),
          ("not-applicable", 0),
          ("onehundredMbit", 2),
          ("tenMbit", 1))
    )


_EPortSpeedAdmin_Type.__name__ = "Integer32"
_EPortSpeedAdmin_Object = MibTableColumn
ePortSpeedAdmin = _EPortSpeedAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 11),
    _EPortSpeedAdmin_Type()
)
ePortSpeedAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortSpeedAdmin.setStatus("current")


class _EPortSpeedOper_Type(Integer32):
    """Custom type ePortSpeedOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gigabit", 3),
          ("onehundredMbit", 2),
          ("tenMbit", 1))
    )


_EPortSpeedOper_Type.__name__ = "Integer32"
_EPortSpeedOper_Object = MibTableColumn
ePortSpeedOper = _EPortSpeedOper_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 12),
    _EPortSpeedOper_Type()
)
ePortSpeedOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortSpeedOper.setStatus("current")


class _EPortAutoNegotiationAdmin_Type(Integer32):
    """Custom type ePortAutoNegotiationAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-applicable", 0))
    )


_EPortAutoNegotiationAdmin_Type.__name__ = "Integer32"
_EPortAutoNegotiationAdmin_Object = MibTableColumn
ePortAutoNegotiationAdmin = _EPortAutoNegotiationAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 13),
    _EPortAutoNegotiationAdmin_Type()
)
ePortAutoNegotiationAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortAutoNegotiationAdmin.setStatus("current")


class _EPortAutoNegotiationOper_Type(Integer32):
    """Custom type ePortAutoNegotiationOper based on Integer32"""
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


_EPortAutoNegotiationOper_Type.__name__ = "Integer32"
_EPortAutoNegotiationOper_Object = MibTableColumn
ePortAutoNegotiationOper = _EPortAutoNegotiationOper_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 14),
    _EPortAutoNegotiationOper_Type()
)
ePortAutoNegotiationOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortAutoNegotiationOper.setStatus("current")


class _EPortReset_Type(Integer32):
    """Custom type ePortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-resetable", 3),
          ("reset", 1),
          ("resetable", 2))
    )


_EPortReset_Type.__name__ = "Integer32"
_EPortReset_Object = MibTableColumn
ePortReset = _EPortReset_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 15),
    _EPortReset_Type()
)
ePortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortReset.setStatus("current")


class _EPortActivity_Type(Integer32):
    """Custom type ePortActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_EPortActivity_Type.__name__ = "Integer32"
_EPortActivity_Object = MibTableColumn
ePortActivity = _EPortActivity_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 16),
    _EPortActivity_Type()
)
ePortActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortActivity.setStatus("current")


class _EPortConnector_Type(Integer32):
    """Custom type ePortConnector based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 5),
          ("mt-rj", 9),
          ("other", 1),
          ("rj11", 2),
          ("rj21", 3),
          ("rj45", 4),
          ("sc", 6),
          ("sma", 8),
          ("st", 7),
          ("vf-45", 10))
    )


_EPortConnector_Type.__name__ = "Integer32"
_EPortConnector_Object = MibTableColumn
ePortConnector = _EPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 17),
    _EPortConnector_Type()
)
ePortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortConnector.setStatus("current")
_EPortParentRelPos_Type = Integer32
_EPortParentRelPos_Object = MibTableColumn
ePortParentRelPos = _EPortParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 6, 1, 1, 18),
    _EPortParentRelPos_Type()
)
ePortParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortParentRelPos.setStatus("current")
_SerialPortGroup_ObjectIdentity = ObjectIdentity
serialPortGroup = _SerialPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7)
)
_SerialPortTable_Object = MibTable
serialPortTable = _SerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    serialPortTable.setStatus("current")
_SerialPortTableEntry_Object = MibTableRow
serialPortTableEntry = _SerialPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1)
)
serialPortTableEntry.setIndexNames(
    (0, "LC-PHYSICAL-ENTITIES-MIB", "serialPortEntityIndex"),
)
if mibBuilder.loadTexts:
    serialPortTableEntry.setStatus("current")
_SerialPortEntityIndex_Type = Integer32
_SerialPortEntityIndex_Object = MibTableColumn
serialPortEntityIndex = _SerialPortEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 1),
    _SerialPortEntityIndex_Type()
)
serialPortEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortEntityIndex.setStatus("current")


class _SerialPortDescription_Type(DisplayString):
    """Custom type serialPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SerialPortDescription_Type.__name__ = "DisplayString"
_SerialPortDescription_Object = MibTableColumn
serialPortDescription = _SerialPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 2),
    _SerialPortDescription_Type()
)
serialPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortDescription.setStatus("current")


class _SerialPortName_Type(DisplayString):
    """Custom type serialPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SerialPortName_Type.__name__ = "DisplayString"
_SerialPortName_Object = MibTableColumn
serialPortName = _SerialPortName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 3),
    _SerialPortName_Type()
)
serialPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortName.setStatus("current")


class _SerialPortSpeed_Type(Integer32):
    """Custom type serialPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9600,
              19200,
              38400)
        )
    )
    namedValues = NamedValues(
        *(("baud-19200", 19200),
          ("baud-38400", 38400),
          ("baud-9600", 9600))
    )


_SerialPortSpeed_Type.__name__ = "Integer32"
_SerialPortSpeed_Object = MibTableColumn
serialPortSpeed = _SerialPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 4),
    _SerialPortSpeed_Type()
)
serialPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortSpeed.setStatus("current")


class _SerialPortDataBits_Type(Integer32):
    """Custom type serialPortDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("seven", 7),
          ("six", 6))
    )


_SerialPortDataBits_Type.__name__ = "Integer32"
_SerialPortDataBits_Object = MibTableColumn
serialPortDataBits = _SerialPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 5),
    _SerialPortDataBits_Type()
)
serialPortDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortDataBits.setStatus("current")


class _SerialPortParity_Type(Integer32):
    """Custom type serialPortParity based on Integer32"""
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
        *(("even", 2),
          ("mark", 4),
          ("none", 1),
          ("odd", 3),
          ("space", 5))
    )


_SerialPortParity_Type.__name__ = "Integer32"
_SerialPortParity_Object = MibTableColumn
serialPortParity = _SerialPortParity_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 6),
    _SerialPortParity_Type()
)
serialPortParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortParity.setStatus("current")


class _SerialPortStopBits_Type(Integer32):
    """Custom type serialPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("one-five", 2),
          ("two", 3))
    )


_SerialPortStopBits_Type.__name__ = "Integer32"
_SerialPortStopBits_Object = MibTableColumn
serialPortStopBits = _SerialPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 7),
    _SerialPortStopBits_Type()
)
serialPortStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortStopBits.setStatus("current")


class _SerialPortFlowControl_Type(Integer32):
    """Custom type serialPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 3),
          ("none", 1),
          ("xon-xoff", 2))
    )


_SerialPortFlowControl_Type.__name__ = "Integer32"
_SerialPortFlowControl_Object = MibTableColumn
serialPortFlowControl = _SerialPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 8),
    _SerialPortFlowControl_Type()
)
serialPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortFlowControl.setStatus("current")


class _SerialPortConnector_Type(Integer32):
    """Custom type serialPortConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("db25", 2),
          ("db9", 1),
          ("rj45", 3))
    )


_SerialPortConnector_Type.__name__ = "Integer32"
_SerialPortConnector_Object = MibTableColumn
serialPortConnector = _SerialPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 2, 7, 1, 1, 9),
    _SerialPortConnector_Type()
)
serialPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortConnector.setStatus("current")

# Managed Objects groups


# Notification objects

tempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 11)
)
tempStatusChange.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "chassisEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "chassisCurrentTemp"),
        ("LC-PHYSICAL-ENTITIES-MIB", "chassisMaxTemp"))
)
if mibBuilder.loadTexts:
    tempStatusChange.setStatus(
        "current"
    )

backPlaneFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 12)
)
backPlaneFailure.setObjects(
    ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot")
)
if mibBuilder.loadTexts:
    backPlaneFailure.setStatus(
        "current"
    )

powerSupply5vChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 13)
)
powerSupply5vChange.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupply5vCurrent"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupply5vMin"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupply5vMax"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyUnitIdentifier"))
)
if mibBuilder.loadTexts:
    powerSupply5vChange.setStatus(
        "current"
    )

powerSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 14)
)
powerSupplyStatusChange.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyStatus"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyUnitIdentifier"))
)
if mibBuilder.loadTexts:
    powerSupplyStatusChange.setStatus(
        "current"
    )

powerSupplyInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 15)
)
powerSupplyInsertion.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyUnitIdentifier"))
)
if mibBuilder.loadTexts:
    powerSupplyInsertion.setStatus(
        "current"
    )

powerSupplyRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 16)
)
powerSupplyRemoval.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "powerSupplyUnitIdentifier"))
)
if mibBuilder.loadTexts:
    powerSupplyRemoval.setStatus(
        "current"
    )

chassisEntityReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 17)
)
chassisEntityReset.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetReason"),
        ("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetTime"))
)
if mibBuilder.loadTexts:
    chassisEntityReset.setStatus(
        "current"
    )

moduleEntityReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 18)
)
moduleEntityReset.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetReason"),
        ("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetTime"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modNumSlotsOccupied"))
)
if mibBuilder.loadTexts:
    moduleEntityReset.setStatus(
        "current"
    )

eportEntityReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 19)
)
eportEntityReset.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetReason"),
        ("LC-PHYSICAL-ENTITIES-MIB", "lastEntityResetTime"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modNumSlotsOccupied"),
        ("LC-PHYSICAL-ENTITIES-MIB", "ePortParentRelPos"))
)
if mibBuilder.loadTexts:
    eportEntityReset.setStatus(
        "current"
    )

moduleInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 20)
)
moduleInsertion.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "modEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modNumSlotsOccupied"))
)
if mibBuilder.loadTexts:
    moduleInsertion.setStatus(
        "current"
    )

moduleRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 21)
)
moduleRemoval.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "modEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modNumSlotsOccupied"))
)
if mibBuilder.loadTexts:
    moduleRemoval.setStatus(
        "current"
    )

unknownModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 22)
)
unknownModule.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "modEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot"))
)
if mibBuilder.loadTexts:
    unknownModule.setStatus(
        "current"
    )

moduleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 23)
)
moduleFailure.setObjects(
    ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot")
)
if mibBuilder.loadTexts:
    moduleFailure.setStatus(
        "current"
    )

ePortLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 24)
)
ePortLinkStatusChange.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "ePortEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "ePortLinkStatus"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modNumSlotsOccupied"))
)
if mibBuilder.loadTexts:
    ePortLinkStatusChange.setStatus(
        "current"
    )

ePortAdminChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 25)
)
ePortAdminChange.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "ePortEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "ePortAdminState"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modType"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modNumSlotsOccupied"))
)
if mibBuilder.loadTexts:
    ePortAdminChange.setStatus(
        "current"
    )

rtwSwitchOverChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 26)
)
rtwSwitchOverChange.setObjects(
      *(("LC-PHYSICAL-ENTITIES-MIB", "rtwEntityIndex"),
        ("LC-PHYSICAL-ENTITIES-MIB", "rtwActivePort"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modFirstSlot"),
        ("LC-PHYSICAL-ENTITIES-MIB", "modNumSlotsOccupied"))
)
if mibBuilder.loadTexts:
    rtwSwitchOverChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LC-PHYSICAL-ENTITIES-MIB",
    **{"tempStatusChange": tempStatusChange,
       "backPlaneFailure": backPlaneFailure,
       "powerSupply5vChange": powerSupply5vChange,
       "powerSupplyStatusChange": powerSupplyStatusChange,
       "powerSupplyInsertion": powerSupplyInsertion,
       "powerSupplyRemoval": powerSupplyRemoval,
       "chassisEntityReset": chassisEntityReset,
       "moduleEntityReset": moduleEntityReset,
       "eportEntityReset": eportEntityReset,
       "moduleInsertion": moduleInsertion,
       "moduleRemoval": moduleRemoval,
       "unknownModule": unknownModule,
       "moduleFailure": moduleFailure,
       "ePortLinkStatusChange": ePortLinkStatusChange,
       "ePortAdminChange": ePortAdminChange,
       "rtwSwitchOverChange": rtwSwitchOverChange,
       "physicalEntities": physicalEntities,
       "chassisGroup": chassisGroup,
       "chassisTable": chassisTable,
       "chassisTableEntry": chassisTableEntry,
       "chassisEntityIndex": chassisEntityIndex,
       "chassisDescription": chassisDescription,
       "chassisPartNumber": chassisPartNumber,
       "chassisNumSlots": chassisNumSlots,
       "chassisCurrentTemp": chassisCurrentTemp,
       "chassisMaxTemp": chassisMaxTemp,
       "chassisReset": chassisReset,
       "lastEntityResetReason": lastEntityResetReason,
       "lastEntityResetIndex": lastEntityResetIndex,
       "lastEntityResetTime": lastEntityResetTime,
       "lastEntityResetType": lastEntityResetType,
       "backPlaneGroup": backPlaneGroup,
       "backPlaneTable": backPlaneTable,
       "backPlaneTableEntry": backPlaneTableEntry,
       "backPlaneEntityIndex": backPlaneEntityIndex,
       "backPlaneDescription": backPlaneDescription,
       "backPlanePartNumber": backPlanePartNumber,
       "backPlaneSerialNumber": backPlaneSerialNumber,
       "backPlaneManufactureDate": backPlaneManufactureDate,
       "backPlaneHWRevisionNumber": backPlaneHWRevisionNumber,
       "powerSupplyGroup": powerSupplyGroup,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyTableEntry": powerSupplyTableEntry,
       "powerSupplyEntityIndex": powerSupplyEntityIndex,
       "powerSupplyStatus": powerSupplyStatus,
       "powerSupplyType": powerSupplyType,
       "powerSupply5vCurrent": powerSupply5vCurrent,
       "powerSupply5vMin": powerSupply5vMin,
       "powerSupply5vMax": powerSupply5vMax,
       "powerSupplyUnitIdentifier": powerSupplyUnitIdentifier,
       "modulesGroup": modulesGroup,
       "moduleTable": moduleTable,
       "moduleTableEntry": moduleTableEntry,
       "modEntityIndex": modEntityIndex,
       "modAdminState": modAdminState,
       "modOperStatus": modOperStatus,
       "modType": modType,
       "modDescription": modDescription,
       "modName": modName,
       "modPartNumber": modPartNumber,
       "modSerialNumber": modSerialNumber,
       "modManufactureDate": modManufactureDate,
       "modDiagnosticTestStatus": modDiagnosticTestStatus,
       "modHWRevisionNumber": modHWRevisionNumber,
       "modNumPorts": modNumPorts,
       "modFirstSlot": modFirstSlot,
       "modNumSlotsOccupied": modNumSlotsOccupied,
       "modReset": modReset,
       "mgmntTable": mgmntTable,
       "mgmntTableEntry": mgmntTableEntry,
       "mgmntEntityIndex": mgmntEntityIndex,
       "mgmntBootImageName": mgmntBootImageName,
       "mgmntBootImageVersion": mgmntBootImageVersion,
       "mgmntCoreImageName": mgmntCoreImageName,
       "mgmntCoreImageVersion": mgmntCoreImageVersion,
       "mgmntAppImageName": mgmntAppImageName,
       "mgmntAppImageVersion": mgmntAppImageVersion,
       "mgmntRamMemorySize": mgmntRamMemorySize,
       "mgmntFlashMemorySize": mgmntFlashMemorySize,
       "mgmntNVRamMemorySize": mgmntNVRamMemorySize,
       "mgmnt5vCurrent": mgmnt5vCurrent,
       "mgmnt5vMin": mgmnt5vMin,
       "mgmnt5vMax": mgmnt5vMax,
       "mgmnt3pt3vCurrent": mgmnt3pt3vCurrent,
       "mgmnt3pt3vMin": mgmnt3pt3vMin,
       "mgmnt3pt3vMax": mgmnt3pt3vMax,
       "mgmntDiagnosticBootError": mgmntDiagnosticBootError,
       "singleTwisterTable": singleTwisterTable,
       "singleTwisterTableEntry": singleTwisterTableEntry,
       "stwEntityIndex": stwEntityIndex,
       "stwLinkLossCarryForward": stwLinkLossCarryForward,
       "dualTwisterTable": dualTwisterTable,
       "dualTwisterTableEntry": dualTwisterTableEntry,
       "dtwEntityIndex": dtwEntityIndex,
       "dtwLinkLossCarryForward": dtwLinkLossCarryForward,
       "redundantTwisterTable": redundantTwisterTable,
       "redundantTwisterTableEntry": redundantTwisterTableEntry,
       "rtwEntityIndex": rtwEntityIndex,
       "rtwAutoRestorePrimary": rtwAutoRestorePrimary,
       "rtwLinkLossCarryForward": rtwLinkLossCarryForward,
       "rtwActivePort": rtwActivePort,
       "rtwRedundantTransmission": rtwRedundantTransmission,
       "rtwSecondarySwitchOver": rtwSecondarySwitchOver,
       "rtwLinkPulseControl": rtwLinkPulseControl,
       "rtwModeControl": rtwModeControl,
       "rtwABSelect": rtwABSelect,
       "ePortGroup": ePortGroup,
       "ePortTable": ePortTable,
       "ePortTableEntry": ePortTableEntry,
       "ePortEntityIndex": ePortEntityIndex,
       "ePortIfIndex": ePortIfIndex,
       "ePortType": ePortType,
       "ePortDescription": ePortDescription,
       "ePortName": ePortName,
       "ePortLinkStatus": ePortLinkStatus,
       "ePortAdminState": ePortAdminState,
       "ePortOperStatus": ePortOperStatus,
       "ePortDuplexAdmin": ePortDuplexAdmin,
       "ePortDuplexOper": ePortDuplexOper,
       "ePortSpeedAdmin": ePortSpeedAdmin,
       "ePortSpeedOper": ePortSpeedOper,
       "ePortAutoNegotiationAdmin": ePortAutoNegotiationAdmin,
       "ePortAutoNegotiationOper": ePortAutoNegotiationOper,
       "ePortReset": ePortReset,
       "ePortActivity": ePortActivity,
       "ePortConnector": ePortConnector,
       "ePortParentRelPos": ePortParentRelPos,
       "serialPortGroup": serialPortGroup,
       "serialPortTable": serialPortTable,
       "serialPortTableEntry": serialPortTableEntry,
       "serialPortEntityIndex": serialPortEntityIndex,
       "serialPortDescription": serialPortDescription,
       "serialPortName": serialPortName,
       "serialPortSpeed": serialPortSpeed,
       "serialPortDataBits": serialPortDataBits,
       "serialPortParity": serialPortParity,
       "serialPortStopBits": serialPortStopBits,
       "serialPortFlowControl": serialPortFlowControl,
       "serialPortConnector": serialPortConnector}
)
