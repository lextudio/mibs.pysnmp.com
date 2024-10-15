# SNMP MIB module (SKYCONTROL-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SKYCONTROL-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:37 2024
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

skycontrol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39052)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtlUnit_ObjectIdentity = ObjectIdentity
ctlUnit = _CtlUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 1)
)
_CtlUnitModulesTable_Object = MibTable
ctlUnitModulesTable = _CtlUnitModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1)
)
if mibBuilder.loadTexts:
    ctlUnitModulesTable.setStatus("current")
_CtlUnitModulesEntry_Object = MibTableRow
ctlUnitModulesEntry = _CtlUnitModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1)
)
ctlUnitModulesEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlUnitModuleId"),
)
if mibBuilder.loadTexts:
    ctlUnitModulesEntry.setStatus("current")
_CtlUnitModuleId_Type = Integer32
_CtlUnitModuleId_Object = MibTableColumn
ctlUnitModuleId = _CtlUnitModuleId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 1),
    _CtlUnitModuleId_Type()
)
ctlUnitModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleId.setStatus("current")
_CtlUnitModulePcode_Type = Integer32
_CtlUnitModulePcode_Object = MibTableColumn
ctlUnitModulePcode = _CtlUnitModulePcode_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 2),
    _CtlUnitModulePcode_Type()
)
ctlUnitModulePcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModulePcode.setStatus("current")
_CtlUnitModuleSN_Type = Integer32
_CtlUnitModuleSN_Object = MibTableColumn
ctlUnitModuleSN = _CtlUnitModuleSN_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 3),
    _CtlUnitModuleSN_Type()
)
ctlUnitModuleSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleSN.setStatus("current")
_CtlUnitModuleClass_Type = OctetString
_CtlUnitModuleClass_Object = MibTableColumn
ctlUnitModuleClass = _CtlUnitModuleClass_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 4),
    _CtlUnitModuleClass_Type()
)
ctlUnitModuleClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleClass.setStatus("current")
_CtlUnitModuleType_Type = OctetString
_CtlUnitModuleType_Object = MibTableColumn
ctlUnitModuleType = _CtlUnitModuleType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 5),
    _CtlUnitModuleType_Type()
)
ctlUnitModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleType.setStatus("current")


class _CtlUnitModuleName_Type(OctetString):
    """Custom type ctlUnitModuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlUnitModuleName_Type.__name__ = "OctetString"
_CtlUnitModuleName_Object = MibTableColumn
ctlUnitModuleName = _CtlUnitModuleName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 6),
    _CtlUnitModuleName_Type()
)
ctlUnitModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitModuleName.setStatus("current")
_CtlUnitModuleState_Type = OctetString
_CtlUnitModuleState_Object = MibTableColumn
ctlUnitModuleState = _CtlUnitModuleState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 1, 1, 7),
    _CtlUnitModuleState_Type()
)
ctlUnitModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitModuleState.setStatus("current")
_CtlUnitGroupsTable_Object = MibTable
ctlUnitGroupsTable = _CtlUnitGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2)
)
if mibBuilder.loadTexts:
    ctlUnitGroupsTable.setStatus("current")
_CtlUnitGroupsEntry_Object = MibTableRow
ctlUnitGroupsEntry = _CtlUnitGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2, 1)
)
ctlUnitGroupsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlUnitGroupId"),
)
if mibBuilder.loadTexts:
    ctlUnitGroupsEntry.setStatus("current")
_CtlUnitGroupId_Type = Integer32
_CtlUnitGroupId_Object = MibTableColumn
ctlUnitGroupId = _CtlUnitGroupId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2, 1, 1),
    _CtlUnitGroupId_Type()
)
ctlUnitGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitGroupId.setStatus("current")


class _CtlUnitGroupName_Type(OctetString):
    """Custom type ctlUnitGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlUnitGroupName_Type.__name__ = "OctetString"
_CtlUnitGroupName_Object = MibTableColumn
ctlUnitGroupName = _CtlUnitGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2, 1, 2),
    _CtlUnitGroupName_Type()
)
ctlUnitGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitGroupName.setStatus("current")


class _CtlUnitGroupDesc_Type(OctetString):
    """Custom type ctlUnitGroupDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CtlUnitGroupDesc_Type.__name__ = "OctetString"
_CtlUnitGroupDesc_Object = MibTableColumn
ctlUnitGroupDesc = _CtlUnitGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 2, 1, 3),
    _CtlUnitGroupDesc_Type()
)
ctlUnitGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitGroupDesc.setStatus("current")
_CtlUnitElementsTable_Object = MibTable
ctlUnitElementsTable = _CtlUnitElementsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3)
)
if mibBuilder.loadTexts:
    ctlUnitElementsTable.setStatus("current")
_CtlUnitElementsEntry_Object = MibTableRow
ctlUnitElementsEntry = _CtlUnitElementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1)
)
ctlUnitElementsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlUnitElementId"),
)
if mibBuilder.loadTexts:
    ctlUnitElementsEntry.setStatus("current")
_CtlUnitElementId_Type = Integer32
_CtlUnitElementId_Object = MibTableColumn
ctlUnitElementId = _CtlUnitElementId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 1),
    _CtlUnitElementId_Type()
)
ctlUnitElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementId.setStatus("current")
_CtlUnitElementGroup_Type = Integer32
_CtlUnitElementGroup_Object = MibTableColumn
ctlUnitElementGroup = _CtlUnitElementGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 2),
    _CtlUnitElementGroup_Type()
)
ctlUnitElementGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitElementGroup.setStatus("current")
_CtlUnitElementModule_Type = Integer32
_CtlUnitElementModule_Object = MibTableColumn
ctlUnitElementModule = _CtlUnitElementModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 3),
    _CtlUnitElementModule_Type()
)
ctlUnitElementModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementModule.setStatus("current")
_CtlUnitElementNum_Type = Integer32
_CtlUnitElementNum_Object = MibTableColumn
ctlUnitElementNum = _CtlUnitElementNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 4),
    _CtlUnitElementNum_Type()
)
ctlUnitElementNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementNum.setStatus("current")
_CtlUnitElementClass_Type = OctetString
_CtlUnitElementClass_Object = MibTableColumn
ctlUnitElementClass = _CtlUnitElementClass_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 5),
    _CtlUnitElementClass_Type()
)
ctlUnitElementClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementClass.setStatus("current")
_CtlUnitElementType_Type = OctetString
_CtlUnitElementType_Object = MibTableColumn
ctlUnitElementType = _CtlUnitElementType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 6),
    _CtlUnitElementType_Type()
)
ctlUnitElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementType.setStatus("current")


class _CtlUnitElementName_Type(OctetString):
    """Custom type ctlUnitElementName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlUnitElementName_Type.__name__ = "OctetString"
_CtlUnitElementName_Object = MibTableColumn
ctlUnitElementName = _CtlUnitElementName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 7),
    _CtlUnitElementName_Type()
)
ctlUnitElementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitElementName.setStatus("current")
_CtlUnitElementState_Type = OctetString
_CtlUnitElementState_Object = MibTableColumn
ctlUnitElementState = _CtlUnitElementState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 8),
    _CtlUnitElementState_Type()
)
ctlUnitElementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementState.setStatus("current")
_CtlUnitElementValue_Type = OctetString
_CtlUnitElementValue_Object = MibTableColumn
ctlUnitElementValue = _CtlUnitElementValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 9),
    _CtlUnitElementValue_Type()
)
ctlUnitElementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementValue.setStatus("current")
_CtlUnitElementSpec_Type = OctetString
_CtlUnitElementSpec_Object = MibTableColumn
ctlUnitElementSpec = _CtlUnitElementSpec_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 3, 1, 10),
    _CtlUnitElementSpec_Type()
)
ctlUnitElementSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitElementSpec.setStatus("current")
_CtlUnitLogicsTable_Object = MibTable
ctlUnitLogicsTable = _CtlUnitLogicsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4)
)
if mibBuilder.loadTexts:
    ctlUnitLogicsTable.setStatus("current")
_CtlUnitLogicsEntry_Object = MibTableRow
ctlUnitLogicsEntry = _CtlUnitLogicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1)
)
ctlUnitLogicsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlUnitLogicId"),
)
if mibBuilder.loadTexts:
    ctlUnitLogicsEntry.setStatus("current")
_CtlUnitLogicId_Type = Integer32
_CtlUnitLogicId_Object = MibTableColumn
ctlUnitLogicId = _CtlUnitLogicId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 1),
    _CtlUnitLogicId_Type()
)
ctlUnitLogicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlUnitLogicId.setStatus("current")


class _CtlUnitLogicName_Type(OctetString):
    """Custom type ctlUnitLogicName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlUnitLogicName_Type.__name__ = "OctetString"
_CtlUnitLogicName_Object = MibTableColumn
ctlUnitLogicName = _CtlUnitLogicName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 2),
    _CtlUnitLogicName_Type()
)
ctlUnitLogicName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctlUnitLogicName.setStatus("current")


class _CtlUnitLogicDesc_Type(OctetString):
    """Custom type ctlUnitLogicDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_CtlUnitLogicDesc_Type.__name__ = "OctetString"
_CtlUnitLogicDesc_Object = MibTableColumn
ctlUnitLogicDesc = _CtlUnitLogicDesc_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 3),
    _CtlUnitLogicDesc_Type()
)
ctlUnitLogicDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctlUnitLogicDesc.setStatus("current")
_CtlUnitLogicDisable_Type = Integer32
_CtlUnitLogicDisable_Object = MibTableColumn
ctlUnitLogicDisable = _CtlUnitLogicDisable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 4),
    _CtlUnitLogicDisable_Type()
)
ctlUnitLogicDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctlUnitLogicDisable.setStatus("current")
_CtlUnitLogicRowStatus_Type = Integer32
_CtlUnitLogicRowStatus_Object = MibTableColumn
ctlUnitLogicRowStatus = _CtlUnitLogicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 4, 1, 5),
    _CtlUnitLogicRowStatus_Type()
)
ctlUnitLogicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctlUnitLogicRowStatus.setStatus("current")
_CtlUnitSaveToFlash_Type = Integer32
_CtlUnitSaveToFlash_Object = MibScalar
ctlUnitSaveToFlash = _CtlUnitSaveToFlash_Object(
    (1, 3, 6, 1, 4, 1, 39052, 1, 6),
    _CtlUnitSaveToFlash_Type()
)
ctlUnitSaveToFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlUnitSaveToFlash.setStatus("current")
_CtlNotifiers_ObjectIdentity = ObjectIdentity
ctlNotifiers = _CtlNotifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 2)
)
_CtlNotifiersMailersTable_Object = MibTable
ctlNotifiersMailersTable = _CtlNotifiersMailersTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1)
)
if mibBuilder.loadTexts:
    ctlNotifiersMailersTable.setStatus("current")
_CtlNotifiersMailersEntry_Object = MibTableRow
ctlNotifiersMailersEntry = _CtlNotifiersMailersEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1)
)
ctlNotifiersMailersEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlNotifiersMailerId"),
)
if mibBuilder.loadTexts:
    ctlNotifiersMailersEntry.setStatus("current")
_CtlNotifiersMailerId_Type = Integer32
_CtlNotifiersMailerId_Object = MibTableColumn
ctlNotifiersMailerId = _CtlNotifiersMailerId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 1),
    _CtlNotifiersMailerId_Type()
)
ctlNotifiersMailerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerId.setStatus("current")
_CtlNotifiersMailerModule_Type = Integer32
_CtlNotifiersMailerModule_Object = MibTableColumn
ctlNotifiersMailerModule = _CtlNotifiersMailerModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 2),
    _CtlNotifiersMailerModule_Type()
)
ctlNotifiersMailerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerModule.setStatus("current")
_CtlNotifiersMailerNum_Type = Integer32
_CtlNotifiersMailerNum_Object = MibTableColumn
ctlNotifiersMailerNum = _CtlNotifiersMailerNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 3),
    _CtlNotifiersMailerNum_Type()
)
ctlNotifiersMailerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerNum.setStatus("current")
_CtlNotifiersMailerGroup_Type = Integer32
_CtlNotifiersMailerGroup_Object = MibTableColumn
ctlNotifiersMailerGroup = _CtlNotifiersMailerGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 4),
    _CtlNotifiersMailerGroup_Type()
)
ctlNotifiersMailerGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerGroup.setStatus("current")
_CtlNotifiersMailerType_Type = OctetString
_CtlNotifiersMailerType_Object = MibTableColumn
ctlNotifiersMailerType = _CtlNotifiersMailerType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 5),
    _CtlNotifiersMailerType_Type()
)
ctlNotifiersMailerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerType.setStatus("current")


class _CtlNotifiersMailerName_Type(OctetString):
    """Custom type ctlNotifiersMailerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersMailerName_Type.__name__ = "OctetString"
_CtlNotifiersMailerName_Object = MibTableColumn
ctlNotifiersMailerName = _CtlNotifiersMailerName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 6),
    _CtlNotifiersMailerName_Type()
)
ctlNotifiersMailerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerName.setStatus("current")
_CtlNotifiersMailerState_Type = OctetString
_CtlNotifiersMailerState_Object = MibTableColumn
ctlNotifiersMailerState = _CtlNotifiersMailerState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 7),
    _CtlNotifiersMailerState_Type()
)
ctlNotifiersMailerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersMailerState.setStatus("current")
_CtlNotifiersMailerValue_Type = OctetString
_CtlNotifiersMailerValue_Object = MibTableColumn
ctlNotifiersMailerValue = _CtlNotifiersMailerValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 8),
    _CtlNotifiersMailerValue_Type()
)
ctlNotifiersMailerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerValue.setStatus("current")


class _CtlNotifiersMailerServer_Type(OctetString):
    """Custom type ctlNotifiersMailerServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_CtlNotifiersMailerServer_Type.__name__ = "OctetString"
