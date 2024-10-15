# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:44 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

(jnxMbgGwIndex,
 jnxMbgGwName) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwIndex",
    "jnxMbgGwName")

(jnxMobileGatewayMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMobileGatewayMibRoot")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxMobileGatewayPgwAAAMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3)
)
jnxMobileGatewayPgwAAAMib.setRevisions(
        ("2011-01-03 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxMbgAAAServerStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("dead", 2),
          ("unknown", 0))
    )



class JnxMbgQueueWaterMarkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_JnxMbgAAANotifications_ObjectIdentity = ObjectIdentity
jnxMbgAAANotifications = _JnxMbgAAANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0)
)
_JnxMbgAAAObjects_ObjectIdentity = ObjectIdentity
jnxMbgAAAObjects = _JnxMbgAAAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1)
)
_JnxMbgAAAGlobalAuthStats_ObjectIdentity = ObjectIdentity
jnxMbgAAAGlobalAuthStats = _JnxMbgAAAGlobalAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1)
)
_JnxMbgTotalAuthRequests_Type = Counter64
_JnxMbgTotalAuthRequests_Object = MibScalar
jnxMbgTotalAuthRequests = _JnxMbgTotalAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1, 1),
    _JnxMbgTotalAuthRequests_Type()
)
jnxMbgTotalAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAuthRequests.setStatus("deprecated")
_JnxMbgTotalAuthAccepts_Type = Counter64
_JnxMbgTotalAuthAccepts_Object = MibScalar
jnxMbgTotalAuthAccepts = _JnxMbgTotalAuthAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1, 2),
    _JnxMbgTotalAuthAccepts_Type()
)
jnxMbgTotalAuthAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAuthAccepts.setStatus("deprecated")
_JnxMbgTotalAuthRejects_Type = Counter64
_JnxMbgTotalAuthRejects_Object = MibScalar
jnxMbgTotalAuthRejects = _JnxMbgTotalAuthRejects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1, 3),
    _JnxMbgTotalAuthRejects_Type()
)
jnxMbgTotalAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAuthRejects.setStatus("deprecated")
_JnxMbgTotalAuthChallenges_Type = Counter64
_JnxMbgTotalAuthChallenges_Object = MibScalar
jnxMbgTotalAuthChallenges = _JnxMbgTotalAuthChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1, 4),
    _JnxMbgTotalAuthChallenges_Type()
)
jnxMbgTotalAuthChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAuthChallenges.setStatus("deprecated")
_JnxMbgTotalAuthRequestTimeouts_Type = Counter64
_JnxMbgTotalAuthRequestTimeouts_Object = MibScalar
jnxMbgTotalAuthRequestTimeouts = _JnxMbgTotalAuthRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1, 5),
    _JnxMbgTotalAuthRequestTimeouts_Type()
)
jnxMbgTotalAuthRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAuthRequestTimeouts.setStatus("deprecated")
_JnxMbgTotalAuthRequestTxErrors_Type = Counter64
_JnxMbgTotalAuthRequestTxErrors_Object = MibScalar
jnxMbgTotalAuthRequestTxErrors = _JnxMbgTotalAuthRequestTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1, 6),
    _JnxMbgTotalAuthRequestTxErrors_Type()
)
jnxMbgTotalAuthRequestTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAuthRequestTxErrors.setStatus("deprecated")
_JnxMbgTotalAuthResponseErrors_Type = Counter64
_JnxMbgTotalAuthResponseErrors_Object = MibScalar
jnxMbgTotalAuthResponseErrors = _JnxMbgTotalAuthResponseErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1, 7),
    _JnxMbgTotalAuthResponseErrors_Type()
)
jnxMbgTotalAuthResponseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAuthResponseErrors.setStatus("deprecated")
_JnxMbgTotalAuthPendingRequests_Type = Counter64
_JnxMbgTotalAuthPendingRequests_Object = MibScalar
jnxMbgTotalAuthPendingRequests = _JnxMbgTotalAuthPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 1, 8),
    _JnxMbgTotalAuthPendingRequests_Type()
)
jnxMbgTotalAuthPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAuthPendingRequests.setStatus("deprecated")
_JnxMbgAAAGlobalAcctStats_ObjectIdentity = ObjectIdentity
jnxMbgAAAGlobalAcctStats = _JnxMbgAAAGlobalAcctStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 2)
)
_JnxMbgTotalAcctRequests_Type = Counter64
_JnxMbgTotalAcctRequests_Object = MibScalar
jnxMbgTotalAcctRequests = _JnxMbgTotalAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 2, 1),
    _JnxMbgTotalAcctRequests_Type()
)
jnxMbgTotalAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAcctRequests.setStatus("deprecated")
_JnxMbgTotalAcctResponses_Type = Counter64
_JnxMbgTotalAcctResponses_Object = MibScalar
jnxMbgTotalAcctResponses = _JnxMbgTotalAcctResponses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 2, 2),
    _JnxMbgTotalAcctResponses_Type()
)
jnxMbgTotalAcctResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAcctResponses.setStatus("deprecated")
_JnxMbgTotalAcctRequestTimeouts_Type = Counter64
_JnxMbgTotalAcctRequestTimeouts_Object = MibScalar
jnxMbgTotalAcctRequestTimeouts = _JnxMbgTotalAcctRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 2, 3),
    _JnxMbgTotalAcctRequestTimeouts_Type()
)
jnxMbgTotalAcctRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAcctRequestTimeouts.setStatus("deprecated")
_JnxMbgTotalAcctRequestTxErrors_Type = Counter64
_JnxMbgTotalAcctRequestTxErrors_Object = MibScalar
jnxMbgTotalAcctRequestTxErrors = _JnxMbgTotalAcctRequestTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 2, 4),
    _JnxMbgTotalAcctRequestTxErrors_Type()
)
jnxMbgTotalAcctRequestTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAcctRequestTxErrors.setStatus("deprecated")
_JnxMbgTotalAcctResponseErrors_Type = Counter64
_JnxMbgTotalAcctResponseErrors_Object = MibScalar
jnxMbgTotalAcctResponseErrors = _JnxMbgTotalAcctResponseErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 2, 5),
    _JnxMbgTotalAcctResponseErrors_Type()
)
jnxMbgTotalAcctResponseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAcctResponseErrors.setStatus("deprecated")
_JnxMbgTotalAcctPendingRequests_Type = Counter64
_JnxMbgTotalAcctPendingRequests_Object = MibScalar
jnxMbgTotalAcctPendingRequests = _JnxMbgTotalAcctPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 2, 6),
    _JnxMbgTotalAcctPendingRequests_Type()
)
jnxMbgTotalAcctPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalAcctPendingRequests.setStatus("deprecated")
_JnxMbgAAAGlobalDynAuthStats_ObjectIdentity = ObjectIdentity
jnxMbgAAAGlobalDynAuthStats = _JnxMbgAAAGlobalDynAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3)
)
_JnxMbgTotalDynAuthReceived_Type = Counter64
_JnxMbgTotalDynAuthReceived_Object = MibScalar
jnxMbgTotalDynAuthReceived = _JnxMbgTotalDynAuthReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 1),
    _JnxMbgTotalDynAuthReceived_Type()
)
jnxMbgTotalDynAuthReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthReceived.setStatus("deprecated")
_JnxMbgTotalDynAuthCoaReceived_Type = Counter64
_JnxMbgTotalDynAuthCoaReceived_Object = MibScalar
jnxMbgTotalDynAuthCoaReceived = _JnxMbgTotalDynAuthCoaReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 2),
    _JnxMbgTotalDynAuthCoaReceived_Type()
)
jnxMbgTotalDynAuthCoaReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthCoaReceived.setStatus("deprecated")
_JnxMbgTotalDynAuthDmReceived_Type = Counter64
_JnxMbgTotalDynAuthDmReceived_Object = MibScalar
jnxMbgTotalDynAuthDmReceived = _JnxMbgTotalDynAuthDmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 3),
    _JnxMbgTotalDynAuthDmReceived_Type()
)
jnxMbgTotalDynAuthDmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthDmReceived.setStatus("deprecated")
_JnxMbgTotalDynAuthCoaAckSent_Type = Counter64
_JnxMbgTotalDynAuthCoaAckSent_Object = MibScalar
jnxMbgTotalDynAuthCoaAckSent = _JnxMbgTotalDynAuthCoaAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 4),
    _JnxMbgTotalDynAuthCoaAckSent_Type()
)
jnxMbgTotalDynAuthCoaAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthCoaAckSent.setStatus("deprecated")
_JnxMbgTotalDynAuthCoaNackSent_Type = Counter64
_JnxMbgTotalDynAuthCoaNackSent_Object = MibScalar
jnxMbgTotalDynAuthCoaNackSent = _JnxMbgTotalDynAuthCoaNackSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 5),
    _JnxMbgTotalDynAuthCoaNackSent_Type()
)
jnxMbgTotalDynAuthCoaNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthCoaNackSent.setStatus("deprecated")
_JnxMbgTotalDynAuthDmAckSent_Type = Counter64
_JnxMbgTotalDynAuthDmAckSent_Object = MibScalar
jnxMbgTotalDynAuthDmAckSent = _JnxMbgTotalDynAuthDmAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 6),
    _JnxMbgTotalDynAuthDmAckSent_Type()
)
jnxMbgTotalDynAuthDmAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthDmAckSent.setStatus("deprecated")
_JnxMbgTotalDynAuthDmNackSent_Type = Counter64
_JnxMbgTotalDynAuthDmNackSent_Object = MibScalar
jnxMbgTotalDynAuthDmNackSent = _JnxMbgTotalDynAuthDmNackSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 7),
    _JnxMbgTotalDynAuthDmNackSent_Type()
)
jnxMbgTotalDynAuthDmNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthDmNackSent.setStatus("deprecated")
_JnxMbgTotalDynAuthDropped_Type = Counter64
_JnxMbgTotalDynAuthDropped_Object = MibScalar
jnxMbgTotalDynAuthDropped = _JnxMbgTotalDynAuthDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 8),
    _JnxMbgTotalDynAuthDropped_Type()
)
jnxMbgTotalDynAuthDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthDropped.setStatus("deprecated")
_JnxMbgTotalDynAuthDuplicate_Type = Counter64
_JnxMbgTotalDynAuthDuplicate_Object = MibScalar
jnxMbgTotalDynAuthDuplicate = _JnxMbgTotalDynAuthDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 9),
    _JnxMbgTotalDynAuthDuplicate_Type()
)
jnxMbgTotalDynAuthDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthDuplicate.setStatus("deprecated")
_JnxMbgTotalDynAuthForwarded_Type = Counter64
_JnxMbgTotalDynAuthForwarded_Object = MibScalar
jnxMbgTotalDynAuthForwarded = _JnxMbgTotalDynAuthForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 10),
    _JnxMbgTotalDynAuthForwarded_Type()
)
jnxMbgTotalDynAuthForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthForwarded.setStatus("deprecated")
_JnxMbgTotalDynAuthTimeouts_Type = Counter64
_JnxMbgTotalDynAuthTimeouts_Object = MibScalar
jnxMbgTotalDynAuthTimeouts = _JnxMbgTotalDynAuthTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 11),
    _JnxMbgTotalDynAuthTimeouts_Type()
)
jnxMbgTotalDynAuthTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthTimeouts.setStatus("deprecated")
_JnxMbgTotalDynAuthDelivered_Type = Counter64
_JnxMbgTotalDynAuthDelivered_Object = MibScalar
jnxMbgTotalDynAuthDelivered = _JnxMbgTotalDynAuthDelivered_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 12),
    _JnxMbgTotalDynAuthDelivered_Type()
)
jnxMbgTotalDynAuthDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthDelivered.setStatus("deprecated")
_JnxMbgTotalDynAuthErrors_Type = Counter64
_JnxMbgTotalDynAuthErrors_Object = MibScalar
jnxMbgTotalDynAuthErrors = _JnxMbgTotalDynAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 13),
    _JnxMbgTotalDynAuthErrors_Type()
)
jnxMbgTotalDynAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthErrors.setStatus("deprecated")
_JnxMbgTotalDynAuthUnknownClnts_Type = Counter64
_JnxMbgTotalDynAuthUnknownClnts_Object = MibScalar
jnxMbgTotalDynAuthUnknownClnts = _JnxMbgTotalDynAuthUnknownClnts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 14),
    _JnxMbgTotalDynAuthUnknownClnts_Type()
)
jnxMbgTotalDynAuthUnknownClnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthUnknownClnts.setStatus("deprecated")
_JnxMbgTotalDynAuthInvalidCode_Type = Counter64
_JnxMbgTotalDynAuthInvalidCode_Object = MibScalar
jnxMbgTotalDynAuthInvalidCode = _JnxMbgTotalDynAuthInvalidCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 15),
    _JnxMbgTotalDynAuthInvalidCode_Type()
)
jnxMbgTotalDynAuthInvalidCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthInvalidCode.setStatus("deprecated")
_JnxMbgTotalDynAuthInvalidAuth_Type = Counter64
_JnxMbgTotalDynAuthInvalidAuth_Object = MibScalar
jnxMbgTotalDynAuthInvalidAuth = _JnxMbgTotalDynAuthInvalidAuth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 16),
    _JnxMbgTotalDynAuthInvalidAuth_Type()
)
jnxMbgTotalDynAuthInvalidAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthInvalidAuth.setStatus("deprecated")
_JnxMbgTotalDynAuthInvalidChId_Type = Counter64
_JnxMbgTotalDynAuthInvalidChId_Object = MibScalar
jnxMbgTotalDynAuthInvalidChId = _JnxMbgTotalDynAuthInvalidChId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 17),
    _JnxMbgTotalDynAuthInvalidChId_Type()
)
jnxMbgTotalDynAuthInvalidChId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthInvalidChId.setStatus("deprecated")
_JnxMbgTotalDynAuthMapErrors_Type = Counter64
_JnxMbgTotalDynAuthMapErrors_Object = MibScalar
jnxMbgTotalDynAuthMapErrors = _JnxMbgTotalDynAuthMapErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 18),
    _JnxMbgTotalDynAuthMapErrors_Type()
)
jnxMbgTotalDynAuthMapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthMapErrors.setStatus("deprecated")
_JnxMbgTotalDynAuthInvalidTrId_Type = Counter64
_JnxMbgTotalDynAuthInvalidTrId_Object = MibScalar
jnxMbgTotalDynAuthInvalidTrId = _JnxMbgTotalDynAuthInvalidTrId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 3, 19),
    _JnxMbgTotalDynAuthInvalidTrId_Type()
)
jnxMbgTotalDynAuthInvalidTrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTotalDynAuthInvalidTrId.setStatus("deprecated")
_JnxMbgRadiusAuthServerTable_Object = MibTable
jnxMbgRadiusAuthServerTable = _JnxMbgRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4)
)
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerTable.setStatus("deprecated")
_JnxMbgRadiusAuthServerEntry_Object = MibTableRow
jnxMbgRadiusAuthServerEntry = _JnxMbgRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1)
)
jnxMbgRadiusAuthServerEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgRadiusAuthServerName"),
)
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerEntry.setStatus("deprecated")


