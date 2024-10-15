# SNMP MIB module (RADIUS-DYNAUTH-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADIUS-DYNAUTH-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:20 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

radiusDynAuthServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 146)
)
radiusDynAuthServerMIB.setRevisions(
        ("2006-08-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusDynAuthServerMIBObjects_ObjectIdentity = ObjectIdentity
radiusDynAuthServerMIBObjects = _RadiusDynAuthServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 146, 1)
)
_RadiusDynAuthServerScalars_ObjectIdentity = ObjectIdentity
radiusDynAuthServerScalars = _RadiusDynAuthServerScalars_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 146, 1, 1)
)
_RadiusDynAuthServerDisconInvalidClientAddresses_Type = Counter32
_RadiusDynAuthServerDisconInvalidClientAddresses_Object = MibScalar
radiusDynAuthServerDisconInvalidClientAddresses = _RadiusDynAuthServerDisconInvalidClientAddresses_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 1, 1),
    _RadiusDynAuthServerDisconInvalidClientAddresses_Type()
)
radiusDynAuthServerDisconInvalidClientAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServerDisconInvalidClientAddresses.setStatus("current")
_RadiusDynAuthServerCoAInvalidClientAddresses_Type = Counter32
_RadiusDynAuthServerCoAInvalidClientAddresses_Object = MibScalar
radiusDynAuthServerCoAInvalidClientAddresses = _RadiusDynAuthServerCoAInvalidClientAddresses_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 1, 2),
    _RadiusDynAuthServerCoAInvalidClientAddresses_Type()
)
radiusDynAuthServerCoAInvalidClientAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServerCoAInvalidClientAddresses.setStatus("current")
_RadiusDynAuthServerIdentifier_Type = SnmpAdminString
_RadiusDynAuthServerIdentifier_Object = MibScalar
radiusDynAuthServerIdentifier = _RadiusDynAuthServerIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 1, 3),
    _RadiusDynAuthServerIdentifier_Type()
)
radiusDynAuthServerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServerIdentifier.setStatus("current")
_RadiusDynAuthClientTable_Object = MibTable
radiusDynAuthClientTable = _RadiusDynAuthClientTable_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2)
)
if mibBuilder.loadTexts:
    radiusDynAuthClientTable.setStatus("current")
_RadiusDynAuthClientEntry_Object = MibTableRow
radiusDynAuthClientEntry = _RadiusDynAuthClientEntry_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1)
)
radiusDynAuthClientEntry.setIndexNames(
    (0, "RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthClientIndex"),
)
if mibBuilder.loadTexts:
    radiusDynAuthClientEntry.setStatus("current")


