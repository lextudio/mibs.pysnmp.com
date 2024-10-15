# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-SM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:52 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(jnxMobileGatewayPgwGgsn,) = mibBuilder.importSymbols(
    "JUNIPER-MBG-SMI",
    "jnxMobileGatewayPgwGgsn")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

(jnxMbgGwIndex,
 jnxMbgGwName) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwIndex",
    "jnxMbgGwName")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxMbgPgwSubscriberManagerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1)
)
jnxMbgPgwSubscriberManagerMib.setRevisions(
        ("2011-01-12 12:00",
         "2011-02-28 12:00",
         "2011-02-28 12:00",
         "2012-03-19 12:00",
         "2012-03-22 12:00",
         "2012-10-12 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgPgwSMNotifications_ObjectIdentity = ObjectIdentity
jnxMbgPgwSMNotifications = _JnxMbgPgwSMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0)
)
_JnxMbgPgwSMObjects_ObjectIdentity = ObjectIdentity
jnxMbgPgwSMObjects = _JnxMbgPgwSMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1)
)
_JnxMbgPgwAPNStatsTable_Object = MibTable
jnxMbgPgwAPNStatsTable = _JnxMbgPgwAPNStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxMbgPgwAPNStatsTable.setStatus("deprecated")
_JnxMbgPgwAPNStatsTableEntry_Object = MibTableRow
jnxMbgPgwAPNStatsTableEntry = _JnxMbgPgwAPNStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1)
)
jnxMbgPgwAPNStatsTableEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwAPNName"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwAPNStatsTableEntry.setStatus("deprecated")
_JnxMbgPgwAPNName_Type = DisplayString
_JnxMbgPgwAPNName_Object = MibTableColumn
jnxMbgPgwAPNName = _JnxMbgPgwAPNName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 1),
    _JnxMbgPgwAPNName_Type()
)
jnxMbgPgwAPNName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwAPNName.setStatus("deprecated")
_JnxMbgPgwSessnEstAttempts_Type = Counter64
_JnxMbgPgwSessnEstAttempts_Object = MibTableColumn
jnxMbgPgwSessnEstAttempts = _JnxMbgPgwSessnEstAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 2),
    _JnxMbgPgwSessnEstAttempts_Type()
)
jnxMbgPgwSessnEstAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnEstAttempts.setStatus("deprecated")
_JnxMbgPgwSuccSessnsEst_Type = Counter64
_JnxMbgPgwSuccSessnsEst_Object = MibTableColumn
jnxMbgPgwSuccSessnsEst = _JnxMbgPgwSuccSessnsEst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 3),
    _JnxMbgPgwSuccSessnsEst_Type()
)
jnxMbgPgwSuccSessnsEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccSessnsEst.setStatus("deprecated")
_JnxMbgPgwSessnFailedServcUnaval_Type = Counter64
_JnxMbgPgwSessnFailedServcUnaval_Object = MibTableColumn
jnxMbgPgwSessnFailedServcUnaval = _JnxMbgPgwSessnFailedServcUnaval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 4),
    _JnxMbgPgwSessnFailedServcUnaval_Type()
)
jnxMbgPgwSessnFailedServcUnaval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnFailedServcUnaval.setStatus("deprecated")
_JnxMbgPgwSessnFailedSysFailure_Type = Counter64
_JnxMbgPgwSessnFailedSysFailure_Object = MibTableColumn
jnxMbgPgwSessnFailedSysFailure = _JnxMbgPgwSessnFailedSysFailure_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 5),
    _JnxMbgPgwSessnFailedSysFailure_Type()
)
jnxMbgPgwSessnFailedSysFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnFailedSysFailure.setStatus("deprecated")
_JnxMbgPgwSessnFailedNoResource_Type = Counter64
_JnxMbgPgwSessnFailedNoResource_Object = MibTableColumn
jnxMbgPgwSessnFailedNoResource = _JnxMbgPgwSessnFailedNoResource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 6),
    _JnxMbgPgwSessnFailedNoResource_Type()
)
jnxMbgPgwSessnFailedNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnFailedNoResource.setStatus("deprecated")
_JnxMbgPgwSessnFailedNoAddr_Type = Counter64
_JnxMbgPgwSessnFailedNoAddr_Object = MibTableColumn
jnxMbgPgwSessnFailedNoAddr = _JnxMbgPgwSessnFailedNoAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 7),
    _JnxMbgPgwSessnFailedNoAddr_Type()
)
jnxMbgPgwSessnFailedNoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnFailedNoAddr.setStatus("deprecated")
_JnxMbgPgwSessnFailedServcDenied_Type = Counter64
_JnxMbgPgwSessnFailedServcDenied_Object = MibTableColumn
jnxMbgPgwSessnFailedServcDenied = _JnxMbgPgwSessnFailedServcDenied_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 8),
    _JnxMbgPgwSessnFailedServcDenied_Type()
)
jnxMbgPgwSessnFailedServcDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnFailedServcDenied.setStatus("deprecated")
_JnxMbgPgwSessnFailedAuthFailed_Type = Counter64
_JnxMbgPgwSessnFailedAuthFailed_Object = MibTableColumn
jnxMbgPgwSessnFailedAuthFailed = _JnxMbgPgwSessnFailedAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 9),
    _JnxMbgPgwSessnFailedAuthFailed_Type()
)
jnxMbgPgwSessnFailedAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnFailedAuthFailed.setStatus("deprecated")
_JnxMbgPgwSessnFailedAccessDenied_Type = Counter64
_JnxMbgPgwSessnFailedAccessDenied_Object = MibTableColumn
jnxMbgPgwSessnFailedAccessDenied = _JnxMbgPgwSessnFailedAccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 10),
    _JnxMbgPgwSessnFailedAccessDenied_Type()
)
jnxMbgPgwSessnFailedAccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnFailedAccessDenied.setStatus("deprecated")
_JnxMbgPgwPeerInitSessnDeact_Type = Counter64
_JnxMbgPgwPeerInitSessnDeact_Object = MibTableColumn
jnxMbgPgwPeerInitSessnDeact = _JnxMbgPgwPeerInitSessnDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 11),
    _JnxMbgPgwPeerInitSessnDeact_Type()
)
jnxMbgPgwPeerInitSessnDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPeerInitSessnDeact.setStatus("deprecated")
_JnxMbgPgwSuccPeerInitSessnDeact_Type = Counter64
_JnxMbgPgwSuccPeerInitSessnDeact_Object = MibTableColumn
jnxMbgPgwSuccPeerInitSessnDeact = _JnxMbgPgwSuccPeerInitSessnDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 12),
    _JnxMbgPgwSuccPeerInitSessnDeact_Type()
)
jnxMbgPgwSuccPeerInitSessnDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccPeerInitSessnDeact.setStatus("deprecated")
_JnxMbgPgwGWInitSessnDeact_Type = Counter64
_JnxMbgPgwGWInitSessnDeact_Object = MibTableColumn
jnxMbgPgwGWInitSessnDeact = _JnxMbgPgwGWInitSessnDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 13),
    _JnxMbgPgwGWInitSessnDeact_Type()
)
jnxMbgPgwGWInitSessnDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGWInitSessnDeact.setStatus("deprecated")
_JnxMbgPgwSuccGWInitSessnDeact_Type = Counter64
_JnxMbgPgwSuccGWInitSessnDeact_Object = MibTableColumn
jnxMbgPgwSuccGWInitSessnDeact = _JnxMbgPgwSuccGWInitSessnDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 1, 1, 14),
    _JnxMbgPgwSuccGWInitSessnDeact_Type()
)
jnxMbgPgwSuccGWInitSessnDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccGWInitSessnDeact.setStatus("deprecated")
_JnxMbgPgwStatus_ObjectIdentity = ObjectIdentity
jnxMbgPgwStatus = _JnxMbgPgwStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 2)
)
_JnxMbgPgwActiveSubscribers_Type = Counter64
_JnxMbgPgwActiveSubscribers_Object = MibScalar
jnxMbgPgwActiveSubscribers = _JnxMbgPgwActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 2, 1),
    _JnxMbgPgwActiveSubscribers_Type()
)
jnxMbgPgwActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActiveSubscribers.setStatus("deprecated")
_JnxMbgPgwActiveSessions_Type = Counter64
_JnxMbgPgwActiveSessions_Object = MibScalar
jnxMbgPgwActiveSessions = _JnxMbgPgwActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 2, 2),
    _JnxMbgPgwActiveSessions_Type()
)
jnxMbgPgwActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActiveSessions.setStatus("deprecated")
_JnxMbgPgwActiveBearers_Type = Counter64
_JnxMbgPgwActiveBearers_Object = MibScalar
jnxMbgPgwActiveBearers = _JnxMbgPgwActiveBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 2, 3),
    _JnxMbgPgwActiveBearers_Type()
)
jnxMbgPgwActiveBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActiveBearers.setStatus("deprecated")
_JnxMbgPgwCPUUtilization_Type = Counter64
_JnxMbgPgwCPUUtilization_Object = MibScalar
jnxMbgPgwCPUUtilization = _JnxMbgPgwCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 2, 4),
    _JnxMbgPgwCPUUtilization_Type()
)
jnxMbgPgwCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCPUUtilization.setStatus("deprecated")
_JnxMbgPgwMemoryUtilization_Type = Counter64
_JnxMbgPgwMemoryUtilization_Object = MibScalar
jnxMbgPgwMemoryUtilization = _JnxMbgPgwMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 2, 5),
    _JnxMbgPgwMemoryUtilization_Type()
)
jnxMbgPgwMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwMemoryUtilization.setStatus("deprecated")
_JnxMbgPgwSMNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgPgwSMNotificationVars = _JnxMbgPgwSMNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3)
)
_JnxMbgPgwGatewayName_Type = DisplayString
_JnxMbgPgwGatewayName_Object = MibScalar
jnxMbgPgwGatewayName = _JnxMbgPgwGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 1),
    _JnxMbgPgwGatewayName_Type()
)
jnxMbgPgwGatewayName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwGatewayName.setStatus("current")
_JnxMbgPgwQosAPNName_Type = DisplayString
_JnxMbgPgwQosAPNName_Object = MibScalar
jnxMbgPgwQosAPNName = _JnxMbgPgwQosAPNName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 2),
    _JnxMbgPgwQosAPNName_Type()
)
jnxMbgPgwQosAPNName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwQosAPNName.setStatus("current")
_JnxMbgPgwQosThreshold1Status_Type = TruthValue
_JnxMbgPgwQosThreshold1Status_Object = MibScalar
jnxMbgPgwQosThreshold1Status = _JnxMbgPgwQosThreshold1Status_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 3),
    _JnxMbgPgwQosThreshold1Status_Type()
)
jnxMbgPgwQosThreshold1Status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwQosThreshold1Status.setStatus("current")
_JnxMbgPgwQosThreshold2Status_Type = TruthValue
_JnxMbgPgwQosThreshold2Status_Object = MibScalar
jnxMbgPgwQosThreshold2Status = _JnxMbgPgwQosThreshold2Status_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 4),
    _JnxMbgPgwQosThreshold2Status_Type()
)
jnxMbgPgwQosThreshold2Status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwQosThreshold2Status.setStatus("current")
_JnxMbgPgwSMGTPEventType_Type = DisplayString
_JnxMbgPgwSMGTPEventType_Object = MibScalar
jnxMbgPgwSMGTPEventType = _JnxMbgPgwSMGTPEventType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 5),
    _JnxMbgPgwSMGTPEventType_Type()
)
jnxMbgPgwSMGTPEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMGTPEventType.setStatus("current")
_JnxMbgPgwSMGTPEventCause_Type = DisplayString
_JnxMbgPgwSMGTPEventCause_Object = MibScalar
jnxMbgPgwSMGTPEventCause = _JnxMbgPgwSMGTPEventCause_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 6),
    _JnxMbgPgwSMGTPEventCause_Type()
)
jnxMbgPgwSMGTPEventCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMGTPEventCause.setStatus("current")
_JnxMbgPgwSMAlarmThrshld_Type = DisplayString
_JnxMbgPgwSMAlarmThrshld_Object = MibScalar
jnxMbgPgwSMAlarmThrshld = _JnxMbgPgwSMAlarmThrshld_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 7),
    _JnxMbgPgwSMAlarmThrshld_Type()
)
jnxMbgPgwSMAlarmThrshld.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMAlarmThrshld.setStatus("current")
_JnxMbgPgwSMAlarmState_Type = DisplayString
_JnxMbgPgwSMAlarmState_Object = MibScalar
jnxMbgPgwSMAlarmState = _JnxMbgPgwSMAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 8),
    _JnxMbgPgwSMAlarmState_Type()
)
jnxMbgPgwSMAlarmState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMAlarmState.setStatus("current")
_JnxMbgPgwSMSPICName_Type = DisplayString
_JnxMbgPgwSMSPICName_Object = MibScalar
jnxMbgPgwSMSPICName = _JnxMbgPgwSMSPICName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 9),
    _JnxMbgPgwSMSPICName_Type()
)
jnxMbgPgwSMSPICName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMSPICName.setStatus("current")
_JnxMbgPgwSMTCName_Type = DisplayString
_JnxMbgPgwSMTCName_Object = MibScalar
jnxMbgPgwSMTCName = _JnxMbgPgwSMTCName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 10),
    _JnxMbgPgwSMTCName_Type()
)
jnxMbgPgwSMTCName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMTCName.setStatus("current")
_JnxMbgPgwSMQCIName_Type = DisplayString
_JnxMbgPgwSMQCIName_Object = MibScalar
jnxMbgPgwSMQCIName = _JnxMbgPgwSMQCIName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 11),
    _JnxMbgPgwSMQCIName_Type()
)
jnxMbgPgwSMQCIName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMQCIName.setStatus("current")
_JnxMbgPgwSMSessionEstFailReason_Type = DisplayString
_JnxMbgPgwSMSessionEstFailReason_Object = MibScalar
jnxMbgPgwSMSessionEstFailReason = _JnxMbgPgwSMSessionEstFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 12),
    _JnxMbgPgwSMSessionEstFailReason_Type()
)
jnxMbgPgwSMSessionEstFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMSessionEstFailReason.setStatus("current")
_JnxMbgPgwMMGatewayName_Type = DisplayString
_JnxMbgPgwMMGatewayName_Object = MibScalar
jnxMbgPgwMMGatewayName = _JnxMbgPgwMMGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 13),
    _JnxMbgPgwMMGatewayName_Type()
)
jnxMbgPgwMMGatewayName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwMMGatewayName.setStatus("current")
_JnxMbgPgwPrevGatewayMMState_Type = DisplayString
_JnxMbgPgwPrevGatewayMMState_Object = MibScalar
jnxMbgPgwPrevGatewayMMState = _JnxMbgPgwPrevGatewayMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 14),
    _JnxMbgPgwPrevGatewayMMState_Type()
)
jnxMbgPgwPrevGatewayMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwPrevGatewayMMState.setStatus("current")
_JnxMbgPgwNewGatewayMMState_Type = DisplayString
_JnxMbgPgwNewGatewayMMState_Object = MibScalar
jnxMbgPgwNewGatewayMMState = _JnxMbgPgwNewGatewayMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 15),
    _JnxMbgPgwNewGatewayMMState_Type()
)
jnxMbgPgwNewGatewayMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwNewGatewayMMState.setStatus("current")
_JnxMbgPgwAPNMMGatewayName_Type = DisplayString
_JnxMbgPgwAPNMMGatewayName_Object = MibScalar
jnxMbgPgwAPNMMGatewayName = _JnxMbgPgwAPNMMGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 16),
    _JnxMbgPgwAPNMMGatewayName_Type()
)
jnxMbgPgwAPNMMGatewayName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwAPNMMGatewayName.setStatus("current")
_JnxMbgPgwAPNMMAPNName_Type = DisplayString
_JnxMbgPgwAPNMMAPNName_Object = MibScalar
jnxMbgPgwAPNMMAPNName = _JnxMbgPgwAPNMMAPNName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 17),
    _JnxMbgPgwAPNMMAPNName_Type()
)
jnxMbgPgwAPNMMAPNName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwAPNMMAPNName.setStatus("current")
_JnxMbgPgwPrevAPNMMState_Type = DisplayString
_JnxMbgPgwPrevAPNMMState_Object = MibScalar
jnxMbgPgwPrevAPNMMState = _JnxMbgPgwPrevAPNMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 18),
    _JnxMbgPgwPrevAPNMMState_Type()
)
jnxMbgPgwPrevAPNMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwPrevAPNMMState.setStatus("current")
_JnxMbgPgwNewAPNMMState_Type = DisplayString
_JnxMbgPgwNewAPNMMState_Object = MibScalar
jnxMbgPgwNewAPNMMState = _JnxMbgPgwNewAPNMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 19),
    _JnxMbgPgwNewAPNMMState_Type()
)
jnxMbgPgwNewAPNMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwNewAPNMMState.setStatus("current")
_JnxMbgPgwTrapGwIndex_Type = Unsigned32
_JnxMbgPgwTrapGwIndex_Object = MibScalar
jnxMbgPgwTrapGwIndex = _JnxMbgPgwTrapGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 20),
    _JnxMbgPgwTrapGwIndex_Type()
)
jnxMbgPgwTrapGwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwTrapGwIndex.setStatus("current")
_JnxMbgPgwTrapGwName_Type = DisplayString
_JnxMbgPgwTrapGwName_Object = MibScalar
jnxMbgPgwTrapGwName = _JnxMbgPgwTrapGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 21),
    _JnxMbgPgwTrapGwName_Type()
)
jnxMbgPgwTrapGwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwTrapGwName.setStatus("current")
_JnxMbgPgwSpicName_Type = DisplayString
_JnxMbgPgwSpicName_Object = MibScalar
jnxMbgPgwSpicName = _JnxMbgPgwSpicName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 22),
    _JnxMbgPgwSpicName_Type()
)
jnxMbgPgwSpicName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicName.setStatus("current")
_JnxMbgPgwSMInterfaceName_Type = DisplayString
_JnxMbgPgwSMInterfaceName_Object = MibScalar
jnxMbgPgwSMInterfaceName = _JnxMbgPgwSMInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 3, 23),
    _JnxMbgPgwSMInterfaceName_Type()
)
jnxMbgPgwSMInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwSMInterfaceName.setStatus("current")
_JnxMbgPgwSMOperStatsTable_Object = MibTable
jnxMbgPgwSMOperStatsTable = _JnxMbgPgwSMOperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMOperStatsTable.setStatus("current")
_JnxMbgPgwSMOperStatsEntry_Object = MibTableRow
jnxMbgPgwSMOperStatsEntry = _JnxMbgPgwSMOperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1)
)
jnxMbgPgwSMOperStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMOperStatsEntry.setStatus("current")
_JnxMbgPgwSessnEstAttmpts_Type = Counter64
_JnxMbgPgwSessnEstAttmpts_Object = MibTableColumn
jnxMbgPgwSessnEstAttmpts = _JnxMbgPgwSessnEstAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 1),
    _JnxMbgPgwSessnEstAttmpts_Type()
)
jnxMbgPgwSessnEstAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessnEstAttmpts.setStatus("current")
_JnxMbgPgwSuccSessnEst_Type = Counter64
_JnxMbgPgwSuccSessnEst_Object = MibTableColumn
jnxMbgPgwSuccSessnEst = _JnxMbgPgwSuccSessnEst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 2),
    _JnxMbgPgwSuccSessnEst_Type()
)
jnxMbgPgwSuccSessnEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccSessnEst.setStatus("current")
_JnxMbgPgwPeerInitDeactv_Type = Counter64
_JnxMbgPgwPeerInitDeactv_Object = MibTableColumn
jnxMbgPgwPeerInitDeactv = _JnxMbgPgwPeerInitDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 3),
    _JnxMbgPgwPeerInitDeactv_Type()
)
jnxMbgPgwPeerInitDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPeerInitDeactv.setStatus("current")
_JnxMbgPgwPeerInitSuccDeactv_Type = Counter64
_JnxMbgPgwPeerInitSuccDeactv_Object = MibTableColumn
jnxMbgPgwPeerInitSuccDeactv = _JnxMbgPgwPeerInitSuccDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 4),
    _JnxMbgPgwPeerInitSuccDeactv_Type()
)
jnxMbgPgwPeerInitSuccDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPeerInitSuccDeactv.setStatus("current")
_JnxMbgPgwGwInitDeactv_Type = Counter64
_JnxMbgPgwGwInitDeactv_Object = MibTableColumn
jnxMbgPgwGwInitDeactv = _JnxMbgPgwGwInitDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 5),
    _JnxMbgPgwGwInitDeactv_Type()
)
jnxMbgPgwGwInitDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGwInitDeactv.setStatus("current")
_JnxMbgPgwGwInitSuccDeactv_Type = Counter64
_JnxMbgPgwGwInitSuccDeactv_Object = MibTableColumn
jnxMbgPgwGwInitSuccDeactv = _JnxMbgPgwGwInitSuccDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 6),
    _JnxMbgPgwGwInitSuccDeactv_Type()
)
jnxMbgPgwGwInitSuccDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGwInitSuccDeactv.setStatus("current")
_JnxMbgPgwGtpStatsGnS5S8InpPkt_Type = Counter64
_JnxMbgPgwGtpStatsGnS5S8InpPkt_Object = MibTableColumn
jnxMbgPgwGtpStatsGnS5S8InpPkt = _JnxMbgPgwGtpStatsGnS5S8InpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 7),
    _JnxMbgPgwGtpStatsGnS5S8InpPkt_Type()
)
jnxMbgPgwGtpStatsGnS5S8InpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGnS5S8InpPkt.setStatus("current")
_JnxMbgPgwGtpStatsGnS5S8InpByt_Type = Counter64
_JnxMbgPgwGtpStatsGnS5S8InpByt_Object = MibTableColumn
jnxMbgPgwGtpStatsGnS5S8InpByt = _JnxMbgPgwGtpStatsGnS5S8InpByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 8),
    _JnxMbgPgwGtpStatsGnS5S8InpByt_Type()
)
jnxMbgPgwGtpStatsGnS5S8InpByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGnS5S8InpByt.setStatus("current")
_JnxMbgPgwGtpStatsGnS5S8OutPkt_Type = Counter64
_JnxMbgPgwGtpStatsGnS5S8OutPkt_Object = MibTableColumn
jnxMbgPgwGtpStatsGnS5S8OutPkt = _JnxMbgPgwGtpStatsGnS5S8OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 9),
    _JnxMbgPgwGtpStatsGnS5S8OutPkt_Type()
)
jnxMbgPgwGtpStatsGnS5S8OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGnS5S8OutPkt.setStatus("current")
_JnxMbgPgwGtpStatsGnS5S8OutByt_Type = Counter64
_JnxMbgPgwGtpStatsGnS5S8OutByt_Object = MibTableColumn
jnxMbgPgwGtpStatsGnS5S8OutByt = _JnxMbgPgwGtpStatsGnS5S8OutByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 10),
    _JnxMbgPgwGtpStatsGnS5S8OutByt_Type()
)
jnxMbgPgwGtpStatsGnS5S8OutByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGnS5S8OutByt.setStatus("current")
_JnxMbgPgwGtpStatsGiInpPkt_Type = Counter64
_JnxMbgPgwGtpStatsGiInpPkt_Object = MibTableColumn
jnxMbgPgwGtpStatsGiInpPkt = _JnxMbgPgwGtpStatsGiInpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 11),
    _JnxMbgPgwGtpStatsGiInpPkt_Type()
)
jnxMbgPgwGtpStatsGiInpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGiInpPkt.setStatus("current")
_JnxMbgPgwGtpStatsGiInpByt_Type = Counter64
_JnxMbgPgwGtpStatsGiInpByt_Object = MibTableColumn
jnxMbgPgwGtpStatsGiInpByt = _JnxMbgPgwGtpStatsGiInpByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 12),
    _JnxMbgPgwGtpStatsGiInpByt_Type()
)
jnxMbgPgwGtpStatsGiInpByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGiInpByt.setStatus("current")
_JnxMbgPgwGtpStatsGiOutPkt_Type = Counter64
_JnxMbgPgwGtpStatsGiOutPkt_Object = MibTableColumn
jnxMbgPgwGtpStatsGiOutPkt = _JnxMbgPgwGtpStatsGiOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 13),
    _JnxMbgPgwGtpStatsGiOutPkt_Type()
)
jnxMbgPgwGtpStatsGiOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGiOutPkt.setStatus("current")
_JnxMbgPgwGtpStatsGiOutByt_Type = Counter64
_JnxMbgPgwGtpStatsGiOutByt_Object = MibTableColumn
jnxMbgPgwGtpStatsGiOutByt = _JnxMbgPgwGtpStatsGiOutByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 14),
    _JnxMbgPgwGtpStatsGiOutByt_Type()
)
jnxMbgPgwGtpStatsGiOutByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGiOutByt.setStatus("current")
_JnxMbgPgwGtpStatsS58DscrdPkts_Type = Counter64
_JnxMbgPgwGtpStatsS58DscrdPkts_Object = MibTableColumn
jnxMbgPgwGtpStatsS58DscrdPkts = _JnxMbgPgwGtpStatsS58DscrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 15),
    _JnxMbgPgwGtpStatsS58DscrdPkts_Type()
)
jnxMbgPgwGtpStatsS58DscrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsS58DscrdPkts.setStatus("current")
_JnxMbgPgwGtpStatsGiDiscrdPkts_Type = Counter64
_JnxMbgPgwGtpStatsGiDiscrdPkts_Object = MibTableColumn
jnxMbgPgwGtpStatsGiDiscrdPkts = _JnxMbgPgwGtpStatsGiDiscrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 16),
    _JnxMbgPgwGtpStatsGiDiscrdPkts_Type()
)
jnxMbgPgwGtpStatsGiDiscrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpStatsGiDiscrdPkts.setStatus("current")
_JnxMbgPgwSrcAddrViolationPkts_Type = Counter64
_JnxMbgPgwSrcAddrViolationPkts_Object = MibTableColumn
jnxMbgPgwSrcAddrViolationPkts = _JnxMbgPgwSrcAddrViolationPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 17),
    _JnxMbgPgwSrcAddrViolationPkts_Type()
)
jnxMbgPgwSrcAddrViolationPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSrcAddrViolationPkts.setStatus("current")
_JnxMbgPgwSrcAddrViolationByts_Type = Counter64
_JnxMbgPgwSrcAddrViolationByts_Object = MibTableColumn
jnxMbgPgwSrcAddrViolationByts = _JnxMbgPgwSrcAddrViolationByts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 18),
    _JnxMbgPgwSrcAddrViolationByts_Type()
)
jnxMbgPgwSrcAddrViolationByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSrcAddrViolationByts.setStatus("current")
_JnxMbgPgwPktsRcvdNonExstTeids_Type = Counter64
_JnxMbgPgwPktsRcvdNonExstTeids_Object = MibTableColumn
jnxMbgPgwPktsRcvdNonExstTeids = _JnxMbgPgwPktsRcvdNonExstTeids_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 19),
    _JnxMbgPgwPktsRcvdNonExstTeids_Type()
)
jnxMbgPgwPktsRcvdNonExstTeids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPktsRcvdNonExstTeids.setStatus("current")
_JnxMbgPgwGtpErrLenPkts_Type = Counter64
_JnxMbgPgwGtpErrLenPkts_Object = MibTableColumn
jnxMbgPgwGtpErrLenPkts = _JnxMbgPgwGtpErrLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 20),
    _JnxMbgPgwGtpErrLenPkts_Type()
)
jnxMbgPgwGtpErrLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpErrLenPkts.setStatus("current")
_JnxMbgPgwNonExstUeAddrPkts_Type = Counter64
_JnxMbgPgwNonExstUeAddrPkts_Object = MibTableColumn
jnxMbgPgwNonExstUeAddrPkts = _JnxMbgPgwNonExstUeAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 21),
    _JnxMbgPgwNonExstUeAddrPkts_Type()
)
jnxMbgPgwNonExstUeAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNonExstUeAddrPkts.setStatus("current")
_JnxMbgPgwSessEstDynPolAttempt_Type = Counter64
_JnxMbgPgwSessEstDynPolAttempt_Object = MibTableColumn
jnxMbgPgwSessEstDynPolAttempt = _JnxMbgPgwSessEstDynPolAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 22),
    _JnxMbgPgwSessEstDynPolAttempt_Type()
)
jnxMbgPgwSessEstDynPolAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSessEstDynPolAttempt.setStatus("current")
_JnxMbgPgwSuccSessEstDynPol_Type = Counter64
_JnxMbgPgwSuccSessEstDynPol_Object = MibTableColumn
jnxMbgPgwSuccSessEstDynPol = _JnxMbgPgwSuccSessEstDynPol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 23),
    _JnxMbgPgwSuccSessEstDynPol_Type()
)
jnxMbgPgwSuccSessEstDynPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccSessEstDynPol.setStatus("current")
_JnxMbgPgwDedBrActAttempt_Type = Counter64
_JnxMbgPgwDedBrActAttempt_Object = MibTableColumn
jnxMbgPgwDedBrActAttempt = _JnxMbgPgwDedBrActAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 24),
    _JnxMbgPgwDedBrActAttempt_Type()
)
jnxMbgPgwDedBrActAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDedBrActAttempt.setStatus("deprecated")
_JnxMbgPgwSuccDedBrAct_Type = Counter64
_JnxMbgPgwSuccDedBrAct_Object = MibTableColumn
jnxMbgPgwSuccDedBrAct = _JnxMbgPgwSuccDedBrAct_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 25),
    _JnxMbgPgwSuccDedBrAct_Type()
)
jnxMbgPgwSuccDedBrAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccDedBrAct.setStatus("deprecated")
_JnxMbgPgwMsInitDedBrDeact_Type = Counter64
_JnxMbgPgwMsInitDedBrDeact_Object = MibTableColumn
jnxMbgPgwMsInitDedBrDeact = _JnxMbgPgwMsInitDedBrDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 26),
    _JnxMbgPgwMsInitDedBrDeact_Type()
)
jnxMbgPgwMsInitDedBrDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwMsInitDedBrDeact.setStatus("current")
_JnxMbgPgwGwInitDedBrDeact_Type = Counter64
_JnxMbgPgwGwInitDedBrDeact_Object = MibTableColumn
jnxMbgPgwGwInitDedBrDeact = _JnxMbgPgwGwInitDedBrDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 27),
    _JnxMbgPgwGwInitDedBrDeact_Type()
)
jnxMbgPgwGwInitDedBrDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGwInitDedBrDeact.setStatus("current")
_JnxMbgPgwPcrfInitDedBrDeact_Type = Counter64
_JnxMbgPgwPcrfInitDedBrDeact_Object = MibTableColumn
jnxMbgPgwPcrfInitDedBrDeact = _JnxMbgPgwPcrfInitDedBrDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 28),
    _JnxMbgPgwPcrfInitDedBrDeact_Type()
)
jnxMbgPgwPcrfInitDedBrDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPcrfInitDedBrDeact.setStatus("current")
_JnxMbgPgwMsInitModAttempt_Type = Counter64
_JnxMbgPgwMsInitModAttempt_Object = MibTableColumn
jnxMbgPgwMsInitModAttempt = _JnxMbgPgwMsInitModAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 29),
    _JnxMbgPgwMsInitModAttempt_Type()
)
jnxMbgPgwMsInitModAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwMsInitModAttempt.setStatus("current")
_JnxMbgPgwSuccMsInitMod_Type = Counter64
_JnxMbgPgwSuccMsInitMod_Object = MibTableColumn
jnxMbgPgwSuccMsInitMod = _JnxMbgPgwSuccMsInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 30),
    _JnxMbgPgwSuccMsInitMod_Type()
)
jnxMbgPgwSuccMsInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccMsInitMod.setStatus("current")
_JnxMbgPgwGwInitModAttempt_Type = Counter64
_JnxMbgPgwGwInitModAttempt_Object = MibTableColumn
jnxMbgPgwGwInitModAttempt = _JnxMbgPgwGwInitModAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 31),
    _JnxMbgPgwGwInitModAttempt_Type()
)
jnxMbgPgwGwInitModAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGwInitModAttempt.setStatus("current")
_JnxMbgPgwSuccGwInitMod_Type = Counter64
_JnxMbgPgwSuccGwInitMod_Object = MibTableColumn
jnxMbgPgwSuccGwInitMod = _JnxMbgPgwSuccGwInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 32),
    _JnxMbgPgwSuccGwInitMod_Type()
)
jnxMbgPgwSuccGwInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccGwInitMod.setStatus("current")
_JnxMbgPgwMsInitDedBrActAttempt_Type = Counter64
_JnxMbgPgwMsInitDedBrActAttempt_Object = MibTableColumn
jnxMbgPgwMsInitDedBrActAttempt = _JnxMbgPgwMsInitDedBrActAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 33),
    _JnxMbgPgwMsInitDedBrActAttempt_Type()
)
jnxMbgPgwMsInitDedBrActAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwMsInitDedBrActAttempt.setStatus("current")
_JnxMbgPgwSuccMsInitDedBrAct_Type = Counter64
_JnxMbgPgwSuccMsInitDedBrAct_Object = MibTableColumn
jnxMbgPgwSuccMsInitDedBrAct = _JnxMbgPgwSuccMsInitDedBrAct_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 34),
    _JnxMbgPgwSuccMsInitDedBrAct_Type()
)
jnxMbgPgwSuccMsInitDedBrAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccMsInitDedBrAct.setStatus("current")
_JnxMbgPgwNwInitDedBrActAttempt_Type = Counter64
_JnxMbgPgwNwInitDedBrActAttempt_Object = MibTableColumn
jnxMbgPgwNwInitDedBrActAttempt = _JnxMbgPgwNwInitDedBrActAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 35),
    _JnxMbgPgwNwInitDedBrActAttempt_Type()
)
jnxMbgPgwNwInitDedBrActAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNwInitDedBrActAttempt.setStatus("current")
_JnxMbgPgwSuccNwInitDedBrAct_Type = Counter64
_JnxMbgPgwSuccNwInitDedBrAct_Object = MibTableColumn
jnxMbgPgwSuccNwInitDedBrAct = _JnxMbgPgwSuccNwInitDedBrAct_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 36),
    _JnxMbgPgwSuccNwInitDedBrAct_Type()
)
jnxMbgPgwSuccNwInitDedBrAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccNwInitDedBrAct.setStatus("current")
_JnxMbgPgwMsInitDedBrModAttempt_Type = Counter64
_JnxMbgPgwMsInitDedBrModAttempt_Object = MibTableColumn
jnxMbgPgwMsInitDedBrModAttempt = _JnxMbgPgwMsInitDedBrModAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 37),
    _JnxMbgPgwMsInitDedBrModAttempt_Type()
)
jnxMbgPgwMsInitDedBrModAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwMsInitDedBrModAttempt.setStatus("current")
_JnxMbgPgwSuccMsInitDedBrMod_Type = Counter64
_JnxMbgPgwSuccMsInitDedBrMod_Object = MibTableColumn
jnxMbgPgwSuccMsInitDedBrMod = _JnxMbgPgwSuccMsInitDedBrMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 38),
    _JnxMbgPgwSuccMsInitDedBrMod_Type()
)
jnxMbgPgwSuccMsInitDedBrMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccMsInitDedBrMod.setStatus("current")
_JnxMbgPgwNwInitDedBrModAttempt_Type = Counter64
_JnxMbgPgwNwInitDedBrModAttempt_Object = MibTableColumn
jnxMbgPgwNwInitDedBrModAttempt = _JnxMbgPgwNwInitDedBrModAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 39),
    _JnxMbgPgwNwInitDedBrModAttempt_Type()
)
jnxMbgPgwNwInitDedBrModAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNwInitDedBrModAttempt.setStatus("current")
_JnxMbgPgwSuccNwInitDedBrMod_Type = Counter64
_JnxMbgPgwSuccNwInitDedBrMod_Object = MibTableColumn
jnxMbgPgwSuccNwInitDedBrMod = _JnxMbgPgwSuccNwInitDedBrMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 40),
    _JnxMbgPgwSuccNwInitDedBrMod_Type()
)
jnxMbgPgwSuccNwInitDedBrMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuccNwInitDedBrMod.setStatus("current")
_JnxMbgPgwInterRatHoAttempt_Type = Counter64
_JnxMbgPgwInterRatHoAttempt_Object = MibTableColumn
jnxMbgPgwInterRatHoAttempt = _JnxMbgPgwInterRatHoAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 41),
    _JnxMbgPgwInterRatHoAttempt_Type()
)
jnxMbgPgwInterRatHoAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwInterRatHoAttempt.setStatus("current")
_JnxMbgPgwInterRatHoSucc_Type = Counter64
_JnxMbgPgwInterRatHoSucc_Object = MibTableColumn
jnxMbgPgwInterRatHoSucc = _JnxMbgPgwInterRatHoSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 42),
    _JnxMbgPgwInterRatHoSucc_Type()
)
jnxMbgPgwInterRatHoSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwInterRatHoSucc.setStatus("current")
_JnxMbgPgwIntraRatHoAttempt_Type = Counter64
_JnxMbgPgwIntraRatHoAttempt_Object = MibTableColumn
jnxMbgPgwIntraRatHoAttempt = _JnxMbgPgwIntraRatHoAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 43),
    _JnxMbgPgwIntraRatHoAttempt_Type()
)
jnxMbgPgwIntraRatHoAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIntraRatHoAttempt.setStatus("current")
_JnxMbgPgwIntraRatHoSucc_Type = Counter64
_JnxMbgPgwIntraRatHoSucc_Object = MibTableColumn
jnxMbgPgwIntraRatHoSucc = _JnxMbgPgwIntraRatHoSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 44),
    _JnxMbgPgwIntraRatHoSucc_Type()
)
jnxMbgPgwIntraRatHoSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIntraRatHoSucc.setStatus("current")
_JnxMbgPgwCdrsAllocd_Type = Counter64
_JnxMbgPgwCdrsAllocd_Object = MibTableColumn
jnxMbgPgwCdrsAllocd = _JnxMbgPgwCdrsAllocd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 45),
    _JnxMbgPgwCdrsAllocd_Type()
)
jnxMbgPgwCdrsAllocd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCdrsAllocd.setStatus("current")
_JnxMbgPgwPartialCdrsAllocd_Type = Counter64
_JnxMbgPgwPartialCdrsAllocd_Object = MibTableColumn
jnxMbgPgwPartialCdrsAllocd = _JnxMbgPgwPartialCdrsAllocd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 46),
    _JnxMbgPgwPartialCdrsAllocd_Type()
)
jnxMbgPgwPartialCdrsAllocd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPartialCdrsAllocd.setStatus("current")
_JnxMbgPgwCdrsClosed_Type = Counter64
_JnxMbgPgwCdrsClosed_Object = MibTableColumn
jnxMbgPgwCdrsClosed = _JnxMbgPgwCdrsClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 47),
    _JnxMbgPgwCdrsClosed_Type()
)
jnxMbgPgwCdrsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCdrsClosed.setStatus("current")
_JnxMbgPgwCdrCntainrsClosed_Type = Counter64
_JnxMbgPgwCdrCntainrsClosed_Object = MibTableColumn
jnxMbgPgwCdrCntainrsClosed = _JnxMbgPgwCdrCntainrsClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 48),
    _JnxMbgPgwCdrCntainrsClosed_Type()
)
jnxMbgPgwCdrCntainrsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCdrCntainrsClosed.setStatus("current")
_JnxMbgPgwGySessEstAttempt_Type = Counter64
_JnxMbgPgwGySessEstAttempt_Object = MibTableColumn
jnxMbgPgwGySessEstAttempt = _JnxMbgPgwGySessEstAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 49),
    _JnxMbgPgwGySessEstAttempt_Type()
)
jnxMbgPgwGySessEstAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGySessEstAttempt.setStatus("current")
_JnxMbgPgwGySuccSessEst_Type = Counter64
_JnxMbgPgwGySuccSessEst_Object = MibTableColumn
jnxMbgPgwGySuccSessEst = _JnxMbgPgwGySuccSessEst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 50),
    _JnxMbgPgwGySuccSessEst_Type()
)
jnxMbgPgwGySuccSessEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGySuccSessEst.setStatus("current")
_JnxMbgPgwGyReauthAttempt_Type = Counter64
_JnxMbgPgwGyReauthAttempt_Object = MibTableColumn
jnxMbgPgwGyReauthAttempt = _JnxMbgPgwGyReauthAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 51),
    _JnxMbgPgwGyReauthAttempt_Type()
)
jnxMbgPgwGyReauthAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGyReauthAttempt.setStatus("current")
_JnxMbgPgwGySuccReauth_Type = Counter64
_JnxMbgPgwGySuccReauth_Object = MibTableColumn
jnxMbgPgwGySuccReauth = _JnxMbgPgwGySuccReauth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 52),
    _JnxMbgPgwGySuccReauth_Type()
)
jnxMbgPgwGySuccReauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGySuccReauth.setStatus("current")
_JnxMbgPgwGyAuthTimeout_Type = Counter64
_JnxMbgPgwGyAuthTimeout_Object = MibTableColumn
jnxMbgPgwGyAuthTimeout = _JnxMbgPgwGyAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 53),
    _JnxMbgPgwGyAuthTimeout_Type()
)
jnxMbgPgwGyAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGyAuthTimeout.setStatus("current")
_JnxMbgPgwGyMsInitSessDeact_Type = Counter64
_JnxMbgPgwGyMsInitSessDeact_Object = MibTableColumn
jnxMbgPgwGyMsInitSessDeact = _JnxMbgPgwGyMsInitSessDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 54),
    _JnxMbgPgwGyMsInitSessDeact_Type()
)
jnxMbgPgwGyMsInitSessDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGyMsInitSessDeact.setStatus("current")
_JnxMbgPgwGyOcsInitSessDeact_Type = Counter64
_JnxMbgPgwGyOcsInitSessDeact_Object = MibTableColumn
jnxMbgPgwGyOcsInitSessDeact = _JnxMbgPgwGyOcsInitSessDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 55),
    _JnxMbgPgwGyOcsInitSessDeact_Type()
)
jnxMbgPgwGyOcsInitSessDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGyOcsInitSessDeact.setStatus("current")
_JnxMbgPgwGyGwInitSessDeact_Type = Counter64
_JnxMbgPgwGyGwInitSessDeact_Object = MibTableColumn
jnxMbgPgwGyGwInitSessDeact = _JnxMbgPgwGyGwInitSessDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 56),
    _JnxMbgPgwGyGwInitSessDeact_Type()
)
jnxMbgPgwGyGwInitSessDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGyGwInitSessDeact.setStatus("current")
_JnxMbgPgwGxMsInitMod_Type = Counter64
_JnxMbgPgwGxMsInitMod_Object = MibTableColumn
jnxMbgPgwGxMsInitMod = _JnxMbgPgwGxMsInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 57),
    _JnxMbgPgwGxMsInitMod_Type()
)
jnxMbgPgwGxMsInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGxMsInitMod.setStatus("current")
_JnxMbgPgwGxSuccMsInitMod_Type = Counter64
_JnxMbgPgwGxSuccMsInitMod_Object = MibTableColumn
jnxMbgPgwGxSuccMsInitMod = _JnxMbgPgwGxSuccMsInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 58),
    _JnxMbgPgwGxSuccMsInitMod_Type()
)
jnxMbgPgwGxSuccMsInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGxSuccMsInitMod.setStatus("current")
_JnxMbgPgwGxPcrfInitMod_Type = Counter64
_JnxMbgPgwGxPcrfInitMod_Object = MibTableColumn
jnxMbgPgwGxPcrfInitMod = _JnxMbgPgwGxPcrfInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 59),
    _JnxMbgPgwGxPcrfInitMod_Type()
)
jnxMbgPgwGxPcrfInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGxPcrfInitMod.setStatus("current")
_JnxMbgPgwGxSuccPcrfInitMod_Type = Counter64
_JnxMbgPgwGxSuccPcrfInitMod_Object = MibTableColumn
jnxMbgPgwGxSuccPcrfInitMod = _JnxMbgPgwGxSuccPcrfInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 60),
    _JnxMbgPgwGxSuccPcrfInitMod_Type()
)
jnxMbgPgwGxSuccPcrfInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGxSuccPcrfInitMod.setStatus("current")
_JnxMbgPgwGxMsInitSessTerm_Type = Counter64
_JnxMbgPgwGxMsInitSessTerm_Object = MibTableColumn
jnxMbgPgwGxMsInitSessTerm = _JnxMbgPgwGxMsInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 61),
    _JnxMbgPgwGxMsInitSessTerm_Type()
)
jnxMbgPgwGxMsInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGxMsInitSessTerm.setStatus("current")
_JnxMbgPgwGxPcrfInitSessTerm_Type = Counter64
_JnxMbgPgwGxPcrfInitSessTerm_Object = MibTableColumn
jnxMbgPgwGxPcrfInitSessTerm = _JnxMbgPgwGxPcrfInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 62),
    _JnxMbgPgwGxPcrfInitSessTerm_Type()
)
jnxMbgPgwGxPcrfInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGxPcrfInitSessTerm.setStatus("current")
_JnxMbgPgwGxGwInitSessTerm_Type = Counter64
_JnxMbgPgwGxGwInitSessTerm_Object = MibTableColumn
jnxMbgPgwGxGwInitSessTerm = _JnxMbgPgwGxGwInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 4, 1, 63),
    _JnxMbgPgwGxGwInitSessTerm_Type()
)
jnxMbgPgwGxGwInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGxGwInitSessTerm.setStatus("current")
_JnxMbgPgwSMStatusTable_Object = MibTable
jnxMbgPgwSMStatusTable = _JnxMbgPgwSMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMStatusTable.setStatus("current")
_JnxMbgPgwSMStatusEntry_Object = MibTableRow
jnxMbgPgwSMStatusEntry = _JnxMbgPgwSMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1)
)
jnxMbgPgwSMStatusEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMStatusEntry.setStatus("current")
_JnxMbgPgwActvSubscribers_Type = CounterBasedGauge64
_JnxMbgPgwActvSubscribers_Object = MibTableColumn
jnxMbgPgwActvSubscribers = _JnxMbgPgwActvSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 1),
    _JnxMbgPgwActvSubscribers_Type()
)
jnxMbgPgwActvSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActvSubscribers.setStatus("current")
_JnxMbgPgwActvSessions_Type = CounterBasedGauge64
_JnxMbgPgwActvSessions_Object = MibTableColumn
jnxMbgPgwActvSessions = _JnxMbgPgwActvSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 2),
    _JnxMbgPgwActvSessions_Type()
)
jnxMbgPgwActvSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActvSessions.setStatus("current")
_JnxMbgPgwActvBearers_Type = CounterBasedGauge64
_JnxMbgPgwActvBearers_Object = MibTableColumn
jnxMbgPgwActvBearers = _JnxMbgPgwActvBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 3),
    _JnxMbgPgwActvBearers_Type()
)
jnxMbgPgwActvBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActvBearers.setStatus("current")
_JnxMbgPgwIdleSubscribers_Type = CounterBasedGauge64
_JnxMbgPgwIdleSubscribers_Object = MibTableColumn
jnxMbgPgwIdleSubscribers = _JnxMbgPgwIdleSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 4),
    _JnxMbgPgwIdleSubscribers_Type()
)
jnxMbgPgwIdleSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIdleSubscribers.setStatus("deprecated")
_JnxMbgPgwIdleSessions_Type = CounterBasedGauge64
_JnxMbgPgwIdleSessions_Object = MibTableColumn
jnxMbgPgwIdleSessions = _JnxMbgPgwIdleSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 5),
    _JnxMbgPgwIdleSessions_Type()
)
jnxMbgPgwIdleSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIdleSessions.setStatus("deprecated")
_JnxMbgPgwIdleBearers_Type = CounterBasedGauge64
_JnxMbgPgwIdleBearers_Object = MibTableColumn
jnxMbgPgwIdleBearers = _JnxMbgPgwIdleBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 6),
    _JnxMbgPgwIdleBearers_Type()
)
jnxMbgPgwIdleBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIdleBearers.setStatus("deprecated")
_JnxMbgPgwSuspSubscribers_Type = CounterBasedGauge64
_JnxMbgPgwSuspSubscribers_Object = MibTableColumn
jnxMbgPgwSuspSubscribers = _JnxMbgPgwSuspSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 7),
    _JnxMbgPgwSuspSubscribers_Type()
)
jnxMbgPgwSuspSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuspSubscribers.setStatus("deprecated")
_JnxMbgPgwSuspSessions_Type = CounterBasedGauge64
_JnxMbgPgwSuspSessions_Object = MibTableColumn
jnxMbgPgwSuspSessions = _JnxMbgPgwSuspSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 8),
    _JnxMbgPgwSuspSessions_Type()
)
jnxMbgPgwSuspSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuspSessions.setStatus("deprecated")
_JnxMbgPgwSuspBearers_Type = CounterBasedGauge64
_JnxMbgPgwSuspBearers_Object = MibTableColumn
jnxMbgPgwSuspBearers = _JnxMbgPgwSuspBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 9),
    _JnxMbgPgwSuspBearers_Type()
)
jnxMbgPgwSuspBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuspBearers.setStatus("deprecated")
_JnxMbgPgwCPUUtil_Type = Gauge32
_JnxMbgPgwCPUUtil_Object = MibTableColumn
jnxMbgPgwCPUUtil = _JnxMbgPgwCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 10),
    _JnxMbgPgwCPUUtil_Type()
)
jnxMbgPgwCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCPUUtil.setStatus("current")
_JnxMbgPgwMemoryUtil_Type = Gauge32
_JnxMbgPgwMemoryUtil_Object = MibTableColumn
jnxMbgPgwMemoryUtil = _JnxMbgPgwMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 11),
    _JnxMbgPgwMemoryUtil_Type()
)
jnxMbgPgwMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwMemoryUtil.setStatus("current")
_JnxMbgPgwActvPrepaidBearers_Type = CounterBasedGauge64
_JnxMbgPgwActvPrepaidBearers_Object = MibTableColumn
jnxMbgPgwActvPrepaidBearers = _JnxMbgPgwActvPrepaidBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 12),
    _JnxMbgPgwActvPrepaidBearers_Type()
)
jnxMbgPgwActvPrepaidBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActvPrepaidBearers.setStatus("current")
_JnxMbgPgwActvPostpaidBearers_Type = CounterBasedGauge64
_JnxMbgPgwActvPostpaidBearers_Object = MibTableColumn
jnxMbgPgwActvPostpaidBearers = _JnxMbgPgwActvPostpaidBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 13),
    _JnxMbgPgwActvPostpaidBearers_Type()
)
jnxMbgPgwActvPostpaidBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActvPostpaidBearers.setStatus("current")
_JnxMbgPgwActvGbrBearers_Type = CounterBasedGauge64
_JnxMbgPgwActvGbrBearers_Object = MibTableColumn
jnxMbgPgwActvGbrBearers = _JnxMbgPgwActvGbrBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 14),
    _JnxMbgPgwActvGbrBearers_Type()
)
jnxMbgPgwActvGbrBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActvGbrBearers.setStatus("current")
_JnxMbgPgwActvNonGbrBearers_Type = CounterBasedGauge64
_JnxMbgPgwActvNonGbrBearers_Object = MibTableColumn
jnxMbgPgwActvNonGbrBearers = _JnxMbgPgwActvNonGbrBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 5, 1, 15),
    _JnxMbgPgwActvNonGbrBearers_Type()
)
jnxMbgPgwActvNonGbrBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwActvNonGbrBearers.setStatus("current")
_JnxMbgPgwApnSMStatsTable_Object = MibTable
jnxMbgPgwApnSMStatsTable = _JnxMbgPgwApnSMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxMbgPgwApnSMStatsTable.setStatus("current")
_JnxMbgPgwApnSMStatsEntry_Object = MibTableRow
jnxMbgPgwApnSMStatsEntry = _JnxMbgPgwApnSMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1)
)
jnxMbgPgwApnSMStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwApnName"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwApnSMStatsEntry.setStatus("current")
_JnxMbgPgwApnName_Type = DisplayString
_JnxMbgPgwApnName_Object = MibTableColumn
jnxMbgPgwApnName = _JnxMbgPgwApnName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 1),
    _JnxMbgPgwApnName_Type()
)
jnxMbgPgwApnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwApnName.setStatus("current")
_JnxMbgPgwApnSessnEstAttmpts_Type = Counter64
_JnxMbgPgwApnSessnEstAttmpts_Object = MibTableColumn
jnxMbgPgwApnSessnEstAttmpts = _JnxMbgPgwApnSessnEstAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 2),
    _JnxMbgPgwApnSessnEstAttmpts_Type()
)
jnxMbgPgwApnSessnEstAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnEstAttmpts.setStatus("current")
_JnxMbgPgwApnSuccSessnEst_Type = Counter64
_JnxMbgPgwApnSuccSessnEst_Object = MibTableColumn
jnxMbgPgwApnSuccSessnEst = _JnxMbgPgwApnSuccSessnEst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 3),
    _JnxMbgPgwApnSuccSessnEst_Type()
)
jnxMbgPgwApnSuccSessnEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccSessnEst.setStatus("current")
_JnxMbgPgwApnPeerInitDeactv_Type = Counter64
_JnxMbgPgwApnPeerInitDeactv_Object = MibTableColumn
jnxMbgPgwApnPeerInitDeactv = _JnxMbgPgwApnPeerInitDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 4),
    _JnxMbgPgwApnPeerInitDeactv_Type()
)
jnxMbgPgwApnPeerInitDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPeerInitDeactv.setStatus("current")
_JnxMbgPgwApnPeerInitSuccDeactv_Type = Counter64
_JnxMbgPgwApnPeerInitSuccDeactv_Object = MibTableColumn
jnxMbgPgwApnPeerInitSuccDeactv = _JnxMbgPgwApnPeerInitSuccDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 5),
    _JnxMbgPgwApnPeerInitSuccDeactv_Type()
)
jnxMbgPgwApnPeerInitSuccDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPeerInitSuccDeactv.setStatus("current")
_JnxMbgPgwApnGwInitDeactv_Type = Counter64
_JnxMbgPgwApnGwInitDeactv_Object = MibTableColumn
jnxMbgPgwApnGwInitDeactv = _JnxMbgPgwApnGwInitDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 6),
    _JnxMbgPgwApnGwInitDeactv_Type()
)
jnxMbgPgwApnGwInitDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGwInitDeactv.setStatus("current")
_JnxMbgPgwApnGwInitSuccDeactv_Type = Counter64
_JnxMbgPgwApnGwInitSuccDeactv_Object = MibTableColumn
jnxMbgPgwApnGwInitSuccDeactv = _JnxMbgPgwApnGwInitSuccDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 7),
    _JnxMbgPgwApnGwInitSuccDeactv_Type()
)
jnxMbgPgwApnGwInitSuccDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGwInitSuccDeactv.setStatus("current")
_JnxMbgPgwApnGtpStatsGnS5S8InpPkt_Type = Counter64
_JnxMbgPgwApnGtpStatsGnS5S8InpPkt_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGnS5S8InpPkt = _JnxMbgPgwApnGtpStatsGnS5S8InpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 8),
    _JnxMbgPgwApnGtpStatsGnS5S8InpPkt_Type()
)
jnxMbgPgwApnGtpStatsGnS5S8InpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGnS5S8InpPkt.setStatus("current")
_JnxMbgPgwApnGtpStatsGnS5S8InpByt_Type = Counter64
_JnxMbgPgwApnGtpStatsGnS5S8InpByt_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGnS5S8InpByt = _JnxMbgPgwApnGtpStatsGnS5S8InpByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 9),
    _JnxMbgPgwApnGtpStatsGnS5S8InpByt_Type()
)
jnxMbgPgwApnGtpStatsGnS5S8InpByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGnS5S8InpByt.setStatus("current")
_JnxMbgPgwApnGtpStatsGnS5S8OutPkt_Type = Counter64
_JnxMbgPgwApnGtpStatsGnS5S8OutPkt_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGnS5S8OutPkt = _JnxMbgPgwApnGtpStatsGnS5S8OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 10),
    _JnxMbgPgwApnGtpStatsGnS5S8OutPkt_Type()
)
jnxMbgPgwApnGtpStatsGnS5S8OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGnS5S8OutPkt.setStatus("current")
_JnxMbgPgwApnGtpStatsGnS5S8OutByt_Type = Counter64
_JnxMbgPgwApnGtpStatsGnS5S8OutByt_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGnS5S8OutByt = _JnxMbgPgwApnGtpStatsGnS5S8OutByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 11),
    _JnxMbgPgwApnGtpStatsGnS5S8OutByt_Type()
)
jnxMbgPgwApnGtpStatsGnS5S8OutByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGnS5S8OutByt.setStatus("current")
_JnxMbgPgwApnGtpStatsGiInpPkt_Type = Counter64
_JnxMbgPgwApnGtpStatsGiInpPkt_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGiInpPkt = _JnxMbgPgwApnGtpStatsGiInpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 12),
    _JnxMbgPgwApnGtpStatsGiInpPkt_Type()
)
jnxMbgPgwApnGtpStatsGiInpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGiInpPkt.setStatus("current")
_JnxMbgPgwApnGtpStatsGiInpByt_Type = Counter64
_JnxMbgPgwApnGtpStatsGiInpByt_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGiInpByt = _JnxMbgPgwApnGtpStatsGiInpByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 13),
    _JnxMbgPgwApnGtpStatsGiInpByt_Type()
)
jnxMbgPgwApnGtpStatsGiInpByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGiInpByt.setStatus("current")
_JnxMbgPgwApnGtpStatsGiOutPkt_Type = Counter64
_JnxMbgPgwApnGtpStatsGiOutPkt_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGiOutPkt = _JnxMbgPgwApnGtpStatsGiOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 14),
    _JnxMbgPgwApnGtpStatsGiOutPkt_Type()
)
jnxMbgPgwApnGtpStatsGiOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGiOutPkt.setStatus("current")
_JnxMbgPgwApnGtpStatsGiOutByt_Type = Counter64
_JnxMbgPgwApnGtpStatsGiOutByt_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGiOutByt = _JnxMbgPgwApnGtpStatsGiOutByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 15),
    _JnxMbgPgwApnGtpStatsGiOutByt_Type()
)
jnxMbgPgwApnGtpStatsGiOutByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGiOutByt.setStatus("current")
_JnxMbgPgwApnSessnFailSrvcUnaval_Type = Counter64
_JnxMbgPgwApnSessnFailSrvcUnaval_Object = MibTableColumn
jnxMbgPgwApnSessnFailSrvcUnaval = _JnxMbgPgwApnSessnFailSrvcUnaval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 16),
    _JnxMbgPgwApnSessnFailSrvcUnaval_Type()
)
jnxMbgPgwApnSessnFailSrvcUnaval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailSrvcUnaval.setStatus("current")
_JnxMbgPgwApnSessnFailSysFailure_Type = Counter64
_JnxMbgPgwApnSessnFailSysFailure_Object = MibTableColumn
jnxMbgPgwApnSessnFailSysFailure = _JnxMbgPgwApnSessnFailSysFailure_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 17),
    _JnxMbgPgwApnSessnFailSysFailure_Type()
)
jnxMbgPgwApnSessnFailSysFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailSysFailure.setStatus("current")
_JnxMbgPgwApnSessnFailNoResource_Type = Counter64
_JnxMbgPgwApnSessnFailNoResource_Object = MibTableColumn
jnxMbgPgwApnSessnFailNoResource = _JnxMbgPgwApnSessnFailNoResource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 18),
    _JnxMbgPgwApnSessnFailNoResource_Type()
)
jnxMbgPgwApnSessnFailNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailNoResource.setStatus("current")
_JnxMbgPgwApnSessnFailNoAddr_Type = Counter64
_JnxMbgPgwApnSessnFailNoAddr_Object = MibTableColumn
jnxMbgPgwApnSessnFailNoAddr = _JnxMbgPgwApnSessnFailNoAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 19),
    _JnxMbgPgwApnSessnFailNoAddr_Type()
)
jnxMbgPgwApnSessnFailNoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailNoAddr.setStatus("current")
_JnxMbgPgwApnSessnFailSrvcDenied_Type = Counter64
_JnxMbgPgwApnSessnFailSrvcDenied_Object = MibTableColumn
jnxMbgPgwApnSessnFailSrvcDenied = _JnxMbgPgwApnSessnFailSrvcDenied_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 20),
    _JnxMbgPgwApnSessnFailSrvcDenied_Type()
)
jnxMbgPgwApnSessnFailSrvcDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailSrvcDenied.setStatus("current")
_JnxMbgPgwApnSessnFailAuthFailed_Type = Counter64
_JnxMbgPgwApnSessnFailAuthFailed_Object = MibTableColumn
jnxMbgPgwApnSessnFailAuthFailed = _JnxMbgPgwApnSessnFailAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 21),
    _JnxMbgPgwApnSessnFailAuthFailed_Type()
)
jnxMbgPgwApnSessnFailAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailAuthFailed.setStatus("current")
_JnxMbgPgwApnSessnFailAccsDenied_Type = Counter64
_JnxMbgPgwApnSessnFailAccsDenied_Object = MibTableColumn
jnxMbgPgwApnSessnFailAccsDenied = _JnxMbgPgwApnSessnFailAccsDenied_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 22),
    _JnxMbgPgwApnSessnFailAccsDenied_Type()
)
jnxMbgPgwApnSessnFailAccsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailAccsDenied.setStatus("current")
_JnxMbgPgwApnMSInitModAttmpts_Type = Counter64
_JnxMbgPgwApnMSInitModAttmpts_Object = MibTableColumn
jnxMbgPgwApnMSInitModAttmpts = _JnxMbgPgwApnMSInitModAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 23),
    _JnxMbgPgwApnMSInitModAttmpts_Type()
)
jnxMbgPgwApnMSInitModAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMSInitModAttmpts.setStatus("current")
_JnxMbgPgwApnSuccMSInitMod_Type = Counter64
_JnxMbgPgwApnSuccMSInitMod_Object = MibTableColumn
jnxMbgPgwApnSuccMSInitMod = _JnxMbgPgwApnSuccMSInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 24),
    _JnxMbgPgwApnSuccMSInitMod_Type()
)
jnxMbgPgwApnSuccMSInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccMSInitMod.setStatus("current")
_JnxMbgPgwApnPgwGgsnInitMod_Type = Counter64
_JnxMbgPgwApnPgwGgsnInitMod_Object = MibTableColumn
jnxMbgPgwApnPgwGgsnInitMod = _JnxMbgPgwApnPgwGgsnInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 25),
    _JnxMbgPgwApnPgwGgsnInitMod_Type()
)
jnxMbgPgwApnPgwGgsnInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPgwGgsnInitMod.setStatus("current")
_JnxMbgPgwApnSuccPgwGgsnInitMod_Type = Counter64
_JnxMbgPgwApnSuccPgwGgsnInitMod_Object = MibTableColumn
jnxMbgPgwApnSuccPgwGgsnInitMod = _JnxMbgPgwApnSuccPgwGgsnInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 26),
    _JnxMbgPgwApnSuccPgwGgsnInitMod_Type()
)
jnxMbgPgwApnSuccPgwGgsnInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccPgwGgsnInitMod.setStatus("current")
_JnxMbgPgwApnUsrAuthAttmpts_Type = Counter64
_JnxMbgPgwApnUsrAuthAttmpts_Object = MibTableColumn
jnxMbgPgwApnUsrAuthAttmpts = _JnxMbgPgwApnUsrAuthAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 27),
    _JnxMbgPgwApnUsrAuthAttmpts_Type()
)
jnxMbgPgwApnUsrAuthAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnUsrAuthAttmpts.setStatus("current")
_JnxMbgPgwApnSuccUsrAuth_Type = Counter64
_JnxMbgPgwApnSuccUsrAuth_Object = MibTableColumn
jnxMbgPgwApnSuccUsrAuth = _JnxMbgPgwApnSuccUsrAuth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 28),
    _JnxMbgPgwApnSuccUsrAuth_Type()
)
jnxMbgPgwApnSuccUsrAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccUsrAuth.setStatus("current")
_JnxMbgPgwApnFailUsrAuth_Type = Counter64
_JnxMbgPgwApnFailUsrAuth_Object = MibTableColumn
jnxMbgPgwApnFailUsrAuth = _JnxMbgPgwApnFailUsrAuth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 29),
    _JnxMbgPgwApnFailUsrAuth_Type()
)
jnxMbgPgwApnFailUsrAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnFailUsrAuth.setStatus("current")
_JnxMbgPgwApnDynIPAllocAttmpts_Type = Counter64
_JnxMbgPgwApnDynIPAllocAttmpts_Object = MibTableColumn
jnxMbgPgwApnDynIPAllocAttmpts = _JnxMbgPgwApnDynIPAllocAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 30),
    _JnxMbgPgwApnDynIPAllocAttmpts_Type()
)
jnxMbgPgwApnDynIPAllocAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnDynIPAllocAttmpts.setStatus("current")
_JnxMbgPgwApnSuccDynIPAlloc_Type = Counter64
_JnxMbgPgwApnSuccDynIPAlloc_Object = MibTableColumn
jnxMbgPgwApnSuccDynIPAlloc = _JnxMbgPgwApnSuccDynIPAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 31),
    _JnxMbgPgwApnSuccDynIPAlloc_Type()
)
jnxMbgPgwApnSuccDynIPAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccDynIPAlloc.setStatus("current")
_JnxMbgPgwApnCdrsAllocd_Type = Counter64
_JnxMbgPgwApnCdrsAllocd_Object = MibTableColumn
jnxMbgPgwApnCdrsAllocd = _JnxMbgPgwApnCdrsAllocd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 32),
    _JnxMbgPgwApnCdrsAllocd_Type()
)
jnxMbgPgwApnCdrsAllocd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCdrsAllocd.setStatus("current")
_JnxMbgPgwApnPartialCdrsAllocd_Type = Counter64
_JnxMbgPgwApnPartialCdrsAllocd_Object = MibTableColumn
jnxMbgPgwApnPartialCdrsAllocd = _JnxMbgPgwApnPartialCdrsAllocd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 33),
    _JnxMbgPgwApnPartialCdrsAllocd_Type()
)
jnxMbgPgwApnPartialCdrsAllocd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPartialCdrsAllocd.setStatus("current")
_JnxMbgPgwApnCdrsClosed_Type = Counter64
_JnxMbgPgwApnCdrsClosed_Object = MibTableColumn
jnxMbgPgwApnCdrsClosed = _JnxMbgPgwApnCdrsClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 34),
    _JnxMbgPgwApnCdrsClosed_Type()
)
jnxMbgPgwApnCdrsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCdrsClosed.setStatus("current")
_JnxMbgPgwApnCdrCntainrsClosed_Type = Counter64
_JnxMbgPgwApnCdrCntainrsClosed_Object = MibTableColumn
jnxMbgPgwApnCdrCntainrsClosed = _JnxMbgPgwApnCdrCntainrsClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 35),
    _JnxMbgPgwApnCdrCntainrsClosed_Type()
)
jnxMbgPgwApnCdrCntainrsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCdrCntainrsClosed.setStatus("current")
_JnxMbgPgwApnPktsViolMIFAcl_Type = Counter64
_JnxMbgPgwApnPktsViolMIFAcl_Object = MibTableColumn
jnxMbgPgwApnPktsViolMIFAcl = _JnxMbgPgwApnPktsViolMIFAcl_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 36),
    _JnxMbgPgwApnPktsViolMIFAcl_Type()
)
jnxMbgPgwApnPktsViolMIFAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPktsViolMIFAcl.setStatus("current")
_JnxMbgPgwApnReDrctMblToMblPkts_Type = Counter64
_JnxMbgPgwApnReDrctMblToMblPkts_Object = MibTableColumn
jnxMbgPgwApnReDrctMblToMblPkts = _JnxMbgPgwApnReDrctMblToMblPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 37),
    _JnxMbgPgwApnReDrctMblToMblPkts_Type()
)
jnxMbgPgwApnReDrctMblToMblPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnReDrctMblToMblPkts.setStatus("current")
_JnxMbgPgwApnReDrctMblToMblByts_Type = Counter64
_JnxMbgPgwApnReDrctMblToMblByts_Object = MibTableColumn
jnxMbgPgwApnReDrctMblToMblByts = _JnxMbgPgwApnReDrctMblToMblByts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 38),
    _JnxMbgPgwApnReDrctMblToMblByts_Type()
)
jnxMbgPgwApnReDrctMblToMblByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnReDrctMblToMblByts.setStatus("current")
_JnxMbgPgwApnIpv6RsRcvd_Type = Counter64
_JnxMbgPgwApnIpv6RsRcvd_Object = MibTableColumn
jnxMbgPgwApnIpv6RsRcvd = _JnxMbgPgwApnIpv6RsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 39),
    _JnxMbgPgwApnIpv6RsRcvd_Type()
)
jnxMbgPgwApnIpv6RsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnIpv6RsRcvd.setStatus("current")
_JnxMbgPgwApnIpv6RaTxd_Type = Counter64
_JnxMbgPgwApnIpv6RaTxd_Object = MibTableColumn
jnxMbgPgwApnIpv6RaTxd = _JnxMbgPgwApnIpv6RaTxd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 40),
    _JnxMbgPgwApnIpv6RaTxd_Type()
)
jnxMbgPgwApnIpv6RaTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnIpv6RaTxd.setStatus("current")
_JnxMbgPgwApnIpv6NsRcvd_Type = Counter64
_JnxMbgPgwApnIpv6NsRcvd_Object = MibTableColumn
jnxMbgPgwApnIpv6NsRcvd = _JnxMbgPgwApnIpv6NsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 41),
    _JnxMbgPgwApnIpv6NsRcvd_Type()
)
jnxMbgPgwApnIpv6NsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnIpv6NsRcvd.setStatus("current")
_JnxMbgPgwApnIpv6NaTxd_Type = Counter64
_JnxMbgPgwApnIpv6NaTxd_Object = MibTableColumn
jnxMbgPgwApnIpv6NaTxd = _JnxMbgPgwApnIpv6NaTxd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 42),
    _JnxMbgPgwApnIpv6NaTxd_Type()
)
jnxMbgPgwApnIpv6NaTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnIpv6NaTxd.setStatus("current")
_JnxMbgPgwApnSessnFailOther_Type = Counter64
_JnxMbgPgwApnSessnFailOther_Object = MibTableColumn
jnxMbgPgwApnSessnFailOther = _JnxMbgPgwApnSessnFailOther_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 43),
    _JnxMbgPgwApnSessnFailOther_Type()
)
jnxMbgPgwApnSessnFailOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailOther.setStatus("current")
_JnxMbgPgwApnGtpStatsS58DscrdPkts_Type = Counter64
_JnxMbgPgwApnGtpStatsS58DscrdPkts_Object = MibTableColumn
jnxMbgPgwApnGtpStatsS58DscrdPkts = _JnxMbgPgwApnGtpStatsS58DscrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 44),
    _JnxMbgPgwApnGtpStatsS58DscrdPkts_Type()
)
jnxMbgPgwApnGtpStatsS58DscrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsS58DscrdPkts.setStatus("current")
_JnxMbgPgwApnGtpStatsGiDiscrdPkts_Type = Counter64
_JnxMbgPgwApnGtpStatsGiDiscrdPkts_Object = MibTableColumn
jnxMbgPgwApnGtpStatsGiDiscrdPkts = _JnxMbgPgwApnGtpStatsGiDiscrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 45),
    _JnxMbgPgwApnGtpStatsGiDiscrdPkts_Type()
)
jnxMbgPgwApnGtpStatsGiDiscrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGtpStatsGiDiscrdPkts.setStatus("current")
_JnxMbgPgwApnSessEstDynPolAttempt_Type = Counter64
_JnxMbgPgwApnSessEstDynPolAttempt_Object = MibTableColumn
jnxMbgPgwApnSessEstDynPolAttempt = _JnxMbgPgwApnSessEstDynPolAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 46),
    _JnxMbgPgwApnSessEstDynPolAttempt_Type()
)
jnxMbgPgwApnSessEstDynPolAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessEstDynPolAttempt.setStatus("current")
_JnxMbgPgwApnSuccSessEstDynPol_Type = Counter64
_JnxMbgPgwApnSuccSessEstDynPol_Object = MibTableColumn
jnxMbgPgwApnSuccSessEstDynPol = _JnxMbgPgwApnSuccSessEstDynPol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 47),
    _JnxMbgPgwApnSuccSessEstDynPol_Type()
)
jnxMbgPgwApnSuccSessEstDynPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccSessEstDynPol.setStatus("current")
_JnxMbgPgwApnSessEstStaPolAttempt_Type = Counter64
_JnxMbgPgwApnSessEstStaPolAttempt_Object = MibTableColumn
jnxMbgPgwApnSessEstStaPolAttempt = _JnxMbgPgwApnSessEstStaPolAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 48),
    _JnxMbgPgwApnSessEstStaPolAttempt_Type()
)
jnxMbgPgwApnSessEstStaPolAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessEstStaPolAttempt.setStatus("deprecated")
_JnxMbgPgwApnSuccSessEstStaPol_Type = Counter64
_JnxMbgPgwApnSuccSessEstStaPol_Object = MibTableColumn
jnxMbgPgwApnSuccSessEstStaPol = _JnxMbgPgwApnSuccSessEstStaPol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 49),
    _JnxMbgPgwApnSuccSessEstStaPol_Type()
)
jnxMbgPgwApnSuccSessEstStaPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccSessEstStaPol.setStatus("deprecated")
_JnxMbgPgwApnMsInitAmbrModReq_Type = Counter64
_JnxMbgPgwApnMsInitAmbrModReq_Object = MibTableColumn
jnxMbgPgwApnMsInitAmbrModReq = _JnxMbgPgwApnMsInitAmbrModReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 50),
    _JnxMbgPgwApnMsInitAmbrModReq_Type()
)
jnxMbgPgwApnMsInitAmbrModReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsInitAmbrModReq.setStatus("deprecated")
_JnxMbgPgwApnMsInitAmbrModSucc_Type = Counter64
_JnxMbgPgwApnMsInitAmbrModSucc_Object = MibTableColumn
jnxMbgPgwApnMsInitAmbrModSucc = _JnxMbgPgwApnMsInitAmbrModSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 51),
    _JnxMbgPgwApnMsInitAmbrModSucc_Type()
)
jnxMbgPgwApnMsInitAmbrModSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsInitAmbrModSucc.setStatus("deprecated")
_JnxMbgPgwApnMsInitQoSModReq_Type = Counter64
_JnxMbgPgwApnMsInitQoSModReq_Object = MibTableColumn
jnxMbgPgwApnMsInitQoSModReq = _JnxMbgPgwApnMsInitQoSModReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 52),
    _JnxMbgPgwApnMsInitQoSModReq_Type()
)
jnxMbgPgwApnMsInitQoSModReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsInitQoSModReq.setStatus("deprecated")
_JnxMbgPgwApnMsInitQoSModSucc_Type = Counter64
_JnxMbgPgwApnMsInitQoSModSucc_Object = MibTableColumn
jnxMbgPgwApnMsInitQoSModSucc = _JnxMbgPgwApnMsInitQoSModSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 53),
    _JnxMbgPgwApnMsInitQoSModSucc_Type()
)
jnxMbgPgwApnMsInitQoSModSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsInitQoSModSucc.setStatus("deprecated")
_JnxMbgPgwApnPcrfInitSessTerm_Type = Counter64
_JnxMbgPgwApnPcrfInitSessTerm_Object = MibTableColumn
jnxMbgPgwApnPcrfInitSessTerm = _JnxMbgPgwApnPcrfInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 54),
    _JnxMbgPgwApnPcrfInitSessTerm_Type()
)
jnxMbgPgwApnPcrfInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPcrfInitSessTerm.setStatus("deprecated")
_JnxMbgPgwApnGwInitSessTerm_Type = Counter64
_JnxMbgPgwApnGwInitSessTerm_Object = MibTableColumn
jnxMbgPgwApnGwInitSessTerm = _JnxMbgPgwApnGwInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 55),
    _JnxMbgPgwApnGwInitSessTerm_Type()
)
jnxMbgPgwApnGwInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGwInitSessTerm.setStatus("deprecated")
_JnxMbgPgwApnMsInitSessTerm_Type = Counter64
_JnxMbgPgwApnMsInitSessTerm_Object = MibTableColumn
jnxMbgPgwApnMsInitSessTerm = _JnxMbgPgwApnMsInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 56),
    _JnxMbgPgwApnMsInitSessTerm_Type()
)
jnxMbgPgwApnMsInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsInitSessTerm.setStatus("deprecated")
_JnxMbgPgwApnMsInitSessModTrgr_Type = Counter64
_JnxMbgPgwApnMsInitSessModTrgr_Object = MibTableColumn
jnxMbgPgwApnMsInitSessModTrgr = _JnxMbgPgwApnMsInitSessModTrgr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 57),
    _JnxMbgPgwApnMsInitSessModTrgr_Type()
)
jnxMbgPgwApnMsInitSessModTrgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsInitSessModTrgr.setStatus("deprecated")
_JnxMbgPgwApnMsInitSessModSucc_Type = Counter64
_JnxMbgPgwApnMsInitSessModSucc_Object = MibTableColumn
jnxMbgPgwApnMsInitSessModSucc = _JnxMbgPgwApnMsInitSessModSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 58),
    _JnxMbgPgwApnMsInitSessModSucc_Type()
)
jnxMbgPgwApnMsInitSessModSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsInitSessModSucc.setStatus("deprecated")
_JnxMbgPgwApnPcrfInitSessModTrgr_Type = Counter64
_JnxMbgPgwApnPcrfInitSessModTrgr_Object = MibTableColumn
jnxMbgPgwApnPcrfInitSessModTrgr = _JnxMbgPgwApnPcrfInitSessModTrgr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 59),
    _JnxMbgPgwApnPcrfInitSessModTrgr_Type()
)
jnxMbgPgwApnPcrfInitSessModTrgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPcrfInitSessModTrgr.setStatus("deprecated")
_JnxMbgPgwApnPcrfInitSessModSucc_Type = Counter64
_JnxMbgPgwApnPcrfInitSessModSucc_Object = MibTableColumn
jnxMbgPgwApnPcrfInitSessModSucc = _JnxMbgPgwApnPcrfInitSessModSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 60),
    _JnxMbgPgwApnPcrfInitSessModSucc_Type()
)
jnxMbgPgwApnPcrfInitSessModSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPcrfInitSessModSucc.setStatus("deprecated")
_JnxMbgPgwApnSessModTrgrQoSChg_Type = Counter64
_JnxMbgPgwApnSessModTrgrQoSChg_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrQoSChg = _JnxMbgPgwApnSessModTrgrQoSChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 61),
    _JnxMbgPgwApnSessModTrgrQoSChg_Type()
)
jnxMbgPgwApnSessModTrgrQoSChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrQoSChg.setStatus("current")
_JnxMbgPgwApnSessModTrgrRatChg_Type = Counter64
_JnxMbgPgwApnSessModTrgrRatChg_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrRatChg = _JnxMbgPgwApnSessModTrgrRatChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 62),
    _JnxMbgPgwApnSessModTrgrRatChg_Type()
)
jnxMbgPgwApnSessModTrgrRatChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrRatChg.setStatus("current")
_JnxMbgPgwApnSessModTrgrSgsnChg_Type = Counter64
_JnxMbgPgwApnSessModTrgrSgsnChg_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrSgsnChg = _JnxMbgPgwApnSessModTrgrSgsnChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 63),
    _JnxMbgPgwApnSessModTrgrSgsnChg_Type()
)
jnxMbgPgwApnSessModTrgrSgsnChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrSgsnChg.setStatus("current")
_JnxMbgPgwApnSessModTrgrSgwChg_Type = Counter64
_JnxMbgPgwApnSessModTrgrSgwChg_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrSgwChg = _JnxMbgPgwApnSessModTrgrSgwChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 64),
    _JnxMbgPgwApnSessModTrgrSgwChg_Type()
)
jnxMbgPgwApnSessModTrgrSgwChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrSgwChg.setStatus("current")
_JnxMbgPgwApnSessModTrgrPlmnChg_Type = Counter64
_JnxMbgPgwApnSessModTrgrPlmnChg_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrPlmnChg = _JnxMbgPgwApnSessModTrgrPlmnChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 65),
    _JnxMbgPgwApnSessModTrgrPlmnChg_Type()
)
jnxMbgPgwApnSessModTrgrPlmnChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrPlmnChg.setStatus("current")
_JnxMbgPgwApnSessModTrgrRaiChg_Type = Counter64
_JnxMbgPgwApnSessModTrgrRaiChg_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrRaiChg = _JnxMbgPgwApnSessModTrgrRaiChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 66),
    _JnxMbgPgwApnSessModTrgrRaiChg_Type()
)
jnxMbgPgwApnSessModTrgrRaiChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrRaiChg.setStatus("current")
_JnxMbgPgwApnSessModTrgrUliChg_Type = Counter64
_JnxMbgPgwApnSessModTrgrUliChg_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrUliChg = _JnxMbgPgwApnSessModTrgrUliChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 67),
    _JnxMbgPgwApnSessModTrgrUliChg_Type()
)
jnxMbgPgwApnSessModTrgrUliChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrUliChg.setStatus("current")
_JnxMbgPgwApnSessModTrgrIPCanChg_Type = Counter64
_JnxMbgPgwApnSessModTrgrIPCanChg_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrIPCanChg = _JnxMbgPgwApnSessModTrgrIPCanChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 68),
    _JnxMbgPgwApnSessModTrgrIPCanChg_Type()
)
jnxMbgPgwApnSessModTrgrIPCanChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrIPCanChg.setStatus("current")
_JnxMbgPgwApnMsInitSessModTftChg_Type = Counter64
_JnxMbgPgwApnMsInitSessModTftChg_Object = MibTableColumn
jnxMbgPgwApnMsInitSessModTftChg = _JnxMbgPgwApnMsInitSessModTftChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 69),
    _JnxMbgPgwApnMsInitSessModTftChg_Type()
)
jnxMbgPgwApnMsInitSessModTftChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsInitSessModTftChg.setStatus("current")
_JnxMbgPgwApnNwInitSessModTftChg_Type = Counter64
_JnxMbgPgwApnNwInitSessModTftChg_Object = MibTableColumn
jnxMbgPgwApnNwInitSessModTftChg = _JnxMbgPgwApnNwInitSessModTftChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 70),
    _JnxMbgPgwApnNwInitSessModTftChg_Type()
)
jnxMbgPgwApnNwInitSessModTftChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnNwInitSessModTftChg.setStatus("current")
_JnxMbgPgwApnSessModTrgrBrLoss_Type = Counter64
_JnxMbgPgwApnSessModTrgrBrLoss_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrBrLoss = _JnxMbgPgwApnSessModTrgrBrLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 71),
    _JnxMbgPgwApnSessModTrgrBrLoss_Type()
)
jnxMbgPgwApnSessModTrgrBrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrBrLoss.setStatus("current")
_JnxMbgPgwApnSessModTrgrBrRecvry_Type = Counter64
_JnxMbgPgwApnSessModTrgrBrRecvry_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrBrRecvry = _JnxMbgPgwApnSessModTrgrBrRecvry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 72),
    _JnxMbgPgwApnSessModTrgrBrRecvry_Type()
)
jnxMbgPgwApnSessModTrgrBrRecvry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrBrRecvry.setStatus("current")
_JnxMbgPgwApnSessModTrgrRsrAlloc_Type = Counter64
_JnxMbgPgwApnSessModTrgrRsrAlloc_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrRsrAlloc = _JnxMbgPgwApnSessModTrgrRsrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 73),
    _JnxMbgPgwApnSessModTrgrRsrAlloc_Type()
)
jnxMbgPgwApnSessModTrgrRsrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrRsrAlloc.setStatus("current")
_JnxMbgPgwApnSessModTrgrRevldTO_Type = Counter64
_JnxMbgPgwApnSessModTrgrRevldTO_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrRevldTO = _JnxMbgPgwApnSessModTrgrRevldTO_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 74),
    _JnxMbgPgwApnSessModTrgrRevldTO_Type()
)
jnxMbgPgwApnSessModTrgrRevldTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrRevldTO.setStatus("current")
_JnxMbgPgwApnSessModQoSExceedAuth_Type = Counter64
_JnxMbgPgwApnSessModQoSExceedAuth_Object = MibTableColumn
jnxMbgPgwApnSessModQoSExceedAuth = _JnxMbgPgwApnSessModQoSExceedAuth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 75),
    _JnxMbgPgwApnSessModQoSExceedAuth_Type()
)
jnxMbgPgwApnSessModQoSExceedAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModQoSExceedAuth.setStatus("current")
_JnxMbgPgwApnSessModTodProc_Type = Counter64
_JnxMbgPgwApnSessModTodProc_Object = MibTableColumn
jnxMbgPgwApnSessModTodProc = _JnxMbgPgwApnSessModTodProc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 76),
    _JnxMbgPgwApnSessModTodProc_Type()
)
jnxMbgPgwApnSessModTodProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTodProc.setStatus("current")
_JnxMbgPgwApnSessModTrgrChgSubsc_Type = Counter64
_JnxMbgPgwApnSessModTrgrChgSubsc_Object = MibTableColumn
jnxMbgPgwApnSessModTrgrChgSubsc = _JnxMbgPgwApnSessModTrgrChgSubsc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 77),
    _JnxMbgPgwApnSessModTrgrChgSubsc_Type()
)
jnxMbgPgwApnSessModTrgrChgSubsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTrgrChgSubsc.setStatus("current")
_JnxMbgPgwApnSessModAmbrChg_Type = Counter64
_JnxMbgPgwApnSessModAmbrChg_Object = MibTableColumn
jnxMbgPgwApnSessModAmbrChg = _JnxMbgPgwApnSessModAmbrChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 78),
    _JnxMbgPgwApnSessModAmbrChg_Type()
)
jnxMbgPgwApnSessModAmbrChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModAmbrChg.setStatus("current")
_JnxMbgPgwApnSessModEcgiChg_Type = Counter64
_JnxMbgPgwApnSessModEcgiChg_Object = MibTableColumn
jnxMbgPgwApnSessModEcgiChg = _JnxMbgPgwApnSessModEcgiChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 79),
    _JnxMbgPgwApnSessModEcgiChg_Type()
)
jnxMbgPgwApnSessModEcgiChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModEcgiChg.setStatus("current")
_JnxMbgPgwApnSessModTaiChg_Type = Counter64
_JnxMbgPgwApnSessModTaiChg_Object = MibTableColumn
jnxMbgPgwApnSessModTaiChg = _JnxMbgPgwApnSessModTaiChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 80),
    _JnxMbgPgwApnSessModTaiChg_Type()
)
jnxMbgPgwApnSessModTaiChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModTaiChg.setStatus("current")
_JnxMbgPgwApnSessModMsTimezoneChg_Type = Counter64
_JnxMbgPgwApnSessModMsTimezoneChg_Object = MibTableColumn
jnxMbgPgwApnSessModMsTimezoneChg = _JnxMbgPgwApnSessModMsTimezoneChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 81),
    _JnxMbgPgwApnSessModMsTimezoneChg_Type()
)
jnxMbgPgwApnSessModMsTimezoneChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModMsTimezoneChg.setStatus("current")
_JnxMbgPgwApnSessModDefQosChg_Type = Counter64
_JnxMbgPgwApnSessModDefQosChg_Object = MibTableColumn
jnxMbgPgwApnSessModDefQosChg = _JnxMbgPgwApnSessModDefQosChg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 82),
    _JnxMbgPgwApnSessModDefQosChg_Type()
)
jnxMbgPgwApnSessModDefQosChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessModDefQosChg.setStatus("current")
_JnxMbgPgwApnMsDedBrActAttempt_Type = Counter64
_JnxMbgPgwApnMsDedBrActAttempt_Object = MibTableColumn
jnxMbgPgwApnMsDedBrActAttempt = _JnxMbgPgwApnMsDedBrActAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 83),
    _JnxMbgPgwApnMsDedBrActAttempt_Type()
)
jnxMbgPgwApnMsDedBrActAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsDedBrActAttempt.setStatus("current")
_JnxMbgPgwApnMsDedBrActSucc_Type = Counter64
_JnxMbgPgwApnMsDedBrActSucc_Object = MibTableColumn
jnxMbgPgwApnMsDedBrActSucc = _JnxMbgPgwApnMsDedBrActSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 84),
    _JnxMbgPgwApnMsDedBrActSucc_Type()
)
jnxMbgPgwApnMsDedBrActSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsDedBrActSucc.setStatus("current")
_JnxMbgPgwApnNwDedBrActAttempt_Type = Counter64
_JnxMbgPgwApnNwDedBrActAttempt_Object = MibTableColumn
jnxMbgPgwApnNwDedBrActAttempt = _JnxMbgPgwApnNwDedBrActAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 85),
    _JnxMbgPgwApnNwDedBrActAttempt_Type()
)
jnxMbgPgwApnNwDedBrActAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnNwDedBrActAttempt.setStatus("current")
_JnxMbgPgwApnNwDedBrActSucc_Type = Counter64
_JnxMbgPgwApnNwDedBrActSucc_Object = MibTableColumn
jnxMbgPgwApnNwDedBrActSucc = _JnxMbgPgwApnNwDedBrActSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 86),
    _JnxMbgPgwApnNwDedBrActSucc_Type()
)
jnxMbgPgwApnNwDedBrActSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnNwDedBrActSucc.setStatus("current")
_JnxMbgPgwApnMsDedBrModAttempt_Type = Counter64
_JnxMbgPgwApnMsDedBrModAttempt_Object = MibTableColumn
jnxMbgPgwApnMsDedBrModAttempt = _JnxMbgPgwApnMsDedBrModAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 87),
    _JnxMbgPgwApnMsDedBrModAttempt_Type()
)
jnxMbgPgwApnMsDedBrModAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsDedBrModAttempt.setStatus("current")
_JnxMbgPgwApnMsDedBrModSucc_Type = Counter64
_JnxMbgPgwApnMsDedBrModSucc_Object = MibTableColumn
jnxMbgPgwApnMsDedBrModSucc = _JnxMbgPgwApnMsDedBrModSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 88),
    _JnxMbgPgwApnMsDedBrModSucc_Type()
)
jnxMbgPgwApnMsDedBrModSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsDedBrModSucc.setStatus("current")
_JnxMbgPgwApnNwDedBrModAttempt_Type = Counter64
_JnxMbgPgwApnNwDedBrModAttempt_Object = MibTableColumn
jnxMbgPgwApnNwDedBrModAttempt = _JnxMbgPgwApnNwDedBrModAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 89),
    _JnxMbgPgwApnNwDedBrModAttempt_Type()
)
jnxMbgPgwApnNwDedBrModAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnNwDedBrModAttempt.setStatus("current")
_JnxMbgPgwApnNwDedBrModSucc_Type = Counter64
_JnxMbgPgwApnNwDedBrModSucc_Object = MibTableColumn
jnxMbgPgwApnNwDedBrModSucc = _JnxMbgPgwApnNwDedBrModSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 90),
    _JnxMbgPgwApnNwDedBrModSucc_Type()
)
jnxMbgPgwApnNwDedBrModSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnNwDedBrModSucc.setStatus("current")
_JnxMbgPgwApnMsDedBrDeactAttempt_Type = Counter64
_JnxMbgPgwApnMsDedBrDeactAttempt_Object = MibTableColumn
jnxMbgPgwApnMsDedBrDeactAttempt = _JnxMbgPgwApnMsDedBrDeactAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 91),
    _JnxMbgPgwApnMsDedBrDeactAttempt_Type()
)
jnxMbgPgwApnMsDedBrDeactAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnMsDedBrDeactAttempt.setStatus("current")
_JnxMbgPgwApnNwDedBrDeactAttempt_Type = Counter64
_JnxMbgPgwApnNwDedBrDeactAttempt_Object = MibTableColumn
jnxMbgPgwApnNwDedBrDeactAttempt = _JnxMbgPgwApnNwDedBrDeactAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 92),
    _JnxMbgPgwApnNwDedBrDeactAttempt_Type()
)
jnxMbgPgwApnNwDedBrDeactAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnNwDedBrDeactAttempt.setStatus("current")
_JnxMbgPgwApnGwDedBrDeactAttempt_Type = Counter64
_JnxMbgPgwApnGwDedBrDeactAttempt_Object = MibTableColumn
jnxMbgPgwApnGwDedBrDeactAttempt = _JnxMbgPgwApnGwDedBrDeactAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 93),
    _JnxMbgPgwApnGwDedBrDeactAttempt_Type()
)
jnxMbgPgwApnGwDedBrDeactAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGwDedBrDeactAttempt.setStatus("current")
_JnxMbgPgwApnGbrDedBrCrtFailCAC_Type = Counter64
_JnxMbgPgwApnGbrDedBrCrtFailCAC_Object = MibTableColumn
jnxMbgPgwApnGbrDedBrCrtFailCAC = _JnxMbgPgwApnGbrDedBrCrtFailCAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 94),
    _JnxMbgPgwApnGbrDedBrCrtFailCAC_Type()
)
jnxMbgPgwApnGbrDedBrCrtFailCAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGbrDedBrCrtFailCAC.setStatus("current")
_JnxMbgPgwApnNGbrDedBrCrtFailCAC_Type = Counter64
_JnxMbgPgwApnNGbrDedBrCrtFailCAC_Object = MibTableColumn
jnxMbgPgwApnNGbrDedBrCrtFailCAC = _JnxMbgPgwApnNGbrDedBrCrtFailCAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 95),
    _JnxMbgPgwApnNGbrDedBrCrtFailCAC_Type()
)
jnxMbgPgwApnNGbrDedBrCrtFailCAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnNGbrDedBrCrtFailCAC.setStatus("current")
_JnxMbgPgwApnSessTermUnreachPcrf_Type = Counter64
_JnxMbgPgwApnSessTermUnreachPcrf_Object = MibTableColumn
jnxMbgPgwApnSessTermUnreachPcrf = _JnxMbgPgwApnSessTermUnreachPcrf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 96),
    _JnxMbgPgwApnSessTermUnreachPcrf_Type()
)
jnxMbgPgwApnSessTermUnreachPcrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessTermUnreachPcrf.setStatus("current")
_JnxMbgPgwApnSessTermPcrfRestart_Type = Counter64
_JnxMbgPgwApnSessTermPcrfRestart_Object = MibTableColumn
jnxMbgPgwApnSessTermPcrfRestart = _JnxMbgPgwApnSessTermPcrfRestart_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 97),
    _JnxMbgPgwApnSessTermPcrfRestart_Type()
)
jnxMbgPgwApnSessTermPcrfRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessTermPcrfRestart.setStatus("current")
_JnxMbgPgwApnGxCcrISent_Type = Counter64
_JnxMbgPgwApnGxCcrISent_Object = MibTableColumn
jnxMbgPgwApnGxCcrISent = _JnxMbgPgwApnGxCcrISent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 98),
    _JnxMbgPgwApnGxCcrISent_Type()
)
jnxMbgPgwApnGxCcrISent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcrISent.setStatus("deprecated")
_JnxMbgPgwApnGxCcaIRcvd_Type = Counter64
_JnxMbgPgwApnGxCcaIRcvd_Object = MibTableColumn
jnxMbgPgwApnGxCcaIRcvd = _JnxMbgPgwApnGxCcaIRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 99),
    _JnxMbgPgwApnGxCcaIRcvd_Type()
)
jnxMbgPgwApnGxCcaIRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcaIRcvd.setStatus("deprecated")
_JnxMbgPgwApnGxCcrUSent_Type = Counter64
_JnxMbgPgwApnGxCcrUSent_Object = MibTableColumn
jnxMbgPgwApnGxCcrUSent = _JnxMbgPgwApnGxCcrUSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 100),
    _JnxMbgPgwApnGxCcrUSent_Type()
)
jnxMbgPgwApnGxCcrUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcrUSent.setStatus("deprecated")
_JnxMbgPgwApnGxCcaURcvd_Type = Counter64
_JnxMbgPgwApnGxCcaURcvd_Object = MibTableColumn
jnxMbgPgwApnGxCcaURcvd = _JnxMbgPgwApnGxCcaURcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 101),
    _JnxMbgPgwApnGxCcaURcvd_Type()
)
jnxMbgPgwApnGxCcaURcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcaURcvd.setStatus("deprecated")
_JnxMbgPgwApnGxCcrTSent_Type = Counter64
_JnxMbgPgwApnGxCcrTSent_Object = MibTableColumn
jnxMbgPgwApnGxCcrTSent = _JnxMbgPgwApnGxCcrTSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 102),
    _JnxMbgPgwApnGxCcrTSent_Type()
)
jnxMbgPgwApnGxCcrTSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcrTSent.setStatus("deprecated")
_JnxMbgPgwApnGxCcaTRcvd_Type = Counter64
_JnxMbgPgwApnGxCcaTRcvd_Object = MibTableColumn
jnxMbgPgwApnGxCcaTRcvd = _JnxMbgPgwApnGxCcaTRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 103),
    _JnxMbgPgwApnGxCcaTRcvd_Type()
)
jnxMbgPgwApnGxCcaTRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcaTRcvd.setStatus("deprecated")
_JnxMbgPgwApnGxRarRcvd_Type = Counter64
_JnxMbgPgwApnGxRarRcvd_Object = MibTableColumn
jnxMbgPgwApnGxRarRcvd = _JnxMbgPgwApnGxRarRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 104),
    _JnxMbgPgwApnGxRarRcvd_Type()
)
jnxMbgPgwApnGxRarRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxRarRcvd.setStatus("deprecated")
_JnxMbgPgwApnGxRaaSent_Type = Counter64
_JnxMbgPgwApnGxRaaSent_Object = MibTableColumn
jnxMbgPgwApnGxRaaSent = _JnxMbgPgwApnGxRaaSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 105),
    _JnxMbgPgwApnGxRaaSent_Type()
)
jnxMbgPgwApnGxRaaSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxRaaSent.setStatus("deprecated")
_JnxMbgPgwApnGxRaaSentRsrFail_Type = Counter64
_JnxMbgPgwApnGxRaaSentRsrFail_Object = MibTableColumn
jnxMbgPgwApnGxRaaSentRsrFail = _JnxMbgPgwApnGxRaaSentRsrFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 106),
    _JnxMbgPgwApnGxRaaSentRsrFail_Type()
)
jnxMbgPgwApnGxRaaSentRsrFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxRaaSentRsrFail.setStatus("deprecated")
_JnxMbgPgwApnGxCcrRejTransntFail_Type = Counter64
_JnxMbgPgwApnGxCcrRejTransntFail_Object = MibTableColumn
jnxMbgPgwApnGxCcrRejTransntFail = _JnxMbgPgwApnGxCcrRejTransntFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 107),
    _JnxMbgPgwApnGxCcrRejTransntFail_Type()
)
jnxMbgPgwApnGxCcrRejTransntFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcrRejTransntFail.setStatus("deprecated")
_JnxMbgPgwApnGxCcrRejInitlParErr_Type = Counter64
_JnxMbgPgwApnGxCcrRejInitlParErr_Object = MibTableColumn
jnxMbgPgwApnGxCcrRejInitlParErr = _JnxMbgPgwApnGxCcrRejInitlParErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 108),
    _JnxMbgPgwApnGxCcrRejInitlParErr_Type()
)
jnxMbgPgwApnGxCcrRejInitlParErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcrRejInitlParErr.setStatus("deprecated")
_JnxMbgPgwApnGxCcrRejPermFail_Type = Counter64
_JnxMbgPgwApnGxCcrRejPermFail_Object = MibTableColumn
jnxMbgPgwApnGxCcrRejPermFail = _JnxMbgPgwApnGxCcrRejPermFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 109),
    _JnxMbgPgwApnGxCcrRejPermFail_Type()
)
jnxMbgPgwApnGxCcrRejPermFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcrRejPermFail.setStatus("deprecated")
_JnxMbgPgwApnGxCcrRejUknCode_Type = Counter64
_JnxMbgPgwApnGxCcrRejUknCode_Object = MibTableColumn
jnxMbgPgwApnGxCcrRejUknCode = _JnxMbgPgwApnGxCcrRejUknCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 110),
    _JnxMbgPgwApnGxCcrRejUknCode_Type()
)
jnxMbgPgwApnGxCcrRejUknCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcrRejUknCode.setStatus("deprecated")
_JnxMbgPgwApnGxCcrRejUknSess_Type = Counter64
_JnxMbgPgwApnGxCcrRejUknSess_Object = MibTableColumn
jnxMbgPgwApnGxCcrRejUknSess = _JnxMbgPgwApnGxCcrRejUknSess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 111),
    _JnxMbgPgwApnGxCcrRejUknSess_Type()
)
jnxMbgPgwApnGxCcrRejUknSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxCcrRejUknSess.setStatus("deprecated")
_JnxMbgPgwApnPccActiveDynRules_Type = Counter64
_JnxMbgPgwApnPccActiveDynRules_Object = MibTableColumn
jnxMbgPgwApnPccActiveDynRules = _JnxMbgPgwApnPccActiveDynRules_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 112),
    _JnxMbgPgwApnPccActiveDynRules_Type()
)
jnxMbgPgwApnPccActiveDynRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccActiveDynRules.setStatus("current")
_JnxMbgPgwApnPccDynRuleDeact_Type = Counter64
_JnxMbgPgwApnPccDynRuleDeact_Object = MibTableColumn
jnxMbgPgwApnPccDynRuleDeact = _JnxMbgPgwApnPccDynRuleDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 113),
    _JnxMbgPgwApnPccDynRuleDeact_Type()
)
jnxMbgPgwApnPccDynRuleDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccDynRuleDeact.setStatus("current")
_JnxMbgPgwApnPccRuleStaticAct_Type = Counter64
_JnxMbgPgwApnPccRuleStaticAct_Object = MibTableColumn
jnxMbgPgwApnPccRuleStaticAct = _JnxMbgPgwApnPccRuleStaticAct_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 114),
    _JnxMbgPgwApnPccRuleStaticAct_Type()
)
jnxMbgPgwApnPccRuleStaticAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccRuleStaticAct.setStatus("current")
_JnxMbgPgwApnPccRuleStaticDeact_Type = Counter64
_JnxMbgPgwApnPccRuleStaticDeact_Object = MibTableColumn
jnxMbgPgwApnPccRuleStaticDeact = _JnxMbgPgwApnPccRuleStaticDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 115),
    _JnxMbgPgwApnPccRuleStaticDeact_Type()
)
jnxMbgPgwApnPccRuleStaticDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccRuleStaticDeact.setStatus("current")
_JnxMbgPgwApnPccRuleDynMod_Type = Counter64
_JnxMbgPgwApnPccRuleDynMod_Object = MibTableColumn
jnxMbgPgwApnPccRuleDynMod = _JnxMbgPgwApnPccRuleDynMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 116),
    _JnxMbgPgwApnPccRuleDynMod_Type()
)
jnxMbgPgwApnPccRuleDynMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccRuleDynMod.setStatus("current")
_JnxMbgPgwApnPccRuleValidnFail_Type = Counter64
_JnxMbgPgwApnPccRuleValidnFail_Object = MibTableColumn
jnxMbgPgwApnPccRuleValidnFail = _JnxMbgPgwApnPccRuleValidnFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 117),
    _JnxMbgPgwApnPccRuleValidnFail_Type()
)
jnxMbgPgwApnPccRuleValidnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccRuleValidnFail.setStatus("current")
_JnxMbgPgwApnPccRuleEnforceFail_Type = Counter64
_JnxMbgPgwApnPccRuleEnforceFail_Object = MibTableColumn
jnxMbgPgwApnPccRuleEnforceFail = _JnxMbgPgwApnPccRuleEnforceFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 118),
    _JnxMbgPgwApnPccRuleEnforceFail_Type()
)
jnxMbgPgwApnPccRuleEnforceFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccRuleEnforceFail.setStatus("deprecated")
_JnxMbgPgwApnPccActFailNoRsr_Type = Counter64
_JnxMbgPgwApnPccActFailNoRsr_Object = MibTableColumn
jnxMbgPgwApnPccActFailNoRsr = _JnxMbgPgwApnPccActFailNoRsr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 119),
    _JnxMbgPgwApnPccActFailNoRsr_Type()
)
jnxMbgPgwApnPccActFailNoRsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccActFailNoRsr.setStatus("current")
_JnxMbgPgwApnPccRuleUpdProcFail_Type = Counter64
_JnxMbgPgwApnPccRuleUpdProcFail_Object = MibTableColumn
jnxMbgPgwApnPccRuleUpdProcFail = _JnxMbgPgwApnPccRuleUpdProcFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 120),
    _JnxMbgPgwApnPccRuleUpdProcFail_Type()
)
jnxMbgPgwApnPccRuleUpdProcFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnPccRuleUpdProcFail.setStatus("current")
_JnxMbgPgwApnInterRatHoAttempt_Type = Counter64
_JnxMbgPgwApnInterRatHoAttempt_Object = MibTableColumn
jnxMbgPgwApnInterRatHoAttempt = _JnxMbgPgwApnInterRatHoAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 121),
    _JnxMbgPgwApnInterRatHoAttempt_Type()
)
jnxMbgPgwApnInterRatHoAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnInterRatHoAttempt.setStatus("current")
_JnxMbgPgwApnInterRatHoSucc_Type = Counter64
_JnxMbgPgwApnInterRatHoSucc_Object = MibTableColumn
jnxMbgPgwApnInterRatHoSucc = _JnxMbgPgwApnInterRatHoSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 122),
    _JnxMbgPgwApnInterRatHoSucc_Type()
)
jnxMbgPgwApnInterRatHoSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnInterRatHoSucc.setStatus("current")
_JnxMbgPgwApnIntraRatHoAttempt_Type = Counter64
_JnxMbgPgwApnIntraRatHoAttempt_Object = MibTableColumn
jnxMbgPgwApnIntraRatHoAttempt = _JnxMbgPgwApnIntraRatHoAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 123),
    _JnxMbgPgwApnIntraRatHoAttempt_Type()
)
jnxMbgPgwApnIntraRatHoAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnIntraRatHoAttempt.setStatus("current")
_JnxMbgPgwApnIntraRatHoSucc_Type = Counter64
_JnxMbgPgwApnIntraRatHoSucc_Object = MibTableColumn
jnxMbgPgwApnIntraRatHoSucc = _JnxMbgPgwApnIntraRatHoSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 124),
    _JnxMbgPgwApnIntraRatHoSucc_Type()
)
jnxMbgPgwApnIntraRatHoSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnIntraRatHoSucc.setStatus("current")
_JnxMbgPgwApnOnlineAuthAttempt_Type = Counter64
_JnxMbgPgwApnOnlineAuthAttempt_Object = MibTableColumn
jnxMbgPgwApnOnlineAuthAttempt = _JnxMbgPgwApnOnlineAuthAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 125),
    _JnxMbgPgwApnOnlineAuthAttempt_Type()
)
jnxMbgPgwApnOnlineAuthAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnOnlineAuthAttempt.setStatus("deprecated")
_JnxMbgPgwApnOnlineAuthSucc_Type = Counter64
_JnxMbgPgwApnOnlineAuthSucc_Object = MibTableColumn
jnxMbgPgwApnOnlineAuthSucc = _JnxMbgPgwApnOnlineAuthSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 126),
    _JnxMbgPgwApnOnlineAuthSucc_Type()
)
jnxMbgPgwApnOnlineAuthSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnOnlineAuthSucc.setStatus("deprecated")
_JnxMbgPgwApnOnlineAuthTimeout_Type = Counter64
_JnxMbgPgwApnOnlineAuthTimeout_Object = MibTableColumn
jnxMbgPgwApnOnlineAuthTimeout = _JnxMbgPgwApnOnlineAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 127),
    _JnxMbgPgwApnOnlineAuthTimeout_Type()
)
jnxMbgPgwApnOnlineAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnOnlineAuthTimeout.setStatus("deprecated")
_JnxMbgPgwApnOnlineQuotaThdUpdReq_Type = Counter64
_JnxMbgPgwApnOnlineQuotaThdUpdReq_Object = MibTableColumn
jnxMbgPgwApnOnlineQuotaThdUpdReq = _JnxMbgPgwApnOnlineQuotaThdUpdReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 128),
    _JnxMbgPgwApnOnlineQuotaThdUpdReq_Type()
)
jnxMbgPgwApnOnlineQuotaThdUpdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnOnlineQuotaThdUpdReq.setStatus("deprecated")
_JnxMbgPgwApnGyCcrISent_Type = Counter64
_JnxMbgPgwApnGyCcrISent_Object = MibTableColumn
jnxMbgPgwApnGyCcrISent = _JnxMbgPgwApnGyCcrISent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 129),
    _JnxMbgPgwApnGyCcrISent_Type()
)
jnxMbgPgwApnGyCcrISent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrISent.setStatus("deprecated")
_JnxMbgPgwApnGyCcaISucc_Type = Counter64
_JnxMbgPgwApnGyCcaISucc_Object = MibTableColumn
jnxMbgPgwApnGyCcaISucc = _JnxMbgPgwApnGyCcaISucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 130),
    _JnxMbgPgwApnGyCcaISucc_Type()
)
jnxMbgPgwApnGyCcaISucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcaISucc.setStatus("deprecated")
_JnxMbgPgwApnGyCcrIFail_Type = Counter64
_JnxMbgPgwApnGyCcrIFail_Object = MibTableColumn
jnxMbgPgwApnGyCcrIFail = _JnxMbgPgwApnGyCcrIFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 131),
    _JnxMbgPgwApnGyCcrIFail_Type()
)
jnxMbgPgwApnGyCcrIFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrIFail.setStatus("deprecated")
_JnxMbgPgwApnGyCcrUSent_Type = Counter64
_JnxMbgPgwApnGyCcrUSent_Object = MibTableColumn
jnxMbgPgwApnGyCcrUSent = _JnxMbgPgwApnGyCcrUSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 132),
    _JnxMbgPgwApnGyCcrUSent_Type()
)
jnxMbgPgwApnGyCcrUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrUSent.setStatus("deprecated")
_JnxMbgPgwApnGyCcaUSucc_Type = Counter64
_JnxMbgPgwApnGyCcaUSucc_Object = MibTableColumn
jnxMbgPgwApnGyCcaUSucc = _JnxMbgPgwApnGyCcaUSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 133),
    _JnxMbgPgwApnGyCcaUSucc_Type()
)
jnxMbgPgwApnGyCcaUSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcaUSucc.setStatus("deprecated")
_JnxMbgPgwApnGyCcrUFail_Type = Counter64
_JnxMbgPgwApnGyCcrUFail_Object = MibTableColumn
jnxMbgPgwApnGyCcrUFail = _JnxMbgPgwApnGyCcrUFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 134),
    _JnxMbgPgwApnGyCcrUFail_Type()
)
jnxMbgPgwApnGyCcrUFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrUFail.setStatus("deprecated")
_JnxMbgPgwApnGyCcrTSent_Type = Counter64
_JnxMbgPgwApnGyCcrTSent_Object = MibTableColumn
jnxMbgPgwApnGyCcrTSent = _JnxMbgPgwApnGyCcrTSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 135),
    _JnxMbgPgwApnGyCcrTSent_Type()
)
jnxMbgPgwApnGyCcrTSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrTSent.setStatus("deprecated")
_JnxMbgPgwApnGyCcaTSucc_Type = Counter64
_JnxMbgPgwApnGyCcaTSucc_Object = MibTableColumn
jnxMbgPgwApnGyCcaTSucc = _JnxMbgPgwApnGyCcaTSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 136),
    _JnxMbgPgwApnGyCcaTSucc_Type()
)
jnxMbgPgwApnGyCcaTSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcaTSucc.setStatus("deprecated")
_JnxMbgPgwApnGyCcrTFail_Type = Counter64
_JnxMbgPgwApnGyCcrTFail_Object = MibTableColumn
jnxMbgPgwApnGyCcrTFail = _JnxMbgPgwApnGyCcrTFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 137),
    _JnxMbgPgwApnGyCcrTFail_Type()
)
jnxMbgPgwApnGyCcrTFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrTFail.setStatus("deprecated")
_JnxMbgPgwApnGyRarRcvd_Type = Counter64
_JnxMbgPgwApnGyRarRcvd_Object = MibTableColumn
jnxMbgPgwApnGyRarRcvd = _JnxMbgPgwApnGyRarRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 138),
    _JnxMbgPgwApnGyRarRcvd_Type()
)
jnxMbgPgwApnGyRarRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyRarRcvd.setStatus("deprecated")
_JnxMbgPgwApnGyRaaSent_Type = Counter64
_JnxMbgPgwApnGyRaaSent_Object = MibTableColumn
jnxMbgPgwApnGyRaaSent = _JnxMbgPgwApnGyRaaSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 139),
    _JnxMbgPgwApnGyRaaSent_Type()
)
jnxMbgPgwApnGyRaaSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyRaaSent.setStatus("deprecated")
_JnxMbgPgwApnGyRaaFail_Type = Counter64
_JnxMbgPgwApnGyRaaFail_Object = MibTableColumn
jnxMbgPgwApnGyRaaFail = _JnxMbgPgwApnGyRaaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 140),
    _JnxMbgPgwApnGyRaaFail_Type()
)
jnxMbgPgwApnGyRaaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyRaaFail.setStatus("deprecated")
_JnxMbgPgwApnGyAbortSessReqRcvd_Type = Counter64
_JnxMbgPgwApnGyAbortSessReqRcvd_Object = MibTableColumn
jnxMbgPgwApnGyAbortSessReqRcvd = _JnxMbgPgwApnGyAbortSessReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 141),
    _JnxMbgPgwApnGyAbortSessReqRcvd_Type()
)
jnxMbgPgwApnGyAbortSessReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyAbortSessReqRcvd.setStatus("deprecated")
_JnxMbgPgwApnGyAbortSessAnsSent_Type = Counter64
_JnxMbgPgwApnGyAbortSessAnsSent_Object = MibTableColumn
jnxMbgPgwApnGyAbortSessAnsSent = _JnxMbgPgwApnGyAbortSessAnsSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 142),
    _JnxMbgPgwApnGyAbortSessAnsSent_Type()
)
jnxMbgPgwApnGyAbortSessAnsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyAbortSessAnsSent.setStatus("deprecated")
_JnxMbgPgwApnGyCcrRejTransntFail_Type = Counter64
_JnxMbgPgwApnGyCcrRejTransntFail_Object = MibTableColumn
jnxMbgPgwApnGyCcrRejTransntFail = _JnxMbgPgwApnGyCcrRejTransntFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 143),
    _JnxMbgPgwApnGyCcrRejTransntFail_Type()
)
jnxMbgPgwApnGyCcrRejTransntFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrRejTransntFail.setStatus("deprecated")
_JnxMbgPgwApnGyCcrRejInitlParErr_Type = Counter64
_JnxMbgPgwApnGyCcrRejInitlParErr_Object = MibTableColumn
jnxMbgPgwApnGyCcrRejInitlParErr = _JnxMbgPgwApnGyCcrRejInitlParErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 144),
    _JnxMbgPgwApnGyCcrRejInitlParErr_Type()
)
jnxMbgPgwApnGyCcrRejInitlParErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrRejInitlParErr.setStatus("deprecated")
_JnxMbgPgwApnGyCcrRejPermFail_Type = Counter64
_JnxMbgPgwApnGyCcrRejPermFail_Object = MibTableColumn
jnxMbgPgwApnGyCcrRejPermFail = _JnxMbgPgwApnGyCcrRejPermFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 145),
    _JnxMbgPgwApnGyCcrRejPermFail_Type()
)
jnxMbgPgwApnGyCcrRejPermFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrRejPermFail.setStatus("deprecated")
_JnxMbgPgwApnGyCcrRejUknCode_Type = Counter64
_JnxMbgPgwApnGyCcrRejUknCode_Object = MibTableColumn
jnxMbgPgwApnGyCcrRejUknCode = _JnxMbgPgwApnGyCcrRejUknCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 146),
    _JnxMbgPgwApnGyCcrRejUknCode_Type()
)
jnxMbgPgwApnGyCcrRejUknCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrRejUknCode.setStatus("deprecated")
_JnxMbgPgwApnGyCcrRejUknSess_Type = Counter64
_JnxMbgPgwApnGyCcrRejUknSess_Object = MibTableColumn
jnxMbgPgwApnGyCcrRejUknSess = _JnxMbgPgwApnGyCcrRejUknSess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 147),
    _JnxMbgPgwApnGyCcrRejUknSess_Type()
)
jnxMbgPgwApnGyCcrRejUknSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyCcrRejUknSess.setStatus("deprecated")
_JnxMbgPgwApnGwAttemptedRedirect_Type = Counter64
_JnxMbgPgwApnGwAttemptedRedirect_Object = MibTableColumn
jnxMbgPgwApnGwAttemptedRedirect = _JnxMbgPgwApnGwAttemptedRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 148),
    _JnxMbgPgwApnGwAttemptedRedirect_Type()
)
jnxMbgPgwApnGwAttemptedRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGwAttemptedRedirect.setStatus("current")
_JnxMbgPgwApnSuccGwRedirect_Type = Counter64
_JnxMbgPgwApnSuccGwRedirect_Object = MibTableColumn
jnxMbgPgwApnSuccGwRedirect = _JnxMbgPgwApnSuccGwRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 149),
    _JnxMbgPgwApnSuccGwRedirect_Type()
)
jnxMbgPgwApnSuccGwRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccGwRedirect.setStatus("current")
_JnxMbgPgwApnSuccApnRedirect_Type = Counter64
_JnxMbgPgwApnSuccApnRedirect_Object = MibTableColumn
jnxMbgPgwApnSuccApnRedirect = _JnxMbgPgwApnSuccApnRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 150),
    _JnxMbgPgwApnSuccApnRedirect_Type()
)
jnxMbgPgwApnSuccApnRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSuccApnRedirect.setStatus("current")
_JnxMbgPgwApnSessnFailCtxNotFound_Type = Counter64
_JnxMbgPgwApnSessnFailCtxNotFound_Object = MibTableColumn
jnxMbgPgwApnSessnFailCtxNotFound = _JnxMbgPgwApnSessnFailCtxNotFound_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 151),
    _JnxMbgPgwApnSessnFailCtxNotFound_Type()
)
jnxMbgPgwApnSessnFailCtxNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnSessnFailCtxNotFound.setStatus("current")
_JnxMbgPgwApnGxMsInitModAttempt_Type = Counter64
_JnxMbgPgwApnGxMsInitModAttempt_Object = MibTableColumn
jnxMbgPgwApnGxMsInitModAttempt = _JnxMbgPgwApnGxMsInitModAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 152),
    _JnxMbgPgwApnGxMsInitModAttempt_Type()
)
jnxMbgPgwApnGxMsInitModAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxMsInitModAttempt.setStatus("current")
_JnxMbgPgwApnGxSuccMsInitMod_Type = Counter64
_JnxMbgPgwApnGxSuccMsInitMod_Object = MibTableColumn
jnxMbgPgwApnGxSuccMsInitMod = _JnxMbgPgwApnGxSuccMsInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 153),
    _JnxMbgPgwApnGxSuccMsInitMod_Type()
)
jnxMbgPgwApnGxSuccMsInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxSuccMsInitMod.setStatus("current")
_JnxMbgPgwApnGxPcrfInitMod_Type = Counter64
_JnxMbgPgwApnGxPcrfInitMod_Object = MibTableColumn
jnxMbgPgwApnGxPcrfInitMod = _JnxMbgPgwApnGxPcrfInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 154),
    _JnxMbgPgwApnGxPcrfInitMod_Type()
)
jnxMbgPgwApnGxPcrfInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxPcrfInitMod.setStatus("current")
_JnxMbgPgwApnGxSuccPcrfInitMod_Type = Counter64
_JnxMbgPgwApnGxSuccPcrfInitMod_Object = MibTableColumn
jnxMbgPgwApnGxSuccPcrfInitMod = _JnxMbgPgwApnGxSuccPcrfInitMod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 155),
    _JnxMbgPgwApnGxSuccPcrfInitMod_Type()
)
jnxMbgPgwApnGxSuccPcrfInitMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxSuccPcrfInitMod.setStatus("current")
_JnxMbgPgwApnGxMsInitSessTerm_Type = Counter64
_JnxMbgPgwApnGxMsInitSessTerm_Object = MibTableColumn
jnxMbgPgwApnGxMsInitSessTerm = _JnxMbgPgwApnGxMsInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 156),
    _JnxMbgPgwApnGxMsInitSessTerm_Type()
)
jnxMbgPgwApnGxMsInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxMsInitSessTerm.setStatus("current")
_JnxMbgPgwApnGxPcrfInitSessTerm_Type = Counter64
_JnxMbgPgwApnGxPcrfInitSessTerm_Object = MibTableColumn
jnxMbgPgwApnGxPcrfInitSessTerm = _JnxMbgPgwApnGxPcrfInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 157),
    _JnxMbgPgwApnGxPcrfInitSessTerm_Type()
)
jnxMbgPgwApnGxPcrfInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxPcrfInitSessTerm.setStatus("current")
_JnxMbgPgwApnGxGwInitSessTerm_Type = Counter64
_JnxMbgPgwApnGxGwInitSessTerm_Object = MibTableColumn
jnxMbgPgwApnGxGwInitSessTerm = _JnxMbgPgwApnGxGwInitSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 158),
    _JnxMbgPgwApnGxGwInitSessTerm_Type()
)
jnxMbgPgwApnGxGwInitSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGxGwInitSessTerm.setStatus("current")
_JnxMbgPgwApnGySessEstAttempt_Type = Counter64
_JnxMbgPgwApnGySessEstAttempt_Object = MibTableColumn
jnxMbgPgwApnGySessEstAttempt = _JnxMbgPgwApnGySessEstAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 159),
    _JnxMbgPgwApnGySessEstAttempt_Type()
)
jnxMbgPgwApnGySessEstAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGySessEstAttempt.setStatus("current")
_JnxMbgPgwApnGySuccSessEst_Type = Counter64
_JnxMbgPgwApnGySuccSessEst_Object = MibTableColumn
jnxMbgPgwApnGySuccSessEst = _JnxMbgPgwApnGySuccSessEst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 160),
    _JnxMbgPgwApnGySuccSessEst_Type()
)
jnxMbgPgwApnGySuccSessEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGySuccSessEst.setStatus("current")
_JnxMbgPgwApnGyReauthAttempt_Type = Counter64
_JnxMbgPgwApnGyReauthAttempt_Object = MibTableColumn
jnxMbgPgwApnGyReauthAttempt = _JnxMbgPgwApnGyReauthAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 161),
    _JnxMbgPgwApnGyReauthAttempt_Type()
)
jnxMbgPgwApnGyReauthAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyReauthAttempt.setStatus("current")
_JnxMbgPgwApnGySuccReauth_Type = Counter64
_JnxMbgPgwApnGySuccReauth_Object = MibTableColumn
jnxMbgPgwApnGySuccReauth = _JnxMbgPgwApnGySuccReauth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 162),
    _JnxMbgPgwApnGySuccReauth_Type()
)
jnxMbgPgwApnGySuccReauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGySuccReauth.setStatus("current")
_JnxMbgPgwApnGyAuthTimeout_Type = Counter64
_JnxMbgPgwApnGyAuthTimeout_Object = MibTableColumn
jnxMbgPgwApnGyAuthTimeout = _JnxMbgPgwApnGyAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 163),
    _JnxMbgPgwApnGyAuthTimeout_Type()
)
jnxMbgPgwApnGyAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyAuthTimeout.setStatus("current")
_JnxMbgPgwApnGyMsInitSessDeact_Type = Counter64
_JnxMbgPgwApnGyMsInitSessDeact_Object = MibTableColumn
jnxMbgPgwApnGyMsInitSessDeact = _JnxMbgPgwApnGyMsInitSessDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 164),
    _JnxMbgPgwApnGyMsInitSessDeact_Type()
)
jnxMbgPgwApnGyMsInitSessDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyMsInitSessDeact.setStatus("current")
_JnxMbgPgwApnGyOcsInitSessDeact_Type = Counter64
_JnxMbgPgwApnGyOcsInitSessDeact_Object = MibTableColumn
jnxMbgPgwApnGyOcsInitSessDeact = _JnxMbgPgwApnGyOcsInitSessDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 165),
    _JnxMbgPgwApnGyOcsInitSessDeact_Type()
)
jnxMbgPgwApnGyOcsInitSessDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyOcsInitSessDeact.setStatus("current")
_JnxMbgPgwApnGyGwInitSessDeact_Type = Counter64
_JnxMbgPgwApnGyGwInitSessDeact_Object = MibTableColumn
jnxMbgPgwApnGyGwInitSessDeact = _JnxMbgPgwApnGyGwInitSessDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 6, 1, 166),
    _JnxMbgPgwApnGyGwInitSessDeact_Type()
)
jnxMbgPgwApnGyGwInitSessDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnGyGwInitSessDeact.setStatus("current")
_JnxMbgPgwApnSMStatusTable_Object = MibTable
jnxMbgPgwApnSMStatusTable = _JnxMbgPgwApnSMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxMbgPgwApnSMStatusTable.setStatus("current")
_JnxMbgPgwApnSMStatusEntry_Object = MibTableRow
jnxMbgPgwApnSMStatusEntry = _JnxMbgPgwApnSMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7, 1)
)
jnxMbgPgwApnSMStatusEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwApnName"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwApnSMStatusEntry.setStatus("current")
_JnxMbgPgwApnActvSubscribers_Type = CounterBasedGauge64
_JnxMbgPgwApnActvSubscribers_Object = MibTableColumn
jnxMbgPgwApnActvSubscribers = _JnxMbgPgwApnActvSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7, 1, 1),
    _JnxMbgPgwApnActvSubscribers_Type()
)
jnxMbgPgwApnActvSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnActvSubscribers.setStatus("current")
_JnxMbgPgwApnActvSessions_Type = CounterBasedGauge64
_JnxMbgPgwApnActvSessions_Object = MibTableColumn
jnxMbgPgwApnActvSessions = _JnxMbgPgwApnActvSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7, 1, 2),
    _JnxMbgPgwApnActvSessions_Type()
)
jnxMbgPgwApnActvSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnActvSessions.setStatus("current")
_JnxMbgPgwApnActvBearers_Type = CounterBasedGauge64
_JnxMbgPgwApnActvBearers_Object = MibTableColumn
jnxMbgPgwApnActvBearers = _JnxMbgPgwApnActvBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7, 1, 3),
    _JnxMbgPgwApnActvBearers_Type()
)
jnxMbgPgwApnActvBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnActvBearers.setStatus("current")
_JnxMbgPgwApnActvPrepaidBearers_Type = CounterBasedGauge64
_JnxMbgPgwApnActvPrepaidBearers_Object = MibTableColumn
jnxMbgPgwApnActvPrepaidBearers = _JnxMbgPgwApnActvPrepaidBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7, 1, 4),
    _JnxMbgPgwApnActvPrepaidBearers_Type()
)
jnxMbgPgwApnActvPrepaidBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnActvPrepaidBearers.setStatus("current")
_JnxMbgPgwApnActvPostpaidBearers_Type = CounterBasedGauge64
_JnxMbgPgwApnActvPostpaidBearers_Object = MibTableColumn
jnxMbgPgwApnActvPostpaidBearers = _JnxMbgPgwApnActvPostpaidBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7, 1, 5),
    _JnxMbgPgwApnActvPostpaidBearers_Type()
)
jnxMbgPgwApnActvPostpaidBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnActvPostpaidBearers.setStatus("current")
_JnxMbgPgwApnActvGbrBearers_Type = CounterBasedGauge64
_JnxMbgPgwApnActvGbrBearers_Object = MibTableColumn
jnxMbgPgwApnActvGbrBearers = _JnxMbgPgwApnActvGbrBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7, 1, 6),
    _JnxMbgPgwApnActvGbrBearers_Type()
)
jnxMbgPgwApnActvGbrBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnActvGbrBearers.setStatus("current")
_JnxMbgPgwApnActvNonGbrBearers_Type = CounterBasedGauge64
_JnxMbgPgwApnActvNonGbrBearers_Object = MibTableColumn
jnxMbgPgwApnActvNonGbrBearers = _JnxMbgPgwApnActvNonGbrBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 7, 1, 7),
    _JnxMbgPgwApnActvNonGbrBearers_Type()
)
jnxMbgPgwApnActvNonGbrBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnActvNonGbrBearers.setStatus("current")
_JnxMbgPgwSMClRateStatsTable_Object = MibTable
jnxMbgPgwSMClRateStatsTable = _JnxMbgPgwSMClRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMClRateStatsTable.setStatus("current")
_JnxMbgPgwSMClRateStatsEntry_Object = MibTableRow
jnxMbgPgwSMClRateStatsEntry = _JnxMbgPgwSMClRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8, 1)
)
jnxMbgPgwSMClRateStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMClRateStatsEntry.setStatus("current")
_JnxMbgPgwClRateIntervalMin_Type = Unsigned32
_JnxMbgPgwClRateIntervalMin_Object = MibTableColumn
jnxMbgPgwClRateIntervalMin = _JnxMbgPgwClRateIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8, 1, 1),
    _JnxMbgPgwClRateIntervalMin_Type()
)
jnxMbgPgwClRateIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwClRateIntervalMin.setStatus("current")
_JnxMbgPgwClRateSuccSessnEst_Type = Counter64
_JnxMbgPgwClRateSuccSessnEst_Object = MibTableColumn
jnxMbgPgwClRateSuccSessnEst = _JnxMbgPgwClRateSuccSessnEst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8, 1, 2),
    _JnxMbgPgwClRateSuccSessnEst_Type()
)
jnxMbgPgwClRateSuccSessnEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwClRateSuccSessnEst.setStatus("current")
_JnxMbgPgwClRateSuccSessnDel_Type = Counter64
_JnxMbgPgwClRateSuccSessnDel_Object = MibTableColumn
jnxMbgPgwClRateSuccSessnDel = _JnxMbgPgwClRateSuccSessnDel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8, 1, 3),
    _JnxMbgPgwClRateSuccSessnDel_Type()
)
jnxMbgPgwClRateSuccSessnDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwClRateSuccSessnDel.setStatus("current")
_JnxMbgPgwClRateStatsGnInpPkt_Type = Counter64
_JnxMbgPgwClRateStatsGnInpPkt_Object = MibTableColumn
jnxMbgPgwClRateStatsGnInpPkt = _JnxMbgPgwClRateStatsGnInpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8, 1, 4),
    _JnxMbgPgwClRateStatsGnInpPkt_Type()
)
jnxMbgPgwClRateStatsGnInpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwClRateStatsGnInpPkt.setStatus("current")
_JnxMbgPgwClRateStatsGnInpByt_Type = Counter64
_JnxMbgPgwClRateStatsGnInpByt_Object = MibTableColumn
jnxMbgPgwClRateStatsGnInpByt = _JnxMbgPgwClRateStatsGnInpByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8, 1, 5),
    _JnxMbgPgwClRateStatsGnInpByt_Type()
)
jnxMbgPgwClRateStatsGnInpByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwClRateStatsGnInpByt.setStatus("current")
_JnxMbgPgwClRateStatsGnOutPkt_Type = Counter64
_JnxMbgPgwClRateStatsGnOutPkt_Object = MibTableColumn
jnxMbgPgwClRateStatsGnOutPkt = _JnxMbgPgwClRateStatsGnOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8, 1, 6),
    _JnxMbgPgwClRateStatsGnOutPkt_Type()
)
jnxMbgPgwClRateStatsGnOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwClRateStatsGnOutPkt.setStatus("current")
_JnxMbgPgwClRateStatsGnOutByt_Type = Counter64
_JnxMbgPgwClRateStatsGnOutByt_Object = MibTableColumn
jnxMbgPgwClRateStatsGnOutByt = _JnxMbgPgwClRateStatsGnOutByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 8, 1, 7),
    _JnxMbgPgwClRateStatsGnOutByt_Type()
)
jnxMbgPgwClRateStatsGnOutByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwClRateStatsGnOutByt.setStatus("current")
_JnxMbgPgwSMSpicStatusTable_Object = MibTable
jnxMbgPgwSMSpicStatusTable = _JnxMbgPgwSMSpicStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMSpicStatusTable.setStatus("current")
_JnxMbgPgwSMSpicStatusEntry_Object = MibTableRow
jnxMbgPgwSMSpicStatusEntry = _JnxMbgPgwSMSpicStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1)
)
jnxMbgPgwSMSpicStatusEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgGwFpc"),
    (0, "JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgGwPic"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMSpicStatusEntry.setStatus("current")
_JnxMbgGwFpc_Type = Unsigned32
_JnxMbgGwFpc_Object = MibTableColumn
jnxMbgGwFpc = _JnxMbgGwFpc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 1),
    _JnxMbgGwFpc_Type()
)
jnxMbgGwFpc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgGwFpc.setStatus("current")
_JnxMbgGwPic_Type = Unsigned32
_JnxMbgGwPic_Object = MibTableColumn
jnxMbgGwPic = _JnxMbgGwPic_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 2),
    _JnxMbgGwPic_Type()
)
jnxMbgGwPic.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgGwPic.setStatus("current")
_JnxMbgPgwSpicStatusName_Type = DisplayString
_JnxMbgPgwSpicStatusName_Object = MibTableColumn
jnxMbgPgwSpicStatusName = _JnxMbgPgwSpicStatusName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 3),
    _JnxMbgPgwSpicStatusName_Type()
)
jnxMbgPgwSpicStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicStatusName.setStatus("current")


