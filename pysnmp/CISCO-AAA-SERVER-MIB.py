# SNMP MIB module (CISCO-AAA-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AAA-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:24 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoAAAServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56)
)
ciscoAAAServerMIB.setRevisions(
        ("2003-11-17 00:00",
         "2002-03-28 00:00",
         "2000-01-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAAAProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("kerberos", 4),
          ("ldap", 3),
          ("ntlm", 5),
          ("other", 7),
          ("radius", 2),
          ("sdi", 6),
          ("tacacsplus", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CAAAServerMIBObjects_ObjectIdentity = ObjectIdentity
cAAAServerMIBObjects = _CAAAServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1)
)
_CasConfig_ObjectIdentity = ObjectIdentity
casConfig = _CasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1)
)
_CasServerStateChangeEnable_Type = TruthValue
_CasServerStateChangeEnable_Object = MibScalar
casServerStateChangeEnable = _CasServerStateChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 1),
    _CasServerStateChangeEnable_Type()
)
casServerStateChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casServerStateChangeEnable.setStatus("current")
_CasConfigTable_Object = MibTable
casConfigTable = _CasConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2)
)
if mibBuilder.loadTexts:
    casConfigTable.setStatus("current")
_CasConfigEntry_Object = MibTableRow
casConfigEntry = _CasConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1)
)
casConfigEntry.setIndexNames(
    (0, "CISCO-AAA-SERVER-MIB", "casProtocol"),
    (0, "CISCO-AAA-SERVER-MIB", "casIndex"),
)
if mibBuilder.loadTexts:
    casConfigEntry.setStatus("current")
_CasProtocol_Type = CiscoAAAProtocol
_CasProtocol_Object = MibTableColumn
casProtocol = _CasProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 1),
    _CasProtocol_Type()
)
casProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casProtocol.setStatus("current")


class _CasIndex_Type(Unsigned32):
    """Custom type casIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CasIndex_Type.__name__ = "Unsigned32"
_CasIndex_Object = MibTableColumn
casIndex = _CasIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 2),
    _CasIndex_Type()
)
casIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casIndex.setStatus("current")
_CasAddress_Type = IpAddress
_CasAddress_Object = MibTableColumn
casAddress = _CasAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 3),
    _CasAddress_Type()
)
casAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casAddress.setStatus("current")


class _CasAuthenPort_Type(Integer32):
    """Custom type casAuthenPort based on Integer32"""
    defaultValue = 1645

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CasAuthenPort_Type.__name__ = "Integer32"
_CasAuthenPort_Object = MibTableColumn
casAuthenPort = _CasAuthenPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 4),
    _CasAuthenPort_Type()
)
casAuthenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casAuthenPort.setStatus("current")


class _CasAcctPort_Type(Integer32):
    """Custom type casAcctPort based on Integer32"""
    defaultValue = 1646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CasAcctPort_Type.__name__ = "Integer32"
_CasAcctPort_Object = MibTableColumn
casAcctPort = _CasAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 5),
    _CasAcctPort_Type()
)
casAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casAcctPort.setStatus("current")
_CasKey_Type = DisplayString
_CasKey_Object = MibTableColumn
casKey = _CasKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 6),
    _CasKey_Type()
)
casKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casKey.setStatus("current")


class _CasPriority_Type(Unsigned32):
    """Custom type casPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CasPriority_Type.__name__ = "Unsigned32"
_CasPriority_Object = MibTableColumn
casPriority = _CasPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 7),
    _CasPriority_Type()
)
casPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casPriority.setStatus("current")
_CasConfigRowStatus_Type = RowStatus
_CasConfigRowStatus_Object = MibTableColumn
casConfigRowStatus = _CasConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 8),
    _CasConfigRowStatus_Type()
)
casConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casConfigRowStatus.setStatus("current")
_CasStatistics_ObjectIdentity = ObjectIdentity
casStatistics = _CasStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2)
)
_CasStatisticsTable_Object = MibTable
casStatisticsTable = _CasStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1)
)
if mibBuilder.loadTexts:
    casStatisticsTable.setStatus("current")
