# SNMP MIB module (APRADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APRADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:55 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apRadiusServerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApRadiusServerMIBObjects_ObjectIdentity = ObjectIdentity
apRadiusServerMIBObjects = _ApRadiusServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1)
)
_ApRadiusServerStatsTable_Object = MibTable
apRadiusServerStatsTable = _ApRadiusServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1)
)
if mibBuilder.loadTexts:
    apRadiusServerStatsTable.setStatus("current")
_ApRadiusServerStatsEntry_Object = MibTableRow
apRadiusServerStatsEntry = _ApRadiusServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1)
)
apRadiusServerStatsEntry.setIndexNames(
    (0, "APRADIUS-MIB", "apRadiusServerAddressType"),
    (0, "APRADIUS-MIB", "apRadiusServerAddress"),
)
if mibBuilder.loadTexts:
    apRadiusServerStatsEntry.setStatus("current")
_ApRadiusServerAddressType_Type = InetAddressType
_ApRadiusServerAddressType_Object = MibTableColumn
apRadiusServerAddressType = _ApRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 1),
    _ApRadiusServerAddressType_Type()
)
apRadiusServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerAddressType.setStatus("current")
_ApRadiusServerAddress_Type = InetAddress
_ApRadiusServerAddress_Object = MibTableColumn
apRadiusServerAddress = _ApRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 2),
    _ApRadiusServerAddress_Type()
)
apRadiusServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerAddress.setStatus("current")
_ApRadiusServerRoundTripTime_Type = Unsigned32
_ApRadiusServerRoundTripTime_Object = MibTableColumn
apRadiusServerRoundTripTime = _ApRadiusServerRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 3),
    _ApRadiusServerRoundTripTime_Type()
)
apRadiusServerRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerRoundTripTime.setStatus("current")
_ApRadiusServerMalformedAccessResponse_Type = Unsigned32
_ApRadiusServerMalformedAccessResponse_Object = MibTableColumn
apRadiusServerMalformedAccessResponse = _ApRadiusServerMalformedAccessResponse_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 4),
    _ApRadiusServerMalformedAccessResponse_Type()
)
apRadiusServerMalformedAccessResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerMalformedAccessResponse.setStatus("current")
_ApRadiusServerAccessRequests_Type = Unsigned32
_ApRadiusServerAccessRequests_Object = MibTableColumn
apRadiusServerAccessRequests = _ApRadiusServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 5),
    _ApRadiusServerAccessRequests_Type()
)
apRadiusServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerAccessRequests.setStatus("current")
_ApRadiusServerDisconnectRequests_Type = Unsigned32
_ApRadiusServerDisconnectRequests_Object = MibTableColumn
apRadiusServerDisconnectRequests = _ApRadiusServerDisconnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 6),
    _ApRadiusServerDisconnectRequests_Type()
)
apRadiusServerDisconnectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerDisconnectRequests.setStatus("current")
_ApRadiusServerDisconnectACKs_Type = Unsigned32
_ApRadiusServerDisconnectACKs_Object = MibTableColumn
apRadiusServerDisconnectACKs = _ApRadiusServerDisconnectACKs_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 7),
    _ApRadiusServerDisconnectACKs_Type()
)
apRadiusServerDisconnectACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerDisconnectACKs.setStatus("current")
_ApRadiusServerDisconnectNACks_Type = Unsigned32
_ApRadiusServerDisconnectNACks_Object = MibTableColumn
apRadiusServerDisconnectNACks = _ApRadiusServerDisconnectNACks_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 8),
    _ApRadiusServerDisconnectNACks_Type()
)
apRadiusServerDisconnectNACks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerDisconnectNACks.setStatus("current")
_ApRadiusServerBadAuthenticators_Type = Unsigned32
_ApRadiusServerBadAuthenticators_Object = MibTableColumn
apRadiusServerBadAuthenticators = _ApRadiusServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 9),
    _ApRadiusServerBadAuthenticators_Type()
)
apRadiusServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerBadAuthenticators.setStatus("current")
_ApRadiusServerAccessRetransmissions_Type = Unsigned32
_ApRadiusServerAccessRetransmissions_Object = MibTableColumn
apRadiusServerAccessRetransmissions = _ApRadiusServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 10),
    _ApRadiusServerAccessRetransmissions_Type()
)
apRadiusServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerAccessRetransmissions.setStatus("current")
_ApRadiusServerAccessAccepts_Type = Unsigned32
_ApRadiusServerAccessAccepts_Object = MibTableColumn
apRadiusServerAccessAccepts = _ApRadiusServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 11),
    _ApRadiusServerAccessAccepts_Type()
)
apRadiusServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerAccessAccepts.setStatus("current")
_ApRadiusServerTimeouts_Type = Unsigned32
_ApRadiusServerTimeouts_Object = MibTableColumn
apRadiusServerTimeouts = _ApRadiusServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 12),
    _ApRadiusServerTimeouts_Type()
)
apRadiusServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerTimeouts.setStatus("current")
_ApRadiusServerAccessRejects_Type = Unsigned32
_ApRadiusServerAccessRejects_Object = MibTableColumn
apRadiusServerAccessRejects = _ApRadiusServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 13),
    _ApRadiusServerAccessRejects_Type()
)
apRadiusServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerAccessRejects.setStatus("current")
_ApRadiusServerUnknownPDUTypes_Type = Unsigned32
_ApRadiusServerUnknownPDUTypes_Object = MibTableColumn
apRadiusServerUnknownPDUTypes = _ApRadiusServerUnknownPDUTypes_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 14),
    _ApRadiusServerUnknownPDUTypes_Type()
)
apRadiusServerUnknownPDUTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerUnknownPDUTypes.setStatus("current")
_ApRadiusServerAccessChallenges_Type = Unsigned32
_ApRadiusServerAccessChallenges_Object = MibTableColumn
apRadiusServerAccessChallenges = _ApRadiusServerAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 15),
    _ApRadiusServerAccessChallenges_Type()
)
apRadiusServerAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusServerAccessChallenges.setStatus("current")
_ApRadiusServerConformance_ObjectIdentity = ObjectIdentity
apRadiusServerConformance = _ApRadiusServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 2)
)
_ApRadiusObjectGroups_ObjectIdentity = ObjectIdentity
apRadiusObjectGroups = _ApRadiusObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 2, 1)
)

