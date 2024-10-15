# SNMP MIB module (APSNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APSNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:00 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Brand_ObjectIdentity = ObjectIdentity
brand = _Brand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716)
)
_WindowsNT_ObjectIdentity = ObjectIdentity
windowsNT = _WindowsNT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1)
)
_ApolloStatsForNT_ObjectIdentity = ObjectIdentity
apolloStatsForNT = _ApolloStatsForNT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1)
)
_StatsForPort_ObjectIdentity = ObjectIdentity
statsForPort = _StatsForPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 1)
)


class _StatsPortsInUse_Type(Integer32):
    """Custom type statsPortsInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPortsInUse_Type.__name__ = "Integer32"
_StatsPortsInUse_Object = MibScalar
statsPortsInUse = _StatsPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 1, 1),
    _StatsPortsInUse_Type()
)
statsPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPortsInUse.setStatus("mandatory")


class _StatsMaxPortsUsed_Type(Integer32):
    """Custom type statsMaxPortsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsMaxPortsUsed_Type.__name__ = "Integer32"
_StatsMaxPortsUsed_Object = MibScalar
statsMaxPortsUsed = _StatsMaxPortsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 1, 2),
    _StatsMaxPortsUsed_Type()
)
statsMaxPortsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsMaxPortsUsed.setStatus("mandatory")


class _StatsPortsInUseIncoming_Type(Integer32):
    """Custom type statsPortsInUseIncoming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPortsInUseIncoming_Type.__name__ = "Integer32"
_StatsPortsInUseIncoming_Object = MibScalar
statsPortsInUseIncoming = _StatsPortsInUseIncoming_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 1, 3),
    _StatsPortsInUseIncoming_Type()
)
statsPortsInUseIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPortsInUseIncoming.setStatus("mandatory")


class _StatsPortsInUseOutgoing_Type(Integer32):
    """Custom type statsPortsInUseOutgoing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPortsInUseOutgoing_Type.__name__ = "Integer32"
_StatsPortsInUseOutgoing_Object = MibScalar
statsPortsInUseOutgoing = _StatsPortsInUseOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 1, 4),
    _StatsPortsInUseOutgoing_Type()
)
statsPortsInUseOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPortsInUseOutgoing.setStatus("mandatory")


class _StatsOverrallCompressionRatioOfAllPorts_Type(Integer32):
    """Custom type statsOverrallCompressionRatioOfAllPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsOverrallCompressionRatioOfAllPorts_Type.__name__ = "Integer32"
_StatsOverrallCompressionRatioOfAllPorts_Object = MibScalar
statsOverrallCompressionRatioOfAllPorts = _StatsOverrallCompressionRatioOfAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 1, 5),
    _StatsOverrallCompressionRatioOfAllPorts_Type()
)
statsOverrallCompressionRatioOfAllPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsOverrallCompressionRatioOfAllPorts.setStatus("mandatory")
_StatsForCalls_ObjectIdentity = ObjectIdentity
statsForCalls = _StatsForCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2)
)


class _StatsTotalCallsMade_Type(Integer32):
    """Custom type statsTotalCallsMade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalCallsMade_Type.__name__ = "Integer32"
_StatsTotalCallsMade_Object = MibScalar
statsTotalCallsMade = _StatsTotalCallsMade_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 1),
    _StatsTotalCallsMade_Type()
)
statsTotalCallsMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalCallsMade.setStatus("mandatory")


class _StatsFailedOutgoingCalls_Type(Integer32):
    """Custom type statsFailedOutgoingCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsFailedOutgoingCalls_Type.__name__ = "Integer32"
_StatsFailedOutgoingCalls_Object = MibScalar
statsFailedOutgoingCalls = _StatsFailedOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 2),
    _StatsFailedOutgoingCalls_Type()
)
statsFailedOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsFailedOutgoingCalls.setStatus("mandatory")


class _StatsTotalCallsReceivedPerMinute_Type(Integer32):
    """Custom type statsTotalCallsReceivedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalCallsReceivedPerMinute_Type.__name__ = "Integer32"
_StatsTotalCallsReceivedPerMinute_Object = MibScalar
statsTotalCallsReceivedPerMinute = _StatsTotalCallsReceivedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 3),
    _StatsTotalCallsReceivedPerMinute_Type()
)
statsTotalCallsReceivedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalCallsReceivedPerMinute.setStatus("mandatory")


class _StatsTotalCallsReceivedPerHour_Type(Integer32):
    """Custom type statsTotalCallsReceivedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalCallsReceivedPerHour_Type.__name__ = "Integer32"
_StatsTotalCallsReceivedPerHour_Object = MibScalar
statsTotalCallsReceivedPerHour = _StatsTotalCallsReceivedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 4),
    _StatsTotalCallsReceivedPerHour_Type()
)
statsTotalCallsReceivedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalCallsReceivedPerHour.setStatus("mandatory")


class _StatsTotalCallsReceivedPerDay_Type(Integer32):
    """Custom type statsTotalCallsReceivedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalCallsReceivedPerDay_Type.__name__ = "Integer32"
_StatsTotalCallsReceivedPerDay_Object = MibScalar
statsTotalCallsReceivedPerDay = _StatsTotalCallsReceivedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 5),
    _StatsTotalCallsReceivedPerDay_Type()
)
statsTotalCallsReceivedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalCallsReceivedPerDay.setStatus("mandatory")


class _StatsTotalCallsMadePerMinute_Type(Integer32):
    """Custom type statsTotalCallsMadePerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalCallsMadePerMinute_Type.__name__ = "Integer32"
_StatsTotalCallsMadePerMinute_Object = MibScalar
statsTotalCallsMadePerMinute = _StatsTotalCallsMadePerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 6),
    _StatsTotalCallsMadePerMinute_Type()
)
statsTotalCallsMadePerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalCallsMadePerMinute.setStatus("mandatory")


class _StatsTotalCallsMadePerHour_Type(Integer32):
    """Custom type statsTotalCallsMadePerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalCallsMadePerHour_Type.__name__ = "Integer32"
_StatsTotalCallsMadePerHour_Object = MibScalar
statsTotalCallsMadePerHour = _StatsTotalCallsMadePerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 7),
    _StatsTotalCallsMadePerHour_Type()
)
statsTotalCallsMadePerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalCallsMadePerHour.setStatus("mandatory")


class _StatsTotalCallsMadePerDay_Type(Integer32):
    """Custom type statsTotalCallsMadePerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalCallsMadePerDay_Type.__name__ = "Integer32"
_StatsTotalCallsMadePerDay_Object = MibScalar
statsTotalCallsMadePerDay = _StatsTotalCallsMadePerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 8),
    _StatsTotalCallsMadePerDay_Type()
)
statsTotalCallsMadePerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalCallsMadePerDay.setStatus("mandatory")


class _StatsTotalCallsReceived_Type(Integer32):
    """Custom type statsTotalCallsReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalCallsReceived_Type.__name__ = "Integer32"
_StatsTotalCallsReceived_Object = MibScalar
statsTotalCallsReceived = _StatsTotalCallsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 2, 9),
    _StatsTotalCallsReceived_Type()
)
statsTotalCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalCallsReceived.setStatus("mandatory")
_StatsForSession_ObjectIdentity = ObjectIdentity
statsForSession = _StatsForSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3)
)
_StatsSessionForGeneral_ObjectIdentity = ObjectIdentity
statsSessionForGeneral = _StatsSessionForGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1)
)


class _StatsMaxSessionsUsed_Type(Integer32):
    """Custom type statsMaxSessionsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsMaxSessionsUsed_Type.__name__ = "Integer32"
_StatsMaxSessionsUsed_Object = MibScalar
statsMaxSessionsUsed = _StatsMaxSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 1),
    _StatsMaxSessionsUsed_Type()
)
statsMaxSessionsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsMaxSessionsUsed.setStatus("mandatory")


class _StatsTotalNumberUserSessionGranted_Type(Integer32):
    """Custom type statsTotalNumberUserSessionGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberUserSessionGranted_Type.__name__ = "Integer32"
_StatsTotalNumberUserSessionGranted_Object = MibScalar
statsTotalNumberUserSessionGranted = _StatsTotalNumberUserSessionGranted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 2),
    _StatsTotalNumberUserSessionGranted_Type()
)
statsTotalNumberUserSessionGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberUserSessionGranted.setStatus("mandatory")


class _StatsTotalNumberUserSessionRefused_Type(Integer32):
    """Custom type statsTotalNumberUserSessionRefused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberUserSessionRefused_Type.__name__ = "Integer32"
_StatsTotalNumberUserSessionRefused_Object = MibScalar
statsTotalNumberUserSessionRefused = _StatsTotalNumberUserSessionRefused_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 3),
    _StatsTotalNumberUserSessionRefused_Type()
)
statsTotalNumberUserSessionRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberUserSessionRefused.setStatus("mandatory")


class _StatsTotalNumberUserSessionsGrantedPerMinute_Type(Integer32):
    """Custom type statsTotalNumberUserSessionsGrantedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberUserSessionsGrantedPerMinute_Type.__name__ = "Integer32"
_StatsTotalNumberUserSessionsGrantedPerMinute_Object = MibScalar
statsTotalNumberUserSessionsGrantedPerMinute = _StatsTotalNumberUserSessionsGrantedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 4),
    _StatsTotalNumberUserSessionsGrantedPerMinute_Type()
)
statsTotalNumberUserSessionsGrantedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberUserSessionsGrantedPerMinute.setStatus("mandatory")


class _StatsTotalNumberUserSessionGrantedPerHour_Type(Integer32):
    """Custom type statsTotalNumberUserSessionGrantedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberUserSessionGrantedPerHour_Type.__name__ = "Integer32"
_StatsTotalNumberUserSessionGrantedPerHour_Object = MibScalar
statsTotalNumberUserSessionGrantedPerHour = _StatsTotalNumberUserSessionGrantedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 5),
    _StatsTotalNumberUserSessionGrantedPerHour_Type()
)
statsTotalNumberUserSessionGrantedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberUserSessionGrantedPerHour.setStatus("mandatory")


class _StatsTotalNumberUserSessionGrantedPerDay_Type(Integer32):
    """Custom type statsTotalNumberUserSessionGrantedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberUserSessionGrantedPerDay_Type.__name__ = "Integer32"
_StatsTotalNumberUserSessionGrantedPerDay_Object = MibScalar
statsTotalNumberUserSessionGrantedPerDay = _StatsTotalNumberUserSessionGrantedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 6),
    _StatsTotalNumberUserSessionGrantedPerDay_Type()
)
statsTotalNumberUserSessionGrantedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberUserSessionGrantedPerDay.setStatus("mandatory")


class _StatsTotalNumberUserSessionRefusedPerMinute_Type(Integer32):
    """Custom type statsTotalNumberUserSessionRefusedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberUserSessionRefusedPerMinute_Type.__name__ = "Integer32"
_StatsTotalNumberUserSessionRefusedPerMinute_Object = MibScalar
statsTotalNumberUserSessionRefusedPerMinute = _StatsTotalNumberUserSessionRefusedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 7),
    _StatsTotalNumberUserSessionRefusedPerMinute_Type()
)
statsTotalNumberUserSessionRefusedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberUserSessionRefusedPerMinute.setStatus("mandatory")


class _StatsTotalNumberUserSessionRefusedPerHour_Type(Integer32):
    """Custom type statsTotalNumberUserSessionRefusedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberUserSessionRefusedPerHour_Type.__name__ = "Integer32"
_StatsTotalNumberUserSessionRefusedPerHour_Object = MibScalar
statsTotalNumberUserSessionRefusedPerHour = _StatsTotalNumberUserSessionRefusedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 8),
    _StatsTotalNumberUserSessionRefusedPerHour_Type()
)
statsTotalNumberUserSessionRefusedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberUserSessionRefusedPerHour.setStatus("mandatory")


class _StatsTotalNumberUserSessionRefusedPerDay_Type(Integer32):
    """Custom type statsTotalNumberUserSessionRefusedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberUserSessionRefusedPerDay_Type.__name__ = "Integer32"
_StatsTotalNumberUserSessionRefusedPerDay_Object = MibScalar
statsTotalNumberUserSessionRefusedPerDay = _StatsTotalNumberUserSessionRefusedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 9),
    _StatsTotalNumberUserSessionRefusedPerDay_Type()
)
statsTotalNumberUserSessionRefusedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberUserSessionRefusedPerDay.setStatus("mandatory")


class _StatsTotalActiveUserSession_Type(Integer32):
    """Custom type statsTotalActiveUserSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalActiveUserSession_Type.__name__ = "Integer32"
_StatsTotalActiveUserSession_Object = MibScalar
statsTotalActiveUserSession = _StatsTotalActiveUserSession_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 1, 10),
    _StatsTotalActiveUserSession_Type()
)
statsTotalActiveUserSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalActiveUserSession.setStatus("mandatory")
_StatsSessionForApollo_ObjectIdentity = ObjectIdentity
statsSessionForApollo = _StatsSessionForApollo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2)
)


class _StatsApolloActiveUserSessions_Type(Integer32):
    """Custom type statsApolloActiveUserSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloActiveUserSessions_Type.__name__ = "Integer32"
_StatsApolloActiveUserSessions_Object = MibScalar
statsApolloActiveUserSessions = _StatsApolloActiveUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 1),
    _StatsApolloActiveUserSessions_Type()
)
statsApolloActiveUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloActiveUserSessions.setStatus("mandatory")


class _StatsApolloNumberUserSessionsGranted_Type(Integer32):
    """Custom type statsApolloNumberUserSessionsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloNumberUserSessionsGranted_Type.__name__ = "Integer32"
_StatsApolloNumberUserSessionsGranted_Object = MibScalar
statsApolloNumberUserSessionsGranted = _StatsApolloNumberUserSessionsGranted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 2),
    _StatsApolloNumberUserSessionsGranted_Type()
)
statsApolloNumberUserSessionsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloNumberUserSessionsGranted.setStatus("mandatory")


class _StatsApolloNumberUserSessionsrefused_Type(Integer32):
    """Custom type statsApolloNumberUserSessionsrefused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloNumberUserSessionsrefused_Type.__name__ = "Integer32"
_StatsApolloNumberUserSessionsrefused_Object = MibScalar
statsApolloNumberUserSessionsrefused = _StatsApolloNumberUserSessionsrefused_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 3),
    _StatsApolloNumberUserSessionsrefused_Type()
)
statsApolloNumberUserSessionsrefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloNumberUserSessionsrefused.setStatus("mandatory")


class _StatsApolloNumberUserSessionsGrantedPerMinute_Type(Integer32):
    """Custom type statsApolloNumberUserSessionsGrantedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloNumberUserSessionsGrantedPerMinute_Type.__name__ = "Integer32"
_StatsApolloNumberUserSessionsGrantedPerMinute_Object = MibScalar
statsApolloNumberUserSessionsGrantedPerMinute = _StatsApolloNumberUserSessionsGrantedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 4),
    _StatsApolloNumberUserSessionsGrantedPerMinute_Type()
)
statsApolloNumberUserSessionsGrantedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloNumberUserSessionsGrantedPerMinute.setStatus("mandatory")


class _StatsApolloNumberUserSessionsGrantedPerHour_Type(Integer32):
    """Custom type statsApolloNumberUserSessionsGrantedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloNumberUserSessionsGrantedPerHour_Type.__name__ = "Integer32"
_StatsApolloNumberUserSessionsGrantedPerHour_Object = MibScalar
statsApolloNumberUserSessionsGrantedPerHour = _StatsApolloNumberUserSessionsGrantedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 5),
    _StatsApolloNumberUserSessionsGrantedPerHour_Type()
)
statsApolloNumberUserSessionsGrantedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloNumberUserSessionsGrantedPerHour.setStatus("mandatory")


class _StatsApolloNumberUserSessionsGrantedPerDay_Type(Integer32):
    """Custom type statsApolloNumberUserSessionsGrantedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloNumberUserSessionsGrantedPerDay_Type.__name__ = "Integer32"
_StatsApolloNumberUserSessionsGrantedPerDay_Object = MibScalar
statsApolloNumberUserSessionsGrantedPerDay = _StatsApolloNumberUserSessionsGrantedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 6),
    _StatsApolloNumberUserSessionsGrantedPerDay_Type()
)
statsApolloNumberUserSessionsGrantedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloNumberUserSessionsGrantedPerDay.setStatus("mandatory")


class _StatsApolloNumberUserSessionsRefusedPerMinute_Type(Integer32):
    """Custom type statsApolloNumberUserSessionsRefusedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloNumberUserSessionsRefusedPerMinute_Type.__name__ = "Integer32"
_StatsApolloNumberUserSessionsRefusedPerMinute_Object = MibScalar
statsApolloNumberUserSessionsRefusedPerMinute = _StatsApolloNumberUserSessionsRefusedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 7),
    _StatsApolloNumberUserSessionsRefusedPerMinute_Type()
)
statsApolloNumberUserSessionsRefusedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloNumberUserSessionsRefusedPerMinute.setStatus("mandatory")


class _StatsApolloNumberUserSessionsRefusedPerHour_Type(Integer32):
    """Custom type statsApolloNumberUserSessionsRefusedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloNumberUserSessionsRefusedPerHour_Type.__name__ = "Integer32"
