# SNMP MIB module (CISCO-ENTITY-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:41 2024
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

(CeRedunArch,
 CeRedunMbrStatus,
 CeRedunMode,
 CeRedunReasonCategories,
 CeRedunScope,
 CeRedunStateCategories,
 CeRedunSwitchCommand,
 CeRedunType) = mibBuilder.importSymbols(
    "CISCO-ENTITY-REDUNDANCY-TC-MIB",
    "CeRedunArch",
    "CeRedunMbrStatus",
    "CeRedunMode",
    "CeRedunReasonCategories",
    "CeRedunScope",
    "CeRedunStateCategories",
    "CeRedunSwitchCommand",
    "CeRedunType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(AutonomousType,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntityRedunMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 498)
)
ciscoEntityRedunMIB.setRevisions(
        ("2005-10-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEntityRedunMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEntityRedunMIBNotifs = _CiscoEntityRedunMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 0)
)
_CiscoEntityRedunMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityRedunMIBObjects = _CiscoEntityRedunMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1)
)
_CeRedunGroup_ObjectIdentity = ObjectIdentity
ceRedunGroup = _CeRedunGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1)
)
_CeRedunGroupTypesTable_Object = MibTable
ceRedunGroupTypesTable = _CeRedunGroupTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceRedunGroupTypesTable.setStatus("current")
_CeRedunGroupTypesEntry_Object = MibTableRow
ceRedunGroupTypesEntry = _CeRedunGroupTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1, 1)
)
ceRedunGroupTypesEntry.setIndexNames(
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupTypeIndex"),
)
if mibBuilder.loadTexts:
    ceRedunGroupTypesEntry.setStatus("current")
_CeRedunGroupTypeIndex_Type = Unsigned32
_CeRedunGroupTypeIndex_Object = MibTableColumn
ceRedunGroupTypeIndex = _CeRedunGroupTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1, 1, 1),
    _CeRedunGroupTypeIndex_Type()
)
ceRedunGroupTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceRedunGroupTypeIndex.setStatus("current")
_CeRedunGroupTypeName_Type = SnmpAdminString
_CeRedunGroupTypeName_Object = MibTableColumn
ceRedunGroupTypeName = _CeRedunGroupTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1, 1, 2),
    _CeRedunGroupTypeName_Type()
)
ceRedunGroupTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunGroupTypeName.setStatus("current")
_CeRedunGroupCounts_Type = Gauge32
_CeRedunGroupCounts_Object = MibTableColumn
ceRedunGroupCounts = _CeRedunGroupCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1, 1, 3),
    _CeRedunGroupCounts_Type()
)
ceRedunGroupCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunGroupCounts.setStatus("current")
_CeRedunNextUnusedGroupIndex_Type = Unsigned32
_CeRedunNextUnusedGroupIndex_Object = MibTableColumn
ceRedunNextUnusedGroupIndex = _CeRedunNextUnusedGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1, 1, 4),
    _CeRedunNextUnusedGroupIndex_Type()
)
ceRedunNextUnusedGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunNextUnusedGroupIndex.setStatus("current")
_CeRedunMaxMbrsInGroup_Type = Unsigned32
_CeRedunMaxMbrsInGroup_Object = MibTableColumn
ceRedunMaxMbrsInGroup = _CeRedunMaxMbrsInGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1, 1, 5),
    _CeRedunMaxMbrsInGroup_Type()
)
ceRedunMaxMbrsInGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMaxMbrsInGroup.setStatus("current")
_CeRedunUsesGroupName_Type = TruthValue
_CeRedunUsesGroupName_Object = MibTableColumn
ceRedunUsesGroupName = _CeRedunUsesGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1, 1, 6),
    _CeRedunUsesGroupName_Type()
)
ceRedunUsesGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunUsesGroupName.setStatus("current")
_CeRedunGroupDefinitionChanged_Type = TimeStamp
_CeRedunGroupDefinitionChanged_Object = MibTableColumn
ceRedunGroupDefinitionChanged = _CeRedunGroupDefinitionChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 1, 1, 7),
    _CeRedunGroupDefinitionChanged_Type()
)
ceRedunGroupDefinitionChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunGroupDefinitionChanged.setStatus("current")
_CeRedunVendorTypesTable_Object = MibTable
ceRedunVendorTypesTable = _CeRedunVendorTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ceRedunVendorTypesTable.setStatus("current")
_CeRedunVendorTypesEntry_Object = MibTableRow
ceRedunVendorTypesEntry = _CeRedunVendorTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 2, 1)
)
ceRedunVendorTypesEntry.setIndexNames(
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupTypeIndex"),
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunVendorType"),
)
if mibBuilder.loadTexts:
    ceRedunVendorTypesEntry.setStatus("current")
