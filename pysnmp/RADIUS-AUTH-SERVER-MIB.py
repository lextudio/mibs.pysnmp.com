# SNMP MIB module (RADIUS-AUTH-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADIUS-AUTH-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:27 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

radiusAuthServMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 79, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RadiusTime(Gauge32, TextualConvention):
    status = "current"
    displayHint = "4d"


# MIB Managed Objects in the order of their OIDs

_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 3, 79)
)
if mibBuilder.loadTexts:
    radius.setStatus("current")
_RadiusAuthentication_ObjectIdentity = ObjectIdentity
radiusAuthentication = _RadiusAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 3, 79, 1)
)
_RadiusAuthServMIBObjects_ObjectIdentity = ObjectIdentity
radiusAuthServMIBObjects = _RadiusAuthServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 79, 1, 1, 1)
)
_RadiusAuthServ_ObjectIdentity = ObjectIdentity
radiusAuthServ = _RadiusAuthServ_ObjectIdentity(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1)
)
_RadiusAuthServIdent_Type = DisplayString
_RadiusAuthServIdent_Object = MibScalar
radiusAuthServIdent = _RadiusAuthServIdent_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 1),
    _RadiusAuthServIdent_Type()
)
radiusAuthServIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServIdent.setStatus("current")
_RadiusAuthServUpTime_Type = RadiusTime
_RadiusAuthServUpTime_Object = MibScalar
radiusAuthServUpTime = _RadiusAuthServUpTime_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 2),
    _RadiusAuthServUpTime_Type()
)
radiusAuthServUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServUpTime.setStatus("current")
_RadiusAuthServResetTime_Type = RadiusTime
_RadiusAuthServResetTime_Object = MibScalar
radiusAuthServResetTime = _RadiusAuthServResetTime_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 3),
    _RadiusAuthServResetTime_Type()
)
radiusAuthServResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServResetTime.setStatus("current")


