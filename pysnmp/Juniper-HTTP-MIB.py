# SNMP MIB module (Juniper-HTTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-HTTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:23 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

juniHttpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78)
)
juniHttpMIB.setRevisions(
        ("2005-08-22 15:51",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniHttpObjects_ObjectIdentity = ObjectIdentity
juniHttpObjects = _JuniHttpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1)
)
_JuniHttpDaemon_ObjectIdentity = ObjectIdentity
juniHttpDaemon = _JuniHttpDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 1)
)
_JuniHttpDaemonRowStatus_Type = RowStatus
_JuniHttpDaemonRowStatus_Object = MibScalar
juniHttpDaemonRowStatus = _JuniHttpDaemonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 1, 1),
    _JuniHttpDaemonRowStatus_Type()
)
juniHttpDaemonRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHttpDaemonRowStatus.setStatus("current")


class _JuniHttpDaemonAccessListName_Type(DisplayString):
    """Custom type juniHttpDaemonAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniHttpDaemonAccessListName_Type.__name__ = "DisplayString"
_JuniHttpDaemonAccessListName_Object = MibScalar
juniHttpDaemonAccessListName = _JuniHttpDaemonAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 1, 2),
    _JuniHttpDaemonAccessListName_Type()
)
juniHttpDaemonAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniHttpDaemonAccessListName.setStatus("current")


class _JuniHttpDaemonPort_Type(Integer32):
    """Custom type juniHttpDaemonPort based on Integer32"""
    defaultValue = 80


_JuniHttpDaemonPort_Object = MibScalar
juniHttpDaemonPort = _JuniHttpDaemonPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 1, 3),
    _JuniHttpDaemonPort_Type()
)
juniHttpDaemonPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniHttpDaemonPort.setStatus("current")


class _JuniHttpDaemonSameAddressLimit_Type(Unsigned32):
    """Custom type juniHttpDaemonSameAddressLimit based on Unsigned32"""
    defaultValue = 10


_JuniHttpDaemonSameAddressLimit_Object = MibScalar
juniHttpDaemonSameAddressLimit = _JuniHttpDaemonSameAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 1, 4),
    _JuniHttpDaemonSameAddressLimit_Type()
)
juniHttpDaemonSameAddressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniHttpDaemonSameAddressLimit.setStatus("current")
_JuniHttpDaemonStats_ObjectIdentity = ObjectIdentity
juniHttpDaemonStats = _JuniHttpDaemonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2)
)
_JuniHttpDaemonStatsEnabled_Type = Counter32
_JuniHttpDaemonStatsEnabled_Object = MibScalar
juniHttpDaemonStatsEnabled = _JuniHttpDaemonStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 1),
    _JuniHttpDaemonStatsEnabled_Type()
)
juniHttpDaemonStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsEnabled.setStatus("current")
_JuniHttpDaemonStatsDisabled_Type = Counter32
_JuniHttpDaemonStatsDisabled_Object = MibScalar
juniHttpDaemonStatsDisabled = _JuniHttpDaemonStatsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 2),
    _JuniHttpDaemonStatsDisabled_Type()
)
juniHttpDaemonStatsDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsDisabled.setStatus("current")
_JuniHttpDaemonStatsSameHost_Type = Counter32
_JuniHttpDaemonStatsSameHost_Object = MibScalar
juniHttpDaemonStatsSameHost = _JuniHttpDaemonStatsSameHost_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 3),
    _JuniHttpDaemonStatsSameHost_Type()
)
juniHttpDaemonStatsSameHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsSameHost.setStatus("current")
_JuniHttpDaemonStatsAccDeny_Type = Counter32
_JuniHttpDaemonStatsAccDeny_Object = MibScalar
juniHttpDaemonStatsAccDeny = _JuniHttpDaemonStatsAccDeny_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 4),
    _JuniHttpDaemonStatsAccDeny_Type()
)
juniHttpDaemonStatsAccDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsAccDeny.setStatus("current")
_JuniHttpDaemonStatsNoResource_Type = Counter32
_JuniHttpDaemonStatsNoResource_Object = MibScalar
juniHttpDaemonStatsNoResource = _JuniHttpDaemonStatsNoResource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 5),
    _JuniHttpDaemonStatsNoResource_Type()
)
juniHttpDaemonStatsNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsNoResource.setStatus("current")
_JuniHttpDaemonStatsCreate_Type = Counter32
_JuniHttpDaemonStatsCreate_Object = MibScalar
juniHttpDaemonStatsCreate = _JuniHttpDaemonStatsCreate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 6),
    _JuniHttpDaemonStatsCreate_Type()
)
juniHttpDaemonStatsCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsCreate.setStatus("current")
_JuniHttpDaemonStatsRemove_Type = Counter32
_JuniHttpDaemonStatsRemove_Object = MibScalar
juniHttpDaemonStatsRemove = _JuniHttpDaemonStatsRemove_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 7),
    _JuniHttpDaemonStatsRemove_Type()
)
juniHttpDaemonStatsRemove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsRemove.setStatus("current")
_JuniHttpDaemonStatsAged_Type = Counter32
_JuniHttpDaemonStatsAged_Object = MibScalar
juniHttpDaemonStatsAged = _JuniHttpDaemonStatsAged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 8),
    _JuniHttpDaemonStatsAged_Type()
)
juniHttpDaemonStatsAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsAged.setStatus("current")
_JuniHttpDaemonStatsServed_Type = Counter32
_JuniHttpDaemonStatsServed_Object = MibScalar
juniHttpDaemonStatsServed = _JuniHttpDaemonStatsServed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 9),
    _JuniHttpDaemonStatsServed_Type()
)
juniHttpDaemonStatsServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsServed.setStatus("current")
_JuniHttpDaemonStatsHtmlError_Type = Counter32
_JuniHttpDaemonStatsHtmlError_Object = MibScalar
juniHttpDaemonStatsHtmlError = _JuniHttpDaemonStatsHtmlError_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 10),
    _JuniHttpDaemonStatsHtmlError_Type()
)
juniHttpDaemonStatsHtmlError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsHtmlError.setStatus("current")
_JuniHttpDaemonStatsUnknownUrl_Type = Counter32
_JuniHttpDaemonStatsUnknownUrl_Object = MibScalar
juniHttpDaemonStatsUnknownUrl = _JuniHttpDaemonStatsUnknownUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 2, 11),
    _JuniHttpDaemonStatsUnknownUrl_Type()
)
juniHttpDaemonStatsUnknownUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHttpDaemonStatsUnknownUrl.setStatus("current")
_JuniHttpInterfaces_ObjectIdentity = ObjectIdentity
juniHttpInterfaces = _JuniHttpInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 3)
)
_JuniHttpInterfaceTable_Object = MibTable
juniHttpInterfaceTable = _JuniHttpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniHttpInterfaceTable.setStatus("current")
_JuniHttpInterfaceEntry_Object = MibTableRow
juniHttpInterfaceEntry = _JuniHttpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 3, 1, 1)
)
juniHttpInterfaceEntry.setIndexNames(
    (0, "Juniper-HTTP-MIB", "juniHttpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    juniHttpInterfaceEntry.setStatus("current")
_JuniHttpInterfaceIndex_Type = InterfaceIndex
_JuniHttpInterfaceIndex_Object = MibTableColumn
juniHttpInterfaceIndex = _JuniHttpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 3, 1, 1, 1),
    _JuniHttpInterfaceIndex_Type()
)
juniHttpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniHttpInterfaceIndex.setStatus("current")
_JuniHttpInterfaceRowStatus_Type = RowStatus
_JuniHttpInterfaceRowStatus_Object = MibTableColumn
juniHttpInterfaceRowStatus = _JuniHttpInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 3, 1, 1, 2),
    _JuniHttpInterfaceRowStatus_Type()
)
juniHttpInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHttpInterfaceRowStatus.setStatus("current")


class _JuniHttpInterfaceRedirectUrl_Type(DisplayString):
    """Custom type juniHttpInterfaceRedirectUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniHttpInterfaceRedirectUrl_Type.__name__ = "DisplayString"
