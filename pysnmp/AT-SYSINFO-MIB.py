# SNMP MIB module (AT-SYSINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-SYSINFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:04 2024
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

(DisplayStringUnsized,
 atRouter) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "atRouter")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

sysinfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3)
)
sysinfo.setRevisions(
        ("2012-09-21 00:00",
         "2011-03-14 00:00",
         "2010-09-18 00:00",
         "2010-09-07 00:00",
         "2010-08-31 00:31",
         "2010-08-16 00:16",
         "2010-06-15 00:15",
         "2010-06-04 00:00",
         "2008-02-26 00:00",
         "2006-06-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FanAndPs_ObjectIdentity = ObjectIdentity
fanAndPs = _FanAndPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1)
)
_FanAndPsTrap_ObjectIdentity = ObjectIdentity
fanAndPsTrap = _FanAndPsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0)
)


class _FanAndPsRpsConnectionStatus_Type(Integer32):
    """Custom type fanAndPsRpsConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2),
          ("notMonitoring", 3),
          ("notSupported", 0))
    )


_FanAndPsRpsConnectionStatus_Type.__name__ = "Integer32"
_FanAndPsRpsConnectionStatus_Object = MibScalar
fanAndPsRpsConnectionStatus = _FanAndPsRpsConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 1),
    _FanAndPsRpsConnectionStatus_Type()
)
fanAndPsRpsConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsRpsConnectionStatus.setStatus("current")


class _FanAndPsMainPSUStatus_Type(Integer32):
    """Custom type fanAndPsMainPSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 3),
          ("off", 2),
          ("on", 1))
    )


_FanAndPsMainPSUStatus_Type.__name__ = "Integer32"
_FanAndPsMainPSUStatus_Object = MibScalar
fanAndPsMainPSUStatus = _FanAndPsMainPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 2),
    _FanAndPsMainPSUStatus_Type()
)
fanAndPsMainPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsMainPSUStatus.setStatus("current")


class _FanAndPsRedundantPSUStatus_Type(Integer32):
    """Custom type fanAndPsRedundantPSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notMonitoring", 3),
          ("notSupported", 0),
          ("off", 2),
          ("on", 1))
    )


_FanAndPsRedundantPSUStatus_Type.__name__ = "Integer32"
_FanAndPsRedundantPSUStatus_Object = MibScalar
fanAndPsRedundantPSUStatus = _FanAndPsRedundantPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 3),
    _FanAndPsRedundantPSUStatus_Type()
)
fanAndPsRedundantPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsRedundantPSUStatus.setStatus("current")


class _FanAndPsRpsMonitoringStatus_Type(Integer32):
    """Custom type fanAndPsRpsMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("off", 2),
          ("on", 1))
    )


_FanAndPsRpsMonitoringStatus_Type.__name__ = "Integer32"
_FanAndPsRpsMonitoringStatus_Object = MibScalar
fanAndPsRpsMonitoringStatus = _FanAndPsRpsMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 4),
    _FanAndPsRpsMonitoringStatus_Type()
)
fanAndPsRpsMonitoringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanAndPsRpsMonitoringStatus.setStatus("current")


class _FanAndPsMainFanStatus_Type(Integer32):
    """Custom type fanAndPsMainFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("notSupported", 0),
          ("ok", 1),
          ("warning", 3))
    )


_FanAndPsMainFanStatus_Type.__name__ = "Integer32"
_FanAndPsMainFanStatus_Object = MibScalar
fanAndPsMainFanStatus = _FanAndPsMainFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 5),
    _FanAndPsMainFanStatus_Type()
)
fanAndPsMainFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsMainFanStatus.setStatus("current")


class _FanAndPsRedundantFanStatus_Type(Integer32):
    """Custom type fanAndPsRedundantFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notMonitoring", 3),
          ("notOk", 2),
          ("notSupported", 0),
          ("ok", 1))
    )


_FanAndPsRedundantFanStatus_Type.__name__ = "Integer32"
_FanAndPsRedundantFanStatus_Object = MibScalar
fanAndPsRedundantFanStatus = _FanAndPsRedundantFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 6),
    _FanAndPsRedundantFanStatus_Type()
)
fanAndPsRedundantFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsRedundantFanStatus.setStatus("current")


class _FanAndPsTemperatureStatus_Type(Integer32):
    """Custom type fanAndPsTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("ok", 1))
    )


_FanAndPsTemperatureStatus_Type.__name__ = "Integer32"
_FanAndPsTemperatureStatus_Object = MibScalar
fanAndPsTemperatureStatus = _FanAndPsTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 7),
    _FanAndPsTemperatureStatus_Type()
)
fanAndPsTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsTemperatureStatus.setStatus("current")


class _FanAndPsFanTrayPresent_Type(Integer32):
    """Custom type fanAndPsFanTrayPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("notSupported", 0),
          ("present", 1))
    )


_FanAndPsFanTrayPresent_Type.__name__ = "Integer32"
_FanAndPsFanTrayPresent_Object = MibScalar
fanAndPsFanTrayPresent = _FanAndPsFanTrayPresent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 8),
    _FanAndPsFanTrayPresent_Type()
)
fanAndPsFanTrayPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsFanTrayPresent.setStatus("current")


