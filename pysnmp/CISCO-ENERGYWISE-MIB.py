# SNMP MIB module (CISCO-ENERGYWISE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENERGYWISE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:20 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(entPhysicalIndex,
 entityMIBObjects) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entityMIBObjects")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoEnergywiseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 683)
)
ciscoEnergywiseMIB.setRevisions(
        ("2010-07-09 00:00",
         "2010-03-26 00:00",
         "2009-11-22 00:00",
         "2009-10-21 00:00",
         "2009-05-20 00:00",
         "2009-05-08 00:00",
         "2009-01-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnergywiseLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("frugal", 7),
          ("full", 11),
          ("hibernate", 2),
          ("high", 10),
          ("low", 6),
          ("medium", 8),
          ("ready", 5),
          ("reduced", 9),
          ("shut", 1),
          ("sleep", 3),
          ("standby", 4))
    )



class EnergywiseId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class EnergywisePowerUnits(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )



class EnergywiseKeywordList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEnergywiseMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEnergywiseMIBNotifs = _CiscoEnergywiseMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 0)
)
_CiscoEnergywiseMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEnergywiseMIBObjects = _CiscoEnergywiseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1)
)
_CewDeviceId_Type = EnergywiseId
_CewDeviceId_Object = MibScalar
cewDeviceId = _CewDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 1),
    _CewDeviceId_Type()
)
cewDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewDeviceId.setStatus("current")
_CewDeviceNeighborCount_Type = Gauge32
_CewDeviceNeighborCount_Object = MibScalar
cewDeviceNeighborCount = _CewDeviceNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 2),
    _CewDeviceNeighborCount_Type()
)
cewDeviceNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewDeviceNeighborCount.setStatus("current")
if mibBuilder.loadTexts:
    cewDeviceNeighborCount.setUnits("neighbors")
_CewDomainName_Type = SnmpAdminString
_CewDomainName_Object = MibScalar
cewDomainName = _CewDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 3),
    _CewDomainName_Type()
)
cewDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewDomainName.setStatus("current")
_CewMaxImportance_Type = Gauge32
_CewMaxImportance_Object = MibScalar
cewMaxImportance = _CewMaxImportance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 4),
    _CewMaxImportance_Type()
)
cewMaxImportance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewMaxImportance.setStatus("current")
if mibBuilder.loadTexts:
    cewMaxImportance.setUnits("importance")
_CewMaxImportanceId_Type = EnergywiseId
_CewMaxImportanceId_Object = MibScalar
cewMaxImportanceId = _CewMaxImportanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 5),
    _CewMaxImportanceId_Type()
)
cewMaxImportanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewMaxImportanceId.setStatus("current")
_CewEntTable_Object = MibTable
cewEntTable = _CewEntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6)
)
if mibBuilder.loadTexts:
    cewEntTable.setStatus("current")
_CewEntEntry_Object = MibTableRow
cewEntEntry = _CewEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1)
)
cewEntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cewEntEntry.setStatus("current")


class _CewEntNannyVector_Type(Bits):
    """Custom type cewEntNannyVector based on Bits"""
    namedValues = NamedValues(
        *(("powerImportance", 14),
          ("powerLevel1", 1),
          ("powerLevel10", 10),
          ("powerLevel11", 11),
          ("powerLevel2", 2),
          ("powerLevel3", 3),
          ("powerLevel4", 4),
          ("powerLevel5", 5),
          ("powerLevel6", 6),
          ("powerLevel7", 7),
          ("powerLevel8", 8),
          ("powerLevel9", 9),
          ("powerShutNWakeUp", 12),
          ("powerUsage", 13),
          ("powerWakeUp", 0))
    )

_CewEntNannyVector_Type.__name__ = "Bits"
_CewEntNannyVector_Object = MibTableColumn
cewEntNannyVector = _CewEntNannyVector_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 1),
    _CewEntNannyVector_Type()
)
cewEntNannyVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntNannyVector.setStatus("current")


class _CewEntNeighborIndex_Type(Unsigned32):
    """Custom type cewEntNeighborIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CewEntNeighborIndex_Type.__name__ = "Unsigned32"
_CewEntNeighborIndex_Object = MibTableColumn
cewEntNeighborIndex = _CewEntNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 2),
    _CewEntNeighborIndex_Type()
)
cewEntNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntNeighborIndex.setStatus("current")
_CewEntKeyword_Type = EnergywiseKeywordList
_CewEntKeyword_Object = MibTableColumn
cewEntKeyword = _CewEntKeyword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 3),
    _CewEntKeyword_Type()
)
cewEntKeyword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEntKeyword.setStatus("current")
_CewEntName_Type = SnmpAdminString
_CewEntName_Object = MibTableColumn
cewEntName = _CewEntName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 4),
    _CewEntName_Type()
)
cewEntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEntName.setStatus("current")
_CewEntRoleDescription_Type = SnmpAdminString
_CewEntRoleDescription_Object = MibTableColumn
cewEntRoleDescription = _CewEntRoleDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 5),
    _CewEntRoleDescription_Type()
)
cewEntRoleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEntRoleDescription.setStatus("current")
_CewEntFullName_Type = SnmpAdminString
_CewEntFullName_Object = MibTableColumn
cewEntFullName = _CewEntFullName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 6),
    _CewEntFullName_Type()
)
cewEntFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntFullName.setStatus("current")
_CewEntEnergyUnits_Type = EnergywisePowerUnits
_CewEntEnergyUnits_Object = MibTableColumn
cewEntEnergyUnits = _CewEntEnergyUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 7),
    _CewEntEnergyUnits_Type()
)
cewEntEnergyUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntEnergyUnits.setStatus("current")


class _CewEntEnergyUsage_Type(Unsigned32):
    """Custom type cewEntEnergyUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CewEntEnergyUsage_Type.__name__ = "Unsigned32"
_CewEntEnergyUsage_Object = MibTableColumn
cewEntEnergyUsage = _CewEntEnergyUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 8),
    _CewEntEnergyUsage_Type()
)
cewEntEnergyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntEnergyUsage.setStatus("current")


class _CewEntEnergyUsageCaliber_Type(Integer32):
    """Custom type cewEntEnergyUsageCaliber based on Integer32"""
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
        *(("actual", 4),
          ("max", 1),
          ("presumed", 2),
          ("trusted", 5),
          ("unknown", 3))
    )


_CewEntEnergyUsageCaliber_Type.__name__ = "Integer32"
_CewEntEnergyUsageCaliber_Object = MibTableColumn
cewEntEnergyUsageCaliber = _CewEntEnergyUsageCaliber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 9),
    _CewEntEnergyUsageCaliber_Type()
)
cewEntEnergyUsageCaliber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntEnergyUsageCaliber.setStatus("current")
_CewEntEnergyLevel_Type = EnergywiseLevel
_CewEntEnergyLevel_Object = MibTableColumn
cewEntEnergyLevel = _CewEntEnergyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 10),
    _CewEntEnergyLevel_Type()
)
cewEntEnergyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntEnergyLevel.setStatus("current")