class _JnxMbgPgwSpicStatusState_Type(Integer32):
    """Custom type jnxMbgPgwSpicStatusState based on Integer32"""
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
          ("backup", 3),
          ("invalid", 0),
          ("standalone", 1))
    )


_JnxMbgPgwSpicStatusState_Type.__name__ = "Integer32"
_JnxMbgPgwSpicStatusState_Object = MibTableColumn
jnxMbgPgwSpicStatusState = _JnxMbgPgwSpicStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 4),
    _JnxMbgPgwSpicStatusState_Type()
)
jnxMbgPgwSpicStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicStatusState.setStatus("current")


class _JnxMbgPgwSpicStatusType_Type(Integer32):
    """Custom type jnxMbgPgwSpicStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pfe", 3),
          ("servicePic", 2),
          ("sessionPic", 1))
    )


_JnxMbgPgwSpicStatusType_Type.__name__ = "Integer32"
_JnxMbgPgwSpicStatusType_Object = MibTableColumn
jnxMbgPgwSpicStatusType = _JnxMbgPgwSpicStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 5),
    _JnxMbgPgwSpicStatusType_Type()
)
jnxMbgPgwSpicStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicStatusType.setStatus("current")
_JnxMbgPgwSpicActvSubscribers_Type = CounterBasedGauge64
_JnxMbgPgwSpicActvSubscribers_Object = MibTableColumn
jnxMbgPgwSpicActvSubscribers = _JnxMbgPgwSpicActvSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 6),
    _JnxMbgPgwSpicActvSubscribers_Type()
)
jnxMbgPgwSpicActvSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicActvSubscribers.setStatus("current")
_JnxMbgPgwSpicActvSessions_Type = CounterBasedGauge64
_JnxMbgPgwSpicActvSessions_Object = MibTableColumn
jnxMbgPgwSpicActvSessions = _JnxMbgPgwSpicActvSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 7),
    _JnxMbgPgwSpicActvSessions_Type()
)
jnxMbgPgwSpicActvSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicActvSessions.setStatus("current")
_JnxMbgPgwSpicActvBearers_Type = CounterBasedGauge64
_JnxMbgPgwSpicActvBearers_Object = MibTableColumn
jnxMbgPgwSpicActvBearers = _JnxMbgPgwSpicActvBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 8),
    _JnxMbgPgwSpicActvBearers_Type()
)
jnxMbgPgwSpicActvBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicActvBearers.setStatus("current")
_JnxMbgPgwSpicCPUUtil_Type = Gauge32
_JnxMbgPgwSpicCPUUtil_Object = MibTableColumn
jnxMbgPgwSpicCPUUtil = _JnxMbgPgwSpicCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 9),
    _JnxMbgPgwSpicCPUUtil_Type()
)
jnxMbgPgwSpicCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicCPUUtil.setStatus("current")
_JnxMbgPgwSpicMemoryUtil_Type = Gauge32
_JnxMbgPgwSpicMemoryUtil_Object = MibTableColumn
jnxMbgPgwSpicMemoryUtil = _JnxMbgPgwSpicMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 10),
    _JnxMbgPgwSpicMemoryUtil_Type()
)
jnxMbgPgwSpicMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicMemoryUtil.setStatus("current")
_JnxMbgPgwSpicActvPrepaidBearers_Type = CounterBasedGauge64
_JnxMbgPgwSpicActvPrepaidBearers_Object = MibTableColumn
jnxMbgPgwSpicActvPrepaidBearers = _JnxMbgPgwSpicActvPrepaidBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 11),
    _JnxMbgPgwSpicActvPrepaidBearers_Type()
)
jnxMbgPgwSpicActvPrepaidBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicActvPrepaidBearers.setStatus("current")
_JnxMbgPgwSpicActvPostpaidBearers_Type = CounterBasedGauge64
_JnxMbgPgwSpicActvPostpaidBearers_Object = MibTableColumn
jnxMbgPgwSpicActvPostpaidBearers = _JnxMbgPgwSpicActvPostpaidBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 12),
    _JnxMbgPgwSpicActvPostpaidBearers_Type()
)
jnxMbgPgwSpicActvPostpaidBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicActvPostpaidBearers.setStatus("current")
_JnxMbgPgwSpicActvGbrBearers_Type = CounterBasedGauge64
_JnxMbgPgwSpicActvGbrBearers_Object = MibTableColumn
jnxMbgPgwSpicActvGbrBearers = _JnxMbgPgwSpicActvGbrBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 13),
    _JnxMbgPgwSpicActvGbrBearers_Type()
)
jnxMbgPgwSpicActvGbrBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicActvGbrBearers.setStatus("current")
_JnxMbgPgwSpicActvNonGbrBearers_Type = CounterBasedGauge64
_JnxMbgPgwSpicActvNonGbrBearers_Object = MibTableColumn
jnxMbgPgwSpicActvNonGbrBearers = _JnxMbgPgwSpicActvNonGbrBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 9, 1, 14),
    _JnxMbgPgwSpicActvNonGbrBearers_Type()
)
jnxMbgPgwSpicActvNonGbrBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSpicActvNonGbrBearers.setStatus("current")
_JnxMbgPgwApnSMClRateStatsTable_Object = MibTable
jnxMbgPgwApnSMClRateStatsTable = _JnxMbgPgwApnSMClRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    jnxMbgPgwApnSMClRateStatsTable.setStatus("current")
_JnxMbgPgwApnSMClRateStatsEntry_Object = MibTableRow
jnxMbgPgwApnSMClRateStatsEntry = _JnxMbgPgwApnSMClRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1)
)
jnxMbgPgwApnSMClRateStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwApnCRName"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwApnSMClRateStatsEntry.setStatus("current")
_JnxMbgPgwApnCRName_Type = DisplayString
_JnxMbgPgwApnCRName_Object = MibTableColumn
jnxMbgPgwApnCRName = _JnxMbgPgwApnCRName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 1),
    _JnxMbgPgwApnCRName_Type()
)
jnxMbgPgwApnCRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCRName.setStatus("current")
_JnxMbgPgwApnCRIntervalMin_Type = Unsigned32
_JnxMbgPgwApnCRIntervalMin_Object = MibTableColumn
jnxMbgPgwApnCRIntervalMin = _JnxMbgPgwApnCRIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 2),
    _JnxMbgPgwApnCRIntervalMin_Type()
)
jnxMbgPgwApnCRIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCRIntervalMin.setStatus("current")
_JnxMbgPgwApnCRPrepaidBrAct_Type = Counter64
_JnxMbgPgwApnCRPrepaidBrAct_Object = MibTableColumn
jnxMbgPgwApnCRPrepaidBrAct = _JnxMbgPgwApnCRPrepaidBrAct_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 3),
    _JnxMbgPgwApnCRPrepaidBrAct_Type()
)
jnxMbgPgwApnCRPrepaidBrAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCRPrepaidBrAct.setStatus("current")
_JnxMbgPgwApnCRPrepaidBrDeact_Type = Counter64
_JnxMbgPgwApnCRPrepaidBrDeact_Object = MibTableColumn
jnxMbgPgwApnCRPrepaidBrDeact = _JnxMbgPgwApnCRPrepaidBrDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 4),
    _JnxMbgPgwApnCRPrepaidBrDeact_Type()
)
jnxMbgPgwApnCRPrepaidBrDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCRPrepaidBrDeact.setStatus("current")
_JnxMbgPgwApnCRPostpaidBrAct_Type = Counter64
_JnxMbgPgwApnCRPostpaidBrAct_Object = MibTableColumn
jnxMbgPgwApnCRPostpaidBrAct = _JnxMbgPgwApnCRPostpaidBrAct_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 5),
    _JnxMbgPgwApnCRPostpaidBrAct_Type()
)
jnxMbgPgwApnCRPostpaidBrAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCRPostpaidBrAct.setStatus("current")
_JnxMbgPgwApnCRPostpaidBrDeact_Type = Counter64
_JnxMbgPgwApnCRPostpaidBrDeact_Object = MibTableColumn
jnxMbgPgwApnCRPostpaidBrDeact = _JnxMbgPgwApnCRPostpaidBrDeact_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 6),
    _JnxMbgPgwApnCRPostpaidBrDeact_Type()
)
jnxMbgPgwApnCRPostpaidBrDeact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCRPostpaidBrDeact.setStatus("current")
_JnxMbgPgwApnCROnlineAuthTimeout_Type = Counter64
_JnxMbgPgwApnCROnlineAuthTimeout_Object = MibTableColumn
jnxMbgPgwApnCROnlineAuthTimeout = _JnxMbgPgwApnCROnlineAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 7),
    _JnxMbgPgwApnCROnlineAuthTimeout_Type()
)
jnxMbgPgwApnCROnlineAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCROnlineAuthTimeout.setStatus("current")
_JnxMbgPgwApnCRQuotaThdUpdReq_Type = Counter64
_JnxMbgPgwApnCRQuotaThdUpdReq_Object = MibTableColumn
jnxMbgPgwApnCRQuotaThdUpdReq = _JnxMbgPgwApnCRQuotaThdUpdReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 8),
    _JnxMbgPgwApnCRQuotaThdUpdReq_Type()
)
jnxMbgPgwApnCRQuotaThdUpdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCRQuotaThdUpdReq.setStatus("current")
_JnxMbgPgwApnCROnlineRarRcvd_Type = Counter64
_JnxMbgPgwApnCROnlineRarRcvd_Object = MibTableColumn
jnxMbgPgwApnCROnlineRarRcvd = _JnxMbgPgwApnCROnlineRarRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 9),
    _JnxMbgPgwApnCROnlineRarRcvd_Type()
)
jnxMbgPgwApnCROnlineRarRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCROnlineRarRcvd.setStatus("current")
_JnxMbgPgwApnCROnlineRarSucc_Type = Counter64
_JnxMbgPgwApnCROnlineRarSucc_Object = MibTableColumn
jnxMbgPgwApnCROnlineRarSucc = _JnxMbgPgwApnCROnlineRarSucc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 1, 10, 1, 10),
    _JnxMbgPgwApnCROnlineRarSucc_Type()
)
jnxMbgPgwApnCROnlineRarSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwApnCROnlineRarSucc.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgPgwQosBearersThresStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 1)
)
jnxMbgPgwQosBearersThresStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosThreshold1Status"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosThreshold2Status"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosBearersThresStatus.setStatus(
        "deprecated"
    )

jnxMbgPgwQosCPUThresholdStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 2)
)
jnxMbgPgwQosCPUThresholdStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosThreshold1Status"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosThreshold2Status"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosCPUThresholdStatus.setStatus(
        "deprecated"
    )

jnxMbgPgwQosMemThresholdStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 3)
)
jnxMbgPgwQosMemThresholdStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosThreshold1Status"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosThreshold2Status"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosMemThresholdStatus.setStatus(
        "deprecated"
    )

jnxMbgPgwAPNQosBearersThreStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 4)
)
jnxMbgPgwAPNQosBearersThreStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosAPNName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosThreshold1Status"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwQosThreshold2Status"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwAPNQosBearersThreStatus.setStatus(
        "deprecated"
    )

jnxMbgPgwSMGtpEventNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 5)
)
jnxMbgPgwSMGtpEventNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMGTPEventType"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMGTPEventCause"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMGtpEventNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwSMSubscribersThresGblNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 6)
)
jnxMbgPgwSMSubscribersThresGblNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmThrshld"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMSubscribersThresGblNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwSMSubscribersThresPerSPNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 7)
)
jnxMbgPgwSMSubscribersThresPerSPNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmThrshld"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMSPICName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMSubscribersThresPerSPNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwSMSessionEstFailThresPerSPNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 8)
)
jnxMbgPgwSMSessionEstFailThresPerSPNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmThrshld"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMSessionEstFailReason"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMSPICName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMSessionEstFailThresPerSPNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwSMSessionEstFailThresPerTCNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 9)
)
jnxMbgPgwSMSessionEstFailThresPerTCNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmThrshld"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMSessionEstFailReason"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMTCName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMSessionEstFailThresPerTCNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwSMSessionEstFailThresPerQCINotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 10)
)
jnxMbgPgwSMSessionEstFailThresPerQCINotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmThrshld"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMSessionEstFailReason"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMQCIName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMSessionEstFailThresPerQCINotif.setStatus(
        "deprecated"
    )

jnxMbgPgwSMBearersThresGblNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 11)
)
jnxMbgPgwSMBearersThresGblNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmThrshld"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMBearersThresGblNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwSMBearersThresPerSPNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 12)
)
jnxMbgPgwSMBearersThresPerSPNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmThrshld"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMAlarmState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMSPICName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMBearersThresPerSPNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwGatewayMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 13)
)
jnxMbgPgwGatewayMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwMMGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwPrevGatewayMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwNewGatewayMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwGatewayMMStateChange.setStatus(
        "current"
    )

jnxMbgPgwAPNMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 14)
)
jnxMbgPgwAPNMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwAPNMMGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwAPNMMAPNName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwPrevAPNMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwNewAPNMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwAPNMMStateChange.setStatus(
        "current"
    )

jnxMbgPgwQosBrThreshStatusHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 15)
)
jnxMbgPgwQosBrThreshStatusHi.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosBrThreshStatusHi.setStatus(
        "current"
    )

jnxMbgPgwQosBrThreshStatusLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 16)
)
jnxMbgPgwQosBrThreshStatusLow.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosBrThreshStatusLow.setStatus(
        "current"
    )

jnxMbgPgwQosBrThreshStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 17)
)
jnxMbgPgwQosBrThreshStatusClear.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosBrThreshStatusClear.setStatus(
        "current"
    )

jnxMbgPgwQosCPUThreshStatusHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 18)
)
jnxMbgPgwQosCPUThreshStatusHi.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosCPUThreshStatusHi.setStatus(
        "current"
    )

jnxMbgPgwQosCPUThreshStatusLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 19)
)
jnxMbgPgwQosCPUThreshStatusLow.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosCPUThreshStatusLow.setStatus(
        "current"
    )

jnxMbgPgwQosCPUThreshStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 20)
)
jnxMbgPgwQosCPUThreshStatusClear.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosCPUThreshStatusClear.setStatus(
        "current"
    )

jnxMbgPgwQosMemThreshStatusHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 21)
)
jnxMbgPgwQosMemThreshStatusHi.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosMemThreshStatusHi.setStatus(
        "current"
    )

jnxMbgPgwQosMemThreshStatusLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 22)
)
jnxMbgPgwQosMemThreshStatusLow.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosMemThreshStatusLow.setStatus(
        "current"
    )

jnxMbgPgwQosMemThreshStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 23)
)
jnxMbgPgwQosMemThreshStatusClear.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwQosMemThreshStatusClear.setStatus(
        "current"
    )

jnxMbgPgwSMGtpEvntNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 24)
)
jnxMbgPgwSMGtpEvntNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMGTPEventType"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMGTPEventCause"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwSMGtpEvntNotif.setStatus(
        "current"
    )

jnxMbgPgwPFEMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 25)
)
jnxMbgPgwPFEMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwAPNMMGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMInterfaceName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwPrevAPNMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwNewAPNMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwPFEMMStateChange.setStatus(
        "current"
    )

jnxMbgPgwMSMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 26)
)
jnxMbgPgwMSMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwAPNMMGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMInterfaceName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwPrevAPNMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwNewAPNMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwMSMMStateChange.setStatus(
        "current"
    )

jnxMbgPgwAPFEMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 27)
)
jnxMbgPgwAPFEMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwAPNMMGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMInterfaceName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwPrevAPNMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwNewAPNMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwAPFEMMStateChange.setStatus(
        "current"
    )

jnxMbgPgwAMSMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 1, 0, 28)
)
jnxMbgPgwAMSMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwAPNMMGatewayName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwSMInterfaceName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwPrevAPNMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-MIB", "jnxMbgPgwNewAPNMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwAMSMMStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-SM-MIB",
    **{"jnxMbgPgwSubscriberManagerMib": jnxMbgPgwSubscriberManagerMib,
       "jnxMbgPgwSMNotifications": jnxMbgPgwSMNotifications,
       "jnxMbgPgwQosBearersThresStatus": jnxMbgPgwQosBearersThresStatus,
       "jnxMbgPgwQosCPUThresholdStatus": jnxMbgPgwQosCPUThresholdStatus,
       "jnxMbgPgwQosMemThresholdStatus": jnxMbgPgwQosMemThresholdStatus,
       "jnxMbgPgwAPNQosBearersThreStatus": jnxMbgPgwAPNQosBearersThreStatus,
       "jnxMbgPgwSMGtpEventNotif": jnxMbgPgwSMGtpEventNotif,
       "jnxMbgPgwSMSubscribersThresGblNotif": jnxMbgPgwSMSubscribersThresGblNotif,
       "jnxMbgPgwSMSubscribersThresPerSPNotif": jnxMbgPgwSMSubscribersThresPerSPNotif,
       "jnxMbgPgwSMSessionEstFailThresPerSPNotif": jnxMbgPgwSMSessionEstFailThresPerSPNotif,
       "jnxMbgPgwSMSessionEstFailThresPerTCNotif": jnxMbgPgwSMSessionEstFailThresPerTCNotif,
       "jnxMbgPgwSMSessionEstFailThresPerQCINotif": jnxMbgPgwSMSessionEstFailThresPerQCINotif,
       "jnxMbgPgwSMBearersThresGblNotif": jnxMbgPgwSMBearersThresGblNotif,
       "jnxMbgPgwSMBearersThresPerSPNotif": jnxMbgPgwSMBearersThresPerSPNotif,
       "jnxMbgPgwGatewayMMStateChange": jnxMbgPgwGatewayMMStateChange,
       "jnxMbgPgwAPNMMStateChange": jnxMbgPgwAPNMMStateChange,
       "jnxMbgPgwQosBrThreshStatusHi": jnxMbgPgwQosBrThreshStatusHi,
       "jnxMbgPgwQosBrThreshStatusLow": jnxMbgPgwQosBrThreshStatusLow,
       "jnxMbgPgwQosBrThreshStatusClear": jnxMbgPgwQosBrThreshStatusClear,
       "jnxMbgPgwQosCPUThreshStatusHi": jnxMbgPgwQosCPUThreshStatusHi,
       "jnxMbgPgwQosCPUThreshStatusLow": jnxMbgPgwQosCPUThreshStatusLow,
       "jnxMbgPgwQosCPUThreshStatusClear": jnxMbgPgwQosCPUThreshStatusClear,
       "jnxMbgPgwQosMemThreshStatusHi": jnxMbgPgwQosMemThreshStatusHi,
       "jnxMbgPgwQosMemThreshStatusLow": jnxMbgPgwQosMemThreshStatusLow,
       "jnxMbgPgwQosMemThreshStatusClear": jnxMbgPgwQosMemThreshStatusClear,
       "jnxMbgPgwSMGtpEvntNotif": jnxMbgPgwSMGtpEvntNotif,
       "jnxMbgPgwPFEMMStateChange": jnxMbgPgwPFEMMStateChange,
       "jnxMbgPgwMSMMStateChange": jnxMbgPgwMSMMStateChange,
       "jnxMbgPgwAPFEMMStateChange": jnxMbgPgwAPFEMMStateChange,
       "jnxMbgPgwAMSMMStateChange": jnxMbgPgwAMSMMStateChange,
       "jnxMbgPgwSMObjects": jnxMbgPgwSMObjects,
       "jnxMbgPgwAPNStatsTable": jnxMbgPgwAPNStatsTable,
       "jnxMbgPgwAPNStatsTableEntry": jnxMbgPgwAPNStatsTableEntry,
       "jnxMbgPgwAPNName": jnxMbgPgwAPNName,
       "jnxMbgPgwSessnEstAttempts": jnxMbgPgwSessnEstAttempts,
       "jnxMbgPgwSuccSessnsEst": jnxMbgPgwSuccSessnsEst,
       "jnxMbgPgwSessnFailedServcUnaval": jnxMbgPgwSessnFailedServcUnaval,
       "jnxMbgPgwSessnFailedSysFailure": jnxMbgPgwSessnFailedSysFailure,
       "jnxMbgPgwSessnFailedNoResource": jnxMbgPgwSessnFailedNoResource,
       "jnxMbgPgwSessnFailedNoAddr": jnxMbgPgwSessnFailedNoAddr,
       "jnxMbgPgwSessnFailedServcDenied": jnxMbgPgwSessnFailedServcDenied,
       "jnxMbgPgwSessnFailedAuthFailed": jnxMbgPgwSessnFailedAuthFailed,
       "jnxMbgPgwSessnFailedAccessDenied": jnxMbgPgwSessnFailedAccessDenied,
       "jnxMbgPgwPeerInitSessnDeact": jnxMbgPgwPeerInitSessnDeact,
       "jnxMbgPgwSuccPeerInitSessnDeact": jnxMbgPgwSuccPeerInitSessnDeact,
       "jnxMbgPgwGWInitSessnDeact": jnxMbgPgwGWInitSessnDeact,
       "jnxMbgPgwSuccGWInitSessnDeact": jnxMbgPgwSuccGWInitSessnDeact,
       "jnxMbgPgwStatus": jnxMbgPgwStatus,
       "jnxMbgPgwActiveSubscribers": jnxMbgPgwActiveSubscribers,
       "jnxMbgPgwActiveSessions": jnxMbgPgwActiveSessions,
       "jnxMbgPgwActiveBearers": jnxMbgPgwActiveBearers,
       "jnxMbgPgwCPUUtilization": jnxMbgPgwCPUUtilization,
       "jnxMbgPgwMemoryUtilization": jnxMbgPgwMemoryUtilization,
       "jnxMbgPgwSMNotificationVars": jnxMbgPgwSMNotificationVars,
       "jnxMbgPgwGatewayName": jnxMbgPgwGatewayName,
       "jnxMbgPgwQosAPNName": jnxMbgPgwQosAPNName,
       "jnxMbgPgwQosThreshold1Status": jnxMbgPgwQosThreshold1Status,
       "jnxMbgPgwQosThreshold2Status": jnxMbgPgwQosThreshold2Status,
       "jnxMbgPgwSMGTPEventType": jnxMbgPgwSMGTPEventType,
       "jnxMbgPgwSMGTPEventCause": jnxMbgPgwSMGTPEventCause,
       "jnxMbgPgwSMAlarmThrshld": jnxMbgPgwSMAlarmThrshld,
       "jnxMbgPgwSMAlarmState": jnxMbgPgwSMAlarmState,
       "jnxMbgPgwSMSPICName": jnxMbgPgwSMSPICName,
       "jnxMbgPgwSMTCName": jnxMbgPgwSMTCName,
       "jnxMbgPgwSMQCIName": jnxMbgPgwSMQCIName,
       "jnxMbgPgwSMSessionEstFailReason": jnxMbgPgwSMSessionEstFailReason,
       "jnxMbgPgwMMGatewayName": jnxMbgPgwMMGatewayName,
       "jnxMbgPgwPrevGatewayMMState": jnxMbgPgwPrevGatewayMMState,
       "jnxMbgPgwNewGatewayMMState": jnxMbgPgwNewGatewayMMState,
       "jnxMbgPgwAPNMMGatewayName": jnxMbgPgwAPNMMGatewayName,
       "jnxMbgPgwAPNMMAPNName": jnxMbgPgwAPNMMAPNName,
       "jnxMbgPgwPrevAPNMMState": jnxMbgPgwPrevAPNMMState,
       "jnxMbgPgwNewAPNMMState": jnxMbgPgwNewAPNMMState,
       "jnxMbgPgwTrapGwIndex": jnxMbgPgwTrapGwIndex,
       "jnxMbgPgwTrapGwName": jnxMbgPgwTrapGwName,
       "jnxMbgPgwSpicName": jnxMbgPgwSpicName,
       "jnxMbgPgwSMInterfaceName": jnxMbgPgwSMInterfaceName,
       "jnxMbgPgwSMOperStatsTable": jnxMbgPgwSMOperStatsTable,
       "jnxMbgPgwSMOperStatsEntry": jnxMbgPgwSMOperStatsEntry,
       "jnxMbgPgwSessnEstAttmpts": jnxMbgPgwSessnEstAttmpts,
       "jnxMbgPgwSuccSessnEst": jnxMbgPgwSuccSessnEst,
       "jnxMbgPgwPeerInitDeactv": jnxMbgPgwPeerInitDeactv,
       "jnxMbgPgwPeerInitSuccDeactv": jnxMbgPgwPeerInitSuccDeactv,
       "jnxMbgPgwGwInitDeactv": jnxMbgPgwGwInitDeactv,
       "jnxMbgPgwGwInitSuccDeactv": jnxMbgPgwGwInitSuccDeactv,
       "jnxMbgPgwGtpStatsGnS5S8InpPkt": jnxMbgPgwGtpStatsGnS5S8InpPkt,
       "jnxMbgPgwGtpStatsGnS5S8InpByt": jnxMbgPgwGtpStatsGnS5S8InpByt,
       "jnxMbgPgwGtpStatsGnS5S8OutPkt": jnxMbgPgwGtpStatsGnS5S8OutPkt,
       "jnxMbgPgwGtpStatsGnS5S8OutByt": jnxMbgPgwGtpStatsGnS5S8OutByt,
       "jnxMbgPgwGtpStatsGiInpPkt": jnxMbgPgwGtpStatsGiInpPkt,
       "jnxMbgPgwGtpStatsGiInpByt": jnxMbgPgwGtpStatsGiInpByt,
       "jnxMbgPgwGtpStatsGiOutPkt": jnxMbgPgwGtpStatsGiOutPkt,
       "jnxMbgPgwGtpStatsGiOutByt": jnxMbgPgwGtpStatsGiOutByt,
       "jnxMbgPgwGtpStatsS58DscrdPkts": jnxMbgPgwGtpStatsS58DscrdPkts,
       "jnxMbgPgwGtpStatsGiDiscrdPkts": jnxMbgPgwGtpStatsGiDiscrdPkts,
       "jnxMbgPgwSrcAddrViolationPkts": jnxMbgPgwSrcAddrViolationPkts,
       "jnxMbgPgwSrcAddrViolationByts": jnxMbgPgwSrcAddrViolationByts,
       "jnxMbgPgwPktsRcvdNonExstTeids": jnxMbgPgwPktsRcvdNonExstTeids,
       "jnxMbgPgwGtpErrLenPkts": jnxMbgPgwGtpErrLenPkts,
       "jnxMbgPgwNonExstUeAddrPkts": jnxMbgPgwNonExstUeAddrPkts,
       "jnxMbgPgwSessEstDynPolAttempt": jnxMbgPgwSessEstDynPolAttempt,
       "jnxMbgPgwSuccSessEstDynPol": jnxMbgPgwSuccSessEstDynPol,
       "jnxMbgPgwDedBrActAttempt": jnxMbgPgwDedBrActAttempt,
       "jnxMbgPgwSuccDedBrAct": jnxMbgPgwSuccDedBrAct,
       "jnxMbgPgwMsInitDedBrDeact": jnxMbgPgwMsInitDedBrDeact,
       "jnxMbgPgwGwInitDedBrDeact": jnxMbgPgwGwInitDedBrDeact,
       "jnxMbgPgwPcrfInitDedBrDeact": jnxMbgPgwPcrfInitDedBrDeact,
       "jnxMbgPgwMsInitModAttempt": jnxMbgPgwMsInitModAttempt,
       "jnxMbgPgwSuccMsInitMod": jnxMbgPgwSuccMsInitMod,
       "jnxMbgPgwGwInitModAttempt": jnxMbgPgwGwInitModAttempt,
       "jnxMbgPgwSuccGwInitMod": jnxMbgPgwSuccGwInitMod,
       "jnxMbgPgwMsInitDedBrActAttempt": jnxMbgPgwMsInitDedBrActAttempt,
       "jnxMbgPgwSuccMsInitDedBrAct": jnxMbgPgwSuccMsInitDedBrAct,
       "jnxMbgPgwNwInitDedBrActAttempt": jnxMbgPgwNwInitDedBrActAttempt,
       "jnxMbgPgwSuccNwInitDedBrAct": jnxMbgPgwSuccNwInitDedBrAct,
       "jnxMbgPgwMsInitDedBrModAttempt": jnxMbgPgwMsInitDedBrModAttempt,
       "jnxMbgPgwSuccMsInitDedBrMod": jnxMbgPgwSuccMsInitDedBrMod,
       "jnxMbgPgwNwInitDedBrModAttempt": jnxMbgPgwNwInitDedBrModAttempt,
       "jnxMbgPgwSuccNwInitDedBrMod": jnxMbgPgwSuccNwInitDedBrMod,
       "jnxMbgPgwInterRatHoAttempt": jnxMbgPgwInterRatHoAttempt,
       "jnxMbgPgwInterRatHoSucc": jnxMbgPgwInterRatHoSucc,
       "jnxMbgPgwIntraRatHoAttempt": jnxMbgPgwIntraRatHoAttempt,
       "jnxMbgPgwIntraRatHoSucc": jnxMbgPgwIntraRatHoSucc,
       "jnxMbgPgwCdrsAllocd": jnxMbgPgwCdrsAllocd,
       "jnxMbgPgwPartialCdrsAllocd": jnxMbgPgwPartialCdrsAllocd,
       "jnxMbgPgwCdrsClosed": jnxMbgPgwCdrsClosed,
       "jnxMbgPgwCdrCntainrsClosed": jnxMbgPgwCdrCntainrsClosed,
       "jnxMbgPgwGySessEstAttempt": jnxMbgPgwGySessEstAttempt,
       "jnxMbgPgwGySuccSessEst": jnxMbgPgwGySuccSessEst,
       "jnxMbgPgwGyReauthAttempt": jnxMbgPgwGyReauthAttempt,
       "jnxMbgPgwGySuccReauth": jnxMbgPgwGySuccReauth,
       "jnxMbgPgwGyAuthTimeout": jnxMbgPgwGyAuthTimeout,
       "jnxMbgPgwGyMsInitSessDeact": jnxMbgPgwGyMsInitSessDeact,
       "jnxMbgPgwGyOcsInitSessDeact": jnxMbgPgwGyOcsInitSessDeact,
       "jnxMbgPgwGyGwInitSessDeact": jnxMbgPgwGyGwInitSessDeact,
       "jnxMbgPgwGxMsInitMod": jnxMbgPgwGxMsInitMod,
       "jnxMbgPgwGxSuccMsInitMod": jnxMbgPgwGxSuccMsInitMod,
       "jnxMbgPgwGxPcrfInitMod": jnxMbgPgwGxPcrfInitMod,
       "jnxMbgPgwGxSuccPcrfInitMod": jnxMbgPgwGxSuccPcrfInitMod,
       "jnxMbgPgwGxMsInitSessTerm": jnxMbgPgwGxMsInitSessTerm,
       "jnxMbgPgwGxPcrfInitSessTerm": jnxMbgPgwGxPcrfInitSessTerm,
       "jnxMbgPgwGxGwInitSessTerm": jnxMbgPgwGxGwInitSessTerm,
       "jnxMbgPgwSMStatusTable": jnxMbgPgwSMStatusTable,
       "jnxMbgPgwSMStatusEntry": jnxMbgPgwSMStatusEntry,
       "jnxMbgPgwActvSubscribers": jnxMbgPgwActvSubscribers,
       "jnxMbgPgwActvSessions": jnxMbgPgwActvSessions,
       "jnxMbgPgwActvBearers": jnxMbgPgwActvBearers,
       "jnxMbgPgwIdleSubscribers": jnxMbgPgwIdleSubscribers,
       "jnxMbgPgwIdleSessions": jnxMbgPgwIdleSessions,
       "jnxMbgPgwIdleBearers": jnxMbgPgwIdleBearers,
       "jnxMbgPgwSuspSubscribers": jnxMbgPgwSuspSubscribers,
       "jnxMbgPgwSuspSessions": jnxMbgPgwSuspSessions,
       "jnxMbgPgwSuspBearers": jnxMbgPgwSuspBearers,
       "jnxMbgPgwCPUUtil": jnxMbgPgwCPUUtil,
       "jnxMbgPgwMemoryUtil": jnxMbgPgwMemoryUtil,
       "jnxMbgPgwActvPrepaidBearers": jnxMbgPgwActvPrepaidBearers,
       "jnxMbgPgwActvPostpaidBearers": jnxMbgPgwActvPostpaidBearers,
       "jnxMbgPgwActvGbrBearers": jnxMbgPgwActvGbrBearers,
       "jnxMbgPgwActvNonGbrBearers": jnxMbgPgwActvNonGbrBearers,
       "jnxMbgPgwApnSMStatsTable": jnxMbgPgwApnSMStatsTable,
       "jnxMbgPgwApnSMStatsEntry": jnxMbgPgwApnSMStatsEntry,
       "jnxMbgPgwApnName": jnxMbgPgwApnName,
       "jnxMbgPgwApnSessnEstAttmpts": jnxMbgPgwApnSessnEstAttmpts,
       "jnxMbgPgwApnSuccSessnEst": jnxMbgPgwApnSuccSessnEst,
       "jnxMbgPgwApnPeerInitDeactv": jnxMbgPgwApnPeerInitDeactv,
       "jnxMbgPgwApnPeerInitSuccDeactv": jnxMbgPgwApnPeerInitSuccDeactv,
       "jnxMbgPgwApnGwInitDeactv": jnxMbgPgwApnGwInitDeactv,
       "jnxMbgPgwApnGwInitSuccDeactv": jnxMbgPgwApnGwInitSuccDeactv,
       "jnxMbgPgwApnGtpStatsGnS5S8InpPkt": jnxMbgPgwApnGtpStatsGnS5S8InpPkt,
       "jnxMbgPgwApnGtpStatsGnS5S8InpByt": jnxMbgPgwApnGtpStatsGnS5S8InpByt,
       "jnxMbgPgwApnGtpStatsGnS5S8OutPkt": jnxMbgPgwApnGtpStatsGnS5S8OutPkt,
       "jnxMbgPgwApnGtpStatsGnS5S8OutByt": jnxMbgPgwApnGtpStatsGnS5S8OutByt,
       "jnxMbgPgwApnGtpStatsGiInpPkt": jnxMbgPgwApnGtpStatsGiInpPkt,
       "jnxMbgPgwApnGtpStatsGiInpByt": jnxMbgPgwApnGtpStatsGiInpByt,
       "jnxMbgPgwApnGtpStatsGiOutPkt": jnxMbgPgwApnGtpStatsGiOutPkt,
       "jnxMbgPgwApnGtpStatsGiOutByt": jnxMbgPgwApnGtpStatsGiOutByt,
       "jnxMbgPgwApnSessnFailSrvcUnaval": jnxMbgPgwApnSessnFailSrvcUnaval,
       "jnxMbgPgwApnSessnFailSysFailure": jnxMbgPgwApnSessnFailSysFailure,
       "jnxMbgPgwApnSessnFailNoResource": jnxMbgPgwApnSessnFailNoResource,
       "jnxMbgPgwApnSessnFailNoAddr": jnxMbgPgwApnSessnFailNoAddr,
       "jnxMbgPgwApnSessnFailSrvcDenied": jnxMbgPgwApnSessnFailSrvcDenied,
       "jnxMbgPgwApnSessnFailAuthFailed": jnxMbgPgwApnSessnFailAuthFailed,
       "jnxMbgPgwApnSessnFailAccsDenied": jnxMbgPgwApnSessnFailAccsDenied,
       "jnxMbgPgwApnMSInitModAttmpts": jnxMbgPgwApnMSInitModAttmpts,
       "jnxMbgPgwApnSuccMSInitMod": jnxMbgPgwApnSuccMSInitMod,
       "jnxMbgPgwApnPgwGgsnInitMod": jnxMbgPgwApnPgwGgsnInitMod,
       "jnxMbgPgwApnSuccPgwGgsnInitMod": jnxMbgPgwApnSuccPgwGgsnInitMod,
       "jnxMbgPgwApnUsrAuthAttmpts": jnxMbgPgwApnUsrAuthAttmpts,
       "jnxMbgPgwApnSuccUsrAuth": jnxMbgPgwApnSuccUsrAuth,
       "jnxMbgPgwApnFailUsrAuth": jnxMbgPgwApnFailUsrAuth,
       "jnxMbgPgwApnDynIPAllocAttmpts": jnxMbgPgwApnDynIPAllocAttmpts,
       "jnxMbgPgwApnSuccDynIPAlloc": jnxMbgPgwApnSuccDynIPAlloc,
       "jnxMbgPgwApnCdrsAllocd": jnxMbgPgwApnCdrsAllocd,
       "jnxMbgPgwApnPartialCdrsAllocd": jnxMbgPgwApnPartialCdrsAllocd,
       "jnxMbgPgwApnCdrsClosed": jnxMbgPgwApnCdrsClosed,
       "jnxMbgPgwApnCdrCntainrsClosed": jnxMbgPgwApnCdrCntainrsClosed,
       "jnxMbgPgwApnPktsViolMIFAcl": jnxMbgPgwApnPktsViolMIFAcl,
       "jnxMbgPgwApnReDrctMblToMblPkts": jnxMbgPgwApnReDrctMblToMblPkts,
       "jnxMbgPgwApnReDrctMblToMblByts": jnxMbgPgwApnReDrctMblToMblByts,
       "jnxMbgPgwApnIpv6RsRcvd": jnxMbgPgwApnIpv6RsRcvd,
       "jnxMbgPgwApnIpv6RaTxd": jnxMbgPgwApnIpv6RaTxd,
       "jnxMbgPgwApnIpv6NsRcvd": jnxMbgPgwApnIpv6NsRcvd,
       "jnxMbgPgwApnIpv6NaTxd": jnxMbgPgwApnIpv6NaTxd,
       "jnxMbgPgwApnSessnFailOther": jnxMbgPgwApnSessnFailOther,
       "jnxMbgPgwApnGtpStatsS58DscrdPkts": jnxMbgPgwApnGtpStatsS58DscrdPkts,
       "jnxMbgPgwApnGtpStatsGiDiscrdPkts": jnxMbgPgwApnGtpStatsGiDiscrdPkts,
       "jnxMbgPgwApnSessEstDynPolAttempt": jnxMbgPgwApnSessEstDynPolAttempt,
       "jnxMbgPgwApnSuccSessEstDynPol": jnxMbgPgwApnSuccSessEstDynPol,
       "jnxMbgPgwApnSessEstStaPolAttempt": jnxMbgPgwApnSessEstStaPolAttempt,
       "jnxMbgPgwApnSuccSessEstStaPol": jnxMbgPgwApnSuccSessEstStaPol,
       "jnxMbgPgwApnMsInitAmbrModReq": jnxMbgPgwApnMsInitAmbrModReq,
       "jnxMbgPgwApnMsInitAmbrModSucc": jnxMbgPgwApnMsInitAmbrModSucc,
       "jnxMbgPgwApnMsInitQoSModReq": jnxMbgPgwApnMsInitQoSModReq,
       "jnxMbgPgwApnMsInitQoSModSucc": jnxMbgPgwApnMsInitQoSModSucc,
       "jnxMbgPgwApnPcrfInitSessTerm": jnxMbgPgwApnPcrfInitSessTerm,
       "jnxMbgPgwApnGwInitSessTerm": jnxMbgPgwApnGwInitSessTerm,
       "jnxMbgPgwApnMsInitSessTerm": jnxMbgPgwApnMsInitSessTerm,
       "jnxMbgPgwApnMsInitSessModTrgr": jnxMbgPgwApnMsInitSessModTrgr,
       "jnxMbgPgwApnMsInitSessModSucc": jnxMbgPgwApnMsInitSessModSucc,
       "jnxMbgPgwApnPcrfInitSessModTrgr": jnxMbgPgwApnPcrfInitSessModTrgr,
       "jnxMbgPgwApnPcrfInitSessModSucc": jnxMbgPgwApnPcrfInitSessModSucc,
       "jnxMbgPgwApnSessModTrgrQoSChg": jnxMbgPgwApnSessModTrgrQoSChg,
       "jnxMbgPgwApnSessModTrgrRatChg": jnxMbgPgwApnSessModTrgrRatChg,
       "jnxMbgPgwApnSessModTrgrSgsnChg": jnxMbgPgwApnSessModTrgrSgsnChg,
       "jnxMbgPgwApnSessModTrgrSgwChg": jnxMbgPgwApnSessModTrgrSgwChg,
       "jnxMbgPgwApnSessModTrgrPlmnChg": jnxMbgPgwApnSessModTrgrPlmnChg,
       "jnxMbgPgwApnSessModTrgrRaiChg": jnxMbgPgwApnSessModTrgrRaiChg,
       "jnxMbgPgwApnSessModTrgrUliChg": jnxMbgPgwApnSessModTrgrUliChg,
       "jnxMbgPgwApnSessModTrgrIPCanChg": jnxMbgPgwApnSessModTrgrIPCanChg,
       "jnxMbgPgwApnMsInitSessModTftChg": jnxMbgPgwApnMsInitSessModTftChg,
       "jnxMbgPgwApnNwInitSessModTftChg": jnxMbgPgwApnNwInitSessModTftChg,
       "jnxMbgPgwApnSessModTrgrBrLoss": jnxMbgPgwApnSessModTrgrBrLoss,
       "jnxMbgPgwApnSessModTrgrBrRecvry": jnxMbgPgwApnSessModTrgrBrRecvry,
       "jnxMbgPgwApnSessModTrgrRsrAlloc": jnxMbgPgwApnSessModTrgrRsrAlloc,
       "jnxMbgPgwApnSessModTrgrRevldTO": jnxMbgPgwApnSessModTrgrRevldTO,
       "jnxMbgPgwApnSessModQoSExceedAuth": jnxMbgPgwApnSessModQoSExceedAuth,
       "jnxMbgPgwApnSessModTodProc": jnxMbgPgwApnSessModTodProc,
       "jnxMbgPgwApnSessModTrgrChgSubsc": jnxMbgPgwApnSessModTrgrChgSubsc,
       "jnxMbgPgwApnSessModAmbrChg": jnxMbgPgwApnSessModAmbrChg,
       "jnxMbgPgwApnSessModEcgiChg": jnxMbgPgwApnSessModEcgiChg,
       "jnxMbgPgwApnSessModTaiChg": jnxMbgPgwApnSessModTaiChg,
       "jnxMbgPgwApnSessModMsTimezoneChg": jnxMbgPgwApnSessModMsTimezoneChg,
       "jnxMbgPgwApnSessModDefQosChg": jnxMbgPgwApnSessModDefQosChg,
       "jnxMbgPgwApnMsDedBrActAttempt": jnxMbgPgwApnMsDedBrActAttempt,
       "jnxMbgPgwApnMsDedBrActSucc": jnxMbgPgwApnMsDedBrActSucc,
       "jnxMbgPgwApnNwDedBrActAttempt": jnxMbgPgwApnNwDedBrActAttempt,
       "jnxMbgPgwApnNwDedBrActSucc": jnxMbgPgwApnNwDedBrActSucc,
       "jnxMbgPgwApnMsDedBrModAttempt": jnxMbgPgwApnMsDedBrModAttempt,
       "jnxMbgPgwApnMsDedBrModSucc": jnxMbgPgwApnMsDedBrModSucc,
       "jnxMbgPgwApnNwDedBrModAttempt": jnxMbgPgwApnNwDedBrModAttempt,
       "jnxMbgPgwApnNwDedBrModSucc": jnxMbgPgwApnNwDedBrModSucc,
       "jnxMbgPgwApnMsDedBrDeactAttempt": jnxMbgPgwApnMsDedBrDeactAttempt,
       "jnxMbgPgwApnNwDedBrDeactAttempt": jnxMbgPgwApnNwDedBrDeactAttempt,
       "jnxMbgPgwApnGwDedBrDeactAttempt": jnxMbgPgwApnGwDedBrDeactAttempt,
       "jnxMbgPgwApnGbrDedBrCrtFailCAC": jnxMbgPgwApnGbrDedBrCrtFailCAC,
       "jnxMbgPgwApnNGbrDedBrCrtFailCAC": jnxMbgPgwApnNGbrDedBrCrtFailCAC,
       "jnxMbgPgwApnSessTermUnreachPcrf": jnxMbgPgwApnSessTermUnreachPcrf,
       "jnxMbgPgwApnSessTermPcrfRestart": jnxMbgPgwApnSessTermPcrfRestart,
       "jnxMbgPgwApnGxCcrISent": jnxMbgPgwApnGxCcrISent,
       "jnxMbgPgwApnGxCcaIRcvd": jnxMbgPgwApnGxCcaIRcvd,
       "jnxMbgPgwApnGxCcrUSent": jnxMbgPgwApnGxCcrUSent,
       "jnxMbgPgwApnGxCcaURcvd": jnxMbgPgwApnGxCcaURcvd,
       "jnxMbgPgwApnGxCcrTSent": jnxMbgPgwApnGxCcrTSent,
       "jnxMbgPgwApnGxCcaTRcvd": jnxMbgPgwApnGxCcaTRcvd,
       "jnxMbgPgwApnGxRarRcvd": jnxMbgPgwApnGxRarRcvd,
       "jnxMbgPgwApnGxRaaSent": jnxMbgPgwApnGxRaaSent,
       "jnxMbgPgwApnGxRaaSentRsrFail": jnxMbgPgwApnGxRaaSentRsrFail,
       "jnxMbgPgwApnGxCcrRejTransntFail": jnxMbgPgwApnGxCcrRejTransntFail,
       "jnxMbgPgwApnGxCcrRejInitlParErr": jnxMbgPgwApnGxCcrRejInitlParErr,
       "jnxMbgPgwApnGxCcrRejPermFail": jnxMbgPgwApnGxCcrRejPermFail,
       "jnxMbgPgwApnGxCcrRejUknCode": jnxMbgPgwApnGxCcrRejUknCode,
       "jnxMbgPgwApnGxCcrRejUknSess": jnxMbgPgwApnGxCcrRejUknSess,
       "jnxMbgPgwApnPccActiveDynRules": jnxMbgPgwApnPccActiveDynRules,
       "jnxMbgPgwApnPccDynRuleDeact": jnxMbgPgwApnPccDynRuleDeact,
       "jnxMbgPgwApnPccRuleStaticAct": jnxMbgPgwApnPccRuleStaticAct,
       "jnxMbgPgwApnPccRuleStaticDeact": jnxMbgPgwApnPccRuleStaticDeact,
       "jnxMbgPgwApnPccRuleDynMod": jnxMbgPgwApnPccRuleDynMod,
       "jnxMbgPgwApnPccRuleValidnFail": jnxMbgPgwApnPccRuleValidnFail,
       "jnxMbgPgwApnPccRuleEnforceFail": jnxMbgPgwApnPccRuleEnforceFail,
       "jnxMbgPgwApnPccActFailNoRsr": jnxMbgPgwApnPccActFailNoRsr,
       "jnxMbgPgwApnPccRuleUpdProcFail": jnxMbgPgwApnPccRuleUpdProcFail,
       "jnxMbgPgwApnInterRatHoAttempt": jnxMbgPgwApnInterRatHoAttempt,
       "jnxMbgPgwApnInterRatHoSucc": jnxMbgPgwApnInterRatHoSucc,
       "jnxMbgPgwApnIntraRatHoAttempt": jnxMbgPgwApnIntraRatHoAttempt,
       "jnxMbgPgwApnIntraRatHoSucc": jnxMbgPgwApnIntraRatHoSucc,
       "jnxMbgPgwApnOnlineAuthAttempt": jnxMbgPgwApnOnlineAuthAttempt,
       "jnxMbgPgwApnOnlineAuthSucc": jnxMbgPgwApnOnlineAuthSucc,
       "jnxMbgPgwApnOnlineAuthTimeout": jnxMbgPgwApnOnlineAuthTimeout,
       "jnxMbgPgwApnOnlineQuotaThdUpdReq": jnxMbgPgwApnOnlineQuotaThdUpdReq,
       "jnxMbgPgwApnGyCcrISent": jnxMbgPgwApnGyCcrISent,
       "jnxMbgPgwApnGyCcaISucc": jnxMbgPgwApnGyCcaISucc,
       "jnxMbgPgwApnGyCcrIFail": jnxMbgPgwApnGyCcrIFail,
       "jnxMbgPgwApnGyCcrUSent": jnxMbgPgwApnGyCcrUSent,
       "jnxMbgPgwApnGyCcaUSucc": jnxMbgPgwApnGyCcaUSucc,
       "jnxMbgPgwApnGyCcrUFail": jnxMbgPgwApnGyCcrUFail,
       "jnxMbgPgwApnGyCcrTSent": jnxMbgPgwApnGyCcrTSent,
       "jnxMbgPgwApnGyCcaTSucc": jnxMbgPgwApnGyCcaTSucc,
       "jnxMbgPgwApnGyCcrTFail": jnxMbgPgwApnGyCcrTFail,
       "jnxMbgPgwApnGyRarRcvd": jnxMbgPgwApnGyRarRcvd,
       "jnxMbgPgwApnGyRaaSent": jnxMbgPgwApnGyRaaSent,
       "jnxMbgPgwApnGyRaaFail": jnxMbgPgwApnGyRaaFail,
       "jnxMbgPgwApnGyAbortSessReqRcvd": jnxMbgPgwApnGyAbortSessReqRcvd,
       "jnxMbgPgwApnGyAbortSessAnsSent": jnxMbgPgwApnGyAbortSessAnsSent,
       "jnxMbgPgwApnGyCcrRejTransntFail": jnxMbgPgwApnGyCcrRejTransntFail,
       "jnxMbgPgwApnGyCcrRejInitlParErr": jnxMbgPgwApnGyCcrRejInitlParErr,
       "jnxMbgPgwApnGyCcrRejPermFail": jnxMbgPgwApnGyCcrRejPermFail,
       "jnxMbgPgwApnGyCcrRejUknCode": jnxMbgPgwApnGyCcrRejUknCode,
       "jnxMbgPgwApnGyCcrRejUknSess": jnxMbgPgwApnGyCcrRejUknSess,
       "jnxMbgPgwApnGwAttemptedRedirect": jnxMbgPgwApnGwAttemptedRedirect,
       "jnxMbgPgwApnSuccGwRedirect": jnxMbgPgwApnSuccGwRedirect,
       "jnxMbgPgwApnSuccApnRedirect": jnxMbgPgwApnSuccApnRedirect,
       "jnxMbgPgwApnSessnFailCtxNotFound": jnxMbgPgwApnSessnFailCtxNotFound,
       "jnxMbgPgwApnGxMsInitModAttempt": jnxMbgPgwApnGxMsInitModAttempt,
       "jnxMbgPgwApnGxSuccMsInitMod": jnxMbgPgwApnGxSuccMsInitMod,
       "jnxMbgPgwApnGxPcrfInitMod": jnxMbgPgwApnGxPcrfInitMod,
       "jnxMbgPgwApnGxSuccPcrfInitMod": jnxMbgPgwApnGxSuccPcrfInitMod,
       "jnxMbgPgwApnGxMsInitSessTerm": jnxMbgPgwApnGxMsInitSessTerm,
       "jnxMbgPgwApnGxPcrfInitSessTerm": jnxMbgPgwApnGxPcrfInitSessTerm,
       "jnxMbgPgwApnGxGwInitSessTerm": jnxMbgPgwApnGxGwInitSessTerm,
       "jnxMbgPgwApnGySessEstAttempt": jnxMbgPgwApnGySessEstAttempt,
       "jnxMbgPgwApnGySuccSessEst": jnxMbgPgwApnGySuccSessEst,
       "jnxMbgPgwApnGyReauthAttempt": jnxMbgPgwApnGyReauthAttempt,
       "jnxMbgPgwApnGySuccReauth": jnxMbgPgwApnGySuccReauth,
       "jnxMbgPgwApnGyAuthTimeout": jnxMbgPgwApnGyAuthTimeout,
       "jnxMbgPgwApnGyMsInitSessDeact": jnxMbgPgwApnGyMsInitSessDeact,
       "jnxMbgPgwApnGyOcsInitSessDeact": jnxMbgPgwApnGyOcsInitSessDeact,
       "jnxMbgPgwApnGyGwInitSessDeact": jnxMbgPgwApnGyGwInitSessDeact,
       "jnxMbgPgwApnSMStatusTable": jnxMbgPgwApnSMStatusTable,
       "jnxMbgPgwApnSMStatusEntry": jnxMbgPgwApnSMStatusEntry,
       "jnxMbgPgwApnActvSubscribers": jnxMbgPgwApnActvSubscribers,
       "jnxMbgPgwApnActvSessions": jnxMbgPgwApnActvSessions,
       "jnxMbgPgwApnActvBearers": jnxMbgPgwApnActvBearers,
       "jnxMbgPgwApnActvPrepaidBearers": jnxMbgPgwApnActvPrepaidBearers,
       "jnxMbgPgwApnActvPostpaidBearers": jnxMbgPgwApnActvPostpaidBearers,
       "jnxMbgPgwApnActvGbrBearers": jnxMbgPgwApnActvGbrBearers,
       "jnxMbgPgwApnActvNonGbrBearers": jnxMbgPgwApnActvNonGbrBearers,
       "jnxMbgPgwSMClRateStatsTable": jnxMbgPgwSMClRateStatsTable,
       "jnxMbgPgwSMClRateStatsEntry": jnxMbgPgwSMClRateStatsEntry,
       "jnxMbgPgwClRateIntervalMin": jnxMbgPgwClRateIntervalMin,
       "jnxMbgPgwClRateSuccSessnEst": jnxMbgPgwClRateSuccSessnEst,
       "jnxMbgPgwClRateSuccSessnDel": jnxMbgPgwClRateSuccSessnDel,
       "jnxMbgPgwClRateStatsGnInpPkt": jnxMbgPgwClRateStatsGnInpPkt,
       "jnxMbgPgwClRateStatsGnInpByt": jnxMbgPgwClRateStatsGnInpByt,
       "jnxMbgPgwClRateStatsGnOutPkt": jnxMbgPgwClRateStatsGnOutPkt,
       "jnxMbgPgwClRateStatsGnOutByt": jnxMbgPgwClRateStatsGnOutByt,
       "jnxMbgPgwSMSpicStatusTable": jnxMbgPgwSMSpicStatusTable,
       "jnxMbgPgwSMSpicStatusEntry": jnxMbgPgwSMSpicStatusEntry,
       "jnxMbgGwFpc": jnxMbgGwFpc,
       "jnxMbgGwPic": jnxMbgGwPic,
       "jnxMbgPgwSpicStatusName": jnxMbgPgwSpicStatusName,
       "jnxMbgPgwSpicStatusState": jnxMbgPgwSpicStatusState,
       "jnxMbgPgwSpicStatusType": jnxMbgPgwSpicStatusType,
       "jnxMbgPgwSpicActvSubscribers": jnxMbgPgwSpicActvSubscribers,
       "jnxMbgPgwSpicActvSessions": jnxMbgPgwSpicActvSessions,
       "jnxMbgPgwSpicActvBearers": jnxMbgPgwSpicActvBearers,
       "jnxMbgPgwSpicCPUUtil": jnxMbgPgwSpicCPUUtil,
       "jnxMbgPgwSpicMemoryUtil": jnxMbgPgwSpicMemoryUtil,
       "jnxMbgPgwSpicActvPrepaidBearers": jnxMbgPgwSpicActvPrepaidBearers,
       "jnxMbgPgwSpicActvPostpaidBearers": jnxMbgPgwSpicActvPostpaidBearers,
       "jnxMbgPgwSpicActvGbrBearers": jnxMbgPgwSpicActvGbrBearers,
       "jnxMbgPgwSpicActvNonGbrBearers": jnxMbgPgwSpicActvNonGbrBearers,
       "jnxMbgPgwApnSMClRateStatsTable": jnxMbgPgwApnSMClRateStatsTable,
       "jnxMbgPgwApnSMClRateStatsEntry": jnxMbgPgwApnSMClRateStatsEntry,
       "jnxMbgPgwApnCRName": jnxMbgPgwApnCRName,
       "jnxMbgPgwApnCRIntervalMin": jnxMbgPgwApnCRIntervalMin,
       "jnxMbgPgwApnCRPrepaidBrAct": jnxMbgPgwApnCRPrepaidBrAct,
       "jnxMbgPgwApnCRPrepaidBrDeact": jnxMbgPgwApnCRPrepaidBrDeact,
       "jnxMbgPgwApnCRPostpaidBrAct": jnxMbgPgwApnCRPostpaidBrAct,
       "jnxMbgPgwApnCRPostpaidBrDeact": jnxMbgPgwApnCRPostpaidBrDeact,
       "jnxMbgPgwApnCROnlineAuthTimeout": jnxMbgPgwApnCROnlineAuthTimeout,
       "jnxMbgPgwApnCRQuotaThdUpdReq": jnxMbgPgwApnCRQuotaThdUpdReq,
       "jnxMbgPgwApnCROnlineRarRcvd": jnxMbgPgwApnCROnlineRarRcvd,
       "jnxMbgPgwApnCROnlineRarSucc": jnxMbgPgwApnCROnlineRarSucc}
)
