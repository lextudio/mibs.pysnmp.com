# SNMP MIB module (Juniper-RADIUS-Disconnect-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-RADIUS-Disconnect-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:10 2024
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

juniRadiusDisconnectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67)
)
juniRadiusDisconnectMIB.setRevisions(
        ("2004-06-09 13:57",
         "2003-01-13 20:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniRadiusDisconnectObjects_ObjectIdentity = ObjectIdentity
juniRadiusDisconnectObjects = _JuniRadiusDisconnectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1)
)
_JuniRadiusDisconnect_ObjectIdentity = ObjectIdentity
juniRadiusDisconnect = _JuniRadiusDisconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1)
)
_JuniRadiusDisconnectInvalidClientAddresses_Type = Counter32
_JuniRadiusDisconnectInvalidClientAddresses_Object = MibScalar
juniRadiusDisconnectInvalidClientAddresses = _JuniRadiusDisconnectInvalidClientAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 1),
    _JuniRadiusDisconnectInvalidClientAddresses_Type()
)
juniRadiusDisconnectInvalidClientAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectInvalidClientAddresses.setStatus("obsolete")
_JuniRadiusDisconnectClientTable_Object = MibTable
juniRadiusDisconnectClientTable = _JuniRadiusDisconnectClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniRadiusDisconnectClientTable.setStatus("obsolete")
_JuniRadiusDisconnectClientEntry_Object = MibTableRow
juniRadiusDisconnectClientEntry = _JuniRadiusDisconnectClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1)
)
juniRadiusDisconnectClientEntry.setIndexNames(
    (0, "Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectClientAddress"),
)
if mibBuilder.loadTexts:
    juniRadiusDisconnectClientEntry.setStatus("obsolete")
_JuniRadiusDisconnectClientAddress_Type = IpAddress
_JuniRadiusDisconnectClientAddress_Object = MibTableColumn
juniRadiusDisconnectClientAddress = _JuniRadiusDisconnectClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 1),
    _JuniRadiusDisconnectClientAddress_Type()
)
juniRadiusDisconnectClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusDisconnectClientAddress.setStatus("obsolete")
_JuniRadiusDisconnectClientPortNumber_Type = Integer32
_JuniRadiusDisconnectClientPortNumber_Object = MibTableColumn
juniRadiusDisconnectClientPortNumber = _JuniRadiusDisconnectClientPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 2),
    _JuniRadiusDisconnectClientPortNumber_Type()
)
juniRadiusDisconnectClientPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectClientPortNumber.setStatus("obsolete")
_JuniRadiusDisconnectRequests_Type = Counter32
_JuniRadiusDisconnectRequests_Object = MibTableColumn
juniRadiusDisconnectRequests = _JuniRadiusDisconnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 3),
    _JuniRadiusDisconnectRequests_Type()
)
juniRadiusDisconnectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectRequests.setStatus("obsolete")
_JuniRadiusDisconnectAccepts_Type = Counter32
_JuniRadiusDisconnectAccepts_Object = MibTableColumn
juniRadiusDisconnectAccepts = _JuniRadiusDisconnectAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 4),
    _JuniRadiusDisconnectAccepts_Type()
)
juniRadiusDisconnectAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectAccepts.setStatus("obsolete")
_JuniRadiusDisconnectRejects_Type = Counter32
_JuniRadiusDisconnectRejects_Object = MibTableColumn
juniRadiusDisconnectRejects = _JuniRadiusDisconnectRejects_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 5),
    _JuniRadiusDisconnectRejects_Type()
)
juniRadiusDisconnectRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectRejects.setStatus("obsolete")
_JuniRadiusDisconnectNoSecret_Type = Counter32
_JuniRadiusDisconnectNoSecret_Object = MibTableColumn
juniRadiusDisconnectNoSecret = _JuniRadiusDisconnectNoSecret_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 6),
    _JuniRadiusDisconnectNoSecret_Type()
)
juniRadiusDisconnectNoSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectNoSecret.setStatus("obsolete")
_JuniRadiusDisconnectNoSessionIds_Type = Counter32
_JuniRadiusDisconnectNoSessionIds_Object = MibTableColumn
juniRadiusDisconnectNoSessionIds = _JuniRadiusDisconnectNoSessionIds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 7),
    _JuniRadiusDisconnectNoSessionIds_Type()
)
juniRadiusDisconnectNoSessionIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectNoSessionIds.setStatus("obsolete")
_JuniRadiusDisconnectBadAuthenticators_Type = Counter32
_JuniRadiusDisconnectBadAuthenticators_Object = MibTableColumn
juniRadiusDisconnectBadAuthenticators = _JuniRadiusDisconnectBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 8),
    _JuniRadiusDisconnectBadAuthenticators_Type()
)
juniRadiusDisconnectBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectBadAuthenticators.setStatus("obsolete")
_JuniRadiusDisconnectUnknownTypes_Type = Counter32
_JuniRadiusDisconnectUnknownTypes_Object = MibTableColumn
juniRadiusDisconnectUnknownTypes = _JuniRadiusDisconnectUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 9),
    _JuniRadiusDisconnectUnknownTypes_Type()
)
juniRadiusDisconnectUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectUnknownTypes.setStatus("obsolete")
_JuniRadiusDisconnectPacketsDropped_Type = Counter32
_JuniRadiusDisconnectPacketsDropped_Object = MibTableColumn
juniRadiusDisconnectPacketsDropped = _JuniRadiusDisconnectPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 2, 1, 10),
    _JuniRadiusDisconnectPacketsDropped_Type()
)
juniRadiusDisconnectPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusDisconnectPacketsDropped.setStatus("obsolete")
_JuniRadiusDisconnectCfgClientTable_Object = MibTable
juniRadiusDisconnectCfgClientTable = _JuniRadiusDisconnectCfgClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniRadiusDisconnectCfgClientTable.setStatus("obsolete")
_JuniRadiusDisconnectCfgClientEntry_Object = MibTableRow
juniRadiusDisconnectCfgClientEntry = _JuniRadiusDisconnectCfgClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 3, 1)
)
juniRadiusDisconnectCfgClientEntry.setIndexNames(
    (0, "Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectCfgClientAddress"),
)
if mibBuilder.loadTexts:
    juniRadiusDisconnectCfgClientEntry.setStatus("obsolete")
