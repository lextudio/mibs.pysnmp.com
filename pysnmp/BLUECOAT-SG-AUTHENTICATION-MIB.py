# SNMP MIB module (BLUECOAT-SG-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-SG-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:17 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

bluecoatSGAuthentication = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15)
)
bluecoatSGAuthentication.setRevisions(
        ("2014-08-06 03:00",)
)


# Types definitions



class ToggleState(Integer32):
    """Custom type ToggleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SchannelStats_ObjectIdentity = ObjectIdentity
schannelStats = _SchannelStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2)
)
_SchannelStatsTable_Object = MibTable
schannelStatsTable = _SchannelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    schannelStatsTable.setStatus("current")
_SchannelStatsEntry_Object = MibTableRow
schannelStatsEntry = _SchannelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1)
)
schannelStatsEntry.setIndexNames(
    (0, "BLUECOAT-SG-AUTHENTICATION-MIB", "schannelStatsIndex"),
)
if mibBuilder.loadTexts:
    schannelStatsEntry.setStatus("current")


class _SchannelStatsIndex_Type(Integer32):
    """Custom type schannelStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SchannelStatsIndex_Type.__name__ = "Integer32"
_SchannelStatsIndex_Object = MibTableColumn
schannelStatsIndex = _SchannelStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 1),
    _SchannelStatsIndex_Type()
)
schannelStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schannelStatsIndex.setStatus("current")
_DomainName_Type = DisplayString
_DomainName_Object = MibTableColumn
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 2),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("current")
_DomainStatus_Type = DisplayString
_DomainStatus_Object = MibTableColumn
domainStatus = _DomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 3),
    _DomainStatus_Type()
)
domainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainStatus.setStatus("current")
_Timeouts_Type = Counter32
_Timeouts_Object = MibTableColumn
timeouts = _Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 4),
    _Timeouts_Type()
)
timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeouts.setStatus("current")
if mibBuilder.loadTexts:
    timeouts.setUnits("Bytes")
_Transactions_Type = Counter32
_Transactions_Object = MibTableColumn
transactions = _Transactions_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 5),
    _Transactions_Type()
)
transactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactions.setStatus("current")
if mibBuilder.loadTexts:
    transactions.setUnits("Bytes")
_CurrentWaiters_Type = Counter32
_CurrentWaiters_Object = MibTableColumn
currentWaiters = _CurrentWaiters_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 6),
    _CurrentWaiters_Type()
)
currentWaiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentWaiters.setStatus("current")
if mibBuilder.loadTexts:
    currentWaiters.setUnits("Bytes")
_MaxWaiters_Type = Counter32
_MaxWaiters_Object = MibTableColumn
maxWaiters = _MaxWaiters_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 7),
    _MaxWaiters_Type()
)
maxWaiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxWaiters.setStatus("current")
if mibBuilder.loadTexts:
    maxWaiters.setUnits("Bytes")
_Resets_Type = Counter32
_Resets_Object = MibTableColumn
resets = _Resets_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 2, 1, 1, 8),
    _Resets_Type()
)
resets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resets.setStatus("current")
if mibBuilder.loadTexts:
    resets.setUnits("Bytes")
_LsaDomainControllerStats_ObjectIdentity = ObjectIdentity
lsaDomainControllerStats = _LsaDomainControllerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3)
)
_LsaDomainControllerStatsTable_Object = MibTable
lsaDomainControllerStatsTable = _LsaDomainControllerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    lsaDomainControllerStatsTable.setStatus("current")
_LsaDomainControllerStatsEntry_Object = MibTableRow
lsaDomainControllerStatsEntry = _LsaDomainControllerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1)
)
lsaDomainControllerStatsEntry.setIndexNames(
    (0, "BLUECOAT-SG-AUTHENTICATION-MIB", "lsaDomainControllerStatsIndex"),
)
if mibBuilder.loadTexts:
    lsaDomainControllerStatsEntry.setStatus("current")