class _JnxMbgRadiusAuthServerName_Type(DisplayString):
    """Custom type jnxMbgRadiusAuthServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxMbgRadiusAuthServerName_Type.__name__ = "DisplayString"
_JnxMbgRadiusAuthServerName_Object = MibTableColumn
jnxMbgRadiusAuthServerName = _JnxMbgRadiusAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 1),
    _JnxMbgRadiusAuthServerName_Type()
)
jnxMbgRadiusAuthServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerName.setStatus("deprecated")
_JnxMbgRadiusAuthServerInetAddressType_Type = InetAddressType
_JnxMbgRadiusAuthServerInetAddressType_Object = MibTableColumn
jnxMbgRadiusAuthServerInetAddressType = _JnxMbgRadiusAuthServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 2),
    _JnxMbgRadiusAuthServerInetAddressType_Type()
)
jnxMbgRadiusAuthServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerInetAddressType.setStatus("deprecated")
_JnxMbgRadiusAuthServerInetAddress_Type = InetAddress
_JnxMbgRadiusAuthServerInetAddress_Object = MibTableColumn
jnxMbgRadiusAuthServerInetAddress = _JnxMbgRadiusAuthServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 3),
    _JnxMbgRadiusAuthServerInetAddress_Type()
)
jnxMbgRadiusAuthServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerInetAddress.setStatus("deprecated")
_JnxMbgRadiusAuthServerInetPort_Type = InetPortNumber
_JnxMbgRadiusAuthServerInetPort_Object = MibTableColumn
jnxMbgRadiusAuthServerInetPort = _JnxMbgRadiusAuthServerInetPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 4),
    _JnxMbgRadiusAuthServerInetPort_Type()
)
jnxMbgRadiusAuthServerInetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerInetPort.setStatus("deprecated")
_JnxMbgRadiusAuthServerRoutingInstance_Type = DisplayString
_JnxMbgRadiusAuthServerRoutingInstance_Object = MibTableColumn
jnxMbgRadiusAuthServerRoutingInstance = _JnxMbgRadiusAuthServerRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 5),
    _JnxMbgRadiusAuthServerRoutingInstance_Type()
)
jnxMbgRadiusAuthServerRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerRoutingInstance.setStatus("deprecated")
_JnxMbgRadiusAuthServerStatus_Type = JnxMbgAAAServerStatus
_JnxMbgRadiusAuthServerStatus_Object = MibTableColumn
jnxMbgRadiusAuthServerStatus = _JnxMbgRadiusAuthServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 6),
    _JnxMbgRadiusAuthServerStatus_Type()
)
jnxMbgRadiusAuthServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerStatus.setStatus("deprecated")
_JnxMbgRadiusAuthServerRequests_Type = Counter64
_JnxMbgRadiusAuthServerRequests_Object = MibTableColumn
jnxMbgRadiusAuthServerRequests = _JnxMbgRadiusAuthServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 7),
    _JnxMbgRadiusAuthServerRequests_Type()
)
jnxMbgRadiusAuthServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerRequests.setStatus("deprecated")
_JnxMbgRadiusAuthServersRetransmissions_Type = Counter64
_JnxMbgRadiusAuthServersRetransmissions_Object = MibTableColumn
jnxMbgRadiusAuthServersRetransmissions = _JnxMbgRadiusAuthServersRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 8),
    _JnxMbgRadiusAuthServersRetransmissions_Type()
)
jnxMbgRadiusAuthServersRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServersRetransmissions.setStatus("deprecated")
_JnxMbgRadiusAuthServerAccepts_Type = Counter64
_JnxMbgRadiusAuthServerAccepts_Object = MibTableColumn
jnxMbgRadiusAuthServerAccepts = _JnxMbgRadiusAuthServerAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 9),
    _JnxMbgRadiusAuthServerAccepts_Type()
)
jnxMbgRadiusAuthServerAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerAccepts.setStatus("deprecated")
_JnxMbgRadiusAuthServerRejects_Type = Counter64
_JnxMbgRadiusAuthServerRejects_Object = MibTableColumn
jnxMbgRadiusAuthServerRejects = _JnxMbgRadiusAuthServerRejects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 10),
    _JnxMbgRadiusAuthServerRejects_Type()
)
jnxMbgRadiusAuthServerRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerRejects.setStatus("deprecated")
_JnxMbgRadiusAuthServerChallenges_Type = Counter64
_JnxMbgRadiusAuthServerChallenges_Object = MibTableColumn
jnxMbgRadiusAuthServerChallenges = _JnxMbgRadiusAuthServerChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 11),
    _JnxMbgRadiusAuthServerChallenges_Type()
)
jnxMbgRadiusAuthServerChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerChallenges.setStatus("deprecated")
_JnxMbgRadiusAuthServerMalformedResponses_Type = Counter64
_JnxMbgRadiusAuthServerMalformedResponses_Object = MibTableColumn
jnxMbgRadiusAuthServerMalformedResponses = _JnxMbgRadiusAuthServerMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 12),
    _JnxMbgRadiusAuthServerMalformedResponses_Type()
)
jnxMbgRadiusAuthServerMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerMalformedResponses.setStatus("deprecated")
_JnxMbgRadiusAuthServerBadAuthenticators_Type = Counter64
_JnxMbgRadiusAuthServerBadAuthenticators_Object = MibTableColumn
jnxMbgRadiusAuthServerBadAuthenticators = _JnxMbgRadiusAuthServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 13),
    _JnxMbgRadiusAuthServerBadAuthenticators_Type()
)
jnxMbgRadiusAuthServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerBadAuthenticators.setStatus("deprecated")
_JnxMbgRadiusAuthServerPendingRequests_Type = Counter64
_JnxMbgRadiusAuthServerPendingRequests_Object = MibTableColumn
jnxMbgRadiusAuthServerPendingRequests = _JnxMbgRadiusAuthServerPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 14),
    _JnxMbgRadiusAuthServerPendingRequests_Type()
)
jnxMbgRadiusAuthServerPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerPendingRequests.setStatus("deprecated")
_JnxMbgRadiusAuthServerTimeouts_Type = Counter64
_JnxMbgRadiusAuthServerTimeouts_Object = MibTableColumn
jnxMbgRadiusAuthServerTimeouts = _JnxMbgRadiusAuthServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 15),
    _JnxMbgRadiusAuthServerTimeouts_Type()
)
jnxMbgRadiusAuthServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerTimeouts.setStatus("deprecated")
_JnxMbgRadiusAuthServerUnknownTypes_Type = Counter64
_JnxMbgRadiusAuthServerUnknownTypes_Object = MibTableColumn
jnxMbgRadiusAuthServerUnknownTypes = _JnxMbgRadiusAuthServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 16),
    _JnxMbgRadiusAuthServerUnknownTypes_Type()
)
jnxMbgRadiusAuthServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerUnknownTypes.setStatus("deprecated")
_JnxMbgRadiusAuthServerPacketsDropped_Type = Counter64
_JnxMbgRadiusAuthServerPacketsDropped_Object = MibTableColumn
jnxMbgRadiusAuthServerPacketsDropped = _JnxMbgRadiusAuthServerPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 17),
    _JnxMbgRadiusAuthServerPacketsDropped_Type()
)
jnxMbgRadiusAuthServerPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerPacketsDropped.setStatus("deprecated")
_JnxMbgRadiusAuthServerRTTAvg_Type = Integer32
_JnxMbgRadiusAuthServerRTTAvg_Object = MibTableColumn
jnxMbgRadiusAuthServerRTTAvg = _JnxMbgRadiusAuthServerRTTAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 18),
    _JnxMbgRadiusAuthServerRTTAvg_Type()
)
jnxMbgRadiusAuthServerRTTAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerRTTAvg.setStatus("deprecated")
_JnxMbgRadiusAuthServerRTTMin_Type = Integer32
_JnxMbgRadiusAuthServerRTTMin_Object = MibTableColumn
jnxMbgRadiusAuthServerRTTMin = _JnxMbgRadiusAuthServerRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 19),
    _JnxMbgRadiusAuthServerRTTMin_Type()
)
jnxMbgRadiusAuthServerRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerRTTMin.setStatus("deprecated")
_JnxMbgRadiusAuthServerRTTMax_Type = Integer32
_JnxMbgRadiusAuthServerRTTMax_Object = MibTableColumn
jnxMbgRadiusAuthServerRTTMax = _JnxMbgRadiusAuthServerRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 4, 1, 20),
    _JnxMbgRadiusAuthServerRTTMax_Type()
)
jnxMbgRadiusAuthServerRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthServerRTTMax.setStatus("deprecated")
_JnxMbgRadiusAcctServerTable_Object = MibTable
jnxMbgRadiusAcctServerTable = _JnxMbgRadiusAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5)
)
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerTable.setStatus("deprecated")
_JnxMbgRadiusAcctServerEntry_Object = MibTableRow
jnxMbgRadiusAcctServerEntry = _JnxMbgRadiusAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1)
)
jnxMbgRadiusAcctServerEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgRadiusAcctServerName"),
)
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerEntry.setStatus("deprecated")


class _JnxMbgRadiusAcctServerName_Type(DisplayString):
    """Custom type jnxMbgRadiusAcctServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxMbgRadiusAcctServerName_Type.__name__ = "DisplayString"