_StatsApolloNumberUserSessionsRefusedPerHour_Object = MibScalar
statsApolloNumberUserSessionsRefusedPerHour = _StatsApolloNumberUserSessionsRefusedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 8),
    _StatsApolloNumberUserSessionsRefusedPerHour_Type()
)
statsApolloNumberUserSessionsRefusedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloNumberUserSessionsRefusedPerHour.setStatus("mandatory")


class _StatsApolloNumberUserSessionsRefusedPerDay_Type(Integer32):
    """Custom type statsApolloNumberUserSessionsRefusedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloNumberUserSessionsRefusedPerDay_Type.__name__ = "Integer32"
_StatsApolloNumberUserSessionsRefusedPerDay_Object = MibScalar
statsApolloNumberUserSessionsRefusedPerDay = _StatsApolloNumberUserSessionsRefusedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 9),
    _StatsApolloNumberUserSessionsRefusedPerDay_Type()
)
statsApolloNumberUserSessionsRefusedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloNumberUserSessionsRefusedPerDay.setStatus("mandatory")


class _StatsApolloMaximumSessionsUsed_Type(Integer32):
    """Custom type statsApolloMaximumSessionsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsApolloMaximumSessionsUsed_Type.__name__ = "Integer32"
_StatsApolloMaximumSessionsUsed_Object = MibScalar
statsApolloMaximumSessionsUsed = _StatsApolloMaximumSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 2, 10),
    _StatsApolloMaximumSessionsUsed_Type()
)
statsApolloMaximumSessionsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsApolloMaximumSessionsUsed.setStatus("mandatory")
_StatsSessionForPPP_ObjectIdentity = ObjectIdentity
statsSessionForPPP = _StatsSessionForPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3)
)


class _StatsPPPActiveUserSessions_Type(Integer32):
    """Custom type statsPPPActiveUserSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPActiveUserSessions_Type.__name__ = "Integer32"
_StatsPPPActiveUserSessions_Object = MibScalar
statsPPPActiveUserSessions = _StatsPPPActiveUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 1),
    _StatsPPPActiveUserSessions_Type()
)
statsPPPActiveUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPActiveUserSessions.setStatus("mandatory")


class _StatsPPPNumberUserSessionsGranted_Type(Integer32):
    """Custom type statsPPPNumberUserSessionsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPNumberUserSessionsGranted_Type.__name__ = "Integer32"
_StatsPPPNumberUserSessionsGranted_Object = MibScalar
statsPPPNumberUserSessionsGranted = _StatsPPPNumberUserSessionsGranted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 2),
    _StatsPPPNumberUserSessionsGranted_Type()
)
statsPPPNumberUserSessionsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPNumberUserSessionsGranted.setStatus("mandatory")


class _StatsPPPNumberUserSessionsRefused_Type(Integer32):
    """Custom type statsPPPNumberUserSessionsRefused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPNumberUserSessionsRefused_Type.__name__ = "Integer32"
_StatsPPPNumberUserSessionsRefused_Object = MibScalar
statsPPPNumberUserSessionsRefused = _StatsPPPNumberUserSessionsRefused_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 3),
    _StatsPPPNumberUserSessionsRefused_Type()
)
statsPPPNumberUserSessionsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPNumberUserSessionsRefused.setStatus("mandatory")


class _StatsPPPNumberUserSessionsGrantedPerMinute_Type(Integer32):
    """Custom type statsPPPNumberUserSessionsGrantedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPNumberUserSessionsGrantedPerMinute_Type.__name__ = "Integer32"
_StatsPPPNumberUserSessionsGrantedPerMinute_Object = MibScalar
statsPPPNumberUserSessionsGrantedPerMinute = _StatsPPPNumberUserSessionsGrantedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 4),
    _StatsPPPNumberUserSessionsGrantedPerMinute_Type()
)
statsPPPNumberUserSessionsGrantedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPNumberUserSessionsGrantedPerMinute.setStatus("mandatory")


class _StatsPPPNumberUserSessionsGrantedPerHour_Type(Integer32):
    """Custom type statsPPPNumberUserSessionsGrantedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPNumberUserSessionsGrantedPerHour_Type.__name__ = "Integer32"
_StatsPPPNumberUserSessionsGrantedPerHour_Object = MibScalar
statsPPPNumberUserSessionsGrantedPerHour = _StatsPPPNumberUserSessionsGrantedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 5),
    _StatsPPPNumberUserSessionsGrantedPerHour_Type()
)
statsPPPNumberUserSessionsGrantedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPNumberUserSessionsGrantedPerHour.setStatus("mandatory")


class _StatsPPPNumberUserSessionsGrantedPerDay_Type(Integer32):
    """Custom type statsPPPNumberUserSessionsGrantedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPNumberUserSessionsGrantedPerDay_Type.__name__ = "Integer32"
_StatsPPPNumberUserSessionsGrantedPerDay_Object = MibScalar
statsPPPNumberUserSessionsGrantedPerDay = _StatsPPPNumberUserSessionsGrantedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 6),
    _StatsPPPNumberUserSessionsGrantedPerDay_Type()
)
statsPPPNumberUserSessionsGrantedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPNumberUserSessionsGrantedPerDay.setStatus("mandatory")


class _StatsPPPNumberUserSessionsRefusedPerMinute_Type(Integer32):
    """Custom type statsPPPNumberUserSessionsRefusedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPNumberUserSessionsRefusedPerMinute_Type.__name__ = "Integer32"
_StatsPPPNumberUserSessionsRefusedPerMinute_Object = MibScalar
statsPPPNumberUserSessionsRefusedPerMinute = _StatsPPPNumberUserSessionsRefusedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 7),
    _StatsPPPNumberUserSessionsRefusedPerMinute_Type()
)
statsPPPNumberUserSessionsRefusedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPNumberUserSessionsRefusedPerMinute.setStatus("mandatory")


class _StatsPPPNumberUserSessionsRefusedPerHour_Type(Integer32):
    """Custom type statsPPPNumberUserSessionsRefusedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPNumberUserSessionsRefusedPerHour_Type.__name__ = "Integer32"
_StatsPPPNumberUserSessionsRefusedPerHour_Object = MibScalar
statsPPPNumberUserSessionsRefusedPerHour = _StatsPPPNumberUserSessionsRefusedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 8),
    _StatsPPPNumberUserSessionsRefusedPerHour_Type()
)
statsPPPNumberUserSessionsRefusedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPNumberUserSessionsRefusedPerHour.setStatus("mandatory")


class _StatsPPPNumberUserSessionsRefusedPerDay_Type(Integer32):
    """Custom type statsPPPNumberUserSessionsRefusedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPNumberUserSessionsRefusedPerDay_Type.__name__ = "Integer32"
_StatsPPPNumberUserSessionsRefusedPerDay_Object = MibScalar
statsPPPNumberUserSessionsRefusedPerDay = _StatsPPPNumberUserSessionsRefusedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 9),
    _StatsPPPNumberUserSessionsRefusedPerDay_Type()
)
statsPPPNumberUserSessionsRefusedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPNumberUserSessionsRefusedPerDay.setStatus("mandatory")


class _StatsPPPMaximumSessionsUsed_Type(Integer32):
    """Custom type statsPPPMaximumSessionsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPPPMaximumSessionsUsed_Type.__name__ = "Integer32"
_StatsPPPMaximumSessionsUsed_Object = MibScalar
statsPPPMaximumSessionsUsed = _StatsPPPMaximumSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 3, 3, 10),
    _StatsPPPMaximumSessionsUsed_Type()
)
statsPPPMaximumSessionsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPPPMaximumSessionsUsed.setStatus("mandatory")
_StatsForData_ObjectIdentity = ObjectIdentity
statsForData = _StatsForData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4)
)


class _StatsNumberBytesReceivedPerSecond_Type(Integer32):
    """Custom type statsNumberBytesReceivedPerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsNumberBytesReceivedPerSecond_Type.__name__ = "Integer32"
_StatsNumberBytesReceivedPerSecond_Object = MibScalar
statsNumberBytesReceivedPerSecond = _StatsNumberBytesReceivedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 1),
    _StatsNumberBytesReceivedPerSecond_Type()
)
statsNumberBytesReceivedPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsNumberBytesReceivedPerSecond.setStatus("mandatory")


class _StatsNumberBytesReceivedPerMinute_Type(Integer32):
    """Custom type statsNumberBytesReceivedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsNumberBytesReceivedPerMinute_Type.__name__ = "Integer32"
_StatsNumberBytesReceivedPerMinute_Object = MibScalar
statsNumberBytesReceivedPerMinute = _StatsNumberBytesReceivedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 2),
    _StatsNumberBytesReceivedPerMinute_Type()
)
statsNumberBytesReceivedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsNumberBytesReceivedPerMinute.setStatus("mandatory")


class _StatsNumberBytesReceivedPerHour_Type(Integer32):
    """Custom type statsNumberBytesReceivedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsNumberBytesReceivedPerHour_Type.__name__ = "Integer32"
_StatsNumberBytesReceivedPerHour_Object = MibScalar
statsNumberBytesReceivedPerHour = _StatsNumberBytesReceivedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 3),
    _StatsNumberBytesReceivedPerHour_Type()
)
statsNumberBytesReceivedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsNumberBytesReceivedPerHour.setStatus("mandatory")


class _StatsNumberBytesReceivedPerDay_Type(Integer32):
    """Custom type statsNumberBytesReceivedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsNumberBytesReceivedPerDay_Type.__name__ = "Integer32"
_StatsNumberBytesReceivedPerDay_Object = MibScalar
statsNumberBytesReceivedPerDay = _StatsNumberBytesReceivedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 4),
    _StatsNumberBytesReceivedPerDay_Type()
)
statsNumberBytesReceivedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsNumberBytesReceivedPerDay.setStatus("mandatory")


class _StatsNumberBytesTransmittedPerSecond_Type(Integer32):
    """Custom type statsNumberBytesTransmittedPerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsNumberBytesTransmittedPerSecond_Type.__name__ = "Integer32"
_StatsNumberBytesTransmittedPerSecond_Object = MibScalar
statsNumberBytesTransmittedPerSecond = _StatsNumberBytesTransmittedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 5),
    _StatsNumberBytesTransmittedPerSecond_Type()
)
statsNumberBytesTransmittedPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsNumberBytesTransmittedPerSecond.setStatus("mandatory")


class _StatsNumberBytesTransmittedPerMinute_Type(Integer32):
    """Custom type statsNumberBytesTransmittedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsNumberBytesTransmittedPerMinute_Type.__name__ = "Integer32"
_StatsNumberBytesTransmittedPerMinute_Object = MibScalar
statsNumberBytesTransmittedPerMinute = _StatsNumberBytesTransmittedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 6),
    _StatsNumberBytesTransmittedPerMinute_Type()
)
statsNumberBytesTransmittedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsNumberBytesTransmittedPerMinute.setStatus("mandatory")


class _StatsNumberBytesTransmittedPerHour_Type(Integer32):
    """Custom type statsNumberBytesTransmittedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsNumberBytesTransmittedPerHour_Type.__name__ = "Integer32"
_StatsNumberBytesTransmittedPerHour_Object = MibScalar
statsNumberBytesTransmittedPerHour = _StatsNumberBytesTransmittedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 7),
    _StatsNumberBytesTransmittedPerHour_Type()
)
statsNumberBytesTransmittedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsNumberBytesTransmittedPerHour.setStatus("mandatory")


class _StatsNumberBytesTransmittedPerDay_Type(Integer32):
    """Custom type statsNumberBytesTransmittedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsNumberBytesTransmittedPerDay_Type.__name__ = "Integer32"
_StatsNumberBytesTransmittedPerDay_Object = MibScalar
statsNumberBytesTransmittedPerDay = _StatsNumberBytesTransmittedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 8),
    _StatsNumberBytesTransmittedPerDay_Type()
)
statsNumberBytesTransmittedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsNumberBytesTransmittedPerDay.setStatus("mandatory")


class _StatsPacketsTransmittedPerMinute_Type(Integer32):
    """Custom type statsPacketsTransmittedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPacketsTransmittedPerMinute_Type.__name__ = "Integer32"
_StatsPacketsTransmittedPerMinute_Object = MibScalar
statsPacketsTransmittedPerMinute = _StatsPacketsTransmittedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 9),
    _StatsPacketsTransmittedPerMinute_Type()
)
statsPacketsTransmittedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPacketsTransmittedPerMinute.setStatus("mandatory")


class _StatsPacketsTransmittedPerHour_Type(Integer32):
    """Custom type statsPacketsTransmittedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPacketsTransmittedPerHour_Type.__name__ = "Integer32"
_StatsPacketsTransmittedPerHour_Object = MibScalar
statsPacketsTransmittedPerHour = _StatsPacketsTransmittedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 10),
    _StatsPacketsTransmittedPerHour_Type()
)
statsPacketsTransmittedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPacketsTransmittedPerHour.setStatus("mandatory")


class _StatsPacketsTransmittedPerDay_Type(Integer32):
    """Custom type statsPacketsTransmittedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPacketsTransmittedPerDay_Type.__name__ = "Integer32"
_StatsPacketsTransmittedPerDay_Object = MibScalar
statsPacketsTransmittedPerDay = _StatsPacketsTransmittedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 11),
    _StatsPacketsTransmittedPerDay_Type()
)
statsPacketsTransmittedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPacketsTransmittedPerDay.setStatus("mandatory")


class _StatsPacketsReceivedPerMinute_Type(Integer32):
    """Custom type statsPacketsReceivedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPacketsReceivedPerMinute_Type.__name__ = "Integer32"
_StatsPacketsReceivedPerMinute_Object = MibScalar
statsPacketsReceivedPerMinute = _StatsPacketsReceivedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 12),
    _StatsPacketsReceivedPerMinute_Type()
)
statsPacketsReceivedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPacketsReceivedPerMinute.setStatus("mandatory")


class _StatsPacketsReceivedPerHour_Type(Integer32):
    """Custom type statsPacketsReceivedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPacketsReceivedPerHour_Type.__name__ = "Integer32"
_StatsPacketsReceivedPerHour_Object = MibScalar
statsPacketsReceivedPerHour = _StatsPacketsReceivedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 13),
    _StatsPacketsReceivedPerHour_Type()
)
statsPacketsReceivedPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPacketsReceivedPerHour.setStatus("mandatory")


class _StatsPacketsReceivedPerDay_Type(Integer32):
    """Custom type statsPacketsReceivedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPacketsReceivedPerDay_Type.__name__ = "Integer32"
_StatsPacketsReceivedPerDay_Object = MibScalar
statsPacketsReceivedPerDay = _StatsPacketsReceivedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 14),
    _StatsPacketsReceivedPerDay_Type()
)
statsPacketsReceivedPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPacketsReceivedPerDay.setStatus("mandatory")


class _StatsPacketReceivedPerSecond_Type(Integer32):
    """Custom type statsPacketReceivedPerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPacketReceivedPerSecond_Type.__name__ = "Integer32"
_StatsPacketReceivedPerSecond_Object = MibScalar
statsPacketReceivedPerSecond = _StatsPacketReceivedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 15),
    _StatsPacketReceivedPerSecond_Type()
)
statsPacketReceivedPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPacketReceivedPerSecond.setStatus("mandatory")


class _StatsPacketTransmittedPerSecond_Type(Integer32):
    """Custom type statsPacketTransmittedPerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPacketTransmittedPerSecond_Type.__name__ = "Integer32"
_StatsPacketTransmittedPerSecond_Object = MibScalar
statsPacketTransmittedPerSecond = _StatsPacketTransmittedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 16),
    _StatsPacketTransmittedPerSecond_Type()
)
statsPacketTransmittedPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPacketTransmittedPerSecond.setStatus("mandatory")


class _StatsTotalPacketReceived_Type(Integer32):
    """Custom type statsTotalPacketReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalPacketReceived_Type.__name__ = "Integer32"
_StatsTotalPacketReceived_Object = MibScalar
statsTotalPacketReceived = _StatsTotalPacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 17),
    _StatsTotalPacketReceived_Type()
)
statsTotalPacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalPacketReceived.setStatus("mandatory")


class _StatsTotalPacketTransmitted_Type(Integer32):
    """Custom type statsTotalPacketTransmitted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalPacketTransmitted_Type.__name__ = "Integer32"
_StatsTotalPacketTransmitted_Object = MibScalar
statsTotalPacketTransmitted = _StatsTotalPacketTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 18),
    _StatsTotalPacketTransmitted_Type()
)
statsTotalPacketTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalPacketTransmitted.setStatus("mandatory")


