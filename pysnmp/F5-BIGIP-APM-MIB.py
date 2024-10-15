# SNMP MIB module (F5-BIGIP-APM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F5-BIGIP-APM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:34 2024
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

(LongDisplayString,
 bigipCompliances,
 bigipGroups,
 bigipTrafficMgmt) = mibBuilder.importSymbols(
    "F5-BIGIP-COMMON-MIB",
    "LongDisplayString",
    "bigipCompliances",
    "bigipGroups",
    "bigipTrafficMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

bigipApm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BigipApmGroups_ObjectIdentity = ObjectIdentity
bigipApmGroups = _BigipApmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6)
)
_ApmProfiles_ObjectIdentity = ObjectIdentity
apmProfiles = _ApmProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1)
)
_ApmProfileAccessStat_ObjectIdentity = ObjectIdentity
apmProfileAccessStat = _ApmProfileAccessStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1)
)
_ApmPaStatResetStats_Type = Integer32
_ApmPaStatResetStats_Object = MibScalar
apmPaStatResetStats = _ApmPaStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 1),
    _ApmPaStatResetStats_Type()
)
apmPaStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmPaStatResetStats.setStatus("current")
_ApmPaStatNumber_Type = Integer32
_ApmPaStatNumber_Object = MibScalar
apmPaStatNumber = _ApmPaStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 2),
    _ApmPaStatNumber_Type()
)
apmPaStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatNumber.setStatus("current")
_ApmPaStatTable_Object = MibTable
apmPaStatTable = _ApmPaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    apmPaStatTable.setStatus("current")
_ApmPaStatEntry_Object = MibTableRow
apmPaStatEntry = _ApmPaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1)
)
apmPaStatEntry.setIndexNames(
    (0, "F5-BIGIP-APM-MIB", "apmPaStatName"),
    (0, "F5-BIGIP-APM-MIB", "apmPaStatVsName"),
)
if mibBuilder.loadTexts:
    apmPaStatEntry.setStatus("current")
