# SNMP MIB module (NET-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NET-SNMP-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:21 2024
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

(netSnmpGroups,
 netSnmpModuleIDs,
 netSnmpNotifications,
 netSnmpObjects) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmpGroups",
    "netSnmpModuleIDs",
    "netSnmpNotifications",
    "netSnmpObjects")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

netSnmpAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 2)
)
netSnmpAgentMIB.setRevisions(
        ("2010-03-17 00:00",
         "2005-02-07 00:00",
         "2002-02-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NetsnmpCacheStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cached", 4),
          ("disabled", 2),
          ("empty", 3),
          ("enabled", 1),
          ("expired", 5))
    )



# MIB Managed Objects in the order of their OIDs

_NsVersion_ObjectIdentity = ObjectIdentity
nsVersion = _NsVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 1)
)
_NsMibRegistry_ObjectIdentity = ObjectIdentity
nsMibRegistry = _NsMibRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2)
)
_NsModuleTable_Object = MibTable
nsModuleTable = _NsModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nsModuleTable.setStatus("current")
_NsModuleEntry_Object = MibTableRow
nsModuleEntry = _NsModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1)
)
nsModuleEntry.setIndexNames(
    (0, "NET-SNMP-AGENT-MIB", "nsmContextName"),
    (0, "NET-SNMP-AGENT-MIB", "nsmRegistrationPoint"),
    (0, "NET-SNMP-AGENT-MIB", "nsmRegistrationPriority"),
)
if mibBuilder.loadTexts:
    nsModuleEntry.setStatus("current")
_NsmContextName_Type = SnmpAdminString
_NsmContextName_Object = MibTableColumn
nsmContextName = _NsmContextName_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 1),
    _NsmContextName_Type()
)
nsmContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsmContextName.setStatus("current")
_NsmRegistrationPoint_Type = ObjectIdentifier
_NsmRegistrationPoint_Object = MibTableColumn
nsmRegistrationPoint = _NsmRegistrationPoint_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 2),
    _NsmRegistrationPoint_Type()
)
nsmRegistrationPoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsmRegistrationPoint.setStatus("current")