class _FanAndPsFanTrayStatus_Type(Integer32):
    """Custom type fanAndPsFanTrayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("notSupported", 0),
          ("ok", 1))
    )


_FanAndPsFanTrayStatus_Type.__name__ = "Integer32"
_FanAndPsFanTrayStatus_Object = MibScalar
fanAndPsFanTrayStatus = _FanAndPsFanTrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 9),
    _FanAndPsFanTrayStatus_Type()
)
fanAndPsFanTrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsFanTrayStatus.setStatus("current")


class _FanAndPsMainMonitoringStatus_Type(Integer32):
    """Custom type fanAndPsMainMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("notSupported", 0),
          ("ok", 1))
    )


_FanAndPsMainMonitoringStatus_Type.__name__ = "Integer32"
_FanAndPsMainMonitoringStatus_Object = MibScalar
fanAndPsMainMonitoringStatus = _FanAndPsMainMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 10),
    _FanAndPsMainMonitoringStatus_Type()
)
fanAndPsMainMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsMainMonitoringStatus.setStatus("current")
_FanAndPsPsuStatusTable_Object = MibTable
fanAndPsPsuStatusTable = _FanAndPsPsuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11)
)
if mibBuilder.loadTexts:
    fanAndPsPsuStatusTable.setStatus("current")
_FanAndPsPsuStatusEntry_Object = MibTableRow
fanAndPsPsuStatusEntry = _FanAndPsPsuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1)
)
fanAndPsPsuStatusEntry.setIndexNames(
    (0, "AT-SYSINFO-MIB", "fanAndPsPsuNumber"),
)
if mibBuilder.loadTexts:
    fanAndPsPsuStatusEntry.setStatus("current")


class _FanAndPsPsuNumber_Type(Integer32):
    """Custom type fanAndPsPsuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanAndPsPsuNumber_Type.__name__ = "Integer32"
_FanAndPsPsuNumber_Object = MibTableColumn
fanAndPsPsuNumber = _FanAndPsPsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 1),
    _FanAndPsPsuNumber_Type()
)
fanAndPsPsuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuNumber.setStatus("current")


class _FanAndPsPsuPresent_Type(Integer32):
    """Custom type fanAndPsPsuPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_FanAndPsPsuPresent_Type.__name__ = "Integer32"
_FanAndPsPsuPresent_Object = MibTableColumn
fanAndPsPsuPresent = _FanAndPsPsuPresent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 2),
    _FanAndPsPsuPresent_Type()
)
fanAndPsPsuPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuPresent.setStatus("current")


class _FanAndPsPsuType_Type(Integer32):
    """Custom type fanAndPsPsuType based on Integer32"""
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
        *(("ac", 0),
          ("dc", 1),
          ("fan", 2),
          ("notPresent", 3),
          ("notSupported", 4))
    )


_FanAndPsPsuType_Type.__name__ = "Integer32"
_FanAndPsPsuType_Object = MibTableColumn
fanAndPsPsuType = _FanAndPsPsuType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 3),
    _FanAndPsPsuType_Type()
)
fanAndPsPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuType.setStatus("current")


class _FanAndPsPsuFan_Type(Integer32):
    """Custom type fanAndPsPsuFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("notPresent", 2),
          ("notSupported", 3),
          ("ok", 0))
    )


_FanAndPsPsuFan_Type.__name__ = "Integer32"
_FanAndPsPsuFan_Object = MibTableColumn
fanAndPsPsuFan = _FanAndPsPsuFan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 4),
    _FanAndPsPsuFan_Type()
)
fanAndPsPsuFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuFan.setStatus("current")


class _FanAndPsPsuTemperature_Type(Integer32):
    """Custom type fanAndPsPsuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("high", 1),
          ("notPresent", 2),
          ("notSupported", 3))
    )


_FanAndPsPsuTemperature_Type.__name__ = "Integer32"
_FanAndPsPsuTemperature_Object = MibTableColumn
fanAndPsPsuTemperature = _FanAndPsPsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 5),
    _FanAndPsPsuTemperature_Type()
)
fanAndPsPsuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuTemperature.setStatus("current")


class _FanAndPsPsuPower_Type(Integer32):
    """Custom type fanAndPsPsuPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("good", 0),
          ("notPresent", 2),
          ("notSupported", 3))
    )


_FanAndPsPsuPower_Type.__name__ = "Integer32"
_FanAndPsPsuPower_Object = MibTableColumn
fanAndPsPsuPower = _FanAndPsPsuPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 6),
    _FanAndPsPsuPower_Type()
)
fanAndPsPsuPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsPsuPower.setStatus("current")


class _FanAndPsAccelFanStatus_Type(Integer32):
    """Custom type fanAndPsAccelFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("notSupported", 0),
          ("ok", 1))
    )


_FanAndPsAccelFanStatus_Type.__name__ = "Integer32"
_FanAndPsAccelFanStatus_Object = MibScalar
fanAndPsAccelFanStatus = _FanAndPsAccelFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 12),
    _FanAndPsAccelFanStatus_Type()
)
fanAndPsAccelFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAndPsAccelFanStatus.setStatus("current")
_RestartGroup_ObjectIdentity = ObjectIdentity
restartGroup = _RestartGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2)
)


