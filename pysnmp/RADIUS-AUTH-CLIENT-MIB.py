# SNMP MIB module (RADIUS-AUTH-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:57 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

radiusAuthClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2)
)
radiusAuthClientMIB.setRevisions(
        ("2006-08-21 00:00",
         "1999-06-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusMIB_ObjectIdentity = ObjectIdentity
radiusMIB = _RadiusMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67)
)
if mibBuilder.loadTexts:
    radiusMIB.setStatus("current")
_RadiusAuthentication_ObjectIdentity = ObjectIdentity
radiusAuthentication = _RadiusAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1)
)
_RadiusAuthClientMIBObjects_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBObjects = _RadiusAuthClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1)
)
_RadiusAuthClient_ObjectIdentity = ObjectIdentity
radiusAuthClient = _RadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1)
)
_RadiusAuthClientInvalidServerAddresses_Type = Counter32
_RadiusAuthClientInvalidServerAddresses_Object = MibScalar
radiusAuthClientInvalidServerAddresses = _RadiusAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 1),
    _RadiusAuthClientInvalidServerAddresses_Type()
)
radiusAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientInvalidServerAddresses.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientInvalidServerAddresses.setUnits("packets")
_RadiusAuthClientIdentifier_Type = SnmpAdminString
_RadiusAuthClientIdentifier_Object = MibScalar
radiusAuthClientIdentifier = _RadiusAuthClientIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 2),
    _RadiusAuthClientIdentifier_Type()
)
radiusAuthClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientIdentifier.setStatus("current")
_RadiusAuthServerTable_Object = MibTable
radiusAuthServerTable = _RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAuthServerTable.setStatus("deprecated")
_RadiusAuthServerEntry_Object = MibTableRow
radiusAuthServerEntry = _RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1)
)
radiusAuthServerEntry.setIndexNames(
    (0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthServerEntry.setStatus("deprecated")


class _RadiusAuthServerIndex_Type(Integer32):
    """Custom type radiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAuthServerIndex_Type.__name__ = "Integer32"
_RadiusAuthServerIndex_Object = MibTableColumn
radiusAuthServerIndex = _RadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 1),
    _RadiusAuthServerIndex_Type()
)
radiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthServerIndex.setStatus("deprecated")
_RadiusAuthServerAddress_Type = IpAddress
_RadiusAuthServerAddress_Object = MibTableColumn
radiusAuthServerAddress = _RadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 2),
    _RadiusAuthServerAddress_Type()
)
radiusAuthServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServerAddress.setStatus("deprecated")


class _RadiusAuthClientServerPortNumber_Type(Integer32):
    """Custom type radiusAuthClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAuthClientServerPortNumber_Type.__name__ = "Integer32"
_RadiusAuthClientServerPortNumber_Object = MibTableColumn
radiusAuthClientServerPortNumber = _RadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 3),
    _RadiusAuthClientServerPortNumber_Type()
)
radiusAuthClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientServerPortNumber.setStatus("deprecated")
_RadiusAuthClientRoundTripTime_Type = TimeTicks
_RadiusAuthClientRoundTripTime_Object = MibTableColumn
radiusAuthClientRoundTripTime = _RadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 4),
    _RadiusAuthClientRoundTripTime_Type()
)
radiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientRoundTripTime.setStatus("deprecated")
_RadiusAuthClientAccessRequests_Type = Counter32
_RadiusAuthClientAccessRequests_Object = MibTableColumn
radiusAuthClientAccessRequests = _RadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 5),
    _RadiusAuthClientAccessRequests_Type()
)
radiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRequests.setUnits("packets")
_RadiusAuthClientAccessRetransmissions_Type = Counter32
_RadiusAuthClientAccessRetransmissions_Object = MibTableColumn
radiusAuthClientAccessRetransmissions = _RadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 6),
    _RadiusAuthClientAccessRetransmissions_Type()
)
radiusAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRetransmissions.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRetransmissions.setUnits("packets")
_RadiusAuthClientAccessAccepts_Type = Counter32
_RadiusAuthClientAccessAccepts_Object = MibTableColumn
radiusAuthClientAccessAccepts = _RadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 7),
    _RadiusAuthClientAccessAccepts_Type()
)
radiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessAccepts.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientAccessAccepts.setUnits("packets")
_RadiusAuthClientAccessRejects_Type = Counter32
_RadiusAuthClientAccessRejects_Object = MibTableColumn
radiusAuthClientAccessRejects = _RadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 8),
    _RadiusAuthClientAccessRejects_Type()
)
radiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRejects.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRejects.setUnits("packets")
_RadiusAuthClientAccessChallenges_Type = Counter32
_RadiusAuthClientAccessChallenges_Object = MibTableColumn
radiusAuthClientAccessChallenges = _RadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 9),
    _RadiusAuthClientAccessChallenges_Type()
)
radiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessChallenges.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientAccessChallenges.setUnits("packets")
_RadiusAuthClientMalformedAccessResponses_Type = Counter32
_RadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
radiusAuthClientMalformedAccessResponses = _RadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 10),
    _RadiusAuthClientMalformedAccessResponses_Type()
)
radiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientMalformedAccessResponses.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientMalformedAccessResponses.setUnits("packets")
_RadiusAuthClientBadAuthenticators_Type = Counter32
_RadiusAuthClientBadAuthenticators_Object = MibTableColumn
radiusAuthClientBadAuthenticators = _RadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 11),
    _RadiusAuthClientBadAuthenticators_Type()
)
radiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientBadAuthenticators.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientBadAuthenticators.setUnits("packets")
_RadiusAuthClientPendingRequests_Type = Gauge32
_RadiusAuthClientPendingRequests_Object = MibTableColumn
radiusAuthClientPendingRequests = _RadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 12),
    _RadiusAuthClientPendingRequests_Type()
)
radiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientPendingRequests.setStatus("deprecated")
_RadiusAuthClientTimeouts_Type = Counter32
_RadiusAuthClientTimeouts_Object = MibTableColumn
radiusAuthClientTimeouts = _RadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 13),
    _RadiusAuthClientTimeouts_Type()
)
radiusAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientTimeouts.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientTimeouts.setUnits("timeouts")
_RadiusAuthClientUnknownTypes_Type = Counter32
_RadiusAuthClientUnknownTypes_Object = MibTableColumn
radiusAuthClientUnknownTypes = _RadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 14),
    _RadiusAuthClientUnknownTypes_Type()
)
radiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientUnknownTypes.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientUnknownTypes.setUnits("packets")
_RadiusAuthClientPacketsDropped_Type = Counter32
_RadiusAuthClientPacketsDropped_Object = MibTableColumn
radiusAuthClientPacketsDropped = _RadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 15),
    _RadiusAuthClientPacketsDropped_Type()
)
radiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientPacketsDropped.setStatus("deprecated")
if mibBuilder.loadTexts:
    radiusAuthClientPacketsDropped.setUnits("packets")