class _StatsTotalNumberBytesTransmitted_Type(Integer32):
    """Custom type statsTotalNumberBytesTransmitted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberBytesTransmitted_Type.__name__ = "Integer32"
_StatsTotalNumberBytesTransmitted_Object = MibScalar
statsTotalNumberBytesTransmitted = _StatsTotalNumberBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 19),
    _StatsTotalNumberBytesTransmitted_Type()
)
statsTotalNumberBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberBytesTransmitted.setStatus("mandatory")


class _StatsTotalNumberBytesReceived_Type(Integer32):
    """Custom type statsTotalNumberBytesReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberBytesReceived_Type.__name__ = "Integer32"
_StatsTotalNumberBytesReceived_Object = MibScalar
statsTotalNumberBytesReceived = _StatsTotalNumberBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 4, 20),
    _StatsTotalNumberBytesReceived_Type()
)
statsTotalNumberBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberBytesReceived.setStatus("mandatory")
_StatsForError_ObjectIdentity = ObjectIdentity
statsForError = _StatsForError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5)
)


class _StatsTotalNumberReceivedErrors_Type(Integer32):
    """Custom type statsTotalNumberReceivedErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberReceivedErrors_Type.__name__ = "Integer32"
_StatsTotalNumberReceivedErrors_Object = MibScalar
statsTotalNumberReceivedErrors = _StatsTotalNumberReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 1),
    _StatsTotalNumberReceivedErrors_Type()
)
statsTotalNumberReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberReceivedErrors.setStatus("mandatory")


class _StatsTotalNumberTransmitErrors_Type(Integer32):
    """Custom type statsTotalNumberTransmitErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberTransmitErrors_Type.__name__ = "Integer32"
_StatsTotalNumberTransmitErrors_Object = MibScalar
statsTotalNumberTransmitErrors = _StatsTotalNumberTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 2),
    _StatsTotalNumberTransmitErrors_Type()
)
statsTotalNumberTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberTransmitErrors.setStatus("mandatory")


class _StatsTotalNumberReceivedErrorsPerMinute_Type(Integer32):
    """Custom type statsTotalNumberReceivedErrorsPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberReceivedErrorsPerMinute_Type.__name__ = "Integer32"
_StatsTotalNumberReceivedErrorsPerMinute_Object = MibScalar
statsTotalNumberReceivedErrorsPerMinute = _StatsTotalNumberReceivedErrorsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 3),
    _StatsTotalNumberReceivedErrorsPerMinute_Type()
)
statsTotalNumberReceivedErrorsPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberReceivedErrorsPerMinute.setStatus("mandatory")


class _StatsTotalNumberReceivedErrorsPerHour_Type(Integer32):
    """Custom type statsTotalNumberReceivedErrorsPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberReceivedErrorsPerHour_Type.__name__ = "Integer32"
_StatsTotalNumberReceivedErrorsPerHour_Object = MibScalar
statsTotalNumberReceivedErrorsPerHour = _StatsTotalNumberReceivedErrorsPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 4),
    _StatsTotalNumberReceivedErrorsPerHour_Type()
)
statsTotalNumberReceivedErrorsPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberReceivedErrorsPerHour.setStatus("mandatory")


class _StatsTotalNumberReceivedErrorsPerDay_Type(Integer32):
    """Custom type statsTotalNumberReceivedErrorsPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberReceivedErrorsPerDay_Type.__name__ = "Integer32"
_StatsTotalNumberReceivedErrorsPerDay_Object = MibScalar
statsTotalNumberReceivedErrorsPerDay = _StatsTotalNumberReceivedErrorsPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 5),
    _StatsTotalNumberReceivedErrorsPerDay_Type()
)
statsTotalNumberReceivedErrorsPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberReceivedErrorsPerDay.setStatus("mandatory")


class _StatsTotalNumberTransmitErrorsPerMinute_Type(Integer32):
    """Custom type statsTotalNumberTransmitErrorsPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberTransmitErrorsPerMinute_Type.__name__ = "Integer32"
_StatsTotalNumberTransmitErrorsPerMinute_Object = MibScalar
statsTotalNumberTransmitErrorsPerMinute = _StatsTotalNumberTransmitErrorsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 6),
    _StatsTotalNumberTransmitErrorsPerMinute_Type()
)
statsTotalNumberTransmitErrorsPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberTransmitErrorsPerMinute.setStatus("mandatory")


class _StatsTotalNumberTransmitErrorsPerHour_Type(Integer32):
    """Custom type statsTotalNumberTransmitErrorsPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberTransmitErrorsPerHour_Type.__name__ = "Integer32"
_StatsTotalNumberTransmitErrorsPerHour_Object = MibScalar
statsTotalNumberTransmitErrorsPerHour = _StatsTotalNumberTransmitErrorsPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 7),
    _StatsTotalNumberTransmitErrorsPerHour_Type()
)
statsTotalNumberTransmitErrorsPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberTransmitErrorsPerHour.setStatus("mandatory")


class _StatsTotalNumberTransmitErrorsPerDay_Type(Integer32):
    """Custom type statsTotalNumberTransmitErrorsPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalNumberTransmitErrorsPerDay_Type.__name__ = "Integer32"
_StatsTotalNumberTransmitErrorsPerDay_Object = MibScalar
statsTotalNumberTransmitErrorsPerDay = _StatsTotalNumberTransmitErrorsPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 8),
    _StatsTotalNumberTransmitErrorsPerDay_Type()
)
statsTotalNumberTransmitErrorsPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalNumberTransmitErrorsPerDay.setStatus("mandatory")


class _StatsMaximumErrorRatePerSecond_Type(Integer32):
    """Custom type statsMaximumErrorRatePerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsMaximumErrorRatePerSecond_Type.__name__ = "Integer32"
_StatsMaximumErrorRatePerSecond_Object = MibScalar
statsMaximumErrorRatePerSecond = _StatsMaximumErrorRatePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 9),
    _StatsMaximumErrorRatePerSecond_Type()
)
statsMaximumErrorRatePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsMaximumErrorRatePerSecond.setStatus("mandatory")


class _StatsTotalErrorRatePerSecond_Type(Integer32):
    """Custom type statsTotalErrorRatePerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalErrorRatePerSecond_Type.__name__ = "Integer32"
_StatsTotalErrorRatePerSecond_Object = MibScalar
statsTotalErrorRatePerSecond = _StatsTotalErrorRatePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 5, 10),
    _StatsTotalErrorRatePerSecond_Type()
)
statsTotalErrorRatePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalErrorRatePerSecond.setStatus("mandatory")
_StatsForDriver_ObjectIdentity = ObjectIdentity
statsForDriver = _StatsForDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 6)
)


class _StatsCurrentClock_Type(Integer32):
    """Custom type statsCurrentClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsCurrentClock_Type.__name__ = "Integer32"
_StatsCurrentClock_Object = MibScalar
statsCurrentClock = _StatsCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 6, 1),
    _StatsCurrentClock_Type()
)
statsCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCurrentClock.setStatus("mandatory")


class _StatsCurrentMemoryUsedByDriver_Type(Integer32):
    """Custom type statsCurrentMemoryUsedByDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsCurrentMemoryUsedByDriver_Type.__name__ = "Integer32"
_StatsCurrentMemoryUsedByDriver_Object = MibScalar
statsCurrentMemoryUsedByDriver = _StatsCurrentMemoryUsedByDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 6, 2),
    _StatsCurrentMemoryUsedByDriver_Type()
)
statsCurrentMemoryUsedByDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCurrentMemoryUsedByDriver.setStatus("mandatory")


class _StatsMaximumMemoryUsedByDriver_Type(Integer32):
    """Custom type statsMaximumMemoryUsedByDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsMaximumMemoryUsedByDriver_Type.__name__ = "Integer32"
_StatsMaximumMemoryUsedByDriver_Object = MibScalar
statsMaximumMemoryUsedByDriver = _StatsMaximumMemoryUsedByDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 6, 3),
    _StatsMaximumMemoryUsedByDriver_Type()
)
statsMaximumMemoryUsedByDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsMaximumMemoryUsedByDriver.setStatus("mandatory")


class _StatsPercentCurrentMemoryUsedByDriver_Type(Integer32):
    """Custom type statsPercentCurrentMemoryUsedByDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPercentCurrentMemoryUsedByDriver_Type.__name__ = "Integer32"
_StatsPercentCurrentMemoryUsedByDriver_Object = MibScalar
statsPercentCurrentMemoryUsedByDriver = _StatsPercentCurrentMemoryUsedByDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 6, 4),
    _StatsPercentCurrentMemoryUsedByDriver_Type()
)
statsPercentCurrentMemoryUsedByDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPercentCurrentMemoryUsedByDriver.setStatus("mandatory")


class _StatsPercentMaximumMemoryUsedByDriver_Type(Integer32):
    """Custom type statsPercentMaximumMemoryUsedByDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsPercentMaximumMemoryUsedByDriver_Type.__name__ = "Integer32"
_StatsPercentMaximumMemoryUsedByDriver_Object = MibScalar
statsPercentMaximumMemoryUsedByDriver = _StatsPercentMaximumMemoryUsedByDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 6, 5),
    _StatsPercentMaximumMemoryUsedByDriver_Type()
)
statsPercentMaximumMemoryUsedByDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPercentMaximumMemoryUsedByDriver.setStatus("mandatory")


class _StatsTotalMemoryAvailableToTheDriver_Type(Integer32):
    """Custom type statsTotalMemoryAvailableToTheDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsTotalMemoryAvailableToTheDriver_Type.__name__ = "Integer32"
_StatsTotalMemoryAvailableToTheDriver_Object = MibScalar
statsTotalMemoryAvailableToTheDriver = _StatsTotalMemoryAvailableToTheDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 6, 6),
    _StatsTotalMemoryAvailableToTheDriver_Type()
)
statsTotalMemoryAvailableToTheDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTotalMemoryAvailableToTheDriver.setStatus("mandatory")
_StatsForCompression_ObjectIdentity = ObjectIdentity
statsForCompression = _StatsForCompression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 7)
)


class _StatsBytesIntoCompression_Type(Integer32):
    """Custom type statsBytesIntoCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsBytesIntoCompression_Type.__name__ = "Integer32"
_StatsBytesIntoCompression_Object = MibScalar
statsBytesIntoCompression = _StatsBytesIntoCompression_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 7, 1),
    _StatsBytesIntoCompression_Type()
)
statsBytesIntoCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsBytesIntoCompression.setStatus("mandatory")


class _StatsBytesOutCompression_Type(Integer32):
    """Custom type statsBytesOutCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsBytesOutCompression_Type.__name__ = "Integer32"
_StatsBytesOutCompression_Object = MibScalar
statsBytesOutCompression = _StatsBytesOutCompression_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 7, 2),
    _StatsBytesOutCompression_Type()
)
statsBytesOutCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsBytesOutCompression.setStatus("mandatory")


class _StatsBytesIntoDecompression_Type(Integer32):
    """Custom type statsBytesIntoDecompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsBytesIntoDecompression_Type.__name__ = "Integer32"
_StatsBytesIntoDecompression_Object = MibScalar
statsBytesIntoDecompression = _StatsBytesIntoDecompression_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 7, 3),
    _StatsBytesIntoDecompression_Type()
)
statsBytesIntoDecompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsBytesIntoDecompression.setStatus("mandatory")


class _StatsBytesOutDecompression_Type(Integer32):
    """Custom type statsBytesOutDecompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StatsBytesOutDecompression_Type.__name__ = "Integer32"
_StatsBytesOutDecompression_Object = MibScalar
statsBytesOutDecompression = _StatsBytesOutDecompression_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 1, 7, 4),
    _StatsBytesOutDecompression_Type()
)
statsBytesOutDecompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsBytesOutDecompression.setStatus("mandatory")
_ApolloThresholdForNT_ObjectIdentity = ObjectIdentity
apolloThresholdForNT = _ApolloThresholdForNT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2)
)
_ThresholdForPort_ObjectIdentity = ObjectIdentity
thresholdForPort = _ThresholdForPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 1)
)


class _ThresholdPortsInUse_Type(Integer32):
    """Custom type thresholdPortsInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPortsInUse_Type.__name__ = "Integer32"
_ThresholdPortsInUse_Object = MibScalar
thresholdPortsInUse = _ThresholdPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 1, 1),
    _ThresholdPortsInUse_Type()
)
thresholdPortsInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPortsInUse.setStatus("mandatory")


class _ThresholdMaxPortsUsed_Type(Integer32):
    """Custom type thresholdMaxPortsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdMaxPortsUsed_Type.__name__ = "Integer32"
_ThresholdMaxPortsUsed_Object = MibScalar
thresholdMaxPortsUsed = _ThresholdMaxPortsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 1, 2),
    _ThresholdMaxPortsUsed_Type()
)
thresholdMaxPortsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdMaxPortsUsed.setStatus("mandatory")


class _ThresholdPortsInUseIncoming_Type(Integer32):
    """Custom type thresholdPortsInUseIncoming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPortsInUseIncoming_Type.__name__ = "Integer32"
_ThresholdPortsInUseIncoming_Object = MibScalar
thresholdPortsInUseIncoming = _ThresholdPortsInUseIncoming_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 1, 3),
    _ThresholdPortsInUseIncoming_Type()
)
thresholdPortsInUseIncoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPortsInUseIncoming.setStatus("mandatory")


class _ThresholdPortsInUseOutgoing_Type(Integer32):
    """Custom type thresholdPortsInUseOutgoing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPortsInUseOutgoing_Type.__name__ = "Integer32"
_ThresholdPortsInUseOutgoing_Object = MibScalar
thresholdPortsInUseOutgoing = _ThresholdPortsInUseOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 1, 4),
    _ThresholdPortsInUseOutgoing_Type()
)
thresholdPortsInUseOutgoing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPortsInUseOutgoing.setStatus("mandatory")


class _ThresholdOverrallCompressionRatioOfAllPorts_Type(Integer32):
    """Custom type thresholdOverrallCompressionRatioOfAllPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdOverrallCompressionRatioOfAllPorts_Type.__name__ = "Integer32"
_ThresholdOverrallCompressionRatioOfAllPorts_Object = MibScalar
thresholdOverrallCompressionRatioOfAllPorts = _ThresholdOverrallCompressionRatioOfAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 1, 5),
    _ThresholdOverrallCompressionRatioOfAllPorts_Type()
)
thresholdOverrallCompressionRatioOfAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdOverrallCompressionRatioOfAllPorts.setStatus("mandatory")
_ThresholdForCalls_ObjectIdentity = ObjectIdentity
thresholdForCalls = _ThresholdForCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2)
)


class _ThresholdTotalCallsMade_Type(Integer32):
    """Custom type thresholdTotalCallsMade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalCallsMade_Type.__name__ = "Integer32"
_ThresholdTotalCallsMade_Object = MibScalar
thresholdTotalCallsMade = _ThresholdTotalCallsMade_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 1),
    _ThresholdTotalCallsMade_Type()
)
thresholdTotalCallsMade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalCallsMade.setStatus("mandatory")


class _ThresholdFailedOutgoingCalls_Type(Integer32):
    """Custom type thresholdFailedOutgoingCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdFailedOutgoingCalls_Type.__name__ = "Integer32"
_ThresholdFailedOutgoingCalls_Object = MibScalar
thresholdFailedOutgoingCalls = _ThresholdFailedOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 2),
    _ThresholdFailedOutgoingCalls_Type()
)
thresholdFailedOutgoingCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdFailedOutgoingCalls.setStatus("mandatory")


class _ThresholdTotalCallsReceivedPerMinute_Type(Integer32):
    """Custom type thresholdTotalCallsReceivedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalCallsReceivedPerMinute_Type.__name__ = "Integer32"
_ThresholdTotalCallsReceivedPerMinute_Object = MibScalar
thresholdTotalCallsReceivedPerMinute = _ThresholdTotalCallsReceivedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 3),
    _ThresholdTotalCallsReceivedPerMinute_Type()
)
thresholdTotalCallsReceivedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalCallsReceivedPerMinute.setStatus("mandatory")


class _ThresholdTotalCallsReceivedPerHour_Type(Integer32):
    """Custom type thresholdTotalCallsReceivedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalCallsReceivedPerHour_Type.__name__ = "Integer32"
_ThresholdTotalCallsReceivedPerHour_Object = MibScalar
thresholdTotalCallsReceivedPerHour = _ThresholdTotalCallsReceivedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 4),
    _ThresholdTotalCallsReceivedPerHour_Type()
)
thresholdTotalCallsReceivedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalCallsReceivedPerHour.setStatus("mandatory")


class _ThresholdTotalCallsReceivedPerDay_Type(Integer32):
    """Custom type thresholdTotalCallsReceivedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalCallsReceivedPerDay_Type.__name__ = "Integer32"