_CtlNotifiersMailerServer_Object = MibTableColumn
ctlNotifiersMailerServer = _CtlNotifiersMailerServer_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 9),
    _CtlNotifiersMailerServer_Type()
)
ctlNotifiersMailerServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerServer.setStatus("current")
_CtlNotifiersMailerPort_Type = Integer32
_CtlNotifiersMailerPort_Object = MibTableColumn
ctlNotifiersMailerPort = _CtlNotifiersMailerPort_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 10),
    _CtlNotifiersMailerPort_Type()
)
ctlNotifiersMailerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerPort.setStatus("current")


class _CtlNotifiersMailerLogin_Type(OctetString):
    """Custom type ctlNotifiersMailerLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersMailerLogin_Type.__name__ = "OctetString"
_CtlNotifiersMailerLogin_Object = MibTableColumn
ctlNotifiersMailerLogin = _CtlNotifiersMailerLogin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 11),
    _CtlNotifiersMailerLogin_Type()
)
ctlNotifiersMailerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerLogin.setStatus("current")
_CtlNotifiersMailerPassword_Type = Integer32
_CtlNotifiersMailerPassword_Object = MibTableColumn
ctlNotifiersMailerPassword = _CtlNotifiersMailerPassword_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 12),
    _CtlNotifiersMailerPassword_Type()
)
ctlNotifiersMailerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerPassword.setStatus("current")


class _CtlNotifiersMailersTo_Type(OctetString):
    """Custom type ctlNotifiersMailersTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersMailersTo_Type.__name__ = "OctetString"
_CtlNotifiersMailersTo_Object = MibTableColumn
ctlNotifiersMailersTo = _CtlNotifiersMailersTo_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 13),
    _CtlNotifiersMailersTo_Type()
)
ctlNotifiersMailersTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailersTo.setStatus("current")


class _CtlNotifiersMailersFrom_Type(OctetString):
    """Custom type ctlNotifiersMailersFrom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 512),
    )


_CtlNotifiersMailersFrom_Type.__name__ = "OctetString"
_CtlNotifiersMailersFrom_Object = MibTableColumn
ctlNotifiersMailersFrom = _CtlNotifiersMailersFrom_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 14),
    _CtlNotifiersMailersFrom_Type()
)
ctlNotifiersMailersFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailersFrom.setStatus("current")
_CtlNotifiersMailerMessage_Type = Integer32
_CtlNotifiersMailerMessage_Object = MibTableColumn
ctlNotifiersMailerMessage = _CtlNotifiersMailerMessage_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 1, 1, 15),
    _CtlNotifiersMailerMessage_Type()
)
ctlNotifiersMailerMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersMailerMessage.setStatus("current")
_CtlNotifiersTrapsTable_Object = MibTable
ctlNotifiersTrapsTable = _CtlNotifiersTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2)
)
if mibBuilder.loadTexts:
    ctlNotifiersTrapsTable.setStatus("current")
_CtlNotifiersTrapsEntry_Object = MibTableRow
ctlNotifiersTrapsEntry = _CtlNotifiersTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1)
)
ctlNotifiersTrapsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlNotifiersTrapId"),
)
if mibBuilder.loadTexts:
    ctlNotifiersTrapsEntry.setStatus("current")
_CtlNotifiersTrapId_Type = Integer32
_CtlNotifiersTrapId_Object = MibTableColumn
ctlNotifiersTrapId = _CtlNotifiersTrapId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 1),
    _CtlNotifiersTrapId_Type()
)
ctlNotifiersTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapId.setStatus("current")
_CtlNotifiersTrapModule_Type = Integer32
_CtlNotifiersTrapModule_Object = MibTableColumn
ctlNotifiersTrapModule = _CtlNotifiersTrapModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 2),
    _CtlNotifiersTrapModule_Type()
)
ctlNotifiersTrapModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapModule.setStatus("current")
_CtlNotifiersTrapNum_Type = Integer32
_CtlNotifiersTrapNum_Object = MibTableColumn
ctlNotifiersTrapNum = _CtlNotifiersTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 3),
    _CtlNotifiersTrapNum_Type()
)
ctlNotifiersTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapNum.setStatus("current")
_CtlNotifiersTrapGroup_Type = Integer32
_CtlNotifiersTrapGroup_Object = MibTableColumn
ctlNotifiersTrapGroup = _CtlNotifiersTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 4),
    _CtlNotifiersTrapGroup_Type()
)
ctlNotifiersTrapGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapGroup.setStatus("current")
_CtlNotifiersTrapType_Type = OctetString
_CtlNotifiersTrapType_Object = MibTableColumn
ctlNotifiersTrapType = _CtlNotifiersTrapType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 5),
    _CtlNotifiersTrapType_Type()
)
ctlNotifiersTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapType.setStatus("current")
_CtlNotifiersTrapName_Type = OctetString
_CtlNotifiersTrapName_Object = MibTableColumn
ctlNotifiersTrapName = _CtlNotifiersTrapName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 6),
    _CtlNotifiersTrapName_Type()
)
ctlNotifiersTrapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapName.setStatus("current")
_CtlNotifiersTrapState_Type = OctetString
_CtlNotifiersTrapState_Object = MibTableColumn
ctlNotifiersTrapState = _CtlNotifiersTrapState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 7),
    _CtlNotifiersTrapState_Type()
)
ctlNotifiersTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersTrapState.setStatus("current")
_CtlNotifiersTrapValue_Type = OctetString
_CtlNotifiersTrapValue_Object = MibTableColumn
ctlNotifiersTrapValue = _CtlNotifiersTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 8),
    _CtlNotifiersTrapValue_Type()
)
ctlNotifiersTrapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapValue.setStatus("current")


class _CtlNotifiersTrapServer_Type(OctetString):
    """Custom type ctlNotifiersTrapServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersTrapServer_Type.__name__ = "OctetString"
_CtlNotifiersTrapServer_Object = MibTableColumn
ctlNotifiersTrapServer = _CtlNotifiersTrapServer_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 9),
    _CtlNotifiersTrapServer_Type()
)
ctlNotifiersTrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapServer.setStatus("current")
_CtlNotifiersTrapPort_Type = Integer32
_CtlNotifiersTrapPort_Object = MibTableColumn
ctlNotifiersTrapPort = _CtlNotifiersTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 10),
    _CtlNotifiersTrapPort_Type()
)
ctlNotifiersTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapPort.setStatus("current")


class _CtlNotifiersTrapVersion_Type(OctetString):
    """Custom type ctlNotifiersTrapVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_CtlNotifiersTrapVersion_Type.__name__ = "OctetString"
_CtlNotifiersTrapVersion_Object = MibTableColumn
ctlNotifiersTrapVersion = _CtlNotifiersTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 11),
    _CtlNotifiersTrapVersion_Type()
)
ctlNotifiersTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapVersion.setStatus("current")


class _CtlNotifiersTrapCommunity_Type(OctetString):
    """Custom type ctlNotifiersTrapCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_CtlNotifiersTrapCommunity_Type.__name__ = "OctetString"
_CtlNotifiersTrapCommunity_Object = MibTableColumn
ctlNotifiersTrapCommunity = _CtlNotifiersTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 2, 1, 12),
    _CtlNotifiersTrapCommunity_Type()
)
ctlNotifiersTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersTrapCommunity.setStatus("current")
_CtlNotifiersSMSsTable_Object = MibTable
ctlNotifiersSMSsTable = _CtlNotifiersSMSsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3)
)
if mibBuilder.loadTexts:
    ctlNotifiersSMSsTable.setStatus("current")
_CtlNotifiersSMSsEntry_Object = MibTableRow
ctlNotifiersSMSsEntry = _CtlNotifiersSMSsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1)
)
ctlNotifiersSMSsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlNotifiersSMSId"),
)
if mibBuilder.loadTexts:
    ctlNotifiersSMSsEntry.setStatus("current")
_CtlNotifiersSMSId_Type = Integer32
_CtlNotifiersSMSId_Object = MibTableColumn
ctlNotifiersSMSId = _CtlNotifiersSMSId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 1),
    _CtlNotifiersSMSId_Type()
)
ctlNotifiersSMSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSId.setStatus("current")
_CtlNotifiersSMSModule_Type = Integer32
_CtlNotifiersSMSModule_Object = MibTableColumn
ctlNotifiersSMSModule = _CtlNotifiersSMSModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 2),
    _CtlNotifiersSMSModule_Type()
)
ctlNotifiersSMSModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSModule.setStatus("current")
_CtlNotifiersSMSNum_Type = Integer32
_CtlNotifiersSMSNum_Object = MibTableColumn
ctlNotifiersSMSNum = _CtlNotifiersSMSNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 3),
    _CtlNotifiersSMSNum_Type()
)
ctlNotifiersSMSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSNum.setStatus("current")
_CtlNotifiersSMSGroup_Type = Integer32
_CtlNotifiersSMSGroup_Object = MibTableColumn
ctlNotifiersSMSGroup = _CtlNotifiersSMSGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 4),
    _CtlNotifiersSMSGroup_Type()
)
ctlNotifiersSMSGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSGroup.setStatus("current")
_CtlNotifiersSMSType_Type = OctetString
_CtlNotifiersSMSType_Object = MibTableColumn
ctlNotifiersSMSType = _CtlNotifiersSMSType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 5),
    _CtlNotifiersSMSType_Type()
)
ctlNotifiersSMSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSType.setStatus("current")


class _CtlNotifiersSMSName_Type(OctetString):
    """Custom type ctlNotifiersSMSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlNotifiersSMSName_Type.__name__ = "OctetString"
_CtlNotifiersSMSName_Object = MibTableColumn
ctlNotifiersSMSName = _CtlNotifiersSMSName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 6),
    _CtlNotifiersSMSName_Type()
)
ctlNotifiersSMSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSName.setStatus("current")
_CtlNotifiersSMSState_Type = OctetString
_CtlNotifiersSMSState_Object = MibTableColumn
ctlNotifiersSMSState = _CtlNotifiersSMSState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 7),
    _CtlNotifiersSMSState_Type()
)
ctlNotifiersSMSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNotifiersSMSState.setStatus("current")
_CtlNotifiersSMSValue_Type = OctetString
_CtlNotifiersSMSValue_Object = MibTableColumn
ctlNotifiersSMSValue = _CtlNotifiersSMSValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 8),
    _CtlNotifiersSMSValue_Type()
)
ctlNotifiersSMSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSValue.setStatus("current")


class _CtlNotifiersSMSTo_Type(OctetString):
    """Custom type ctlNotifiersSMSTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 256),
    )


_CtlNotifiersSMSTo_Type.__name__ = "OctetString"
_CtlNotifiersSMSTo_Object = MibTableColumn
ctlNotifiersSMSTo = _CtlNotifiersSMSTo_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 9),
    _CtlNotifiersSMSTo_Type()
)
ctlNotifiersSMSTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSTo.setStatus("current")


class _CtlNotifiersSMSMessage_Type(OctetString):
    """Custom type ctlNotifiersSMSMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 512),
    )


_CtlNotifiersSMSMessage_Type.__name__ = "OctetString"
_CtlNotifiersSMSMessage_Object = MibTableColumn
ctlNotifiersSMSMessage = _CtlNotifiersSMSMessage_Object(
    (1, 3, 6, 1, 4, 1, 39052, 2, 3, 1, 10),
    _CtlNotifiersSMSMessage_Type()
)
ctlNotifiersSMSMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlNotifiersSMSMessage.setStatus("current")
_CtlVirtualDevices_ObjectIdentity = ObjectIdentity
ctlVirtualDevices = _CtlVirtualDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 3)
)
_CtlVirtualDevicesTimersTable_Object = MibTable
ctlVirtualDevicesTimersTable = _CtlVirtualDevicesTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1)
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimersTable.setStatus("current")
_CtlVirtualDevicesTimersEntry_Object = MibTableRow
ctlVirtualDevicesTimersEntry = _CtlVirtualDevicesTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1)
)
ctlVirtualDevicesTimersEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlVirtualDevicesTimerId"),
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimersEntry.setStatus("current")
_CtlVirtualDevicesTimerId_Type = Integer32
_CtlVirtualDevicesTimerId_Object = MibTableColumn
ctlVirtualDevicesTimerId = _CtlVirtualDevicesTimerId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 1),
    _CtlVirtualDevicesTimerId_Type()
)
ctlVirtualDevicesTimerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerId.setStatus("current")
_CtlVirtualDevicesTimerModule_Type = Integer32
_CtlVirtualDevicesTimerModule_Object = MibTableColumn
ctlVirtualDevicesTimerModule = _CtlVirtualDevicesTimerModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 2),
    _CtlVirtualDevicesTimerModule_Type()
)
ctlVirtualDevicesTimerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerModule.setStatus("current")
_CtlVirtualDevicesTimerNum_Type = Integer32
_CtlVirtualDevicesTimerNum_Object = MibTableColumn
ctlVirtualDevicesTimerNum = _CtlVirtualDevicesTimerNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 3),
    _CtlVirtualDevicesTimerNum_Type()
)
ctlVirtualDevicesTimerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerNum.setStatus("current")
_CtlVirtualDevicesTimerGroup_Type = Integer32
_CtlVirtualDevicesTimerGroup_Object = MibTableColumn
ctlVirtualDevicesTimerGroup = _CtlVirtualDevicesTimerGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 4),
    _CtlVirtualDevicesTimerGroup_Type()
)
ctlVirtualDevicesTimerGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerGroup.setStatus("current")
_CtlVirtualDevicesTimerType_Type = OctetString
_CtlVirtualDevicesTimerType_Object = MibTableColumn
ctlVirtualDevicesTimerType = _CtlVirtualDevicesTimerType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 5),
    _CtlVirtualDevicesTimerType_Type()
)
ctlVirtualDevicesTimerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerType.setStatus("current")


class _CtlVirtualDevicesTimerName_Type(OctetString):
    """Custom type ctlVirtualDevicesTimerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlVirtualDevicesTimerName_Type.__name__ = "OctetString"