class _LsaDomainControllerStatsIndex_Type(Integer32):
    """Custom type lsaDomainControllerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LsaDomainControllerStatsIndex_Type.__name__ = "Integer32"
_LsaDomainControllerStatsIndex_Object = MibTableColumn
lsaDomainControllerStatsIndex = _LsaDomainControllerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 1),
    _LsaDomainControllerStatsIndex_Type()
)
lsaDomainControllerStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lsaDomainControllerStatsIndex.setStatus("current")
_DomainControllerName_Type = DisplayString
_DomainControllerName_Object = MibTableColumn
domainControllerName = _DomainControllerName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 2),
    _DomainControllerName_Type()
)
domainControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainControllerName.setStatus("current")
_Address_Type = DisplayString
_Address_Object = MibTableColumn
address = _Address_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 3),
    _Address_Type()
)
address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    address.setStatus("current")
_SiteName_Type = DisplayString
_SiteName_Object = MibScalar
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 4),
    _SiteName_Type()
)
siteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteName.setStatus("current")
_AvgLDAPPingTime_Type = Counter32
_AvgLDAPPingTime_Object = MibTableColumn
avgLDAPPingTime = _AvgLDAPPingTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 5),
    _AvgLDAPPingTime_Type()
)
avgLDAPPingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgLDAPPingTime.setStatus("current")
_LastLDAPPingTime_Type = Counter32
_LastLDAPPingTime_Object = MibScalar
lastLDAPPingTime = _LastLDAPPingTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 6),
    _LastLDAPPingTime_Type()
)
lastLDAPPingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastLDAPPingTime.setStatus("current")
_Flags_Type = DisplayString
_Flags_Object = MibTableColumn
flags = _Flags_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 3, 1, 1, 7),
    _Flags_Type()
)
flags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flags.setStatus("current")
_SchannelServerStats_ObjectIdentity = ObjectIdentity
schannelServerStats = _SchannelServerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4)
)
_SchannelServerStatsTable_Object = MibTable
schannelServerStatsTable = _SchannelServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1)
)
if mibBuilder.loadTexts:
    schannelServerStatsTable.setStatus("current")
_SchannelServerStatsEntry_Object = MibTableRow
schannelServerStatsEntry = _SchannelServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1)
)
schannelServerStatsEntry.setIndexNames(
    (0, "BLUECOAT-SG-AUTHENTICATION-MIB", "schannelServerStatsIndex"),
)
if mibBuilder.loadTexts:
    schannelServerStatsEntry.setStatus("current")


class _SchannelServerStatsIndex_Type(Integer32):
    """Custom type schannelServerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SchannelServerStatsIndex_Type.__name__ = "Integer32"
_SchannelServerStatsIndex_Object = MibTableColumn
schannelServerStatsIndex = _SchannelServerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 1),
    _SchannelServerStatsIndex_Type()
)
schannelServerStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schannelServerStatsIndex.setStatus("current")
_ServerName_Type = DisplayString
_ServerName_Object = MibTableColumn
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 2),
    _ServerName_Type()
)
serverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverName.setStatus("current")
_ConnectionsInUse_Type = Counter32
_ConnectionsInUse_Object = MibTableColumn
connectionsInUse = _ConnectionsInUse_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 3),
    _ConnectionsInUse_Type()
)
connectionsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsInUse.setStatus("current")
_AvailableConnections_Type = Counter32
_AvailableConnections_Object = MibTableColumn
availableConnections = _AvailableConnections_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 4),
    _AvailableConnections_Type()
)
availableConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableConnections.setStatus("current")
_AverageTransactions_Type = Counter32
_AverageTransactions_Object = MibTableColumn
averageTransactions = _AverageTransactions_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 5),
    _AverageTransactions_Type()
)
averageTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageTransactions.setStatus("current")
_AuthsByDomainLast1Minute_Type = Counter32
_AuthsByDomainLast1Minute_Object = MibTableColumn
authsByDomainLast1Minute = _AuthsByDomainLast1Minute_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 6),
    _AuthsByDomainLast1Minute_Type()
)
authsByDomainLast1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authsByDomainLast1Minute.setStatus("current")
if mibBuilder.loadTexts:
    authsByDomainLast1Minute.setUnits("Bytes")
