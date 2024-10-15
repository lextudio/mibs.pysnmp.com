# SNMP MIB module (CISCO-ERM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ERM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:51 2024
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

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoErmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510)
)
ciscoErmMIB.setRevisions(
        ("2006-02-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CermSubEntityId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CermUserTypeId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CermUserTypeIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CermUserId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CermUserIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CermGroupId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CermOwnerId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CermOwnerIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CermMonitorId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CermUserOrGroup(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 1),
          ("user", 2))
    )



class CermResUsagePct(Unsigned32, TextualConvention):
    status = "current"


class CermThreshold(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CermThresholdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CermDampenInterval(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2592000),
    )



class CermThresholdSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("major", 2),
          ("minor", 1))
    )



class CermNotificationSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("none", 1))
    )



class CermNotificationDirection(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_CiscoErmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoErmMIBNotifs = _CiscoErmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 0)
)
_CiscoErmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoErmMIBObjects = _CiscoErmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1)
)
_CermScalars_ObjectIdentity = ObjectIdentity
cermScalars = _CermScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1)
)


class _CermScalarsGlobalPolicyName_Type(SnmpAdminString):
    """Custom type cermScalarsGlobalPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CermScalarsGlobalPolicyName_Type.__name__ = "SnmpAdminString"
_CermScalarsGlobalPolicyName_Object = MibScalar
cermScalarsGlobalPolicyName = _CermScalarsGlobalPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1),
    _CermScalarsGlobalPolicyName_Type()
)
cermScalarsGlobalPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cermScalarsGlobalPolicyName.setStatus("current")
_CermStats_ObjectIdentity = ObjectIdentity
cermStats = _CermStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2)
)
_CermResOwnerTable_Object = MibTable
cermResOwnerTable = _CermResOwnerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cermResOwnerTable.setStatus("current")
_CermResOwnerEntry_Object = MibTableRow
cermResOwnerEntry = _CermResOwnerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1, 1)
)
cermResOwnerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerId"),
)
if mibBuilder.loadTexts:
    cermResOwnerEntry.setStatus("current")
_CermResOwnerSubEntityId_Type = CermSubEntityId
_CermResOwnerSubEntityId_Object = MibTableColumn
cermResOwnerSubEntityId = _CermResOwnerSubEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1, 1, 1),
    _CermResOwnerSubEntityId_Type()
)
cermResOwnerSubEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResOwnerSubEntityId.setStatus("current")
_CermResOwnerId_Type = CermOwnerId
_CermResOwnerId_Object = MibTableColumn
cermResOwnerId = _CermResOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1, 1, 2),
    _CermResOwnerId_Type()
)
cermResOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResOwnerId.setStatus("current")


class _CermResOwnerName_Type(SnmpAdminString):
    """Custom type cermResOwnerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermResOwnerName_Type.__name__ = "SnmpAdminString"
_CermResOwnerName_Object = MibTableColumn
cermResOwnerName = _CermResOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1, 1, 3),
    _CermResOwnerName_Type()
)
cermResOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerName.setStatus("current")


class _CermResOwnerMeasurementUnit_Type(SnmpAdminString):
    """Custom type cermResOwnerMeasurementUnit based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermResOwnerMeasurementUnit_Type.__name__ = "SnmpAdminString"
_CermResOwnerMeasurementUnit_Object = MibTableColumn
cermResOwnerMeasurementUnit = _CermResOwnerMeasurementUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1, 1, 4),
    _CermResOwnerMeasurementUnit_Type()
)
cermResOwnerMeasurementUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerMeasurementUnit.setStatus("current")
_CermResOwnerThreshIsConfigurable_Type = TruthValue
_CermResOwnerThreshIsConfigurable_Object = MibTableColumn
cermResOwnerThreshIsConfigurable = _CermResOwnerThreshIsConfigurable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1, 1, 5),
    _CermResOwnerThreshIsConfigurable_Type()
)
cermResOwnerThreshIsConfigurable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerThreshIsConfigurable.setStatus("current")
_CermResOwnerResUserCount_Type = Unsigned32
_CermResOwnerResUserCount_Object = MibTableColumn
cermResOwnerResUserCount = _CermResOwnerResUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1, 1, 6),
    _CermResOwnerResUserCount_Type()
)
cermResOwnerResUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerResUserCount.setStatus("current")
_CermResOwnerResGroupCount_Type = Unsigned32
_CermResOwnerResGroupCount_Object = MibTableColumn
cermResOwnerResGroupCount = _CermResOwnerResGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 1, 1, 7),
    _CermResOwnerResGroupCount_Type()
)
cermResOwnerResGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerResGroupCount.setStatus("current")
_CermResOwnerSubTypeTable_Object = MibTable
cermResOwnerSubTypeTable = _CermResOwnerSubTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cermResOwnerSubTypeTable.setStatus("current")
_CermResOwnerSubTypeEntry_Object = MibTableRow
cermResOwnerSubTypeEntry = _CermResOwnerSubTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 2, 1)
)
cermResOwnerSubTypeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubTypeId"),
)
if mibBuilder.loadTexts:
    cermResOwnerSubTypeEntry.setStatus("current")
_CermResOwnerSubTypeId_Type = Unsigned32
_CermResOwnerSubTypeId_Object = MibTableColumn
cermResOwnerSubTypeId = _CermResOwnerSubTypeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 2, 1, 1),
    _CermResOwnerSubTypeId_Type()
)
cermResOwnerSubTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeId.setStatus("current")


class _CermResOwnerSubTypeName_Type(SnmpAdminString):
    """Custom type cermResOwnerSubTypeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CermResOwnerSubTypeName_Type.__name__ = "SnmpAdminString"
_CermResOwnerSubTypeName_Object = MibTableColumn
cermResOwnerSubTypeName = _CermResOwnerSubTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 2, 1, 2),
    _CermResOwnerSubTypeName_Type()
)
cermResOwnerSubTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeName.setStatus("current")
_CermResOwnerSubTypeUsagePct_Type = CermResUsagePct
_CermResOwnerSubTypeUsagePct_Object = MibTableColumn
cermResOwnerSubTypeUsagePct = _CermResOwnerSubTypeUsagePct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 2, 1, 3),
    _CermResOwnerSubTypeUsagePct_Type()
)
cermResOwnerSubTypeUsagePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeUsagePct.setStatus("current")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeUsagePct.setUnits("percentage")
_CermResOwnerSubTypeUsage_Type = Unsigned32
_CermResOwnerSubTypeUsage_Object = MibTableColumn
cermResOwnerSubTypeUsage = _CermResOwnerSubTypeUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 2, 1, 4),
    _CermResOwnerSubTypeUsage_Type()
)
cermResOwnerSubTypeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeUsage.setStatus("current")
_CermResOwnerSubTypeMaxUsage_Type = Unsigned32
_CermResOwnerSubTypeMaxUsage_Object = MibTableColumn
cermResOwnerSubTypeMaxUsage = _CermResOwnerSubTypeMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 2, 1, 5),
    _CermResOwnerSubTypeMaxUsage_Type()
)
cermResOwnerSubTypeMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeMaxUsage.setStatus("current")
_CermResOwnerSubTypeGlobNotifSeverity_Type = CermNotificationSeverity
_CermResOwnerSubTypeGlobNotifSeverity_Object = MibTableColumn
cermResOwnerSubTypeGlobNotifSeverity = _CermResOwnerSubTypeGlobNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 2, 1, 6),
    _CermResOwnerSubTypeGlobNotifSeverity_Type()
)
cermResOwnerSubTypeGlobNotifSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeGlobNotifSeverity.setStatus("current")
_CermResOwnerSubTypeThresholdTable_Object = MibTable
cermResOwnerSubTypeThresholdTable = _CermResOwnerSubTypeThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cermResOwnerSubTypeThresholdTable.setStatus("current")
_CermResOwnerSubTypeThresholdEntry_Object = MibTableRow
cermResOwnerSubTypeThresholdEntry = _CermResOwnerSubTypeThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 3, 1)
)
cermResOwnerSubTypeThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubTypeId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubTypeThreshSeverity"),
)
if mibBuilder.loadTexts:
    cermResOwnerSubTypeThresholdEntry.setStatus("current")
