# SNMP MIB module (ALTIGA-SDI-ACE-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-SDI-ACE-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:20 2024
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

(alACEServerMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alACEServerMibModule")

(alACEServerGroup,
 alACEServerStats) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alACEServerGroup",
    "alACEServerStats")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

altigaACEStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 50, 1)
)
altigaACEStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaACEStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaACEStatsMibConformance = _AltigaACEStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 50, 1, 1)
)
_AltigaACEStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaACEStatsMibCompliances = _AltigaACEStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 50, 1, 1, 1)
)
_AlCfgACEGlobal_ObjectIdentity = ObjectIdentity
alCfgACEGlobal = _AlCfgACEGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 1)
)
_AlACEServerTable_Object = MibTable
alACEServerTable = _AlACEServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2)
)
if mibBuilder.loadTexts:
    alACEServerTable.setStatus("current")
_AlACEServerEntry_Object = MibTableRow
alACEServerEntry = _AlACEServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1)
)
alACEServerEntry.setIndexNames(
    (0, "ALTIGA-SDI-ACE-STATS-MIB", "alACEPrimaryIndex"),
    (0, "ALTIGA-SDI-ACE-STATS-MIB", "alACEServerIndex"),
)
if mibBuilder.loadTexts:
    alACEServerEntry.setStatus("current")
_AlACEPrimaryIndex_Type = Integer32
_AlACEPrimaryIndex_Object = MibTableColumn
alACEPrimaryIndex = _AlACEPrimaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 1),
    _AlACEPrimaryIndex_Type()
)
alACEPrimaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEPrimaryIndex.setStatus("current")


class _AlACEServerIndex_Type(Integer32):
    """Custom type alACEServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AlACEServerIndex_Type.__name__ = "Integer32"
_AlACEServerIndex_Object = MibTableColumn
alACEServerIndex = _AlACEServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 2),
    _AlACEServerIndex_Type()
)
alACEServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerIndex.setStatus("current")


class _AlACEServerPriority_Type(Integer32):
    """Custom type alACEServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AlACEServerPriority_Type.__name__ = "Integer32"
_AlACEServerPriority_Object = MibTableColumn
alACEServerPriority = _AlACEServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 3),
    _AlACEServerPriority_Type()
)
alACEServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerPriority.setStatus("current")
_AlACEServerAddress_Type = IpAddress
_AlACEServerAddress_Object = MibTableColumn
alACEServerAddress = _AlACEServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 4),
    _AlACEServerAddress_Type()
)
alACEServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerAddress.setStatus("current")


class _AlACEServerPort_Type(Integer32):
    """Custom type alACEServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlACEServerPort_Type.__name__ = "Integer32"
_AlACEServerPort_Object = MibTableColumn
alACEServerPort = _AlACEServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 5),
    _AlACEServerPort_Type()
)
alACEServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerPort.setStatus("current")
_AlACEServerRetries_Type = Counter32
_AlACEServerRetries_Object = MibTableColumn
alACEServerRetries = _AlACEServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 6),
    _AlACEServerRetries_Type()
)
alACEServerRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerRetries.setStatus("current")
_AlACEServerTimeout_Type = Counter32
_AlACEServerTimeout_Object = MibTableColumn
alACEServerTimeout = _AlACEServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 7),
    _AlACEServerTimeout_Type()
)
alACEServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerTimeout.setStatus("current")
_AlACEServerGroupId_Type = Gauge32
_AlACEServerGroupId_Object = MibTableColumn
alACEServerGroupId = _AlACEServerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 8),
    _AlACEServerGroupId_Type()
)
alACEServerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerGroupId.setStatus("current")
_AlACEServerAuthSuccesses_Type = Counter32
_AlACEServerAuthSuccesses_Object = MibTableColumn
alACEServerAuthSuccesses = _AlACEServerAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 9),
    _AlACEServerAuthSuccesses_Type()
)
alACEServerAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerAuthSuccesses.setStatus("current")
_AlACEServerAuthFailures_Type = Counter32
_AlACEServerAuthFailures_Object = MibTableColumn
alACEServerAuthFailures = _AlACEServerAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 10),
    _AlACEServerAuthFailures_Type()
)
alACEServerAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerAuthFailures.setStatus("current")
_AlACEServerBadCodeSent_Type = Counter32
_AlACEServerBadCodeSent_Object = MibTableColumn
alACEServerBadCodeSent = _AlACEServerBadCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 11),
    _AlACEServerBadCodeSent_Type()
)
alACEServerBadCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerBadCodeSent.setStatus("current")
_AlACEServerBadPinSent_Type = Counter32
_AlACEServerBadPinSent_Object = MibTableColumn
alACEServerBadPinSent = _AlACEServerBadPinSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 45, 2, 1, 12),
    _AlACEServerBadPinSent_Type()
)
alACEServerBadPinSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alACEServerBadPinSent.setStatus("current")

# Managed Objects groups

altigaACEServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 45, 1)
)
altigaACEServerGroup.setObjects(
      *(("ALTIGA-SDI-ACE-STATS-MIB", "alACEPrimaryIndex"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerIndex"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerPriority"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerAddress"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerPort"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerRetries"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerTimeout"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerGroupId"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerAuthSuccesses"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerAuthFailures"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerBadCodeSent"),
        ("ALTIGA-SDI-ACE-STATS-MIB", "alACEServerBadPinSent"))
)
if mibBuilder.loadTexts:
    altigaACEServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaACEStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 50, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaACEStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-SDI-ACE-STATS-MIB",
    **{"altigaACEStatsMibModule": altigaACEStatsMibModule,
       "altigaACEStatsMibConformance": altigaACEStatsMibConformance,
       "altigaACEStatsMibCompliances": altigaACEStatsMibCompliances,
       "altigaACEStatsMibCompliance": altigaACEStatsMibCompliance,
       "altigaACEServerGroup": altigaACEServerGroup,
       "alCfgACEGlobal": alCfgACEGlobal,
       "alACEServerTable": alACEServerTable,
       "alACEServerEntry": alACEServerEntry,
       "alACEPrimaryIndex": alACEPrimaryIndex,
       "alACEServerIndex": alACEServerIndex,
       "alACEServerPriority": alACEServerPriority,
       "alACEServerAddress": alACEServerAddress,
       "alACEServerPort": alACEServerPort,
       "alACEServerRetries": alACEServerRetries,
       "alACEServerTimeout": alACEServerTimeout,
       "alACEServerGroupId": alACEServerGroupId,
       "alACEServerAuthSuccesses": alACEServerAuthSuccesses,
       "alACEServerAuthFailures": alACEServerAuthFailures,
       "alACEServerBadCodeSent": alACEServerBadCodeSent,
       "alACEServerBadPinSent": alACEServerBadPinSent}
)
