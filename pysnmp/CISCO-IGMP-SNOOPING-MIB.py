# SNMP MIB module (CISCO-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IGMP-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:17 2024
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

(VlanIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-PRIVATE-VLAN-MIB",
    "VlanIndexOrZero")

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPortList,
 CiscoPortListRange) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPortList",
    "CiscoPortListRange")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIgmpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263)
)
ciscoIgmpSnoopingMIB.setRevisions(
        ("2010-06-08 00:00",
         "2007-11-08 00:00",
         "2004-04-02 00:00",
         "2003-03-24 00:00",
         "2002-05-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CisIgmpMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("igmpCgmp", 3),
          ("igmpOnly", 2))
    )



class CisIgmpVersion(Integer32, TextualConvention):
    status = "current"
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
        *(("unknown", 4),
          ("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIgmpSnoopingNotification_ObjectIdentity = ObjectIdentity
ciscoIgmpSnoopingNotification = _CiscoIgmpSnoopingNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 0)
)
_CiscoIgmpSnoopingMIBObject_ObjectIdentity = ObjectIdentity
ciscoIgmpSnoopingMIBObject = _CiscoIgmpSnoopingMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1)
)
_CisSystemInfo_ObjectIdentity = ObjectIdentity
cisSystemInfo = _CisSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1)
)
_CisIgmpSnoopingEnabled_Type = TruthValue
_CisIgmpSnoopingEnabled_Object = MibScalar
cisIgmpSnoopingEnabled = _CisIgmpSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 1),
    _CisIgmpSnoopingEnabled_Type()
)
cisIgmpSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpSnoopingEnabled.setStatus("current")
_CisV3ProcessEnabledAdminStatus_Type = TruthValue
_CisV3ProcessEnabledAdminStatus_Object = MibScalar
cisV3ProcessEnabledAdminStatus = _CisV3ProcessEnabledAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 2),
    _CisV3ProcessEnabledAdminStatus_Type()
)
cisV3ProcessEnabledAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisV3ProcessEnabledAdminStatus.setStatus("current")
_CisV3ProcessEnabledOperStatus_Type = TruthValue
_CisV3ProcessEnabledOperStatus_Object = MibScalar
cisV3ProcessEnabledOperStatus = _CisV3ProcessEnabledOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 3),
    _CisV3ProcessEnabledOperStatus_Type()
)
cisV3ProcessEnabledOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisV3ProcessEnabledOperStatus.setStatus("current")
_CisFastLeaveEnabled_Type = TruthValue
_CisFastLeaveEnabled_Object = MibScalar
cisFastLeaveEnabled = _CisFastLeaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 4),
    _CisFastLeaveEnabled_Type()
)
cisFastLeaveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisFastLeaveEnabled.setStatus("current")
_CisFastBlockEnabled_Type = TruthValue
_CisFastBlockEnabled_Object = MibScalar
cisFastBlockEnabled = _CisFastBlockEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 5),
    _CisFastBlockEnabled_Type()
)
cisFastBlockEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisFastBlockEnabled.setStatus("current")
_CisAdminMode_Type = CisIgmpMode
_CisAdminMode_Object = MibScalar
cisAdminMode = _CisAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 6),
    _CisAdminMode_Type()
)
cisAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisAdminMode.setStatus("current")
_CisOperMode_Type = CisIgmpMode
_CisOperMode_Object = MibScalar
cisOperMode = _CisOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 7),
    _CisOperMode_Type()
)
cisOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisOperMode.setStatus("current")


class _CisLeaveQueryType_Type(Integer32):
    """Custom type cisLeaveQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("generalQuery", 1),
          ("macGenQuery", 2))
    )


_CisLeaveQueryType_Type.__name__ = "Integer32"
_CisLeaveQueryType_Object = MibScalar
cisLeaveQueryType = _CisLeaveQueryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 8),
    _CisLeaveQueryType_Type()
)
cisLeaveQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisLeaveQueryType.setStatus("current")


class _CisAddressAliasingMode_Type(Integer32):
    """Custom type cisAddressAliasingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallback", 2),
          ("normal", 1))
    )


_CisAddressAliasingMode_Type.__name__ = "Integer32"
_CisAddressAliasingMode_Object = MibScalar
cisAddressAliasingMode = _CisAddressAliasingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 9),
    _CisAddressAliasingMode_Type()
)
cisAddressAliasingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisAddressAliasingMode.setStatus("current")
_CisFallbackTime_Type = TimeStamp
_CisFallbackTime_Object = MibScalar
cisFallbackTime = _CisFallbackTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 10),
    _CisFallbackTime_Type()
)
cisFallbackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisFallbackTime.setStatus("current")
_CisReportSuppressionEnabled_Type = TruthValue
_CisReportSuppressionEnabled_Object = MibScalar
cisReportSuppressionEnabled = _CisReportSuppressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 11),
    _CisReportSuppressionEnabled_Type()
)
cisReportSuppressionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisReportSuppressionEnabled.setStatus("current")


class _CisTopoChangeFloodQueryCount_Type(Unsigned32):
    """Custom type cisTopoChangeFloodQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CisTopoChangeFloodQueryCount_Type.__name__ = "Unsigned32"
_CisTopoChangeFloodQueryCount_Object = MibScalar
cisTopoChangeFloodQueryCount = _CisTopoChangeFloodQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 12),
    _CisTopoChangeFloodQueryCount_Type()
)
cisTopoChangeFloodQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisTopoChangeFloodQueryCount.setStatus("current")
_CisTopoChangeQuerySolicitEnabled_Type = TruthValue
_CisTopoChangeQuerySolicitEnabled_Object = MibScalar
cisTopoChangeQuerySolicitEnabled = _CisTopoChangeQuerySolicitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 13),
    _CisTopoChangeQuerySolicitEnabled_Type()
)
cisTopoChangeQuerySolicitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisTopoChangeQuerySolicitEnabled.setStatus("current")
_CisSourceOnlyLearningEnabled_Type = TruthValue
_CisSourceOnlyLearningEnabled_Object = MibScalar
cisSourceOnlyLearningEnabled = _CisSourceOnlyLearningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 14),
    _CisSourceOnlyLearningEnabled_Type()
)
cisSourceOnlyLearningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisSourceOnlyLearningEnabled.setStatus("current")


class _CisSourceOnlyEntryAgeTime_Type(Integer32):
    """Custom type cisSourceOnlyEntryAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2880),
    )


_CisSourceOnlyEntryAgeTime_Type.__name__ = "Integer32"
_CisSourceOnlyEntryAgeTime_Object = MibScalar
cisSourceOnlyEntryAgeTime = _CisSourceOnlyEntryAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 15),
    _CisSourceOnlyEntryAgeTime_Type()
)
cisSourceOnlyEntryAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisSourceOnlyEntryAgeTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cisSourceOnlyEntryAgeTime.setUnits("minutes")


class _CisV3SnoopingSupport_Type(Integer32):
    """Custom type cisV3SnoopingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("full", 2))
    )


_CisV3SnoopingSupport_Type.__name__ = "Integer32"
_CisV3SnoopingSupport_Object = MibScalar
cisV3SnoopingSupport = _CisV3SnoopingSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 16),
    _CisV3SnoopingSupport_Type()
)
cisV3SnoopingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisV3SnoopingSupport.setStatus("current")
_CisSourceOnlyEntryAgingTime_Type = Unsigned32
_CisSourceOnlyEntryAgingTime_Object = MibScalar
cisSourceOnlyEntryAgingTime = _CisSourceOnlyEntryAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 17),
    _CisSourceOnlyEntryAgingTime_Type()
)
cisSourceOnlyEntryAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisSourceOnlyEntryAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cisSourceOnlyEntryAgingTime.setUnits("seconds")


class _CisRobustnessVariable_Type(Unsigned32):
    """Custom type cisRobustnessVariable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CisRobustnessVariable_Type.__name__ = "Unsigned32"
_CisRobustnessVariable_Object = MibScalar
cisRobustnessVariable = _CisRobustnessVariable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 18),
    _CisRobustnessVariable_Type()
)
cisRobustnessVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisRobustnessVariable.setStatus("current")


class _CisLastMemberQueryInterval_Type(Unsigned32):
    """Custom type cisLastMemberQueryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CisLastMemberQueryInterval_Type.__name__ = "Unsigned32"
_CisLastMemberQueryInterval_Object = MibScalar
cisLastMemberQueryInterval = _CisLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 19),
    _CisLastMemberQueryInterval_Type()
)
cisLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cisLastMemberQueryInterval.setUnits("milliseconds")


class _CisLastMemberQueryCount_Type(Unsigned32):
    """Custom type cisLastMemberQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CisLastMemberQueryCount_Type.__name__ = "Unsigned32"
_CisLastMemberQueryCount_Object = MibScalar
cisLastMemberQueryCount = _CisLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 20),
    _CisLastMemberQueryCount_Type()
)
cisLastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisLastMemberQueryCount.setStatus("current")
_CisTimeToLiveCheckEnabled_Type = TruthValue
_CisTimeToLiveCheckEnabled_Object = MibScalar
cisTimeToLiveCheckEnabled = _CisTimeToLiveCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 21),
    _CisTimeToLiveCheckEnabled_Type()
)
cisTimeToLiveCheckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisTimeToLiveCheckEnabled.setStatus("current")
_CisRouterAlertCheckEnabled_Type = TruthValue
_CisRouterAlertCheckEnabled_Object = MibScalar
cisRouterAlertCheckEnabled = _CisRouterAlertCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 1, 22),
    _CisRouterAlertCheckEnabled_Type()
)
cisRouterAlertCheckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisRouterAlertCheckEnabled.setStatus("current")
_CisStatisticsInfo_ObjectIdentity = ObjectIdentity
cisStatisticsInfo = _CisStatisticsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2)
)
_CisInterfaceStatsTable_Object = MibTable
cisInterfaceStatsTable = _CisInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cisInterfaceStatsTable.setStatus("current")
_CisInterfaceStatsEntry_Object = MibTableRow
cisInterfaceStatsEntry = _CisInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1)
)
cisInterfaceStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cisInterfaceStatsEntry.setStatus("current")
_CisTxGeneralQueries_Type = Counter32
_CisTxGeneralQueries_Object = MibTableColumn
cisTxGeneralQueries = _CisTxGeneralQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 1),
    _CisTxGeneralQueries_Type()
)
cisTxGeneralQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisTxGeneralQueries.setStatus("current")
_CisTxGroupSpecificQueries_Type = Counter32
_CisTxGroupSpecificQueries_Object = MibTableColumn
cisTxGroupSpecificQueries = _CisTxGroupSpecificQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 2),
    _CisTxGroupSpecificQueries_Type()
)
cisTxGroupSpecificQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisTxGroupSpecificQueries.setStatus("current")
_CisTxReports_Type = Counter32
_CisTxReports_Object = MibTableColumn
cisTxReports = _CisTxReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 3),
    _CisTxReports_Type()
)
cisTxReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisTxReports.setStatus("current")
_CisTxLeaves_Type = Counter32
_CisTxLeaves_Object = MibTableColumn
cisTxLeaves = _CisTxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 4),
    _CisTxLeaves_Type()
)
cisTxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisTxLeaves.setStatus("current")
_CisRxGeneralQueries_Type = Counter32
_CisRxGeneralQueries_Object = MibTableColumn
cisRxGeneralQueries = _CisRxGeneralQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 5),
    _CisRxGeneralQueries_Type()
)
cisRxGeneralQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxGeneralQueries.setStatus("current")
_CisRxGroupSpecificQueries_Type = Counter32
_CisRxGroupSpecificQueries_Object = MibTableColumn
cisRxGroupSpecificQueries = _CisRxGroupSpecificQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 6),
    _CisRxGroupSpecificQueries_Type()
)
cisRxGroupSpecificQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxGroupSpecificQueries.setStatus("current")
_CisRxReports_Type = Counter32
_CisRxReports_Object = MibTableColumn
cisRxReports = _CisRxReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 7),
    _CisRxReports_Type()
)
cisRxReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxReports.setStatus("current")
_CisRxLeaves_Type = Counter32
_CisRxLeaves_Object = MibTableColumn
cisRxLeaves = _CisRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 8),
    _CisRxLeaves_Type()
)
cisRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxLeaves.setStatus("current")
_CisRxValidPackets_Type = Counter32
_CisRxValidPackets_Object = MibTableColumn
cisRxValidPackets = _CisRxValidPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 9),
    _CisRxValidPackets_Type()
)
cisRxValidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxValidPackets.setStatus("current")
_CisRxInvalidPackets_Type = Counter32
_CisRxInvalidPackets_Object = MibTableColumn
cisRxInvalidPackets = _CisRxInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 10),
    _CisRxInvalidPackets_Type()
)
cisRxInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxInvalidPackets.setStatus("current")
_CisRxOtherPackets_Type = Counter32
_CisRxOtherPackets_Object = MibTableColumn
cisRxOtherPackets = _CisRxOtherPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 11),
    _CisRxOtherPackets_Type()
)
cisRxOtherPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxOtherPackets.setStatus("current")
_CisRxMACGeneralQueries_Type = Counter32
_CisRxMACGeneralQueries_Object = MibTableColumn
cisRxMACGeneralQueries = _CisRxMACGeneralQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 12),
    _CisRxMACGeneralQueries_Type()
)
cisRxMACGeneralQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxMACGeneralQueries.setStatus("current")
_CisRxTopoNotifications_Type = Counter32
_CisRxTopoNotifications_Object = MibTableColumn
cisRxTopoNotifications = _CisRxTopoNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 13),
    _CisRxTopoNotifications_Type()
)
cisRxTopoNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisRxTopoNotifications.setStatus("current")
_CisV3Allows_Type = Counter32
_CisV3Allows_Object = MibTableColumn
cisV3Allows = _CisV3Allows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 14),
    _CisV3Allows_Type()
)
cisV3Allows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisV3Allows.setStatus("current")
_CisV3Blocks_Type = Counter32
_CisV3Blocks_Object = MibTableColumn
cisV3Blocks = _CisV3Blocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 15),
    _CisV3Blocks_Type()
)
cisV3Blocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisV3Blocks.setStatus("current")
_CisV3IsIncluded_Type = Counter32
_CisV3IsIncluded_Object = MibTableColumn
cisV3IsIncluded = _CisV3IsIncluded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 16),
    _CisV3IsIncluded_Type()
)
cisV3IsIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisV3IsIncluded.setStatus("current")
_CisV3IsExcluded_Type = Counter32
_CisV3IsExcluded_Object = MibTableColumn
cisV3IsExcluded = _CisV3IsExcluded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 17),
    _CisV3IsExcluded_Type()
)
cisV3IsExcluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisV3IsExcluded.setStatus("current")
_CisV3ToIncluded_Type = Counter32
_CisV3ToIncluded_Object = MibTableColumn
cisV3ToIncluded = _CisV3ToIncluded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 18),
    _CisV3ToIncluded_Type()
)
cisV3ToIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisV3ToIncluded.setStatus("current")
_CisV3ToExcluded_Type = Counter32
_CisV3ToExcluded_Object = MibTableColumn
cisV3ToExcluded = _CisV3ToExcluded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 2, 1, 1, 19),
    _CisV3ToExcluded_Type()
)
cisV3ToExcluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisV3ToExcluded.setStatus("current")
_CisRateLimitInfo_ObjectIdentity = ObjectIdentity
cisRateLimitInfo = _CisRateLimitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 3)
)
_CisGeneralQueryRateLimit_Type = Unsigned32
_CisGeneralQueryRateLimit_Object = MibScalar
cisGeneralQueryRateLimit = _CisGeneralQueryRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 3, 1),
    _CisGeneralQueryRateLimit_Type()
)
cisGeneralQueryRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisGeneralQueryRateLimit.setStatus("deprecated")
if mibBuilder.loadTexts:
    cisGeneralQueryRateLimit.setUnits("packets per 30 seconds")