_CermResOwnerSubTypeThreshSeverity_Type = CermThresholdSeverity
_CermResOwnerSubTypeThreshSeverity_Object = MibTableColumn
cermResOwnerSubTypeThreshSeverity = _CermResOwnerSubTypeThreshSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 3, 1, 1),
    _CermResOwnerSubTypeThreshSeverity_Type()
)
cermResOwnerSubTypeThreshSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeThreshSeverity.setStatus("current")
_CermResOwnerSubTypeRisingThresh_Type = CermThreshold
_CermResOwnerSubTypeRisingThresh_Object = MibTableColumn
cermResOwnerSubTypeRisingThresh = _CermResOwnerSubTypeRisingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 3, 1, 2),
    _CermResOwnerSubTypeRisingThresh_Type()
)
cermResOwnerSubTypeRisingThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeRisingThresh.setStatus("current")
_CermResOwnerSubTypeRisingInterval_Type = CermDampenInterval
_CermResOwnerSubTypeRisingInterval_Object = MibTableColumn
cermResOwnerSubTypeRisingInterval = _CermResOwnerSubTypeRisingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 3, 1, 3),
    _CermResOwnerSubTypeRisingInterval_Type()
)
cermResOwnerSubTypeRisingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeRisingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeRisingInterval.setUnits("seconds")
_CermResOwnerSubTypeFallingThresh_Type = CermThreshold
_CermResOwnerSubTypeFallingThresh_Object = MibTableColumn
cermResOwnerSubTypeFallingThresh = _CermResOwnerSubTypeFallingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 3, 1, 4),
    _CermResOwnerSubTypeFallingThresh_Type()
)
cermResOwnerSubTypeFallingThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeFallingThresh.setStatus("current")
_CermResOwnerSubTypeFallingInterval_Type = CermDampenInterval
_CermResOwnerSubTypeFallingInterval_Object = MibTableColumn
cermResOwnerSubTypeFallingInterval = _CermResOwnerSubTypeFallingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 3, 1, 5),
    _CermResOwnerSubTypeFallingInterval_Type()
)
cermResOwnerSubTypeFallingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeFallingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cermResOwnerSubTypeFallingInterval.setUnits("seconds")
_CermResUserTypeTable_Object = MibTable
cermResUserTypeTable = _CermResUserTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cermResUserTypeTable.setStatus("current")
_CermResUserTypeEntry_Object = MibTableRow
cermResUserTypeEntry = _CermResUserTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 4, 1)
)
cermResUserTypeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeId"),
)
if mibBuilder.loadTexts:
    cermResUserTypeEntry.setStatus("current")
_CermResUserTypeSubEntityId_Type = CermSubEntityId
_CermResUserTypeSubEntityId_Object = MibTableColumn
cermResUserTypeSubEntityId = _CermResUserTypeSubEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 4, 1, 1),
    _CermResUserTypeSubEntityId_Type()
)
cermResUserTypeSubEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResUserTypeSubEntityId.setStatus("current")
_CermResUserTypeId_Type = CermUserTypeId
_CermResUserTypeId_Object = MibTableColumn
cermResUserTypeId = _CermResUserTypeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 4, 1, 2),
    _CermResUserTypeId_Type()
)
cermResUserTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResUserTypeId.setStatus("current")


class _CermResUserTypeName_Type(SnmpAdminString):
    """Custom type cermResUserTypeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermResUserTypeName_Type.__name__ = "SnmpAdminString"
_CermResUserTypeName_Object = MibTableColumn
cermResUserTypeName = _CermResUserTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 4, 1, 3),
    _CermResUserTypeName_Type()
)
cermResUserTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserTypeName.setStatus("current")
_CermResUserTypeResOwnerCount_Type = Unsigned32
_CermResUserTypeResOwnerCount_Object = MibTableColumn
cermResUserTypeResOwnerCount = _CermResUserTypeResOwnerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 4, 1, 4),
    _CermResUserTypeResOwnerCount_Type()
)
cermResUserTypeResOwnerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserTypeResOwnerCount.setStatus("current")
_CermResUserTypeResUserCount_Type = Unsigned32
_CermResUserTypeResUserCount_Object = MibTableColumn
cermResUserTypeResUserCount = _CermResUserTypeResUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 4, 1, 5),
    _CermResUserTypeResUserCount_Type()
)
cermResUserTypeResUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserTypeResUserCount.setStatus("current")
_CermResUserTypeResGroupCount_Type = Unsigned32
_CermResUserTypeResGroupCount_Object = MibTableColumn
cermResUserTypeResGroupCount = _CermResUserTypeResGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 4, 1, 6),
    _CermResUserTypeResGroupCount_Type()
)
cermResUserTypeResGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserTypeResGroupCount.setStatus("current")
_CermResUserTable_Object = MibTable
cermResUserTable = _CermResUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cermResUserTable.setStatus("current")
_CermResUserEntry_Object = MibTableRow
cermResUserEntry = _CermResUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 5, 1)
)
cermResUserEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeId"),
    (0, "CISCO-ERM-MIB", "cermResUserId"),
)
if mibBuilder.loadTexts:
    cermResUserEntry.setStatus("current")
_CermResUserId_Type = CermUserId
_CermResUserId_Object = MibTableColumn
cermResUserId = _CermResUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 5, 1, 1),
    _CermResUserId_Type()
)
cermResUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResUserId.setStatus("current")


class _CermResUserName_Type(SnmpAdminString):
    """Custom type cermResUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermResUserName_Type.__name__ = "SnmpAdminString"
_CermResUserName_Object = MibTableColumn
cermResUserName = _CermResUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 5, 1, 2),
    _CermResUserName_Type()
)
cermResUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserName.setStatus("current")
_CermResUserPriority_Type = Unsigned32
_CermResUserPriority_Object = MibTableColumn
cermResUserPriority = _CermResUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 5, 1, 3),
    _CermResUserPriority_Type()
)
cermResUserPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserPriority.setStatus("current")
_CermResUserResGroupId_Type = CermGroupId
_CermResUserResGroupId_Object = MibTableColumn
cermResUserResGroupId = _CermResUserResGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 5, 1, 4),
    _CermResUserResGroupId_Type()
)
cermResUserResGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserResGroupId.setStatus("current")
_CermResGroupTable_Object = MibTable
cermResGroupTable = _CermResGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cermResGroupTable.setStatus("current")
_CermResGroupEntry_Object = MibTableRow
cermResGroupEntry = _CermResGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 6, 1)
)
cermResGroupEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeId"),
    (0, "CISCO-ERM-MIB", "cermResGroupId"),
)
if mibBuilder.loadTexts:
    cermResGroupEntry.setStatus("current")
_CermResGroupId_Type = CermGroupId
_CermResGroupId_Object = MibTableColumn
cermResGroupId = _CermResGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 6, 1, 1),
    _CermResGroupId_Type()
)
cermResGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResGroupId.setStatus("current")