_JuniRadiusDisconnectCfgClientAddress_Type = IpAddress
_JuniRadiusDisconnectCfgClientAddress_Object = MibTableColumn
juniRadiusDisconnectCfgClientAddress = _JuniRadiusDisconnectCfgClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 3, 1, 1),
    _JuniRadiusDisconnectCfgClientAddress_Type()
)
juniRadiusDisconnectCfgClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusDisconnectCfgClientAddress.setStatus("obsolete")


class _JuniRadiusDisconnectCfgClientPortNumber_Type(Integer32):
    """Custom type juniRadiusDisconnectCfgClientPortNumber based on Integer32"""
    defaultValue = 1700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniRadiusDisconnectCfgClientPortNumber_Type.__name__ = "Integer32"
_JuniRadiusDisconnectCfgClientPortNumber_Object = MibTableColumn
juniRadiusDisconnectCfgClientPortNumber = _JuniRadiusDisconnectCfgClientPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 3, 1, 2),
    _JuniRadiusDisconnectCfgClientPortNumber_Type()
)
juniRadiusDisconnectCfgClientPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusDisconnectCfgClientPortNumber.setStatus("obsolete")


class _JuniRadiusDisconnectCfgKey_Type(DisplayString):
    """Custom type juniRadiusDisconnectCfgKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniRadiusDisconnectCfgKey_Type.__name__ = "DisplayString"
_JuniRadiusDisconnectCfgKey_Object = MibTableColumn
juniRadiusDisconnectCfgKey = _JuniRadiusDisconnectCfgKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 3, 1, 3),
    _JuniRadiusDisconnectCfgKey_Type()
)
juniRadiusDisconnectCfgKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusDisconnectCfgKey.setStatus("obsolete")
_JuniRadiusDisconnectCfgRowStatus_Type = RowStatus
_JuniRadiusDisconnectCfgRowStatus_Object = MibTableColumn
juniRadiusDisconnectCfgRowStatus = _JuniRadiusDisconnectCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 1, 1, 3, 1, 4),
    _JuniRadiusDisconnectCfgRowStatus_Type()
)
juniRadiusDisconnectCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusDisconnectCfgRowStatus.setStatus("obsolete")
_JuniRadiusDisconnectMIBConformance_ObjectIdentity = ObjectIdentity
juniRadiusDisconnectMIBConformance = _JuniRadiusDisconnectMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 2)
)
_JuniRadiusDisconnectMIBCompliances_ObjectIdentity = ObjectIdentity
juniRadiusDisconnectMIBCompliances = _JuniRadiusDisconnectMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 2, 1)
)
_JuniRadiusDisconnectMIBGroups_ObjectIdentity = ObjectIdentity
juniRadiusDisconnectMIBGroups = _JuniRadiusDisconnectMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 2, 2)
)

# Managed Objects groups

juniRadiusDisconnectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 2, 2, 1)
)
juniRadiusDisconnectGroup.setObjects(
      *(("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectInvalidClientAddresses"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectClientPortNumber"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectRequests"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectAccepts"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectRejects"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectNoSecret"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectNoSessionIds"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectBadAuthenticators"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectUnknownTypes"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectPacketsDropped"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectCfgClientPortNumber"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectCfgKey"),
        ("Juniper-RADIUS-Disconnect-MIB", "juniRadiusDisconnectCfgRowStatus"))
)
if mibBuilder.loadTexts:
    juniRadiusDisconnectGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniRadiusAuthDisconnectCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniRadiusAuthDisconnectCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-RADIUS-Disconnect-MIB",
    **{"juniRadiusDisconnectMIB": juniRadiusDisconnectMIB,
       "juniRadiusDisconnectObjects": juniRadiusDisconnectObjects,
       "juniRadiusDisconnect": juniRadiusDisconnect,
       "juniRadiusDisconnectInvalidClientAddresses": juniRadiusDisconnectInvalidClientAddresses,
       "juniRadiusDisconnectClientTable": juniRadiusDisconnectClientTable,
       "juniRadiusDisconnectClientEntry": juniRadiusDisconnectClientEntry,
       "juniRadiusDisconnectClientAddress": juniRadiusDisconnectClientAddress,
       "juniRadiusDisconnectClientPortNumber": juniRadiusDisconnectClientPortNumber,
       "juniRadiusDisconnectRequests": juniRadiusDisconnectRequests,
       "juniRadiusDisconnectAccepts": juniRadiusDisconnectAccepts,
       "juniRadiusDisconnectRejects": juniRadiusDisconnectRejects,
       "juniRadiusDisconnectNoSecret": juniRadiusDisconnectNoSecret,
       "juniRadiusDisconnectNoSessionIds": juniRadiusDisconnectNoSessionIds,
       "juniRadiusDisconnectBadAuthenticators": juniRadiusDisconnectBadAuthenticators,
       "juniRadiusDisconnectUnknownTypes": juniRadiusDisconnectUnknownTypes,
       "juniRadiusDisconnectPacketsDropped": juniRadiusDisconnectPacketsDropped,
       "juniRadiusDisconnectCfgClientTable": juniRadiusDisconnectCfgClientTable,
       "juniRadiusDisconnectCfgClientEntry": juniRadiusDisconnectCfgClientEntry,
       "juniRadiusDisconnectCfgClientAddress": juniRadiusDisconnectCfgClientAddress,
       "juniRadiusDisconnectCfgClientPortNumber": juniRadiusDisconnectCfgClientPortNumber,
       "juniRadiusDisconnectCfgKey": juniRadiusDisconnectCfgKey,
       "juniRadiusDisconnectCfgRowStatus": juniRadiusDisconnectCfgRowStatus,
       "juniRadiusDisconnectMIBConformance": juniRadiusDisconnectMIBConformance,
       "juniRadiusDisconnectMIBCompliances": juniRadiusDisconnectMIBCompliances,
       "juniRadiusAuthDisconnectCompliance": juniRadiusAuthDisconnectCompliance,
       "juniRadiusDisconnectMIBGroups": juniRadiusDisconnectMIBGroups,
       "juniRadiusDisconnectGroup": juniRadiusDisconnectGroup}
)