_ApmPaStatName_Type = LongDisplayString
_ApmPaStatName_Object = MibTableColumn
apmPaStatName = _ApmPaStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 1),
    _ApmPaStatName_Type()
)
apmPaStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatName.setStatus("current")
_ApmPaStatConfigSyncState_Type = Counter64
_ApmPaStatConfigSyncState_Object = MibTableColumn
apmPaStatConfigSyncState = _ApmPaStatConfigSyncState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 2),
    _ApmPaStatConfigSyncState_Type()
)
apmPaStatConfigSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatConfigSyncState.setStatus("deprecated")
_ApmPaStatTotalSessions_Type = Counter64
_ApmPaStatTotalSessions_Object = MibTableColumn
apmPaStatTotalSessions = _ApmPaStatTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 3),
    _ApmPaStatTotalSessions_Type()
)
apmPaStatTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatTotalSessions.setStatus("current")
_ApmPaStatTotalEstablishedStateSessions_Type = Counter64
_ApmPaStatTotalEstablishedStateSessions_Object = MibTableColumn
apmPaStatTotalEstablishedStateSessions = _ApmPaStatTotalEstablishedStateSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 4),
    _ApmPaStatTotalEstablishedStateSessions_Type()
)
apmPaStatTotalEstablishedStateSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatTotalEstablishedStateSessions.setStatus("current")
_ApmPaStatCurrentActiveSessions_Type = Counter64
_ApmPaStatCurrentActiveSessions_Object = MibTableColumn
apmPaStatCurrentActiveSessions = _ApmPaStatCurrentActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 5),
    _ApmPaStatCurrentActiveSessions_Type()
)
apmPaStatCurrentActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatCurrentActiveSessions.setStatus("current")
_ApmPaStatCurrentPendingSessions_Type = Counter64
_ApmPaStatCurrentPendingSessions_Object = MibTableColumn
apmPaStatCurrentPendingSessions = _ApmPaStatCurrentPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 6),
    _ApmPaStatCurrentPendingSessions_Type()
)
apmPaStatCurrentPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatCurrentPendingSessions.setStatus("current")
_ApmPaStatCurrentCompletedSessions_Type = Counter64
_ApmPaStatCurrentCompletedSessions_Object = MibTableColumn
apmPaStatCurrentCompletedSessions = _ApmPaStatCurrentCompletedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 7),
    _ApmPaStatCurrentCompletedSessions_Type()
)
apmPaStatCurrentCompletedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatCurrentCompletedSessions.setStatus("current")
_ApmPaStatUserLoggedoutSessions_Type = Counter64
_ApmPaStatUserLoggedoutSessions_Object = MibTableColumn
apmPaStatUserLoggedoutSessions = _ApmPaStatUserLoggedoutSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 8),
    _ApmPaStatUserLoggedoutSessions_Type()
)
apmPaStatUserLoggedoutSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatUserLoggedoutSessions.setStatus("current")
_ApmPaStatAdminTerminatedSessions_Type = Counter64
_ApmPaStatAdminTerminatedSessions_Object = MibTableColumn
apmPaStatAdminTerminatedSessions = _ApmPaStatAdminTerminatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 9),
    _ApmPaStatAdminTerminatedSessions_Type()
)
apmPaStatAdminTerminatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAdminTerminatedSessions.setStatus("current")
_ApmPaStatMiscTerminatedSessions_Type = Counter64
_ApmPaStatMiscTerminatedSessions_Object = MibTableColumn
apmPaStatMiscTerminatedSessions = _ApmPaStatMiscTerminatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 10),
    _ApmPaStatMiscTerminatedSessions_Type()
)
apmPaStatMiscTerminatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatMiscTerminatedSessions.setStatus("current")
_ApmPaStatAccessPolicyResultAllow_Type = Counter64
_ApmPaStatAccessPolicyResultAllow_Object = MibTableColumn
apmPaStatAccessPolicyResultAllow = _ApmPaStatAccessPolicyResultAllow_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 11),
    _ApmPaStatAccessPolicyResultAllow_Type()
)
apmPaStatAccessPolicyResultAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAccessPolicyResultAllow.setStatus("current")
_ApmPaStatAccessPolicyResultDeny_Type = Counter64
_ApmPaStatAccessPolicyResultDeny_Object = MibTableColumn
apmPaStatAccessPolicyResultDeny = _ApmPaStatAccessPolicyResultDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 12),
    _ApmPaStatAccessPolicyResultDeny_Type()
)
apmPaStatAccessPolicyResultDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAccessPolicyResultDeny.setStatus("current")
_ApmPaStatAccessPolicyResultRedirect_Type = Counter64
_ApmPaStatAccessPolicyResultRedirect_Object = MibTableColumn
apmPaStatAccessPolicyResultRedirect = _ApmPaStatAccessPolicyResultRedirect_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 13),
    _ApmPaStatAccessPolicyResultRedirect_Type()
)
apmPaStatAccessPolicyResultRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAccessPolicyResultRedirect.setStatus("current")
_ApmPaStatAccessPolicyResultRedirectWithSession_Type = Counter64
_ApmPaStatAccessPolicyResultRedirectWithSession_Object = MibTableColumn
apmPaStatAccessPolicyResultRedirectWithSession = _ApmPaStatAccessPolicyResultRedirectWithSession_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 14),
    _ApmPaStatAccessPolicyResultRedirectWithSession_Type()
)
apmPaStatAccessPolicyResultRedirectWithSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAccessPolicyResultRedirectWithSession.setStatus("current")
_ApmPaStatEndingDenyAgentTotalInstances_Type = Counter64
_ApmPaStatEndingDenyAgentTotalInstances_Object = MibTableColumn
apmPaStatEndingDenyAgentTotalInstances = _ApmPaStatEndingDenyAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 15),
    _ApmPaStatEndingDenyAgentTotalInstances_Type()
)
apmPaStatEndingDenyAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingDenyAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEndingDenyAgentTotalUsages_Type = Counter64
_ApmPaStatEndingDenyAgentTotalUsages_Object = MibTableColumn
apmPaStatEndingDenyAgentTotalUsages = _ApmPaStatEndingDenyAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 16),
    _ApmPaStatEndingDenyAgentTotalUsages_Type()
)
apmPaStatEndingDenyAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingDenyAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEndingDenyAgentTotalSuccesses_Type = Counter64
_ApmPaStatEndingDenyAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEndingDenyAgentTotalSuccesses = _ApmPaStatEndingDenyAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 17),
    _ApmPaStatEndingDenyAgentTotalSuccesses_Type()
)
apmPaStatEndingDenyAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingDenyAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEndingDenyAgentTotalFailures_Type = Counter64
_ApmPaStatEndingDenyAgentTotalFailures_Object = MibTableColumn
apmPaStatEndingDenyAgentTotalFailures = _ApmPaStatEndingDenyAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 18),
    _ApmPaStatEndingDenyAgentTotalFailures_Type()
)
apmPaStatEndingDenyAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingDenyAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEndingDenyAgentTotalErrors_Type = Counter64
_ApmPaStatEndingDenyAgentTotalErrors_Object = MibTableColumn
apmPaStatEndingDenyAgentTotalErrors = _ApmPaStatEndingDenyAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 19),
    _ApmPaStatEndingDenyAgentTotalErrors_Type()
)
apmPaStatEndingDenyAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingDenyAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEndingDenyAgentTotalSessVars_Type = Counter64
_ApmPaStatEndingDenyAgentTotalSessVars_Object = MibTableColumn
apmPaStatEndingDenyAgentTotalSessVars = _ApmPaStatEndingDenyAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 20),
    _ApmPaStatEndingDenyAgentTotalSessVars_Type()
)
apmPaStatEndingDenyAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingDenyAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEndingRedirectAgentTotalInstances_Type = Counter64
_ApmPaStatEndingRedirectAgentTotalInstances_Object = MibTableColumn
apmPaStatEndingRedirectAgentTotalInstances = _ApmPaStatEndingRedirectAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 21),
    _ApmPaStatEndingRedirectAgentTotalInstances_Type()
)
apmPaStatEndingRedirectAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingRedirectAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEndingRedirectAgentTotalUsages_Type = Counter64
_ApmPaStatEndingRedirectAgentTotalUsages_Object = MibTableColumn
apmPaStatEndingRedirectAgentTotalUsages = _ApmPaStatEndingRedirectAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 22),
    _ApmPaStatEndingRedirectAgentTotalUsages_Type()
)
apmPaStatEndingRedirectAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingRedirectAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEndingRedirectAgentTotalSuccesses_Type = Counter64
_ApmPaStatEndingRedirectAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEndingRedirectAgentTotalSuccesses = _ApmPaStatEndingRedirectAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 23),
    _ApmPaStatEndingRedirectAgentTotalSuccesses_Type()
)
apmPaStatEndingRedirectAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingRedirectAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEndingRedirectAgentTotalFailures_Type = Counter64
_ApmPaStatEndingRedirectAgentTotalFailures_Object = MibTableColumn
apmPaStatEndingRedirectAgentTotalFailures = _ApmPaStatEndingRedirectAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 24),
    _ApmPaStatEndingRedirectAgentTotalFailures_Type()
)
apmPaStatEndingRedirectAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingRedirectAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEndingRedirectAgentTotalErrors_Type = Counter64
_ApmPaStatEndingRedirectAgentTotalErrors_Object = MibTableColumn
apmPaStatEndingRedirectAgentTotalErrors = _ApmPaStatEndingRedirectAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 25),
    _ApmPaStatEndingRedirectAgentTotalErrors_Type()
)
apmPaStatEndingRedirectAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingRedirectAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEndingRedirectAgentTotalSessVars_Type = Counter64
_ApmPaStatEndingRedirectAgentTotalSessVars_Object = MibTableColumn
apmPaStatEndingRedirectAgentTotalSessVars = _ApmPaStatEndingRedirectAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 26),
    _ApmPaStatEndingRedirectAgentTotalSessVars_Type()
)
apmPaStatEndingRedirectAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingRedirectAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEndingAllowAgentTotalInstances_Type = Counter64
_ApmPaStatEndingAllowAgentTotalInstances_Object = MibTableColumn
apmPaStatEndingAllowAgentTotalInstances = _ApmPaStatEndingAllowAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 27),
    _ApmPaStatEndingAllowAgentTotalInstances_Type()
)
apmPaStatEndingAllowAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingAllowAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEndingAllowAgentTotalUsages_Type = Counter64
_ApmPaStatEndingAllowAgentTotalUsages_Object = MibTableColumn
apmPaStatEndingAllowAgentTotalUsages = _ApmPaStatEndingAllowAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 28),
    _ApmPaStatEndingAllowAgentTotalUsages_Type()
)
apmPaStatEndingAllowAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingAllowAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEndingAllowAgentTotalSuccesses_Type = Counter64
_ApmPaStatEndingAllowAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEndingAllowAgentTotalSuccesses = _ApmPaStatEndingAllowAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 29),
    _ApmPaStatEndingAllowAgentTotalSuccesses_Type()
)
apmPaStatEndingAllowAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingAllowAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEndingAllowAgentTotalFailures_Type = Counter64
_ApmPaStatEndingAllowAgentTotalFailures_Object = MibTableColumn
apmPaStatEndingAllowAgentTotalFailures = _ApmPaStatEndingAllowAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 30),
    _ApmPaStatEndingAllowAgentTotalFailures_Type()
)
apmPaStatEndingAllowAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingAllowAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEndingAllowAgentTotalErrors_Type = Counter64
_ApmPaStatEndingAllowAgentTotalErrors_Object = MibTableColumn
apmPaStatEndingAllowAgentTotalErrors = _ApmPaStatEndingAllowAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 31),
    _ApmPaStatEndingAllowAgentTotalErrors_Type()
)
apmPaStatEndingAllowAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingAllowAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEndingAllowAgentTotalSessVars_Type = Counter64
_ApmPaStatEndingAllowAgentTotalSessVars_Object = MibTableColumn
apmPaStatEndingAllowAgentTotalSessVars = _ApmPaStatEndingAllowAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 32),
    _ApmPaStatEndingAllowAgentTotalSessVars_Type()
)
apmPaStatEndingAllowAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEndingAllowAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatAdAgentTotalInstances_Type = Counter64
_ApmPaStatAdAgentTotalInstances_Object = MibTableColumn
apmPaStatAdAgentTotalInstances = _ApmPaStatAdAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 33),
    _ApmPaStatAdAgentTotalInstances_Type()
)
apmPaStatAdAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAdAgentTotalInstances.setStatus("deprecated")
_ApmPaStatAdAgentTotalUsages_Type = Counter64
_ApmPaStatAdAgentTotalUsages_Object = MibTableColumn
apmPaStatAdAgentTotalUsages = _ApmPaStatAdAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 34),
    _ApmPaStatAdAgentTotalUsages_Type()
)
apmPaStatAdAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAdAgentTotalUsages.setStatus("deprecated")
_ApmPaStatAdAgentTotalSuccesses_Type = Counter64
_ApmPaStatAdAgentTotalSuccesses_Object = MibTableColumn
apmPaStatAdAgentTotalSuccesses = _ApmPaStatAdAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 35),
    _ApmPaStatAdAgentTotalSuccesses_Type()
)
apmPaStatAdAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAdAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatAdAgentTotalFailures_Type = Counter64
_ApmPaStatAdAgentTotalFailures_Object = MibTableColumn
apmPaStatAdAgentTotalFailures = _ApmPaStatAdAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 36),
    _ApmPaStatAdAgentTotalFailures_Type()
)
apmPaStatAdAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAdAgentTotalFailures.setStatus("deprecated")
_ApmPaStatAdAgentTotalErrors_Type = Counter64
_ApmPaStatAdAgentTotalErrors_Object = MibTableColumn
apmPaStatAdAgentTotalErrors = _ApmPaStatAdAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 37),
    _ApmPaStatAdAgentTotalErrors_Type()
)
apmPaStatAdAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAdAgentTotalErrors.setStatus("deprecated")
_ApmPaStatAdAgentTotalSessVars_Type = Counter64
_ApmPaStatAdAgentTotalSessVars_Object = MibTableColumn
apmPaStatAdAgentTotalSessVars = _ApmPaStatAdAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 38),
    _ApmPaStatAdAgentTotalSessVars_Type()
)
apmPaStatAdAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAdAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatClientCertAgentTotalInstances_Type = Counter64
_ApmPaStatClientCertAgentTotalInstances_Object = MibTableColumn
apmPaStatClientCertAgentTotalInstances = _ApmPaStatClientCertAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 39),
    _ApmPaStatClientCertAgentTotalInstances_Type()
)
apmPaStatClientCertAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatClientCertAgentTotalInstances.setStatus("deprecated")
_ApmPaStatClientCertAgentTotalUsages_Type = Counter64
_ApmPaStatClientCertAgentTotalUsages_Object = MibTableColumn
apmPaStatClientCertAgentTotalUsages = _ApmPaStatClientCertAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 40),
    _ApmPaStatClientCertAgentTotalUsages_Type()
)
apmPaStatClientCertAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatClientCertAgentTotalUsages.setStatus("deprecated")
_ApmPaStatClientCertAgentTotalSuccesses_Type = Counter64
_ApmPaStatClientCertAgentTotalSuccesses_Object = MibTableColumn
apmPaStatClientCertAgentTotalSuccesses = _ApmPaStatClientCertAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 41),
    _ApmPaStatClientCertAgentTotalSuccesses_Type()
)
apmPaStatClientCertAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatClientCertAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatClientCertAgentTotalFailures_Type = Counter64
_ApmPaStatClientCertAgentTotalFailures_Object = MibTableColumn
apmPaStatClientCertAgentTotalFailures = _ApmPaStatClientCertAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 42),
    _ApmPaStatClientCertAgentTotalFailures_Type()
)
apmPaStatClientCertAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatClientCertAgentTotalFailures.setStatus("deprecated")
_ApmPaStatClientCertAgentTotalErrors_Type = Counter64
_ApmPaStatClientCertAgentTotalErrors_Object = MibTableColumn
apmPaStatClientCertAgentTotalErrors = _ApmPaStatClientCertAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 43),
    _ApmPaStatClientCertAgentTotalErrors_Type()
)
apmPaStatClientCertAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatClientCertAgentTotalErrors.setStatus("deprecated")
_ApmPaStatClientCertAgentTotalSessVars_Type = Counter64
_ApmPaStatClientCertAgentTotalSessVars_Object = MibTableColumn
apmPaStatClientCertAgentTotalSessVars = _ApmPaStatClientCertAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 44),
    _ApmPaStatClientCertAgentTotalSessVars_Type()
)
apmPaStatClientCertAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatClientCertAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatHttpAgentTotalInstances_Type = Counter64
_ApmPaStatHttpAgentTotalInstances_Object = MibTableColumn
apmPaStatHttpAgentTotalInstances = _ApmPaStatHttpAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 45),
    _ApmPaStatHttpAgentTotalInstances_Type()
)
apmPaStatHttpAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatHttpAgentTotalInstances.setStatus("deprecated")
_ApmPaStatHttpAgentTotalUsages_Type = Counter64
_ApmPaStatHttpAgentTotalUsages_Object = MibTableColumn
apmPaStatHttpAgentTotalUsages = _ApmPaStatHttpAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 46),
    _ApmPaStatHttpAgentTotalUsages_Type()
)
apmPaStatHttpAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatHttpAgentTotalUsages.setStatus("deprecated")
_ApmPaStatHttpAgentTotalSuccesses_Type = Counter64
_ApmPaStatHttpAgentTotalSuccesses_Object = MibTableColumn
apmPaStatHttpAgentTotalSuccesses = _ApmPaStatHttpAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 47),
    _ApmPaStatHttpAgentTotalSuccesses_Type()
)
apmPaStatHttpAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatHttpAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatHttpAgentTotalFailures_Type = Counter64
_ApmPaStatHttpAgentTotalFailures_Object = MibTableColumn
apmPaStatHttpAgentTotalFailures = _ApmPaStatHttpAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 48),
    _ApmPaStatHttpAgentTotalFailures_Type()
)
apmPaStatHttpAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatHttpAgentTotalFailures.setStatus("deprecated")
_ApmPaStatHttpAgentTotalErrors_Type = Counter64
_ApmPaStatHttpAgentTotalErrors_Object = MibTableColumn
apmPaStatHttpAgentTotalErrors = _ApmPaStatHttpAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 49),
    _ApmPaStatHttpAgentTotalErrors_Type()
)
apmPaStatHttpAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatHttpAgentTotalErrors.setStatus("deprecated")
_ApmPaStatHttpAgentTotalSessVars_Type = Counter64
_ApmPaStatHttpAgentTotalSessVars_Object = MibTableColumn
apmPaStatHttpAgentTotalSessVars = _ApmPaStatHttpAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 50),
    _ApmPaStatHttpAgentTotalSessVars_Type()
)
apmPaStatHttpAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatHttpAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatLdapAgentTotalInstances_Type = Counter64
_ApmPaStatLdapAgentTotalInstances_Object = MibTableColumn
apmPaStatLdapAgentTotalInstances = _ApmPaStatLdapAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 51),
    _ApmPaStatLdapAgentTotalInstances_Type()
)
apmPaStatLdapAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLdapAgentTotalInstances.setStatus("deprecated")
_ApmPaStatLdapAgentTotalUsages_Type = Counter64
_ApmPaStatLdapAgentTotalUsages_Object = MibTableColumn
apmPaStatLdapAgentTotalUsages = _ApmPaStatLdapAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 52),
    _ApmPaStatLdapAgentTotalUsages_Type()
)
apmPaStatLdapAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLdapAgentTotalUsages.setStatus("deprecated")
_ApmPaStatLdapAgentTotalSuccesses_Type = Counter64
_ApmPaStatLdapAgentTotalSuccesses_Object = MibTableColumn
apmPaStatLdapAgentTotalSuccesses = _ApmPaStatLdapAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 53),
    _ApmPaStatLdapAgentTotalSuccesses_Type()
)
apmPaStatLdapAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLdapAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatLdapAgentTotalFailures_Type = Counter64
_ApmPaStatLdapAgentTotalFailures_Object = MibTableColumn
apmPaStatLdapAgentTotalFailures = _ApmPaStatLdapAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 54),
    _ApmPaStatLdapAgentTotalFailures_Type()
)
apmPaStatLdapAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLdapAgentTotalFailures.setStatus("deprecated")
_ApmPaStatLdapAgentTotalErrors_Type = Counter64
_ApmPaStatLdapAgentTotalErrors_Object = MibTableColumn
apmPaStatLdapAgentTotalErrors = _ApmPaStatLdapAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 55),
    _ApmPaStatLdapAgentTotalErrors_Type()
)
apmPaStatLdapAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLdapAgentTotalErrors.setStatus("deprecated")
_ApmPaStatLdapAgentTotalSessVars_Type = Counter64
_ApmPaStatLdapAgentTotalSessVars_Object = MibTableColumn
apmPaStatLdapAgentTotalSessVars = _ApmPaStatLdapAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 56),
    _ApmPaStatLdapAgentTotalSessVars_Type()
)
apmPaStatLdapAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLdapAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatRadiusAgentTotalInstances_Type = Counter64
_ApmPaStatRadiusAgentTotalInstances_Object = MibTableColumn
apmPaStatRadiusAgentTotalInstances = _ApmPaStatRadiusAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 57),
    _ApmPaStatRadiusAgentTotalInstances_Type()
)
apmPaStatRadiusAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAgentTotalInstances.setStatus("deprecated")
_ApmPaStatRadiusAgentTotalUsages_Type = Counter64
_ApmPaStatRadiusAgentTotalUsages_Object = MibTableColumn
apmPaStatRadiusAgentTotalUsages = _ApmPaStatRadiusAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 58),
    _ApmPaStatRadiusAgentTotalUsages_Type()
)
apmPaStatRadiusAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAgentTotalUsages.setStatus("deprecated")
_ApmPaStatRadiusAgentTotalSuccesses_Type = Counter64
_ApmPaStatRadiusAgentTotalSuccesses_Object = MibTableColumn
apmPaStatRadiusAgentTotalSuccesses = _ApmPaStatRadiusAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 59),
    _ApmPaStatRadiusAgentTotalSuccesses_Type()
)
apmPaStatRadiusAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatRadiusAgentTotalFailures_Type = Counter64
_ApmPaStatRadiusAgentTotalFailures_Object = MibTableColumn
apmPaStatRadiusAgentTotalFailures = _ApmPaStatRadiusAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 60),
    _ApmPaStatRadiusAgentTotalFailures_Type()
)
apmPaStatRadiusAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAgentTotalFailures.setStatus("deprecated")
_ApmPaStatRadiusAgentTotalErrors_Type = Counter64
_ApmPaStatRadiusAgentTotalErrors_Object = MibTableColumn
apmPaStatRadiusAgentTotalErrors = _ApmPaStatRadiusAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 61),
    _ApmPaStatRadiusAgentTotalErrors_Type()
)
apmPaStatRadiusAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAgentTotalErrors.setStatus("deprecated")
_ApmPaStatRadiusAgentTotalSessVars_Type = Counter64
_ApmPaStatRadiusAgentTotalSessVars_Object = MibTableColumn
apmPaStatRadiusAgentTotalSessVars = _ApmPaStatRadiusAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 62),
    _ApmPaStatRadiusAgentTotalSessVars_Type()
)
apmPaStatRadiusAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatSecuridAgentTotalInstances_Type = Counter64
_ApmPaStatSecuridAgentTotalInstances_Object = MibTableColumn
apmPaStatSecuridAgentTotalInstances = _ApmPaStatSecuridAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 63),
    _ApmPaStatSecuridAgentTotalInstances_Type()
)
apmPaStatSecuridAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatSecuridAgentTotalInstances.setStatus("deprecated")
_ApmPaStatSecuridAgentTotalUsages_Type = Counter64
_ApmPaStatSecuridAgentTotalUsages_Object = MibTableColumn
apmPaStatSecuridAgentTotalUsages = _ApmPaStatSecuridAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 64),
    _ApmPaStatSecuridAgentTotalUsages_Type()
)
apmPaStatSecuridAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatSecuridAgentTotalUsages.setStatus("deprecated")
_ApmPaStatSecuridAgentTotalSuccesses_Type = Counter64
_ApmPaStatSecuridAgentTotalSuccesses_Object = MibTableColumn
apmPaStatSecuridAgentTotalSuccesses = _ApmPaStatSecuridAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 65),
    _ApmPaStatSecuridAgentTotalSuccesses_Type()
)
apmPaStatSecuridAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatSecuridAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatSecuridAgentTotalFailures_Type = Counter64
_ApmPaStatSecuridAgentTotalFailures_Object = MibTableColumn
apmPaStatSecuridAgentTotalFailures = _ApmPaStatSecuridAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 66),
    _ApmPaStatSecuridAgentTotalFailures_Type()
)
apmPaStatSecuridAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatSecuridAgentTotalFailures.setStatus("deprecated")
_ApmPaStatSecuridAgentTotalErrors_Type = Counter64
_ApmPaStatSecuridAgentTotalErrors_Object = MibTableColumn
apmPaStatSecuridAgentTotalErrors = _ApmPaStatSecuridAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 67),
    _ApmPaStatSecuridAgentTotalErrors_Type()
)
apmPaStatSecuridAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatSecuridAgentTotalErrors.setStatus("deprecated")
_ApmPaStatSecuridAgentTotalSessVars_Type = Counter64
_ApmPaStatSecuridAgentTotalSessVars_Object = MibTableColumn
apmPaStatSecuridAgentTotalSessVars = _ApmPaStatSecuridAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 68),
    _ApmPaStatSecuridAgentTotalSessVars_Type()
)
apmPaStatSecuridAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatSecuridAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatRadiusAcctAgentTotalInstances_Type = Counter64
_ApmPaStatRadiusAcctAgentTotalInstances_Object = MibTableColumn
apmPaStatRadiusAcctAgentTotalInstances = _ApmPaStatRadiusAcctAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 69),
    _ApmPaStatRadiusAcctAgentTotalInstances_Type()
)
apmPaStatRadiusAcctAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAcctAgentTotalInstances.setStatus("deprecated")
_ApmPaStatRadiusAcctAgentTotalUsages_Type = Counter64
_ApmPaStatRadiusAcctAgentTotalUsages_Object = MibTableColumn
apmPaStatRadiusAcctAgentTotalUsages = _ApmPaStatRadiusAcctAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 70),
    _ApmPaStatRadiusAcctAgentTotalUsages_Type()
)
apmPaStatRadiusAcctAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAcctAgentTotalUsages.setStatus("deprecated")
_ApmPaStatRadiusAcctAgentTotalSuccesses_Type = Counter64
_ApmPaStatRadiusAcctAgentTotalSuccesses_Object = MibTableColumn
apmPaStatRadiusAcctAgentTotalSuccesses = _ApmPaStatRadiusAcctAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 71),
    _ApmPaStatRadiusAcctAgentTotalSuccesses_Type()
)
apmPaStatRadiusAcctAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAcctAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatRadiusAcctAgentTotalFailures_Type = Counter64
_ApmPaStatRadiusAcctAgentTotalFailures_Object = MibTableColumn
apmPaStatRadiusAcctAgentTotalFailures = _ApmPaStatRadiusAcctAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 72),
    _ApmPaStatRadiusAcctAgentTotalFailures_Type()
)
apmPaStatRadiusAcctAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAcctAgentTotalFailures.setStatus("deprecated")
_ApmPaStatRadiusAcctAgentTotalErrors_Type = Counter64
_ApmPaStatRadiusAcctAgentTotalErrors_Object = MibTableColumn
apmPaStatRadiusAcctAgentTotalErrors = _ApmPaStatRadiusAcctAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 73),
    _ApmPaStatRadiusAcctAgentTotalErrors_Type()
)
apmPaStatRadiusAcctAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAcctAgentTotalErrors.setStatus("deprecated")
_ApmPaStatRadiusAcctAgentTotalSessVars_Type = Counter64
_ApmPaStatRadiusAcctAgentTotalSessVars_Object = MibTableColumn
apmPaStatRadiusAcctAgentTotalSessVars = _ApmPaStatRadiusAcctAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 74),
    _ApmPaStatRadiusAcctAgentTotalSessVars_Type()
)
apmPaStatRadiusAcctAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRadiusAcctAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsLinuxFcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsLinuxFcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsLinuxFcAgentTotalInstances = _ApmPaStatEpsLinuxFcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 75),
    _ApmPaStatEpsLinuxFcAgentTotalInstances_Type()
)
apmPaStatEpsLinuxFcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxFcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsLinuxFcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsLinuxFcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsLinuxFcAgentTotalUsages = _ApmPaStatEpsLinuxFcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 76),
    _ApmPaStatEpsLinuxFcAgentTotalUsages_Type()
)
apmPaStatEpsLinuxFcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxFcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsLinuxFcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsLinuxFcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsLinuxFcAgentTotalSuccesses = _ApmPaStatEpsLinuxFcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 77),
    _ApmPaStatEpsLinuxFcAgentTotalSuccesses_Type()
)
apmPaStatEpsLinuxFcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxFcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsLinuxFcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsLinuxFcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsLinuxFcAgentTotalFailures = _ApmPaStatEpsLinuxFcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 78),
    _ApmPaStatEpsLinuxFcAgentTotalFailures_Type()
)
apmPaStatEpsLinuxFcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxFcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsLinuxFcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsLinuxFcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsLinuxFcAgentTotalErrors = _ApmPaStatEpsLinuxFcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 79),
    _ApmPaStatEpsLinuxFcAgentTotalErrors_Type()
)
apmPaStatEpsLinuxFcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxFcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsLinuxFcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsLinuxFcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsLinuxFcAgentTotalSessVars = _ApmPaStatEpsLinuxFcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 80),
    _ApmPaStatEpsLinuxFcAgentTotalSessVars_Type()
)
apmPaStatEpsLinuxFcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxFcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsLinuxPcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsLinuxPcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsLinuxPcAgentTotalInstances = _ApmPaStatEpsLinuxPcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 81),
    _ApmPaStatEpsLinuxPcAgentTotalInstances_Type()
)
apmPaStatEpsLinuxPcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxPcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsLinuxPcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsLinuxPcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsLinuxPcAgentTotalUsages = _ApmPaStatEpsLinuxPcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 82),
    _ApmPaStatEpsLinuxPcAgentTotalUsages_Type()
)
apmPaStatEpsLinuxPcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxPcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsLinuxPcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsLinuxPcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsLinuxPcAgentTotalSuccesses = _ApmPaStatEpsLinuxPcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 83),
    _ApmPaStatEpsLinuxPcAgentTotalSuccesses_Type()
)
apmPaStatEpsLinuxPcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxPcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsLinuxPcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsLinuxPcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsLinuxPcAgentTotalFailures = _ApmPaStatEpsLinuxPcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 84),
    _ApmPaStatEpsLinuxPcAgentTotalFailures_Type()
)
apmPaStatEpsLinuxPcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxPcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsLinuxPcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsLinuxPcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsLinuxPcAgentTotalErrors = _ApmPaStatEpsLinuxPcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 85),
    _ApmPaStatEpsLinuxPcAgentTotalErrors_Type()
)
apmPaStatEpsLinuxPcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxPcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsLinuxPcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsLinuxPcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsLinuxPcAgentTotalSessVars = _ApmPaStatEpsLinuxPcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 86),
    _ApmPaStatEpsLinuxPcAgentTotalSessVars_Type()
)
apmPaStatEpsLinuxPcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsLinuxPcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsMacFcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsMacFcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsMacFcAgentTotalInstances = _ApmPaStatEpsMacFcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 87),
    _ApmPaStatEpsMacFcAgentTotalInstances_Type()
)
apmPaStatEpsMacFcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacFcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsMacFcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsMacFcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsMacFcAgentTotalUsages = _ApmPaStatEpsMacFcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 88),
    _ApmPaStatEpsMacFcAgentTotalUsages_Type()
)
apmPaStatEpsMacFcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacFcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsMacFcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsMacFcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsMacFcAgentTotalSuccesses = _ApmPaStatEpsMacFcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 89),
    _ApmPaStatEpsMacFcAgentTotalSuccesses_Type()
)
apmPaStatEpsMacFcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacFcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsMacFcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsMacFcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsMacFcAgentTotalFailures = _ApmPaStatEpsMacFcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 90),
    _ApmPaStatEpsMacFcAgentTotalFailures_Type()
)
apmPaStatEpsMacFcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacFcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsMacFcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsMacFcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsMacFcAgentTotalErrors = _ApmPaStatEpsMacFcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 91),
    _ApmPaStatEpsMacFcAgentTotalErrors_Type()
)
apmPaStatEpsMacFcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacFcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsMacFcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsMacFcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsMacFcAgentTotalSessVars = _ApmPaStatEpsMacFcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 92),
    _ApmPaStatEpsMacFcAgentTotalSessVars_Type()
)
apmPaStatEpsMacFcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacFcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsMacPcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsMacPcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsMacPcAgentTotalInstances = _ApmPaStatEpsMacPcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 93),
    _ApmPaStatEpsMacPcAgentTotalInstances_Type()
)
apmPaStatEpsMacPcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacPcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsMacPcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsMacPcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsMacPcAgentTotalUsages = _ApmPaStatEpsMacPcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 94),
    _ApmPaStatEpsMacPcAgentTotalUsages_Type()
)
apmPaStatEpsMacPcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacPcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsMacPcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsMacPcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsMacPcAgentTotalSuccesses = _ApmPaStatEpsMacPcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 95),
    _ApmPaStatEpsMacPcAgentTotalSuccesses_Type()
)
apmPaStatEpsMacPcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacPcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsMacPcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsMacPcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsMacPcAgentTotalFailures = _ApmPaStatEpsMacPcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 96),
    _ApmPaStatEpsMacPcAgentTotalFailures_Type()
)
apmPaStatEpsMacPcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacPcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsMacPcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsMacPcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsMacPcAgentTotalErrors = _ApmPaStatEpsMacPcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 97),
    _ApmPaStatEpsMacPcAgentTotalErrors_Type()
)
apmPaStatEpsMacPcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacPcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsMacPcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsMacPcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsMacPcAgentTotalSessVars = _ApmPaStatEpsMacPcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 98),
    _ApmPaStatEpsMacPcAgentTotalSessVars_Type()
)
apmPaStatEpsMacPcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsMacPcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsWinCcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsWinCcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsWinCcAgentTotalInstances = _ApmPaStatEpsWinCcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 99),
    _ApmPaStatEpsWinCcAgentTotalInstances_Type()
)
apmPaStatEpsWinCcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinCcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsWinCcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsWinCcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsWinCcAgentTotalUsages = _ApmPaStatEpsWinCcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 100),
    _ApmPaStatEpsWinCcAgentTotalUsages_Type()
)
apmPaStatEpsWinCcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinCcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsWinCcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsWinCcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsWinCcAgentTotalSuccesses = _ApmPaStatEpsWinCcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 101),
    _ApmPaStatEpsWinCcAgentTotalSuccesses_Type()
)
apmPaStatEpsWinCcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinCcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsWinCcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsWinCcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsWinCcAgentTotalFailures = _ApmPaStatEpsWinCcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 102),
    _ApmPaStatEpsWinCcAgentTotalFailures_Type()
)
apmPaStatEpsWinCcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinCcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsWinCcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsWinCcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsWinCcAgentTotalErrors = _ApmPaStatEpsWinCcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 103),
    _ApmPaStatEpsWinCcAgentTotalErrors_Type()
)
apmPaStatEpsWinCcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinCcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsWinCcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsWinCcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsWinCcAgentTotalSessVars = _ApmPaStatEpsWinCcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 104),
    _ApmPaStatEpsWinCcAgentTotalSessVars_Type()
)
apmPaStatEpsWinCcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinCcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsAvAgentTotalInstances_Type = Counter64
_ApmPaStatEpsAvAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsAvAgentTotalInstances = _ApmPaStatEpsAvAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 105),
    _ApmPaStatEpsAvAgentTotalInstances_Type()
)
apmPaStatEpsAvAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsAvAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsAvAgentTotalUsages_Type = Counter64
_ApmPaStatEpsAvAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsAvAgentTotalUsages = _ApmPaStatEpsAvAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 106),
    _ApmPaStatEpsAvAgentTotalUsages_Type()
)
apmPaStatEpsAvAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsAvAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsAvAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsAvAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsAvAgentTotalSuccesses = _ApmPaStatEpsAvAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 107),
    _ApmPaStatEpsAvAgentTotalSuccesses_Type()
)
apmPaStatEpsAvAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsAvAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsAvAgentTotalFailures_Type = Counter64
_ApmPaStatEpsAvAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsAvAgentTotalFailures = _ApmPaStatEpsAvAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 108),
    _ApmPaStatEpsAvAgentTotalFailures_Type()
)
apmPaStatEpsAvAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsAvAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsAvAgentTotalErrors_Type = Counter64
_ApmPaStatEpsAvAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsAvAgentTotalErrors = _ApmPaStatEpsAvAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 109),
    _ApmPaStatEpsAvAgentTotalErrors_Type()
)
apmPaStatEpsAvAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsAvAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsAvAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsAvAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsAvAgentTotalSessVars = _ApmPaStatEpsAvAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 110),
    _ApmPaStatEpsAvAgentTotalSessVars_Type()
)
apmPaStatEpsAvAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsAvAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsWinOsInfoAgentTotalInstances_Type = Counter64
_ApmPaStatEpsWinOsInfoAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsWinOsInfoAgentTotalInstances = _ApmPaStatEpsWinOsInfoAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 111),
    _ApmPaStatEpsWinOsInfoAgentTotalInstances_Type()
)
apmPaStatEpsWinOsInfoAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinOsInfoAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsWinOsInfoAgentTotalUsages_Type = Counter64
_ApmPaStatEpsWinOsInfoAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsWinOsInfoAgentTotalUsages = _ApmPaStatEpsWinOsInfoAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 112),
    _ApmPaStatEpsWinOsInfoAgentTotalUsages_Type()
)
apmPaStatEpsWinOsInfoAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinOsInfoAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsWinOsInfoAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsWinOsInfoAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsWinOsInfoAgentTotalSuccesses = _ApmPaStatEpsWinOsInfoAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 113),
    _ApmPaStatEpsWinOsInfoAgentTotalSuccesses_Type()
)
apmPaStatEpsWinOsInfoAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinOsInfoAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsWinOsInfoAgentTotalFailures_Type = Counter64
_ApmPaStatEpsWinOsInfoAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsWinOsInfoAgentTotalFailures = _ApmPaStatEpsWinOsInfoAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 114),
    _ApmPaStatEpsWinOsInfoAgentTotalFailures_Type()
)
apmPaStatEpsWinOsInfoAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinOsInfoAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsWinOsInfoAgentTotalErrors_Type = Counter64
_ApmPaStatEpsWinOsInfoAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsWinOsInfoAgentTotalErrors = _ApmPaStatEpsWinOsInfoAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 115),
    _ApmPaStatEpsWinOsInfoAgentTotalErrors_Type()
)
apmPaStatEpsWinOsInfoAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinOsInfoAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsWinOsInfoAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsWinOsInfoAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsWinOsInfoAgentTotalSessVars = _ApmPaStatEpsWinOsInfoAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 116),
    _ApmPaStatEpsWinOsInfoAgentTotalSessVars_Type()
)
apmPaStatEpsWinOsInfoAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinOsInfoAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsWinFcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsWinFcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsWinFcAgentTotalInstances = _ApmPaStatEpsWinFcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 117),
    _ApmPaStatEpsWinFcAgentTotalInstances_Type()
)
apmPaStatEpsWinFcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinFcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsWinFcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsWinFcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsWinFcAgentTotalUsages = _ApmPaStatEpsWinFcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 118),
    _ApmPaStatEpsWinFcAgentTotalUsages_Type()
)
apmPaStatEpsWinFcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinFcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsWinFcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsWinFcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsWinFcAgentTotalSuccesses = _ApmPaStatEpsWinFcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 119),
    _ApmPaStatEpsWinFcAgentTotalSuccesses_Type()
)
apmPaStatEpsWinFcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinFcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsWinFcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsWinFcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsWinFcAgentTotalFailures = _ApmPaStatEpsWinFcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 120),
    _ApmPaStatEpsWinFcAgentTotalFailures_Type()
)
apmPaStatEpsWinFcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinFcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsWinFcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsWinFcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsWinFcAgentTotalErrors = _ApmPaStatEpsWinFcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 121),
    _ApmPaStatEpsWinFcAgentTotalErrors_Type()
)
apmPaStatEpsWinFcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinFcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsWinFcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsWinFcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsWinFcAgentTotalSessVars = _ApmPaStatEpsWinFcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 122),
    _ApmPaStatEpsWinFcAgentTotalSessVars_Type()
)
apmPaStatEpsWinFcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinFcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsWinMcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsWinMcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsWinMcAgentTotalInstances = _ApmPaStatEpsWinMcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 123),
    _ApmPaStatEpsWinMcAgentTotalInstances_Type()
)
apmPaStatEpsWinMcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinMcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsWinMcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsWinMcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsWinMcAgentTotalUsages = _ApmPaStatEpsWinMcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 124),
    _ApmPaStatEpsWinMcAgentTotalUsages_Type()
)
apmPaStatEpsWinMcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinMcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsWinMcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsWinMcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsWinMcAgentTotalSuccesses = _ApmPaStatEpsWinMcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 125),
    _ApmPaStatEpsWinMcAgentTotalSuccesses_Type()
)
apmPaStatEpsWinMcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinMcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsWinMcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsWinMcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsWinMcAgentTotalFailures = _ApmPaStatEpsWinMcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 126),
    _ApmPaStatEpsWinMcAgentTotalFailures_Type()
)
apmPaStatEpsWinMcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinMcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsWinMcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsWinMcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsWinMcAgentTotalErrors = _ApmPaStatEpsWinMcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 127),
    _ApmPaStatEpsWinMcAgentTotalErrors_Type()
)
apmPaStatEpsWinMcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinMcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsWinMcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsWinMcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsWinMcAgentTotalSessVars = _ApmPaStatEpsWinMcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 128),
    _ApmPaStatEpsWinMcAgentTotalSessVars_Type()
)
apmPaStatEpsWinMcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinMcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsFwcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsFwcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsFwcAgentTotalInstances = _ApmPaStatEpsFwcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 129),
    _ApmPaStatEpsFwcAgentTotalInstances_Type()
)
apmPaStatEpsFwcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsFwcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsFwcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsFwcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsFwcAgentTotalUsages = _ApmPaStatEpsFwcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 130),
    _ApmPaStatEpsFwcAgentTotalUsages_Type()
)
apmPaStatEpsFwcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsFwcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsFwcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsFwcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsFwcAgentTotalSuccesses = _ApmPaStatEpsFwcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 131),
    _ApmPaStatEpsFwcAgentTotalSuccesses_Type()
)
apmPaStatEpsFwcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsFwcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsFwcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsFwcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsFwcAgentTotalFailures = _ApmPaStatEpsFwcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 132),
    _ApmPaStatEpsFwcAgentTotalFailures_Type()
)
apmPaStatEpsFwcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsFwcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsFwcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsFwcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsFwcAgentTotalErrors = _ApmPaStatEpsFwcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 133),
    _ApmPaStatEpsFwcAgentTotalErrors_Type()
)
apmPaStatEpsFwcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsFwcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsFwcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsFwcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsFwcAgentTotalSessVars = _ApmPaStatEpsFwcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 134),
    _ApmPaStatEpsFwcAgentTotalSessVars_Type()
)
apmPaStatEpsFwcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsFwcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsWinPcTotalInstances_Type = Counter64
_ApmPaStatEpsWinPcTotalInstances_Object = MibTableColumn
apmPaStatEpsWinPcTotalInstances = _ApmPaStatEpsWinPcTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 135),
    _ApmPaStatEpsWinPcTotalInstances_Type()
)
apmPaStatEpsWinPcTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPcTotalInstances.setStatus("deprecated")
_ApmPaStatEpsWinPcTotalUsages_Type = Counter64
_ApmPaStatEpsWinPcTotalUsages_Object = MibTableColumn
apmPaStatEpsWinPcTotalUsages = _ApmPaStatEpsWinPcTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 136),
    _ApmPaStatEpsWinPcTotalUsages_Type()
)
apmPaStatEpsWinPcTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPcTotalUsages.setStatus("deprecated")
_ApmPaStatEpsWinPcTotalSuccesses_Type = Counter64
_ApmPaStatEpsWinPcTotalSuccesses_Object = MibTableColumn
apmPaStatEpsWinPcTotalSuccesses = _ApmPaStatEpsWinPcTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 137),
    _ApmPaStatEpsWinPcTotalSuccesses_Type()
)
apmPaStatEpsWinPcTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPcTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsWinPcTotalFailures_Type = Counter64
_ApmPaStatEpsWinPcTotalFailures_Object = MibTableColumn
apmPaStatEpsWinPcTotalFailures = _ApmPaStatEpsWinPcTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 138),
    _ApmPaStatEpsWinPcTotalFailures_Type()
)
apmPaStatEpsWinPcTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPcTotalFailures.setStatus("deprecated")
_ApmPaStatEpsWinPcTotalErrors_Type = Counter64
_ApmPaStatEpsWinPcTotalErrors_Object = MibTableColumn
apmPaStatEpsWinPcTotalErrors = _ApmPaStatEpsWinPcTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 139),
    _ApmPaStatEpsWinPcTotalErrors_Type()
)
apmPaStatEpsWinPcTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPcTotalErrors.setStatus("deprecated")
_ApmPaStatEpsWinPcTotalSessVars_Type = Counter64
_ApmPaStatEpsWinPcTotalSessVars_Object = MibTableColumn
apmPaStatEpsWinPcTotalSessVars = _ApmPaStatEpsWinPcTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 140),
    _ApmPaStatEpsWinPcTotalSessVars_Type()
)
apmPaStatEpsWinPcTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPcTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsWinPwTotalInstances_Type = Counter64
_ApmPaStatEpsWinPwTotalInstances_Object = MibTableColumn
apmPaStatEpsWinPwTotalInstances = _ApmPaStatEpsWinPwTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 141),
    _ApmPaStatEpsWinPwTotalInstances_Type()
)
apmPaStatEpsWinPwTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPwTotalInstances.setStatus("deprecated")
_ApmPaStatEpsWinPwTotalUsages_Type = Counter64
_ApmPaStatEpsWinPwTotalUsages_Object = MibTableColumn
apmPaStatEpsWinPwTotalUsages = _ApmPaStatEpsWinPwTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 142),
    _ApmPaStatEpsWinPwTotalUsages_Type()
)
apmPaStatEpsWinPwTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPwTotalUsages.setStatus("deprecated")
_ApmPaStatEpsWinPwTotalSuccesses_Type = Counter64
_ApmPaStatEpsWinPwTotalSuccesses_Object = MibTableColumn
apmPaStatEpsWinPwTotalSuccesses = _ApmPaStatEpsWinPwTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 143),
    _ApmPaStatEpsWinPwTotalSuccesses_Type()
)
apmPaStatEpsWinPwTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPwTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsWinPwTotalFailures_Type = Counter64
_ApmPaStatEpsWinPwTotalFailures_Object = MibTableColumn
apmPaStatEpsWinPwTotalFailures = _ApmPaStatEpsWinPwTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 144),
    _ApmPaStatEpsWinPwTotalFailures_Type()
)
apmPaStatEpsWinPwTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPwTotalFailures.setStatus("deprecated")
_ApmPaStatEpsWinPwTotalErrors_Type = Counter64
_ApmPaStatEpsWinPwTotalErrors_Object = MibTableColumn
apmPaStatEpsWinPwTotalErrors = _ApmPaStatEpsWinPwTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 145),
    _ApmPaStatEpsWinPwTotalErrors_Type()
)
apmPaStatEpsWinPwTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPwTotalErrors.setStatus("deprecated")
_ApmPaStatEpsWinPwTotalSessVars_Type = Counter64
_ApmPaStatEpsWinPwTotalSessVars_Object = MibTableColumn
apmPaStatEpsWinPwTotalSessVars = _ApmPaStatEpsWinPwTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 146),
    _ApmPaStatEpsWinPwTotalSessVars_Type()
)
apmPaStatEpsWinPwTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinPwTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsWinRcAgentTotalInstances_Type = Counter64
_ApmPaStatEpsWinRcAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsWinRcAgentTotalInstances = _ApmPaStatEpsWinRcAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 147),
    _ApmPaStatEpsWinRcAgentTotalInstances_Type()
)
apmPaStatEpsWinRcAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinRcAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsWinRcAgentTotalUsages_Type = Counter64
_ApmPaStatEpsWinRcAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsWinRcAgentTotalUsages = _ApmPaStatEpsWinRcAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 148),
    _ApmPaStatEpsWinRcAgentTotalUsages_Type()
)
apmPaStatEpsWinRcAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinRcAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsWinRcAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsWinRcAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsWinRcAgentTotalSuccesses = _ApmPaStatEpsWinRcAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 149),
    _ApmPaStatEpsWinRcAgentTotalSuccesses_Type()
)
apmPaStatEpsWinRcAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinRcAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsWinRcAgentTotalFailures_Type = Counter64
_ApmPaStatEpsWinRcAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsWinRcAgentTotalFailures = _ApmPaStatEpsWinRcAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 150),
    _ApmPaStatEpsWinRcAgentTotalFailures_Type()
)
apmPaStatEpsWinRcAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinRcAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsWinRcAgentTotalErrors_Type = Counter64
_ApmPaStatEpsWinRcAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsWinRcAgentTotalErrors = _ApmPaStatEpsWinRcAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 151),
    _ApmPaStatEpsWinRcAgentTotalErrors_Type()
)
apmPaStatEpsWinRcAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinRcAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsWinRcAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsWinRcAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsWinRcAgentTotalSessVars = _ApmPaStatEpsWinRcAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 152),
    _ApmPaStatEpsWinRcAgentTotalSessVars_Type()
)
apmPaStatEpsWinRcAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinRcAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatEpsWinGpAgentTotalInstances_Type = Counter64
_ApmPaStatEpsWinGpAgentTotalInstances_Object = MibTableColumn
apmPaStatEpsWinGpAgentTotalInstances = _ApmPaStatEpsWinGpAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 153),
    _ApmPaStatEpsWinGpAgentTotalInstances_Type()
)
apmPaStatEpsWinGpAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinGpAgentTotalInstances.setStatus("deprecated")
_ApmPaStatEpsWinGpAgentTotalUsages_Type = Counter64
_ApmPaStatEpsWinGpAgentTotalUsages_Object = MibTableColumn
apmPaStatEpsWinGpAgentTotalUsages = _ApmPaStatEpsWinGpAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 154),
    _ApmPaStatEpsWinGpAgentTotalUsages_Type()
)
apmPaStatEpsWinGpAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinGpAgentTotalUsages.setStatus("deprecated")
_ApmPaStatEpsWinGpAgentTotalSuccesses_Type = Counter64
_ApmPaStatEpsWinGpAgentTotalSuccesses_Object = MibTableColumn
apmPaStatEpsWinGpAgentTotalSuccesses = _ApmPaStatEpsWinGpAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 155),
    _ApmPaStatEpsWinGpAgentTotalSuccesses_Type()
)
apmPaStatEpsWinGpAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinGpAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatEpsWinGpAgentTotalFailures_Type = Counter64
_ApmPaStatEpsWinGpAgentTotalFailures_Object = MibTableColumn
apmPaStatEpsWinGpAgentTotalFailures = _ApmPaStatEpsWinGpAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 156),
    _ApmPaStatEpsWinGpAgentTotalFailures_Type()
)
apmPaStatEpsWinGpAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinGpAgentTotalFailures.setStatus("deprecated")
_ApmPaStatEpsWinGpAgentTotalErrors_Type = Counter64
_ApmPaStatEpsWinGpAgentTotalErrors_Object = MibTableColumn
apmPaStatEpsWinGpAgentTotalErrors = _ApmPaStatEpsWinGpAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 157),
    _ApmPaStatEpsWinGpAgentTotalErrors_Type()
)
apmPaStatEpsWinGpAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinGpAgentTotalErrors.setStatus("deprecated")
_ApmPaStatEpsWinGpAgentTotalSessVars_Type = Counter64
_ApmPaStatEpsWinGpAgentTotalSessVars_Object = MibTableColumn
apmPaStatEpsWinGpAgentTotalSessVars = _ApmPaStatEpsWinGpAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 158),
    _ApmPaStatEpsWinGpAgentTotalSessVars_Type()
)
apmPaStatEpsWinGpAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatEpsWinGpAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatExternalLogonAgentTotalInstances_Type = Counter64
_ApmPaStatExternalLogonAgentTotalInstances_Object = MibTableColumn
apmPaStatExternalLogonAgentTotalInstances = _ApmPaStatExternalLogonAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 159),
    _ApmPaStatExternalLogonAgentTotalInstances_Type()
)
apmPaStatExternalLogonAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatExternalLogonAgentTotalInstances.setStatus("deprecated")
_ApmPaStatExternalLogonAgentTotalUsages_Type = Counter64
_ApmPaStatExternalLogonAgentTotalUsages_Object = MibTableColumn
apmPaStatExternalLogonAgentTotalUsages = _ApmPaStatExternalLogonAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 160),
    _ApmPaStatExternalLogonAgentTotalUsages_Type()
)
apmPaStatExternalLogonAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatExternalLogonAgentTotalUsages.setStatus("deprecated")
_ApmPaStatExternalLogonAgentTotalSuccesses_Type = Counter64
_ApmPaStatExternalLogonAgentTotalSuccesses_Object = MibTableColumn
apmPaStatExternalLogonAgentTotalSuccesses = _ApmPaStatExternalLogonAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 161),
    _ApmPaStatExternalLogonAgentTotalSuccesses_Type()
)
apmPaStatExternalLogonAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatExternalLogonAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatExternalLogonAgentTotalFailures_Type = Counter64
_ApmPaStatExternalLogonAgentTotalFailures_Object = MibTableColumn
apmPaStatExternalLogonAgentTotalFailures = _ApmPaStatExternalLogonAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 162),
    _ApmPaStatExternalLogonAgentTotalFailures_Type()
)
apmPaStatExternalLogonAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatExternalLogonAgentTotalFailures.setStatus("deprecated")
_ApmPaStatExternalLogonAgentTotalErrors_Type = Counter64
_ApmPaStatExternalLogonAgentTotalErrors_Object = MibTableColumn
apmPaStatExternalLogonAgentTotalErrors = _ApmPaStatExternalLogonAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 163),
    _ApmPaStatExternalLogonAgentTotalErrors_Type()
)
apmPaStatExternalLogonAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatExternalLogonAgentTotalErrors.setStatus("deprecated")
_ApmPaStatExternalLogonAgentTotalSessVars_Type = Counter64
_ApmPaStatExternalLogonAgentTotalSessVars_Object = MibTableColumn
apmPaStatExternalLogonAgentTotalSessVars = _ApmPaStatExternalLogonAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 164),
    _ApmPaStatExternalLogonAgentTotalSessVars_Type()
)
apmPaStatExternalLogonAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatExternalLogonAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatLogonAgentTotalInstances_Type = Counter64
_ApmPaStatLogonAgentTotalInstances_Object = MibTableColumn
apmPaStatLogonAgentTotalInstances = _ApmPaStatLogonAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 165),
    _ApmPaStatLogonAgentTotalInstances_Type()
)
apmPaStatLogonAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLogonAgentTotalInstances.setStatus("deprecated")
_ApmPaStatLogonAgentTotalUsages_Type = Counter64
_ApmPaStatLogonAgentTotalUsages_Object = MibTableColumn
apmPaStatLogonAgentTotalUsages = _ApmPaStatLogonAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 166),
    _ApmPaStatLogonAgentTotalUsages_Type()
)
apmPaStatLogonAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLogonAgentTotalUsages.setStatus("deprecated")
_ApmPaStatLogonAgentTotalSuccesses_Type = Counter64
_ApmPaStatLogonAgentTotalSuccesses_Object = MibTableColumn
apmPaStatLogonAgentTotalSuccesses = _ApmPaStatLogonAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 167),
    _ApmPaStatLogonAgentTotalSuccesses_Type()
)
apmPaStatLogonAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLogonAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatLogonAgentTotalFailures_Type = Counter64
_ApmPaStatLogonAgentTotalFailures_Object = MibTableColumn
apmPaStatLogonAgentTotalFailures = _ApmPaStatLogonAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 168),
    _ApmPaStatLogonAgentTotalFailures_Type()
)
apmPaStatLogonAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLogonAgentTotalFailures.setStatus("deprecated")
_ApmPaStatLogonAgentTotalErrors_Type = Counter64
_ApmPaStatLogonAgentTotalErrors_Object = MibTableColumn
apmPaStatLogonAgentTotalErrors = _ApmPaStatLogonAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 169),
    _ApmPaStatLogonAgentTotalErrors_Type()
)
apmPaStatLogonAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLogonAgentTotalErrors.setStatus("deprecated")
_ApmPaStatLogonAgentTotalSessVars_Type = Counter64
_ApmPaStatLogonAgentTotalSessVars_Object = MibTableColumn
apmPaStatLogonAgentTotalSessVars = _ApmPaStatLogonAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 170),
    _ApmPaStatLogonAgentTotalSessVars_Type()
)
apmPaStatLogonAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLogonAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatRaAgentTotalInstances_Type = Counter64
_ApmPaStatRaAgentTotalInstances_Object = MibTableColumn
apmPaStatRaAgentTotalInstances = _ApmPaStatRaAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 171),
    _ApmPaStatRaAgentTotalInstances_Type()
)
apmPaStatRaAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRaAgentTotalInstances.setStatus("deprecated")
_ApmPaStatRaAgentTotalUsages_Type = Counter64
_ApmPaStatRaAgentTotalUsages_Object = MibTableColumn
apmPaStatRaAgentTotalUsages = _ApmPaStatRaAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 172),
    _ApmPaStatRaAgentTotalUsages_Type()
)
apmPaStatRaAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRaAgentTotalUsages.setStatus("deprecated")
_ApmPaStatRaAgentTotalSuccesses_Type = Counter64
_ApmPaStatRaAgentTotalSuccesses_Object = MibTableColumn
apmPaStatRaAgentTotalSuccesses = _ApmPaStatRaAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 173),
    _ApmPaStatRaAgentTotalSuccesses_Type()
)
apmPaStatRaAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRaAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatRaAgentTotalFailures_Type = Counter64
_ApmPaStatRaAgentTotalFailures_Object = MibTableColumn
apmPaStatRaAgentTotalFailures = _ApmPaStatRaAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 174),
    _ApmPaStatRaAgentTotalFailures_Type()
)
apmPaStatRaAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRaAgentTotalFailures.setStatus("deprecated")
_ApmPaStatRaAgentTotalErrors_Type = Counter64
_ApmPaStatRaAgentTotalErrors_Object = MibTableColumn
apmPaStatRaAgentTotalErrors = _ApmPaStatRaAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 175),
    _ApmPaStatRaAgentTotalErrors_Type()
)
apmPaStatRaAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRaAgentTotalErrors.setStatus("deprecated")
_ApmPaStatRaAgentTotalSessVars_Type = Counter64
_ApmPaStatRaAgentTotalSessVars_Object = MibTableColumn
apmPaStatRaAgentTotalSessVars = _ApmPaStatRaAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 176),
    _ApmPaStatRaAgentTotalSessVars_Type()
)
apmPaStatRaAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRaAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatRdsAgentTotalInstances_Type = Counter64
_ApmPaStatRdsAgentTotalInstances_Object = MibTableColumn
apmPaStatRdsAgentTotalInstances = _ApmPaStatRdsAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 177),
    _ApmPaStatRdsAgentTotalInstances_Type()
)
apmPaStatRdsAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRdsAgentTotalInstances.setStatus("deprecated")
_ApmPaStatRdsAgentTotalUsages_Type = Counter64
_ApmPaStatRdsAgentTotalUsages_Object = MibTableColumn
apmPaStatRdsAgentTotalUsages = _ApmPaStatRdsAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 178),
    _ApmPaStatRdsAgentTotalUsages_Type()
)
apmPaStatRdsAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRdsAgentTotalUsages.setStatus("deprecated")
_ApmPaStatRdsAgentTotalSuccesses_Type = Counter64
_ApmPaStatRdsAgentTotalSuccesses_Object = MibTableColumn
apmPaStatRdsAgentTotalSuccesses = _ApmPaStatRdsAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 179),
    _ApmPaStatRdsAgentTotalSuccesses_Type()
)
apmPaStatRdsAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRdsAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatRdsAgentTotalFailures_Type = Counter64
_ApmPaStatRdsAgentTotalFailures_Object = MibTableColumn
apmPaStatRdsAgentTotalFailures = _ApmPaStatRdsAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 180),
    _ApmPaStatRdsAgentTotalFailures_Type()
)
apmPaStatRdsAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRdsAgentTotalFailures.setStatus("deprecated")
_ApmPaStatRdsAgentTotalErrors_Type = Counter64
_ApmPaStatRdsAgentTotalErrors_Object = MibTableColumn
apmPaStatRdsAgentTotalErrors = _ApmPaStatRdsAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 181),
    _ApmPaStatRdsAgentTotalErrors_Type()
)
apmPaStatRdsAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRdsAgentTotalErrors.setStatus("deprecated")
_ApmPaStatRdsAgentTotalSessVars_Type = Counter64
_ApmPaStatRdsAgentTotalSessVars_Object = MibTableColumn
apmPaStatRdsAgentTotalSessVars = _ApmPaStatRdsAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 182),
    _ApmPaStatRdsAgentTotalSessVars_Type()
)
apmPaStatRdsAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatRdsAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatVaAgentTotalInstances_Type = Counter64
_ApmPaStatVaAgentTotalInstances_Object = MibTableColumn
apmPaStatVaAgentTotalInstances = _ApmPaStatVaAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 183),
    _ApmPaStatVaAgentTotalInstances_Type()
)
apmPaStatVaAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatVaAgentTotalInstances.setStatus("deprecated")
_ApmPaStatVaAgentTotalUsages_Type = Counter64
_ApmPaStatVaAgentTotalUsages_Object = MibTableColumn
apmPaStatVaAgentTotalUsages = _ApmPaStatVaAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 184),
    _ApmPaStatVaAgentTotalUsages_Type()
)
apmPaStatVaAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatVaAgentTotalUsages.setStatus("deprecated")
_ApmPaStatVaAgentTotalSuccesses_Type = Counter64
_ApmPaStatVaAgentTotalSuccesses_Object = MibTableColumn
apmPaStatVaAgentTotalSuccesses = _ApmPaStatVaAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 185),
    _ApmPaStatVaAgentTotalSuccesses_Type()
)
apmPaStatVaAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatVaAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatVaAgentTotalFailures_Type = Counter64
_ApmPaStatVaAgentTotalFailures_Object = MibTableColumn
apmPaStatVaAgentTotalFailures = _ApmPaStatVaAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 186),
    _ApmPaStatVaAgentTotalFailures_Type()
)
apmPaStatVaAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatVaAgentTotalFailures.setStatus("deprecated")
_ApmPaStatVaAgentTotalErrors_Type = Counter64
_ApmPaStatVaAgentTotalErrors_Object = MibTableColumn
apmPaStatVaAgentTotalErrors = _ApmPaStatVaAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 187),
    _ApmPaStatVaAgentTotalErrors_Type()
)
apmPaStatVaAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatVaAgentTotalErrors.setStatus("deprecated")
_ApmPaStatVaAgentTotalSessVars_Type = Counter64
_ApmPaStatVaAgentTotalSessVars_Object = MibTableColumn
apmPaStatVaAgentTotalSessVars = _ApmPaStatVaAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 188),
    _ApmPaStatVaAgentTotalSessVars_Type()
)
apmPaStatVaAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatVaAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatIeAgentTotalInstances_Type = Counter64
_ApmPaStatIeAgentTotalInstances_Object = MibTableColumn
apmPaStatIeAgentTotalInstances = _ApmPaStatIeAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 189),
    _ApmPaStatIeAgentTotalInstances_Type()
)
apmPaStatIeAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatIeAgentTotalInstances.setStatus("deprecated")
_ApmPaStatIeAgentTotalUsages_Type = Counter64
_ApmPaStatIeAgentTotalUsages_Object = MibTableColumn
apmPaStatIeAgentTotalUsages = _ApmPaStatIeAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 190),
    _ApmPaStatIeAgentTotalUsages_Type()
)
apmPaStatIeAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatIeAgentTotalUsages.setStatus("deprecated")
_ApmPaStatIeAgentTotalSuccesses_Type = Counter64
_ApmPaStatIeAgentTotalSuccesses_Object = MibTableColumn
apmPaStatIeAgentTotalSuccesses = _ApmPaStatIeAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 191),
    _ApmPaStatIeAgentTotalSuccesses_Type()
)
apmPaStatIeAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatIeAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatIeAgentTotalFailures_Type = Counter64
_ApmPaStatIeAgentTotalFailures_Object = MibTableColumn
apmPaStatIeAgentTotalFailures = _ApmPaStatIeAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 192),
    _ApmPaStatIeAgentTotalFailures_Type()
)
apmPaStatIeAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatIeAgentTotalFailures.setStatus("deprecated")
_ApmPaStatIeAgentTotalErrors_Type = Counter64
_ApmPaStatIeAgentTotalErrors_Object = MibTableColumn
apmPaStatIeAgentTotalErrors = _ApmPaStatIeAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 193),
    _ApmPaStatIeAgentTotalErrors_Type()
)
apmPaStatIeAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatIeAgentTotalErrors.setStatus("deprecated")
_ApmPaStatIeAgentTotalSessVars_Type = Counter64
_ApmPaStatIeAgentTotalSessVars_Object = MibTableColumn
apmPaStatIeAgentTotalSessVars = _ApmPaStatIeAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 194),
    _ApmPaStatIeAgentTotalSessVars_Type()
)
apmPaStatIeAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatIeAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatLoggingAgentTotalInstances_Type = Counter64
_ApmPaStatLoggingAgentTotalInstances_Object = MibTableColumn
apmPaStatLoggingAgentTotalInstances = _ApmPaStatLoggingAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 195),
    _ApmPaStatLoggingAgentTotalInstances_Type()
)
apmPaStatLoggingAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLoggingAgentTotalInstances.setStatus("deprecated")
_ApmPaStatLoggingAgentTotalUsages_Type = Counter64
_ApmPaStatLoggingAgentTotalUsages_Object = MibTableColumn
apmPaStatLoggingAgentTotalUsages = _ApmPaStatLoggingAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 196),
    _ApmPaStatLoggingAgentTotalUsages_Type()
)
apmPaStatLoggingAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLoggingAgentTotalUsages.setStatus("deprecated")
_ApmPaStatLoggingAgentTotalSuccesses_Type = Counter64
_ApmPaStatLoggingAgentTotalSuccesses_Object = MibTableColumn
apmPaStatLoggingAgentTotalSuccesses = _ApmPaStatLoggingAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 197),
    _ApmPaStatLoggingAgentTotalSuccesses_Type()
)
apmPaStatLoggingAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLoggingAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatLoggingAgentTotalFailures_Type = Counter64
_ApmPaStatLoggingAgentTotalFailures_Object = MibTableColumn
apmPaStatLoggingAgentTotalFailures = _ApmPaStatLoggingAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 198),
    _ApmPaStatLoggingAgentTotalFailures_Type()
)
apmPaStatLoggingAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLoggingAgentTotalFailures.setStatus("deprecated")
_ApmPaStatLoggingAgentTotalErrors_Type = Counter64
_ApmPaStatLoggingAgentTotalErrors_Object = MibTableColumn
apmPaStatLoggingAgentTotalErrors = _ApmPaStatLoggingAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 199),
    _ApmPaStatLoggingAgentTotalErrors_Type()
)
apmPaStatLoggingAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLoggingAgentTotalErrors.setStatus("deprecated")
_ApmPaStatLoggingAgentTotalSessVars_Type = Counter64
_ApmPaStatLoggingAgentTotalSessVars_Object = MibTableColumn
apmPaStatLoggingAgentTotalSessVars = _ApmPaStatLoggingAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 200),
    _ApmPaStatLoggingAgentTotalSessVars_Type()
)
apmPaStatLoggingAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatLoggingAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatDecnBoxAgentTotalInstances_Type = Counter64
_ApmPaStatDecnBoxAgentTotalInstances_Object = MibTableColumn
apmPaStatDecnBoxAgentTotalInstances = _ApmPaStatDecnBoxAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 201),
    _ApmPaStatDecnBoxAgentTotalInstances_Type()
)
apmPaStatDecnBoxAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatDecnBoxAgentTotalInstances.setStatus("deprecated")
_ApmPaStatDecnBoxAgentTotalUsages_Type = Counter64
_ApmPaStatDecnBoxAgentTotalUsages_Object = MibTableColumn
apmPaStatDecnBoxAgentTotalUsages = _ApmPaStatDecnBoxAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 202),
    _ApmPaStatDecnBoxAgentTotalUsages_Type()
)
apmPaStatDecnBoxAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatDecnBoxAgentTotalUsages.setStatus("deprecated")
_ApmPaStatDecnBoxAgentTotalSuccesses_Type = Counter64
_ApmPaStatDecnBoxAgentTotalSuccesses_Object = MibTableColumn
apmPaStatDecnBoxAgentTotalSuccesses = _ApmPaStatDecnBoxAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 203),
    _ApmPaStatDecnBoxAgentTotalSuccesses_Type()
)
apmPaStatDecnBoxAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatDecnBoxAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatDecnBoxAgentTotalFailures_Type = Counter64
_ApmPaStatDecnBoxAgentTotalFailures_Object = MibTableColumn
apmPaStatDecnBoxAgentTotalFailures = _ApmPaStatDecnBoxAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 204),
    _ApmPaStatDecnBoxAgentTotalFailures_Type()
)
apmPaStatDecnBoxAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatDecnBoxAgentTotalFailures.setStatus("deprecated")
_ApmPaStatDecnBoxAgentTotalErrors_Type = Counter64
_ApmPaStatDecnBoxAgentTotalErrors_Object = MibTableColumn
apmPaStatDecnBoxAgentTotalErrors = _ApmPaStatDecnBoxAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 205),
    _ApmPaStatDecnBoxAgentTotalErrors_Type()
)
apmPaStatDecnBoxAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatDecnBoxAgentTotalErrors.setStatus("deprecated")
_ApmPaStatDecnBoxAgentTotalSessVars_Type = Counter64
_ApmPaStatDecnBoxAgentTotalSessVars_Object = MibTableColumn
apmPaStatDecnBoxAgentTotalSessVars = _ApmPaStatDecnBoxAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 206),
    _ApmPaStatDecnBoxAgentTotalSessVars_Type()
)
apmPaStatDecnBoxAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatDecnBoxAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatMesgBoxAgentTotalInstances_Type = Counter64
_ApmPaStatMesgBoxAgentTotalInstances_Object = MibTableColumn
apmPaStatMesgBoxAgentTotalInstances = _ApmPaStatMesgBoxAgentTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 207),
    _ApmPaStatMesgBoxAgentTotalInstances_Type()
)
apmPaStatMesgBoxAgentTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatMesgBoxAgentTotalInstances.setStatus("deprecated")
_ApmPaStatMesgBoxAgentTotalUsages_Type = Counter64
_ApmPaStatMesgBoxAgentTotalUsages_Object = MibTableColumn
apmPaStatMesgBoxAgentTotalUsages = _ApmPaStatMesgBoxAgentTotalUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 208),
    _ApmPaStatMesgBoxAgentTotalUsages_Type()
)
apmPaStatMesgBoxAgentTotalUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatMesgBoxAgentTotalUsages.setStatus("deprecated")
_ApmPaStatMesgBoxAgentTotalSuccesses_Type = Counter64
_ApmPaStatMesgBoxAgentTotalSuccesses_Object = MibTableColumn
apmPaStatMesgBoxAgentTotalSuccesses = _ApmPaStatMesgBoxAgentTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 209),
    _ApmPaStatMesgBoxAgentTotalSuccesses_Type()
)
apmPaStatMesgBoxAgentTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatMesgBoxAgentTotalSuccesses.setStatus("deprecated")
_ApmPaStatMesgBoxAgentTotalFailures_Type = Counter64
_ApmPaStatMesgBoxAgentTotalFailures_Object = MibTableColumn
apmPaStatMesgBoxAgentTotalFailures = _ApmPaStatMesgBoxAgentTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 210),
    _ApmPaStatMesgBoxAgentTotalFailures_Type()
)
apmPaStatMesgBoxAgentTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatMesgBoxAgentTotalFailures.setStatus("deprecated")
_ApmPaStatMesgBoxAgentTotalErrors_Type = Counter64
_ApmPaStatMesgBoxAgentTotalErrors_Object = MibTableColumn
apmPaStatMesgBoxAgentTotalErrors = _ApmPaStatMesgBoxAgentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 211),
    _ApmPaStatMesgBoxAgentTotalErrors_Type()
)
apmPaStatMesgBoxAgentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatMesgBoxAgentTotalErrors.setStatus("deprecated")
_ApmPaStatMesgBoxAgentTotalSessVars_Type = Counter64
_ApmPaStatMesgBoxAgentTotalSessVars_Object = MibTableColumn
apmPaStatMesgBoxAgentTotalSessVars = _ApmPaStatMesgBoxAgentTotalSessVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 212),
    _ApmPaStatMesgBoxAgentTotalSessVars_Type()
)
apmPaStatMesgBoxAgentTotalSessVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatMesgBoxAgentTotalSessVars.setStatus("deprecated")
_ApmPaStatApdNoResultErrors_Type = Counter64
_ApmPaStatApdNoResultErrors_Object = MibTableColumn
apmPaStatApdNoResultErrors = _ApmPaStatApdNoResultErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 213),
    _ApmPaStatApdNoResultErrors_Type()
)
apmPaStatApdNoResultErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdNoResultErrors.setStatus("deprecated")
_ApmPaStatApdNoSessionErrors_Type = Counter64
_ApmPaStatApdNoSessionErrors_Object = MibTableColumn
apmPaStatApdNoSessionErrors = _ApmPaStatApdNoSessionErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 214),
    _ApmPaStatApdNoSessionErrors_Type()
)
apmPaStatApdNoSessionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdNoSessionErrors.setStatus("deprecated")
_ApmPaStatApdNoDeviceInfoErrors_Type = Counter64
_ApmPaStatApdNoDeviceInfoErrors_Object = MibTableColumn
apmPaStatApdNoDeviceInfoErrors = _ApmPaStatApdNoDeviceInfoErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 215),
    _ApmPaStatApdNoDeviceInfoErrors_Type()
)
apmPaStatApdNoDeviceInfoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdNoDeviceInfoErrors.setStatus("deprecated")
_ApmPaStatApdNoTokenErrors_Type = Counter64
_ApmPaStatApdNoTokenErrors_Object = MibTableColumn
apmPaStatApdNoTokenErrors = _ApmPaStatApdNoTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 216),
    _ApmPaStatApdNoTokenErrors_Type()
)
apmPaStatApdNoTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdNoTokenErrors.setStatus("deprecated")
_ApmPaStatApdNoSigErrors_Type = Counter64
_ApmPaStatApdNoSigErrors_Object = MibTableColumn
apmPaStatApdNoSigErrors = _ApmPaStatApdNoSigErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 217),
    _ApmPaStatApdNoSigErrors_Type()
)
apmPaStatApdNoSigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdNoSigErrors.setStatus("deprecated")
_ApmPaStatApdTotalMismatchErrors_Type = Counter64
_ApmPaStatApdTotalMismatchErrors_Object = MibTableColumn
apmPaStatApdTotalMismatchErrors = _ApmPaStatApdTotalMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 218),
    _ApmPaStatApdTotalMismatchErrors_Type()
)
apmPaStatApdTotalMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdTotalMismatchErrors.setStatus("deprecated")
_ApmPaStatApdInvalidSigErrors_Type = Counter64
_ApmPaStatApdInvalidSigErrors_Object = MibTableColumn
apmPaStatApdInvalidSigErrors = _ApmPaStatApdInvalidSigErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 219),
    _ApmPaStatApdInvalidSigErrors_Type()
)
apmPaStatApdInvalidSigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdInvalidSigErrors.setStatus("deprecated")
_ApmPaStatApdMcPipelineInitErrors_Type = Counter64
_ApmPaStatApdMcPipelineInitErrors_Object = MibTableColumn
apmPaStatApdMcPipelineInitErrors = _ApmPaStatApdMcPipelineInitErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 220),
    _ApmPaStatApdMcPipelineInitErrors_Type()
)
apmPaStatApdMcPipelineInitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdMcPipelineInitErrors.setStatus("deprecated")
_ApmPaStatApdMcSetSessVarErrors_Type = Counter64
_ApmPaStatApdMcSetSessVarErrors_Object = MibTableColumn
apmPaStatApdMcSetSessVarErrors = _ApmPaStatApdMcSetSessVarErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 221),
    _ApmPaStatApdMcSetSessVarErrors_Type()
)
apmPaStatApdMcSetSessVarErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdMcSetSessVarErrors.setStatus("deprecated")
_ApmPaStatApdMcPipelineCloseErrors_Type = Counter64
_ApmPaStatApdMcPipelineCloseErrors_Object = MibTableColumn
apmPaStatApdMcPipelineCloseErrors = _ApmPaStatApdMcPipelineCloseErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 222),
    _ApmPaStatApdMcPipelineCloseErrors_Type()
)
apmPaStatApdMcPipelineCloseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdMcPipelineCloseErrors.setStatus("deprecated")
_ApmPaStatApdApResultErrors_Type = Counter64
_ApmPaStatApdApResultErrors_Object = MibTableColumn
apmPaStatApdApResultErrors = _ApmPaStatApdApResultErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 223),
    _ApmPaStatApdApResultErrors_Type()
)
apmPaStatApdApResultErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdApResultErrors.setStatus("deprecated")
_ApmPaStatApdApInternalErrors_Type = Counter64
_ApmPaStatApdApInternalErrors_Object = MibTableColumn
apmPaStatApdApInternalErrors = _ApmPaStatApdApInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 224),
    _ApmPaStatApdApInternalErrors_Type()
)
apmPaStatApdApInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatApdApInternalErrors.setStatus("deprecated")
_ApmPaStatAllowedRequests_Type = Counter64
_ApmPaStatAllowedRequests_Object = MibTableColumn
apmPaStatAllowedRequests = _ApmPaStatAllowedRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 225),
    _ApmPaStatAllowedRequests_Type()
)
apmPaStatAllowedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatAllowedRequests.setStatus("current")
_ApmPaStatDeniedRequests_Type = Counter64
_ApmPaStatDeniedRequests_Object = MibTableColumn
apmPaStatDeniedRequests = _ApmPaStatDeniedRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 226),
    _ApmPaStatDeniedRequests_Type()
)
apmPaStatDeniedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatDeniedRequests.setStatus("current")
_ApmPaStatVsName_Type = LongDisplayString
_ApmPaStatVsName_Object = MibTableColumn
apmPaStatVsName = _ApmPaStatVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 1, 3, 1, 227),
    _ApmPaStatVsName_Type()
)
apmPaStatVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPaStatVsName.setStatus("current")
_ApmProfileConnectivityStat_ObjectIdentity = ObjectIdentity
apmProfileConnectivityStat = _ApmProfileConnectivityStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2)
)
_ApmPcStatResetStats_Type = Integer32
_ApmPcStatResetStats_Object = MibScalar
apmPcStatResetStats = _ApmPcStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 1),
    _ApmPcStatResetStats_Type()
)
apmPcStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmPcStatResetStats.setStatus("current")
_ApmPcStatNumber_Type = Integer32
_ApmPcStatNumber_Object = MibScalar
apmPcStatNumber = _ApmPcStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 2),
    _ApmPcStatNumber_Type()
)
apmPcStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatNumber.setStatus("current")
_ApmPcStatTable_Object = MibTable
apmPcStatTable = _ApmPcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    apmPcStatTable.setStatus("current")
_ApmPcStatEntry_Object = MibTableRow
apmPcStatEntry = _ApmPcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1)
)
apmPcStatEntry.setIndexNames(
    (0, "F5-BIGIP-APM-MIB", "apmPcStatName"),
)
if mibBuilder.loadTexts:
    apmPcStatEntry.setStatus("current")