class _CewEntEnergyUsageProvisioned_Type(Unsigned32):
    """Custom type cewEntEnergyUsageProvisioned based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CewEntEnergyUsageProvisioned_Type.__name__ = "Unsigned32"
_CewEntEnergyUsageProvisioned_Object = MibTableColumn
cewEntEnergyUsageProvisioned = _CewEntEnergyUsageProvisioned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 11),
    _CewEntEnergyUsageProvisioned_Type()
)
cewEntEnergyUsageProvisioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntEnergyUsageProvisioned.setStatus("current")


class _CewEntImportanceInt_Type(Unsigned32):
    """Custom type cewEntImportanceInt based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CewEntImportanceInt_Type.__name__ = "Unsigned32"
_CewEntImportanceInt_Object = MibTableColumn
cewEntImportanceInt = _CewEntImportanceInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 12),
    _CewEntImportanceInt_Type()
)
cewEntImportanceInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEntImportanceInt.setStatus("current")


class _CewEntImportanceExt_Type(Unsigned32):
    """Custom type cewEntImportanceExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CewEntImportanceExt_Type.__name__ = "Unsigned32"
_CewEntImportanceExt_Object = MibTableColumn
cewEntImportanceExt = _CewEntImportanceExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 13),
    _CewEntImportanceExt_Type()
)
cewEntImportanceExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntImportanceExt.setStatus("current")


class _CewEntImportanceRelative_Type(Unsigned32):
    """Custom type cewEntImportanceRelative based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CewEntImportanceRelative_Type.__name__ = "Unsigned32"
_CewEntImportanceRelative_Object = MibTableColumn
cewEntImportanceRelative = _CewEntImportanceRelative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 14),
    _CewEntImportanceRelative_Type()
)
cewEntImportanceRelative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntImportanceRelative.setStatus("current")
_CewEntImportanceParentId_Type = EnergywiseId
_CewEntImportanceParentId_Object = MibTableColumn
cewEntImportanceParentId = _CewEntImportanceParentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 15),
    _CewEntImportanceParentId_Type()
)
cewEntImportanceParentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntImportanceParentId.setStatus("current")
_CewEntParentId_Type = EnergywiseId
_CewEntParentId_Object = MibTableColumn
cewEntParentId = _CewEntParentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 16),
    _CewEntParentId_Type()
)
cewEntParentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntParentId.setStatus("current")


class _CewEntAdminStatus_Type(Integer32):
    """Custom type cewEntAdminStatus based on Integer32"""
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


_CewEntAdminStatus_Type.__name__ = "Integer32"
_CewEntAdminStatus_Object = MibTableColumn
cewEntAdminStatus = _CewEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 17),
    _CewEntAdminStatus_Type()
)
cewEntAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEntAdminStatus.setStatus("current")


class _CewEntOperStatus_Type(Integer32):
    """Custom type cewEntOperStatus based on Integer32"""
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
          ("error", 3),
          ("up", 1))
    )


_CewEntOperStatus_Type.__name__ = "Integer32"
_CewEntOperStatus_Object = MibTableColumn
cewEntOperStatus = _CewEntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 18),
    _CewEntOperStatus_Type()
)
cewEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntOperStatus.setStatus("current")
_CewEntConfiguredLevel_Type = EnergywiseLevel
_CewEntConfiguredLevel_Object = MibTableColumn
cewEntConfiguredLevel = _CewEntConfiguredLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 19),
    _CewEntConfiguredLevel_Type()
)
cewEntConfiguredLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEntConfiguredLevel.setStatus("current")


class _CewEntEnergyUsageCategory_Type(Integer32):
    """Custom type cewEntEnergyUsageCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("consumer", 1),
          ("meter", 3),
          ("producer", 2))
    )


_CewEntEnergyUsageCategory_Type.__name__ = "Integer32"
_CewEntEnergyUsageCategory_Object = MibTableColumn
cewEntEnergyUsageCategory = _CewEntEnergyUsageCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 20),
    _CewEntEnergyUsageCategory_Type()
)
cewEntEnergyUsageCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntEnergyUsageCategory.setStatus("current")


class _CewEntEnergyUsageDirection_Type(Integer32):
    """Custom type cewEntEnergyUsageDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", -1))
    )


_CewEntEnergyUsageDirection_Type.__name__ = "Integer32"
_CewEntEnergyUsageDirection_Object = MibTableColumn
cewEntEnergyUsageDirection = _CewEntEnergyUsageDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 21),
    _CewEntEnergyUsageDirection_Type()
)
cewEntEnergyUsageDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewEntEnergyUsageDirection.setStatus("current")
_CewEntAllowSet_Type = TruthValue
_CewEntAllowSet_Object = MibTableColumn
cewEntAllowSet = _CewEntAllowSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 22),
    _CewEntAllowSet_Type()
)
cewEntAllowSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEntAllowSet.setStatus("current")
_CewEntActivityCheck_Type = TruthValue
_CewEntActivityCheck_Object = MibTableColumn
cewEntActivityCheck = _CewEntActivityCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 6, 1, 23),
    _CewEntActivityCheck_Type()
)
cewEntActivityCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEntActivityCheck.setStatus("current")
_CewLevelTable_Object = MibTable
cewLevelTable = _CewLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 7)
)
if mibBuilder.loadTexts:
    cewLevelTable.setStatus("current")
_CewLevelEntry_Object = MibTableRow
cewLevelEntry = _CewLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 7, 1)
)
cewLevelEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENERGYWISE-MIB", "cewLevelIndex"),
)
if mibBuilder.loadTexts:
    cewLevelEntry.setStatus("current")
_CewLevelIndex_Type = EnergywiseLevel
_CewLevelIndex_Object = MibTableColumn
cewLevelIndex = _CewLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 7, 1, 1),
    _CewLevelIndex_Type()
)
cewLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewLevelIndex.setStatus("current")


class _CewLevelMaxUsage_Type(Unsigned32):
    """Custom type cewLevelMaxUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CewLevelMaxUsage_Type.__name__ = "Unsigned32"
_CewLevelMaxUsage_Object = MibTableColumn
cewLevelMaxUsage = _CewLevelMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 7, 1, 2),
    _CewLevelMaxUsage_Type()
)
cewLevelMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewLevelMaxUsage.setStatus("current")


class _CewLevelDeltaUsage_Type(Integer32):
    """Custom type cewLevelDeltaUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CewLevelDeltaUsage_Type.__name__ = "Integer32"
_CewLevelDeltaUsage_Object = MibTableColumn
cewLevelDeltaUsage = _CewLevelDeltaUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 7, 1, 3),
    _CewLevelDeltaUsage_Type()
)
cewLevelDeltaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewLevelDeltaUsage.setStatus("current")
_CewLevelUnits_Type = EnergywisePowerUnits
_CewLevelUnits_Object = MibTableColumn
cewLevelUnits = _CewLevelUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 7, 1, 4),
    _CewLevelUnits_Type()
)
cewLevelUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewLevelUnits.setStatus("current")
_CewProxyTable_Object = MibTable
cewProxyTable = _CewProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8)
)
if mibBuilder.loadTexts:
    cewProxyTable.setStatus("current")
_CewProxyEntry_Object = MibTableRow
cewProxyEntry = _CewProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8, 1)
)
cewProxyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENERGYWISE-MIB", "cewProxyId"),
)
if mibBuilder.loadTexts:
    cewProxyEntry.setStatus("current")