_CisDvmrpRateLimit_Type = Unsigned32
_CisDvmrpRateLimit_Object = MibScalar
cisDvmrpRateLimit = _CisDvmrpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 3, 2),
    _CisDvmrpRateLimit_Type()
)
cisDvmrpRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisDvmrpRateLimit.setStatus("deprecated")
if mibBuilder.loadTexts:
    cisDvmrpRateLimit.setUnits("packets per 30 seconds")
_CisMospf1RateLimit_Type = Unsigned32
_CisMospf1RateLimit_Object = MibScalar
cisMospf1RateLimit = _CisMospf1RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 3, 3),
    _CisMospf1RateLimit_Type()
)
cisMospf1RateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisMospf1RateLimit.setStatus("deprecated")
if mibBuilder.loadTexts:
    cisMospf1RateLimit.setUnits("packets per 30 seconds")
_CisMospf2RateLimit_Type = Unsigned32
_CisMospf2RateLimit_Object = MibScalar
cisMospf2RateLimit = _CisMospf2RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 3, 4),
    _CisMospf2RateLimit_Type()
)
cisMospf2RateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisMospf2RateLimit.setStatus("deprecated")
if mibBuilder.loadTexts:
    cisMospf2RateLimit.setUnits("packets per 30 seconds")
_CisPimV2RateLimit_Type = Unsigned32
_CisPimV2RateLimit_Object = MibScalar
cisPimV2RateLimit = _CisPimV2RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 3, 5),
    _CisPimV2RateLimit_Type()
)
cisPimV2RateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisPimV2RateLimit.setStatus("deprecated")
if mibBuilder.loadTexts:
    cisPimV2RateLimit.setUnits("packets per 30 seconds")
_CisRateLimit_Type = Unsigned32
_CisRateLimit_Object = MibScalar
cisRateLimit = _CisRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 3, 6),
    _CisRateLimit_Type()
)
cisRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cisRateLimit.setUnits("packets per second")
_CisVlanConfigInfo_ObjectIdentity = ObjectIdentity
cisVlanConfigInfo = _CisVlanConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4)
)
_CisVlanConfigTable_Object = MibTable
cisVlanConfigTable = _CisVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cisVlanConfigTable.setStatus("current")
_CisVlanConfigEntry_Object = MibTableRow
cisVlanConfigEntry = _CisVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1)
)
cisVlanConfigEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisVlanIndex"),
)
if mibBuilder.loadTexts:
    cisVlanConfigEntry.setStatus("current")
_CisVlanIndex_Type = VlanIndex
_CisVlanIndex_Object = MibTableColumn
cisVlanIndex = _CisVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 1),
    _CisVlanIndex_Type()
)
cisVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisVlanIndex.setStatus("current")
_CisVlanIgmpSnoopingEnabled_Type = TruthValue
_CisVlanIgmpSnoopingEnabled_Object = MibTableColumn
cisVlanIgmpSnoopingEnabled = _CisVlanIgmpSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 2),
    _CisVlanIgmpSnoopingEnabled_Type()
)
cisVlanIgmpSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanIgmpSnoopingEnabled.setStatus("current")
_CisVlanFastLeaveEnabled_Type = TruthValue
_CisVlanFastLeaveEnabled_Object = MibTableColumn
cisVlanFastLeaveEnabled = _CisVlanFastLeaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 3),
    _CisVlanFastLeaveEnabled_Type()
)
cisVlanFastLeaveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanFastLeaveEnabled.setStatus("current")
_CisVlanIgmpSnoopingOperMode_Type = CisIgmpMode
_CisVlanIgmpSnoopingOperMode_Object = MibTableColumn
cisVlanIgmpSnoopingOperMode = _CisVlanIgmpSnoopingOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 4),
    _CisVlanIgmpSnoopingOperMode_Type()
)
cisVlanIgmpSnoopingOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisVlanIgmpSnoopingOperMode.setStatus("current")


class _CisVlanIgmpSnoopingLearningMode_Type(Integer32):
    """Custom type cisVlanIgmpSnoopingLearningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cgmp", 2),
          ("pimDvmrp", 1))
    )


_CisVlanIgmpSnoopingLearningMode_Type.__name__ = "Integer32"
_CisVlanIgmpSnoopingLearningMode_Object = MibTableColumn
cisVlanIgmpSnoopingLearningMode = _CisVlanIgmpSnoopingLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 5),
    _CisVlanIgmpSnoopingLearningMode_Type()
)
cisVlanIgmpSnoopingLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanIgmpSnoopingLearningMode.setStatus("current")
_CisVlanReportSuppressionEnabled_Type = TruthValue
_CisVlanReportSuppressionEnabled_Object = MibTableColumn
cisVlanReportSuppressionEnabled = _CisVlanReportSuppressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 6),
    _CisVlanReportSuppressionEnabled_Type()
)
cisVlanReportSuppressionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanReportSuppressionEnabled.setStatus("current")


class _CisVlanLeaveQueryInterval_Type(Unsigned32):
    """Custom type cisVlanLeaveQueryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CisVlanLeaveQueryInterval_Type.__name__ = "Unsigned32"
_CisVlanLeaveQueryInterval_Object = MibTableColumn
cisVlanLeaveQueryInterval = _CisVlanLeaveQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 7),
    _CisVlanLeaveQueryInterval_Type()
)
cisVlanLeaveQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanLeaveQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cisVlanLeaveQueryInterval.setUnits("milliseconds")


class _CisVlanLastMemberQueryCount_Type(Unsigned32):
    """Custom type cisVlanLastMemberQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CisVlanLastMemberQueryCount_Type.__name__ = "Unsigned32"
_CisVlanLastMemberQueryCount_Object = MibTableColumn
cisVlanLastMemberQueryCount = _CisVlanLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 8),
    _CisVlanLastMemberQueryCount_Type()
)
cisVlanLastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanLastMemberQueryCount.setStatus("current")


class _CisVlanRobustnessVariable_Type(Unsigned32):
    """Custom type cisVlanRobustnessVariable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 7),
    )


_CisVlanRobustnessVariable_Type.__name__ = "Unsigned32"
_CisVlanRobustnessVariable_Object = MibTableColumn
cisVlanRobustnessVariable = _CisVlanRobustnessVariable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 9),
    _CisVlanRobustnessVariable_Type()
)
cisVlanRobustnessVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanRobustnessVariable.setStatus("current")
_CisVlanTimeToLiveCheckEnabled_Type = TruthValue
_CisVlanTimeToLiveCheckEnabled_Object = MibTableColumn
cisVlanTimeToLiveCheckEnabled = _CisVlanTimeToLiveCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 10),
    _CisVlanTimeToLiveCheckEnabled_Type()
)
cisVlanTimeToLiveCheckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanTimeToLiveCheckEnabled.setStatus("current")
_CisVlanRouterAlertCheckEnabled_Type = TruthValue
_CisVlanRouterAlertCheckEnabled_Object = MibTableColumn
cisVlanRouterAlertCheckEnabled = _CisVlanRouterAlertCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 1, 1, 11),
    _CisVlanRouterAlertCheckEnabled_Type()
)
cisVlanRouterAlertCheckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanRouterAlertCheckEnabled.setStatus("current")
_CisIgmpQuerierTable_Object = MibTable
cisIgmpQuerierTable = _CisIgmpQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cisIgmpQuerierTable.setStatus("current")
_CisIgmpQuerierEntry_Object = MibTableRow
cisIgmpQuerierEntry = _CisIgmpQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1)
)
cisIgmpQuerierEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierVlanIndex"),
)
if mibBuilder.loadTexts:
    cisIgmpQuerierEntry.setStatus("current")
_CisIgmpQuerierVlanIndex_Type = VlanIndex
_CisIgmpQuerierVlanIndex_Object = MibTableColumn
cisIgmpQuerierVlanIndex = _CisIgmpQuerierVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 1),
    _CisIgmpQuerierVlanIndex_Type()
)
cisIgmpQuerierVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisIgmpQuerierVlanIndex.setStatus("current")
_CisIgmpQuerierEnabled_Type = TruthValue
_CisIgmpQuerierEnabled_Object = MibTableColumn
cisIgmpQuerierEnabled = _CisIgmpQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 2),
    _CisIgmpQuerierEnabled_Type()
)
cisIgmpQuerierEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierEnabled.setStatus("current")


class _CisIgmpQuerierState_Type(Integer32):
    """Custom type cisIgmpQuerierState based on Integer32"""
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
        *(("disabled", 1),
          ("electing", 2),
          ("inactive", 5),
          ("nonQuerier", 4),
          ("querier", 3))
    )