_AuthsByDomainLast3Minutes_Type = Counter32
_AuthsByDomainLast3Minutes_Object = MibTableColumn
authsByDomainLast3Minutes = _AuthsByDomainLast3Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 7),
    _AuthsByDomainLast3Minutes_Type()
)
authsByDomainLast3Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authsByDomainLast3Minutes.setStatus("current")
if mibBuilder.loadTexts:
    authsByDomainLast3Minutes.setUnits("Bytes")
_AuthsByDomainLast5Minutes_Type = Counter32
_AuthsByDomainLast5Minutes_Object = MibTableColumn
authsByDomainLast5Minutes = _AuthsByDomainLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 8),
    _AuthsByDomainLast5Minutes_Type()
)
authsByDomainLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authsByDomainLast5Minutes.setStatus("current")
if mibBuilder.loadTexts:
    authsByDomainLast5Minutes.setUnits("Bytes")
_AuthsByDomainLast15Minutes_Type = Counter32
_AuthsByDomainLast15Minutes_Object = MibTableColumn
authsByDomainLast15Minutes = _AuthsByDomainLast15Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 9),
    _AuthsByDomainLast15Minutes_Type()
)
authsByDomainLast15Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authsByDomainLast15Minutes.setStatus("current")
if mibBuilder.loadTexts:
    authsByDomainLast15Minutes.setUnits("Bytes")
_AuthsByDomainLast60Minutes_Type = Counter32
_AuthsByDomainLast60Minutes_Object = MibTableColumn
authsByDomainLast60Minutes = _AuthsByDomainLast60Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 10),
    _AuthsByDomainLast60Minutes_Type()
)
authsByDomainLast60Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authsByDomainLast60Minutes.setStatus("current")
if mibBuilder.loadTexts:
    authsByDomainLast60Minutes.setUnits("Bytes")
_FailedAuthsByDomainLast1Minute_Type = Counter32
_FailedAuthsByDomainLast1Minute_Object = MibTableColumn
failedAuthsByDomainLast1Minute = _FailedAuthsByDomainLast1Minute_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 11),
    _FailedAuthsByDomainLast1Minute_Type()
)
failedAuthsByDomainLast1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast1Minute.setStatus("current")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast1Minute.setUnits("Bytes")
_FailedAuthsByDomainLast3Minutes_Type = Counter32
_FailedAuthsByDomainLast3Minutes_Object = MibTableColumn
failedAuthsByDomainLast3Minutes = _FailedAuthsByDomainLast3Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 12),
    _FailedAuthsByDomainLast3Minutes_Type()
)
failedAuthsByDomainLast3Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast3Minutes.setStatus("current")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast3Minutes.setUnits("Bytes")
_FailedAuthsByDomainLast5Minutes_Type = Counter32
_FailedAuthsByDomainLast5Minutes_Object = MibTableColumn
failedAuthsByDomainLast5Minutes = _FailedAuthsByDomainLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 13),
    _FailedAuthsByDomainLast5Minutes_Type()
)
failedAuthsByDomainLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast5Minutes.setStatus("current")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast5Minutes.setUnits("Bytes")
_FailedAuthsByDomainLast15Minutes_Type = Counter32
_FailedAuthsByDomainLast15Minutes_Object = MibTableColumn
failedAuthsByDomainLast15Minutes = _FailedAuthsByDomainLast15Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 14),
    _FailedAuthsByDomainLast15Minutes_Type()
)
failedAuthsByDomainLast15Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast15Minutes.setStatus("current")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast15Minutes.setUnits("Bytes")
_FailedAuthsByDomainLast60Minutes_Type = Counter32
_FailedAuthsByDomainLast60Minutes_Object = MibTableColumn
failedAuthsByDomainLast60Minutes = _FailedAuthsByDomainLast60Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 15),
    _FailedAuthsByDomainLast60Minutes_Type()
)
failedAuthsByDomainLast60Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast60Minutes.setStatus("current")
if mibBuilder.loadTexts:
    failedAuthsByDomainLast60Minutes.setUnits("Bytes")