_CeRedunVendorType_Type = AutonomousType
_CeRedunVendorType_Object = MibTableColumn
ceRedunVendorType = _CeRedunVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 2, 1, 1),
    _CeRedunVendorType_Type()
)
ceRedunVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunVendorType.setStatus("current")
_CeRedunInternalStatesTable_Object = MibTable
ceRedunInternalStatesTable = _CeRedunInternalStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ceRedunInternalStatesTable.setStatus("current")
_CeRedunInternalStatesEntry_Object = MibTableRow
ceRedunInternalStatesEntry = _CeRedunInternalStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 3, 1)
)
ceRedunInternalStatesEntry.setIndexNames(
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupTypeIndex"),
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunInternalStateIndex"),
)
if mibBuilder.loadTexts:
    ceRedunInternalStatesEntry.setStatus("current")
_CeRedunInternalStateIndex_Type = Unsigned32
_CeRedunInternalStateIndex_Object = MibTableColumn
ceRedunInternalStateIndex = _CeRedunInternalStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 3, 1, 1),
    _CeRedunInternalStateIndex_Type()
)
ceRedunInternalStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceRedunInternalStateIndex.setStatus("current")
_CeRedunStateCategory_Type = CeRedunStateCategories
_CeRedunStateCategory_Object = MibTableColumn
ceRedunStateCategory = _CeRedunStateCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 3, 1, 2),
    _CeRedunStateCategory_Type()
)
ceRedunStateCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunStateCategory.setStatus("current")
_CeRedunInternalStateDescr_Type = SnmpAdminString
_CeRedunInternalStateDescr_Object = MibTableColumn
ceRedunInternalStateDescr = _CeRedunInternalStateDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 3, 1, 3),
    _CeRedunInternalStateDescr_Type()
)
ceRedunInternalStateDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunInternalStateDescr.setStatus("current")
_CeRedunSwitchoverReasonTable_Object = MibTable
ceRedunSwitchoverReasonTable = _CeRedunSwitchoverReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ceRedunSwitchoverReasonTable.setStatus("current")
_CeRedunSwitchoverReasonEntry_Object = MibTableRow
ceRedunSwitchoverReasonEntry = _CeRedunSwitchoverReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 4, 1)
)
ceRedunSwitchoverReasonEntry.setIndexNames(
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupTypeIndex"),
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunSwitchoverReasonIndex"),
)
if mibBuilder.loadTexts:
    ceRedunSwitchoverReasonEntry.setStatus("current")
_CeRedunSwitchoverReasonIndex_Type = Unsigned32
_CeRedunSwitchoverReasonIndex_Object = MibTableColumn
ceRedunSwitchoverReasonIndex = _CeRedunSwitchoverReasonIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 4, 1, 1),
    _CeRedunSwitchoverReasonIndex_Type()
)
ceRedunSwitchoverReasonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceRedunSwitchoverReasonIndex.setStatus("current")
_CeRedunReasonCategory_Type = CeRedunReasonCategories
_CeRedunReasonCategory_Object = MibTableColumn
ceRedunReasonCategory = _CeRedunReasonCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 4, 1, 2),
    _CeRedunReasonCategory_Type()
)
ceRedunReasonCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunReasonCategory.setStatus("current")
_CeRedunSwitchoverReasonDescr_Type = SnmpAdminString
_CeRedunSwitchoverReasonDescr_Object = MibTableColumn
ceRedunSwitchoverReasonDescr = _CeRedunSwitchoverReasonDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 4, 1, 3),
    _CeRedunSwitchoverReasonDescr_Type()
)
ceRedunSwitchoverReasonDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunSwitchoverReasonDescr.setStatus("current")
_CeRedunGroupLastChanged_Type = TimeStamp
_CeRedunGroupLastChanged_Object = MibScalar
ceRedunGroupLastChanged = _CeRedunGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 5),
    _CeRedunGroupLastChanged_Type()
)
ceRedunGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunGroupLastChanged.setStatus("current")
_CeRedunGroupTable_Object = MibTable
ceRedunGroupTable = _CeRedunGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ceRedunGroupTable.setStatus("current")
_CeRedunGroupEntry_Object = MibTableRow
ceRedunGroupEntry = _CeRedunGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1)
)
ceRedunGroupEntry.setIndexNames(
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupTypeIndex"),
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupIndex"),
)
if mibBuilder.loadTexts:
    ceRedunGroupEntry.setStatus("current")
