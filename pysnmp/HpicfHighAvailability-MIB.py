# SNMP MIB module (HpicfHighAvailability-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HpicfHighAvailability-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:53 2024
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

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(EntityStandbyStatus,) = mibBuilder.importSymbols(
    "ENTITY-STATE-MIB",
    "EntityStandbyStatus")

(hpicfCommon,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpicfHighAvailability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11)
)
hpicfHighAvailability.setRevisions(
        ("2017-01-05 00:00",
         "2012-05-15 00:00",
         "2009-10-18 00:00",
         "2009-09-06 00:00",
         "2009-08-21 00:00",
         "2006-09-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfHAConfigObjects_ObjectIdentity = ObjectIdentity
hpicfHAConfigObjects = _HpicfHAConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 1)
)


class _HpicfHARedundancyManagementModuleMode_Type(Integer32):
    """Custom type hpicfHARedundancyManagementModuleMode based on Integer32"""
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
          ("warmStandby", 3))
    )


_HpicfHARedundancyManagementModuleMode_Type.__name__ = "Integer32"
_HpicfHARedundancyManagementModuleMode_Object = MibScalar
hpicfHARedundancyManagementModuleMode = _HpicfHARedundancyManagementModuleMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 1, 1),
    _HpicfHARedundancyManagementModuleMode_Type()
)
hpicfHARedundancyManagementModuleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfHARedundancyManagementModuleMode.setStatus("current")


class _HpicfHAContinuousFwdingTime_Type(Unsigned32):
    """Custom type hpicfHAContinuousFwdingTime based on Unsigned32"""
    defaultValue = 300


_HpicfHAContinuousFwdingTime_Object = MibScalar
hpicfHAContinuousFwdingTime = _HpicfHAContinuousFwdingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 1, 2),
    _HpicfHAContinuousFwdingTime_Type()
)
hpicfHAContinuousFwdingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfHAContinuousFwdingTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfHAContinuousFwdingTime.setUnits("seconds")


class _HpicfHAPreferredActiveManagement_Type(Integer32):
    """Custom type hpicfHAPreferredActiveManagement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("management-module1", 1),
          ("management-module2", 2),
          ("none", 0))
    )


_HpicfHAPreferredActiveManagement_Type.__name__ = "Integer32"
_HpicfHAPreferredActiveManagement_Object = MibScalar
hpicfHAPreferredActiveManagement = _HpicfHAPreferredActiveManagement_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 1, 3),
    _HpicfHAPreferredActiveManagement_Type()
)
hpicfHAPreferredActiveManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfHAPreferredActiveManagement.setStatus("current")
_HpicfHAStatusObjects_ObjectIdentity = ObjectIdentity
hpicfHAStatusObjects = _HpicfHAStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2)
)


class _HpicfHAMgmtRedundancyFailureReason_Type(Integer32):
    """Custom type hpicfHAMgmtRedundancyFailureReason based on Integer32"""
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
        *(("communicationFailure", 6),
          ("failedSelftest", 5),
          ("mismatchOS", 4),
          ("noFailure", 2),
          ("noRedundantModule", 1),
          ("redundancyDisable", 7),
          ("unknownReason", 3))
    )


_HpicfHAMgmtRedundancyFailureReason_Type.__name__ = "Integer32"
_HpicfHAMgmtRedundancyFailureReason_Object = MibScalar
hpicfHAMgmtRedundancyFailureReason = _HpicfHAMgmtRedundancyFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 1),
    _HpicfHAMgmtRedundancyFailureReason_Type()
)
hpicfHAMgmtRedundancyFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAMgmtRedundancyFailureReason.setStatus("current")
_HpicfHAMgmtFailovers_Type = Counter32
_HpicfHAMgmtFailovers_Object = MibScalar
hpicfHAMgmtFailovers = _HpicfHAMgmtFailovers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 2),
    _HpicfHAMgmtFailovers_Type()
)
hpicfHAMgmtFailovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAMgmtFailovers.setStatus("current")
_HpicfHALastFailoverTime_Type = TimeTicks
_HpicfHALastFailoverTime_Object = MibScalar
hpicfHALastFailoverTime = _HpicfHALastFailoverTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 3),
    _HpicfHALastFailoverTime_Type()
)
hpicfHALastFailoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHALastFailoverTime.setStatus("current")
_HpicfHAFailOverLogTable_Object = MibTable
hpicfHAFailOverLogTable = _HpicfHAFailOverLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfHAFailOverLogTable.setStatus("current")
_HpicfHAFailOverLogEntry_Object = MibTableRow
hpicfHAFailOverLogEntry = _HpicfHAFailOverLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 4, 1)
)
hpicfHAFailOverLogEntry.setIndexNames(
    (0, "HpicfHighAvailability-MIB", "hpicfHAFailOverIndex"),
)
if mibBuilder.loadTexts:
    hpicfHAFailOverLogEntry.setStatus("current")


class _HpicfHAFailOverIndex_Type(Integer32):
    """Custom type hpicfHAFailOverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfHAFailOverIndex_Type.__name__ = "Integer32"
