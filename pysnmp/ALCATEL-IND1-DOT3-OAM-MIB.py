# SNMP MIB module (ALCATEL-IND1-DOT3-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DOT3-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:55 2024
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

(softentIND1Dot3Oam,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Dot3Oam")

(dot3OamEntry,
 dot3OamEventLogEventTotal,
 dot3OamEventLogLocation,
 dot3OamEventLogOui,
 dot3OamEventLogRunningTotal,
 dot3OamEventLogThresholdHi,
 dot3OamEventLogThresholdLo,
 dot3OamEventLogTimestamp,
 dot3OamEventLogType,
 dot3OamEventLogValue,
 dot3OamEventLogWindowHi,
 dot3OamEventLogWindowLo,
 dot3OamLoopbackEntry,
 dot3OamStatsEntry) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "dot3OamEntry",
    "dot3OamEventLogEventTotal",
    "dot3OamEventLogLocation",
    "dot3OamEventLogOui",
    "dot3OamEventLogRunningTotal",
    "dot3OamEventLogThresholdHi",
    "dot3OamEventLogThresholdLo",
    "dot3OamEventLogTimestamp",
    "dot3OamEventLogType",
    "dot3OamEventLogValue",
    "dot3OamEventLogWindowHi",
    "dot3OamEventLogWindowLo",
    "dot3OamLoopbackEntry",
    "dot3OamStatsEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1Dot3OamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1)
)
alcatelIND1Dot3OamMIB.setRevisions(
        ("2009-02-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1Dot3OamNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1Dot3OamNotifications = _AlcatelIND1Dot3OamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot3OamNotifications.setStatus("current")
_AlcatelIND1Dot3OamMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1Dot3OamMIBObjects = _AlcatelIND1Dot3OamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot3OamMIBObjects.setStatus("current")


class _AlaDot3OamStatus_Type(Integer32):
    """Custom type alaDot3OamStatus based on Integer32"""
    defaultValue = 2

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


_AlaDot3OamStatus_Type.__name__ = "Integer32"
_AlaDot3OamStatus_Object = MibScalar
alaDot3OamStatus = _AlaDot3OamStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 1),
    _AlaDot3OamStatus_Type()
)
alaDot3OamStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamStatus.setStatus("current")


class _AlaDot3OamGlobalClearStats_Type(Integer32):
    """Custom type alaDot3OamGlobalClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDot3OamGlobalClearStats_Type.__name__ = "Integer32"
_AlaDot3OamGlobalClearStats_Object = MibScalar
alaDot3OamGlobalClearStats = _AlaDot3OamGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 2),
    _AlaDot3OamGlobalClearStats_Type()
)
alaDot3OamGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamGlobalClearStats.setStatus("current")


class _AlaDot3OamGlobalClearEventLogs_Type(Integer32):
    """Custom type alaDot3OamGlobalClearEventLogs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDot3OamGlobalClearEventLogs_Type.__name__ = "Integer32"
_AlaDot3OamGlobalClearEventLogs_Object = MibScalar
alaDot3OamGlobalClearEventLogs = _AlaDot3OamGlobalClearEventLogs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 3),
    _AlaDot3OamGlobalClearEventLogs_Type()
)
alaDot3OamGlobalClearEventLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamGlobalClearEventLogs.setStatus("current")


class _AlaDot3OamGlobalClearVariableTransactions_Type(Integer32):
    """Custom type alaDot3OamGlobalClearVariableTransactions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDot3OamGlobalClearVariableTransactions_Type.__name__ = "Integer32"
_AlaDot3OamGlobalClearVariableTransactions_Object = MibScalar
alaDot3OamGlobalClearVariableTransactions = _AlaDot3OamGlobalClearVariableTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 4),
    _AlaDot3OamGlobalClearVariableTransactions_Type()
)
alaDot3OamGlobalClearVariableTransactions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamGlobalClearVariableTransactions.setStatus("current")


class _AlaDot3OamMultiplePduCount_Type(Integer32):
    """Custom type alaDot3OamMultiplePduCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlaDot3OamMultiplePduCount_Type.__name__ = "Integer32"
