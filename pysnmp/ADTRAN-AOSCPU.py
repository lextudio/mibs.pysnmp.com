# SNMP MIB module (ADTRAN-AOSCPU) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOSCPU
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:17 2024
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentityShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenAOSCpuUtilMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 4)
)
adGenAOSCpuUtilMib.setRevisions(
        ("2004-10-04 00:00",
         "2009-04-30 00:00",
         "2009-08-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSCpuUtil_ObjectIdentity = ObjectIdentity
adGenAOSCpuUtil = _AdGenAOSCpuUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4)
)
_AdGenAOSResUtilThreshTraps_ObjectIdentity = ObjectIdentity
adGenAOSResUtilThreshTraps = _AdGenAOSResUtilThreshTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 0)
)
if mibBuilder.loadTexts:
    adGenAOSResUtilThreshTraps.setStatus("current")


class _AdGenAOSCurrentCpuUtil_Type(Gauge32):
    """Custom type adGenAOSCurrentCpuUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenAOSCurrentCpuUtil_Type.__name__ = "Gauge32"
_AdGenAOSCurrentCpuUtil_Object = MibScalar
adGenAOSCurrentCpuUtil = _AdGenAOSCurrentCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 1),
    _AdGenAOSCurrentCpuUtil_Type()
)
adGenAOSCurrentCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSCurrentCpuUtil.setStatus("current")


class _AdGenAOSClearUtilizationStats_Type(Integer32):
    """Custom type adGenAOSClearUtilizationStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenAOSClearUtilizationStats_Type.__name__ = "Integer32"
_AdGenAOSClearUtilizationStats_Object = MibScalar
adGenAOSClearUtilizationStats = _AdGenAOSClearUtilizationStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 2),
    _AdGenAOSClearUtilizationStats_Type()
)
adGenAOSClearUtilizationStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSClearUtilizationStats.setStatus("current")


class _AdGenAOS1MinCpuUtil_Type(Gauge32):
    """Custom type adGenAOS1MinCpuUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenAOS1MinCpuUtil_Type.__name__ = "Gauge32"
_AdGenAOS1MinCpuUtil_Object = MibScalar
adGenAOS1MinCpuUtil = _AdGenAOS1MinCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 3),
    _AdGenAOS1MinCpuUtil_Type()
)
adGenAOS1MinCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS1MinCpuUtil.setStatus("current")


class _AdGenAOS5MinCpuUtil_Type(Gauge32):
    """Custom type adGenAOS5MinCpuUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenAOS5MinCpuUtil_Type.__name__ = "Gauge32"
_AdGenAOS5MinCpuUtil_Object = MibScalar
adGenAOS5MinCpuUtil = _AdGenAOS5MinCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 4),
    _AdGenAOS5MinCpuUtil_Type()
)
adGenAOS5MinCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS5MinCpuUtil.setStatus("current")


class _AdGenAOSMaxCpuUtil_Type(Gauge32):
    """Custom type adGenAOSMaxCpuUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenAOSMaxCpuUtil_Type.__name__ = "Gauge32"
_AdGenAOSMaxCpuUtil_Object = MibScalar
adGenAOSMaxCpuUtil = _AdGenAOSMaxCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 5),
    _AdGenAOSMaxCpuUtil_Type()
)
adGenAOSMaxCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSMaxCpuUtil.setStatus("current")
_AdGenAOSMemPool_Type = Gauge32
_AdGenAOSMemPool_Object = MibScalar
adGenAOSMemPool = _AdGenAOSMemPool_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 6),
    _AdGenAOSMemPool_Type()
)
adGenAOSMemPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSMemPool.setStatus("current")
_AdGenAOSHeapSize_Type = Gauge32
_AdGenAOSHeapSize_Object = MibScalar
adGenAOSHeapSize = _AdGenAOSHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 7),
    _AdGenAOSHeapSize_Type()
)
adGenAOSHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSHeapSize.setStatus("current")
_AdGenAOSHeapFree_Type = Gauge32
_AdGenAOSHeapFree_Object = MibScalar
adGenAOSHeapFree = _AdGenAOSHeapFree_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 8),
    _AdGenAOSHeapFree_Type()
)
adGenAOSHeapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSHeapFree.setStatus("current")
_AdGenAOSProcessTable_Object = MibTable
adGenAOSProcessTable = _AdGenAOSProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9)
)
if mibBuilder.loadTexts:
    adGenAOSProcessTable.setStatus("current")
_AdGenAOSProcessEntry_Object = MibTableRow
adGenAOSProcessEntry = _AdGenAOSProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1)
)
adGenAOSProcessEntry.setIndexNames(
    (0, "ADTRAN-AOSCPU", "adGenAOSProcID"),
)
if mibBuilder.loadTexts:
    adGenAOSProcessEntry.setStatus("current")


class _AdGenAOSProcID_Type(Integer32):
    """Custom type adGenAOSProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenAOSProcID_Type.__name__ = "Integer32"