class _CermResGroupName_Type(SnmpAdminString):
    """Custom type cermResGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermResGroupName_Type.__name__ = "SnmpAdminString"
_CermResGroupName_Object = MibTableColumn
cermResGroupName = _CermResGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 6, 1, 2),
    _CermResGroupName_Type()
)
cermResGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResGroupName.setStatus("current")
_CermResGroupUserInstanceCount_Type = Unsigned32
_CermResGroupUserInstanceCount_Object = MibTableColumn
cermResGroupUserInstanceCount = _CermResGroupUserInstanceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 6, 1, 3),
    _CermResGroupUserInstanceCount_Type()
)
cermResGroupUserInstanceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResGroupUserInstanceCount.setStatus("current")
_CermResGroupResUserTable_Object = MibTable
cermResGroupResUserTable = _CermResGroupResUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cermResGroupResUserTable.setStatus("current")
_CermResGroupResUserEntry_Object = MibTableRow
cermResGroupResUserEntry = _CermResGroupResUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 7, 1)
)
cermResGroupResUserEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeId"),
    (0, "CISCO-ERM-MIB", "cermResGroupId"),
    (0, "CISCO-ERM-MIB", "cermResGroupResUserId"),
)
if mibBuilder.loadTexts:
    cermResGroupResUserEntry.setStatus("current")
_CermResGroupResUserId_Type = CermUserId
_CermResGroupResUserId_Object = MibTableColumn
cermResGroupResUserId = _CermResGroupResUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 7, 1, 1),
    _CermResGroupResUserId_Type()
)
cermResGroupResUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResGroupResUserId.setStatus("current")
_CermResOwnerResUserOrGroupTable_Object = MibTable
cermResOwnerResUserOrGroupTable = _CermResOwnerResUserOrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cermResOwnerResUserOrGroupTable.setStatus("current")
_CermResOwnerResUserOrGroupEntry_Object = MibTableRow
cermResOwnerResUserOrGroupEntry = _CermResOwnerResUserOrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1)
)
cermResOwnerResUserOrGroupEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubTypeId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerResUserTypeId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerResUserOrGroupId"),
)
if mibBuilder.loadTexts:
    cermResOwnerResUserOrGroupEntry.setStatus("current")
_CermResOwnerResUserTypeId_Type = CermUserTypeId
_CermResOwnerResUserTypeId_Object = MibTableColumn
cermResOwnerResUserTypeId = _CermResOwnerResUserTypeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1, 1),
    _CermResOwnerResUserTypeId_Type()
)
cermResOwnerResUserTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResOwnerResUserTypeId.setStatus("current")
_CermResOwnerResUserOrGroupId_Type = CermUserId
_CermResOwnerResUserOrGroupId_Object = MibTableColumn
cermResOwnerResUserOrGroupId = _CermResOwnerResUserOrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1, 2),
    _CermResOwnerResUserOrGroupId_Type()
)
cermResOwnerResUserOrGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResOwnerResUserOrGroupId.setStatus("current")
_CermResUserOrGroupFlag_Type = CermUserOrGroup
_CermResUserOrGroupFlag_Object = MibTableColumn
cermResUserOrGroupFlag = _CermResUserOrGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1, 3),
    _CermResUserOrGroupFlag_Type()
)
cermResUserOrGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupFlag.setStatus("current")
_CermResUserOrGroupUsagePct_Type = CermResUsagePct
_CermResUserOrGroupUsagePct_Object = MibTableColumn
cermResUserOrGroupUsagePct = _CermResUserOrGroupUsagePct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1, 4),
    _CermResUserOrGroupUsagePct_Type()
)
cermResUserOrGroupUsagePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupUsagePct.setStatus("current")
if mibBuilder.loadTexts:
    cermResUserOrGroupUsagePct.setUnits("percentage")
_CermResUserOrGroupUsage_Type = Unsigned32
_CermResUserOrGroupUsage_Object = MibTableColumn
cermResUserOrGroupUsage = _CermResUserOrGroupUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1, 5),
    _CermResUserOrGroupUsage_Type()
)
cermResUserOrGroupUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupUsage.setStatus("current")
_CermResUserOrGroupMaxUsage_Type = Unsigned32
_CermResUserOrGroupMaxUsage_Object = MibTableColumn
cermResUserOrGroupMaxUsage = _CermResUserOrGroupMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1, 6),
    _CermResUserOrGroupMaxUsage_Type()
)
cermResUserOrGroupMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupMaxUsage.setStatus("current")
_CermResUserOrGroupNotifSeverity_Type = CermNotificationSeverity
_CermResUserOrGroupNotifSeverity_Object = MibTableColumn
cermResUserOrGroupNotifSeverity = _CermResUserOrGroupNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1, 7),
    _CermResUserOrGroupNotifSeverity_Type()
)
cermResUserOrGroupNotifSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupNotifSeverity.setStatus("current")
_CermResUserOrGroupGlobNotifSeverity_Type = CermNotificationSeverity
_CermResUserOrGroupGlobNotifSeverity_Object = MibTableColumn
cermResUserOrGroupGlobNotifSeverity = _CermResUserOrGroupGlobNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 8, 1, 8),
    _CermResUserOrGroupGlobNotifSeverity_Type()
)
cermResUserOrGroupGlobNotifSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupGlobNotifSeverity.setStatus("current")
_CermResOwnerResUserOrGroupThresholdTable_Object = MibTable
cermResOwnerResUserOrGroupThresholdTable = _CermResOwnerResUserOrGroupThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cermResOwnerResUserOrGroupThresholdTable.setStatus("current")
_CermResOwnerResUserOrGroupThresholdEntry_Object = MibTableRow
cermResOwnerResUserOrGroupThresholdEntry = _CermResOwnerResUserOrGroupThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9, 1)
)
cermResOwnerResUserOrGroupThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerSubTypeId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerResUserTypeId"),
    (0, "CISCO-ERM-MIB", "cermResOwnerResUserOrGroupId"),
    (0, "CISCO-ERM-MIB", "cermResUserOrGroupThreshIsUserGlob"),
    (0, "CISCO-ERM-MIB", "cermResUserOrGroupThreshSeverity"),
)
if mibBuilder.loadTexts:
    cermResOwnerResUserOrGroupThresholdEntry.setStatus("current")
_CermResUserOrGroupThreshIsUserGlob_Type = TruthValue
_CermResUserOrGroupThreshIsUserGlob_Object = MibTableColumn
cermResUserOrGroupThreshIsUserGlob = _CermResUserOrGroupThreshIsUserGlob_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9, 1, 1),
    _CermResUserOrGroupThreshIsUserGlob_Type()
)
cermResUserOrGroupThreshIsUserGlob.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResUserOrGroupThreshIsUserGlob.setStatus("current")
_CermResUserOrGroupThreshSeverity_Type = CermThresholdSeverity
_CermResUserOrGroupThreshSeverity_Object = MibTableColumn
cermResUserOrGroupThreshSeverity = _CermResUserOrGroupThreshSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9, 1, 2),
    _CermResUserOrGroupThreshSeverity_Type()
)
cermResUserOrGroupThreshSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResUserOrGroupThreshSeverity.setStatus("current")
_CermResUserOrGroupThreshFlag_Type = CermUserOrGroup
_CermResUserOrGroupThreshFlag_Object = MibTableColumn
cermResUserOrGroupThreshFlag = _CermResUserOrGroupThreshFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9, 1, 3),
    _CermResUserOrGroupThreshFlag_Type()
)
cermResUserOrGroupThreshFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupThreshFlag.setStatus("current")
_CermResUserOrGroupRisingThresh_Type = CermThreshold
_CermResUserOrGroupRisingThresh_Object = MibTableColumn
cermResUserOrGroupRisingThresh = _CermResUserOrGroupRisingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9, 1, 4),
    _CermResUserOrGroupRisingThresh_Type()
)
cermResUserOrGroupRisingThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupRisingThresh.setStatus("current")
_CermResUserOrGroupRisingInterval_Type = CermDampenInterval
_CermResUserOrGroupRisingInterval_Object = MibTableColumn
cermResUserOrGroupRisingInterval = _CermResUserOrGroupRisingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9, 1, 5),
    _CermResUserOrGroupRisingInterval_Type()
)
cermResUserOrGroupRisingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupRisingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cermResUserOrGroupRisingInterval.setUnits("seconds")
_CermResUserOrGroupFallingThresh_Type = CermThreshold
_CermResUserOrGroupFallingThresh_Object = MibTableColumn
cermResUserOrGroupFallingThresh = _CermResUserOrGroupFallingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9, 1, 6),
    _CermResUserOrGroupFallingThresh_Type()
)
cermResUserOrGroupFallingThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupFallingThresh.setStatus("current")
_CermResUserOrGroupFallingInterval_Type = CermDampenInterval
_CermResUserOrGroupFallingInterval_Object = MibTableColumn
cermResUserOrGroupFallingInterval = _CermResUserOrGroupFallingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 9, 1, 7),
    _CermResUserOrGroupFallingInterval_Type()
)
cermResUserOrGroupFallingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserOrGroupFallingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cermResUserOrGroupFallingInterval.setUnits("seconds")
_CermResUserTypeResOwnerTable_Object = MibTable
cermResUserTypeResOwnerTable = _CermResUserTypeResOwnerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cermResUserTypeResOwnerTable.setStatus("current")
_CermResUserTypeResOwnerEntry_Object = MibTableRow
cermResUserTypeResOwnerEntry = _CermResUserTypeResOwnerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 10, 1)
)
cermResUserTypeResOwnerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeId"),
    (0, "CISCO-ERM-MIB", "cermResUserTypeResOwnerId"),
)
if mibBuilder.loadTexts:
    cermResUserTypeResOwnerEntry.setStatus("current")
_CermResUserTypeResOwnerId_Type = CermOwnerId
_CermResUserTypeResOwnerId_Object = MibTableColumn
cermResUserTypeResOwnerId = _CermResUserTypeResOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 10, 1, 1),
    _CermResUserTypeResOwnerId_Type()
)
cermResUserTypeResOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResUserTypeResOwnerId.setStatus("current")
_CermResMonitorTable_Object = MibTable
cermResMonitorTable = _CermResMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cermResMonitorTable.setStatus("current")
_CermResMonitorEntry_Object = MibTableRow
cermResMonitorEntry = _CermResMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 11, 1)
)
cermResMonitorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResMonitorSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResMonitorId"),
)
if mibBuilder.loadTexts:
    cermResMonitorEntry.setStatus("current")
_CermResMonitorSubEntityId_Type = CermSubEntityId
_CermResMonitorSubEntityId_Object = MibTableColumn
cermResMonitorSubEntityId = _CermResMonitorSubEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 11, 1, 1),
    _CermResMonitorSubEntityId_Type()
)
cermResMonitorSubEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResMonitorSubEntityId.setStatus("current")
_CermResMonitorId_Type = CermMonitorId
_CermResMonitorId_Object = MibTableColumn
cermResMonitorId = _CermResMonitorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 11, 1, 2),
    _CermResMonitorId_Type()
)
cermResMonitorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResMonitorId.setStatus("current")


class _CermResMonitorName_Type(SnmpAdminString):
    """Custom type cermResMonitorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermResMonitorName_Type.__name__ = "SnmpAdminString"