_HpicfHAFailOverIndex_Object = MibTableColumn
hpicfHAFailOverIndex = _HpicfHAFailOverIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 4, 1, 1),
    _HpicfHAFailOverIndex_Type()
)
hpicfHAFailOverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfHAFailOverIndex.setStatus("current")
_HpicfHAFailOverMgmtModule_Type = PhysicalIndex
_HpicfHAFailOverMgmtModule_Object = MibTableColumn
hpicfHAFailOverMgmtModule = _HpicfHAFailOverMgmtModule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 4, 1, 2),
    _HpicfHAFailOverMgmtModule_Type()
)
hpicfHAFailOverMgmtModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAFailOverMgmtModule.setStatus("current")


class _HpicfHAFailOverState_Type(Integer32):
    """Custom type hpicfHAFailOverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 3),
          ("unknown", 1))
    )


_HpicfHAFailOverState_Type.__name__ = "Integer32"
_HpicfHAFailOverState_Object = MibTableColumn
hpicfHAFailOverState = _HpicfHAFailOverState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 4, 1, 3),
    _HpicfHAFailOverState_Type()
)
hpicfHAFailOverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAFailOverState.setStatus("current")
_HpicfHAFailOverTime_Type = Integer32
_HpicfHAFailOverTime_Object = MibTableColumn
hpicfHAFailOverTime = _HpicfHAFailOverTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 4, 1, 4),
    _HpicfHAFailOverTime_Type()
)
hpicfHAFailOverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAFailOverTime.setStatus("current")


class _HpicfHAFailOverReason_Type(Integer32):
    """Custom type hpicfHAFailOverReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("activeReset", 4),
          ("altReset", 5),
          ("buttonReq", 2),
          ("crashReq", 3),
          ("invalid", 0),
          ("switchoverReq", 1))
    )


_HpicfHAFailOverReason_Type.__name__ = "Integer32"
_HpicfHAFailOverReason_Object = MibTableColumn
hpicfHAFailOverReason = _HpicfHAFailOverReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 4, 1, 5),
    _HpicfHAFailOverReason_Type()
)
hpicfHAFailOverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAFailOverReason.setStatus("current")
_HpicfHAMgmtModuleTable_Object = MibTable
hpicfHAMgmtModuleTable = _HpicfHAMgmtModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleTable.setStatus("current")
_HpicfHAMgmtModuleEntry_Object = MibTableRow
hpicfHAMgmtModuleEntry = _HpicfHAMgmtModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 5, 1)
)
hpicfHAMgmtModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleEntry.setStatus("current")
_HpicfHAMgmtModuleState_Type = EntityStandbyStatus
_HpicfHAMgmtModuleState_Object = MibTableColumn
hpicfHAMgmtModuleState = _HpicfHAMgmtModuleState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 5, 1, 1),
    _HpicfHAMgmtModuleState_Type()
)
hpicfHAMgmtModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleState.setStatus("current")
_HpicfHAMgmtModuleCardUpSince_Type = Integer32
_HpicfHAMgmtModuleCardUpSince_Object = MibTableColumn
hpicfHAMgmtModuleCardUpSince = _HpicfHAMgmtModuleCardUpSince_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 5, 1, 2),
    _HpicfHAMgmtModuleCardUpSince_Type()
)
hpicfHAMgmtModuleCardUpSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleCardUpSince.setStatus("current")
_HpicfHAMgmtModuleStateSince_Type = Integer32
_HpicfHAMgmtModuleStateSince_Object = MibTableColumn
hpicfHAMgmtModuleStateSince = _HpicfHAMgmtModuleStateSince_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 5, 1, 3),
    _HpicfHAMgmtModuleStateSince_Type()
)
hpicfHAMgmtModuleStateSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleStateSince.setStatus("current")