_ApmPcStatName_Type = LongDisplayString
_ApmPcStatName_Object = MibTableColumn
apmPcStatName = _ApmPcStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1, 1),
    _ApmPcStatName_Type()
)
apmPcStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatName.setStatus("current")
_ApmPcStatTotConns_Type = Counter64
_ApmPcStatTotConns_Object = MibTableColumn
apmPcStatTotConns = _ApmPcStatTotConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1, 2),
    _ApmPcStatTotConns_Type()
)
apmPcStatTotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatTotConns.setStatus("current")
_ApmPcStatCurConns_Type = Counter64
_ApmPcStatCurConns_Object = MibTableColumn
apmPcStatCurConns = _ApmPcStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1, 3),
    _ApmPcStatCurConns_Type()
)
apmPcStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatCurConns.setStatus("current")
_ApmPcStatMaxConns_Type = Counter64
_ApmPcStatMaxConns_Object = MibTableColumn
apmPcStatMaxConns = _ApmPcStatMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1, 4),
    _ApmPcStatMaxConns_Type()
)
apmPcStatMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatMaxConns.setStatus("current")
_ApmPcStatIngressRaw_Type = Counter64
_ApmPcStatIngressRaw_Object = MibTableColumn
apmPcStatIngressRaw = _ApmPcStatIngressRaw_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1, 5),
    _ApmPcStatIngressRaw_Type()
)
apmPcStatIngressRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatIngressRaw.setStatus("current")
_ApmPcStatEgressRaw_Type = Counter64
_ApmPcStatEgressRaw_Object = MibTableColumn
apmPcStatEgressRaw = _ApmPcStatEgressRaw_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1, 6),
    _ApmPcStatEgressRaw_Type()
)
apmPcStatEgressRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatEgressRaw.setStatus("current")
_ApmPcStatIngressCompressed_Type = Counter64
_ApmPcStatIngressCompressed_Object = MibTableColumn
apmPcStatIngressCompressed = _ApmPcStatIngressCompressed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1, 7),
    _ApmPcStatIngressCompressed_Type()
)
apmPcStatIngressCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatIngressCompressed.setStatus("current")
_ApmPcStatEgressCompressed_Type = Counter64
_ApmPcStatEgressCompressed_Object = MibTableColumn
apmPcStatEgressCompressed = _ApmPcStatEgressCompressed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 2, 3, 1, 8),
    _ApmPcStatEgressCompressed_Type()
)
apmPcStatEgressCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPcStatEgressCompressed.setStatus("current")
_ApmProfileRewriteStat_ObjectIdentity = ObjectIdentity
apmProfileRewriteStat = _ApmProfileRewriteStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3)
)
_ApmPrStatResetStats_Type = Integer32
_ApmPrStatResetStats_Object = MibScalar
apmPrStatResetStats = _ApmPrStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 1),
    _ApmPrStatResetStats_Type()
)
apmPrStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmPrStatResetStats.setStatus("current")
_ApmPrStatNumber_Type = Integer32
_ApmPrStatNumber_Object = MibScalar
apmPrStatNumber = _ApmPrStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 2),
    _ApmPrStatNumber_Type()
)
apmPrStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatNumber.setStatus("current")
_ApmPrStatTable_Object = MibTable
apmPrStatTable = _ApmPrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    apmPrStatTable.setStatus("current")
_ApmPrStatEntry_Object = MibTableRow
apmPrStatEntry = _ApmPrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1)
)
apmPrStatEntry.setIndexNames(
    (0, "F5-BIGIP-APM-MIB", "apmPrStatName"),
)
if mibBuilder.loadTexts:
    apmPrStatEntry.setStatus("current")
