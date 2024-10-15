# SNMP MIB module (Juniper-RADIUS-Initiated-Request-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-RADIUS-Initiated-Request-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:11 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

juniRadiusInitiatedRequestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75)
)
juniRadiusInitiatedRequestMIB.setRevisions(
        ("2004-06-10 19:08",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniRadiusInitiatedRequestObjects_ObjectIdentity = ObjectIdentity
juniRadiusInitiatedRequestObjects = _JuniRadiusInitiatedRequestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1)
)
_JuniRadiusInitiatedRequest_ObjectIdentity = ObjectIdentity
juniRadiusInitiatedRequest = _JuniRadiusInitiatedRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1)
)
_JuniRadiusInitiatedRequestInvalidClientAddresses_Type = Counter32
_JuniRadiusInitiatedRequestInvalidClientAddresses_Object = MibScalar
juniRadiusInitiatedRequestInvalidClientAddresses = _JuniRadiusInitiatedRequestInvalidClientAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 1),
    _JuniRadiusInitiatedRequestInvalidClientAddresses_Type()
)
juniRadiusInitiatedRequestInvalidClientAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestInvalidClientAddresses.setStatus("current")
_JuniRadiusInitiatedRequestClientTable_Object = MibTable
juniRadiusInitiatedRequestClientTable = _JuniRadiusInitiatedRequestClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestClientTable.setStatus("current")
_JuniRadiusInitiatedRequestClientEntry_Object = MibTableRow
juniRadiusInitiatedRequestClientEntry = _JuniRadiusInitiatedRequestClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1)
)
juniRadiusInitiatedRequestClientEntry.setIndexNames(
    (0, "Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestClientAddress"),
)
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestClientEntry.setStatus("current")
_JuniRadiusInitiatedRequestClientAddress_Type = IpAddress
_JuniRadiusInitiatedRequestClientAddress_Object = MibTableColumn
juniRadiusInitiatedRequestClientAddress = _JuniRadiusInitiatedRequestClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 1),
    _JuniRadiusInitiatedRequestClientAddress_Type()
)
juniRadiusInitiatedRequestClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestClientAddress.setStatus("current")
_JuniRadiusInitiatedRequestClientPortNumber_Type = Integer32
_JuniRadiusInitiatedRequestClientPortNumber_Object = MibTableColumn
juniRadiusInitiatedRequestClientPortNumber = _JuniRadiusInitiatedRequestClientPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 2),
    _JuniRadiusInitiatedRequestClientPortNumber_Type()
)
juniRadiusInitiatedRequestClientPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestClientPortNumber.setStatus("current")
_JuniRadiusInitiatedRequestUnknownTypes_Type = Counter32
_JuniRadiusInitiatedRequestUnknownTypes_Object = MibTableColumn
juniRadiusInitiatedRequestUnknownTypes = _JuniRadiusInitiatedRequestUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 3),
    _JuniRadiusInitiatedRequestUnknownTypes_Type()
)
juniRadiusInitiatedRequestUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestUnknownTypes.setStatus("current")
_JuniRadiusInitiatedRequestNoSecret_Type = Counter32
_JuniRadiusInitiatedRequestNoSecret_Object = MibTableColumn
juniRadiusInitiatedRequestNoSecret = _JuniRadiusInitiatedRequestNoSecret_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 4),
    _JuniRadiusInitiatedRequestNoSecret_Type()
)
juniRadiusInitiatedRequestNoSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestNoSecret.setStatus("current")
_JuniRadiusInitiatedRequestDisconnectRequests_Type = Counter32
_JuniRadiusInitiatedRequestDisconnectRequests_Object = MibTableColumn
juniRadiusInitiatedRequestDisconnectRequests = _JuniRadiusInitiatedRequestDisconnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 5),
    _JuniRadiusInitiatedRequestDisconnectRequests_Type()
)
juniRadiusInitiatedRequestDisconnectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestDisconnectRequests.setStatus("current")
_JuniRadiusInitiatedRequestDisconnectAccepts_Type = Counter32
_JuniRadiusInitiatedRequestDisconnectAccepts_Object = MibTableColumn
juniRadiusInitiatedRequestDisconnectAccepts = _JuniRadiusInitiatedRequestDisconnectAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 6),
    _JuniRadiusInitiatedRequestDisconnectAccepts_Type()
)
juniRadiusInitiatedRequestDisconnectAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestDisconnectAccepts.setStatus("current")
_JuniRadiusInitiatedRequestDisconnectRejects_Type = Counter32
_JuniRadiusInitiatedRequestDisconnectRejects_Object = MibTableColumn
juniRadiusInitiatedRequestDisconnectRejects = _JuniRadiusInitiatedRequestDisconnectRejects_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 7),
    _JuniRadiusInitiatedRequestDisconnectRejects_Type()
)
juniRadiusInitiatedRequestDisconnectRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestDisconnectRejects.setStatus("current")
_JuniRadiusInitiatedRequestDisconnectNoSessionIds_Type = Counter32
_JuniRadiusInitiatedRequestDisconnectNoSessionIds_Object = MibTableColumn
juniRadiusInitiatedRequestDisconnectNoSessionIds = _JuniRadiusInitiatedRequestDisconnectNoSessionIds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 8),
    _JuniRadiusInitiatedRequestDisconnectNoSessionIds_Type()
)
juniRadiusInitiatedRequestDisconnectNoSessionIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestDisconnectNoSessionIds.setStatus("current")
_JuniRadiusInitiatedRequestDisconnectBadAuthenticators_Type = Counter32
_JuniRadiusInitiatedRequestDisconnectBadAuthenticators_Object = MibTableColumn
juniRadiusInitiatedRequestDisconnectBadAuthenticators = _JuniRadiusInitiatedRequestDisconnectBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 9),
    _JuniRadiusInitiatedRequestDisconnectBadAuthenticators_Type()
)
juniRadiusInitiatedRequestDisconnectBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestDisconnectBadAuthenticators.setStatus("current")
_JuniRadiusInitiatedRequestDisconnectPacketsDropped_Type = Counter32
_JuniRadiusInitiatedRequestDisconnectPacketsDropped_Object = MibTableColumn
juniRadiusInitiatedRequestDisconnectPacketsDropped = _JuniRadiusInitiatedRequestDisconnectPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 10),
    _JuniRadiusInitiatedRequestDisconnectPacketsDropped_Type()
)
juniRadiusInitiatedRequestDisconnectPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestDisconnectPacketsDropped.setStatus("current")
_JuniRadiusInitiatedRequestCoaRequests_Type = Counter32
_JuniRadiusInitiatedRequestCoaRequests_Object = MibTableColumn
juniRadiusInitiatedRequestCoaRequests = _JuniRadiusInitiatedRequestCoaRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 11),
    _JuniRadiusInitiatedRequestCoaRequests_Type()
)
juniRadiusInitiatedRequestCoaRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCoaRequests.setStatus("current")
_JuniRadiusInitiatedRequestCoaAccepts_Type = Counter32
_JuniRadiusInitiatedRequestCoaAccepts_Object = MibTableColumn
juniRadiusInitiatedRequestCoaAccepts = _JuniRadiusInitiatedRequestCoaAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 12),
    _JuniRadiusInitiatedRequestCoaAccepts_Type()
)
juniRadiusInitiatedRequestCoaAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCoaAccepts.setStatus("current")
_JuniRadiusInitiatedRequestCoaRejects_Type = Counter32
_JuniRadiusInitiatedRequestCoaRejects_Object = MibTableColumn
juniRadiusInitiatedRequestCoaRejects = _JuniRadiusInitiatedRequestCoaRejects_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 13),
    _JuniRadiusInitiatedRequestCoaRejects_Type()
)
juniRadiusInitiatedRequestCoaRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCoaRejects.setStatus("current")
_JuniRadiusInitiatedRequestCoaNoSessionIds_Type = Counter32
_JuniRadiusInitiatedRequestCoaNoSessionIds_Object = MibTableColumn
juniRadiusInitiatedRequestCoaNoSessionIds = _JuniRadiusInitiatedRequestCoaNoSessionIds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 14),
    _JuniRadiusInitiatedRequestCoaNoSessionIds_Type()
)
juniRadiusInitiatedRequestCoaNoSessionIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCoaNoSessionIds.setStatus("current")
_JuniRadiusInitiatedRequestCoaBadAuthenticators_Type = Counter32
_JuniRadiusInitiatedRequestCoaBadAuthenticators_Object = MibTableColumn
juniRadiusInitiatedRequestCoaBadAuthenticators = _JuniRadiusInitiatedRequestCoaBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 15),
    _JuniRadiusInitiatedRequestCoaBadAuthenticators_Type()
)
juniRadiusInitiatedRequestCoaBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCoaBadAuthenticators.setStatus("current")
_JuniRadiusInitiatedRequestCoaPacketsDropped_Type = Counter32
_JuniRadiusInitiatedRequestCoaPacketsDropped_Object = MibTableColumn
juniRadiusInitiatedRequestCoaPacketsDropped = _JuniRadiusInitiatedRequestCoaPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 2, 1, 16),
    _JuniRadiusInitiatedRequestCoaPacketsDropped_Type()
)
juniRadiusInitiatedRequestCoaPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCoaPacketsDropped.setStatus("current")
_JuniRadiusInitiatedRequestCfgClientTable_Object = MibTable
juniRadiusInitiatedRequestCfgClientTable = _JuniRadiusInitiatedRequestCfgClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCfgClientTable.setStatus("current")
_JuniRadiusInitiatedRequestCfgClientEntry_Object = MibTableRow
juniRadiusInitiatedRequestCfgClientEntry = _JuniRadiusInitiatedRequestCfgClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 3, 1)
)
juniRadiusInitiatedRequestCfgClientEntry.setIndexNames(
    (0, "Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCfgClientAddress"),
)
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCfgClientEntry.setStatus("current")
_JuniRadiusInitiatedRequestCfgClientAddress_Type = IpAddress
_JuniRadiusInitiatedRequestCfgClientAddress_Object = MibTableColumn
juniRadiusInitiatedRequestCfgClientAddress = _JuniRadiusInitiatedRequestCfgClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 3, 1, 1),
    _JuniRadiusInitiatedRequestCfgClientAddress_Type()
)
juniRadiusInitiatedRequestCfgClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCfgClientAddress.setStatus("current")