_JnxMbgRadiusAcctServerName_Object = MibTableColumn
jnxMbgRadiusAcctServerName = _JnxMbgRadiusAcctServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 1),
    _JnxMbgRadiusAcctServerName_Type()
)
jnxMbgRadiusAcctServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerName.setStatus("deprecated")
_JnxMbgRadiusAcctServerInetAddressType_Type = InetAddressType
_JnxMbgRadiusAcctServerInetAddressType_Object = MibTableColumn
jnxMbgRadiusAcctServerInetAddressType = _JnxMbgRadiusAcctServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 2),
    _JnxMbgRadiusAcctServerInetAddressType_Type()
)
jnxMbgRadiusAcctServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerInetAddressType.setStatus("deprecated")
_JnxMbgRadiusAcctServerInetAddress_Type = InetAddress
_JnxMbgRadiusAcctServerInetAddress_Object = MibTableColumn
jnxMbgRadiusAcctServerInetAddress = _JnxMbgRadiusAcctServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 3),
    _JnxMbgRadiusAcctServerInetAddress_Type()
)
jnxMbgRadiusAcctServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerInetAddress.setStatus("deprecated")
_JnxMbgRadiusAcctServerInetPort_Type = InetPortNumber
_JnxMbgRadiusAcctServerInetPort_Object = MibTableColumn
jnxMbgRadiusAcctServerInetPort = _JnxMbgRadiusAcctServerInetPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 4),
    _JnxMbgRadiusAcctServerInetPort_Type()
)
jnxMbgRadiusAcctServerInetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerInetPort.setStatus("deprecated")
_JnxMbgRadiusAcctServerRoutingInstance_Type = DisplayString
_JnxMbgRadiusAcctServerRoutingInstance_Object = MibTableColumn
jnxMbgRadiusAcctServerRoutingInstance = _JnxMbgRadiusAcctServerRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 5),
    _JnxMbgRadiusAcctServerRoutingInstance_Type()
)
jnxMbgRadiusAcctServerRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerRoutingInstance.setStatus("deprecated")
_JnxMbgRadiusAcctServerStatus_Type = JnxMbgAAAServerStatus
_JnxMbgRadiusAcctServerStatus_Object = MibTableColumn
jnxMbgRadiusAcctServerStatus = _JnxMbgRadiusAcctServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 6),
    _JnxMbgRadiusAcctServerStatus_Type()
)
jnxMbgRadiusAcctServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerStatus.setStatus("deprecated")
_JnxMbgRadiusAcctServerRequests_Type = Counter64
_JnxMbgRadiusAcctServerRequests_Object = MibTableColumn
jnxMbgRadiusAcctServerRequests = _JnxMbgRadiusAcctServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 7),
    _JnxMbgRadiusAcctServerRequests_Type()
)
jnxMbgRadiusAcctServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerRequests.setStatus("deprecated")
_JnxMbgRadiusAcctServersRetransmissions_Type = Counter64
_JnxMbgRadiusAcctServersRetransmissions_Object = MibTableColumn
jnxMbgRadiusAcctServersRetransmissions = _JnxMbgRadiusAcctServersRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 8),
    _JnxMbgRadiusAcctServersRetransmissions_Type()
)
jnxMbgRadiusAcctServersRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServersRetransmissions.setStatus("deprecated")
_JnxMbgRadiusAcctServerResponses_Type = Counter64
_JnxMbgRadiusAcctServerResponses_Object = MibTableColumn
jnxMbgRadiusAcctServerResponses = _JnxMbgRadiusAcctServerResponses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 9),
    _JnxMbgRadiusAcctServerResponses_Type()
)
jnxMbgRadiusAcctServerResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerResponses.setStatus("deprecated")
_JnxMbgRadiusAcctServerMalformedResponses_Type = Counter64
_JnxMbgRadiusAcctServerMalformedResponses_Object = MibTableColumn
jnxMbgRadiusAcctServerMalformedResponses = _JnxMbgRadiusAcctServerMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 10),
    _JnxMbgRadiusAcctServerMalformedResponses_Type()
)
jnxMbgRadiusAcctServerMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerMalformedResponses.setStatus("deprecated")
_JnxMbgRadiusAcctServerBadAuthenticators_Type = Counter64
_JnxMbgRadiusAcctServerBadAuthenticators_Object = MibTableColumn
jnxMbgRadiusAcctServerBadAuthenticators = _JnxMbgRadiusAcctServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 11),
    _JnxMbgRadiusAcctServerBadAuthenticators_Type()
)
jnxMbgRadiusAcctServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerBadAuthenticators.setStatus("deprecated")
_JnxMbgRadiusAcctServerPendingRequests_Type = Counter64
_JnxMbgRadiusAcctServerPendingRequests_Object = MibTableColumn
jnxMbgRadiusAcctServerPendingRequests = _JnxMbgRadiusAcctServerPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 12),
    _JnxMbgRadiusAcctServerPendingRequests_Type()
)
jnxMbgRadiusAcctServerPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerPendingRequests.setStatus("deprecated")
_JnxMbgRadiusAcctServerTimeouts_Type = Counter64
_JnxMbgRadiusAcctServerTimeouts_Object = MibTableColumn
jnxMbgRadiusAcctServerTimeouts = _JnxMbgRadiusAcctServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 13),
    _JnxMbgRadiusAcctServerTimeouts_Type()
)
jnxMbgRadiusAcctServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerTimeouts.setStatus("deprecated")
_JnxMbgRadiusAcctServerUnknownTypes_Type = Counter64
_JnxMbgRadiusAcctServerUnknownTypes_Object = MibTableColumn
jnxMbgRadiusAcctServerUnknownTypes = _JnxMbgRadiusAcctServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 14),
    _JnxMbgRadiusAcctServerUnknownTypes_Type()
)
jnxMbgRadiusAcctServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerUnknownTypes.setStatus("deprecated")
_JnxMbgRadiusAcctServerPacketsDropped_Type = Counter64
_JnxMbgRadiusAcctServerPacketsDropped_Object = MibTableColumn
jnxMbgRadiusAcctServerPacketsDropped = _JnxMbgRadiusAcctServerPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 15),
    _JnxMbgRadiusAcctServerPacketsDropped_Type()
)
jnxMbgRadiusAcctServerPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerPacketsDropped.setStatus("deprecated")
_JnxMbgRadiusAcctServerRTTAvg_Type = Integer32
_JnxMbgRadiusAcctServerRTTAvg_Object = MibTableColumn
jnxMbgRadiusAcctServerRTTAvg = _JnxMbgRadiusAcctServerRTTAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 16),
    _JnxMbgRadiusAcctServerRTTAvg_Type()
)
jnxMbgRadiusAcctServerRTTAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerRTTAvg.setStatus("deprecated")
_JnxMbgRadiusAcctServerRTTMin_Type = Integer32
_JnxMbgRadiusAcctServerRTTMin_Object = MibTableColumn
jnxMbgRadiusAcctServerRTTMin = _JnxMbgRadiusAcctServerRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 17),
    _JnxMbgRadiusAcctServerRTTMin_Type()
)
jnxMbgRadiusAcctServerRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerRTTMin.setStatus("deprecated")
_JnxMbgRadiusAcctServerRTTMax_Type = Integer32
_JnxMbgRadiusAcctServerRTTMax_Object = MibTableColumn
jnxMbgRadiusAcctServerRTTMax = _JnxMbgRadiusAcctServerRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 5, 1, 18),
    _JnxMbgRadiusAcctServerRTTMax_Type()
)
jnxMbgRadiusAcctServerRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctServerRTTMax.setStatus("deprecated")
_JnxMbgDynAuthClientTable_Object = MibTable
jnxMbgDynAuthClientTable = _JnxMbgDynAuthClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6)
)
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientTable.setStatus("deprecated")
_JnxMbgDynAuthClientEntry_Object = MibTableRow
jnxMbgDynAuthClientEntry = _JnxMbgDynAuthClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1)
)
jnxMbgDynAuthClientEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgRadiusAcctServerName"),
)
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientEntry.setStatus("deprecated")