class _NsmRegistrationPriority_Type(Integer32):
    """Custom type nsmRegistrationPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NsmRegistrationPriority_Type.__name__ = "Integer32"
_NsmRegistrationPriority_Object = MibTableColumn
nsmRegistrationPriority = _NsmRegistrationPriority_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 3),
    _NsmRegistrationPriority_Type()
)
nsmRegistrationPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsmRegistrationPriority.setStatus("current")
_NsModuleName_Type = DisplayString
_NsModuleName_Object = MibTableColumn
nsModuleName = _NsModuleName_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 4),
    _NsModuleName_Type()
)
nsModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModuleName.setStatus("current")


class _NsModuleModes_Type(Bits):
    """Custom type nsModuleModes based on Bits"""
    namedValues = NamedValues(
        *(("getAndGetNext", 0),
          ("getBulk", 2),
          ("set", 1))
    )

_NsModuleModes_Type.__name__ = "Bits"
_NsModuleModes_Object = MibTableColumn
nsModuleModes = _NsModuleModes_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 5),
    _NsModuleModes_Type()
)
nsModuleModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModuleModes.setStatus("current")
_NsModuleTimeout_Type = Integer32
_NsModuleTimeout_Object = MibTableColumn
nsModuleTimeout = _NsModuleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 2, 1, 1, 6),
    _NsModuleTimeout_Type()
)
nsModuleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModuleTimeout.setStatus("current")
_NsExtensions_ObjectIdentity = ObjectIdentity
nsExtensions = _NsExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3)
)
_NsDLMod_ObjectIdentity = ObjectIdentity
nsDLMod = _NsDLMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 4)
)
_NsCache_ObjectIdentity = ObjectIdentity
nsCache = _NsCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5)
)


class _NsCacheDefaultTimeout_Type(Integer32):
    """Custom type nsCacheDefaultTimeout based on Integer32"""
    defaultValue = 5


_NsCacheDefaultTimeout_Object = MibScalar
nsCacheDefaultTimeout = _NsCacheDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 1),
    _NsCacheDefaultTimeout_Type()
)
nsCacheDefaultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCacheDefaultTimeout.setStatus("current")


class _NsCacheEnabled_Type(TruthValue):
    """Custom type nsCacheEnabled based on TruthValue"""


_NsCacheEnabled_Object = MibScalar
nsCacheEnabled = _NsCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 2),
    _NsCacheEnabled_Type()
)
nsCacheEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCacheEnabled.setStatus("current")
_NsCacheTable_Object = MibTable
nsCacheTable = _NsCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3)
)
if mibBuilder.loadTexts:
    nsCacheTable.setStatus("current")
_NsCacheEntry_Object = MibTableRow
nsCacheEntry = _NsCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1)
)
nsCacheEntry.setIndexNames(
    (1, "NET-SNMP-AGENT-MIB", "nsCachedOID"),
)
if mibBuilder.loadTexts:
    nsCacheEntry.setStatus("current")
_NsCachedOID_Type = ObjectIdentifier
_NsCachedOID_Object = MibTableColumn
nsCachedOID = _NsCachedOID_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 1),
    _NsCachedOID_Type()
)
nsCachedOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCachedOID.setStatus("current")
_NsCacheTimeout_Type = Integer32
_NsCacheTimeout_Object = MibTableColumn
nsCacheTimeout = _NsCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 2),
    _NsCacheTimeout_Type()
)
nsCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCacheTimeout.setStatus("current")
_NsCacheStatus_Type = NetsnmpCacheStatus
_NsCacheStatus_Object = MibTableColumn
nsCacheStatus = _NsCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 5, 3, 1, 3),
    _NsCacheStatus_Type()
)
nsCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCacheStatus.setStatus("current")
_NsErrorHistory_ObjectIdentity = ObjectIdentity
nsErrorHistory = _NsErrorHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 6)
)
_NsConfiguration_ObjectIdentity = ObjectIdentity
nsConfiguration = _NsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7)
)
_NsConfigDebug_ObjectIdentity = ObjectIdentity
nsConfigDebug = _NsConfigDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1)
)


class _NsDebugEnabled_Type(TruthValue):
    """Custom type nsDebugEnabled based on TruthValue"""


_NsDebugEnabled_Object = MibScalar
nsDebugEnabled = _NsDebugEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 1),
    _NsDebugEnabled_Type()
)
nsDebugEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsDebugEnabled.setStatus("current")


class _NsDebugOutputAll_Type(TruthValue):
    """Custom type nsDebugOutputAll based on TruthValue"""


_NsDebugOutputAll_Object = MibScalar
nsDebugOutputAll = _NsDebugOutputAll_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 2),
    _NsDebugOutputAll_Type()
)
nsDebugOutputAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsDebugOutputAll.setStatus("current")


class _NsDebugDumpPdu_Type(TruthValue):
    """Custom type nsDebugDumpPdu based on TruthValue"""


_NsDebugDumpPdu_Object = MibScalar
nsDebugDumpPdu = _NsDebugDumpPdu_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 3),
    _NsDebugDumpPdu_Type()
)
nsDebugDumpPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsDebugDumpPdu.setStatus("current")
_NsDebugTokenTable_Object = MibTable
nsDebugTokenTable = _NsDebugTokenTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    nsDebugTokenTable.setStatus("current")
_NsDebugTokenEntry_Object = MibTableRow
nsDebugTokenEntry = _NsDebugTokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1)
)
nsDebugTokenEntry.setIndexNames(
    (1, "NET-SNMP-AGENT-MIB", "nsDebugTokenPrefix"),
)
if mibBuilder.loadTexts:
    nsDebugTokenEntry.setStatus("current")
_NsDebugTokenPrefix_Type = DisplayString
_NsDebugTokenPrefix_Object = MibTableColumn
nsDebugTokenPrefix = _NsDebugTokenPrefix_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1, 2),
    _NsDebugTokenPrefix_Type()
)
nsDebugTokenPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsDebugTokenPrefix.setStatus("current")
_NsDebugTokenStatus_Type = RowStatus
_NsDebugTokenStatus_Object = MibTableColumn
nsDebugTokenStatus = _NsDebugTokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 1, 4, 1, 4),
    _NsDebugTokenStatus_Type()
)
nsDebugTokenStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsDebugTokenStatus.setStatus("current")
_NsConfigLogging_ObjectIdentity = ObjectIdentity
nsConfigLogging = _NsConfigLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2)
)
_NsLoggingTable_Object = MibTable
nsLoggingTable = _NsLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    nsLoggingTable.setStatus("current")
_NsLoggingEntry_Object = MibTableRow
nsLoggingEntry = _NsLoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1)
)
nsLoggingEntry.setIndexNames(
    (0, "NET-SNMP-AGENT-MIB", "nsLogLevel"),
    (1, "NET-SNMP-AGENT-MIB", "nsLogToken"),
)
if mibBuilder.loadTexts:
    nsLoggingEntry.setStatus("current")


class _NsLogLevel_Type(Integer32):
    """Custom type nsLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_NsLogLevel_Type.__name__ = "Integer32"