class _JuniRadiusInitiatedRequestCfgClientPortNumber_Type(Integer32):
    """Custom type juniRadiusInitiatedRequestCfgClientPortNumber based on Integer32"""
    defaultValue = 3799

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniRadiusInitiatedRequestCfgClientPortNumber_Type.__name__ = "Integer32"
_JuniRadiusInitiatedRequestCfgClientPortNumber_Object = MibTableColumn
juniRadiusInitiatedRequestCfgClientPortNumber = _JuniRadiusInitiatedRequestCfgClientPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 3, 1, 2),
    _JuniRadiusInitiatedRequestCfgClientPortNumber_Type()
)
juniRadiusInitiatedRequestCfgClientPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCfgClientPortNumber.setStatus("current")


class _JuniRadiusInitiatedRequestCfgKey_Type(DisplayString):
    """Custom type juniRadiusInitiatedRequestCfgKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniRadiusInitiatedRequestCfgKey_Type.__name__ = "DisplayString"
_JuniRadiusInitiatedRequestCfgKey_Object = MibTableColumn
juniRadiusInitiatedRequestCfgKey = _JuniRadiusInitiatedRequestCfgKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 3, 1, 3),
    _JuniRadiusInitiatedRequestCfgKey_Type()
)
juniRadiusInitiatedRequestCfgKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCfgKey.setStatus("current")


class _JuniRadiusInitiatedRequestCfgDisconnect_Type(JuniEnable):
    """Custom type juniRadiusInitiatedRequestCfgDisconnect based on JuniEnable"""


_JuniRadiusInitiatedRequestCfgDisconnect_Object = MibTableColumn
juniRadiusInitiatedRequestCfgDisconnect = _JuniRadiusInitiatedRequestCfgDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 3, 1, 4),
    _JuniRadiusInitiatedRequestCfgDisconnect_Type()
)
juniRadiusInitiatedRequestCfgDisconnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCfgDisconnect.setStatus("current")


class _JuniRadiusInitiatedRequestCfgChangeOfAuthorization_Type(JuniEnable):
    """Custom type juniRadiusInitiatedRequestCfgChangeOfAuthorization based on JuniEnable"""


_JuniRadiusInitiatedRequestCfgChangeOfAuthorization_Object = MibTableColumn
juniRadiusInitiatedRequestCfgChangeOfAuthorization = _JuniRadiusInitiatedRequestCfgChangeOfAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 3, 1, 5),
    _JuniRadiusInitiatedRequestCfgChangeOfAuthorization_Type()
)
juniRadiusInitiatedRequestCfgChangeOfAuthorization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCfgChangeOfAuthorization.setStatus("current")
_JuniRadiusInitiatedRequestCfgRowStatus_Type = RowStatus
_JuniRadiusInitiatedRequestCfgRowStatus_Object = MibTableColumn
juniRadiusInitiatedRequestCfgRowStatus = _JuniRadiusInitiatedRequestCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 1, 1, 3, 1, 6),
    _JuniRadiusInitiatedRequestCfgRowStatus_Type()
)
juniRadiusInitiatedRequestCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestCfgRowStatus.setStatus("current")
_JuniRadiusInitiatedRequestMIBConformance_ObjectIdentity = ObjectIdentity
juniRadiusInitiatedRequestMIBConformance = _JuniRadiusInitiatedRequestMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 2)
)
_JuniRadiusInitiatedRequestMIBCompliances_ObjectIdentity = ObjectIdentity
juniRadiusInitiatedRequestMIBCompliances = _JuniRadiusInitiatedRequestMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 2, 1)
)
_JuniRadiusInitiatedRequestMIBGroups_ObjectIdentity = ObjectIdentity
juniRadiusInitiatedRequestMIBGroups = _JuniRadiusInitiatedRequestMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 2, 2)
)

# Managed Objects groups

juniRadiusInitiatedRequestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 2, 2, 1)
)
juniRadiusInitiatedRequestGroup.setObjects(
      *(("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestInvalidClientAddresses"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestClientPortNumber"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestUnknownTypes"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestNoSecret"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestDisconnectRequests"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestDisconnectAccepts"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestDisconnectRejects"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestDisconnectNoSessionIds"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestDisconnectBadAuthenticators"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestDisconnectPacketsDropped"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCoaRequests"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCoaAccepts"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCoaRejects"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCoaNoSessionIds"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCoaBadAuthenticators"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCoaPacketsDropped"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCfgClientPortNumber"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCfgKey"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCfgDisconnect"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCfgChangeOfAuthorization"),
        ("Juniper-RADIUS-Initiated-Request-MIB", "juniRadiusInitiatedRequestCfgRowStatus"))
)
if mibBuilder.loadTexts:
    juniRadiusInitiatedRequestGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniRadiusAuthInitiatedRequestCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniRadiusAuthInitiatedRequestCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-RADIUS-Initiated-Request-MIB",
    **{"juniRadiusInitiatedRequestMIB": juniRadiusInitiatedRequestMIB,
       "juniRadiusInitiatedRequestObjects": juniRadiusInitiatedRequestObjects,
       "juniRadiusInitiatedRequest": juniRadiusInitiatedRequest,
       "juniRadiusInitiatedRequestInvalidClientAddresses": juniRadiusInitiatedRequestInvalidClientAddresses,
       "juniRadiusInitiatedRequestClientTable": juniRadiusInitiatedRequestClientTable,
       "juniRadiusInitiatedRequestClientEntry": juniRadiusInitiatedRequestClientEntry,
       "juniRadiusInitiatedRequestClientAddress": juniRadiusInitiatedRequestClientAddress,
       "juniRadiusInitiatedRequestClientPortNumber": juniRadiusInitiatedRequestClientPortNumber,
       "juniRadiusInitiatedRequestUnknownTypes": juniRadiusInitiatedRequestUnknownTypes,
       "juniRadiusInitiatedRequestNoSecret": juniRadiusInitiatedRequestNoSecret,
       "juniRadiusInitiatedRequestDisconnectRequests": juniRadiusInitiatedRequestDisconnectRequests,
       "juniRadiusInitiatedRequestDisconnectAccepts": juniRadiusInitiatedRequestDisconnectAccepts,
       "juniRadiusInitiatedRequestDisconnectRejects": juniRadiusInitiatedRequestDisconnectRejects,
       "juniRadiusInitiatedRequestDisconnectNoSessionIds": juniRadiusInitiatedRequestDisconnectNoSessionIds,
       "juniRadiusInitiatedRequestDisconnectBadAuthenticators": juniRadiusInitiatedRequestDisconnectBadAuthenticators,
       "juniRadiusInitiatedRequestDisconnectPacketsDropped": juniRadiusInitiatedRequestDisconnectPacketsDropped,
       "juniRadiusInitiatedRequestCoaRequests": juniRadiusInitiatedRequestCoaRequests,
       "juniRadiusInitiatedRequestCoaAccepts": juniRadiusInitiatedRequestCoaAccepts,
       "juniRadiusInitiatedRequestCoaRejects": juniRadiusInitiatedRequestCoaRejects,
       "juniRadiusInitiatedRequestCoaNoSessionIds": juniRadiusInitiatedRequestCoaNoSessionIds,
       "juniRadiusInitiatedRequestCoaBadAuthenticators": juniRadiusInitiatedRequestCoaBadAuthenticators,
       "juniRadiusInitiatedRequestCoaPacketsDropped": juniRadiusInitiatedRequestCoaPacketsDropped,
       "juniRadiusInitiatedRequestCfgClientTable": juniRadiusInitiatedRequestCfgClientTable,
       "juniRadiusInitiatedRequestCfgClientEntry": juniRadiusInitiatedRequestCfgClientEntry,
       "juniRadiusInitiatedRequestCfgClientAddress": juniRadiusInitiatedRequestCfgClientAddress,
       "juniRadiusInitiatedRequestCfgClientPortNumber": juniRadiusInitiatedRequestCfgClientPortNumber,
       "juniRadiusInitiatedRequestCfgKey": juniRadiusInitiatedRequestCfgKey,
       "juniRadiusInitiatedRequestCfgDisconnect": juniRadiusInitiatedRequestCfgDisconnect,
       "juniRadiusInitiatedRequestCfgChangeOfAuthorization": juniRadiusInitiatedRequestCfgChangeOfAuthorization,
       "juniRadiusInitiatedRequestCfgRowStatus": juniRadiusInitiatedRequestCfgRowStatus,
       "juniRadiusInitiatedRequestMIBConformance": juniRadiusInitiatedRequestMIBConformance,
       "juniRadiusInitiatedRequestMIBCompliances": juniRadiusInitiatedRequestMIBCompliances,
       "juniRadiusAuthInitiatedRequestCompliance": juniRadiusAuthInitiatedRequestCompliance,
       "juniRadiusInitiatedRequestMIBGroups": juniRadiusInitiatedRequestMIBGroups,
       "juniRadiusInitiatedRequestGroup": juniRadiusInitiatedRequestGroup}
)
