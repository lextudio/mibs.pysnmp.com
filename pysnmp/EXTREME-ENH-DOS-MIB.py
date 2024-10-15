# SNMP MIB module (EXTREME-ENH-DOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,
 extremeV2Traps) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent",
    "extremeV2Traps")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeEnhDosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeEnhDosProtect_ObjectIdentity = ObjectIdentity
extremeEnhDosProtect = _ExtremeEnhDosProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1)
)


class _ExtremeEnhDosEnableRateLimit_Type(TruthValue):
    """Custom type extremeEnhDosEnableRateLimit based on TruthValue"""


_ExtremeEnhDosEnableRateLimit_Object = MibScalar
extremeEnhDosEnableRateLimit = _ExtremeEnhDosEnableRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 1),
    _ExtremeEnhDosEnableRateLimit_Type()
)
extremeEnhDosEnableRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEnhDosEnableRateLimit.setStatus("current")


class _ExtremeEnhDosEnableIpFdb_Type(TruthValue):
    """Custom type extremeEnhDosEnableIpFdb based on TruthValue"""


_ExtremeEnhDosEnableIpFdb_Object = MibScalar
extremeEnhDosEnableIpFdb = _ExtremeEnhDosEnableIpFdb_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 2),
    _ExtremeEnhDosEnableIpFdb_Type()
)
extremeEnhDosEnableIpFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEnhDosEnableIpFdb.setStatus("current")


class _ExtremeEnhDosEnableBenchMark_Type(TruthValue):
    """Custom type extremeEnhDosEnableBenchMark based on TruthValue"""


_ExtremeEnhDosEnableBenchMark_Object = MibScalar
extremeEnhDosEnableBenchMark = _ExtremeEnhDosEnableBenchMark_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 3),
    _ExtremeEnhDosEnableBenchMark_Type()
)
extremeEnhDosEnableBenchMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEnhDosEnableBenchMark.setStatus("current")


class _ExtremeEnhDosCacheSize_Type(Integer32):
    """Custom type extremeEnhDosCacheSize based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 262144),
    )


_ExtremeEnhDosCacheSize_Type.__name__ = "Integer32"
_ExtremeEnhDosCacheSize_Object = MibScalar
extremeEnhDosCacheSize = _ExtremeEnhDosCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 4),
    _ExtremeEnhDosCacheSize_Type()
)
extremeEnhDosCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEnhDosCacheSize.setStatus("current")
_ExtremeEnhDosPortTable_Object = MibTable
extremeEnhDosPortTable = _ExtremeEnhDosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5)
)
if mibBuilder.loadTexts:
    extremeEnhDosPortTable.setStatus("current")
_ExtremeEnhDosPortEntry_Object = MibTableRow
extremeEnhDosPortEntry = _ExtremeEnhDosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1)
)
extremeEnhDosPortEntry.setIndexNames(
    (0, "EXTREME-ENH-DOS-MIB", "extremeEnhDosPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeEnhDosPortEntry.setStatus("current")
_ExtremeEnhDosPortIfIndex_Type = Integer32
_ExtremeEnhDosPortIfIndex_Object = MibTableColumn
extremeEnhDosPortIfIndex = _ExtremeEnhDosPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 1),
    _ExtremeEnhDosPortIfIndex_Type()
)
extremeEnhDosPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEnhDosPortIfIndex.setStatus("current")


class _ExtremeEnhDosPortTrusted_Type(TruthValue):
    """Custom type extremeEnhDosPortTrusted based on TruthValue"""


_ExtremeEnhDosPortTrusted_Object = MibTableColumn
extremeEnhDosPortTrusted = _ExtremeEnhDosPortTrusted_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 2),
    _ExtremeEnhDosPortTrusted_Type()
)
extremeEnhDosPortTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortTrusted.setStatus("current")


class _ExtremeEnhDosPortAlarmState_Type(TruthValue):
    """Custom type extremeEnhDosPortAlarmState based on TruthValue"""


_ExtremeEnhDosPortAlarmState_Object = MibTableColumn
extremeEnhDosPortAlarmState = _ExtremeEnhDosPortAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 3),
    _ExtremeEnhDosPortAlarmState_Type()
)
extremeEnhDosPortAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEnhDosPortAlarmState.setStatus("current")


class _ExtremeEnhDosPortLearnLimit_Type(Integer32):
    """Custom type extremeEnhDosPortLearnLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1953125),
    )