_NsLogLevel_Object = MibTableColumn
nsLogLevel = _NsLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 1),
    _NsLogLevel_Type()
)
nsLogLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsLogLevel.setStatus("current")
_NsLogToken_Type = DisplayString
_NsLogToken_Object = MibTableColumn
nsLogToken = _NsLogToken_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 2),
    _NsLogToken_Type()
)
nsLogToken.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsLogToken.setStatus("current")


class _NsLogType_Type(Integer32):
    """Custom type nsLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("callback", 5),
          ("file", 3),
          ("stderr", 2),
          ("stdout", 1),
          ("syslog", 4))
    )


_NsLogType_Type.__name__ = "Integer32"
_NsLogType_Object = MibTableColumn
nsLogType = _NsLogType_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 3),
    _NsLogType_Type()
)
nsLogType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsLogType.setStatus("current")


class _NsLogMaxLevel_Type(Integer32):
    """Custom type nsLogMaxLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_NsLogMaxLevel_Type.__name__ = "Integer32"
_NsLogMaxLevel_Object = MibTableColumn
nsLogMaxLevel = _NsLogMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 4),
    _NsLogMaxLevel_Type()
)
nsLogMaxLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsLogMaxLevel.setStatus("current")
_NsLogStatus_Type = RowStatus
_NsLogStatus_Object = MibTableColumn
nsLogStatus = _NsLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 7, 2, 1, 1, 5),
    _NsLogStatus_Type()
)
nsLogStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsLogStatus.setStatus("current")
_NsTransactions_ObjectIdentity = ObjectIdentity
nsTransactions = _NsTransactions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8)
)
_NsTransactionTable_Object = MibTable
nsTransactionTable = _NsTransactionTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8, 1)
)
if mibBuilder.loadTexts:
    nsTransactionTable.setStatus("current")
_NsTransactionEntry_Object = MibTableRow
nsTransactionEntry = _NsTransactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1)
)
nsTransactionEntry.setIndexNames(
    (0, "NET-SNMP-AGENT-MIB", "nsTransactionID"),
)
if mibBuilder.loadTexts:
    nsTransactionEntry.setStatus("current")