class _Restart_Type(Integer32):
    """Custom type restart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restartCold", 2),
          ("restartNone", 0),
          ("restartWarm", 1))
    )


_Restart_Type.__name__ = "Integer32"
_Restart_Object = MibScalar
restart = _Restart_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2, 1),
    _Restart_Type()
)
restart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restart.setStatus("current")


class _RestartCause_Type(Integer32):
    """Custom type restartCause based on Integer32"""
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
        *(("hardwareReset", 1),
          ("hardwareWatchdog", 2),
          ("powerOnSelfTestfailure", 7),
          ("softwareException", 4),
          ("softwareInvalidImage", 5),
          ("softwareLicenceCheckFailure", 6),
          ("softwareRequest", 3),
          ("unknown", 0))
    )


_RestartCause_Type.__name__ = "Integer32"
_RestartCause_Object = MibScalar
restartCause = _RestartCause_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2, 2),
    _RestartCause_Type()
)
restartCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartCause.setStatus("current")


class _RestartLog_Type(DisplayStringUnsized):
    """Custom type restartLog based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_RestartLog_Type.__name__ = "DisplayStringUnsized"
_RestartLog_Object = MibScalar
restartLog = _RestartLog_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2, 3),
    _RestartLog_Type()
)
restartLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartLog.setStatus("current")
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3)
)


class _CpuUtilisationMax_Type(Integer32):
    """Custom type cpuUtilisationMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationMax_Type.__name__ = "Integer32"
_CpuUtilisationMax_Object = MibScalar
cpuUtilisationMax = _CpuUtilisationMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 1),
    _CpuUtilisationMax_Type()
)
cpuUtilisationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationMax.setStatus("current")


class _CpuUtilisationAvg_Type(Integer32):
    """Custom type cpuUtilisationAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvg_Type.__name__ = "Integer32"
_CpuUtilisationAvg_Object = MibScalar
cpuUtilisationAvg = _CpuUtilisationAvg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 2),
    _CpuUtilisationAvg_Type()
)
cpuUtilisationAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvg.setStatus("current")


class _CpuUtilisationAvgLastMinute_Type(Integer32):
    """Custom type cpuUtilisationAvgLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvgLastMinute_Type.__name__ = "Integer32"
_CpuUtilisationAvgLastMinute_Object = MibScalar
cpuUtilisationAvgLastMinute = _CpuUtilisationAvgLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 3),
    _CpuUtilisationAvgLastMinute_Type()
)
cpuUtilisationAvgLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvgLastMinute.setStatus("current")


class _CpuUtilisationAvgLast10Seconds_Type(Integer32):
    """Custom type cpuUtilisationAvgLast10Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvgLast10Seconds_Type.__name__ = "Integer32"
_CpuUtilisationAvgLast10Seconds_Object = MibScalar
cpuUtilisationAvgLast10Seconds = _CpuUtilisationAvgLast10Seconds_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 4),
    _CpuUtilisationAvgLast10Seconds_Type()
)
cpuUtilisationAvgLast10Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvgLast10Seconds.setStatus("current")


class _CpuUtilisationAvgLastSecond_Type(Integer32):
    """Custom type cpuUtilisationAvgLastSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvgLastSecond_Type.__name__ = "Integer32"
_CpuUtilisationAvgLastSecond_Object = MibScalar
cpuUtilisationAvgLastSecond = _CpuUtilisationAvgLastSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 5),
    _CpuUtilisationAvgLastSecond_Type()
)
cpuUtilisationAvgLastSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvgLastSecond.setStatus("current")


class _CpuUtilisationMaxLast5Minutes_Type(Integer32):
    """Custom type cpuUtilisationMaxLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationMaxLast5Minutes_Type.__name__ = "Integer32"
_CpuUtilisationMaxLast5Minutes_Object = MibScalar
cpuUtilisationMaxLast5Minutes = _CpuUtilisationMaxLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 6),
    _CpuUtilisationMaxLast5Minutes_Type()
)
cpuUtilisationMaxLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationMaxLast5Minutes.setStatus("current")


class _CpuUtilisationAvgLast5Minutes_Type(Integer32):
    """Custom type cpuUtilisationAvgLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationAvgLast5Minutes_Type.__name__ = "Integer32"
_CpuUtilisationAvgLast5Minutes_Object = MibScalar
cpuUtilisationAvgLast5Minutes = _CpuUtilisationAvgLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 7),
    _CpuUtilisationAvgLast5Minutes_Type()
)
cpuUtilisationAvgLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationAvgLast5Minutes.setStatus("current")
_CpuUtilisationStackTable_Object = MibTable
cpuUtilisationStackTable = _CpuUtilisationStackTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8)
)
if mibBuilder.loadTexts:
    cpuUtilisationStackTable.setStatus("current")
_CpuUtilisationStackEntry_Object = MibTableRow
cpuUtilisationStackEntry = _CpuUtilisationStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1)
)
cpuUtilisationStackEntry.setIndexNames(
    (0, "AT-SYSINFO-MIB", "cpuUtilisationStackId"),
)
if mibBuilder.loadTexts:
    cpuUtilisationStackEntry.setStatus("current")
_CpuUtilisationStackId_Type = Unsigned32
_CpuUtilisationStackId_Object = MibTableColumn
cpuUtilisationStackId = _CpuUtilisationStackId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 1),
    _CpuUtilisationStackId_Type()
)
cpuUtilisationStackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationStackId.setStatus("current")


class _CpuUtilisationStackMax_Type(Integer32):
    """Custom type cpuUtilisationStackMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationStackMax_Type.__name__ = "Integer32"
