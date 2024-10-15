# SNMP MIB module (BW-OpenClientServer) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-OpenClientServer
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:09 2024
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

broadsoft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431)
)
broadsoft.setRevisions(
        ("2005-08-16 10:00",
         "2000-09-19 14:31")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadworks_ObjectIdentity = ObjectIdentity
broadworks = _Broadworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1)
)
_OpenClientServer_ObjectIdentity = ObjectIdentity
openClientServer = _OpenClientServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8)
)
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1)
)
_Cap_ObjectIdentity = ObjectIdentity
cap = _Cap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1)
)
_BwOCSCAPRegisterAuthentications_Type = Counter32
_BwOCSCAPRegisterAuthentications_Object = MibScalar
bwOCSCAPRegisterAuthentications = _BwOCSCAPRegisterAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 1),
    _BwOCSCAPRegisterAuthentications_Type()
)
bwOCSCAPRegisterAuthentications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPRegisterAuthentications.setStatus("current")
_BwOCSCAPResponseAuthentications_Type = Counter32
_BwOCSCAPResponseAuthentications_Object = MibScalar
bwOCSCAPResponseAuthentications = _BwOCSCAPResponseAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 2),
    _BwOCSCAPResponseAuthentications_Type()
)
bwOCSCAPResponseAuthentications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPResponseAuthentications.setStatus("obsolete")
_BwOCSCAPRegisterRequests_Type = Counter32
_BwOCSCAPRegisterRequests_Object = MibScalar
bwOCSCAPRegisterRequests = _BwOCSCAPRegisterRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 3),
    _BwOCSCAPRegisterRequests_Type()
)
bwOCSCAPRegisterRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPRegisterRequests.setStatus("obsolete")
_BwOCSCAPRegisterResponses_Type = Counter32
_BwOCSCAPRegisterResponses_Object = MibScalar
bwOCSCAPRegisterResponses = _BwOCSCAPRegisterResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 4),
    _BwOCSCAPRegisterResponses_Type()
)
bwOCSCAPRegisterResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPRegisterResponses.setStatus("obsolete")
_BwOCSCAPUnsuccessfulRegisterResponses_Type = Counter32
_BwOCSCAPUnsuccessfulRegisterResponses_Object = MibScalar
bwOCSCAPUnsuccessfulRegisterResponses = _BwOCSCAPUnsuccessfulRegisterResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 5),
    _BwOCSCAPUnsuccessfulRegisterResponses_Type()
)
bwOCSCAPUnsuccessfulRegisterResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPUnsuccessfulRegisterResponses.setStatus("current")
_BwOCSCAPAcknowledgements_Type = Counter32
_BwOCSCAPAcknowledgements_Object = MibScalar
bwOCSCAPAcknowledgements = _BwOCSCAPAcknowledgements_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 6),
    _BwOCSCAPAcknowledgements_Type()
)
bwOCSCAPAcknowledgements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPAcknowledgements.setStatus("current")
_BwOCSCAPUnregisterIns_Type = Counter32
_BwOCSCAPUnregisterIns_Object = MibScalar
bwOCSCAPUnregisterIns = _BwOCSCAPUnregisterIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 7),
    _BwOCSCAPUnregisterIns_Type()
)
bwOCSCAPUnregisterIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPUnregisterIns.setStatus("current")
_BwOCSCAPUnregisterOuts_Type = Counter32
_BwOCSCAPUnregisterOuts_Object = MibScalar
bwOCSCAPUnregisterOuts = _BwOCSCAPUnregisterOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 8),
    _BwOCSCAPUnregisterOuts_Type()
)
bwOCSCAPUnregisterOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPUnregisterOuts.setStatus("current")
_BwOCSCAPSessionUpdates_Type = Counter32
_BwOCSCAPSessionUpdates_Object = MibScalar
bwOCSCAPSessionUpdates = _BwOCSCAPSessionUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 9),
    _BwOCSCAPSessionUpdates_Type()
)
bwOCSCAPSessionUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPSessionUpdates.setStatus("current")
_BwOCSCAPProfileUpdates_Type = Counter32
_BwOCSCAPProfileUpdates_Object = MibScalar
bwOCSCAPProfileUpdates = _BwOCSCAPProfileUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 10),
    _BwOCSCAPProfileUpdates_Type()
)
bwOCSCAPProfileUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPProfileUpdates.setStatus("current")
_BwOCSCAPCallUpdates_Type = Counter32
_BwOCSCAPCallUpdates_Object = MibScalar
bwOCSCAPCallUpdates = _BwOCSCAPCallUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 11),
    _BwOCSCAPCallUpdates_Type()
)
bwOCSCAPCallUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPCallUpdates.setStatus("current")
_BwOCSCAPCallActions_Type = Counter32
_BwOCSCAPCallActions_Object = MibScalar
bwOCSCAPCallActions = _BwOCSCAPCallActions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 12),
    _BwOCSCAPCallActions_Type()
)
bwOCSCAPCallActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPCallActions.setStatus("current")
_BwOCSCAPCallControlInfos_Type = Counter32
_BwOCSCAPCallControlInfos_Object = MibScalar
bwOCSCAPCallControlInfos = _BwOCSCAPCallControlInfos_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 13),
    _BwOCSCAPCallControlInfos_Type()
)
bwOCSCAPCallControlInfos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPCallControlInfos.setStatus("current")
_BwOCSCAPInfoRequests_Type = Counter32
_BwOCSCAPInfoRequests_Object = MibScalar
bwOCSCAPInfoRequests = _BwOCSCAPInfoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 14),
    _BwOCSCAPInfoRequests_Type()
)
bwOCSCAPInfoRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPInfoRequests.setStatus("current")
_BwOCSCAPInfoResponses_Type = Counter32
_BwOCSCAPInfoResponses_Object = MibScalar
bwOCSCAPInfoResponses = _BwOCSCAPInfoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 15),
    _BwOCSCAPInfoResponses_Type()
)
bwOCSCAPInfoResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPInfoResponses.setStatus("current")
_BwOCSCAPServerStatusRequests_Type = Counter32
_BwOCSCAPServerStatusRequests_Object = MibScalar
bwOCSCAPServerStatusRequests = _BwOCSCAPServerStatusRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 16),
    _BwOCSCAPServerStatusRequests_Type()
)
bwOCSCAPServerStatusRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPServerStatusRequests.setStatus("current")
_BwOCSCAPExternalNotifies_Type = Counter32
_BwOCSCAPExternalNotifies_Object = MibScalar
bwOCSCAPExternalNotifies = _BwOCSCAPExternalNotifies_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 17),
    _BwOCSCAPExternalNotifies_Type()
)
bwOCSCAPExternalNotifies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPExternalNotifies.setStatus("current")
_BwOCSCAPMonitoringUsersRequests_Type = Counter32
_BwOCSCAPMonitoringUsersRequests_Object = MibScalar
bwOCSCAPMonitoringUsersRequests = _BwOCSCAPMonitoringUsersRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 18),
    _BwOCSCAPMonitoringUsersRequests_Type()
)
bwOCSCAPMonitoringUsersRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPMonitoringUsersRequests.setStatus("current")
_BwOCSCAPMonitoringUsersResponses_Type = Counter32
_BwOCSCAPMonitoringUsersResponses_Object = MibScalar
bwOCSCAPMonitoringUsersResponses = _BwOCSCAPMonitoringUsersResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 19),
    _BwOCSCAPMonitoringUsersResponses_Type()
)
bwOCSCAPMonitoringUsersResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPMonitoringUsersResponses.setStatus("current")
_BwOCSCAPStatsQueueUpdatesOut_Type = Counter32
_BwOCSCAPStatsQueueUpdatesOut_Object = MibScalar
bwOCSCAPStatsQueueUpdatesOut = _BwOCSCAPStatsQueueUpdatesOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 20),
    _BwOCSCAPStatsQueueUpdatesOut_Type()
)
bwOCSCAPStatsQueueUpdatesOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPStatsQueueUpdatesOut.setStatus("current")
_BwOCSCAPStatsQueueActionsIn_Type = Counter32
_BwOCSCAPStatsQueueActionsIn_Object = MibScalar
bwOCSCAPStatsQueueActionsIn = _BwOCSCAPStatsQueueActionsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 21),
    _BwOCSCAPStatsQueueActionsIn_Type()
)
bwOCSCAPStatsQueueActionsIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPStatsQueueActionsIn.setStatus("current")
_BwOCSCAPStatsDatagramsIn_Type = Counter32
_BwOCSCAPStatsDatagramsIn_Object = MibScalar
bwOCSCAPStatsDatagramsIn = _BwOCSCAPStatsDatagramsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 22),
    _BwOCSCAPStatsDatagramsIn_Type()
)
bwOCSCAPStatsDatagramsIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPStatsDatagramsIn.setStatus("current")
_BwOCSCAPStatsDatagramsOut_Type = Counter32
_BwOCSCAPStatsDatagramsOut_Object = MibScalar
bwOCSCAPStatsDatagramsOut = _BwOCSCAPStatsDatagramsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 23),
    _BwOCSCAPStatsDatagramsOut_Type()
)
bwOCSCAPStatsDatagramsOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPStatsDatagramsOut.setStatus("current")
_BwOCSCAPRegisterRequestIns_Type = Counter32
_BwOCSCAPRegisterRequestIns_Object = MibScalar
bwOCSCAPRegisterRequestIns = _BwOCSCAPRegisterRequestIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 24),
    _BwOCSCAPRegisterRequestIns_Type()
)
bwOCSCAPRegisterRequestIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPRegisterRequestIns.setStatus("current")
_BwOCSCAPRegisterRequestOuts_Type = Counter32
_BwOCSCAPRegisterRequestOuts_Object = MibScalar
bwOCSCAPRegisterRequestOuts = _BwOCSCAPRegisterRequestOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 25),
    _BwOCSCAPRegisterRequestOuts_Type()
)
bwOCSCAPRegisterRequestOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPRegisterRequestOuts.setStatus("current")
_BwOCSCAPResponseAuthenticationIns_Type = Counter32
_BwOCSCAPResponseAuthenticationIns_Object = MibScalar
bwOCSCAPResponseAuthenticationIns = _BwOCSCAPResponseAuthenticationIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 26),
    _BwOCSCAPResponseAuthenticationIns_Type()
)
bwOCSCAPResponseAuthenticationIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPResponseAuthenticationIns.setStatus("current")
_BwOCSCAPResponseAuthenticationOuts_Type = Counter32
_BwOCSCAPResponseAuthenticationOuts_Object = MibScalar
bwOCSCAPResponseAuthenticationOuts = _BwOCSCAPResponseAuthenticationOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 1, 27),
    _BwOCSCAPResponseAuthenticationOuts_Type()
)
bwOCSCAPResponseAuthenticationOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCAPResponseAuthenticationOuts.setStatus("current")
_Oss_ObjectIdentity = ObjectIdentity
oss = _Oss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2)
)
_BwOCSOSSRequestAuthentications_Type = Counter32
_BwOCSOSSRequestAuthentications_Object = MibScalar
bwOCSOSSRequestAuthentications = _BwOCSOSSRequestAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 1),
    _BwOCSOSSRequestAuthentications_Type()
)
bwOCSOSSRequestAuthentications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSRequestAuthentications.setStatus("obsolete")
_BwOCSOSSResponseAuthentications_Type = Counter32
_BwOCSOSSResponseAuthentications_Object = MibScalar
bwOCSOSSResponseAuthentications = _BwOCSOSSResponseAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 2),
    _BwOCSOSSResponseAuthentications_Type()
)
bwOCSOSSResponseAuthentications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSResponseAuthentications.setStatus("obsolete")
_BwOCSOSSRequestLogins_Type = Counter32
_BwOCSOSSRequestLogins_Object = MibScalar
bwOCSOSSRequestLogins = _BwOCSOSSRequestLogins_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 3),
    _BwOCSOSSRequestLogins_Type()
)
bwOCSOSSRequestLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSRequestLogins.setStatus("obsolete")
_BwOCSOSSResponseLogins_Type = Counter32
_BwOCSOSSResponseLogins_Object = MibScalar
bwOCSOSSResponseLogins = _BwOCSOSSResponseLogins_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 4),
    _BwOCSOSSResponseLogins_Type()
)
bwOCSOSSResponseLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSResponseLogins.setStatus("obsolete")
_BwOCSOSSUnsuccessfulResponseLogins_Type = Counter32
_BwOCSOSSUnsuccessfulResponseLogins_Object = MibScalar
bwOCSOSSUnsuccessfulResponseLogins = _BwOCSOSSUnsuccessfulResponseLogins_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 5),
    _BwOCSOSSUnsuccessfulResponseLogins_Type()
)
bwOCSOSSUnsuccessfulResponseLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSUnsuccessfulResponseLogins.setStatus("obsolete")
_BwOCSOSSRequestLogoutIns_Type = Counter32
_BwOCSOSSRequestLogoutIns_Object = MibScalar
bwOCSOSSRequestLogoutIns = _BwOCSOSSRequestLogoutIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 6),
    _BwOCSOSSRequestLogoutIns_Type()
)
bwOCSOSSRequestLogoutIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSRequestLogoutIns.setStatus("obsolete")
_BwOCSOSSRequestLogoutOuts_Type = Counter32
_BwOCSOSSRequestLogoutOuts_Object = MibScalar
bwOCSOSSRequestLogoutOuts = _BwOCSOSSRequestLogoutOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 7),
    _BwOCSOSSRequestLogoutOuts_Type()
)
bwOCSOSSRequestLogoutOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSRequestLogoutOuts.setStatus("obsolete")
_BwOCSOSSRequests_Type = Counter32
_BwOCSOSSRequests_Object = MibScalar
bwOCSOSSRequests = _BwOCSOSSRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 8),
    _BwOCSOSSRequests_Type()
)
bwOCSOSSRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSRequests.setStatus("obsolete")
_BwOCSOSSResponses_Type = Counter32
_BwOCSOSSResponses_Object = MibScalar
bwOCSOSSResponses = _BwOCSOSSResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 9),
    _BwOCSOSSResponses_Type()
)
bwOCSOSSResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSResponses.setStatus("obsolete")
_BwOCSOSSResponseAuthenticationOuts_Type = Counter32
_BwOCSOSSResponseAuthenticationOuts_Object = MibScalar
bwOCSOSSResponseAuthenticationOuts = _BwOCSOSSResponseAuthenticationOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 10),
    _BwOCSOSSResponseAuthenticationOuts_Type()
)
bwOCSOSSResponseAuthenticationOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSResponseAuthenticationOuts.setStatus("obsolete")
_BwOCSOSSResponseAuthenticationIns_Type = Counter32
_BwOCSOSSResponseAuthenticationIns_Object = MibScalar
bwOCSOSSResponseAuthenticationIns = _BwOCSOSSResponseAuthenticationIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 2, 11),
    _BwOCSOSSResponseAuthenticationIns_Type()
)
bwOCSOSSResponseAuthenticationIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOSSResponseAuthenticationIns.setStatus("obsolete")
_Nsoss_ObjectIdentity = ObjectIdentity
nsoss = _Nsoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3)
)
_BwOCSNSOSSRequestAuthentications_Type = Counter32
_BwOCSNSOSSRequestAuthentications_Object = MibScalar
bwOCSNSOSSRequestAuthentications = _BwOCSNSOSSRequestAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 1),
    _BwOCSNSOSSRequestAuthentications_Type()
)
bwOCSNSOSSRequestAuthentications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSRequestAuthentications.setStatus("current")
_BwOCSNSOSSResponseAuthentications_Type = Counter32
_BwOCSNSOSSResponseAuthentications_Object = MibScalar
bwOCSNSOSSResponseAuthentications = _BwOCSNSOSSResponseAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 2),
    _BwOCSNSOSSResponseAuthentications_Type()
)
bwOCSNSOSSResponseAuthentications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSResponseAuthentications.setStatus("obsolete")
_BwOCSNSOSSRequestLogins_Type = Counter32
_BwOCSNSOSSRequestLogins_Object = MibScalar
bwOCSNSOSSRequestLogins = _BwOCSNSOSSRequestLogins_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 3),
    _BwOCSNSOSSRequestLogins_Type()
)
bwOCSNSOSSRequestLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSRequestLogins.setStatus("current")
_BwOCSNSOSSResponseLogins_Type = Counter32
_BwOCSNSOSSResponseLogins_Object = MibScalar
bwOCSNSOSSResponseLogins = _BwOCSNSOSSResponseLogins_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 4),
    _BwOCSNSOSSResponseLogins_Type()
)
bwOCSNSOSSResponseLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSResponseLogins.setStatus("current")
_BwOCSNSOSSUnsuccessfulResponseLogins_Type = Counter32
_BwOCSNSOSSUnsuccessfulResponseLogins_Object = MibScalar
bwOCSNSOSSUnsuccessfulResponseLogins = _BwOCSNSOSSUnsuccessfulResponseLogins_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 5),
    _BwOCSNSOSSUnsuccessfulResponseLogins_Type()
)
bwOCSNSOSSUnsuccessfulResponseLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSUnsuccessfulResponseLogins.setStatus("current")
_BwOCSNSOSSRequestLogoutIns_Type = Counter32
_BwOCSNSOSSRequestLogoutIns_Object = MibScalar
bwOCSNSOSSRequestLogoutIns = _BwOCSNSOSSRequestLogoutIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 6),
    _BwOCSNSOSSRequestLogoutIns_Type()
)
bwOCSNSOSSRequestLogoutIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSRequestLogoutIns.setStatus("current")
_BwOCSNSOSSRequestLogoutOuts_Type = Counter32
_BwOCSNSOSSRequestLogoutOuts_Object = MibScalar
bwOCSNSOSSRequestLogoutOuts = _BwOCSNSOSSRequestLogoutOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 7),
    _BwOCSNSOSSRequestLogoutOuts_Type()
)
bwOCSNSOSSRequestLogoutOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSRequestLogoutOuts.setStatus("current")
_BwOCSNSOSSRequests_Type = Counter32
_BwOCSNSOSSRequests_Object = MibScalar
bwOCSNSOSSRequests = _BwOCSNSOSSRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 8),
    _BwOCSNSOSSRequests_Type()
)
bwOCSNSOSSRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSRequests.setStatus("current")
_BwOCSNSOSSResponses_Type = Counter32
_BwOCSNSOSSResponses_Object = MibScalar
bwOCSNSOSSResponses = _BwOCSNSOSSResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 9),
    _BwOCSNSOSSResponses_Type()
)
bwOCSNSOSSResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSResponses.setStatus("current")
_BwOCSNSOSSResponseAuthenticationOuts_Type = Counter32
_BwOCSNSOSSResponseAuthenticationOuts_Object = MibScalar
bwOCSNSOSSResponseAuthenticationOuts = _BwOCSNSOSSResponseAuthenticationOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 10),
    _BwOCSNSOSSResponseAuthenticationOuts_Type()
)
bwOCSNSOSSResponseAuthenticationOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSResponseAuthenticationOuts.setStatus("current")
_BwOCSNSOSSResponseAuthenticationIns_Type = Counter32
_BwOCSNSOSSResponseAuthenticationIns_Object = MibScalar
bwOCSNSOSSResponseAuthenticationIns = _BwOCSNSOSSResponseAuthenticationIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 3, 11),
    _BwOCSNSOSSResponseAuthenticationIns_Type()
)
bwOCSNSOSSResponseAuthenticationIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSNSOSSResponseAuthenticationIns.setStatus("current")
_CommonComm_ObjectIdentity = ObjectIdentity
commonComm = _CommonComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4)
)
_BwOCSCommonCommStatsTable_Object = MibTable
bwOCSCommonCommStatsTable = _BwOCSCommonCommStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bwOCSCommonCommStatsTable.setStatus("current")
_BwOCSCommonCommStatsEntry_Object = MibTableRow
bwOCSCommonCommStatsEntry = _BwOCSCommonCommStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1)
)
bwOCSCommonCommStatsEntry.setIndexNames(
    (0, "BW-OpenClientServer", "bwOCSCommonCommStatsIndex"),
)
if mibBuilder.loadTexts:
    bwOCSCommonCommStatsEntry.setStatus("current")