_CtlVirtualDevicesTimerName_Object = MibTableColumn
ctlVirtualDevicesTimerName = _CtlVirtualDevicesTimerName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 6),
    _CtlVirtualDevicesTimerName_Type()
)
ctlVirtualDevicesTimerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerName.setStatus("current")
_CtlVirtualDevicesTimerState_Type = OctetString
_CtlVirtualDevicesTimerState_Object = MibTableColumn
ctlVirtualDevicesTimerState = _CtlVirtualDevicesTimerState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 7),
    _CtlVirtualDevicesTimerState_Type()
)
ctlVirtualDevicesTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerState.setStatus("current")
_CtlVirtualDevicesTimerValue_Type = OctetString
_CtlVirtualDevicesTimerValue_Object = MibTableColumn
ctlVirtualDevicesTimerValue = _CtlVirtualDevicesTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 8),
    _CtlVirtualDevicesTimerValue_Type()
)
ctlVirtualDevicesTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerValue.setStatus("current")
_CtlVirtualDevicesTimerBegin_Type = OctetString
_CtlVirtualDevicesTimerBegin_Object = MibTableColumn
ctlVirtualDevicesTimerBegin = _CtlVirtualDevicesTimerBegin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 9),
    _CtlVirtualDevicesTimerBegin_Type()
)
ctlVirtualDevicesTimerBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerBegin.setStatus("current")
_CtlVirtualDevicesTimerEnd_Type = OctetString
_CtlVirtualDevicesTimerEnd_Object = MibTableColumn
ctlVirtualDevicesTimerEnd = _CtlVirtualDevicesTimerEnd_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 10),
    _CtlVirtualDevicesTimerEnd_Type()
)
ctlVirtualDevicesTimerEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerEnd.setStatus("current")
_CtlVirtualDevicesTimerDays_Type = OctetString
_CtlVirtualDevicesTimerDays_Object = MibTableColumn
ctlVirtualDevicesTimerDays = _CtlVirtualDevicesTimerDays_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 11),
    _CtlVirtualDevicesTimerDays_Type()
)
ctlVirtualDevicesTimerDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerDays.setStatus("current")
_CtlVirtualDevicesTimerMode_Type = OctetString
_CtlVirtualDevicesTimerMode_Object = MibTableColumn
ctlVirtualDevicesTimerMode = _CtlVirtualDevicesTimerMode_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 1, 1, 12),
    _CtlVirtualDevicesTimerMode_Type()
)
ctlVirtualDevicesTimerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesTimerMode.setStatus("current")
_CtlVirtualDevicesPingsTable_Object = MibTable
ctlVirtualDevicesPingsTable = _CtlVirtualDevicesPingsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2)
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingsTable.setStatus("current")
_CtlVirtualDevicesPingsEntry_Object = MibTableRow
ctlVirtualDevicesPingsEntry = _CtlVirtualDevicesPingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1)
)
ctlVirtualDevicesPingsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlVirtualDevicesPingId"),
)
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingsEntry.setStatus("current")
_CtlVirtualDevicesPingId_Type = Integer32
_CtlVirtualDevicesPingId_Object = MibTableColumn
ctlVirtualDevicesPingId = _CtlVirtualDevicesPingId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 1),
    _CtlVirtualDevicesPingId_Type()
)
ctlVirtualDevicesPingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingId.setStatus("current")
_CtlVirtualDevicesPingModule_Type = Integer32
_CtlVirtualDevicesPingModule_Object = MibTableColumn
ctlVirtualDevicesPingModule = _CtlVirtualDevicesPingModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 2),
    _CtlVirtualDevicesPingModule_Type()
)
ctlVirtualDevicesPingModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingModule.setStatus("current")
_CtlVirtualDevicesPingNum_Type = Integer32
_CtlVirtualDevicesPingNum_Object = MibTableColumn
ctlVirtualDevicesPingNum = _CtlVirtualDevicesPingNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 3),
    _CtlVirtualDevicesPingNum_Type()
)
ctlVirtualDevicesPingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingNum.setStatus("current")
_CtlVirtualDevicesPingGroup_Type = Integer32
_CtlVirtualDevicesPingGroup_Object = MibTableColumn
ctlVirtualDevicesPingGroup = _CtlVirtualDevicesPingGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 4),
    _CtlVirtualDevicesPingGroup_Type()
)
ctlVirtualDevicesPingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingGroup.setStatus("current")
_CtlVirtualDevicesPingType_Type = OctetString
_CtlVirtualDevicesPingType_Object = MibTableColumn
ctlVirtualDevicesPingType = _CtlVirtualDevicesPingType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 5),
    _CtlVirtualDevicesPingType_Type()
)
ctlVirtualDevicesPingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingType.setStatus("current")


class _CtlVirtualDevicesPingName_Type(OctetString):
    """Custom type ctlVirtualDevicesPingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlVirtualDevicesPingName_Type.__name__ = "OctetString"
_CtlVirtualDevicesPingName_Object = MibTableColumn
ctlVirtualDevicesPingName = _CtlVirtualDevicesPingName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 6),
    _CtlVirtualDevicesPingName_Type()
)
ctlVirtualDevicesPingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingName.setStatus("current")
_CtlVirtualDevicesPingState_Type = OctetString
_CtlVirtualDevicesPingState_Object = MibTableColumn
ctlVirtualDevicesPingState = _CtlVirtualDevicesPingState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 7),
    _CtlVirtualDevicesPingState_Type()
)
ctlVirtualDevicesPingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingState.setStatus("current")
_CtlVirtualDevicesPingValue_Type = OctetString
_CtlVirtualDevicesPingValue_Object = MibTableColumn
ctlVirtualDevicesPingValue = _CtlVirtualDevicesPingValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 8),
    _CtlVirtualDevicesPingValue_Type()
)
ctlVirtualDevicesPingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingValue.setStatus("current")
_CtlVirtualDevicesPingPeriod_Type = Integer32
_CtlVirtualDevicesPingPeriod_Object = MibTableColumn
ctlVirtualDevicesPingPeriod = _CtlVirtualDevicesPingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 9),
    _CtlVirtualDevicesPingPeriod_Type()
)
ctlVirtualDevicesPingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingPeriod.setStatus("current")
_CtlVirtualDevicesPingRTT_Type = Integer32
_CtlVirtualDevicesPingRTT_Object = MibTableColumn
ctlVirtualDevicesPingRTT = _CtlVirtualDevicesPingRTT_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 10),
    _CtlVirtualDevicesPingRTT_Type()
)
ctlVirtualDevicesPingRTT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingRTT.setStatus("current")


class _CtlVirtualDevicesPingServer_Type(OctetString):
    """Custom type ctlVirtualDevicesPingServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_CtlVirtualDevicesPingServer_Type.__name__ = "OctetString"
_CtlVirtualDevicesPingServer_Object = MibTableColumn
ctlVirtualDevicesPingServer = _CtlVirtualDevicesPingServer_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 11),
    _CtlVirtualDevicesPingServer_Type()
)
ctlVirtualDevicesPingServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingServer.setStatus("current")
_CtlVirtualDevicesPingIP_Type = OctetString
_CtlVirtualDevicesPingIP_Object = MibTableColumn
ctlVirtualDevicesPingIP = _CtlVirtualDevicesPingIP_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 12),
    _CtlVirtualDevicesPingIP_Type()
)
ctlVirtualDevicesPingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingIP.setStatus("current")
_CtlVirtualDevicesPingSent_Type = Integer32
_CtlVirtualDevicesPingSent_Object = MibTableColumn
ctlVirtualDevicesPingSent = _CtlVirtualDevicesPingSent_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 13),
    _CtlVirtualDevicesPingSent_Type()
)
ctlVirtualDevicesPingSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingSent.setStatus("current")
_CtlVirtualDevicesPingReceived_Type = Integer32
_CtlVirtualDevicesPingReceived_Object = MibTableColumn
ctlVirtualDevicesPingReceived = _CtlVirtualDevicesPingReceived_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 14),
    _CtlVirtualDevicesPingReceived_Type()
)
ctlVirtualDevicesPingReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingReceived.setStatus("current")
_CtlVirtualDevicesPingStatus_Type = OctetString
_CtlVirtualDevicesPingStatus_Object = MibTableColumn
ctlVirtualDevicesPingStatus = _CtlVirtualDevicesPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 39052, 3, 2, 1, 15),
    _CtlVirtualDevicesPingStatus_Type()
)
ctlVirtualDevicesPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlVirtualDevicesPingStatus.setStatus("current")
_CtlHardwareDevices_ObjectIdentity = ObjectIdentity
ctlHardwareDevices = _CtlHardwareDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 4)
)
_CtlHardwareDevicesCamerasTable_Object = MibTable
ctlHardwareDevicesCamerasTable = _CtlHardwareDevicesCamerasTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1)
)
if mibBuilder.loadTexts:
    ctlHardwareDevicesCamerasTable.setStatus("current")
_CtlHardwareDevicesCamerasEntry_Object = MibTableRow
ctlHardwareDevicesCamerasEntry = _CtlHardwareDevicesCamerasEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1)
)
ctlHardwareDevicesCamerasEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlHardwareDevicesCameraId"),
)
if mibBuilder.loadTexts:
    ctlHardwareDevicesCamerasEntry.setStatus("current")
_CtlHardwareDevicesCameraId_Type = Integer32
_CtlHardwareDevicesCameraId_Object = MibTableColumn
ctlHardwareDevicesCameraId = _CtlHardwareDevicesCameraId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 1),
    _CtlHardwareDevicesCameraId_Type()
)
ctlHardwareDevicesCameraId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraId.setStatus("current")
_CtlHardwareDevicesCameraModule_Type = Integer32
_CtlHardwareDevicesCameraModule_Object = MibTableColumn
ctlHardwareDevicesCameraModule = _CtlHardwareDevicesCameraModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 2),
    _CtlHardwareDevicesCameraModule_Type()
)
ctlHardwareDevicesCameraModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraModule.setStatus("current")
_CtlHardwareDevicesCameraNum_Type = Integer32
_CtlHardwareDevicesCameraNum_Object = MibTableColumn
ctlHardwareDevicesCameraNum = _CtlHardwareDevicesCameraNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 3),
    _CtlHardwareDevicesCameraNum_Type()
)
ctlHardwareDevicesCameraNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraNum.setStatus("current")
_CtlHardwareDevicesCameraGroup_Type = Integer32
_CtlHardwareDevicesCameraGroup_Object = MibTableColumn
ctlHardwareDevicesCameraGroup = _CtlHardwareDevicesCameraGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 4),
    _CtlHardwareDevicesCameraGroup_Type()
)
ctlHardwareDevicesCameraGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraGroup.setStatus("current")
_CtlHardwareDevicesCameraType_Type = OctetString
_CtlHardwareDevicesCameraType_Object = MibTableColumn
ctlHardwareDevicesCameraType = _CtlHardwareDevicesCameraType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 5),
    _CtlHardwareDevicesCameraType_Type()
)
ctlHardwareDevicesCameraType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraType.setStatus("current")


class _CtlHardwareDevicesCameraName_Type(OctetString):
    """Custom type ctlHardwareDevicesCameraName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_CtlHardwareDevicesCameraName_Type.__name__ = "OctetString"
_CtlHardwareDevicesCameraName_Object = MibTableColumn
ctlHardwareDevicesCameraName = _CtlHardwareDevicesCameraName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 6),
    _CtlHardwareDevicesCameraName_Type()
)
ctlHardwareDevicesCameraName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraName.setStatus("current")
_CtlHardwareDevicesCameraState_Type = OctetString
_CtlHardwareDevicesCameraState_Object = MibTableColumn
ctlHardwareDevicesCameraState = _CtlHardwareDevicesCameraState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 7),
    _CtlHardwareDevicesCameraState_Type()
)
ctlHardwareDevicesCameraState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraState.setStatus("current")
_CtlHardwareDevicesCameraValue_Type = OctetString
_CtlHardwareDevicesCameraValue_Object = MibTableColumn
ctlHardwareDevicesCameraValue = _CtlHardwareDevicesCameraValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 8),
    _CtlHardwareDevicesCameraValue_Type()
)
ctlHardwareDevicesCameraValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraValue.setStatus("current")


class _CtlHardwareDevicesCameraURL_Type(OctetString):
    """Custom type ctlHardwareDevicesCameraURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_CtlHardwareDevicesCameraURL_Type.__name__ = "OctetString"