_CeRedunGroupIndex_Type = Unsigned32
_CeRedunGroupIndex_Object = MibTableColumn
ceRedunGroupIndex = _CeRedunGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 1),
    _CeRedunGroupIndex_Type()
)
ceRedunGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceRedunGroupIndex.setStatus("current")
_CeRedunGroupString_Type = SnmpAdminString
_CeRedunGroupString_Object = MibTableColumn
ceRedunGroupString = _CeRedunGroupString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 2),
    _CeRedunGroupString_Type()
)
ceRedunGroupString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupString.setStatus("current")
_CeRedunGroupRedunType_Type = CeRedunType
_CeRedunGroupRedunType_Object = MibTableColumn
ceRedunGroupRedunType = _CeRedunGroupRedunType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 3),
    _CeRedunGroupRedunType_Type()
)
ceRedunGroupRedunType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupRedunType.setStatus("current")


class _CeRedunGroupScope_Type(CeRedunScope):
    """Custom type ceRedunGroupScope based on CeRedunScope"""


_CeRedunGroupScope_Object = MibTableColumn
ceRedunGroupScope = _CeRedunGroupScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 4),
    _CeRedunGroupScope_Type()
)
ceRedunGroupScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupScope.setStatus("current")


class _CeRedunGroupArch_Type(CeRedunArch):
    """Custom type ceRedunGroupArch based on CeRedunArch"""


_CeRedunGroupArch_Object = MibTableColumn
ceRedunGroupArch = _CeRedunGroupArch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 5),
    _CeRedunGroupArch_Type()
)
ceRedunGroupArch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupArch.setStatus("current")


class _CeRedunGroupRevert_Type(Integer32):
    """Custom type ceRedunGroupRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_CeRedunGroupRevert_Type.__name__ = "Integer32"
_CeRedunGroupRevert_Object = MibTableColumn
ceRedunGroupRevert = _CeRedunGroupRevert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 6),
    _CeRedunGroupRevert_Type()
)
ceRedunGroupRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupRevert.setStatus("current")


class _CeRedunGroupWaitToRestore_Type(Unsigned32):
    """Custom type ceRedunGroupWaitToRestore based on Unsigned32"""
    defaultValue = 300


_CeRedunGroupWaitToRestore_Object = MibTableColumn
ceRedunGroupWaitToRestore = _CeRedunGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 7),
    _CeRedunGroupWaitToRestore_Type()
)
ceRedunGroupWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    ceRedunGroupWaitToRestore.setUnits("seconds")


class _CeRedunGroupDirection_Type(Integer32):
    """Custom type ceRedunGroupDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_CeRedunGroupDirection_Type.__name__ = "Integer32"
_CeRedunGroupDirection_Object = MibTableColumn
ceRedunGroupDirection = _CeRedunGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 8),
    _CeRedunGroupDirection_Type()
)
ceRedunGroupDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupDirection.setStatus("current")


class _CeRedunGroupStorageType_Type(StorageType):
    """Custom type ceRedunGroupStorageType based on StorageType"""