_CermResMonitorName_Object = MibTableColumn
cermResMonitorName = _CermResMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 11, 1, 3),
    _CermResMonitorName_Type()
)
cermResMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResMonitorName.setStatus("current")
_CermResMonitorResOwnerResUserTable_Object = MibTable
cermResMonitorResOwnerResUserTable = _CermResMonitorResOwnerResUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cermResMonitorResOwnerResUserTable.setStatus("current")
_CermResMonitorResOwnerResUserEntry_Object = MibTableRow
cermResMonitorResOwnerResUserEntry = _CermResMonitorResOwnerResUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 12, 1)
)
cermResMonitorResOwnerResUserEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResMonitorSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResMonitorId"),
    (0, "CISCO-ERM-MIB", "cermResMonitorResOwnerId"),
    (0, "CISCO-ERM-MIB", "cermResMonitorResUserTypeId"),
    (0, "CISCO-ERM-MIB", "cermResMonitorResUserId"),
)
if mibBuilder.loadTexts:
    cermResMonitorResOwnerResUserEntry.setStatus("current")
_CermResMonitorResOwnerId_Type = CermOwnerIdOrZero
_CermResMonitorResOwnerId_Object = MibTableColumn
cermResMonitorResOwnerId = _CermResMonitorResOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 12, 1, 1),
    _CermResMonitorResOwnerId_Type()
)
cermResMonitorResOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResMonitorResOwnerId.setStatus("current")
_CermResMonitorResUserTypeId_Type = CermUserTypeIdOrZero
_CermResMonitorResUserTypeId_Object = MibTableColumn
cermResMonitorResUserTypeId = _CermResMonitorResUserTypeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 12, 1, 2),
    _CermResMonitorResUserTypeId_Type()
)
cermResMonitorResUserTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResMonitorResUserTypeId.setStatus("current")
_CermResMonitorResUserId_Type = CermUserIdOrZero
_CermResMonitorResUserId_Object = MibTableColumn
cermResMonitorResUserId = _CermResMonitorResUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 12, 1, 3),
    _CermResMonitorResUserId_Type()
)
cermResMonitorResUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermResMonitorResUserId.setStatus("current")


class _CermResMonitorResPolicyName_Type(SnmpAdminString):
    """Custom type cermResMonitorResPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CermResMonitorResPolicyName_Type.__name__ = "SnmpAdminString"
_CermResMonitorResPolicyName_Object = MibTableColumn
cermResMonitorResPolicyName = _CermResMonitorResPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 12, 1, 4),
    _CermResMonitorResPolicyName_Type()
)
cermResMonitorResPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResMonitorResPolicyName.setStatus("current")
_CermResMonitorPolicyTable_Object = MibTable
cermResMonitorPolicyTable = _CermResMonitorPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cermResMonitorPolicyTable.setStatus("current")
_CermResMonitorPolicyEntry_Object = MibTableRow
cermResMonitorPolicyEntry = _CermResMonitorPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 13, 1)
)
cermResMonitorPolicyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermResMonitorSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermResMonitorId"),
    (0, "CISCO-ERM-MIB", "cermResMonitorPolicyName"),
)
if mibBuilder.loadTexts:
    cermResMonitorPolicyEntry.setStatus("current")


class _CermResMonitorPolicyName_Type(SnmpAdminString):
    """Custom type cermResMonitorPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermResMonitorPolicyName_Type.__name__ = "SnmpAdminString"
_CermResMonitorPolicyName_Object = MibTableColumn
cermResMonitorPolicyName = _CermResMonitorPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 2, 13, 1, 1),
    _CermResMonitorPolicyName_Type()
)
cermResMonitorPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermResMonitorPolicyName.setStatus("current")
_CermConfig_ObjectIdentity = ObjectIdentity
cermConfig = _CermConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3)
)
_CermConfigPolicyTable_Object = MibTable
cermConfigPolicyTable = _CermConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cermConfigPolicyTable.setStatus("current")
_CermConfigPolicyEntry_Object = MibTableRow
cermConfigPolicyEntry = _CermConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1, 1)
)
cermConfigPolicyEntry.setIndexNames(
    (0, "CISCO-ERM-MIB", "cermPolicyName"),
)
if mibBuilder.loadTexts:
    cermConfigPolicyEntry.setStatus("current")


class _CermPolicyName_Type(SnmpAdminString):
    """Custom type cermPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermPolicyName_Type.__name__ = "SnmpAdminString"
_CermPolicyName_Object = MibTableColumn
cermPolicyName = _CermPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1, 1, 1),
    _CermPolicyName_Type()
)
cermPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyName.setStatus("current")


class _CermPolicyIsGlobal_Type(TruthValue):
    """Custom type cermPolicyIsGlobal based on TruthValue"""


_CermPolicyIsGlobal_Object = MibTableColumn
cermPolicyIsGlobal = _CermPolicyIsGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1, 1, 2),
    _CermPolicyIsGlobal_Type()
)
cermPolicyIsGlobal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyIsGlobal.setStatus("current")


class _CermPolicyUserTypeName_Type(SnmpAdminString):
    """Custom type cermPolicyUserTypeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CermPolicyUserTypeName_Type.__name__ = "SnmpAdminString"
_CermPolicyUserTypeName_Object = MibTableColumn
cermPolicyUserTypeName = _CermPolicyUserTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1, 1, 3),
    _CermPolicyUserTypeName_Type()
)
cermPolicyUserTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyUserTypeName.setStatus("current")


class _CermPolicyLoggingEnabled_Type(TruthValue):
    """Custom type cermPolicyLoggingEnabled based on TruthValue"""


_CermPolicyLoggingEnabled_Object = MibTableColumn
cermPolicyLoggingEnabled = _CermPolicyLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1, 1, 4),
    _CermPolicyLoggingEnabled_Type()
)
cermPolicyLoggingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyLoggingEnabled.setStatus("current")


class _CermPolicySnmpNotifEnabled_Type(TruthValue):
    """Custom type cermPolicySnmpNotifEnabled based on TruthValue"""


_CermPolicySnmpNotifEnabled_Object = MibTableColumn
cermPolicySnmpNotifEnabled = _CermPolicySnmpNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1, 1, 5),
    _CermPolicySnmpNotifEnabled_Type()
)
cermPolicySnmpNotifEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicySnmpNotifEnabled.setStatus("current")


class _CermPolicyStorageType_Type(StorageType):
    """Custom type cermPolicyStorageType based on StorageType"""


_CermPolicyStorageType_Object = MibTableColumn
cermPolicyStorageType = _CermPolicyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1, 1, 6),
    _CermPolicyStorageType_Type()
)
cermPolicyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyStorageType.setStatus("current")
_CermPolicyRowStatus_Type = RowStatus
_CermPolicyRowStatus_Object = MibTableColumn
cermPolicyRowStatus = _CermPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 1, 1, 7),
    _CermPolicyRowStatus_Type()
)
cermPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyRowStatus.setStatus("current")
_CermConfigPolicyResOwnerThreshTable_Object = MibTable
cermConfigPolicyResOwnerThreshTable = _CermConfigPolicyResOwnerThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cermConfigPolicyResOwnerThreshTable.setStatus("current")
_CermConfigPolicyResOwnerThreshEntry_Object = MibTableRow
cermConfigPolicyResOwnerThreshEntry = _CermConfigPolicyResOwnerThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1)
)
cermConfigPolicyResOwnerThreshEntry.setIndexNames(
    (0, "CISCO-ERM-MIB", "cermPolicyName"),
    (0, "CISCO-ERM-MIB", "cermPolicyPhysicalIndex"),
    (0, "CISCO-ERM-MIB", "cermPolicyResOwnerSubEntityId"),
    (0, "CISCO-ERM-MIB", "cermPolicyResOwnerId"),
    (0, "CISCO-ERM-MIB", "cermPolicyResOwnerSubTypeId"),
    (0, "CISCO-ERM-MIB", "cermPolicyIsUserGlobal"),
    (0, "CISCO-ERM-MIB", "cermPolicyThresholdSeverity"),
)
if mibBuilder.loadTexts:
    cermConfigPolicyResOwnerThreshEntry.setStatus("current")