class _JnxMbgDynAuthClientName_Type(DisplayString):
    """Custom type jnxMbgDynAuthClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxMbgDynAuthClientName_Type.__name__ = "DisplayString"
_JnxMbgDynAuthClientName_Object = MibTableColumn
jnxMbgDynAuthClientName = _JnxMbgDynAuthClientName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 1),
    _JnxMbgDynAuthClientName_Type()
)
jnxMbgDynAuthClientName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientName.setStatus("deprecated")
_JnxMbgDynAuthClientInAddrType_Type = InetAddressType
_JnxMbgDynAuthClientInAddrType_Object = MibTableColumn
jnxMbgDynAuthClientInAddrType = _JnxMbgDynAuthClientInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 2),
    _JnxMbgDynAuthClientInAddrType_Type()
)
jnxMbgDynAuthClientInAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientInAddrType.setStatus("deprecated")
_JnxMbgDynAuthClientInetAddress_Type = InetAddress
_JnxMbgDynAuthClientInetAddress_Object = MibTableColumn
jnxMbgDynAuthClientInetAddress = _JnxMbgDynAuthClientInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 3),
    _JnxMbgDynAuthClientInetAddress_Type()
)
jnxMbgDynAuthClientInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientInetAddress.setStatus("deprecated")
_JnxMbgDynAuthClientCoaReceived_Type = Counter64
_JnxMbgDynAuthClientCoaReceived_Object = MibTableColumn
jnxMbgDynAuthClientCoaReceived = _JnxMbgDynAuthClientCoaReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 4),
    _JnxMbgDynAuthClientCoaReceived_Type()
)
jnxMbgDynAuthClientCoaReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientCoaReceived.setStatus("deprecated")
_JnxMbgDynAuthClientDmReceived_Type = Counter64
_JnxMbgDynAuthClientDmReceived_Object = MibTableColumn
jnxMbgDynAuthClientDmReceived = _JnxMbgDynAuthClientDmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 5),
    _JnxMbgDynAuthClientDmReceived_Type()
)
jnxMbgDynAuthClientDmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientDmReceived.setStatus("deprecated")
_JnxMbgDynAuthClientCoaAckSent_Type = Counter64
_JnxMbgDynAuthClientCoaAckSent_Object = MibTableColumn
jnxMbgDynAuthClientCoaAckSent = _JnxMbgDynAuthClientCoaAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 6),
    _JnxMbgDynAuthClientCoaAckSent_Type()
)
jnxMbgDynAuthClientCoaAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientCoaAckSent.setStatus("deprecated")
_JnxMbgDynAuthClientCoaNackSent_Type = Counter64
_JnxMbgDynAuthClientCoaNackSent_Object = MibTableColumn
jnxMbgDynAuthClientCoaNackSent = _JnxMbgDynAuthClientCoaNackSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 7),
    _JnxMbgDynAuthClientCoaNackSent_Type()
)
jnxMbgDynAuthClientCoaNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientCoaNackSent.setStatus("deprecated")
_JnxMbgDynAuthClientDmAckSent_Type = Counter64
_JnxMbgDynAuthClientDmAckSent_Object = MibTableColumn
jnxMbgDynAuthClientDmAckSent = _JnxMbgDynAuthClientDmAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 8),
    _JnxMbgDynAuthClientDmAckSent_Type()
)
jnxMbgDynAuthClientDmAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientDmAckSent.setStatus("deprecated")
_JnxMbgDynAuthClientDmNackSent_Type = Counter64
_JnxMbgDynAuthClientDmNackSent_Object = MibTableColumn
jnxMbgDynAuthClientDmNackSent = _JnxMbgDynAuthClientDmNackSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 9),
    _JnxMbgDynAuthClientDmNackSent_Type()
)
jnxMbgDynAuthClientDmNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientDmNackSent.setStatus("deprecated")
_JnxMbgDynAuthClientDropped_Type = Counter64
_JnxMbgDynAuthClientDropped_Object = MibTableColumn
jnxMbgDynAuthClientDropped = _JnxMbgDynAuthClientDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 10),
    _JnxMbgDynAuthClientDropped_Type()
)
jnxMbgDynAuthClientDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientDropped.setStatus("deprecated")
_JnxMbgDynAuthClientDuplicate_Type = Counter64
_JnxMbgDynAuthClientDuplicate_Object = MibTableColumn
jnxMbgDynAuthClientDuplicate = _JnxMbgDynAuthClientDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 11),
    _JnxMbgDynAuthClientDuplicate_Type()
)
jnxMbgDynAuthClientDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientDuplicate.setStatus("deprecated")
_JnxMbgDynAuthClientForwarded_Type = Counter64
_JnxMbgDynAuthClientForwarded_Object = MibTableColumn
jnxMbgDynAuthClientForwarded = _JnxMbgDynAuthClientForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 12),
    _JnxMbgDynAuthClientForwarded_Type()
)
jnxMbgDynAuthClientForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientForwarded.setStatus("deprecated")
_JnxMbgDynAuthClientTimeouts_Type = Counter64
_JnxMbgDynAuthClientTimeouts_Object = MibTableColumn
jnxMbgDynAuthClientTimeouts = _JnxMbgDynAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 13),
    _JnxMbgDynAuthClientTimeouts_Type()
)
jnxMbgDynAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientTimeouts.setStatus("deprecated")
_JnxMbgDynAuthClientDelivered_Type = Counter64
_JnxMbgDynAuthClientDelivered_Object = MibTableColumn
jnxMbgDynAuthClientDelivered = _JnxMbgDynAuthClientDelivered_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 14),
    _JnxMbgDynAuthClientDelivered_Type()
)
jnxMbgDynAuthClientDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientDelivered.setStatus("deprecated")
_JnxMbgDynAuthClientErrors_Type = Counter64
_JnxMbgDynAuthClientErrors_Object = MibTableColumn
jnxMbgDynAuthClientErrors = _JnxMbgDynAuthClientErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 15),
    _JnxMbgDynAuthClientErrors_Type()
)
jnxMbgDynAuthClientErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientErrors.setStatus("deprecated")
_JnxMbgDynAuthClientInvalidAuth_Type = Counter64
_JnxMbgDynAuthClientInvalidAuth_Object = MibTableColumn
jnxMbgDynAuthClientInvalidAuth = _JnxMbgDynAuthClientInvalidAuth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 17),
    _JnxMbgDynAuthClientInvalidAuth_Type()
)
jnxMbgDynAuthClientInvalidAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientInvalidAuth.setStatus("deprecated")
_JnxMbgDynAuthClientInvalidCode_Type = Counter64
_JnxMbgDynAuthClientInvalidCode_Object = MibTableColumn
jnxMbgDynAuthClientInvalidCode = _JnxMbgDynAuthClientInvalidCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 18),
    _JnxMbgDynAuthClientInvalidCode_Type()
)
jnxMbgDynAuthClientInvalidCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientInvalidCode.setStatus("deprecated")
_JnxMbgDynAuthClientInvalidChId_Type = Counter64
_JnxMbgDynAuthClientInvalidChId_Object = MibTableColumn
jnxMbgDynAuthClientInvalidChId = _JnxMbgDynAuthClientInvalidChId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 19),
    _JnxMbgDynAuthClientInvalidChId_Type()
)
jnxMbgDynAuthClientInvalidChId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientInvalidChId.setStatus("deprecated")
_JnxMbgDynAuthClientMapErrors_Type = Counter64
_JnxMbgDynAuthClientMapErrors_Object = MibTableColumn
jnxMbgDynAuthClientMapErrors = _JnxMbgDynAuthClientMapErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 6, 1, 20),
    _JnxMbgDynAuthClientMapErrors_Type()
)
jnxMbgDynAuthClientMapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClientMapErrors.setStatus("deprecated")
_JnxMbgAAANotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgAAANotificationVars = _JnxMbgAAANotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 7)
)
_JnxMbgAAAServerName_Type = DisplayString
_JnxMbgAAAServerName_Object = MibScalar
jnxMbgAAAServerName = _JnxMbgAAAServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 7, 1),
    _JnxMbgAAAServerName_Type()
)
jnxMbgAAAServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgAAAServerName.setStatus("current")
_JnxMbgSPIdentifier_Type = DisplayString
_JnxMbgSPIdentifier_Object = MibScalar
jnxMbgSPIdentifier = _JnxMbgSPIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 7, 2),
    _JnxMbgSPIdentifier_Type()
)
jnxMbgSPIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSPIdentifier.setStatus("current")
_JnxMbgAAANetworkElementName_Type = DisplayString
_JnxMbgAAANetworkElementName_Object = MibScalar
jnxMbgAAANetworkElementName = _JnxMbgAAANetworkElementName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 7, 3),
    _JnxMbgAAANetworkElementName_Type()
)
jnxMbgAAANetworkElementName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgAAANetworkElementName.setStatus("current")
_JnxMbgPendQWaterMarkType_Type = JnxMbgQueueWaterMarkType
_JnxMbgPendQWaterMarkType_Object = MibScalar
jnxMbgPendQWaterMarkType = _JnxMbgPendQWaterMarkType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 7, 4),
    _JnxMbgPendQWaterMarkType_Type()
)
jnxMbgPendQWaterMarkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPendQWaterMarkType.setStatus("current")
_JnxMbgPendQWaterMarkValue_Type = Integer32
_JnxMbgPendQWaterMarkValue_Object = MibScalar
jnxMbgPendQWaterMarkValue = _JnxMbgPendQWaterMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 7, 5),
    _JnxMbgPendQWaterMarkValue_Type()
)
jnxMbgPendQWaterMarkValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPendQWaterMarkValue.setStatus("current")
_JnxMbgPendQLength_Type = Counter32
_JnxMbgPendQLength_Object = MibScalar
jnxMbgPendQLength = _JnxMbgPendQLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 7, 6),
    _JnxMbgPendQLength_Type()
)
jnxMbgPendQLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPendQLength.setStatus("current")
_JnxMbgAAAAuthStatsTable_Object = MibTable
jnxMbgAAAAuthStatsTable = _JnxMbgAAAAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8)
)
if mibBuilder.loadTexts:
    jnxMbgAAAAuthStatsTable.setStatus("current")
_JnxMbgAAAAuthStatsEntry_Object = MibTableRow
jnxMbgAAAAuthStatsEntry = _JnxMbgAAAAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1)
)
jnxMbgAAAAuthStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgAAAAuthStatsEntry.setStatus("current")
_JnxMbgTtlAuthRequests_Type = Counter64
_JnxMbgTtlAuthRequests_Object = MibTableColumn
jnxMbgTtlAuthRequests = _JnxMbgTtlAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1, 1),
    _JnxMbgTtlAuthRequests_Type()
)
jnxMbgTtlAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAuthRequests.setStatus("current")
_JnxMbgTtlAuthAccepts_Type = Counter64
_JnxMbgTtlAuthAccepts_Object = MibTableColumn
jnxMbgTtlAuthAccepts = _JnxMbgTtlAuthAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1, 2),
    _JnxMbgTtlAuthAccepts_Type()
)
jnxMbgTtlAuthAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAuthAccepts.setStatus("current")
_JnxMbgTtlAuthRejects_Type = Counter64
_JnxMbgTtlAuthRejects_Object = MibTableColumn
jnxMbgTtlAuthRejects = _JnxMbgTtlAuthRejects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1, 3),
    _JnxMbgTtlAuthRejects_Type()
)
jnxMbgTtlAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAuthRejects.setStatus("current")
_JnxMbgTtlAuthChallenges_Type = Counter64
_JnxMbgTtlAuthChallenges_Object = MibTableColumn
jnxMbgTtlAuthChallenges = _JnxMbgTtlAuthChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1, 4),
    _JnxMbgTtlAuthChallenges_Type()
)
jnxMbgTtlAuthChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAuthChallenges.setStatus("current")
_JnxMbgTtlAuthRequestTimeouts_Type = Counter64
_JnxMbgTtlAuthRequestTimeouts_Object = MibTableColumn
jnxMbgTtlAuthRequestTimeouts = _JnxMbgTtlAuthRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1, 5),
    _JnxMbgTtlAuthRequestTimeouts_Type()
)
jnxMbgTtlAuthRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAuthRequestTimeouts.setStatus("current")
_JnxMbgTtlAuthRequestTxErrors_Type = Counter64
_JnxMbgTtlAuthRequestTxErrors_Object = MibTableColumn
jnxMbgTtlAuthRequestTxErrors = _JnxMbgTtlAuthRequestTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1, 6),
    _JnxMbgTtlAuthRequestTxErrors_Type()
)
jnxMbgTtlAuthRequestTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAuthRequestTxErrors.setStatus("current")
_JnxMbgTtlAuthResponseErrors_Type = Counter64
_JnxMbgTtlAuthResponseErrors_Object = MibTableColumn
jnxMbgTtlAuthResponseErrors = _JnxMbgTtlAuthResponseErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1, 7),
    _JnxMbgTtlAuthResponseErrors_Type()
)
jnxMbgTtlAuthResponseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAuthResponseErrors.setStatus("current")
_JnxMbgTtlAuthPendingRequests_Type = Counter64
_JnxMbgTtlAuthPendingRequests_Object = MibTableColumn
jnxMbgTtlAuthPendingRequests = _JnxMbgTtlAuthPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 8, 1, 8),
    _JnxMbgTtlAuthPendingRequests_Type()
)
jnxMbgTtlAuthPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAuthPendingRequests.setStatus("current")
_JnxMbgAAAAcctStatsTable_Object = MibTable
jnxMbgAAAAcctStatsTable = _JnxMbgAAAAcctStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 9)
)
if mibBuilder.loadTexts:
    jnxMbgAAAAcctStatsTable.setStatus("current")
_JnxMbgAAAAcctStatsEntry_Object = MibTableRow
jnxMbgAAAAcctStatsEntry = _JnxMbgAAAAcctStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 9, 1)
)
jnxMbgAAAAcctStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgAAAAcctStatsEntry.setStatus("current")
_JnxMbgTtlAcctRequests_Type = Counter64
_JnxMbgTtlAcctRequests_Object = MibTableColumn
jnxMbgTtlAcctRequests = _JnxMbgTtlAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 9, 1, 1),
    _JnxMbgTtlAcctRequests_Type()
)
jnxMbgTtlAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAcctRequests.setStatus("current")
_JnxMbgTtlAcctResp_Type = Counter64
_JnxMbgTtlAcctResp_Object = MibTableColumn
jnxMbgTtlAcctResp = _JnxMbgTtlAcctResp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 9, 1, 2),
    _JnxMbgTtlAcctResp_Type()
)
jnxMbgTtlAcctResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAcctResp.setStatus("current")
_JnxMbgTtlAcctRequestTimeouts_Type = Counter64
_JnxMbgTtlAcctRequestTimeouts_Object = MibTableColumn
jnxMbgTtlAcctRequestTimeouts = _JnxMbgTtlAcctRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 9, 1, 3),
    _JnxMbgTtlAcctRequestTimeouts_Type()
)
jnxMbgTtlAcctRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAcctRequestTimeouts.setStatus("current")
_JnxMbgTtlAcctRequestTxErrors_Type = Counter64
_JnxMbgTtlAcctRequestTxErrors_Object = MibTableColumn
jnxMbgTtlAcctRequestTxErrors = _JnxMbgTtlAcctRequestTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 9, 1, 4),
    _JnxMbgTtlAcctRequestTxErrors_Type()
)
jnxMbgTtlAcctRequestTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAcctRequestTxErrors.setStatus("current")
_JnxMbgTtlAcctResponseErrors_Type = Counter64
_JnxMbgTtlAcctResponseErrors_Object = MibTableColumn
jnxMbgTtlAcctResponseErrors = _JnxMbgTtlAcctResponseErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 9, 1, 5),
    _JnxMbgTtlAcctResponseErrors_Type()
)
jnxMbgTtlAcctResponseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAcctResponseErrors.setStatus("current")
_JnxMbgTtlAcctPendingRequests_Type = Counter64
_JnxMbgTtlAcctPendingRequests_Object = MibTableColumn
jnxMbgTtlAcctPendingRequests = _JnxMbgTtlAcctPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 9, 1, 6),
    _JnxMbgTtlAcctPendingRequests_Type()
)
jnxMbgTtlAcctPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlAcctPendingRequests.setStatus("current")
_JnxMbgAAADynAuthStatsTable_Object = MibTable
jnxMbgAAADynAuthStatsTable = _JnxMbgAAADynAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10)
)
if mibBuilder.loadTexts:
    jnxMbgAAADynAuthStatsTable.setStatus("current")
_JnxMbgAAADynAuthStatsEntry_Object = MibTableRow
jnxMbgAAADynAuthStatsEntry = _JnxMbgAAADynAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1)
)
jnxMbgAAADynAuthStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgAAADynAuthStatsEntry.setStatus("current")
_JnxMbgTtlDynAuthReceived_Type = Counter64
_JnxMbgTtlDynAuthReceived_Object = MibTableColumn
jnxMbgTtlDynAuthReceived = _JnxMbgTtlDynAuthReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 1),
    _JnxMbgTtlDynAuthReceived_Type()
)
jnxMbgTtlDynAuthReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthReceived.setStatus("current")
_JnxMbgTtlDynAuthCoaReceived_Type = Counter64
_JnxMbgTtlDynAuthCoaReceived_Object = MibTableColumn
jnxMbgTtlDynAuthCoaReceived = _JnxMbgTtlDynAuthCoaReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 2),
    _JnxMbgTtlDynAuthCoaReceived_Type()
)
jnxMbgTtlDynAuthCoaReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthCoaReceived.setStatus("current")
_JnxMbgTtlDynAuthDmReceived_Type = Counter64
_JnxMbgTtlDynAuthDmReceived_Object = MibTableColumn
jnxMbgTtlDynAuthDmReceived = _JnxMbgTtlDynAuthDmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 3),
    _JnxMbgTtlDynAuthDmReceived_Type()
)
jnxMbgTtlDynAuthDmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthDmReceived.setStatus("current")
_JnxMbgTtlDynAuthCoaAckSent_Type = Counter64
_JnxMbgTtlDynAuthCoaAckSent_Object = MibTableColumn
jnxMbgTtlDynAuthCoaAckSent = _JnxMbgTtlDynAuthCoaAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 4),
    _JnxMbgTtlDynAuthCoaAckSent_Type()
)
jnxMbgTtlDynAuthCoaAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthCoaAckSent.setStatus("current")
_JnxMbgTtlDynAuthCoaNackSent_Type = Counter64
_JnxMbgTtlDynAuthCoaNackSent_Object = MibTableColumn
jnxMbgTtlDynAuthCoaNackSent = _JnxMbgTtlDynAuthCoaNackSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 5),
    _JnxMbgTtlDynAuthCoaNackSent_Type()
)
jnxMbgTtlDynAuthCoaNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthCoaNackSent.setStatus("current")
_JnxMbgTtlDynAuthDmAckSent_Type = Counter64
_JnxMbgTtlDynAuthDmAckSent_Object = MibTableColumn
jnxMbgTtlDynAuthDmAckSent = _JnxMbgTtlDynAuthDmAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 6),
    _JnxMbgTtlDynAuthDmAckSent_Type()
)
jnxMbgTtlDynAuthDmAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthDmAckSent.setStatus("current")
_JnxMbgTtlDynAuthDmNackSent_Type = Counter64
_JnxMbgTtlDynAuthDmNackSent_Object = MibTableColumn
jnxMbgTtlDynAuthDmNackSent = _JnxMbgTtlDynAuthDmNackSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 7),
    _JnxMbgTtlDynAuthDmNackSent_Type()
)
jnxMbgTtlDynAuthDmNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthDmNackSent.setStatus("current")
_JnxMbgTtlDynAuthDropped_Type = Counter64
_JnxMbgTtlDynAuthDropped_Object = MibTableColumn
jnxMbgTtlDynAuthDropped = _JnxMbgTtlDynAuthDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 8),
    _JnxMbgTtlDynAuthDropped_Type()
)
jnxMbgTtlDynAuthDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthDropped.setStatus("current")
_JnxMbgTtlDynAuthDuplicate_Type = Counter64
_JnxMbgTtlDynAuthDuplicate_Object = MibTableColumn
jnxMbgTtlDynAuthDuplicate = _JnxMbgTtlDynAuthDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 9),
    _JnxMbgTtlDynAuthDuplicate_Type()
)
jnxMbgTtlDynAuthDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthDuplicate.setStatus("current")
_JnxMbgTtlDynAuthForwarded_Type = Counter64
_JnxMbgTtlDynAuthForwarded_Object = MibTableColumn
jnxMbgTtlDynAuthForwarded = _JnxMbgTtlDynAuthForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 10),
    _JnxMbgTtlDynAuthForwarded_Type()
)
jnxMbgTtlDynAuthForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthForwarded.setStatus("current")
_JnxMbgTtlDynAuthTimeouts_Type = Counter64
_JnxMbgTtlDynAuthTimeouts_Object = MibTableColumn
jnxMbgTtlDynAuthTimeouts = _JnxMbgTtlDynAuthTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 11),
    _JnxMbgTtlDynAuthTimeouts_Type()
)
jnxMbgTtlDynAuthTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthTimeouts.setStatus("current")
_JnxMbgTtlDynAuthDelivered_Type = Counter64
_JnxMbgTtlDynAuthDelivered_Object = MibTableColumn
jnxMbgTtlDynAuthDelivered = _JnxMbgTtlDynAuthDelivered_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 12),
    _JnxMbgTtlDynAuthDelivered_Type()
)
jnxMbgTtlDynAuthDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthDelivered.setStatus("current")
_JnxMbgTtlDynAuthErrors_Type = Counter64
_JnxMbgTtlDynAuthErrors_Object = MibTableColumn
jnxMbgTtlDynAuthErrors = _JnxMbgTtlDynAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 13),
    _JnxMbgTtlDynAuthErrors_Type()
)
jnxMbgTtlDynAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthErrors.setStatus("current")
_JnxMbgTtlDynAuthUnknownClnts_Type = Counter64
_JnxMbgTtlDynAuthUnknownClnts_Object = MibTableColumn
jnxMbgTtlDynAuthUnknownClnts = _JnxMbgTtlDynAuthUnknownClnts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 14),
    _JnxMbgTtlDynAuthUnknownClnts_Type()
)
jnxMbgTtlDynAuthUnknownClnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthUnknownClnts.setStatus("current")
_JnxMbgTtlDynAuthInvalidCode_Type = Counter64
_JnxMbgTtlDynAuthInvalidCode_Object = MibTableColumn
jnxMbgTtlDynAuthInvalidCode = _JnxMbgTtlDynAuthInvalidCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 15),
    _JnxMbgTtlDynAuthInvalidCode_Type()
)
jnxMbgTtlDynAuthInvalidCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthInvalidCode.setStatus("current")
_JnxMbgTtlDynAuthInvalidAuth_Type = Counter64
_JnxMbgTtlDynAuthInvalidAuth_Object = MibTableColumn
jnxMbgTtlDynAuthInvalidAuth = _JnxMbgTtlDynAuthInvalidAuth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 16),
    _JnxMbgTtlDynAuthInvalidAuth_Type()
)
jnxMbgTtlDynAuthInvalidAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthInvalidAuth.setStatus("current")
_JnxMbgTtlDynAuthInvalidChId_Type = Counter64
_JnxMbgTtlDynAuthInvalidChId_Object = MibTableColumn
jnxMbgTtlDynAuthInvalidChId = _JnxMbgTtlDynAuthInvalidChId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 17),
    _JnxMbgTtlDynAuthInvalidChId_Type()
)
jnxMbgTtlDynAuthInvalidChId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthInvalidChId.setStatus("current")
_JnxMbgTtlDynAuthMapErrors_Type = Counter64
_JnxMbgTtlDynAuthMapErrors_Object = MibTableColumn
jnxMbgTtlDynAuthMapErrors = _JnxMbgTtlDynAuthMapErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 18),
    _JnxMbgTtlDynAuthMapErrors_Type()
)
jnxMbgTtlDynAuthMapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthMapErrors.setStatus("current")
_JnxMbgTtlDynAuthInvalidTrId_Type = Counter64
_JnxMbgTtlDynAuthInvalidTrId_Object = MibTableColumn
jnxMbgTtlDynAuthInvalidTrId = _JnxMbgTtlDynAuthInvalidTrId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 10, 1, 19),
    _JnxMbgTtlDynAuthInvalidTrId_Type()
)
jnxMbgTtlDynAuthInvalidTrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgTtlDynAuthInvalidTrId.setStatus("current")
_JnxMbgRadiusAuthSrvrTable_Object = MibTable
jnxMbgRadiusAuthSrvrTable = _JnxMbgRadiusAuthSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11)
)
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrTable.setStatus("current")
_JnxMbgRadiusAuthSrvrEntry_Object = MibTableRow
jnxMbgRadiusAuthSrvrEntry = _JnxMbgRadiusAuthSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1)
)
jnxMbgRadiusAuthSrvrEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgRadiusAuthSrvrName"),
)
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrEntry.setStatus("current")


class _JnxMbgRadiusAuthSrvrName_Type(DisplayString):
    """Custom type jnxMbgRadiusAuthSrvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxMbgRadiusAuthSrvrName_Type.__name__ = "DisplayString"
