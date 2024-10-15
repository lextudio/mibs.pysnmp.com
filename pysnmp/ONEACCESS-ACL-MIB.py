# SNMP MIB module (ONEACCESS-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:46 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(oacEventSeverityLevel,
 oacEventText) = mibBuilder.importSymbols(
    "ONEACCESS-EVENTS-MIB",
    "oacEventSeverityLevel",
    "oacEventText")

(oacExpIMIpAcl,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIpAcl",
    "oacMIBModules")

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

oacAclMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 669)
)
oacAclMIBModule.setRevisions(
        ("2011-06-15 00:00",
         "2010-07-08 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mainInterface", 1),
          ("subInterface", 2))
    )



# MIB Managed Objects in the order of their OIDs

_OacExpIMIpAclStatistics_ObjectIdentity = ObjectIdentity
oacExpIMIpAclStatistics = _OacExpIMIpAclStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1)
)
_OacAclStatObjects_ObjectIdentity = ObjectIdentity
oacAclStatObjects = _OacAclStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1)
)
_OacAclStatGlobal_ObjectIdentity = ObjectIdentity
oacAclStatGlobal = _OacAclStatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1)
)
_OacAclMaxSessions_Type = Unsigned32
_OacAclMaxSessions_Object = MibScalar
oacAclMaxSessions = _OacAclMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 1),
    _OacAclMaxSessions_Type()
)
oacAclMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAclMaxSessions.setStatus("current")
_OacAclActiveSessions_Type = Unsigned32
_OacAclActiveSessions_Object = MibScalar
oacAclActiveSessions = _OacAclActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 2),
    _OacAclActiveSessions_Type()
)
oacAclActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAclActiveSessions.setStatus("current")
_OacAclSessionsClosed_Type = Counter32
_OacAclSessionsClosed_Object = MibScalar
oacAclSessionsClosed = _OacAclSessionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 3),
    _OacAclSessionsClosed_Type()
)
oacAclSessionsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAclSessionsClosed.setStatus("current")
_OacAclDynamicAllocFailures_Type = Counter32
_OacAclDynamicAllocFailures_Object = MibScalar
oacAclDynamicAllocFailures = _OacAclDynamicAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 4),
    _OacAclDynamicAllocFailures_Type()
)
oacAclDynamicAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAclDynamicAllocFailures.setStatus("current")
_OacAclInboundPkts_Type = Counter32
_OacAclInboundPkts_Object = MibScalar
oacAclInboundPkts = _OacAclInboundPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 5),
    _OacAclInboundPkts_Type()
)
oacAclInboundPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAclInboundPkts.setStatus("current")
_OacAclOutboundPkts_Type = Counter32
_OacAclOutboundPkts_Object = MibScalar
oacAclOutboundPkts = _OacAclOutboundPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 6),
    _OacAclOutboundPkts_Type()
)
oacAclOutboundPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAclOutboundPkts.setStatus("current")
_OacAclInboundPktsDropped_Type = Counter32
_OacAclInboundPktsDropped_Object = MibScalar
oacAclInboundPktsDropped = _OacAclInboundPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 7),
    _OacAclInboundPktsDropped_Type()
)
oacAclInboundPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAclInboundPktsDropped.setStatus("current")
_OacAclOutboundPktsDropped_Type = Counter32
_OacAclOutboundPktsDropped_Object = MibScalar
oacAclOutboundPktsDropped = _OacAclOutboundPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 8),
    _OacAclOutboundPktsDropped_Type()
)
oacAclOutboundPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAclOutboundPktsDropped.setStatus("current")
_OacAclStatNotifications_ObjectIdentity = ObjectIdentity
oacAclStatNotifications = _OacAclStatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 2)
)
_OacAclStatConformance_ObjectIdentity = ObjectIdentity
oacAclStatConformance = _OacAclStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3)
)
_OacAclStatGroups_ObjectIdentity = ObjectIdentity
oacAclStatGroups = _OacAclStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3, 1)
)
_OacAclStatCompliances_ObjectIdentity = ObjectIdentity
oacAclStatCompliances = _OacAclStatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3, 2)
)
_OacExpIMIpAclNotifications_ObjectIdentity = ObjectIdentity
oacExpIMIpAclNotifications = _OacExpIMIpAclNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2)
)
_OacExpIMIpAccountingStatistics_ObjectIdentity = ObjectIdentity
oacExpIMIpAccountingStatistics = _OacExpIMIpAccountingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3)
)
_OacIpAccountingTable_Object = MibTable
oacIpAccountingTable = _OacIpAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    oacIpAccountingTable.setStatus("current")
_OacIpAccountingEntry_Object = MibTableRow
oacIpAccountingEntry = _OacIpAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1, 1)
)
oacIpAccountingEntry.setIndexNames(
    (0, "ONEACCESS-ACL-MIB", "oacIpAccountingIndex"),
)
if mibBuilder.loadTexts:
    oacIpAccountingEntry.setStatus("current")