_CasStatisticsEntry_Object = MibTableRow
casStatisticsEntry = _CasStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    casStatisticsEntry.setStatus("current")
_CasAuthenRequests_Type = Counter32
_CasAuthenRequests_Object = MibTableColumn
casAuthenRequests = _CasAuthenRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 1),
    _CasAuthenRequests_Type()
)
casAuthenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenRequests.setStatus("current")
_CasAuthenRequestTimeouts_Type = Counter32
_CasAuthenRequestTimeouts_Object = MibTableColumn
casAuthenRequestTimeouts = _CasAuthenRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 2),
    _CasAuthenRequestTimeouts_Type()
)
casAuthenRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenRequestTimeouts.setStatus("current")
_CasAuthenUnexpectedResponses_Type = Counter32
_CasAuthenUnexpectedResponses_Object = MibTableColumn
casAuthenUnexpectedResponses = _CasAuthenUnexpectedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 3),
    _CasAuthenUnexpectedResponses_Type()
)
casAuthenUnexpectedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenUnexpectedResponses.setStatus("current")
_CasAuthenServerErrorResponses_Type = Counter32
_CasAuthenServerErrorResponses_Object = MibTableColumn
casAuthenServerErrorResponses = _CasAuthenServerErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 4),
    _CasAuthenServerErrorResponses_Type()
)
casAuthenServerErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenServerErrorResponses.setStatus("current")
_CasAuthenIncorrectResponses_Type = Counter32
_CasAuthenIncorrectResponses_Object = MibTableColumn
casAuthenIncorrectResponses = _CasAuthenIncorrectResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 5),
    _CasAuthenIncorrectResponses_Type()
)
casAuthenIncorrectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenIncorrectResponses.setStatus("current")
_CasAuthenResponseTime_Type = TimeInterval
_CasAuthenResponseTime_Object = MibTableColumn
casAuthenResponseTime = _CasAuthenResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 6),
    _CasAuthenResponseTime_Type()
)
casAuthenResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenResponseTime.setStatus("current")
_CasAuthenTransactionSuccesses_Type = Counter32
_CasAuthenTransactionSuccesses_Object = MibTableColumn
casAuthenTransactionSuccesses = _CasAuthenTransactionSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 7),
    _CasAuthenTransactionSuccesses_Type()
)
casAuthenTransactionSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenTransactionSuccesses.setStatus("current")
_CasAuthenTransactionFailures_Type = Counter32
_CasAuthenTransactionFailures_Object = MibTableColumn
casAuthenTransactionFailures = _CasAuthenTransactionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 8),
    _CasAuthenTransactionFailures_Type()
)
casAuthenTransactionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenTransactionFailures.setStatus("current")
_CasAuthorRequests_Type = Counter32
_CasAuthorRequests_Object = MibTableColumn
casAuthorRequests = _CasAuthorRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 9),
    _CasAuthorRequests_Type()
)
casAuthorRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorRequests.setStatus("current")
_CasAuthorRequestTimeouts_Type = Counter32
_CasAuthorRequestTimeouts_Object = MibTableColumn
casAuthorRequestTimeouts = _CasAuthorRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 10),
    _CasAuthorRequestTimeouts_Type()
)
casAuthorRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorRequestTimeouts.setStatus("current")
_CasAuthorUnexpectedResponses_Type = Counter32
_CasAuthorUnexpectedResponses_Object = MibTableColumn
casAuthorUnexpectedResponses = _CasAuthorUnexpectedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 11),
    _CasAuthorUnexpectedResponses_Type()
)
casAuthorUnexpectedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorUnexpectedResponses.setStatus("current")
_CasAuthorServerErrorResponses_Type = Counter32
_CasAuthorServerErrorResponses_Object = MibTableColumn
casAuthorServerErrorResponses = _CasAuthorServerErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 12),
    _CasAuthorServerErrorResponses_Type()
)
casAuthorServerErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorServerErrorResponses.setStatus("current")
_CasAuthorIncorrectResponses_Type = Counter32
_CasAuthorIncorrectResponses_Object = MibTableColumn
casAuthorIncorrectResponses = _CasAuthorIncorrectResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 13),
    _CasAuthorIncorrectResponses_Type()
)
casAuthorIncorrectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorIncorrectResponses.setStatus("current")
_CasAuthorResponseTime_Type = TimeInterval
_CasAuthorResponseTime_Object = MibTableColumn
casAuthorResponseTime = _CasAuthorResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 14),
    _CasAuthorResponseTime_Type()
)
casAuthorResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorResponseTime.setStatus("current")
_CasAuthorTransactionSuccesses_Type = Counter32
_CasAuthorTransactionSuccesses_Object = MibTableColumn
casAuthorTransactionSuccesses = _CasAuthorTransactionSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 15),
    _CasAuthorTransactionSuccesses_Type()
)
casAuthorTransactionSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorTransactionSuccesses.setStatus("current")
_CasAuthorTransactionFailures_Type = Counter32
_CasAuthorTransactionFailures_Object = MibTableColumn
casAuthorTransactionFailures = _CasAuthorTransactionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 16),
    _CasAuthorTransactionFailures_Type()
)
casAuthorTransactionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorTransactionFailures.setStatus("current")
_CasAcctRequests_Type = Counter32
_CasAcctRequests_Object = MibTableColumn
casAcctRequests = _CasAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 17),
    _CasAcctRequests_Type()
)
casAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequests.setStatus("current")
_CasAcctRequestTimeouts_Type = Counter32
_CasAcctRequestTimeouts_Object = MibTableColumn
casAcctRequestTimeouts = _CasAcctRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 18),
    _CasAcctRequestTimeouts_Type()
)
casAcctRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequestTimeouts.setStatus("current")
_CasAcctUnexpectedResponses_Type = Counter32
_CasAcctUnexpectedResponses_Object = MibTableColumn
casAcctUnexpectedResponses = _CasAcctUnexpectedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 19),
    _CasAcctUnexpectedResponses_Type()
)
casAcctUnexpectedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctUnexpectedResponses.setStatus("current")
_CasAcctServerErrorResponses_Type = Counter32
_CasAcctServerErrorResponses_Object = MibTableColumn
casAcctServerErrorResponses = _CasAcctServerErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 20),
    _CasAcctServerErrorResponses_Type()
)
casAcctServerErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctServerErrorResponses.setStatus("current")
_CasAcctIncorrectResponses_Type = Counter32
_CasAcctIncorrectResponses_Object = MibTableColumn
casAcctIncorrectResponses = _CasAcctIncorrectResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 21),
    _CasAcctIncorrectResponses_Type()
)
casAcctIncorrectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctIncorrectResponses.setStatus("current")
_CasAcctResponseTime_Type = TimeInterval
_CasAcctResponseTime_Object = MibTableColumn
casAcctResponseTime = _CasAcctResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 22),
    _CasAcctResponseTime_Type()
)
casAcctResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctResponseTime.setStatus("current")
_CasAcctTransactionSuccesses_Type = Counter32
_CasAcctTransactionSuccesses_Object = MibTableColumn
casAcctTransactionSuccesses = _CasAcctTransactionSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 23),
    _CasAcctTransactionSuccesses_Type()
)
casAcctTransactionSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctTransactionSuccesses.setStatus("current")
_CasAcctTransactionFailures_Type = Counter32
_CasAcctTransactionFailures_Object = MibTableColumn
casAcctTransactionFailures = _CasAcctTransactionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 24),
    _CasAcctTransactionFailures_Type()
)
casAcctTransactionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctTransactionFailures.setStatus("current")