_ApmPrStatName_Type = LongDisplayString
_ApmPrStatName_Object = MibTableColumn
apmPrStatName = _ApmPrStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 1),
    _ApmPrStatName_Type()
)
apmPrStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatName.setStatus("current")
_ApmPrStatClientReqBytes_Type = Counter64
_ApmPrStatClientReqBytes_Object = MibTableColumn
apmPrStatClientReqBytes = _ApmPrStatClientReqBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 2),
    _ApmPrStatClientReqBytes_Type()
)
apmPrStatClientReqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatClientReqBytes.setStatus("current")
_ApmPrStatClientRespBytes_Type = Counter64
_ApmPrStatClientRespBytes_Object = MibTableColumn
apmPrStatClientRespBytes = _ApmPrStatClientRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 3),
    _ApmPrStatClientRespBytes_Type()
)
apmPrStatClientRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatClientRespBytes.setStatus("current")
_ApmPrStatServerReqBytes_Type = Counter64
_ApmPrStatServerReqBytes_Object = MibTableColumn
apmPrStatServerReqBytes = _ApmPrStatServerReqBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 4),
    _ApmPrStatServerReqBytes_Type()
)
apmPrStatServerReqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatServerReqBytes.setStatus("current")
_ApmPrStatServerRespBytes_Type = Counter64
_ApmPrStatServerRespBytes_Object = MibTableColumn
apmPrStatServerRespBytes = _ApmPrStatServerRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 5),
    _ApmPrStatServerRespBytes_Type()
)
apmPrStatServerRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatServerRespBytes.setStatus("current")
_ApmPrStatClientReqs_Type = Counter64
_ApmPrStatClientReqs_Object = MibTableColumn
apmPrStatClientReqs = _ApmPrStatClientReqs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 6),
    _ApmPrStatClientReqs_Type()
)
apmPrStatClientReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatClientReqs.setStatus("current")
_ApmPrStatClientResps_Type = Counter64
_ApmPrStatClientResps_Object = MibTableColumn
apmPrStatClientResps = _ApmPrStatClientResps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 7),
    _ApmPrStatClientResps_Type()
)
apmPrStatClientResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatClientResps.setStatus("current")
_ApmPrStatServerReqs_Type = Counter64
_ApmPrStatServerReqs_Object = MibTableColumn
apmPrStatServerReqs = _ApmPrStatServerReqs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 8),
    _ApmPrStatServerReqs_Type()
)
apmPrStatServerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatServerReqs.setStatus("current")
_ApmPrStatServerResps_Type = Counter64
_ApmPrStatServerResps_Object = MibTableColumn
apmPrStatServerResps = _ApmPrStatServerResps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 3, 3, 1, 9),
    _ApmPrStatServerResps_Type()
)
apmPrStatServerResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPrStatServerResps.setStatus("current")
_ApmAccessStat_ObjectIdentity = ObjectIdentity
apmAccessStat = _ApmAccessStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4)
)
_ApmAccessStatResetStats_Type = Integer32
_ApmAccessStatResetStats_Object = MibScalar
apmAccessStatResetStats = _ApmAccessStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 1),
    _ApmAccessStatResetStats_Type()
)
apmAccessStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAccessStatResetStats.setStatus("current")
_ApmAccessStatTotalSessions_Type = Integer32
_ApmAccessStatTotalSessions_Object = MibScalar
apmAccessStatTotalSessions = _ApmAccessStatTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 2),
    _ApmAccessStatTotalSessions_Type()
)
apmAccessStatTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatTotalSessions.setStatus("current")
_ApmAccessStatCurrentActiveSessions_Type = Counter64
_ApmAccessStatCurrentActiveSessions_Object = MibScalar
apmAccessStatCurrentActiveSessions = _ApmAccessStatCurrentActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 3),
    _ApmAccessStatCurrentActiveSessions_Type()
)
apmAccessStatCurrentActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatCurrentActiveSessions.setStatus("current")
_ApmAccessStatCurrentPendingSessions_Type = Counter64
_ApmAccessStatCurrentPendingSessions_Object = MibScalar
apmAccessStatCurrentPendingSessions = _ApmAccessStatCurrentPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 4),
    _ApmAccessStatCurrentPendingSessions_Type()
)
apmAccessStatCurrentPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatCurrentPendingSessions.setStatus("current")
_ApmAccessStatCurrentEndedSessions_Type = Counter64
_ApmAccessStatCurrentEndedSessions_Object = MibScalar
apmAccessStatCurrentEndedSessions = _ApmAccessStatCurrentEndedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 5),
    _ApmAccessStatCurrentEndedSessions_Type()
)
apmAccessStatCurrentEndedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatCurrentEndedSessions.setStatus("current")
_ApmAccessStatUserLoggedoutSessions_Type = Counter64
_ApmAccessStatUserLoggedoutSessions_Object = MibScalar
apmAccessStatUserLoggedoutSessions = _ApmAccessStatUserLoggedoutSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 6),
    _ApmAccessStatUserLoggedoutSessions_Type()
)
apmAccessStatUserLoggedoutSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatUserLoggedoutSessions.setStatus("current")
_ApmAccessStatAdminTerminatedSessions_Type = Counter64
_ApmAccessStatAdminTerminatedSessions_Object = MibScalar
apmAccessStatAdminTerminatedSessions = _ApmAccessStatAdminTerminatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 7),
    _ApmAccessStatAdminTerminatedSessions_Type()
)
apmAccessStatAdminTerminatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatAdminTerminatedSessions.setStatus("current")
_ApmAccessStatMiscTerminatedSessions_Type = Counter64
_ApmAccessStatMiscTerminatedSessions_Object = MibScalar
apmAccessStatMiscTerminatedSessions = _ApmAccessStatMiscTerminatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 8),
    _ApmAccessStatMiscTerminatedSessions_Type()
)
apmAccessStatMiscTerminatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatMiscTerminatedSessions.setStatus("current")
_ApmAccessStatResultAllow_Type = Counter64
_ApmAccessStatResultAllow_Object = MibScalar
apmAccessStatResultAllow = _ApmAccessStatResultAllow_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 9),
    _ApmAccessStatResultAllow_Type()
)
apmAccessStatResultAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatResultAllow.setStatus("current")
_ApmAccessStatResultDeny_Type = Counter64
_ApmAccessStatResultDeny_Object = MibScalar
apmAccessStatResultDeny = _ApmAccessStatResultDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 10),
    _ApmAccessStatResultDeny_Type()
)
apmAccessStatResultDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatResultDeny.setStatus("current")
_ApmAccessStatResultRedirect_Type = Counter64
_ApmAccessStatResultRedirect_Object = MibScalar
apmAccessStatResultRedirect = _ApmAccessStatResultRedirect_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 11),
    _ApmAccessStatResultRedirect_Type()
)
apmAccessStatResultRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatResultRedirect.setStatus("current")
_ApmAccessStatResultRedirectWithSession_Type = Counter64
_ApmAccessStatResultRedirectWithSession_Object = MibScalar
apmAccessStatResultRedirectWithSession = _ApmAccessStatResultRedirectWithSession_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 4, 12),
    _ApmAccessStatResultRedirectWithSession_Type()
)
apmAccessStatResultRedirectWithSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAccessStatResultRedirectWithSession.setStatus("current")
_ApmGlobalConnectivityStat_ObjectIdentity = ObjectIdentity
apmGlobalConnectivityStat = _ApmGlobalConnectivityStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5)
)
_ApmGlobalConnectivityStatResetStats_Type = Integer32
_ApmGlobalConnectivityStatResetStats_Object = MibScalar
apmGlobalConnectivityStatResetStats = _ApmGlobalConnectivityStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5, 1),
    _ApmGlobalConnectivityStatResetStats_Type()
)
apmGlobalConnectivityStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatResetStats.setStatus("current")
_ApmGlobalConnectivityStatTotConns_Type = Counter64
_ApmGlobalConnectivityStatTotConns_Object = MibScalar
apmGlobalConnectivityStatTotConns = _ApmGlobalConnectivityStatTotConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5, 2),
    _ApmGlobalConnectivityStatTotConns_Type()
)
apmGlobalConnectivityStatTotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatTotConns.setStatus("current")
_ApmGlobalConnectivityStatCurConns_Type = Counter64
_ApmGlobalConnectivityStatCurConns_Object = MibScalar
apmGlobalConnectivityStatCurConns = _ApmGlobalConnectivityStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5, 3),
    _ApmGlobalConnectivityStatCurConns_Type()
)
apmGlobalConnectivityStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatCurConns.setStatus("current")
_ApmGlobalConnectivityStatMaxConns_Type = Counter64
_ApmGlobalConnectivityStatMaxConns_Object = MibScalar
apmGlobalConnectivityStatMaxConns = _ApmGlobalConnectivityStatMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5, 4),
    _ApmGlobalConnectivityStatMaxConns_Type()
)
apmGlobalConnectivityStatMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatMaxConns.setStatus("current")
_ApmGlobalConnectivityStatIngressRaw_Type = Counter64
_ApmGlobalConnectivityStatIngressRaw_Object = MibScalar
apmGlobalConnectivityStatIngressRaw = _ApmGlobalConnectivityStatIngressRaw_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5, 5),
    _ApmGlobalConnectivityStatIngressRaw_Type()
)
apmGlobalConnectivityStatIngressRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatIngressRaw.setStatus("current")
_ApmGlobalConnectivityStatEgressRaw_Type = Counter64
_ApmGlobalConnectivityStatEgressRaw_Object = MibScalar
apmGlobalConnectivityStatEgressRaw = _ApmGlobalConnectivityStatEgressRaw_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5, 6),
    _ApmGlobalConnectivityStatEgressRaw_Type()
)
apmGlobalConnectivityStatEgressRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatEgressRaw.setStatus("current")
_ApmGlobalConnectivityStatIngressCompressed_Type = Counter64
_ApmGlobalConnectivityStatIngressCompressed_Object = MibScalar
apmGlobalConnectivityStatIngressCompressed = _ApmGlobalConnectivityStatIngressCompressed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5, 7),
    _ApmGlobalConnectivityStatIngressCompressed_Type()
)
apmGlobalConnectivityStatIngressCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatIngressCompressed.setStatus("current")
_ApmGlobalConnectivityStatEgressCompressed_Type = Counter64
_ApmGlobalConnectivityStatEgressCompressed_Object = MibScalar
apmGlobalConnectivityStatEgressCompressed = _ApmGlobalConnectivityStatEgressCompressed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 5, 8),
    _ApmGlobalConnectivityStatEgressCompressed_Type()
)
apmGlobalConnectivityStatEgressCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatEgressCompressed.setStatus("current")
_ApmGlobalRewriteStat_ObjectIdentity = ObjectIdentity
apmGlobalRewriteStat = _ApmGlobalRewriteStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6)
)
_ApmGlobalRewriteStatResetStats_Type = Integer32
_ApmGlobalRewriteStatResetStats_Object = MibScalar
apmGlobalRewriteStatResetStats = _ApmGlobalRewriteStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 1),
    _ApmGlobalRewriteStatResetStats_Type()
)
apmGlobalRewriteStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatResetStats.setStatus("current")
_ApmGlobalRewriteStatClientReqBytes_Type = Counter64
_ApmGlobalRewriteStatClientReqBytes_Object = MibScalar
apmGlobalRewriteStatClientReqBytes = _ApmGlobalRewriteStatClientReqBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 2),
    _ApmGlobalRewriteStatClientReqBytes_Type()
)
apmGlobalRewriteStatClientReqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatClientReqBytes.setStatus("current")
_ApmGlobalRewriteStatClientRespBytes_Type = Counter64
_ApmGlobalRewriteStatClientRespBytes_Object = MibScalar
apmGlobalRewriteStatClientRespBytes = _ApmGlobalRewriteStatClientRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 3),
    _ApmGlobalRewriteStatClientRespBytes_Type()
)
apmGlobalRewriteStatClientRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatClientRespBytes.setStatus("current")
_ApmGlobalRewriteStatServerReqBytes_Type = Counter64
_ApmGlobalRewriteStatServerReqBytes_Object = MibScalar
apmGlobalRewriteStatServerReqBytes = _ApmGlobalRewriteStatServerReqBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 4),
    _ApmGlobalRewriteStatServerReqBytes_Type()
)
apmGlobalRewriteStatServerReqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatServerReqBytes.setStatus("current")
_ApmGlobalRewriteStatServerRespBytes_Type = Counter64
_ApmGlobalRewriteStatServerRespBytes_Object = MibScalar
apmGlobalRewriteStatServerRespBytes = _ApmGlobalRewriteStatServerRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 5),
    _ApmGlobalRewriteStatServerRespBytes_Type()
)
apmGlobalRewriteStatServerRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatServerRespBytes.setStatus("current")
_ApmGlobalRewriteStatClientReqs_Type = Counter64
_ApmGlobalRewriteStatClientReqs_Object = MibScalar
apmGlobalRewriteStatClientReqs = _ApmGlobalRewriteStatClientReqs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 6),
    _ApmGlobalRewriteStatClientReqs_Type()
)
apmGlobalRewriteStatClientReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatClientReqs.setStatus("current")
_ApmGlobalRewriteStatClientResps_Type = Counter64
_ApmGlobalRewriteStatClientResps_Object = MibScalar
apmGlobalRewriteStatClientResps = _ApmGlobalRewriteStatClientResps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 7),
    _ApmGlobalRewriteStatClientResps_Type()
)
apmGlobalRewriteStatClientResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatClientResps.setStatus("current")
_ApmGlobalRewriteStatServerReqs_Type = Counter64
_ApmGlobalRewriteStatServerReqs_Object = MibScalar
apmGlobalRewriteStatServerReqs = _ApmGlobalRewriteStatServerReqs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 8),
    _ApmGlobalRewriteStatServerReqs_Type()
)
apmGlobalRewriteStatServerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatServerReqs.setStatus("current")
_ApmGlobalRewriteStatServerResps_Type = Counter64
_ApmGlobalRewriteStatServerResps_Object = MibScalar
apmGlobalRewriteStatServerResps = _ApmGlobalRewriteStatServerResps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 6, 9),
    _ApmGlobalRewriteStatServerResps_Type()
)
apmGlobalRewriteStatServerResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmGlobalRewriteStatServerResps.setStatus("current")
_ApmProfileAccessAgentStat_ObjectIdentity = ObjectIdentity
apmProfileAccessAgentStat = _ApmProfileAccessAgentStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7)
)
_ApmPgStatResetStats_Type = Integer32
_ApmPgStatResetStats_Object = MibScalar
apmPgStatResetStats = _ApmPgStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 1),
    _ApmPgStatResetStats_Type()
)
apmPgStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmPgStatResetStats.setStatus("current")
_ApmPgStatNumber_Type = Integer32
_ApmPgStatNumber_Object = MibScalar
apmPgStatNumber = _ApmPgStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 2),
    _ApmPgStatNumber_Type()
)
apmPgStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatNumber.setStatus("current")
_ApmPgStatTable_Object = MibTable
apmPgStatTable = _ApmPgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3)
)
if mibBuilder.loadTexts:
    apmPgStatTable.setStatus("current")