_OacIpAccountingIndex_Type = Gauge32
_OacIpAccountingIndex_Object = MibTableColumn
oacIpAccountingIndex = _OacIpAccountingIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1, 1, 1),
    _OacIpAccountingIndex_Type()
)
oacIpAccountingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingIndex.setStatus("current")
_OacIpAccountingIfIndex_Type = InterfaceIndex
_OacIpAccountingIfIndex_Object = MibTableColumn
oacIpAccountingIfIndex = _OacIpAccountingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1, 1, 2),
    _OacIpAccountingIfIndex_Type()
)
oacIpAccountingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingIfIndex.setStatus("current")
_OacIpAccountingIfType_Type = InterfaceType
_OacIpAccountingIfType_Object = MibTableColumn
oacIpAccountingIfType = _OacIpAccountingIfType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1, 1, 3),
    _OacIpAccountingIfType_Type()
)
oacIpAccountingIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingIfType.setStatus("current")
_OacIpAccountingStatTable_Object = MibTable
oacIpAccountingStatTable = _OacIpAccountingStatTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    oacIpAccountingStatTable.setStatus("current")
_OacIpAccountingStatEntry_Object = MibTableRow
oacIpAccountingStatEntry = _OacIpAccountingStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1)
)
oacIpAccountingStatEntry.setIndexNames(
    (0, "ONEACCESS-ACL-MIB", "oacIpAccountingIndex"),
)
if mibBuilder.loadTexts:
    oacIpAccountingStatEntry.setStatus("current")