_CeRedunGroupStorageType_Object = MibTableColumn
ceRedunGroupStorageType = _CeRedunGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 9),
    _CeRedunGroupStorageType_Type()
)
ceRedunGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupStorageType.setStatus("current")
_CeRedunGroupRowStatus_Type = RowStatus
_CeRedunGroupRowStatus_Object = MibTableColumn
ceRedunGroupRowStatus = _CeRedunGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 1, 6, 1, 10),
    _CeRedunGroupRowStatus_Type()
)
ceRedunGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunGroupRowStatus.setStatus("current")
_CeRedunMembers_ObjectIdentity = ObjectIdentity
ceRedunMembers = _CeRedunMembers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2)
)
_CeRedunMbrLastChanged_Type = TimeStamp
_CeRedunMbrLastChanged_Object = MibScalar
ceRedunMbrLastChanged = _CeRedunMbrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 1),
    _CeRedunMbrLastChanged_Type()
)
ceRedunMbrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrLastChanged.setStatus("current")
_CeRedunMbrConfigTable_Object = MibTable
ceRedunMbrConfigTable = _CeRedunMbrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ceRedunMbrConfigTable.setStatus("current")
_CeRedunMbrConfigEntry_Object = MibTableRow
ceRedunMbrConfigEntry = _CeRedunMbrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1)
)
ceRedunMbrConfigEntry.setIndexNames(
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupTypeIndex"),
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupIndex"),
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrNumber"),
)
if mibBuilder.loadTexts:
    ceRedunMbrConfigEntry.setStatus("current")
_CeRedunMbrNumber_Type = Unsigned32
_CeRedunMbrNumber_Object = MibTableColumn
ceRedunMbrNumber = _CeRedunMbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1, 1),
    _CeRedunMbrNumber_Type()
)
ceRedunMbrNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceRedunMbrNumber.setStatus("current")
_CeRedunMbrPhysIndex_Type = PhysicalIndex
_CeRedunMbrPhysIndex_Object = MibTableColumn
ceRedunMbrPhysIndex = _CeRedunMbrPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1, 2),
    _CeRedunMbrPhysIndex_Type()
)
ceRedunMbrPhysIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunMbrPhysIndex.setStatus("current")
_CeRedunMbrMode_Type = CeRedunMode
_CeRedunMbrMode_Object = MibTableColumn
ceRedunMbrMode = _CeRedunMbrMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1, 3),
    _CeRedunMbrMode_Type()
)
ceRedunMbrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunMbrMode.setStatus("current")
_CeRedunMbrAddressType_Type = InetAddressType
_CeRedunMbrAddressType_Object = MibTableColumn
ceRedunMbrAddressType = _CeRedunMbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1, 4),
    _CeRedunMbrAddressType_Type()
)
ceRedunMbrAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunMbrAddressType.setStatus("current")
_CeRedunMbrRemoteAddress_Type = InetAddress
_CeRedunMbrRemoteAddress_Object = MibTableColumn
ceRedunMbrRemoteAddress = _CeRedunMbrRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1, 5),
    _CeRedunMbrRemoteAddress_Type()
)
ceRedunMbrRemoteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunMbrRemoteAddress.setStatus("current")