_AdGenAOSProcID_Object = MibTableColumn
adGenAOSProcID = _AdGenAOSProcID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 1),
    _AdGenAOSProcID_Type()
)
adGenAOSProcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenAOSProcID.setStatus("current")
_AdGenAOSProcName_Type = DisplayString
_AdGenAOSProcName_Object = MibTableColumn
adGenAOSProcName = _AdGenAOSProcName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 2),
    _AdGenAOSProcName_Type()
)
adGenAOSProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSProcName.setStatus("current")


class _AdGenAOSProcPriority_Type(Integer32):
    """Custom type adGenAOSProcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenAOSProcPriority_Type.__name__ = "Integer32"
_AdGenAOSProcPriority_Object = MibTableColumn
adGenAOSProcPriority = _AdGenAOSProcPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 3),
    _AdGenAOSProcPriority_Type()
)
adGenAOSProcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSProcPriority.setStatus("current")


class _AdGenAOSProcState_Type(Integer32):
    """Custom type adGenAOSProcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("running", 1),
          ("wait", 3))
    )


_AdGenAOSProcState_Type.__name__ = "Integer32"
_AdGenAOSProcState_Object = MibTableColumn
adGenAOSProcState = _AdGenAOSProcState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 4),
    _AdGenAOSProcState_Type()
)
adGenAOSProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSProcState.setStatus("current")


class _AdGenAOSProcCount_Type(Gauge32):
    """Custom type adGenAOSProcCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSProcCount_Type.__name__ = "Gauge32"
_AdGenAOSProcCount_Object = MibTableColumn
adGenAOSProcCount = _AdGenAOSProcCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 5),
    _AdGenAOSProcCount_Type()
)
adGenAOSProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSProcCount.setStatus("current")


class _AdGenAOSProcExecTime_Type(Gauge32):
    """Custom type adGenAOSProcExecTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSProcExecTime_Type.__name__ = "Gauge32"
_AdGenAOSProcExecTime_Object = MibTableColumn
adGenAOSProcExecTime = _AdGenAOSProcExecTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 6),
    _AdGenAOSProcExecTime_Type()
)
adGenAOSProcExecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSProcExecTime.setStatus("current")


class _AdGenAOSProcRunTime_Type(Gauge32):
    """Custom type adGenAOSProcRunTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSProcRunTime_Type.__name__ = "Gauge32"
_AdGenAOSProcRunTime_Object = MibTableColumn
adGenAOSProcRunTime = _AdGenAOSProcRunTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 7),
    _AdGenAOSProcRunTime_Type()
)
adGenAOSProcRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSProcRunTime.setStatus("current")


class _AdGenAOSProc1SecLd_Type(Gauge32):
    """Custom type adGenAOSProc1SecLd based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenAOSProc1SecLd_Type.__name__ = "Gauge32"
_AdGenAOSProc1SecLd_Object = MibTableColumn
adGenAOSProc1SecLd = _AdGenAOSProc1SecLd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 8),
    _AdGenAOSProc1SecLd_Type()
)
adGenAOSProc1SecLd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSProc1SecLd.setStatus("current")
_AdGenAOSResUtilThreshTable_Object = MibTable
adGenAOSResUtilThreshTable = _AdGenAOSResUtilThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10)
)
if mibBuilder.loadTexts:
    adGenAOSResUtilThreshTable.setStatus("current")
_AdGenAOSResUtilThreshEntry_Object = MibTableRow
adGenAOSResUtilThreshEntry = _AdGenAOSResUtilThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1)
)
adGenAOSResUtilThreshEntry.setIndexNames(
    (0, "ADTRAN-AOSCPU", "adGenAOSResType"),
    (0, "ADTRAN-AOSCPU", "adGenAOSResUtilThresh"),
    (0, "ADTRAN-AOSCPU", "adGenAOSResUtilTimeInterval"),
)
if mibBuilder.loadTexts:
    adGenAOSResUtilThreshEntry.setStatus("current")