# Managed Objects groups

apRadiusInterfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 18, 2, 1, 1)
)
apRadiusInterfaceStatsGroup.setObjects(
      *(("APRADIUS-MIB", "apRadiusServerRoundTripTime"),
        ("APRADIUS-MIB", "apRadiusServerMalformedAccessResponse"),
        ("APRADIUS-MIB", "apRadiusServerAccessRequests"),
        ("APRADIUS-MIB", "apRadiusServerDisconnectRequests"),
        ("APRADIUS-MIB", "apRadiusServerDisconnectACKs"),
        ("APRADIUS-MIB", "apRadiusServerDisconnectNACks"),
        ("APRADIUS-MIB", "apRadiusServerBadAuthenticators"),
        ("APRADIUS-MIB", "apRadiusServerAccessRetransmissions"),
        ("APRADIUS-MIB", "apRadiusServerAccessAccepts"),
        ("APRADIUS-MIB", "apRadiusServerTimeouts"),
        ("APRADIUS-MIB", "apRadiusServerAccessRejects"),
        ("APRADIUS-MIB", "apRadiusServerUnknownPDUTypes"),
        ("APRADIUS-MIB", "apRadiusServerAccessChallenges"))
)
if mibBuilder.loadTexts:
    apRadiusInterfaceStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APRADIUS-MIB",
    **{"apRadiusServerModule": apRadiusServerModule,
       "apRadiusServerMIBObjects": apRadiusServerMIBObjects,
       "apRadiusServerStatsTable": apRadiusServerStatsTable,
       "apRadiusServerStatsEntry": apRadiusServerStatsEntry,
       "apRadiusServerAddressType": apRadiusServerAddressType,
       "apRadiusServerAddress": apRadiusServerAddress,
       "apRadiusServerRoundTripTime": apRadiusServerRoundTripTime,
       "apRadiusServerMalformedAccessResponse": apRadiusServerMalformedAccessResponse,
       "apRadiusServerAccessRequests": apRadiusServerAccessRequests,
       "apRadiusServerDisconnectRequests": apRadiusServerDisconnectRequests,
       "apRadiusServerDisconnectACKs": apRadiusServerDisconnectACKs,
       "apRadiusServerDisconnectNACks": apRadiusServerDisconnectNACks,
       "apRadiusServerBadAuthenticators": apRadiusServerBadAuthenticators,
       "apRadiusServerAccessRetransmissions": apRadiusServerAccessRetransmissions,
       "apRadiusServerAccessAccepts": apRadiusServerAccessAccepts,
       "apRadiusServerTimeouts": apRadiusServerTimeouts,
       "apRadiusServerAccessRejects": apRadiusServerAccessRejects,
       "apRadiusServerUnknownPDUTypes": apRadiusServerUnknownPDUTypes,
       "apRadiusServerAccessChallenges": apRadiusServerAccessChallenges,
       "apRadiusServerConformance": apRadiusServerConformance,
       "apRadiusObjectGroups": apRadiusObjectGroups,
       "apRadiusInterfaceStatsGroup": apRadiusInterfaceStatsGroup}
)