_CermPolicyPhysicalIndex_Type = PhysicalIndex
_CermPolicyPhysicalIndex_Object = MibTableColumn
cermPolicyPhysicalIndex = _CermPolicyPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 1),
    _CermPolicyPhysicalIndex_Type()
)
cermPolicyPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyPhysicalIndex.setStatus("current")
_CermPolicyResOwnerSubEntityId_Type = CermSubEntityId
_CermPolicyResOwnerSubEntityId_Object = MibTableColumn
cermPolicyResOwnerSubEntityId = _CermPolicyResOwnerSubEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 2),
    _CermPolicyResOwnerSubEntityId_Type()
)
cermPolicyResOwnerSubEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyResOwnerSubEntityId.setStatus("current")
_CermPolicyResOwnerId_Type = CermOwnerId
_CermPolicyResOwnerId_Object = MibTableColumn
cermPolicyResOwnerId = _CermPolicyResOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 3),
    _CermPolicyResOwnerId_Type()
)
cermPolicyResOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyResOwnerId.setStatus("current")
_CermPolicyResOwnerSubTypeId_Type = Unsigned32
_CermPolicyResOwnerSubTypeId_Object = MibTableColumn
cermPolicyResOwnerSubTypeId = _CermPolicyResOwnerSubTypeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 4),
    _CermPolicyResOwnerSubTypeId_Type()
)
cermPolicyResOwnerSubTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyResOwnerSubTypeId.setStatus("current")
_CermPolicyIsUserGlobal_Type = TruthValue
_CermPolicyIsUserGlobal_Object = MibTableColumn
cermPolicyIsUserGlobal = _CermPolicyIsUserGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 5),
    _CermPolicyIsUserGlobal_Type()
)
cermPolicyIsUserGlobal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyIsUserGlobal.setStatus("current")
_CermPolicyThresholdSeverity_Type = CermThresholdSeverity
_CermPolicyThresholdSeverity_Object = MibTableColumn
cermPolicyThresholdSeverity = _CermPolicyThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 6),
    _CermPolicyThresholdSeverity_Type()
)
cermPolicyThresholdSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyThresholdSeverity.setStatus("current")
_CermPolicyRisingThreshold_Type = CermThreshold
_CermPolicyRisingThreshold_Object = MibTableColumn
cermPolicyRisingThreshold = _CermPolicyRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 7),
    _CermPolicyRisingThreshold_Type()
)
cermPolicyRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyRisingThreshold.setStatus("current")


class _CermPolicyRisingInterval_Type(CermDampenInterval):
    """Custom type cermPolicyRisingInterval based on CermDampenInterval"""
    defaultValue = 0


_CermPolicyRisingInterval_Object = MibTableColumn
cermPolicyRisingInterval = _CermPolicyRisingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 8),
    _CermPolicyRisingInterval_Type()
)
cermPolicyRisingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyRisingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cermPolicyRisingInterval.setUnits("seconds")


class _CermPolicyFallingThreshold_Type(CermThresholdOrZero):
    """Custom type cermPolicyFallingThreshold based on CermThresholdOrZero"""
    defaultValue = 0


_CermPolicyFallingThreshold_Object = MibTableColumn
cermPolicyFallingThreshold = _CermPolicyFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 9),
    _CermPolicyFallingThreshold_Type()
)
cermPolicyFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyFallingThreshold.setStatus("current")


class _CermPolicyFallingInterval_Type(CermDampenInterval):
    """Custom type cermPolicyFallingInterval based on CermDampenInterval"""
    defaultValue = 0


_CermPolicyFallingInterval_Object = MibTableColumn
cermPolicyFallingInterval = _CermPolicyFallingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 10),
    _CermPolicyFallingInterval_Type()
)
cermPolicyFallingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyFallingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cermPolicyFallingInterval.setUnits("seconds")


class _CermPolicyResOwnerThreshStorageType_Type(StorageType):
    """Custom type cermPolicyResOwnerThreshStorageType based on StorageType"""


_CermPolicyResOwnerThreshStorageType_Object = MibTableColumn
cermPolicyResOwnerThreshStorageType = _CermPolicyResOwnerThreshStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 11),
    _CermPolicyResOwnerThreshStorageType_Type()
)
cermPolicyResOwnerThreshStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyResOwnerThreshStorageType.setStatus("current")
_CermPolicyResOwnerThreshRowStatus_Type = RowStatus
_CermPolicyResOwnerThreshRowStatus_Object = MibTableColumn
cermPolicyResOwnerThreshRowStatus = _CermPolicyResOwnerThreshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 2, 1, 12),
    _CermPolicyResOwnerThreshRowStatus_Type()
)
cermPolicyResOwnerThreshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyResOwnerThreshRowStatus.setStatus("current")
_CermConfigResGroupTable_Object = MibTable
cermConfigResGroupTable = _CermConfigResGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cermConfigResGroupTable.setStatus("current")
_CermConfigResGroupEntry_Object = MibTableRow
cermConfigResGroupEntry = _CermConfigResGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 3, 1)
)
cermConfigResGroupEntry.setIndexNames(
    (0, "CISCO-ERM-MIB", "cermConfigResGroupName"),
)
if mibBuilder.loadTexts:
    cermConfigResGroupEntry.setStatus("current")


class _CermConfigResGroupName_Type(SnmpAdminString):
    """Custom type cermConfigResGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CermConfigResGroupName_Type.__name__ = "SnmpAdminString"
_CermConfigResGroupName_Object = MibTableColumn
cermConfigResGroupName = _CermConfigResGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 3, 1, 1),
    _CermConfigResGroupName_Type()
)
cermConfigResGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermConfigResGroupName.setStatus("current")


class _CermConfigResGroupUserTypeName_Type(SnmpAdminString):
    """Custom type cermConfigResGroupUserTypeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermConfigResGroupUserTypeName_Type.__name__ = "SnmpAdminString"
_CermConfigResGroupUserTypeName_Object = MibTableColumn
cermConfigResGroupUserTypeName = _CermConfigResGroupUserTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 3, 1, 2),
    _CermConfigResGroupUserTypeName_Type()
)
cermConfigResGroupUserTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermConfigResGroupUserTypeName.setStatus("current")


class _CermConfigResGroupStorageType_Type(StorageType):
    """Custom type cermConfigResGroupStorageType based on StorageType"""


_CermConfigResGroupStorageType_Object = MibTableColumn
cermConfigResGroupStorageType = _CermConfigResGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 3, 1, 3),
    _CermConfigResGroupStorageType_Type()
)
cermConfigResGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermConfigResGroupStorageType.setStatus("current")
_CermConfigResGroupRowStatus_Type = RowStatus
_CermConfigResGroupRowStatus_Object = MibTableColumn
cermConfigResGroupRowStatus = _CermConfigResGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 3, 1, 4),
    _CermConfigResGroupRowStatus_Type()
)
cermConfigResGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermConfigResGroupRowStatus.setStatus("current")
_CermConfigResGroupUserTable_Object = MibTable
cermConfigResGroupUserTable = _CermConfigResGroupUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cermConfigResGroupUserTable.setStatus("current")
_CermConfigResGroupUserEntry_Object = MibTableRow
cermConfigResGroupUserEntry = _CermConfigResGroupUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 4, 1)
)
cermConfigResGroupUserEntry.setIndexNames(
    (0, "CISCO-ERM-MIB", "cermConfigResGroupName"),
    (0, "CISCO-ERM-MIB", "cermConfigResGroupUserName"),
)
if mibBuilder.loadTexts:
    cermConfigResGroupUserEntry.setStatus("current")


class _CermConfigResGroupUserName_Type(SnmpAdminString):
    """Custom type cermConfigResGroupUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermConfigResGroupUserName_Type.__name__ = "SnmpAdminString"
_CermConfigResGroupUserName_Object = MibTableColumn
cermConfigResGroupUserName = _CermConfigResGroupUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 4, 1, 1),
    _CermConfigResGroupUserName_Type()
)
cermConfigResGroupUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermConfigResGroupUserName.setStatus("current")


class _CermConfigResGroupUserStorageType_Type(StorageType):
    """Custom type cermConfigResGroupUserStorageType based on StorageType"""


_CermConfigResGroupUserStorageType_Object = MibTableColumn
cermConfigResGroupUserStorageType = _CermConfigResGroupUserStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 4, 1, 2),
    _CermConfigResGroupUserStorageType_Type()
)
cermConfigResGroupUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermConfigResGroupUserStorageType.setStatus("current")
_CermConfigResGroupUserRowStatus_Type = RowStatus
_CermConfigResGroupUserRowStatus_Object = MibTableColumn
cermConfigResGroupUserRowStatus = _CermConfigResGroupUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 4, 1, 3),
    _CermConfigResGroupUserRowStatus_Type()
)
cermConfigResGroupUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermConfigResGroupUserRowStatus.setStatus("current")
_CermConfigPolicyApplyTable_Object = MibTable
cermConfigPolicyApplyTable = _CermConfigPolicyApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cermConfigPolicyApplyTable.setStatus("current")
_CermConfigPolicyApplyEntry_Object = MibTableRow
cermConfigPolicyApplyEntry = _CermConfigPolicyApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 5, 1)
)
cermConfigPolicyApplyEntry.setIndexNames(
    (0, "CISCO-ERM-MIB", "cermPolicyApplyUserOrGroupName"),
    (0, "CISCO-ERM-MIB", "cermPolicyApplyUserOrGroupFlag"),
)
if mibBuilder.loadTexts:
    cermConfigPolicyApplyEntry.setStatus("current")


class _CermPolicyApplyUserOrGroupName_Type(SnmpAdminString):
    """Custom type cermPolicyApplyUserOrGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermPolicyApplyUserOrGroupName_Type.__name__ = "SnmpAdminString"