_CtlHardwareDevicesCameraURL_Object = MibTableColumn
ctlHardwareDevicesCameraURL = _CtlHardwareDevicesCameraURL_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 9),
    _CtlHardwareDevicesCameraURL_Type()
)
ctlHardwareDevicesCameraURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraURL.setStatus("current")
_CtlHardwareDevicesCameraFPS_Type = OctetString
_CtlHardwareDevicesCameraFPS_Object = MibTableColumn
ctlHardwareDevicesCameraFPS = _CtlHardwareDevicesCameraFPS_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 10),
    _CtlHardwareDevicesCameraFPS_Type()
)
ctlHardwareDevicesCameraFPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraFPS.setStatus("current")
_CtlHardwareDevicesCameraResolution_Type = OctetString
_CtlHardwareDevicesCameraResolution_Object = MibTableColumn
ctlHardwareDevicesCameraResolution = _CtlHardwareDevicesCameraResolution_Object(
    (1, 3, 6, 1, 4, 1, 39052, 4, 1, 1, 11),
    _CtlHardwareDevicesCameraResolution_Type()
)
ctlHardwareDevicesCameraResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlHardwareDevicesCameraResolution.setStatus("current")
_CtIInternalSensors_ObjectIdentity = ObjectIdentity
ctIInternalSensors = _CtIInternalSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 5)
)
_CtlInternalSensorsDiscretsTable_Object = MibTable
ctlInternalSensorsDiscretsTable = _CtlInternalSensorsDiscretsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1)
)
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretsTable.setStatus("current")
_CtlInternalSensorsDiscretsEntry_Object = MibTableRow
ctlInternalSensorsDiscretsEntry = _CtlInternalSensorsDiscretsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1)
)
ctlInternalSensorsDiscretsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlInternalSensorsDiscretId"),
)
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretsEntry.setStatus("current")
_CtlInternalSensorsDiscretId_Type = Integer32
_CtlInternalSensorsDiscretId_Object = MibTableColumn
ctlInternalSensorsDiscretId = _CtlInternalSensorsDiscretId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 1),
    _CtlInternalSensorsDiscretId_Type()
)
ctlInternalSensorsDiscretId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretId.setStatus("current")
_CtlInternalSensorsDiscretModule_Type = Integer32
_CtlInternalSensorsDiscretModule_Object = MibTableColumn
ctlInternalSensorsDiscretModule = _CtlInternalSensorsDiscretModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 2),
    _CtlInternalSensorsDiscretModule_Type()
)
ctlInternalSensorsDiscretModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretModule.setStatus("current")
_CtlInternalSensorsDiscretNum_Type = Integer32
_CtlInternalSensorsDiscretNum_Object = MibTableColumn
ctlInternalSensorsDiscretNum = _CtlInternalSensorsDiscretNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 3),
    _CtlInternalSensorsDiscretNum_Type()
)
ctlInternalSensorsDiscretNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretNum.setStatus("current")
_CtlInternalSensorsDiscretGroup_Type = Integer32
_CtlInternalSensorsDiscretGroup_Object = MibTableColumn
ctlInternalSensorsDiscretGroup = _CtlInternalSensorsDiscretGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 4),
    _CtlInternalSensorsDiscretGroup_Type()
)
ctlInternalSensorsDiscretGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretGroup.setStatus("current")
_CtlInternalSensorsDiscretType_Type = OctetString
_CtlInternalSensorsDiscretType_Object = MibTableColumn
ctlInternalSensorsDiscretType = _CtlInternalSensorsDiscretType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 5),
    _CtlInternalSensorsDiscretType_Type()
)
ctlInternalSensorsDiscretType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretType.setStatus("current")


class _CtlInternalSensorsDiscretName_Type(OctetString):
    """Custom type ctlInternalSensorsDiscretName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlInternalSensorsDiscretName_Type.__name__ = "OctetString"
_CtlInternalSensorsDiscretName_Object = MibTableColumn
ctlInternalSensorsDiscretName = _CtlInternalSensorsDiscretName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 6),
    _CtlInternalSensorsDiscretName_Type()
)
ctlInternalSensorsDiscretName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretName.setStatus("current")
_CtlInternalSensorsDiscretState_Type = OctetString
_CtlInternalSensorsDiscretState_Object = MibTableColumn
ctlInternalSensorsDiscretState = _CtlInternalSensorsDiscretState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 7),
    _CtlInternalSensorsDiscretState_Type()
)
ctlInternalSensorsDiscretState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretState.setStatus("current")
_CtlInternalSensorsDiscretValue_Type = Integer32
_CtlInternalSensorsDiscretValue_Object = MibTableColumn
ctlInternalSensorsDiscretValue = _CtlInternalSensorsDiscretValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 8),
    _CtlInternalSensorsDiscretValue_Type()
)
ctlInternalSensorsDiscretValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretValue.setStatus("current")
_CtlInternalSensorsDiscretReset_Type = Integer32
_CtlInternalSensorsDiscretReset_Object = MibTableColumn
ctlInternalSensorsDiscretReset = _CtlInternalSensorsDiscretReset_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 9),
    _CtlInternalSensorsDiscretReset_Type()
)
ctlInternalSensorsDiscretReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretReset.setStatus("current")
_CtlInternalSensorsDiscretLevel_Type = Integer32
_CtlInternalSensorsDiscretLevel_Object = MibTableColumn
ctlInternalSensorsDiscretLevel = _CtlInternalSensorsDiscretLevel_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 10),
    _CtlInternalSensorsDiscretLevel_Type()
)
ctlInternalSensorsDiscretLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretLevel.setStatus("current")
_CtlInternalSensorsDiscretReverse_Type = Integer32
_CtlInternalSensorsDiscretReverse_Object = MibTableColumn
ctlInternalSensorsDiscretReverse = _CtlInternalSensorsDiscretReverse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 11),
    _CtlInternalSensorsDiscretReverse_Type()
)
ctlInternalSensorsDiscretReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretReverse.setStatus("current")
_CtlInternalSensorsDiscretSpecific_Type = OctetString
_CtlInternalSensorsDiscretSpecific_Object = MibTableColumn
ctlInternalSensorsDiscretSpecific = _CtlInternalSensorsDiscretSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 1, 1, 12),
    _CtlInternalSensorsDiscretSpecific_Type()
)
ctlInternalSensorsDiscretSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretSpecific.setStatus("current")
_CtlInternalSensorsAnalogsTable_Object = MibTable
ctlInternalSensorsAnalogsTable = _CtlInternalSensorsAnalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2)
)
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogsTable.setStatus("current")
_CtlInternalSensorsAnalogsEntry_Object = MibTableRow
ctlInternalSensorsAnalogsEntry = _CtlInternalSensorsAnalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1)
)
ctlInternalSensorsAnalogsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlInternalSensorsAnalogId"),
)
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogsEntry.setStatus("current")
_CtlInternalSensorsAnalogId_Type = Integer32
_CtlInternalSensorsAnalogId_Object = MibTableColumn
ctlInternalSensorsAnalogId = _CtlInternalSensorsAnalogId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 1),
    _CtlInternalSensorsAnalogId_Type()
)
ctlInternalSensorsAnalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogId.setStatus("current")
_CtlInternalSensorsAnalogModule_Type = Integer32
_CtlInternalSensorsAnalogModule_Object = MibTableColumn
ctlInternalSensorsAnalogModule = _CtlInternalSensorsAnalogModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 2),
    _CtlInternalSensorsAnalogModule_Type()
)
ctlInternalSensorsAnalogModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogModule.setStatus("current")
_CtlInternalSensorsAnalogNum_Type = Integer32
_CtlInternalSensorsAnalogNum_Object = MibTableColumn
ctlInternalSensorsAnalogNum = _CtlInternalSensorsAnalogNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 3),
    _CtlInternalSensorsAnalogNum_Type()
)
ctlInternalSensorsAnalogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogNum.setStatus("current")
_CtlInternalSensorsAnalogGroup_Type = Integer32
_CtlInternalSensorsAnalogGroup_Object = MibTableColumn
ctlInternalSensorsAnalogGroup = _CtlInternalSensorsAnalogGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 4),
    _CtlInternalSensorsAnalogGroup_Type()
)
ctlInternalSensorsAnalogGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogGroup.setStatus("current")
_CtlInternalSensorsAnalogType_Type = OctetString
_CtlInternalSensorsAnalogType_Object = MibTableColumn
ctlInternalSensorsAnalogType = _CtlInternalSensorsAnalogType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 5),
    _CtlInternalSensorsAnalogType_Type()
)
ctlInternalSensorsAnalogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogType.setStatus("current")


class _CtlInternalSensorsAnalogName_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlInternalSensorsAnalogName_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogName_Object = MibTableColumn
ctlInternalSensorsAnalogName = _CtlInternalSensorsAnalogName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 6),
    _CtlInternalSensorsAnalogName_Type()
)
ctlInternalSensorsAnalogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogName.setStatus("current")
_CtlInternalSensorsAnalogState_Type = OctetString
_CtlInternalSensorsAnalogState_Object = MibTableColumn
ctlInternalSensorsAnalogState = _CtlInternalSensorsAnalogState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 7),
    _CtlInternalSensorsAnalogState_Type()
)
ctlInternalSensorsAnalogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogState.setStatus("current")
_CtlInternalSensorsAnalogValue_Type = OctetString
_CtlInternalSensorsAnalogValue_Object = MibTableColumn
ctlInternalSensorsAnalogValue = _CtlInternalSensorsAnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 8),
    _CtlInternalSensorsAnalogValue_Type()
)
ctlInternalSensorsAnalogValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogValue.setStatus("current")
_CtlInternalSensorsAnalogMin_Type = OctetString
_CtlInternalSensorsAnalogMin_Object = MibTableColumn
ctlInternalSensorsAnalogMin = _CtlInternalSensorsAnalogMin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 9),
    _CtlInternalSensorsAnalogMin_Type()
)
ctlInternalSensorsAnalogMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogMin.setStatus("current")
_CtlInternalSensorsAnalogMax_Type = OctetString
_CtlInternalSensorsAnalogMax_Object = MibTableColumn
ctlInternalSensorsAnalogMax = _CtlInternalSensorsAnalogMax_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 10),
    _CtlInternalSensorsAnalogMax_Type()
)
ctlInternalSensorsAnalogMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogMax.setStatus("current")


class _CtlInternalSensorsAnalogLow_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogLow_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogLow_Object = MibTableColumn
ctlInternalSensorsAnalogLow = _CtlInternalSensorsAnalogLow_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 11),
    _CtlInternalSensorsAnalogLow_Type()
)
ctlInternalSensorsAnalogLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogLow.setStatus("current")


class _CtlInternalSensorsAnalogWarning_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogWarning_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogWarning_Object = MibTableColumn
ctlInternalSensorsAnalogWarning = _CtlInternalSensorsAnalogWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 12),
    _CtlInternalSensorsAnalogWarning_Type()
)
ctlInternalSensorsAnalogWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogWarning.setStatus("current")


class _CtlInternalSensorsAnalogHigh_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogHigh_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogHigh_Object = MibTableColumn
ctlInternalSensorsAnalogHigh = _CtlInternalSensorsAnalogHigh_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 13),
    _CtlInternalSensorsAnalogHigh_Type()
)
ctlInternalSensorsAnalogHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogHigh.setStatus("current")


class _CtlInternalSensorsAnalogAt0_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogAt0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogAt0_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogAt0_Object = MibTableColumn
ctlInternalSensorsAnalogAt0 = _CtlInternalSensorsAnalogAt0_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 14),
    _CtlInternalSensorsAnalogAt0_Type()
)
ctlInternalSensorsAnalogAt0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogAt0.setStatus("current")


class _CtlInternalSensorsAnalogAt75_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogAt75 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CtlInternalSensorsAnalogAt75_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogAt75_Object = MibTableColumn
ctlInternalSensorsAnalogAt75 = _CtlInternalSensorsAnalogAt75_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 15),
    _CtlInternalSensorsAnalogAt75_Type()
)
ctlInternalSensorsAnalogAt75.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogAt75.setStatus("current")


class _CtlInternalSensorsAnalogExpression_Type(OctetString):
    """Custom type ctlInternalSensorsAnalogExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CtlInternalSensorsAnalogExpression_Type.__name__ = "OctetString"
_CtlInternalSensorsAnalogExpression_Object = MibTableColumn
ctlInternalSensorsAnalogExpression = _CtlInternalSensorsAnalogExpression_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 16),
    _CtlInternalSensorsAnalogExpression_Type()
)
ctlInternalSensorsAnalogExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogExpression.setStatus("current")
_CtlInternalSensorsAnalogSpecific_Type = OctetString
_CtlInternalSensorsAnalogSpecific_Object = MibTableColumn
ctlInternalSensorsAnalogSpecific = _CtlInternalSensorsAnalogSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 2, 1, 17),
    _CtlInternalSensorsAnalogSpecific_Type()
)
ctlInternalSensorsAnalogSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsAnalogSpecific.setStatus("current")
_CtlInternalSensorsOutletsTable_Object = MibTable
ctlInternalSensorsOutletsTable = _CtlInternalSensorsOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3)
)
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletsTable.setStatus("current")
_CtlInternalSensorsOutletsEntry_Object = MibTableRow
ctlInternalSensorsOutletsEntry = _CtlInternalSensorsOutletsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1)
)
ctlInternalSensorsOutletsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlInternalSensorsOutletId"),
)
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletsEntry.setStatus("current")
_CtlInternalSensorsOutletId_Type = Integer32
_CtlInternalSensorsOutletId_Object = MibTableColumn
ctlInternalSensorsOutletId = _CtlInternalSensorsOutletId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 1),
    _CtlInternalSensorsOutletId_Type()
)
ctlInternalSensorsOutletId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletId.setStatus("current")
_CtlInternalSensorsOutletModule_Type = Integer32
_CtlInternalSensorsOutletModule_Object = MibTableColumn
ctlInternalSensorsOutletModule = _CtlInternalSensorsOutletModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 2),
    _CtlInternalSensorsOutletModule_Type()
)
ctlInternalSensorsOutletModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletModule.setStatus("current")
_CtlInternalSensorsOutletNum_Type = Integer32
_CtlInternalSensorsOutletNum_Object = MibTableColumn
ctlInternalSensorsOutletNum = _CtlInternalSensorsOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 3),
    _CtlInternalSensorsOutletNum_Type()
)
ctlInternalSensorsOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletNum.setStatus("current")
_CtlInternalSensorsOutletGroup_Type = Integer32
_CtlInternalSensorsOutletGroup_Object = MibTableColumn
ctlInternalSensorsOutletGroup = _CtlInternalSensorsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 4),
    _CtlInternalSensorsOutletGroup_Type()
)
ctlInternalSensorsOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletGroup.setStatus("current")
_CtlInternalSensorsOutletType_Type = OctetString
_CtlInternalSensorsOutletType_Object = MibTableColumn
ctlInternalSensorsOutletType = _CtlInternalSensorsOutletType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 5),
    _CtlInternalSensorsOutletType_Type()
)
ctlInternalSensorsOutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletType.setStatus("current")