_ThresholdTotalCallsReceivedPerDay_Object = MibScalar
thresholdTotalCallsReceivedPerDay = _ThresholdTotalCallsReceivedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 5),
    _ThresholdTotalCallsReceivedPerDay_Type()
)
thresholdTotalCallsReceivedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalCallsReceivedPerDay.setStatus("mandatory")


class _ThresholdTotalCallsMadePerMinute_Type(Integer32):
    """Custom type thresholdTotalCallsMadePerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalCallsMadePerMinute_Type.__name__ = "Integer32"
_ThresholdTotalCallsMadePerMinute_Object = MibScalar
thresholdTotalCallsMadePerMinute = _ThresholdTotalCallsMadePerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 6),
    _ThresholdTotalCallsMadePerMinute_Type()
)
thresholdTotalCallsMadePerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalCallsMadePerMinute.setStatus("mandatory")


class _ThresholdTotalCallsMadePerHour_Type(Integer32):
    """Custom type thresholdTotalCallsMadePerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalCallsMadePerHour_Type.__name__ = "Integer32"
_ThresholdTotalCallsMadePerHour_Object = MibScalar
thresholdTotalCallsMadePerHour = _ThresholdTotalCallsMadePerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 7),
    _ThresholdTotalCallsMadePerHour_Type()
)
thresholdTotalCallsMadePerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalCallsMadePerHour.setStatus("mandatory")


class _ThresholdTotalCallsMadePerDay_Type(Integer32):
    """Custom type thresholdTotalCallsMadePerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalCallsMadePerDay_Type.__name__ = "Integer32"
_ThresholdTotalCallsMadePerDay_Object = MibScalar
thresholdTotalCallsMadePerDay = _ThresholdTotalCallsMadePerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 8),
    _ThresholdTotalCallsMadePerDay_Type()
)
thresholdTotalCallsMadePerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalCallsMadePerDay.setStatus("mandatory")


class _ThresholdTotalCallsReceived_Type(Integer32):
    """Custom type thresholdTotalCallsReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalCallsReceived_Type.__name__ = "Integer32"
_ThresholdTotalCallsReceived_Object = MibScalar
thresholdTotalCallsReceived = _ThresholdTotalCallsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 2, 9),
    _ThresholdTotalCallsReceived_Type()
)
thresholdTotalCallsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalCallsReceived.setStatus("mandatory")
_ThresholdForSession_ObjectIdentity = ObjectIdentity
thresholdForSession = _ThresholdForSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3)
)
_ThresholdSessionForGeneral_ObjectIdentity = ObjectIdentity
thresholdSessionForGeneral = _ThresholdSessionForGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1)
)


class _ThresholdMaxSessionsUsed_Type(Integer32):
    """Custom type thresholdMaxSessionsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdMaxSessionsUsed_Type.__name__ = "Integer32"
_ThresholdMaxSessionsUsed_Object = MibScalar
thresholdMaxSessionsUsed = _ThresholdMaxSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 1),
    _ThresholdMaxSessionsUsed_Type()
)
thresholdMaxSessionsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdMaxSessionsUsed.setStatus("mandatory")


class _ThresholdTotalNumberUserSessionGranted_Type(Integer32):
    """Custom type thresholdTotalNumberUserSessionGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberUserSessionGranted_Type.__name__ = "Integer32"
_ThresholdTotalNumberUserSessionGranted_Object = MibScalar
thresholdTotalNumberUserSessionGranted = _ThresholdTotalNumberUserSessionGranted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 2),
    _ThresholdTotalNumberUserSessionGranted_Type()
)
thresholdTotalNumberUserSessionGranted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberUserSessionGranted.setStatus("mandatory")


class _ThresholdTotalNumberUserSessionRefused_Type(Integer32):
    """Custom type thresholdTotalNumberUserSessionRefused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberUserSessionRefused_Type.__name__ = "Integer32"
_ThresholdTotalNumberUserSessionRefused_Object = MibScalar
thresholdTotalNumberUserSessionRefused = _ThresholdTotalNumberUserSessionRefused_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 3),
    _ThresholdTotalNumberUserSessionRefused_Type()
)
thresholdTotalNumberUserSessionRefused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberUserSessionRefused.setStatus("mandatory")


class _ThresholdTotalNumberUserSessionsGrantedPerMinute_Type(Integer32):
    """Custom type thresholdTotalNumberUserSessionsGrantedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberUserSessionsGrantedPerMinute_Type.__name__ = "Integer32"
_ThresholdTotalNumberUserSessionsGrantedPerMinute_Object = MibScalar
thresholdTotalNumberUserSessionsGrantedPerMinute = _ThresholdTotalNumberUserSessionsGrantedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 4),
    _ThresholdTotalNumberUserSessionsGrantedPerMinute_Type()
)
thresholdTotalNumberUserSessionsGrantedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberUserSessionsGrantedPerMinute.setStatus("mandatory")


class _ThresholdTotalNumberUserSessionGrantedPerHour_Type(Integer32):
    """Custom type thresholdTotalNumberUserSessionGrantedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberUserSessionGrantedPerHour_Type.__name__ = "Integer32"
_ThresholdTotalNumberUserSessionGrantedPerHour_Object = MibScalar
thresholdTotalNumberUserSessionGrantedPerHour = _ThresholdTotalNumberUserSessionGrantedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 5),
    _ThresholdTotalNumberUserSessionGrantedPerHour_Type()
)
thresholdTotalNumberUserSessionGrantedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberUserSessionGrantedPerHour.setStatus("mandatory")


class _ThresholdTotalNumberUserSessionGrantedPerDay_Type(Integer32):
    """Custom type thresholdTotalNumberUserSessionGrantedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberUserSessionGrantedPerDay_Type.__name__ = "Integer32"
_ThresholdTotalNumberUserSessionGrantedPerDay_Object = MibScalar
thresholdTotalNumberUserSessionGrantedPerDay = _ThresholdTotalNumberUserSessionGrantedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 6),
    _ThresholdTotalNumberUserSessionGrantedPerDay_Type()
)
thresholdTotalNumberUserSessionGrantedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberUserSessionGrantedPerDay.setStatus("mandatory")


class _ThresholdTotalNumberUserSessionRefusedPerMinute_Type(Integer32):
    """Custom type thresholdTotalNumberUserSessionRefusedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberUserSessionRefusedPerMinute_Type.__name__ = "Integer32"
_ThresholdTotalNumberUserSessionRefusedPerMinute_Object = MibScalar
thresholdTotalNumberUserSessionRefusedPerMinute = _ThresholdTotalNumberUserSessionRefusedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 7),
    _ThresholdTotalNumberUserSessionRefusedPerMinute_Type()
)
thresholdTotalNumberUserSessionRefusedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberUserSessionRefusedPerMinute.setStatus("mandatory")


class _ThresholdTotalNumberUserSessionRefusedPerHour_Type(Integer32):
    """Custom type thresholdTotalNumberUserSessionRefusedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberUserSessionRefusedPerHour_Type.__name__ = "Integer32"
_ThresholdTotalNumberUserSessionRefusedPerHour_Object = MibScalar
thresholdTotalNumberUserSessionRefusedPerHour = _ThresholdTotalNumberUserSessionRefusedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 8),
    _ThresholdTotalNumberUserSessionRefusedPerHour_Type()
)
thresholdTotalNumberUserSessionRefusedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberUserSessionRefusedPerHour.setStatus("mandatory")


class _ThresholdTotalNumberUserSessionRefusedPerDay_Type(Integer32):
    """Custom type thresholdTotalNumberUserSessionRefusedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberUserSessionRefusedPerDay_Type.__name__ = "Integer32"
_ThresholdTotalNumberUserSessionRefusedPerDay_Object = MibScalar
thresholdTotalNumberUserSessionRefusedPerDay = _ThresholdTotalNumberUserSessionRefusedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 9),
    _ThresholdTotalNumberUserSessionRefusedPerDay_Type()
)
thresholdTotalNumberUserSessionRefusedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberUserSessionRefusedPerDay.setStatus("mandatory")


class _ThresholdTotalActiveUserSession_Type(Integer32):
    """Custom type thresholdTotalActiveUserSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalActiveUserSession_Type.__name__ = "Integer32"
_ThresholdTotalActiveUserSession_Object = MibScalar
thresholdTotalActiveUserSession = _ThresholdTotalActiveUserSession_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 1, 10),
    _ThresholdTotalActiveUserSession_Type()
)
thresholdTotalActiveUserSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalActiveUserSession.setStatus("mandatory")
_ThresholdSessionForApollo_ObjectIdentity = ObjectIdentity
thresholdSessionForApollo = _ThresholdSessionForApollo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2)
)


class _ThresholdApolloActiveUserSessions_Type(Integer32):
    """Custom type thresholdApolloActiveUserSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloActiveUserSessions_Type.__name__ = "Integer32"
_ThresholdApolloActiveUserSessions_Object = MibScalar
thresholdApolloActiveUserSessions = _ThresholdApolloActiveUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 1),
    _ThresholdApolloActiveUserSessions_Type()
)
thresholdApolloActiveUserSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloActiveUserSessions.setStatus("mandatory")


class _ThresholdApolloNumberUserSessionsGranted_Type(Integer32):
    """Custom type thresholdApolloNumberUserSessionsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloNumberUserSessionsGranted_Type.__name__ = "Integer32"
_ThresholdApolloNumberUserSessionsGranted_Object = MibScalar
thresholdApolloNumberUserSessionsGranted = _ThresholdApolloNumberUserSessionsGranted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 2),
    _ThresholdApolloNumberUserSessionsGranted_Type()
)
thresholdApolloNumberUserSessionsGranted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloNumberUserSessionsGranted.setStatus("mandatory")


class _ThresholdApolloNumberUserSessionsrefused_Type(Integer32):
    """Custom type thresholdApolloNumberUserSessionsrefused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloNumberUserSessionsrefused_Type.__name__ = "Integer32"
_ThresholdApolloNumberUserSessionsrefused_Object = MibScalar
thresholdApolloNumberUserSessionsrefused = _ThresholdApolloNumberUserSessionsrefused_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 3),
    _ThresholdApolloNumberUserSessionsrefused_Type()
)
thresholdApolloNumberUserSessionsrefused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloNumberUserSessionsrefused.setStatus("mandatory")


class _ThresholdApolloNumberUserSessionsGrantedPerMinute_Type(Integer32):
    """Custom type thresholdApolloNumberUserSessionsGrantedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloNumberUserSessionsGrantedPerMinute_Type.__name__ = "Integer32"
_ThresholdApolloNumberUserSessionsGrantedPerMinute_Object = MibScalar
thresholdApolloNumberUserSessionsGrantedPerMinute = _ThresholdApolloNumberUserSessionsGrantedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 4),
    _ThresholdApolloNumberUserSessionsGrantedPerMinute_Type()
)
thresholdApolloNumberUserSessionsGrantedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloNumberUserSessionsGrantedPerMinute.setStatus("mandatory")


class _ThresholdApolloNumberUserSessionsGrantedPerHour_Type(Integer32):
    """Custom type thresholdApolloNumberUserSessionsGrantedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloNumberUserSessionsGrantedPerHour_Type.__name__ = "Integer32"
_ThresholdApolloNumberUserSessionsGrantedPerHour_Object = MibScalar
thresholdApolloNumberUserSessionsGrantedPerHour = _ThresholdApolloNumberUserSessionsGrantedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 5),
    _ThresholdApolloNumberUserSessionsGrantedPerHour_Type()
)
thresholdApolloNumberUserSessionsGrantedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloNumberUserSessionsGrantedPerHour.setStatus("mandatory")


class _ThresholdApolloNumberUserSessionsGrantedPerDay_Type(Integer32):
    """Custom type thresholdApolloNumberUserSessionsGrantedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloNumberUserSessionsGrantedPerDay_Type.__name__ = "Integer32"
_ThresholdApolloNumberUserSessionsGrantedPerDay_Object = MibScalar
thresholdApolloNumberUserSessionsGrantedPerDay = _ThresholdApolloNumberUserSessionsGrantedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 6),
    _ThresholdApolloNumberUserSessionsGrantedPerDay_Type()
)
thresholdApolloNumberUserSessionsGrantedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloNumberUserSessionsGrantedPerDay.setStatus("mandatory")


class _ThresholdApolloNumberUserSessionsRefusedPerMinute_Type(Integer32):
    """Custom type thresholdApolloNumberUserSessionsRefusedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloNumberUserSessionsRefusedPerMinute_Type.__name__ = "Integer32"
_ThresholdApolloNumberUserSessionsRefusedPerMinute_Object = MibScalar
thresholdApolloNumberUserSessionsRefusedPerMinute = _ThresholdApolloNumberUserSessionsRefusedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 7),
    _ThresholdApolloNumberUserSessionsRefusedPerMinute_Type()
)
thresholdApolloNumberUserSessionsRefusedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloNumberUserSessionsRefusedPerMinute.setStatus("mandatory")


class _ThresholdApolloNumberUserSessionsRefusedPerHour_Type(Integer32):
    """Custom type thresholdApolloNumberUserSessionsRefusedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloNumberUserSessionsRefusedPerHour_Type.__name__ = "Integer32"
_ThresholdApolloNumberUserSessionsRefusedPerHour_Object = MibScalar
thresholdApolloNumberUserSessionsRefusedPerHour = _ThresholdApolloNumberUserSessionsRefusedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 8),
    _ThresholdApolloNumberUserSessionsRefusedPerHour_Type()
)
thresholdApolloNumberUserSessionsRefusedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloNumberUserSessionsRefusedPerHour.setStatus("mandatory")


class _ThresholdApolloNumberUserSessionsRefusedPerDay_Type(Integer32):
    """Custom type thresholdApolloNumberUserSessionsRefusedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloNumberUserSessionsRefusedPerDay_Type.__name__ = "Integer32"
_ThresholdApolloNumberUserSessionsRefusedPerDay_Object = MibScalar
thresholdApolloNumberUserSessionsRefusedPerDay = _ThresholdApolloNumberUserSessionsRefusedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 9),
    _ThresholdApolloNumberUserSessionsRefusedPerDay_Type()
)
thresholdApolloNumberUserSessionsRefusedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloNumberUserSessionsRefusedPerDay.setStatus("mandatory")


class _ThresholdApolloMaximumSessionsUsed_Type(Integer32):
    """Custom type thresholdApolloMaximumSessionsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdApolloMaximumSessionsUsed_Type.__name__ = "Integer32"
_ThresholdApolloMaximumSessionsUsed_Object = MibScalar
thresholdApolloMaximumSessionsUsed = _ThresholdApolloMaximumSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 2, 10),
    _ThresholdApolloMaximumSessionsUsed_Type()
)
thresholdApolloMaximumSessionsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdApolloMaximumSessionsUsed.setStatus("mandatory")
_ThresholdSessionForPPP_ObjectIdentity = ObjectIdentity
thresholdSessionForPPP = _ThresholdSessionForPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3)
)


class _ThresholdPPPActiveUserSessions_Type(Integer32):
    """Custom type thresholdPPPActiveUserSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPActiveUserSessions_Type.__name__ = "Integer32"
_ThresholdPPPActiveUserSessions_Object = MibScalar
thresholdPPPActiveUserSessions = _ThresholdPPPActiveUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 1),
    _ThresholdPPPActiveUserSessions_Type()
)
thresholdPPPActiveUserSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPActiveUserSessions.setStatus("mandatory")


class _ThresholdPPPNumberUserSessionsGranted_Type(Integer32):
    """Custom type thresholdPPPNumberUserSessionsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPNumberUserSessionsGranted_Type.__name__ = "Integer32"
_ThresholdPPPNumberUserSessionsGranted_Object = MibScalar
thresholdPPPNumberUserSessionsGranted = _ThresholdPPPNumberUserSessionsGranted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 2),
    _ThresholdPPPNumberUserSessionsGranted_Type()
)
thresholdPPPNumberUserSessionsGranted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPNumberUserSessionsGranted.setStatus("mandatory")


class _ThresholdPPPNumberUserSessionsRefused_Type(Integer32):
    """Custom type thresholdPPPNumberUserSessionsRefused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPNumberUserSessionsRefused_Type.__name__ = "Integer32"
_ThresholdPPPNumberUserSessionsRefused_Object = MibScalar
thresholdPPPNumberUserSessionsRefused = _ThresholdPPPNumberUserSessionsRefused_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 3),
    _ThresholdPPPNumberUserSessionsRefused_Type()
)
thresholdPPPNumberUserSessionsRefused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPNumberUserSessionsRefused.setStatus("mandatory")


class _ThresholdPPPNumberUserSessionsGrantedPerMinute_Type(Integer32):
    """Custom type thresholdPPPNumberUserSessionsGrantedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPNumberUserSessionsGrantedPerMinute_Type.__name__ = "Integer32"