_RadiusAuthServerExtTable_Object = MibTable
radiusAuthServerExtTable = _RadiusAuthServerExtTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    radiusAuthServerExtTable.setStatus("current")
_RadiusAuthServerExtEntry_Object = MibTableRow
radiusAuthServerExtEntry = _RadiusAuthServerExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1)
)
radiusAuthServerExtEntry.setIndexNames(
    (0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerExtIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthServerExtEntry.setStatus("current")


class _RadiusAuthServerExtIndex_Type(Integer32):
    """Custom type radiusAuthServerExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAuthServerExtIndex_Type.__name__ = "Integer32"
_RadiusAuthServerExtIndex_Object = MibTableColumn
radiusAuthServerExtIndex = _RadiusAuthServerExtIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 1),
    _RadiusAuthServerExtIndex_Type()
)
radiusAuthServerExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthServerExtIndex.setStatus("current")
_RadiusAuthServerInetAddressType_Type = InetAddressType
_RadiusAuthServerInetAddressType_Object = MibTableColumn
radiusAuthServerInetAddressType = _RadiusAuthServerInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 2),
    _RadiusAuthServerInetAddressType_Type()
)
radiusAuthServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServerInetAddressType.setStatus("current")
_RadiusAuthServerInetAddress_Type = InetAddress
_RadiusAuthServerInetAddress_Object = MibTableColumn
radiusAuthServerInetAddress = _RadiusAuthServerInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 3),
    _RadiusAuthServerInetAddress_Type()
)
radiusAuthServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServerInetAddress.setStatus("current")


class _RadiusAuthClientServerInetPortNumber_Type(InetPortNumber):
    """Custom type radiusAuthClientServerInetPortNumber based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusAuthClientServerInetPortNumber_Type.__name__ = "InetPortNumber"
_RadiusAuthClientServerInetPortNumber_Object = MibTableColumn
radiusAuthClientServerInetPortNumber = _RadiusAuthClientServerInetPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 4),
    _RadiusAuthClientServerInetPortNumber_Type()
)
radiusAuthClientServerInetPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientServerInetPortNumber.setStatus("current")
_RadiusAuthClientExtRoundTripTime_Type = TimeTicks
_RadiusAuthClientExtRoundTripTime_Object = MibTableColumn
radiusAuthClientExtRoundTripTime = _RadiusAuthClientExtRoundTripTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 5),
    _RadiusAuthClientExtRoundTripTime_Type()
)
radiusAuthClientExtRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtRoundTripTime.setStatus("current")
_RadiusAuthClientExtAccessRequests_Type = Counter32
_RadiusAuthClientExtAccessRequests_Object = MibTableColumn
radiusAuthClientExtAccessRequests = _RadiusAuthClientExtAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 6),
    _RadiusAuthClientExtAccessRequests_Type()
)
radiusAuthClientExtAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessRequests.setUnits("packets")
_RadiusAuthClientExtAccessRetransmissions_Type = Counter32
_RadiusAuthClientExtAccessRetransmissions_Object = MibTableColumn
radiusAuthClientExtAccessRetransmissions = _RadiusAuthClientExtAccessRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 7),
    _RadiusAuthClientExtAccessRetransmissions_Type()
)
radiusAuthClientExtAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessRetransmissions.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessRetransmissions.setUnits("packets")
_RadiusAuthClientExtAccessAccepts_Type = Counter32
_RadiusAuthClientExtAccessAccepts_Object = MibTableColumn
radiusAuthClientExtAccessAccepts = _RadiusAuthClientExtAccessAccepts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 8),
    _RadiusAuthClientExtAccessAccepts_Type()
)
radiusAuthClientExtAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessAccepts.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessAccepts.setUnits("packets")
_RadiusAuthClientExtAccessRejects_Type = Counter32
_RadiusAuthClientExtAccessRejects_Object = MibTableColumn
radiusAuthClientExtAccessRejects = _RadiusAuthClientExtAccessRejects_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 9),
    _RadiusAuthClientExtAccessRejects_Type()
)
radiusAuthClientExtAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessRejects.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessRejects.setUnits("packets")
_RadiusAuthClientExtAccessChallenges_Type = Counter32
_RadiusAuthClientExtAccessChallenges_Object = MibTableColumn
radiusAuthClientExtAccessChallenges = _RadiusAuthClientExtAccessChallenges_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 10),
    _RadiusAuthClientExtAccessChallenges_Type()
)
radiusAuthClientExtAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessChallenges.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtAccessChallenges.setUnits("packets")
_RadiusAuthClientExtMalformedAccessResponses_Type = Counter32
_RadiusAuthClientExtMalformedAccessResponses_Object = MibTableColumn
radiusAuthClientExtMalformedAccessResponses = _RadiusAuthClientExtMalformedAccessResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 11),
    _RadiusAuthClientExtMalformedAccessResponses_Type()
)
radiusAuthClientExtMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtMalformedAccessResponses.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtMalformedAccessResponses.setUnits("packets")
_RadiusAuthClientExtBadAuthenticators_Type = Counter32
_RadiusAuthClientExtBadAuthenticators_Object = MibTableColumn
radiusAuthClientExtBadAuthenticators = _RadiusAuthClientExtBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 12),
    _RadiusAuthClientExtBadAuthenticators_Type()
)
radiusAuthClientExtBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtBadAuthenticators.setUnits("packets")
_RadiusAuthClientExtPendingRequests_Type = Gauge32
_RadiusAuthClientExtPendingRequests_Object = MibTableColumn
radiusAuthClientExtPendingRequests = _RadiusAuthClientExtPendingRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 13),
    _RadiusAuthClientExtPendingRequests_Type()
)
radiusAuthClientExtPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtPendingRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtPendingRequests.setUnits("packets")
_RadiusAuthClientExtTimeouts_Type = Counter32
_RadiusAuthClientExtTimeouts_Object = MibTableColumn
radiusAuthClientExtTimeouts = _RadiusAuthClientExtTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 14),
    _RadiusAuthClientExtTimeouts_Type()
)
radiusAuthClientExtTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtTimeouts.setUnits("timeouts")
_RadiusAuthClientExtUnknownTypes_Type = Counter32
_RadiusAuthClientExtUnknownTypes_Object = MibTableColumn
radiusAuthClientExtUnknownTypes = _RadiusAuthClientExtUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 15),
    _RadiusAuthClientExtUnknownTypes_Type()
)
radiusAuthClientExtUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtUnknownTypes.setUnits("packets")
_RadiusAuthClientExtPacketsDropped_Type = Counter32
_RadiusAuthClientExtPacketsDropped_Object = MibTableColumn
radiusAuthClientExtPacketsDropped = _RadiusAuthClientExtPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 16),
    _RadiusAuthClientExtPacketsDropped_Type()
)
radiusAuthClientExtPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientExtPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientExtPacketsDropped.setUnits("packets")
_RadiusAuthClientCounterDiscontinuity_Type = TimeTicks
_RadiusAuthClientCounterDiscontinuity_Object = MibTableColumn
radiusAuthClientCounterDiscontinuity = _RadiusAuthClientCounterDiscontinuity_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 17),
    _RadiusAuthClientCounterDiscontinuity_Type()
)
radiusAuthClientCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientCounterDiscontinuity.setStatus("current")
if mibBuilder.loadTexts:
    radiusAuthClientCounterDiscontinuity.setUnits("centiseconds")