_CisIgmpQuerierState_Type.__name__ = "Integer32"
_CisIgmpQuerierState_Object = MibTableColumn
cisIgmpQuerierState = _CisIgmpQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 3),
    _CisIgmpQuerierState_Type()
)
cisIgmpQuerierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisIgmpQuerierState.setStatus("current")
_CisIgmpQuerierVersion_Type = CisIgmpVersion
_CisIgmpQuerierVersion_Object = MibTableColumn
cisIgmpQuerierVersion = _CisIgmpQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 4),
    _CisIgmpQuerierVersion_Type()
)
cisIgmpQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisIgmpQuerierVersion.setStatus("current")
_CisIgmpQuerierAddressType_Type = InetAddressType
_CisIgmpQuerierAddressType_Object = MibTableColumn
cisIgmpQuerierAddressType = _CisIgmpQuerierAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 5),
    _CisIgmpQuerierAddressType_Type()
)
cisIgmpQuerierAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisIgmpQuerierAddressType.setStatus("current")
_CisIgmpQuerierAddress_Type = InetAddress
_CisIgmpQuerierAddress_Object = MibTableColumn
cisIgmpQuerierAddress = _CisIgmpQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 6),
    _CisIgmpQuerierAddress_Type()
)
cisIgmpQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisIgmpQuerierAddress.setStatus("current")
_CisIgmpQuerierInterface_Type = InterfaceIndex
_CisIgmpQuerierInterface_Object = MibTableColumn
cisIgmpQuerierInterface = _CisIgmpQuerierInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 7),
    _CisIgmpQuerierInterface_Type()
)
cisIgmpQuerierInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisIgmpQuerierInterface.setStatus("current")


class _CisIgmpQuerierTcnQueryCount_Type(Unsigned32):
    """Custom type cisIgmpQuerierTcnQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CisIgmpQuerierTcnQueryCount_Type.__name__ = "Unsigned32"
_CisIgmpQuerierTcnQueryCount_Object = MibTableColumn
cisIgmpQuerierTcnQueryCount = _CisIgmpQuerierTcnQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 8),
    _CisIgmpQuerierTcnQueryCount_Type()
)
cisIgmpQuerierTcnQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierTcnQueryCount.setStatus("current")


class _CisIgmpQuerierTcnQueryInterval_Type(Unsigned32):
    """Custom type cisIgmpQuerierTcnQueryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CisIgmpQuerierTcnQueryInterval_Type.__name__ = "Unsigned32"
_CisIgmpQuerierTcnQueryInterval_Object = MibTableColumn
cisIgmpQuerierTcnQueryInterval = _CisIgmpQuerierTcnQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 9),
    _CisIgmpQuerierTcnQueryInterval_Type()
)
cisIgmpQuerierTcnQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierTcnQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cisIgmpQuerierTcnQueryInterval.setUnits("seconds")


class _CisIgmpQuerierTimerExpiry_Type(Unsigned32):
    """Custom type cisIgmpQuerierTimerExpiry based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CisIgmpQuerierTimerExpiry_Type.__name__ = "Unsigned32"
_CisIgmpQuerierTimerExpiry_Object = MibTableColumn
cisIgmpQuerierTimerExpiry = _CisIgmpQuerierTimerExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 10),
    _CisIgmpQuerierTimerExpiry_Type()
)
cisIgmpQuerierTimerExpiry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierTimerExpiry.setStatus("current")
if mibBuilder.loadTexts:
    cisIgmpQuerierTimerExpiry.setUnits("seconds")


class _CisIgmpQuerierMaxResponseTime_Type(Unsigned32):
    """Custom type cisIgmpQuerierMaxResponseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CisIgmpQuerierMaxResponseTime_Type.__name__ = "Unsigned32"
_CisIgmpQuerierMaxResponseTime_Object = MibTableColumn
cisIgmpQuerierMaxResponseTime = _CisIgmpQuerierMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 11),
    _CisIgmpQuerierMaxResponseTime_Type()
)
cisIgmpQuerierMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    cisIgmpQuerierMaxResponseTime.setUnits("seconds")


class _CisIgmpQuerierQueryInterval_Type(Unsigned32):
    """Custom type cisIgmpQuerierQueryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CisIgmpQuerierQueryInterval_Type.__name__ = "Unsigned32"
_CisIgmpQuerierQueryInterval_Object = MibTableColumn
cisIgmpQuerierQueryInterval = _CisIgmpQuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 12),
    _CisIgmpQuerierQueryInterval_Type()
)
cisIgmpQuerierQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cisIgmpQuerierQueryInterval.setUnits("seconds")
_CisIgmpQuerierAdminAddressType_Type = InetAddressType
_CisIgmpQuerierAdminAddressType_Object = MibTableColumn
cisIgmpQuerierAdminAddressType = _CisIgmpQuerierAdminAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 13),
    _CisIgmpQuerierAdminAddressType_Type()
)
cisIgmpQuerierAdminAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierAdminAddressType.setStatus("current")
_CisIgmpQuerierAdminAddress_Type = InetAddress
_CisIgmpQuerierAdminAddress_Object = MibTableColumn
cisIgmpQuerierAdminAddress = _CisIgmpQuerierAdminAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 14),
    _CisIgmpQuerierAdminAddress_Type()
)
cisIgmpQuerierAdminAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierAdminAddress.setStatus("current")
_CisIgmpQuerierAdminVersion_Type = CisIgmpVersion
_CisIgmpQuerierAdminVersion_Object = MibTableColumn
cisIgmpQuerierAdminVersion = _CisIgmpQuerierAdminVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 15),
    _CisIgmpQuerierAdminVersion_Type()
)
cisIgmpQuerierAdminVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIgmpQuerierAdminVersion.setStatus("current")
_CisIgmpQuerierTcnQueryPending_Type = Counter32
_CisIgmpQuerierTcnQueryPending_Object = MibTableColumn
cisIgmpQuerierTcnQueryPending = _CisIgmpQuerierTcnQueryPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 4, 2, 1, 16),
    _CisIgmpQuerierTcnQueryPending_Type()
)
cisIgmpQuerierTcnQueryPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisIgmpQuerierTcnQueryPending.setStatus("current")
_CisIfConfigInfo_ObjectIdentity = ObjectIdentity
cisIfConfigInfo = _CisIfConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 5)
)
_CisIfConfigTable_Object = MibTable
cisIfConfigTable = _CisIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cisIfConfigTable.setStatus("current")
_CisIfConfigEntry_Object = MibTableRow
cisIfConfigEntry = _CisIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 5, 1, 1)
)
cisIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cisIfConfigEntry.setStatus("current")
_CisIfTopoChangeFloodEnabled_Type = TruthValue
_CisIfTopoChangeFloodEnabled_Object = MibTableColumn
cisIfTopoChangeFloodEnabled = _CisIfTopoChangeFloodEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 5, 1, 1, 1),
    _CisIfTopoChangeFloodEnabled_Type()
)
cisIfTopoChangeFloodEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisIfTopoChangeFloodEnabled.setStatus("current")
_CisMulticastRouterInfo_ObjectIdentity = ObjectIdentity
cisMulticastRouterInfo = _CisMulticastRouterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6)
)
_CisMcastRouterCfgTable_Object = MibTable
cisMcastRouterCfgTable = _CisMcastRouterCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cisMcastRouterCfgTable.setStatus("deprecated")
_CisMcastRouterCfgEntry_Object = MibTableRow
cisMcastRouterCfgEntry = _CisMcastRouterCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 1, 1)
)
cisMcastRouterCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMcastRouterVlanIndex"),
)
if mibBuilder.loadTexts:
    cisMcastRouterCfgEntry.setStatus("deprecated")
_CisMcastRouterVlanIndex_Type = VlanIndex
_CisMcastRouterVlanIndex_Object = MibTableColumn
cisMcastRouterVlanIndex = _CisMcastRouterVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 1, 1, 1),
    _CisMcastRouterVlanIndex_Type()
)
cisMcastRouterVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMcastRouterVlanIndex.setStatus("deprecated")


class _CisMcastRouterType_Type(Integer32):
    """Custom type cisMcastRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CisMcastRouterType_Type.__name__ = "Integer32"
_CisMcastRouterType_Object = MibTableColumn
cisMcastRouterType = _CisMcastRouterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 1, 1, 2),
    _CisMcastRouterType_Type()
)
cisMcastRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMcastRouterType.setStatus("deprecated")
_CisMcastRouterRowStatus_Type = RowStatus
_CisMcastRouterRowStatus_Object = MibTableColumn
cisMcastRouterRowStatus = _CisMcastRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 1, 1, 3),
    _CisMcastRouterRowStatus_Type()
)
cisMcastRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisMcastRouterRowStatus.setStatus("deprecated")
_CisMcastRouterConfigTable_Object = MibTable
cisMcastRouterConfigTable = _CisMcastRouterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cisMcastRouterConfigTable.setStatus("current")
_CisMcastRouterConfigEntry_Object = MibTableRow
cisMcastRouterConfigEntry = _CisMcastRouterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 2, 1)
)
cisMcastRouterConfigEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMcastRouterConfigVlanIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cisMcastRouterConfigEntry.setStatus("current")
_CisMcastRouterConfigVlanIndex_Type = VlanIndex
_CisMcastRouterConfigVlanIndex_Object = MibTableColumn
cisMcastRouterConfigVlanIndex = _CisMcastRouterConfigVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 2, 1, 1),
    _CisMcastRouterConfigVlanIndex_Type()
)
cisMcastRouterConfigVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMcastRouterConfigVlanIndex.setStatus("current")


class _CisMcastRouterConfigRouterType_Type(Integer32):
    """Custom type cisMcastRouterConfigRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CisMcastRouterConfigRouterType_Type.__name__ = "Integer32"
_CisMcastRouterConfigRouterType_Object = MibTableColumn
cisMcastRouterConfigRouterType = _CisMcastRouterConfigRouterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 2, 1, 2),
    _CisMcastRouterConfigRouterType_Type()
)
cisMcastRouterConfigRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMcastRouterConfigRouterType.setStatus("current")


class _CisMcastRouterConfigStorageType_Type(StorageType):
    """Custom type cisMcastRouterConfigStorageType based on StorageType"""


_CisMcastRouterConfigStorageType_Object = MibTableColumn
cisMcastRouterConfigStorageType = _CisMcastRouterConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 2, 1, 3),
    _CisMcastRouterConfigStorageType_Type()
)
cisMcastRouterConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisMcastRouterConfigStorageType.setStatus("current")
_CisMcastRouterConfigRowStatus_Type = RowStatus
_CisMcastRouterConfigRowStatus_Object = MibTableColumn
cisMcastRouterConfigRowStatus = _CisMcastRouterConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 6, 2, 1, 4),
    _CisMcastRouterConfigRowStatus_Type()
)
cisMcastRouterConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisMcastRouterConfigRowStatus.setStatus("current")
_CisMulticastGroupInfo_ObjectIdentity = ObjectIdentity
cisMulticastGroupInfo = _CisMulticastGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7)
)
_CisMcastGroupTable_Object = MibTable
cisMcastGroupTable = _CisMcastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cisMcastGroupTable.setStatus("deprecated")
_CisMcastGroupEntry_Object = MibTableRow
cisMcastGroupEntry = _CisMcastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1)
)
cisMcastGroupEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMcastGroupVlanIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMcastGroupAddressType"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMcastGroupAddress"),
)
if mibBuilder.loadTexts:
    cisMcastGroupEntry.setStatus("deprecated")
_CisMcastGroupVlanIndex_Type = VlanIndex
_CisMcastGroupVlanIndex_Object = MibTableColumn
cisMcastGroupVlanIndex = _CisMcastGroupVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1, 1),
    _CisMcastGroupVlanIndex_Type()
)
cisMcastGroupVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMcastGroupVlanIndex.setStatus("deprecated")
_CisMcastGroupAddressType_Type = InetAddressType
_CisMcastGroupAddressType_Object = MibTableColumn
cisMcastGroupAddressType = _CisMcastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1, 2),
    _CisMcastGroupAddressType_Type()
)
cisMcastGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMcastGroupAddressType.setStatus("deprecated")


class _CisMcastGroupAddress_Type(InetAddress):
    """Custom type cisMcastGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CisMcastGroupAddress_Type.__name__ = "InetAddress"
_CisMcastGroupAddress_Object = MibTableColumn
cisMcastGroupAddress = _CisMcastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1, 3),
    _CisMcastGroupAddress_Type()
)
cisMcastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMcastGroupAddress.setStatus("deprecated")