_AlaDot3OamMultiplePduCount_Object = MibScalar
alaDot3OamMultiplePduCount = _AlaDot3OamMultiplePduCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 5),
    _AlaDot3OamMultiplePduCount_Type()
)
alaDot3OamMultiplePduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamMultiplePduCount.setStatus("current")
_AlaDot3OamPortConfig_ObjectIdentity = ObjectIdentity
alaDot3OamPortConfig = _AlaDot3OamPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8)
)
_AlaDot3OamTable_Object = MibTable
alaDot3OamTable = _AlaDot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamTable.setStatus("current")
_AlaDot3OamEntry_Object = MibTableRow
alaDot3OamEntry = _AlaDot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamEntry.setStatus("current")


class _AlaDot3OamKeepAliveInterval_Type(Integer32):
    """Custom type alaDot3OamKeepAliveInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_AlaDot3OamKeepAliveInterval_Type.__name__ = "Integer32"
_AlaDot3OamKeepAliveInterval_Object = MibTableColumn
alaDot3OamKeepAliveInterval = _AlaDot3OamKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1, 1, 1),
    _AlaDot3OamKeepAliveInterval_Type()
)
alaDot3OamKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamKeepAliveInterval.setStatus("current")


class _AlaDot3OamHelloInterval_Type(Integer32):
    """Custom type alaDot3OamHelloInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlaDot3OamHelloInterval_Type.__name__ = "Integer32"
_AlaDot3OamHelloInterval_Object = MibTableColumn
alaDot3OamHelloInterval = _AlaDot3OamHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1, 1, 2),
    _AlaDot3OamHelloInterval_Type()
)
alaDot3OamHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaDot3OamHelloInterval.setUnits("seconds")


class _AlaDot3OamNextTransactionId_Type(Integer32):
    """Custom type alaDot3OamNextTransactionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaDot3OamNextTransactionId_Type.__name__ = "Integer32"
_AlaDot3OamNextTransactionId_Object = MibTableColumn
alaDot3OamNextTransactionId = _AlaDot3OamNextTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1, 1, 3),
    _AlaDot3OamNextTransactionId_Type()
)
alaDot3OamNextTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot3OamNextTransactionId.setStatus("current")
_AlaDot3OamPortLoopbackControl_ObjectIdentity = ObjectIdentity
alaDot3OamPortLoopbackControl = _AlaDot3OamPortLoopbackControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9)
)
_AlaDot3OamLoopbackTable_Object = MibTable
alaDot3OamLoopbackTable = _AlaDot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamLoopbackTable.setStatus("current")
_AlaDot3OamLoopbackEntry_Object = MibTableRow
alaDot3OamLoopbackEntry = _AlaDot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamLoopbackEntry.setStatus("current")


class _AlaDot3OamPortL1PingFramesConf_Type(Integer32):
    """Custom type alaDot3OamPortL1PingFramesConf based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AlaDot3OamPortL1PingFramesConf_Type.__name__ = "Integer32"
_AlaDot3OamPortL1PingFramesConf_Object = MibTableColumn
alaDot3OamPortL1PingFramesConf = _AlaDot3OamPortL1PingFramesConf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 1),
    _AlaDot3OamPortL1PingFramesConf_Type()
)
alaDot3OamPortL1PingFramesConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamPortL1PingFramesConf.setStatus("current")


class _AlaDot3OamPortL1PingFramesDelay_Type(Integer32):
    """Custom type alaDot3OamPortL1PingFramesDelay based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_AlaDot3OamPortL1PingFramesDelay_Type.__name__ = "Integer32"
_AlaDot3OamPortL1PingFramesDelay_Object = MibTableColumn
alaDot3OamPortL1PingFramesDelay = _AlaDot3OamPortL1PingFramesDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 2),
    _AlaDot3OamPortL1PingFramesDelay_Type()
)
alaDot3OamPortL1PingFramesDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamPortL1PingFramesDelay.setStatus("current")
if mibBuilder.loadTexts:
    alaDot3OamPortL1PingFramesDelay.setUnits("milliseconds")


class _AlaDot3OamPortL1PingStatus_Type(Integer32):
    """Custom type alaDot3OamPortL1PingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("operationSuccessful", 3),
          ("operationUnsuccessful", 4),
          ("running", 2),
          ("start", 1))
    )