_JnxMbgRadiusAuthSrvrName_Object = MibTableColumn
jnxMbgRadiusAuthSrvrName = _JnxMbgRadiusAuthSrvrName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 1),
    _JnxMbgRadiusAuthSrvrName_Type()
)
jnxMbgRadiusAuthSrvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrName.setStatus("current")
_JnxMbgRadiusAuthSrvrInetAddrType_Type = InetAddressType
_JnxMbgRadiusAuthSrvrInetAddrType_Object = MibTableColumn
jnxMbgRadiusAuthSrvrInetAddrType = _JnxMbgRadiusAuthSrvrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 2),
    _JnxMbgRadiusAuthSrvrInetAddrType_Type()
)
jnxMbgRadiusAuthSrvrInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrInetAddrType.setStatus("current")
_JnxMbgRadiusAuthSrvrInetAddress_Type = InetAddress
_JnxMbgRadiusAuthSrvrInetAddress_Object = MibTableColumn
jnxMbgRadiusAuthSrvrInetAddress = _JnxMbgRadiusAuthSrvrInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 3),
    _JnxMbgRadiusAuthSrvrInetAddress_Type()
)
jnxMbgRadiusAuthSrvrInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrInetAddress.setStatus("current")
_JnxMbgRadiusAuthSrvrInetPort_Type = InetPortNumber
_JnxMbgRadiusAuthSrvrInetPort_Object = MibTableColumn
jnxMbgRadiusAuthSrvrInetPort = _JnxMbgRadiusAuthSrvrInetPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 4),
    _JnxMbgRadiusAuthSrvrInetPort_Type()
)
jnxMbgRadiusAuthSrvrInetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrInetPort.setStatus("current")
_JnxMbgRadiusAuthSrvrRtngInstance_Type = DisplayString
_JnxMbgRadiusAuthSrvrRtngInstance_Object = MibTableColumn
jnxMbgRadiusAuthSrvrRtngInstance = _JnxMbgRadiusAuthSrvrRtngInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 5),
    _JnxMbgRadiusAuthSrvrRtngInstance_Type()
)
jnxMbgRadiusAuthSrvrRtngInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrRtngInstance.setStatus("current")
_JnxMbgRadiusAuthSrvrStatus_Type = JnxMbgAAAServerStatus
_JnxMbgRadiusAuthSrvrStatus_Object = MibTableColumn
jnxMbgRadiusAuthSrvrStatus = _JnxMbgRadiusAuthSrvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 6),
    _JnxMbgRadiusAuthSrvrStatus_Type()
)
jnxMbgRadiusAuthSrvrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrStatus.setStatus("current")
_JnxMbgRadiusAuthSrvrRequests_Type = Counter64
_JnxMbgRadiusAuthSrvrRequests_Object = MibTableColumn
jnxMbgRadiusAuthSrvrRequests = _JnxMbgRadiusAuthSrvrRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 7),
    _JnxMbgRadiusAuthSrvrRequests_Type()
)
jnxMbgRadiusAuthSrvrRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrRequests.setStatus("current")
_JnxMbgRadiusAuthSrvrRetrans_Type = Counter64
_JnxMbgRadiusAuthSrvrRetrans_Object = MibTableColumn
jnxMbgRadiusAuthSrvrRetrans = _JnxMbgRadiusAuthSrvrRetrans_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 8),
    _JnxMbgRadiusAuthSrvrRetrans_Type()
)
jnxMbgRadiusAuthSrvrRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrRetrans.setStatus("current")
_JnxMbgRadiusAuthSrvrAccepts_Type = Counter64
_JnxMbgRadiusAuthSrvrAccepts_Object = MibTableColumn
jnxMbgRadiusAuthSrvrAccepts = _JnxMbgRadiusAuthSrvrAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 9),
    _JnxMbgRadiusAuthSrvrAccepts_Type()
)
jnxMbgRadiusAuthSrvrAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrAccepts.setStatus("current")
_JnxMbgRadiusAuthSrvrRejects_Type = Counter64
_JnxMbgRadiusAuthSrvrRejects_Object = MibTableColumn
jnxMbgRadiusAuthSrvrRejects = _JnxMbgRadiusAuthSrvrRejects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 10),
    _JnxMbgRadiusAuthSrvrRejects_Type()
)
jnxMbgRadiusAuthSrvrRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrRejects.setStatus("current")
_JnxMbgRadiusAuthSrvrChallenges_Type = Counter64
_JnxMbgRadiusAuthSrvrChallenges_Object = MibTableColumn
jnxMbgRadiusAuthSrvrChallenges = _JnxMbgRadiusAuthSrvrChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 11),
    _JnxMbgRadiusAuthSrvrChallenges_Type()
)
jnxMbgRadiusAuthSrvrChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrChallenges.setStatus("current")
_JnxMbgRadiusAuthSrvrMalformResp_Type = Counter64
_JnxMbgRadiusAuthSrvrMalformResp_Object = MibTableColumn
jnxMbgRadiusAuthSrvrMalformResp = _JnxMbgRadiusAuthSrvrMalformResp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 12),
    _JnxMbgRadiusAuthSrvrMalformResp_Type()
)
jnxMbgRadiusAuthSrvrMalformResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrMalformResp.setStatus("current")
_JnxMbgRadiusAuthSrvrBadAuthen_Type = Counter64
_JnxMbgRadiusAuthSrvrBadAuthen_Object = MibTableColumn
jnxMbgRadiusAuthSrvrBadAuthen = _JnxMbgRadiusAuthSrvrBadAuthen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 13),
    _JnxMbgRadiusAuthSrvrBadAuthen_Type()
)
jnxMbgRadiusAuthSrvrBadAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrBadAuthen.setStatus("current")
_JnxMbgRadiusAuthSrvrPendingRqsts_Type = Counter64
_JnxMbgRadiusAuthSrvrPendingRqsts_Object = MibTableColumn
jnxMbgRadiusAuthSrvrPendingRqsts = _JnxMbgRadiusAuthSrvrPendingRqsts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 14),
    _JnxMbgRadiusAuthSrvrPendingRqsts_Type()
)
jnxMbgRadiusAuthSrvrPendingRqsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrPendingRqsts.setStatus("current")
_JnxMbgRadiusAuthSrvrTimeouts_Type = Counter64
_JnxMbgRadiusAuthSrvrTimeouts_Object = MibTableColumn
jnxMbgRadiusAuthSrvrTimeouts = _JnxMbgRadiusAuthSrvrTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 15),
    _JnxMbgRadiusAuthSrvrTimeouts_Type()
)
jnxMbgRadiusAuthSrvrTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrTimeouts.setStatus("current")
_JnxMbgRadiusAuthSrvrUnknownTypes_Type = Counter64
_JnxMbgRadiusAuthSrvrUnknownTypes_Object = MibTableColumn
jnxMbgRadiusAuthSrvrUnknownTypes = _JnxMbgRadiusAuthSrvrUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 16),
    _JnxMbgRadiusAuthSrvrUnknownTypes_Type()
)
jnxMbgRadiusAuthSrvrUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrUnknownTypes.setStatus("current")
_JnxMbgRadiusAuthSrvrPacketsDrop_Type = Counter64
_JnxMbgRadiusAuthSrvrPacketsDrop_Object = MibTableColumn
jnxMbgRadiusAuthSrvrPacketsDrop = _JnxMbgRadiusAuthSrvrPacketsDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 17),
    _JnxMbgRadiusAuthSrvrPacketsDrop_Type()
)
jnxMbgRadiusAuthSrvrPacketsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrPacketsDrop.setStatus("current")
_JnxMbgRadiusAuthSrvrRTTAvg_Type = Gauge32
_JnxMbgRadiusAuthSrvrRTTAvg_Object = MibTableColumn
jnxMbgRadiusAuthSrvrRTTAvg = _JnxMbgRadiusAuthSrvrRTTAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 18),
    _JnxMbgRadiusAuthSrvrRTTAvg_Type()
)
jnxMbgRadiusAuthSrvrRTTAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrRTTAvg.setStatus("current")
_JnxMbgRadiusAuthSrvrRTTMin_Type = Gauge32
_JnxMbgRadiusAuthSrvrRTTMin_Object = MibTableColumn
jnxMbgRadiusAuthSrvrRTTMin = _JnxMbgRadiusAuthSrvrRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 19),
    _JnxMbgRadiusAuthSrvrRTTMin_Type()
)
jnxMbgRadiusAuthSrvrRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrRTTMin.setStatus("current")
_JnxMbgRadiusAuthSrvrRTTMax_Type = Gauge32
_JnxMbgRadiusAuthSrvrRTTMax_Object = MibTableColumn
jnxMbgRadiusAuthSrvrRTTMax = _JnxMbgRadiusAuthSrvrRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 11, 1, 20),
    _JnxMbgRadiusAuthSrvrRTTMax_Type()
)
jnxMbgRadiusAuthSrvrRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAuthSrvrRTTMax.setStatus("current")
_JnxMbgRadiusAcctSrvrTable_Object = MibTable
jnxMbgRadiusAcctSrvrTable = _JnxMbgRadiusAcctSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12)
)
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrTable.setStatus("current")
_JnxMbgRadiusAcctSrvrEntry_Object = MibTableRow
jnxMbgRadiusAcctSrvrEntry = _JnxMbgRadiusAcctSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1)
)
jnxMbgRadiusAcctSrvrEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgRadiusAcctSrvrName"),
)
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrEntry.setStatus("current")