class _CisMcastGroupFilterMode_Type(Integer32):
    """Custom type cisMcastGroupFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_CisMcastGroupFilterMode_Type.__name__ = "Integer32"
_CisMcastGroupFilterMode_Object = MibTableColumn
cisMcastGroupFilterMode = _CisMcastGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1, 4),
    _CisMcastGroupFilterMode_Type()
)
cisMcastGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMcastGroupFilterMode.setStatus("deprecated")
_CisMcastGroupIgmpVersion_Type = CisIgmpVersion
_CisMcastGroupIgmpVersion_Object = MibTableColumn
cisMcastGroupIgmpVersion = _CisMcastGroupIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1, 5),
    _CisMcastGroupIgmpVersion_Type()
)
cisMcastGroupIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMcastGroupIgmpVersion.setStatus("deprecated")
_CisMcastGroupIncludeHostCount_Type = Counter32
_CisMcastGroupIncludeHostCount_Object = MibTableColumn
cisMcastGroupIncludeHostCount = _CisMcastGroupIncludeHostCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1, 6),
    _CisMcastGroupIncludeHostCount_Type()
)
cisMcastGroupIncludeHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMcastGroupIncludeHostCount.setStatus("deprecated")
_CisMcastGroupExcludeHostCount_Type = Counter32
_CisMcastGroupExcludeHostCount_Object = MibTableColumn
cisMcastGroupExcludeHostCount = _CisMcastGroupExcludeHostCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1, 7),
    _CisMcastGroupExcludeHostCount_Type()
)
cisMcastGroupExcludeHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMcastGroupExcludeHostCount.setStatus("deprecated")
_CisMcastGroupPortList_Type = CiscoPortList
_CisMcastGroupPortList_Object = MibTableColumn
cisMcastGroupPortList = _CisMcastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 1, 1, 8),
    _CisMcastGroupPortList_Type()
)
cisMcastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMcastGroupPortList.setStatus("deprecated")
_CisMulticastGroupTable_Object = MibTable
cisMulticastGroupTable = _CisMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cisMulticastGroupTable.setStatus("current")
_CisMulticastGroupEntry_Object = MibTableRow
cisMulticastGroupEntry = _CisMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1)
)
cisMulticastGroupEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupVlanIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupCeVlanIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupAddressType"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupAddress"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupSourceAddress"),
)
if mibBuilder.loadTexts:
    cisMulticastGroupEntry.setStatus("current")
_CisMulticastGroupVlanIndex_Type = VlanIndex
_CisMulticastGroupVlanIndex_Object = MibTableColumn
cisMulticastGroupVlanIndex = _CisMulticastGroupVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 1),
    _CisMulticastGroupVlanIndex_Type()
)
cisMulticastGroupVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupVlanIndex.setStatus("current")
_CisMulticastGroupCeVlanIndex_Type = VlanIndex
_CisMulticastGroupCeVlanIndex_Object = MibTableColumn
cisMulticastGroupCeVlanIndex = _CisMulticastGroupCeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 2),
    _CisMulticastGroupCeVlanIndex_Type()
)
cisMulticastGroupCeVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupCeVlanIndex.setStatus("current")
_CisMulticastGroupAddressType_Type = InetAddressType
_CisMulticastGroupAddressType_Object = MibTableColumn
cisMulticastGroupAddressType = _CisMulticastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 3),
    _CisMulticastGroupAddressType_Type()
)
cisMulticastGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupAddressType.setStatus("current")


class _CisMulticastGroupAddress_Type(InetAddress):
    """Custom type cisMulticastGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CisMulticastGroupAddress_Type.__name__ = "InetAddress"
_CisMulticastGroupAddress_Object = MibTableColumn
cisMulticastGroupAddress = _CisMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 4),
    _CisMulticastGroupAddress_Type()
)
cisMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupAddress.setStatus("current")


class _CisMulticastGroupSourceAddress_Type(InetAddress):
    """Custom type cisMulticastGroupSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CisMulticastGroupSourceAddress_Type.__name__ = "InetAddress"
_CisMulticastGroupSourceAddress_Object = MibTableColumn
cisMulticastGroupSourceAddress = _CisMulticastGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 5),
    _CisMulticastGroupSourceAddress_Type()
)
cisMulticastGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupSourceAddress.setStatus("current")


class _CisMulticastGroupGroupType_Type(Integer32):
    """Custom type cisMulticastGroupGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_CisMulticastGroupGroupType_Type.__name__ = "Integer32"
_CisMulticastGroupGroupType_Object = MibTableColumn
cisMulticastGroupGroupType = _CisMulticastGroupGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 6),
    _CisMulticastGroupGroupType_Type()
)
cisMulticastGroupGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMulticastGroupGroupType.setStatus("current")


class _CisMulticastGroupIgmpVersion_Type(Bits):
    """Custom type cisMulticastGroupIgmpVersion based on Bits"""
    namedValues = NamedValues(
        *(("igmpV1", 0),
          ("igmpV2", 1),
          ("igmpV3", 2))
    )

_CisMulticastGroupIgmpVersion_Type.__name__ = "Bits"
_CisMulticastGroupIgmpVersion_Object = MibTableColumn
cisMulticastGroupIgmpVersion = _CisMulticastGroupIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 7),
    _CisMulticastGroupIgmpVersion_Type()
)
cisMulticastGroupIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMulticastGroupIgmpVersion.setStatus("current")
_CisMulticastGroupSourceUpTime_Type = Unsigned32
_CisMulticastGroupSourceUpTime_Object = MibTableColumn
cisMulticastGroupSourceUpTime = _CisMulticastGroupSourceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 8),
    _CisMulticastGroupSourceUpTime_Type()
)
cisMulticastGroupSourceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMulticastGroupSourceUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cisMulticastGroupSourceUpTime.setUnits("seconds")
_CisMulticastGroupSourceExpires_Type = Unsigned32
_CisMulticastGroupSourceExpires_Object = MibTableColumn
cisMulticastGroupSourceExpires = _CisMulticastGroupSourceExpires_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 9),
    _CisMulticastGroupSourceExpires_Type()
)
cisMulticastGroupSourceExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMulticastGroupSourceExpires.setStatus("current")
if mibBuilder.loadTexts:
    cisMulticastGroupSourceExpires.setUnits("seconds")
_CisMulticastGroupInclHostCount_Type = Counter32
_CisMulticastGroupInclHostCount_Object = MibTableColumn
cisMulticastGroupInclHostCount = _CisMulticastGroupInclHostCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 10),
    _CisMulticastGroupInclHostCount_Type()
)
cisMulticastGroupInclHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMulticastGroupInclHostCount.setStatus("current")
_CisMulticastGroupExclHostCount_Type = Counter32
_CisMulticastGroupExclHostCount_Object = MibTableColumn
cisMulticastGroupExclHostCount = _CisMulticastGroupExclHostCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 2, 1, 11),
    _CisMulticastGroupExclHostCount_Type()
)
cisMulticastGroupExclHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMulticastGroupExclHostCount.setStatus("current")
_CisMulticastGroupPortListTable_Object = MibTable
cisMulticastGroupPortListTable = _CisMulticastGroupPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cisMulticastGroupPortListTable.setStatus("current")
_CisMulticastGroupPortListEntry_Object = MibTableRow
cisMulticastGroupPortListEntry = _CisMulticastGroupPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 3, 1)
)
cisMulticastGroupPortListEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupVlanIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupCeVlanIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupAddressType"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupAddress"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupSourceAddress"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupPortRangeIndex"),
)
if mibBuilder.loadTexts:
    cisMulticastGroupPortListEntry.setStatus("current")
_CisMulticastGroupPortRangeIndex_Type = CiscoPortListRange
_CisMulticastGroupPortRangeIndex_Object = MibTableColumn
cisMulticastGroupPortRangeIndex = _CisMulticastGroupPortRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 3, 1, 1),
    _CisMulticastGroupPortRangeIndex_Type()
)
cisMulticastGroupPortRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupPortRangeIndex.setStatus("current")
_CisMulticastGroupPortList_Type = CiscoPortList
_CisMulticastGroupPortList_Object = MibTableColumn
cisMulticastGroupPortList = _CisMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 3, 1, 2),
    _CisMulticastGroupPortList_Type()
)
cisMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisMulticastGroupPortList.setStatus("current")
_CisMulticastGroupConfigTable_Object = MibTable
cisMulticastGroupConfigTable = _CisMulticastGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cisMulticastGroupConfigTable.setStatus("current")
_CisMulticastGroupConfigEntry_Object = MibTableRow
cisMulticastGroupConfigEntry = _CisMulticastGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1)
)
cisMulticastGroupConfigEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfVlanIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfCeVlanIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfAddressType"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfAddress"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfSourceAddress"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfPortRange"),
)
if mibBuilder.loadTexts:
    cisMulticastGroupConfigEntry.setStatus("current")
_CisMulticastGroupConfVlanIndex_Type = VlanIndex
_CisMulticastGroupConfVlanIndex_Object = MibTableColumn
cisMulticastGroupConfVlanIndex = _CisMulticastGroupConfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 1),
    _CisMulticastGroupConfVlanIndex_Type()
)
cisMulticastGroupConfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupConfVlanIndex.setStatus("current")
_CisMulticastGroupConfCeVlanIndex_Type = VlanIndex
_CisMulticastGroupConfCeVlanIndex_Object = MibTableColumn
cisMulticastGroupConfCeVlanIndex = _CisMulticastGroupConfCeVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 2),
    _CisMulticastGroupConfCeVlanIndex_Type()
)
cisMulticastGroupConfCeVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupConfCeVlanIndex.setStatus("current")
_CisMulticastGroupConfAddressType_Type = InetAddressType
_CisMulticastGroupConfAddressType_Object = MibTableColumn
cisMulticastGroupConfAddressType = _CisMulticastGroupConfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 3),
    _CisMulticastGroupConfAddressType_Type()
)
cisMulticastGroupConfAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupConfAddressType.setStatus("current")


class _CisMulticastGroupConfAddress_Type(InetAddress):
    """Custom type cisMulticastGroupConfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CisMulticastGroupConfAddress_Type.__name__ = "InetAddress"
_CisMulticastGroupConfAddress_Object = MibTableColumn
cisMulticastGroupConfAddress = _CisMulticastGroupConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 4),
    _CisMulticastGroupConfAddress_Type()
)
cisMulticastGroupConfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupConfAddress.setStatus("current")


class _CisMulticastGroupConfSourceAddress_Type(InetAddress):
    """Custom type cisMulticastGroupConfSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CisMulticastGroupConfSourceAddress_Type.__name__ = "InetAddress"
_CisMulticastGroupConfSourceAddress_Object = MibTableColumn
cisMulticastGroupConfSourceAddress = _CisMulticastGroupConfSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 5),
    _CisMulticastGroupConfSourceAddress_Type()
)
cisMulticastGroupConfSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupConfSourceAddress.setStatus("current")
_CisMulticastGroupConfPortRange_Type = CiscoPortListRange
_CisMulticastGroupConfPortRange_Object = MibTableColumn
cisMulticastGroupConfPortRange = _CisMulticastGroupConfPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 6),
    _CisMulticastGroupConfPortRange_Type()
)
cisMulticastGroupConfPortRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisMulticastGroupConfPortRange.setStatus("current")
_CisMulticastGroupConfPortList_Type = CiscoPortList
_CisMulticastGroupConfPortList_Object = MibTableColumn
cisMulticastGroupConfPortList = _CisMulticastGroupConfPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 7),
    _CisMulticastGroupConfPortList_Type()
)
cisMulticastGroupConfPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisMulticastGroupConfPortList.setStatus("current")


class _CisMulticastGroupConfStorageType_Type(StorageType):
    """Custom type cisMulticastGroupConfStorageType based on StorageType"""


