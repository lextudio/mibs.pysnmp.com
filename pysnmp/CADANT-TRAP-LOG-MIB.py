# SNMP MIB module (CADANT-TRAP-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-TRAP-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:15 2024
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

(cadNotification,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadNotification")

(InetAddressIPv4or6,) = mibBuilder.importSymbols(
    "CADANT-TC",
    "InetAddressIPv4or6")

(docsDevEvControlEntry,) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvControlEntry")

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

cadTrapLogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2)
)
cadTrapLogMib.setRevisions(
        ("2006-04-20 00:00",
         "2005-03-31 00:00",
         "2004-03-16 00:00",
         "2004-02-04 00:00",
         "2003-06-30 00:00",
         "2003-05-30 00:00",
         "2003-05-07 00:00",
         "2003-04-29 00:00",
         "2002-08-13 00:00",
         "2002-08-06 00:00",
         "2001-06-19 00:00",
         "2001-06-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadTrapLogGlobals_ObjectIdentity = ObjectIdentity
cadTrapLogGlobals = _CadTrapLogGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1)
)


class _CadProprietaryLoggingEnabled_Type(TruthValue):
    """Custom type cadProprietaryLoggingEnabled based on TruthValue"""


_CadProprietaryLoggingEnabled_Object = MibScalar
cadProprietaryLoggingEnabled = _CadProprietaryLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 1),
    _CadProprietaryLoggingEnabled_Type()
)
cadProprietaryLoggingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadProprietaryLoggingEnabled.setStatus("current")


class _CadLocalLogSize_Type(Unsigned32):
    """Custom type cadLocalLogSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CadLocalLogSize_Type.__name__ = "Unsigned32"
_CadLocalLogSize_Object = MibScalar
cadLocalLogSize = _CadLocalLogSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 2),
    _CadLocalLogSize_Type()
)
cadLocalLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLocalLogSize.setStatus("current")


class _CadLogHistorySize_Type(Unsigned32):
    """Custom type cadLogHistorySize based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_CadLogHistorySize_Type.__name__ = "Unsigned32"
_CadLogHistorySize_Object = MibScalar
cadLogHistorySize = _CadLogHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 3),
    _CadLogHistorySize_Type()
)
cadLogHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLogHistorySize.setStatus("current")


class _CadSyslogFacility_Type(Integer32):
    """Custom type cadSyslogFacility based on Integer32"""
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
        *(("local0", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_CadSyslogFacility_Type.__name__ = "Integer32"
_CadSyslogFacility_Object = MibScalar
cadSyslogFacility = _CadSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 4),
    _CadSyslogFacility_Type()
)
cadSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSyslogFacility.setStatus("current")


class _CadCmTrapInhibit_Type(Bits):
    """Custom type cadCmTrapInhibit based on Bits"""
    defaultHexValue = "f8"

    namedValues = NamedValues(
        *(("registered", 4),
          ("resetClear", 3),
          ("resetProvisioning", 1),
          ("resetRanging", 0),
          ("resetRegistered", 2))
    )

_CadCmTrapInhibit_Type.__name__ = "Bits"
_CadCmTrapInhibit_Object = MibScalar
cadCmTrapInhibit = _CadCmTrapInhibit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 5),
    _CadCmTrapInhibit_Type()
)
cadCmTrapInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmTrapInhibit.setStatus("current")
_CadEvControlTable_Object = MibTable
cadEvControlTable = _CadEvControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    cadEvControlTable.setStatus("current")
_CadEvControlEntry_Object = MibTableRow
cadEvControlEntry = _CadEvControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cadEvControlEntry.setStatus("current")


class _CadEvReporting_Type(Bits):
    """Custom type cadEvReporting based on Bits"""
    namedValues = NamedValues(
        ("console", 0)
    )

_CadEvReporting_Type.__name__ = "Bits"
_CadEvReporting_Object = MibTableColumn
cadEvReporting = _CadEvReporting_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 2, 1, 1),
    _CadEvReporting_Type()
)
cadEvReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadEvReporting.setStatus("current")
_CadEvOverrideTable_Object = MibTable
cadEvOverrideTable = _CadEvOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    cadEvOverrideTable.setStatus("current")
_CadEvOverrideEntry_Object = MibTableRow
cadEvOverrideEntry = _CadEvOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1)
)
cadEvOverrideEntry.setIndexNames(
    (0, "CADANT-TRAP-LOG-MIB", "cadEvOvrdEvId"),
)
if mibBuilder.loadTexts:
    cadEvOverrideEntry.setStatus("current")
_CadEvOvrdEvId_Type = Unsigned32
_CadEvOvrdEvId_Object = MibTableColumn
cadEvOvrdEvId = _CadEvOvrdEvId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1, 1),
    _CadEvOvrdEvId_Type()
)
cadEvOvrdEvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadEvOvrdEvId.setStatus("current")