class _CasState_Type(Integer32):
    """Custom type casState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dead", 2),
          ("up", 1))
    )


_CasState_Type.__name__ = "Integer32"
_CasState_Object = MibTableColumn
casState = _CasState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 25),
    _CasState_Type()
)
casState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casState.setStatus("current")
_CasCurrentStateDuration_Type = TimeInterval
_CasCurrentStateDuration_Object = MibTableColumn
casCurrentStateDuration = _CasCurrentStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 26),
    _CasCurrentStateDuration_Type()
)
casCurrentStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casCurrentStateDuration.setStatus("current")
_CasPreviousStateDuration_Type = TimeInterval
_CasPreviousStateDuration_Object = MibTableColumn
casPreviousStateDuration = _CasPreviousStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 27),
    _CasPreviousStateDuration_Type()
)
casPreviousStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casPreviousStateDuration.setStatus("current")
_CasTotalDeadTime_Type = TimeInterval
_CasTotalDeadTime_Object = MibTableColumn
casTotalDeadTime = _CasTotalDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 28),
    _CasTotalDeadTime_Type()
)
casTotalDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casTotalDeadTime.setStatus("current")
_CasDeadCount_Type = Counter32
_CasDeadCount_Object = MibTableColumn
casDeadCount = _CasDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 29),
    _CasDeadCount_Type()
)
casDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casDeadCount.setStatus("current")
_CAAAServerMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cAAAServerMIBNotificationPrefix = _CAAAServerMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 2)
)
_CAAAServerMIBNotifications_ObjectIdentity = ObjectIdentity
cAAAServerMIBNotifications = _CAAAServerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 2, 0)
)
_CAAAServerMIBConformance_ObjectIdentity = ObjectIdentity
cAAAServerMIBConformance = _CAAAServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3)
)
_CasMIBCompliances_ObjectIdentity = ObjectIdentity
casMIBCompliances = _CasMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 1)
)
_CasMIBGroups_ObjectIdentity = ObjectIdentity
casMIBGroups = _CasMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2)
)
casConfigEntry.registerAugmentions(
    ("CISCO-AAA-SERVER-MIB",
     "casStatisticsEntry")
)
casStatisticsEntry.setIndexNames(*casConfigEntry.getIndexNames())

# Managed Objects groups

casStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 1)
)
casStatisticsGroup.setObjects(
      *(("CISCO-AAA-SERVER-MIB", "casAuthenRequests"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenRequestTimeouts"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenUnexpectedResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenServerErrorResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenIncorrectResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenResponseTime"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenTransactionSuccesses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenTransactionFailures"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorRequests"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorRequestTimeouts"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorUnexpectedResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorServerErrorResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorIncorrectResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorResponseTime"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorTransactionSuccesses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorTransactionFailures"),
        ("CISCO-AAA-SERVER-MIB", "casAcctRequests"),
        ("CISCO-AAA-SERVER-MIB", "casAcctRequestTimeouts"),
        ("CISCO-AAA-SERVER-MIB", "casAcctUnexpectedResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAcctServerErrorResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAcctIncorrectResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAcctResponseTime"),
        ("CISCO-AAA-SERVER-MIB", "casAcctTransactionSuccesses"),
        ("CISCO-AAA-SERVER-MIB", "casAcctTransactionFailures"),
        ("CISCO-AAA-SERVER-MIB", "casState"),
        ("CISCO-AAA-SERVER-MIB", "casCurrentStateDuration"),
        ("CISCO-AAA-SERVER-MIB", "casPreviousStateDuration"),
        ("CISCO-AAA-SERVER-MIB", "casTotalDeadTime"),
        ("CISCO-AAA-SERVER-MIB", "casDeadCount"))
)
if mibBuilder.loadTexts:
    casStatisticsGroup.setStatus("current")

casConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 2)
)
casConfigGroup.setObjects(
      *(("CISCO-AAA-SERVER-MIB", "casServerStateChangeEnable"),
        ("CISCO-AAA-SERVER-MIB", "casAddress"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenPort"),
        ("CISCO-AAA-SERVER-MIB", "casAcctPort"),
        ("CISCO-AAA-SERVER-MIB", "casKey"),
        ("CISCO-AAA-SERVER-MIB", "casPriority"),
        ("CISCO-AAA-SERVER-MIB", "casConfigRowStatus"))
)
if mibBuilder.loadTexts:
    casConfigGroup.setStatus("current")


# Notification objects

casServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 2, 0, 1)
)
casServerStateChange.setObjects(
      *(("CISCO-AAA-SERVER-MIB", "casState"),
        ("CISCO-AAA-SERVER-MIB", "casPreviousStateDuration"),
        ("CISCO-AAA-SERVER-MIB", "casTotalDeadTime"))
)
if mibBuilder.loadTexts:
    casServerStateChange.setStatus(
        "current"
    )


# Notifications groups

casServerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 3)
)
casServerNotificationGroup.setObjects(
    ("CISCO-AAA-SERVER-MIB", "casServerStateChange")
)
if mibBuilder.loadTexts:
    casServerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

casMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 1, 1)
)
if mibBuilder.loadTexts:
    casMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AAA-SERVER-MIB",
    **{"CiscoAAAProtocol": CiscoAAAProtocol,
       "ciscoAAAServerMIB": ciscoAAAServerMIB,
       "cAAAServerMIBObjects": cAAAServerMIBObjects,
       "casConfig": casConfig,
       "casServerStateChangeEnable": casServerStateChangeEnable,
       "casConfigTable": casConfigTable,
       "casConfigEntry": casConfigEntry,
       "casProtocol": casProtocol,
       "casIndex": casIndex,
       "casAddress": casAddress,
       "casAuthenPort": casAuthenPort,
       "casAcctPort": casAcctPort,
       "casKey": casKey,
       "casPriority": casPriority,
       "casConfigRowStatus": casConfigRowStatus,
       "casStatistics": casStatistics,
       "casStatisticsTable": casStatisticsTable,
       "casStatisticsEntry": casStatisticsEntry,
       "casAuthenRequests": casAuthenRequests,
       "casAuthenRequestTimeouts": casAuthenRequestTimeouts,
       "casAuthenUnexpectedResponses": casAuthenUnexpectedResponses,
       "casAuthenServerErrorResponses": casAuthenServerErrorResponses,
       "casAuthenIncorrectResponses": casAuthenIncorrectResponses,
       "casAuthenResponseTime": casAuthenResponseTime,
       "casAuthenTransactionSuccesses": casAuthenTransactionSuccesses,
       "casAuthenTransactionFailures": casAuthenTransactionFailures,
       "casAuthorRequests": casAuthorRequests,
       "casAuthorRequestTimeouts": casAuthorRequestTimeouts,
       "casAuthorUnexpectedResponses": casAuthorUnexpectedResponses,
       "casAuthorServerErrorResponses": casAuthorServerErrorResponses,
       "casAuthorIncorrectResponses": casAuthorIncorrectResponses,
       "casAuthorResponseTime": casAuthorResponseTime,
       "casAuthorTransactionSuccesses": casAuthorTransactionSuccesses,
       "casAuthorTransactionFailures": casAuthorTransactionFailures,
       "casAcctRequests": casAcctRequests,
       "casAcctRequestTimeouts": casAcctRequestTimeouts,
       "casAcctUnexpectedResponses": casAcctUnexpectedResponses,
       "casAcctServerErrorResponses": casAcctServerErrorResponses,
       "casAcctIncorrectResponses": casAcctIncorrectResponses,
       "casAcctResponseTime": casAcctResponseTime,
       "casAcctTransactionSuccesses": casAcctTransactionSuccesses,
       "casAcctTransactionFailures": casAcctTransactionFailures,
       "casState": casState,
       "casCurrentStateDuration": casCurrentStateDuration,
       "casPreviousStateDuration": casPreviousStateDuration,
       "casTotalDeadTime": casTotalDeadTime,
       "casDeadCount": casDeadCount,
       "cAAAServerMIBNotificationPrefix": cAAAServerMIBNotificationPrefix,
       "cAAAServerMIBNotifications": cAAAServerMIBNotifications,
       "casServerStateChange": casServerStateChange,
       "cAAAServerMIBConformance": cAAAServerMIBConformance,
       "casMIBCompliances": casMIBCompliances,
       "casMIBCompliance": casMIBCompliance,
       "casMIBGroups": casMIBGroups,
       "casStatisticsGroup": casStatisticsGroup,
       "casConfigGroup": casConfigGroup,
       "casServerNotificationGroup": casServerNotificationGroup}
)
