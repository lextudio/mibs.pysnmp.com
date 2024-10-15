# SNMP MIB module (FORCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:29 2024
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

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

forcesMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 187)
)
forcesMib.setRevisions(
        ("2010-03-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ForcesID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class ForcesProtocolVersion(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_ForcesMibNotifications_ObjectIdentity = ObjectIdentity
forcesMibNotifications = _ForcesMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 187, 0)
)
_ForcesMibObjects_ObjectIdentity = ObjectIdentity
forcesMibObjects = _ForcesMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 187, 1)
)
_ForcesLatestProtocolVersionSupported_Type = ForcesProtocolVersion
_ForcesLatestProtocolVersionSupported_Object = MibScalar
forcesLatestProtocolVersionSupported = _ForcesLatestProtocolVersionSupported_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 1),
    _ForcesLatestProtocolVersionSupported_Type()
)
forcesLatestProtocolVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forcesLatestProtocolVersionSupported.setStatus("current")
_ForcesAssociations_ObjectIdentity = ObjectIdentity
forcesAssociations = _ForcesAssociations_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 187, 1, 2)
)
_ForcesAssociationTable_Object = MibTable
forcesAssociationTable = _ForcesAssociationTable_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1)
)
if mibBuilder.loadTexts:
    forcesAssociationTable.setStatus("current")
_ForcesAssociationEntry_Object = MibTableRow
forcesAssociationEntry = _ForcesAssociationEntry_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1)
)
forcesAssociationEntry.setIndexNames(
    (0, "FORCES-MIB", "forcesAssociationCEID"),
    (0, "FORCES-MIB", "forcesAssociationFEID"),
)
if mibBuilder.loadTexts:
    forcesAssociationEntry.setStatus("current")
_ForcesAssociationCEID_Type = ForcesID
_ForcesAssociationCEID_Object = MibTableColumn
forcesAssociationCEID = _ForcesAssociationCEID_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 1),
    _ForcesAssociationCEID_Type()
)
forcesAssociationCEID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    forcesAssociationCEID.setStatus("current")
_ForcesAssociationFEID_Type = ForcesID
_ForcesAssociationFEID_Object = MibTableColumn
forcesAssociationFEID = _ForcesAssociationFEID_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 2),
    _ForcesAssociationFEID_Type()
)
forcesAssociationFEID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    forcesAssociationFEID.setStatus("current")
_ForcesAssociationRunningProtocolVersion_Type = ForcesProtocolVersion
_ForcesAssociationRunningProtocolVersion_Object = MibTableColumn
forcesAssociationRunningProtocolVersion = _ForcesAssociationRunningProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 3),
    _ForcesAssociationRunningProtocolVersion_Type()
)
forcesAssociationRunningProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forcesAssociationRunningProtocolVersion.setStatus("current")
_ForcesAssociationTimeUp_Type = TimeStamp
_ForcesAssociationTimeUp_Object = MibTableColumn
forcesAssociationTimeUp = _ForcesAssociationTimeUp_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 4),
    _ForcesAssociationTimeUp_Type()
)
forcesAssociationTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forcesAssociationTimeUp.setStatus("current")
_ForcesAssociationTimeDown_Type = TimeStamp
_ForcesAssociationTimeDown_Object = MibTableColumn
forcesAssociationTimeDown = _ForcesAssociationTimeDown_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 5),
    _ForcesAssociationTimeDown_Type()
)
forcesAssociationTimeDown.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    forcesAssociationTimeDown.setStatus("current")
_ForcesAssociationHBMsgSent_Type = ZeroBasedCounter32
_ForcesAssociationHBMsgSent_Object = MibTableColumn
forcesAssociationHBMsgSent = _ForcesAssociationHBMsgSent_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 6),
    _ForcesAssociationHBMsgSent_Type()
)
forcesAssociationHBMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forcesAssociationHBMsgSent.setStatus("current")
_ForcesAssociationHBMsgReceived_Type = ZeroBasedCounter32
_ForcesAssociationHBMsgReceived_Object = MibTableColumn
forcesAssociationHBMsgReceived = _ForcesAssociationHBMsgReceived_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 7),
    _ForcesAssociationHBMsgReceived_Type()
)
forcesAssociationHBMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forcesAssociationHBMsgReceived.setStatus("current")
_ForcesAssociationOperMsgSent_Type = ZeroBasedCounter32
_ForcesAssociationOperMsgSent_Object = MibTableColumn
forcesAssociationOperMsgSent = _ForcesAssociationOperMsgSent_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 8),
    _ForcesAssociationOperMsgSent_Type()
)
forcesAssociationOperMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forcesAssociationOperMsgSent.setStatus("current")
_ForcesAssociationOperMsgReceived_Type = ZeroBasedCounter32
_ForcesAssociationOperMsgReceived_Object = MibTableColumn
forcesAssociationOperMsgReceived = _ForcesAssociationOperMsgReceived_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 9),
    _ForcesAssociationOperMsgReceived_Type()
)
forcesAssociationOperMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forcesAssociationOperMsgReceived.setStatus("current")
_ForcesAssociationCounterDiscontinuityTime_Type = TimeStamp
_ForcesAssociationCounterDiscontinuityTime_Object = MibTableColumn
forcesAssociationCounterDiscontinuityTime = _ForcesAssociationCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 187, 1, 2, 1, 1, 10),
    _ForcesAssociationCounterDiscontinuityTime_Type()
)
forcesAssociationCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forcesAssociationCounterDiscontinuityTime.setStatus("current")
_ForcesMibConformance_ObjectIdentity = ObjectIdentity
forcesMibConformance = _ForcesMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 187, 2)
)
_ForcesMibCompliances_ObjectIdentity = ObjectIdentity
forcesMibCompliances = _ForcesMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 187, 2, 1)
)
_ForcesMibGroups_ObjectIdentity = ObjectIdentity
forcesMibGroups = _ForcesMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 187, 2, 2)
)