class _CeRedunMbrPriority_Type(Integer32):
    """Custom type ceRedunMbrPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_CeRedunMbrPriority_Type.__name__ = "Integer32"
_CeRedunMbrPriority_Object = MibTableColumn
ceRedunMbrPriority = _CeRedunMbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1, 6),
    _CeRedunMbrPriority_Type()
)
ceRedunMbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunMbrPriority.setStatus("current")


class _CeRedunMbrStorageType_Type(StorageType):
    """Custom type ceRedunMbrStorageType based on StorageType"""


_CeRedunMbrStorageType_Object = MibTableColumn
ceRedunMbrStorageType = _CeRedunMbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1, 8),
    _CeRedunMbrStorageType_Type()
)
ceRedunMbrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunMbrStorageType.setStatus("current")
_CeRedunMbrRowStatus_Type = RowStatus
_CeRedunMbrRowStatus_Object = MibTableColumn
ceRedunMbrRowStatus = _CeRedunMbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 2, 1, 9),
    _CeRedunMbrRowStatus_Type()
)
ceRedunMbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceRedunMbrRowStatus.setStatus("current")
_CeRedunMbrStatusLastChanged_Type = TimeStamp
_CeRedunMbrStatusLastChanged_Object = MibScalar
ceRedunMbrStatusLastChanged = _CeRedunMbrStatusLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 3),
    _CeRedunMbrStatusLastChanged_Type()
)
ceRedunMbrStatusLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrStatusLastChanged.setStatus("current")
_CeRedunMbrStatusTable_Object = MibTable
ceRedunMbrStatusTable = _CeRedunMbrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ceRedunMbrStatusTable.setStatus("current")
_CeRedunMbrStatusEntry_Object = MibTableRow
ceRedunMbrStatusEntry = _CeRedunMbrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ceRedunMbrStatusEntry.setStatus("current")
_CeRedunMbrStatusCurrent_Type = CeRedunMbrStatus
_CeRedunMbrStatusCurrent_Object = MibTableColumn
ceRedunMbrStatusCurrent = _CeRedunMbrStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4, 1, 1),
    _CeRedunMbrStatusCurrent_Type()
)
ceRedunMbrStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrStatusCurrent.setStatus("current")
_CeRedunMbrProtectingMbr_Type = Unsigned32
_CeRedunMbrProtectingMbr_Object = MibTableColumn
ceRedunMbrProtectingMbr = _CeRedunMbrProtectingMbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4, 1, 2),
    _CeRedunMbrProtectingMbr_Type()
)
ceRedunMbrProtectingMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrProtectingMbr.setStatus("current")
_CeRedunMbrInternalState_Type = Unsigned32
_CeRedunMbrInternalState_Object = MibTableColumn
ceRedunMbrInternalState = _CeRedunMbrInternalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4, 1, 3),
    _CeRedunMbrInternalState_Type()
)
ceRedunMbrInternalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrInternalState.setStatus("current")
_CeRedunMbrSwitchoverCounts_Type = Gauge32
_CeRedunMbrSwitchoverCounts_Object = MibTableColumn
ceRedunMbrSwitchoverCounts = _CeRedunMbrSwitchoverCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4, 1, 4),
    _CeRedunMbrSwitchoverCounts_Type()
)
ceRedunMbrSwitchoverCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrSwitchoverCounts.setStatus("current")
_CeRedunMbrLastSwitchover_Type = TimeStamp
_CeRedunMbrLastSwitchover_Object = MibTableColumn
ceRedunMbrLastSwitchover = _CeRedunMbrLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4, 1, 5),
    _CeRedunMbrLastSwitchover_Type()
)
ceRedunMbrLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrLastSwitchover.setStatus("current")
_CeRedunMbrSwitchoverReason_Type = Unsigned32
_CeRedunMbrSwitchoverReason_Object = MibTableColumn
ceRedunMbrSwitchoverReason = _CeRedunMbrSwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4, 1, 6),
    _CeRedunMbrSwitchoverReason_Type()
)
ceRedunMbrSwitchoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrSwitchoverReason.setStatus("current")
_CeRedunMbrSwitchoverSeconds_Type = Counter64
_CeRedunMbrSwitchoverSeconds_Object = MibTableColumn
ceRedunMbrSwitchoverSeconds = _CeRedunMbrSwitchoverSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 2, 4, 1, 8),
    _CeRedunMbrSwitchoverSeconds_Type()
)
ceRedunMbrSwitchoverSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRedunMbrSwitchoverSeconds.setStatus("current")
_CeRedunCommandTable_Object = MibTable
ceRedunCommandTable = _CeRedunCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 3)
)
if mibBuilder.loadTexts:
    ceRedunCommandTable.setStatus("current")
_CeRedunCommandEntry_Object = MibTableRow
ceRedunCommandEntry = _CeRedunCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 3, 1)
)
ceRedunCommandEntry.setIndexNames(
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupTypeIndex"),
    (0, "CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupIndex"),
)
if mibBuilder.loadTexts:
    ceRedunCommandEntry.setStatus("current")


class _CeRedunCommandMbrNumber_Type(Integer32):
    """Custom type ceRedunCommandMbrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CeRedunCommandMbrNumber_Type.__name__ = "Integer32"
_CeRedunCommandMbrNumber_Object = MibTableColumn
ceRedunCommandMbrNumber = _CeRedunCommandMbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 3, 1, 1),
    _CeRedunCommandMbrNumber_Type()
)
ceRedunCommandMbrNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceRedunCommandMbrNumber.setStatus("current")
_CeRedunCommandSwitch_Type = CeRedunSwitchCommand
_CeRedunCommandSwitch_Object = MibTableColumn
ceRedunCommandSwitch = _CeRedunCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 3, 1, 2),
    _CeRedunCommandSwitch_Type()
)
ceRedunCommandSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceRedunCommandSwitch.setStatus("current")


class _CeRedunEnableSwitchoverNotifs_Type(TruthValue):
    """Custom type ceRedunEnableSwitchoverNotifs based on TruthValue"""