_ThresholdPPPNumberUserSessionsGrantedPerMinute_Object = MibScalar
thresholdPPPNumberUserSessionsGrantedPerMinute = _ThresholdPPPNumberUserSessionsGrantedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 4),
    _ThresholdPPPNumberUserSessionsGrantedPerMinute_Type()
)
thresholdPPPNumberUserSessionsGrantedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPNumberUserSessionsGrantedPerMinute.setStatus("mandatory")


class _ThresholdPPPNumberUserSessionsGrantedPerHour_Type(Integer32):
    """Custom type thresholdPPPNumberUserSessionsGrantedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPNumberUserSessionsGrantedPerHour_Type.__name__ = "Integer32"
_ThresholdPPPNumberUserSessionsGrantedPerHour_Object = MibScalar
thresholdPPPNumberUserSessionsGrantedPerHour = _ThresholdPPPNumberUserSessionsGrantedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 5),
    _ThresholdPPPNumberUserSessionsGrantedPerHour_Type()
)
thresholdPPPNumberUserSessionsGrantedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPNumberUserSessionsGrantedPerHour.setStatus("mandatory")


class _ThresholdPPPNumberUserSessionsGrantedPerDay_Type(Integer32):
    """Custom type thresholdPPPNumberUserSessionsGrantedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPNumberUserSessionsGrantedPerDay_Type.__name__ = "Integer32"
_ThresholdPPPNumberUserSessionsGrantedPerDay_Object = MibScalar
thresholdPPPNumberUserSessionsGrantedPerDay = _ThresholdPPPNumberUserSessionsGrantedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 6),
    _ThresholdPPPNumberUserSessionsGrantedPerDay_Type()
)
thresholdPPPNumberUserSessionsGrantedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPNumberUserSessionsGrantedPerDay.setStatus("mandatory")


class _ThresholdPPPNumberUserSessionsRefusedPerMinute_Type(Integer32):
    """Custom type thresholdPPPNumberUserSessionsRefusedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPNumberUserSessionsRefusedPerMinute_Type.__name__ = "Integer32"
_ThresholdPPPNumberUserSessionsRefusedPerMinute_Object = MibScalar
thresholdPPPNumberUserSessionsRefusedPerMinute = _ThresholdPPPNumberUserSessionsRefusedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 7),
    _ThresholdPPPNumberUserSessionsRefusedPerMinute_Type()
)
thresholdPPPNumberUserSessionsRefusedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPNumberUserSessionsRefusedPerMinute.setStatus("mandatory")


class _ThresholdPPPNumberUserSessionsRefusedPerHour_Type(Integer32):
    """Custom type thresholdPPPNumberUserSessionsRefusedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPNumberUserSessionsRefusedPerHour_Type.__name__ = "Integer32"
_ThresholdPPPNumberUserSessionsRefusedPerHour_Object = MibScalar
thresholdPPPNumberUserSessionsRefusedPerHour = _ThresholdPPPNumberUserSessionsRefusedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 8),
    _ThresholdPPPNumberUserSessionsRefusedPerHour_Type()
)
thresholdPPPNumberUserSessionsRefusedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPNumberUserSessionsRefusedPerHour.setStatus("mandatory")


class _ThresholdPPPNumberUserSessionsRefusedPerDay_Type(Integer32):
    """Custom type thresholdPPPNumberUserSessionsRefusedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPNumberUserSessionsRefusedPerDay_Type.__name__ = "Integer32"
_ThresholdPPPNumberUserSessionsRefusedPerDay_Object = MibScalar
thresholdPPPNumberUserSessionsRefusedPerDay = _ThresholdPPPNumberUserSessionsRefusedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 9),
    _ThresholdPPPNumberUserSessionsRefusedPerDay_Type()
)
thresholdPPPNumberUserSessionsRefusedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPNumberUserSessionsRefusedPerDay.setStatus("mandatory")


class _ThresholdPPPMaximumSessionsUsed_Type(Integer32):
    """Custom type thresholdPPPMaximumSessionsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPPPMaximumSessionsUsed_Type.__name__ = "Integer32"
_ThresholdPPPMaximumSessionsUsed_Object = MibScalar
thresholdPPPMaximumSessionsUsed = _ThresholdPPPMaximumSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 3, 3, 10),
    _ThresholdPPPMaximumSessionsUsed_Type()
)
thresholdPPPMaximumSessionsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPPPMaximumSessionsUsed.setStatus("mandatory")
_ThresholdForData_ObjectIdentity = ObjectIdentity
thresholdForData = _ThresholdForData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4)
)


class _ThresholdNumberBytesReceivedPerSecond_Type(Integer32):
    """Custom type thresholdNumberBytesReceivedPerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumberBytesReceivedPerSecond_Type.__name__ = "Integer32"
_ThresholdNumberBytesReceivedPerSecond_Object = MibScalar
thresholdNumberBytesReceivedPerSecond = _ThresholdNumberBytesReceivedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 1),
    _ThresholdNumberBytesReceivedPerSecond_Type()
)
thresholdNumberBytesReceivedPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdNumberBytesReceivedPerSecond.setStatus("mandatory")


class _ThresholdNumberBytesReceivedPerMinute_Type(Integer32):
    """Custom type thresholdNumberBytesReceivedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumberBytesReceivedPerMinute_Type.__name__ = "Integer32"
_ThresholdNumberBytesReceivedPerMinute_Object = MibScalar
thresholdNumberBytesReceivedPerMinute = _ThresholdNumberBytesReceivedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 2),
    _ThresholdNumberBytesReceivedPerMinute_Type()
)
thresholdNumberBytesReceivedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdNumberBytesReceivedPerMinute.setStatus("mandatory")


class _ThresholdNumberBytesReceivedPerHour_Type(Integer32):
    """Custom type thresholdNumberBytesReceivedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumberBytesReceivedPerHour_Type.__name__ = "Integer32"
_ThresholdNumberBytesReceivedPerHour_Object = MibScalar
thresholdNumberBytesReceivedPerHour = _ThresholdNumberBytesReceivedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 3),
    _ThresholdNumberBytesReceivedPerHour_Type()
)
thresholdNumberBytesReceivedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdNumberBytesReceivedPerHour.setStatus("mandatory")


class _ThresholdNumberBytesReceivedPerDay_Type(Integer32):
    """Custom type thresholdNumberBytesReceivedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumberBytesReceivedPerDay_Type.__name__ = "Integer32"
_ThresholdNumberBytesReceivedPerDay_Object = MibScalar
thresholdNumberBytesReceivedPerDay = _ThresholdNumberBytesReceivedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 4),
    _ThresholdNumberBytesReceivedPerDay_Type()
)
thresholdNumberBytesReceivedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdNumberBytesReceivedPerDay.setStatus("mandatory")


class _ThresholdNumberBytesTransmittedPerSecond_Type(Integer32):
    """Custom type thresholdNumberBytesTransmittedPerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumberBytesTransmittedPerSecond_Type.__name__ = "Integer32"
_ThresholdNumberBytesTransmittedPerSecond_Object = MibScalar
thresholdNumberBytesTransmittedPerSecond = _ThresholdNumberBytesTransmittedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 5),
    _ThresholdNumberBytesTransmittedPerSecond_Type()
)
thresholdNumberBytesTransmittedPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdNumberBytesTransmittedPerSecond.setStatus("mandatory")


class _ThresholdNumberBytesTransmittedPerMinute_Type(Integer32):
    """Custom type thresholdNumberBytesTransmittedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumberBytesTransmittedPerMinute_Type.__name__ = "Integer32"
_ThresholdNumberBytesTransmittedPerMinute_Object = MibScalar
thresholdNumberBytesTransmittedPerMinute = _ThresholdNumberBytesTransmittedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 6),
    _ThresholdNumberBytesTransmittedPerMinute_Type()
)
thresholdNumberBytesTransmittedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdNumberBytesTransmittedPerMinute.setStatus("mandatory")


class _ThresholdNumberBytesTransmittedPerHour_Type(Integer32):
    """Custom type thresholdNumberBytesTransmittedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumberBytesTransmittedPerHour_Type.__name__ = "Integer32"
_ThresholdNumberBytesTransmittedPerHour_Object = MibScalar
thresholdNumberBytesTransmittedPerHour = _ThresholdNumberBytesTransmittedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 7),
    _ThresholdNumberBytesTransmittedPerHour_Type()
)
thresholdNumberBytesTransmittedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdNumberBytesTransmittedPerHour.setStatus("mandatory")


class _ThresholdNumberBytesTransmittedPerDay_Type(Integer32):
    """Custom type thresholdNumberBytesTransmittedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumberBytesTransmittedPerDay_Type.__name__ = "Integer32"
_ThresholdNumberBytesTransmittedPerDay_Object = MibScalar
thresholdNumberBytesTransmittedPerDay = _ThresholdNumberBytesTransmittedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 8),
    _ThresholdNumberBytesTransmittedPerDay_Type()
)
thresholdNumberBytesTransmittedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdNumberBytesTransmittedPerDay.setStatus("mandatory")


class _ThresholdPacketsTransmittedPerMinute_Type(Integer32):
    """Custom type thresholdPacketsTransmittedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPacketsTransmittedPerMinute_Type.__name__ = "Integer32"
_ThresholdPacketsTransmittedPerMinute_Object = MibScalar
thresholdPacketsTransmittedPerMinute = _ThresholdPacketsTransmittedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 9),
    _ThresholdPacketsTransmittedPerMinute_Type()
)
thresholdPacketsTransmittedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPacketsTransmittedPerMinute.setStatus("mandatory")


class _ThresholdPacketsTransmittedPerHour_Type(Integer32):
    """Custom type thresholdPacketsTransmittedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPacketsTransmittedPerHour_Type.__name__ = "Integer32"
_ThresholdPacketsTransmittedPerHour_Object = MibScalar
thresholdPacketsTransmittedPerHour = _ThresholdPacketsTransmittedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 10),
    _ThresholdPacketsTransmittedPerHour_Type()
)
thresholdPacketsTransmittedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPacketsTransmittedPerHour.setStatus("mandatory")


class _ThresholdPacketsTransmittedPerDay_Type(Integer32):
    """Custom type thresholdPacketsTransmittedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPacketsTransmittedPerDay_Type.__name__ = "Integer32"
_ThresholdPacketsTransmittedPerDay_Object = MibScalar
thresholdPacketsTransmittedPerDay = _ThresholdPacketsTransmittedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 11),
    _ThresholdPacketsTransmittedPerDay_Type()
)
thresholdPacketsTransmittedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPacketsTransmittedPerDay.setStatus("mandatory")


class _ThresholdPacketsReceivedPerMinute_Type(Integer32):
    """Custom type thresholdPacketsReceivedPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPacketsReceivedPerMinute_Type.__name__ = "Integer32"
_ThresholdPacketsReceivedPerMinute_Object = MibScalar
thresholdPacketsReceivedPerMinute = _ThresholdPacketsReceivedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 12),
    _ThresholdPacketsReceivedPerMinute_Type()
)
thresholdPacketsReceivedPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPacketsReceivedPerMinute.setStatus("mandatory")


class _ThresholdPacketsReceivedPerHour_Type(Integer32):
    """Custom type thresholdPacketsReceivedPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPacketsReceivedPerHour_Type.__name__ = "Integer32"
_ThresholdPacketsReceivedPerHour_Object = MibScalar
thresholdPacketsReceivedPerHour = _ThresholdPacketsReceivedPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 13),
    _ThresholdPacketsReceivedPerHour_Type()
)
thresholdPacketsReceivedPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPacketsReceivedPerHour.setStatus("mandatory")


class _ThresholdPacketsReceivedPerDay_Type(Integer32):
    """Custom type thresholdPacketsReceivedPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPacketsReceivedPerDay_Type.__name__ = "Integer32"
_ThresholdPacketsReceivedPerDay_Object = MibScalar
thresholdPacketsReceivedPerDay = _ThresholdPacketsReceivedPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 14),
    _ThresholdPacketsReceivedPerDay_Type()
)
thresholdPacketsReceivedPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPacketsReceivedPerDay.setStatus("mandatory")


class _ThresholdPacketReceivedPerSecond_Type(Integer32):
    """Custom type thresholdPacketReceivedPerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPacketReceivedPerSecond_Type.__name__ = "Integer32"
_ThresholdPacketReceivedPerSecond_Object = MibScalar
thresholdPacketReceivedPerSecond = _ThresholdPacketReceivedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 15),
    _ThresholdPacketReceivedPerSecond_Type()
)
thresholdPacketReceivedPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPacketReceivedPerSecond.setStatus("mandatory")


class _ThresholdPacketTransmittedPerSecond_Type(Integer32):
    """Custom type thresholdPacketTransmittedPerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPacketTransmittedPerSecond_Type.__name__ = "Integer32"
_ThresholdPacketTransmittedPerSecond_Object = MibScalar
thresholdPacketTransmittedPerSecond = _ThresholdPacketTransmittedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 16),
    _ThresholdPacketTransmittedPerSecond_Type()
)
thresholdPacketTransmittedPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPacketTransmittedPerSecond.setStatus("mandatory")


class _ThresholdTotalPacketReceived_Type(Integer32):
    """Custom type thresholdTotalPacketReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalPacketReceived_Type.__name__ = "Integer32"
_ThresholdTotalPacketReceived_Object = MibScalar
thresholdTotalPacketReceived = _ThresholdTotalPacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 17),
    _ThresholdTotalPacketReceived_Type()
)
thresholdTotalPacketReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalPacketReceived.setStatus("mandatory")


class _ThresholdTotalPacketTransmitted_Type(Integer32):
    """Custom type thresholdTotalPacketTransmitted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalPacketTransmitted_Type.__name__ = "Integer32"
_ThresholdTotalPacketTransmitted_Object = MibScalar
thresholdTotalPacketTransmitted = _ThresholdTotalPacketTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 18),
    _ThresholdTotalPacketTransmitted_Type()
)
thresholdTotalPacketTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalPacketTransmitted.setStatus("mandatory")


class _ThresholdTotalNumberBytesTransmitted_Type(Integer32):
    """Custom type thresholdTotalNumberBytesTransmitted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberBytesTransmitted_Type.__name__ = "Integer32"
_ThresholdTotalNumberBytesTransmitted_Object = MibScalar
thresholdTotalNumberBytesTransmitted = _ThresholdTotalNumberBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 19),
    _ThresholdTotalNumberBytesTransmitted_Type()
)
thresholdTotalNumberBytesTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberBytesTransmitted.setStatus("mandatory")


class _ThresholdTotalNumberBytesReceived_Type(Integer32):
    """Custom type thresholdTotalNumberBytesReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberBytesReceived_Type.__name__ = "Integer32"
_ThresholdTotalNumberBytesReceived_Object = MibScalar
thresholdTotalNumberBytesReceived = _ThresholdTotalNumberBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 4, 20),
    _ThresholdTotalNumberBytesReceived_Type()
)
thresholdTotalNumberBytesReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberBytesReceived.setStatus("mandatory")
_ThresholdForError_ObjectIdentity = ObjectIdentity
thresholdForError = _ThresholdForError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5)
)


class _ThresholdTotalNumberReceivedErrors_Type(Integer32):
    """Custom type thresholdTotalNumberReceivedErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberReceivedErrors_Type.__name__ = "Integer32"
_ThresholdTotalNumberReceivedErrors_Object = MibScalar
thresholdTotalNumberReceivedErrors = _ThresholdTotalNumberReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 1),
    _ThresholdTotalNumberReceivedErrors_Type()
)
thresholdTotalNumberReceivedErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberReceivedErrors.setStatus("mandatory")


class _ThresholdTotalNumberTransmitErrors_Type(Integer32):
    """Custom type thresholdTotalNumberTransmitErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberTransmitErrors_Type.__name__ = "Integer32"
_ThresholdTotalNumberTransmitErrors_Object = MibScalar
thresholdTotalNumberTransmitErrors = _ThresholdTotalNumberTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 2),
    _ThresholdTotalNumberTransmitErrors_Type()
)
thresholdTotalNumberTransmitErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberTransmitErrors.setStatus("mandatory")


class _ThresholdTotalNumberReceivedErrorsPerMinute_Type(Integer32):
    """Custom type thresholdTotalNumberReceivedErrorsPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberReceivedErrorsPerMinute_Type.__name__ = "Integer32"
_ThresholdTotalNumberReceivedErrorsPerMinute_Object = MibScalar
thresholdTotalNumberReceivedErrorsPerMinute = _ThresholdTotalNumberReceivedErrorsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 3),
    _ThresholdTotalNumberReceivedErrorsPerMinute_Type()
)
thresholdTotalNumberReceivedErrorsPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberReceivedErrorsPerMinute.setStatus("mandatory")


class _ThresholdTotalNumberReceivedErrorsPerHour_Type(Integer32):
    """Custom type thresholdTotalNumberReceivedErrorsPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberReceivedErrorsPerHour_Type.__name__ = "Integer32"