_CpuUtilisationStackMax_Object = MibTableColumn
cpuUtilisationStackMax = _CpuUtilisationStackMax_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 2),
    _CpuUtilisationStackMax_Type()
)
cpuUtilisationStackMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationStackMax.setStatus("current")


class _CpuUtilisationStackAvg_Type(Integer32):
    """Custom type cpuUtilisationStackAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationStackAvg_Type.__name__ = "Integer32"
_CpuUtilisationStackAvg_Object = MibTableColumn
cpuUtilisationStackAvg = _CpuUtilisationStackAvg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 3),
    _CpuUtilisationStackAvg_Type()
)
cpuUtilisationStackAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationStackAvg.setStatus("current")


class _CpuUtilisationStackAvgLastMinute_Type(Integer32):
    """Custom type cpuUtilisationStackAvgLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationStackAvgLastMinute_Type.__name__ = "Integer32"
_CpuUtilisationStackAvgLastMinute_Object = MibTableColumn
cpuUtilisationStackAvgLastMinute = _CpuUtilisationStackAvgLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 4),
    _CpuUtilisationStackAvgLastMinute_Type()
)
cpuUtilisationStackAvgLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationStackAvgLastMinute.setStatus("current")


class _CpuUtilisationStackAvgLast10Seconds_Type(Integer32):
    """Custom type cpuUtilisationStackAvgLast10Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationStackAvgLast10Seconds_Type.__name__ = "Integer32"
_CpuUtilisationStackAvgLast10Seconds_Object = MibTableColumn
cpuUtilisationStackAvgLast10Seconds = _CpuUtilisationStackAvgLast10Seconds_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 5),
    _CpuUtilisationStackAvgLast10Seconds_Type()
)
cpuUtilisationStackAvgLast10Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationStackAvgLast10Seconds.setStatus("current")


class _CpuUtilisationStackAvgLastSecond_Type(Integer32):
    """Custom type cpuUtilisationStackAvgLastSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationStackAvgLastSecond_Type.__name__ = "Integer32"
_CpuUtilisationStackAvgLastSecond_Object = MibTableColumn
cpuUtilisationStackAvgLastSecond = _CpuUtilisationStackAvgLastSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 6),
    _CpuUtilisationStackAvgLastSecond_Type()
)
cpuUtilisationStackAvgLastSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationStackAvgLastSecond.setStatus("current")


class _CpuUtilisationStackMaxLast5Minutes_Type(Integer32):
    """Custom type cpuUtilisationStackMaxLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationStackMaxLast5Minutes_Type.__name__ = "Integer32"
_CpuUtilisationStackMaxLast5Minutes_Object = MibTableColumn
cpuUtilisationStackMaxLast5Minutes = _CpuUtilisationStackMaxLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 7),
    _CpuUtilisationStackMaxLast5Minutes_Type()
)
cpuUtilisationStackMaxLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationStackMaxLast5Minutes.setStatus("current")


class _CpuUtilisationStackAvgLast5Minutes_Type(Integer32):
    """Custom type cpuUtilisationStackAvgLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUtilisationStackAvgLast5Minutes_Type.__name__ = "Integer32"
_CpuUtilisationStackAvgLast5Minutes_Object = MibTableColumn
cpuUtilisationStackAvgLast5Minutes = _CpuUtilisationStackAvgLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 8),
    _CpuUtilisationStackAvgLast5Minutes_Type()
)
cpuUtilisationStackAvgLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilisationStackAvgLast5Minutes.setStatus("current")
_SysTemperature_ObjectIdentity = ObjectIdentity
sysTemperature = _SysTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4)
)
_GeneralTemperature_ObjectIdentity = ObjectIdentity
generalTemperature = _GeneralTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1)
)
_GeneralTemperatureTrap_ObjectIdentity = ObjectIdentity
generalTemperatureTrap = _GeneralTemperatureTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 0)
)


class _GeneralTemperatureSupported_Type(Integer32):
    """Custom type generalTemperatureSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supported", 1))
    )


_GeneralTemperatureSupported_Type.__name__ = "Integer32"
_GeneralTemperatureSupported_Object = MibScalar
generalTemperatureSupported = _GeneralTemperatureSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 1),
    _GeneralTemperatureSupported_Type()
)
generalTemperatureSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalTemperatureSupported.setStatus("current")
_GeneralTemperatureActualTemp_Type = Integer32
_GeneralTemperatureActualTemp_Object = MibScalar
generalTemperatureActualTemp = _GeneralTemperatureActualTemp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 2),
    _GeneralTemperatureActualTemp_Type()
)
generalTemperatureActualTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalTemperatureActualTemp.setStatus("current")


class _GeneralTemperatureStatus_Type(Integer32):
    """Custom type generalTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("ok", 1))
    )


_GeneralTemperatureStatus_Type.__name__ = "Integer32"
_GeneralTemperatureStatus_Object = MibScalar
generalTemperatureStatus = _GeneralTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 3),
    _GeneralTemperatureStatus_Type()
)
generalTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalTemperatureStatus.setStatus("current")
_GeneralTemperatureThreshold_Type = Integer32
_GeneralTemperatureThreshold_Object = MibScalar
generalTemperatureThreshold = _GeneralTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 4),
    _GeneralTemperatureThreshold_Type()
)
generalTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalTemperatureThreshold.setStatus("current")
_SbTemperature_ObjectIdentity = ObjectIdentity
sbTemperature = _SbTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2)
)
_SbTemperatureTrap_ObjectIdentity = ObjectIdentity
sbTemperatureTrap = _SbTemperatureTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 0)
)
_SbTempTable_Object = MibTable
sbTempTable = _SbTempTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sbTempTable.setStatus("current")
_SbTempEntry_Object = MibTableRow
sbTempEntry = _SbTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1)
)
sbTempEntry.setIndexNames(
    (0, "AT-SYSINFO-MIB", "sbTempIndex"),
)
if mibBuilder.loadTexts:
    sbTempEntry.setStatus("current")


