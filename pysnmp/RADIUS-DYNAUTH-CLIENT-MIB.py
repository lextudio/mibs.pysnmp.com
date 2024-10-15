# SNMP MIB module (RADIUS-DYNAUTH-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADIUS-DYNAUTH-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:30 2024
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

radiusDynAuthClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 145)
)
radiusDynAuthClientMIB.setRevisions(
        ("2006-09-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusDynAuthClientMIBObjects_ObjectIdentity = ObjectIdentity
radiusDynAuthClientMIBObjects = _RadiusDynAuthClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 145, 1)
)
_RadiusDynAuthClientScalars_ObjectIdentity = ObjectIdentity
radiusDynAuthClientScalars = _RadiusDynAuthClientScalars_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 145, 1, 1)
)
_RadiusDynAuthClientDisconInvalidServerAddresses_Type = Counter32
_RadiusDynAuthClientDisconInvalidServerAddresses_Object = MibScalar
radiusDynAuthClientDisconInvalidServerAddresses = _RadiusDynAuthClientDisconInvalidServerAddresses_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 1, 1),
    _RadiusDynAuthClientDisconInvalidServerAddresses_Type()
)
radiusDynAuthClientDisconInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconInvalidServerAddresses.setStatus("current")
_RadiusDynAuthClientCoAInvalidServerAddresses_Type = Counter32
_RadiusDynAuthClientCoAInvalidServerAddresses_Object = MibScalar
radiusDynAuthClientCoAInvalidServerAddresses = _RadiusDynAuthClientCoAInvalidServerAddresses_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 1, 2),
    _RadiusDynAuthClientCoAInvalidServerAddresses_Type()
)
radiusDynAuthClientCoAInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAInvalidServerAddresses.setStatus("current")
_RadiusDynAuthServerTable_Object = MibTable
radiusDynAuthServerTable = _RadiusDynAuthServerTable_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2)
)
if mibBuilder.loadTexts:
    radiusDynAuthServerTable.setStatus("current")
