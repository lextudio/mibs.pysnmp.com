# SNMP MIB module (JUNIPER-JS-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:20 2024
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

(jnxJsPolicies,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsPolicies")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

jnxJsSecPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1)
)
jnxJsSecPolicyMIB.setRevisions(
        ("2006-12-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsPolicyNotifications_ObjectIdentity = ObjectIdentity
jnxJsPolicyNotifications = _JnxJsPolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 0)
)
_JnxJsPolicyObjects_ObjectIdentity = ObjectIdentity
jnxJsPolicyObjects = _JnxJsPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1)
)
_JnxJsPolicyNumber_Type = Integer32
_JnxJsPolicyNumber_Object = MibScalar
jnxJsPolicyNumber = _JnxJsPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 1),
    _JnxJsPolicyNumber_Type()
)
jnxJsPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyNumber.setStatus("current")
_JnxJsPolicyTable_Object = MibTable
jnxJsPolicyTable = _JnxJsPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxJsPolicyTable.setStatus("current")
_JnxJsPolicyEntry_Object = MibTableRow
jnxJsPolicyEntry = _JnxJsPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1)
)
jnxJsPolicyEntry.setIndexNames(
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyFromZone"),
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyToZone"),
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyName"),
)
if mibBuilder.loadTexts:
    jnxJsPolicyEntry.setStatus("current")


class _JnxJsPolicyFromZone_Type(DisplayString):
    """Custom type jnxJsPolicyFromZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxJsPolicyFromZone_Type.__name__ = "DisplayString"
_JnxJsPolicyFromZone_Object = MibTableColumn
jnxJsPolicyFromZone = _JnxJsPolicyFromZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 1),
    _JnxJsPolicyFromZone_Type()
)
jnxJsPolicyFromZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsPolicyFromZone.setStatus("current")


class _JnxJsPolicyToZone_Type(DisplayString):
    """Custom type jnxJsPolicyToZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxJsPolicyToZone_Type.__name__ = "DisplayString"
_JnxJsPolicyToZone_Object = MibTableColumn
jnxJsPolicyToZone = _JnxJsPolicyToZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 2),
    _JnxJsPolicyToZone_Type()
)
jnxJsPolicyToZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsPolicyToZone.setStatus("current")


class _JnxJsPolicyName_Type(DisplayString):
    """Custom type jnxJsPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxJsPolicyName_Type.__name__ = "DisplayString"
_JnxJsPolicyName_Object = MibTableColumn
jnxJsPolicyName = _JnxJsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 3),
    _JnxJsPolicyName_Type()
)
jnxJsPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsPolicyName.setStatus("current")
_JnxJsPolicySequenceNumber_Type = Integer32
_JnxJsPolicySequenceNumber_Object = MibTableColumn
jnxJsPolicySequenceNumber = _JnxJsPolicySequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 4),
    _JnxJsPolicySequenceNumber_Type()
)
jnxJsPolicySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySequenceNumber.setStatus("current")


class _JnxJsPolicyAction_Type(Integer32):
    """Custom type jnxJsPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1),
          ("reject", 3))
    )


_JnxJsPolicyAction_Type.__name__ = "Integer32"
_JnxJsPolicyAction_Object = MibTableColumn
jnxJsPolicyAction = _JnxJsPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 5),
    _JnxJsPolicyAction_Type()
)
jnxJsPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyAction.setStatus("current")


class _JnxJsPolicyScheduler_Type(DisplayString):
    """Custom type jnxJsPolicyScheduler based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxJsPolicyScheduler_Type.__name__ = "DisplayString"
_JnxJsPolicyScheduler_Object = MibTableColumn
jnxJsPolicyScheduler = _JnxJsPolicyScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 6),
    _JnxJsPolicyScheduler_Type()
)
jnxJsPolicyScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyScheduler.setStatus("current")


class _JnxJsPolicyState_Type(Integer32):
    """Custom type jnxJsPolicyState based on Integer32"""
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
          ("inactive", 2),
          ("unavailable", 3))
    )


_JnxJsPolicyState_Type.__name__ = "Integer32"
_JnxJsPolicyState_Object = MibTableColumn
jnxJsPolicyState = _JnxJsPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 7),
    _JnxJsPolicyState_Type()
)
jnxJsPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyState.setStatus("current")


class _JnxJsPolicyStatsAvailability_Type(Integer32):
    """Custom type jnxJsPolicyStatsAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_JnxJsPolicyStatsAvailability_Type.__name__ = "Integer32"