class _SbTempIndex_Type(Integer32):
    """Custom type sbTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_SbTempIndex_Type.__name__ = "Integer32"
_SbTempIndex_Object = MibTableColumn
sbTempIndex = _SbTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 1),
    _SbTempIndex_Type()
)
sbTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempIndex.setStatus("current")
_SbTempActualTemperature_Type = Integer32
_SbTempActualTemperature_Object = MibTableColumn
sbTempActualTemperature = _SbTempActualTemperature_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 2),
    _SbTempActualTemperature_Type()
)
sbTempActualTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempActualTemperature.setStatus("current")


class _SbTempFixedThresholdStatus_Type(Integer32):
    """Custom type sbTempFixedThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 2),
          ("normal", 1))
    )


_SbTempFixedThresholdStatus_Type.__name__ = "Integer32"
_SbTempFixedThresholdStatus_Object = MibTableColumn
sbTempFixedThresholdStatus = _SbTempFixedThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 3),
    _SbTempFixedThresholdStatus_Type()
)
sbTempFixedThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempFixedThresholdStatus.setStatus("current")


class _SbTempSettableThresholdStatus_Type(Integer32):
    """Custom type sbTempSettableThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 2),
          ("normal", 1),
          ("undefined", 3))
    )


_SbTempSettableThresholdStatus_Type.__name__ = "Integer32"
_SbTempSettableThresholdStatus_Object = MibTableColumn
sbTempSettableThresholdStatus = _SbTempSettableThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 4),
    _SbTempSettableThresholdStatus_Type()
)
sbTempSettableThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempSettableThresholdStatus.setStatus("current")


class _SbTempSettableThreshold_Type(Integer32):
    """Custom type sbTempSettableThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_SbTempSettableThreshold_Type.__name__ = "Integer32"
_SbTempSettableThreshold_Object = MibTableColumn
sbTempSettableThreshold = _SbTempSettableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 5),
    _SbTempSettableThreshold_Type()
)
sbTempSettableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbTempSettableThreshold.setStatus("current")
_SbTempFixedThreshold_Type = Integer32
_SbTempFixedThreshold_Object = MibScalar
sbTempFixedThreshold = _SbTempFixedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 2),
    _SbTempFixedThreshold_Type()
)
sbTempFixedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTempFixedThreshold.setStatus("current")
_AcceleratorTemperature_ObjectIdentity = ObjectIdentity
acceleratorTemperature = _AcceleratorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3)
)
_AcceleratorTemperatureTrap_ObjectIdentity = ObjectIdentity
acceleratorTemperatureTrap = _AcceleratorTemperatureTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 0)
)


class _AcceleratorTemperatureSupported_Type(Integer32):
    """Custom type acceleratorTemperatureSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supported", 1))
    )


_AcceleratorTemperatureSupported_Type.__name__ = "Integer32"
_AcceleratorTemperatureSupported_Object = MibScalar
acceleratorTemperatureSupported = _AcceleratorTemperatureSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 1),
    _AcceleratorTemperatureSupported_Type()
)
acceleratorTemperatureSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceleratorTemperatureSupported.setStatus("current")
_AcceleratorTemperatureActualTemp_Type = Integer32
_AcceleratorTemperatureActualTemp_Object = MibScalar
acceleratorTemperatureActualTemp = _AcceleratorTemperatureActualTemp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 2),
    _AcceleratorTemperatureActualTemp_Type()
)
acceleratorTemperatureActualTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceleratorTemperatureActualTemp.setStatus("current")


class _AcceleratorTemperatureStatus_Type(Integer32):
    """Custom type acceleratorTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("ok", 1))
    )


_AcceleratorTemperatureStatus_Type.__name__ = "Integer32"
_AcceleratorTemperatureStatus_Object = MibScalar
acceleratorTemperatureStatus = _AcceleratorTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 3),
    _AcceleratorTemperatureStatus_Type()
)
acceleratorTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceleratorTemperatureStatus.setStatus("current")
_AcceleratorTemperatureThreshold_Type = Integer32
_AcceleratorTemperatureThreshold_Object = MibScalar
acceleratorTemperatureThreshold = _AcceleratorTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 4),
    _AcceleratorTemperatureThreshold_Type()
)
acceleratorTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceleratorTemperatureThreshold.setStatus("current")
_AtContactDetails_Type = DisplayString
_AtContactDetails_Object = MibScalar
atContactDetails = _AtContactDetails_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 5),
    _AtContactDetails_Type()
)
atContactDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atContactDetails.setStatus("current")
_BbrNvs_ObjectIdentity = ObjectIdentity
bbrNvs = _BbrNvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 6)
)
_BbrNvsTrap_ObjectIdentity = ObjectIdentity
bbrNvsTrap = _BbrNvsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 6, 0)
)
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7)
)