_RadiusDynAuthServerEntry_Object = MibTableRow
radiusDynAuthServerEntry = _RadiusDynAuthServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1)
)
radiusDynAuthServerEntry.setIndexNames(
    (0, "RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusDynAuthServerEntry.setStatus("current")


class _RadiusDynAuthServerIndex_Type(Integer32):
    """Custom type radiusDynAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusDynAuthServerIndex_Type.__name__ = "Integer32"
_RadiusDynAuthServerIndex_Object = MibTableColumn
radiusDynAuthServerIndex = _RadiusDynAuthServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 1),
    _RadiusDynAuthServerIndex_Type()
)
radiusDynAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusDynAuthServerIndex.setStatus("current")
_RadiusDynAuthServerAddressType_Type = InetAddressType
_RadiusDynAuthServerAddressType_Object = MibTableColumn
radiusDynAuthServerAddressType = _RadiusDynAuthServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 2),
    _RadiusDynAuthServerAddressType_Type()
)
radiusDynAuthServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServerAddressType.setStatus("current")
_RadiusDynAuthServerAddress_Type = InetAddress
_RadiusDynAuthServerAddress_Object = MibTableColumn
radiusDynAuthServerAddress = _RadiusDynAuthServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 3),
    _RadiusDynAuthServerAddress_Type()
)
radiusDynAuthServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServerAddress.setStatus("current")


class _RadiusDynAuthServerClientPortNumber_Type(InetPortNumber):
    """Custom type radiusDynAuthServerClientPortNumber based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusDynAuthServerClientPortNumber_Type.__name__ = "InetPortNumber"
_RadiusDynAuthServerClientPortNumber_Object = MibTableColumn
radiusDynAuthServerClientPortNumber = _RadiusDynAuthServerClientPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 4),
    _RadiusDynAuthServerClientPortNumber_Type()
)
radiusDynAuthServerClientPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServerClientPortNumber.setStatus("current")
_RadiusDynAuthServerID_Type = SnmpAdminString
_RadiusDynAuthServerID_Object = MibTableColumn
radiusDynAuthServerID = _RadiusDynAuthServerID_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 5),
    _RadiusDynAuthServerID_Type()
)
radiusDynAuthServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServerID.setStatus("current")
_RadiusDynAuthClientRoundTripTime_Type = TimeTicks
_RadiusDynAuthClientRoundTripTime_Object = MibTableColumn
radiusDynAuthClientRoundTripTime = _RadiusDynAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 6),
    _RadiusDynAuthClientRoundTripTime_Type()
)
radiusDynAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientRoundTripTime.setUnits("hundredths of a second")
_RadiusDynAuthClientDisconRequests_Type = Counter32
_RadiusDynAuthClientDisconRequests_Object = MibTableColumn
radiusDynAuthClientDisconRequests = _RadiusDynAuthClientDisconRequests_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 7),
    _RadiusDynAuthClientDisconRequests_Type()
)
radiusDynAuthClientDisconRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconRequests.setUnits("requests")
_RadiusDynAuthClientDisconAuthOnlyRequests_Type = Counter32
_RadiusDynAuthClientDisconAuthOnlyRequests_Object = MibTableColumn
radiusDynAuthClientDisconAuthOnlyRequests = _RadiusDynAuthClientDisconAuthOnlyRequests_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 8),
    _RadiusDynAuthClientDisconAuthOnlyRequests_Type()
)
radiusDynAuthClientDisconAuthOnlyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconAuthOnlyRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconAuthOnlyRequests.setUnits("requests")
_RadiusDynAuthClientDisconRetransmissions_Type = Counter32
_RadiusDynAuthClientDisconRetransmissions_Object = MibTableColumn
radiusDynAuthClientDisconRetransmissions = _RadiusDynAuthClientDisconRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 9),
    _RadiusDynAuthClientDisconRetransmissions_Type()
)
radiusDynAuthClientDisconRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconRetransmissions.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconRetransmissions.setUnits("retransmissions")
_RadiusDynAuthClientDisconAcks_Type = Counter32
_RadiusDynAuthClientDisconAcks_Object = MibTableColumn
radiusDynAuthClientDisconAcks = _RadiusDynAuthClientDisconAcks_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 10),
    _RadiusDynAuthClientDisconAcks_Type()
)
radiusDynAuthClientDisconAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconAcks.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconAcks.setUnits("replies")
_RadiusDynAuthClientDisconNaks_Type = Counter32
_RadiusDynAuthClientDisconNaks_Object = MibTableColumn
radiusDynAuthClientDisconNaks = _RadiusDynAuthClientDisconNaks_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 11),
    _RadiusDynAuthClientDisconNaks_Type()
)
radiusDynAuthClientDisconNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconNaks.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconNaks.setUnits("replies")
_RadiusDynAuthClientDisconNakAuthOnlyRequest_Type = Counter32
_RadiusDynAuthClientDisconNakAuthOnlyRequest_Object = MibTableColumn
radiusDynAuthClientDisconNakAuthOnlyRequest = _RadiusDynAuthClientDisconNakAuthOnlyRequest_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 12),
    _RadiusDynAuthClientDisconNakAuthOnlyRequest_Type()
)
radiusDynAuthClientDisconNakAuthOnlyRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconNakAuthOnlyRequest.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconNakAuthOnlyRequest.setUnits("replies")
_RadiusDynAuthClientDisconNakSessNoContext_Type = Counter32
_RadiusDynAuthClientDisconNakSessNoContext_Object = MibTableColumn
radiusDynAuthClientDisconNakSessNoContext = _RadiusDynAuthClientDisconNakSessNoContext_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 13),
    _RadiusDynAuthClientDisconNakSessNoContext_Type()
)
radiusDynAuthClientDisconNakSessNoContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconNakSessNoContext.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconNakSessNoContext.setUnits("replies")
_RadiusDynAuthClientMalformedDisconResponses_Type = Counter32
_RadiusDynAuthClientMalformedDisconResponses_Object = MibTableColumn
radiusDynAuthClientMalformedDisconResponses = _RadiusDynAuthClientMalformedDisconResponses_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 14),
    _RadiusDynAuthClientMalformedDisconResponses_Type()
)
radiusDynAuthClientMalformedDisconResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientMalformedDisconResponses.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientMalformedDisconResponses.setUnits("replies")
_RadiusDynAuthClientDisconBadAuthenticators_Type = Counter32
_RadiusDynAuthClientDisconBadAuthenticators_Object = MibTableColumn
radiusDynAuthClientDisconBadAuthenticators = _RadiusDynAuthClientDisconBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 15),
    _RadiusDynAuthClientDisconBadAuthenticators_Type()
)
radiusDynAuthClientDisconBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconBadAuthenticators.setUnits("replies")
_RadiusDynAuthClientDisconPendingRequests_Type = Gauge32
_RadiusDynAuthClientDisconPendingRequests_Object = MibTableColumn
radiusDynAuthClientDisconPendingRequests = _RadiusDynAuthClientDisconPendingRequests_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 16),
    _RadiusDynAuthClientDisconPendingRequests_Type()
)
radiusDynAuthClientDisconPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconPendingRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconPendingRequests.setUnits("requests")
_RadiusDynAuthClientDisconTimeouts_Type = Counter32
_RadiusDynAuthClientDisconTimeouts_Object = MibTableColumn
radiusDynAuthClientDisconTimeouts = _RadiusDynAuthClientDisconTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 17),
    _RadiusDynAuthClientDisconTimeouts_Type()
)
radiusDynAuthClientDisconTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconTimeouts.setUnits("timeouts")
_RadiusDynAuthClientDisconPacketsDropped_Type = Counter32
_RadiusDynAuthClientDisconPacketsDropped_Object = MibTableColumn
radiusDynAuthClientDisconPacketsDropped = _RadiusDynAuthClientDisconPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 18),
    _RadiusDynAuthClientDisconPacketsDropped_Type()
)
radiusDynAuthClientDisconPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientDisconPacketsDropped.setUnits("replies")
_RadiusDynAuthClientCoARequests_Type = Counter32
_RadiusDynAuthClientCoARequests_Object = MibTableColumn
radiusDynAuthClientCoARequests = _RadiusDynAuthClientCoARequests_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 19),
    _RadiusDynAuthClientCoARequests_Type()
)
radiusDynAuthClientCoARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoARequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoARequests.setUnits("requests")
_RadiusDynAuthClientCoAAuthOnlyRequest_Type = Counter32
_RadiusDynAuthClientCoAAuthOnlyRequest_Object = MibTableColumn
radiusDynAuthClientCoAAuthOnlyRequest = _RadiusDynAuthClientCoAAuthOnlyRequest_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 20),
    _RadiusDynAuthClientCoAAuthOnlyRequest_Type()
)
radiusDynAuthClientCoAAuthOnlyRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAAuthOnlyRequest.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAAuthOnlyRequest.setUnits("requests")
_RadiusDynAuthClientCoARetransmissions_Type = Counter32
_RadiusDynAuthClientCoARetransmissions_Object = MibTableColumn
radiusDynAuthClientCoARetransmissions = _RadiusDynAuthClientCoARetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 21),
    _RadiusDynAuthClientCoARetransmissions_Type()
)
radiusDynAuthClientCoARetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoARetransmissions.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoARetransmissions.setUnits("retransmissions")
_RadiusDynAuthClientCoAAcks_Type = Counter32
_RadiusDynAuthClientCoAAcks_Object = MibTableColumn
radiusDynAuthClientCoAAcks = _RadiusDynAuthClientCoAAcks_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 22),
    _RadiusDynAuthClientCoAAcks_Type()
)
radiusDynAuthClientCoAAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAAcks.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAAcks.setUnits("replies")
_RadiusDynAuthClientCoANaks_Type = Counter32
_RadiusDynAuthClientCoANaks_Object = MibTableColumn
radiusDynAuthClientCoANaks = _RadiusDynAuthClientCoANaks_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 23),
    _RadiusDynAuthClientCoANaks_Type()
)
radiusDynAuthClientCoANaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoANaks.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoANaks.setUnits("replies")
_RadiusDynAuthClientCoANakAuthOnlyRequest_Type = Counter32
_RadiusDynAuthClientCoANakAuthOnlyRequest_Object = MibTableColumn
radiusDynAuthClientCoANakAuthOnlyRequest = _RadiusDynAuthClientCoANakAuthOnlyRequest_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 24),
    _RadiusDynAuthClientCoANakAuthOnlyRequest_Type()
)
radiusDynAuthClientCoANakAuthOnlyRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoANakAuthOnlyRequest.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoANakAuthOnlyRequest.setUnits("replies")
_RadiusDynAuthClientCoANakSessNoContext_Type = Counter32
_RadiusDynAuthClientCoANakSessNoContext_Object = MibTableColumn
radiusDynAuthClientCoANakSessNoContext = _RadiusDynAuthClientCoANakSessNoContext_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 25),
    _RadiusDynAuthClientCoANakSessNoContext_Type()
)
radiusDynAuthClientCoANakSessNoContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoANakSessNoContext.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoANakSessNoContext.setUnits("replies")
_RadiusDynAuthClientMalformedCoAResponses_Type = Counter32
_RadiusDynAuthClientMalformedCoAResponses_Object = MibTableColumn
radiusDynAuthClientMalformedCoAResponses = _RadiusDynAuthClientMalformedCoAResponses_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 26),
    _RadiusDynAuthClientMalformedCoAResponses_Type()
)
radiusDynAuthClientMalformedCoAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientMalformedCoAResponses.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientMalformedCoAResponses.setUnits("replies")
_RadiusDynAuthClientCoABadAuthenticators_Type = Counter32
_RadiusDynAuthClientCoABadAuthenticators_Object = MibTableColumn
radiusDynAuthClientCoABadAuthenticators = _RadiusDynAuthClientCoABadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 27),
    _RadiusDynAuthClientCoABadAuthenticators_Type()
)
radiusDynAuthClientCoABadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoABadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoABadAuthenticators.setUnits("replies")
_RadiusDynAuthClientCoAPendingRequests_Type = Gauge32
_RadiusDynAuthClientCoAPendingRequests_Object = MibTableColumn
radiusDynAuthClientCoAPendingRequests = _RadiusDynAuthClientCoAPendingRequests_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 28),
    _RadiusDynAuthClientCoAPendingRequests_Type()
)
radiusDynAuthClientCoAPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAPendingRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAPendingRequests.setUnits("requests")
_RadiusDynAuthClientCoATimeouts_Type = Counter32
_RadiusDynAuthClientCoATimeouts_Object = MibTableColumn
radiusDynAuthClientCoATimeouts = _RadiusDynAuthClientCoATimeouts_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 29),
    _RadiusDynAuthClientCoATimeouts_Type()
)
radiusDynAuthClientCoATimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoATimeouts.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoATimeouts.setUnits("timeouts")
_RadiusDynAuthClientCoAPacketsDropped_Type = Counter32
_RadiusDynAuthClientCoAPacketsDropped_Object = MibTableColumn
radiusDynAuthClientCoAPacketsDropped = _RadiusDynAuthClientCoAPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 30),
    _RadiusDynAuthClientCoAPacketsDropped_Type()
)
radiusDynAuthClientCoAPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCoAPacketsDropped.setUnits("replies")
_RadiusDynAuthClientUnknownTypes_Type = Counter32
_RadiusDynAuthClientUnknownTypes_Object = MibTableColumn
radiusDynAuthClientUnknownTypes = _RadiusDynAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 31),
    _RadiusDynAuthClientUnknownTypes_Type()
)
radiusDynAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientUnknownTypes.setUnits("replies")
_RadiusDynAuthClientCounterDiscontinuity_Type = TimeTicks
_RadiusDynAuthClientCounterDiscontinuity_Object = MibTableColumn
radiusDynAuthClientCounterDiscontinuity = _RadiusDynAuthClientCounterDiscontinuity_Object(
    (1, 3, 6, 1, 2, 1, 145, 1, 2, 1, 32),
    _RadiusDynAuthClientCounterDiscontinuity_Type()
)
radiusDynAuthClientCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientCounterDiscontinuity.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthClientCounterDiscontinuity.setUnits("hundredths of a second")
_RadiusDynAuthClientMIBConformance_ObjectIdentity = ObjectIdentity
radiusDynAuthClientMIBConformance = _RadiusDynAuthClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 145, 2)
)
_RadiusDynAuthClientMIBCompliances_ObjectIdentity = ObjectIdentity
radiusDynAuthClientMIBCompliances = _RadiusDynAuthClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 145, 2, 1)
)
_RadiusDynAuthClientMIBGroups_ObjectIdentity = ObjectIdentity
radiusDynAuthClientMIBGroups = _RadiusDynAuthClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 145, 2, 2)
)