_AlaDot3OamPortL1PingStatus_Type.__name__ = "Integer32"
_AlaDot3OamPortL1PingStatus_Object = MibTableColumn
alaDot3OamPortL1PingStatus = _AlaDot3OamPortL1PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 3),
    _AlaDot3OamPortL1PingStatus_Type()
)
alaDot3OamPortL1PingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamPortL1PingStatus.setStatus("current")
_AlaDot3OamPortL1PingFramesSent_Type = Counter32
_AlaDot3OamPortL1PingFramesSent_Object = MibTableColumn
alaDot3OamPortL1PingFramesSent = _AlaDot3OamPortL1PingFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 4),
    _AlaDot3OamPortL1PingFramesSent_Type()
)
alaDot3OamPortL1PingFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot3OamPortL1PingFramesSent.setStatus("current")
_AlaDot3OamPortL1PingFramesReceived_Type = Counter32
_AlaDot3OamPortL1PingFramesReceived_Object = MibTableColumn
alaDot3OamPortL1PingFramesReceived = _AlaDot3OamPortL1PingFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 5),
    _AlaDot3OamPortL1PingFramesReceived_Type()
)
alaDot3OamPortL1PingFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot3OamPortL1PingFramesReceived.setStatus("current")
_AlaDot3OamPortL1PingAverageRoundTripDelay_Type = Integer32
_AlaDot3OamPortL1PingAverageRoundTripDelay_Object = MibTableColumn
alaDot3OamPortL1PingAverageRoundTripDelay = _AlaDot3OamPortL1PingAverageRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 6),
    _AlaDot3OamPortL1PingAverageRoundTripDelay_Type()
)
alaDot3OamPortL1PingAverageRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot3OamPortL1PingAverageRoundTripDelay.setStatus("current")
_AlaDot3OamPortStats_ObjectIdentity = ObjectIdentity
alaDot3OamPortStats = _AlaDot3OamPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 10)
)
_AlaDot3OamStatsTable_Object = MibTable
alaDot3OamStatsTable = _AlaDot3OamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamStatsTable.setStatus("current")
_AlaDot3OamStatsEntry_Object = MibTableRow
alaDot3OamStatsEntry = _AlaDot3OamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamStatsEntry.setStatus("current")


class _AlaDot3OamPortClearStats_Type(Integer32):
    """Custom type alaDot3OamPortClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDot3OamPortClearStats_Type.__name__ = "Integer32"
_AlaDot3OamPortClearStats_Object = MibTableColumn
alaDot3OamPortClearStats = _AlaDot3OamPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 10, 1, 1, 1),
    _AlaDot3OamPortClearStats_Type()
)
alaDot3OamPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamPortClearStats.setStatus("current")
_AlaDot3OamPortEventLogs_ObjectIdentity = ObjectIdentity
alaDot3OamPortEventLogs = _AlaDot3OamPortEventLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 11)
)
_AlaDot3OamEventLogTable_Object = MibTable
alaDot3OamEventLogTable = _AlaDot3OamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamEventLogTable.setStatus("current")
_AlaDot3OamEventLogEntry_Object = MibTableRow
alaDot3OamEventLogEntry = _AlaDot3OamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 11, 1, 1)
)
alaDot3OamEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alaDot3OamEventLogEntry.setStatus("current")


class _AlaDot3OamPortClearEventLogs_Type(Integer32):
    """Custom type alaDot3OamPortClearEventLogs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDot3OamPortClearEventLogs_Type.__name__ = "Integer32"
_AlaDot3OamPortClearEventLogs_Object = MibTableColumn
alaDot3OamPortClearEventLogs = _AlaDot3OamPortClearEventLogs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 11, 1, 1, 1),
    _AlaDot3OamPortClearEventLogs_Type()
)
alaDot3OamPortClearEventLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot3OamPortClearEventLogs.setStatus("current")
_AlaDot3OamRetrieveRequest_ObjectIdentity = ObjectIdentity
alaDot3OamRetrieveRequest = _AlaDot3OamRetrieveRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12)
)
_AlaDot3OamRetrieveRequestTable_Object = MibTable
alaDot3OamRetrieveRequestTable = _AlaDot3OamRetrieveRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamRetrieveRequestTable.setStatus("current")
_AlaDot3OamRetrieveRequestEntry_Object = MibTableRow
alaDot3OamRetrieveRequestEntry = _AlaDot3OamRetrieveRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1)
)
alaDot3OamRetrieveRequestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamTransactionId"),
    (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableRequestBranch"),
    (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableRequestLeaf"),
)
if mibBuilder.loadTexts:
    alaDot3OamRetrieveRequestEntry.setStatus("current")
_AlaDot3OamTransactionId_Type = Integer32
_AlaDot3OamTransactionId_Object = MibTableColumn
alaDot3OamTransactionId = _AlaDot3OamTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 1),
    _AlaDot3OamTransactionId_Type()
)
alaDot3OamTransactionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot3OamTransactionId.setStatus("current")