_BwOCSCommonCommStatsIndex_Type = Unsigned32
_BwOCSCommonCommStatsIndex_Object = MibTableColumn
bwOCSCommonCommStatsIndex = _BwOCSCommonCommStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 1),
    _BwOCSCommonCommStatsIndex_Type()
)
bwOCSCommonCommStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSCommonCommStatsIndex.setStatus("current")
_BwOCSCommonCommHost_Type = DisplayString
_BwOCSCommonCommHost_Object = MibTableColumn
bwOCSCommonCommHost = _BwOCSCommonCommHost_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 2),
    _BwOCSCommonCommHost_Type()
)
bwOCSCommonCommHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSCommonCommHost.setStatus("current")
_BwOCSCommonCommInterface_Type = DisplayString
_BwOCSCommonCommInterface_Object = MibTableColumn
bwOCSCommonCommInterface = _BwOCSCommonCommInterface_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 3),
    _BwOCSCommonCommInterface_Type()
)
bwOCSCommonCommInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSCommonCommInterface.setStatus("current")
_BwOCSCommonCommProtocol_Type = DisplayString
_BwOCSCommonCommProtocol_Object = MibTableColumn
bwOCSCommonCommProtocol = _BwOCSCommonCommProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 4),
    _BwOCSCommonCommProtocol_Type()
)
bwOCSCommonCommProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSCommonCommProtocol.setStatus("current")
_BwOCSCommonCommAcceptedOutboundConnections_Type = Counter32
_BwOCSCommonCommAcceptedOutboundConnections_Object = MibTableColumn
bwOCSCommonCommAcceptedOutboundConnections = _BwOCSCommonCommAcceptedOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 5),
    _BwOCSCommonCommAcceptedOutboundConnections_Type()
)
bwOCSCommonCommAcceptedOutboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCommonCommAcceptedOutboundConnections.setStatus("current")
_BwOCSCommonCommAcceptedInboundConnections_Type = Counter32
_BwOCSCommonCommAcceptedInboundConnections_Object = MibTableColumn
bwOCSCommonCommAcceptedInboundConnections = _BwOCSCommonCommAcceptedInboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 6),
    _BwOCSCommonCommAcceptedInboundConnections_Type()
)
bwOCSCommonCommAcceptedInboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCommonCommAcceptedInboundConnections.setStatus("current")
_BwOCSCommonCommRejectedOutboundConnections_Type = Counter32
_BwOCSCommonCommRejectedOutboundConnections_Object = MibTableColumn
bwOCSCommonCommRejectedOutboundConnections = _BwOCSCommonCommRejectedOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 7),
    _BwOCSCommonCommRejectedOutboundConnections_Type()
)
bwOCSCommonCommRejectedOutboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCommonCommRejectedOutboundConnections.setStatus("current")
_BwOCSCommonCommRejectedInboundConnections_Type = Counter32
_BwOCSCommonCommRejectedInboundConnections_Object = MibTableColumn
bwOCSCommonCommRejectedInboundConnections = _BwOCSCommonCommRejectedInboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 8),
    _BwOCSCommonCommRejectedInboundConnections_Type()
)
bwOCSCommonCommRejectedInboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCommonCommRejectedInboundConnections.setStatus("current")
_BwOCSCommonCommOutputMessagesProcessed_Type = Counter32
_BwOCSCommonCommOutputMessagesProcessed_Object = MibTableColumn
bwOCSCommonCommOutputMessagesProcessed = _BwOCSCommonCommOutputMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 9),
    _BwOCSCommonCommOutputMessagesProcessed_Type()
)
bwOCSCommonCommOutputMessagesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCommonCommOutputMessagesProcessed.setStatus("current")
_BwOCSCommonCommInputMessagesProcessed_Type = Counter32
_BwOCSCommonCommInputMessagesProcessed_Object = MibTableColumn
bwOCSCommonCommInputMessagesProcessed = _BwOCSCommonCommInputMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 10),
    _BwOCSCommonCommInputMessagesProcessed_Type()
)
bwOCSCommonCommInputMessagesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCommonCommInputMessagesProcessed.setStatus("current")
_BwOCSCommonCommOutputCommunicationErrors_Type = Counter32
_BwOCSCommonCommOutputCommunicationErrors_Object = MibTableColumn
bwOCSCommonCommOutputCommunicationErrors = _BwOCSCommonCommOutputCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 11),
    _BwOCSCommonCommOutputCommunicationErrors_Type()
)
bwOCSCommonCommOutputCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCommonCommOutputCommunicationErrors.setStatus("current")
_BwOCSCommonCommInputCommunicationErrors_Type = Counter32
_BwOCSCommonCommInputCommunicationErrors_Object = MibTableColumn
bwOCSCommonCommInputCommunicationErrors = _BwOCSCommonCommInputCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 4, 1, 1, 12),
    _BwOCSCommonCommInputCommunicationErrors_Type()
)
bwOCSCommonCommInputCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSCommonCommInputCommunicationErrors.setStatus("current")
_ExtAuth_ObjectIdentity = ObjectIdentity
extAuth = _ExtAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5)
)
_BwOCSWASAuthenticationAttempts_Type = Counter32
_BwOCSWASAuthenticationAttempts_Object = MibScalar
bwOCSWASAuthenticationAttempts = _BwOCSWASAuthenticationAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5, 1),
    _BwOCSWASAuthenticationAttempts_Type()
)
bwOCSWASAuthenticationAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSWASAuthenticationAttempts.setStatus("current")
_BwOCSWASLoginAttempts_Type = Counter32
_BwOCSWASLoginAttempts_Object = MibScalar
bwOCSWASLoginAttempts = _BwOCSWASLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5, 2),
    _BwOCSWASLoginAttempts_Type()
)
bwOCSWASLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSWASLoginAttempts.setStatus("current")
_BwOCSWASCommunicationErrors_Type = Counter32
_BwOCSWASCommunicationErrors_Object = MibScalar
bwOCSWASCommunicationErrors = _BwOCSWASCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5, 3),
    _BwOCSWASCommunicationErrors_Type()
)
bwOCSWASCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSWASCommunicationErrors.setStatus("current")
_BwOCSWASProcessingErrors_Type = Counter32
_BwOCSWASProcessingErrors_Object = MibScalar
bwOCSWASProcessingErrors = _BwOCSWASProcessingErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 5, 4),
    _BwOCSWASProcessingErrors_Type()
)
bwOCSWASProcessingErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSWASProcessingErrors.setStatus("current")
_Oci_ObjectIdentity = ObjectIdentity
oci = _Oci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6)
)
_BwOCSOCIAuthenticationRequests_Type = Counter32
_BwOCSOCIAuthenticationRequests_Object = MibScalar
bwOCSOCIAuthenticationRequests = _BwOCSOCIAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 1),
    _BwOCSOCIAuthenticationRequests_Type()
)
bwOCSOCIAuthenticationRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCIAuthenticationRequests.setStatus("current")
_BwOCSOCILoginRequestIns_Type = Counter32
_BwOCSOCILoginRequestIns_Object = MibScalar
bwOCSOCILoginRequestIns = _BwOCSOCILoginRequestIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 2),
    _BwOCSOCILoginRequestIns_Type()
)
bwOCSOCILoginRequestIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCILoginRequestIns.setStatus("current")
_BwOCSOCILoginRequestOuts_Type = Counter32
_BwOCSOCILoginRequestOuts_Object = MibScalar
bwOCSOCILoginRequestOuts = _BwOCSOCILoginRequestOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 3),
    _BwOCSOCILoginRequestOuts_Type()
)
bwOCSOCILoginRequestOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCILoginRequestOuts.setStatus("current")
_BwOCSOCILoginResponses_Type = Counter32
_BwOCSOCILoginResponses_Object = MibScalar
bwOCSOCILoginResponses = _BwOCSOCILoginResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 4),
    _BwOCSOCILoginResponses_Type()
)
bwOCSOCILoginResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCILoginResponses.setStatus("current")
_BwOCSOCIUnsuccessfulLoginResponses_Type = Counter32
_BwOCSOCIUnsuccessfulLoginResponses_Object = MibScalar
bwOCSOCIUnsuccessfulLoginResponses = _BwOCSOCIUnsuccessfulLoginResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 5),
    _BwOCSOCIUnsuccessfulLoginResponses_Type()
)
bwOCSOCIUnsuccessfulLoginResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCIUnsuccessfulLoginResponses.setStatus("current")
_BwOCSOCILogoutRequestIns_Type = Counter32
_BwOCSOCILogoutRequestIns_Object = MibScalar
bwOCSOCILogoutRequestIns = _BwOCSOCILogoutRequestIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 6),
    _BwOCSOCILogoutRequestIns_Type()
)
bwOCSOCILogoutRequestIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCILogoutRequestIns.setStatus("current")
_BwOCSOCILogoutRequestOuts_Type = Counter32
_BwOCSOCILogoutRequestOuts_Object = MibScalar
bwOCSOCILogoutRequestOuts = _BwOCSOCILogoutRequestOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 7),
    _BwOCSOCILogoutRequestOuts_Type()
)
bwOCSOCILogoutRequestOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCILogoutRequestOuts.setStatus("current")
_BwOCSOCIRequests_Type = Counter32
_BwOCSOCIRequests_Object = MibScalar
bwOCSOCIRequests = _BwOCSOCIRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 8),
    _BwOCSOCIRequests_Type()
)
bwOCSOCIRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCIRequests.setStatus("current")
_BwOCSOCIResponses_Type = Counter32
_BwOCSOCIResponses_Object = MibScalar
bwOCSOCIResponses = _BwOCSOCIResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 10),
    _BwOCSOCIResponses_Type()
)
bwOCSOCIResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCIResponses.setStatus("current")
_BwOCSOCIAuthenticationResponseOuts_Type = Counter32
_BwOCSOCIAuthenticationResponseOuts_Object = MibScalar
bwOCSOCIAuthenticationResponseOuts = _BwOCSOCIAuthenticationResponseOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 11),
    _BwOCSOCIAuthenticationResponseOuts_Type()
)
bwOCSOCIAuthenticationResponseOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCIAuthenticationResponseOuts.setStatus("current")
_BwOCSOCIAuthenticationResponseIns_Type = Counter32
_BwOCSOCIAuthenticationResponseIns_Object = MibScalar
bwOCSOCIAuthenticationResponseIns = _BwOCSOCIAuthenticationResponseIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 12),
    _BwOCSOCIAuthenticationResponseIns_Type()
)
bwOCSOCIAuthenticationResponseIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCIAuthenticationResponseIns.setStatus("current")
_BwOCSOCIUserIdLoginLevelNotAllowed_Type = Counter32
_BwOCSOCIUserIdLoginLevelNotAllowed_Object = MibScalar
bwOCSOCIUserIdLoginLevelNotAllowed = _BwOCSOCIUserIdLoginLevelNotAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 13),
    _BwOCSOCIUserIdLoginLevelNotAllowed_Type()
)
bwOCSOCIUserIdLoginLevelNotAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCIUserIdLoginLevelNotAllowed.setStatus("current")
_BwOCSOCIErrorResponse_Type = Counter32
_BwOCSOCIErrorResponse_Object = MibScalar
bwOCSOCIErrorResponse = _BwOCSOCIErrorResponse_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 6, 14),
    _BwOCSOCIErrorResponse_Type()
)
bwOCSOCIErrorResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSOCIErrorResponse.setStatus("current")
_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7)
)
_BwOCSTcpServersStatsTable_Object = MibTable
bwOCSTcpServersStatsTable = _BwOCSTcpServersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1)
)
if mibBuilder.loadTexts:
    bwOCSTcpServersStatsTable.setStatus("current")