_CisMulticastGroupConfStorageType_Object = MibTableColumn
cisMulticastGroupConfStorageType = _CisMulticastGroupConfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 8),
    _CisMulticastGroupConfStorageType_Type()
)
cisMulticastGroupConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisMulticastGroupConfStorageType.setStatus("current")
_CisMulticastGroupConfRowStatus_Type = RowStatus
_CisMulticastGroupConfRowStatus_Object = MibTableColumn
cisMulticastGroupConfRowStatus = _CisMulticastGroupConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 7, 4, 1, 9),
    _CisMulticastGroupConfRowStatus_Type()
)
cisMulticastGroupConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisMulticastGroupConfRowStatus.setStatus("current")
_CisResourceLimitInfo_ObjectIdentity = ObjectIdentity
cisResourceLimitInfo = _CisResourceLimitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 8)
)
_CisL2EntryLimit_Type = Unsigned32
_CisL2EntryLimit_Object = MibScalar
cisL2EntryLimit = _CisL2EntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 8, 1),
    _CisL2EntryLimit_Type()
)
cisL2EntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisL2EntryLimit.setStatus("current")
_CisEntryTrackingLimit_Type = Unsigned32
_CisEntryTrackingLimit_Object = MibScalar
cisEntryTrackingLimit = _CisEntryTrackingLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 8, 2),
    _CisEntryTrackingLimit_Type()
)
cisEntryTrackingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisEntryTrackingLimit.setStatus("current")
_CisSourceOnlyPercentageScanLimit_Type = Percent
_CisSourceOnlyPercentageScanLimit_Object = MibScalar
cisSourceOnlyPercentageScanLimit = _CisSourceOnlyPercentageScanLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 8, 3),
    _CisSourceOnlyPercentageScanLimit_Type()
)
cisSourceOnlyPercentageScanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisSourceOnlyPercentageScanLimit.setStatus("current")
_CisSourceOnlyLearningLimit_Type = Unsigned32
_CisSourceOnlyLearningLimit_Object = MibScalar
cisSourceOnlyLearningLimit = _CisSourceOnlyLearningLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 8, 4),
    _CisSourceOnlyLearningLimit_Type()
)
cisSourceOnlyLearningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisSourceOnlyLearningLimit.setStatus("current")
_CisQuerierConfigInfo_ObjectIdentity = ObjectIdentity
cisQuerierConfigInfo = _CisQuerierConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9)
)
_CisQuerierEnabled_Type = TruthValue
_CisQuerierEnabled_Object = MibScalar
cisQuerierEnabled = _CisQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 1),
    _CisQuerierEnabled_Type()
)
cisQuerierEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierEnabled.setStatus("current")
_CisQuerierTcnQueryInterval_Type = Unsigned32
_CisQuerierTcnQueryInterval_Object = MibScalar
cisQuerierTcnQueryInterval = _CisQuerierTcnQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 2),
    _CisQuerierTcnQueryInterval_Type()
)
cisQuerierTcnQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierTcnQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cisQuerierTcnQueryInterval.setUnits("seconds")
_CisQuerierTimerExpiry_Type = Unsigned32
_CisQuerierTimerExpiry_Object = MibScalar
cisQuerierTimerExpiry = _CisQuerierTimerExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 3),
    _CisQuerierTimerExpiry_Type()
)
cisQuerierTimerExpiry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierTimerExpiry.setStatus("current")
if mibBuilder.loadTexts:
    cisQuerierTimerExpiry.setUnits("seconds")
_CisQuerierMaxResponseTime_Type = Unsigned32
_CisQuerierMaxResponseTime_Object = MibScalar
cisQuerierMaxResponseTime = _CisQuerierMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 4),
    _CisQuerierMaxResponseTime_Type()
)
cisQuerierMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    cisQuerierMaxResponseTime.setUnits("one-tenth of second")
_CisQuerierQueryInterval_Type = Unsigned32
_CisQuerierQueryInterval_Object = MibScalar
cisQuerierQueryInterval = _CisQuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 5),
    _CisQuerierQueryInterval_Type()
)
cisQuerierQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cisQuerierQueryInterval.setUnits("seconds")
_CisQuerierAddressType_Type = InetAddressType
_CisQuerierAddressType_Object = MibScalar
cisQuerierAddressType = _CisQuerierAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 6),
    _CisQuerierAddressType_Type()
)
cisQuerierAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierAddressType.setStatus("current")
_CisQuerierAddress_Type = InetAddress
_CisQuerierAddress_Object = MibScalar
cisQuerierAddress = _CisQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 7),
    _CisQuerierAddress_Type()
)
cisQuerierAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierAddress.setStatus("current")
_CisQuerierVersion_Type = CisIgmpVersion
_CisQuerierVersion_Object = MibScalar
cisQuerierVersion = _CisQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 8),
    _CisQuerierVersion_Type()
)
cisQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierVersion.setStatus("current")


class _CisQuerierTcnQueryCount_Type(Unsigned32):
    """Custom type cisQuerierTcnQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CisQuerierTcnQueryCount_Type.__name__ = "Unsigned32"
_CisQuerierTcnQueryCount_Object = MibScalar
cisQuerierTcnQueryCount = _CisQuerierTcnQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 9, 9),
    _CisQuerierTcnQueryCount_Type()
)
cisQuerierTcnQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisQuerierTcnQueryCount.setStatus("current")
_CisFilteringInfo_ObjectIdentity = ObjectIdentity
cisFilteringInfo = _CisFilteringInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10)
)
_CisIfLimitTable_Object = MibTable
cisIfLimitTable = _CisIfLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cisIfLimitTable.setStatus("current")
_CisIfLimitEntry_Object = MibTableRow
cisIfLimitEntry = _CisIfLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 1, 1)
)
cisIfLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisIfLimitVlanNumber"),
)
if mibBuilder.loadTexts:
    cisIfLimitEntry.setStatus("current")
_CisIfLimitVlanNumber_Type = VlanIndexOrZero
_CisIfLimitVlanNumber_Object = MibTableColumn
cisIfLimitVlanNumber = _CisIfLimitVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 1, 1, 1),
    _CisIfLimitVlanNumber_Type()
)
cisIfLimitVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisIfLimitVlanNumber.setStatus("current")


class _CisIfLimitMax_Type(Unsigned32):
    """Custom type cisIfLimitMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CisIfLimitMax_Type.__name__ = "Unsigned32"
_CisIfLimitMax_Object = MibTableColumn
cisIfLimitMax = _CisIfLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 1, 1, 2),
    _CisIfLimitMax_Type()
)
cisIfLimitMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfLimitMax.setStatus("current")
_CisIfLimitExcludeAccessGrp_Type = SnmpAdminString
_CisIfLimitExcludeAccessGrp_Object = MibTableColumn
cisIfLimitExcludeAccessGrp = _CisIfLimitExcludeAccessGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 1, 1, 3),
    _CisIfLimitExcludeAccessGrp_Type()
)
cisIfLimitExcludeAccessGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfLimitExcludeAccessGrp.setStatus("current")


class _CisIfLimitStorageType_Type(StorageType):
    """Custom type cisIfLimitStorageType based on StorageType"""


_CisIfLimitStorageType_Object = MibTableColumn
cisIfLimitStorageType = _CisIfLimitStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 1, 1, 4),
    _CisIfLimitStorageType_Type()
)
cisIfLimitStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfLimitStorageType.setStatus("current")
_CisIfLimitRowStatus_Type = RowStatus
_CisIfLimitRowStatus_Object = MibTableColumn
cisIfLimitRowStatus = _CisIfLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 1, 1, 5),
    _CisIfLimitRowStatus_Type()
)
cisIfLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfLimitRowStatus.setStatus("current")
_CisIfLimitTotalTable_Object = MibTable
cisIfLimitTotalTable = _CisIfLimitTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 2)
)
if mibBuilder.loadTexts:
    cisIfLimitTotalTable.setStatus("current")
_CisIfLimitTotalEntry_Object = MibTableRow
cisIfLimitTotalEntry = _CisIfLimitTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 2, 1)
)
cisIfLimitTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cisIfLimitTotalEntry.setStatus("current")


class _CisIfLimitTotalLimitMax_Type(Unsigned32):
    """Custom type cisIfLimitTotalLimitMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CisIfLimitTotalLimitMax_Type.__name__ = "Unsigned32"
_CisIfLimitTotalLimitMax_Object = MibTableColumn
cisIfLimitTotalLimitMax = _CisIfLimitTotalLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 2, 1, 1),
    _CisIfLimitTotalLimitMax_Type()
)
cisIfLimitTotalLimitMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfLimitTotalLimitMax.setStatus("current")
_CisIfLimitTotalExcludeAccessGrp_Type = SnmpAdminString
_CisIfLimitTotalExcludeAccessGrp_Object = MibTableColumn
cisIfLimitTotalExcludeAccessGrp = _CisIfLimitTotalExcludeAccessGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 2, 1, 2),
    _CisIfLimitTotalExcludeAccessGrp_Type()
)
cisIfLimitTotalExcludeAccessGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfLimitTotalExcludeAccessGrp.setStatus("current")


class _CisIfLimitTotalStorageType_Type(StorageType):
    """Custom type cisIfLimitTotalStorageType based on StorageType"""


_CisIfLimitTotalStorageType_Object = MibTableColumn
cisIfLimitTotalStorageType = _CisIfLimitTotalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 2, 1, 3),
    _CisIfLimitTotalStorageType_Type()
)
cisIfLimitTotalStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfLimitTotalStorageType.setStatus("current")
_CisIfLimitTotalRowStatus_Type = RowStatus
_CisIfLimitTotalRowStatus_Object = MibTableColumn
cisIfLimitTotalRowStatus = _CisIfLimitTotalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 2, 1, 4),
    _CisIfLimitTotalRowStatus_Type()
)
cisIfLimitTotalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfLimitTotalRowStatus.setStatus("current")
_CisIfAccessGroupTable_Object = MibTable
cisIfAccessGroupTable = _CisIfAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 3)
)
if mibBuilder.loadTexts:
    cisIfAccessGroupTable.setStatus("current")
_CisIfAccessGroupEntry_Object = MibTableRow
cisIfAccessGroupEntry = _CisIfAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 3, 1)
)
cisIfAccessGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisIfAccessGroupVlan"),
)
if mibBuilder.loadTexts:
    cisIfAccessGroupEntry.setStatus("current")
_CisIfAccessGroupVlan_Type = VlanIndexOrZero
_CisIfAccessGroupVlan_Object = MibTableColumn
cisIfAccessGroupVlan = _CisIfAccessGroupVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 3, 1, 1),
    _CisIfAccessGroupVlan_Type()
)
cisIfAccessGroupVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisIfAccessGroupVlan.setStatus("current")


class _CisIfAccessGroupsChannelsAllowed_Type(SnmpAdminString):
    """Custom type cisIfAccessGroupsChannelsAllowed based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisIfAccessGroupsChannelsAllowed_Type.__name__ = "SnmpAdminString"
_CisIfAccessGroupsChannelsAllowed_Object = MibTableColumn
cisIfAccessGroupsChannelsAllowed = _CisIfAccessGroupsChannelsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 3, 1, 2),
    _CisIfAccessGroupsChannelsAllowed_Type()
)
cisIfAccessGroupsChannelsAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfAccessGroupsChannelsAllowed.setStatus("current")


class _CisIfAccessGroupStorageType_Type(StorageType):
    """Custom type cisIfAccessGroupStorageType based on StorageType"""


_CisIfAccessGroupStorageType_Object = MibTableColumn
cisIfAccessGroupStorageType = _CisIfAccessGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 3, 1, 3),
    _CisIfAccessGroupStorageType_Type()
)
cisIfAccessGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfAccessGroupStorageType.setStatus("current")
_CisIfAccessGroupRowStatus_Type = RowStatus
_CisIfAccessGroupRowStatus_Object = MibTableColumn
cisIfAccessGroupRowStatus = _CisIfAccessGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 3, 1, 4),
    _CisIfAccessGroupRowStatus_Type()
)
cisIfAccessGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisIfAccessGroupRowStatus.setStatus("current")
_CisVlanFilterConfigTable_Object = MibTable
cisVlanFilterConfigTable = _CisVlanFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 4)
)
if mibBuilder.loadTexts:
    cisVlanFilterConfigTable.setStatus("current")
_CisVlanFilterConfigEntry_Object = MibTableRow
cisVlanFilterConfigEntry = _CisVlanFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 4, 1)
)
cisVlanFilterConfigEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisVlanIndex"),
)
if mibBuilder.loadTexts:
    cisVlanFilterConfigEntry.setStatus("current")