class _FreeMemory_Type(Integer32):
    """Custom type freeMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FreeMemory_Type.__name__ = "Integer32"
_FreeMemory_Object = MibScalar
freeMemory = _FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7, 1),
    _FreeMemory_Type()
)
freeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemory.setStatus("current")
_TotalBuffers_Type = Integer32
_TotalBuffers_Object = MibScalar
totalBuffers = _TotalBuffers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7, 2),
    _TotalBuffers_Type()
)
totalBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBuffers.setStatus("current")


class _RealTimeClockStatus_Type(Integer32):
    """Custom type realTimeClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1))
    )


_RealTimeClockStatus_Type.__name__ = "Integer32"
_RealTimeClockStatus_Object = MibScalar
realTimeClockStatus = _RealTimeClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 8),
    _RealTimeClockStatus_Type()
)
realTimeClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realTimeClockStatus.setStatus("current")


class _HostId_Type(Integer32):
    """Custom type hostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HostId_Type.__name__ = "Integer32"
_HostId_Object = MibScalar
hostId = _HostId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 9),
    _HostId_Type()
)
hostId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostId.setStatus("current")
_AtPortInfo_ObjectIdentity = ObjectIdentity
atPortInfo = _AtPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14)
)
_AtPortInfoTransceiverTable_Object = MibTable
atPortInfoTransceiverTable = _AtPortInfoTransceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 1)
)
if mibBuilder.loadTexts:
    atPortInfoTransceiverTable.setStatus("current")
_AtPortInfoTransceiverEntry_Object = MibTableRow
atPortInfoTransceiverEntry = _AtPortInfoTransceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 1, 1)
)
atPortInfoTransceiverEntry.setIndexNames(
    (0, "AT-SYSINFO-MIB", "atPortInfoTransceiverifIndex"),
)
if mibBuilder.loadTexts:
    atPortInfoTransceiverEntry.setStatus("current")
_AtPortInfoTransceiverifIndex_Type = InterfaceIndex
_AtPortInfoTransceiverifIndex_Object = MibTableColumn
atPortInfoTransceiverifIndex = _AtPortInfoTransceiverifIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 1, 1, 1),
    _AtPortInfoTransceiverifIndex_Type()
)
atPortInfoTransceiverifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPortInfoTransceiverifIndex.setStatus("current")


class _AtPortInfoTransceiverType_Type(Integer32):
    """Custom type atPortInfoTransceiverType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("cx4", 34),
          ("empty", 25),
          ("inf-1-x-copper-actv", 31),
          ("inf-1-x-copper-pasv", 30),
          ("inf-1-x-lx", 32),
          ("inf-1-x-sx", 33),
          ("rj45", 1),
          ("sfp-100base-lx", 5),
          ("sfp-bx10", 3),
          ("sfp-cx", 7),
          ("sfp-fx", 4),
          ("sfp-lx", 9),
          ("sfp-oc3-ir", 12),
          ("sfp-oc3-lr", 11),
          ("sfp-oc3-mm", 13),
          ("sfp-px", 2),
          ("sfp-sx", 10),
          ("sfp-t", 6),
          ("sfp-zx-cwdm", 8),
          ("sfpp-er", 28),
          ("sfpp-lr", 27),
          ("sfpp-lrm", 29),
          ("sfpp-sr", 26),
          ("unknown", 24),
          ("xfp-er", 19),
          ("xfp-erew", 16),
          ("xfp-ew", 23),
          ("xfp-lr", 18),
          ("xfp-lrlw", 15),
          ("xfp-lrm", 20),
          ("xfp-lw", 22),
          ("xfp-sr", 17),
          ("xfp-srsw", 14),
          ("xfp-sw", 21))
    )


_AtPortInfoTransceiverType_Type.__name__ = "Integer32"
_AtPortInfoTransceiverType_Object = MibTableColumn
atPortInfoTransceiverType = _AtPortInfoTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 1, 1, 2),
    _AtPortInfoTransceiverType_Type()
)
atPortInfoTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPortInfoTransceiverType.setStatus("current")
_AtPortRenumberEvents_Type = Integer32
_AtPortRenumberEvents_Object = MibScalar
atPortRenumberEvents = _AtPortRenumberEvents_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 2),
    _AtPortRenumberEvents_Type()
)
atPortRenumberEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPortRenumberEvents.setStatus("current")

# Managed Objects groups


# Notification objects

fanAndPsRpsConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 1)
)
fanAndPsRpsConnectionTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsRpsConnectionStatus")
)
if mibBuilder.loadTexts:
    fanAndPsRpsConnectionTrap.setStatus(
        "current"
    )

fanAndPsMainPSUStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 2)
)
fanAndPsMainPSUStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsMainPSUStatus")
)
if mibBuilder.loadTexts:
    fanAndPsMainPSUStatusTrap.setStatus(
        "current"
    )

fanAndPsRedundantPSUStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 3)
)
fanAndPsRedundantPSUStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsRedundantPSUStatus")
)
if mibBuilder.loadTexts:
    fanAndPsRedundantPSUStatusTrap.setStatus(
        "current"
    )

fanAndPsMainFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 4)
)
fanAndPsMainFanStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsMainFanStatus")
)
if mibBuilder.loadTexts:
    fanAndPsMainFanStatusTrap.setStatus(
        "current"
    )

fanAndPsRedundantFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 5)
)
fanAndPsRedundantFanStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsRedundantFanStatus")
)
if mibBuilder.loadTexts:
    fanAndPsRedundantFanStatusTrap.setStatus(
        "current"
    )

fanAndPsTemperatureStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 6)
)
fanAndPsTemperatureStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsTemperatureStatus")
)
if mibBuilder.loadTexts:
    fanAndPsTemperatureStatusTrap.setStatus(
        "current"
    )

fanAndPsFanTrayPresentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 7)
)
fanAndPsFanTrayPresentTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsFanTrayPresent")
)
if mibBuilder.loadTexts:
    fanAndPsFanTrayPresentTrap.setStatus(
        "current"
    )

fanAndPsFanTrayStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 8)
)
fanAndPsFanTrayStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsFanTrayStatus")
)
if mibBuilder.loadTexts:
    fanAndPsFanTrayStatusTrap.setStatus(
        "current"
    )

fanAndPsMainMonitoringStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 9)
)
fanAndPsMainMonitoringStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsMainMonitoringStatus")
)
if mibBuilder.loadTexts:
    fanAndPsMainMonitoringStatusTrap.setStatus(
        "current"
    )

fanAndPsAccelFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 10)
)
fanAndPsAccelFanStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "fanAndPsAccelFanStatus")
)
if mibBuilder.loadTexts:
    fanAndPsAccelFanStatusTrap.setStatus(
        "current"
    )

restartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2, 11)
)
restartNotification.setObjects(
    ("AT-SYSINFO-MIB", "restartCause")
)
if mibBuilder.loadTexts:
    restartNotification.setStatus(
        "current"
    )

generalTemperatureStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 0, 1)
)
generalTemperatureStatusTrap.setObjects(
      *(("AT-SYSINFO-MIB", "generalTemperatureStatus"),
        ("AT-SYSINFO-MIB", "generalTemperatureActualTemp"),
        ("AT-SYSINFO-MIB", "generalTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    generalTemperatureStatusTrap.setStatus(
        "current"
    )

sbTempFixedThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 0, 1)
)
sbTempFixedThresholdTrap.setObjects(
      *(("AT-SYSINFO-MIB", "sbTempFixedThresholdStatus"),
        ("AT-SYSINFO-MIB", "sbTempActualTemperature"),
        ("AT-SYSINFO-MIB", "sbTempFixedThreshold"))
)
if mibBuilder.loadTexts:
    sbTempFixedThresholdTrap.setStatus(
        "current"
    )

sbTempSettableThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 0, 2)
)
sbTempSettableThresholdTrap.setObjects(
      *(("AT-SYSINFO-MIB", "sbTempSettableThresholdStatus"),
        ("AT-SYSINFO-MIB", "sbTempActualTemperature"),
        ("AT-SYSINFO-MIB", "sbTempSettableThreshold"))
)
if mibBuilder.loadTexts:
    sbTempSettableThresholdTrap.setStatus(
        "current"
    )

acceleratorTemperatureStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 0, 1)
)
acceleratorTemperatureStatusTrap.setObjects(
    ("AT-SYSINFO-MIB", "acceleratorTemperatureStatus")
)
if mibBuilder.loadTexts:
    acceleratorTemperatureStatusTrap.setStatus(
        "current"
    )

bbrNvsReinitialiseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 6, 0, 1)
)
if mibBuilder.loadTexts:
    bbrNvsReinitialiseTrap.setStatus(
        "current"
    )

lowMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7, 11)
)
lowMemoryTrap.setObjects(
      *(("AT-SYSINFO-MIB", "freeMemory"),
        ("AT-SYSINFO-MIB", "totalBuffers"))
)
if mibBuilder.loadTexts:
    lowMemoryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-SYSINFO-MIB",
    **{"sysinfo": sysinfo,
       "fanAndPs": fanAndPs,
       "fanAndPsTrap": fanAndPsTrap,
       "fanAndPsRpsConnectionTrap": fanAndPsRpsConnectionTrap,
       "fanAndPsMainPSUStatusTrap": fanAndPsMainPSUStatusTrap,
       "fanAndPsRedundantPSUStatusTrap": fanAndPsRedundantPSUStatusTrap,
       "fanAndPsMainFanStatusTrap": fanAndPsMainFanStatusTrap,
       "fanAndPsRedundantFanStatusTrap": fanAndPsRedundantFanStatusTrap,
       "fanAndPsTemperatureStatusTrap": fanAndPsTemperatureStatusTrap,
       "fanAndPsFanTrayPresentTrap": fanAndPsFanTrayPresentTrap,
       "fanAndPsFanTrayStatusTrap": fanAndPsFanTrayStatusTrap,
       "fanAndPsMainMonitoringStatusTrap": fanAndPsMainMonitoringStatusTrap,
       "fanAndPsAccelFanStatusTrap": fanAndPsAccelFanStatusTrap,
       "fanAndPsRpsConnectionStatus": fanAndPsRpsConnectionStatus,
       "fanAndPsMainPSUStatus": fanAndPsMainPSUStatus,
       "fanAndPsRedundantPSUStatus": fanAndPsRedundantPSUStatus,
       "fanAndPsRpsMonitoringStatus": fanAndPsRpsMonitoringStatus,
       "fanAndPsMainFanStatus": fanAndPsMainFanStatus,
       "fanAndPsRedundantFanStatus": fanAndPsRedundantFanStatus,
       "fanAndPsTemperatureStatus": fanAndPsTemperatureStatus,
       "fanAndPsFanTrayPresent": fanAndPsFanTrayPresent,
       "fanAndPsFanTrayStatus": fanAndPsFanTrayStatus,
       "fanAndPsMainMonitoringStatus": fanAndPsMainMonitoringStatus,
       "fanAndPsPsuStatusTable": fanAndPsPsuStatusTable,
       "fanAndPsPsuStatusEntry": fanAndPsPsuStatusEntry,
       "fanAndPsPsuNumber": fanAndPsPsuNumber,
       "fanAndPsPsuPresent": fanAndPsPsuPresent,
       "fanAndPsPsuType": fanAndPsPsuType,
       "fanAndPsPsuFan": fanAndPsPsuFan,
       "fanAndPsPsuTemperature": fanAndPsPsuTemperature,
       "fanAndPsPsuPower": fanAndPsPsuPower,
       "fanAndPsAccelFanStatus": fanAndPsAccelFanStatus,
       "restartGroup": restartGroup,
       "restart": restart,
       "restartCause": restartCause,
       "restartLog": restartLog,
       "restartNotification": restartNotification,
       "cpu": cpu,
       "cpuUtilisationMax": cpuUtilisationMax,
       "cpuUtilisationAvg": cpuUtilisationAvg,
       "cpuUtilisationAvgLastMinute": cpuUtilisationAvgLastMinute,
       "cpuUtilisationAvgLast10Seconds": cpuUtilisationAvgLast10Seconds,
       "cpuUtilisationAvgLastSecond": cpuUtilisationAvgLastSecond,
       "cpuUtilisationMaxLast5Minutes": cpuUtilisationMaxLast5Minutes,
       "cpuUtilisationAvgLast5Minutes": cpuUtilisationAvgLast5Minutes,
       "cpuUtilisationStackTable": cpuUtilisationStackTable,
       "cpuUtilisationStackEntry": cpuUtilisationStackEntry,
       "cpuUtilisationStackId": cpuUtilisationStackId,
       "cpuUtilisationStackMax": cpuUtilisationStackMax,
       "cpuUtilisationStackAvg": cpuUtilisationStackAvg,
       "cpuUtilisationStackAvgLastMinute": cpuUtilisationStackAvgLastMinute,
       "cpuUtilisationStackAvgLast10Seconds": cpuUtilisationStackAvgLast10Seconds,
       "cpuUtilisationStackAvgLastSecond": cpuUtilisationStackAvgLastSecond,
       "cpuUtilisationStackMaxLast5Minutes": cpuUtilisationStackMaxLast5Minutes,
       "cpuUtilisationStackAvgLast5Minutes": cpuUtilisationStackAvgLast5Minutes,
       "sysTemperature": sysTemperature,
       "generalTemperature": generalTemperature,
       "generalTemperatureTrap": generalTemperatureTrap,
       "generalTemperatureStatusTrap": generalTemperatureStatusTrap,
       "generalTemperatureSupported": generalTemperatureSupported,
       "generalTemperatureActualTemp": generalTemperatureActualTemp,
       "generalTemperatureStatus": generalTemperatureStatus,
       "generalTemperatureThreshold": generalTemperatureThreshold,
       "sbTemperature": sbTemperature,
       "sbTemperatureTrap": sbTemperatureTrap,
       "sbTempFixedThresholdTrap": sbTempFixedThresholdTrap,
       "sbTempSettableThresholdTrap": sbTempSettableThresholdTrap,
       "sbTempTable": sbTempTable,
       "sbTempEntry": sbTempEntry,
       "sbTempIndex": sbTempIndex,
       "sbTempActualTemperature": sbTempActualTemperature,
       "sbTempFixedThresholdStatus": sbTempFixedThresholdStatus,
       "sbTempSettableThresholdStatus": sbTempSettableThresholdStatus,
       "sbTempSettableThreshold": sbTempSettableThreshold,
       "sbTempFixedThreshold": sbTempFixedThreshold,
       "acceleratorTemperature": acceleratorTemperature,
       "acceleratorTemperatureTrap": acceleratorTemperatureTrap,
       "acceleratorTemperatureStatusTrap": acceleratorTemperatureStatusTrap,
       "acceleratorTemperatureSupported": acceleratorTemperatureSupported,
       "acceleratorTemperatureActualTemp": acceleratorTemperatureActualTemp,
       "acceleratorTemperatureStatus": acceleratorTemperatureStatus,
       "acceleratorTemperatureThreshold": acceleratorTemperatureThreshold,
       "atContactDetails": atContactDetails,
       "bbrNvs": bbrNvs,
       "bbrNvsTrap": bbrNvsTrap,
       "bbrNvsReinitialiseTrap": bbrNvsReinitialiseTrap,
       "memory": memory,
       "freeMemory": freeMemory,
       "totalBuffers": totalBuffers,
       "lowMemoryTrap": lowMemoryTrap,
       "realTimeClockStatus": realTimeClockStatus,
       "hostId": hostId,
       "atPortInfo": atPortInfo,
       "atPortInfoTransceiverTable": atPortInfoTransceiverTable,
       "atPortInfoTransceiverEntry": atPortInfoTransceiverEntry,
       "atPortInfoTransceiverifIndex": atPortInfoTransceiverifIndex,
       "atPortInfoTransceiverType": atPortInfoTransceiverType,
       "atPortRenumberEvents": atPortRenumberEvents}
)