_BwOCSTcpServersStatsEntry_Object = MibTableRow
bwOCSTcpServersStatsEntry = _BwOCSTcpServersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1)
)
bwOCSTcpServersStatsEntry.setIndexNames(
    (0, "BW-OpenClientServer", "bwOCSTcpServersStatsIndex"),
)
if mibBuilder.loadTexts:
    bwOCSTcpServersStatsEntry.setStatus("current")
_BwOCSTcpServersStatsIndex_Type = Unsigned32
_BwOCSTcpServersStatsIndex_Object = MibTableColumn
bwOCSTcpServersStatsIndex = _BwOCSTcpServersStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 1),
    _BwOCSTcpServersStatsIndex_Type()
)
bwOCSTcpServersStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSTcpServersStatsIndex.setStatus("current")
_BwOCSTcpServersName_Type = DisplayString
_BwOCSTcpServersName_Object = MibTableColumn
bwOCSTcpServersName = _BwOCSTcpServersName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 2),
    _BwOCSTcpServersName_Type()
)
bwOCSTcpServersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSTcpServersName.setStatus("current")
_BwOCSTcpServersNbConnectionsAccepted_Type = Counter32
_BwOCSTcpServersNbConnectionsAccepted_Object = MibTableColumn
bwOCSTcpServersNbConnectionsAccepted = _BwOCSTcpServersNbConnectionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 3),
    _BwOCSTcpServersNbConnectionsAccepted_Type()
)
bwOCSTcpServersNbConnectionsAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSTcpServersNbConnectionsAccepted.setStatus("current")
_BwOCSTcpServersNbConnectionsRefused_Type = Counter32
_BwOCSTcpServersNbConnectionsRefused_Object = MibTableColumn
bwOCSTcpServersNbConnectionsRefused = _BwOCSTcpServersNbConnectionsRefused_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 4),
    _BwOCSTcpServersNbConnectionsRefused_Type()
)
bwOCSTcpServersNbConnectionsRefused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSTcpServersNbConnectionsRefused.setStatus("current")
_BwOCSTcpServersNbConnectionsInitiated_Type = Counter32
_BwOCSTcpServersNbConnectionsInitiated_Object = MibTableColumn
bwOCSTcpServersNbConnectionsInitiated = _BwOCSTcpServersNbConnectionsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 5),
    _BwOCSTcpServersNbConnectionsInitiated_Type()
)
bwOCSTcpServersNbConnectionsInitiated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSTcpServersNbConnectionsInitiated.setStatus("current")
_BwOCSTcpServersNbConnectionsClosed_Type = Counter32
_BwOCSTcpServersNbConnectionsClosed_Object = MibTableColumn
bwOCSTcpServersNbConnectionsClosed = _BwOCSTcpServersNbConnectionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 6),
    _BwOCSTcpServersNbConnectionsClosed_Type()
)
bwOCSTcpServersNbConnectionsClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSTcpServersNbConnectionsClosed.setStatus("current")
_BwOCSTcpServersNbBytesSent_Type = Gauge32
_BwOCSTcpServersNbBytesSent_Object = MibTableColumn
bwOCSTcpServersNbBytesSent = _BwOCSTcpServersNbBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 7),
    _BwOCSTcpServersNbBytesSent_Type()
)
bwOCSTcpServersNbBytesSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSTcpServersNbBytesSent.setStatus("current")
_BwOCSTcpServersNbBytesReceived_Type = Gauge32
_BwOCSTcpServersNbBytesReceived_Object = MibTableColumn
bwOCSTcpServersNbBytesReceived = _BwOCSTcpServersNbBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 8),
    _BwOCSTcpServersNbBytesReceived_Type()
)
bwOCSTcpServersNbBytesReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSTcpServersNbBytesReceived.setStatus("current")
_BwOCSTcpServersOutgoingQueueSize_Type = Gauge32
_BwOCSTcpServersOutgoingQueueSize_Object = MibTableColumn
bwOCSTcpServersOutgoingQueueSize = _BwOCSTcpServersOutgoingQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 9),
    _BwOCSTcpServersOutgoingQueueSize_Type()
)
bwOCSTcpServersOutgoingQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSTcpServersOutgoingQueueSize.setStatus("current")
_BwOCSTcpServersIncomingQueueSize_Type = Gauge32
_BwOCSTcpServersIncomingQueueSize_Object = MibTableColumn
bwOCSTcpServersIncomingQueueSize = _BwOCSTcpServersIncomingQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 10),
    _BwOCSTcpServersIncomingQueueSize_Type()
)
bwOCSTcpServersIncomingQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSTcpServersIncomingQueueSize.setStatus("current")
_BwOCSTcpServersNbBytesSentSecure_Type = Gauge32
_BwOCSTcpServersNbBytesSentSecure_Object = MibTableColumn
bwOCSTcpServersNbBytesSentSecure = _BwOCSTcpServersNbBytesSentSecure_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 11),
    _BwOCSTcpServersNbBytesSentSecure_Type()
)
bwOCSTcpServersNbBytesSentSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSTcpServersNbBytesSentSecure.setStatus("current")
_BwOCSTcpServersNbBytesReceivedSecure_Type = Gauge32
_BwOCSTcpServersNbBytesReceivedSecure_Object = MibTableColumn
bwOCSTcpServersNbBytesReceivedSecure = _BwOCSTcpServersNbBytesReceivedSecure_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1, 7, 1, 1, 12),
    _BwOCSTcpServersNbBytesReceivedSecure_Type()
)
bwOCSTcpServersNbBytesReceivedSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSTcpServersNbBytesReceivedSecure.setStatus("current")
_Concurrent_ObjectIdentity = ObjectIdentity
concurrent = _Concurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2)
)
_BwOCSMonitoringExecutorTable_Object = MibTable
bwOCSMonitoringExecutorTable = _BwOCSMonitoringExecutorTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorTable.setStatus("current")
_BwOCSMonitoringExecutorEntry_Object = MibTableRow
bwOCSMonitoringExecutorEntry = _BwOCSMonitoringExecutorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1)
)
bwOCSMonitoringExecutorEntry.setIndexNames(
    (0, "BW-OpenClientServer", "bwOCSMonitoringExecutorIndex"),
)
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorEntry.setStatus("current")
_BwOCSMonitoringExecutorIndex_Type = Unsigned32
_BwOCSMonitoringExecutorIndex_Object = MibTableColumn
bwOCSMonitoringExecutorIndex = _BwOCSMonitoringExecutorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 1),
    _BwOCSMonitoringExecutorIndex_Type()
)
bwOCSMonitoringExecutorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorIndex.setStatus("current")
_BwOCSMonitoringExecutorName_Type = DisplayString
_BwOCSMonitoringExecutorName_Object = MibTableColumn
bwOCSMonitoringExecutorName = _BwOCSMonitoringExecutorName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 2),
    _BwOCSMonitoringExecutorName_Type()
)
bwOCSMonitoringExecutorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorName.setStatus("current")
_BwOCSMonitoringExecutorCurrentPoolSize_Type = Gauge32
_BwOCSMonitoringExecutorCurrentPoolSize_Object = MibTableColumn
bwOCSMonitoringExecutorCurrentPoolSize = _BwOCSMonitoringExecutorCurrentPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 3),
    _BwOCSMonitoringExecutorCurrentPoolSize_Type()
)
bwOCSMonitoringExecutorCurrentPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorCurrentPoolSize.setStatus("current")
_BwOCSMonitoringExecutorMaxPoolSize_Type = Gauge32
_BwOCSMonitoringExecutorMaxPoolSize_Object = MibTableColumn
bwOCSMonitoringExecutorMaxPoolSize = _BwOCSMonitoringExecutorMaxPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 4),
    _BwOCSMonitoringExecutorMaxPoolSize_Type()
)
bwOCSMonitoringExecutorMaxPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorMaxPoolSize.setStatus("current")
_BwOCSMonitoringExecutorAvgActiveThreads_Type = Gauge32
_BwOCSMonitoringExecutorAvgActiveThreads_Object = MibTableColumn
bwOCSMonitoringExecutorAvgActiveThreads = _BwOCSMonitoringExecutorAvgActiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 5),
    _BwOCSMonitoringExecutorAvgActiveThreads_Type()
)
bwOCSMonitoringExecutorAvgActiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorAvgActiveThreads.setStatus("current")
_BwOCSMonitoringExecutorTaskQueueSize_Type = Gauge32
_BwOCSMonitoringExecutorTaskQueueSize_Object = MibTableColumn
bwOCSMonitoringExecutorTaskQueueSize = _BwOCSMonitoringExecutorTaskQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 6),
    _BwOCSMonitoringExecutorTaskQueueSize_Type()
)
bwOCSMonitoringExecutorTaskQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorTaskQueueSize.setStatus("current")
_BwOCSMonitoringExecutorNbTasksRun_Type = Counter32
_BwOCSMonitoringExecutorNbTasksRun_Object = MibTableColumn
bwOCSMonitoringExecutorNbTasksRun = _BwOCSMonitoringExecutorNbTasksRun_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 7),
    _BwOCSMonitoringExecutorNbTasksRun_Type()
)
bwOCSMonitoringExecutorNbTasksRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorNbTasksRun.setStatus("current")
_BwOCSMonitoringExecutorNbWarnings_Type = Counter32
_BwOCSMonitoringExecutorNbWarnings_Object = MibTableColumn
bwOCSMonitoringExecutorNbWarnings = _BwOCSMonitoringExecutorNbWarnings_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 8),
    _BwOCSMonitoringExecutorNbWarnings_Type()
)
bwOCSMonitoringExecutorNbWarnings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorNbWarnings.setStatus("current")
_BwOCSMonitoringExecutorNbErrors_Type = Counter32
_BwOCSMonitoringExecutorNbErrors_Object = MibTableColumn
bwOCSMonitoringExecutorNbErrors = _BwOCSMonitoringExecutorNbErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 9),
    _BwOCSMonitoringExecutorNbErrors_Type()
)
bwOCSMonitoringExecutorNbErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorNbErrors.setStatus("current")
_BwOCSMonitoringExecutorLongestTaskMs_Type = Gauge32
_BwOCSMonitoringExecutorLongestTaskMs_Object = MibTableColumn
bwOCSMonitoringExecutorLongestTaskMs = _BwOCSMonitoringExecutorLongestTaskMs_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 10),
    _BwOCSMonitoringExecutorLongestTaskMs_Type()
)
bwOCSMonitoringExecutorLongestTaskMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorLongestTaskMs.setStatus("current")
_BwOCSMonitoringExecutorLongestTaskName_Type = DisplayString
_BwOCSMonitoringExecutorLongestTaskName_Object = MibTableColumn
bwOCSMonitoringExecutorLongestTaskName = _BwOCSMonitoringExecutorLongestTaskName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 2, 1, 1, 11),
    _BwOCSMonitoringExecutorLongestTaskName_Type()
)
bwOCSMonitoringExecutorLongestTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSMonitoringExecutorLongestTaskName.setStatus("current")
_OcsReserved_ObjectIdentity = ObjectIdentity
ocsReserved = _OcsReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 999)
)
_BwOCSReserved_Type = Counter32
_BwOCSReserved_Object = MibScalar
bwOCSReserved = _BwOCSReserved_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 999, 1),
    _BwOCSReserved_Type()
)
bwOCSReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOCSReserved.setStatus("obsolete")
_BwOcsMibConformance_ObjectIdentity = ObjectIdentity
bwOcsMibConformance = _BwOcsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000)
)
_BwOcsMibGroups_ObjectIdentity = ObjectIdentity
bwOcsMibGroups = _BwOcsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1)
)
_BwOcsMibCompliancy_ObjectIdentity = ObjectIdentity
bwOcsMibCompliancy = _BwOcsMibCompliancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 2)
)