class _JnxMbgRadiusAcctSrvrName_Type(DisplayString):
    """Custom type jnxMbgRadiusAcctSrvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxMbgRadiusAcctSrvrName_Type.__name__ = "DisplayString"
_JnxMbgRadiusAcctSrvrName_Object = MibTableColumn
jnxMbgRadiusAcctSrvrName = _JnxMbgRadiusAcctSrvrName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 1),
    _JnxMbgRadiusAcctSrvrName_Type()
)
jnxMbgRadiusAcctSrvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrName.setStatus("current")
_JnxMbgRadiusAcctSrvrInetAddrType_Type = InetAddressType
_JnxMbgRadiusAcctSrvrInetAddrType_Object = MibTableColumn
jnxMbgRadiusAcctSrvrInetAddrType = _JnxMbgRadiusAcctSrvrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 2),
    _JnxMbgRadiusAcctSrvrInetAddrType_Type()
)
jnxMbgRadiusAcctSrvrInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrInetAddrType.setStatus("current")
_JnxMbgRadiusAcctSrvrInetAddress_Type = InetAddress
_JnxMbgRadiusAcctSrvrInetAddress_Object = MibTableColumn
jnxMbgRadiusAcctSrvrInetAddress = _JnxMbgRadiusAcctSrvrInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 3),
    _JnxMbgRadiusAcctSrvrInetAddress_Type()
)
jnxMbgRadiusAcctSrvrInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrInetAddress.setStatus("current")
_JnxMbgRadiusAcctSrvrInetPort_Type = InetPortNumber
_JnxMbgRadiusAcctSrvrInetPort_Object = MibTableColumn
jnxMbgRadiusAcctSrvrInetPort = _JnxMbgRadiusAcctSrvrInetPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 4),
    _JnxMbgRadiusAcctSrvrInetPort_Type()
)
jnxMbgRadiusAcctSrvrInetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrInetPort.setStatus("current")
_JnxMbgRadiusAcctSrvrRtngInstance_Type = DisplayString
_JnxMbgRadiusAcctSrvrRtngInstance_Object = MibTableColumn
jnxMbgRadiusAcctSrvrRtngInstance = _JnxMbgRadiusAcctSrvrRtngInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 5),
    _JnxMbgRadiusAcctSrvrRtngInstance_Type()
)
jnxMbgRadiusAcctSrvrRtngInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrRtngInstance.setStatus("current")
_JnxMbgRadiusAcctSrvrStatus_Type = JnxMbgAAAServerStatus
_JnxMbgRadiusAcctSrvrStatus_Object = MibTableColumn
jnxMbgRadiusAcctSrvrStatus = _JnxMbgRadiusAcctSrvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 6),
    _JnxMbgRadiusAcctSrvrStatus_Type()
)
jnxMbgRadiusAcctSrvrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrStatus.setStatus("current")
_JnxMbgRadiusAcctSrvrRequests_Type = Counter64
_JnxMbgRadiusAcctSrvrRequests_Object = MibTableColumn
jnxMbgRadiusAcctSrvrRequests = _JnxMbgRadiusAcctSrvrRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 7),
    _JnxMbgRadiusAcctSrvrRequests_Type()
)
jnxMbgRadiusAcctSrvrRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrRequests.setStatus("current")
_JnxMbgRadiusAcctSrvrRetrans_Type = Counter64
_JnxMbgRadiusAcctSrvrRetrans_Object = MibTableColumn
jnxMbgRadiusAcctSrvrRetrans = _JnxMbgRadiusAcctSrvrRetrans_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 8),
    _JnxMbgRadiusAcctSrvrRetrans_Type()
)
jnxMbgRadiusAcctSrvrRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrRetrans.setStatus("current")
_JnxMbgRadiusAcctSrvrResp_Type = Counter64
_JnxMbgRadiusAcctSrvrResp_Object = MibTableColumn
jnxMbgRadiusAcctSrvrResp = _JnxMbgRadiusAcctSrvrResp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 9),
    _JnxMbgRadiusAcctSrvrResp_Type()
)
jnxMbgRadiusAcctSrvrResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrResp.setStatus("current")
_JnxMbgRadiusAcctSrvrMalformResp_Type = Counter64
_JnxMbgRadiusAcctSrvrMalformResp_Object = MibTableColumn
jnxMbgRadiusAcctSrvrMalformResp = _JnxMbgRadiusAcctSrvrMalformResp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 10),
    _JnxMbgRadiusAcctSrvrMalformResp_Type()
)
jnxMbgRadiusAcctSrvrMalformResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrMalformResp.setStatus("current")
_JnxMbgRadiusAcctSrvrBadAuthen_Type = Counter64
_JnxMbgRadiusAcctSrvrBadAuthen_Object = MibTableColumn
jnxMbgRadiusAcctSrvrBadAuthen = _JnxMbgRadiusAcctSrvrBadAuthen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 11),
    _JnxMbgRadiusAcctSrvrBadAuthen_Type()
)
jnxMbgRadiusAcctSrvrBadAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrBadAuthen.setStatus("current")
_JnxMbgRadiusAcctSrvrPendingRqsts_Type = Counter64
_JnxMbgRadiusAcctSrvrPendingRqsts_Object = MibTableColumn
jnxMbgRadiusAcctSrvrPendingRqsts = _JnxMbgRadiusAcctSrvrPendingRqsts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 12),
    _JnxMbgRadiusAcctSrvrPendingRqsts_Type()
)
jnxMbgRadiusAcctSrvrPendingRqsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrPendingRqsts.setStatus("current")
_JnxMbgRadiusAcctSrvrTimeouts_Type = Counter64
_JnxMbgRadiusAcctSrvrTimeouts_Object = MibTableColumn
jnxMbgRadiusAcctSrvrTimeouts = _JnxMbgRadiusAcctSrvrTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 13),
    _JnxMbgRadiusAcctSrvrTimeouts_Type()
)
jnxMbgRadiusAcctSrvrTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrTimeouts.setStatus("current")
_JnxMbgRadiusAcctSrvrUnknownTypes_Type = Counter64
_JnxMbgRadiusAcctSrvrUnknownTypes_Object = MibTableColumn
jnxMbgRadiusAcctSrvrUnknownTypes = _JnxMbgRadiusAcctSrvrUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 14),
    _JnxMbgRadiusAcctSrvrUnknownTypes_Type()
)
jnxMbgRadiusAcctSrvrUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrUnknownTypes.setStatus("current")
_JnxMbgRadiusAcctSrvrPacketsDrop_Type = Counter64
_JnxMbgRadiusAcctSrvrPacketsDrop_Object = MibTableColumn
jnxMbgRadiusAcctSrvrPacketsDrop = _JnxMbgRadiusAcctSrvrPacketsDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 15),
    _JnxMbgRadiusAcctSrvrPacketsDrop_Type()
)
jnxMbgRadiusAcctSrvrPacketsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrPacketsDrop.setStatus("current")
_JnxMbgRadiusAcctSrvrRTTAvg_Type = Gauge32
_JnxMbgRadiusAcctSrvrRTTAvg_Object = MibTableColumn
jnxMbgRadiusAcctSrvrRTTAvg = _JnxMbgRadiusAcctSrvrRTTAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 16),
    _JnxMbgRadiusAcctSrvrRTTAvg_Type()
)
jnxMbgRadiusAcctSrvrRTTAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrRTTAvg.setStatus("current")
_JnxMbgRadiusAcctSrvrRTTMin_Type = Gauge32
_JnxMbgRadiusAcctSrvrRTTMin_Object = MibTableColumn
jnxMbgRadiusAcctSrvrRTTMin = _JnxMbgRadiusAcctSrvrRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 17),
    _JnxMbgRadiusAcctSrvrRTTMin_Type()
)
jnxMbgRadiusAcctSrvrRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrRTTMin.setStatus("current")
_JnxMbgRadiusAcctSrvrRTTMax_Type = Gauge32
_JnxMbgRadiusAcctSrvrRTTMax_Object = MibTableColumn
jnxMbgRadiusAcctSrvrRTTMax = _JnxMbgRadiusAcctSrvrRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 12, 1, 18),
    _JnxMbgRadiusAcctSrvrRTTMax_Type()
)
jnxMbgRadiusAcctSrvrRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgRadiusAcctSrvrRTTMax.setStatus("current")
_JnxMbgDynAuthClntTable_Object = MibTable
jnxMbgDynAuthClntTable = _JnxMbgDynAuthClntTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13)
)
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntTable.setStatus("current")
_JnxMbgDynAuthClntEntry_Object = MibTableRow
jnxMbgDynAuthClntEntry = _JnxMbgDynAuthClntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1)
)
jnxMbgDynAuthClntEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgDynAuthClntName"),
)
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntEntry.setStatus("current")


class _JnxMbgDynAuthClntName_Type(DisplayString):
    """Custom type jnxMbgDynAuthClntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxMbgDynAuthClntName_Type.__name__ = "DisplayString"
_JnxMbgDynAuthClntName_Object = MibTableColumn
jnxMbgDynAuthClntName = _JnxMbgDynAuthClntName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 1),
    _JnxMbgDynAuthClntName_Type()
)
jnxMbgDynAuthClntName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntName.setStatus("current")
_JnxMbgDynAuthClntInAddrType_Type = InetAddressType
_JnxMbgDynAuthClntInAddrType_Object = MibTableColumn
jnxMbgDynAuthClntInAddrType = _JnxMbgDynAuthClntInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 2),
    _JnxMbgDynAuthClntInAddrType_Type()
)
jnxMbgDynAuthClntInAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntInAddrType.setStatus("current")
_JnxMbgDynAuthClntInetAddress_Type = InetAddress
_JnxMbgDynAuthClntInetAddress_Object = MibTableColumn
jnxMbgDynAuthClntInetAddress = _JnxMbgDynAuthClntInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 3),
    _JnxMbgDynAuthClntInetAddress_Type()
)
jnxMbgDynAuthClntInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntInetAddress.setStatus("current")
_JnxMbgDynAuthClntCoaReceived_Type = Counter64
_JnxMbgDynAuthClntCoaReceived_Object = MibTableColumn
jnxMbgDynAuthClntCoaReceived = _JnxMbgDynAuthClntCoaReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 4),
    _JnxMbgDynAuthClntCoaReceived_Type()
)
jnxMbgDynAuthClntCoaReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntCoaReceived.setStatus("current")
_JnxMbgDynAuthClntDmReceived_Type = Counter64
_JnxMbgDynAuthClntDmReceived_Object = MibTableColumn
jnxMbgDynAuthClntDmReceived = _JnxMbgDynAuthClntDmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 5),
    _JnxMbgDynAuthClntDmReceived_Type()
)
jnxMbgDynAuthClntDmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntDmReceived.setStatus("current")
_JnxMbgDynAuthClntCoaAckSent_Type = Counter64
_JnxMbgDynAuthClntCoaAckSent_Object = MibTableColumn
jnxMbgDynAuthClntCoaAckSent = _JnxMbgDynAuthClntCoaAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 6),
    _JnxMbgDynAuthClntCoaAckSent_Type()
)
jnxMbgDynAuthClntCoaAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntCoaAckSent.setStatus("current")
_JnxMbgDynAuthClntCoaNackSent_Type = Counter64
_JnxMbgDynAuthClntCoaNackSent_Object = MibTableColumn
jnxMbgDynAuthClntCoaNackSent = _JnxMbgDynAuthClntCoaNackSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 7),
    _JnxMbgDynAuthClntCoaNackSent_Type()
)
jnxMbgDynAuthClntCoaNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntCoaNackSent.setStatus("current")
_JnxMbgDynAuthClntDmAckSent_Type = Counter64
_JnxMbgDynAuthClntDmAckSent_Object = MibTableColumn
jnxMbgDynAuthClntDmAckSent = _JnxMbgDynAuthClntDmAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 8),
    _JnxMbgDynAuthClntDmAckSent_Type()
)
jnxMbgDynAuthClntDmAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntDmAckSent.setStatus("current")
_JnxMbgDynAuthClntDmNackSent_Type = Counter64
_JnxMbgDynAuthClntDmNackSent_Object = MibTableColumn
jnxMbgDynAuthClntDmNackSent = _JnxMbgDynAuthClntDmNackSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 9),
    _JnxMbgDynAuthClntDmNackSent_Type()
)
jnxMbgDynAuthClntDmNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntDmNackSent.setStatus("current")
_JnxMbgDynAuthClntDropped_Type = Counter64
_JnxMbgDynAuthClntDropped_Object = MibTableColumn
jnxMbgDynAuthClntDropped = _JnxMbgDynAuthClntDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 10),
    _JnxMbgDynAuthClntDropped_Type()
)
jnxMbgDynAuthClntDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntDropped.setStatus("current")
_JnxMbgDynAuthClntDuplicate_Type = Counter64
_JnxMbgDynAuthClntDuplicate_Object = MibTableColumn
jnxMbgDynAuthClntDuplicate = _JnxMbgDynAuthClntDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 11),
    _JnxMbgDynAuthClntDuplicate_Type()
)
jnxMbgDynAuthClntDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntDuplicate.setStatus("current")
_JnxMbgDynAuthClntForwarded_Type = Counter64
_JnxMbgDynAuthClntForwarded_Object = MibTableColumn
jnxMbgDynAuthClntForwarded = _JnxMbgDynAuthClntForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 12),
    _JnxMbgDynAuthClntForwarded_Type()
)
jnxMbgDynAuthClntForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntForwarded.setStatus("current")
_JnxMbgDynAuthClntTimeouts_Type = Counter64
_JnxMbgDynAuthClntTimeouts_Object = MibTableColumn
jnxMbgDynAuthClntTimeouts = _JnxMbgDynAuthClntTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 13),
    _JnxMbgDynAuthClntTimeouts_Type()
)
jnxMbgDynAuthClntTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntTimeouts.setStatus("current")
_JnxMbgDynAuthClntDelivered_Type = Counter64
_JnxMbgDynAuthClntDelivered_Object = MibTableColumn
jnxMbgDynAuthClntDelivered = _JnxMbgDynAuthClntDelivered_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 14),
    _JnxMbgDynAuthClntDelivered_Type()
)
jnxMbgDynAuthClntDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntDelivered.setStatus("current")
_JnxMbgDynAuthClntErrors_Type = Counter64
_JnxMbgDynAuthClntErrors_Object = MibTableColumn
jnxMbgDynAuthClntErrors = _JnxMbgDynAuthClntErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 15),
    _JnxMbgDynAuthClntErrors_Type()
)
jnxMbgDynAuthClntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntErrors.setStatus("current")
_JnxMbgDynAuthClntInvalidAuth_Type = Counter64
_JnxMbgDynAuthClntInvalidAuth_Object = MibTableColumn
jnxMbgDynAuthClntInvalidAuth = _JnxMbgDynAuthClntInvalidAuth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 16),
    _JnxMbgDynAuthClntInvalidAuth_Type()
)
jnxMbgDynAuthClntInvalidAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntInvalidAuth.setStatus("current")
_JnxMbgDynAuthClntInvalidCode_Type = Counter64
_JnxMbgDynAuthClntInvalidCode_Object = MibTableColumn
jnxMbgDynAuthClntInvalidCode = _JnxMbgDynAuthClntInvalidCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 17),
    _JnxMbgDynAuthClntInvalidCode_Type()
)
jnxMbgDynAuthClntInvalidCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntInvalidCode.setStatus("current")
_JnxMbgDynAuthClntInvalidChId_Type = Counter64
_JnxMbgDynAuthClntInvalidChId_Object = MibTableColumn
jnxMbgDynAuthClntInvalidChId = _JnxMbgDynAuthClntInvalidChId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 18),
    _JnxMbgDynAuthClntInvalidChId_Type()
)
jnxMbgDynAuthClntInvalidChId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntInvalidChId.setStatus("current")
_JnxMbgDynAuthClntMapErrors_Type = Counter64
_JnxMbgDynAuthClntMapErrors_Object = MibTableColumn
jnxMbgDynAuthClntMapErrors = _JnxMbgDynAuthClntMapErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 1, 13, 1, 19),
    _JnxMbgDynAuthClntMapErrors_Type()
)
jnxMbgDynAuthClntMapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgDynAuthClntMapErrors.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgAAAServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 1)
)
jnxMbgAAAServerUp.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAAServerName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"))
)
if mibBuilder.loadTexts:
    jnxMbgAAAServerUp.setStatus(
        "deprecated"
    )

jnxMbgAAAServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 2)
)
jnxMbgAAAServerDown.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAAServerName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"))
)
if mibBuilder.loadTexts:
    jnxMbgAAAServerDown.setStatus(
        "deprecated"
    )

jnxMbgAAANetworkElementUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 3)
)
jnxMbgAAANetworkElementUp.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAANetworkElementName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"))
)
if mibBuilder.loadTexts:
    jnxMbgAAANetworkElementUp.setStatus(
        "deprecated"
    )

jnxMbgAAANetworkElementDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 4)
)
jnxMbgAAANetworkElementDown.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAANetworkElementName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"))
)
if mibBuilder.loadTexts:
    jnxMbgAAANetworkElementDown.setStatus(
        "deprecated"
    )

jnxMbgAAANEPendAuthQStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 5)
)
jnxMbgAAANEPendAuthQStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAANetworkElementName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQWaterMarkType"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQWaterMarkValue"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQLength"))
)
if mibBuilder.loadTexts:
    jnxMbgAAANEPendAuthQStatus.setStatus(
        "deprecated"
    )

jnxMbgAAANEPendAcctQStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 6)
)
jnxMbgAAANEPendAcctQStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAANetworkElementName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQWaterMarkType"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQWaterMarkValue"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQLength"))
)
if mibBuilder.loadTexts:
    jnxMbgAAANEPendAcctQStatus.setStatus(
        "deprecated"
    )

jnxMbgAAARadiusServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 7)
)
jnxMbgAAARadiusServerUp.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
        ("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAAServerName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"))
)
if mibBuilder.loadTexts:
    jnxMbgAAARadiusServerUp.setStatus(
        "current"
    )

jnxMbgAAARadiusServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 8)
)
jnxMbgAAARadiusServerDown.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
        ("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAAServerName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"))
)
if mibBuilder.loadTexts:
    jnxMbgAAARadiusServerDown.setStatus(
        "current"
    )

jnxMbgAAARadiusNetworkElementUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 9)
)
jnxMbgAAARadiusNetworkElementUp.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
        ("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAANetworkElementName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"))
)
if mibBuilder.loadTexts:
    jnxMbgAAARadiusNetworkElementUp.setStatus(
        "current"
    )

jnxMbgAAARadiusNetworkElementDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 10)
)
jnxMbgAAARadiusNetworkElementDown.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
        ("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAANetworkElementName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"))
)
if mibBuilder.loadTexts:
    jnxMbgAAARadiusNetworkElementDown.setStatus(
        "current"
    )

jnxMbgAAARadiusNEPendAuthQStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 11)
)
jnxMbgAAARadiusNEPendAuthQStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
        ("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAANetworkElementName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQWaterMarkType"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQWaterMarkValue"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQLength"))
)
if mibBuilder.loadTexts:
    jnxMbgAAARadiusNEPendAuthQStatus.setStatus(
        "current"
    )

jnxMbgAAARadiusNEPendAcctQStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 3, 0, 12)
)
jnxMbgAAARadiusNEPendAcctQStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
        ("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgAAANetworkElementName"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgSPIdentifier"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQWaterMarkType"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQWaterMarkValue"),
        ("JUNIPER-MOBILE-GATEWAY-AAA-MIB", "jnxMbgPendQLength"))
)
if mibBuilder.loadTexts:
    jnxMbgAAARadiusNEPendAcctQStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-AAA-MIB",
    **{"JnxMbgAAAServerStatus": JnxMbgAAAServerStatus,
       "JnxMbgQueueWaterMarkType": JnxMbgQueueWaterMarkType,
       "jnxMobileGatewayPgwAAAMib": jnxMobileGatewayPgwAAAMib,
       "jnxMbgAAANotifications": jnxMbgAAANotifications,
       "jnxMbgAAAServerUp": jnxMbgAAAServerUp,
       "jnxMbgAAAServerDown": jnxMbgAAAServerDown,
       "jnxMbgAAANetworkElementUp": jnxMbgAAANetworkElementUp,
       "jnxMbgAAANetworkElementDown": jnxMbgAAANetworkElementDown,
       "jnxMbgAAANEPendAuthQStatus": jnxMbgAAANEPendAuthQStatus,
       "jnxMbgAAANEPendAcctQStatus": jnxMbgAAANEPendAcctQStatus,
       "jnxMbgAAARadiusServerUp": jnxMbgAAARadiusServerUp,
       "jnxMbgAAARadiusServerDown": jnxMbgAAARadiusServerDown,
       "jnxMbgAAARadiusNetworkElementUp": jnxMbgAAARadiusNetworkElementUp,
       "jnxMbgAAARadiusNetworkElementDown": jnxMbgAAARadiusNetworkElementDown,
       "jnxMbgAAARadiusNEPendAuthQStatus": jnxMbgAAARadiusNEPendAuthQStatus,
       "jnxMbgAAARadiusNEPendAcctQStatus": jnxMbgAAARadiusNEPendAcctQStatus,
       "jnxMbgAAAObjects": jnxMbgAAAObjects,
       "jnxMbgAAAGlobalAuthStats": jnxMbgAAAGlobalAuthStats,
       "jnxMbgTotalAuthRequests": jnxMbgTotalAuthRequests,
       "jnxMbgTotalAuthAccepts": jnxMbgTotalAuthAccepts,
       "jnxMbgTotalAuthRejects": jnxMbgTotalAuthRejects,
       "jnxMbgTotalAuthChallenges": jnxMbgTotalAuthChallenges,
       "jnxMbgTotalAuthRequestTimeouts": jnxMbgTotalAuthRequestTimeouts,
       "jnxMbgTotalAuthRequestTxErrors": jnxMbgTotalAuthRequestTxErrors,
       "jnxMbgTotalAuthResponseErrors": jnxMbgTotalAuthResponseErrors,
       "jnxMbgTotalAuthPendingRequests": jnxMbgTotalAuthPendingRequests,
       "jnxMbgAAAGlobalAcctStats": jnxMbgAAAGlobalAcctStats,
       "jnxMbgTotalAcctRequests": jnxMbgTotalAcctRequests,
       "jnxMbgTotalAcctResponses": jnxMbgTotalAcctResponses,
       "jnxMbgTotalAcctRequestTimeouts": jnxMbgTotalAcctRequestTimeouts,
       "jnxMbgTotalAcctRequestTxErrors": jnxMbgTotalAcctRequestTxErrors,
       "jnxMbgTotalAcctResponseErrors": jnxMbgTotalAcctResponseErrors,
       "jnxMbgTotalAcctPendingRequests": jnxMbgTotalAcctPendingRequests,
       "jnxMbgAAAGlobalDynAuthStats": jnxMbgAAAGlobalDynAuthStats,
       "jnxMbgTotalDynAuthReceived": jnxMbgTotalDynAuthReceived,
       "jnxMbgTotalDynAuthCoaReceived": jnxMbgTotalDynAuthCoaReceived,
       "jnxMbgTotalDynAuthDmReceived": jnxMbgTotalDynAuthDmReceived,
       "jnxMbgTotalDynAuthCoaAckSent": jnxMbgTotalDynAuthCoaAckSent,
       "jnxMbgTotalDynAuthCoaNackSent": jnxMbgTotalDynAuthCoaNackSent,
       "jnxMbgTotalDynAuthDmAckSent": jnxMbgTotalDynAuthDmAckSent,
       "jnxMbgTotalDynAuthDmNackSent": jnxMbgTotalDynAuthDmNackSent,
       "jnxMbgTotalDynAuthDropped": jnxMbgTotalDynAuthDropped,
       "jnxMbgTotalDynAuthDuplicate": jnxMbgTotalDynAuthDuplicate,
       "jnxMbgTotalDynAuthForwarded": jnxMbgTotalDynAuthForwarded,
       "jnxMbgTotalDynAuthTimeouts": jnxMbgTotalDynAuthTimeouts,
       "jnxMbgTotalDynAuthDelivered": jnxMbgTotalDynAuthDelivered,
       "jnxMbgTotalDynAuthErrors": jnxMbgTotalDynAuthErrors,
       "jnxMbgTotalDynAuthUnknownClnts": jnxMbgTotalDynAuthUnknownClnts,
       "jnxMbgTotalDynAuthInvalidCode": jnxMbgTotalDynAuthInvalidCode,
       "jnxMbgTotalDynAuthInvalidAuth": jnxMbgTotalDynAuthInvalidAuth,
       "jnxMbgTotalDynAuthInvalidChId": jnxMbgTotalDynAuthInvalidChId,
       "jnxMbgTotalDynAuthMapErrors": jnxMbgTotalDynAuthMapErrors,
       "jnxMbgTotalDynAuthInvalidTrId": jnxMbgTotalDynAuthInvalidTrId,
       "jnxMbgRadiusAuthServerTable": jnxMbgRadiusAuthServerTable,
       "jnxMbgRadiusAuthServerEntry": jnxMbgRadiusAuthServerEntry,
       "jnxMbgRadiusAuthServerName": jnxMbgRadiusAuthServerName,
       "jnxMbgRadiusAuthServerInetAddressType": jnxMbgRadiusAuthServerInetAddressType,
       "jnxMbgRadiusAuthServerInetAddress": jnxMbgRadiusAuthServerInetAddress,
       "jnxMbgRadiusAuthServerInetPort": jnxMbgRadiusAuthServerInetPort,
       "jnxMbgRadiusAuthServerRoutingInstance": jnxMbgRadiusAuthServerRoutingInstance,
       "jnxMbgRadiusAuthServerStatus": jnxMbgRadiusAuthServerStatus,
       "jnxMbgRadiusAuthServerRequests": jnxMbgRadiusAuthServerRequests,
       "jnxMbgRadiusAuthServersRetransmissions": jnxMbgRadiusAuthServersRetransmissions,
       "jnxMbgRadiusAuthServerAccepts": jnxMbgRadiusAuthServerAccepts,
       "jnxMbgRadiusAuthServerRejects": jnxMbgRadiusAuthServerRejects,
       "jnxMbgRadiusAuthServerChallenges": jnxMbgRadiusAuthServerChallenges,
       "jnxMbgRadiusAuthServerMalformedResponses": jnxMbgRadiusAuthServerMalformedResponses,
       "jnxMbgRadiusAuthServerBadAuthenticators": jnxMbgRadiusAuthServerBadAuthenticators,
       "jnxMbgRadiusAuthServerPendingRequests": jnxMbgRadiusAuthServerPendingRequests,
       "jnxMbgRadiusAuthServerTimeouts": jnxMbgRadiusAuthServerTimeouts,
       "jnxMbgRadiusAuthServerUnknownTypes": jnxMbgRadiusAuthServerUnknownTypes,
       "jnxMbgRadiusAuthServerPacketsDropped": jnxMbgRadiusAuthServerPacketsDropped,
       "jnxMbgRadiusAuthServerRTTAvg": jnxMbgRadiusAuthServerRTTAvg,
       "jnxMbgRadiusAuthServerRTTMin": jnxMbgRadiusAuthServerRTTMin,
       "jnxMbgRadiusAuthServerRTTMax": jnxMbgRadiusAuthServerRTTMax,
       "jnxMbgRadiusAcctServerTable": jnxMbgRadiusAcctServerTable,
       "jnxMbgRadiusAcctServerEntry": jnxMbgRadiusAcctServerEntry,
       "jnxMbgRadiusAcctServerName": jnxMbgRadiusAcctServerName,
       "jnxMbgRadiusAcctServerInetAddressType": jnxMbgRadiusAcctServerInetAddressType,
       "jnxMbgRadiusAcctServerInetAddress": jnxMbgRadiusAcctServerInetAddress,
       "jnxMbgRadiusAcctServerInetPort": jnxMbgRadiusAcctServerInetPort,
       "jnxMbgRadiusAcctServerRoutingInstance": jnxMbgRadiusAcctServerRoutingInstance,
       "jnxMbgRadiusAcctServerStatus": jnxMbgRadiusAcctServerStatus,
       "jnxMbgRadiusAcctServerRequests": jnxMbgRadiusAcctServerRequests,
       "jnxMbgRadiusAcctServersRetransmissions": jnxMbgRadiusAcctServersRetransmissions,
       "jnxMbgRadiusAcctServerResponses": jnxMbgRadiusAcctServerResponses,
       "jnxMbgRadiusAcctServerMalformedResponses": jnxMbgRadiusAcctServerMalformedResponses,
       "jnxMbgRadiusAcctServerBadAuthenticators": jnxMbgRadiusAcctServerBadAuthenticators,
       "jnxMbgRadiusAcctServerPendingRequests": jnxMbgRadiusAcctServerPendingRequests,
       "jnxMbgRadiusAcctServerTimeouts": jnxMbgRadiusAcctServerTimeouts,
       "jnxMbgRadiusAcctServerUnknownTypes": jnxMbgRadiusAcctServerUnknownTypes,
       "jnxMbgRadiusAcctServerPacketsDropped": jnxMbgRadiusAcctServerPacketsDropped,
       "jnxMbgRadiusAcctServerRTTAvg": jnxMbgRadiusAcctServerRTTAvg,
       "jnxMbgRadiusAcctServerRTTMin": jnxMbgRadiusAcctServerRTTMin,
       "jnxMbgRadiusAcctServerRTTMax": jnxMbgRadiusAcctServerRTTMax,
       "jnxMbgDynAuthClientTable": jnxMbgDynAuthClientTable,
       "jnxMbgDynAuthClientEntry": jnxMbgDynAuthClientEntry,
       "jnxMbgDynAuthClientName": jnxMbgDynAuthClientName,
       "jnxMbgDynAuthClientInAddrType": jnxMbgDynAuthClientInAddrType,
       "jnxMbgDynAuthClientInetAddress": jnxMbgDynAuthClientInetAddress,
       "jnxMbgDynAuthClientCoaReceived": jnxMbgDynAuthClientCoaReceived,
       "jnxMbgDynAuthClientDmReceived": jnxMbgDynAuthClientDmReceived,
       "jnxMbgDynAuthClientCoaAckSent": jnxMbgDynAuthClientCoaAckSent,
       "jnxMbgDynAuthClientCoaNackSent": jnxMbgDynAuthClientCoaNackSent,
       "jnxMbgDynAuthClientDmAckSent": jnxMbgDynAuthClientDmAckSent,
       "jnxMbgDynAuthClientDmNackSent": jnxMbgDynAuthClientDmNackSent,
       "jnxMbgDynAuthClientDropped": jnxMbgDynAuthClientDropped,
       "jnxMbgDynAuthClientDuplicate": jnxMbgDynAuthClientDuplicate,
       "jnxMbgDynAuthClientForwarded": jnxMbgDynAuthClientForwarded,
       "jnxMbgDynAuthClientTimeouts": jnxMbgDynAuthClientTimeouts,
       "jnxMbgDynAuthClientDelivered": jnxMbgDynAuthClientDelivered,
       "jnxMbgDynAuthClientErrors": jnxMbgDynAuthClientErrors,
       "jnxMbgDynAuthClientInvalidAuth": jnxMbgDynAuthClientInvalidAuth,
       "jnxMbgDynAuthClientInvalidCode": jnxMbgDynAuthClientInvalidCode,
       "jnxMbgDynAuthClientInvalidChId": jnxMbgDynAuthClientInvalidChId,
       "jnxMbgDynAuthClientMapErrors": jnxMbgDynAuthClientMapErrors,
       "jnxMbgAAANotificationVars": jnxMbgAAANotificationVars,
       "jnxMbgAAAServerName": jnxMbgAAAServerName,
       "jnxMbgSPIdentifier": jnxMbgSPIdentifier,
       "jnxMbgAAANetworkElementName": jnxMbgAAANetworkElementName,
       "jnxMbgPendQWaterMarkType": jnxMbgPendQWaterMarkType,
       "jnxMbgPendQWaterMarkValue": jnxMbgPendQWaterMarkValue,
       "jnxMbgPendQLength": jnxMbgPendQLength,
       "jnxMbgAAAAuthStatsTable": jnxMbgAAAAuthStatsTable,
       "jnxMbgAAAAuthStatsEntry": jnxMbgAAAAuthStatsEntry,
       "jnxMbgTtlAuthRequests": jnxMbgTtlAuthRequests,
       "jnxMbgTtlAuthAccepts": jnxMbgTtlAuthAccepts,
       "jnxMbgTtlAuthRejects": jnxMbgTtlAuthRejects,
       "jnxMbgTtlAuthChallenges": jnxMbgTtlAuthChallenges,
       "jnxMbgTtlAuthRequestTimeouts": jnxMbgTtlAuthRequestTimeouts,
       "jnxMbgTtlAuthRequestTxErrors": jnxMbgTtlAuthRequestTxErrors,
       "jnxMbgTtlAuthResponseErrors": jnxMbgTtlAuthResponseErrors,
       "jnxMbgTtlAuthPendingRequests": jnxMbgTtlAuthPendingRequests,
       "jnxMbgAAAAcctStatsTable": jnxMbgAAAAcctStatsTable,
       "jnxMbgAAAAcctStatsEntry": jnxMbgAAAAcctStatsEntry,
       "jnxMbgTtlAcctRequests": jnxMbgTtlAcctRequests,
       "jnxMbgTtlAcctResp": jnxMbgTtlAcctResp,
       "jnxMbgTtlAcctRequestTimeouts": jnxMbgTtlAcctRequestTimeouts,
       "jnxMbgTtlAcctRequestTxErrors": jnxMbgTtlAcctRequestTxErrors,
       "jnxMbgTtlAcctResponseErrors": jnxMbgTtlAcctResponseErrors,
       "jnxMbgTtlAcctPendingRequests": jnxMbgTtlAcctPendingRequests,
       "jnxMbgAAADynAuthStatsTable": jnxMbgAAADynAuthStatsTable,
       "jnxMbgAAADynAuthStatsEntry": jnxMbgAAADynAuthStatsEntry,
       "jnxMbgTtlDynAuthReceived": jnxMbgTtlDynAuthReceived,
       "jnxMbgTtlDynAuthCoaReceived": jnxMbgTtlDynAuthCoaReceived,
       "jnxMbgTtlDynAuthDmReceived": jnxMbgTtlDynAuthDmReceived,
       "jnxMbgTtlDynAuthCoaAckSent": jnxMbgTtlDynAuthCoaAckSent,
       "jnxMbgTtlDynAuthCoaNackSent": jnxMbgTtlDynAuthCoaNackSent,
       "jnxMbgTtlDynAuthDmAckSent": jnxMbgTtlDynAuthDmAckSent,
       "jnxMbgTtlDynAuthDmNackSent": jnxMbgTtlDynAuthDmNackSent,
       "jnxMbgTtlDynAuthDropped": jnxMbgTtlDynAuthDropped,
       "jnxMbgTtlDynAuthDuplicate": jnxMbgTtlDynAuthDuplicate,
       "jnxMbgTtlDynAuthForwarded": jnxMbgTtlDynAuthForwarded,
       "jnxMbgTtlDynAuthTimeouts": jnxMbgTtlDynAuthTimeouts,
       "jnxMbgTtlDynAuthDelivered": jnxMbgTtlDynAuthDelivered,
       "jnxMbgTtlDynAuthErrors": jnxMbgTtlDynAuthErrors,
       "jnxMbgTtlDynAuthUnknownClnts": jnxMbgTtlDynAuthUnknownClnts,
       "jnxMbgTtlDynAuthInvalidCode": jnxMbgTtlDynAuthInvalidCode,
       "jnxMbgTtlDynAuthInvalidAuth": jnxMbgTtlDynAuthInvalidAuth,
       "jnxMbgTtlDynAuthInvalidChId": jnxMbgTtlDynAuthInvalidChId,
       "jnxMbgTtlDynAuthMapErrors": jnxMbgTtlDynAuthMapErrors,
       "jnxMbgTtlDynAuthInvalidTrId": jnxMbgTtlDynAuthInvalidTrId,
       "jnxMbgRadiusAuthSrvrTable": jnxMbgRadiusAuthSrvrTable,
       "jnxMbgRadiusAuthSrvrEntry": jnxMbgRadiusAuthSrvrEntry,
       "jnxMbgRadiusAuthSrvrName": jnxMbgRadiusAuthSrvrName,
       "jnxMbgRadiusAuthSrvrInetAddrType": jnxMbgRadiusAuthSrvrInetAddrType,
       "jnxMbgRadiusAuthSrvrInetAddress": jnxMbgRadiusAuthSrvrInetAddress,
       "jnxMbgRadiusAuthSrvrInetPort": jnxMbgRadiusAuthSrvrInetPort,
       "jnxMbgRadiusAuthSrvrRtngInstance": jnxMbgRadiusAuthSrvrRtngInstance,
       "jnxMbgRadiusAuthSrvrStatus": jnxMbgRadiusAuthSrvrStatus,
       "jnxMbgRadiusAuthSrvrRequests": jnxMbgRadiusAuthSrvrRequests,
       "jnxMbgRadiusAuthSrvrRetrans": jnxMbgRadiusAuthSrvrRetrans,
       "jnxMbgRadiusAuthSrvrAccepts": jnxMbgRadiusAuthSrvrAccepts,
       "jnxMbgRadiusAuthSrvrRejects": jnxMbgRadiusAuthSrvrRejects,
       "jnxMbgRadiusAuthSrvrChallenges": jnxMbgRadiusAuthSrvrChallenges,
       "jnxMbgRadiusAuthSrvrMalformResp": jnxMbgRadiusAuthSrvrMalformResp,
       "jnxMbgRadiusAuthSrvrBadAuthen": jnxMbgRadiusAuthSrvrBadAuthen,
       "jnxMbgRadiusAuthSrvrPendingRqsts": jnxMbgRadiusAuthSrvrPendingRqsts,
       "jnxMbgRadiusAuthSrvrTimeouts": jnxMbgRadiusAuthSrvrTimeouts,
       "jnxMbgRadiusAuthSrvrUnknownTypes": jnxMbgRadiusAuthSrvrUnknownTypes,
       "jnxMbgRadiusAuthSrvrPacketsDrop": jnxMbgRadiusAuthSrvrPacketsDrop,
       "jnxMbgRadiusAuthSrvrRTTAvg": jnxMbgRadiusAuthSrvrRTTAvg,
       "jnxMbgRadiusAuthSrvrRTTMin": jnxMbgRadiusAuthSrvrRTTMin,
       "jnxMbgRadiusAuthSrvrRTTMax": jnxMbgRadiusAuthSrvrRTTMax,
       "jnxMbgRadiusAcctSrvrTable": jnxMbgRadiusAcctSrvrTable,
       "jnxMbgRadiusAcctSrvrEntry": jnxMbgRadiusAcctSrvrEntry,
       "jnxMbgRadiusAcctSrvrName": jnxMbgRadiusAcctSrvrName,
       "jnxMbgRadiusAcctSrvrInetAddrType": jnxMbgRadiusAcctSrvrInetAddrType,
       "jnxMbgRadiusAcctSrvrInetAddress": jnxMbgRadiusAcctSrvrInetAddress,
       "jnxMbgRadiusAcctSrvrInetPort": jnxMbgRadiusAcctSrvrInetPort,
       "jnxMbgRadiusAcctSrvrRtngInstance": jnxMbgRadiusAcctSrvrRtngInstance,
       "jnxMbgRadiusAcctSrvrStatus": jnxMbgRadiusAcctSrvrStatus,
       "jnxMbgRadiusAcctSrvrRequests": jnxMbgRadiusAcctSrvrRequests,
       "jnxMbgRadiusAcctSrvrRetrans": jnxMbgRadiusAcctSrvrRetrans,
       "jnxMbgRadiusAcctSrvrResp": jnxMbgRadiusAcctSrvrResp,
       "jnxMbgRadiusAcctSrvrMalformResp": jnxMbgRadiusAcctSrvrMalformResp,
       "jnxMbgRadiusAcctSrvrBadAuthen": jnxMbgRadiusAcctSrvrBadAuthen,
       "jnxMbgRadiusAcctSrvrPendingRqsts": jnxMbgRadiusAcctSrvrPendingRqsts,
       "jnxMbgRadiusAcctSrvrTimeouts": jnxMbgRadiusAcctSrvrTimeouts,
       "jnxMbgRadiusAcctSrvrUnknownTypes": jnxMbgRadiusAcctSrvrUnknownTypes,
       "jnxMbgRadiusAcctSrvrPacketsDrop": jnxMbgRadiusAcctSrvrPacketsDrop,
       "jnxMbgRadiusAcctSrvrRTTAvg": jnxMbgRadiusAcctSrvrRTTAvg,
       "jnxMbgRadiusAcctSrvrRTTMin": jnxMbgRadiusAcctSrvrRTTMin,
       "jnxMbgRadiusAcctSrvrRTTMax": jnxMbgRadiusAcctSrvrRTTMax,
       "jnxMbgDynAuthClntTable": jnxMbgDynAuthClntTable,
       "jnxMbgDynAuthClntEntry": jnxMbgDynAuthClntEntry,
       "jnxMbgDynAuthClntName": jnxMbgDynAuthClntName,
       "jnxMbgDynAuthClntInAddrType": jnxMbgDynAuthClntInAddrType,
       "jnxMbgDynAuthClntInetAddress": jnxMbgDynAuthClntInetAddress,
       "jnxMbgDynAuthClntCoaReceived": jnxMbgDynAuthClntCoaReceived,
       "jnxMbgDynAuthClntDmReceived": jnxMbgDynAuthClntDmReceived,
       "jnxMbgDynAuthClntCoaAckSent": jnxMbgDynAuthClntCoaAckSent,
       "jnxMbgDynAuthClntCoaNackSent": jnxMbgDynAuthClntCoaNackSent,
       "jnxMbgDynAuthClntDmAckSent": jnxMbgDynAuthClntDmAckSent,
       "jnxMbgDynAuthClntDmNackSent": jnxMbgDynAuthClntDmNackSent,
       "jnxMbgDynAuthClntDropped": jnxMbgDynAuthClntDropped,
       "jnxMbgDynAuthClntDuplicate": jnxMbgDynAuthClntDuplicate,
       "jnxMbgDynAuthClntForwarded": jnxMbgDynAuthClntForwarded,
       "jnxMbgDynAuthClntTimeouts": jnxMbgDynAuthClntTimeouts,
       "jnxMbgDynAuthClntDelivered": jnxMbgDynAuthClntDelivered,
       "jnxMbgDynAuthClntErrors": jnxMbgDynAuthClntErrors,
       "jnxMbgDynAuthClntInvalidAuth": jnxMbgDynAuthClntInvalidAuth,
       "jnxMbgDynAuthClntInvalidCode": jnxMbgDynAuthClntInvalidCode,
       "jnxMbgDynAuthClntInvalidChId": jnxMbgDynAuthClntInvalidChId,
       "jnxMbgDynAuthClntMapErrors": jnxMbgDynAuthClntMapErrors}
)