_AvgLatencyPerDomainLast1Minute_Type = Counter32
_AvgLatencyPerDomainLast1Minute_Object = MibTableColumn
avgLatencyPerDomainLast1Minute = _AvgLatencyPerDomainLast1Minute_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 16),
    _AvgLatencyPerDomainLast1Minute_Type()
)
avgLatencyPerDomainLast1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast1Minute.setStatus("current")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast1Minute.setUnits("Bytes")
_AvgLatencyPerDomainLast3Minutes_Type = Counter32
_AvgLatencyPerDomainLast3Minutes_Object = MibTableColumn
avgLatencyPerDomainLast3Minutes = _AvgLatencyPerDomainLast3Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 17),
    _AvgLatencyPerDomainLast3Minutes_Type()
)
avgLatencyPerDomainLast3Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast3Minutes.setStatus("current")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast3Minutes.setUnits("Bytes")
_AvgLatencyPerDomainLast5Minutes_Type = Counter32
_AvgLatencyPerDomainLast5Minutes_Object = MibTableColumn
avgLatencyPerDomainLast5Minutes = _AvgLatencyPerDomainLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 18),
    _AvgLatencyPerDomainLast5Minutes_Type()
)
avgLatencyPerDomainLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast5Minutes.setStatus("current")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast5Minutes.setUnits("Bytes")
_AvgLatencyPerDomainLast15Minutes_Type = Counter32
_AvgLatencyPerDomainLast15Minutes_Object = MibTableColumn
avgLatencyPerDomainLast15Minutes = _AvgLatencyPerDomainLast15Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 19),
    _AvgLatencyPerDomainLast15Minutes_Type()
)
avgLatencyPerDomainLast15Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast15Minutes.setStatus("current")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast15Minutes.setUnits("Bytes")
_AvgLatencyPerDomainLast60Minutes_Type = Counter32
_AvgLatencyPerDomainLast60Minutes_Object = MibTableColumn
avgLatencyPerDomainLast60Minutes = _AvgLatencyPerDomainLast60Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 20),
    _AvgLatencyPerDomainLast60Minutes_Type()
)
avgLatencyPerDomainLast60Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast60Minutes.setStatus("current")
if mibBuilder.loadTexts:
    avgLatencyPerDomainLast60Minutes.setUnits("Bytes")
_MaxLatencyPerDomainLast1Minute_Type = Counter32
_MaxLatencyPerDomainLast1Minute_Object = MibTableColumn
maxLatencyPerDomainLast1Minute = _MaxLatencyPerDomainLast1Minute_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 21),
    _MaxLatencyPerDomainLast1Minute_Type()
)
maxLatencyPerDomainLast1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast1Minute.setStatus("current")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast1Minute.setUnits("Bytes")
_MaxLatencyPerDomainLast3Minutes_Type = Counter32
_MaxLatencyPerDomainLast3Minutes_Object = MibTableColumn
maxLatencyPerDomainLast3Minutes = _MaxLatencyPerDomainLast3Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 22),
    _MaxLatencyPerDomainLast3Minutes_Type()
)
maxLatencyPerDomainLast3Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast3Minutes.setStatus("current")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast3Minutes.setUnits("Bytes")
_MaxLatencyPerDomainLast5Minutes_Type = Counter32
_MaxLatencyPerDomainLast5Minutes_Object = MibTableColumn
maxLatencyPerDomainLast5Minutes = _MaxLatencyPerDomainLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 23),
    _MaxLatencyPerDomainLast5Minutes_Type()
)
maxLatencyPerDomainLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast5Minutes.setStatus("current")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast5Minutes.setUnits("Bytes")
_MaxLatencyPerDomainLast15Minutes_Type = Counter32
_MaxLatencyPerDomainLast15Minutes_Object = MibTableColumn
maxLatencyPerDomainLast15Minutes = _MaxLatencyPerDomainLast15Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 24),
    _MaxLatencyPerDomainLast15Minutes_Type()
)
maxLatencyPerDomainLast15Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast15Minutes.setStatus("current")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast15Minutes.setUnits("Bytes")
_MaxLatencyPerDomainLast60Minutes_Type = Counter32
_MaxLatencyPerDomainLast60Minutes_Object = MibTableColumn
maxLatencyPerDomainLast60Minutes = _MaxLatencyPerDomainLast60Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 25),
    _MaxLatencyPerDomainLast60Minutes_Type()
)
maxLatencyPerDomainLast60Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast60Minutes.setStatus("current")
if mibBuilder.loadTexts:
    maxLatencyPerDomainLast60Minutes.setUnits("Bytes")