class _CtlInternalSensorsOutletName_Type(OctetString):
    """Custom type ctlInternalSensorsOutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlInternalSensorsOutletName_Type.__name__ = "OctetString"
_CtlInternalSensorsOutletName_Object = MibTableColumn
ctlInternalSensorsOutletName = _CtlInternalSensorsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 6),
    _CtlInternalSensorsOutletName_Type()
)
ctlInternalSensorsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletName.setStatus("current")
_CtlInternalSensorsOutletState_Type = OctetString
_CtlInternalSensorsOutletState_Object = MibTableColumn
ctlInternalSensorsOutletState = _CtlInternalSensorsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 7),
    _CtlInternalSensorsOutletState_Type()
)
ctlInternalSensorsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletState.setStatus("current")
_CtlInternalSensorsOutletValue_Type = OctetString
_CtlInternalSensorsOutletValue_Object = MibTableColumn
ctlInternalSensorsOutletValue = _CtlInternalSensorsOutletValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 8),
    _CtlInternalSensorsOutletValue_Type()
)
ctlInternalSensorsOutletValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletValue.setStatus("current")
_CtlInternalSensorsOutletInitial_Type = OctetString
_CtlInternalSensorsOutletInitial_Object = MibTableColumn
ctlInternalSensorsOutletInitial = _CtlInternalSensorsOutletInitial_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 9),
    _CtlInternalSensorsOutletInitial_Type()
)
ctlInternalSensorsOutletInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsOutletInitial.setStatus("current")
_CtlInternalSensorsDiscretPulse_Type = Integer32
_CtlInternalSensorsDiscretPulse_Object = MibTableColumn
ctlInternalSensorsDiscretPulse = _CtlInternalSensorsDiscretPulse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 5, 3, 1, 10),
    _CtlInternalSensorsDiscretPulse_Type()
)
ctlInternalSensorsDiscretPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlInternalSensorsDiscretPulse.setStatus("current")
_CtlCANSensors_ObjectIdentity = ObjectIdentity
ctlCANSensors = _CtlCANSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 6)
)
_CtlCANSensorsDiscretsTable_Object = MibTable
ctlCANSensorsDiscretsTable = _CtlCANSensorsDiscretsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1)
)
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretsTable.setStatus("current")
_CtlCANSensorsDiscretsEntry_Object = MibTableRow
ctlCANSensorsDiscretsEntry = _CtlCANSensorsDiscretsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1)
)
ctlCANSensorsDiscretsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlCANSensorsDiscretId"),
)
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretsEntry.setStatus("current")
_CtlCANSensorsDiscretId_Type = Integer32
_CtlCANSensorsDiscretId_Object = MibTableColumn
ctlCANSensorsDiscretId = _CtlCANSensorsDiscretId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 1),
    _CtlCANSensorsDiscretId_Type()
)
ctlCANSensorsDiscretId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretId.setStatus("current")
_CtlCANSensorsDiscretModule_Type = Integer32
_CtlCANSensorsDiscretModule_Object = MibTableColumn
ctlCANSensorsDiscretModule = _CtlCANSensorsDiscretModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 2),
    _CtlCANSensorsDiscretModule_Type()
)
ctlCANSensorsDiscretModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretModule.setStatus("current")
_CtlCANSensorsDiscretNum_Type = Integer32
_CtlCANSensorsDiscretNum_Object = MibTableColumn
ctlCANSensorsDiscretNum = _CtlCANSensorsDiscretNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 3),
    _CtlCANSensorsDiscretNum_Type()
)
ctlCANSensorsDiscretNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretNum.setStatus("current")
_CtlCANSensorsDiscretGroup_Type = Integer32
_CtlCANSensorsDiscretGroup_Object = MibTableColumn
ctlCANSensorsDiscretGroup = _CtlCANSensorsDiscretGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 4),
    _CtlCANSensorsDiscretGroup_Type()
)
ctlCANSensorsDiscretGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretGroup.setStatus("current")
_CtlCANSensorsDiscretType_Type = OctetString
_CtlCANSensorsDiscretType_Object = MibTableColumn
ctlCANSensorsDiscretType = _CtlCANSensorsDiscretType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 5),
    _CtlCANSensorsDiscretType_Type()
)
ctlCANSensorsDiscretType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretType.setStatus("current")


class _CtlCANSensorsDiscretName_Type(OctetString):
    """Custom type ctlCANSensorsDiscretName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlCANSensorsDiscretName_Type.__name__ = "OctetString"
_CtlCANSensorsDiscretName_Object = MibTableColumn
ctlCANSensorsDiscretName = _CtlCANSensorsDiscretName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 6),
    _CtlCANSensorsDiscretName_Type()
)
ctlCANSensorsDiscretName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretName.setStatus("current")
_CtlCANSensorsDiscretState_Type = OctetString
_CtlCANSensorsDiscretState_Object = MibTableColumn
ctlCANSensorsDiscretState = _CtlCANSensorsDiscretState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 7),
    _CtlCANSensorsDiscretState_Type()
)
ctlCANSensorsDiscretState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretState.setStatus("current")
_CtlCANSensorsDiscretValue_Type = OctetString
_CtlCANSensorsDiscretValue_Object = MibTableColumn
ctlCANSensorsDiscretValue = _CtlCANSensorsDiscretValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 8),
    _CtlCANSensorsDiscretValue_Type()
)
ctlCANSensorsDiscretValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretValue.setStatus("current")
_CtlCANSensorsDiscretReset_Type = Integer32
_CtlCANSensorsDiscretReset_Object = MibTableColumn
ctlCANSensorsDiscretReset = _CtlCANSensorsDiscretReset_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 9),
    _CtlCANSensorsDiscretReset_Type()
)
ctlCANSensorsDiscretReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretReset.setStatus("current")
_CtlCANSensorsDiscretLevel_Type = Integer32
_CtlCANSensorsDiscretLevel_Object = MibTableColumn
ctlCANSensorsDiscretLevel = _CtlCANSensorsDiscretLevel_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 10),
    _CtlCANSensorsDiscretLevel_Type()
)
ctlCANSensorsDiscretLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretLevel.setStatus("current")
_CtlCANSensorsDiscretReverse_Type = Integer32
_CtlCANSensorsDiscretReverse_Object = MibTableColumn
ctlCANSensorsDiscretReverse = _CtlCANSensorsDiscretReverse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 11),
    _CtlCANSensorsDiscretReverse_Type()
)
ctlCANSensorsDiscretReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretReverse.setStatus("current")
_CtlCANSensorsDiscretSpecific_Type = OctetString
_CtlCANSensorsDiscretSpecific_Object = MibTableColumn
ctlCANSensorsDiscretSpecific = _CtlCANSensorsDiscretSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 1, 1, 12),
    _CtlCANSensorsDiscretSpecific_Type()
)
ctlCANSensorsDiscretSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretSpecific.setStatus("current")
_CtlCANSensorsAnalogsTable_Object = MibTable
ctlCANSensorsAnalogsTable = _CtlCANSensorsAnalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2)
)
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogsTable.setStatus("current")
_CtlCANSensorsAnalogsEntry_Object = MibTableRow
ctlCANSensorsAnalogsEntry = _CtlCANSensorsAnalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1)
)
ctlCANSensorsAnalogsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlCANSensorsAnalogId"),
)
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogsEntry.setStatus("current")
_CtlCANSensorsAnalogId_Type = Integer32
_CtlCANSensorsAnalogId_Object = MibTableColumn
ctlCANSensorsAnalogId = _CtlCANSensorsAnalogId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 1),
    _CtlCANSensorsAnalogId_Type()
)
ctlCANSensorsAnalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogId.setStatus("current")
_CtlCANSensorsAnalogModule_Type = Integer32
_CtlCANSensorsAnalogModule_Object = MibTableColumn
ctlCANSensorsAnalogModule = _CtlCANSensorsAnalogModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 2),
    _CtlCANSensorsAnalogModule_Type()
)
ctlCANSensorsAnalogModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogModule.setStatus("current")
_CtlCANSensorsAnalogNum_Type = Integer32
_CtlCANSensorsAnalogNum_Object = MibTableColumn
ctlCANSensorsAnalogNum = _CtlCANSensorsAnalogNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 3),
    _CtlCANSensorsAnalogNum_Type()
)
ctlCANSensorsAnalogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogNum.setStatus("current")
_CtlCANSensorsAnalogGroup_Type = Integer32
_CtlCANSensorsAnalogGroup_Object = MibTableColumn
ctlCANSensorsAnalogGroup = _CtlCANSensorsAnalogGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 4),
    _CtlCANSensorsAnalogGroup_Type()
)
ctlCANSensorsAnalogGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogGroup.setStatus("current")
_CtlCANSensorsAnalogType_Type = OctetString
_CtlCANSensorsAnalogType_Object = MibTableColumn
ctlCANSensorsAnalogType = _CtlCANSensorsAnalogType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 5),
    _CtlCANSensorsAnalogType_Type()
)
ctlCANSensorsAnalogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogType.setStatus("current")


class _CtlCANSensorsAnalogName_Type(OctetString):
    """Custom type ctlCANSensorsAnalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlCANSensorsAnalogName_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogName_Object = MibTableColumn
ctlCANSensorsAnalogName = _CtlCANSensorsAnalogName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 6),
    _CtlCANSensorsAnalogName_Type()
)
ctlCANSensorsAnalogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogName.setStatus("current")
_CtlCANSensorsAnalogState_Type = OctetString
_CtlCANSensorsAnalogState_Object = MibTableColumn
ctlCANSensorsAnalogState = _CtlCANSensorsAnalogState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 7),
    _CtlCANSensorsAnalogState_Type()
)
ctlCANSensorsAnalogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogState.setStatus("current")
_CtlCANSensorsAnalogValue_Type = OctetString
_CtlCANSensorsAnalogValue_Object = MibTableColumn
ctlCANSensorsAnalogValue = _CtlCANSensorsAnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 8),
    _CtlCANSensorsAnalogValue_Type()
)
ctlCANSensorsAnalogValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogValue.setStatus("current")
_CtlCANSensorsAnalogMin_Type = OctetString
_CtlCANSensorsAnalogMin_Object = MibTableColumn
ctlCANSensorsAnalogMin = _CtlCANSensorsAnalogMin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 9),
    _CtlCANSensorsAnalogMin_Type()
)
ctlCANSensorsAnalogMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogMin.setStatus("current")
_CtlCANSensorsAnalogMax_Type = OctetString
_CtlCANSensorsAnalogMax_Object = MibTableColumn
ctlCANSensorsAnalogMax = _CtlCANSensorsAnalogMax_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 10),
    _CtlCANSensorsAnalogMax_Type()
)
ctlCANSensorsAnalogMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogMax.setStatus("current")


class _CtlCANSensorsAnalogLow_Type(OctetString):
    """Custom type ctlCANSensorsAnalogLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogLow_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogLow_Object = MibTableColumn
ctlCANSensorsAnalogLow = _CtlCANSensorsAnalogLow_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 11),
    _CtlCANSensorsAnalogLow_Type()
)
ctlCANSensorsAnalogLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogLow.setStatus("current")


class _CtlCANSensorsAnalogWarning_Type(OctetString):
    """Custom type ctlCANSensorsAnalogWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogWarning_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogWarning_Object = MibTableColumn
ctlCANSensorsAnalogWarning = _CtlCANSensorsAnalogWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 12),
    _CtlCANSensorsAnalogWarning_Type()
)
ctlCANSensorsAnalogWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogWarning.setStatus("current")


class _CtlCANSensorsAnalogHigh_Type(OctetString):
    """Custom type ctlCANSensorsAnalogHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogHigh_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogHigh_Object = MibTableColumn
ctlCANSensorsAnalogHigh = _CtlCANSensorsAnalogHigh_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 13),
    _CtlCANSensorsAnalogHigh_Type()
)
ctlCANSensorsAnalogHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogHigh.setStatus("current")


class _CtlCANSensorsAnalogAt0_Type(OctetString):
    """Custom type ctlCANSensorsAnalogAt0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogAt0_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogAt0_Object = MibTableColumn
ctlCANSensorsAnalogAt0 = _CtlCANSensorsAnalogAt0_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 14),
    _CtlCANSensorsAnalogAt0_Type()
)
ctlCANSensorsAnalogAt0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogAt0.setStatus("current")


class _CtlCANSensorsAnalogAt75_Type(OctetString):
    """Custom type ctlCANSensorsAnalogAt75 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogAt75_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogAt75_Object = MibTableColumn
ctlCANSensorsAnalogAt75 = _CtlCANSensorsAnalogAt75_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 15),
    _CtlCANSensorsAnalogAt75_Type()
)
ctlCANSensorsAnalogAt75.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogAt75.setStatus("current")


class _CtlCANSensorsAnalogExpression_Type(OctetString):
    """Custom type ctlCANSensorsAnalogExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 80),
    )


_CtlCANSensorsAnalogExpression_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogExpression_Object = MibTableColumn
ctlCANSensorsAnalogExpression = _CtlCANSensorsAnalogExpression_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 16),
    _CtlCANSensorsAnalogExpression_Type()
)
ctlCANSensorsAnalogExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogExpression.setStatus("current")


class _CtlCANSensorsAnalogSpecific_Type(OctetString):
    """Custom type ctlCANSensorsAnalogSpecific based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlCANSensorsAnalogSpecific_Type.__name__ = "OctetString"
_CtlCANSensorsAnalogSpecific_Object = MibTableColumn
ctlCANSensorsAnalogSpecific = _CtlCANSensorsAnalogSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 2, 1, 17),
    _CtlCANSensorsAnalogSpecific_Type()
)
ctlCANSensorsAnalogSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsAnalogSpecific.setStatus("current")
_CtlCANSensorsOutletsTable_Object = MibTable
ctlCANSensorsOutletsTable = _CtlCANSensorsOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3)
)
if mibBuilder.loadTexts:
    ctlCANSensorsOutletsTable.setStatus("current")
