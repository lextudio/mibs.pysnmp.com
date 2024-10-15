# SNMP MIB module (ARISTA-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:26 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

aristaRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8)
)
aristaRedundancyMIB.setRevisions(
        ("2014-08-15 00:00",
         "2012-11-10 22:37")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaRedundancyState(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 2),
          ("disabled", 3),
          ("standby", 1),
          ("unknown", 0))
    )



class AristaRedundancyProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("rpr", 2),
          ("simplex", 1),
          ("sso", 3),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_AristaRedundancyObjects_ObjectIdentity = ObjectIdentity
aristaRedundancyObjects = _AristaRedundancyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0)
)
_AristaRedundancyStatus_ObjectIdentity = ObjectIdentity
aristaRedundancyStatus = _AristaRedundancyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0)
)
_AristaRedundancyProtocolConfig_Type = AristaRedundancyProtocol
_AristaRedundancyProtocolConfig_Object = MibScalar
aristaRedundancyProtocolConfig = _AristaRedundancyProtocolConfig_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 1),
    _AristaRedundancyProtocolConfig_Type()
)
aristaRedundancyProtocolConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaRedundancyProtocolConfig.setStatus("current")
_AristaRedundancyProtocolOper_Type = AristaRedundancyProtocol
_AristaRedundancyProtocolOper_Object = MibScalar
aristaRedundancyProtocolOper = _AristaRedundancyProtocolOper_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 2),
    _AristaRedundancyProtocolOper_Type()
)
aristaRedundancyProtocolOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaRedundancyProtocolOper.setStatus("current")
_AristaRedundancyUnitStateTable_Object = MibTable
aristaRedundancyUnitStateTable = _AristaRedundancyUnitStateTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3)
)
if mibBuilder.loadTexts:
    aristaRedundancyUnitStateTable.setStatus("current")
_AristaRedundancyUnitStateEntry_Object = MibTableRow
aristaRedundancyUnitStateEntry = _AristaRedundancyUnitStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1)
)
aristaRedundancyUnitStateEntry.setIndexNames(
    (0, "ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitId"),
)
if mibBuilder.loadTexts:
    aristaRedundancyUnitStateEntry.setStatus("current")
_AristaRedundancyUnitId_Type = Unsigned32
_AristaRedundancyUnitId_Object = MibTableColumn
aristaRedundancyUnitId = _AristaRedundancyUnitId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 1),
    _AristaRedundancyUnitId_Type()
)
aristaRedundancyUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaRedundancyUnitId.setStatus("current")
_AristaRedundancyUnitState_Type = AristaRedundancyState
_AristaRedundancyUnitState_Object = MibTableColumn
aristaRedundancyUnitState = _AristaRedundancyUnitState_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 2),
    _AristaRedundancyUnitState_Type()
)
aristaRedundancyUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaRedundancyUnitState.setStatus("current")
_AristaRedundancyUnitStateEntryTime_Type = TimeStamp
_AristaRedundancyUnitStateEntryTime_Object = MibTableColumn
aristaRedundancyUnitStateEntryTime = _AristaRedundancyUnitStateEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 3),
    _AristaRedundancyUnitStateEntryTime_Type()
)
aristaRedundancyUnitStateEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaRedundancyUnitStateEntryTime.setStatus("current")


class _AristaRedundancyLastSwOverReason_Type(OctetString):
    """Custom type aristaRedundancyLastSwOverReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaRedundancyLastSwOverReason_Type.__name__ = "OctetString"
_AristaRedundancyLastSwOverReason_Object = MibScalar
aristaRedundancyLastSwOverReason = _AristaRedundancyLastSwOverReason_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 4),
    _AristaRedundancyLastSwOverReason_Type()
)
aristaRedundancyLastSwOverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaRedundancyLastSwOverReason.setStatus("current")
_AristaRedundancyHistory_ObjectIdentity = ObjectIdentity
aristaRedundancyHistory = _AristaRedundancyHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 1)
)
_AristaRedundancyNotifications_ObjectIdentity = ObjectIdentity
aristaRedundancyNotifications = _AristaRedundancyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 1)
)
_AristaRedundancyNotificationPrefix_ObjectIdentity = ObjectIdentity
aristaRedundancyNotificationPrefix = _AristaRedundancyNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0)
)
_AristaRedundancyConformance_ObjectIdentity = ObjectIdentity
aristaRedundancyConformance = _AristaRedundancyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 2)
)
_AristaRedundancyCompliances_ObjectIdentity = ObjectIdentity
aristaRedundancyCompliances = _AristaRedundancyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1)
)
_AristaRedundancyGroups_ObjectIdentity = ObjectIdentity
aristaRedundancyGroups = _AristaRedundancyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2)
)

# Managed Objects groups

aristaRedundancyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 1)
)
aristaRedundancyStatusGroup.setObjects(
      *(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolConfig"),
        ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolOper"),
        ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitState"),
        ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"),
        ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"))
)
if mibBuilder.loadTexts:
    aristaRedundancyStatusGroup.setStatus("current")


# Notification objects

aristaRedundancySwitchOverNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0, 1)
)
aristaRedundancySwitchOverNotif.setObjects(
      *(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"),
        ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"))
)
if mibBuilder.loadTexts:
    aristaRedundancySwitchOverNotif.setStatus(
        "current"
    )


# Notifications groups

aristaRedundancyNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 2)
)
aristaRedundancyNotificationsGroup.setObjects(
    ("ARISTA-REDUNDANCY-MIB", "aristaRedundancySwitchOverNotif")
)
if mibBuilder.loadTexts:
    aristaRedundancyNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaRedundancyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaRedundancyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-REDUNDANCY-MIB",
    **{"AristaRedundancyState": AristaRedundancyState,
       "AristaRedundancyProtocol": AristaRedundancyProtocol,
       "aristaRedundancyMIB": aristaRedundancyMIB,
       "aristaRedundancyObjects": aristaRedundancyObjects,
       "aristaRedundancyStatus": aristaRedundancyStatus,
       "aristaRedundancyProtocolConfig": aristaRedundancyProtocolConfig,
       "aristaRedundancyProtocolOper": aristaRedundancyProtocolOper,
       "aristaRedundancyUnitStateTable": aristaRedundancyUnitStateTable,
       "aristaRedundancyUnitStateEntry": aristaRedundancyUnitStateEntry,
       "aristaRedundancyUnitId": aristaRedundancyUnitId,
       "aristaRedundancyUnitState": aristaRedundancyUnitState,
       "aristaRedundancyUnitStateEntryTime": aristaRedundancyUnitStateEntryTime,
       "aristaRedundancyLastSwOverReason": aristaRedundancyLastSwOverReason,
       "aristaRedundancyHistory": aristaRedundancyHistory,
       "aristaRedundancyNotifications": aristaRedundancyNotifications,
       "aristaRedundancyNotificationPrefix": aristaRedundancyNotificationPrefix,
       "aristaRedundancySwitchOverNotif": aristaRedundancySwitchOverNotif,
       "aristaRedundancyConformance": aristaRedundancyConformance,
       "aristaRedundancyCompliances": aristaRedundancyCompliances,
       "aristaRedundancyCompliance": aristaRedundancyCompliance,
       "aristaRedundancyGroups": aristaRedundancyGroups,
       "aristaRedundancyStatusGroup": aristaRedundancyStatusGroup,
       "aristaRedundancyNotificationsGroup": aristaRedundancyNotificationsGroup}
)