class _RadiusDynAuthClientIndex_Type(Integer32):
    """Custom type radiusDynAuthClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusDynAuthClientIndex_Type.__name__ = "Integer32"
_RadiusDynAuthClientIndex_Object = MibTableColumn
radiusDynAuthClientIndex = _RadiusDynAuthClientIndex_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 1),
    _RadiusDynAuthClientIndex_Type()
)
radiusDynAuthClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusDynAuthClientIndex.setStatus("current")
_RadiusDynAuthClientAddressType_Type = InetAddressType
_RadiusDynAuthClientAddressType_Object = MibTableColumn
radiusDynAuthClientAddressType = _RadiusDynAuthClientAddressType_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 2),
    _RadiusDynAuthClientAddressType_Type()
)
radiusDynAuthClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientAddressType.setStatus("current")
_RadiusDynAuthClientAddress_Type = InetAddress
_RadiusDynAuthClientAddress_Object = MibTableColumn
radiusDynAuthClientAddress = _RadiusDynAuthClientAddress_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 3),
    _RadiusDynAuthClientAddress_Type()
)
radiusDynAuthClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthClientAddress.setStatus("current")
_RadiusDynAuthServDisconRequests_Type = Counter32
_RadiusDynAuthServDisconRequests_Object = MibTableColumn
radiusDynAuthServDisconRequests = _RadiusDynAuthServDisconRequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 4),
    _RadiusDynAuthServDisconRequests_Type()
)
radiusDynAuthServDisconRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconRequests.setUnits("requests")
_RadiusDynAuthServDisconAuthOnlyRequests_Type = Counter32
_RadiusDynAuthServDisconAuthOnlyRequests_Object = MibTableColumn
radiusDynAuthServDisconAuthOnlyRequests = _RadiusDynAuthServDisconAuthOnlyRequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 5),
    _RadiusDynAuthServDisconAuthOnlyRequests_Type()
)
radiusDynAuthServDisconAuthOnlyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconAuthOnlyRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconAuthOnlyRequests.setUnits("requests")
_RadiusDynAuthServDupDisconRequests_Type = Counter32
_RadiusDynAuthServDupDisconRequests_Object = MibTableColumn
radiusDynAuthServDupDisconRequests = _RadiusDynAuthServDupDisconRequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 6),
    _RadiusDynAuthServDupDisconRequests_Type()
)
radiusDynAuthServDupDisconRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDupDisconRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDupDisconRequests.setUnits("requests")
_RadiusDynAuthServDisconAcks_Type = Counter32
_RadiusDynAuthServDisconAcks_Object = MibTableColumn
radiusDynAuthServDisconAcks = _RadiusDynAuthServDisconAcks_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 7),
    _RadiusDynAuthServDisconAcks_Type()
)
radiusDynAuthServDisconAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconAcks.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconAcks.setUnits("replies")
_RadiusDynAuthServDisconNaks_Type = Counter32
_RadiusDynAuthServDisconNaks_Object = MibTableColumn
radiusDynAuthServDisconNaks = _RadiusDynAuthServDisconNaks_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 8),
    _RadiusDynAuthServDisconNaks_Type()
)
radiusDynAuthServDisconNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconNaks.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconNaks.setUnits("replies")
_RadiusDynAuthServDisconNakAuthOnlyRequests_Type = Counter32
_RadiusDynAuthServDisconNakAuthOnlyRequests_Object = MibTableColumn
radiusDynAuthServDisconNakAuthOnlyRequests = _RadiusDynAuthServDisconNakAuthOnlyRequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 9),
    _RadiusDynAuthServDisconNakAuthOnlyRequests_Type()
)
radiusDynAuthServDisconNakAuthOnlyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconNakAuthOnlyRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconNakAuthOnlyRequests.setUnits("replies")
_RadiusDynAuthServDisconNakSessNoContext_Type = Counter32
_RadiusDynAuthServDisconNakSessNoContext_Object = MibTableColumn
radiusDynAuthServDisconNakSessNoContext = _RadiusDynAuthServDisconNakSessNoContext_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 10),
    _RadiusDynAuthServDisconNakSessNoContext_Type()
)
radiusDynAuthServDisconNakSessNoContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconNakSessNoContext.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconNakSessNoContext.setUnits("replies")
_RadiusDynAuthServDisconUserSessRemoved_Type = Counter32
_RadiusDynAuthServDisconUserSessRemoved_Object = MibTableColumn
radiusDynAuthServDisconUserSessRemoved = _RadiusDynAuthServDisconUserSessRemoved_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 11),
    _RadiusDynAuthServDisconUserSessRemoved_Type()
)
radiusDynAuthServDisconUserSessRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconUserSessRemoved.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconUserSessRemoved.setUnits("sessions")
_RadiusDynAuthServMalformedDisconRequests_Type = Counter32
_RadiusDynAuthServMalformedDisconRequests_Object = MibTableColumn
radiusDynAuthServMalformedDisconRequests = _RadiusDynAuthServMalformedDisconRequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 12),
    _RadiusDynAuthServMalformedDisconRequests_Type()
)
radiusDynAuthServMalformedDisconRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServMalformedDisconRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServMalformedDisconRequests.setUnits("requests")
_RadiusDynAuthServDisconBadAuthenticators_Type = Counter32
_RadiusDynAuthServDisconBadAuthenticators_Object = MibTableColumn
radiusDynAuthServDisconBadAuthenticators = _RadiusDynAuthServDisconBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 13),
    _RadiusDynAuthServDisconBadAuthenticators_Type()
)
radiusDynAuthServDisconBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconBadAuthenticators.setUnits("requests")
_RadiusDynAuthServDisconPacketsDropped_Type = Counter32
_RadiusDynAuthServDisconPacketsDropped_Object = MibTableColumn
radiusDynAuthServDisconPacketsDropped = _RadiusDynAuthServDisconPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 14),
    _RadiusDynAuthServDisconPacketsDropped_Type()
)
radiusDynAuthServDisconPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDisconPacketsDropped.setUnits("requests")
_RadiusDynAuthServCoARequests_Type = Counter32
_RadiusDynAuthServCoARequests_Object = MibTableColumn
radiusDynAuthServCoARequests = _RadiusDynAuthServCoARequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 15),
    _RadiusDynAuthServCoARequests_Type()
)
radiusDynAuthServCoARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoARequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoARequests.setUnits("requests")
_RadiusDynAuthServCoAAuthOnlyRequests_Type = Counter32
_RadiusDynAuthServCoAAuthOnlyRequests_Object = MibTableColumn
radiusDynAuthServCoAAuthOnlyRequests = _RadiusDynAuthServCoAAuthOnlyRequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 16),
    _RadiusDynAuthServCoAAuthOnlyRequests_Type()
)
radiusDynAuthServCoAAuthOnlyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoAAuthOnlyRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoAAuthOnlyRequests.setUnits("requests")
_RadiusDynAuthServDupCoARequests_Type = Counter32
_RadiusDynAuthServDupCoARequests_Object = MibTableColumn
radiusDynAuthServDupCoARequests = _RadiusDynAuthServDupCoARequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 17),
    _RadiusDynAuthServDupCoARequests_Type()
)
radiusDynAuthServDupCoARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServDupCoARequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServDupCoARequests.setUnits("requests")
_RadiusDynAuthServCoAAcks_Type = Counter32
_RadiusDynAuthServCoAAcks_Object = MibTableColumn
radiusDynAuthServCoAAcks = _RadiusDynAuthServCoAAcks_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 18),
    _RadiusDynAuthServCoAAcks_Type()
)
radiusDynAuthServCoAAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoAAcks.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoAAcks.setUnits("replies")
_RadiusDynAuthServCoANaks_Type = Counter32
_RadiusDynAuthServCoANaks_Object = MibTableColumn
radiusDynAuthServCoANaks = _RadiusDynAuthServCoANaks_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 19),
    _RadiusDynAuthServCoANaks_Type()
)
radiusDynAuthServCoANaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoANaks.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoANaks.setUnits("replies")
_RadiusDynAuthServCoANakAuthOnlyRequests_Type = Counter32
_RadiusDynAuthServCoANakAuthOnlyRequests_Object = MibTableColumn
radiusDynAuthServCoANakAuthOnlyRequests = _RadiusDynAuthServCoANakAuthOnlyRequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 20),
    _RadiusDynAuthServCoANakAuthOnlyRequests_Type()
)
radiusDynAuthServCoANakAuthOnlyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoANakAuthOnlyRequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoANakAuthOnlyRequests.setUnits("replies")
_RadiusDynAuthServCoANakSessNoContext_Type = Counter32
_RadiusDynAuthServCoANakSessNoContext_Object = MibTableColumn
radiusDynAuthServCoANakSessNoContext = _RadiusDynAuthServCoANakSessNoContext_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 21),
    _RadiusDynAuthServCoANakSessNoContext_Type()
)
radiusDynAuthServCoANakSessNoContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoANakSessNoContext.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoANakSessNoContext.setUnits("replies")
_RadiusDynAuthServCoAUserSessChanged_Type = Counter32
_RadiusDynAuthServCoAUserSessChanged_Object = MibTableColumn
radiusDynAuthServCoAUserSessChanged = _RadiusDynAuthServCoAUserSessChanged_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 22),
    _RadiusDynAuthServCoAUserSessChanged_Type()
)
radiusDynAuthServCoAUserSessChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoAUserSessChanged.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoAUserSessChanged.setUnits("sessions")
_RadiusDynAuthServMalformedCoARequests_Type = Counter32
_RadiusDynAuthServMalformedCoARequests_Object = MibTableColumn
radiusDynAuthServMalformedCoARequests = _RadiusDynAuthServMalformedCoARequests_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 23),
    _RadiusDynAuthServMalformedCoARequests_Type()
)
radiusDynAuthServMalformedCoARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServMalformedCoARequests.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServMalformedCoARequests.setUnits("requests")
_RadiusDynAuthServCoABadAuthenticators_Type = Counter32
_RadiusDynAuthServCoABadAuthenticators_Object = MibTableColumn
radiusDynAuthServCoABadAuthenticators = _RadiusDynAuthServCoABadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 24),
    _RadiusDynAuthServCoABadAuthenticators_Type()
)
radiusDynAuthServCoABadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoABadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoABadAuthenticators.setUnits("requests")
_RadiusDynAuthServCoAPacketsDropped_Type = Counter32
_RadiusDynAuthServCoAPacketsDropped_Object = MibTableColumn
radiusDynAuthServCoAPacketsDropped = _RadiusDynAuthServCoAPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 25),
    _RadiusDynAuthServCoAPacketsDropped_Type()
)
radiusDynAuthServCoAPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServCoAPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServCoAPacketsDropped.setUnits("requests")
_RadiusDynAuthServUnknownTypes_Type = Counter32
_RadiusDynAuthServUnknownTypes_Object = MibTableColumn
radiusDynAuthServUnknownTypes = _RadiusDynAuthServUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 26),
    _RadiusDynAuthServUnknownTypes_Type()
)
radiusDynAuthServUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServUnknownTypes.setUnits("requests")
_RadiusDynAuthServerCounterDiscontinuity_Type = TimeTicks
_RadiusDynAuthServerCounterDiscontinuity_Object = MibTableColumn
radiusDynAuthServerCounterDiscontinuity = _RadiusDynAuthServerCounterDiscontinuity_Object(
    (1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 27),
    _RadiusDynAuthServerCounterDiscontinuity_Type()
)
radiusDynAuthServerCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDynAuthServerCounterDiscontinuity.setStatus("current")
if mibBuilder.loadTexts:
    radiusDynAuthServerCounterDiscontinuity.setUnits("hundredths of a second")
_RadiusDynAuthServerMIBConformance_ObjectIdentity = ObjectIdentity
radiusDynAuthServerMIBConformance = _RadiusDynAuthServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 146, 2)
)
_RadiusDynAuthServerMIBCompliances_ObjectIdentity = ObjectIdentity
radiusDynAuthServerMIBCompliances = _RadiusDynAuthServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 146, 2, 1)
)
_RadiusDynAuthServerMIBGroups_ObjectIdentity = ObjectIdentity
radiusDynAuthServerMIBGroups = _RadiusDynAuthServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 146, 2, 2)
)

# Managed Objects groups

radiusDynAuthServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 146, 2, 2, 1)
)
radiusDynAuthServerMIBGroup.setObjects(
      *(("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerDisconInvalidClientAddresses"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerCoAInvalidClientAddresses"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerIdentifier"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthClientAddressType"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthClientAddress"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconRequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDupDisconRequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconAcks"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconNaks"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconUserSessRemoved"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServMalformedDisconRequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconBadAuthenticators"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconPacketsDropped"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoARequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDupCoARequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoAAcks"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoANaks"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoAUserSessChanged"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServMalformedCoARequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoABadAuthenticators"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoAPacketsDropped"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServUnknownTypes"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerCounterDiscontinuity"))
)
if mibBuilder.loadTexts:
    radiusDynAuthServerMIBGroup.setStatus("current")

radiusDynAuthServerAuthOnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 146, 2, 2, 2)
)
radiusDynAuthServerAuthOnlyGroup.setObjects(
      *(("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconAuthOnlyRequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconNakAuthOnlyRequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoAAuthOnlyRequests"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoANakAuthOnlyRequests"))
)
if mibBuilder.loadTexts:
    radiusDynAuthServerAuthOnlyGroup.setStatus("current")

radiusDynAuthServerNoSessGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 146, 2, 2, 3)
)
radiusDynAuthServerNoSessGroup.setObjects(
      *(("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconNakSessNoContext"),
        ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoANakSessNoContext"))
)
if mibBuilder.loadTexts:
    radiusDynAuthServerNoSessGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAuthServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 146, 2, 1, 1)
)
if mibBuilder.loadTexts:
    radiusAuthServerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-DYNAUTH-SERVER-MIB",
    **{"radiusDynAuthServerMIB": radiusDynAuthServerMIB,
       "radiusDynAuthServerMIBObjects": radiusDynAuthServerMIBObjects,
       "radiusDynAuthServerScalars": radiusDynAuthServerScalars,
       "radiusDynAuthServerDisconInvalidClientAddresses": radiusDynAuthServerDisconInvalidClientAddresses,
       "radiusDynAuthServerCoAInvalidClientAddresses": radiusDynAuthServerCoAInvalidClientAddresses,
       "radiusDynAuthServerIdentifier": radiusDynAuthServerIdentifier,
       "radiusDynAuthClientTable": radiusDynAuthClientTable,
       "radiusDynAuthClientEntry": radiusDynAuthClientEntry,
       "radiusDynAuthClientIndex": radiusDynAuthClientIndex,
       "radiusDynAuthClientAddressType": radiusDynAuthClientAddressType,
       "radiusDynAuthClientAddress": radiusDynAuthClientAddress,
       "radiusDynAuthServDisconRequests": radiusDynAuthServDisconRequests,
       "radiusDynAuthServDisconAuthOnlyRequests": radiusDynAuthServDisconAuthOnlyRequests,
       "radiusDynAuthServDupDisconRequests": radiusDynAuthServDupDisconRequests,
       "radiusDynAuthServDisconAcks": radiusDynAuthServDisconAcks,
       "radiusDynAuthServDisconNaks": radiusDynAuthServDisconNaks,
       "radiusDynAuthServDisconNakAuthOnlyRequests": radiusDynAuthServDisconNakAuthOnlyRequests,
       "radiusDynAuthServDisconNakSessNoContext": radiusDynAuthServDisconNakSessNoContext,
       "radiusDynAuthServDisconUserSessRemoved": radiusDynAuthServDisconUserSessRemoved,
       "radiusDynAuthServMalformedDisconRequests": radiusDynAuthServMalformedDisconRequests,
       "radiusDynAuthServDisconBadAuthenticators": radiusDynAuthServDisconBadAuthenticators,
       "radiusDynAuthServDisconPacketsDropped": radiusDynAuthServDisconPacketsDropped,
       "radiusDynAuthServCoARequests": radiusDynAuthServCoARequests,
       "radiusDynAuthServCoAAuthOnlyRequests": radiusDynAuthServCoAAuthOnlyRequests,
       "radiusDynAuthServDupCoARequests": radiusDynAuthServDupCoARequests,
       "radiusDynAuthServCoAAcks": radiusDynAuthServCoAAcks,
       "radiusDynAuthServCoANaks": radiusDynAuthServCoANaks,
       "radiusDynAuthServCoANakAuthOnlyRequests": radiusDynAuthServCoANakAuthOnlyRequests,
       "radiusDynAuthServCoANakSessNoContext": radiusDynAuthServCoANakSessNoContext,
       "radiusDynAuthServCoAUserSessChanged": radiusDynAuthServCoAUserSessChanged,
       "radiusDynAuthServMalformedCoARequests": radiusDynAuthServMalformedCoARequests,
       "radiusDynAuthServCoABadAuthenticators": radiusDynAuthServCoABadAuthenticators,
       "radiusDynAuthServCoAPacketsDropped": radiusDynAuthServCoAPacketsDropped,
       "radiusDynAuthServUnknownTypes": radiusDynAuthServUnknownTypes,
       "radiusDynAuthServerCounterDiscontinuity": radiusDynAuthServerCounterDiscontinuity,
       "radiusDynAuthServerMIBConformance": radiusDynAuthServerMIBConformance,
       "radiusDynAuthServerMIBCompliances": radiusDynAuthServerMIBCompliances,
       "radiusAuthServerMIBCompliance": radiusAuthServerMIBCompliance,
       "radiusDynAuthServerMIBGroups": radiusDynAuthServerMIBGroups,
       "radiusDynAuthServerMIBGroup": radiusDynAuthServerMIBGroup,
       "radiusDynAuthServerAuthOnlyGroup": radiusDynAuthServerAuthOnlyGroup,
       "radiusDynAuthServerNoSessGroup": radiusDynAuthServerNoSessGroup}
)