_CeRedunEnableSwitchoverNotifs_Object = MibScalar
ceRedunEnableSwitchoverNotifs = _CeRedunEnableSwitchoverNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 4),
    _CeRedunEnableSwitchoverNotifs_Type()
)
ceRedunEnableSwitchoverNotifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceRedunEnableSwitchoverNotifs.setStatus("current")


class _CeRedunEnableStatusChangeNotifs_Type(TruthValue):
    """Custom type ceRedunEnableStatusChangeNotifs based on TruthValue"""


_CeRedunEnableStatusChangeNotifs_Object = MibScalar
ceRedunEnableStatusChangeNotifs = _CeRedunEnableStatusChangeNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 1, 5),
    _CeRedunEnableStatusChangeNotifs_Type()
)
ceRedunEnableStatusChangeNotifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceRedunEnableStatusChangeNotifs.setStatus("current")
_CiscoEntityRedunMIBConform_ObjectIdentity = ObjectIdentity
ciscoEntityRedunMIBConform = _CiscoEntityRedunMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2)
)
_CeRedunCompliances_ObjectIdentity = ObjectIdentity
ceRedunCompliances = _CeRedunCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 1)
)
_CeRedunGroups_ObjectIdentity = ObjectIdentity
ceRedunGroups = _CeRedunGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2)
)
ceRedunMbrConfigEntry.registerAugmentions(
    ("CISCO-ENTITY-REDUNDANCY-MIB",
     "ceRedunMbrStatusEntry")
)
ceRedunMbrStatusEntry.setIndexNames(*ceRedunMbrConfigEntry.getIndexNames())

# Managed Objects groups

ceRedunGroupTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 1)
)
ceRedunGroupTypeGroup.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunNextUnusedGroupIndex"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMaxMbrsInGroup"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunUsesGroupName"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupDefinitionChanged"))
)
if mibBuilder.loadTexts:
    ceRedunGroupTypeGroup.setStatus("current")

ceRedunOptionalGroupTypes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 2)
)
ceRedunOptionalGroupTypes.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupTypeName"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupCounts"))
)
if mibBuilder.loadTexts:
    ceRedunOptionalGroupTypes.setStatus("current")

ceRedunInternalStates = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 3)
)
ceRedunInternalStates.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunStateCategory"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunInternalStateDescr"))
)
if mibBuilder.loadTexts:
    ceRedunInternalStates.setStatus("current")

ceRedunSwitchoverReason = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 4)
)
ceRedunSwitchoverReason.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunReasonCategory"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunSwitchoverReasonDescr"))
)
if mibBuilder.loadTexts:
    ceRedunSwitchoverReason.setStatus("current")

ceRedunGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 5)
)
ceRedunGroupObjects.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupLastChanged"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupString"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupRedunType"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupScope"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupArch"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupStorageType"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ceRedunGroupObjects.setStatus("current")

ceRedunRevertiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 6)
)
ceRedunRevertiveGroup.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupRevert"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupWaitToRestore"))
)
if mibBuilder.loadTexts:
    ceRedunRevertiveGroup.setStatus("current")

ceRedunBidirectional = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 7)
)
ceRedunBidirectional.setObjects(
    ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunGroupDirection")
)
if mibBuilder.loadTexts:
    ceRedunBidirectional.setStatus("current")

ceRedunMemberConfig = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 8)
)
ceRedunMemberConfig.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrLastChanged"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrPhysIndex"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrMode"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrStorageType"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrRowStatus"))
)
if mibBuilder.loadTexts:
    ceRedunMemberConfig.setStatus("current")

ceRedunRemoteSystem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 9)
)
ceRedunRemoteSystem.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrAddressType"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrRemoteAddress"))
)
if mibBuilder.loadTexts:
    ceRedunRemoteSystem.setStatus("current")

ceRedunOneToN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 10)
)
ceRedunOneToN.setObjects(
    ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrPriority")
)
if mibBuilder.loadTexts:
    ceRedunOneToN.setStatus("current")

ceRedunMemberStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 11)
)
ceRedunMemberStatus.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrStatusLastChanged"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrStatusCurrent"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrProtectingMbr"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrSwitchoverCounts"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrLastSwitchover"))
)
if mibBuilder.loadTexts:
    ceRedunMemberStatus.setStatus("current")

ceRedunOptionalMbrStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 12)
)
ceRedunOptionalMbrStatus.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrInternalState"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrSwitchoverReason"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrSwitchoverSeconds"))
)
if mibBuilder.loadTexts:
    ceRedunOptionalMbrStatus.setStatus("current")

ceRedunCommandsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 13)
)
ceRedunCommandsGroup.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunCommandMbrNumber"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunCommandSwitch"))
)
if mibBuilder.loadTexts:
    ceRedunCommandsGroup.setStatus("current")

ceRedunNotifEnables = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 14)
)
ceRedunNotifEnables.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunEnableSwitchoverNotifs"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunEnableStatusChangeNotifs"))
)
if mibBuilder.loadTexts:
    ceRedunNotifEnables.setStatus("current")


# Notification objects

ceRedunEventSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 0, 1)
)
ceRedunEventSwitchover.setObjects(
      *(("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrProtectingMbr"),
        ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrStatusCurrent"))
)
if mibBuilder.loadTexts:
    ceRedunEventSwitchover.setStatus(
        "current"
    )

ceRedunProtectStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 0, 2)
)
ceRedunProtectStatusChange.setObjects(
    ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunMbrStatusCurrent")
)
if mibBuilder.loadTexts:
    ceRedunProtectStatusChange.setStatus(
        "current"
    )


# Notifications groups

ceRedunSwitchNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 15)
)
ceRedunSwitchNotifGroup.setObjects(
    ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunEventSwitchover")
)
if mibBuilder.loadTexts:
    ceRedunSwitchNotifGroup.setStatus(
        "current"
    )

ceRedunProtectStatusNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 2, 16)
)
ceRedunProtectStatusNotifGroup.setObjects(
    ("CISCO-ENTITY-REDUNDANCY-MIB", "ceRedunProtectStatusChange")
)
if mibBuilder.loadTexts:
    ceRedunProtectStatusNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ceRedunCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 498, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ceRedunCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-REDUNDANCY-MIB",
    **{"ciscoEntityRedunMIB": ciscoEntityRedunMIB,
       "ciscoEntityRedunMIBNotifs": ciscoEntityRedunMIBNotifs,
       "ceRedunEventSwitchover": ceRedunEventSwitchover,
       "ceRedunProtectStatusChange": ceRedunProtectStatusChange,
       "ciscoEntityRedunMIBObjects": ciscoEntityRedunMIBObjects,
       "ceRedunGroup": ceRedunGroup,
       "ceRedunGroupTypesTable": ceRedunGroupTypesTable,
       "ceRedunGroupTypesEntry": ceRedunGroupTypesEntry,
       "ceRedunGroupTypeIndex": ceRedunGroupTypeIndex,
       "ceRedunGroupTypeName": ceRedunGroupTypeName,
       "ceRedunGroupCounts": ceRedunGroupCounts,
       "ceRedunNextUnusedGroupIndex": ceRedunNextUnusedGroupIndex,
       "ceRedunMaxMbrsInGroup": ceRedunMaxMbrsInGroup,
       "ceRedunUsesGroupName": ceRedunUsesGroupName,
       "ceRedunGroupDefinitionChanged": ceRedunGroupDefinitionChanged,
       "ceRedunVendorTypesTable": ceRedunVendorTypesTable,
       "ceRedunVendorTypesEntry": ceRedunVendorTypesEntry,
       "ceRedunVendorType": ceRedunVendorType,
       "ceRedunInternalStatesTable": ceRedunInternalStatesTable,
       "ceRedunInternalStatesEntry": ceRedunInternalStatesEntry,
       "ceRedunInternalStateIndex": ceRedunInternalStateIndex,
       "ceRedunStateCategory": ceRedunStateCategory,
       "ceRedunInternalStateDescr": ceRedunInternalStateDescr,
       "ceRedunSwitchoverReasonTable": ceRedunSwitchoverReasonTable,
       "ceRedunSwitchoverReasonEntry": ceRedunSwitchoverReasonEntry,
       "ceRedunSwitchoverReasonIndex": ceRedunSwitchoverReasonIndex,
       "ceRedunReasonCategory": ceRedunReasonCategory,
       "ceRedunSwitchoverReasonDescr": ceRedunSwitchoverReasonDescr,
       "ceRedunGroupLastChanged": ceRedunGroupLastChanged,
       "ceRedunGroupTable": ceRedunGroupTable,
       "ceRedunGroupEntry": ceRedunGroupEntry,
       "ceRedunGroupIndex": ceRedunGroupIndex,
       "ceRedunGroupString": ceRedunGroupString,
       "ceRedunGroupRedunType": ceRedunGroupRedunType,
       "ceRedunGroupScope": ceRedunGroupScope,
       "ceRedunGroupArch": ceRedunGroupArch,
       "ceRedunGroupRevert": ceRedunGroupRevert,
       "ceRedunGroupWaitToRestore": ceRedunGroupWaitToRestore,
       "ceRedunGroupDirection": ceRedunGroupDirection,
       "ceRedunGroupStorageType": ceRedunGroupStorageType,
       "ceRedunGroupRowStatus": ceRedunGroupRowStatus,
       "ceRedunMembers": ceRedunMembers,
       "ceRedunMbrLastChanged": ceRedunMbrLastChanged,
       "ceRedunMbrConfigTable": ceRedunMbrConfigTable,
       "ceRedunMbrConfigEntry": ceRedunMbrConfigEntry,
       "ceRedunMbrNumber": ceRedunMbrNumber,
       "ceRedunMbrPhysIndex": ceRedunMbrPhysIndex,
       "ceRedunMbrMode": ceRedunMbrMode,
       "ceRedunMbrAddressType": ceRedunMbrAddressType,
       "ceRedunMbrRemoteAddress": ceRedunMbrRemoteAddress,
       "ceRedunMbrPriority": ceRedunMbrPriority,
       "ceRedunMbrStorageType": ceRedunMbrStorageType,
       "ceRedunMbrRowStatus": ceRedunMbrRowStatus,
       "ceRedunMbrStatusLastChanged": ceRedunMbrStatusLastChanged,
       "ceRedunMbrStatusTable": ceRedunMbrStatusTable,
       "ceRedunMbrStatusEntry": ceRedunMbrStatusEntry,
       "ceRedunMbrStatusCurrent": ceRedunMbrStatusCurrent,
       "ceRedunMbrProtectingMbr": ceRedunMbrProtectingMbr,
       "ceRedunMbrInternalState": ceRedunMbrInternalState,
       "ceRedunMbrSwitchoverCounts": ceRedunMbrSwitchoverCounts,
       "ceRedunMbrLastSwitchover": ceRedunMbrLastSwitchover,
       "ceRedunMbrSwitchoverReason": ceRedunMbrSwitchoverReason,
       "ceRedunMbrSwitchoverSeconds": ceRedunMbrSwitchoverSeconds,
       "ceRedunCommandTable": ceRedunCommandTable,
       "ceRedunCommandEntry": ceRedunCommandEntry,
       "ceRedunCommandMbrNumber": ceRedunCommandMbrNumber,
       "ceRedunCommandSwitch": ceRedunCommandSwitch,
       "ceRedunEnableSwitchoverNotifs": ceRedunEnableSwitchoverNotifs,
       "ceRedunEnableStatusChangeNotifs": ceRedunEnableStatusChangeNotifs,
       "ciscoEntityRedunMIBConform": ciscoEntityRedunMIBConform,
       "ceRedunCompliances": ceRedunCompliances,
       "ceRedunCompliance": ceRedunCompliance,
       "ceRedunGroups": ceRedunGroups,
       "ceRedunGroupTypeGroup": ceRedunGroupTypeGroup,
       "ceRedunOptionalGroupTypes": ceRedunOptionalGroupTypes,
       "ceRedunInternalStates": ceRedunInternalStates,
       "ceRedunSwitchoverReason": ceRedunSwitchoverReason,
       "ceRedunGroupObjects": ceRedunGroupObjects,
       "ceRedunRevertiveGroup": ceRedunRevertiveGroup,
       "ceRedunBidirectional": ceRedunBidirectional,
       "ceRedunMemberConfig": ceRedunMemberConfig,
       "ceRedunRemoteSystem": ceRedunRemoteSystem,
       "ceRedunOneToN": ceRedunOneToN,
       "ceRedunMemberStatus": ceRedunMemberStatus,
       "ceRedunOptionalMbrStatus": ceRedunOptionalMbrStatus,
       "ceRedunCommandsGroup": ceRedunCommandsGroup,
       "ceRedunNotifEnables": ceRedunNotifEnables,
       "ceRedunSwitchNotifGroup": ceRedunSwitchNotifGroup,
       "ceRedunProtectStatusNotifGroup": ceRedunProtectStatusNotifGroup}
)