_ThresholdTotalNumberReceivedErrorsPerHour_Object = MibScalar
thresholdTotalNumberReceivedErrorsPerHour = _ThresholdTotalNumberReceivedErrorsPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 4),
    _ThresholdTotalNumberReceivedErrorsPerHour_Type()
)
thresholdTotalNumberReceivedErrorsPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberReceivedErrorsPerHour.setStatus("mandatory")


class _ThresholdTotalNumberReceivedErrorsPerDay_Type(Integer32):
    """Custom type thresholdTotalNumberReceivedErrorsPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberReceivedErrorsPerDay_Type.__name__ = "Integer32"
_ThresholdTotalNumberReceivedErrorsPerDay_Object = MibScalar
thresholdTotalNumberReceivedErrorsPerDay = _ThresholdTotalNumberReceivedErrorsPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 5),
    _ThresholdTotalNumberReceivedErrorsPerDay_Type()
)
thresholdTotalNumberReceivedErrorsPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberReceivedErrorsPerDay.setStatus("mandatory")


class _ThresholdTotalNumberTransmitErrorsPerMinute_Type(Integer32):
    """Custom type thresholdTotalNumberTransmitErrorsPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberTransmitErrorsPerMinute_Type.__name__ = "Integer32"
_ThresholdTotalNumberTransmitErrorsPerMinute_Object = MibScalar
thresholdTotalNumberTransmitErrorsPerMinute = _ThresholdTotalNumberTransmitErrorsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 6),
    _ThresholdTotalNumberTransmitErrorsPerMinute_Type()
)
thresholdTotalNumberTransmitErrorsPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberTransmitErrorsPerMinute.setStatus("mandatory")


class _ThresholdTotalNumberTransmitErrorsPerHour_Type(Integer32):
    """Custom type thresholdTotalNumberTransmitErrorsPerHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberTransmitErrorsPerHour_Type.__name__ = "Integer32"
_ThresholdTotalNumberTransmitErrorsPerHour_Object = MibScalar
thresholdTotalNumberTransmitErrorsPerHour = _ThresholdTotalNumberTransmitErrorsPerHour_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 7),
    _ThresholdTotalNumberTransmitErrorsPerHour_Type()
)
thresholdTotalNumberTransmitErrorsPerHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberTransmitErrorsPerHour.setStatus("mandatory")


class _ThresholdTotalNumberTransmitErrorsPerDay_Type(Integer32):
    """Custom type thresholdTotalNumberTransmitErrorsPerDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalNumberTransmitErrorsPerDay_Type.__name__ = "Integer32"
_ThresholdTotalNumberTransmitErrorsPerDay_Object = MibScalar
thresholdTotalNumberTransmitErrorsPerDay = _ThresholdTotalNumberTransmitErrorsPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 8),
    _ThresholdTotalNumberTransmitErrorsPerDay_Type()
)
thresholdTotalNumberTransmitErrorsPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalNumberTransmitErrorsPerDay.setStatus("mandatory")


class _ThresholdMaximumErrorRatePerSecond_Type(Integer32):
    """Custom type thresholdMaximumErrorRatePerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdMaximumErrorRatePerSecond_Type.__name__ = "Integer32"
_ThresholdMaximumErrorRatePerSecond_Object = MibScalar
thresholdMaximumErrorRatePerSecond = _ThresholdMaximumErrorRatePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 9),
    _ThresholdMaximumErrorRatePerSecond_Type()
)
thresholdMaximumErrorRatePerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdMaximumErrorRatePerSecond.setStatus("mandatory")


class _ThresholdTotalErrorRatePerSecond_Type(Integer32):
    """Custom type thresholdTotalErrorRatePerSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalErrorRatePerSecond_Type.__name__ = "Integer32"
_ThresholdTotalErrorRatePerSecond_Object = MibScalar
thresholdTotalErrorRatePerSecond = _ThresholdTotalErrorRatePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 5, 10),
    _ThresholdTotalErrorRatePerSecond_Type()
)
thresholdTotalErrorRatePerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalErrorRatePerSecond.setStatus("mandatory")
_ThresholdForDriver_ObjectIdentity = ObjectIdentity
thresholdForDriver = _ThresholdForDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 6)
)


class _ThresholdCurrentClock_Type(Integer32):
    """Custom type thresholdCurrentClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdCurrentClock_Type.__name__ = "Integer32"
_ThresholdCurrentClock_Object = MibScalar
thresholdCurrentClock = _ThresholdCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 6, 1),
    _ThresholdCurrentClock_Type()
)
thresholdCurrentClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdCurrentClock.setStatus("mandatory")


class _ThresholdCurrentMemoryUsedByDriver_Type(Integer32):
    """Custom type thresholdCurrentMemoryUsedByDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdCurrentMemoryUsedByDriver_Type.__name__ = "Integer32"
_ThresholdCurrentMemoryUsedByDriver_Object = MibScalar
thresholdCurrentMemoryUsedByDriver = _ThresholdCurrentMemoryUsedByDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 6, 2),
    _ThresholdCurrentMemoryUsedByDriver_Type()
)
thresholdCurrentMemoryUsedByDriver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdCurrentMemoryUsedByDriver.setStatus("mandatory")


class _ThresholdMaximumMemoryUsedByDriver_Type(Integer32):
    """Custom type thresholdMaximumMemoryUsedByDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdMaximumMemoryUsedByDriver_Type.__name__ = "Integer32"
_ThresholdMaximumMemoryUsedByDriver_Object = MibScalar
thresholdMaximumMemoryUsedByDriver = _ThresholdMaximumMemoryUsedByDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 6, 3),
    _ThresholdMaximumMemoryUsedByDriver_Type()
)
thresholdMaximumMemoryUsedByDriver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdMaximumMemoryUsedByDriver.setStatus("mandatory")


class _ThresholdPercentCurrentMemoryUsedByDriver_Type(Integer32):
    """Custom type thresholdPercentCurrentMemoryUsedByDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPercentCurrentMemoryUsedByDriver_Type.__name__ = "Integer32"
_ThresholdPercentCurrentMemoryUsedByDriver_Object = MibScalar
thresholdPercentCurrentMemoryUsedByDriver = _ThresholdPercentCurrentMemoryUsedByDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 6, 4),
    _ThresholdPercentCurrentMemoryUsedByDriver_Type()
)
thresholdPercentCurrentMemoryUsedByDriver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPercentCurrentMemoryUsedByDriver.setStatus("mandatory")


class _ThresholdPercentMaximumMemoryUsedByDriver_Type(Integer32):
    """Custom type thresholdPercentMaximumMemoryUsedByDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdPercentMaximumMemoryUsedByDriver_Type.__name__ = "Integer32"
_ThresholdPercentMaximumMemoryUsedByDriver_Object = MibScalar
thresholdPercentMaximumMemoryUsedByDriver = _ThresholdPercentMaximumMemoryUsedByDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 6, 5),
    _ThresholdPercentMaximumMemoryUsedByDriver_Type()
)
thresholdPercentMaximumMemoryUsedByDriver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdPercentMaximumMemoryUsedByDriver.setStatus("mandatory")


class _ThresholdTotalMemoryAvailableToTheDriver_Type(Integer32):
    """Custom type thresholdTotalMemoryAvailableToTheDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdTotalMemoryAvailableToTheDriver_Type.__name__ = "Integer32"
_ThresholdTotalMemoryAvailableToTheDriver_Object = MibScalar
thresholdTotalMemoryAvailableToTheDriver = _ThresholdTotalMemoryAvailableToTheDriver_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 6, 6),
    _ThresholdTotalMemoryAvailableToTheDriver_Type()
)
thresholdTotalMemoryAvailableToTheDriver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdTotalMemoryAvailableToTheDriver.setStatus("mandatory")
_ThresholdForCompression_ObjectIdentity = ObjectIdentity
thresholdForCompression = _ThresholdForCompression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 7)
)


class _ThresholdBytesIntoCompression_Type(Integer32):
    """Custom type thresholdBytesIntoCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdBytesIntoCompression_Type.__name__ = "Integer32"
_ThresholdBytesIntoCompression_Object = MibScalar
thresholdBytesIntoCompression = _ThresholdBytesIntoCompression_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 7, 1),
    _ThresholdBytesIntoCompression_Type()
)
thresholdBytesIntoCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdBytesIntoCompression.setStatus("mandatory")


class _ThresholdBytesOutCompression_Type(Integer32):
    """Custom type thresholdBytesOutCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdBytesOutCompression_Type.__name__ = "Integer32"
_ThresholdBytesOutCompression_Object = MibScalar
thresholdBytesOutCompression = _ThresholdBytesOutCompression_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 7, 2),
    _ThresholdBytesOutCompression_Type()
)
thresholdBytesOutCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdBytesOutCompression.setStatus("mandatory")


class _ThresholdBytesIntoDecompression_Type(Integer32):
    """Custom type thresholdBytesIntoDecompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdBytesIntoDecompression_Type.__name__ = "Integer32"
_ThresholdBytesIntoDecompression_Object = MibScalar
thresholdBytesIntoDecompression = _ThresholdBytesIntoDecompression_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 7, 3),
    _ThresholdBytesIntoDecompression_Type()
)
thresholdBytesIntoDecompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdBytesIntoDecompression.setStatus("mandatory")


class _ThresholdBytesOutDecompression_Type(Integer32):
    """Custom type thresholdBytesOutDecompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdBytesOutDecompression_Type.__name__ = "Integer32"
_ThresholdBytesOutDecompression_Object = MibScalar
thresholdBytesOutDecompression = _ThresholdBytesOutDecompression_Object(
    (1, 3, 6, 1, 4, 1, 3716, 1, 2, 7, 4),
    _ThresholdBytesOutDecompression_Type()
)
thresholdBytesOutDecompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdBytesOutDecompression.setStatus("mandatory")
_ApolloTrapsForNT_ObjectIdentity = ObjectIdentity
apolloTrapsForNT = _ApolloTrapsForNT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3)
)

# Managed Objects groups


# Notification objects

trapsPortsInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    trapsPortsInUse.setStatus(
        ""
    )

trapsMaxPortsUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    trapsMaxPortsUsed.setStatus(
        ""
    )

trapsPortsInUseIncoming = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 3)
)
if mibBuilder.loadTexts:
    trapsPortsInUseIncoming.setStatus(
        ""
    )

trapsPortsInUseOutgoing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 4)
)
if mibBuilder.loadTexts:
    trapsPortsInUseOutgoing.setStatus(
        ""
    )

trapsOverrallCompressionRatioOfAllPorts = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 5)
)
if mibBuilder.loadTexts:
    trapsOverrallCompressionRatioOfAllPorts.setStatus(
        ""
    )

trapsTotalCallsMade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 6)
)
if mibBuilder.loadTexts:
    trapsTotalCallsMade.setStatus(
        ""
    )

trapsFailedOutgoingCalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 7)
)
if mibBuilder.loadTexts:
    trapsFailedOutgoingCalls.setStatus(
        ""
    )

trapsTotalCallsReceivedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 8)
)
if mibBuilder.loadTexts:
    trapsTotalCallsReceivedPerMinute.setStatus(
        ""
    )

trapsTotalCallsReceivedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 9)
)
if mibBuilder.loadTexts:
    trapsTotalCallsReceivedPerHour.setStatus(
        ""
    )

trapsTotalCallsReceivedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 10)
)
if mibBuilder.loadTexts:
    trapsTotalCallsReceivedPerDay.setStatus(
        ""
    )

trapsTotalCallsMadePerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 11)
)
if mibBuilder.loadTexts:
    trapsTotalCallsMadePerMinute.setStatus(
        ""
    )

trapsTotalCallsMadePerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 12)
)
if mibBuilder.loadTexts:
    trapsTotalCallsMadePerHour.setStatus(
        ""
    )

trapsTotalCallsMadePerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 13)
)
if mibBuilder.loadTexts:
    trapsTotalCallsMadePerDay.setStatus(
        ""
    )

trapsTotalCallsReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 14)
)
if mibBuilder.loadTexts:
    trapsTotalCallsReceived.setStatus(
        ""
    )

trapsMaxSessionsUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 15)
)
if mibBuilder.loadTexts:
    trapsMaxSessionsUsed.setStatus(
        ""
    )

trapsTotalNumberUserSessionGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 16)
)
if mibBuilder.loadTexts:
    trapsTotalNumberUserSessionGranted.setStatus(
        ""
    )

trapsTotalNumberUserSessionRefused = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 17)
)
if mibBuilder.loadTexts:
    trapsTotalNumberUserSessionRefused.setStatus(
        ""
    )

trapsTotalNumberUserSessionsGrantedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 18)
)
if mibBuilder.loadTexts:
    trapsTotalNumberUserSessionsGrantedPerMinute.setStatus(
        ""
    )

trapsTotalNumberUserSessionGrantedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 19)
)
if mibBuilder.loadTexts:
    trapsTotalNumberUserSessionGrantedPerHour.setStatus(
        ""
    )

trapsTotalNumberUserSessionGrantedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 20)
)
if mibBuilder.loadTexts:
    trapsTotalNumberUserSessionGrantedPerDay.setStatus(
        ""
    )

trapsTotalNumberUserSessionRefusedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 21)
)
if mibBuilder.loadTexts:
    trapsTotalNumberUserSessionRefusedPerMinute.setStatus(
        ""
    )

trapsTotalNumberUserSessionRefusedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 22)
)
if mibBuilder.loadTexts:
    trapsTotalNumberUserSessionRefusedPerHour.setStatus(
        ""
    )

trapsTotalNumberUserSessionRefusedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 23)
)
if mibBuilder.loadTexts:
    trapsTotalNumberUserSessionRefusedPerDay.setStatus(
        ""
    )

trapsTotalActiveUserSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 24)
)
if mibBuilder.loadTexts:
    trapsTotalActiveUserSession.setStatus(
        ""
    )

trapsApolloActiveUserSessions = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 25)
)
if mibBuilder.loadTexts:
    trapsApolloActiveUserSessions.setStatus(
        ""
    )

trapsApolloNumberUserSessionsGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 26)
)
if mibBuilder.loadTexts:
    trapsApolloNumberUserSessionsGranted.setStatus(
        ""
    )

trapsApolloNumberUserSessionsrefused = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 27)
)
if mibBuilder.loadTexts:
    trapsApolloNumberUserSessionsrefused.setStatus(
        ""
    )

trapsApolloNumberUserSessionsGrantedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 28)
)
if mibBuilder.loadTexts:
    trapsApolloNumberUserSessionsGrantedPerMinute.setStatus(
        ""
    )

trapsApolloNumberUserSessionsGrantedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 29)
)
if mibBuilder.loadTexts:
    trapsApolloNumberUserSessionsGrantedPerHour.setStatus(
        ""
    )

trapsApolloNumberUserSessionsGrantedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 30)
)
if mibBuilder.loadTexts:
    trapsApolloNumberUserSessionsGrantedPerDay.setStatus(
        ""
    )

trapsApolloNumberUserSessionsRefusedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 31)
)
if mibBuilder.loadTexts:
    trapsApolloNumberUserSessionsRefusedPerMinute.setStatus(
        ""
    )

trapsApolloNumberUserSessionsRefusedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 32)
)
if mibBuilder.loadTexts:
    trapsApolloNumberUserSessionsRefusedPerHour.setStatus(
        ""
    )

trapsApolloNumberUserSessionsRefusedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 33)
)
if mibBuilder.loadTexts:
    trapsApolloNumberUserSessionsRefusedPerDay.setStatus(
        ""
    )

trapsApolloMaximumSessionsUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 34)
)
if mibBuilder.loadTexts:
    trapsApolloMaximumSessionsUsed.setStatus(
        ""
    )

trapsPPPActiveUserSessions = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 35)
)
if mibBuilder.loadTexts:
    trapsPPPActiveUserSessions.setStatus(
        ""
    )

trapsPPPNumberUserSessionsGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 36)
)
if mibBuilder.loadTexts:
    trapsPPPNumberUserSessionsGranted.setStatus(
        ""
    )

trapsPPPNumberUserSessionsRefused = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 37)
)
if mibBuilder.loadTexts:
    trapsPPPNumberUserSessionsRefused.setStatus(
        ""
    )

trapsPPPNumberUserSessionsGrantedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 38)
)
if mibBuilder.loadTexts:
    trapsPPPNumberUserSessionsGrantedPerMinute.setStatus(
        ""
    )

trapsPPPNumberUserSessionsGrantedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 39)
)
if mibBuilder.loadTexts:
    trapsPPPNumberUserSessionsGrantedPerHour.setStatus(
        ""
    )

trapsPPPNumberUserSessionsGrantedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 40)
)
if mibBuilder.loadTexts:
    trapsPPPNumberUserSessionsGrantedPerDay.setStatus(
        ""
    )

trapsPPPNumberUserSessionsRefusedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 41)
)
if mibBuilder.loadTexts:
    trapsPPPNumberUserSessionsRefusedPerMinute.setStatus(
        ""
    )

trapsPPPNumberUserSessionsRefusedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 42)
)
if mibBuilder.loadTexts:
    trapsPPPNumberUserSessionsRefusedPerHour.setStatus(
        ""
    )

trapsPPPNumberUserSessionsRefusedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 43)
)
if mibBuilder.loadTexts:
    trapsPPPNumberUserSessionsRefusedPerDay.setStatus(
        ""
    )

trapsPPPMaximumSessionsUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 44)
)
if mibBuilder.loadTexts:
    trapsPPPMaximumSessionsUsed.setStatus(
        ""
    )

trapsNumberBytesReceivedPerSecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 45)
)
if mibBuilder.loadTexts:
    trapsNumberBytesReceivedPerSecond.setStatus(
        ""
    )

trapsNumberBytesReceivedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 46)
)
if mibBuilder.loadTexts:
    trapsNumberBytesReceivedPerMinute.setStatus(
        ""
    )

trapsNumberBytesReceivedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 47)
)
if mibBuilder.loadTexts:
    trapsNumberBytesReceivedPerHour.setStatus(
        ""
    )

trapsNumberBytesReceivedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 48)
)
if mibBuilder.loadTexts:
    trapsNumberBytesReceivedPerDay.setStatus(
        ""
    )

trapsNumberBytesTransmittedPerSecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 49)
)
if mibBuilder.loadTexts:
    trapsNumberBytesTransmittedPerSecond.setStatus(
        ""
    )

trapsNumberBytesTransmittedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 50)
)
if mibBuilder.loadTexts:
    trapsNumberBytesTransmittedPerMinute.setStatus(
        ""
    )

trapsNumberBytesTransmittedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 51)
)
if mibBuilder.loadTexts:
    trapsNumberBytesTransmittedPerHour.setStatus(
        ""
    )

trapsNumberBytesTransmittedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 52)
)
if mibBuilder.loadTexts:
    trapsNumberBytesTransmittedPerDay.setStatus(
        ""
    )

trapsPacketsTransmittedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 53)
)
if mibBuilder.loadTexts:
    trapsPacketsTransmittedPerMinute.setStatus(
        ""
    )

trapsPacketsTransmittedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 54)
)
if mibBuilder.loadTexts:
    trapsPacketsTransmittedPerHour.setStatus(
        ""
    )

trapsPacketsTransmittedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 55)
)
if mibBuilder.loadTexts:
    trapsPacketsTransmittedPerDay.setStatus(
        ""
    )

trapsPacketsReceivedPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 56)
)
if mibBuilder.loadTexts:
    trapsPacketsReceivedPerMinute.setStatus(
        ""
    )

trapsPacketsReceivedPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 57)
)
if mibBuilder.loadTexts:
    trapsPacketsReceivedPerHour.setStatus(
        ""
    )

trapsPacketsReceivedPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 58)
)
if mibBuilder.loadTexts:
    trapsPacketsReceivedPerDay.setStatus(
        ""
    )

trapsPacketReceivedPerSecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 59)
)
if mibBuilder.loadTexts:
    trapsPacketReceivedPerSecond.setStatus(
        ""
    )

trapsPacketTransmittedPerSecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 60)
)
if mibBuilder.loadTexts:
    trapsPacketTransmittedPerSecond.setStatus(
        ""
    )

trapsTotalPacketReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 61)
)
if mibBuilder.loadTexts:
    trapsTotalPacketReceived.setStatus(
        ""
    )

trapsTotalPacketTransmitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 62)
)
if mibBuilder.loadTexts:
    trapsTotalPacketTransmitted.setStatus(
        ""
    )

trapsTotalNumberBytesTransmitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 63)
)
if mibBuilder.loadTexts:
    trapsTotalNumberBytesTransmitted.setStatus(
        ""
    )

trapsTotalNumberBytesReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 64)
)
if mibBuilder.loadTexts:
    trapsTotalNumberBytesReceived.setStatus(
        ""
    )

trapsTotalNumberReceivedErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 65)
)
if mibBuilder.loadTexts:
    trapsTotalNumberReceivedErrors.setStatus(
        ""
    )

trapsTotalNumberTransmitErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 66)
)
if mibBuilder.loadTexts:
    trapsTotalNumberTransmitErrors.setStatus(
        ""
    )

trapsTotalNumberReceivedErrorsPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 67)
)
if mibBuilder.loadTexts:
    trapsTotalNumberReceivedErrorsPerMinute.setStatus(
        ""
    )

trapsTotalNumberReceivedErrorsPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 68)
)
if mibBuilder.loadTexts:
    trapsTotalNumberReceivedErrorsPerHour.setStatus(
        ""
    )

trapsTotalNumberReceivedErrorsPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 69)
)
if mibBuilder.loadTexts:
    trapsTotalNumberReceivedErrorsPerDay.setStatus(
        ""
    )

trapsTotalNumberTransmitErrorsPerMinute = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 70)
)
if mibBuilder.loadTexts:
    trapsTotalNumberTransmitErrorsPerMinute.setStatus(
        ""
    )

trapsTotalNumberTransmitErrorsPerHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 71)
)
if mibBuilder.loadTexts:
    trapsTotalNumberTransmitErrorsPerHour.setStatus(
        ""
    )

trapsTotalNumberTransmitErrorsPerDay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 72)
)
if mibBuilder.loadTexts:
    trapsTotalNumberTransmitErrorsPerDay.setStatus(
        ""
    )

trapsMaximumErrorRatePerSecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 73)
)
if mibBuilder.loadTexts:
    trapsMaximumErrorRatePerSecond.setStatus(
        ""
    )

trapsTotalErrorRatePerSecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 74)
)
if mibBuilder.loadTexts:
    trapsTotalErrorRatePerSecond.setStatus(
        ""
    )

trapsCurrentClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 75)
)
if mibBuilder.loadTexts:
    trapsCurrentClock.setStatus(
        ""
    )

trapsCurrentMemoryUsedByDriver = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 76)
)
if mibBuilder.loadTexts:
    trapsCurrentMemoryUsedByDriver.setStatus(
        ""
    )

trapsMaximumMemoryUsedByDriver = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 77)
)
if mibBuilder.loadTexts:
    trapsMaximumMemoryUsedByDriver.setStatus(
        ""
    )

trapsPercentCurrentMemoryUsedByDriver = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 78)
)
if mibBuilder.loadTexts:
    trapsPercentCurrentMemoryUsedByDriver.setStatus(
        ""
    )

trapsPercentMaximumMemoryUsedByDriver = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 79)
)
if mibBuilder.loadTexts:
    trapsPercentMaximumMemoryUsedByDriver.setStatus(
        ""
    )

trapsTotalMemoryAvailableToTheDriver = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 80)
)
if mibBuilder.loadTexts:
    trapsTotalMemoryAvailableToTheDriver.setStatus(
        ""
    )

trapsBytesIntoCompression = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 81)
)
if mibBuilder.loadTexts:
    trapsBytesIntoCompression.setStatus(
        ""
    )

trapsBytesOutCompression = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 82)
)
if mibBuilder.loadTexts:
    trapsBytesOutCompression.setStatus(
        ""
    )

trapsBytesIntoDecompression = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 83)
)
if mibBuilder.loadTexts:
    trapsBytesIntoDecompression.setStatus(
        ""
    )