class _CewProxyId_Type(Unsigned32):
    """Custom type cewProxyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CewProxyId_Type.__name__ = "Unsigned32"
_CewProxyId_Object = MibTableColumn
cewProxyId = _CewProxyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8, 1, 1),
    _CewProxyId_Type()
)
cewProxyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewProxyId.setStatus("current")
_CewProxyAddressType_Type = InetAddressType
_CewProxyAddressType_Object = MibTableColumn
cewProxyAddressType = _CewProxyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8, 1, 2),
    _CewProxyAddressType_Type()
)
cewProxyAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewProxyAddressType.setStatus("current")
_CewProxyAddress_Type = InetAddress
_CewProxyAddress_Object = MibTableColumn
cewProxyAddress = _CewProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8, 1, 3),
    _CewProxyAddress_Type()
)
cewProxyAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewProxyAddress.setStatus("current")
_CewProxyPort_Type = InetPortNumber
_CewProxyPort_Object = MibTableColumn
cewProxyPort = _CewProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8, 1, 4),
    _CewProxyPort_Type()
)
cewProxyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewProxyPort.setStatus("current")
_CewProxyClass_Type = SnmpAdminString
_CewProxyClass_Object = MibTableColumn
cewProxyClass = _CewProxyClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8, 1, 5),
    _CewProxyClass_Type()
)
cewProxyClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewProxyClass.setStatus("current")


class _CewProxyStorage_Type(StorageType):
    """Custom type cewProxyStorage based on StorageType"""


_CewProxyStorage_Object = MibTableColumn
cewProxyStorage = _CewProxyStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8, 1, 6),
    _CewProxyStorage_Type()
)
cewProxyStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewProxyStorage.setStatus("current")
_CewProxyStatus_Type = RowStatus
_CewProxyStatus_Object = MibTableColumn
cewProxyStatus = _CewProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 8, 1, 7),
    _CewProxyStatus_Type()
)
cewProxyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewProxyStatus.setStatus("current")
_CewNeighborTable_Object = MibTable
cewNeighborTable = _CewNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9)
)
if mibBuilder.loadTexts:
    cewNeighborTable.setStatus("current")
_CewNeighborEntry_Object = MibTableRow
cewNeighborEntry = _CewNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1)
)
cewNeighborEntry.setIndexNames(
    (0, "CISCO-ENERGYWISE-MIB", "cewNeighborIndex"),
)
if mibBuilder.loadTexts:
    cewNeighborEntry.setStatus("current")


class _CewNeighborIndex_Type(Unsigned32):
    """Custom type cewNeighborIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CewNeighborIndex_Type.__name__ = "Unsigned32"
_CewNeighborIndex_Object = MibTableColumn
cewNeighborIndex = _CewNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 1),
    _CewNeighborIndex_Type()
)
cewNeighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewNeighborIndex.setStatus("current")
_CewNeighborId_Type = EnergywiseId
_CewNeighborId_Object = MibTableColumn
cewNeighborId = _CewNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 2),
    _CewNeighborId_Type()
)
cewNeighborId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewNeighborId.setStatus("current")


class _CewNeighborType_Type(Integer32):
    """Custom type cewNeighborType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("child", 3),
          ("dynamic", 2),
          ("static", 1))
    )


_CewNeighborType_Type.__name__ = "Integer32"
_CewNeighborType_Object = MibTableColumn
cewNeighborType = _CewNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 3),
    _CewNeighborType_Type()
)
cewNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborType.setStatus("current")
_CewNeighborHeartBeat_Type = TimeStamp
_CewNeighborHeartBeat_Object = MibTableColumn
cewNeighborHeartBeat = _CewNeighborHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 4),
    _CewNeighborHeartBeat_Type()
)
cewNeighborHeartBeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborHeartBeat.setStatus("current")


class _CewNeighborStorage_Type(StorageType):
    """Custom type cewNeighborStorage based on StorageType"""


_CewNeighborStorage_Object = MibTableColumn
cewNeighborStorage = _CewNeighborStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 5),
    _CewNeighborStorage_Type()
)
cewNeighborStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewNeighborStorage.setStatus("current")
_CewNeighborStatus_Type = RowStatus
_CewNeighborStatus_Object = MibTableColumn
cewNeighborStatus = _CewNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 6),
    _CewNeighborStatus_Type()
)
cewNeighborStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewNeighborStatus.setStatus("current")
_CewNeighborDeviceType_Type = SnmpAdminString
_CewNeighborDeviceType_Object = MibTableColumn
cewNeighborDeviceType = _CewNeighborDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 7),
    _CewNeighborDeviceType_Type()
)
cewNeighborDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborDeviceType.setStatus("current")
_CewNeighborKeyword_Type = EnergywiseKeywordList
_CewNeighborKeyword_Object = MibTableColumn
cewNeighborKeyword = _CewNeighborKeyword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 8),
    _CewNeighborKeyword_Type()
)
cewNeighborKeyword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborKeyword.setStatus("current")
_CewNeighborConfiguredKeyword_Type = EnergywiseKeywordList
_CewNeighborConfiguredKeyword_Object = MibTableColumn
cewNeighborConfiguredKeyword = _CewNeighborConfiguredKeyword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 9),
    _CewNeighborConfiguredKeyword_Type()
)
cewNeighborConfiguredKeyword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewNeighborConfiguredKeyword.setStatus("current")
_CewNeighborName_Type = SnmpAdminString
_CewNeighborName_Object = MibTableColumn
cewNeighborName = _CewNeighborName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 10),
    _CewNeighborName_Type()
)
cewNeighborName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborName.setStatus("current")
_CewNeighborConfiguredName_Type = SnmpAdminString
_CewNeighborConfiguredName_Object = MibTableColumn
cewNeighborConfiguredName = _CewNeighborConfiguredName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 11),
    _CewNeighborConfiguredName_Type()
)
cewNeighborConfiguredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewNeighborConfiguredName.setStatus("current")
_CewNeighborRoleDescription_Type = SnmpAdminString
_CewNeighborRoleDescription_Object = MibTableColumn
cewNeighborRoleDescription = _CewNeighborRoleDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 12),
    _CewNeighborRoleDescription_Type()
)
cewNeighborRoleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborRoleDescription.setStatus("current")
_CewNeighborConfiguredRoleDesc_Type = SnmpAdminString
_CewNeighborConfiguredRoleDesc_Object = MibTableColumn
cewNeighborConfiguredRoleDesc = _CewNeighborConfiguredRoleDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 13),
    _CewNeighborConfiguredRoleDesc_Type()
)
cewNeighborConfiguredRoleDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewNeighborConfiguredRoleDesc.setStatus("current")
_CewNeighborEnergyLevel_Type = EnergywiseLevel
_CewNeighborEnergyLevel_Object = MibTableColumn
cewNeighborEnergyLevel = _CewNeighborEnergyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 14),
    _CewNeighborEnergyLevel_Type()
)
cewNeighborEnergyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborEnergyLevel.setStatus("current")
_CewNeighborConfiguredLevel_Type = EnergywiseLevel
_CewNeighborConfiguredLevel_Object = MibTableColumn
cewNeighborConfiguredLevel = _CewNeighborConfiguredLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 15),
    _CewNeighborConfiguredLevel_Type()
)
cewNeighborConfiguredLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewNeighborConfiguredLevel.setStatus("current")


class _CewNeighborImportance_Type(Unsigned32):
    """Custom type cewNeighborImportance based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CewNeighborImportance_Type.__name__ = "Unsigned32"