# Managed Objects groups

radiusDynAuthClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 145, 2, 2, 1)
)
radiusDynAuthClientMIBGroup.setObjects(
      *(("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconInvalidServerAddresses"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoAInvalidServerAddresses"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthServerAddressType"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthServerAddress"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthServerClientPortNumber"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthServerID"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientRoundTripTime"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconRequests"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconRetransmissions"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconAcks"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconNaks"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientMalformedDisconResponses"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconBadAuthenticators"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconPendingRequests"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconTimeouts"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconPacketsDropped"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoARequests"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoARetransmissions"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoAAcks"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoANaks"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientMalformedCoAResponses"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoABadAuthenticators"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoAPendingRequests"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoATimeouts"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoAPacketsDropped"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientUnknownTypes"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCounterDiscontinuity"))
)
if mibBuilder.loadTexts:
    radiusDynAuthClientMIBGroup.setStatus("current")

radiusDynAuthClientAuthOnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 145, 2, 2, 2)
)
radiusDynAuthClientAuthOnlyGroup.setObjects(
      *(("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconAuthOnlyRequests"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconNakAuthOnlyRequest"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoAAuthOnlyRequest"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoANakAuthOnlyRequest"))
)
if mibBuilder.loadTexts:
    radiusDynAuthClientAuthOnlyGroup.setStatus("current")

radiusDynAuthClientNoSessGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 145, 2, 2, 3)
)
radiusDynAuthClientNoSessGroup.setObjects(
      *(("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientDisconNakSessNoContext"),
        ("RADIUS-DYNAUTH-CLIENT-MIB", "radiusDynAuthClientCoANakSessNoContext"))
)
if mibBuilder.loadTexts:
    radiusDynAuthClientNoSessGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusDynAuthClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 145, 2, 1, 1)
)
if mibBuilder.loadTexts:
    radiusDynAuthClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-DYNAUTH-CLIENT-MIB",
    **{"radiusDynAuthClientMIB": radiusDynAuthClientMIB,
       "radiusDynAuthClientMIBObjects": radiusDynAuthClientMIBObjects,
       "radiusDynAuthClientScalars": radiusDynAuthClientScalars,
       "radiusDynAuthClientDisconInvalidServerAddresses": radiusDynAuthClientDisconInvalidServerAddresses,
       "radiusDynAuthClientCoAInvalidServerAddresses": radiusDynAuthClientCoAInvalidServerAddresses,
       "radiusDynAuthServerTable": radiusDynAuthServerTable,
       "radiusDynAuthServerEntry": radiusDynAuthServerEntry,
       "radiusDynAuthServerIndex": radiusDynAuthServerIndex,
       "radiusDynAuthServerAddressType": radiusDynAuthServerAddressType,
       "radiusDynAuthServerAddress": radiusDynAuthServerAddress,
       "radiusDynAuthServerClientPortNumber": radiusDynAuthServerClientPortNumber,
       "radiusDynAuthServerID": radiusDynAuthServerID,
       "radiusDynAuthClientRoundTripTime": radiusDynAuthClientRoundTripTime,
       "radiusDynAuthClientDisconRequests": radiusDynAuthClientDisconRequests,
       "radiusDynAuthClientDisconAuthOnlyRequests": radiusDynAuthClientDisconAuthOnlyRequests,
       "radiusDynAuthClientDisconRetransmissions": radiusDynAuthClientDisconRetransmissions,
       "radiusDynAuthClientDisconAcks": radiusDynAuthClientDisconAcks,
       "radiusDynAuthClientDisconNaks": radiusDynAuthClientDisconNaks,
       "radiusDynAuthClientDisconNakAuthOnlyRequest": radiusDynAuthClientDisconNakAuthOnlyRequest,
       "radiusDynAuthClientDisconNakSessNoContext": radiusDynAuthClientDisconNakSessNoContext,
       "radiusDynAuthClientMalformedDisconResponses": radiusDynAuthClientMalformedDisconResponses,
       "radiusDynAuthClientDisconBadAuthenticators": radiusDynAuthClientDisconBadAuthenticators,
       "radiusDynAuthClientDisconPendingRequests": radiusDynAuthClientDisconPendingRequests,
       "radiusDynAuthClientDisconTimeouts": radiusDynAuthClientDisconTimeouts,
       "radiusDynAuthClientDisconPacketsDropped": radiusDynAuthClientDisconPacketsDropped,
       "radiusDynAuthClientCoARequests": radiusDynAuthClientCoARequests,
       "radiusDynAuthClientCoAAuthOnlyRequest": radiusDynAuthClientCoAAuthOnlyRequest,
       "radiusDynAuthClientCoARetransmissions": radiusDynAuthClientCoARetransmissions,
       "radiusDynAuthClientCoAAcks": radiusDynAuthClientCoAAcks,
       "radiusDynAuthClientCoANaks": radiusDynAuthClientCoANaks,
       "radiusDynAuthClientCoANakAuthOnlyRequest": radiusDynAuthClientCoANakAuthOnlyRequest,
       "radiusDynAuthClientCoANakSessNoContext": radiusDynAuthClientCoANakSessNoContext,
       "radiusDynAuthClientMalformedCoAResponses": radiusDynAuthClientMalformedCoAResponses,
       "radiusDynAuthClientCoABadAuthenticators": radiusDynAuthClientCoABadAuthenticators,
       "radiusDynAuthClientCoAPendingRequests": radiusDynAuthClientCoAPendingRequests,
       "radiusDynAuthClientCoATimeouts": radiusDynAuthClientCoATimeouts,
       "radiusDynAuthClientCoAPacketsDropped": radiusDynAuthClientCoAPacketsDropped,
       "radiusDynAuthClientUnknownTypes": radiusDynAuthClientUnknownTypes,
       "radiusDynAuthClientCounterDiscontinuity": radiusDynAuthClientCounterDiscontinuity,
       "radiusDynAuthClientMIBConformance": radiusDynAuthClientMIBConformance,
       "radiusDynAuthClientMIBCompliances": radiusDynAuthClientMIBCompliances,
       "radiusDynAuthClientMIBCompliance": radiusDynAuthClientMIBCompliance,
       "radiusDynAuthClientMIBGroups": radiusDynAuthClientMIBGroups,
       "radiusDynAuthClientMIBGroup": radiusDynAuthClientMIBGroup,
       "radiusDynAuthClientAuthOnlyGroup": radiusDynAuthClientAuthOnlyGroup,
       "radiusDynAuthClientNoSessGroup": radiusDynAuthClientNoSessGroup}
)
