# SNMP MIB module (CISCO-APPLICATION-ACCELERATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-APPLICATION-ACCELERATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:38 2024
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

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoApplicationAccelerationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 594)
)
ciscoApplicationAccelerationMIB.setRevisions(
        ("2006-10-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CaaState(Integer32, TextualConvention):
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
        *(("active", 1),
          ("down", 3),
          ("impaired", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CaaMIBNotifications_ObjectIdentity = ObjectIdentity
caaMIBNotifications = _CaaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 0)
)
_CaaMIBObjects_ObjectIdentity = ObjectIdentity
caaMIBObjects = _CaaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1)
)
_CaaStats_ObjectIdentity = ObjectIdentity
caaStats = _CaaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1)
)
_CaaStatTable_Object = MibTable
caaStatTable = _CaaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caaStatTable.setStatus("current")
_CaaStatEntry_Object = MibTableRow
caaStatEntry = _CaaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1)
)
caaStatEntry.setIndexNames(
    (0, "CISCO-APPLICATION-ACCELERATION-MIB", "caaPort"),
)
if mibBuilder.loadTexts:
    caaStatEntry.setStatus("current")


class _CaaPort_Type(InetPortNumber):
    """Custom type caaPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaaPort_Type.__name__ = "InetPortNumber"
_CaaPort_Object = MibTableColumn
caaPort = _CaaPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 1),
    _CaaPort_Type()
)
caaPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caaPort.setStatus("current")
_CaaState_Type = CaaState
_CaaState_Object = MibTableColumn
caaState = _CaaState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 2),
    _CaaState_Type()
)
caaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaState.setStatus("current")
_CaaRequests_Type = Counter32
_CaaRequests_Object = MibTableColumn
caaRequests = _CaaRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 3),
    _CaaRequests_Type()
)
caaRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaRequests.setStatus("current")
if mibBuilder.loadTexts:
    caaRequests.setUnits("requests")
_CaaNoncondensableRequests_Type = Counter32
_CaaNoncondensableRequests_Object = MibTableColumn
caaNoncondensableRequests = _CaaNoncondensableRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 4),
    _CaaNoncondensableRequests_Type()
)
caaNoncondensableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaNoncondensableRequests.setStatus("current")
if mibBuilder.loadTexts:
    caaNoncondensableRequests.setUnits("requests")
_CaaRequestedObjectSize_Type = Counter32
_CaaRequestedObjectSize_Object = MibTableColumn
caaRequestedObjectSize = _CaaRequestedObjectSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 5),
    _CaaRequestedObjectSize_Type()
)
caaRequestedObjectSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaRequestedObjectSize.setStatus("current")
if mibBuilder.loadTexts:
    caaRequestedObjectSize.setUnits("bytes")
_CaaFinalResponseSize_Type = Counter32
_CaaFinalResponseSize_Object = MibTableColumn
caaFinalResponseSize = _CaaFinalResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 6),
    _CaaFinalResponseSize_Type()
)
caaFinalResponseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaFinalResponseSize.setStatus("current")
if mibBuilder.loadTexts:
    caaFinalResponseSize.setUnits("bytes")
_CaaLastRestartedTime_Type = DateAndTime
_CaaLastRestartedTime_Object = MibTableColumn
caaLastRestartedTime = _CaaLastRestartedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 7),
    _CaaLastRestartedTime_Type()
)
caaLastRestartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaLastRestartedTime.setStatus("current")
_CaaTransformed_Type = Counter32
_CaaTransformed_Object = MibTableColumn
caaTransformed = _CaaTransformed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 8),
    _CaaTransformed_Type()
)
caaTransformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaTransformed.setStatus("current")
if mibBuilder.loadTexts:
    caaTransformed.setUnits("transformations")
_CaaUntransformed_Type = Counter32
_CaaUntransformed_Object = MibTableColumn
caaUntransformed = _CaaUntransformed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 9),
    _CaaUntransformed_Type()
)
caaUntransformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaUntransformed.setStatus("current")
if mibBuilder.loadTexts:
    caaUntransformed.setUnits("transformations")
_CaaTransformedObjectRequests_Type = Counter32
_CaaTransformedObjectRequests_Object = MibTableColumn
caaTransformedObjectRequests = _CaaTransformedObjectRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 10),
    _CaaTransformedObjectRequests_Type()
)
caaTransformedObjectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaTransformedObjectRequests.setStatus("current")
if mibBuilder.loadTexts:
    caaTransformedObjectRequests.setUnits("requests")
_CaaTransformedObjectIMSRequests_Type = Counter32
_CaaTransformedObjectIMSRequests_Object = MibTableColumn
caaTransformedObjectIMSRequests = _CaaTransformedObjectIMSRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 11),
    _CaaTransformedObjectIMSRequests_Type()
)
caaTransformedObjectIMSRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaTransformedObjectIMSRequests.setStatus("current")
if mibBuilder.loadTexts:
    caaTransformedObjectIMSRequests.setUnits("requests")
_CaaStaticObjectHits_Type = Counter32
_CaaStaticObjectHits_Object = MibTableColumn
caaStaticObjectHits = _CaaStaticObjectHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 12),
    _CaaStaticObjectHits_Type()
)
caaStaticObjectHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaStaticObjectHits.setStatus("current")
if mibBuilder.loadTexts:
    caaStaticObjectHits.setUnits("cache-hits")
_CaaStaticObjectHitSize_Type = Counter32
_CaaStaticObjectHitSize_Object = MibTableColumn
caaStaticObjectHitSize = _CaaStaticObjectHitSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 13),
    _CaaStaticObjectHitSize_Type()
)
caaStaticObjectHitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaStaticObjectHitSize.setStatus("current")
if mibBuilder.loadTexts:
    caaStaticObjectHitSize.setUnits("bytes")
_CaaStaticObjectMisses_Type = Counter32
_CaaStaticObjectMisses_Object = MibTableColumn
caaStaticObjectMisses = _CaaStaticObjectMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 14),
    _CaaStaticObjectMisses_Type()
)
caaStaticObjectMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaStaticObjectMisses.setStatus("current")
if mibBuilder.loadTexts:
    caaStaticObjectMisses.setUnits("cache-misses")
_CaaStaticObjectMissSize_Type = Counter32
_CaaStaticObjectMissSize_Object = MibTableColumn
caaStaticObjectMissSize = _CaaStaticObjectMissSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 15),
    _CaaStaticObjectMissSize_Type()
)
caaStaticObjectMissSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaStaticObjectMissSize.setStatus("current")
if mibBuilder.loadTexts:
    caaStaticObjectMissSize.setUnits("bytes")
_CaaRefreshHits_Type = Counter32
_CaaRefreshHits_Object = MibTableColumn
caaRefreshHits = _CaaRefreshHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 16),
    _CaaRefreshHits_Type()
)
caaRefreshHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaRefreshHits.setStatus("current")
if mibBuilder.loadTexts:
    caaRefreshHits.setUnits("requests")
_CaaIMSHits_Type = Counter32
_CaaIMSHits_Object = MibTableColumn
caaIMSHits = _CaaIMSHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 17),
    _CaaIMSHits_Type()
)
caaIMSHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaIMSHits.setStatus("current")
if mibBuilder.loadTexts:
    caaIMSHits.setUnits("requests")
_CaaIMSMisses_Type = Counter32
_CaaIMSMisses_Object = MibTableColumn
caaIMSMisses = _CaaIMSMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 18),
    _CaaIMSMisses_Type()
)
caaIMSMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaIMSMisses.setStatus("current")
if mibBuilder.loadTexts:
    caaIMSMisses.setUnits("requests")
_CaaDirectRequests_Type = Counter32
_CaaDirectRequests_Object = MibTableColumn
caaDirectRequests = _CaaDirectRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 19),
    _CaaDirectRequests_Type()
)
caaDirectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaDirectRequests.setStatus("current")
if mibBuilder.loadTexts:
    caaDirectRequests.setUnits("requests")
_CaaRequestSize_Type = Counter32
_CaaRequestSize_Object = MibTableColumn
caaRequestSize = _CaaRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 20),
    _CaaRequestSize_Type()
)
caaRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaRequestSize.setStatus("current")
if mibBuilder.loadTexts:
    caaRequestSize.setUnits("bytes")
_CaaDeltaAbandons_Type = Counter32
_CaaDeltaAbandons_Object = MibTableColumn
caaDeltaAbandons = _CaaDeltaAbandons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 21),
    _CaaDeltaAbandons_Type()
)
caaDeltaAbandons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caaDeltaAbandons.setStatus("current")
if mibBuilder.loadTexts:
    caaDeltaAbandons.setUnits("requests")
_CaaNotificationObjects_ObjectIdentity = ObjectIdentity
caaNotificationObjects = _CaaNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 2)
)


class _CaaStateChangeNotifEnabled_Type(TruthValue):
    """Custom type caaStateChangeNotifEnabled based on TruthValue"""


_CaaStateChangeNotifEnabled_Object = MibScalar
caaStateChangeNotifEnabled = _CaaStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 2, 1),
    _CaaStateChangeNotifEnabled_Type()
)
caaStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caaStateChangeNotifEnabled.setStatus("current")
_CaaMIBConformance_ObjectIdentity = ObjectIdentity
caaMIBConformance = _CaaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 2)
)
_CaaMIBCompliances_ObjectIdentity = ObjectIdentity
caaMIBCompliances = _CaaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 1)
)
_CaaMIBGroups_ObjectIdentity = ObjectIdentity
caaMIBGroups = _CaaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 2)
)

# Managed Objects groups

caaMIBStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 2, 1)
)
caaMIBStatsGroup.setObjects(
      *(("CISCO-APPLICATION-ACCELERATION-MIB", "caaState"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaRequests"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaNoncondensableRequests"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaRequestedObjectSize"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaFinalResponseSize"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaLastRestartedTime"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaTransformed"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaUntransformed"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaTransformedObjectRequests"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaTransformedObjectIMSRequests"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStaticObjectHits"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStaticObjectHitSize"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStaticObjectMisses"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStaticObjectMissSize"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaRefreshHits"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaIMSHits"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaIMSMisses"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaDirectRequests"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaRequestSize"),
        ("CISCO-APPLICATION-ACCELERATION-MIB", "caaDeltaAbandons"))
)
if mibBuilder.loadTexts:
    caaMIBStatsGroup.setStatus("current")

caaMIBNotifObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 2, 3)
)
caaMIBNotifObjectGroup.setObjects(
    ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStateChangeNotifEnabled")
)
if mibBuilder.loadTexts:
    caaMIBNotifObjectGroup.setStatus("current")


# Notification objects

caaStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 0, 1)
)
caaStateChange.setObjects(
    ("CISCO-APPLICATION-ACCELERATION-MIB", "caaState")
)
if mibBuilder.loadTexts:
    caaStateChange.setStatus(
        "current"
    )


# Notifications groups

caaMIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 2, 2)
)
caaMIBNotificationsGroup.setObjects(
    ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStateChange")
)
if mibBuilder.loadTexts:
    caaMIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

caaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 1, 1)
)
if mibBuilder.loadTexts:
    caaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-APPLICATION-ACCELERATION-MIB",
    **{"CaaState": CaaState,
       "ciscoApplicationAccelerationMIB": ciscoApplicationAccelerationMIB,
       "caaMIBNotifications": caaMIBNotifications,
       "caaStateChange": caaStateChange,
       "caaMIBObjects": caaMIBObjects,
       "caaStats": caaStats,
       "caaStatTable": caaStatTable,
       "caaStatEntry": caaStatEntry,
       "caaPort": caaPort,
       "caaState": caaState,
       "caaRequests": caaRequests,
       "caaNoncondensableRequests": caaNoncondensableRequests,
       "caaRequestedObjectSize": caaRequestedObjectSize,
       "caaFinalResponseSize": caaFinalResponseSize,
       "caaLastRestartedTime": caaLastRestartedTime,
       "caaTransformed": caaTransformed,
       "caaUntransformed": caaUntransformed,
       "caaTransformedObjectRequests": caaTransformedObjectRequests,
       "caaTransformedObjectIMSRequests": caaTransformedObjectIMSRequests,
       "caaStaticObjectHits": caaStaticObjectHits,
       "caaStaticObjectHitSize": caaStaticObjectHitSize,
       "caaStaticObjectMisses": caaStaticObjectMisses,
       "caaStaticObjectMissSize": caaStaticObjectMissSize,
       "caaRefreshHits": caaRefreshHits,
       "caaIMSHits": caaIMSHits,
       "caaIMSMisses": caaIMSMisses,
       "caaDirectRequests": caaDirectRequests,
       "caaRequestSize": caaRequestSize,
       "caaDeltaAbandons": caaDeltaAbandons,
       "caaNotificationObjects": caaNotificationObjects,
       "caaStateChangeNotifEnabled": caaStateChangeNotifEnabled,
       "caaMIBConformance": caaMIBConformance,
       "caaMIBCompliances": caaMIBCompliances,
       "caaMIBCompliance": caaMIBCompliance,
       "caaMIBGroups": caaMIBGroups,
       "caaMIBStatsGroup": caaMIBStatsGroup,
       "caaMIBNotificationsGroup": caaMIBNotificationsGroup,
       "caaMIBNotifObjectGroup": caaMIBNotifObjectGroup}
)