class _CadEvOvrdState_Type(Integer32):
    """Custom type cadEvOvrdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admit", 1),
          ("inhibit", 2),
          ("priority", 3))
    )


_CadEvOvrdState_Type.__name__ = "Integer32"
_CadEvOvrdState_Object = MibTableColumn
cadEvOvrdState = _CadEvOvrdState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1, 2),
    _CadEvOvrdState_Type()
)
cadEvOvrdState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEvOvrdState.setStatus("current")
_CadEvOvrdRowStatus_Type = RowStatus
_CadEvOvrdRowStatus_Object = MibTableColumn
cadEvOvrdRowStatus = _CadEvOvrdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1, 3),
    _CadEvOvrdRowStatus_Type()
)
cadEvOvrdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEvOvrdRowStatus.setStatus("current")


class _CadEvOvrdPriority_Type(Integer32):
    """Custom type cadEvOvrdPriority based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("invalid", 0),
          ("notice", 6),
          ("warning", 5))
    )


_CadEvOvrdPriority_Type.__name__ = "Integer32"
_CadEvOvrdPriority_Object = MibTableColumn
cadEvOvrdPriority = _CadEvOvrdPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1, 4),
    _CadEvOvrdPriority_Type()
)
cadEvOvrdPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadEvOvrdPriority.setStatus("current")
_CadSyslogSvrTable_Object = MibTable
cadSyslogSvrTable = _CadSyslogSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4)
)
if mibBuilder.loadTexts:
    cadSyslogSvrTable.setStatus("current")
_CadSyslogSvrEntry_Object = MibTableRow
cadSyslogSvrEntry = _CadSyslogSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4, 1)
)
cadSyslogSvrEntry.setIndexNames(
    (0, "CADANT-TRAP-LOG-MIB", "cadSyslogSvrIpAddr"),
)
if mibBuilder.loadTexts:
    cadSyslogSvrEntry.setStatus("current")
_CadSyslogSvrIpAddr_Type = InetAddressIPv4or6
_CadSyslogSvrIpAddr_Object = MibTableColumn
cadSyslogSvrIpAddr = _CadSyslogSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4, 1, 1),
    _CadSyslogSvrIpAddr_Type()
)
cadSyslogSvrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSyslogSvrIpAddr.setStatus("current")


class _CadSyslogSvrFacility_Type(Integer32):
    """Custom type cadSyslogSvrFacility based on Integer32"""
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
        *(("local0", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_CadSyslogSvrFacility_Type.__name__ = "Integer32"
_CadSyslogSvrFacility_Object = MibTableColumn
cadSyslogSvrFacility = _CadSyslogSvrFacility_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4, 1, 2),
    _CadSyslogSvrFacility_Type()
)
cadSyslogSvrFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSyslogSvrFacility.setStatus("current")
_CadSyslogSvrRowStatus_Type = RowStatus
_CadSyslogSvrRowStatus_Object = MibTableColumn
cadSyslogSvrRowStatus = _CadSyslogSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4, 1, 3),
    _CadSyslogSvrRowStatus_Type()
)
cadSyslogSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSyslogSvrRowStatus.setStatus("current")
_CadCliAuthToLogLevelTable_Object = MibTable
cadCliAuthToLogLevelTable = _CadCliAuthToLogLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 5)
)
if mibBuilder.loadTexts:
    cadCliAuthToLogLevelTable.setStatus("current")
_CadCliAuthToLogLevelEntry_Object = MibTableRow
cadCliAuthToLogLevelEntry = _CadCliAuthToLogLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 5, 1)
)
cadCliAuthToLogLevelEntry.setIndexNames(
    (0, "CADANT-TRAP-LOG-MIB", "cadCliAuthLevel"),
)
if mibBuilder.loadTexts:
    cadCliAuthToLogLevelEntry.setStatus("current")


class _CadCliAuthLevel_Type(Integer32):
    """Custom type cadCliAuthLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CadCliAuthLevel_Type.__name__ = "Integer32"
_CadCliAuthLevel_Object = MibTableColumn
cadCliAuthLevel = _CadCliAuthLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 5, 1, 1),
    _CadCliAuthLevel_Type()
)
cadCliAuthLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCliAuthLevel.setStatus("current")


class _CadCliLogLevel_Type(Integer32):
    """Custom type cadCliLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_CadCliLogLevel_Type.__name__ = "Integer32"