# Managed Objects groups

forcesMibGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 187, 2, 2, 2)
)
forcesMibGroup.setObjects(
      *(("FORCES-MIB", "forcesLatestProtocolVersionSupported"),
        ("FORCES-MIB", "forcesAssociationRunningProtocolVersion"))
)
if mibBuilder.loadTexts:
    forcesMibGroup.setStatus("current")

forcesStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 187, 2, 2, 4)
)
forcesStatsGroup.setObjects(
      *(("FORCES-MIB", "forcesAssociationTimeUp"),
        ("FORCES-MIB", "forcesAssociationTimeDown"),
        ("FORCES-MIB", "forcesAssociationHBMsgSent"),
        ("FORCES-MIB", "forcesAssociationHBMsgReceived"),
        ("FORCES-MIB", "forcesAssociationOperMsgSent"),
        ("FORCES-MIB", "forcesAssociationOperMsgReceived"),
        ("FORCES-MIB", "forcesAssociationCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    forcesStatsGroup.setStatus("current")


# Notification objects

forcesAssociationEntryUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 187, 0, 1)
)
forcesAssociationEntryUp.setObjects(
    ("FORCES-MIB", "forcesAssociationRunningProtocolVersion")
)
if mibBuilder.loadTexts:
    forcesAssociationEntryUp.setStatus(
        "current"
    )

forcesAssociationEntryDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 187, 0, 2)
)
forcesAssociationEntryDown.setObjects(
    ("FORCES-MIB", "forcesAssociationRunningProtocolVersion")
)
if mibBuilder.loadTexts:
    forcesAssociationEntryDown.setStatus(
        "current"
    )

forcesAssociationEntryUpStats = NotificationType(
    (1, 3, 6, 1, 2, 1, 187, 0, 3)
)
forcesAssociationEntryUpStats.setObjects(
      *(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"),
        ("FORCES-MIB", "forcesAssociationTimeUp"))
)
if mibBuilder.loadTexts:
    forcesAssociationEntryUpStats.setStatus(
        "current"
    )