_RadiusAuthClientMIBConformance_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBConformance = _RadiusAuthClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2)
)
_RadiusAuthClientMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBCompliances = _RadiusAuthClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1)
)
_RadiusAuthClientMIBGroups_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBGroups = _RadiusAuthClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2)
)

# Managed Objects groups

radiusAuthClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 1)
)
radiusAuthClientMIBGroup.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientRoundTripTime"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRequests"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRetransmissions"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessAccepts"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRejects"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessChallenges"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMalformedAccessResponses"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientBadAuthenticators"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPendingRequests"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientTimeouts"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientUnknownTypes"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPacketsDropped"))
)
if mibBuilder.loadTexts:
    radiusAuthClientMIBGroup.setStatus("deprecated")

radiusAuthClientExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 2)
)
radiusAuthClientExtMIBGroup.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerInetAddressType"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerInetAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerInetPortNumber"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtRoundTripTime"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRequests"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRetransmissions"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessAccepts"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRejects"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessChallenges"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtMalformedAccessResponses"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtBadAuthenticators"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtPendingRequests"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtTimeouts"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtUnknownTypes"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtPacketsDropped"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientCounterDiscontinuity"))
)
if mibBuilder.loadTexts:
    radiusAuthClientExtMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAuthClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    radiusAuthClientMIBCompliance.setStatus(
        "deprecated"
    )

radiusAuthClientExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    radiusAuthClientExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    **{"radiusMIB": radiusMIB,
       "radiusAuthentication": radiusAuthentication,
       "radiusAuthClientMIB": radiusAuthClientMIB,
       "radiusAuthClientMIBObjects": radiusAuthClientMIBObjects,
       "radiusAuthClient": radiusAuthClient,
       "radiusAuthClientInvalidServerAddresses": radiusAuthClientInvalidServerAddresses,
       "radiusAuthClientIdentifier": radiusAuthClientIdentifier,
       "radiusAuthServerTable": radiusAuthServerTable,
       "radiusAuthServerEntry": radiusAuthServerEntry,
       "radiusAuthServerIndex": radiusAuthServerIndex,
       "radiusAuthServerAddress": radiusAuthServerAddress,
       "radiusAuthClientServerPortNumber": radiusAuthClientServerPortNumber,
       "radiusAuthClientRoundTripTime": radiusAuthClientRoundTripTime,
       "radiusAuthClientAccessRequests": radiusAuthClientAccessRequests,
       "radiusAuthClientAccessRetransmissions": radiusAuthClientAccessRetransmissions,
       "radiusAuthClientAccessAccepts": radiusAuthClientAccessAccepts,
       "radiusAuthClientAccessRejects": radiusAuthClientAccessRejects,
       "radiusAuthClientAccessChallenges": radiusAuthClientAccessChallenges,
       "radiusAuthClientMalformedAccessResponses": radiusAuthClientMalformedAccessResponses,
       "radiusAuthClientBadAuthenticators": radiusAuthClientBadAuthenticators,
       "radiusAuthClientPendingRequests": radiusAuthClientPendingRequests,
       "radiusAuthClientTimeouts": radiusAuthClientTimeouts,
       "radiusAuthClientUnknownTypes": radiusAuthClientUnknownTypes,
       "radiusAuthClientPacketsDropped": radiusAuthClientPacketsDropped,
       "radiusAuthServerExtTable": radiusAuthServerExtTable,
       "radiusAuthServerExtEntry": radiusAuthServerExtEntry,
       "radiusAuthServerExtIndex": radiusAuthServerExtIndex,
       "radiusAuthServerInetAddressType": radiusAuthServerInetAddressType,
       "radiusAuthServerInetAddress": radiusAuthServerInetAddress,
       "radiusAuthClientServerInetPortNumber": radiusAuthClientServerInetPortNumber,
       "radiusAuthClientExtRoundTripTime": radiusAuthClientExtRoundTripTime,
       "radiusAuthClientExtAccessRequests": radiusAuthClientExtAccessRequests,
       "radiusAuthClientExtAccessRetransmissions": radiusAuthClientExtAccessRetransmissions,
       "radiusAuthClientExtAccessAccepts": radiusAuthClientExtAccessAccepts,
       "radiusAuthClientExtAccessRejects": radiusAuthClientExtAccessRejects,
       "radiusAuthClientExtAccessChallenges": radiusAuthClientExtAccessChallenges,
       "radiusAuthClientExtMalformedAccessResponses": radiusAuthClientExtMalformedAccessResponses,
       "radiusAuthClientExtBadAuthenticators": radiusAuthClientExtBadAuthenticators,
       "radiusAuthClientExtPendingRequests": radiusAuthClientExtPendingRequests,
       "radiusAuthClientExtTimeouts": radiusAuthClientExtTimeouts,
       "radiusAuthClientExtUnknownTypes": radiusAuthClientExtUnknownTypes,
       "radiusAuthClientExtPacketsDropped": radiusAuthClientExtPacketsDropped,
       "radiusAuthClientCounterDiscontinuity": radiusAuthClientCounterDiscontinuity,
       "radiusAuthClientMIBConformance": radiusAuthClientMIBConformance,
       "radiusAuthClientMIBCompliances": radiusAuthClientMIBCompliances,
       "radiusAuthClientMIBCompliance": radiusAuthClientMIBCompliance,
       "radiusAuthClientExtMIBCompliance": radiusAuthClientExtMIBCompliance,
       "radiusAuthClientMIBGroups": radiusAuthClientMIBGroups,
       "radiusAuthClientMIBGroup": radiusAuthClientMIBGroup,
       "radiusAuthClientExtMIBGroup": radiusAuthClientExtMIBGroup}
)