_JuniHttpInterfaceRedirectUrl_Object = MibTableColumn
juniHttpInterfaceRedirectUrl = _JuniHttpInterfaceRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 1, 3, 1, 1, 3),
    _JuniHttpInterfaceRedirectUrl_Type()
)
juniHttpInterfaceRedirectUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniHttpInterfaceRedirectUrl.setStatus("current")
_JuniHttpConformance_ObjectIdentity = ObjectIdentity
juniHttpConformance = _JuniHttpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 4)
)
_JuniHttpCompliances_ObjectIdentity = ObjectIdentity
juniHttpCompliances = _JuniHttpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 4, 1)
)
_JuniHttpGroups_ObjectIdentity = ObjectIdentity
juniHttpGroups = _JuniHttpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 4, 2)
)

# Managed Objects groups

juniHttpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 4, 2, 1)
)
juniHttpGroup.setObjects(
      *(("Juniper-HTTP-MIB", "juniHttpDaemonRowStatus"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonAccessListName"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonPort"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonSameAddressLimit"))
)
if mibBuilder.loadTexts:
    juniHttpGroup.setStatus("current")

juniHttpDaemonStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 4, 2, 2)
)
juniHttpDaemonStatsGroup.setObjects(
      *(("Juniper-HTTP-MIB", "juniHttpDaemonStatsEnabled"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsDisabled"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsSameHost"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsAccDeny"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsNoResource"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsCreate"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsRemove"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsAged"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsServed"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsHtmlError"),
        ("Juniper-HTTP-MIB", "juniHttpDaemonStatsUnknownUrl"))
)
if mibBuilder.loadTexts:
    juniHttpDaemonStatsGroup.setStatus("current")

juniHttpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 4, 2, 3)
)
juniHttpInterfaceGroup.setObjects(
      *(("Juniper-HTTP-MIB", "juniHttpInterfaceRowStatus"),
        ("Juniper-HTTP-MIB", "juniHttpInterfaceRedirectUrl"))
)
if mibBuilder.loadTexts:
    juniHttpInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniHttpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniHttpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-HTTP-MIB",
    **{"juniHttpMIB": juniHttpMIB,
       "juniHttpObjects": juniHttpObjects,
       "juniHttpDaemon": juniHttpDaemon,
       "juniHttpDaemonRowStatus": juniHttpDaemonRowStatus,
       "juniHttpDaemonAccessListName": juniHttpDaemonAccessListName,
       "juniHttpDaemonPort": juniHttpDaemonPort,
       "juniHttpDaemonSameAddressLimit": juniHttpDaemonSameAddressLimit,
       "juniHttpDaemonStats": juniHttpDaemonStats,
       "juniHttpDaemonStatsEnabled": juniHttpDaemonStatsEnabled,
       "juniHttpDaemonStatsDisabled": juniHttpDaemonStatsDisabled,
       "juniHttpDaemonStatsSameHost": juniHttpDaemonStatsSameHost,
       "juniHttpDaemonStatsAccDeny": juniHttpDaemonStatsAccDeny,
       "juniHttpDaemonStatsNoResource": juniHttpDaemonStatsNoResource,
       "juniHttpDaemonStatsCreate": juniHttpDaemonStatsCreate,
       "juniHttpDaemonStatsRemove": juniHttpDaemonStatsRemove,
       "juniHttpDaemonStatsAged": juniHttpDaemonStatsAged,
       "juniHttpDaemonStatsServed": juniHttpDaemonStatsServed,
       "juniHttpDaemonStatsHtmlError": juniHttpDaemonStatsHtmlError,
       "juniHttpDaemonStatsUnknownUrl": juniHttpDaemonStatsUnknownUrl,
       "juniHttpInterfaces": juniHttpInterfaces,
       "juniHttpInterfaceTable": juniHttpInterfaceTable,
       "juniHttpInterfaceEntry": juniHttpInterfaceEntry,
       "juniHttpInterfaceIndex": juniHttpInterfaceIndex,
       "juniHttpInterfaceRowStatus": juniHttpInterfaceRowStatus,
       "juniHttpInterfaceRedirectUrl": juniHttpInterfaceRedirectUrl,
       "juniHttpConformance": juniHttpConformance,
       "juniHttpCompliances": juniHttpCompliances,
       "juniHttpCompliance": juniHttpCompliance,
       "juniHttpGroups": juniHttpGroups,
       "juniHttpGroup": juniHttpGroup,
       "juniHttpDaemonStatsGroup": juniHttpDaemonStatsGroup,
       "juniHttpInterfaceGroup": juniHttpInterfaceGroup}
)