_CtlCANSensorsOutletsEntry_Object = MibTableRow
ctlCANSensorsOutletsEntry = _CtlCANSensorsOutletsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1)
)
ctlCANSensorsOutletsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlCANSensorsOutletId"),
)
if mibBuilder.loadTexts:
    ctlCANSensorsOutletsEntry.setStatus("current")
_CtlCANSensorsOutletId_Type = Integer32
_CtlCANSensorsOutletId_Object = MibTableColumn
ctlCANSensorsOutletId = _CtlCANSensorsOutletId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 1),
    _CtlCANSensorsOutletId_Type()
)
ctlCANSensorsOutletId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletId.setStatus("current")
_CtlCANSensorsOutletModule_Type = Integer32
_CtlCANSensorsOutletModule_Object = MibTableColumn
ctlCANSensorsOutletModule = _CtlCANSensorsOutletModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 2),
    _CtlCANSensorsOutletModule_Type()
)
ctlCANSensorsOutletModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletModule.setStatus("current")
_CtlCANSensorsOutletNum_Type = Integer32
_CtlCANSensorsOutletNum_Object = MibTableColumn
ctlCANSensorsOutletNum = _CtlCANSensorsOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 3),
    _CtlCANSensorsOutletNum_Type()
)
ctlCANSensorsOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletNum.setStatus("current")
_CtlCANSensorsOutletGroup_Type = Integer32
_CtlCANSensorsOutletGroup_Object = MibTableColumn
ctlCANSensorsOutletGroup = _CtlCANSensorsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 4),
    _CtlCANSensorsOutletGroup_Type()
)
ctlCANSensorsOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletGroup.setStatus("current")
_CtlCANSensorsOutletType_Type = OctetString
_CtlCANSensorsOutletType_Object = MibTableColumn
ctlCANSensorsOutletType = _CtlCANSensorsOutletType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 5),
    _CtlCANSensorsOutletType_Type()
)
ctlCANSensorsOutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletType.setStatus("current")


class _CtlCANSensorsOutletName_Type(OctetString):
    """Custom type ctlCANSensorsOutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlCANSensorsOutletName_Type.__name__ = "OctetString"
_CtlCANSensorsOutletName_Object = MibTableColumn
ctlCANSensorsOutletName = _CtlCANSensorsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 6),
    _CtlCANSensorsOutletName_Type()
)
ctlCANSensorsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletName.setStatus("current")
_CtlCANSensorsOutletState_Type = OctetString
_CtlCANSensorsOutletState_Object = MibTableColumn
ctlCANSensorsOutletState = _CtlCANSensorsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 7),
    _CtlCANSensorsOutletState_Type()
)
ctlCANSensorsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletState.setStatus("current")
_CtlCANSensorsOutletValue_Type = OctetString
_CtlCANSensorsOutletValue_Object = MibTableColumn
ctlCANSensorsOutletValue = _CtlCANSensorsOutletValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 8),
    _CtlCANSensorsOutletValue_Type()
)
ctlCANSensorsOutletValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletValue.setStatus("current")
_CtlCANSensorsOutletInitial_Type = OctetString
_CtlCANSensorsOutletInitial_Object = MibTableColumn
ctlCANSensorsOutletInitial = _CtlCANSensorsOutletInitial_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 9),
    _CtlCANSensorsOutletInitial_Type()
)
ctlCANSensorsOutletInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsOutletInitial.setStatus("current")
_CtlCANSensorsDiscretPulse_Type = Integer32
_CtlCANSensorsDiscretPulse_Object = MibTableColumn
ctlCANSensorsDiscretPulse = _CtlCANSensorsDiscretPulse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 6, 3, 1, 10),
    _CtlCANSensorsDiscretPulse_Type()
)
ctlCANSensorsDiscretPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCANSensorsDiscretPulse.setStatus("current")
_CtlRsSensors_ObjectIdentity = ObjectIdentity
ctlRsSensors = _CtlRsSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39052, 7)
)
_CtlRsSensorsDiscretsTable_Object = MibTable
ctlRsSensorsDiscretsTable = _CtlRsSensorsDiscretsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1)
)
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretsTable.setStatus("current")
_CtlRsSensorsDiscretsEntry_Object = MibTableRow
ctlRsSensorsDiscretsEntry = _CtlRsSensorsDiscretsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1)
)
ctlRsSensorsDiscretsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlRsSensorsDiscretId"),
)
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretsEntry.setStatus("current")
_CtlRsSensorsDiscretId_Type = Integer32
_CtlRsSensorsDiscretId_Object = MibTableColumn
ctlRsSensorsDiscretId = _CtlRsSensorsDiscretId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 1),
    _CtlRsSensorsDiscretId_Type()
)
ctlRsSensorsDiscretId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretId.setStatus("current")
_CtlRsSensorsDiscretModule_Type = Integer32
_CtlRsSensorsDiscretModule_Object = MibTableColumn
ctlRsSensorsDiscretModule = _CtlRsSensorsDiscretModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 2),
    _CtlRsSensorsDiscretModule_Type()
)
ctlRsSensorsDiscretModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretModule.setStatus("current")
_CtlRsSensorsDiscretNum_Type = Integer32
_CtlRsSensorsDiscretNum_Object = MibTableColumn
ctlRsSensorsDiscretNum = _CtlRsSensorsDiscretNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 3),
    _CtlRsSensorsDiscretNum_Type()
)
ctlRsSensorsDiscretNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretNum.setStatus("current")
_CtlRsSensorsDiscretGroup_Type = Integer32
_CtlRsSensorsDiscretGroup_Object = MibTableColumn
ctlRsSensorsDiscretGroup = _CtlRsSensorsDiscretGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 4),
    _CtlRsSensorsDiscretGroup_Type()
)
ctlRsSensorsDiscretGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretGroup.setStatus("current")
_CtlRsSensorsDiscretType_Type = OctetString
_CtlRsSensorsDiscretType_Object = MibTableColumn
ctlRsSensorsDiscretType = _CtlRsSensorsDiscretType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 5),
    _CtlRsSensorsDiscretType_Type()
)
ctlRsSensorsDiscretType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretType.setStatus("current")


class _CtlRsSensorsDiscretName_Type(OctetString):
    """Custom type ctlRsSensorsDiscretName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlRsSensorsDiscretName_Type.__name__ = "OctetString"
_CtlRsSensorsDiscretName_Object = MibTableColumn
ctlRsSensorsDiscretName = _CtlRsSensorsDiscretName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 6),
    _CtlRsSensorsDiscretName_Type()
)
ctlRsSensorsDiscretName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretName.setStatus("current")
_CtlRsSensorsDiscretState_Type = OctetString
_CtlRsSensorsDiscretState_Object = MibTableColumn
ctlRsSensorsDiscretState = _CtlRsSensorsDiscretState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 7),
    _CtlRsSensorsDiscretState_Type()
)
ctlRsSensorsDiscretState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretState.setStatus("current")
_CtlRsSensorsDiscretValue_Type = OctetString
_CtlRsSensorsDiscretValue_Object = MibTableColumn
ctlRsSensorsDiscretValue = _CtlRsSensorsDiscretValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 8),
    _CtlRsSensorsDiscretValue_Type()
)
ctlRsSensorsDiscretValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretValue.setStatus("current")
_CtlRsSensorsDiscretReset_Type = Integer32
_CtlRsSensorsDiscretReset_Object = MibTableColumn
ctlRsSensorsDiscretReset = _CtlRsSensorsDiscretReset_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 9),
    _CtlRsSensorsDiscretReset_Type()
)
ctlRsSensorsDiscretReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretReset.setStatus("current")
_CtlRsSensorsDiscretLevel_Type = Integer32
_CtlRsSensorsDiscretLevel_Object = MibTableColumn
ctlRsSensorsDiscretLevel = _CtlRsSensorsDiscretLevel_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 10),
    _CtlRsSensorsDiscretLevel_Type()
)
ctlRsSensorsDiscretLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretLevel.setStatus("current")
_CtlRsSensorsDiscretReverse_Type = Integer32
_CtlRsSensorsDiscretReverse_Object = MibTableColumn
ctlRsSensorsDiscretReverse = _CtlRsSensorsDiscretReverse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 11),
    _CtlRsSensorsDiscretReverse_Type()
)
ctlRsSensorsDiscretReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretReverse.setStatus("current")
_CtlRsSensorsDiscretSpecific_Type = OctetString
_CtlRsSensorsDiscretSpecific_Object = MibTableColumn
ctlRsSensorsDiscretSpecific = _CtlRsSensorsDiscretSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 1, 1, 12),
    _CtlRsSensorsDiscretSpecific_Type()
)
ctlRsSensorsDiscretSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretSpecific.setStatus("current")
_CtlRsSensorsAnalogsTable_Object = MibTable
ctlRsSensorsAnalogsTable = _CtlRsSensorsAnalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2)
)
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogsTable.setStatus("current")
_CtlRsSensorsAnalogsEntry_Object = MibTableRow
ctlRsSensorsAnalogsEntry = _CtlRsSensorsAnalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1)
)
ctlRsSensorsAnalogsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlRsSensorsAnalogId"),
)
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogsEntry.setStatus("current")
_CtlRsSensorsAnalogId_Type = Integer32
_CtlRsSensorsAnalogId_Object = MibTableColumn
ctlRsSensorsAnalogId = _CtlRsSensorsAnalogId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 1),
    _CtlRsSensorsAnalogId_Type()
)
ctlRsSensorsAnalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogId.setStatus("current")
_CtlRsSensorsAnalogModule_Type = Integer32
_CtlRsSensorsAnalogModule_Object = MibTableColumn
ctlRsSensorsAnalogModule = _CtlRsSensorsAnalogModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 2),
    _CtlRsSensorsAnalogModule_Type()
)
ctlRsSensorsAnalogModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogModule.setStatus("current")
_CtlRsSensorsAnalogNum_Type = Integer32
_CtlRsSensorsAnalogNum_Object = MibTableColumn
ctlRsSensorsAnalogNum = _CtlRsSensorsAnalogNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 3),
    _CtlRsSensorsAnalogNum_Type()
)
ctlRsSensorsAnalogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogNum.setStatus("current")
_CtlRsSensorsAnalogGroup_Type = Integer32
_CtlRsSensorsAnalogGroup_Object = MibTableColumn
ctlRsSensorsAnalogGroup = _CtlRsSensorsAnalogGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 4),
    _CtlRsSensorsAnalogGroup_Type()
)
ctlRsSensorsAnalogGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogGroup.setStatus("current")
_CtlRsSensorsAnalogType_Type = OctetString
_CtlRsSensorsAnalogType_Object = MibTableColumn
ctlRsSensorsAnalogType = _CtlRsSensorsAnalogType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 5),
    _CtlRsSensorsAnalogType_Type()
)
ctlRsSensorsAnalogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogType.setStatus("current")


class _CtlRsSensorsAnalogName_Type(OctetString):
    """Custom type ctlRsSensorsAnalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlRsSensorsAnalogName_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogName_Object = MibTableColumn
ctlRsSensorsAnalogName = _CtlRsSensorsAnalogName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 6),
    _CtlRsSensorsAnalogName_Type()
)
ctlRsSensorsAnalogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogName.setStatus("current")
_CtlRsSensorsAnalogState_Type = OctetString
_CtlRsSensorsAnalogState_Object = MibTableColumn
ctlRsSensorsAnalogState = _CtlRsSensorsAnalogState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 7),
    _CtlRsSensorsAnalogState_Type()
)
ctlRsSensorsAnalogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogState.setStatus("current")
_CtlRsSensorsAnalogValue_Type = OctetString
_CtlRsSensorsAnalogValue_Object = MibTableColumn
ctlRsSensorsAnalogValue = _CtlRsSensorsAnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 8),
    _CtlRsSensorsAnalogValue_Type()
)
ctlRsSensorsAnalogValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogValue.setStatus("current")
_CtlRsSensorsAnalogMin_Type = OctetString
_CtlRsSensorsAnalogMin_Object = MibTableColumn
ctlRsSensorsAnalogMin = _CtlRsSensorsAnalogMin_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 9),
    _CtlRsSensorsAnalogMin_Type()
)
ctlRsSensorsAnalogMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogMin.setStatus("current")
_CtlRsSensorsAnalogMax_Type = OctetString
_CtlRsSensorsAnalogMax_Object = MibTableColumn
ctlRsSensorsAnalogMax = _CtlRsSensorsAnalogMax_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 10),
    _CtlRsSensorsAnalogMax_Type()
)
ctlRsSensorsAnalogMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogMax.setStatus("current")


class _CtlRsSensorsAnalogLow_Type(OctetString):
    """Custom type ctlRsSensorsAnalogLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogLow_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogLow_Object = MibTableColumn
ctlRsSensorsAnalogLow = _CtlRsSensorsAnalogLow_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 11),
    _CtlRsSensorsAnalogLow_Type()
)
ctlRsSensorsAnalogLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogLow.setStatus("current")


class _CtlRsSensorsAnalogWarning_Type(OctetString):
    """Custom type ctlRsSensorsAnalogWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogWarning_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogWarning_Object = MibTableColumn
ctlRsSensorsAnalogWarning = _CtlRsSensorsAnalogWarning_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 12),
    _CtlRsSensorsAnalogWarning_Type()
)
ctlRsSensorsAnalogWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogWarning.setStatus("current")


class _CtlRsSensorsAnalogHigh_Type(OctetString):
    """Custom type ctlRsSensorsAnalogHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogHigh_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogHigh_Object = MibTableColumn
ctlRsSensorsAnalogHigh = _CtlRsSensorsAnalogHigh_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 13),
    _CtlRsSensorsAnalogHigh_Type()
)
ctlRsSensorsAnalogHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogHigh.setStatus("current")