_OacIpAccountingStatIpSource_Type = IpAddress
_OacIpAccountingStatIpSource_Object = MibTableColumn
oacIpAccountingStatIpSource = _OacIpAccountingStatIpSource_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1, 1),
    _OacIpAccountingStatIpSource_Type()
)
oacIpAccountingStatIpSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingStatIpSource.setStatus("current")
_OacIpAccountingStatIpDest_Type = IpAddress
_OacIpAccountingStatIpDest_Object = MibTableColumn
oacIpAccountingStatIpDest = _OacIpAccountingStatIpDest_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1, 2),
    _OacIpAccountingStatIpDest_Type()
)
oacIpAccountingStatIpDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingStatIpDest.setStatus("current")
_OacIpAccountingStatNbPackets_Type = Counter32
_OacIpAccountingStatNbPackets_Object = MibTableColumn
oacIpAccountingStatNbPackets = _OacIpAccountingStatNbPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1, 3),
    _OacIpAccountingStatNbPackets_Type()
)
oacIpAccountingStatNbPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingStatNbPackets.setStatus("current")
_OacIpAccountingStatNbBytes_Type = Counter32
_OacIpAccountingStatNbBytes_Object = MibTableColumn
oacIpAccountingStatNbBytes = _OacIpAccountingStatNbBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1, 4),
    _OacIpAccountingStatNbBytes_Type()
)
oacIpAccountingStatNbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingStatNbBytes.setStatus("current")
_OacIpAccoutingGlobal_ObjectIdentity = ObjectIdentity
oacIpAccoutingGlobal = _OacIpAccoutingGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3)
)
_OacIpAccountingMaxSessions_Type = Gauge32
_OacIpAccountingMaxSessions_Object = MibScalar
oacIpAccountingMaxSessions = _OacIpAccountingMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 1),
    _OacIpAccountingMaxSessions_Type()
)
oacIpAccountingMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingMaxSessions.setStatus("current")
_OacIpAccountingCurrentSessions_Type = Gauge32
_OacIpAccountingCurrentSessions_Object = MibScalar
oacIpAccountingCurrentSessions = _OacIpAccountingCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 2),
    _OacIpAccountingCurrentSessions_Type()
)
oacIpAccountingCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingCurrentSessions.setStatus("current")
_OacIpAccountingAge_Type = DisplayString
_OacIpAccountingAge_Object = MibScalar
oacIpAccountingAge = _OacIpAccountingAge_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 3),
    _OacIpAccountingAge_Type()
)
oacIpAccountingAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingAge.setStatus("current")
_OacIpAccountingNbNotAnalysedBytes_Type = Gauge32
_OacIpAccountingNbNotAnalysedBytes_Object = MibScalar
oacIpAccountingNbNotAnalysedBytes = _OacIpAccountingNbNotAnalysedBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 4),
    _OacIpAccountingNbNotAnalysedBytes_Type()
)
oacIpAccountingNbNotAnalysedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingNbNotAnalysedBytes.setStatus("current")
_OacIpAccountingNbNotAnalysedPackets_Type = Gauge32
_OacIpAccountingNbNotAnalysedPackets_Object = MibScalar
oacIpAccountingNbNotAnalysedPackets = _OacIpAccountingNbNotAnalysedPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 5),
    _OacIpAccountingNbNotAnalysedPackets_Type()
)
oacIpAccountingNbNotAnalysedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpAccountingNbNotAnalysedPackets.setStatus("current")