_ExtremeEnhDosPortLearnLimit_Type.__name__ = "Integer32"
_ExtremeEnhDosPortLearnLimit_Object = MibTableColumn
extremeEnhDosPortLearnLimit = _ExtremeEnhDosPortLearnLimit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 4),
    _ExtremeEnhDosPortLearnLimit_Type()
)
extremeEnhDosPortLearnLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortLearnLimit.setStatus("current")


class _ExtremeEnhDosPortLearnWindow_Type(Integer32):
    """Custom type extremeEnhDosPortLearnWindow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ExtremeEnhDosPortLearnWindow_Type.__name__ = "Integer32"
_ExtremeEnhDosPortLearnWindow_Object = MibTableColumn
extremeEnhDosPortLearnWindow = _ExtremeEnhDosPortLearnWindow_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 5),
    _ExtremeEnhDosPortLearnWindow_Type()
)
extremeEnhDosPortLearnWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortLearnWindow.setStatus("current")


class _ExtremeEnhDosPortAgingTime_Type(Integer32):
    """Custom type extremeEnhDosPortAgingTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ExtremeEnhDosPortAgingTime_Type.__name__ = "Integer32"
_ExtremeEnhDosPortAgingTime_Object = MibTableColumn
extremeEnhDosPortAgingTime = _ExtremeEnhDosPortAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 6),
    _ExtremeEnhDosPortAgingTime_Type()
)
extremeEnhDosPortAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortAgingTime.setStatus("current")


class _ExtremeEnhDosPortRateLimitEnable_Type(TruthValue):
    """Custom type extremeEnhDosPortRateLimitEnable based on TruthValue"""


_ExtremeEnhDosPortRateLimitEnable_Object = MibTableColumn
extremeEnhDosPortRateLimitEnable = _ExtremeEnhDosPortRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 7),
    _ExtremeEnhDosPortRateLimitEnable_Type()
)
extremeEnhDosPortRateLimitEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortRateLimitEnable.setStatus("current")


class _ExtremeEnhDosPortIpFdbEnable_Type(TruthValue):
    """Custom type extremeEnhDosPortIpFdbEnable based on TruthValue"""


_ExtremeEnhDosPortIpFdbEnable_Object = MibTableColumn
extremeEnhDosPortIpFdbEnable = _ExtremeEnhDosPortIpFdbEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 8),
    _ExtremeEnhDosPortIpFdbEnable_Type()
)
extremeEnhDosPortIpFdbEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortIpFdbEnable.setStatus("current")


class _ExtremeEnhDosPortBenchMarkEnable_Type(TruthValue):
    """Custom type extremeEnhDosPortBenchMarkEnable based on TruthValue"""


_ExtremeEnhDosPortBenchMarkEnable_Object = MibTableColumn
extremeEnhDosPortBenchMarkEnable = _ExtremeEnhDosPortBenchMarkEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 9),
    _ExtremeEnhDosPortBenchMarkEnable_Type()
)
extremeEnhDosPortBenchMarkEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortBenchMarkEnable.setStatus("current")