class _CtlRsSensorsAnalogAt0_Type(OctetString):
    """Custom type ctlRsSensorsAnalogAt0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogAt0_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogAt0_Object = MibTableColumn
ctlRsSensorsAnalogAt0 = _CtlRsSensorsAnalogAt0_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 14),
    _CtlRsSensorsAnalogAt0_Type()
)
ctlRsSensorsAnalogAt0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogAt0.setStatus("current")


class _CtlRsSensorsAnalogAt75_Type(OctetString):
    """Custom type ctlRsSensorsAnalogAt75 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogAt75_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogAt75_Object = MibTableColumn
ctlRsSensorsAnalogAt75 = _CtlRsSensorsAnalogAt75_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 15),
    _CtlRsSensorsAnalogAt75_Type()
)
ctlRsSensorsAnalogAt75.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogAt75.setStatus("current")


class _CtlRsSensorsAnalogExpression_Type(OctetString):
    """Custom type ctlRsSensorsAnalogExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 80),
    )


_CtlRsSensorsAnalogExpression_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogExpression_Object = MibTableColumn
ctlRsSensorsAnalogExpression = _CtlRsSensorsAnalogExpression_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 16),
    _CtlRsSensorsAnalogExpression_Type()
)
ctlRsSensorsAnalogExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogExpression.setStatus("current")


class _CtlRsSensorsAnalogSpecific_Type(OctetString):
    """Custom type ctlRsSensorsAnalogSpecific based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_CtlRsSensorsAnalogSpecific_Type.__name__ = "OctetString"
_CtlRsSensorsAnalogSpecific_Object = MibTableColumn
ctlRsSensorsAnalogSpecific = _CtlRsSensorsAnalogSpecific_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 2, 1, 17),
    _CtlRsSensorsAnalogSpecific_Type()
)
ctlRsSensorsAnalogSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsAnalogSpecific.setStatus("current")
_CtlRsSensorsOutletsTable_Object = MibTable
ctlRsSensorsOutletsTable = _CtlRsSensorsOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3)
)
if mibBuilder.loadTexts:
    ctlRsSensorsOutletsTable.setStatus("current")
_CtlRsSensorsOutletsEntry_Object = MibTableRow
ctlRsSensorsOutletsEntry = _CtlRsSensorsOutletsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1)
)
ctlRsSensorsOutletsEntry.setIndexNames(
    (0, "SKYCONTROL-SYSTEM-MIB", "ctlRsSensorsOutletId"),
)
if mibBuilder.loadTexts:
    ctlRsSensorsOutletsEntry.setStatus("current")
_CtlRsSensorsOutletId_Type = Integer32
_CtlRsSensorsOutletId_Object = MibTableColumn
ctlRsSensorsOutletId = _CtlRsSensorsOutletId_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 1),
    _CtlRsSensorsOutletId_Type()
)
ctlRsSensorsOutletId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletId.setStatus("current")
_CtlRsSensorsOutletModule_Type = Integer32
_CtlRsSensorsOutletModule_Object = MibTableColumn
ctlRsSensorsOutletModule = _CtlRsSensorsOutletModule_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 2),
    _CtlRsSensorsOutletModule_Type()
)
ctlRsSensorsOutletModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletModule.setStatus("current")
_CtlRsSensorsOutletNum_Type = Integer32
_CtlRsSensorsOutletNum_Object = MibTableColumn
ctlRsSensorsOutletNum = _CtlRsSensorsOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 3),
    _CtlRsSensorsOutletNum_Type()
)
ctlRsSensorsOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletNum.setStatus("current")
_CtlRsSensorsOutletGroup_Type = Integer32
_CtlRsSensorsOutletGroup_Object = MibTableColumn
ctlRsSensorsOutletGroup = _CtlRsSensorsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 4),
    _CtlRsSensorsOutletGroup_Type()
)
ctlRsSensorsOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletGroup.setStatus("current")
_CtlRsSensorsOutletType_Type = OctetString
_CtlRsSensorsOutletType_Object = MibTableColumn
ctlRsSensorsOutletType = _CtlRsSensorsOutletType_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 5),
    _CtlRsSensorsOutletType_Type()
)
ctlRsSensorsOutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletType.setStatus("current")