_CermPolicyApplyUserOrGroupName_Object = MibTableColumn
cermPolicyApplyUserOrGroupName = _CermPolicyApplyUserOrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 5, 1, 1),
    _CermPolicyApplyUserOrGroupName_Type()
)
cermPolicyApplyUserOrGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyApplyUserOrGroupName.setStatus("current")
_CermPolicyApplyUserOrGroupFlag_Type = CermUserOrGroup
_CermPolicyApplyUserOrGroupFlag_Object = MibTableColumn
cermPolicyApplyUserOrGroupFlag = _CermPolicyApplyUserOrGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 5, 1, 2),
    _CermPolicyApplyUserOrGroupFlag_Type()
)
cermPolicyApplyUserOrGroupFlag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cermPolicyApplyUserOrGroupFlag.setStatus("current")


class _CermPolicyApplyPolicyName_Type(SnmpAdminString):
    """Custom type cermPolicyApplyPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CermPolicyApplyPolicyName_Type.__name__ = "SnmpAdminString"
_CermPolicyApplyPolicyName_Object = MibTableColumn
cermPolicyApplyPolicyName = _CermPolicyApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 5, 1, 3),
    _CermPolicyApplyPolicyName_Type()
)
cermPolicyApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyApplyPolicyName.setStatus("current")


class _CermPolicyApplyStorageType_Type(StorageType):
    """Custom type cermPolicyApplyStorageType based on StorageType"""


_CermPolicyApplyStorageType_Object = MibTableColumn
cermPolicyApplyStorageType = _CermPolicyApplyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 5, 1, 4),
    _CermPolicyApplyStorageType_Type()
)
cermPolicyApplyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyApplyStorageType.setStatus("current")
_CermPolicyApplyRowStatus_Type = RowStatus
_CermPolicyApplyRowStatus_Object = MibTableColumn
cermPolicyApplyRowStatus = _CermPolicyApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 3, 5, 1, 5),
    _CermPolicyApplyRowStatus_Type()
)
cermPolicyApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cermPolicyApplyRowStatus.setStatus("current")
_CermNotifObjects_ObjectIdentity = ObjectIdentity
cermNotifObjects = _CermNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 4)
)
_CermNotifsThresholdSeverity_Type = CermThresholdSeverity
_CermNotifsThresholdSeverity_Object = MibScalar
cermNotifsThresholdSeverity = _CermNotifsThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 4, 1),
    _CermNotifsThresholdSeverity_Type()
)
cermNotifsThresholdSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermNotifsThresholdSeverity.setStatus("current")
_CermNotifsThresholdIsUserGlob_Type = TruthValue
_CermNotifsThresholdIsUserGlob_Object = MibScalar
cermNotifsThresholdIsUserGlob = _CermNotifsThresholdIsUserGlob_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 4, 2),
    _CermNotifsThresholdIsUserGlob_Type()
)
cermNotifsThresholdIsUserGlob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermNotifsThresholdIsUserGlob.setStatus("current")
_CermNotifsThresholdValue_Type = CermThreshold
_CermNotifsThresholdValue_Object = MibScalar
cermNotifsThresholdValue = _CermNotifsThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 4, 3),
    _CermNotifsThresholdValue_Type()
)
cermNotifsThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermNotifsThresholdValue.setStatus("current")
_CermNotifsDirection_Type = CermNotificationDirection
_CermNotifsDirection_Object = MibScalar
cermNotifsDirection = _CermNotifsDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 4, 4),
    _CermNotifsDirection_Type()
)
cermNotifsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermNotifsDirection.setStatus("current")
_CermNotifsPolicyName_Type = SnmpAdminString
_CermNotifsPolicyName_Object = MibScalar
cermNotifsPolicyName = _CermNotifsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 4, 5),
    _CermNotifsPolicyName_Type()
)
cermNotifsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cermNotifsPolicyName.setStatus("current")
_CermNotifControlObjects_ObjectIdentity = ObjectIdentity
cermNotifControlObjects = _CermNotifControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 5)
)


class _CermNotifsEnabled_Type(TruthValue):
    """Custom type cermNotifsEnabled based on TruthValue"""


_CermNotifsEnabled_Object = MibScalar
cermNotifsEnabled = _CermNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 5, 1),
    _CermNotifsEnabled_Type()
)
cermNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cermNotifsEnabled.setStatus("current")
_CiscoErmMIBConform_ObjectIdentity = ObjectIdentity
ciscoErmMIBConform = _CiscoErmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2)
)
_CiscoErmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoErmMIBCompliances = _CiscoErmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1)
)
_CiscoErmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoErmMIBGroups = _CiscoErmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2)
)

# Managed Objects groups

ciscoErmResOwnerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 1)
)
ciscoErmResOwnerGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermResOwnerName"),
        ("CISCO-ERM-MIB", "cermResOwnerMeasurementUnit"),
        ("CISCO-ERM-MIB", "cermResOwnerThreshIsConfigurable"),
        ("CISCO-ERM-MIB", "cermResOwnerResUserCount"),
        ("CISCO-ERM-MIB", "cermResOwnerResGroupCount"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeName"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeUsagePct"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeUsage"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeMaxUsage"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeGlobNotifSeverity"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeRisingThresh"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeRisingInterval"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeFallingThresh"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeFallingInterval"))
)
if mibBuilder.loadTexts:
    ciscoErmResOwnerGroup.setStatus("current")

ciscoErmResUserTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 2)
)
ciscoErmResUserTypeGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermResUserTypeName"),
        ("CISCO-ERM-MIB", "cermResUserTypeResOwnerCount"),
        ("CISCO-ERM-MIB", "cermResUserTypeResUserCount"),
        ("CISCO-ERM-MIB", "cermResUserTypeResGroupCount"),
        ("CISCO-ERM-MIB", "cermResUserTypeResOwnerId"))
)
if mibBuilder.loadTexts:
    ciscoErmResUserTypeGroup.setStatus("current")

ciscoErmResUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 3)
)
ciscoErmResUserGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermResUserName"),
        ("CISCO-ERM-MIB", "cermResUserPriority"),
        ("CISCO-ERM-MIB", "cermResUserResGroupId"))
)
if mibBuilder.loadTexts:
    ciscoErmResUserGroup.setStatus("current")

ciscoErmResGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 4)
)
ciscoErmResGroupGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermResGroupName"),
        ("CISCO-ERM-MIB", "cermResGroupUserInstanceCount"),
        ("CISCO-ERM-MIB", "cermResGroupResUserId"))
)
if mibBuilder.loadTexts:
    ciscoErmResGroupGroup.setStatus("current")

ciscoErmResOwnerResUserOrGroupRelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 5)
)
ciscoErmResOwnerResUserOrGroupRelationGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermResUserOrGroupFlag"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupUsagePct"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupUsage"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupMaxUsage"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupNotifSeverity"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupGlobNotifSeverity"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupThreshFlag"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupRisingThresh"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupRisingInterval"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupFallingThresh"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupFallingInterval"))
)
if mibBuilder.loadTexts:
    ciscoErmResOwnerResUserOrGroupRelationGroup.setStatus("current")

ciscoErmResMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 6)
)
ciscoErmResMonitorGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermResMonitorName"),
        ("CISCO-ERM-MIB", "cermResMonitorResPolicyName"),
        ("CISCO-ERM-MIB", "cermResMonitorPolicyName"))
)
if mibBuilder.loadTexts:
    ciscoErmResMonitorGroup.setStatus("current")

ciscoErmPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 7)
)
ciscoErmPolicyConfigGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermScalarsGlobalPolicyName"),
        ("CISCO-ERM-MIB", "cermPolicyIsGlobal"),
        ("CISCO-ERM-MIB", "cermPolicyUserTypeName"),
        ("CISCO-ERM-MIB", "cermPolicyLoggingEnabled"),
        ("CISCO-ERM-MIB", "cermPolicySnmpNotifEnabled"),
        ("CISCO-ERM-MIB", "cermPolicyStorageType"),
        ("CISCO-ERM-MIB", "cermPolicyRowStatus"),
        ("CISCO-ERM-MIB", "cermPolicyRisingThreshold"),
        ("CISCO-ERM-MIB", "cermPolicyRisingInterval"),
        ("CISCO-ERM-MIB", "cermPolicyFallingThreshold"),
        ("CISCO-ERM-MIB", "cermPolicyFallingInterval"),
        ("CISCO-ERM-MIB", "cermPolicyResOwnerThreshStorageType"),
        ("CISCO-ERM-MIB", "cermPolicyResOwnerThreshRowStatus"),
        ("CISCO-ERM-MIB", "cermPolicyApplyPolicyName"),
        ("CISCO-ERM-MIB", "cermPolicyApplyStorageType"),
        ("CISCO-ERM-MIB", "cermPolicyApplyRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoErmPolicyConfigGroup.setStatus("current")

ciscoErmResGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 8)
)
ciscoErmResGroupConfigGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermConfigResGroupUserTypeName"),
        ("CISCO-ERM-MIB", "cermConfigResGroupStorageType"),
        ("CISCO-ERM-MIB", "cermConfigResGroupRowStatus"),
        ("CISCO-ERM-MIB", "cermConfigResGroupUserStorageType"),
        ("CISCO-ERM-MIB", "cermConfigResGroupUserRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoErmResGroupConfigGroup.setStatus("current")

ciscoErmNotifControlObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 9)
)
ciscoErmNotifControlObjectsGroup.setObjects(
    ("CISCO-ERM-MIB", "cermNotifsEnabled")
)
if mibBuilder.loadTexts:
    ciscoErmNotifControlObjectsGroup.setStatus("current")

ciscoErmNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 10)
)
ciscoErmNotifObjectsGroup.setObjects(
      *(("CISCO-ERM-MIB", "cermNotifsThresholdSeverity"),
        ("CISCO-ERM-MIB", "cermNotifsThresholdIsUserGlob"),
        ("CISCO-ERM-MIB", "cermNotifsThresholdValue"),
        ("CISCO-ERM-MIB", "cermNotifsDirection"),
        ("CISCO-ERM-MIB", "cermNotifsPolicyName"))
)
if mibBuilder.loadTexts:
    ciscoErmNotifObjectsGroup.setStatus("current")


# Notification objects

ciscoErmGlobalPolicyViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 0, 1)
)
ciscoErmGlobalPolicyViolation.setObjects(
      *(("CISCO-ERM-MIB", "cermResOwnerName"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeName"),
        ("CISCO-ERM-MIB", "cermNotifsThresholdSeverity"),
        ("CISCO-ERM-MIB", "cermNotifsThresholdValue"),
        ("CISCO-ERM-MIB", "cermNotifsDirection"),
        ("CISCO-ERM-MIB", "cermNotifsPolicyName"))
)
if mibBuilder.loadTexts:
    ciscoErmGlobalPolicyViolation.setStatus(
        "current"
    )

ciscoErmLocalPolicyViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 0, 2)
)
ciscoErmLocalPolicyViolation.setObjects(
      *(("CISCO-ERM-MIB", "cermResOwnerName"),
        ("CISCO-ERM-MIB", "cermResOwnerSubTypeName"),
        ("CISCO-ERM-MIB", "cermResUserTypeName"),
        ("CISCO-ERM-MIB", "cermResUserName"),
        ("CISCO-ERM-MIB", "cermResUserOrGroupThreshFlag"),
        ("CISCO-ERM-MIB", "cermNotifsThresholdIsUserGlob"),
        ("CISCO-ERM-MIB", "cermNotifsThresholdSeverity"),
        ("CISCO-ERM-MIB", "cermNotifsThresholdValue"),
        ("CISCO-ERM-MIB", "cermNotifsDirection"),
        ("CISCO-ERM-MIB", "cermNotifsPolicyName"))
)
if mibBuilder.loadTexts:
    ciscoErmLocalPolicyViolation.setStatus(
        "current"
    )


# Notifications groups

ciscoErmPolicyViolationNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 11)
)
ciscoErmPolicyViolationNotifGroup.setObjects(
      *(("CISCO-ERM-MIB", "ciscoErmGlobalPolicyViolation"),
        ("CISCO-ERM-MIB", "ciscoErmLocalPolicyViolation"))
)
if mibBuilder.loadTexts:
    ciscoErmPolicyViolationNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoErmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoErmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ERM-MIB",
    **{"CermSubEntityId": CermSubEntityId,
       "CermUserTypeId": CermUserTypeId,
       "CermUserTypeIdOrZero": CermUserTypeIdOrZero,
       "CermUserId": CermUserId,
       "CermUserIdOrZero": CermUserIdOrZero,
       "CermGroupId": CermGroupId,
       "CermOwnerId": CermOwnerId,
       "CermOwnerIdOrZero": CermOwnerIdOrZero,
       "CermMonitorId": CermMonitorId,
       "CermUserOrGroup": CermUserOrGroup,
       "CermResUsagePct": CermResUsagePct,
       "CermThreshold": CermThreshold,
       "CermThresholdOrZero": CermThresholdOrZero,
       "CermDampenInterval": CermDampenInterval,
       "CermThresholdSeverity": CermThresholdSeverity,
       "CermNotificationSeverity": CermNotificationSeverity,
       "CermNotificationDirection": CermNotificationDirection,
       "ciscoErmMIB": ciscoErmMIB,
       "ciscoErmMIBNotifs": ciscoErmMIBNotifs,
       "ciscoErmGlobalPolicyViolation": ciscoErmGlobalPolicyViolation,
       "ciscoErmLocalPolicyViolation": ciscoErmLocalPolicyViolation,
       "ciscoErmMIBObjects": ciscoErmMIBObjects,
       "cermScalars": cermScalars,
       "cermScalarsGlobalPolicyName": cermScalarsGlobalPolicyName,
       "cermStats": cermStats,
       "cermResOwnerTable": cermResOwnerTable,
       "cermResOwnerEntry": cermResOwnerEntry,
       "cermResOwnerSubEntityId": cermResOwnerSubEntityId,
       "cermResOwnerId": cermResOwnerId,
       "cermResOwnerName": cermResOwnerName,
       "cermResOwnerMeasurementUnit": cermResOwnerMeasurementUnit,
       "cermResOwnerThreshIsConfigurable": cermResOwnerThreshIsConfigurable,
       "cermResOwnerResUserCount": cermResOwnerResUserCount,
       "cermResOwnerResGroupCount": cermResOwnerResGroupCount,
       "cermResOwnerSubTypeTable": cermResOwnerSubTypeTable,
       "cermResOwnerSubTypeEntry": cermResOwnerSubTypeEntry,
       "cermResOwnerSubTypeId": cermResOwnerSubTypeId,
       "cermResOwnerSubTypeName": cermResOwnerSubTypeName,
       "cermResOwnerSubTypeUsagePct": cermResOwnerSubTypeUsagePct,
       "cermResOwnerSubTypeUsage": cermResOwnerSubTypeUsage,
       "cermResOwnerSubTypeMaxUsage": cermResOwnerSubTypeMaxUsage,
       "cermResOwnerSubTypeGlobNotifSeverity": cermResOwnerSubTypeGlobNotifSeverity,
       "cermResOwnerSubTypeThresholdTable": cermResOwnerSubTypeThresholdTable,
       "cermResOwnerSubTypeThresholdEntry": cermResOwnerSubTypeThresholdEntry,
       "cermResOwnerSubTypeThreshSeverity": cermResOwnerSubTypeThreshSeverity,
       "cermResOwnerSubTypeRisingThresh": cermResOwnerSubTypeRisingThresh,
       "cermResOwnerSubTypeRisingInterval": cermResOwnerSubTypeRisingInterval,
       "cermResOwnerSubTypeFallingThresh": cermResOwnerSubTypeFallingThresh,
       "cermResOwnerSubTypeFallingInterval": cermResOwnerSubTypeFallingInterval,
       "cermResUserTypeTable": cermResUserTypeTable,
       "cermResUserTypeEntry": cermResUserTypeEntry,
       "cermResUserTypeSubEntityId": cermResUserTypeSubEntityId,
       "cermResUserTypeId": cermResUserTypeId,
       "cermResUserTypeName": cermResUserTypeName,
       "cermResUserTypeResOwnerCount": cermResUserTypeResOwnerCount,
       "cermResUserTypeResUserCount": cermResUserTypeResUserCount,
       "cermResUserTypeResGroupCount": cermResUserTypeResGroupCount,
       "cermResUserTable": cermResUserTable,
       "cermResUserEntry": cermResUserEntry,
       "cermResUserId": cermResUserId,
       "cermResUserName": cermResUserName,
       "cermResUserPriority": cermResUserPriority,
       "cermResUserResGroupId": cermResUserResGroupId,
       "cermResGroupTable": cermResGroupTable,
       "cermResGroupEntry": cermResGroupEntry,
       "cermResGroupId": cermResGroupId,
       "cermResGroupName": cermResGroupName,
       "cermResGroupUserInstanceCount": cermResGroupUserInstanceCount,
       "cermResGroupResUserTable": cermResGroupResUserTable,
       "cermResGroupResUserEntry": cermResGroupResUserEntry,
       "cermResGroupResUserId": cermResGroupResUserId,
       "cermResOwnerResUserOrGroupTable": cermResOwnerResUserOrGroupTable,
       "cermResOwnerResUserOrGroupEntry": cermResOwnerResUserOrGroupEntry,
       "cermResOwnerResUserTypeId": cermResOwnerResUserTypeId,
       "cermResOwnerResUserOrGroupId": cermResOwnerResUserOrGroupId,
       "cermResUserOrGroupFlag": cermResUserOrGroupFlag,
       "cermResUserOrGroupUsagePct": cermResUserOrGroupUsagePct,
       "cermResUserOrGroupUsage": cermResUserOrGroupUsage,
       "cermResUserOrGroupMaxUsage": cermResUserOrGroupMaxUsage,
       "cermResUserOrGroupNotifSeverity": cermResUserOrGroupNotifSeverity,
       "cermResUserOrGroupGlobNotifSeverity": cermResUserOrGroupGlobNotifSeverity,
       "cermResOwnerResUserOrGroupThresholdTable": cermResOwnerResUserOrGroupThresholdTable,
       "cermResOwnerResUserOrGroupThresholdEntry": cermResOwnerResUserOrGroupThresholdEntry,
       "cermResUserOrGroupThreshIsUserGlob": cermResUserOrGroupThreshIsUserGlob,
       "cermResUserOrGroupThreshSeverity": cermResUserOrGroupThreshSeverity,
       "cermResUserOrGroupThreshFlag": cermResUserOrGroupThreshFlag,
       "cermResUserOrGroupRisingThresh": cermResUserOrGroupRisingThresh,
       "cermResUserOrGroupRisingInterval": cermResUserOrGroupRisingInterval,
       "cermResUserOrGroupFallingThresh": cermResUserOrGroupFallingThresh,
       "cermResUserOrGroupFallingInterval": cermResUserOrGroupFallingInterval,
       "cermResUserTypeResOwnerTable": cermResUserTypeResOwnerTable,
       "cermResUserTypeResOwnerEntry": cermResUserTypeResOwnerEntry,
       "cermResUserTypeResOwnerId": cermResUserTypeResOwnerId,
       "cermResMonitorTable": cermResMonitorTable,
       "cermResMonitorEntry": cermResMonitorEntry,
       "cermResMonitorSubEntityId": cermResMonitorSubEntityId,
       "cermResMonitorId": cermResMonitorId,
       "cermResMonitorName": cermResMonitorName,
       "cermResMonitorResOwnerResUserTable": cermResMonitorResOwnerResUserTable,
       "cermResMonitorResOwnerResUserEntry": cermResMonitorResOwnerResUserEntry,
       "cermResMonitorResOwnerId": cermResMonitorResOwnerId,
       "cermResMonitorResUserTypeId": cermResMonitorResUserTypeId,
       "cermResMonitorResUserId": cermResMonitorResUserId,
       "cermResMonitorResPolicyName": cermResMonitorResPolicyName,
       "cermResMonitorPolicyTable": cermResMonitorPolicyTable,
       "cermResMonitorPolicyEntry": cermResMonitorPolicyEntry,
       "cermResMonitorPolicyName": cermResMonitorPolicyName,
       "cermConfig": cermConfig,
       "cermConfigPolicyTable": cermConfigPolicyTable,
       "cermConfigPolicyEntry": cermConfigPolicyEntry,
       "cermPolicyName": cermPolicyName,
       "cermPolicyIsGlobal": cermPolicyIsGlobal,
       "cermPolicyUserTypeName": cermPolicyUserTypeName,
       "cermPolicyLoggingEnabled": cermPolicyLoggingEnabled,
       "cermPolicySnmpNotifEnabled": cermPolicySnmpNotifEnabled,
       "cermPolicyStorageType": cermPolicyStorageType,
       "cermPolicyRowStatus": cermPolicyRowStatus,
       "cermConfigPolicyResOwnerThreshTable": cermConfigPolicyResOwnerThreshTable,
       "cermConfigPolicyResOwnerThreshEntry": cermConfigPolicyResOwnerThreshEntry,
       "cermPolicyPhysicalIndex": cermPolicyPhysicalIndex,
       "cermPolicyResOwnerSubEntityId": cermPolicyResOwnerSubEntityId,
       "cermPolicyResOwnerId": cermPolicyResOwnerId,
       "cermPolicyResOwnerSubTypeId": cermPolicyResOwnerSubTypeId,
       "cermPolicyIsUserGlobal": cermPolicyIsUserGlobal,
       "cermPolicyThresholdSeverity": cermPolicyThresholdSeverity,
       "cermPolicyRisingThreshold": cermPolicyRisingThreshold,
       "cermPolicyRisingInterval": cermPolicyRisingInterval,
       "cermPolicyFallingThreshold": cermPolicyFallingThreshold,
       "cermPolicyFallingInterval": cermPolicyFallingInterval,
       "cermPolicyResOwnerThreshStorageType": cermPolicyResOwnerThreshStorageType,
       "cermPolicyResOwnerThreshRowStatus": cermPolicyResOwnerThreshRowStatus,
       "cermConfigResGroupTable": cermConfigResGroupTable,
       "cermConfigResGroupEntry": cermConfigResGroupEntry,
       "cermConfigResGroupName": cermConfigResGroupName,
       "cermConfigResGroupUserTypeName": cermConfigResGroupUserTypeName,
       "cermConfigResGroupStorageType": cermConfigResGroupStorageType,
       "cermConfigResGroupRowStatus": cermConfigResGroupRowStatus,
       "cermConfigResGroupUserTable": cermConfigResGroupUserTable,
       "cermConfigResGroupUserEntry": cermConfigResGroupUserEntry,
       "cermConfigResGroupUserName": cermConfigResGroupUserName,
       "cermConfigResGroupUserStorageType": cermConfigResGroupUserStorageType,
       "cermConfigResGroupUserRowStatus": cermConfigResGroupUserRowStatus,
       "cermConfigPolicyApplyTable": cermConfigPolicyApplyTable,
       "cermConfigPolicyApplyEntry": cermConfigPolicyApplyEntry,
       "cermPolicyApplyUserOrGroupName": cermPolicyApplyUserOrGroupName,
       "cermPolicyApplyUserOrGroupFlag": cermPolicyApplyUserOrGroupFlag,
       "cermPolicyApplyPolicyName": cermPolicyApplyPolicyName,
       "cermPolicyApplyStorageType": cermPolicyApplyStorageType,
       "cermPolicyApplyRowStatus": cermPolicyApplyRowStatus,
       "cermNotifObjects": cermNotifObjects,
       "cermNotifsThresholdSeverity": cermNotifsThresholdSeverity,
       "cermNotifsThresholdIsUserGlob": cermNotifsThresholdIsUserGlob,
       "cermNotifsThresholdValue": cermNotifsThresholdValue,
       "cermNotifsDirection": cermNotifsDirection,
       "cermNotifsPolicyName": cermNotifsPolicyName,
       "cermNotifControlObjects": cermNotifControlObjects,
       "cermNotifsEnabled": cermNotifsEnabled,
       "ciscoErmMIBConform": ciscoErmMIBConform,
       "ciscoErmMIBCompliances": ciscoErmMIBCompliances,
       "ciscoErmMIBCompliance": ciscoErmMIBCompliance,
       "ciscoErmMIBGroups": ciscoErmMIBGroups,
       "ciscoErmResOwnerGroup": ciscoErmResOwnerGroup,
       "ciscoErmResUserTypeGroup": ciscoErmResUserTypeGroup,
       "ciscoErmResUserGroup": ciscoErmResUserGroup,
       "ciscoErmResGroupGroup": ciscoErmResGroupGroup,
       "ciscoErmResOwnerResUserOrGroupRelationGroup": ciscoErmResOwnerResUserOrGroupRelationGroup,
       "ciscoErmResMonitorGroup": ciscoErmResMonitorGroup,
       "ciscoErmPolicyConfigGroup": ciscoErmPolicyConfigGroup,
       "ciscoErmResGroupConfigGroup": ciscoErmResGroupConfigGroup,
       "ciscoErmNotifControlObjectsGroup": ciscoErmNotifControlObjectsGroup,
       "ciscoErmNotifObjectsGroup": ciscoErmNotifObjectsGroup,
       "ciscoErmPolicyViolationNotifGroup": ciscoErmPolicyViolationNotifGroup}
)