trapsBytesOutDecompression = NotificationType(
    (1, 3, 6, 1, 4, 1, 3716, 1, 3, 0, 84)
)
if mibBuilder.loadTexts:
    trapsBytesOutDecompression.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APSNMP-MIB",
    **{"brand": brand,
       "windowsNT": windowsNT,
       "apolloStatsForNT": apolloStatsForNT,
       "statsForPort": statsForPort,
       "statsPortsInUse": statsPortsInUse,
       "statsMaxPortsUsed": statsMaxPortsUsed,
       "statsPortsInUseIncoming": statsPortsInUseIncoming,
       "statsPortsInUseOutgoing": statsPortsInUseOutgoing,
       "statsOverrallCompressionRatioOfAllPorts": statsOverrallCompressionRatioOfAllPorts,
       "statsForCalls": statsForCalls,
       "statsTotalCallsMade": statsTotalCallsMade,
       "statsFailedOutgoingCalls": statsFailedOutgoingCalls,
       "statsTotalCallsReceivedPerMinute": statsTotalCallsReceivedPerMinute,
       "statsTotalCallsReceivedPerHour": statsTotalCallsReceivedPerHour,
       "statsTotalCallsReceivedPerDay": statsTotalCallsReceivedPerDay,
       "statsTotalCallsMadePerMinute": statsTotalCallsMadePerMinute,
       "statsTotalCallsMadePerHour": statsTotalCallsMadePerHour,
       "statsTotalCallsMadePerDay": statsTotalCallsMadePerDay,
       "statsTotalCallsReceived": statsTotalCallsReceived,
       "statsForSession": statsForSession,
       "statsSessionForGeneral": statsSessionForGeneral,
       "statsMaxSessionsUsed": statsMaxSessionsUsed,
       "statsTotalNumberUserSessionGranted": statsTotalNumberUserSessionGranted,
       "statsTotalNumberUserSessionRefused": statsTotalNumberUserSessionRefused,
       "statsTotalNumberUserSessionsGrantedPerMinute": statsTotalNumberUserSessionsGrantedPerMinute,
       "statsTotalNumberUserSessionGrantedPerHour": statsTotalNumberUserSessionGrantedPerHour,
       "statsTotalNumberUserSessionGrantedPerDay": statsTotalNumberUserSessionGrantedPerDay,
       "statsTotalNumberUserSessionRefusedPerMinute": statsTotalNumberUserSessionRefusedPerMinute,
       "statsTotalNumberUserSessionRefusedPerHour": statsTotalNumberUserSessionRefusedPerHour,
       "statsTotalNumberUserSessionRefusedPerDay": statsTotalNumberUserSessionRefusedPerDay,
       "statsTotalActiveUserSession": statsTotalActiveUserSession,
       "statsSessionForApollo": statsSessionForApollo,
       "statsApolloActiveUserSessions": statsApolloActiveUserSessions,
       "statsApolloNumberUserSessionsGranted": statsApolloNumberUserSessionsGranted,
       "statsApolloNumberUserSessionsrefused": statsApolloNumberUserSessionsrefused,
       "statsApolloNumberUserSessionsGrantedPerMinute": statsApolloNumberUserSessionsGrantedPerMinute,
       "statsApolloNumberUserSessionsGrantedPerHour": statsApolloNumberUserSessionsGrantedPerHour,
       "statsApolloNumberUserSessionsGrantedPerDay": statsApolloNumberUserSessionsGrantedPerDay,
       "statsApolloNumberUserSessionsRefusedPerMinute": statsApolloNumberUserSessionsRefusedPerMinute,
       "statsApolloNumberUserSessionsRefusedPerHour": statsApolloNumberUserSessionsRefusedPerHour,
       "statsApolloNumberUserSessionsRefusedPerDay": statsApolloNumberUserSessionsRefusedPerDay,
       "statsApolloMaximumSessionsUsed": statsApolloMaximumSessionsUsed,
       "statsSessionForPPP": statsSessionForPPP,
       "statsPPPActiveUserSessions": statsPPPActiveUserSessions,
       "statsPPPNumberUserSessionsGranted": statsPPPNumberUserSessionsGranted,
       "statsPPPNumberUserSessionsRefused": statsPPPNumberUserSessionsRefused,
       "statsPPPNumberUserSessionsGrantedPerMinute": statsPPPNumberUserSessionsGrantedPerMinute,
       "statsPPPNumberUserSessionsGrantedPerHour": statsPPPNumberUserSessionsGrantedPerHour,
       "statsPPPNumberUserSessionsGrantedPerDay": statsPPPNumberUserSessionsGrantedPerDay,
       "statsPPPNumberUserSessionsRefusedPerMinute": statsPPPNumberUserSessionsRefusedPerMinute,
       "statsPPPNumberUserSessionsRefusedPerHour": statsPPPNumberUserSessionsRefusedPerHour,
       "statsPPPNumberUserSessionsRefusedPerDay": statsPPPNumberUserSessionsRefusedPerDay,
       "statsPPPMaximumSessionsUsed": statsPPPMaximumSessionsUsed,
       "statsForData": statsForData,
       "statsNumberBytesReceivedPerSecond": statsNumberBytesReceivedPerSecond,
       "statsNumberBytesReceivedPerMinute": statsNumberBytesReceivedPerMinute,
       "statsNumberBytesReceivedPerHour": statsNumberBytesReceivedPerHour,
       "statsNumberBytesReceivedPerDay": statsNumberBytesReceivedPerDay,
       "statsNumberBytesTransmittedPerSecond": statsNumberBytesTransmittedPerSecond,
       "statsNumberBytesTransmittedPerMinute": statsNumberBytesTransmittedPerMinute,
       "statsNumberBytesTransmittedPerHour": statsNumberBytesTransmittedPerHour,
       "statsNumberBytesTransmittedPerDay": statsNumberBytesTransmittedPerDay,
       "statsPacketsTransmittedPerMinute": statsPacketsTransmittedPerMinute,
       "statsPacketsTransmittedPerHour": statsPacketsTransmittedPerHour,
       "statsPacketsTransmittedPerDay": statsPacketsTransmittedPerDay,
       "statsPacketsReceivedPerMinute": statsPacketsReceivedPerMinute,
       "statsPacketsReceivedPerHour": statsPacketsReceivedPerHour,
       "statsPacketsReceivedPerDay": statsPacketsReceivedPerDay,
       "statsPacketReceivedPerSecond": statsPacketReceivedPerSecond,
       "statsPacketTransmittedPerSecond": statsPacketTransmittedPerSecond,
       "statsTotalPacketReceived": statsTotalPacketReceived,
       "statsTotalPacketTransmitted": statsTotalPacketTransmitted,
       "statsTotalNumberBytesTransmitted": statsTotalNumberBytesTransmitted,
       "statsTotalNumberBytesReceived": statsTotalNumberBytesReceived,
       "statsForError": statsForError,
       "statsTotalNumberReceivedErrors": statsTotalNumberReceivedErrors,
       "statsTotalNumberTransmitErrors": statsTotalNumberTransmitErrors,
       "statsTotalNumberReceivedErrorsPerMinute": statsTotalNumberReceivedErrorsPerMinute,
       "statsTotalNumberReceivedErrorsPerHour": statsTotalNumberReceivedErrorsPerHour,
       "statsTotalNumberReceivedErrorsPerDay": statsTotalNumberReceivedErrorsPerDay,
       "statsTotalNumberTransmitErrorsPerMinute": statsTotalNumberTransmitErrorsPerMinute,
       "statsTotalNumberTransmitErrorsPerHour": statsTotalNumberTransmitErrorsPerHour,
       "statsTotalNumberTransmitErrorsPerDay": statsTotalNumberTransmitErrorsPerDay,
       "statsMaximumErrorRatePerSecond": statsMaximumErrorRatePerSecond,
       "statsTotalErrorRatePerSecond": statsTotalErrorRatePerSecond,
       "statsForDriver": statsForDriver,
       "statsCurrentClock": statsCurrentClock,
       "statsCurrentMemoryUsedByDriver": statsCurrentMemoryUsedByDriver,
       "statsMaximumMemoryUsedByDriver": statsMaximumMemoryUsedByDriver,
       "statsPercentCurrentMemoryUsedByDriver": statsPercentCurrentMemoryUsedByDriver,
       "statsPercentMaximumMemoryUsedByDriver": statsPercentMaximumMemoryUsedByDriver,
       "statsTotalMemoryAvailableToTheDriver": statsTotalMemoryAvailableToTheDriver,
       "statsForCompression": statsForCompression,
       "statsBytesIntoCompression": statsBytesIntoCompression,
       "statsBytesOutCompression": statsBytesOutCompression,
       "statsBytesIntoDecompression": statsBytesIntoDecompression,
       "statsBytesOutDecompression": statsBytesOutDecompression,
       "apolloThresholdForNT": apolloThresholdForNT,
       "thresholdForPort": thresholdForPort,
       "thresholdPortsInUse": thresholdPortsInUse,
       "thresholdMaxPortsUsed": thresholdMaxPortsUsed,
       "thresholdPortsInUseIncoming": thresholdPortsInUseIncoming,
       "thresholdPortsInUseOutgoing": thresholdPortsInUseOutgoing,
       "thresholdOverrallCompressionRatioOfAllPorts": thresholdOverrallCompressionRatioOfAllPorts,
       "thresholdForCalls": thresholdForCalls,
       "thresholdTotalCallsMade": thresholdTotalCallsMade,
       "thresholdFailedOutgoingCalls": thresholdFailedOutgoingCalls,
       "thresholdTotalCallsReceivedPerMinute": thresholdTotalCallsReceivedPerMinute,
       "thresholdTotalCallsReceivedPerHour": thresholdTotalCallsReceivedPerHour,
       "thresholdTotalCallsReceivedPerDay": thresholdTotalCallsReceivedPerDay,
       "thresholdTotalCallsMadePerMinute": thresholdTotalCallsMadePerMinute,
       "thresholdTotalCallsMadePerHour": thresholdTotalCallsMadePerHour,
       "thresholdTotalCallsMadePerDay": thresholdTotalCallsMadePerDay,
       "thresholdTotalCallsReceived": thresholdTotalCallsReceived,
       "thresholdForSession": thresholdForSession,
       "thresholdSessionForGeneral": thresholdSessionForGeneral,
       "thresholdMaxSessionsUsed": thresholdMaxSessionsUsed,
       "thresholdTotalNumberUserSessionGranted": thresholdTotalNumberUserSessionGranted,
       "thresholdTotalNumberUserSessionRefused": thresholdTotalNumberUserSessionRefused,
       "thresholdTotalNumberUserSessionsGrantedPerMinute": thresholdTotalNumberUserSessionsGrantedPerMinute,
       "thresholdTotalNumberUserSessionGrantedPerHour": thresholdTotalNumberUserSessionGrantedPerHour,
       "thresholdTotalNumberUserSessionGrantedPerDay": thresholdTotalNumberUserSessionGrantedPerDay,
       "thresholdTotalNumberUserSessionRefusedPerMinute": thresholdTotalNumberUserSessionRefusedPerMinute,
       "thresholdTotalNumberUserSessionRefusedPerHour": thresholdTotalNumberUserSessionRefusedPerHour,
       "thresholdTotalNumberUserSessionRefusedPerDay": thresholdTotalNumberUserSessionRefusedPerDay,
       "thresholdTotalActiveUserSession": thresholdTotalActiveUserSession,
       "thresholdSessionForApollo": thresholdSessionForApollo,
       "thresholdApolloActiveUserSessions": thresholdApolloActiveUserSessions,
       "thresholdApolloNumberUserSessionsGranted": thresholdApolloNumberUserSessionsGranted,
       "thresholdApolloNumberUserSessionsrefused": thresholdApolloNumberUserSessionsrefused,
       "thresholdApolloNumberUserSessionsGrantedPerMinute": thresholdApolloNumberUserSessionsGrantedPerMinute,
       "thresholdApolloNumberUserSessionsGrantedPerHour": thresholdApolloNumberUserSessionsGrantedPerHour,
       "thresholdApolloNumberUserSessionsGrantedPerDay": thresholdApolloNumberUserSessionsGrantedPerDay,
       "thresholdApolloNumberUserSessionsRefusedPerMinute": thresholdApolloNumberUserSessionsRefusedPerMinute,
       "thresholdApolloNumberUserSessionsRefusedPerHour": thresholdApolloNumberUserSessionsRefusedPerHour,
       "thresholdApolloNumberUserSessionsRefusedPerDay": thresholdApolloNumberUserSessionsRefusedPerDay,
       "thresholdApolloMaximumSessionsUsed": thresholdApolloMaximumSessionsUsed,
       "thresholdSessionForPPP": thresholdSessionForPPP,
       "thresholdPPPActiveUserSessions": thresholdPPPActiveUserSessions,
       "thresholdPPPNumberUserSessionsGranted": thresholdPPPNumberUserSessionsGranted,
       "thresholdPPPNumberUserSessionsRefused": thresholdPPPNumberUserSessionsRefused,
       "thresholdPPPNumberUserSessionsGrantedPerMinute": thresholdPPPNumberUserSessionsGrantedPerMinute,
       "thresholdPPPNumberUserSessionsGrantedPerHour": thresholdPPPNumberUserSessionsGrantedPerHour,
       "thresholdPPPNumberUserSessionsGrantedPerDay": thresholdPPPNumberUserSessionsGrantedPerDay,
       "thresholdPPPNumberUserSessionsRefusedPerMinute": thresholdPPPNumberUserSessionsRefusedPerMinute,
       "thresholdPPPNumberUserSessionsRefusedPerHour": thresholdPPPNumberUserSessionsRefusedPerHour,
       "thresholdPPPNumberUserSessionsRefusedPerDay": thresholdPPPNumberUserSessionsRefusedPerDay,
       "thresholdPPPMaximumSessionsUsed": thresholdPPPMaximumSessionsUsed,
       "thresholdForData": thresholdForData,
       "thresholdNumberBytesReceivedPerSecond": thresholdNumberBytesReceivedPerSecond,
       "thresholdNumberBytesReceivedPerMinute": thresholdNumberBytesReceivedPerMinute,
       "thresholdNumberBytesReceivedPerHour": thresholdNumberBytesReceivedPerHour,
       "thresholdNumberBytesReceivedPerDay": thresholdNumberBytesReceivedPerDay,
       "thresholdNumberBytesTransmittedPerSecond": thresholdNumberBytesTransmittedPerSecond,
       "thresholdNumberBytesTransmittedPerMinute": thresholdNumberBytesTransmittedPerMinute,
       "thresholdNumberBytesTransmittedPerHour": thresholdNumberBytesTransmittedPerHour,
       "thresholdNumberBytesTransmittedPerDay": thresholdNumberBytesTransmittedPerDay,
       "thresholdPacketsTransmittedPerMinute": thresholdPacketsTransmittedPerMinute,
       "thresholdPacketsTransmittedPerHour": thresholdPacketsTransmittedPerHour,
       "thresholdPacketsTransmittedPerDay": thresholdPacketsTransmittedPerDay,
       "thresholdPacketsReceivedPerMinute": thresholdPacketsReceivedPerMinute,
       "thresholdPacketsReceivedPerHour": thresholdPacketsReceivedPerHour,
       "thresholdPacketsReceivedPerDay": thresholdPacketsReceivedPerDay,
       "thresholdPacketReceivedPerSecond": thresholdPacketReceivedPerSecond,
       "thresholdPacketTransmittedPerSecond": thresholdPacketTransmittedPerSecond,
       "thresholdTotalPacketReceived": thresholdTotalPacketReceived,
       "thresholdTotalPacketTransmitted": thresholdTotalPacketTransmitted,
       "thresholdTotalNumberBytesTransmitted": thresholdTotalNumberBytesTransmitted,
       "thresholdTotalNumberBytesReceived": thresholdTotalNumberBytesReceived,
       "thresholdForError": thresholdForError,
       "thresholdTotalNumberReceivedErrors": thresholdTotalNumberReceivedErrors,
       "thresholdTotalNumberTransmitErrors": thresholdTotalNumberTransmitErrors,
       "thresholdTotalNumberReceivedErrorsPerMinute": thresholdTotalNumberReceivedErrorsPerMinute,
       "thresholdTotalNumberReceivedErrorsPerHour": thresholdTotalNumberReceivedErrorsPerHour,
       "thresholdTotalNumberReceivedErrorsPerDay": thresholdTotalNumberReceivedErrorsPerDay,
       "thresholdTotalNumberTransmitErrorsPerMinute": thresholdTotalNumberTransmitErrorsPerMinute,
       "thresholdTotalNumberTransmitErrorsPerHour": thresholdTotalNumberTransmitErrorsPerHour,
       "thresholdTotalNumberTransmitErrorsPerDay": thresholdTotalNumberTransmitErrorsPerDay,
       "thresholdMaximumErrorRatePerSecond": thresholdMaximumErrorRatePerSecond,
       "thresholdTotalErrorRatePerSecond": thresholdTotalErrorRatePerSecond,
       "thresholdForDriver": thresholdForDriver,
       "thresholdCurrentClock": thresholdCurrentClock,
       "thresholdCurrentMemoryUsedByDriver": thresholdCurrentMemoryUsedByDriver,
       "thresholdMaximumMemoryUsedByDriver": thresholdMaximumMemoryUsedByDriver,
       "thresholdPercentCurrentMemoryUsedByDriver": thresholdPercentCurrentMemoryUsedByDriver,
       "thresholdPercentMaximumMemoryUsedByDriver": thresholdPercentMaximumMemoryUsedByDriver,
       "thresholdTotalMemoryAvailableToTheDriver": thresholdTotalMemoryAvailableToTheDriver,
       "thresholdForCompression": thresholdForCompression,
       "thresholdBytesIntoCompression": thresholdBytesIntoCompression,
       "thresholdBytesOutCompression": thresholdBytesOutCompression,
       "thresholdBytesIntoDecompression": thresholdBytesIntoDecompression,
       "thresholdBytesOutDecompression": thresholdBytesOutDecompression,
       "apolloTrapsForNT": apolloTrapsForNT,
       "trapsPortsInUse": trapsPortsInUse,
       "trapsMaxPortsUsed": trapsMaxPortsUsed,
       "trapsPortsInUseIncoming": trapsPortsInUseIncoming,
       "trapsPortsInUseOutgoing": trapsPortsInUseOutgoing,
       "trapsOverrallCompressionRatioOfAllPorts": trapsOverrallCompressionRatioOfAllPorts,
       "trapsTotalCallsMade": trapsTotalCallsMade,
       "trapsFailedOutgoingCalls": trapsFailedOutgoingCalls,
       "trapsTotalCallsReceivedPerMinute": trapsTotalCallsReceivedPerMinute,
       "trapsTotalCallsReceivedPerHour": trapsTotalCallsReceivedPerHour,
       "trapsTotalCallsReceivedPerDay": trapsTotalCallsReceivedPerDay,
       "trapsTotalCallsMadePerMinute": trapsTotalCallsMadePerMinute,
       "trapsTotalCallsMadePerHour": trapsTotalCallsMadePerHour,
       "trapsTotalCallsMadePerDay": trapsTotalCallsMadePerDay,
       "trapsTotalCallsReceived": trapsTotalCallsReceived,
       "trapsMaxSessionsUsed": trapsMaxSessionsUsed,
       "trapsTotalNumberUserSessionGranted": trapsTotalNumberUserSessionGranted,
       "trapsTotalNumberUserSessionRefused": trapsTotalNumberUserSessionRefused,
       "trapsTotalNumberUserSessionsGrantedPerMinute": trapsTotalNumberUserSessionsGrantedPerMinute,
       "trapsTotalNumberUserSessionGrantedPerHour": trapsTotalNumberUserSessionGrantedPerHour,
       "trapsTotalNumberUserSessionGrantedPerDay": trapsTotalNumberUserSessionGrantedPerDay,
       "trapsTotalNumberUserSessionRefusedPerMinute": trapsTotalNumberUserSessionRefusedPerMinute,
       "trapsTotalNumberUserSessionRefusedPerHour": trapsTotalNumberUserSessionRefusedPerHour,
       "trapsTotalNumberUserSessionRefusedPerDay": trapsTotalNumberUserSessionRefusedPerDay,
       "trapsTotalActiveUserSession": trapsTotalActiveUserSession,
       "trapsApolloActiveUserSessions": trapsApolloActiveUserSessions,
       "trapsApolloNumberUserSessionsGranted": trapsApolloNumberUserSessionsGranted,
       "trapsApolloNumberUserSessionsrefused": trapsApolloNumberUserSessionsrefused,
       "trapsApolloNumberUserSessionsGrantedPerMinute": trapsApolloNumberUserSessionsGrantedPerMinute,
       "trapsApolloNumberUserSessionsGrantedPerHour": trapsApolloNumberUserSessionsGrantedPerHour,
       "trapsApolloNumberUserSessionsGrantedPerDay": trapsApolloNumberUserSessionsGrantedPerDay,
       "trapsApolloNumberUserSessionsRefusedPerMinute": trapsApolloNumberUserSessionsRefusedPerMinute,
       "trapsApolloNumberUserSessionsRefusedPerHour": trapsApolloNumberUserSessionsRefusedPerHour,
       "trapsApolloNumberUserSessionsRefusedPerDay": trapsApolloNumberUserSessionsRefusedPerDay,
       "trapsApolloMaximumSessionsUsed": trapsApolloMaximumSessionsUsed,
       "trapsPPPActiveUserSessions": trapsPPPActiveUserSessions,
       "trapsPPPNumberUserSessionsGranted": trapsPPPNumberUserSessionsGranted,
       "trapsPPPNumberUserSessionsRefused": trapsPPPNumberUserSessionsRefused,
       "trapsPPPNumberUserSessionsGrantedPerMinute": trapsPPPNumberUserSessionsGrantedPerMinute,
       "trapsPPPNumberUserSessionsGrantedPerHour": trapsPPPNumberUserSessionsGrantedPerHour,
       "trapsPPPNumberUserSessionsGrantedPerDay": trapsPPPNumberUserSessionsGrantedPerDay,
       "trapsPPPNumberUserSessionsRefusedPerMinute": trapsPPPNumberUserSessionsRefusedPerMinute,
       "trapsPPPNumberUserSessionsRefusedPerHour": trapsPPPNumberUserSessionsRefusedPerHour,
       "trapsPPPNumberUserSessionsRefusedPerDay": trapsPPPNumberUserSessionsRefusedPerDay,
       "trapsPPPMaximumSessionsUsed": trapsPPPMaximumSessionsUsed,
       "trapsNumberBytesReceivedPerSecond": trapsNumberBytesReceivedPerSecond,
       "trapsNumberBytesReceivedPerMinute": trapsNumberBytesReceivedPerMinute,
       "trapsNumberBytesReceivedPerHour": trapsNumberBytesReceivedPerHour,
       "trapsNumberBytesReceivedPerDay": trapsNumberBytesReceivedPerDay,
       "trapsNumberBytesTransmittedPerSecond": trapsNumberBytesTransmittedPerSecond,
       "trapsNumberBytesTransmittedPerMinute": trapsNumberBytesTransmittedPerMinute,
       "trapsNumberBytesTransmittedPerHour": trapsNumberBytesTransmittedPerHour,
       "trapsNumberBytesTransmittedPerDay": trapsNumberBytesTransmittedPerDay,
       "trapsPacketsTransmittedPerMinute": trapsPacketsTransmittedPerMinute,
       "trapsPacketsTransmittedPerHour": trapsPacketsTransmittedPerHour,
       "trapsPacketsTransmittedPerDay": trapsPacketsTransmittedPerDay,
       "trapsPacketsReceivedPerMinute": trapsPacketsReceivedPerMinute,
       "trapsPacketsReceivedPerHour": trapsPacketsReceivedPerHour,
       "trapsPacketsReceivedPerDay": trapsPacketsReceivedPerDay,
       "trapsPacketReceivedPerSecond": trapsPacketReceivedPerSecond,
       "trapsPacketTransmittedPerSecond": trapsPacketTransmittedPerSecond,
       "trapsTotalPacketReceived": trapsTotalPacketReceived,
       "trapsTotalPacketTransmitted": trapsTotalPacketTransmitted,
       "trapsTotalNumberBytesTransmitted": trapsTotalNumberBytesTransmitted,
       "trapsTotalNumberBytesReceived": trapsTotalNumberBytesReceived,
       "trapsTotalNumberReceivedErrors": trapsTotalNumberReceivedErrors,
       "trapsTotalNumberTransmitErrors": trapsTotalNumberTransmitErrors,
       "trapsTotalNumberReceivedErrorsPerMinute": trapsTotalNumberReceivedErrorsPerMinute,
       "trapsTotalNumberReceivedErrorsPerHour": trapsTotalNumberReceivedErrorsPerHour,
       "trapsTotalNumberReceivedErrorsPerDay": trapsTotalNumberReceivedErrorsPerDay,
       "trapsTotalNumberTransmitErrorsPerMinute": trapsTotalNumberTransmitErrorsPerMinute,
       "trapsTotalNumberTransmitErrorsPerHour": trapsTotalNumberTransmitErrorsPerHour,
       "trapsTotalNumberTransmitErrorsPerDay": trapsTotalNumberTransmitErrorsPerDay,
       "trapsMaximumErrorRatePerSecond": trapsMaximumErrorRatePerSecond,
       "trapsTotalErrorRatePerSecond": trapsTotalErrorRatePerSecond,
       "trapsCurrentClock": trapsCurrentClock,
       "trapsCurrentMemoryUsedByDriver": trapsCurrentMemoryUsedByDriver,
       "trapsMaximumMemoryUsedByDriver": trapsMaximumMemoryUsedByDriver,
       "trapsPercentCurrentMemoryUsedByDriver": trapsPercentCurrentMemoryUsedByDriver,
       "trapsPercentMaximumMemoryUsedByDriver": trapsPercentMaximumMemoryUsedByDriver,
       "trapsTotalMemoryAvailableToTheDriver": trapsTotalMemoryAvailableToTheDriver,
       "trapsBytesIntoCompression": trapsBytesIntoCompression,
       "trapsBytesOutCompression": trapsBytesOutCompression,
       "trapsBytesIntoDecompression": trapsBytesIntoDecompression,
       "trapsBytesOutDecompression": trapsBytesOutDecompression}
)