_CewNeighborImportance_Object = MibTableColumn
cewNeighborImportance = _CewNeighborImportance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 16),
    _CewNeighborImportance_Type()
)
cewNeighborImportance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborImportance.setStatus("current")


class _CewNeighborConfiguredImportance_Type(Unsigned32):
    """Custom type cewNeighborConfiguredImportance based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CewNeighborConfiguredImportance_Type.__name__ = "Unsigned32"
_CewNeighborConfiguredImportance_Object = MibTableColumn
cewNeighborConfiguredImportance = _CewNeighborConfiguredImportance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 17),
    _CewNeighborConfiguredImportance_Type()
)
cewNeighborConfiguredImportance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewNeighborConfiguredImportance.setStatus("current")
_CewNeighborEnergyUnits_Type = EnergywisePowerUnits
_CewNeighborEnergyUnits_Object = MibTableColumn
cewNeighborEnergyUnits = _CewNeighborEnergyUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 18),
    _CewNeighborEnergyUnits_Type()
)
cewNeighborEnergyUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborEnergyUnits.setStatus("current")


class _CewNeighborEnergyUsage_Type(Unsigned32):
    """Custom type cewNeighborEnergyUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CewNeighborEnergyUsage_Type.__name__ = "Unsigned32"
_CewNeighborEnergyUsage_Object = MibTableColumn
cewNeighborEnergyUsage = _CewNeighborEnergyUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 19),
    _CewNeighborEnergyUsage_Type()
)
cewNeighborEnergyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborEnergyUsage.setStatus("current")


class _CewNeighborEnergyUsageCategory_Type(Integer32):
    """Custom type cewNeighborEnergyUsageCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("consumer", 1),
          ("meter", 3),
          ("producer", 2))
    )


_CewNeighborEnergyUsageCategory_Type.__name__ = "Integer32"
_CewNeighborEnergyUsageCategory_Object = MibTableColumn
cewNeighborEnergyUsageCategory = _CewNeighborEnergyUsageCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 20),
    _CewNeighborEnergyUsageCategory_Type()
)
cewNeighborEnergyUsageCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborEnergyUsageCategory.setStatus("current")


class _CewNeighborEnergyUsageDirection_Type(Integer32):
    """Custom type cewNeighborEnergyUsageDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", -1))
    )


_CewNeighborEnergyUsageDirection_Type.__name__ = "Integer32"
_CewNeighborEnergyUsageDirection_Object = MibTableColumn
cewNeighborEnergyUsageDirection = _CewNeighborEnergyUsageDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 21),
    _CewNeighborEnergyUsageDirection_Type()
)
cewNeighborEnergyUsageDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborEnergyUsageDirection.setStatus("current")
_CewNeighborMacAddress_Type = MacAddress
_CewNeighborMacAddress_Object = MibTableColumn
cewNeighborMacAddress = _CewNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 22),
    _CewNeighborMacAddress_Type()
)
cewNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborMacAddress.setStatus("current")
_CewNeighborPhysicalEntityId_Type = EntPhysicalIndexOrZero
_CewNeighborPhysicalEntityId_Object = MibTableColumn
cewNeighborPhysicalEntityId = _CewNeighborPhysicalEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 23),
    _CewNeighborPhysicalEntityId_Type()
)
cewNeighborPhysicalEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborPhysicalEntityId.setStatus("current")
_CewNeighborParentPortIndex_Type = EntPhysicalIndexOrZero
_CewNeighborParentPortIndex_Object = MibTableColumn
cewNeighborParentPortIndex = _CewNeighborParentPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 9, 1, 24),
    _CewNeighborParentPortIndex_Type()
)
cewNeighborParentPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborParentPortIndex.setStatus("current")
_CewEventTable_Object = MibTable
cewEventTable = _CewEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10)
)
if mibBuilder.loadTexts:
    cewEventTable.setStatus("current")
_CewEventEntry_Object = MibTableRow
cewEventEntry = _CewEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10, 1)
)
cewEventEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENERGYWISE-MIB", "cewEventIndex"),
)
if mibBuilder.loadTexts:
    cewEventEntry.setStatus("current")


class _CewEventIndex_Type(Unsigned32):
    """Custom type cewEventIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CewEventIndex_Type.__name__ = "Unsigned32"
_CewEventIndex_Object = MibTableColumn
cewEventIndex = _CewEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10, 1, 1),
    _CewEventIndex_Type()
)
cewEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewEventIndex.setStatus("current")
_CewEventLevel_Type = EnergywiseLevel
_CewEventLevel_Object = MibTableColumn
cewEventLevel = _CewEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10, 1, 2),
    _CewEventLevel_Type()
)
cewEventLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewEventLevel.setStatus("current")


class _CewEventRecurrence_Type(TruthValue):
    """Custom type cewEventRecurrence based on TruthValue"""


_CewEventRecurrence_Object = MibTableColumn
cewEventRecurrence = _CewEventRecurrence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10, 1, 3),
    _CewEventRecurrence_Type()
)
cewEventRecurrence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewEventRecurrence.setStatus("current")
_CewEventTime_Type = SnmpAdminString
_CewEventTime_Object = MibTableColumn
cewEventTime = _CewEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10, 1, 4),
    _CewEventTime_Type()
)
cewEventTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewEventTime.setStatus("current")


class _CewEventStorage_Type(StorageType):
    """Custom type cewEventStorage based on StorageType"""


_CewEventStorage_Object = MibTableColumn
cewEventStorage = _CewEventStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10, 1, 5),
    _CewEventStorage_Type()
)
cewEventStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewEventStorage.setStatus("current")
_CewEventStatus_Type = RowStatus
_CewEventStatus_Object = MibTableColumn
cewEventStatus = _CewEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10, 1, 6),
    _CewEventStatus_Type()
)
cewEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewEventStatus.setStatus("current")


class _CewEventImportance_Type(Unsigned32):
    """Custom type cewEventImportance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CewEventImportance_Type.__name__ = "Unsigned32"
_CewEventImportance_Object = MibTableColumn
cewEventImportance = _CewEventImportance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 10, 1, 7),
    _CewEventImportance_Type()
)
cewEventImportance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewEventImportance.setStatus("current")
_CewLevelChangeNotifEnable_Type = TruthValue
_CewLevelChangeNotifEnable_Object = MibScalar
cewLevelChangeNotifEnable = _CewLevelChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 11),
    _CewLevelChangeNotifEnable_Type()
)
cewLevelChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewLevelChangeNotifEnable.setStatus("current")
_CewNeighborAddedNotifEnable_Type = TruthValue
_CewNeighborAddedNotifEnable_Object = MibScalar
cewNeighborAddedNotifEnable = _CewNeighborAddedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 12),
    _CewNeighborAddedNotifEnable_Type()
)
cewNeighborAddedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewNeighborAddedNotifEnable.setStatus("current")
_CewNeighborDeletedNotifEnable_Type = TruthValue
_CewNeighborDeletedNotifEnable_Object = MibScalar
cewNeighborDeletedNotifEnable = _CewNeighborDeletedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 13),
    _CewNeighborDeletedNotifEnable_Type()
)
cewNeighborDeletedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewNeighborDeletedNotifEnable.setStatus("current")
_CewEventOccuredNotifEnable_Type = TruthValue
_CewEventOccuredNotifEnable_Object = MibScalar
cewEventOccuredNotifEnable = _CewEventOccuredNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 14),
    _CewEventOccuredNotifEnable_Type()
)
cewEventOccuredNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEventOccuredNotifEnable.setStatus("current")