class _OacIpAccoutingClear_Type(Integer32):
    """Custom type oacIpAccoutingClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_OacIpAccoutingClear_Type.__name__ = "Integer32"
_OacIpAccoutingClear_Object = MibScalar
oacIpAccoutingClear = _OacIpAccoutingClear_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 10),
    _OacIpAccoutingClear_Type()
)
oacIpAccoutingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacIpAccoutingClear.setStatus("current")

# Managed Objects groups

oacAclStatGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3, 1, 1)
)
oacAclStatGeneralGroup.setObjects(
      *(("ONEACCESS-ACL-MIB", "oacAclMaxSessions"),
        ("ONEACCESS-ACL-MIB", "oacAclActiveSessions"),
        ("ONEACCESS-ACL-MIB", "oacAclSessionsClosed"),
        ("ONEACCESS-ACL-MIB", "oacAclDynamicAllocFailures"),
        ("ONEACCESS-ACL-MIB", "oacAclInboundPkts"),
        ("ONEACCESS-ACL-MIB", "oacAclOutboundPkts"),
        ("ONEACCESS-ACL-MIB", "oacAclInboundPktsDropped"),
        ("ONEACCESS-ACL-MIB", "oacAclOutboundPktsDropped"))
)
if mibBuilder.loadTexts:
    oacAclStatGeneralGroup.setStatus("current")


# Notification objects

oacAclNotificationMaximumSessionReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oacAclNotificationMaximumSessionReached.setStatus(
        "current"
    )

oacAclNotificationWarningSessionReachingLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    oacAclNotificationWarningSessionReachingLimit.setStatus(
        "current"
    )

oacAclNotificationMaximumHalfSessionReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    oacAclNotificationMaximumHalfSessionReached.setStatus(
        "current"
    )

oacAclNotificationWarningHalfSessionReachingLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    oacAclNotificationWarningHalfSessionReachingLimit.setStatus(
        "current"
    )

oacAclNotificationMaximumSessionReachedPerHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 5)
)
oacAclNotificationMaximumSessionReachedPerHost.setObjects(
      *(("ONEACCESS-EVENTS-MIB", "oacEventText"),
        ("ONEACCESS-EVENTS-MIB", "oacEventSeverityLevel"))
)
if mibBuilder.loadTexts:
    oacAclNotificationMaximumSessionReachedPerHost.setStatus(
        "current"
    )

oacAclNotificationMaximumHalfSessionReachedPerHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    oacAclNotificationMaximumHalfSessionReachedPerHost.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

oacAclStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    oacAclStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-ACL-MIB",
    **{"InterfaceType": InterfaceType,
       "oacAclMIBModule": oacAclMIBModule,
       "oacExpIMIpAclStatistics": oacExpIMIpAclStatistics,
       "oacAclStatObjects": oacAclStatObjects,
       "oacAclStatGlobal": oacAclStatGlobal,
       "oacAclMaxSessions": oacAclMaxSessions,
       "oacAclActiveSessions": oacAclActiveSessions,
       "oacAclSessionsClosed": oacAclSessionsClosed,
       "oacAclDynamicAllocFailures": oacAclDynamicAllocFailures,
       "oacAclInboundPkts": oacAclInboundPkts,
       "oacAclOutboundPkts": oacAclOutboundPkts,
       "oacAclInboundPktsDropped": oacAclInboundPktsDropped,
       "oacAclOutboundPktsDropped": oacAclOutboundPktsDropped,
       "oacAclStatNotifications": oacAclStatNotifications,
       "oacAclStatConformance": oacAclStatConformance,
       "oacAclStatGroups": oacAclStatGroups,
       "oacAclStatGeneralGroup": oacAclStatGeneralGroup,
       "oacAclStatCompliances": oacAclStatCompliances,
       "oacAclStatCompliance": oacAclStatCompliance,
       "oacExpIMIpAclNotifications": oacExpIMIpAclNotifications,
       "oacAclNotificationMaximumSessionReached": oacAclNotificationMaximumSessionReached,
       "oacAclNotificationWarningSessionReachingLimit": oacAclNotificationWarningSessionReachingLimit,
       "oacAclNotificationMaximumHalfSessionReached": oacAclNotificationMaximumHalfSessionReached,
       "oacAclNotificationWarningHalfSessionReachingLimit": oacAclNotificationWarningHalfSessionReachingLimit,
       "oacAclNotificationMaximumSessionReachedPerHost": oacAclNotificationMaximumSessionReachedPerHost,
       "oacAclNotificationMaximumHalfSessionReachedPerHost": oacAclNotificationMaximumHalfSessionReachedPerHost,
       "oacExpIMIpAccountingStatistics": oacExpIMIpAccountingStatistics,
       "oacIpAccountingTable": oacIpAccountingTable,
       "oacIpAccountingEntry": oacIpAccountingEntry,
       "oacIpAccountingIndex": oacIpAccountingIndex,
       "oacIpAccountingIfIndex": oacIpAccountingIfIndex,
       "oacIpAccountingIfType": oacIpAccountingIfType,
       "oacIpAccountingStatTable": oacIpAccountingStatTable,
       "oacIpAccountingStatEntry": oacIpAccountingStatEntry,
       "oacIpAccountingStatIpSource": oacIpAccountingStatIpSource,
       "oacIpAccountingStatIpDest": oacIpAccountingStatIpDest,
       "oacIpAccountingStatNbPackets": oacIpAccountingStatNbPackets,
       "oacIpAccountingStatNbBytes": oacIpAccountingStatNbBytes,
       "oacIpAccoutingGlobal": oacIpAccoutingGlobal,
       "oacIpAccountingMaxSessions": oacIpAccountingMaxSessions,
       "oacIpAccountingCurrentSessions": oacIpAccountingCurrentSessions,
       "oacIpAccountingAge": oacIpAccountingAge,
       "oacIpAccountingNbNotAnalysedBytes": oacIpAccountingNbNotAnalysedBytes,
       "oacIpAccountingNbNotAnalysedPackets": oacIpAccountingNbNotAnalysedPackets,
       "oacIpAccoutingClear": oacIpAccoutingClear}
)