class _HpicfHAMgmtModuleRedundancyState_Type(Integer32):
    """Custom type hpicfHAMgmtModuleRedundancyState based on Integer32"""
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
        *(("active", 2),
          ("disabled", 3),
          ("hitless", 6),
          ("syncing", 4),
          ("unavailable", 1),
          ("warmStandby", 5))
    )


_HpicfHAMgmtModuleRedundancyState_Type.__name__ = "Integer32"
_HpicfHAMgmtModuleRedundancyState_Object = MibTableColumn
hpicfHAMgmtModuleRedundancyState = _HpicfHAMgmtModuleRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 5, 1, 4),
    _HpicfHAMgmtModuleRedundancyState_Type()
)
hpicfHAMgmtModuleRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleRedundancyState.setStatus("current")


class _HpicfHAMgmtModuleBackUpState_Type(Integer32):
    """Custom type hpicfHAMgmtModuleBackUpState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("batchBackup", 5),
          ("failed", 0),
          ("offline", 7),
          ("realtimeBackupToSlave", 3),
          ("receivingRealtimeData", 6),
          ("slaveIsAbsent", 4),
          ("unknown", 1),
          ("waiting", 2))
    )


_HpicfHAMgmtModuleBackUpState_Type.__name__ = "Integer32"
_HpicfHAMgmtModuleBackUpState_Object = MibTableColumn
hpicfHAMgmtModuleBackUpState = _HpicfHAMgmtModuleBackUpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 2, 5, 1, 5),
    _HpicfHAMgmtModuleBackUpState_Type()
)
hpicfHAMgmtModuleBackUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleBackUpState.setStatus("current")
_HpicfHAConformance_ObjectIdentity = ObjectIdentity
hpicfHAConformance = _HpicfHAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3)
)
_HpicfHACompliances_ObjectIdentity = ObjectIdentity
hpicfHACompliances = _HpicfHACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 1)
)
_HpicfHAGroups_ObjectIdentity = ObjectIdentity
hpicfHAGroups = _HpicfHAGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 2)
)

# Managed Objects groups

hpicfHAConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 2, 1)
)
hpicfHAConfigGroup.setObjects(
      *(("HpicfHighAvailability-MIB", "hpicfHARedundancyManagementModuleMode"),
        ("HpicfHighAvailability-MIB", "hpicfHAContinuousFwdingTime"))
)
if mibBuilder.loadTexts:
    hpicfHAConfigGroup.setStatus("deprecated")

hpicfHAStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 2, 2)
)
hpicfHAStatusGroup.setObjects(
      *(("HpicfHighAvailability-MIB", "hpicfHAMgmtRedundancyFailureReason"),
        ("HpicfHighAvailability-MIB", "hpicfHAMgmtFailovers"),
        ("HpicfHighAvailability-MIB", "hpicfHALastFailoverTime"))
)
if mibBuilder.loadTexts:
    hpicfHAStatusGroup.setStatus("current")

hpicfHAFailOverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 2, 3)
)
hpicfHAFailOverGroup.setObjects(
      *(("HpicfHighAvailability-MIB", "hpicfHAFailOverMgmtModule"),
        ("HpicfHighAvailability-MIB", "hpicfHAFailOverState"),
        ("HpicfHighAvailability-MIB", "hpicfHAFailOverTime"),
        ("HpicfHighAvailability-MIB", "hpicfHAFailOverReason"))
)
if mibBuilder.loadTexts:
    hpicfHAFailOverGroup.setStatus("current")

hpicfHAMgmtModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 2, 4)
)
hpicfHAMgmtModuleGroup.setObjects(
      *(("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleState"),
        ("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleCardUpSince"),
        ("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleStateSince"),
        ("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleRedundancyState"))
)
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleGroup.setStatus("deprecated")

hpicfHAMgmtModuleGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 2, 5)
)
hpicfHAMgmtModuleGroup1.setObjects(
      *(("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleState"),
        ("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleCardUpSince"),
        ("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleStateSince"),
        ("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleRedundancyState"),
        ("HpicfHighAvailability-MIB", "hpicfHAMgmtModuleBackUpState"))
)
if mibBuilder.loadTexts:
    hpicfHAMgmtModuleGroup1.setStatus("current")

hpicfHAConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 2, 6)
)
hpicfHAConfigGroup1.setObjects(
      *(("HpicfHighAvailability-MIB", "hpicfHARedundancyManagementModuleMode"),
        ("HpicfHighAvailability-MIB", "hpicfHAContinuousFwdingTime"),
        ("HpicfHighAvailability-MIB", "hpicfHAPreferredActiveManagement"))
)
if mibBuilder.loadTexts:
    hpicfHAConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfHACompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfHACompliance.setStatus(
        "deprecated"
    )

hpicfHACompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfHACompliance1.setStatus(
        "deprecated"
    )

hpicfHACompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfHACompliance2.setStatus(
        "current"
    )

hpicfHACompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 11, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfHACompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HpicfHighAvailability-MIB",
    **{"hpicfHighAvailability": hpicfHighAvailability,
       "hpicfHAConfigObjects": hpicfHAConfigObjects,
       "hpicfHARedundancyManagementModuleMode": hpicfHARedundancyManagementModuleMode,
       "hpicfHAContinuousFwdingTime": hpicfHAContinuousFwdingTime,
       "hpicfHAPreferredActiveManagement": hpicfHAPreferredActiveManagement,
       "hpicfHAStatusObjects": hpicfHAStatusObjects,
       "hpicfHAMgmtRedundancyFailureReason": hpicfHAMgmtRedundancyFailureReason,
       "hpicfHAMgmtFailovers": hpicfHAMgmtFailovers,
       "hpicfHALastFailoverTime": hpicfHALastFailoverTime,
       "hpicfHAFailOverLogTable": hpicfHAFailOverLogTable,
       "hpicfHAFailOverLogEntry": hpicfHAFailOverLogEntry,
       "hpicfHAFailOverIndex": hpicfHAFailOverIndex,
       "hpicfHAFailOverMgmtModule": hpicfHAFailOverMgmtModule,
       "hpicfHAFailOverState": hpicfHAFailOverState,
       "hpicfHAFailOverTime": hpicfHAFailOverTime,
       "hpicfHAFailOverReason": hpicfHAFailOverReason,
       "hpicfHAMgmtModuleTable": hpicfHAMgmtModuleTable,
       "hpicfHAMgmtModuleEntry": hpicfHAMgmtModuleEntry,
       "hpicfHAMgmtModuleState": hpicfHAMgmtModuleState,
       "hpicfHAMgmtModuleCardUpSince": hpicfHAMgmtModuleCardUpSince,
       "hpicfHAMgmtModuleStateSince": hpicfHAMgmtModuleStateSince,
       "hpicfHAMgmtModuleRedundancyState": hpicfHAMgmtModuleRedundancyState,
       "hpicfHAMgmtModuleBackUpState": hpicfHAMgmtModuleBackUpState,
       "hpicfHAConformance": hpicfHAConformance,
       "hpicfHACompliances": hpicfHACompliances,
       "hpicfHACompliance": hpicfHACompliance,
       "hpicfHACompliance1": hpicfHACompliance1,
       "hpicfHACompliance2": hpicfHACompliance2,
       "hpicfHACompliance3": hpicfHACompliance3,
       "hpicfHAGroups": hpicfHAGroups,
       "hpicfHAConfigGroup": hpicfHAConfigGroup,
       "hpicfHAStatusGroup": hpicfHAStatusGroup,
       "hpicfHAFailOverGroup": hpicfHAFailOverGroup,
       "hpicfHAMgmtModuleGroup": hpicfHAMgmtModuleGroup,
       "hpicfHAMgmtModuleGroup1": hpicfHAMgmtModuleGroup1,
       "hpicfHAConfigGroup1": hpicfHAConfigGroup1}
)