_JnxJsPolicyStatsAvailability_Object = MibTableColumn
jnxJsPolicyStatsAvailability = _JnxJsPolicyStatsAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 8),
    _JnxJsPolicyStatsAvailability_Type()
)
jnxJsPolicyStatsAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsAvailability.setStatus("current")
_JnxJsPolicyPerSecBytesThreshold_Type = Integer32
_JnxJsPolicyPerSecBytesThreshold_Object = MibTableColumn
jnxJsPolicyPerSecBytesThreshold = _JnxJsPolicyPerSecBytesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 9),
    _JnxJsPolicyPerSecBytesThreshold_Type()
)
jnxJsPolicyPerSecBytesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyPerSecBytesThreshold.setStatus("current")
_JnxJsPolicyPerMinKbytesThreshold_Type = Integer32
_JnxJsPolicyPerMinKbytesThreshold_Object = MibTableColumn
jnxJsPolicyPerMinKbytesThreshold = _JnxJsPolicyPerMinKbytesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 10),
    _JnxJsPolicyPerMinKbytesThreshold_Type()
)
jnxJsPolicyPerMinKbytesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyPerMinKbytesThreshold.setStatus("current")
_JnxJsPolicyStatsTable_Object = MibTable
jnxJsPolicyStatsTable = _JnxJsPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxJsPolicyStatsTable.setStatus("current")
_JnxJsPolicyStatsEntry_Object = MibTableRow
jnxJsPolicyStatsEntry = _JnxJsPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1)
)
jnxJsPolicyStatsEntry.setIndexNames(
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyFromZone"),
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyToZone"),
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyName"),
)
if mibBuilder.loadTexts:
    jnxJsPolicyStatsEntry.setStatus("current")