class _RadiusAuthServConfigReset_Type(Integer32):
    """Custom type radiusAuthServConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 3),
          ("other", 1),
          ("reset", 2),
          ("running", 4))
    )


_RadiusAuthServConfigReset_Type.__name__ = "Integer32"
_RadiusAuthServConfigReset_Object = MibScalar
radiusAuthServConfigReset = _RadiusAuthServConfigReset_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 4),
    _RadiusAuthServConfigReset_Type()
)
radiusAuthServConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServConfigReset.setStatus("current")
_RadiusAuthServTotalAccessRequests_Type = Counter32
_RadiusAuthServTotalAccessRequests_Object = MibScalar
radiusAuthServTotalAccessRequests = _RadiusAuthServTotalAccessRequests_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 5),
    _RadiusAuthServTotalAccessRequests_Type()
)
radiusAuthServTotalAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessRequests.setStatus("current")
_RadiusAuthServTotalInvalidRequests_Type = Counter32
_RadiusAuthServTotalInvalidRequests_Object = MibScalar
radiusAuthServTotalInvalidRequests = _RadiusAuthServTotalInvalidRequests_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 6),
    _RadiusAuthServTotalInvalidRequests_Type()
)
radiusAuthServTotalInvalidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalInvalidRequests.setStatus("current")
_RadiusAuthServTotalDupAccessRequests_Type = Counter32
_RadiusAuthServTotalDupAccessRequests_Object = MibScalar
radiusAuthServTotalDupAccessRequests = _RadiusAuthServTotalDupAccessRequests_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 7),
    _RadiusAuthServTotalDupAccessRequests_Type()
)
radiusAuthServTotalDupAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalDupAccessRequests.setStatus("current")
_RadiusAuthServTotalAccessAccepts_Type = Counter32
_RadiusAuthServTotalAccessAccepts_Object = MibScalar
radiusAuthServTotalAccessAccepts = _RadiusAuthServTotalAccessAccepts_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 8),
    _RadiusAuthServTotalAccessAccepts_Type()
)
radiusAuthServTotalAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessAccepts.setStatus("current")
_RadiusAuthServTotalAccessRejects_Type = Counter32
_RadiusAuthServTotalAccessRejects_Object = MibScalar
radiusAuthServTotalAccessRejects = _RadiusAuthServTotalAccessRejects_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 9),
    _RadiusAuthServTotalAccessRejects_Type()
)
radiusAuthServTotalAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessRejects.setStatus("current")
_RadiusAuthServTotalAccessChallenges_Type = Counter32
_RadiusAuthServTotalAccessChallenges_Object = MibScalar
radiusAuthServTotalAccessChallenges = _RadiusAuthServTotalAccessChallenges_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 10),
    _RadiusAuthServTotalAccessChallenges_Type()
)
radiusAuthServTotalAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalAccessChallenges.setStatus("current")
_RadiusAuthServTotalMalformedAccessRequests_Type = Counter32
_RadiusAuthServTotalMalformedAccessRequests_Object = MibScalar
radiusAuthServTotalMalformedAccessRequests = _RadiusAuthServTotalMalformedAccessRequests_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 11),
    _RadiusAuthServTotalMalformedAccessRequests_Type()
)
radiusAuthServTotalMalformedAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalMalformedAccessRequests.setStatus("current")
_RadiusAuthServTotalBadAuthenticators_Type = Counter32
_RadiusAuthServTotalBadAuthenticators_Object = MibScalar
radiusAuthServTotalBadAuthenticators = _RadiusAuthServTotalBadAuthenticators_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 12),
    _RadiusAuthServTotalBadAuthenticators_Type()
)
radiusAuthServTotalBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalBadAuthenticators.setStatus("current")
_RadiusAuthServTotalPacketsDropped_Type = Counter32
_RadiusAuthServTotalPacketsDropped_Object = MibScalar
radiusAuthServTotalPacketsDropped = _RadiusAuthServTotalPacketsDropped_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 13),
    _RadiusAuthServTotalPacketsDropped_Type()
)
radiusAuthServTotalPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalPacketsDropped.setStatus("current")
_RadiusAuthServTotalUnknownType_Type = Counter32
_RadiusAuthServTotalUnknownType_Object = MibScalar
radiusAuthServTotalUnknownType = _RadiusAuthServTotalUnknownType_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 14),
    _RadiusAuthServTotalUnknownType_Type()
)
radiusAuthServTotalUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServTotalUnknownType.setStatus("current")
_RadiusAuthClientTable_Object = MibTable
radiusAuthClientTable = _RadiusAuthClientTable_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    radiusAuthClientTable.setStatus("current")
_RadiusAuthClientEntry_Object = MibTableRow
radiusAuthClientEntry = _RadiusAuthClientEntry_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1)
)
radiusAuthClientEntry.setIndexNames(
    (0, "RADIUS-AUTH-SERVER-MIB", "radiusAuthClientIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthClientEntry.setStatus("current")
_RadiusAuthClientIndex_Type = Integer32
_RadiusAuthClientIndex_Object = MibTableColumn
radiusAuthClientIndex = _RadiusAuthClientIndex_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 1),
    _RadiusAuthClientIndex_Type()
)
radiusAuthClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthClientIndex.setStatus("current")
_RadiusAuthClientAddress_Type = IpAddress
_RadiusAuthClientAddress_Object = MibTableColumn
radiusAuthClientAddress = _RadiusAuthClientAddress_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 2),
    _RadiusAuthClientAddress_Type()
)
radiusAuthClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAddress.setStatus("current")
_RadiusAuthClientID_Type = DisplayString
_RadiusAuthClientID_Object = MibTableColumn
radiusAuthClientID = _RadiusAuthClientID_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 3),
    _RadiusAuthClientID_Type()
)
radiusAuthClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientID.setStatus("current")
_RadiusAuthServAccessRequests_Type = Counter32
_RadiusAuthServAccessRequests_Object = MibTableColumn
radiusAuthServAccessRequests = _RadiusAuthServAccessRequests_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 4),
    _RadiusAuthServAccessRequests_Type()
)
radiusAuthServAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServAccessRequests.setStatus("current")
_RadiusAuthServDupAccessRequests_Type = Counter32
_RadiusAuthServDupAccessRequests_Object = MibTableColumn
radiusAuthServDupAccessRequests = _RadiusAuthServDupAccessRequests_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 5),
    _RadiusAuthServDupAccessRequests_Type()
)
radiusAuthServDupAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServDupAccessRequests.setStatus("current")
_RadiusAuthServAccessAccepts_Type = Counter32
_RadiusAuthServAccessAccepts_Object = MibTableColumn
radiusAuthServAccessAccepts = _RadiusAuthServAccessAccepts_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 6),
    _RadiusAuthServAccessAccepts_Type()
)
radiusAuthServAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServAccessAccepts.setStatus("current")
_RadiusAuthServAccessRejects_Type = Counter32
_RadiusAuthServAccessRejects_Object = MibTableColumn
radiusAuthServAccessRejects = _RadiusAuthServAccessRejects_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 7),
    _RadiusAuthServAccessRejects_Type()
)
radiusAuthServAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServAccessRejects.setStatus("current")
_RadiusAuthServAccessChallenges_Type = Counter32
_RadiusAuthServAccessChallenges_Object = MibTableColumn
radiusAuthServAccessChallenges = _RadiusAuthServAccessChallenges_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 8),
    _RadiusAuthServAccessChallenges_Type()
)
radiusAuthServAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServAccessChallenges.setStatus("current")
_RadiusAuthServMalformedAccessRequests_Type = Counter32
_RadiusAuthServMalformedAccessRequests_Object = MibTableColumn
radiusAuthServMalformedAccessRequests = _RadiusAuthServMalformedAccessRequests_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 9),
    _RadiusAuthServMalformedAccessRequests_Type()
)
radiusAuthServMalformedAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServMalformedAccessRequests.setStatus("current")
_RadiusAuthServBadAuthenticators_Type = Counter32
_RadiusAuthServBadAuthenticators_Object = MibTableColumn
radiusAuthServBadAuthenticators = _RadiusAuthServBadAuthenticators_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 10),
    _RadiusAuthServBadAuthenticators_Type()
)
radiusAuthServBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServBadAuthenticators.setStatus("current")
_RadiusAuthServPacketsDropped_Type = Counter32
_RadiusAuthServPacketsDropped_Object = MibTableColumn
radiusAuthServPacketsDropped = _RadiusAuthServPacketsDropped_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 11),
    _RadiusAuthServPacketsDropped_Type()
)
radiusAuthServPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServPacketsDropped.setStatus("current")
_RadiusAuthServUnknownType_Type = Counter32
_RadiusAuthServUnknownType_Object = MibTableColumn
radiusAuthServUnknownType = _RadiusAuthServUnknownType_Object(
    (1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 12),
    _RadiusAuthServUnknownType_Type()
)
radiusAuthServUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServUnknownType.setStatus("current")
_RadiusAuthServMIBConformance_ObjectIdentity = ObjectIdentity
radiusAuthServMIBConformance = _RadiusAuthServMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 79, 1, 1, 2)
)
_RadiusAuthServMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAuthServMIBCompliances = _RadiusAuthServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 79, 1, 1, 2, 1)
)
_RadiusAuthServMIBGroups_ObjectIdentity = ObjectIdentity
radiusAuthServMIBGroups = _RadiusAuthServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 79, 1, 1, 2, 2)
)

# Managed Objects groups

radiusAuthServMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 79, 1, 1, 2, 2, 1)
)
radiusAuthServMIBGroup.setObjects(
      *(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServIdent"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUpTime"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServResetTime"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServConfigReset"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalInvalidRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalDupAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessAccepts"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRejects"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessChallenges"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalMalformedAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalBadAuthenticators"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalPacketsDropped"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalUnknownType"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientAddress"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientID"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServDupAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessAccepts"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRejects"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessChallenges"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMalformedAccessRequests"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServBadAuthenticators"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServPacketsDropped"),
        ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUnknownType"))
)
if mibBuilder.loadTexts:
    radiusAuthServMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAuthServMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 79, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    radiusAuthServMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-AUTH-SERVER-MIB",
    **{"RadiusTime": RadiusTime,
       "radius": radius,
       "radiusAuthentication": radiusAuthentication,
       "radiusAuthServMIB": radiusAuthServMIB,
       "radiusAuthServMIBObjects": radiusAuthServMIBObjects,
       "radiusAuthServ": radiusAuthServ,
       "radiusAuthServIdent": radiusAuthServIdent,
       "radiusAuthServUpTime": radiusAuthServUpTime,
       "radiusAuthServResetTime": radiusAuthServResetTime,
       "radiusAuthServConfigReset": radiusAuthServConfigReset,
       "radiusAuthServTotalAccessRequests": radiusAuthServTotalAccessRequests,
       "radiusAuthServTotalInvalidRequests": radiusAuthServTotalInvalidRequests,
       "radiusAuthServTotalDupAccessRequests": radiusAuthServTotalDupAccessRequests,
       "radiusAuthServTotalAccessAccepts": radiusAuthServTotalAccessAccepts,
       "radiusAuthServTotalAccessRejects": radiusAuthServTotalAccessRejects,
       "radiusAuthServTotalAccessChallenges": radiusAuthServTotalAccessChallenges,
       "radiusAuthServTotalMalformedAccessRequests": radiusAuthServTotalMalformedAccessRequests,
       "radiusAuthServTotalBadAuthenticators": radiusAuthServTotalBadAuthenticators,
       "radiusAuthServTotalPacketsDropped": radiusAuthServTotalPacketsDropped,
       "radiusAuthServTotalUnknownType": radiusAuthServTotalUnknownType,
       "radiusAuthClientTable": radiusAuthClientTable,
       "radiusAuthClientEntry": radiusAuthClientEntry,
       "radiusAuthClientIndex": radiusAuthClientIndex,
       "radiusAuthClientAddress": radiusAuthClientAddress,
       "radiusAuthClientID": radiusAuthClientID,
       "radiusAuthServAccessRequests": radiusAuthServAccessRequests,
       "radiusAuthServDupAccessRequests": radiusAuthServDupAccessRequests,
       "radiusAuthServAccessAccepts": radiusAuthServAccessAccepts,
       "radiusAuthServAccessRejects": radiusAuthServAccessRejects,
       "radiusAuthServAccessChallenges": radiusAuthServAccessChallenges,
       "radiusAuthServMalformedAccessRequests": radiusAuthServMalformedAccessRequests,
       "radiusAuthServBadAuthenticators": radiusAuthServBadAuthenticators,
       "radiusAuthServPacketsDropped": radiusAuthServPacketsDropped,
       "radiusAuthServUnknownType": radiusAuthServUnknownType,
       "radiusAuthServMIBConformance": radiusAuthServMIBConformance,
       "radiusAuthServMIBCompliances": radiusAuthServMIBCompliances,
       "radiusAuthServMIBCompliance": radiusAuthServMIBCompliance,
       "radiusAuthServMIBGroups": radiusAuthServMIBGroups,
       "radiusAuthServMIBGroup": radiusAuthServMIBGroup}
)