_ApmPgStatEntry_Object = MibTableRow
apmPgStatEntry = _ApmPgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1)
)
apmPgStatEntry.setIndexNames(
    (0, "F5-BIGIP-APM-MIB", "apmPgStatName"),
    (0, "F5-BIGIP-APM-MIB", "apmPgStatAgentName"),
)
if mibBuilder.loadTexts:
    apmPgStatEntry.setStatus("current")
_ApmPgStatName_Type = LongDisplayString
_ApmPgStatName_Object = MibTableColumn
apmPgStatName = _ApmPgStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1, 1),
    _ApmPgStatName_Type()
)
apmPgStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatName.setStatus("current")
_ApmPgStatAgentName_Type = LongDisplayString
_ApmPgStatAgentName_Object = MibTableColumn
apmPgStatAgentName = _ApmPgStatAgentName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1, 2),
    _ApmPgStatAgentName_Type()
)
apmPgStatAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatAgentName.setStatus("current")
_ApmPgStatInstances_Type = Counter64
_ApmPgStatInstances_Object = MibTableColumn
apmPgStatInstances = _ApmPgStatInstances_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1, 3),
    _ApmPgStatInstances_Type()
)
apmPgStatInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatInstances.setStatus("current")
_ApmPgStatUsages_Type = Counter64
_ApmPgStatUsages_Object = MibTableColumn
apmPgStatUsages = _ApmPgStatUsages_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1, 4),
    _ApmPgStatUsages_Type()
)
apmPgStatUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatUsages.setStatus("current")
_ApmPgStatSuccesses_Type = Counter64
_ApmPgStatSuccesses_Object = MibTableColumn
apmPgStatSuccesses = _ApmPgStatSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1, 5),
    _ApmPgStatSuccesses_Type()
)
apmPgStatSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatSuccesses.setStatus("current")
_ApmPgStatFailures_Type = Counter64
_ApmPgStatFailures_Object = MibTableColumn
apmPgStatFailures = _ApmPgStatFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1, 6),
    _ApmPgStatFailures_Type()
)
apmPgStatFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatFailures.setStatus("current")
_ApmPgStatErrors_Type = Counter64
_ApmPgStatErrors_Object = MibTableColumn
apmPgStatErrors = _ApmPgStatErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1, 7),
    _ApmPgStatErrors_Type()
)
apmPgStatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatErrors.setStatus("current")
_ApmPgStatSessionVars_Type = Counter64
_ApmPgStatSessionVars_Object = MibTableColumn
apmPgStatSessionVars = _ApmPgStatSessionVars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 7, 3, 1, 8),
    _ApmPgStatSessionVars_Type()
)
apmPgStatSessionVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPgStatSessionVars.setStatus("current")
_ApmProfileAccessMiscStat_ObjectIdentity = ObjectIdentity
apmProfileAccessMiscStat = _ApmProfileAccessMiscStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8)
)
_ApmPmStatResetStats_Type = Integer32
_ApmPmStatResetStats_Object = MibScalar
apmPmStatResetStats = _ApmPmStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 1),
    _ApmPmStatResetStats_Type()
)
apmPmStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmPmStatResetStats.setStatus("current")
_ApmPmStatNumber_Type = Integer32
_ApmPmStatNumber_Object = MibScalar
apmPmStatNumber = _ApmPmStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 2),
    _ApmPmStatNumber_Type()
)
apmPmStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatNumber.setStatus("current")
_ApmPmStatTable_Object = MibTable
apmPmStatTable = _ApmPmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3)
)
if mibBuilder.loadTexts:
    apmPmStatTable.setStatus("current")