class _AdGenAOSResType_Type(Integer32):
    """Custom type adGenAOSResType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 1),
          ("heap", 2))
    )


_AdGenAOSResType_Type.__name__ = "Integer32"
_AdGenAOSResType_Object = MibTableColumn
adGenAOSResType = _AdGenAOSResType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1, 1),
    _AdGenAOSResType_Type()
)
adGenAOSResType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSResType.setStatus("current")


class _AdGenAOSResUtilThresh_Type(Gauge32):
    """Custom type adGenAOSResUtilThresh based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AdGenAOSResUtilThresh_Type.__name__ = "Gauge32"
_AdGenAOSResUtilThresh_Object = MibTableColumn
adGenAOSResUtilThresh = _AdGenAOSResUtilThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1, 2),
    _AdGenAOSResUtilThresh_Type()
)
adGenAOSResUtilThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSResUtilThresh.setStatus("current")


class _AdGenAOSResUtilTimeInterval_Type(Gauge32):
    """Custom type adGenAOSResUtilTimeInterval based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_AdGenAOSResUtilTimeInterval_Type.__name__ = "Gauge32"
_AdGenAOSResUtilTimeInterval_Object = MibTableColumn
adGenAOSResUtilTimeInterval = _AdGenAOSResUtilTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1, 3),
    _AdGenAOSResUtilTimeInterval_Type()
)
adGenAOSResUtilTimeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSResUtilTimeInterval.setStatus("current")
_AdGenAOSResUtilThreshRowStatus_Type = RowStatus
_AdGenAOSResUtilThreshRowStatus_Object = MibTableColumn
adGenAOSResUtilThreshRowStatus = _AdGenAOSResUtilThreshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1, 4),
    _AdGenAOSResUtilThreshRowStatus_Type()
)
adGenAOSResUtilThreshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSResUtilThreshRowStatus.setStatus("current")
_AdGenAOSResUtilThreshTimestamp_Type = Unsigned32
_AdGenAOSResUtilThreshTimestamp_Object = MibScalar
adGenAOSResUtilThreshTimestamp = _AdGenAOSResUtilThreshTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 11),
    _AdGenAOSResUtilThreshTimestamp_Type()
)
adGenAOSResUtilThreshTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adGenAOSResUtilThreshTimestamp.setStatus("current")
_AdGenAOSCpuConformance_ObjectIdentity = ObjectIdentity
adGenAOSCpuConformance = _AdGenAOSCpuConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4)
)
_AdAOSCpuCompliances_ObjectIdentity = ObjectIdentity
adAOSCpuCompliances = _AdAOSCpuCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 1)
)
_AdAOSCpuGroups_ObjectIdentity = ObjectIdentity
adAOSCpuGroups = _AdAOSCpuGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2)
)

# Managed Objects groups

adGenAOSCpuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2, 1)
)
adGenAOSCpuGroup.setObjects(
      *(("ADTRAN-AOSCPU", "adGenAOSCurrentCpuUtil"),
        ("ADTRAN-AOSCPU", "adGenAOSClearUtilizationStats"),
        ("ADTRAN-AOSCPU", "adGenAOS1MinCpuUtil"),
        ("ADTRAN-AOSCPU", "adGenAOS5MinCpuUtil"),
        ("ADTRAN-AOSCPU", "adGenAOSMaxCpuUtil"),
        ("ADTRAN-AOSCPU", "adGenAOSMemPool"),
        ("ADTRAN-AOSCPU", "adGenAOSHeapSize"),
        ("ADTRAN-AOSCPU", "adGenAOSHeapFree"))
)
if mibBuilder.loadTexts:
    adGenAOSCpuGroup.setStatus("current")

adGenAOSProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2, 2)
)
adGenAOSProcessGroup.setObjects(
      *(("ADTRAN-AOSCPU", "adGenAOSProcName"),
        ("ADTRAN-AOSCPU", "adGenAOSProcPriority"),
        ("ADTRAN-AOSCPU", "adGenAOSProcState"),
        ("ADTRAN-AOSCPU", "adGenAOSProcCount"),
        ("ADTRAN-AOSCPU", "adGenAOSProcExecTime"),
        ("ADTRAN-AOSCPU", "adGenAOSProcRunTime"),
        ("ADTRAN-AOSCPU", "adGenAOSProc1SecLd"))
)
if mibBuilder.loadTexts:
    adGenAOSProcessGroup.setStatus("current")

adGenAOSThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2, 3)
)
adGenAOSThresholdGroup.setObjects(
      *(("ADTRAN-AOSCPU", "adGenAOSResType"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilThresh"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilTimeInterval"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshRowStatus"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshTimestamp"))
)
if mibBuilder.loadTexts:
    adGenAOSThresholdGroup.setStatus("current")


# Notification objects

adGenAOSResUtilThreshAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 0, 1)
)
adGenAOSResUtilThreshAlarm.setObjects(
      *(("ADTRAN-AOSCPU", "adGenAOSResType"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilThresh"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilTimeInterval"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshTimestamp"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adGenAOSResUtilThreshAlarm.setStatus(
        "current"
    )

adGenAOSResUtilThreshNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 0, 2)
)
adGenAOSResUtilThreshNormal.setObjects(
      *(("ADTRAN-AOSCPU", "adGenAOSResType"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilThresh"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilTimeInterval"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshTimestamp"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adGenAOSResUtilThreshNormal.setStatus(
        "current"
    )


# Notifications groups

adGenAOSThresholdTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2, 4)
)
adGenAOSThresholdTrapGroup.setObjects(
      *(("ADTRAN-AOSCPU", "adGenAOSResUtilThreshAlarm"),
        ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshNormal"))
)
if mibBuilder.loadTexts:
    adGenAOSThresholdTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adAOSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 1, 1)
)
if mibBuilder.loadTexts:
    adAOSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOSCPU",
    **{"adGenAOSCpuUtil": adGenAOSCpuUtil,
       "adGenAOSResUtilThreshTraps": adGenAOSResUtilThreshTraps,
       "adGenAOSResUtilThreshAlarm": adGenAOSResUtilThreshAlarm,
       "adGenAOSResUtilThreshNormal": adGenAOSResUtilThreshNormal,
       "adGenAOSCurrentCpuUtil": adGenAOSCurrentCpuUtil,
       "adGenAOSClearUtilizationStats": adGenAOSClearUtilizationStats,
       "adGenAOS1MinCpuUtil": adGenAOS1MinCpuUtil,
       "adGenAOS5MinCpuUtil": adGenAOS5MinCpuUtil,
       "adGenAOSMaxCpuUtil": adGenAOSMaxCpuUtil,
       "adGenAOSMemPool": adGenAOSMemPool,
       "adGenAOSHeapSize": adGenAOSHeapSize,
       "adGenAOSHeapFree": adGenAOSHeapFree,
       "adGenAOSProcessTable": adGenAOSProcessTable,
       "adGenAOSProcessEntry": adGenAOSProcessEntry,
       "adGenAOSProcID": adGenAOSProcID,
       "adGenAOSProcName": adGenAOSProcName,
       "adGenAOSProcPriority": adGenAOSProcPriority,
       "adGenAOSProcState": adGenAOSProcState,
       "adGenAOSProcCount": adGenAOSProcCount,
       "adGenAOSProcExecTime": adGenAOSProcExecTime,
       "adGenAOSProcRunTime": adGenAOSProcRunTime,
       "adGenAOSProc1SecLd": adGenAOSProc1SecLd,
       "adGenAOSResUtilThreshTable": adGenAOSResUtilThreshTable,
       "adGenAOSResUtilThreshEntry": adGenAOSResUtilThreshEntry,
       "adGenAOSResType": adGenAOSResType,
       "adGenAOSResUtilThresh": adGenAOSResUtilThresh,
       "adGenAOSResUtilTimeInterval": adGenAOSResUtilTimeInterval,
       "adGenAOSResUtilThreshRowStatus": adGenAOSResUtilThreshRowStatus,
       "adGenAOSResUtilThreshTimestamp": adGenAOSResUtilThreshTimestamp,
       "adGenAOSCpuConformance": adGenAOSCpuConformance,
       "adAOSCpuCompliances": adAOSCpuCompliances,
       "adAOSCompliance": adAOSCompliance,
       "adAOSCpuGroups": adAOSCpuGroups,
       "adGenAOSCpuGroup": adGenAOSCpuGroup,
       "adGenAOSProcessGroup": adGenAOSProcessGroup,
       "adGenAOSThresholdGroup": adGenAOSThresholdGroup,
       "adGenAOSThresholdTrapGroup": adGenAOSThresholdTrapGroup,
       "adGenAOSCpuUtilMib": adGenAOSCpuUtilMib}
)