_CadCliLogLevel_Object = MibTableColumn
cadCliLogLevel = _CadCliLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 5, 1, 2),
    _CadCliLogLevel_Type()
)
cadCliLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCliLogLevel.setStatus("current")
_CadTrapLogMibConformance_ObjectIdentity = ObjectIdentity
cadTrapLogMibConformance = _CadTrapLogMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10)
)
_CadTrapLogCompliances_ObjectIdentity = ObjectIdentity
cadTrapLogCompliances = _CadTrapLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 1)
)
_CadTrapLogGroups_ObjectIdentity = ObjectIdentity
cadTrapLogGroups = _CadTrapLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2)
)
docsDevEvControlEntry.registerAugmentions(
    ("CADANT-TRAP-LOG-MIB",
     "cadEvControlEntry")
)
cadEvControlEntry.setIndexNames(*docsDevEvControlEntry.getIndexNames())

# Managed Objects groups

cadTrapLogGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2, 1)
)
cadTrapLogGlobalsGroup.setObjects(
      *(("CADANT-TRAP-LOG-MIB", "cadProprietaryLoggingEnabled"),
        ("CADANT-TRAP-LOG-MIB", "cadLocalLogSize"),
        ("CADANT-TRAP-LOG-MIB", "cadLogHistorySize"),
        ("CADANT-TRAP-LOG-MIB", "cadSyslogFacility"),
        ("CADANT-TRAP-LOG-MIB", "cadCmTrapInhibit"))
)
if mibBuilder.loadTexts:
    cadTrapLogGlobalsGroup.setStatus("current")

cadTrapLogEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2, 2)
)
cadTrapLogEventGroup.setObjects(
      *(("CADANT-TRAP-LOG-MIB", "cadEvReporting"),
        ("CADANT-TRAP-LOG-MIB", "cadEvOvrdEvId"),
        ("CADANT-TRAP-LOG-MIB", "cadEvOvrdState"),
        ("CADANT-TRAP-LOG-MIB", "cadEvOvrdRowStatus"))
)
if mibBuilder.loadTexts:
    cadTrapLogEventGroup.setStatus("current")

cadSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2, 3)
)
cadSyslogGroup.setObjects(
      *(("CADANT-TRAP-LOG-MIB", "cadSyslogSvrFacility"),
        ("CADANT-TRAP-LOG-MIB", "cadSyslogSvrRowStatus"))
)
if mibBuilder.loadTexts:
    cadSyslogGroup.setStatus("current")

cadCliAuthToLogLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2, 4)
)
cadCliAuthToLogLevelGroup.setObjects(
    ("CADANT-TRAP-LOG-MIB", "cadCliLogLevel")
)
if mibBuilder.loadTexts:
    cadCliAuthToLogLevelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cadTrapLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    cadTrapLogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-TRAP-LOG-MIB",
    **{"cadTrapLogMib": cadTrapLogMib,
       "cadTrapLogGlobals": cadTrapLogGlobals,
       "cadProprietaryLoggingEnabled": cadProprietaryLoggingEnabled,
       "cadLocalLogSize": cadLocalLogSize,
       "cadLogHistorySize": cadLogHistorySize,
       "cadSyslogFacility": cadSyslogFacility,
       "cadCmTrapInhibit": cadCmTrapInhibit,
       "cadEvControlTable": cadEvControlTable,
       "cadEvControlEntry": cadEvControlEntry,
       "cadEvReporting": cadEvReporting,
       "cadEvOverrideTable": cadEvOverrideTable,
       "cadEvOverrideEntry": cadEvOverrideEntry,
       "cadEvOvrdEvId": cadEvOvrdEvId,
       "cadEvOvrdState": cadEvOvrdState,
       "cadEvOvrdRowStatus": cadEvOvrdRowStatus,
       "cadEvOvrdPriority": cadEvOvrdPriority,
       "cadSyslogSvrTable": cadSyslogSvrTable,
       "cadSyslogSvrEntry": cadSyslogSvrEntry,
       "cadSyslogSvrIpAddr": cadSyslogSvrIpAddr,
       "cadSyslogSvrFacility": cadSyslogSvrFacility,
       "cadSyslogSvrRowStatus": cadSyslogSvrRowStatus,
       "cadCliAuthToLogLevelTable": cadCliAuthToLogLevelTable,
       "cadCliAuthToLogLevelEntry": cadCliAuthToLogLevelEntry,
       "cadCliAuthLevel": cadCliAuthLevel,
       "cadCliLogLevel": cadCliLogLevel,
       "cadTrapLogMibConformance": cadTrapLogMibConformance,
       "cadTrapLogCompliances": cadTrapLogCompliances,
       "cadTrapLogCompliance": cadTrapLogCompliance,
       "cadTrapLogGroups": cadTrapLogGroups,
       "cadTrapLogGlobalsGroup": cadTrapLogGlobalsGroup,
       "cadTrapLogEventGroup": cadTrapLogEventGroup,
       "cadSyslogGroup": cadSyslogGroup,
       "cadCliAuthToLogLevelGroup": cadCliAuthToLogLevelGroup}
)