_ApmPmStatEntry_Object = MibTableRow
apmPmStatEntry = _ApmPmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1)
)
apmPmStatEntry.setIndexNames(
    (0, "F5-BIGIP-APM-MIB", "apmPmStatName"),
)
if mibBuilder.loadTexts:
    apmPmStatEntry.setStatus("current")
_ApmPmStatName_Type = LongDisplayString
_ApmPmStatName_Object = MibTableColumn
apmPmStatName = _ApmPmStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 1),
    _ApmPmStatName_Type()
)
apmPmStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatName.setStatus("current")
_ApmPmStatConfigSyncState_Type = Counter64
_ApmPmStatConfigSyncState_Object = MibTableColumn
apmPmStatConfigSyncState = _ApmPmStatConfigSyncState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 2),
    _ApmPmStatConfigSyncState_Type()
)
apmPmStatConfigSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatConfigSyncState.setStatus("current")
_ApmPmStatInspResultError_Type = Counter64
_ApmPmStatInspResultError_Object = MibTableColumn
apmPmStatInspResultError = _ApmPmStatInspResultError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 3),
    _ApmPmStatInspResultError_Type()
)
apmPmStatInspResultError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatInspResultError.setStatus("current")
_ApmPmStatInspSessionError_Type = Counter64
_ApmPmStatInspSessionError_Object = MibTableColumn
apmPmStatInspSessionError = _ApmPmStatInspSessionError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 4),
    _ApmPmStatInspSessionError_Type()
)
apmPmStatInspSessionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatInspSessionError.setStatus("current")
_ApmPmStatInspDeviceInfoError_Type = Counter64
_ApmPmStatInspDeviceInfoError_Object = MibTableColumn
apmPmStatInspDeviceInfoError = _ApmPmStatInspDeviceInfoError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 5),
    _ApmPmStatInspDeviceInfoError_Type()
)
apmPmStatInspDeviceInfoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatInspDeviceInfoError.setStatus("current")
_ApmPmStatInspTokenError_Type = Counter64
_ApmPmStatInspTokenError_Object = MibTableColumn
apmPmStatInspTokenError = _ApmPmStatInspTokenError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 6),
    _ApmPmStatInspTokenError_Type()
)
apmPmStatInspTokenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatInspTokenError.setStatus("current")
_ApmPmStatInspSignatureError_Type = Counter64
_ApmPmStatInspSignatureError_Object = MibTableColumn
apmPmStatInspSignatureError = _ApmPmStatInspSignatureError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 7),
    _ApmPmStatInspSignatureError_Type()
)
apmPmStatInspSignatureError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatInspSignatureError.setStatus("current")
_ApmPmStatInspDataMsmtchError_Type = Counter64
_ApmPmStatInspDataMsmtchError_Object = MibTableColumn
apmPmStatInspDataMsmtchError = _ApmPmStatInspDataMsmtchError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 8),
    _ApmPmStatInspDataMsmtchError_Type()
)
apmPmStatInspDataMsmtchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatInspDataMsmtchError.setStatus("current")
_ApmPmStatInspClientSignError_Type = Counter64
_ApmPmStatInspClientSignError_Object = MibTableColumn
apmPmStatInspClientSignError = _ApmPmStatInspClientSignError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 9),
    _ApmPmStatInspClientSignError_Type()
)
apmPmStatInspClientSignError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatInspClientSignError.setStatus("current")
_ApmPmStatMemInitError_Type = Counter64
_ApmPmStatMemInitError_Object = MibTableColumn
apmPmStatMemInitError = _ApmPmStatMemInitError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 10),
    _ApmPmStatMemInitError_Type()
)
apmPmStatMemInitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatMemInitError.setStatus("current")
_ApmPmStatMemSessionVarError_Type = Counter64
_ApmPmStatMemSessionVarError_Object = MibTableColumn
apmPmStatMemSessionVarError = _ApmPmStatMemSessionVarError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 11),
    _ApmPmStatMemSessionVarError_Type()
)
apmPmStatMemSessionVarError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatMemSessionVarError.setStatus("current")
_ApmPmStatMemCloseError_Type = Counter64
_ApmPmStatMemCloseError_Object = MibTableColumn
apmPmStatMemCloseError = _ApmPmStatMemCloseError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 12),
    _ApmPmStatMemCloseError_Type()
)
apmPmStatMemCloseError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatMemCloseError.setStatus("current")
_ApmPmStatResultError_Type = Counter64
_ApmPmStatResultError_Object = MibTableColumn
apmPmStatResultError = _ApmPmStatResultError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 13),
    _ApmPmStatResultError_Type()
)
apmPmStatResultError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatResultError.setStatus("current")
_ApmPmStatInternalError_Type = Counter64
_ApmPmStatInternalError_Object = MibTableColumn
apmPmStatInternalError = _ApmPmStatInternalError_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 1, 8, 3, 1, 14),
    _ApmPmStatInternalError_Type()
)
apmPmStatInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmPmStatInternalError.setStatus("current")
_ApmLeasepool_ObjectIdentity = ObjectIdentity
apmLeasepool = _ApmLeasepool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2)
)
_ApmLeasepoolStat_ObjectIdentity = ObjectIdentity
apmLeasepoolStat = _ApmLeasepoolStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1)
)
_ApmLeasepoolStatResetStats_Type = Integer32
_ApmLeasepoolStatResetStats_Object = MibScalar
apmLeasepoolStatResetStats = _ApmLeasepoolStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 1),
    _ApmLeasepoolStatResetStats_Type()
)
apmLeasepoolStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmLeasepoolStatResetStats.setStatus("current")
_ApmLeasepoolStatNumber_Type = Integer32
_ApmLeasepoolStatNumber_Object = MibScalar
apmLeasepoolStatNumber = _ApmLeasepoolStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 2),
    _ApmLeasepoolStatNumber_Type()
)
apmLeasepoolStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatNumber.setStatus("current")
_ApmLeasepoolStatTable_Object = MibTable
apmLeasepoolStatTable = _ApmLeasepoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    apmLeasepoolStatTable.setStatus("current")
_ApmLeasepoolStatEntry_Object = MibTableRow
apmLeasepoolStatEntry = _ApmLeasepoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1)
)
apmLeasepoolStatEntry.setIndexNames(
    (0, "F5-BIGIP-APM-MIB", "apmLeasepoolStatName"),
)
if mibBuilder.loadTexts:
    apmLeasepoolStatEntry.setStatus("current")
_ApmLeasepoolStatName_Type = LongDisplayString
_ApmLeasepoolStatName_Object = MibTableColumn
apmLeasepoolStatName = _ApmLeasepoolStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 1),
    _ApmLeasepoolStatName_Type()
)
apmLeasepoolStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatName.setStatus("current")
_ApmLeasepoolStatCurMembers_Type = Integer32
_ApmLeasepoolStatCurMembers_Object = MibTableColumn
apmLeasepoolStatCurMembers = _ApmLeasepoolStatCurMembers_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 2),
    _ApmLeasepoolStatCurMembers_Type()
)
apmLeasepoolStatCurMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatCurMembers.setStatus("current")
_ApmLeasepoolStatCurAssigned_Type = Integer32
_ApmLeasepoolStatCurAssigned_Object = MibTableColumn
apmLeasepoolStatCurAssigned = _ApmLeasepoolStatCurAssigned_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 3),
    _ApmLeasepoolStatCurAssigned_Type()
)
apmLeasepoolStatCurAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatCurAssigned.setStatus("current")
_ApmLeasepoolStatCurFree_Type = Integer32
_ApmLeasepoolStatCurFree_Object = MibTableColumn
apmLeasepoolStatCurFree = _ApmLeasepoolStatCurFree_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 4),
    _ApmLeasepoolStatCurFree_Type()
)
apmLeasepoolStatCurFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatCurFree.setStatus("current")
_ApmLeasepoolStatMaxAssigned_Type = Integer32
_ApmLeasepoolStatMaxAssigned_Object = MibTableColumn
apmLeasepoolStatMaxAssigned = _ApmLeasepoolStatMaxAssigned_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 5),
    _ApmLeasepoolStatMaxAssigned_Type()
)
apmLeasepoolStatMaxAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatMaxAssigned.setStatus("current")
_ApmLeasepoolStatTotPickRequests_Type = Counter64
_ApmLeasepoolStatTotPickRequests_Object = MibTableColumn
apmLeasepoolStatTotPickRequests = _ApmLeasepoolStatTotPickRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 6),
    _ApmLeasepoolStatTotPickRequests_Type()
)
apmLeasepoolStatTotPickRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatTotPickRequests.setStatus("current")
_ApmLeasepoolStatTotPickFailure_Type = Counter64
_ApmLeasepoolStatTotPickFailure_Object = MibTableColumn
apmLeasepoolStatTotPickFailure = _ApmLeasepoolStatTotPickFailure_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 7),
    _ApmLeasepoolStatTotPickFailure_Type()
)
apmLeasepoolStatTotPickFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatTotPickFailure.setStatus("current")
_ApmLeasepoolStatTotReserveRequests_Type = Counter64
_ApmLeasepoolStatTotReserveRequests_Object = MibTableColumn
apmLeasepoolStatTotReserveRequests = _ApmLeasepoolStatTotReserveRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 8),
    _ApmLeasepoolStatTotReserveRequests_Type()
)
apmLeasepoolStatTotReserveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatTotReserveRequests.setStatus("current")
_ApmLeasepoolStatTotReserveFailure_Type = Counter64
_ApmLeasepoolStatTotReserveFailure_Object = MibTableColumn
apmLeasepoolStatTotReserveFailure = _ApmLeasepoolStatTotReserveFailure_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 9),
    _ApmLeasepoolStatTotReserveFailure_Type()
)
apmLeasepoolStatTotReserveFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatTotReserveFailure.setStatus("current")
_ApmLeasepoolStatTotReleaseRequests_Type = Counter64
_ApmLeasepoolStatTotReleaseRequests_Object = MibTableColumn
apmLeasepoolStatTotReleaseRequests = _ApmLeasepoolStatTotReleaseRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 10),
    _ApmLeasepoolStatTotReleaseRequests_Type()
)
apmLeasepoolStatTotReleaseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatTotReleaseRequests.setStatus("current")
_ApmLeasepoolStatTotReleaseFailure_Type = Counter64
_ApmLeasepoolStatTotReleaseFailure_Object = MibTableColumn
apmLeasepoolStatTotReleaseFailure = _ApmLeasepoolStatTotReleaseFailure_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 2, 1, 3, 1, 11),
    _ApmLeasepoolStatTotReleaseFailure_Type()
)
apmLeasepoolStatTotReleaseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmLeasepoolStatTotReleaseFailure.setStatus("current")
_ApmAcl_ObjectIdentity = ObjectIdentity
apmAcl = _ApmAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3)
)
_ApmAclStat_ObjectIdentity = ObjectIdentity
apmAclStat = _ApmAclStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1)
)
_ApmAclStatResetStats_Type = Integer32
_ApmAclStatResetStats_Object = MibScalar
apmAclStatResetStats = _ApmAclStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 1),
    _ApmAclStatResetStats_Type()
)
apmAclStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAclStatResetStats.setStatus("current")
_ApmAclStatNumber_Type = Integer32
_ApmAclStatNumber_Object = MibScalar
apmAclStatNumber = _ApmAclStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 2),
    _ApmAclStatNumber_Type()
)
apmAclStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAclStatNumber.setStatus("current")
_ApmAclStatTable_Object = MibTable
apmAclStatTable = _ApmAclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 3)
)
if mibBuilder.loadTexts:
    apmAclStatTable.setStatus("current")
_ApmAclStatEntry_Object = MibTableRow
apmAclStatEntry = _ApmAclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 3, 1)
)
apmAclStatEntry.setIndexNames(
    (0, "F5-BIGIP-APM-MIB", "apmAclStatName"),
)
if mibBuilder.loadTexts:
    apmAclStatEntry.setStatus("current")
_ApmAclStatName_Type = LongDisplayString
_ApmAclStatName_Object = MibTableColumn
apmAclStatName = _ApmAclStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 3, 1, 1),
    _ApmAclStatName_Type()
)
apmAclStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAclStatName.setStatus("current")
_ApmAclStatActionAllow_Type = Counter64
_ApmAclStatActionAllow_Object = MibTableColumn
apmAclStatActionAllow = _ApmAclStatActionAllow_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 3, 1, 2),
    _ApmAclStatActionAllow_Type()
)
apmAclStatActionAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAclStatActionAllow.setStatus("current")
_ApmAclStatActionContinue_Type = Counter64
_ApmAclStatActionContinue_Object = MibTableColumn
apmAclStatActionContinue = _ApmAclStatActionContinue_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 3, 1, 3),
    _ApmAclStatActionContinue_Type()
)
apmAclStatActionContinue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAclStatActionContinue.setStatus("current")
_ApmAclStatActionDiscard_Type = Counter64
_ApmAclStatActionDiscard_Object = MibTableColumn
apmAclStatActionDiscard = _ApmAclStatActionDiscard_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 3, 1, 4),
    _ApmAclStatActionDiscard_Type()
)
apmAclStatActionDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAclStatActionDiscard.setStatus("current")
_ApmAclStatActionReject_Type = Counter64
_ApmAclStatActionReject_Object = MibTableColumn
apmAclStatActionReject = _ApmAclStatActionReject_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 6, 3, 1, 3, 1, 5),
    _ApmAclStatActionReject_Type()
)
apmAclStatActionReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmAclStatActionReject.setStatus("current")

# Managed Objects groups

apmPaStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 1)
)
apmPaStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmPaStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmPaStatNumber"),
        ("F5-BIGIP-APM-MIB", "apmPaStatName"),
        ("F5-BIGIP-APM-MIB", "apmPaStatConfigSyncState"),
        ("F5-BIGIP-APM-MIB", "apmPaStatTotalSessions"),
        ("F5-BIGIP-APM-MIB", "apmPaStatTotalEstablishedStateSessions"),
        ("F5-BIGIP-APM-MIB", "apmPaStatCurrentActiveSessions"),
        ("F5-BIGIP-APM-MIB", "apmPaStatCurrentPendingSessions"),
        ("F5-BIGIP-APM-MIB", "apmPaStatCurrentCompletedSessions"),
        ("F5-BIGIP-APM-MIB", "apmPaStatUserLoggedoutSessions"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAdminTerminatedSessions"),
        ("F5-BIGIP-APM-MIB", "apmPaStatMiscTerminatedSessions"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAccessPolicyResultAllow"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAccessPolicyResultDeny"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAccessPolicyResultRedirect"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAccessPolicyResultRedirectWithSession"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingDenyAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingDenyAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingDenyAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingDenyAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingDenyAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingDenyAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingRedirectAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingRedirectAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingRedirectAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingRedirectAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingRedirectAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingRedirectAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingAllowAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingAllowAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingAllowAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingAllowAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingAllowAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEndingAllowAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAdAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAdAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAdAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAdAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAdAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAdAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatClientCertAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatClientCertAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatClientCertAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatClientCertAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatClientCertAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatClientCertAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatHttpAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatHttpAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatHttpAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatHttpAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatHttpAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatHttpAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLdapAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLdapAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLdapAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLdapAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLdapAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLdapAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatSecuridAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatSecuridAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatSecuridAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatSecuridAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatSecuridAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatSecuridAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAcctAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAcctAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAcctAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAcctAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAcctAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRadiusAcctAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxFcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxFcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxFcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxFcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxFcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxFcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxPcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxPcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxPcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxPcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxPcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsLinuxPcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacFcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacFcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacFcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacFcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacFcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacFcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacPcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacPcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacPcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacPcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacPcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsMacPcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinCcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinCcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinCcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinCcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinCcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinCcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsAvAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsAvAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsAvAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsAvAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsAvAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsAvAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinOsInfoAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinOsInfoAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinOsInfoAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinOsInfoAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinOsInfoAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinOsInfoAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinFcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinFcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinFcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinFcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinFcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinFcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinMcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinMcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinMcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinMcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinMcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinMcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsFwcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsFwcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsFwcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsFwcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsFwcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsFwcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPcTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPcTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPcTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPcTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPcTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPcTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPwTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPwTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPwTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPwTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPwTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinPwTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinRcAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinRcAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinRcAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinRcAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinRcAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinRcAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinGpAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinGpAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinGpAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinGpAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinGpAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatEpsWinGpAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatExternalLogonAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatExternalLogonAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatExternalLogonAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatExternalLogonAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatExternalLogonAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatExternalLogonAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLogonAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLogonAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLogonAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLogonAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLogonAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLogonAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRaAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRaAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRaAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRaAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRaAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRaAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRdsAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRdsAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRdsAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRdsAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRdsAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatRdsAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatVaAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatVaAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatVaAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatVaAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatVaAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatVaAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatIeAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatIeAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatIeAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatIeAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatIeAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatIeAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLoggingAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLoggingAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLoggingAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLoggingAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLoggingAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatLoggingAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatDecnBoxAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatDecnBoxAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatDecnBoxAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatDecnBoxAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatDecnBoxAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatDecnBoxAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatMesgBoxAgentTotalInstances"),
        ("F5-BIGIP-APM-MIB", "apmPaStatMesgBoxAgentTotalUsages"),
        ("F5-BIGIP-APM-MIB", "apmPaStatMesgBoxAgentTotalSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPaStatMesgBoxAgentTotalFailures"),
        ("F5-BIGIP-APM-MIB", "apmPaStatMesgBoxAgentTotalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatMesgBoxAgentTotalSessVars"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdNoResultErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdNoSessionErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdNoDeviceInfoErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdNoTokenErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdNoSigErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdTotalMismatchErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdInvalidSigErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdMcPipelineInitErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdMcSetSessVarErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdMcPipelineCloseErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdApResultErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatApdApInternalErrors"),
        ("F5-BIGIP-APM-MIB", "apmPaStatAllowedRequests"),
        ("F5-BIGIP-APM-MIB", "apmPaStatDeniedRequests"),
        ("F5-BIGIP-APM-MIB", "apmPaStatVsName"))
)
if mibBuilder.loadTexts:
    apmPaStatGroup.setStatus("current")

apmPcStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 2)
)
apmPcStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmPcStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmPcStatNumber"),
        ("F5-BIGIP-APM-MIB", "apmPcStatName"),
        ("F5-BIGIP-APM-MIB", "apmPcStatTotConns"),
        ("F5-BIGIP-APM-MIB", "apmPcStatCurConns"),
        ("F5-BIGIP-APM-MIB", "apmPcStatMaxConns"),
        ("F5-BIGIP-APM-MIB", "apmPcStatIngressRaw"),
        ("F5-BIGIP-APM-MIB", "apmPcStatEgressRaw"),
        ("F5-BIGIP-APM-MIB", "apmPcStatIngressCompressed"),
        ("F5-BIGIP-APM-MIB", "apmPcStatEgressCompressed"))
)
if mibBuilder.loadTexts:
    apmPcStatGroup.setStatus("current")

apmPrStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 3)
)
apmPrStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmPrStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmPrStatNumber"),
        ("F5-BIGIP-APM-MIB", "apmPrStatName"),
        ("F5-BIGIP-APM-MIB", "apmPrStatClientReqBytes"),
        ("F5-BIGIP-APM-MIB", "apmPrStatClientRespBytes"),
        ("F5-BIGIP-APM-MIB", "apmPrStatServerReqBytes"),
        ("F5-BIGIP-APM-MIB", "apmPrStatServerRespBytes"),
        ("F5-BIGIP-APM-MIB", "apmPrStatClientReqs"),
        ("F5-BIGIP-APM-MIB", "apmPrStatClientResps"),
        ("F5-BIGIP-APM-MIB", "apmPrStatServerReqs"),
        ("F5-BIGIP-APM-MIB", "apmPrStatServerResps"))
)
if mibBuilder.loadTexts:
    apmPrStatGroup.setStatus("current")

apmPgStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 4)
)
apmPgStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmPgStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmPgStatNumber"),
        ("F5-BIGIP-APM-MIB", "apmPgStatName"),
        ("F5-BIGIP-APM-MIB", "apmPgStatAgentName"),
        ("F5-BIGIP-APM-MIB", "apmPgStatInstances"),
        ("F5-BIGIP-APM-MIB", "apmPgStatUsages"),
        ("F5-BIGIP-APM-MIB", "apmPgStatSuccesses"),
        ("F5-BIGIP-APM-MIB", "apmPgStatFailures"),
        ("F5-BIGIP-APM-MIB", "apmPgStatErrors"),
        ("F5-BIGIP-APM-MIB", "apmPgStatSessionVars"))
)
if mibBuilder.loadTexts:
    apmPgStatGroup.setStatus("current")

apmPmStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 5)
)
apmPmStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmPmStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmPmStatNumber"),
        ("F5-BIGIP-APM-MIB", "apmPmStatName"),
        ("F5-BIGIP-APM-MIB", "apmPmStatConfigSyncState"),
        ("F5-BIGIP-APM-MIB", "apmPmStatInspResultError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatInspSessionError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatInspDeviceInfoError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatInspTokenError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatInspSignatureError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatInspDataMsmtchError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatInspClientSignError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatMemInitError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatMemSessionVarError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatMemCloseError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatResultError"),
        ("F5-BIGIP-APM-MIB", "apmPmStatInternalError"))
)
if mibBuilder.loadTexts:
    apmPmStatGroup.setStatus("current")

apmAccessStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 6)
)
apmAccessStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmAccessStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatTotalSessions"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatCurrentActiveSessions"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatCurrentPendingSessions"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatCurrentEndedSessions"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatUserLoggedoutSessions"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatAdminTerminatedSessions"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatMiscTerminatedSessions"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatResultAllow"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatResultDeny"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatResultRedirect"),
        ("F5-BIGIP-APM-MIB", "apmAccessStatResultRedirectWithSession"))
)
if mibBuilder.loadTexts:
    apmAccessStatGroup.setStatus("current")

apmGlobalConnectivityStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 7)
)
apmGlobalConnectivityStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmGlobalConnectivityStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmGlobalConnectivityStatTotConns"),
        ("F5-BIGIP-APM-MIB", "apmGlobalConnectivityStatCurConns"),
        ("F5-BIGIP-APM-MIB", "apmGlobalConnectivityStatMaxConns"),
        ("F5-BIGIP-APM-MIB", "apmGlobalConnectivityStatIngressRaw"),
        ("F5-BIGIP-APM-MIB", "apmGlobalConnectivityStatEgressRaw"),
        ("F5-BIGIP-APM-MIB", "apmGlobalConnectivityStatIngressCompressed"),
        ("F5-BIGIP-APM-MIB", "apmGlobalConnectivityStatEgressCompressed"))
)
if mibBuilder.loadTexts:
    apmGlobalConnectivityStatGroup.setStatus("current")

apmGlobalRewriteStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 8)
)
apmGlobalRewriteStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatClientReqBytes"),
        ("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatClientRespBytes"),
        ("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatServerReqBytes"),
        ("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatServerRespBytes"),
        ("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatClientReqs"),
        ("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatClientResps"),
        ("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatServerReqs"),
        ("F5-BIGIP-APM-MIB", "apmGlobalRewriteStatServerResps"))
)
if mibBuilder.loadTexts:
    apmGlobalRewriteStatGroup.setStatus("current")

apmLeasepoolStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 9)
)
apmLeasepoolStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmLeasepoolStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatNumber"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatName"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatCurMembers"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatCurAssigned"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatCurFree"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatMaxAssigned"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatTotPickRequests"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatTotPickFailure"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatTotReserveRequests"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatTotReserveFailure"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatTotReleaseRequests"),
        ("F5-BIGIP-APM-MIB", "apmLeasepoolStatTotReleaseFailure"))
)
if mibBuilder.loadTexts:
    apmLeasepoolStatGroup.setStatus("current")

apmAclStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 6, 10)
)
apmAclStatGroup.setObjects(
      *(("F5-BIGIP-APM-MIB", "apmAclStatResetStats"),
        ("F5-BIGIP-APM-MIB", "apmAclStatNumber"),
        ("F5-BIGIP-APM-MIB", "apmAclStatName"),
        ("F5-BIGIP-APM-MIB", "apmAclStatActionAllow"),
        ("F5-BIGIP-APM-MIB", "apmAclStatActionContinue"),
        ("F5-BIGIP-APM-MIB", "apmAclStatActionDiscard"),
        ("F5-BIGIP-APM-MIB", "apmAclStatActionReject"))
)
if mibBuilder.loadTexts:
    apmAclStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bigipApmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 1, 6)
)
if mibBuilder.loadTexts:
    bigipApmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-BIGIP-APM-MIB",
    **{"bigipApmCompliance": bigipApmCompliance,
       "bigipApmGroups": bigipApmGroups,
       "apmPaStatGroup": apmPaStatGroup,
       "apmPcStatGroup": apmPcStatGroup,
       "apmPrStatGroup": apmPrStatGroup,
       "apmPgStatGroup": apmPgStatGroup,
       "apmPmStatGroup": apmPmStatGroup,
       "apmAccessStatGroup": apmAccessStatGroup,
       "apmGlobalConnectivityStatGroup": apmGlobalConnectivityStatGroup,
       "apmGlobalRewriteStatGroup": apmGlobalRewriteStatGroup,
       "apmLeasepoolStatGroup": apmLeasepoolStatGroup,
       "apmAclStatGroup": apmAclStatGroup,
       "bigipApm": bigipApm,
       "apmProfiles": apmProfiles,
       "apmProfileAccessStat": apmProfileAccessStat,
       "apmPaStatResetStats": apmPaStatResetStats,
       "apmPaStatNumber": apmPaStatNumber,
       "apmPaStatTable": apmPaStatTable,
       "apmPaStatEntry": apmPaStatEntry,
       "apmPaStatName": apmPaStatName,
       "apmPaStatConfigSyncState": apmPaStatConfigSyncState,
       "apmPaStatTotalSessions": apmPaStatTotalSessions,
       "apmPaStatTotalEstablishedStateSessions": apmPaStatTotalEstablishedStateSessions,
       "apmPaStatCurrentActiveSessions": apmPaStatCurrentActiveSessions,
       "apmPaStatCurrentPendingSessions": apmPaStatCurrentPendingSessions,
       "apmPaStatCurrentCompletedSessions": apmPaStatCurrentCompletedSessions,
       "apmPaStatUserLoggedoutSessions": apmPaStatUserLoggedoutSessions,
       "apmPaStatAdminTerminatedSessions": apmPaStatAdminTerminatedSessions,
       "apmPaStatMiscTerminatedSessions": apmPaStatMiscTerminatedSessions,
       "apmPaStatAccessPolicyResultAllow": apmPaStatAccessPolicyResultAllow,
       "apmPaStatAccessPolicyResultDeny": apmPaStatAccessPolicyResultDeny,
       "apmPaStatAccessPolicyResultRedirect": apmPaStatAccessPolicyResultRedirect,
       "apmPaStatAccessPolicyResultRedirectWithSession": apmPaStatAccessPolicyResultRedirectWithSession,
       "apmPaStatEndingDenyAgentTotalInstances": apmPaStatEndingDenyAgentTotalInstances,
       "apmPaStatEndingDenyAgentTotalUsages": apmPaStatEndingDenyAgentTotalUsages,
       "apmPaStatEndingDenyAgentTotalSuccesses": apmPaStatEndingDenyAgentTotalSuccesses,
       "apmPaStatEndingDenyAgentTotalFailures": apmPaStatEndingDenyAgentTotalFailures,
       "apmPaStatEndingDenyAgentTotalErrors": apmPaStatEndingDenyAgentTotalErrors,
       "apmPaStatEndingDenyAgentTotalSessVars": apmPaStatEndingDenyAgentTotalSessVars,
       "apmPaStatEndingRedirectAgentTotalInstances": apmPaStatEndingRedirectAgentTotalInstances,
       "apmPaStatEndingRedirectAgentTotalUsages": apmPaStatEndingRedirectAgentTotalUsages,
       "apmPaStatEndingRedirectAgentTotalSuccesses": apmPaStatEndingRedirectAgentTotalSuccesses,
       "apmPaStatEndingRedirectAgentTotalFailures": apmPaStatEndingRedirectAgentTotalFailures,
       "apmPaStatEndingRedirectAgentTotalErrors": apmPaStatEndingRedirectAgentTotalErrors,
       "apmPaStatEndingRedirectAgentTotalSessVars": apmPaStatEndingRedirectAgentTotalSessVars,
       "apmPaStatEndingAllowAgentTotalInstances": apmPaStatEndingAllowAgentTotalInstances,
       "apmPaStatEndingAllowAgentTotalUsages": apmPaStatEndingAllowAgentTotalUsages,
       "apmPaStatEndingAllowAgentTotalSuccesses": apmPaStatEndingAllowAgentTotalSuccesses,
       "apmPaStatEndingAllowAgentTotalFailures": apmPaStatEndingAllowAgentTotalFailures,
       "apmPaStatEndingAllowAgentTotalErrors": apmPaStatEndingAllowAgentTotalErrors,
       "apmPaStatEndingAllowAgentTotalSessVars": apmPaStatEndingAllowAgentTotalSessVars,
       "apmPaStatAdAgentTotalInstances": apmPaStatAdAgentTotalInstances,
       "apmPaStatAdAgentTotalUsages": apmPaStatAdAgentTotalUsages,
       "apmPaStatAdAgentTotalSuccesses": apmPaStatAdAgentTotalSuccesses,
       "apmPaStatAdAgentTotalFailures": apmPaStatAdAgentTotalFailures,
       "apmPaStatAdAgentTotalErrors": apmPaStatAdAgentTotalErrors,
       "apmPaStatAdAgentTotalSessVars": apmPaStatAdAgentTotalSessVars,
       "apmPaStatClientCertAgentTotalInstances": apmPaStatClientCertAgentTotalInstances,
       "apmPaStatClientCertAgentTotalUsages": apmPaStatClientCertAgentTotalUsages,
       "apmPaStatClientCertAgentTotalSuccesses": apmPaStatClientCertAgentTotalSuccesses,
       "apmPaStatClientCertAgentTotalFailures": apmPaStatClientCertAgentTotalFailures,
       "apmPaStatClientCertAgentTotalErrors": apmPaStatClientCertAgentTotalErrors,
       "apmPaStatClientCertAgentTotalSessVars": apmPaStatClientCertAgentTotalSessVars,
       "apmPaStatHttpAgentTotalInstances": apmPaStatHttpAgentTotalInstances,
       "apmPaStatHttpAgentTotalUsages": apmPaStatHttpAgentTotalUsages,
       "apmPaStatHttpAgentTotalSuccesses": apmPaStatHttpAgentTotalSuccesses,
       "apmPaStatHttpAgentTotalFailures": apmPaStatHttpAgentTotalFailures,
       "apmPaStatHttpAgentTotalErrors": apmPaStatHttpAgentTotalErrors,
       "apmPaStatHttpAgentTotalSessVars": apmPaStatHttpAgentTotalSessVars,
       "apmPaStatLdapAgentTotalInstances": apmPaStatLdapAgentTotalInstances,
       "apmPaStatLdapAgentTotalUsages": apmPaStatLdapAgentTotalUsages,
       "apmPaStatLdapAgentTotalSuccesses": apmPaStatLdapAgentTotalSuccesses,
       "apmPaStatLdapAgentTotalFailures": apmPaStatLdapAgentTotalFailures,
       "apmPaStatLdapAgentTotalErrors": apmPaStatLdapAgentTotalErrors,
       "apmPaStatLdapAgentTotalSessVars": apmPaStatLdapAgentTotalSessVars,
       "apmPaStatRadiusAgentTotalInstances": apmPaStatRadiusAgentTotalInstances,
       "apmPaStatRadiusAgentTotalUsages": apmPaStatRadiusAgentTotalUsages,
       "apmPaStatRadiusAgentTotalSuccesses": apmPaStatRadiusAgentTotalSuccesses,
       "apmPaStatRadiusAgentTotalFailures": apmPaStatRadiusAgentTotalFailures,
       "apmPaStatRadiusAgentTotalErrors": apmPaStatRadiusAgentTotalErrors,
       "apmPaStatRadiusAgentTotalSessVars": apmPaStatRadiusAgentTotalSessVars,
       "apmPaStatSecuridAgentTotalInstances": apmPaStatSecuridAgentTotalInstances,
       "apmPaStatSecuridAgentTotalUsages": apmPaStatSecuridAgentTotalUsages,
       "apmPaStatSecuridAgentTotalSuccesses": apmPaStatSecuridAgentTotalSuccesses,
       "apmPaStatSecuridAgentTotalFailures": apmPaStatSecuridAgentTotalFailures,
       "apmPaStatSecuridAgentTotalErrors": apmPaStatSecuridAgentTotalErrors,
       "apmPaStatSecuridAgentTotalSessVars": apmPaStatSecuridAgentTotalSessVars,
       "apmPaStatRadiusAcctAgentTotalInstances": apmPaStatRadiusAcctAgentTotalInstances,
       "apmPaStatRadiusAcctAgentTotalUsages": apmPaStatRadiusAcctAgentTotalUsages,
       "apmPaStatRadiusAcctAgentTotalSuccesses": apmPaStatRadiusAcctAgentTotalSuccesses,
       "apmPaStatRadiusAcctAgentTotalFailures": apmPaStatRadiusAcctAgentTotalFailures,
       "apmPaStatRadiusAcctAgentTotalErrors": apmPaStatRadiusAcctAgentTotalErrors,
       "apmPaStatRadiusAcctAgentTotalSessVars": apmPaStatRadiusAcctAgentTotalSessVars,
       "apmPaStatEpsLinuxFcAgentTotalInstances": apmPaStatEpsLinuxFcAgentTotalInstances,
       "apmPaStatEpsLinuxFcAgentTotalUsages": apmPaStatEpsLinuxFcAgentTotalUsages,
       "apmPaStatEpsLinuxFcAgentTotalSuccesses": apmPaStatEpsLinuxFcAgentTotalSuccesses,
       "apmPaStatEpsLinuxFcAgentTotalFailures": apmPaStatEpsLinuxFcAgentTotalFailures,
       "apmPaStatEpsLinuxFcAgentTotalErrors": apmPaStatEpsLinuxFcAgentTotalErrors,
       "apmPaStatEpsLinuxFcAgentTotalSessVars": apmPaStatEpsLinuxFcAgentTotalSessVars,
       "apmPaStatEpsLinuxPcAgentTotalInstances": apmPaStatEpsLinuxPcAgentTotalInstances,
       "apmPaStatEpsLinuxPcAgentTotalUsages": apmPaStatEpsLinuxPcAgentTotalUsages,
       "apmPaStatEpsLinuxPcAgentTotalSuccesses": apmPaStatEpsLinuxPcAgentTotalSuccesses,
       "apmPaStatEpsLinuxPcAgentTotalFailures": apmPaStatEpsLinuxPcAgentTotalFailures,
       "apmPaStatEpsLinuxPcAgentTotalErrors": apmPaStatEpsLinuxPcAgentTotalErrors,
       "apmPaStatEpsLinuxPcAgentTotalSessVars": apmPaStatEpsLinuxPcAgentTotalSessVars,
       "apmPaStatEpsMacFcAgentTotalInstances": apmPaStatEpsMacFcAgentTotalInstances,
       "apmPaStatEpsMacFcAgentTotalUsages": apmPaStatEpsMacFcAgentTotalUsages,
       "apmPaStatEpsMacFcAgentTotalSuccesses": apmPaStatEpsMacFcAgentTotalSuccesses,
       "apmPaStatEpsMacFcAgentTotalFailures": apmPaStatEpsMacFcAgentTotalFailures,
       "apmPaStatEpsMacFcAgentTotalErrors": apmPaStatEpsMacFcAgentTotalErrors,
       "apmPaStatEpsMacFcAgentTotalSessVars": apmPaStatEpsMacFcAgentTotalSessVars,
       "apmPaStatEpsMacPcAgentTotalInstances": apmPaStatEpsMacPcAgentTotalInstances,
       "apmPaStatEpsMacPcAgentTotalUsages": apmPaStatEpsMacPcAgentTotalUsages,
       "apmPaStatEpsMacPcAgentTotalSuccesses": apmPaStatEpsMacPcAgentTotalSuccesses,
       "apmPaStatEpsMacPcAgentTotalFailures": apmPaStatEpsMacPcAgentTotalFailures,
       "apmPaStatEpsMacPcAgentTotalErrors": apmPaStatEpsMacPcAgentTotalErrors,
       "apmPaStatEpsMacPcAgentTotalSessVars": apmPaStatEpsMacPcAgentTotalSessVars,
       "apmPaStatEpsWinCcAgentTotalInstances": apmPaStatEpsWinCcAgentTotalInstances,
       "apmPaStatEpsWinCcAgentTotalUsages": apmPaStatEpsWinCcAgentTotalUsages,
       "apmPaStatEpsWinCcAgentTotalSuccesses": apmPaStatEpsWinCcAgentTotalSuccesses,
       "apmPaStatEpsWinCcAgentTotalFailures": apmPaStatEpsWinCcAgentTotalFailures,
       "apmPaStatEpsWinCcAgentTotalErrors": apmPaStatEpsWinCcAgentTotalErrors,
       "apmPaStatEpsWinCcAgentTotalSessVars": apmPaStatEpsWinCcAgentTotalSessVars,
       "apmPaStatEpsAvAgentTotalInstances": apmPaStatEpsAvAgentTotalInstances,
       "apmPaStatEpsAvAgentTotalUsages": apmPaStatEpsAvAgentTotalUsages,
       "apmPaStatEpsAvAgentTotalSuccesses": apmPaStatEpsAvAgentTotalSuccesses,
       "apmPaStatEpsAvAgentTotalFailures": apmPaStatEpsAvAgentTotalFailures,
       "apmPaStatEpsAvAgentTotalErrors": apmPaStatEpsAvAgentTotalErrors,
       "apmPaStatEpsAvAgentTotalSessVars": apmPaStatEpsAvAgentTotalSessVars,
       "apmPaStatEpsWinOsInfoAgentTotalInstances": apmPaStatEpsWinOsInfoAgentTotalInstances,
       "apmPaStatEpsWinOsInfoAgentTotalUsages": apmPaStatEpsWinOsInfoAgentTotalUsages,
       "apmPaStatEpsWinOsInfoAgentTotalSuccesses": apmPaStatEpsWinOsInfoAgentTotalSuccesses,
       "apmPaStatEpsWinOsInfoAgentTotalFailures": apmPaStatEpsWinOsInfoAgentTotalFailures,
       "apmPaStatEpsWinOsInfoAgentTotalErrors": apmPaStatEpsWinOsInfoAgentTotalErrors,
       "apmPaStatEpsWinOsInfoAgentTotalSessVars": apmPaStatEpsWinOsInfoAgentTotalSessVars,
       "apmPaStatEpsWinFcAgentTotalInstances": apmPaStatEpsWinFcAgentTotalInstances,
       "apmPaStatEpsWinFcAgentTotalUsages": apmPaStatEpsWinFcAgentTotalUsages,
       "apmPaStatEpsWinFcAgentTotalSuccesses": apmPaStatEpsWinFcAgentTotalSuccesses,
       "apmPaStatEpsWinFcAgentTotalFailures": apmPaStatEpsWinFcAgentTotalFailures,
       "apmPaStatEpsWinFcAgentTotalErrors": apmPaStatEpsWinFcAgentTotalErrors,
       "apmPaStatEpsWinFcAgentTotalSessVars": apmPaStatEpsWinFcAgentTotalSessVars,
       "apmPaStatEpsWinMcAgentTotalInstances": apmPaStatEpsWinMcAgentTotalInstances,
       "apmPaStatEpsWinMcAgentTotalUsages": apmPaStatEpsWinMcAgentTotalUsages,
       "apmPaStatEpsWinMcAgentTotalSuccesses": apmPaStatEpsWinMcAgentTotalSuccesses,
       "apmPaStatEpsWinMcAgentTotalFailures": apmPaStatEpsWinMcAgentTotalFailures,
       "apmPaStatEpsWinMcAgentTotalErrors": apmPaStatEpsWinMcAgentTotalErrors,
       "apmPaStatEpsWinMcAgentTotalSessVars": apmPaStatEpsWinMcAgentTotalSessVars,
       "apmPaStatEpsFwcAgentTotalInstances": apmPaStatEpsFwcAgentTotalInstances,
       "apmPaStatEpsFwcAgentTotalUsages": apmPaStatEpsFwcAgentTotalUsages,
       "apmPaStatEpsFwcAgentTotalSuccesses": apmPaStatEpsFwcAgentTotalSuccesses,
       "apmPaStatEpsFwcAgentTotalFailures": apmPaStatEpsFwcAgentTotalFailures,
       "apmPaStatEpsFwcAgentTotalErrors": apmPaStatEpsFwcAgentTotalErrors,
       "apmPaStatEpsFwcAgentTotalSessVars": apmPaStatEpsFwcAgentTotalSessVars,
       "apmPaStatEpsWinPcTotalInstances": apmPaStatEpsWinPcTotalInstances,
       "apmPaStatEpsWinPcTotalUsages": apmPaStatEpsWinPcTotalUsages,
       "apmPaStatEpsWinPcTotalSuccesses": apmPaStatEpsWinPcTotalSuccesses,
       "apmPaStatEpsWinPcTotalFailures": apmPaStatEpsWinPcTotalFailures,
       "apmPaStatEpsWinPcTotalErrors": apmPaStatEpsWinPcTotalErrors,
       "apmPaStatEpsWinPcTotalSessVars": apmPaStatEpsWinPcTotalSessVars,
       "apmPaStatEpsWinPwTotalInstances": apmPaStatEpsWinPwTotalInstances,
       "apmPaStatEpsWinPwTotalUsages": apmPaStatEpsWinPwTotalUsages,
       "apmPaStatEpsWinPwTotalSuccesses": apmPaStatEpsWinPwTotalSuccesses,
       "apmPaStatEpsWinPwTotalFailures": apmPaStatEpsWinPwTotalFailures,
       "apmPaStatEpsWinPwTotalErrors": apmPaStatEpsWinPwTotalErrors,
       "apmPaStatEpsWinPwTotalSessVars": apmPaStatEpsWinPwTotalSessVars,
       "apmPaStatEpsWinRcAgentTotalInstances": apmPaStatEpsWinRcAgentTotalInstances,
       "apmPaStatEpsWinRcAgentTotalUsages": apmPaStatEpsWinRcAgentTotalUsages,
       "apmPaStatEpsWinRcAgentTotalSuccesses": apmPaStatEpsWinRcAgentTotalSuccesses,
       "apmPaStatEpsWinRcAgentTotalFailures": apmPaStatEpsWinRcAgentTotalFailures,
       "apmPaStatEpsWinRcAgentTotalErrors": apmPaStatEpsWinRcAgentTotalErrors,
       "apmPaStatEpsWinRcAgentTotalSessVars": apmPaStatEpsWinRcAgentTotalSessVars,
       "apmPaStatEpsWinGpAgentTotalInstances": apmPaStatEpsWinGpAgentTotalInstances,
       "apmPaStatEpsWinGpAgentTotalUsages": apmPaStatEpsWinGpAgentTotalUsages,
       "apmPaStatEpsWinGpAgentTotalSuccesses": apmPaStatEpsWinGpAgentTotalSuccesses,
       "apmPaStatEpsWinGpAgentTotalFailures": apmPaStatEpsWinGpAgentTotalFailures,
       "apmPaStatEpsWinGpAgentTotalErrors": apmPaStatEpsWinGpAgentTotalErrors,
       "apmPaStatEpsWinGpAgentTotalSessVars": apmPaStatEpsWinGpAgentTotalSessVars,
       "apmPaStatExternalLogonAgentTotalInstances": apmPaStatExternalLogonAgentTotalInstances,
       "apmPaStatExternalLogonAgentTotalUsages": apmPaStatExternalLogonAgentTotalUsages,
       "apmPaStatExternalLogonAgentTotalSuccesses": apmPaStatExternalLogonAgentTotalSuccesses,
       "apmPaStatExternalLogonAgentTotalFailures": apmPaStatExternalLogonAgentTotalFailures,
       "apmPaStatExternalLogonAgentTotalErrors": apmPaStatExternalLogonAgentTotalErrors,
       "apmPaStatExternalLogonAgentTotalSessVars": apmPaStatExternalLogonAgentTotalSessVars,
       "apmPaStatLogonAgentTotalInstances": apmPaStatLogonAgentTotalInstances,
       "apmPaStatLogonAgentTotalUsages": apmPaStatLogonAgentTotalUsages,
       "apmPaStatLogonAgentTotalSuccesses": apmPaStatLogonAgentTotalSuccesses,
       "apmPaStatLogonAgentTotalFailures": apmPaStatLogonAgentTotalFailures,
       "apmPaStatLogonAgentTotalErrors": apmPaStatLogonAgentTotalErrors,
       "apmPaStatLogonAgentTotalSessVars": apmPaStatLogonAgentTotalSessVars,
       "apmPaStatRaAgentTotalInstances": apmPaStatRaAgentTotalInstances,
       "apmPaStatRaAgentTotalUsages": apmPaStatRaAgentTotalUsages,
       "apmPaStatRaAgentTotalSuccesses": apmPaStatRaAgentTotalSuccesses,
       "apmPaStatRaAgentTotalFailures": apmPaStatRaAgentTotalFailures,
       "apmPaStatRaAgentTotalErrors": apmPaStatRaAgentTotalErrors,
       "apmPaStatRaAgentTotalSessVars": apmPaStatRaAgentTotalSessVars,
       "apmPaStatRdsAgentTotalInstances": apmPaStatRdsAgentTotalInstances,
       "apmPaStatRdsAgentTotalUsages": apmPaStatRdsAgentTotalUsages,
       "apmPaStatRdsAgentTotalSuccesses": apmPaStatRdsAgentTotalSuccesses,
       "apmPaStatRdsAgentTotalFailures": apmPaStatRdsAgentTotalFailures,
       "apmPaStatRdsAgentTotalErrors": apmPaStatRdsAgentTotalErrors,
       "apmPaStatRdsAgentTotalSessVars": apmPaStatRdsAgentTotalSessVars,
       "apmPaStatVaAgentTotalInstances": apmPaStatVaAgentTotalInstances,
       "apmPaStatVaAgentTotalUsages": apmPaStatVaAgentTotalUsages,
       "apmPaStatVaAgentTotalSuccesses": apmPaStatVaAgentTotalSuccesses,
       "apmPaStatVaAgentTotalFailures": apmPaStatVaAgentTotalFailures,
       "apmPaStatVaAgentTotalErrors": apmPaStatVaAgentTotalErrors,
       "apmPaStatVaAgentTotalSessVars": apmPaStatVaAgentTotalSessVars,
       "apmPaStatIeAgentTotalInstances": apmPaStatIeAgentTotalInstances,
       "apmPaStatIeAgentTotalUsages": apmPaStatIeAgentTotalUsages,
       "apmPaStatIeAgentTotalSuccesses": apmPaStatIeAgentTotalSuccesses,
       "apmPaStatIeAgentTotalFailures": apmPaStatIeAgentTotalFailures,
       "apmPaStatIeAgentTotalErrors": apmPaStatIeAgentTotalErrors,
       "apmPaStatIeAgentTotalSessVars": apmPaStatIeAgentTotalSessVars,
       "apmPaStatLoggingAgentTotalInstances": apmPaStatLoggingAgentTotalInstances,
       "apmPaStatLoggingAgentTotalUsages": apmPaStatLoggingAgentTotalUsages,
       "apmPaStatLoggingAgentTotalSuccesses": apmPaStatLoggingAgentTotalSuccesses,
       "apmPaStatLoggingAgentTotalFailures": apmPaStatLoggingAgentTotalFailures,
       "apmPaStatLoggingAgentTotalErrors": apmPaStatLoggingAgentTotalErrors,
       "apmPaStatLoggingAgentTotalSessVars": apmPaStatLoggingAgentTotalSessVars,
       "apmPaStatDecnBoxAgentTotalInstances": apmPaStatDecnBoxAgentTotalInstances,
       "apmPaStatDecnBoxAgentTotalUsages": apmPaStatDecnBoxAgentTotalUsages,
       "apmPaStatDecnBoxAgentTotalSuccesses": apmPaStatDecnBoxAgentTotalSuccesses,
       "apmPaStatDecnBoxAgentTotalFailures": apmPaStatDecnBoxAgentTotalFailures,
       "apmPaStatDecnBoxAgentTotalErrors": apmPaStatDecnBoxAgentTotalErrors,
       "apmPaStatDecnBoxAgentTotalSessVars": apmPaStatDecnBoxAgentTotalSessVars,
       "apmPaStatMesgBoxAgentTotalInstances": apmPaStatMesgBoxAgentTotalInstances,
       "apmPaStatMesgBoxAgentTotalUsages": apmPaStatMesgBoxAgentTotalUsages,
       "apmPaStatMesgBoxAgentTotalSuccesses": apmPaStatMesgBoxAgentTotalSuccesses,
       "apmPaStatMesgBoxAgentTotalFailures": apmPaStatMesgBoxAgentTotalFailures,
       "apmPaStatMesgBoxAgentTotalErrors": apmPaStatMesgBoxAgentTotalErrors,
       "apmPaStatMesgBoxAgentTotalSessVars": apmPaStatMesgBoxAgentTotalSessVars,
       "apmPaStatApdNoResultErrors": apmPaStatApdNoResultErrors,
       "apmPaStatApdNoSessionErrors": apmPaStatApdNoSessionErrors,
       "apmPaStatApdNoDeviceInfoErrors": apmPaStatApdNoDeviceInfoErrors,
       "apmPaStatApdNoTokenErrors": apmPaStatApdNoTokenErrors,
       "apmPaStatApdNoSigErrors": apmPaStatApdNoSigErrors,
       "apmPaStatApdTotalMismatchErrors": apmPaStatApdTotalMismatchErrors,
       "apmPaStatApdInvalidSigErrors": apmPaStatApdInvalidSigErrors,
       "apmPaStatApdMcPipelineInitErrors": apmPaStatApdMcPipelineInitErrors,
       "apmPaStatApdMcSetSessVarErrors": apmPaStatApdMcSetSessVarErrors,
       "apmPaStatApdMcPipelineCloseErrors": apmPaStatApdMcPipelineCloseErrors,
       "apmPaStatApdApResultErrors": apmPaStatApdApResultErrors,
       "apmPaStatApdApInternalErrors": apmPaStatApdApInternalErrors,
       "apmPaStatAllowedRequests": apmPaStatAllowedRequests,
       "apmPaStatDeniedRequests": apmPaStatDeniedRequests,
       "apmPaStatVsName": apmPaStatVsName,
       "apmProfileConnectivityStat": apmProfileConnectivityStat,
       "apmPcStatResetStats": apmPcStatResetStats,
       "apmPcStatNumber": apmPcStatNumber,
       "apmPcStatTable": apmPcStatTable,
       "apmPcStatEntry": apmPcStatEntry,
       "apmPcStatName": apmPcStatName,
       "apmPcStatTotConns": apmPcStatTotConns,
       "apmPcStatCurConns": apmPcStatCurConns,
       "apmPcStatMaxConns": apmPcStatMaxConns,
       "apmPcStatIngressRaw": apmPcStatIngressRaw,
       "apmPcStatEgressRaw": apmPcStatEgressRaw,
       "apmPcStatIngressCompressed": apmPcStatIngressCompressed,
       "apmPcStatEgressCompressed": apmPcStatEgressCompressed,
       "apmProfileRewriteStat": apmProfileRewriteStat,
       "apmPrStatResetStats": apmPrStatResetStats,
       "apmPrStatNumber": apmPrStatNumber,
       "apmPrStatTable": apmPrStatTable,
       "apmPrStatEntry": apmPrStatEntry,
       "apmPrStatName": apmPrStatName,
       "apmPrStatClientReqBytes": apmPrStatClientReqBytes,
       "apmPrStatClientRespBytes": apmPrStatClientRespBytes,
       "apmPrStatServerReqBytes": apmPrStatServerReqBytes,
       "apmPrStatServerRespBytes": apmPrStatServerRespBytes,
       "apmPrStatClientReqs": apmPrStatClientReqs,
       "apmPrStatClientResps": apmPrStatClientResps,
       "apmPrStatServerReqs": apmPrStatServerReqs,
       "apmPrStatServerResps": apmPrStatServerResps,
       "apmAccessStat": apmAccessStat,
       "apmAccessStatResetStats": apmAccessStatResetStats,
       "apmAccessStatTotalSessions": apmAccessStatTotalSessions,
       "apmAccessStatCurrentActiveSessions": apmAccessStatCurrentActiveSessions,
       "apmAccessStatCurrentPendingSessions": apmAccessStatCurrentPendingSessions,
       "apmAccessStatCurrentEndedSessions": apmAccessStatCurrentEndedSessions,
       "apmAccessStatUserLoggedoutSessions": apmAccessStatUserLoggedoutSessions,
       "apmAccessStatAdminTerminatedSessions": apmAccessStatAdminTerminatedSessions,
       "apmAccessStatMiscTerminatedSessions": apmAccessStatMiscTerminatedSessions,
       "apmAccessStatResultAllow": apmAccessStatResultAllow,
       "apmAccessStatResultDeny": apmAccessStatResultDeny,
       "apmAccessStatResultRedirect": apmAccessStatResultRedirect,
       "apmAccessStatResultRedirectWithSession": apmAccessStatResultRedirectWithSession,
       "apmGlobalConnectivityStat": apmGlobalConnectivityStat,
       "apmGlobalConnectivityStatResetStats": apmGlobalConnectivityStatResetStats,
       "apmGlobalConnectivityStatTotConns": apmGlobalConnectivityStatTotConns,
       "apmGlobalConnectivityStatCurConns": apmGlobalConnectivityStatCurConns,
       "apmGlobalConnectivityStatMaxConns": apmGlobalConnectivityStatMaxConns,
       "apmGlobalConnectivityStatIngressRaw": apmGlobalConnectivityStatIngressRaw,
       "apmGlobalConnectivityStatEgressRaw": apmGlobalConnectivityStatEgressRaw,
       "apmGlobalConnectivityStatIngressCompressed": apmGlobalConnectivityStatIngressCompressed,
       "apmGlobalConnectivityStatEgressCompressed": apmGlobalConnectivityStatEgressCompressed,
       "apmGlobalRewriteStat": apmGlobalRewriteStat,
       "apmGlobalRewriteStatResetStats": apmGlobalRewriteStatResetStats,
       "apmGlobalRewriteStatClientReqBytes": apmGlobalRewriteStatClientReqBytes,
       "apmGlobalRewriteStatClientRespBytes": apmGlobalRewriteStatClientRespBytes,
       "apmGlobalRewriteStatServerReqBytes": apmGlobalRewriteStatServerReqBytes,
       "apmGlobalRewriteStatServerRespBytes": apmGlobalRewriteStatServerRespBytes,
       "apmGlobalRewriteStatClientReqs": apmGlobalRewriteStatClientReqs,
       "apmGlobalRewriteStatClientResps": apmGlobalRewriteStatClientResps,
       "apmGlobalRewriteStatServerReqs": apmGlobalRewriteStatServerReqs,
       "apmGlobalRewriteStatServerResps": apmGlobalRewriteStatServerResps,
       "apmProfileAccessAgentStat": apmProfileAccessAgentStat,
       "apmPgStatResetStats": apmPgStatResetStats,
       "apmPgStatNumber": apmPgStatNumber,
       "apmPgStatTable": apmPgStatTable,
       "apmPgStatEntry": apmPgStatEntry,
       "apmPgStatName": apmPgStatName,
       "apmPgStatAgentName": apmPgStatAgentName,
       "apmPgStatInstances": apmPgStatInstances,
       "apmPgStatUsages": apmPgStatUsages,
       "apmPgStatSuccesses": apmPgStatSuccesses,
       "apmPgStatFailures": apmPgStatFailures,
       "apmPgStatErrors": apmPgStatErrors,
       "apmPgStatSessionVars": apmPgStatSessionVars,
       "apmProfileAccessMiscStat": apmProfileAccessMiscStat,
       "apmPmStatResetStats": apmPmStatResetStats,
       "apmPmStatNumber": apmPmStatNumber,
       "apmPmStatTable": apmPmStatTable,
       "apmPmStatEntry": apmPmStatEntry,
       "apmPmStatName": apmPmStatName,
       "apmPmStatConfigSyncState": apmPmStatConfigSyncState,
       "apmPmStatInspResultError": apmPmStatInspResultError,
       "apmPmStatInspSessionError": apmPmStatInspSessionError,
       "apmPmStatInspDeviceInfoError": apmPmStatInspDeviceInfoError,
       "apmPmStatInspTokenError": apmPmStatInspTokenError,
       "apmPmStatInspSignatureError": apmPmStatInspSignatureError,
       "apmPmStatInspDataMsmtchError": apmPmStatInspDataMsmtchError,
       "apmPmStatInspClientSignError": apmPmStatInspClientSignError,
       "apmPmStatMemInitError": apmPmStatMemInitError,
       "apmPmStatMemSessionVarError": apmPmStatMemSessionVarError,
       "apmPmStatMemCloseError": apmPmStatMemCloseError,
       "apmPmStatResultError": apmPmStatResultError,
       "apmPmStatInternalError": apmPmStatInternalError,
       "apmLeasepool": apmLeasepool,
       "apmLeasepoolStat": apmLeasepoolStat,
       "apmLeasepoolStatResetStats": apmLeasepoolStatResetStats,
       "apmLeasepoolStatNumber": apmLeasepoolStatNumber,
       "apmLeasepoolStatTable": apmLeasepoolStatTable,
       "apmLeasepoolStatEntry": apmLeasepoolStatEntry,
       "apmLeasepoolStatName": apmLeasepoolStatName,
       "apmLeasepoolStatCurMembers": apmLeasepoolStatCurMembers,
       "apmLeasepoolStatCurAssigned": apmLeasepoolStatCurAssigned,
       "apmLeasepoolStatCurFree": apmLeasepoolStatCurFree,
       "apmLeasepoolStatMaxAssigned": apmLeasepoolStatMaxAssigned,
       "apmLeasepoolStatTotPickRequests": apmLeasepoolStatTotPickRequests,
       "apmLeasepoolStatTotPickFailure": apmLeasepoolStatTotPickFailure,
       "apmLeasepoolStatTotReserveRequests": apmLeasepoolStatTotReserveRequests,
       "apmLeasepoolStatTotReserveFailure": apmLeasepoolStatTotReserveFailure,
       "apmLeasepoolStatTotReleaseRequests": apmLeasepoolStatTotReleaseRequests,
       "apmLeasepoolStatTotReleaseFailure": apmLeasepoolStatTotReleaseFailure,
       "apmAcl": apmAcl,
       "apmAclStat": apmAclStat,
       "apmAclStatResetStats": apmAclStatResetStats,
       "apmAclStatNumber": apmAclStatNumber,
       "apmAclStatTable": apmAclStatTable,
       "apmAclStatEntry": apmAclStatEntry,
       "apmAclStatName": apmAclStatName,
       "apmAclStatActionAllow": apmAclStatActionAllow,
       "apmAclStatActionContinue": apmAclStatActionContinue,
       "apmAclStatActionDiscard": apmAclStatActionDiscard,
       "apmAclStatActionReject": apmAclStatActionReject}
)