class _AlaDot3OamVariableRequestBranch_Type(Integer32):
    """Custom type alaDot3OamVariableRequestBranch based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("attribute", 7),
          ("object", 3),
          ("package", 4))
    )


_AlaDot3OamVariableRequestBranch_Type.__name__ = "Integer32"
_AlaDot3OamVariableRequestBranch_Object = MibTableColumn
alaDot3OamVariableRequestBranch = _AlaDot3OamVariableRequestBranch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 2),
    _AlaDot3OamVariableRequestBranch_Type()
)
alaDot3OamVariableRequestBranch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot3OamVariableRequestBranch.setStatus("current")


class _AlaDot3OamVariableRequestLeaf_Type(Integer32):
    """Custom type alaDot3OamVariableRequestLeaf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaDot3OamVariableRequestLeaf_Type.__name__ = "Integer32"
_AlaDot3OamVariableRequestLeaf_Object = MibTableColumn
alaDot3OamVariableRequestLeaf = _AlaDot3OamVariableRequestLeaf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 3),
    _AlaDot3OamVariableRequestLeaf_Type()
)
alaDot3OamVariableRequestLeaf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot3OamVariableRequestLeaf.setStatus("current")


class _AlaDot3OamVariableRequestRetrieveStatus_Type(Integer32):
    """Custom type alaDot3OamVariableRequestRetrieveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failed", 2),
          ("success", 3))
    )


_AlaDot3OamVariableRequestRetrieveStatus_Type.__name__ = "Integer32"
_AlaDot3OamVariableRequestRetrieveStatus_Object = MibTableColumn
alaDot3OamVariableRequestRetrieveStatus = _AlaDot3OamVariableRequestRetrieveStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 4),
    _AlaDot3OamVariableRequestRetrieveStatus_Type()
)
alaDot3OamVariableRequestRetrieveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot3OamVariableRequestRetrieveStatus.setStatus("current")
_AlaDot3OamVariableRequestRowStatus_Type = RowStatus
_AlaDot3OamVariableRequestRowStatus_Object = MibTableColumn
alaDot3OamVariableRequestRowStatus = _AlaDot3OamVariableRequestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 5),
    _AlaDot3OamVariableRequestRowStatus_Type()
)
alaDot3OamVariableRequestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDot3OamVariableRequestRowStatus.setStatus("current")


class _AlaDot3OamPortClearVariableTransactions_Type(Integer32):
    """Custom type alaDot3OamPortClearVariableTransactions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDot3OamPortClearVariableTransactions_Type.__name__ = "Integer32"