forcesAssociationEntryDownStats = NotificationType(
    (1, 3, 6, 1, 2, 1, 187, 0, 4)
)
forcesAssociationEntryDownStats.setObjects(
      *(("FORCES-MIB", "forcesAssociationRunningProtocolVersion"),
        ("FORCES-MIB", "forcesAssociationTimeUp"),
        ("FORCES-MIB", "forcesAssociationTimeDown"),
        ("FORCES-MIB", "forcesAssociationHBMsgSent"),
        ("FORCES-MIB", "forcesAssociationHBMsgReceived"),
        ("FORCES-MIB", "forcesAssociationOperMsgSent"),
        ("FORCES-MIB", "forcesAssociationOperMsgReceived"),
        ("FORCES-MIB", "forcesAssociationCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    forcesAssociationEntryDownStats.setStatus(
        "current"
    )


# Notifications groups

forcesNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 187, 2, 2, 1)
)
forcesNotificationGroup.setObjects(
      *(("FORCES-MIB", "forcesAssociationEntryUp"),
        ("FORCES-MIB", "forcesAssociationEntryDown"))
)
if mibBuilder.loadTexts:
    forcesNotificationGroup.setStatus(
        "current"
    )

forcesNotificationStatsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 187, 2, 2, 3)
)
forcesNotificationStatsGroup.setObjects(
      *(("FORCES-MIB", "forcesAssociationEntryUpStats"),
        ("FORCES-MIB", "forcesAssociationEntryDownStats"))
)
if mibBuilder.loadTexts:
    forcesNotificationStatsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

forcesMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 187, 2, 1, 1)
)
if mibBuilder.loadTexts:
    forcesMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCES-MIB",
    **{"ForcesID": ForcesID,
       "ForcesProtocolVersion": ForcesProtocolVersion,
       "forcesMib": forcesMib,
       "forcesMibNotifications": forcesMibNotifications,
       "forcesAssociationEntryUp": forcesAssociationEntryUp,
       "forcesAssociationEntryDown": forcesAssociationEntryDown,
       "forcesAssociationEntryUpStats": forcesAssociationEntryUpStats,
       "forcesAssociationEntryDownStats": forcesAssociationEntryDownStats,
       "forcesMibObjects": forcesMibObjects,
       "forcesLatestProtocolVersionSupported": forcesLatestProtocolVersionSupported,
       "forcesAssociations": forcesAssociations,
       "forcesAssociationTable": forcesAssociationTable,
       "forcesAssociationEntry": forcesAssociationEntry,
       "forcesAssociationCEID": forcesAssociationCEID,
       "forcesAssociationFEID": forcesAssociationFEID,
       "forcesAssociationRunningProtocolVersion": forcesAssociationRunningProtocolVersion,
       "forcesAssociationTimeUp": forcesAssociationTimeUp,
       "forcesAssociationTimeDown": forcesAssociationTimeDown,
       "forcesAssociationHBMsgSent": forcesAssociationHBMsgSent,
       "forcesAssociationHBMsgReceived": forcesAssociationHBMsgReceived,
       "forcesAssociationOperMsgSent": forcesAssociationOperMsgSent,
       "forcesAssociationOperMsgReceived": forcesAssociationOperMsgReceived,
       "forcesAssociationCounterDiscontinuityTime": forcesAssociationCounterDiscontinuityTime,
       "forcesMibConformance": forcesMibConformance,
       "forcesMibCompliances": forcesMibCompliances,
       "forcesMibCompliance": forcesMibCompliance,
       "forcesMibGroups": forcesMibGroups,
       "forcesNotificationGroup": forcesNotificationGroup,
       "forcesMibGroup": forcesMibGroup,
       "forcesNotificationStatsGroup": forcesNotificationStatsGroup,
       "forcesStatsGroup": forcesStatsGroup}
)