# Managed Objects groups

bwOcsCapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 1)
)
bwOcsCapGroup.setObjects(
      *(("BW-OpenClientServer", "bwOCSCAPRegisterAuthentications"),
        ("BW-OpenClientServer", "bwOCSCAPResponseAuthentications"),
        ("BW-OpenClientServer", "bwOCSCAPRegisterRequests"),
        ("BW-OpenClientServer", "bwOCSCAPUnsuccessfulRegisterResponses"),
        ("BW-OpenClientServer", "bwOCSCAPAcknowledgements"),
        ("BW-OpenClientServer", "bwOCSCAPUnregisterIns"),
        ("BW-OpenClientServer", "bwOCSCAPUnregisterOuts"),
        ("BW-OpenClientServer", "bwOCSCAPSessionUpdates"),
        ("BW-OpenClientServer", "bwOCSCAPProfileUpdates"),
        ("BW-OpenClientServer", "bwOCSCAPCallUpdates"),
        ("BW-OpenClientServer", "bwOCSCAPCallActions"),
        ("BW-OpenClientServer", "bwOCSCAPCallControlInfos"),
        ("BW-OpenClientServer", "bwOCSCAPInfoRequests"),
        ("BW-OpenClientServer", "bwOCSCAPInfoResponses"),
        ("BW-OpenClientServer", "bwOCSCAPServerStatusRequests"),
        ("BW-OpenClientServer", "bwOCSCAPExternalNotifies"),
        ("BW-OpenClientServer", "bwOCSCAPMonitoringUsersRequests"),
        ("BW-OpenClientServer", "bwOCSCAPMonitoringUsersResponses"),
        ("BW-OpenClientServer", "bwOCSCAPStatsQueueUpdatesOut"),
        ("BW-OpenClientServer", "bwOCSCAPStatsQueueActionsIn"),
        ("BW-OpenClientServer", "bwOCSCAPStatsDatagramsIn"),
        ("BW-OpenClientServer", "bwOCSCAPStatsDatagramsOut"),
        ("BW-OpenClientServer", "bwOCSCAPRegisterRequestIns"),
        ("BW-OpenClientServer", "bwOCSCAPRegisterRequestOuts"),
        ("BW-OpenClientServer", "bwOCSCAPResponseAuthenticationIns"),
        ("BW-OpenClientServer", "bwOCSCAPResponseAuthenticationOuts"))
)
if mibBuilder.loadTexts:
    bwOcsCapGroup.setStatus("current")

bwOcsAsOSSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 2)
)
bwOcsAsOSSGroup.setObjects(
      *(("BW-OpenClientServer", "bwOCSOSSRequestAuthentications"),
        ("BW-OpenClientServer", "bwOCSOSSResponseAuthentications"),
        ("BW-OpenClientServer", "bwOCSOSSRequestLogins"),
        ("BW-OpenClientServer", "bwOCSOSSResponseLogins"),
        ("BW-OpenClientServer", "bwOCSOSSUnsuccessfulResponseLogins"),
        ("BW-OpenClientServer", "bwOCSOSSRequestLogoutIns"),
        ("BW-OpenClientServer", "bwOCSOSSRequestLogoutOuts"),
        ("BW-OpenClientServer", "bwOCSOSSRequests"),
        ("BW-OpenClientServer", "bwOCSOSSResponses"),
        ("BW-OpenClientServer", "bwOCSOSSResponseAuthenticationOuts"),
        ("BW-OpenClientServer", "bwOCSOSSResponseAuthenticationIns"))
)
if mibBuilder.loadTexts:
    bwOcsAsOSSGroup.setStatus("obsolete")

bwOcsNsOSSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 3)
)
bwOcsNsOSSGroup.setObjects(
      *(("BW-OpenClientServer", "bwOCSNSOSSRequestAuthentications"),
        ("BW-OpenClientServer", "bwOCSNSOSSResponseAuthentications"),
        ("BW-OpenClientServer", "bwOCSNSOSSRequestLogins"),
        ("BW-OpenClientServer", "bwOCSNSOSSResponseLogins"),
        ("BW-OpenClientServer", "bwOCSNSOSSUnsuccessfulResponseLogins"),
        ("BW-OpenClientServer", "bwOCSNSOSSRequestLogoutIns"),
        ("BW-OpenClientServer", "bwOCSNSOSSRequestLogoutOuts"),
        ("BW-OpenClientServer", "bwOCSNSOSSRequests"),
        ("BW-OpenClientServer", "bwOCSNSOSSResponses"),
        ("BW-OpenClientServer", "bwOCSNSOSSResponseAuthenticationOuts"),
        ("BW-OpenClientServer", "bwOCSNSOSSResponseAuthenticationIns"))
)
if mibBuilder.loadTexts:
    bwOcsNsOSSGroup.setStatus("current")

bwOcsBcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 4)
)
bwOcsBcctGroup.setObjects(
      *(("BW-OpenClientServer", "bwOCSCommonCommStatsTable"),
        ("BW-OpenClientServer", "bwOCSCommonCommStatsIndex"),
        ("BW-OpenClientServer", "bwOCSCommonCommHost"),
        ("BW-OpenClientServer", "bwOCSCommonCommInterface"),
        ("BW-OpenClientServer", "bwOCSCommonCommProtocol"),
        ("BW-OpenClientServer", "bwOCSCommonCommAcceptedOutboundConnections"),
        ("BW-OpenClientServer", "bwOCSCommonCommAcceptedInboundConnections"),
        ("BW-OpenClientServer", "bwOCSCommonCommRejectedOutboundConnections"),
        ("BW-OpenClientServer", "bwOCSCommonCommRejectedInboundConnections"),
        ("BW-OpenClientServer", "bwOCSCommonCommOutputMessagesProcessed"),
        ("BW-OpenClientServer", "bwOCSCommonCommInputMessagesProcessed"),
        ("BW-OpenClientServer", "bwOCSCommonCommOutputCommunicationErrors"),
        ("BW-OpenClientServer", "bwOCSCommonCommInputCommunicationErrors"))
)
if mibBuilder.loadTexts:
    bwOcsBcctGroup.setStatus("current")

bwOcsReserveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 5)
)
bwOcsReserveGroup.setObjects(
    ("BW-OpenClientServer", "bwOCSReserved")
)
if mibBuilder.loadTexts:
    bwOcsReserveGroup.setStatus("current")

bwOcsExtAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 6)
)
bwOcsExtAuthGroup.setObjects(
      *(("BW-OpenClientServer", "bwOCSWASAuthenticationAttempts"),
        ("BW-OpenClientServer", "bwOCSWASLoginAttempts"),
        ("BW-OpenClientServer", "bwOCSWASCommunicationErrors"),
        ("BW-OpenClientServer", "bwOCSWASProcessingErrors"))
)
if mibBuilder.loadTexts:
    bwOcsExtAuthGroup.setStatus("current")

bwOcsOciAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 7)
)
bwOcsOciAuthGroup.setObjects(
      *(("BW-OpenClientServer", "bwOCSOCIAuthenticationRequests"),
        ("BW-OpenClientServer", "bwOCSOCILoginRequestIns"),
        ("BW-OpenClientServer", "bwOCSOCILoginRequestOuts"),
        ("BW-OpenClientServer", "bwOCSOCILoginResponses"),
        ("BW-OpenClientServer", "bwOCSOCIUnsuccessfulLoginResponses"),
        ("BW-OpenClientServer", "bwOCSOCILogoutRequestIns"),
        ("BW-OpenClientServer", "bwOCSOCILogoutRequestOuts"),
        ("BW-OpenClientServer", "bwOCSOCIRequests"),
        ("BW-OpenClientServer", "bwOCSOCIResponses"),
        ("BW-OpenClientServer", "bwOCSOCIAuthenticationResponseOuts"),
        ("BW-OpenClientServer", "bwOCSOCIAuthenticationResponseIns"),
        ("BW-OpenClientServer", "bwOCSOCIUserIdLoginLevelNotAllowed"),
        ("BW-OpenClientServer", "bwOCSOCIErrorResponse"))
)
if mibBuilder.loadTexts:
    bwOcsOciAuthGroup.setStatus("current")

bwOcsTcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 8)
)
bwOcsTcpStatsGroup.setObjects(
      *(("BW-OpenClientServer", "bwOCSTcpServersStatsTable"),
        ("BW-OpenClientServer", "bwOCSTcpServersStatsIndex"),
        ("BW-OpenClientServer", "bwOCSTcpServersName"),
        ("BW-OpenClientServer", "bwOCSTcpServersNbConnectionsAccepted"),
        ("BW-OpenClientServer", "bwOCSTcpServersNbConnectionsClosed"),
        ("BW-OpenClientServer", "bwOCSTcpServersOutgoingQueueSize"),
        ("BW-OpenClientServer", "bwOCSTcpServersIncomingQueueSize"))
)
if mibBuilder.loadTexts:
    bwOcsTcpStatsGroup.setStatus("current")

bwOCSConcurrentFrameworkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 1, 9)
)
bwOCSConcurrentFrameworkStatsGroup.setObjects(
      *(("BW-OpenClientServer", "bwOCSMonitoringExecutorTable"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorIndex"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorName"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorCurrentPoolSize"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorMaxPoolSize"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorAvgActiveThreads"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorTaskQueueSize"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorNbTasksRun"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorNbWarnings"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorNbErrors"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorLongestTaskMs"),
        ("BW-OpenClientServer", "bwOCSMonitoringExecutorLongestTaskName"))
)
if mibBuilder.loadTexts:
    bwOCSConcurrentFrameworkStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bwOcsBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6431, 1, 8, 1000, 2, 1)
)
if mibBuilder.loadTexts:
    bwOcsBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-OpenClientServer",
    **{"broadsoft": broadsoft,
       "broadworks": broadworks,
       "openClientServer": openClientServer,
       "protocols": protocols,
       "cap": cap,
       "bwOCSCAPRegisterAuthentications": bwOCSCAPRegisterAuthentications,
       "bwOCSCAPResponseAuthentications": bwOCSCAPResponseAuthentications,
       "bwOCSCAPRegisterRequests": bwOCSCAPRegisterRequests,
       "bwOCSCAPRegisterResponses": bwOCSCAPRegisterResponses,
       "bwOCSCAPUnsuccessfulRegisterResponses": bwOCSCAPUnsuccessfulRegisterResponses,
       "bwOCSCAPAcknowledgements": bwOCSCAPAcknowledgements,
       "bwOCSCAPUnregisterIns": bwOCSCAPUnregisterIns,
       "bwOCSCAPUnregisterOuts": bwOCSCAPUnregisterOuts,
       "bwOCSCAPSessionUpdates": bwOCSCAPSessionUpdates,
       "bwOCSCAPProfileUpdates": bwOCSCAPProfileUpdates,
       "bwOCSCAPCallUpdates": bwOCSCAPCallUpdates,
       "bwOCSCAPCallActions": bwOCSCAPCallActions,
       "bwOCSCAPCallControlInfos": bwOCSCAPCallControlInfos,
       "bwOCSCAPInfoRequests": bwOCSCAPInfoRequests,
       "bwOCSCAPInfoResponses": bwOCSCAPInfoResponses,
       "bwOCSCAPServerStatusRequests": bwOCSCAPServerStatusRequests,
       "bwOCSCAPExternalNotifies": bwOCSCAPExternalNotifies,
       "bwOCSCAPMonitoringUsersRequests": bwOCSCAPMonitoringUsersRequests,
       "bwOCSCAPMonitoringUsersResponses": bwOCSCAPMonitoringUsersResponses,
       "bwOCSCAPStatsQueueUpdatesOut": bwOCSCAPStatsQueueUpdatesOut,
       "bwOCSCAPStatsQueueActionsIn": bwOCSCAPStatsQueueActionsIn,
       "bwOCSCAPStatsDatagramsIn": bwOCSCAPStatsDatagramsIn,
       "bwOCSCAPStatsDatagramsOut": bwOCSCAPStatsDatagramsOut,
       "bwOCSCAPRegisterRequestIns": bwOCSCAPRegisterRequestIns,
       "bwOCSCAPRegisterRequestOuts": bwOCSCAPRegisterRequestOuts,
       "bwOCSCAPResponseAuthenticationIns": bwOCSCAPResponseAuthenticationIns,
       "bwOCSCAPResponseAuthenticationOuts": bwOCSCAPResponseAuthenticationOuts,
       "oss": oss,
       "bwOCSOSSRequestAuthentications": bwOCSOSSRequestAuthentications,
       "bwOCSOSSResponseAuthentications": bwOCSOSSResponseAuthentications,
       "bwOCSOSSRequestLogins": bwOCSOSSRequestLogins,
       "bwOCSOSSResponseLogins": bwOCSOSSResponseLogins,
       "bwOCSOSSUnsuccessfulResponseLogins": bwOCSOSSUnsuccessfulResponseLogins,
       "bwOCSOSSRequestLogoutIns": bwOCSOSSRequestLogoutIns,
       "bwOCSOSSRequestLogoutOuts": bwOCSOSSRequestLogoutOuts,
       "bwOCSOSSRequests": bwOCSOSSRequests,
       "bwOCSOSSResponses": bwOCSOSSResponses,
       "bwOCSOSSResponseAuthenticationOuts": bwOCSOSSResponseAuthenticationOuts,
       "bwOCSOSSResponseAuthenticationIns": bwOCSOSSResponseAuthenticationIns,
       "nsoss": nsoss,
       "bwOCSNSOSSRequestAuthentications": bwOCSNSOSSRequestAuthentications,
       "bwOCSNSOSSResponseAuthentications": bwOCSNSOSSResponseAuthentications,
       "bwOCSNSOSSRequestLogins": bwOCSNSOSSRequestLogins,
       "bwOCSNSOSSResponseLogins": bwOCSNSOSSResponseLogins,
       "bwOCSNSOSSUnsuccessfulResponseLogins": bwOCSNSOSSUnsuccessfulResponseLogins,
       "bwOCSNSOSSRequestLogoutIns": bwOCSNSOSSRequestLogoutIns,
       "bwOCSNSOSSRequestLogoutOuts": bwOCSNSOSSRequestLogoutOuts,
       "bwOCSNSOSSRequests": bwOCSNSOSSRequests,
       "bwOCSNSOSSResponses": bwOCSNSOSSResponses,
       "bwOCSNSOSSResponseAuthenticationOuts": bwOCSNSOSSResponseAuthenticationOuts,
       "bwOCSNSOSSResponseAuthenticationIns": bwOCSNSOSSResponseAuthenticationIns,
       "commonComm": commonComm,
       "bwOCSCommonCommStatsTable": bwOCSCommonCommStatsTable,
       "bwOCSCommonCommStatsEntry": bwOCSCommonCommStatsEntry,
       "bwOCSCommonCommStatsIndex": bwOCSCommonCommStatsIndex,
       "bwOCSCommonCommHost": bwOCSCommonCommHost,
       "bwOCSCommonCommInterface": bwOCSCommonCommInterface,
       "bwOCSCommonCommProtocol": bwOCSCommonCommProtocol,
       "bwOCSCommonCommAcceptedOutboundConnections": bwOCSCommonCommAcceptedOutboundConnections,
       "bwOCSCommonCommAcceptedInboundConnections": bwOCSCommonCommAcceptedInboundConnections,
       "bwOCSCommonCommRejectedOutboundConnections": bwOCSCommonCommRejectedOutboundConnections,
       "bwOCSCommonCommRejectedInboundConnections": bwOCSCommonCommRejectedInboundConnections,
       "bwOCSCommonCommOutputMessagesProcessed": bwOCSCommonCommOutputMessagesProcessed,
       "bwOCSCommonCommInputMessagesProcessed": bwOCSCommonCommInputMessagesProcessed,
       "bwOCSCommonCommOutputCommunicationErrors": bwOCSCommonCommOutputCommunicationErrors,
       "bwOCSCommonCommInputCommunicationErrors": bwOCSCommonCommInputCommunicationErrors,
       "extAuth": extAuth,
       "bwOCSWASAuthenticationAttempts": bwOCSWASAuthenticationAttempts,
       "bwOCSWASLoginAttempts": bwOCSWASLoginAttempts,
       "bwOCSWASCommunicationErrors": bwOCSWASCommunicationErrors,
       "bwOCSWASProcessingErrors": bwOCSWASProcessingErrors,
       "oci": oci,
       "bwOCSOCIAuthenticationRequests": bwOCSOCIAuthenticationRequests,
       "bwOCSOCILoginRequestIns": bwOCSOCILoginRequestIns,
       "bwOCSOCILoginRequestOuts": bwOCSOCILoginRequestOuts,
       "bwOCSOCILoginResponses": bwOCSOCILoginResponses,
       "bwOCSOCIUnsuccessfulLoginResponses": bwOCSOCIUnsuccessfulLoginResponses,
       "bwOCSOCILogoutRequestIns": bwOCSOCILogoutRequestIns,
       "bwOCSOCILogoutRequestOuts": bwOCSOCILogoutRequestOuts,
       "bwOCSOCIRequests": bwOCSOCIRequests,
       "bwOCSOCIResponses": bwOCSOCIResponses,
       "bwOCSOCIAuthenticationResponseOuts": bwOCSOCIAuthenticationResponseOuts,
       "bwOCSOCIAuthenticationResponseIns": bwOCSOCIAuthenticationResponseIns,
       "bwOCSOCIUserIdLoginLevelNotAllowed": bwOCSOCIUserIdLoginLevelNotAllowed,
       "bwOCSOCIErrorResponse": bwOCSOCIErrorResponse,
       "tcp": tcp,
       "bwOCSTcpServersStatsTable": bwOCSTcpServersStatsTable,
       "bwOCSTcpServersStatsEntry": bwOCSTcpServersStatsEntry,
       "bwOCSTcpServersStatsIndex": bwOCSTcpServersStatsIndex,
       "bwOCSTcpServersName": bwOCSTcpServersName,
       "bwOCSTcpServersNbConnectionsAccepted": bwOCSTcpServersNbConnectionsAccepted,
       "bwOCSTcpServersNbConnectionsRefused": bwOCSTcpServersNbConnectionsRefused,
       "bwOCSTcpServersNbConnectionsInitiated": bwOCSTcpServersNbConnectionsInitiated,
       "bwOCSTcpServersNbConnectionsClosed": bwOCSTcpServersNbConnectionsClosed,
       "bwOCSTcpServersNbBytesSent": bwOCSTcpServersNbBytesSent,
       "bwOCSTcpServersNbBytesReceived": bwOCSTcpServersNbBytesReceived,
       "bwOCSTcpServersOutgoingQueueSize": bwOCSTcpServersOutgoingQueueSize,
       "bwOCSTcpServersIncomingQueueSize": bwOCSTcpServersIncomingQueueSize,
       "bwOCSTcpServersNbBytesSentSecure": bwOCSTcpServersNbBytesSentSecure,
       "bwOCSTcpServersNbBytesReceivedSecure": bwOCSTcpServersNbBytesReceivedSecure,
       "concurrent": concurrent,
       "bwOCSMonitoringExecutorTable": bwOCSMonitoringExecutorTable,
       "bwOCSMonitoringExecutorEntry": bwOCSMonitoringExecutorEntry,
       "bwOCSMonitoringExecutorIndex": bwOCSMonitoringExecutorIndex,
       "bwOCSMonitoringExecutorName": bwOCSMonitoringExecutorName,
       "bwOCSMonitoringExecutorCurrentPoolSize": bwOCSMonitoringExecutorCurrentPoolSize,
       "bwOCSMonitoringExecutorMaxPoolSize": bwOCSMonitoringExecutorMaxPoolSize,
       "bwOCSMonitoringExecutorAvgActiveThreads": bwOCSMonitoringExecutorAvgActiveThreads,
       "bwOCSMonitoringExecutorTaskQueueSize": bwOCSMonitoringExecutorTaskQueueSize,
       "bwOCSMonitoringExecutorNbTasksRun": bwOCSMonitoringExecutorNbTasksRun,
       "bwOCSMonitoringExecutorNbWarnings": bwOCSMonitoringExecutorNbWarnings,
       "bwOCSMonitoringExecutorNbErrors": bwOCSMonitoringExecutorNbErrors,
       "bwOCSMonitoringExecutorLongestTaskMs": bwOCSMonitoringExecutorLongestTaskMs,
       "bwOCSMonitoringExecutorLongestTaskName": bwOCSMonitoringExecutorLongestTaskName,
       "ocsReserved": ocsReserved,
       "bwOCSReserved": bwOCSReserved,
       "bwOcsMibConformance": bwOcsMibConformance,
       "bwOcsMibGroups": bwOcsMibGroups,
       "bwOcsCapGroup": bwOcsCapGroup,
       "bwOcsAsOSSGroup": bwOcsAsOSSGroup,
       "bwOcsNsOSSGroup": bwOcsNsOSSGroup,
       "bwOcsBcctGroup": bwOcsBcctGroup,
       "bwOcsReserveGroup": bwOcsReserveGroup,
       "bwOcsExtAuthGroup": bwOcsExtAuthGroup,
       "bwOcsOciAuthGroup": bwOcsOciAuthGroup,
       "bwOcsTcpStatsGroup": bwOcsTcpStatsGroup,
       "bwOCSConcurrentFrameworkStatsGroup": bwOCSConcurrentFrameworkStatsGroup,
       "bwOcsMibCompliancy": bwOcsMibCompliancy,
       "bwOcsBasicCompliance": bwOcsBasicCompliance}
)