class _CtlRsSensorsOutletName_Type(OctetString):
    """Custom type ctlRsSensorsOutletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_CtlRsSensorsOutletName_Type.__name__ = "OctetString"
_CtlRsSensorsOutletName_Object = MibTableColumn
ctlRsSensorsOutletName = _CtlRsSensorsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 6),
    _CtlRsSensorsOutletName_Type()
)
ctlRsSensorsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletName.setStatus("current")
_CtlRsSensorsOutletState_Type = OctetString
_CtlRsSensorsOutletState_Object = MibTableColumn
ctlRsSensorsOutletState = _CtlRsSensorsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 7),
    _CtlRsSensorsOutletState_Type()
)
ctlRsSensorsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletState.setStatus("current")
_CtlRsSensorsOutletValue_Type = OctetString
_CtlRsSensorsOutletValue_Object = MibTableColumn
ctlRsSensorsOutletValue = _CtlRsSensorsOutletValue_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 8),
    _CtlRsSensorsOutletValue_Type()
)
ctlRsSensorsOutletValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletValue.setStatus("current")
_CtlRsSensorsOutletInitial_Type = OctetString
_CtlRsSensorsOutletInitial_Object = MibTableColumn
ctlRsSensorsOutletInitial = _CtlRsSensorsOutletInitial_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 9),
    _CtlRsSensorsOutletInitial_Type()
)
ctlRsSensorsOutletInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsOutletInitial.setStatus("current")
_CtlRsSensorsDiscretPulse_Type = Integer32
_CtlRsSensorsDiscretPulse_Object = MibTableColumn
ctlRsSensorsDiscretPulse = _CtlRsSensorsDiscretPulse_Object(
    (1, 3, 6, 1, 4, 1, 39052, 7, 3, 1, 10),
    _CtlRsSensorsDiscretPulse_Type()
)
ctlRsSensorsDiscretPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlRsSensorsDiscretPulse.setStatus("current")

# Managed Objects groups


# Notification objects

ctlUnitTrapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 39052, 1, 5)
)
if mibBuilder.loadTexts:
    ctlUnitTrapNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SKYCONTROL-SYSTEM-MIB",
    **{"skycontrol": skycontrol,
       "ctlUnit": ctlUnit,
       "ctlUnitModulesTable": ctlUnitModulesTable,
       "ctlUnitModulesEntry": ctlUnitModulesEntry,
       "ctlUnitModuleId": ctlUnitModuleId,
       "ctlUnitModulePcode": ctlUnitModulePcode,
       "ctlUnitModuleSN": ctlUnitModuleSN,
       "ctlUnitModuleClass": ctlUnitModuleClass,
       "ctlUnitModuleType": ctlUnitModuleType,
       "ctlUnitModuleName": ctlUnitModuleName,
       "ctlUnitModuleState": ctlUnitModuleState,
       "ctlUnitGroupsTable": ctlUnitGroupsTable,
       "ctlUnitGroupsEntry": ctlUnitGroupsEntry,
       "ctlUnitGroupId": ctlUnitGroupId,
       "ctlUnitGroupName": ctlUnitGroupName,
       "ctlUnitGroupDesc": ctlUnitGroupDesc,
       "ctlUnitElementsTable": ctlUnitElementsTable,
       "ctlUnitElementsEntry": ctlUnitElementsEntry,
       "ctlUnitElementId": ctlUnitElementId,
       "ctlUnitElementGroup": ctlUnitElementGroup,
       "ctlUnitElementModule": ctlUnitElementModule,
       "ctlUnitElementNum": ctlUnitElementNum,
       "ctlUnitElementClass": ctlUnitElementClass,
       "ctlUnitElementType": ctlUnitElementType,
       "ctlUnitElementName": ctlUnitElementName,
       "ctlUnitElementState": ctlUnitElementState,
       "ctlUnitElementValue": ctlUnitElementValue,
       "ctlUnitElementSpec": ctlUnitElementSpec,
       "ctlUnitLogicsTable": ctlUnitLogicsTable,
       "ctlUnitLogicsEntry": ctlUnitLogicsEntry,
       "ctlUnitLogicId": ctlUnitLogicId,
       "ctlUnitLogicName": ctlUnitLogicName,
       "ctlUnitLogicDesc": ctlUnitLogicDesc,
       "ctlUnitLogicDisable": ctlUnitLogicDisable,
       "ctlUnitLogicRowStatus": ctlUnitLogicRowStatus,
       "ctlUnitTrapNotification": ctlUnitTrapNotification,
       "ctlUnitSaveToFlash": ctlUnitSaveToFlash,
       "ctlNotifiers": ctlNotifiers,
       "ctlNotifiersMailersTable": ctlNotifiersMailersTable,
       "ctlNotifiersMailersEntry": ctlNotifiersMailersEntry,
       "ctlNotifiersMailerId": ctlNotifiersMailerId,
       "ctlNotifiersMailerModule": ctlNotifiersMailerModule,
       "ctlNotifiersMailerNum": ctlNotifiersMailerNum,
       "ctlNotifiersMailerGroup": ctlNotifiersMailerGroup,
       "ctlNotifiersMailerType": ctlNotifiersMailerType,
       "ctlNotifiersMailerName": ctlNotifiersMailerName,
       "ctlNotifiersMailerState": ctlNotifiersMailerState,
       "ctlNotifiersMailerValue": ctlNotifiersMailerValue,
       "ctlNotifiersMailerServer": ctlNotifiersMailerServer,
       "ctlNotifiersMailerPort": ctlNotifiersMailerPort,
       "ctlNotifiersMailerLogin": ctlNotifiersMailerLogin,
       "ctlNotifiersMailerPassword": ctlNotifiersMailerPassword,
       "ctlNotifiersMailersTo": ctlNotifiersMailersTo,
       "ctlNotifiersMailersFrom": ctlNotifiersMailersFrom,
       "ctlNotifiersMailerMessage": ctlNotifiersMailerMessage,
       "ctlNotifiersTrapsTable": ctlNotifiersTrapsTable,
       "ctlNotifiersTrapsEntry": ctlNotifiersTrapsEntry,
       "ctlNotifiersTrapId": ctlNotifiersTrapId,
       "ctlNotifiersTrapModule": ctlNotifiersTrapModule,
       "ctlNotifiersTrapNum": ctlNotifiersTrapNum,
       "ctlNotifiersTrapGroup": ctlNotifiersTrapGroup,
       "ctlNotifiersTrapType": ctlNotifiersTrapType,
       "ctlNotifiersTrapName": ctlNotifiersTrapName,
       "ctlNotifiersTrapState": ctlNotifiersTrapState,
       "ctlNotifiersTrapValue": ctlNotifiersTrapValue,
       "ctlNotifiersTrapServer": ctlNotifiersTrapServer,
       "ctlNotifiersTrapPort": ctlNotifiersTrapPort,
       "ctlNotifiersTrapVersion": ctlNotifiersTrapVersion,
       "ctlNotifiersTrapCommunity": ctlNotifiersTrapCommunity,
       "ctlNotifiersSMSsTable": ctlNotifiersSMSsTable,
       "ctlNotifiersSMSsEntry": ctlNotifiersSMSsEntry,
       "ctlNotifiersSMSId": ctlNotifiersSMSId,
       "ctlNotifiersSMSModule": ctlNotifiersSMSModule,
       "ctlNotifiersSMSNum": ctlNotifiersSMSNum,
       "ctlNotifiersSMSGroup": ctlNotifiersSMSGroup,
       "ctlNotifiersSMSType": ctlNotifiersSMSType,
       "ctlNotifiersSMSName": ctlNotifiersSMSName,
       "ctlNotifiersSMSState": ctlNotifiersSMSState,
       "ctlNotifiersSMSValue": ctlNotifiersSMSValue,
       "ctlNotifiersSMSTo": ctlNotifiersSMSTo,
       "ctlNotifiersSMSMessage": ctlNotifiersSMSMessage,
       "ctlVirtualDevices": ctlVirtualDevices,
       "ctlVirtualDevicesTimersTable": ctlVirtualDevicesTimersTable,
       "ctlVirtualDevicesTimersEntry": ctlVirtualDevicesTimersEntry,
       "ctlVirtualDevicesTimerId": ctlVirtualDevicesTimerId,
       "ctlVirtualDevicesTimerModule": ctlVirtualDevicesTimerModule,
       "ctlVirtualDevicesTimerNum": ctlVirtualDevicesTimerNum,
       "ctlVirtualDevicesTimerGroup": ctlVirtualDevicesTimerGroup,
       "ctlVirtualDevicesTimerType": ctlVirtualDevicesTimerType,
       "ctlVirtualDevicesTimerName": ctlVirtualDevicesTimerName,
       "ctlVirtualDevicesTimerState": ctlVirtualDevicesTimerState,
       "ctlVirtualDevicesTimerValue": ctlVirtualDevicesTimerValue,
       "ctlVirtualDevicesTimerBegin": ctlVirtualDevicesTimerBegin,
       "ctlVirtualDevicesTimerEnd": ctlVirtualDevicesTimerEnd,
       "ctlVirtualDevicesTimerDays": ctlVirtualDevicesTimerDays,
       "ctlVirtualDevicesTimerMode": ctlVirtualDevicesTimerMode,
       "ctlVirtualDevicesPingsTable": ctlVirtualDevicesPingsTable,
       "ctlVirtualDevicesPingsEntry": ctlVirtualDevicesPingsEntry,
       "ctlVirtualDevicesPingId": ctlVirtualDevicesPingId,
       "ctlVirtualDevicesPingModule": ctlVirtualDevicesPingModule,
       "ctlVirtualDevicesPingNum": ctlVirtualDevicesPingNum,
       "ctlVirtualDevicesPingGroup": ctlVirtualDevicesPingGroup,
       "ctlVirtualDevicesPingType": ctlVirtualDevicesPingType,
       "ctlVirtualDevicesPingName": ctlVirtualDevicesPingName,
       "ctlVirtualDevicesPingState": ctlVirtualDevicesPingState,
       "ctlVirtualDevicesPingValue": ctlVirtualDevicesPingValue,
       "ctlVirtualDevicesPingPeriod": ctlVirtualDevicesPingPeriod,
       "ctlVirtualDevicesPingRTT": ctlVirtualDevicesPingRTT,
       "ctlVirtualDevicesPingServer": ctlVirtualDevicesPingServer,
       "ctlVirtualDevicesPingIP": ctlVirtualDevicesPingIP,
       "ctlVirtualDevicesPingSent": ctlVirtualDevicesPingSent,
       "ctlVirtualDevicesPingReceived": ctlVirtualDevicesPingReceived,
       "ctlVirtualDevicesPingStatus": ctlVirtualDevicesPingStatus,
       "ctlHardwareDevices": ctlHardwareDevices,
       "ctlHardwareDevicesCamerasTable": ctlHardwareDevicesCamerasTable,
       "ctlHardwareDevicesCamerasEntry": ctlHardwareDevicesCamerasEntry,
       "ctlHardwareDevicesCameraId": ctlHardwareDevicesCameraId,
       "ctlHardwareDevicesCameraModule": ctlHardwareDevicesCameraModule,
       "ctlHardwareDevicesCameraNum": ctlHardwareDevicesCameraNum,
       "ctlHardwareDevicesCameraGroup": ctlHardwareDevicesCameraGroup,
       "ctlHardwareDevicesCameraType": ctlHardwareDevicesCameraType,
       "ctlHardwareDevicesCameraName": ctlHardwareDevicesCameraName,
       "ctlHardwareDevicesCameraState": ctlHardwareDevicesCameraState,
       "ctlHardwareDevicesCameraValue": ctlHardwareDevicesCameraValue,
       "ctlHardwareDevicesCameraURL": ctlHardwareDevicesCameraURL,
       "ctlHardwareDevicesCameraFPS": ctlHardwareDevicesCameraFPS,
       "ctlHardwareDevicesCameraResolution": ctlHardwareDevicesCameraResolution,
       "ctIInternalSensors": ctIInternalSensors,
       "ctlInternalSensorsDiscretsTable": ctlInternalSensorsDiscretsTable,
       "ctlInternalSensorsDiscretsEntry": ctlInternalSensorsDiscretsEntry,
       "ctlInternalSensorsDiscretId": ctlInternalSensorsDiscretId,
       "ctlInternalSensorsDiscretModule": ctlInternalSensorsDiscretModule,
       "ctlInternalSensorsDiscretNum": ctlInternalSensorsDiscretNum,
       "ctlInternalSensorsDiscretGroup": ctlInternalSensorsDiscretGroup,
       "ctlInternalSensorsDiscretType": ctlInternalSensorsDiscretType,
       "ctlInternalSensorsDiscretName": ctlInternalSensorsDiscretName,
       "ctlInternalSensorsDiscretState": ctlInternalSensorsDiscretState,
       "ctlInternalSensorsDiscretValue": ctlInternalSensorsDiscretValue,
       "ctlInternalSensorsDiscretReset": ctlInternalSensorsDiscretReset,
       "ctlInternalSensorsDiscretLevel": ctlInternalSensorsDiscretLevel,
       "ctlInternalSensorsDiscretReverse": ctlInternalSensorsDiscretReverse,
       "ctlInternalSensorsDiscretSpecific": ctlInternalSensorsDiscretSpecific,
       "ctlInternalSensorsAnalogsTable": ctlInternalSensorsAnalogsTable,
       "ctlInternalSensorsAnalogsEntry": ctlInternalSensorsAnalogsEntry,
       "ctlInternalSensorsAnalogId": ctlInternalSensorsAnalogId,
       "ctlInternalSensorsAnalogModule": ctlInternalSensorsAnalogModule,
       "ctlInternalSensorsAnalogNum": ctlInternalSensorsAnalogNum,
       "ctlInternalSensorsAnalogGroup": ctlInternalSensorsAnalogGroup,
       "ctlInternalSensorsAnalogType": ctlInternalSensorsAnalogType,
       "ctlInternalSensorsAnalogName": ctlInternalSensorsAnalogName,
       "ctlInternalSensorsAnalogState": ctlInternalSensorsAnalogState,
       "ctlInternalSensorsAnalogValue": ctlInternalSensorsAnalogValue,
       "ctlInternalSensorsAnalogMin": ctlInternalSensorsAnalogMin,
       "ctlInternalSensorsAnalogMax": ctlInternalSensorsAnalogMax,
       "ctlInternalSensorsAnalogLow": ctlInternalSensorsAnalogLow,
       "ctlInternalSensorsAnalogWarning": ctlInternalSensorsAnalogWarning,
       "ctlInternalSensorsAnalogHigh": ctlInternalSensorsAnalogHigh,
       "ctlInternalSensorsAnalogAt0": ctlInternalSensorsAnalogAt0,
       "ctlInternalSensorsAnalogAt75": ctlInternalSensorsAnalogAt75,
       "ctlInternalSensorsAnalogExpression": ctlInternalSensorsAnalogExpression,
       "ctlInternalSensorsAnalogSpecific": ctlInternalSensorsAnalogSpecific,
       "ctlInternalSensorsOutletsTable": ctlInternalSensorsOutletsTable,
       "ctlInternalSensorsOutletsEntry": ctlInternalSensorsOutletsEntry,
       "ctlInternalSensorsOutletId": ctlInternalSensorsOutletId,
       "ctlInternalSensorsOutletModule": ctlInternalSensorsOutletModule,
       "ctlInternalSensorsOutletNum": ctlInternalSensorsOutletNum,
       "ctlInternalSensorsOutletGroup": ctlInternalSensorsOutletGroup,
       "ctlInternalSensorsOutletType": ctlInternalSensorsOutletType,
       "ctlInternalSensorsOutletName": ctlInternalSensorsOutletName,
       "ctlInternalSensorsOutletState": ctlInternalSensorsOutletState,
       "ctlInternalSensorsOutletValue": ctlInternalSensorsOutletValue,
       "ctlInternalSensorsOutletInitial": ctlInternalSensorsOutletInitial,
       "ctlInternalSensorsDiscretPulse": ctlInternalSensorsDiscretPulse,
       "ctlCANSensors": ctlCANSensors,
       "ctlCANSensorsDiscretsTable": ctlCANSensorsDiscretsTable,
       "ctlCANSensorsDiscretsEntry": ctlCANSensorsDiscretsEntry,
       "ctlCANSensorsDiscretId": ctlCANSensorsDiscretId,
       "ctlCANSensorsDiscretModule": ctlCANSensorsDiscretModule,
       "ctlCANSensorsDiscretNum": ctlCANSensorsDiscretNum,
       "ctlCANSensorsDiscretGroup": ctlCANSensorsDiscretGroup,
       "ctlCANSensorsDiscretType": ctlCANSensorsDiscretType,
       "ctlCANSensorsDiscretName": ctlCANSensorsDiscretName,
       "ctlCANSensorsDiscretState": ctlCANSensorsDiscretState,
       "ctlCANSensorsDiscretValue": ctlCANSensorsDiscretValue,
       "ctlCANSensorsDiscretReset": ctlCANSensorsDiscretReset,
       "ctlCANSensorsDiscretLevel": ctlCANSensorsDiscretLevel,
       "ctlCANSensorsDiscretReverse": ctlCANSensorsDiscretReverse,
       "ctlCANSensorsDiscretSpecific": ctlCANSensorsDiscretSpecific,
       "ctlCANSensorsAnalogsTable": ctlCANSensorsAnalogsTable,
       "ctlCANSensorsAnalogsEntry": ctlCANSensorsAnalogsEntry,
       "ctlCANSensorsAnalogId": ctlCANSensorsAnalogId,
       "ctlCANSensorsAnalogModule": ctlCANSensorsAnalogModule,
       "ctlCANSensorsAnalogNum": ctlCANSensorsAnalogNum,
       "ctlCANSensorsAnalogGroup": ctlCANSensorsAnalogGroup,
       "ctlCANSensorsAnalogType": ctlCANSensorsAnalogType,
       "ctlCANSensorsAnalogName": ctlCANSensorsAnalogName,
       "ctlCANSensorsAnalogState": ctlCANSensorsAnalogState,
       "ctlCANSensorsAnalogValue": ctlCANSensorsAnalogValue,
       "ctlCANSensorsAnalogMin": ctlCANSensorsAnalogMin,
       "ctlCANSensorsAnalogMax": ctlCANSensorsAnalogMax,
       "ctlCANSensorsAnalogLow": ctlCANSensorsAnalogLow,
       "ctlCANSensorsAnalogWarning": ctlCANSensorsAnalogWarning,
       "ctlCANSensorsAnalogHigh": ctlCANSensorsAnalogHigh,
       "ctlCANSensorsAnalogAt0": ctlCANSensorsAnalogAt0,
       "ctlCANSensorsAnalogAt75": ctlCANSensorsAnalogAt75,
       "ctlCANSensorsAnalogExpression": ctlCANSensorsAnalogExpression,
       "ctlCANSensorsAnalogSpecific": ctlCANSensorsAnalogSpecific,
       "ctlCANSensorsOutletsTable": ctlCANSensorsOutletsTable,
       "ctlCANSensorsOutletsEntry": ctlCANSensorsOutletsEntry,
       "ctlCANSensorsOutletId": ctlCANSensorsOutletId,
       "ctlCANSensorsOutletModule": ctlCANSensorsOutletModule,
       "ctlCANSensorsOutletNum": ctlCANSensorsOutletNum,
       "ctlCANSensorsOutletGroup": ctlCANSensorsOutletGroup,
       "ctlCANSensorsOutletType": ctlCANSensorsOutletType,
       "ctlCANSensorsOutletName": ctlCANSensorsOutletName,
       "ctlCANSensorsOutletState": ctlCANSensorsOutletState,
       "ctlCANSensorsOutletValue": ctlCANSensorsOutletValue,
       "ctlCANSensorsOutletInitial": ctlCANSensorsOutletInitial,
       "ctlCANSensorsDiscretPulse": ctlCANSensorsDiscretPulse,
       "ctlRsSensors": ctlRsSensors,
       "ctlRsSensorsDiscretsTable": ctlRsSensorsDiscretsTable,
       "ctlRsSensorsDiscretsEntry": ctlRsSensorsDiscretsEntry,
       "ctlRsSensorsDiscretId": ctlRsSensorsDiscretId,
       "ctlRsSensorsDiscretModule": ctlRsSensorsDiscretModule,
       "ctlRsSensorsDiscretNum": ctlRsSensorsDiscretNum,
       "ctlRsSensorsDiscretGroup": ctlRsSensorsDiscretGroup,
       "ctlRsSensorsDiscretType": ctlRsSensorsDiscretType,
       "ctlRsSensorsDiscretName": ctlRsSensorsDiscretName,
       "ctlRsSensorsDiscretState": ctlRsSensorsDiscretState,
       "ctlRsSensorsDiscretValue": ctlRsSensorsDiscretValue,
       "ctlRsSensorsDiscretReset": ctlRsSensorsDiscretReset,
       "ctlRsSensorsDiscretLevel": ctlRsSensorsDiscretLevel,
       "ctlRsSensorsDiscretReverse": ctlRsSensorsDiscretReverse,
       "ctlRsSensorsDiscretSpecific": ctlRsSensorsDiscretSpecific,
       "ctlRsSensorsAnalogsTable": ctlRsSensorsAnalogsTable,
       "ctlRsSensorsAnalogsEntry": ctlRsSensorsAnalogsEntry,
       "ctlRsSensorsAnalogId": ctlRsSensorsAnalogId,
       "ctlRsSensorsAnalogModule": ctlRsSensorsAnalogModule,
       "ctlRsSensorsAnalogNum": ctlRsSensorsAnalogNum,
       "ctlRsSensorsAnalogGroup": ctlRsSensorsAnalogGroup,
       "ctlRsSensorsAnalogType": ctlRsSensorsAnalogType,
       "ctlRsSensorsAnalogName": ctlRsSensorsAnalogName,
       "ctlRsSensorsAnalogState": ctlRsSensorsAnalogState,
       "ctlRsSensorsAnalogValue": ctlRsSensorsAnalogValue,
       "ctlRsSensorsAnalogMin": ctlRsSensorsAnalogMin,
       "ctlRsSensorsAnalogMax": ctlRsSensorsAnalogMax,
       "ctlRsSensorsAnalogLow": ctlRsSensorsAnalogLow,
       "ctlRsSensorsAnalogWarning": ctlRsSensorsAnalogWarning,
       "ctlRsSensorsAnalogHigh": ctlRsSensorsAnalogHigh,
       "ctlRsSensorsAnalogAt0": ctlRsSensorsAnalogAt0,
       "ctlRsSensorsAnalogAt75": ctlRsSensorsAnalogAt75,
       "ctlRsSensorsAnalogExpression": ctlRsSensorsAnalogExpression,
       "ctlRsSensorsAnalogSpecific": ctlRsSensorsAnalogSpecific,
       "ctlRsSensorsOutletsTable": ctlRsSensorsOutletsTable,
       "ctlRsSensorsOutletsEntry": ctlRsSensorsOutletsEntry,
       "ctlRsSensorsOutletId": ctlRsSensorsOutletId,
       "ctlRsSensorsOutletModule": ctlRsSensorsOutletModule,
       "ctlRsSensorsOutletNum": ctlRsSensorsOutletNum,
       "ctlRsSensorsOutletGroup": ctlRsSensorsOutletGroup,
       "ctlRsSensorsOutletType": ctlRsSensorsOutletType,
       "ctlRsSensorsOutletName": ctlRsSensorsOutletName,
       "ctlRsSensorsOutletState": ctlRsSensorsOutletState,
       "ctlRsSensorsOutletValue": ctlRsSensorsOutletValue,
       "ctlRsSensorsOutletInitial": ctlRsSensorsOutletInitial,
       "ctlRsSensorsDiscretPulse": ctlRsSensorsDiscretPulse}
)