class _NsTransactionID_Type(Unsigned32):
    """Custom type nsTransactionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NsTransactionID_Type.__name__ = "Unsigned32"
_NsTransactionID_Object = MibTableColumn
nsTransactionID = _NsTransactionID_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1, 1),
    _NsTransactionID_Type()
)
nsTransactionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsTransactionID.setStatus("current")
_NsTransactionMode_Type = Integer32
_NsTransactionMode_Object = MibTableColumn
nsTransactionMode = _NsTransactionMode_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 8, 1, 1, 2),
    _NsTransactionMode_Type()
)
nsTransactionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTransactionMode.setStatus("current")
_NsConfigGroups_ObjectIdentity = ObjectIdentity
nsConfigGroups = _NsConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 7)
)

# Managed Objects groups

nsModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 2)
)
nsModuleGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsModuleName"),
        ("NET-SNMP-AGENT-MIB", "nsModuleModes"),
        ("NET-SNMP-AGENT-MIB", "nsModuleTimeout"))
)
if mibBuilder.loadTexts:
    nsModuleGroup.setStatus("current")

nsCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 4)
)
nsCacheGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsCacheDefaultTimeout"),
        ("NET-SNMP-AGENT-MIB", "nsCacheEnabled"),
        ("NET-SNMP-AGENT-MIB", "nsCacheTimeout"),
        ("NET-SNMP-AGENT-MIB", "nsCacheStatus"))
)
if mibBuilder.loadTexts:
    nsCacheGroup.setStatus("current")

nsDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 7, 1)
)
nsDebugGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsDebugEnabled"),
        ("NET-SNMP-AGENT-MIB", "nsDebugOutputAll"),
        ("NET-SNMP-AGENT-MIB", "nsDebugDumpPdu"),
        ("NET-SNMP-AGENT-MIB", "nsDebugTokenStatus"))
)
if mibBuilder.loadTexts:
    nsDebugGroup.setStatus("current")

nsLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 7, 2)
)
nsLoggingGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsLogType"),
        ("NET-SNMP-AGENT-MIB", "nsLogMaxLevel"),
        ("NET-SNMP-AGENT-MIB", "nsLogStatus"))
)
if mibBuilder.loadTexts:
    nsLoggingGroup.setStatus("current")

nsTransactionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 8)
)
nsTransactionGroup.setObjects(
    ("NET-SNMP-AGENT-MIB", "nsTransactionMode")
)
if mibBuilder.loadTexts:
    nsTransactionGroup.setStatus("current")


# Notification objects

nsNotifyStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 4, 0, 1)
)
if mibBuilder.loadTexts:
    nsNotifyStart.setStatus(
        "current"
    )

nsNotifyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 4, 0, 2)
)
if mibBuilder.loadTexts:
    nsNotifyShutdown.setStatus(
        "current"
    )

nsNotifyRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 4, 0, 3)
)
if mibBuilder.loadTexts:
    nsNotifyRestart.setStatus(
        "current"
    )


# Notifications groups

nsAgentNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8072, 5, 2, 9)
)
nsAgentNotifyGroup.setObjects(
      *(("NET-SNMP-AGENT-MIB", "nsNotifyStart"),
        ("NET-SNMP-AGENT-MIB", "nsNotifyShutdown"),
        ("NET-SNMP-AGENT-MIB", "nsNotifyRestart"))
)
if mibBuilder.loadTexts:
    nsAgentNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-AGENT-MIB",
    **{"NetsnmpCacheStatus": NetsnmpCacheStatus,
       "nsVersion": nsVersion,
       "nsMibRegistry": nsMibRegistry,
       "nsModuleTable": nsModuleTable,
       "nsModuleEntry": nsModuleEntry,
       "nsmContextName": nsmContextName,
       "nsmRegistrationPoint": nsmRegistrationPoint,
       "nsmRegistrationPriority": nsmRegistrationPriority,
       "nsModuleName": nsModuleName,
       "nsModuleModes": nsModuleModes,
       "nsModuleTimeout": nsModuleTimeout,
       "nsExtensions": nsExtensions,
       "nsDLMod": nsDLMod,
       "nsCache": nsCache,
       "nsCacheDefaultTimeout": nsCacheDefaultTimeout,
       "nsCacheEnabled": nsCacheEnabled,
       "nsCacheTable": nsCacheTable,
       "nsCacheEntry": nsCacheEntry,
       "nsCachedOID": nsCachedOID,
       "nsCacheTimeout": nsCacheTimeout,
       "nsCacheStatus": nsCacheStatus,
       "nsErrorHistory": nsErrorHistory,
       "nsConfiguration": nsConfiguration,
       "nsConfigDebug": nsConfigDebug,
       "nsDebugEnabled": nsDebugEnabled,
       "nsDebugOutputAll": nsDebugOutputAll,
       "nsDebugDumpPdu": nsDebugDumpPdu,
       "nsDebugTokenTable": nsDebugTokenTable,
       "nsDebugTokenEntry": nsDebugTokenEntry,
       "nsDebugTokenPrefix": nsDebugTokenPrefix,
       "nsDebugTokenStatus": nsDebugTokenStatus,
       "nsConfigLogging": nsConfigLogging,
       "nsLoggingTable": nsLoggingTable,
       "nsLoggingEntry": nsLoggingEntry,
       "nsLogLevel": nsLogLevel,
       "nsLogToken": nsLogToken,
       "nsLogType": nsLogType,
       "nsLogMaxLevel": nsLogMaxLevel,
       "nsLogStatus": nsLogStatus,
       "nsTransactions": nsTransactions,
       "nsTransactionTable": nsTransactionTable,
       "nsTransactionEntry": nsTransactionEntry,
       "nsTransactionID": nsTransactionID,
       "nsTransactionMode": nsTransactionMode,
       "netSnmpAgentMIB": netSnmpAgentMIB,
       "nsNotifyStart": nsNotifyStart,
       "nsNotifyShutdown": nsNotifyShutdown,
       "nsNotifyRestart": nsNotifyRestart,
       "nsModuleGroup": nsModuleGroup,
       "nsCacheGroup": nsCacheGroup,
       "nsConfigGroups": nsConfigGroups,
       "nsDebugGroup": nsDebugGroup,
       "nsLoggingGroup": nsLoggingGroup,
       "nsTransactionGroup": nsTransactionGroup,
       "nsAgentNotifyGroup": nsAgentNotifyGroup}
)