class _CewEventOccuredErrorCode_Type(Integer32):
    """Custom type cewEventOccuredErrorCode based on Integer32"""
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
        *(("hwfault", 5),
          ("noerror", 1),
          ("outofrange", 3),
          ("swfault", 4),
          ("wrongtype", 2))
    )


_CewEventOccuredErrorCode_Type.__name__ = "Integer32"
_CewEventOccuredErrorCode_Object = MibScalar
cewEventOccuredErrorCode = _CewEventOccuredErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 15),
    _CewEventOccuredErrorCode_Type()
)
cewEventOccuredErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cewEventOccuredErrorCode.setStatus("current")
_CewManagementSecret_Type = SnmpAdminString
_CewManagementSecret_Object = MibScalar
cewManagementSecret = _CewManagementSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 16),
    _CewManagementSecret_Type()
)
cewManagementSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewManagementSecret.setStatus("current")
_CewEndPointSecret_Type = SnmpAdminString
_CewEndPointSecret_Object = MibScalar
cewEndPointSecret = _CewEndPointSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 17),
    _CewEndPointSecret_Type()
)
cewEndPointSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEndPointSecret.setStatus("current")
_CewDomainSecret_Type = SnmpAdminString
_CewDomainSecret_Object = MibScalar
cewDomainSecret = _CewDomainSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 18),
    _CewDomainSecret_Type()
)
cewDomainSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewDomainSecret.setStatus("current")


class _CewProtocol_Type(Integer32):
    """Custom type cewProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("udp", 1)
    )


_CewProtocol_Type.__name__ = "Integer32"
_CewProtocol_Object = MibScalar
cewProtocol = _CewProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 19),
    _CewProtocol_Type()
)
cewProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewProtocol.setStatus("current")
_CewAddressType_Type = InetAddressType
_CewAddressType_Object = MibScalar
cewAddressType = _CewAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 20),
    _CewAddressType_Type()
)
cewAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewAddressType.setStatus("current")
_CewAddress_Type = InetAddress
_CewAddress_Object = MibScalar
cewAddress = _CewAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 21),
    _CewAddress_Type()
)
cewAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewAddress.setStatus("current")
_CewPort_Type = InetPortNumber
_CewPort_Object = MibScalar
cewPort = _CewPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 22),
    _CewPort_Type()
)
cewPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewPort.setStatus("current")


class _CewEnable_Type(Integer32):
    """Custom type cewEnable based on Integer32"""
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


_CewEnable_Type.__name__ = "Integer32"
_CewEnable_Object = MibScalar
cewEnable = _CewEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 23),
    _CewEnable_Type()
)
cewEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewEnable.setStatus("current")
_CewVersion_Type = SnmpAdminString
_CewVersion_Object = MibScalar
cewVersion = _CewVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 24),
    _CewVersion_Type()
)
cewVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewVersion.setStatus("current")


class _CewDeviceTotalUsage_Type(Unsigned32):
    """Custom type cewDeviceTotalUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CewDeviceTotalUsage_Type.__name__ = "Unsigned32"
_CewDeviceTotalUsage_Object = MibScalar
cewDeviceTotalUsage = _CewDeviceTotalUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 25),
    _CewDeviceTotalUsage_Type()
)
cewDeviceTotalUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewDeviceTotalUsage.setStatus("current")
if mibBuilder.loadTexts:
    cewDeviceTotalUsage.setUnits("watts")
_CewDeviceTotalUsageUnits_Type = EnergywisePowerUnits
_CewDeviceTotalUsageUnits_Object = MibScalar
cewDeviceTotalUsageUnits = _CewDeviceTotalUsageUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 26),
    _CewDeviceTotalUsageUnits_Type()
)
cewDeviceTotalUsageUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewDeviceTotalUsageUnits.setStatus("current")
if mibBuilder.loadTexts:
    cewDeviceTotalUsageUnits.setUnits("watts")
_CewDeviceType_Type = SnmpAdminString
_CewDeviceType_Object = MibScalar
cewDeviceType = _CewDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 27),
    _CewDeviceType_Type()
)
cewDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewDeviceType.setStatus("current")
_CewAllowSet_Type = TruthValue
_CewAllowSet_Object = MibScalar
cewAllowSet = _CewAllowSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 28),
    _CewAllowSet_Type()
)
cewAllowSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewAllowSet.setStatus("current")
_CewNeighborLevelTable_Object = MibTable
cewNeighborLevelTable = _CewNeighborLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 29)
)
if mibBuilder.loadTexts:
    cewNeighborLevelTable.setStatus("current")
_CewNeighborLevelEntry_Object = MibTableRow
cewNeighborLevelEntry = _CewNeighborLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 29, 1)
)
cewNeighborLevelEntry.setIndexNames(
    (0, "CISCO-ENERGYWISE-MIB", "cewNeighborIndex"),
    (0, "CISCO-ENERGYWISE-MIB", "cewNeighborLevelIndex"),
)
if mibBuilder.loadTexts:
    cewNeighborLevelEntry.setStatus("current")
_CewNeighborLevelIndex_Type = EnergywiseLevel
_CewNeighborLevelIndex_Object = MibTableColumn
cewNeighborLevelIndex = _CewNeighborLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 29, 1, 1),
    _CewNeighborLevelIndex_Type()
)
cewNeighborLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewNeighborLevelIndex.setStatus("current")


class _CewNeighborLevelMaxUsage_Type(Unsigned32):
    """Custom type cewNeighborLevelMaxUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CewNeighborLevelMaxUsage_Type.__name__ = "Unsigned32"
_CewNeighborLevelMaxUsage_Object = MibTableColumn
cewNeighborLevelMaxUsage = _CewNeighborLevelMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 29, 1, 2),
    _CewNeighborLevelMaxUsage_Type()
)
cewNeighborLevelMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborLevelMaxUsage.setStatus("current")


class _CewNeighborLevelDeltaUsage_Type(Integer32):
    """Custom type cewNeighborLevelDeltaUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CewNeighborLevelDeltaUsage_Type.__name__ = "Integer32"