_MinLatencyPerDomainLast1Minute_Type = Counter32
_MinLatencyPerDomainLast1Minute_Object = MibTableColumn
minLatencyPerDomainLast1Minute = _MinLatencyPerDomainLast1Minute_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 26),
    _MinLatencyPerDomainLast1Minute_Type()
)
minLatencyPerDomainLast1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast1Minute.setStatus("current")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast1Minute.setUnits("Bytes")
_MinLatencyPerDomainLast3Minutes_Type = Counter32
_MinLatencyPerDomainLast3Minutes_Object = MibTableColumn
minLatencyPerDomainLast3Minutes = _MinLatencyPerDomainLast3Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 27),
    _MinLatencyPerDomainLast3Minutes_Type()
)
minLatencyPerDomainLast3Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast3Minutes.setStatus("current")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast3Minutes.setUnits("Bytes")
_MinLatencyPerDomainLast5Minutes_Type = Counter32
_MinLatencyPerDomainLast5Minutes_Object = MibTableColumn
minLatencyPerDomainLast5Minutes = _MinLatencyPerDomainLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 28),
    _MinLatencyPerDomainLast5Minutes_Type()
)
minLatencyPerDomainLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast5Minutes.setStatus("current")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast5Minutes.setUnits("Bytes")
_MinLatencyPerDomainLast15Minutes_Type = Counter32
_MinLatencyPerDomainLast15Minutes_Object = MibTableColumn
minLatencyPerDomainLast15Minutes = _MinLatencyPerDomainLast15Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 29),
    _MinLatencyPerDomainLast15Minutes_Type()
)
minLatencyPerDomainLast15Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast15Minutes.setStatus("current")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast15Minutes.setUnits("Bytes")
_MinLatencyPerDomainLast60Minutes_Type = Counter32
_MinLatencyPerDomainLast60Minutes_Object = MibTableColumn
minLatencyPerDomainLast60Minutes = _MinLatencyPerDomainLast60Minutes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 4, 1, 1, 30),
    _MinLatencyPerDomainLast60Minutes_Type()
)
minLatencyPerDomainLast60Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast60Minutes.setStatus("current")
if mibBuilder.loadTexts:
    minLatencyPerDomainLast60Minutes.setUnits("Bytes")
_AuthNotifications_ObjectIdentity = ObjectIdentity
authNotifications = _AuthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 5)
)
_AuthNotificationsPrefix_ObjectIdentity = ObjectIdentity
authNotificationsPrefix = _AuthNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 5, 0)
)

# Managed Objects groups


# Notification objects

schannelLatencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 15, 5, 0, 1)
)
schannelLatencyTrap.setObjects(
      *(("BLUECOAT-SG-AUTHENTICATION-MIB", "domainName"),
        ("BLUECOAT-SG-AUTHENTICATION-MIB", "latencyType"),
        ("BLUECOAT-SG-AUTHENTICATION-MIB", "latencyValue"))
)
if mibBuilder.loadTexts:
    schannelLatencyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-AUTHENTICATION-MIB",
    **{"ToggleState": ToggleState,
       "bluecoatSGAuthentication": bluecoatSGAuthentication,
       "schannelStats": schannelStats,
       "schannelStatsTable": schannelStatsTable,
       "schannelStatsEntry": schannelStatsEntry,
       "schannelStatsIndex": schannelStatsIndex,
       "domainName": domainName,
       "domainStatus": domainStatus,
       "timeouts": timeouts,
       "transactions": transactions,
       "currentWaiters": currentWaiters,
       "maxWaiters": maxWaiters,
       "resets": resets,
       "lsaDomainControllerStats": lsaDomainControllerStats,
       "lsaDomainControllerStatsTable": lsaDomainControllerStatsTable,
       "lsaDomainControllerStatsEntry": lsaDomainControllerStatsEntry,
       "lsaDomainControllerStatsIndex": lsaDomainControllerStatsIndex,
       "domainControllerName": domainControllerName,
       "address": address,
       "siteName": siteName,
       "avgLDAPPingTime": avgLDAPPingTime,
       "lastLDAPPingTime": lastLDAPPingTime,
       "flags": flags,
       "schannelServerStats": schannelServerStats,
       "schannelServerStatsTable": schannelServerStatsTable,
       "schannelServerStatsEntry": schannelServerStatsEntry,
       "schannelServerStatsIndex": schannelServerStatsIndex,
       "serverName": serverName,
       "connectionsInUse": connectionsInUse,
       "availableConnections": availableConnections,
       "averageTransactions": averageTransactions,
       "authsByDomainLast1Minute": authsByDomainLast1Minute,
       "authsByDomainLast3Minutes": authsByDomainLast3Minutes,
       "authsByDomainLast5Minutes": authsByDomainLast5Minutes,
       "authsByDomainLast15Minutes": authsByDomainLast15Minutes,
       "authsByDomainLast60Minutes": authsByDomainLast60Minutes,
       "failedAuthsByDomainLast1Minute": failedAuthsByDomainLast1Minute,
       "failedAuthsByDomainLast3Minutes": failedAuthsByDomainLast3Minutes,
       "failedAuthsByDomainLast5Minutes": failedAuthsByDomainLast5Minutes,
       "failedAuthsByDomainLast15Minutes": failedAuthsByDomainLast15Minutes,
       "failedAuthsByDomainLast60Minutes": failedAuthsByDomainLast60Minutes,
       "avgLatencyPerDomainLast1Minute": avgLatencyPerDomainLast1Minute,
       "avgLatencyPerDomainLast3Minutes": avgLatencyPerDomainLast3Minutes,
       "avgLatencyPerDomainLast5Minutes": avgLatencyPerDomainLast5Minutes,
       "avgLatencyPerDomainLast15Minutes": avgLatencyPerDomainLast15Minutes,
       "avgLatencyPerDomainLast60Minutes": avgLatencyPerDomainLast60Minutes,
       "maxLatencyPerDomainLast1Minute": maxLatencyPerDomainLast1Minute,
       "maxLatencyPerDomainLast3Minutes": maxLatencyPerDomainLast3Minutes,
       "maxLatencyPerDomainLast5Minutes": maxLatencyPerDomainLast5Minutes,
       "maxLatencyPerDomainLast15Minutes": maxLatencyPerDomainLast15Minutes,
       "maxLatencyPerDomainLast60Minutes": maxLatencyPerDomainLast60Minutes,
       "minLatencyPerDomainLast1Minute": minLatencyPerDomainLast1Minute,
       "minLatencyPerDomainLast3Minutes": minLatencyPerDomainLast3Minutes,
       "minLatencyPerDomainLast5Minutes": minLatencyPerDomainLast5Minutes,
       "minLatencyPerDomainLast15Minutes": minLatencyPerDomainLast15Minutes,
       "minLatencyPerDomainLast60Minutes": minLatencyPerDomainLast60Minutes,
       "authNotifications": authNotifications,
       "authNotificationsPrefix": authNotificationsPrefix,
       "schannelLatencyTrap": schannelLatencyTrap}
)