class _ExtremeEnhDosPortRateLimitThreshold_Type(Integer32):
    """Custom type extremeEnhDosPortRateLimitThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1953125),
    )


_ExtremeEnhDosPortRateLimitThreshold_Type.__name__ = "Integer32"
_ExtremeEnhDosPortRateLimitThreshold_Object = MibTableColumn
extremeEnhDosPortRateLimitThreshold = _ExtremeEnhDosPortRateLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 10),
    _ExtremeEnhDosPortRateLimitThreshold_Type()
)
extremeEnhDosPortRateLimitThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortRateLimitThreshold.setStatus("current")


class _ExtremeEnhDosPortRateLimitDropProbability_Type(Integer32):
    """Custom type extremeEnhDosPortRateLimitDropProbability based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_ExtremeEnhDosPortRateLimitDropProbability_Type.__name__ = "Integer32"
_ExtremeEnhDosPortRateLimitDropProbability_Object = MibTableColumn
extremeEnhDosPortRateLimitDropProbability = _ExtremeEnhDosPortRateLimitDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 11),
    _ExtremeEnhDosPortRateLimitDropProbability_Type()
)
extremeEnhDosPortRateLimitDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortRateLimitDropProbability.setStatus("current")


class _ExtremeEnhDosPortRateLimitLearningWindow_Type(Integer32):
    """Custom type extremeEnhDosPortRateLimitLearningWindow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ExtremeEnhDosPortRateLimitLearningWindow_Type.__name__ = "Integer32"
_ExtremeEnhDosPortRateLimitLearningWindow_Object = MibTableColumn
extremeEnhDosPortRateLimitLearningWindow = _ExtremeEnhDosPortRateLimitLearningWindow_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 12),
    _ExtremeEnhDosPortRateLimitLearningWindow_Type()
)
extremeEnhDosPortRateLimitLearningWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortRateLimitLearningWindow.setStatus("current")


class _ExtremeEnhDosPortRateLimitProtocol_Type(Integer32):
    """Custom type extremeEnhDosPortRateLimitProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("icmp", 1))
    )


_ExtremeEnhDosPortRateLimitProtocol_Type.__name__ = "Integer32"
_ExtremeEnhDosPortRateLimitProtocol_Object = MibTableColumn
extremeEnhDosPortRateLimitProtocol = _ExtremeEnhDosPortRateLimitProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 5, 1, 13),
    _ExtremeEnhDosPortRateLimitProtocol_Type()
)
extremeEnhDosPortRateLimitProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEnhDosPortRateLimitProtocol.setStatus("current")
_ExtremeEnhDosPortStatisticsTable_Object = MibTable
extremeEnhDosPortStatisticsTable = _ExtremeEnhDosPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 6)
)
if mibBuilder.loadTexts:
    extremeEnhDosPortStatisticsTable.setStatus("current")
_ExtremeEnhDosPortStatisticsEntry_Object = MibTableRow
extremeEnhDosPortStatisticsEntry = _ExtremeEnhDosPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 6, 1)
)
extremeEnhDosPortStatisticsEntry.setIndexNames(
    (0, "EXTREME-ENH-DOS-MIB", "extremeEnhDosPortStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    extremeEnhDosPortStatisticsEntry.setStatus("current")
_ExtremeEnhDosPortStatisticsIfIndex_Type = Integer32
_ExtremeEnhDosPortStatisticsIfIndex_Object = MibTableColumn
extremeEnhDosPortStatisticsIfIndex = _ExtremeEnhDosPortStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 6, 1, 1),
    _ExtremeEnhDosPortStatisticsIfIndex_Type()
)
extremeEnhDosPortStatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEnhDosPortStatisticsIfIndex.setStatus("current")
_ExtremeEnhDosPortStatisticsRateLimitFilteredPackets_Type = Integer32
_ExtremeEnhDosPortStatisticsRateLimitFilteredPackets_Object = MibTableColumn
extremeEnhDosPortStatisticsRateLimitFilteredPackets = _ExtremeEnhDosPortStatisticsRateLimitFilteredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29, 1, 6, 1, 2),
    _ExtremeEnhDosPortStatisticsRateLimitFilteredPackets_Type()
)
extremeEnhDosPortStatisticsRateLimitFilteredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEnhDosPortStatisticsRateLimitFilteredPackets.setStatus("current")
_ExtremeEnhDosTraps_ObjectIdentity = ObjectIdentity
extremeEnhDosTraps = _ExtremeEnhDosTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 11)
)
_ExtremeEnhDosTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeEnhDosTrapsPrefix = _ExtremeEnhDosTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 11, 0)
)