_CewNeighborLevelDeltaUsage_Object = MibTableColumn
cewNeighborLevelDeltaUsage = _CewNeighborLevelDeltaUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 29, 1, 3),
    _CewNeighborLevelDeltaUsage_Type()
)
cewNeighborLevelDeltaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborLevelDeltaUsage.setStatus("current")
_CewNeighborLevelUnits_Type = EnergywisePowerUnits
_CewNeighborLevelUnits_Object = MibTableColumn
cewNeighborLevelUnits = _CewNeighborLevelUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 1, 29, 1, 4),
    _CewNeighborLevelUnits_Type()
)
cewNeighborLevelUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewNeighborLevelUnits.setStatus("current")
_CiscoEnergywiseMIBConform_ObjectIdentity = ObjectIdentity
ciscoEnergywiseMIBConform = _CiscoEnergywiseMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2)
)
_CiscoEnergywiseMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEnergywiseMIBCompliances = _CiscoEnergywiseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1)
)
_CiscoEnergywiseMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEnergywiseMIBGroups = _CiscoEnergywiseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2)
)

# Managed Objects groups

ciscoEnergywiseEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 1)
)
ciscoEnergywiseEntityGroup.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewMaxImportance"),
        ("CISCO-ENERGYWISE-MIB", "cewMaxImportanceId"),
        ("CISCO-ENERGYWISE-MIB", "cewEntNeighborIndex"),
        ("CISCO-ENERGYWISE-MIB", "cewEntNannyVector"),
        ("CISCO-ENERGYWISE-MIB", "cewEntKeyword"),
        ("CISCO-ENERGYWISE-MIB", "cewEntName"),
        ("CISCO-ENERGYWISE-MIB", "cewEntRoleDescription"),
        ("CISCO-ENERGYWISE-MIB", "cewEntFullName"),
        ("CISCO-ENERGYWISE-MIB", "cewEntEnergyUnits"),
        ("CISCO-ENERGYWISE-MIB", "cewEntEnergyUsage"),
        ("CISCO-ENERGYWISE-MIB", "cewEntEnergyLevel"),
        ("CISCO-ENERGYWISE-MIB", "cewEntEnergyUsageProvisioned"),
        ("CISCO-ENERGYWISE-MIB", "cewEntImportanceInt"),
        ("CISCO-ENERGYWISE-MIB", "cewEntImportanceExt"),
        ("CISCO-ENERGYWISE-MIB", "cewEntImportanceParentId"),
        ("CISCO-ENERGYWISE-MIB", "cewEntParentId"),
        ("CISCO-ENERGYWISE-MIB", "cewEntImportanceRelative"),
        ("CISCO-ENERGYWISE-MIB", "cewEntAdminStatus"),
        ("CISCO-ENERGYWISE-MIB", "cewEntOperStatus"),
        ("CISCO-ENERGYWISE-MIB", "cewLevelMaxUsage"),
        ("CISCO-ENERGYWISE-MIB", "cewLevelDeltaUsage"),
        ("CISCO-ENERGYWISE-MIB", "cewLevelUnits"),
        ("CISCO-ENERGYWISE-MIB", "cewDeviceId"),
        ("CISCO-ENERGYWISE-MIB", "cewDeviceNeighborCount"),
        ("CISCO-ENERGYWISE-MIB", "cewEntEnergyUsageCaliber"),
        ("CISCO-ENERGYWISE-MIB", "cewDomainName"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseEntityGroup.setStatus("current")

ciscoEnergywiseNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 2)
)
ciscoEnergywiseNeighborGroup.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewNeighborId"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborType"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborHeartBeat"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborStatus"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborStorage"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseNeighborGroup.setStatus("current")

ciscoEnergywiseEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 3)
)
ciscoEnergywiseEventGroup.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewEventLevel"),
        ("CISCO-ENERGYWISE-MIB", "cewEventRecurrence"),
        ("CISCO-ENERGYWISE-MIB", "cewEventStatus"),
        ("CISCO-ENERGYWISE-MIB", "cewEventTime"),
        ("CISCO-ENERGYWISE-MIB", "cewEventStorage"),
        ("CISCO-ENERGYWISE-MIB", "cewEventOccuredErrorCode"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseEventGroup.setStatus("current")

ciscoEnergywiseProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 4)
)
ciscoEnergywiseProxyGroup.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewProxyAddressType"),
        ("CISCO-ENERGYWISE-MIB", "cewProxyAddress"),
        ("CISCO-ENERGYWISE-MIB", "cewProxyPort"),
        ("CISCO-ENERGYWISE-MIB", "cewProxyClass"),
        ("CISCO-ENERGYWISE-MIB", "cewProxyStorage"),
        ("CISCO-ENERGYWISE-MIB", "cewProxyStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseProxyGroup.setStatus("current")

ciscoEnergywiseNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 6)
)
ciscoEnergywiseNotifEnableGroup.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewLevelChangeNotifEnable"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborAddedNotifEnable"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborDeletedNotifEnable"),
        ("CISCO-ENERGYWISE-MIB", "cewEventOccuredNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseNotifEnableGroup.setStatus("current")

ciscoEnergywiseActivationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 7)
)
ciscoEnergywiseActivationGroup.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewDomainName"),
        ("CISCO-ENERGYWISE-MIB", "cewDomainSecret"),
        ("CISCO-ENERGYWISE-MIB", "cewProtocol"),
        ("CISCO-ENERGYWISE-MIB", "cewAddressType"),
        ("CISCO-ENERGYWISE-MIB", "cewAddress"),
        ("CISCO-ENERGYWISE-MIB", "cewPort"),
        ("CISCO-ENERGYWISE-MIB", "cewEnable"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseActivationGroup.setStatus("current")

ciscoEnergywiseEntityGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 8)
)
ciscoEnergywiseEntityGroupSup1.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewEntConfiguredLevel"),
        ("CISCO-ENERGYWISE-MIB", "cewVersion"),
        ("CISCO-ENERGYWISE-MIB", "cewManagementSecret"),
        ("CISCO-ENERGYWISE-MIB", "cewEndPointSecret"),
        ("CISCO-ENERGYWISE-MIB", "cewDeviceTotalUsage"),
        ("CISCO-ENERGYWISE-MIB", "cewDeviceTotalUsageUnits"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseEntityGroupSup1.setStatus("current")

ciscoEnergywiseEventGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 9)
)
ciscoEnergywiseEventGroupSup1.setObjects(
    ("CISCO-ENERGYWISE-MIB", "cewEventImportance")
)
if mibBuilder.loadTexts:
    ciscoEnergywiseEventGroupSup1.setStatus("current")

ciscoEnergywiseEntityGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 11)
)
ciscoEnergywiseEntityGroupSup2.setObjects(
    ("CISCO-ENERGYWISE-MIB", "cewDeviceType")
)
if mibBuilder.loadTexts:
    ciscoEnergywiseEntityGroupSup2.setStatus("current")

ciscoEnergywiseNeighborGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 12)
)
ciscoEnergywiseNeighborGroupSup1.setObjects(
    ("CISCO-ENERGYWISE-MIB", "cewNeighborDeviceType")
)
if mibBuilder.loadTexts:
    ciscoEnergywiseNeighborGroupSup1.setStatus("current")

ciscoEnergywiseEntityGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 13)
)
ciscoEnergywiseEntityGroupSup3.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewEntEnergyUsageCategory"),
        ("CISCO-ENERGYWISE-MIB", "cewEntEnergyUsageDirection"),
        ("CISCO-ENERGYWISE-MIB", "cewEntAllowSet"),
        ("CISCO-ENERGYWISE-MIB", "cewEntActivityCheck"),
        ("CISCO-ENERGYWISE-MIB", "cewAllowSet"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseEntityGroupSup3.setStatus("current")

ciscoEnergywiseNeighborGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 14)
)
ciscoEnergywiseNeighborGroupSup2.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewNeighborKeyword"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborConfiguredKeyword"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborName"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborConfiguredName"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborRoleDescription"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborConfiguredRoleDesc"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborEnergyLevel"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborConfiguredLevel"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborImportance"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborConfiguredImportance"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborEnergyUnits"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborEnergyUsage"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborEnergyUsageCategory"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborEnergyUsageDirection"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborLevelMaxUsage"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborLevelDeltaUsage"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborLevelUnits"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseNeighborGroupSup2.setStatus("current")

ciscoEnergywiseNeighborGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 15)
)
ciscoEnergywiseNeighborGroupSup3.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewNeighborMacAddress"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborPhysicalEntityId"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborParentPortIndex"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseNeighborGroupSup3.setStatus("current")


# Notification objects

cewLevelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 0, 1)
)
cewLevelChange.setObjects(
    ("CISCO-ENERGYWISE-MIB", "cewEntEnergyLevel")
)
if mibBuilder.loadTexts:
    cewLevelChange.setStatus(
        "current"
    )

cewNeighborAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 0, 2)
)
cewNeighborAdded.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewNeighborId"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborType"))
)
if mibBuilder.loadTexts:
    cewNeighborAdded.setStatus(
        "current"
    )

cewNeighborDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 0, 3)
)
cewNeighborDeleted.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewNeighborId"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborType"))
)
if mibBuilder.loadTexts:
    cewNeighborDeleted.setStatus(
        "current"
    )

cewEventOccured = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 0, 4)
)
cewEventOccured.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewEventLevel"),
        ("CISCO-ENERGYWISE-MIB", "cewEventOccuredErrorCode"))
)
if mibBuilder.loadTexts:
    cewEventOccured.setStatus(
        "deprecated"
    )

cewEventOccuredRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 0, 5)
)
cewEventOccuredRev1.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewEventLevel"),
        ("CISCO-ENERGYWISE-MIB", "cewEventImportance"),
        ("CISCO-ENERGYWISE-MIB", "cewEventOccuredErrorCode"))
)
if mibBuilder.loadTexts:
    cewEventOccuredRev1.setStatus(
        "current"
    )


# Notifications groups

ciscoEnergywiseNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 5)
)
ciscoEnergywiseNotifGroup.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewLevelChange"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborAdded"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborDeleted"),
        ("CISCO-ENERGYWISE-MIB", "cewEventOccured"))
)
if mibBuilder.loadTexts:
    ciscoEnergywiseNotifGroup.setStatus(
        "deprecated"
    )

cewEnergywiseNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 2, 10)
)
cewEnergywiseNotifGroupRev1.setObjects(
      *(("CISCO-ENERGYWISE-MIB", "cewLevelChange"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborAdded"),
        ("CISCO-ENERGYWISE-MIB", "cewNeighborDeleted"),
        ("CISCO-ENERGYWISE-MIB", "cewEventOccuredRev1"))
)
if mibBuilder.loadTexts:
    cewEnergywiseNotifGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEnergywiseMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBFullCompliance.setStatus(
        "deprecated"
    )

ciscoEnergywiseMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBReadOnlyCompliance.setStatus(
        "deprecated"
    )

ciscoEnergywiseMIBFullComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBFullComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEnergywiseMIBReadOnlyComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBReadOnlyComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEnergywiseMIBFullComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBFullComplianceRev2.setStatus(
        "deprecated"
    )

ciscoEnergywiseMIBReadOnlyComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBReadOnlyComplianceRev2.setStatus(
        "deprecated"
    )

ciscoEnergywiseMIBFullComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBFullComplianceRev3.setStatus(
        "deprecated"
    )

ciscoEnergywiseMIBReadOnlyComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBReadOnlyComplianceRev3.setStatus(
        "deprecated"
    )

ciscoEnergywiseMIBFullComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBFullComplianceRev4.setStatus(
        "current"
    )

ciscoEnergywiseMIBReadOnlyComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 683, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ciscoEnergywiseMIBReadOnlyComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENERGYWISE-MIB",
    **{"EnergywiseLevel": EnergywiseLevel,
       "EnergywiseId": EnergywiseId,
       "EnergywisePowerUnits": EnergywisePowerUnits,
       "EnergywiseKeywordList": EnergywiseKeywordList,
       "ciscoEnergywiseMIB": ciscoEnergywiseMIB,
       "ciscoEnergywiseMIBNotifs": ciscoEnergywiseMIBNotifs,
       "cewLevelChange": cewLevelChange,
       "cewNeighborAdded": cewNeighborAdded,
       "cewNeighborDeleted": cewNeighborDeleted,
       "cewEventOccured": cewEventOccured,
       "cewEventOccuredRev1": cewEventOccuredRev1,
       "ciscoEnergywiseMIBObjects": ciscoEnergywiseMIBObjects,
       "cewDeviceId": cewDeviceId,
       "cewDeviceNeighborCount": cewDeviceNeighborCount,
       "cewDomainName": cewDomainName,
       "cewMaxImportance": cewMaxImportance,
       "cewMaxImportanceId": cewMaxImportanceId,
       "cewEntTable": cewEntTable,
       "cewEntEntry": cewEntEntry,
       "cewEntNannyVector": cewEntNannyVector,
       "cewEntNeighborIndex": cewEntNeighborIndex,
       "cewEntKeyword": cewEntKeyword,
       "cewEntName": cewEntName,
       "cewEntRoleDescription": cewEntRoleDescription,
       "cewEntFullName": cewEntFullName,
       "cewEntEnergyUnits": cewEntEnergyUnits,
       "cewEntEnergyUsage": cewEntEnergyUsage,
       "cewEntEnergyUsageCaliber": cewEntEnergyUsageCaliber,
       "cewEntEnergyLevel": cewEntEnergyLevel,
       "cewEntEnergyUsageProvisioned": cewEntEnergyUsageProvisioned,
       "cewEntImportanceInt": cewEntImportanceInt,
       "cewEntImportanceExt": cewEntImportanceExt,
       "cewEntImportanceRelative": cewEntImportanceRelative,
       "cewEntImportanceParentId": cewEntImportanceParentId,
       "cewEntParentId": cewEntParentId,
       "cewEntAdminStatus": cewEntAdminStatus,
       "cewEntOperStatus": cewEntOperStatus,
       "cewEntConfiguredLevel": cewEntConfiguredLevel,
       "cewEntEnergyUsageCategory": cewEntEnergyUsageCategory,
       "cewEntEnergyUsageDirection": cewEntEnergyUsageDirection,
       "cewEntAllowSet": cewEntAllowSet,
       "cewEntActivityCheck": cewEntActivityCheck,
       "cewLevelTable": cewLevelTable,
       "cewLevelEntry": cewLevelEntry,
       "cewLevelIndex": cewLevelIndex,
       "cewLevelMaxUsage": cewLevelMaxUsage,
       "cewLevelDeltaUsage": cewLevelDeltaUsage,
       "cewLevelUnits": cewLevelUnits,
       "cewProxyTable": cewProxyTable,
       "cewProxyEntry": cewProxyEntry,
       "cewProxyId": cewProxyId,
       "cewProxyAddressType": cewProxyAddressType,
       "cewProxyAddress": cewProxyAddress,
       "cewProxyPort": cewProxyPort,
       "cewProxyClass": cewProxyClass,
       "cewProxyStorage": cewProxyStorage,
       "cewProxyStatus": cewProxyStatus,
       "cewNeighborTable": cewNeighborTable,
       "cewNeighborEntry": cewNeighborEntry,
       "cewNeighborIndex": cewNeighborIndex,
       "cewNeighborId": cewNeighborId,
       "cewNeighborType": cewNeighborType,
       "cewNeighborHeartBeat": cewNeighborHeartBeat,
       "cewNeighborStorage": cewNeighborStorage,
       "cewNeighborStatus": cewNeighborStatus,
       "cewNeighborDeviceType": cewNeighborDeviceType,
       "cewNeighborKeyword": cewNeighborKeyword,
       "cewNeighborConfiguredKeyword": cewNeighborConfiguredKeyword,
       "cewNeighborName": cewNeighborName,
       "cewNeighborConfiguredName": cewNeighborConfiguredName,
       "cewNeighborRoleDescription": cewNeighborRoleDescription,
       "cewNeighborConfiguredRoleDesc": cewNeighborConfiguredRoleDesc,
       "cewNeighborEnergyLevel": cewNeighborEnergyLevel,
       "cewNeighborConfiguredLevel": cewNeighborConfiguredLevel,
       "cewNeighborImportance": cewNeighborImportance,
       "cewNeighborConfiguredImportance": cewNeighborConfiguredImportance,
       "cewNeighborEnergyUnits": cewNeighborEnergyUnits,
       "cewNeighborEnergyUsage": cewNeighborEnergyUsage,
       "cewNeighborEnergyUsageCategory": cewNeighborEnergyUsageCategory,
       "cewNeighborEnergyUsageDirection": cewNeighborEnergyUsageDirection,
       "cewNeighborMacAddress": cewNeighborMacAddress,
       "cewNeighborPhysicalEntityId": cewNeighborPhysicalEntityId,
       "cewNeighborParentPortIndex": cewNeighborParentPortIndex,
       "cewEventTable": cewEventTable,
       "cewEventEntry": cewEventEntry,
       "cewEventIndex": cewEventIndex,
       "cewEventLevel": cewEventLevel,
       "cewEventRecurrence": cewEventRecurrence,
       "cewEventTime": cewEventTime,
       "cewEventStorage": cewEventStorage,
       "cewEventStatus": cewEventStatus,
       "cewEventImportance": cewEventImportance,
       "cewLevelChangeNotifEnable": cewLevelChangeNotifEnable,
       "cewNeighborAddedNotifEnable": cewNeighborAddedNotifEnable,
       "cewNeighborDeletedNotifEnable": cewNeighborDeletedNotifEnable,
       "cewEventOccuredNotifEnable": cewEventOccuredNotifEnable,
       "cewEventOccuredErrorCode": cewEventOccuredErrorCode,
       "cewManagementSecret": cewManagementSecret,
       "cewEndPointSecret": cewEndPointSecret,
       "cewDomainSecret": cewDomainSecret,
       "cewProtocol": cewProtocol,
       "cewAddressType": cewAddressType,
       "cewAddress": cewAddress,
       "cewPort": cewPort,
       "cewEnable": cewEnable,
       "cewVersion": cewVersion,
       "cewDeviceTotalUsage": cewDeviceTotalUsage,
       "cewDeviceTotalUsageUnits": cewDeviceTotalUsageUnits,
       "cewDeviceType": cewDeviceType,
       "cewAllowSet": cewAllowSet,
       "cewNeighborLevelTable": cewNeighborLevelTable,
       "cewNeighborLevelEntry": cewNeighborLevelEntry,
       "cewNeighborLevelIndex": cewNeighborLevelIndex,
       "cewNeighborLevelMaxUsage": cewNeighborLevelMaxUsage,
       "cewNeighborLevelDeltaUsage": cewNeighborLevelDeltaUsage,
       "cewNeighborLevelUnits": cewNeighborLevelUnits,
       "ciscoEnergywiseMIBConform": ciscoEnergywiseMIBConform,
       "ciscoEnergywiseMIBCompliances": ciscoEnergywiseMIBCompliances,
       "ciscoEnergywiseMIBFullCompliance": ciscoEnergywiseMIBFullCompliance,
       "ciscoEnergywiseMIBReadOnlyCompliance": ciscoEnergywiseMIBReadOnlyCompliance,
       "ciscoEnergywiseMIBFullComplianceRev1": ciscoEnergywiseMIBFullComplianceRev1,
       "ciscoEnergywiseMIBReadOnlyComplianceRev1": ciscoEnergywiseMIBReadOnlyComplianceRev1,
       "ciscoEnergywiseMIBFullComplianceRev2": ciscoEnergywiseMIBFullComplianceRev2,
       "ciscoEnergywiseMIBReadOnlyComplianceRev2": ciscoEnergywiseMIBReadOnlyComplianceRev2,
       "ciscoEnergywiseMIBFullComplianceRev3": ciscoEnergywiseMIBFullComplianceRev3,
       "ciscoEnergywiseMIBReadOnlyComplianceRev3": ciscoEnergywiseMIBReadOnlyComplianceRev3,
       "ciscoEnergywiseMIBFullComplianceRev4": ciscoEnergywiseMIBFullComplianceRev4,
       "ciscoEnergywiseMIBReadOnlyComplianceRev4": ciscoEnergywiseMIBReadOnlyComplianceRev4,
       "ciscoEnergywiseMIBGroups": ciscoEnergywiseMIBGroups,
       "ciscoEnergywiseEntityGroup": ciscoEnergywiseEntityGroup,
       "ciscoEnergywiseNeighborGroup": ciscoEnergywiseNeighborGroup,
       "ciscoEnergywiseEventGroup": ciscoEnergywiseEventGroup,
       "ciscoEnergywiseProxyGroup": ciscoEnergywiseProxyGroup,
       "ciscoEnergywiseNotifGroup": ciscoEnergywiseNotifGroup,
       "ciscoEnergywiseNotifEnableGroup": ciscoEnergywiseNotifEnableGroup,
       "ciscoEnergywiseActivationGroup": ciscoEnergywiseActivationGroup,
       "ciscoEnergywiseEntityGroupSup1": ciscoEnergywiseEntityGroupSup1,
       "ciscoEnergywiseEventGroupSup1": ciscoEnergywiseEventGroupSup1,
       "cewEnergywiseNotifGroupRev1": cewEnergywiseNotifGroupRev1,
       "ciscoEnergywiseEntityGroupSup2": ciscoEnergywiseEntityGroupSup2,
       "ciscoEnergywiseNeighborGroupSup1": ciscoEnergywiseNeighborGroupSup1,
       "ciscoEnergywiseEntityGroupSup3": ciscoEnergywiseEntityGroupSup3,
       "ciscoEnergywiseNeighborGroupSup2": ciscoEnergywiseNeighborGroupSup2,
       "ciscoEnergywiseNeighborGroupSup3": ciscoEnergywiseNeighborGroupSup3}
)