_AlaDot3OamPortClearVariableTransactions_Object = MibTableColumn
alaDot3OamPortClearVariableTransactions = _AlaDot3OamPortClearVariableTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 6),
    _AlaDot3OamPortClearVariableTransactions_Type()
)
alaDot3OamPortClearVariableTransactions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDot3OamPortClearVariableTransactions.setStatus("current")
_AlaDot3OamRetrieveResponse_ObjectIdentity = ObjectIdentity
alaDot3OamRetrieveResponse = _AlaDot3OamRetrieveResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13)
)
_AlaDot3OamRetrieveResponseTable_Object = MibTable
alaDot3OamRetrieveResponseTable = _AlaDot3OamRetrieveResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    alaDot3OamRetrieveResponseTable.setStatus("current")
_AlaDot3OamRetrieveResponseEntry_Object = MibTableRow
alaDot3OamRetrieveResponseEntry = _AlaDot3OamRetrieveResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1, 1)
)
alaDot3OamRetrieveResponseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamTransactionId"),
    (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableResponseBranch"),
    (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableResponseLeaf"),
)
if mibBuilder.loadTexts:
    alaDot3OamRetrieveResponseEntry.setStatus("current")


class _AlaDot3OamVariableResponseBranch_Type(Integer32):
    """Custom type alaDot3OamVariableResponseBranch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("attribute", 7),
          ("object", 3),
          ("package", 4))
    )


_AlaDot3OamVariableResponseBranch_Type.__name__ = "Integer32"
_AlaDot3OamVariableResponseBranch_Object = MibTableColumn
alaDot3OamVariableResponseBranch = _AlaDot3OamVariableResponseBranch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1, 1, 1),
    _AlaDot3OamVariableResponseBranch_Type()
)
alaDot3OamVariableResponseBranch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot3OamVariableResponseBranch.setStatus("current")


class _AlaDot3OamVariableResponseLeaf_Type(Integer32):
    """Custom type alaDot3OamVariableResponseLeaf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaDot3OamVariableResponseLeaf_Type.__name__ = "Integer32"
_AlaDot3OamVariableResponseLeaf_Object = MibTableColumn
alaDot3OamVariableResponseLeaf = _AlaDot3OamVariableResponseLeaf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1, 1, 2),
    _AlaDot3OamVariableResponseLeaf_Type()
)
alaDot3OamVariableResponseLeaf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot3OamVariableResponseLeaf.setStatus("current")