# Managed Objects groups


# Notification objects

extremeEnhDosThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 11, 0, 1)
)
extremeEnhDosThresholdReached.setObjects(
      *(("EXTREME-ENH-DOS-MIB", "extremeEnhDosPortIfIndex"),
        ("EXTREME-ENH-DOS-MIB", "extremeEnhDosPortRateLimitThreshold"))
)
if mibBuilder.loadTexts:
    extremeEnhDosThresholdReached.setStatus(
        "current"
    )

extremeEnhDosThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 11, 0, 2)
)
extremeEnhDosThresholdCleared.setObjects(
      *(("EXTREME-ENH-DOS-MIB", "extremeEnhDosPortIfIndex"),
        ("EXTREME-ENH-DOS-MIB", "extremeEnhDosPortRateLimitThreshold"))
)
if mibBuilder.loadTexts:
    extremeEnhDosThresholdCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-ENH-DOS-MIB",
    **{"extremeEnhDosMib": extremeEnhDosMib,
       "extremeEnhDosProtect": extremeEnhDosProtect,
       "extremeEnhDosEnableRateLimit": extremeEnhDosEnableRateLimit,
       "extremeEnhDosEnableIpFdb": extremeEnhDosEnableIpFdb,
       "extremeEnhDosEnableBenchMark": extremeEnhDosEnableBenchMark,
       "extremeEnhDosCacheSize": extremeEnhDosCacheSize,
       "extremeEnhDosPortTable": extremeEnhDosPortTable,
       "extremeEnhDosPortEntry": extremeEnhDosPortEntry,
       "extremeEnhDosPortIfIndex": extremeEnhDosPortIfIndex,
       "extremeEnhDosPortTrusted": extremeEnhDosPortTrusted,
       "extremeEnhDosPortAlarmState": extremeEnhDosPortAlarmState,
       "extremeEnhDosPortLearnLimit": extremeEnhDosPortLearnLimit,
       "extremeEnhDosPortLearnWindow": extremeEnhDosPortLearnWindow,
       "extremeEnhDosPortAgingTime": extremeEnhDosPortAgingTime,
       "extremeEnhDosPortRateLimitEnable": extremeEnhDosPortRateLimitEnable,
       "extremeEnhDosPortIpFdbEnable": extremeEnhDosPortIpFdbEnable,
       "extremeEnhDosPortBenchMarkEnable": extremeEnhDosPortBenchMarkEnable,
       "extremeEnhDosPortRateLimitThreshold": extremeEnhDosPortRateLimitThreshold,
       "extremeEnhDosPortRateLimitDropProbability": extremeEnhDosPortRateLimitDropProbability,
       "extremeEnhDosPortRateLimitLearningWindow": extremeEnhDosPortRateLimitLearningWindow,
       "extremeEnhDosPortRateLimitProtocol": extremeEnhDosPortRateLimitProtocol,
       "extremeEnhDosPortStatisticsTable": extremeEnhDosPortStatisticsTable,
       "extremeEnhDosPortStatisticsEntry": extremeEnhDosPortStatisticsEntry,
       "extremeEnhDosPortStatisticsIfIndex": extremeEnhDosPortStatisticsIfIndex,
       "extremeEnhDosPortStatisticsRateLimitFilteredPackets": extremeEnhDosPortStatisticsRateLimitFilteredPackets,
       "extremeEnhDosTraps": extremeEnhDosTraps,
       "extremeEnhDosTrapsPrefix": extremeEnhDosTrapsPrefix,
       "extremeEnhDosThresholdReached": extremeEnhDosThresholdReached,
       "extremeEnhDosThresholdCleared": extremeEnhDosThresholdCleared}
)