_CisVlanFilterAccessGroup_Type = SnmpAdminString
_CisVlanFilterAccessGroup_Object = MibTableColumn
cisVlanFilterAccessGroup = _CisVlanFilterAccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 4, 1, 1),
    _CisVlanFilterAccessGroup_Type()
)
cisVlanFilterAccessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanFilterAccessGroup.setStatus("current")
_CisVlanFilterLimitMax_Type = Unsigned32
_CisVlanFilterLimitMax_Object = MibTableColumn
cisVlanFilterLimitMax = _CisVlanFilterLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 4, 1, 2),
    _CisVlanFilterLimitMax_Type()
)
cisVlanFilterLimitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanFilterLimitMax.setStatus("current")
_CisVlanFilterLimitExclAccessGrp_Type = SnmpAdminString
_CisVlanFilterLimitExclAccessGrp_Object = MibTableColumn
cisVlanFilterLimitExclAccessGrp = _CisVlanFilterLimitExclAccessGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 4, 1, 3),
    _CisVlanFilterLimitExclAccessGrp_Type()
)
cisVlanFilterLimitExclAccessGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanFilterLimitExclAccessGrp.setStatus("current")
_CisVlanFilterMinVersionAllowed_Type = CisIgmpVersion
_CisVlanFilterMinVersionAllowed_Object = MibTableColumn
cisVlanFilterMinVersionAllowed = _CisVlanFilterMinVersionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 4, 1, 4),
    _CisVlanFilterMinVersionAllowed_Type()
)
cisVlanFilterMinVersionAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanFilterMinVersionAllowed.setStatus("current")
_CisFilterStatsTable_Object = MibTable
cisFilterStatsTable = _CisFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 5)
)
if mibBuilder.loadTexts:
    cisFilterStatsTable.setStatus("current")
_CisFilterStatsEntry_Object = MibTableRow
cisFilterStatsEntry = _CisFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 5, 1)
)
cisFilterStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisFilterStatsVlanNumber"),
)
if mibBuilder.loadTexts:
    cisFilterStatsEntry.setStatus("current")
_CisFilterStatsVlanNumber_Type = VlanIndexOrZero
_CisFilterStatsVlanNumber_Object = MibTableColumn
cisFilterStatsVlanNumber = _CisFilterStatsVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 5, 1, 1),
    _CisFilterStatsVlanNumber_Type()
)
cisFilterStatsVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisFilterStatsVlanNumber.setStatus("current")
_CisFilterAccessGroupDenied_Type = Counter32
_CisFilterAccessGroupDenied_Object = MibTableColumn
cisFilterAccessGroupDenied = _CisFilterAccessGroupDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 5, 1, 2),
    _CisFilterAccessGroupDenied_Type()
)
cisFilterAccessGroupDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisFilterAccessGroupDenied.setStatus("current")
_CisFilterLimitDenied_Type = Counter32
_CisFilterLimitDenied_Object = MibTableColumn
cisFilterLimitDenied = _CisFilterLimitDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 5, 1, 3),
    _CisFilterLimitDenied_Type()
)
cisFilterLimitDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisFilterLimitDenied.setStatus("current")
_CisFilterTotalLimitDenied_Type = Counter32
_CisFilterTotalLimitDenied_Object = MibTableColumn
cisFilterTotalLimitDenied = _CisFilterTotalLimitDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 5, 1, 4),
    _CisFilterTotalLimitDenied_Type()
)
cisFilterTotalLimitDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisFilterTotalLimitDenied.setStatus("current")
_CisFilterMinVersionDenied_Type = Counter32
_CisFilterMinVersionDenied_Object = MibTableColumn
cisFilterMinVersionDenied = _CisFilterMinVersionDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 10, 5, 1, 5),
    _CisFilterMinVersionDenied_Type()
)
cisFilterMinVersionDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisFilterMinVersionDenied.setStatus("current")
_CisExplicitTrackingInfo_ObjectIdentity = ObjectIdentity
cisExplicitTrackingInfo = _CisExplicitTrackingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 11)
)
_CisVlanExplicitTrackingTable_Object = MibTable
cisVlanExplicitTrackingTable = _CisVlanExplicitTrackingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cisVlanExplicitTrackingTable.setStatus("current")
_CisVlanExplicitTrackingEntry_Object = MibTableRow
cisVlanExplicitTrackingEntry = _CisVlanExplicitTrackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 11, 1, 1)
)
cisVlanExplicitTrackingEntry.setIndexNames(
    (0, "CISCO-IGMP-SNOOPING-MIB", "cisVlanIndex"),
)
if mibBuilder.loadTexts:
    cisVlanExplicitTrackingEntry.setStatus("current")
_CisVlanExplicitTrackingEnabled_Type = TruthValue
_CisVlanExplicitTrackingEnabled_Object = MibTableColumn
cisVlanExplicitTrackingEnabled = _CisVlanExplicitTrackingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 11, 1, 1, 1),
    _CisVlanExplicitTrackingEnabled_Type()
)
cisVlanExplicitTrackingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanExplicitTrackingEnabled.setStatus("current")