_JnxJsPolicyStatsCreationTime_Type = TimeStamp
_JnxJsPolicyStatsCreationTime_Object = MibTableColumn
jnxJsPolicyStatsCreationTime = _JnxJsPolicyStatsCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 1),
    _JnxJsPolicyStatsCreationTime_Type()
)
jnxJsPolicyStatsCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsCreationTime.setStatus("current")
_JnxJsPolicyStatsInputBytes_Type = Counter64
_JnxJsPolicyStatsInputBytes_Object = MibTableColumn
jnxJsPolicyStatsInputBytes = _JnxJsPolicyStatsInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 2),
    _JnxJsPolicyStatsInputBytes_Type()
)
jnxJsPolicyStatsInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInputBytes.setStatus("current")
_JnxJsPolicyStatsInputByteRate_Type = Gauge32
_JnxJsPolicyStatsInputByteRate_Object = MibTableColumn
jnxJsPolicyStatsInputByteRate = _JnxJsPolicyStatsInputByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 3),
    _JnxJsPolicyStatsInputByteRate_Type()
)
jnxJsPolicyStatsInputByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInputByteRate.setStatus("current")
_JnxJsPolicyStatsOutputBytes_Type = Counter64
_JnxJsPolicyStatsOutputBytes_Object = MibTableColumn
jnxJsPolicyStatsOutputBytes = _JnxJsPolicyStatsOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 4),
    _JnxJsPolicyStatsOutputBytes_Type()
)
jnxJsPolicyStatsOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutputBytes.setStatus("current")
_JnxJsPolicyStatsOutputByteRate_Type = Gauge32
_JnxJsPolicyStatsOutputByteRate_Object = MibTableColumn
jnxJsPolicyStatsOutputByteRate = _JnxJsPolicyStatsOutputByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 5),
    _JnxJsPolicyStatsOutputByteRate_Type()
)
jnxJsPolicyStatsOutputByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutputByteRate.setStatus("current")
_JnxJsPolicyStatsInputPackets_Type = Counter32
_JnxJsPolicyStatsInputPackets_Object = MibTableColumn
jnxJsPolicyStatsInputPackets = _JnxJsPolicyStatsInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 6),
    _JnxJsPolicyStatsInputPackets_Type()
)
jnxJsPolicyStatsInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInputPackets.setStatus("current")
_JnxJsPolicyStatsInputPacketRate_Type = Gauge32
_JnxJsPolicyStatsInputPacketRate_Object = MibTableColumn
jnxJsPolicyStatsInputPacketRate = _JnxJsPolicyStatsInputPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 7),
    _JnxJsPolicyStatsInputPacketRate_Type()
)
jnxJsPolicyStatsInputPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInputPacketRate.setStatus("current")
_JnxJsPolicyStatsOutputPackets_Type = Counter32
_JnxJsPolicyStatsOutputPackets_Object = MibTableColumn
jnxJsPolicyStatsOutputPackets = _JnxJsPolicyStatsOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 8),
    _JnxJsPolicyStatsOutputPackets_Type()
)
jnxJsPolicyStatsOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutputPackets.setStatus("current")
_JnxJsPolicyStatsOutputPacketRate_Type = Gauge32
_JnxJsPolicyStatsOutputPacketRate_Object = MibTableColumn
jnxJsPolicyStatsOutputPacketRate = _JnxJsPolicyStatsOutputPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 9),
    _JnxJsPolicyStatsOutputPacketRate_Type()
)
jnxJsPolicyStatsOutputPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutputPacketRate.setStatus("current")
_JnxJsPolicyStatsNumSessions_Type = Counter32
_JnxJsPolicyStatsNumSessions_Object = MibTableColumn
jnxJsPolicyStatsNumSessions = _JnxJsPolicyStatsNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 10),
    _JnxJsPolicyStatsNumSessions_Type()
)
jnxJsPolicyStatsNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsNumSessions.setStatus("current")
_JnxJsPolicyStatsSessionRate_Type = Gauge32
_JnxJsPolicyStatsSessionRate_Object = MibTableColumn
jnxJsPolicyStatsSessionRate = _JnxJsPolicyStatsSessionRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 11),
    _JnxJsPolicyStatsSessionRate_Type()
)
jnxJsPolicyStatsSessionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsSessionRate.setStatus("current")
_JnxJsPolicyStatsSessionDeleted_Type = Counter32
_JnxJsPolicyStatsSessionDeleted_Object = MibTableColumn
jnxJsPolicyStatsSessionDeleted = _JnxJsPolicyStatsSessionDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 12),
    _JnxJsPolicyStatsSessionDeleted_Type()
)
jnxJsPolicyStatsSessionDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsSessionDeleted.setStatus("current")
_JnxJsPolicyStatsLookups_Type = Counter32
_JnxJsPolicyStatsLookups_Object = MibTableColumn
jnxJsPolicyStatsLookups = _JnxJsPolicyStatsLookups_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 13),
    _JnxJsPolicyStatsLookups_Type()
)
jnxJsPolicyStatsLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsLookups.setStatus("current")
_JnxJsPolicyStatsCountAlarm_Type = Counter32
_JnxJsPolicyStatsCountAlarm_Object = MibTableColumn
jnxJsPolicyStatsCountAlarm = _JnxJsPolicyStatsCountAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 14),
    _JnxJsPolicyStatsCountAlarm_Type()
)
jnxJsPolicyStatsCountAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsCountAlarm.setStatus("current")
_JnxJsPolicyTrapVars_ObjectIdentity = ObjectIdentity
jnxJsPolicyTrapVars = _JnxJsPolicyTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-POLICY-MIB",
    **{"jnxJsSecPolicyMIB": jnxJsSecPolicyMIB,
       "jnxJsPolicyNotifications": jnxJsPolicyNotifications,
       "jnxJsPolicyObjects": jnxJsPolicyObjects,
       "jnxJsPolicyNumber": jnxJsPolicyNumber,
       "jnxJsPolicyTable": jnxJsPolicyTable,
       "jnxJsPolicyEntry": jnxJsPolicyEntry,
       "jnxJsPolicyFromZone": jnxJsPolicyFromZone,
       "jnxJsPolicyToZone": jnxJsPolicyToZone,
       "jnxJsPolicyName": jnxJsPolicyName,
       "jnxJsPolicySequenceNumber": jnxJsPolicySequenceNumber,
       "jnxJsPolicyAction": jnxJsPolicyAction,
       "jnxJsPolicyScheduler": jnxJsPolicyScheduler,
       "jnxJsPolicyState": jnxJsPolicyState,
       "jnxJsPolicyStatsAvailability": jnxJsPolicyStatsAvailability,
       "jnxJsPolicyPerSecBytesThreshold": jnxJsPolicyPerSecBytesThreshold,
       "jnxJsPolicyPerMinKbytesThreshold": jnxJsPolicyPerMinKbytesThreshold,
       "jnxJsPolicyStatsTable": jnxJsPolicyStatsTable,
       "jnxJsPolicyStatsEntry": jnxJsPolicyStatsEntry,
       "jnxJsPolicyStatsCreationTime": jnxJsPolicyStatsCreationTime,
       "jnxJsPolicyStatsInputBytes": jnxJsPolicyStatsInputBytes,
       "jnxJsPolicyStatsInputByteRate": jnxJsPolicyStatsInputByteRate,
       "jnxJsPolicyStatsOutputBytes": jnxJsPolicyStatsOutputBytes,
       "jnxJsPolicyStatsOutputByteRate": jnxJsPolicyStatsOutputByteRate,
       "jnxJsPolicyStatsInputPackets": jnxJsPolicyStatsInputPackets,
       "jnxJsPolicyStatsInputPacketRate": jnxJsPolicyStatsInputPacketRate,
       "jnxJsPolicyStatsOutputPackets": jnxJsPolicyStatsOutputPackets,
       "jnxJsPolicyStatsOutputPacketRate": jnxJsPolicyStatsOutputPacketRate,
       "jnxJsPolicyStatsNumSessions": jnxJsPolicyStatsNumSessions,
       "jnxJsPolicyStatsSessionRate": jnxJsPolicyStatsSessionRate,
       "jnxJsPolicyStatsSessionDeleted": jnxJsPolicyStatsSessionDeleted,
       "jnxJsPolicyStatsLookups": jnxJsPolicyStatsLookups,
       "jnxJsPolicyStatsCountAlarm": jnxJsPolicyStatsCountAlarm,
       "jnxJsPolicyTrapVars": jnxJsPolicyTrapVars}
)