class _AlaDot3OamVariableResponseValue_Type(DisplayString):
    """Custom type alaDot3OamVariableResponseValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaDot3OamVariableResponseValue_Type.__name__ = "DisplayString"
_AlaDot3OamVariableResponseValue_Object = MibTableColumn
alaDot3OamVariableResponseValue = _AlaDot3OamVariableResponseValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1, 1, 3),
    _AlaDot3OamVariableResponseValue_Type()
)
alaDot3OamVariableResponseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot3OamVariableResponseValue.setStatus("current")
_AlcatelIND1Dot3OamMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1Dot3OamMIBConformance = _AlcatelIND1Dot3OamMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot3OamMIBConformance.setStatus("current")
_AlcatelIND1Dot3OamMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1Dot3OamMIBGroups = _AlcatelIND1Dot3OamMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot3OamMIBGroups.setStatus("current")
_AlcatelIND1Dot3OamMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1Dot3OamMIBCompliances = _AlcatelIND1Dot3OamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot3OamMIBCompliances.setStatus("current")
dot3OamEntry.registerAugmentions(
    ("ALCATEL-IND1-DOT3-OAM-MIB",
     "alaDot3OamEntry")
)
alaDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamLoopbackEntry.registerAugmentions(
    ("ALCATEL-IND1-DOT3-OAM-MIB",
     "alaDot3OamLoopbackEntry")
)
alaDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())
dot3OamStatsEntry.registerAugmentions(
    ("ALCATEL-IND1-DOT3-OAM-MIB",
     "alaDot3OamStatsEntry")
)
alaDot3OamStatsEntry.setIndexNames(*dot3OamStatsEntry.getIndexNames())

# Managed Objects groups

alaDot3OamBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 1)
)
alaDot3OamBaseGroup.setObjects(
      *(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamStatus"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamGlobalClearStats"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamGlobalClearEventLogs"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamGlobalClearVariableTransactions"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamMultiplePduCount"))
)
if mibBuilder.loadTexts:
    alaDot3OamBaseGroup.setStatus("current")

alaDot3OamPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 2)
)
alaDot3OamPortConfigGroup.setObjects(
      *(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamKeepAliveInterval"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamHelloInterval"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamNextTransactionId"))
)
if mibBuilder.loadTexts:
    alaDot3OamPortConfigGroup.setStatus("current")

alaDot3OamPortLoopbackControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 3)
)
alaDot3OamPortLoopbackControlGroup.setObjects(
      *(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingFramesConf"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingFramesDelay"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingStatus"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingFramesSent"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingFramesReceived"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingAverageRoundTripDelay"))
)
if mibBuilder.loadTexts:
    alaDot3OamPortLoopbackControlGroup.setStatus("current")

alaDot3OamPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 4)
)
alaDot3OamPortStatsGroup.setObjects(
    ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortClearStats")
)
if mibBuilder.loadTexts:
    alaDot3OamPortStatsGroup.setStatus("current")

alaDot3OamPortEventLogsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 5)
)
alaDot3OamPortEventLogsGroup.setObjects(
    ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortClearEventLogs")
)
if mibBuilder.loadTexts:
    alaDot3OamPortEventLogsGroup.setStatus("current")

alaDot3OamRetrieveRequestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 6)
)
alaDot3OamRetrieveRequestGroup.setObjects(
      *(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableRequestRetrieveStatus"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableRequestRowStatus"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortClearVariableTransactions"))
)
if mibBuilder.loadTexts:
    alaDot3OamRetrieveRequestGroup.setStatus("current")

alaDot3OamRetrieveResponseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 7)
)
alaDot3OamRetrieveResponseGroup.setObjects(
    ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableResponseValue")
)
if mibBuilder.loadTexts:
    alaDot3OamRetrieveResponseGroup.setStatus("current")


# Notification objects

alaDot3OamThresholdEventClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 0, 1)
)
alaDot3OamThresholdEventClear.setObjects(
      *(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"),
        ("DOT3-OAM-MIB", "dot3OamEventLogOui"),
        ("DOT3-OAM-MIB", "dot3OamEventLogType"),
        ("DOT3-OAM-MIB", "dot3OamEventLogLocation"),
        ("DOT3-OAM-MIB", "dot3OamEventLogWindowHi"),
        ("DOT3-OAM-MIB", "dot3OamEventLogWindowLo"),
        ("DOT3-OAM-MIB", "dot3OamEventLogThresholdHi"),
        ("DOT3-OAM-MIB", "dot3OamEventLogThresholdLo"),
        ("DOT3-OAM-MIB", "dot3OamEventLogValue"),
        ("DOT3-OAM-MIB", "dot3OamEventLogRunningTotal"),
        ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    alaDot3OamThresholdEventClear.setStatus(
        "current"
    )

alaDot3OamNonThresholdEventClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 0, 2)
)
alaDot3OamNonThresholdEventClear.setObjects(
      *(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"),
        ("DOT3-OAM-MIB", "dot3OamEventLogOui"),
        ("DOT3-OAM-MIB", "dot3OamEventLogType"),
        ("DOT3-OAM-MIB", "dot3OamEventLogLocation"),
        ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    alaDot3OamNonThresholdEventClear.setStatus(
        "current"
    )


# Notifications groups

alaDot3OamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 8)
)
alaDot3OamNotificationGroup.setObjects(
      *(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamThresholdEventClear"),
        ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamNonThresholdEventClear"))
)
if mibBuilder.loadTexts:
    alaDot3OamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1Dot3OamMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot3OamMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DOT3-OAM-MIB",
    **{"alcatelIND1Dot3OamMIB": alcatelIND1Dot3OamMIB,
       "alcatelIND1Dot3OamNotifications": alcatelIND1Dot3OamNotifications,
       "alaDot3OamThresholdEventClear": alaDot3OamThresholdEventClear,
       "alaDot3OamNonThresholdEventClear": alaDot3OamNonThresholdEventClear,
       "alcatelIND1Dot3OamMIBObjects": alcatelIND1Dot3OamMIBObjects,
       "alaDot3OamStatus": alaDot3OamStatus,
       "alaDot3OamGlobalClearStats": alaDot3OamGlobalClearStats,
       "alaDot3OamGlobalClearEventLogs": alaDot3OamGlobalClearEventLogs,
       "alaDot3OamGlobalClearVariableTransactions": alaDot3OamGlobalClearVariableTransactions,
       "alaDot3OamMultiplePduCount": alaDot3OamMultiplePduCount,
       "alaDot3OamPortConfig": alaDot3OamPortConfig,
       "alaDot3OamTable": alaDot3OamTable,
       "alaDot3OamEntry": alaDot3OamEntry,
       "alaDot3OamKeepAliveInterval": alaDot3OamKeepAliveInterval,
       "alaDot3OamHelloInterval": alaDot3OamHelloInterval,
       "alaDot3OamNextTransactionId": alaDot3OamNextTransactionId,
       "alaDot3OamPortLoopbackControl": alaDot3OamPortLoopbackControl,
       "alaDot3OamLoopbackTable": alaDot3OamLoopbackTable,
       "alaDot3OamLoopbackEntry": alaDot3OamLoopbackEntry,
       "alaDot3OamPortL1PingFramesConf": alaDot3OamPortL1PingFramesConf,
       "alaDot3OamPortL1PingFramesDelay": alaDot3OamPortL1PingFramesDelay,
       "alaDot3OamPortL1PingStatus": alaDot3OamPortL1PingStatus,
       "alaDot3OamPortL1PingFramesSent": alaDot3OamPortL1PingFramesSent,
       "alaDot3OamPortL1PingFramesReceived": alaDot3OamPortL1PingFramesReceived,
       "alaDot3OamPortL1PingAverageRoundTripDelay": alaDot3OamPortL1PingAverageRoundTripDelay,
       "alaDot3OamPortStats": alaDot3OamPortStats,
       "alaDot3OamStatsTable": alaDot3OamStatsTable,
       "alaDot3OamStatsEntry": alaDot3OamStatsEntry,
       "alaDot3OamPortClearStats": alaDot3OamPortClearStats,
       "alaDot3OamPortEventLogs": alaDot3OamPortEventLogs,
       "alaDot3OamEventLogTable": alaDot3OamEventLogTable,
       "alaDot3OamEventLogEntry": alaDot3OamEventLogEntry,
       "alaDot3OamPortClearEventLogs": alaDot3OamPortClearEventLogs,
       "alaDot3OamRetrieveRequest": alaDot3OamRetrieveRequest,
       "alaDot3OamRetrieveRequestTable": alaDot3OamRetrieveRequestTable,
       "alaDot3OamRetrieveRequestEntry": alaDot3OamRetrieveRequestEntry,
       "alaDot3OamTransactionId": alaDot3OamTransactionId,
       "alaDot3OamVariableRequestBranch": alaDot3OamVariableRequestBranch,
       "alaDot3OamVariableRequestLeaf": alaDot3OamVariableRequestLeaf,
       "alaDot3OamVariableRequestRetrieveStatus": alaDot3OamVariableRequestRetrieveStatus,
       "alaDot3OamVariableRequestRowStatus": alaDot3OamVariableRequestRowStatus,
       "alaDot3OamPortClearVariableTransactions": alaDot3OamPortClearVariableTransactions,
       "alaDot3OamRetrieveResponse": alaDot3OamRetrieveResponse,
       "alaDot3OamRetrieveResponseTable": alaDot3OamRetrieveResponseTable,
       "alaDot3OamRetrieveResponseEntry": alaDot3OamRetrieveResponseEntry,
       "alaDot3OamVariableResponseBranch": alaDot3OamVariableResponseBranch,
       "alaDot3OamVariableResponseLeaf": alaDot3OamVariableResponseLeaf,
       "alaDot3OamVariableResponseValue": alaDot3OamVariableResponseValue,
       "alcatelIND1Dot3OamMIBConformance": alcatelIND1Dot3OamMIBConformance,
       "alcatelIND1Dot3OamMIBGroups": alcatelIND1Dot3OamMIBGroups,
       "alaDot3OamBaseGroup": alaDot3OamBaseGroup,
       "alaDot3OamPortConfigGroup": alaDot3OamPortConfigGroup,
       "alaDot3OamPortLoopbackControlGroup": alaDot3OamPortLoopbackControlGroup,
       "alaDot3OamPortStatsGroup": alaDot3OamPortStatsGroup,
       "alaDot3OamPortEventLogsGroup": alaDot3OamPortEventLogsGroup,
       "alaDot3OamRetrieveRequestGroup": alaDot3OamRetrieveRequestGroup,
       "alaDot3OamRetrieveResponseGroup": alaDot3OamRetrieveResponseGroup,
       "alaDot3OamNotificationGroup": alaDot3OamNotificationGroup,
       "alcatelIND1Dot3OamMIBCompliances": alcatelIND1Dot3OamMIBCompliances,
       "alcatelIND1Dot3OamMIBCompliance": alcatelIND1Dot3OamMIBCompliance}
)