class _CisVlanExplicitTrackingLimit_Type(Integer32):
    """Custom type cisVlanExplicitTrackingLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_CisVlanExplicitTrackingLimit_Type.__name__ = "Integer32"
_CisVlanExplicitTrackingLimit_Object = MibTableColumn
cisVlanExplicitTrackingLimit = _CisVlanExplicitTrackingLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 1, 11, 1, 1, 2),
    _CisVlanExplicitTrackingLimit_Type()
)
cisVlanExplicitTrackingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisVlanExplicitTrackingLimit.setStatus("current")
_CisMIBConformance_ObjectIdentity = ObjectIdentity
cisMIBConformance = _CisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2)
)
_CisMIBCompliances_ObjectIdentity = ObjectIdentity
cisMIBCompliances = _CisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 1)
)
_CisMIBGroups_ObjectIdentity = ObjectIdentity
cisMIBGroups = _CisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2)
)

# Managed Objects groups

cisSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 1)
)
cisSystemGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpSnoopingEnabled")
)
if mibBuilder.loadTexts:
    cisSystemGroup.setStatus("deprecated")

cisSystemV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 2)
)
cisSystemV2Group.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisFastLeaveEnabled")
)
if mibBuilder.loadTexts:
    cisSystemV2Group.setStatus("deprecated")

cisSystemV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 3)
)
cisSystemV3Group.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisV3ProcessEnabledAdminStatus"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisV3ProcessEnabledOperStatus"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisFastBlockEnabled"))
)
if mibBuilder.loadTexts:
    cisSystemV3Group.setStatus("deprecated")

cisStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 4)
)
cisStatsGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisTxGeneralQueries"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisTxGroupSpecificQueries"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisTxReports"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisTxLeaves"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxGeneralQueries"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxGroupSpecificQueries"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxReports"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxLeaves"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxValidPackets"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxInvalidPackets"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxOtherPackets"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxMACGeneralQueries"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisRxTopoNotifications"))
)
if mibBuilder.loadTexts:
    cisStatsGroup.setStatus("current")

cisV3StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 5)
)
cisV3StatsGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisV3Allows"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisV3Blocks"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisV3IsIncluded"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisV3IsExcluded"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisV3ToIncluded"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisV3ToExcluded"))
)
if mibBuilder.loadTexts:
    cisV3StatsGroup.setStatus("current")

cisBaseConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 6)
)
cisBaseConfigGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpSnoopingEnabled")
)
if mibBuilder.loadTexts:
    cisBaseConfigGroup.setStatus("current")

cisGlobalIgmpV3ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 7)
)
cisGlobalIgmpV3ConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisV3ProcessEnabledAdminStatus"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisV3ProcessEnabledOperStatus"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisFastBlockEnabled"))
)
if mibBuilder.loadTexts:
    cisGlobalIgmpV3ConfigGroup.setStatus("current")

cisGlobalIgmpV3InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 8)
)
cisGlobalIgmpV3InfoGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisV3SnoopingSupport")
)
if mibBuilder.loadTexts:
    cisGlobalIgmpV3InfoGroup.setStatus("current")

cisExtConfig1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 9)
)
cisExtConfig1Group.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisFastLeaveEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisAdminMode"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisOperMode"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisLeaveQueryType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisAddressAliasingMode"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisFallbackTime"))
)
if mibBuilder.loadTexts:
    cisExtConfig1Group.setStatus("current")

cisExtConfig2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 10)
)
cisExtConfig2Group.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisReportSuppressionEnabled")
)
if mibBuilder.loadTexts:
    cisExtConfig2Group.setStatus("current")

cisGlobalTcnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 11)
)
cisGlobalTcnGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisTopoChangeFloodQueryCount"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisTopoChangeQuerySolicitEnabled"))
)
if mibBuilder.loadTexts:
    cisGlobalTcnGroup.setStatus("current")

cisGlobalSourceOnlyLearnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 12)
)
cisGlobalSourceOnlyLearnGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisSourceOnlyLearningEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisSourceOnlyEntryAgeTime"))
)
if mibBuilder.loadTexts:
    cisGlobalSourceOnlyLearnGroup.setStatus("deprecated")

cisRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 13)
)
cisRateLimitGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisGeneralQueryRateLimit"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisDvmrpRateLimit"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMospf1RateLimit"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMospf2RateLimit"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisPimV2RateLimit"))
)
if mibBuilder.loadTexts:
    cisRateLimitGroup.setStatus("deprecated")

cisVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 14)
)
cisVlanConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisVlanIgmpSnoopingEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanFastLeaveEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanIgmpSnoopingOperMode"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanIgmpSnoopingLearningMode"))
)
if mibBuilder.loadTexts:
    cisVlanConfigGroup.setStatus("current")

cisIgmpQuerierConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 15)
)
cisIgmpQuerierConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierState"))
)
if mibBuilder.loadTexts:
    cisIgmpQuerierConfigGroup.setStatus("current")

cisIgmpQuerierInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 16)
)
cisIgmpQuerierInfoGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierVersion"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierAddressType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierAddress"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierInterface"))
)
if mibBuilder.loadTexts:
    cisIgmpQuerierInfoGroup.setStatus("current")

cisMcastRouterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 17)
)
cisMcastRouterConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisMcastRouterType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMcastRouterRowStatus"))
)
if mibBuilder.loadTexts:
    cisMcastRouterConfigGroup.setStatus("deprecated")

cisMcastGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 18)
)
cisMcastGroupInfoGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisMcastGroupFilterMode"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMcastGroupIgmpVersion"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMcastGroupIncludeHostCount"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMcastGroupExcludeHostCount"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMcastGroupPortList"))
)
if mibBuilder.loadTexts:
    cisMcastGroupInfoGroup.setStatus("deprecated")

cisIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 19)
)
cisIfConfigGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisIfTopoChangeFloodEnabled")
)
if mibBuilder.loadTexts:
    cisIfConfigGroup.setStatus("current")

cisL2EntryLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 20)
)
cisL2EntryLimitGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisL2EntryLimit")
)
if mibBuilder.loadTexts:
    cisL2EntryLimitGroup.setStatus("current")

cisTrackingLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 21)
)
cisTrackingLimitGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisEntryTrackingLimit")
)
if mibBuilder.loadTexts:
    cisTrackingLimitGroup.setStatus("current")

cisSourceOnlyLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 22)
)
cisSourceOnlyLimitGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisSourceOnlyPercentageScanLimit"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisSourceOnlyLearningLimit"))
)
if mibBuilder.loadTexts:
    cisSourceOnlyLimitGroup.setStatus("current")

cisRateLimitGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 23)
)
cisRateLimitGroup2.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisRateLimit")
)
if mibBuilder.loadTexts:
    cisRateLimitGroup2.setStatus("current")

cisVlanConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 24)
)
cisVlanConfigGroup2.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisVlanReportSuppressionEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanLeaveQueryInterval"))
)
if mibBuilder.loadTexts:
    cisVlanConfigGroup2.setStatus("current")

cisSourceOnlyAgeTimerInSecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 25)
)
cisSourceOnlyAgeTimerInSecGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisSourceOnlyLearningEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisSourceOnlyEntryAgingTime"))
)
if mibBuilder.loadTexts:
    cisSourceOnlyAgeTimerInSecGroup.setStatus("current")

cisMulticastGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 26)
)
cisMulticastGroupInfoGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupGroupType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupIgmpVersion"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupSourceUpTime"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupSourceExpires"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupInclHostCount"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupExclHostCount"))
)
if mibBuilder.loadTexts:
    cisMulticastGroupInfoGroup.setStatus("current")

cisMulticastGroupPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 27)
)
cisMulticastGroupPortInfoGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupPortList")
)
if mibBuilder.loadTexts:
    cisMulticastGroupPortInfoGroup.setStatus("current")

cisMulticastGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 28)
)
cisMulticastGroupConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfPortList"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfStorageType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMulticastGroupConfRowStatus"))
)
if mibBuilder.loadTexts:
    cisMulticastGroupConfigGroup.setStatus("current")

cisMulticastRouterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 29)
)
cisMulticastRouterConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisMcastRouterConfigRouterType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMcastRouterConfigStorageType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisMcastRouterConfigRowStatus"))
)
if mibBuilder.loadTexts:
    cisMulticastRouterConfigGroup.setStatus("current")

cisLeaveQueryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 30)
)
cisLeaveQueryConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisLastMemberQueryCount"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisLastMemberQueryInterval"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanLastMemberQueryCount"))
)
if mibBuilder.loadTexts:
    cisLeaveQueryConfigGroup.setStatus("current")

cisQuerierGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 31)
)
cisQuerierGlobalConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisQuerierEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisQuerierTcnQueryInterval"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisQuerierTimerExpiry"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisQuerierMaxResponseTime"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisQuerierQueryInterval"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisQuerierAddressType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisQuerierAddress"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisQuerierVersion"))
)
if mibBuilder.loadTexts:
    cisQuerierGlobalConfigGroup.setStatus("current")

cisIgmpQuerierConfigExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 32)
)
cisIgmpQuerierConfigExtGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierTcnQueryCount"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierTcnQueryInterval"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierTimerExpiry"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierMaxResponseTime"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierQueryInterval"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierAdminAddressType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierAdminAddress"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierAdminVersion"))
)
if mibBuilder.loadTexts:
    cisIgmpQuerierConfigExtGroup.setStatus("current")

cisRobustnessConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 33)
)
cisRobustnessConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisRobustnessVariable"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanRobustnessVariable"))
)
if mibBuilder.loadTexts:
    cisRobustnessConfigGroup.setStatus("current")

cisTimeToLiveConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 34)
)
cisTimeToLiveConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisTimeToLiveCheckEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanTimeToLiveCheckEnabled"))
)
if mibBuilder.loadTexts:
    cisTimeToLiveConfigGroup.setStatus("current")

cisRouterAlertConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 35)
)
cisRouterAlertConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisRouterAlertCheckEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanRouterAlertCheckEnabled"))
)
if mibBuilder.loadTexts:
    cisRouterAlertConfigGroup.setStatus("current")

cisVlanExplicitTrackingCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 36)
)
cisVlanExplicitTrackingCfgGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisVlanExplicitTrackingEnabled"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanExplicitTrackingLimit"))
)
if mibBuilder.loadTexts:
    cisVlanExplicitTrackingCfgGroup.setStatus("current")

cisIfLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 37)
)
cisIfLimitGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisIfLimitMax"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIfLimitExcludeAccessGrp"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIfLimitStorageType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIfLimitRowStatus"))
)
if mibBuilder.loadTexts:
    cisIfLimitGroup.setStatus("current")

cisIfLimitTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 38)
)
cisIfLimitTotalGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisIfLimitTotalLimitMax"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIfLimitTotalExcludeAccessGrp"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIfLimitTotalStorageType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIfLimitTotalRowStatus"))
)
if mibBuilder.loadTexts:
    cisIfLimitTotalGroup.setStatus("current")

cisIfAccessGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 39)
)
cisIfAccessGroupGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisIfAccessGroupsChannelsAllowed"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIfAccessGroupStorageType"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisIfAccessGroupRowStatus"))
)
if mibBuilder.loadTexts:
    cisIfAccessGroupGroup.setStatus("current")

cisVlanFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 40)
)
cisVlanFilterConfigGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisVlanFilterAccessGroup"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanFilterLimitMax"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanFilterLimitExclAccessGrp"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisVlanFilterMinVersionAllowed"))
)
if mibBuilder.loadTexts:
    cisVlanFilterConfigGroup.setStatus("current")

cisFilterStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 41)
)
cisFilterStatisticsGroup.setObjects(
      *(("CISCO-IGMP-SNOOPING-MIB", "cisFilterAccessGroupDenied"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisFilterLimitDenied"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisFilterTotalLimitDenied"),
        ("CISCO-IGMP-SNOOPING-MIB", "cisFilterMinVersionDenied"))
)
if mibBuilder.loadTexts:
    cisFilterStatisticsGroup.setStatus("current")

cisQuerierGlobalTcnQueryCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 42)
)
cisQuerierGlobalTcnQueryCountGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisQuerierTcnQueryCount")
)
if mibBuilder.loadTexts:
    cisQuerierGlobalTcnQueryCountGroup.setStatus("current")

cisQuerierTcnQueryPendingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 2, 43)
)
cisQuerierTcnQueryPendingGroup.setObjects(
    ("CISCO-IGMP-SNOOPING-MIB", "cisIgmpQuerierTcnQueryPending")
)
if mibBuilder.loadTexts:
    cisQuerierTcnQueryPendingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cisV2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cisV2Compliance.setStatus(
        "deprecated"
    )

cisV3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cisV3Compliance.setStatus(
        "deprecated"
    )

cisIgmpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cisIgmpSnoopingMIBCompliance.setStatus(
        "deprecated"
    )

cisIgmpSnoopingMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cisIgmpSnoopingMIBCompliance2.setStatus(
        "deprecated"
    )

cisIgmpSnoopingMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 263, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cisIgmpSnoopingMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IGMP-SNOOPING-MIB",
    **{"CisIgmpMode": CisIgmpMode,
       "CisIgmpVersion": CisIgmpVersion,
       "ciscoIgmpSnoopingMIB": ciscoIgmpSnoopingMIB,
       "ciscoIgmpSnoopingNotification": ciscoIgmpSnoopingNotification,
       "ciscoIgmpSnoopingMIBObject": ciscoIgmpSnoopingMIBObject,
       "cisSystemInfo": cisSystemInfo,
       "cisIgmpSnoopingEnabled": cisIgmpSnoopingEnabled,
       "cisV3ProcessEnabledAdminStatus": cisV3ProcessEnabledAdminStatus,
       "cisV3ProcessEnabledOperStatus": cisV3ProcessEnabledOperStatus,
       "cisFastLeaveEnabled": cisFastLeaveEnabled,
       "cisFastBlockEnabled": cisFastBlockEnabled,
       "cisAdminMode": cisAdminMode,
       "cisOperMode": cisOperMode,
       "cisLeaveQueryType": cisLeaveQueryType,
       "cisAddressAliasingMode": cisAddressAliasingMode,
       "cisFallbackTime": cisFallbackTime,
       "cisReportSuppressionEnabled": cisReportSuppressionEnabled,
       "cisTopoChangeFloodQueryCount": cisTopoChangeFloodQueryCount,
       "cisTopoChangeQuerySolicitEnabled": cisTopoChangeQuerySolicitEnabled,
       "cisSourceOnlyLearningEnabled": cisSourceOnlyLearningEnabled,
       "cisSourceOnlyEntryAgeTime": cisSourceOnlyEntryAgeTime,
       "cisV3SnoopingSupport": cisV3SnoopingSupport,
       "cisSourceOnlyEntryAgingTime": cisSourceOnlyEntryAgingTime,
       "cisRobustnessVariable": cisRobustnessVariable,
       "cisLastMemberQueryInterval": cisLastMemberQueryInterval,
       "cisLastMemberQueryCount": cisLastMemberQueryCount,
       "cisTimeToLiveCheckEnabled": cisTimeToLiveCheckEnabled,
       "cisRouterAlertCheckEnabled": cisRouterAlertCheckEnabled,
       "cisStatisticsInfo": cisStatisticsInfo,
       "cisInterfaceStatsTable": cisInterfaceStatsTable,
       "cisInterfaceStatsEntry": cisInterfaceStatsEntry,
       "cisTxGeneralQueries": cisTxGeneralQueries,
       "cisTxGroupSpecificQueries": cisTxGroupSpecificQueries,
       "cisTxReports": cisTxReports,
       "cisTxLeaves": cisTxLeaves,
       "cisRxGeneralQueries": cisRxGeneralQueries,
       "cisRxGroupSpecificQueries": cisRxGroupSpecificQueries,
       "cisRxReports": cisRxReports,
       "cisRxLeaves": cisRxLeaves,
       "cisRxValidPackets": cisRxValidPackets,
       "cisRxInvalidPackets": cisRxInvalidPackets,
       "cisRxOtherPackets": cisRxOtherPackets,
       "cisRxMACGeneralQueries": cisRxMACGeneralQueries,
       "cisRxTopoNotifications": cisRxTopoNotifications,
       "cisV3Allows": cisV3Allows,
       "cisV3Blocks": cisV3Blocks,
       "cisV3IsIncluded": cisV3IsIncluded,
       "cisV3IsExcluded": cisV3IsExcluded,
       "cisV3ToIncluded": cisV3ToIncluded,
       "cisV3ToExcluded": cisV3ToExcluded,
       "cisRateLimitInfo": cisRateLimitInfo,
       "cisGeneralQueryRateLimit": cisGeneralQueryRateLimit,
       "cisDvmrpRateLimit": cisDvmrpRateLimit,
       "cisMospf1RateLimit": cisMospf1RateLimit,
       "cisMospf2RateLimit": cisMospf2RateLimit,
       "cisPimV2RateLimit": cisPimV2RateLimit,
       "cisRateLimit": cisRateLimit,
       "cisVlanConfigInfo": cisVlanConfigInfo,
       "cisVlanConfigTable": cisVlanConfigTable,
       "cisVlanConfigEntry": cisVlanConfigEntry,
       "cisVlanIndex": cisVlanIndex,
       "cisVlanIgmpSnoopingEnabled": cisVlanIgmpSnoopingEnabled,
       "cisVlanFastLeaveEnabled": cisVlanFastLeaveEnabled,
       "cisVlanIgmpSnoopingOperMode": cisVlanIgmpSnoopingOperMode,
       "cisVlanIgmpSnoopingLearningMode": cisVlanIgmpSnoopingLearningMode,
       "cisVlanReportSuppressionEnabled": cisVlanReportSuppressionEnabled,
       "cisVlanLeaveQueryInterval": cisVlanLeaveQueryInterval,
       "cisVlanLastMemberQueryCount": cisVlanLastMemberQueryCount,
       "cisVlanRobustnessVariable": cisVlanRobustnessVariable,
       "cisVlanTimeToLiveCheckEnabled": cisVlanTimeToLiveCheckEnabled,
       "cisVlanRouterAlertCheckEnabled": cisVlanRouterAlertCheckEnabled,
       "cisIgmpQuerierTable": cisIgmpQuerierTable,
       "cisIgmpQuerierEntry": cisIgmpQuerierEntry,
       "cisIgmpQuerierVlanIndex": cisIgmpQuerierVlanIndex,
       "cisIgmpQuerierEnabled": cisIgmpQuerierEnabled,
       "cisIgmpQuerierState": cisIgmpQuerierState,
       "cisIgmpQuerierVersion": cisIgmpQuerierVersion,
       "cisIgmpQuerierAddressType": cisIgmpQuerierAddressType,
       "cisIgmpQuerierAddress": cisIgmpQuerierAddress,
       "cisIgmpQuerierInterface": cisIgmpQuerierInterface,
       "cisIgmpQuerierTcnQueryCount": cisIgmpQuerierTcnQueryCount,
       "cisIgmpQuerierTcnQueryInterval": cisIgmpQuerierTcnQueryInterval,
       "cisIgmpQuerierTimerExpiry": cisIgmpQuerierTimerExpiry,
       "cisIgmpQuerierMaxResponseTime": cisIgmpQuerierMaxResponseTime,
       "cisIgmpQuerierQueryInterval": cisIgmpQuerierQueryInterval,
       "cisIgmpQuerierAdminAddressType": cisIgmpQuerierAdminAddressType,
       "cisIgmpQuerierAdminAddress": cisIgmpQuerierAdminAddress,
       "cisIgmpQuerierAdminVersion": cisIgmpQuerierAdminVersion,
       "cisIgmpQuerierTcnQueryPending": cisIgmpQuerierTcnQueryPending,
       "cisIfConfigInfo": cisIfConfigInfo,
       "cisIfConfigTable": cisIfConfigTable,
       "cisIfConfigEntry": cisIfConfigEntry,
       "cisIfTopoChangeFloodEnabled": cisIfTopoChangeFloodEnabled,
       "cisMulticastRouterInfo": cisMulticastRouterInfo,
       "cisMcastRouterCfgTable": cisMcastRouterCfgTable,
       "cisMcastRouterCfgEntry": cisMcastRouterCfgEntry,
       "cisMcastRouterVlanIndex": cisMcastRouterVlanIndex,
       "cisMcastRouterType": cisMcastRouterType,
       "cisMcastRouterRowStatus": cisMcastRouterRowStatus,
       "cisMcastRouterConfigTable": cisMcastRouterConfigTable,
       "cisMcastRouterConfigEntry": cisMcastRouterConfigEntry,
       "cisMcastRouterConfigVlanIndex": cisMcastRouterConfigVlanIndex,
       "cisMcastRouterConfigRouterType": cisMcastRouterConfigRouterType,
       "cisMcastRouterConfigStorageType": cisMcastRouterConfigStorageType,
       "cisMcastRouterConfigRowStatus": cisMcastRouterConfigRowStatus,
       "cisMulticastGroupInfo": cisMulticastGroupInfo,
       "cisMcastGroupTable": cisMcastGroupTable,
       "cisMcastGroupEntry": cisMcastGroupEntry,
       "cisMcastGroupVlanIndex": cisMcastGroupVlanIndex,
       "cisMcastGroupAddressType": cisMcastGroupAddressType,
       "cisMcastGroupAddress": cisMcastGroupAddress,
       "cisMcastGroupFilterMode": cisMcastGroupFilterMode,
       "cisMcastGroupIgmpVersion": cisMcastGroupIgmpVersion,
       "cisMcastGroupIncludeHostCount": cisMcastGroupIncludeHostCount,
       "cisMcastGroupExcludeHostCount": cisMcastGroupExcludeHostCount,
       "cisMcastGroupPortList": cisMcastGroupPortList,
       "cisMulticastGroupTable": cisMulticastGroupTable,
       "cisMulticastGroupEntry": cisMulticastGroupEntry,
       "cisMulticastGroupVlanIndex": cisMulticastGroupVlanIndex,
       "cisMulticastGroupCeVlanIndex": cisMulticastGroupCeVlanIndex,
       "cisMulticastGroupAddressType": cisMulticastGroupAddressType,
       "cisMulticastGroupAddress": cisMulticastGroupAddress,
       "cisMulticastGroupSourceAddress": cisMulticastGroupSourceAddress,
       "cisMulticastGroupGroupType": cisMulticastGroupGroupType,
       "cisMulticastGroupIgmpVersion": cisMulticastGroupIgmpVersion,
       "cisMulticastGroupSourceUpTime": cisMulticastGroupSourceUpTime,
       "cisMulticastGroupSourceExpires": cisMulticastGroupSourceExpires,
       "cisMulticastGroupInclHostCount": cisMulticastGroupInclHostCount,
       "cisMulticastGroupExclHostCount": cisMulticastGroupExclHostCount,
       "cisMulticastGroupPortListTable": cisMulticastGroupPortListTable,
       "cisMulticastGroupPortListEntry": cisMulticastGroupPortListEntry,
       "cisMulticastGroupPortRangeIndex": cisMulticastGroupPortRangeIndex,
       "cisMulticastGroupPortList": cisMulticastGroupPortList,
       "cisMulticastGroupConfigTable": cisMulticastGroupConfigTable,
       "cisMulticastGroupConfigEntry": cisMulticastGroupConfigEntry,
       "cisMulticastGroupConfVlanIndex": cisMulticastGroupConfVlanIndex,
       "cisMulticastGroupConfCeVlanIndex": cisMulticastGroupConfCeVlanIndex,
       "cisMulticastGroupConfAddressType": cisMulticastGroupConfAddressType,
       "cisMulticastGroupConfAddress": cisMulticastGroupConfAddress,
       "cisMulticastGroupConfSourceAddress": cisMulticastGroupConfSourceAddress,
       "cisMulticastGroupConfPortRange": cisMulticastGroupConfPortRange,
       "cisMulticastGroupConfPortList": cisMulticastGroupConfPortList,
       "cisMulticastGroupConfStorageType": cisMulticastGroupConfStorageType,
       "cisMulticastGroupConfRowStatus": cisMulticastGroupConfRowStatus,
       "cisResourceLimitInfo": cisResourceLimitInfo,
       "cisL2EntryLimit": cisL2EntryLimit,
       "cisEntryTrackingLimit": cisEntryTrackingLimit,
       "cisSourceOnlyPercentageScanLimit": cisSourceOnlyPercentageScanLimit,
       "cisSourceOnlyLearningLimit": cisSourceOnlyLearningLimit,
       "cisQuerierConfigInfo": cisQuerierConfigInfo,
       "cisQuerierEnabled": cisQuerierEnabled,
       "cisQuerierTcnQueryInterval": cisQuerierTcnQueryInterval,
       "cisQuerierTimerExpiry": cisQuerierTimerExpiry,
       "cisQuerierMaxResponseTime": cisQuerierMaxResponseTime,
       "cisQuerierQueryInterval": cisQuerierQueryInterval,
       "cisQuerierAddressType": cisQuerierAddressType,
       "cisQuerierAddress": cisQuerierAddress,
       "cisQuerierVersion": cisQuerierVersion,
       "cisQuerierTcnQueryCount": cisQuerierTcnQueryCount,
       "cisFilteringInfo": cisFilteringInfo,
       "cisIfLimitTable": cisIfLimitTable,
       "cisIfLimitEntry": cisIfLimitEntry,
       "cisIfLimitVlanNumber": cisIfLimitVlanNumber,
       "cisIfLimitMax": cisIfLimitMax,
       "cisIfLimitExcludeAccessGrp": cisIfLimitExcludeAccessGrp,
       "cisIfLimitStorageType": cisIfLimitStorageType,
       "cisIfLimitRowStatus": cisIfLimitRowStatus,
       "cisIfLimitTotalTable": cisIfLimitTotalTable,
       "cisIfLimitTotalEntry": cisIfLimitTotalEntry,
       "cisIfLimitTotalLimitMax": cisIfLimitTotalLimitMax,
       "cisIfLimitTotalExcludeAccessGrp": cisIfLimitTotalExcludeAccessGrp,
       "cisIfLimitTotalStorageType": cisIfLimitTotalStorageType,
       "cisIfLimitTotalRowStatus": cisIfLimitTotalRowStatus,
       "cisIfAccessGroupTable": cisIfAccessGroupTable,
       "cisIfAccessGroupEntry": cisIfAccessGroupEntry,
       "cisIfAccessGroupVlan": cisIfAccessGroupVlan,
       "cisIfAccessGroupsChannelsAllowed": cisIfAccessGroupsChannelsAllowed,
       "cisIfAccessGroupStorageType": cisIfAccessGroupStorageType,
       "cisIfAccessGroupRowStatus": cisIfAccessGroupRowStatus,
       "cisVlanFilterConfigTable": cisVlanFilterConfigTable,
       "cisVlanFilterConfigEntry": cisVlanFilterConfigEntry,
       "cisVlanFilterAccessGroup": cisVlanFilterAccessGroup,
       "cisVlanFilterLimitMax": cisVlanFilterLimitMax,
       "cisVlanFilterLimitExclAccessGrp": cisVlanFilterLimitExclAccessGrp,
       "cisVlanFilterMinVersionAllowed": cisVlanFilterMinVersionAllowed,
       "cisFilterStatsTable": cisFilterStatsTable,
       "cisFilterStatsEntry": cisFilterStatsEntry,
       "cisFilterStatsVlanNumber": cisFilterStatsVlanNumber,
       "cisFilterAccessGroupDenied": cisFilterAccessGroupDenied,
       "cisFilterLimitDenied": cisFilterLimitDenied,
       "cisFilterTotalLimitDenied": cisFilterTotalLimitDenied,
       "cisFilterMinVersionDenied": cisFilterMinVersionDenied,
       "cisExplicitTrackingInfo": cisExplicitTrackingInfo,
       "cisVlanExplicitTrackingTable": cisVlanExplicitTrackingTable,
       "cisVlanExplicitTrackingEntry": cisVlanExplicitTrackingEntry,
       "cisVlanExplicitTrackingEnabled": cisVlanExplicitTrackingEnabled,
       "cisVlanExplicitTrackingLimit": cisVlanExplicitTrackingLimit,
       "cisMIBConformance": cisMIBConformance,
       "cisMIBCompliances": cisMIBCompliances,
       "cisV2Compliance": cisV2Compliance,
       "cisV3Compliance": cisV3Compliance,
       "cisIgmpSnoopingMIBCompliance": cisIgmpSnoopingMIBCompliance,
       "cisIgmpSnoopingMIBCompliance2": cisIgmpSnoopingMIBCompliance2,
       "cisIgmpSnoopingMIBCompliance3": cisIgmpSnoopingMIBCompliance3,
       "cisMIBGroups": cisMIBGroups,
       "cisSystemGroup": cisSystemGroup,
       "cisSystemV2Group": cisSystemV2Group,
       "cisSystemV3Group": cisSystemV3Group,
       "cisStatsGroup": cisStatsGroup,
       "cisV3StatsGroup": cisV3StatsGroup,
       "cisBaseConfigGroup": cisBaseConfigGroup,
       "cisGlobalIgmpV3ConfigGroup": cisGlobalIgmpV3ConfigGroup,
       "cisGlobalIgmpV3InfoGroup": cisGlobalIgmpV3InfoGroup,
       "cisExtConfig1Group": cisExtConfig1Group,
       "cisExtConfig2Group": cisExtConfig2Group,
       "cisGlobalTcnGroup": cisGlobalTcnGroup,
       "cisGlobalSourceOnlyLearnGroup": cisGlobalSourceOnlyLearnGroup,
       "cisRateLimitGroup": cisRateLimitGroup,
       "cisVlanConfigGroup": cisVlanConfigGroup,
       "cisIgmpQuerierConfigGroup": cisIgmpQuerierConfigGroup,
       "cisIgmpQuerierInfoGroup": cisIgmpQuerierInfoGroup,
       "cisMcastRouterConfigGroup": cisMcastRouterConfigGroup,
       "cisMcastGroupInfoGroup": cisMcastGroupInfoGroup,
       "cisIfConfigGroup": cisIfConfigGroup,
       "cisL2EntryLimitGroup": cisL2EntryLimitGroup,
       "cisTrackingLimitGroup": cisTrackingLimitGroup,
       "cisSourceOnlyLimitGroup": cisSourceOnlyLimitGroup,
       "cisRateLimitGroup2": cisRateLimitGroup2,
       "cisVlanConfigGroup2": cisVlanConfigGroup2,
       "cisSourceOnlyAgeTimerInSecGroup": cisSourceOnlyAgeTimerInSecGroup,
       "cisMulticastGroupInfoGroup": cisMulticastGroupInfoGroup,
       "cisMulticastGroupPortInfoGroup": cisMulticastGroupPortInfoGroup,
       "cisMulticastGroupConfigGroup": cisMulticastGroupConfigGroup,
       "cisMulticastRouterConfigGroup": cisMulticastRouterConfigGroup,
       "cisLeaveQueryConfigGroup": cisLeaveQueryConfigGroup,
       "cisQuerierGlobalConfigGroup": cisQuerierGlobalConfigGroup,
       "cisIgmpQuerierConfigExtGroup": cisIgmpQuerierConfigExtGroup,
       "cisRobustnessConfigGroup": cisRobustnessConfigGroup,
       "cisTimeToLiveConfigGroup": cisTimeToLiveConfigGroup,
       "cisRouterAlertConfigGroup": cisRouterAlertConfigGroup,
       "cisVlanExplicitTrackingCfgGroup": cisVlanExplicitTrackingCfgGroup,
       "cisIfLimitGroup": cisIfLimitGroup,
       "cisIfLimitTotalGroup": cisIfLimitTotalGroup,
       "cisIfAccessGroupGroup": cisIfAccessGroupGroup,
       "cisVlanFilterConfigGroup": cisVlanFilterConfigGroup,
       "cisFilterStatisticsGroup": cisFilterStatisticsGroup,
       "cisQuerierGlobalTcnQueryCountGroup": cisQuerierGlobalTcnQueryCountGroup,
       "cisQuerierTcnQueryPendingGroup": cisQuerierTcnQueryPendingGroup}
)
