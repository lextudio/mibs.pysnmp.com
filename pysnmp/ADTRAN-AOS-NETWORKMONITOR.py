# SNMP MIB module (ADTRAN-AOS-NETWORKMONITOR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-NETWORKMONITOR
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:10 2024
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

(adGenAOSConformance,
 adGenAOSRouter) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSRouter")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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

adGenAOSNetMonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 2, 2)
)
adGenAOSNetMonMib.setRevisions(
        ("2010-10-27 00:00",
         "2009-01-20 00:00",
         "2008-09-30 00:00",
         "2008-08-12 00:00",
         "2008-06-25 00:00",
         "2007-08-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSNetMon_ObjectIdentity = ObjectIdentity
adGenAOSNetMon = _AdGenAOSNetMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2)
)
_AdGenAOSnmTrackTraps_ObjectIdentity = ObjectIdentity
adGenAOSnmTrackTraps = _AdGenAOSnmTrackTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 0)
)


class _AdGenAOSnmProbeTableNextIndex_Type(Integer32):
    """Custom type adGenAOSnmProbeTableNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdGenAOSnmProbeTableNextIndex_Type.__name__ = "Integer32"
_AdGenAOSnmProbeTableNextIndex_Object = MibScalar
adGenAOSnmProbeTableNextIndex = _AdGenAOSnmProbeTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 1),
    _AdGenAOSnmProbeTableNextIndex_Type()
)
adGenAOSnmProbeTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmProbeTableNextIndex.setStatus("current")
_AdGenAOSnmProbeTable_Object = MibTable
adGenAOSnmProbeTable = _AdGenAOSnmProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 2)
)
if mibBuilder.loadTexts:
    adGenAOSnmProbeTable.setStatus("current")
_AdGenAOSnmProbeEntry_Object = MibTableRow
adGenAOSnmProbeEntry = _AdGenAOSnmProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 2, 1)
)
adGenAOSnmProbeEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmProbeEntry.setStatus("current")


class _AdGenAOSnmIndex_Type(Integer32):
    """Custom type adGenAOSnmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdGenAOSnmIndex_Type.__name__ = "Integer32"
_AdGenAOSnmIndex_Object = MibTableColumn
adGenAOSnmIndex = _AdGenAOSnmIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 2, 1, 1),
    _AdGenAOSnmIndex_Type()
)
adGenAOSnmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmIndex.setStatus("current")


class _AdGenAOSnmName_Type(OctetString):
    """Custom type adGenAOSnmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmName_Type.__name__ = "OctetString"
_AdGenAOSnmName_Object = MibTableColumn
adGenAOSnmName = _AdGenAOSnmName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 2, 1, 2),
    _AdGenAOSnmName_Type()
)
adGenAOSnmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSnmName.setStatus("current")


class _AdGenAOSnmType_Type(Integer32):
    """Custom type adGenAOSnmType based on Integer32"""
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
        *(("httpRequest", 3),
          ("icmpEcho", 1),
          ("icmpTimeStamp", 4),
          ("tcpConnect", 2),
          ("twamp", 5))
    )


_AdGenAOSnmType_Type.__name__ = "Integer32"
_AdGenAOSnmType_Object = MibTableColumn
adGenAOSnmType = _AdGenAOSnmType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 2, 1, 3),
    _AdGenAOSnmType_Type()
)
adGenAOSnmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSnmType.setStatus("current")
_AdGenAOSnmRowStatus_Type = RowStatus
_AdGenAOSnmRowStatus_Object = MibTableColumn
adGenAOSnmRowStatus = _AdGenAOSnmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 2, 1, 4),
    _AdGenAOSnmRowStatus_Type()
)
adGenAOSnmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSnmRowStatus.setStatus("current")
_AdGenAOSnmConfigProbeTable_Object = MibTable
adGenAOSnmConfigProbeTable = _AdGenAOSnmConfigProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3)
)
if mibBuilder.loadTexts:
    adGenAOSnmConfigProbeTable.setStatus("current")
_AdGenAOSnmConfigProbeEntry_Object = MibTableRow
adGenAOSnmConfigProbeEntry = _AdGenAOSnmConfigProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1)
)
adGenAOSnmConfigProbeEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmConfigProbeEntry.setStatus("current")


class _AdGenAOSnmCfgName_Type(OctetString):
    """Custom type adGenAOSnmCfgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmCfgName_Type.__name__ = "OctetString"
_AdGenAOSnmCfgName_Object = MibTableColumn
adGenAOSnmCfgName = _AdGenAOSnmCfgName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 1),
    _AdGenAOSnmCfgName_Type()
)
adGenAOSnmCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmCfgName.setStatus("current")


class _AdGenAOSnmAdminStatus_Type(Integer32):
    """Custom type adGenAOSnmAdminStatus based on Integer32"""
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


_AdGenAOSnmAdminStatus_Type.__name__ = "Integer32"
_AdGenAOSnmAdminStatus_Object = MibTableColumn
adGenAOSnmAdminStatus = _AdGenAOSnmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 2),
    _AdGenAOSnmAdminStatus_Type()
)
adGenAOSnmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmAdminStatus.setStatus("current")


class _AdGenAOSnmPollPeriod_Type(Integer32):
    """Custom type adGenAOSnmPollPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenAOSnmPollPeriod_Type.__name__ = "Integer32"
_AdGenAOSnmPollPeriod_Object = MibTableColumn
adGenAOSnmPollPeriod = _AdGenAOSnmPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 3),
    _AdGenAOSnmPollPeriod_Type()
)
adGenAOSnmPollPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmPollPeriod.setStatus("current")
_AdGenAOSnmTimeoutPeriod_Type = Unsigned32
_AdGenAOSnmTimeoutPeriod_Object = MibTableColumn
adGenAOSnmTimeoutPeriod = _AdGenAOSnmTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 4),
    _AdGenAOSnmTimeoutPeriod_Type()
)
adGenAOSnmTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTimeoutPeriod.setStatus("current")


class _AdGenAOSnmToleranceMode_Type(Integer32):
    """Custom type adGenAOSnmToleranceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("consecutive", 3),
          ("none", 1),
          ("rate", 2))
    )


_AdGenAOSnmToleranceMode_Type.__name__ = "Integer32"
_AdGenAOSnmToleranceMode_Object = MibTableColumn
adGenAOSnmToleranceMode = _AdGenAOSnmToleranceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 5),
    _AdGenAOSnmToleranceMode_Type()
)
adGenAOSnmToleranceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmToleranceMode.setStatus("current")


class _AdGenAOSnmFailTolerance_Type(Integer32):
    """Custom type adGenAOSnmFailTolerance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AdGenAOSnmFailTolerance_Type.__name__ = "Integer32"
_AdGenAOSnmFailTolerance_Object = MibTableColumn
adGenAOSnmFailTolerance = _AdGenAOSnmFailTolerance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 6),
    _AdGenAOSnmFailTolerance_Type()
)
adGenAOSnmFailTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmFailTolerance.setStatus("current")


class _AdGenAOSnmPassTolerance_Type(Integer32):
    """Custom type adGenAOSnmPassTolerance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenAOSnmPassTolerance_Type.__name__ = "Integer32"
_AdGenAOSnmPassTolerance_Object = MibTableColumn
adGenAOSnmPassTolerance = _AdGenAOSnmPassTolerance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 7),
    _AdGenAOSnmPassTolerance_Type()
)
adGenAOSnmPassTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmPassTolerance.setStatus("current")


class _AdGenAOSnmToleranceTestSize_Type(Integer32):
    """Custom type adGenAOSnmToleranceTestSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenAOSnmToleranceTestSize_Type.__name__ = "Integer32"
_AdGenAOSnmToleranceTestSize_Object = MibTableColumn
adGenAOSnmToleranceTestSize = _AdGenAOSnmToleranceTestSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 8),
    _AdGenAOSnmToleranceTestSize_Type()
)
adGenAOSnmToleranceTestSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmToleranceTestSize.setStatus("current")


class _AdGenAOSnmClearCounters_Type(Integer32):
    """Custom type adGenAOSnmClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenAOSnmClearCounters_Type.__name__ = "Integer32"
_AdGenAOSnmClearCounters_Object = MibTableColumn
adGenAOSnmClearCounters = _AdGenAOSnmClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 3, 1, 9),
    _AdGenAOSnmClearCounters_Type()
)
adGenAOSnmClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmClearCounters.setStatus("current")
_AdGenAOSnmProbeStatusTable_Object = MibTable
adGenAOSnmProbeStatusTable = _AdGenAOSnmProbeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4)
)
if mibBuilder.loadTexts:
    adGenAOSnmProbeStatusTable.setStatus("current")
_AdGenAOSnmProbeStatusEntry_Object = MibTableRow
adGenAOSnmProbeStatusEntry = _AdGenAOSnmProbeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4, 1)
)
adGenAOSnmProbeStatusEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmProbeStatusEntry.setStatus("current")


class _AdGenAOSnmStatusName_Type(OctetString):
    """Custom type adGenAOSnmStatusName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmStatusName_Type.__name__ = "OctetString"
_AdGenAOSnmStatusName_Object = MibTableColumn
adGenAOSnmStatusName = _AdGenAOSnmStatusName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4, 1, 1),
    _AdGenAOSnmStatusName_Type()
)
adGenAOSnmStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmStatusName.setStatus("current")


class _AdGenAOSnmTestStatus_Type(Integer32):
    """Custom type adGenAOSnmTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("pass", 2))
    )


_AdGenAOSnmTestStatus_Type.__name__ = "Integer32"
_AdGenAOSnmTestStatus_Object = MibTableColumn
adGenAOSnmTestStatus = _AdGenAOSnmTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4, 1, 2),
    _AdGenAOSnmTestStatus_Type()
)
adGenAOSnmTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTestStatus.setStatus("current")
_AdGenAOSnmTestsRun_Type = Counter32
_AdGenAOSnmTestsRun_Object = MibTableColumn
adGenAOSnmTestsRun = _AdGenAOSnmTestsRun_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4, 1, 3),
    _AdGenAOSnmTestsRun_Type()
)
adGenAOSnmTestsRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTestsRun.setStatus("current")
_AdGenAOSnmTestsFailed_Type = Counter32
_AdGenAOSnmTestsFailed_Object = MibTableColumn
adGenAOSnmTestsFailed = _AdGenAOSnmTestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4, 1, 4),
    _AdGenAOSnmTestsFailed_Type()
)
adGenAOSnmTestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTestsFailed.setStatus("current")
_AdGenAOSnmStatsToleranceTestSize_Type = Counter32
_AdGenAOSnmStatsToleranceTestSize_Object = MibTableColumn
adGenAOSnmStatsToleranceTestSize = _AdGenAOSnmStatsToleranceTestSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4, 1, 5),
    _AdGenAOSnmStatsToleranceTestSize_Type()
)
adGenAOSnmStatsToleranceTestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmStatsToleranceTestSize.setStatus("current")
_AdGenAOSnmStatsToleranceTestValue_Type = Counter32
_AdGenAOSnmStatsToleranceTestValue_Object = MibTableColumn
adGenAOSnmStatsToleranceTestValue = _AdGenAOSnmStatsToleranceTestValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4, 1, 6),
    _AdGenAOSnmStatsToleranceTestValue_Type()
)
adGenAOSnmStatsToleranceTestValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmStatsToleranceTestValue.setStatus("current")
_AdGenAOSnmTimeSinceLastStatusChange_Type = TimeTicks
_AdGenAOSnmTimeSinceLastStatusChange_Object = MibTableColumn
adGenAOSnmTimeSinceLastStatusChange = _AdGenAOSnmTimeSinceLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 4, 1, 7),
    _AdGenAOSnmTimeSinceLastStatusChange_Type()
)
adGenAOSnmTimeSinceLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTimeSinceLastStatusChange.setStatus("current")
_AdGenAOSnmCfgTwampProbeTable_Object = MibTable
adGenAOSnmCfgTwampProbeTable = _AdGenAOSnmCfgTwampProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5)
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgTwampProbeTable.setStatus("current")
_AdGenAOSnmCfgTwampProbeEntry_Object = MibTableRow
adGenAOSnmCfgTwampProbeEntry = _AdGenAOSnmCfgTwampProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1)
)
adGenAOSnmCfgTwampProbeEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgTwampProbeEntry.setStatus("current")


class _AdGenAOSnmCfgTwName_Type(OctetString):
    """Custom type adGenAOSnmCfgTwName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmCfgTwName_Type.__name__ = "OctetString"
_AdGenAOSnmCfgTwName_Object = MibTableColumn
adGenAOSnmCfgTwName = _AdGenAOSnmCfgTwName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 1),
    _AdGenAOSnmCfgTwName_Type()
)
adGenAOSnmCfgTwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmCfgTwName.setStatus("current")
_AdGenAOSnmTwDestHostname_Type = DisplayString
_AdGenAOSnmTwDestHostname_Object = MibTableColumn
adGenAOSnmTwDestHostname = _AdGenAOSnmTwDestHostname_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 2),
    _AdGenAOSnmTwDestHostname_Type()
)
adGenAOSnmTwDestHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDestHostname.setStatus("current")


class _AdGenAOSnmTwDestPort_Type(Integer32):
    """Custom type adGenAOSnmTwDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenAOSnmTwDestPort_Type.__name__ = "Integer32"
_AdGenAOSnmTwDestPort_Object = MibTableColumn
adGenAOSnmTwDestPort = _AdGenAOSnmTwDestPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 3),
    _AdGenAOSnmTwDestPort_Type()
)
adGenAOSnmTwDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDestPort.setStatus("current")
_AdGenAOSnmTwSrcIP_Type = IpAddress
_AdGenAOSnmTwSrcIP_Object = MibTableColumn
adGenAOSnmTwSrcIP = _AdGenAOSnmTwSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 4),
    _AdGenAOSnmTwSrcIP_Type()
)
adGenAOSnmTwSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwSrcIP.setStatus("current")


class _AdGenAOSnmTwSrcPort_Type(Integer32):
    """Custom type adGenAOSnmTwSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenAOSnmTwSrcPort_Type.__name__ = "Integer32"
_AdGenAOSnmTwSrcPort_Object = MibTableColumn
adGenAOSnmTwSrcPort = _AdGenAOSnmTwSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 5),
    _AdGenAOSnmTwSrcPort_Type()
)
adGenAOSnmTwSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwSrcPort.setStatus("current")


class _AdGenAOSnmTwDscp_Type(Integer32):
    """Custom type adGenAOSnmTwDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenAOSnmTwDscp_Type.__name__ = "Integer32"
_AdGenAOSnmTwDscp_Object = MibTableColumn
adGenAOSnmTwDscp = _AdGenAOSnmTwDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 6),
    _AdGenAOSnmTwDscp_Type()
)
adGenAOSnmTwDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDscp.setStatus("current")


class _AdGenAOSnmTwPaddingLen_Type(Integer32):
    """Custom type adGenAOSnmTwPaddingLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1462),
    )


_AdGenAOSnmTwPaddingLen_Type.__name__ = "Integer32"
_AdGenAOSnmTwPaddingLen_Object = MibTableColumn
adGenAOSnmTwPaddingLen = _AdGenAOSnmTwPaddingLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 7),
    _AdGenAOSnmTwPaddingLen_Type()
)
adGenAOSnmTwPaddingLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwPaddingLen.setStatus("current")


class _AdGenAOSnmTwPaddingFormat_Type(Integer32):
    """Custom type adGenAOSnmTwPaddingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_AdGenAOSnmTwPaddingFormat_Type.__name__ = "Integer32"
_AdGenAOSnmTwPaddingFormat_Object = MibTableColumn
adGenAOSnmTwPaddingFormat = _AdGenAOSnmTwPaddingFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 8),
    _AdGenAOSnmTwPaddingFormat_Type()
)
adGenAOSnmTwPaddingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwPaddingFormat.setStatus("current")


class _AdGenAOSnmTwPaddingPattern_Type(OctetString):
    """Custom type adGenAOSnmTwPaddingPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenAOSnmTwPaddingPattern_Type.__name__ = "OctetString"
_AdGenAOSnmTwPaddingPattern_Object = MibTableColumn
adGenAOSnmTwPaddingPattern = _AdGenAOSnmTwPaddingPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 9),
    _AdGenAOSnmTwPaddingPattern_Type()
)
adGenAOSnmTwPaddingPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwPaddingPattern.setStatus("current")


class _AdGenAOSnmTwDataPadType_Type(Integer32):
    """Custom type adGenAOSnmTwDataPadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("custom", 3),
          ("random", 2),
          ("zeroes", 1))
    )


_AdGenAOSnmTwDataPadType_Type.__name__ = "Integer32"
_AdGenAOSnmTwDataPadType_Object = MibTableColumn
adGenAOSnmTwDataPadType = _AdGenAOSnmTwDataPadType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 10),
    _AdGenAOSnmTwDataPadType_Type()
)
adGenAOSnmTwDataPadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDataPadType.setStatus("current")


class _AdGenAOSnmTwPktSendCnt_Type(Integer32):
    """Custom type adGenAOSnmTwPktSendCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AdGenAOSnmTwPktSendCnt_Type.__name__ = "Integer32"
_AdGenAOSnmTwPktSendCnt_Object = MibTableColumn
adGenAOSnmTwPktSendCnt = _AdGenAOSnmTwPktSendCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 11),
    _AdGenAOSnmTwPktSendCnt_Type()
)
adGenAOSnmTwPktSendCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwPktSendCnt.setStatus("current")


class _AdGenAOSnmTwSendScheduleType_Type(Integer32):
    """Custom type adGenAOSnmTwSendScheduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("periodic", 1),
          ("poisson", 2))
    )


_AdGenAOSnmTwSendScheduleType_Type.__name__ = "Integer32"
_AdGenAOSnmTwSendScheduleType_Object = MibTableColumn
adGenAOSnmTwSendScheduleType = _AdGenAOSnmTwSendScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 12),
    _AdGenAOSnmTwSendScheduleType_Type()
)
adGenAOSnmTwSendScheduleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwSendScheduleType.setStatus("current")


class _AdGenAOSnmTwSendScheduleValue_Type(Integer32):
    """Custom type adGenAOSnmTwSendScheduleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5000),
    )


_AdGenAOSnmTwSendScheduleValue_Type.__name__ = "Integer32"
_AdGenAOSnmTwSendScheduleValue_Object = MibTableColumn
adGenAOSnmTwSendScheduleValue = _AdGenAOSnmTwSendScheduleValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 13),
    _AdGenAOSnmTwSendScheduleValue_Type()
)
adGenAOSnmTwSendScheduleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwSendScheduleValue.setStatus("current")
_AdGenAOSnmTwIpdvAbsInMinFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsInMinFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsInMinFail = _AdGenAOSnmTwIpdvAbsInMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 14),
    _AdGenAOSnmTwIpdvAbsInMinFail_Type()
)
adGenAOSnmTwIpdvAbsInMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsInMinFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsInAvgFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsInAvgFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsInAvgFail = _AdGenAOSnmTwIpdvAbsInAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 15),
    _AdGenAOSnmTwIpdvAbsInAvgFail_Type()
)
adGenAOSnmTwIpdvAbsInAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsInAvgFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsInMaxFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsInMaxFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsInMaxFail = _AdGenAOSnmTwIpdvAbsInMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 16),
    _AdGenAOSnmTwIpdvAbsInMaxFail_Type()
)
adGenAOSnmTwIpdvAbsInMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsInMaxFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsInMinPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsInMinPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsInMinPass = _AdGenAOSnmTwIpdvAbsInMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 17),
    _AdGenAOSnmTwIpdvAbsInMinPass_Type()
)
adGenAOSnmTwIpdvAbsInMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsInMinPass.setStatus("current")
_AdGenAOSnmTwIpdvAbsInAvgPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsInAvgPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsInAvgPass = _AdGenAOSnmTwIpdvAbsInAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 18),
    _AdGenAOSnmTwIpdvAbsInAvgPass_Type()
)
adGenAOSnmTwIpdvAbsInAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsInAvgPass.setStatus("current")
_AdGenAOSnmTwIpdvAbsInMaxPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsInMaxPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsInMaxPass = _AdGenAOSnmTwIpdvAbsInMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 19),
    _AdGenAOSnmTwIpdvAbsInMaxPass_Type()
)
adGenAOSnmTwIpdvAbsInMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsInMaxPass.setStatus("current")
_AdGenAOSnmTwIpdvAbsOutMinFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsOutMinFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsOutMinFail = _AdGenAOSnmTwIpdvAbsOutMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 20),
    _AdGenAOSnmTwIpdvAbsOutMinFail_Type()
)
adGenAOSnmTwIpdvAbsOutMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsOutMinFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsOutAvgFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsOutAvgFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsOutAvgFail = _AdGenAOSnmTwIpdvAbsOutAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 21),
    _AdGenAOSnmTwIpdvAbsOutAvgFail_Type()
)
adGenAOSnmTwIpdvAbsOutAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsOutAvgFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsOutMaxFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsOutMaxFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsOutMaxFail = _AdGenAOSnmTwIpdvAbsOutMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 22),
    _AdGenAOSnmTwIpdvAbsOutMaxFail_Type()
)
adGenAOSnmTwIpdvAbsOutMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsOutMaxFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsOutMinPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsOutMinPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsOutMinPass = _AdGenAOSnmTwIpdvAbsOutMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 23),
    _AdGenAOSnmTwIpdvAbsOutMinPass_Type()
)
adGenAOSnmTwIpdvAbsOutMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsOutMinPass.setStatus("current")
_AdGenAOSnmTwIpdvAbsOutAvgPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsOutAvgPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsOutAvgPass = _AdGenAOSnmTwIpdvAbsOutAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 24),
    _AdGenAOSnmTwIpdvAbsOutAvgPass_Type()
)
adGenAOSnmTwIpdvAbsOutAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsOutAvgPass.setStatus("current")
_AdGenAOSnmTwIpdvAbsOutMaxPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsOutMaxPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsOutMaxPass = _AdGenAOSnmTwIpdvAbsOutMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 25),
    _AdGenAOSnmTwIpdvAbsOutMaxPass_Type()
)
adGenAOSnmTwIpdvAbsOutMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsOutMaxPass.setStatus("current")
_AdGenAOSnmTwIpdvAbsRtMinFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsRtMinFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsRtMinFail = _AdGenAOSnmTwIpdvAbsRtMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 26),
    _AdGenAOSnmTwIpdvAbsRtMinFail_Type()
)
adGenAOSnmTwIpdvAbsRtMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsRtMinFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsRtAvgFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsRtAvgFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsRtAvgFail = _AdGenAOSnmTwIpdvAbsRtAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 27),
    _AdGenAOSnmTwIpdvAbsRtAvgFail_Type()
)
adGenAOSnmTwIpdvAbsRtAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsRtAvgFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsRtMaxFail_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsRtMaxFail_Object = MibTableColumn
adGenAOSnmTwIpdvAbsRtMaxFail = _AdGenAOSnmTwIpdvAbsRtMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 28),
    _AdGenAOSnmTwIpdvAbsRtMaxFail_Type()
)
adGenAOSnmTwIpdvAbsRtMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsRtMaxFail.setStatus("current")
_AdGenAOSnmTwIpdvAbsRtMinPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsRtMinPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsRtMinPass = _AdGenAOSnmTwIpdvAbsRtMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 29),
    _AdGenAOSnmTwIpdvAbsRtMinPass_Type()
)
adGenAOSnmTwIpdvAbsRtMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsRtMinPass.setStatus("current")
_AdGenAOSnmTwIpdvAbsRtAvgPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsRtAvgPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsRtAvgPass = _AdGenAOSnmTwIpdvAbsRtAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 30),
    _AdGenAOSnmTwIpdvAbsRtAvgPass_Type()
)
adGenAOSnmTwIpdvAbsRtAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsRtAvgPass.setStatus("current")
_AdGenAOSnmTwIpdvAbsRtMaxPass_Type = Unsigned32
_AdGenAOSnmTwIpdvAbsRtMaxPass_Object = MibTableColumn
adGenAOSnmTwIpdvAbsRtMaxPass = _AdGenAOSnmTwIpdvAbsRtMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 31),
    _AdGenAOSnmTwIpdvAbsRtMaxPass_Type()
)
adGenAOSnmTwIpdvAbsRtMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpdvAbsRtMaxPass.setStatus("current")
_AdGenAOSnmTwDelayInMinFail_Type = Integer32
_AdGenAOSnmTwDelayInMinFail_Object = MibTableColumn
adGenAOSnmTwDelayInMinFail = _AdGenAOSnmTwDelayInMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 32),
    _AdGenAOSnmTwDelayInMinFail_Type()
)
adGenAOSnmTwDelayInMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInMinFail.setStatus("current")
_AdGenAOSnmTwDelayInAvgFail_Type = Integer32
_AdGenAOSnmTwDelayInAvgFail_Object = MibTableColumn
adGenAOSnmTwDelayInAvgFail = _AdGenAOSnmTwDelayInAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 33),
    _AdGenAOSnmTwDelayInAvgFail_Type()
)
adGenAOSnmTwDelayInAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInAvgFail.setStatus("current")
_AdGenAOSnmTwDelayInMaxFail_Type = Integer32
_AdGenAOSnmTwDelayInMaxFail_Object = MibTableColumn
adGenAOSnmTwDelayInMaxFail = _AdGenAOSnmTwDelayInMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 34),
    _AdGenAOSnmTwDelayInMaxFail_Type()
)
adGenAOSnmTwDelayInMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInMaxFail.setStatus("current")
_AdGenAOSnmTwDelayInMinPass_Type = Integer32
_AdGenAOSnmTwDelayInMinPass_Object = MibTableColumn
adGenAOSnmTwDelayInMinPass = _AdGenAOSnmTwDelayInMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 35),
    _AdGenAOSnmTwDelayInMinPass_Type()
)
adGenAOSnmTwDelayInMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInMinPass.setStatus("current")
_AdGenAOSnmTwDelayInAvgPass_Type = Integer32
_AdGenAOSnmTwDelayInAvgPass_Object = MibTableColumn
adGenAOSnmTwDelayInAvgPass = _AdGenAOSnmTwDelayInAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 36),
    _AdGenAOSnmTwDelayInAvgPass_Type()
)
adGenAOSnmTwDelayInAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInAvgPass.setStatus("current")
_AdGenAOSnmTwDelayInMaxPass_Type = Integer32
_AdGenAOSnmTwDelayInMaxPass_Object = MibTableColumn
adGenAOSnmTwDelayInMaxPass = _AdGenAOSnmTwDelayInMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 37),
    _AdGenAOSnmTwDelayInMaxPass_Type()
)
adGenAOSnmTwDelayInMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInMaxPass.setStatus("current")
_AdGenAOSnmTwDelayOutMinFail_Type = Integer32
_AdGenAOSnmTwDelayOutMinFail_Object = MibTableColumn
adGenAOSnmTwDelayOutMinFail = _AdGenAOSnmTwDelayOutMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 38),
    _AdGenAOSnmTwDelayOutMinFail_Type()
)
adGenAOSnmTwDelayOutMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutMinFail.setStatus("current")
_AdGenAOSnmTwDelayOutAvgFail_Type = Integer32
_AdGenAOSnmTwDelayOutAvgFail_Object = MibTableColumn
adGenAOSnmTwDelayOutAvgFail = _AdGenAOSnmTwDelayOutAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 39),
    _AdGenAOSnmTwDelayOutAvgFail_Type()
)
adGenAOSnmTwDelayOutAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutAvgFail.setStatus("current")
_AdGenAOSnmTwDelayOutMaxFail_Type = Integer32
_AdGenAOSnmTwDelayOutMaxFail_Object = MibTableColumn
adGenAOSnmTwDelayOutMaxFail = _AdGenAOSnmTwDelayOutMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 40),
    _AdGenAOSnmTwDelayOutMaxFail_Type()
)
adGenAOSnmTwDelayOutMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutMaxFail.setStatus("current")
_AdGenAOSnmTwDelayOutMinPass_Type = Integer32
_AdGenAOSnmTwDelayOutMinPass_Object = MibTableColumn
adGenAOSnmTwDelayOutMinPass = _AdGenAOSnmTwDelayOutMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 41),
    _AdGenAOSnmTwDelayOutMinPass_Type()
)
adGenAOSnmTwDelayOutMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutMinPass.setStatus("current")
_AdGenAOSnmTwDelayOutAvgPass_Type = Integer32
_AdGenAOSnmTwDelayOutAvgPass_Object = MibTableColumn
adGenAOSnmTwDelayOutAvgPass = _AdGenAOSnmTwDelayOutAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 42),
    _AdGenAOSnmTwDelayOutAvgPass_Type()
)
adGenAOSnmTwDelayOutAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutAvgPass.setStatus("current")
_AdGenAOSnmTwDelayOutMaxPass_Type = Integer32
_AdGenAOSnmTwDelayOutMaxPass_Object = MibTableColumn
adGenAOSnmTwDelayOutMaxPass = _AdGenAOSnmTwDelayOutMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 43),
    _AdGenAOSnmTwDelayOutMaxPass_Type()
)
adGenAOSnmTwDelayOutMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutMaxPass.setStatus("current")
_AdGenAOSnmTwDelayRtMinFail_Type = Integer32
_AdGenAOSnmTwDelayRtMinFail_Object = MibTableColumn
adGenAOSnmTwDelayRtMinFail = _AdGenAOSnmTwDelayRtMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 44),
    _AdGenAOSnmTwDelayRtMinFail_Type()
)
adGenAOSnmTwDelayRtMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtMinFail.setStatus("current")
_AdGenAOSnmTwDelayRtAvgFail_Type = Integer32
_AdGenAOSnmTwDelayRtAvgFail_Object = MibTableColumn
adGenAOSnmTwDelayRtAvgFail = _AdGenAOSnmTwDelayRtAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 45),
    _AdGenAOSnmTwDelayRtAvgFail_Type()
)
adGenAOSnmTwDelayRtAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtAvgFail.setStatus("current")
_AdGenAOSnmTwDelayRtMaxFail_Type = Integer32
_AdGenAOSnmTwDelayRtMaxFail_Object = MibTableColumn
adGenAOSnmTwDelayRtMaxFail = _AdGenAOSnmTwDelayRtMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 46),
    _AdGenAOSnmTwDelayRtMaxFail_Type()
)
adGenAOSnmTwDelayRtMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtMaxFail.setStatus("current")
_AdGenAOSnmTwDelayRtMinPass_Type = Integer32
_AdGenAOSnmTwDelayRtMinPass_Object = MibTableColumn
adGenAOSnmTwDelayRtMinPass = _AdGenAOSnmTwDelayRtMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 47),
    _AdGenAOSnmTwDelayRtMinPass_Type()
)
adGenAOSnmTwDelayRtMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtMinPass.setStatus("current")
_AdGenAOSnmTwDelayRtAvgPass_Type = Integer32
_AdGenAOSnmTwDelayRtAvgPass_Object = MibTableColumn
adGenAOSnmTwDelayRtAvgPass = _AdGenAOSnmTwDelayRtAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 48),
    _AdGenAOSnmTwDelayRtAvgPass_Type()
)
adGenAOSnmTwDelayRtAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtAvgPass.setStatus("current")
_AdGenAOSnmTwDelayRtMaxPass_Type = Integer32
_AdGenAOSnmTwDelayRtMaxPass_Object = MibTableColumn
adGenAOSnmTwDelayRtMaxPass = _AdGenAOSnmTwDelayRtMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 49),
    _AdGenAOSnmTwDelayRtMaxPass_Type()
)
adGenAOSnmTwDelayRtMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtMaxPass.setStatus("current")


class _AdGenAOSnmTwPktRtLossFail_Type(Integer32):
    """Custom type adGenAOSnmTwPktRtLossFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdGenAOSnmTwPktRtLossFail_Type.__name__ = "Integer32"
_AdGenAOSnmTwPktRtLossFail_Object = MibTableColumn
adGenAOSnmTwPktRtLossFail = _AdGenAOSnmTwPktRtLossFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 50),
    _AdGenAOSnmTwPktRtLossFail_Type()
)
adGenAOSnmTwPktRtLossFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwPktRtLossFail.setStatus("current")


class _AdGenAOSnmTwPktRtLossPass_Type(Integer32):
    """Custom type adGenAOSnmTwPktRtLossPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdGenAOSnmTwPktRtLossPass_Type.__name__ = "Integer32"
_AdGenAOSnmTwPktRtLossPass_Object = MibTableColumn
adGenAOSnmTwPktRtLossPass = _AdGenAOSnmTwPktRtLossPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 51),
    _AdGenAOSnmTwPktRtLossPass_Type()
)
adGenAOSnmTwPktRtLossPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwPktRtLossPass.setStatus("current")


class _AdGenAOSnmTwHistoryDepth_Type(Integer32):
    """Custom type adGenAOSnmTwHistoryDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AdGenAOSnmTwHistoryDepth_Type.__name__ = "Integer32"
_AdGenAOSnmTwHistoryDepth_Object = MibTableColumn
adGenAOSnmTwHistoryDepth = _AdGenAOSnmTwHistoryDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 5, 1, 52),
    _AdGenAOSnmTwHistoryDepth_Type()
)
adGenAOSnmTwHistoryDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTwHistoryDepth.setStatus("current")
_AdGenAOSnmTwampHistoryTable_Object = MibTable
adGenAOSnmTwampHistoryTable = _AdGenAOSnmTwampHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6)
)
if mibBuilder.loadTexts:
    adGenAOSnmTwampHistoryTable.setStatus("current")
_AdGenAOSnmTwampHistoryEntry_Object = MibTableRow
adGenAOSnmTwampHistoryEntry = _AdGenAOSnmTwampHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1)
)
adGenAOSnmTwampHistoryEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwSeqNum"),
)
if mibBuilder.loadTexts:
    adGenAOSnmTwampHistoryEntry.setStatus("current")


class _AdGenAOSnmTwSeqNum_Type(Integer32):
    """Custom type adGenAOSnmTwSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AdGenAOSnmTwSeqNum_Type.__name__ = "Integer32"
_AdGenAOSnmTwSeqNum_Object = MibTableColumn
adGenAOSnmTwSeqNum = _AdGenAOSnmTwSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 1),
    _AdGenAOSnmTwSeqNum_Type()
)
adGenAOSnmTwSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwSeqNum.setStatus("current")


class _AdGenAOSnmTwHistoryName_Type(OctetString):
    """Custom type adGenAOSnmTwHistoryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmTwHistoryName_Type.__name__ = "OctetString"
_AdGenAOSnmTwHistoryName_Object = MibTableColumn
adGenAOSnmTwHistoryName = _AdGenAOSnmTwHistoryName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 2),
    _AdGenAOSnmTwHistoryName_Type()
)
adGenAOSnmTwHistoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwHistoryName.setStatus("current")
_AdGenAOSnmTwStartTime_Type = DisplayString
_AdGenAOSnmTwStartTime_Object = MibTableColumn
adGenAOSnmTwStartTime = _AdGenAOSnmTwStartTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 3),
    _AdGenAOSnmTwStartTime_Type()
)
adGenAOSnmTwStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwStartTime.setStatus("current")
_AdGenAOSnmTwEndTime_Type = DisplayString
_AdGenAOSnmTwEndTime_Object = MibTableColumn
adGenAOSnmTwEndTime = _AdGenAOSnmTwEndTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 4),
    _AdGenAOSnmTwEndTime_Type()
)
adGenAOSnmTwEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwEndTime.setStatus("current")
_AdGenAOSnmTwLocalSyncState_Type = TruthValue
_AdGenAOSnmTwLocalSyncState_Object = MibTableColumn
adGenAOSnmTwLocalSyncState = _AdGenAOSnmTwLocalSyncState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 5),
    _AdGenAOSnmTwLocalSyncState_Type()
)
adGenAOSnmTwLocalSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwLocalSyncState.setStatus("current")
_AdGenAOSnmTwLocalClkErr_Type = Counter64
_AdGenAOSnmTwLocalClkErr_Object = MibTableColumn
adGenAOSnmTwLocalClkErr = _AdGenAOSnmTwLocalClkErr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 6),
    _AdGenAOSnmTwLocalClkErr_Type()
)
adGenAOSnmTwLocalClkErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwLocalClkErr.setStatus("current")
_AdGenAOSnmTwRemoteSyncState_Type = TruthValue
_AdGenAOSnmTwRemoteSyncState_Object = MibTableColumn
adGenAOSnmTwRemoteSyncState = _AdGenAOSnmTwRemoteSyncState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 7),
    _AdGenAOSnmTwRemoteSyncState_Type()
)
adGenAOSnmTwRemoteSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwRemoteSyncState.setStatus("current")
_AdGenAOSnmTwRemoteClkErr_Type = Counter64
_AdGenAOSnmTwRemoteClkErr_Object = MibTableColumn
adGenAOSnmTwRemoteClkErr = _AdGenAOSnmTwRemoteClkErr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 8),
    _AdGenAOSnmTwRemoteClkErr_Type()
)
adGenAOSnmTwRemoteClkErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwRemoteClkErr.setStatus("current")
_AdGenAOSnmTwDelayInMin_Type = Integer32
_AdGenAOSnmTwDelayInMin_Object = MibTableColumn
adGenAOSnmTwDelayInMin = _AdGenAOSnmTwDelayInMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 9),
    _AdGenAOSnmTwDelayInMin_Type()
)
adGenAOSnmTwDelayInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInMin.setStatus("current")
_AdGenAOSnmTwDelayInMax_Type = Integer32
_AdGenAOSnmTwDelayInMax_Object = MibTableColumn
adGenAOSnmTwDelayInMax = _AdGenAOSnmTwDelayInMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 10),
    _AdGenAOSnmTwDelayInMax_Type()
)
adGenAOSnmTwDelayInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInMax.setStatus("current")
_AdGenAOSnmTwDelayOutMin_Type = Integer32
_AdGenAOSnmTwDelayOutMin_Object = MibTableColumn
adGenAOSnmTwDelayOutMin = _AdGenAOSnmTwDelayOutMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 11),
    _AdGenAOSnmTwDelayOutMin_Type()
)
adGenAOSnmTwDelayOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutMin.setStatus("current")
_AdGenAOSnmTwDelayOutMax_Type = Integer32
_AdGenAOSnmTwDelayOutMax_Object = MibTableColumn
adGenAOSnmTwDelayOutMax = _AdGenAOSnmTwDelayOutMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 12),
    _AdGenAOSnmTwDelayOutMax_Type()
)
adGenAOSnmTwDelayOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutMax.setStatus("current")
_AdGenAOSnmTwDelayRtMin_Type = Integer32
_AdGenAOSnmTwDelayRtMin_Object = MibTableColumn
adGenAOSnmTwDelayRtMin = _AdGenAOSnmTwDelayRtMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 13),
    _AdGenAOSnmTwDelayRtMin_Type()
)
adGenAOSnmTwDelayRtMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtMin.setStatus("current")
_AdGenAOSnmTwDelayRtMax_Type = Integer32
_AdGenAOSnmTwDelayRtMax_Object = MibTableColumn
adGenAOSnmTwDelayRtMax = _AdGenAOSnmTwDelayRtMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 14),
    _AdGenAOSnmTwDelayRtMax_Type()
)
adGenAOSnmTwDelayRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtMax.setStatus("current")
_AdGenAOSnmTwLossRoundTrip_Type = Counter32
_AdGenAOSnmTwLossRoundTrip_Object = MibTableColumn
adGenAOSnmTwLossRoundTrip = _AdGenAOSnmTwLossRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 15),
    _AdGenAOSnmTwLossRoundTrip_Type()
)
adGenAOSnmTwLossRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwLossRoundTrip.setStatus("current")
_AdGenAOSnmTwDelayOutSum_Type = Integer32
_AdGenAOSnmTwDelayOutSum_Object = MibTableColumn
adGenAOSnmTwDelayOutSum = _AdGenAOSnmTwDelayOutSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 16),
    _AdGenAOSnmTwDelayOutSum_Type()
)
adGenAOSnmTwDelayOutSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutSum.setStatus("current")
_AdGenAOSnmTwDelayOutSum2_Type = Counter64
_AdGenAOSnmTwDelayOutSum2_Object = MibTableColumn
adGenAOSnmTwDelayOutSum2 = _AdGenAOSnmTwDelayOutSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 17),
    _AdGenAOSnmTwDelayOutSum2_Type()
)
adGenAOSnmTwDelayOutSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutSum2.setStatus("current")
_AdGenAOSnmTwDelayOutNum_Type = Counter32
_AdGenAOSnmTwDelayOutNum_Object = MibTableColumn
adGenAOSnmTwDelayOutNum = _AdGenAOSnmTwDelayOutNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 18),
    _AdGenAOSnmTwDelayOutNum_Type()
)
adGenAOSnmTwDelayOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayOutNum.setStatus("current")
_AdGenAOSnmTwDelayInSum_Type = Integer32
_AdGenAOSnmTwDelayInSum_Object = MibTableColumn
adGenAOSnmTwDelayInSum = _AdGenAOSnmTwDelayInSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 19),
    _AdGenAOSnmTwDelayInSum_Type()
)
adGenAOSnmTwDelayInSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInSum.setStatus("current")
_AdGenAOSnmTwDelayInSum2_Type = Counter64
_AdGenAOSnmTwDelayInSum2_Object = MibTableColumn
adGenAOSnmTwDelayInSum2 = _AdGenAOSnmTwDelayInSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 20),
    _AdGenAOSnmTwDelayInSum2_Type()
)
adGenAOSnmTwDelayInSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInSum2.setStatus("current")
_AdGenAOSnmTwDelayInNum_Type = Counter32
_AdGenAOSnmTwDelayInNum_Object = MibTableColumn
adGenAOSnmTwDelayInNum = _AdGenAOSnmTwDelayInNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 21),
    _AdGenAOSnmTwDelayInNum_Type()
)
adGenAOSnmTwDelayInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayInNum.setStatus("current")
_AdGenAOSnmTwDelayRtSum_Type = Integer32
_AdGenAOSnmTwDelayRtSum_Object = MibTableColumn
adGenAOSnmTwDelayRtSum = _AdGenAOSnmTwDelayRtSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 22),
    _AdGenAOSnmTwDelayRtSum_Type()
)
adGenAOSnmTwDelayRtSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtSum.setStatus("current")
_AdGenAOSnmTwDelayRtSum2_Type = Counter64
_AdGenAOSnmTwDelayRtSum2_Object = MibTableColumn
adGenAOSnmTwDelayRtSum2 = _AdGenAOSnmTwDelayRtSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 23),
    _AdGenAOSnmTwDelayRtSum2_Type()
)
adGenAOSnmTwDelayRtSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtSum2.setStatus("current")
_AdGenAOSnmTwDelayRtNum_Type = Counter32
_AdGenAOSnmTwDelayRtNum_Object = MibTableColumn
adGenAOSnmTwDelayRtNum = _AdGenAOSnmTwDelayRtNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 24),
    _AdGenAOSnmTwDelayRtNum_Type()
)
adGenAOSnmTwDelayRtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwDelayRtNum.setStatus("current")
_AdGenAOSnmTwIpvPosInMin_Type = Counter32
_AdGenAOSnmTwIpvPosInMin_Object = MibTableColumn
adGenAOSnmTwIpvPosInMin = _AdGenAOSnmTwIpvPosInMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 25),
    _AdGenAOSnmTwIpvPosInMin_Type()
)
adGenAOSnmTwIpvPosInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosInMin.setStatus("current")
_AdGenAOSnmTwIpvPosInMax_Type = Counter32
_AdGenAOSnmTwIpvPosInMax_Object = MibTableColumn
adGenAOSnmTwIpvPosInMax = _AdGenAOSnmTwIpvPosInMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 26),
    _AdGenAOSnmTwIpvPosInMax_Type()
)
adGenAOSnmTwIpvPosInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosInMax.setStatus("current")
_AdGenAOSnmTwIpvPosInSum_Type = Counter32
_AdGenAOSnmTwIpvPosInSum_Object = MibTableColumn
adGenAOSnmTwIpvPosInSum = _AdGenAOSnmTwIpvPosInSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 27),
    _AdGenAOSnmTwIpvPosInSum_Type()
)
adGenAOSnmTwIpvPosInSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosInSum.setStatus("current")
_AdGenAOSnmTwIpvPosInSum2_Type = Counter64
_AdGenAOSnmTwIpvPosInSum2_Object = MibTableColumn
adGenAOSnmTwIpvPosInSum2 = _AdGenAOSnmTwIpvPosInSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 28),
    _AdGenAOSnmTwIpvPosInSum2_Type()
)
adGenAOSnmTwIpvPosInSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosInSum2.setStatus("current")
_AdGenAOSnmTwIpvPosInNum_Type = Counter32
_AdGenAOSnmTwIpvPosInNum_Object = MibTableColumn
adGenAOSnmTwIpvPosInNum = _AdGenAOSnmTwIpvPosInNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 29),
    _AdGenAOSnmTwIpvPosInNum_Type()
)
adGenAOSnmTwIpvPosInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosInNum.setStatus("current")
_AdGenAOSnmTwIpvPosOutMin_Type = Counter32
_AdGenAOSnmTwIpvPosOutMin_Object = MibTableColumn
adGenAOSnmTwIpvPosOutMin = _AdGenAOSnmTwIpvPosOutMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 30),
    _AdGenAOSnmTwIpvPosOutMin_Type()
)
adGenAOSnmTwIpvPosOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosOutMin.setStatus("current")
_AdGenAOSnmTwIpvPosOutMax_Type = Counter32
_AdGenAOSnmTwIpvPosOutMax_Object = MibTableColumn
adGenAOSnmTwIpvPosOutMax = _AdGenAOSnmTwIpvPosOutMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 31),
    _AdGenAOSnmTwIpvPosOutMax_Type()
)
adGenAOSnmTwIpvPosOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosOutMax.setStatus("current")
_AdGenAOSnmTwIpvPosOutSum_Type = Counter32
_AdGenAOSnmTwIpvPosOutSum_Object = MibTableColumn
adGenAOSnmTwIpvPosOutSum = _AdGenAOSnmTwIpvPosOutSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 32),
    _AdGenAOSnmTwIpvPosOutSum_Type()
)
adGenAOSnmTwIpvPosOutSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosOutSum.setStatus("current")
_AdGenAOSnmTwIpvPosOutSum2_Type = Counter64
_AdGenAOSnmTwIpvPosOutSum2_Object = MibTableColumn
adGenAOSnmTwIpvPosOutSum2 = _AdGenAOSnmTwIpvPosOutSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 33),
    _AdGenAOSnmTwIpvPosOutSum2_Type()
)
adGenAOSnmTwIpvPosOutSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosOutSum2.setStatus("current")
_AdGenAOSnmTwIpvPosOutNum_Type = Counter32
_AdGenAOSnmTwIpvPosOutNum_Object = MibTableColumn
adGenAOSnmTwIpvPosOutNum = _AdGenAOSnmTwIpvPosOutNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 34),
    _AdGenAOSnmTwIpvPosOutNum_Type()
)
adGenAOSnmTwIpvPosOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosOutNum.setStatus("current")
_AdGenAOSnmTwIpvPosRtMin_Type = Counter32
_AdGenAOSnmTwIpvPosRtMin_Object = MibTableColumn
adGenAOSnmTwIpvPosRtMin = _AdGenAOSnmTwIpvPosRtMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 35),
    _AdGenAOSnmTwIpvPosRtMin_Type()
)
adGenAOSnmTwIpvPosRtMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosRtMin.setStatus("current")
_AdGenAOSnmTwIpvPosRtMax_Type = Counter32
_AdGenAOSnmTwIpvPosRtMax_Object = MibTableColumn
adGenAOSnmTwIpvPosRtMax = _AdGenAOSnmTwIpvPosRtMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 36),
    _AdGenAOSnmTwIpvPosRtMax_Type()
)
adGenAOSnmTwIpvPosRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosRtMax.setStatus("current")
_AdGenAOSnmTwIpvPosRtSum_Type = Counter32
_AdGenAOSnmTwIpvPosRtSum_Object = MibTableColumn
adGenAOSnmTwIpvPosRtSum = _AdGenAOSnmTwIpvPosRtSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 37),
    _AdGenAOSnmTwIpvPosRtSum_Type()
)
adGenAOSnmTwIpvPosRtSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosRtSum.setStatus("current")
_AdGenAOSnmTwIpvPosRtSum2_Type = Counter64
_AdGenAOSnmTwIpvPosRtSum2_Object = MibTableColumn
adGenAOSnmTwIpvPosRtSum2 = _AdGenAOSnmTwIpvPosRtSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 38),
    _AdGenAOSnmTwIpvPosRtSum2_Type()
)
adGenAOSnmTwIpvPosRtSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosRtSum2.setStatus("current")
_AdGenAOSnmTwIpvPosRtNum_Type = Counter32
_AdGenAOSnmTwIpvPosRtNum_Object = MibTableColumn
adGenAOSnmTwIpvPosRtNum = _AdGenAOSnmTwIpvPosRtNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 39),
    _AdGenAOSnmTwIpvPosRtNum_Type()
)
adGenAOSnmTwIpvPosRtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvPosRtNum.setStatus("current")
_AdGenAOSnmTwIpvNegInMin_Type = Counter32
_AdGenAOSnmTwIpvNegInMin_Object = MibTableColumn
adGenAOSnmTwIpvNegInMin = _AdGenAOSnmTwIpvNegInMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 40),
    _AdGenAOSnmTwIpvNegInMin_Type()
)
adGenAOSnmTwIpvNegInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegInMin.setStatus("current")
_AdGenAOSnmTwIpvNegInMax_Type = Counter32
_AdGenAOSnmTwIpvNegInMax_Object = MibTableColumn
adGenAOSnmTwIpvNegInMax = _AdGenAOSnmTwIpvNegInMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 41),
    _AdGenAOSnmTwIpvNegInMax_Type()
)
adGenAOSnmTwIpvNegInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegInMax.setStatus("current")
_AdGenAOSnmTwIpvNegInSum_Type = Counter32
_AdGenAOSnmTwIpvNegInSum_Object = MibTableColumn
adGenAOSnmTwIpvNegInSum = _AdGenAOSnmTwIpvNegInSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 42),
    _AdGenAOSnmTwIpvNegInSum_Type()
)
adGenAOSnmTwIpvNegInSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegInSum.setStatus("current")
_AdGenAOSnmTwIpvNegInSum2_Type = Counter64
_AdGenAOSnmTwIpvNegInSum2_Object = MibTableColumn
adGenAOSnmTwIpvNegInSum2 = _AdGenAOSnmTwIpvNegInSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 43),
    _AdGenAOSnmTwIpvNegInSum2_Type()
)
adGenAOSnmTwIpvNegInSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegInSum2.setStatus("current")
_AdGenAOSnmTwIpvNegInNum_Type = Counter32
_AdGenAOSnmTwIpvNegInNum_Object = MibTableColumn
adGenAOSnmTwIpvNegInNum = _AdGenAOSnmTwIpvNegInNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 44),
    _AdGenAOSnmTwIpvNegInNum_Type()
)
adGenAOSnmTwIpvNegInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegInNum.setStatus("current")
_AdGenAOSnmTwIpvNegOutMin_Type = Counter32
_AdGenAOSnmTwIpvNegOutMin_Object = MibTableColumn
adGenAOSnmTwIpvNegOutMin = _AdGenAOSnmTwIpvNegOutMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 45),
    _AdGenAOSnmTwIpvNegOutMin_Type()
)
adGenAOSnmTwIpvNegOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegOutMin.setStatus("current")
_AdGenAOSnmTwIpvNegOutMax_Type = Counter32
_AdGenAOSnmTwIpvNegOutMax_Object = MibTableColumn
adGenAOSnmTwIpvNegOutMax = _AdGenAOSnmTwIpvNegOutMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 46),
    _AdGenAOSnmTwIpvNegOutMax_Type()
)
adGenAOSnmTwIpvNegOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegOutMax.setStatus("current")
_AdGenAOSnmTwIpvNegOutSum_Type = Counter32
_AdGenAOSnmTwIpvNegOutSum_Object = MibTableColumn
adGenAOSnmTwIpvNegOutSum = _AdGenAOSnmTwIpvNegOutSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 47),
    _AdGenAOSnmTwIpvNegOutSum_Type()
)
adGenAOSnmTwIpvNegOutSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegOutSum.setStatus("current")
_AdGenAOSnmTwIpvNegOutSum2_Type = Counter64
_AdGenAOSnmTwIpvNegOutSum2_Object = MibTableColumn
adGenAOSnmTwIpvNegOutSum2 = _AdGenAOSnmTwIpvNegOutSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 48),
    _AdGenAOSnmTwIpvNegOutSum2_Type()
)
adGenAOSnmTwIpvNegOutSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegOutSum2.setStatus("current")
_AdGenAOSnmTwIpvNegOutNum_Type = Counter32
_AdGenAOSnmTwIpvNegOutNum_Object = MibTableColumn
adGenAOSnmTwIpvNegOutNum = _AdGenAOSnmTwIpvNegOutNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 49),
    _AdGenAOSnmTwIpvNegOutNum_Type()
)
adGenAOSnmTwIpvNegOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegOutNum.setStatus("current")
_AdGenAOSnmTwIpvNegRtMin_Type = Counter32
_AdGenAOSnmTwIpvNegRtMin_Object = MibTableColumn
adGenAOSnmTwIpvNegRtMin = _AdGenAOSnmTwIpvNegRtMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 50),
    _AdGenAOSnmTwIpvNegRtMin_Type()
)
adGenAOSnmTwIpvNegRtMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegRtMin.setStatus("current")
_AdGenAOSnmTwIpvNegRtMax_Type = Counter32
_AdGenAOSnmTwIpvNegRtMax_Object = MibTableColumn
adGenAOSnmTwIpvNegRtMax = _AdGenAOSnmTwIpvNegRtMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 51),
    _AdGenAOSnmTwIpvNegRtMax_Type()
)
adGenAOSnmTwIpvNegRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegRtMax.setStatus("current")
_AdGenAOSnmTwIpvNegRtSum_Type = Counter32
_AdGenAOSnmTwIpvNegRtSum_Object = MibTableColumn
adGenAOSnmTwIpvNegRtSum = _AdGenAOSnmTwIpvNegRtSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 52),
    _AdGenAOSnmTwIpvNegRtSum_Type()
)
adGenAOSnmTwIpvNegRtSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegRtSum.setStatus("current")
_AdGenAOSnmTwIpvNegRtSum2_Type = Counter64
_AdGenAOSnmTwIpvNegRtSum2_Object = MibTableColumn
adGenAOSnmTwIpvNegRtSum2 = _AdGenAOSnmTwIpvNegRtSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 53),
    _AdGenAOSnmTwIpvNegRtSum2_Type()
)
adGenAOSnmTwIpvNegRtSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegRtSum2.setStatus("current")
_AdGenAOSnmTwIpvNegRtNum_Type = Counter32
_AdGenAOSnmTwIpvNegRtNum_Object = MibTableColumn
adGenAOSnmTwIpvNegRtNum = _AdGenAOSnmTwIpvNegRtNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 54),
    _AdGenAOSnmTwIpvNegRtNum_Type()
)
adGenAOSnmTwIpvNegRtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvNegRtNum.setStatus("current")
_AdGenAOSnmTwIpvAbsInMin_Type = Counter32
_AdGenAOSnmTwIpvAbsInMin_Object = MibTableColumn
adGenAOSnmTwIpvAbsInMin = _AdGenAOSnmTwIpvAbsInMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 55),
    _AdGenAOSnmTwIpvAbsInMin_Type()
)
adGenAOSnmTwIpvAbsInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsInMin.setStatus("current")
_AdGenAOSnmTwIpvAbsInMax_Type = Counter32
_AdGenAOSnmTwIpvAbsInMax_Object = MibTableColumn
adGenAOSnmTwIpvAbsInMax = _AdGenAOSnmTwIpvAbsInMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 56),
    _AdGenAOSnmTwIpvAbsInMax_Type()
)
adGenAOSnmTwIpvAbsInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsInMax.setStatus("current")
_AdGenAOSnmTwIpvAbsInSum_Type = Counter32
_AdGenAOSnmTwIpvAbsInSum_Object = MibTableColumn
adGenAOSnmTwIpvAbsInSum = _AdGenAOSnmTwIpvAbsInSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 57),
    _AdGenAOSnmTwIpvAbsInSum_Type()
)
adGenAOSnmTwIpvAbsInSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsInSum.setStatus("current")
_AdGenAOSnmTwIpvAbsInSum2_Type = Counter64
_AdGenAOSnmTwIpvAbsInSum2_Object = MibTableColumn
adGenAOSnmTwIpvAbsInSum2 = _AdGenAOSnmTwIpvAbsInSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 58),
    _AdGenAOSnmTwIpvAbsInSum2_Type()
)
adGenAOSnmTwIpvAbsInSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsInSum2.setStatus("current")
_AdGenAOSnmTwIpvAbsInNum_Type = Counter32
_AdGenAOSnmTwIpvAbsInNum_Object = MibTableColumn
adGenAOSnmTwIpvAbsInNum = _AdGenAOSnmTwIpvAbsInNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 59),
    _AdGenAOSnmTwIpvAbsInNum_Type()
)
adGenAOSnmTwIpvAbsInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsInNum.setStatus("current")
_AdGenAOSnmTwIpvAbsOutMin_Type = Counter32
_AdGenAOSnmTwIpvAbsOutMin_Object = MibTableColumn
adGenAOSnmTwIpvAbsOutMin = _AdGenAOSnmTwIpvAbsOutMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 60),
    _AdGenAOSnmTwIpvAbsOutMin_Type()
)
adGenAOSnmTwIpvAbsOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsOutMin.setStatus("current")
_AdGenAOSnmTwIpvAbsOutMax_Type = Counter32
_AdGenAOSnmTwIpvAbsOutMax_Object = MibTableColumn
adGenAOSnmTwIpvAbsOutMax = _AdGenAOSnmTwIpvAbsOutMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 61),
    _AdGenAOSnmTwIpvAbsOutMax_Type()
)
adGenAOSnmTwIpvAbsOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsOutMax.setStatus("current")
_AdGenAOSnmTwIpvAbsOutSum_Type = Counter32
_AdGenAOSnmTwIpvAbsOutSum_Object = MibTableColumn
adGenAOSnmTwIpvAbsOutSum = _AdGenAOSnmTwIpvAbsOutSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 62),
    _AdGenAOSnmTwIpvAbsOutSum_Type()
)
adGenAOSnmTwIpvAbsOutSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsOutSum.setStatus("current")
_AdGenAOSnmTwIpvAbsOutSum2_Type = Counter64
_AdGenAOSnmTwIpvAbsOutSum2_Object = MibTableColumn
adGenAOSnmTwIpvAbsOutSum2 = _AdGenAOSnmTwIpvAbsOutSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 63),
    _AdGenAOSnmTwIpvAbsOutSum2_Type()
)
adGenAOSnmTwIpvAbsOutSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsOutSum2.setStatus("current")
_AdGenAOSnmTwIpvAbsOutNum_Type = Counter32
_AdGenAOSnmTwIpvAbsOutNum_Object = MibTableColumn
adGenAOSnmTwIpvAbsOutNum = _AdGenAOSnmTwIpvAbsOutNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 64),
    _AdGenAOSnmTwIpvAbsOutNum_Type()
)
adGenAOSnmTwIpvAbsOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsOutNum.setStatus("current")
_AdGenAOSnmTwIpvAbsRtMin_Type = Counter32
_AdGenAOSnmTwIpvAbsRtMin_Object = MibTableColumn
adGenAOSnmTwIpvAbsRtMin = _AdGenAOSnmTwIpvAbsRtMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 65),
    _AdGenAOSnmTwIpvAbsRtMin_Type()
)
adGenAOSnmTwIpvAbsRtMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsRtMin.setStatus("current")
_AdGenAOSnmTwIpvAbsRtMax_Type = Counter32
_AdGenAOSnmTwIpvAbsRtMax_Object = MibTableColumn
adGenAOSnmTwIpvAbsRtMax = _AdGenAOSnmTwIpvAbsRtMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 66),
    _AdGenAOSnmTwIpvAbsRtMax_Type()
)
adGenAOSnmTwIpvAbsRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsRtMax.setStatus("current")
_AdGenAOSnmTwIpvAbsRtSum_Type = Counter32
_AdGenAOSnmTwIpvAbsRtSum_Object = MibTableColumn
adGenAOSnmTwIpvAbsRtSum = _AdGenAOSnmTwIpvAbsRtSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 67),
    _AdGenAOSnmTwIpvAbsRtSum_Type()
)
adGenAOSnmTwIpvAbsRtSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsRtSum.setStatus("current")
_AdGenAOSnmTwIpvAbsRtSum2_Type = Counter64
_AdGenAOSnmTwIpvAbsRtSum2_Object = MibTableColumn
adGenAOSnmTwIpvAbsRtSum2 = _AdGenAOSnmTwIpvAbsRtSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 68),
    _AdGenAOSnmTwIpvAbsRtSum2_Type()
)
adGenAOSnmTwIpvAbsRtSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsRtSum2.setStatus("current")
_AdGenAOSnmTwIpvAbsRtNum_Type = Counter32
_AdGenAOSnmTwIpvAbsRtNum_Object = MibTableColumn
adGenAOSnmTwIpvAbsRtNum = _AdGenAOSnmTwIpvAbsRtNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 69),
    _AdGenAOSnmTwIpvAbsRtNum_Type()
)
adGenAOSnmTwIpvAbsRtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwIpvAbsRtNum.setStatus("current")
_AdGenAOSnmTwPktSentCount_Type = Counter32
_AdGenAOSnmTwPktSentCount_Object = MibTableColumn
adGenAOSnmTwPktSentCount = _AdGenAOSnmTwPktSentCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 6, 1, 70),
    _AdGenAOSnmTwPktSentCount_Type()
)
adGenAOSnmTwPktSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwPktSentCount.setStatus("current")
_AdGenAOSnmCfgICMPTSProbeTable_Object = MibTable
adGenAOSnmCfgICMPTSProbeTable = _AdGenAOSnmCfgICMPTSProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7)
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgICMPTSProbeTable.setStatus("current")
_AdGenAOSnmCfgICMPTSProbeEntry_Object = MibTableRow
adGenAOSnmCfgICMPTSProbeEntry = _AdGenAOSnmCfgICMPTSProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1)
)
adGenAOSnmCfgICMPTSProbeEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgICMPTSProbeEntry.setStatus("current")


class _AdGenAOSnmCfgICMPTSName_Type(OctetString):
    """Custom type adGenAOSnmCfgICMPTSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmCfgICMPTSName_Type.__name__ = "OctetString"
_AdGenAOSnmCfgICMPTSName_Object = MibTableColumn
adGenAOSnmCfgICMPTSName = _AdGenAOSnmCfgICMPTSName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 1),
    _AdGenAOSnmCfgICMPTSName_Type()
)
adGenAOSnmCfgICMPTSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmCfgICMPTSName.setStatus("current")
_AdGenAOSnmICMPTSDestHostname_Type = DisplayString
_AdGenAOSnmICMPTSDestHostname_Object = MibTableColumn
adGenAOSnmICMPTSDestHostname = _AdGenAOSnmICMPTSDestHostname_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 2),
    _AdGenAOSnmICMPTSDestHostname_Type()
)
adGenAOSnmICMPTSDestHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDestHostname.setStatus("current")
_AdGenAOSnmICMPTSSrcIP_Type = IpAddress
_AdGenAOSnmICMPTSSrcIP_Object = MibTableColumn
adGenAOSnmICMPTSSrcIP = _AdGenAOSnmICMPTSSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 3),
    _AdGenAOSnmICMPTSSrcIP_Type()
)
adGenAOSnmICMPTSSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSSrcIP.setStatus("current")


class _AdGenAOSnmICMPTSDscp_Type(Integer32):
    """Custom type adGenAOSnmICMPTSDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenAOSnmICMPTSDscp_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSDscp_Object = MibTableColumn
adGenAOSnmICMPTSDscp = _AdGenAOSnmICMPTSDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 4),
    _AdGenAOSnmICMPTSDscp_Type()
)
adGenAOSnmICMPTSDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDscp.setStatus("current")


class _AdGenAOSnmICMPTSPaddingLen_Type(Integer32):
    """Custom type adGenAOSnmICMPTSPaddingLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1462),
    )


_AdGenAOSnmICMPTSPaddingLen_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSPaddingLen_Object = MibTableColumn
adGenAOSnmICMPTSPaddingLen = _AdGenAOSnmICMPTSPaddingLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 5),
    _AdGenAOSnmICMPTSPaddingLen_Type()
)
adGenAOSnmICMPTSPaddingLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSPaddingLen.setStatus("current")


class _AdGenAOSnmICMPTSPaddingFormat_Type(Integer32):
    """Custom type adGenAOSnmICMPTSPaddingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_AdGenAOSnmICMPTSPaddingFormat_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSPaddingFormat_Object = MibTableColumn
adGenAOSnmICMPTSPaddingFormat = _AdGenAOSnmICMPTSPaddingFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 6),
    _AdGenAOSnmICMPTSPaddingFormat_Type()
)
adGenAOSnmICMPTSPaddingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSPaddingFormat.setStatus("current")


class _AdGenAOSnmICMPTSPaddingPattern_Type(OctetString):
    """Custom type adGenAOSnmICMPTSPaddingPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenAOSnmICMPTSPaddingPattern_Type.__name__ = "OctetString"
_AdGenAOSnmICMPTSPaddingPattern_Object = MibTableColumn
adGenAOSnmICMPTSPaddingPattern = _AdGenAOSnmICMPTSPaddingPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 7),
    _AdGenAOSnmICMPTSPaddingPattern_Type()
)
adGenAOSnmICMPTSPaddingPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSPaddingPattern.setStatus("current")


class _AdGenAOSnmICMPTSDataPadType_Type(Integer32):
    """Custom type adGenAOSnmICMPTSDataPadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("custom", 3),
          ("random", 2),
          ("zeroes", 1))
    )


_AdGenAOSnmICMPTSDataPadType_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSDataPadType_Object = MibTableColumn
adGenAOSnmICMPTSDataPadType = _AdGenAOSnmICMPTSDataPadType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 8),
    _AdGenAOSnmICMPTSDataPadType_Type()
)
adGenAOSnmICMPTSDataPadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDataPadType.setStatus("current")


class _AdGenAOSnmICMPTSPktSendCnt_Type(Integer32):
    """Custom type adGenAOSnmICMPTSPktSendCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AdGenAOSnmICMPTSPktSendCnt_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSPktSendCnt_Object = MibTableColumn
adGenAOSnmICMPTSPktSendCnt = _AdGenAOSnmICMPTSPktSendCnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 9),
    _AdGenAOSnmICMPTSPktSendCnt_Type()
)
adGenAOSnmICMPTSPktSendCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSPktSendCnt.setStatus("current")


class _AdGenAOSnmICMPTSSendScheduleType_Type(Integer32):
    """Custom type adGenAOSnmICMPTSSendScheduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("periodic", 1),
          ("poisson", 2))
    )


_AdGenAOSnmICMPTSSendScheduleType_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSSendScheduleType_Object = MibTableColumn
adGenAOSnmICMPTSSendScheduleType = _AdGenAOSnmICMPTSSendScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 10),
    _AdGenAOSnmICMPTSSendScheduleType_Type()
)
adGenAOSnmICMPTSSendScheduleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSSendScheduleType.setStatus("current")


class _AdGenAOSnmICMPTSSendScheduleValue_Type(Integer32):
    """Custom type adGenAOSnmICMPTSSendScheduleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5000),
    )


_AdGenAOSnmICMPTSSendScheduleValue_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSSendScheduleValue_Object = MibTableColumn
adGenAOSnmICMPTSSendScheduleValue = _AdGenAOSnmICMPTSSendScheduleValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 11),
    _AdGenAOSnmICMPTSSendScheduleValue_Type()
)
adGenAOSnmICMPTSSendScheduleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSSendScheduleValue.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsInMinFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsInMinFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsInMinFail = _AdGenAOSnmICMPTSIpdvAbsInMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 12),
    _AdGenAOSnmICMPTSIpdvAbsInMinFail_Type()
)
adGenAOSnmICMPTSIpdvAbsInMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsInMinFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsInAvgFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsInAvgFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsInAvgFail = _AdGenAOSnmICMPTSIpdvAbsInAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 13),
    _AdGenAOSnmICMPTSIpdvAbsInAvgFail_Type()
)
adGenAOSnmICMPTSIpdvAbsInAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsInAvgFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsInMaxFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsInMaxFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsInMaxFail = _AdGenAOSnmICMPTSIpdvAbsInMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 14),
    _AdGenAOSnmICMPTSIpdvAbsInMaxFail_Type()
)
adGenAOSnmICMPTSIpdvAbsInMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsInMaxFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsInMinPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsInMinPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsInMinPass = _AdGenAOSnmICMPTSIpdvAbsInMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 15),
    _AdGenAOSnmICMPTSIpdvAbsInMinPass_Type()
)
adGenAOSnmICMPTSIpdvAbsInMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsInMinPass.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsInAvgPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsInAvgPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsInAvgPass = _AdGenAOSnmICMPTSIpdvAbsInAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 16),
    _AdGenAOSnmICMPTSIpdvAbsInAvgPass_Type()
)
adGenAOSnmICMPTSIpdvAbsInAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsInAvgPass.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsInMaxPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsInMaxPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsInMaxPass = _AdGenAOSnmICMPTSIpdvAbsInMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 17),
    _AdGenAOSnmICMPTSIpdvAbsInMaxPass_Type()
)
adGenAOSnmICMPTSIpdvAbsInMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsInMaxPass.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsOutMinFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsOutMinFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsOutMinFail = _AdGenAOSnmICMPTSIpdvAbsOutMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 18),
    _AdGenAOSnmICMPTSIpdvAbsOutMinFail_Type()
)
adGenAOSnmICMPTSIpdvAbsOutMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsOutMinFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsOutAvgFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsOutAvgFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsOutAvgFail = _AdGenAOSnmICMPTSIpdvAbsOutAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 19),
    _AdGenAOSnmICMPTSIpdvAbsOutAvgFail_Type()
)
adGenAOSnmICMPTSIpdvAbsOutAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsOutAvgFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsOutMaxFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsOutMaxFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsOutMaxFail = _AdGenAOSnmICMPTSIpdvAbsOutMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 20),
    _AdGenAOSnmICMPTSIpdvAbsOutMaxFail_Type()
)
adGenAOSnmICMPTSIpdvAbsOutMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsOutMaxFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsOutMinPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsOutMinPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsOutMinPass = _AdGenAOSnmICMPTSIpdvAbsOutMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 21),
    _AdGenAOSnmICMPTSIpdvAbsOutMinPass_Type()
)
adGenAOSnmICMPTSIpdvAbsOutMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsOutMinPass.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsOutAvgPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsOutAvgPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsOutAvgPass = _AdGenAOSnmICMPTSIpdvAbsOutAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 22),
    _AdGenAOSnmICMPTSIpdvAbsOutAvgPass_Type()
)
adGenAOSnmICMPTSIpdvAbsOutAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsOutAvgPass.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsOutMaxPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsOutMaxPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsOutMaxPass = _AdGenAOSnmICMPTSIpdvAbsOutMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 23),
    _AdGenAOSnmICMPTSIpdvAbsOutMaxPass_Type()
)
adGenAOSnmICMPTSIpdvAbsOutMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsOutMaxPass.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsRtMinFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsRtMinFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsRtMinFail = _AdGenAOSnmICMPTSIpdvAbsRtMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 24),
    _AdGenAOSnmICMPTSIpdvAbsRtMinFail_Type()
)
adGenAOSnmICMPTSIpdvAbsRtMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsRtMinFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsRtAvgFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsRtAvgFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsRtAvgFail = _AdGenAOSnmICMPTSIpdvAbsRtAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 25),
    _AdGenAOSnmICMPTSIpdvAbsRtAvgFail_Type()
)
adGenAOSnmICMPTSIpdvAbsRtAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsRtAvgFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsRtMaxFail_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsRtMaxFail_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsRtMaxFail = _AdGenAOSnmICMPTSIpdvAbsRtMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 26),
    _AdGenAOSnmICMPTSIpdvAbsRtMaxFail_Type()
)
adGenAOSnmICMPTSIpdvAbsRtMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsRtMaxFail.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsRtMinPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsRtMinPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsRtMinPass = _AdGenAOSnmICMPTSIpdvAbsRtMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 27),
    _AdGenAOSnmICMPTSIpdvAbsRtMinPass_Type()
)
adGenAOSnmICMPTSIpdvAbsRtMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsRtMinPass.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsRtAvgPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsRtAvgPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsRtAvgPass = _AdGenAOSnmICMPTSIpdvAbsRtAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 28),
    _AdGenAOSnmICMPTSIpdvAbsRtAvgPass_Type()
)
adGenAOSnmICMPTSIpdvAbsRtAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsRtAvgPass.setStatus("current")
_AdGenAOSnmICMPTSIpdvAbsRtMaxPass_Type = Unsigned32
_AdGenAOSnmICMPTSIpdvAbsRtMaxPass_Object = MibTableColumn
adGenAOSnmICMPTSIpdvAbsRtMaxPass = _AdGenAOSnmICMPTSIpdvAbsRtMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 29),
    _AdGenAOSnmICMPTSIpdvAbsRtMaxPass_Type()
)
adGenAOSnmICMPTSIpdvAbsRtMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpdvAbsRtMaxPass.setStatus("current")
_AdGenAOSnmICMPTSDelayInMinFail_Type = Integer32
_AdGenAOSnmICMPTSDelayInMinFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayInMinFail = _AdGenAOSnmICMPTSDelayInMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 30),
    _AdGenAOSnmICMPTSDelayInMinFail_Type()
)
adGenAOSnmICMPTSDelayInMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInMinFail.setStatus("current")
_AdGenAOSnmICMPTSDelayInAvgFail_Type = Integer32
_AdGenAOSnmICMPTSDelayInAvgFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayInAvgFail = _AdGenAOSnmICMPTSDelayInAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 31),
    _AdGenAOSnmICMPTSDelayInAvgFail_Type()
)
adGenAOSnmICMPTSDelayInAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInAvgFail.setStatus("current")
_AdGenAOSnmICMPTSDelayInMaxFail_Type = Integer32
_AdGenAOSnmICMPTSDelayInMaxFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayInMaxFail = _AdGenAOSnmICMPTSDelayInMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 32),
    _AdGenAOSnmICMPTSDelayInMaxFail_Type()
)
adGenAOSnmICMPTSDelayInMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInMaxFail.setStatus("current")
_AdGenAOSnmICMPTSDelayInMinPass_Type = Integer32
_AdGenAOSnmICMPTSDelayInMinPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayInMinPass = _AdGenAOSnmICMPTSDelayInMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 33),
    _AdGenAOSnmICMPTSDelayInMinPass_Type()
)
adGenAOSnmICMPTSDelayInMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInMinPass.setStatus("current")
_AdGenAOSnmICMPTSDelayInAvgPass_Type = Integer32
_AdGenAOSnmICMPTSDelayInAvgPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayInAvgPass = _AdGenAOSnmICMPTSDelayInAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 34),
    _AdGenAOSnmICMPTSDelayInAvgPass_Type()
)
adGenAOSnmICMPTSDelayInAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInAvgPass.setStatus("current")
_AdGenAOSnmICMPTSDelayInMaxPass_Type = Integer32
_AdGenAOSnmICMPTSDelayInMaxPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayInMaxPass = _AdGenAOSnmICMPTSDelayInMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 35),
    _AdGenAOSnmICMPTSDelayInMaxPass_Type()
)
adGenAOSnmICMPTSDelayInMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInMaxPass.setStatus("current")
_AdGenAOSnmICMPTSDelayOutMinFail_Type = Integer32
_AdGenAOSnmICMPTSDelayOutMinFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutMinFail = _AdGenAOSnmICMPTSDelayOutMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 36),
    _AdGenAOSnmICMPTSDelayOutMinFail_Type()
)
adGenAOSnmICMPTSDelayOutMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutMinFail.setStatus("current")
_AdGenAOSnmICMPTSDelayOutAvgFail_Type = Integer32
_AdGenAOSnmICMPTSDelayOutAvgFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutAvgFail = _AdGenAOSnmICMPTSDelayOutAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 37),
    _AdGenAOSnmICMPTSDelayOutAvgFail_Type()
)
adGenAOSnmICMPTSDelayOutAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutAvgFail.setStatus("current")
_AdGenAOSnmICMPTSDelayOutMaxFail_Type = Integer32
_AdGenAOSnmICMPTSDelayOutMaxFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutMaxFail = _AdGenAOSnmICMPTSDelayOutMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 38),
    _AdGenAOSnmICMPTSDelayOutMaxFail_Type()
)
adGenAOSnmICMPTSDelayOutMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutMaxFail.setStatus("current")
_AdGenAOSnmICMPTSDelayOutMinPass_Type = Integer32
_AdGenAOSnmICMPTSDelayOutMinPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutMinPass = _AdGenAOSnmICMPTSDelayOutMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 39),
    _AdGenAOSnmICMPTSDelayOutMinPass_Type()
)
adGenAOSnmICMPTSDelayOutMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutMinPass.setStatus("current")
_AdGenAOSnmICMPTSDelayOutAvgPass_Type = Integer32
_AdGenAOSnmICMPTSDelayOutAvgPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutAvgPass = _AdGenAOSnmICMPTSDelayOutAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 40),
    _AdGenAOSnmICMPTSDelayOutAvgPass_Type()
)
adGenAOSnmICMPTSDelayOutAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutAvgPass.setStatus("current")
_AdGenAOSnmICMPTSDelayOutMaxPass_Type = Integer32
_AdGenAOSnmICMPTSDelayOutMaxPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutMaxPass = _AdGenAOSnmICMPTSDelayOutMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 41),
    _AdGenAOSnmICMPTSDelayOutMaxPass_Type()
)
adGenAOSnmICMPTSDelayOutMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutMaxPass.setStatus("current")
_AdGenAOSnmICMPTSDelayRtMinFail_Type = Integer32
_AdGenAOSnmICMPTSDelayRtMinFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtMinFail = _AdGenAOSnmICMPTSDelayRtMinFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 42),
    _AdGenAOSnmICMPTSDelayRtMinFail_Type()
)
adGenAOSnmICMPTSDelayRtMinFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtMinFail.setStatus("current")
_AdGenAOSnmICMPTSDelayRtAvgFail_Type = Integer32
_AdGenAOSnmICMPTSDelayRtAvgFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtAvgFail = _AdGenAOSnmICMPTSDelayRtAvgFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 43),
    _AdGenAOSnmICMPTSDelayRtAvgFail_Type()
)
adGenAOSnmICMPTSDelayRtAvgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtAvgFail.setStatus("current")
_AdGenAOSnmICMPTSDelayRtMaxFail_Type = Integer32
_AdGenAOSnmICMPTSDelayRtMaxFail_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtMaxFail = _AdGenAOSnmICMPTSDelayRtMaxFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 44),
    _AdGenAOSnmICMPTSDelayRtMaxFail_Type()
)
adGenAOSnmICMPTSDelayRtMaxFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtMaxFail.setStatus("current")
_AdGenAOSnmICMPTSDelayRtMinPass_Type = Integer32
_AdGenAOSnmICMPTSDelayRtMinPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtMinPass = _AdGenAOSnmICMPTSDelayRtMinPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 45),
    _AdGenAOSnmICMPTSDelayRtMinPass_Type()
)
adGenAOSnmICMPTSDelayRtMinPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtMinPass.setStatus("current")
_AdGenAOSnmICMPTSDelayRtAvgPass_Type = Integer32
_AdGenAOSnmICMPTSDelayRtAvgPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtAvgPass = _AdGenAOSnmICMPTSDelayRtAvgPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 46),
    _AdGenAOSnmICMPTSDelayRtAvgPass_Type()
)
adGenAOSnmICMPTSDelayRtAvgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtAvgPass.setStatus("current")
_AdGenAOSnmICMPTSDelayRtMaxPass_Type = Integer32
_AdGenAOSnmICMPTSDelayRtMaxPass_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtMaxPass = _AdGenAOSnmICMPTSDelayRtMaxPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 47),
    _AdGenAOSnmICMPTSDelayRtMaxPass_Type()
)
adGenAOSnmICMPTSDelayRtMaxPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtMaxPass.setStatus("current")


class _AdGenAOSnmICMPTSPktRtLossFail_Type(Integer32):
    """Custom type adGenAOSnmICMPTSPktRtLossFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdGenAOSnmICMPTSPktRtLossFail_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSPktRtLossFail_Object = MibTableColumn
adGenAOSnmICMPTSPktRtLossFail = _AdGenAOSnmICMPTSPktRtLossFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 48),
    _AdGenAOSnmICMPTSPktRtLossFail_Type()
)
adGenAOSnmICMPTSPktRtLossFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSPktRtLossFail.setStatus("current")


class _AdGenAOSnmICMPTSPktRtLossPass_Type(Integer32):
    """Custom type adGenAOSnmICMPTSPktRtLossPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdGenAOSnmICMPTSPktRtLossPass_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSPktRtLossPass_Object = MibTableColumn
adGenAOSnmICMPTSPktRtLossPass = _AdGenAOSnmICMPTSPktRtLossPass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 49),
    _AdGenAOSnmICMPTSPktRtLossPass_Type()
)
adGenAOSnmICMPTSPktRtLossPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSPktRtLossPass.setStatus("current")


class _AdGenAOSnmICMPTSHistoryDepth_Type(Integer32):
    """Custom type adGenAOSnmICMPTSHistoryDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AdGenAOSnmICMPTSHistoryDepth_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSHistoryDepth_Object = MibTableColumn
adGenAOSnmICMPTSHistoryDepth = _AdGenAOSnmICMPTSHistoryDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 7, 1, 50),
    _AdGenAOSnmICMPTSHistoryDepth_Type()
)
adGenAOSnmICMPTSHistoryDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSHistoryDepth.setStatus("current")
_AdGenAOSnmICMPTSHistoryTable_Object = MibTable
adGenAOSnmICMPTSHistoryTable = _AdGenAOSnmICMPTSHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8)
)
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSHistoryTable.setStatus("current")
_AdGenAOSnmICMPTSHistoryEntry_Object = MibTableRow
adGenAOSnmICMPTSHistoryEntry = _AdGenAOSnmICMPTSHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1)
)
adGenAOSnmICMPTSHistoryEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSSeqNum"),
)
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSHistoryEntry.setStatus("current")


class _AdGenAOSnmICMPTSSeqNum_Type(Integer32):
    """Custom type adGenAOSnmICMPTSSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AdGenAOSnmICMPTSSeqNum_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSSeqNum_Object = MibTableColumn
adGenAOSnmICMPTSSeqNum = _AdGenAOSnmICMPTSSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 1),
    _AdGenAOSnmICMPTSSeqNum_Type()
)
adGenAOSnmICMPTSSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSSeqNum.setStatus("current")


class _AdGenAOSnmICMPTSHistoryName_Type(OctetString):
    """Custom type adGenAOSnmICMPTSHistoryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmICMPTSHistoryName_Type.__name__ = "OctetString"
_AdGenAOSnmICMPTSHistoryName_Object = MibTableColumn
adGenAOSnmICMPTSHistoryName = _AdGenAOSnmICMPTSHistoryName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 2),
    _AdGenAOSnmICMPTSHistoryName_Type()
)
adGenAOSnmICMPTSHistoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSHistoryName.setStatus("current")
_AdGenAOSnmICMPTSStartTime_Type = DisplayString
_AdGenAOSnmICMPTSStartTime_Object = MibTableColumn
adGenAOSnmICMPTSStartTime = _AdGenAOSnmICMPTSStartTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 3),
    _AdGenAOSnmICMPTSStartTime_Type()
)
adGenAOSnmICMPTSStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSStartTime.setStatus("current")
_AdGenAOSnmICMPTSEndTime_Type = DisplayString
_AdGenAOSnmICMPTSEndTime_Object = MibTableColumn
adGenAOSnmICMPTSEndTime = _AdGenAOSnmICMPTSEndTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 4),
    _AdGenAOSnmICMPTSEndTime_Type()
)
adGenAOSnmICMPTSEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSEndTime.setStatus("current")
_AdGenAOSnmICMPTSDelayInMin_Type = Integer32
_AdGenAOSnmICMPTSDelayInMin_Object = MibTableColumn
adGenAOSnmICMPTSDelayInMin = _AdGenAOSnmICMPTSDelayInMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 5),
    _AdGenAOSnmICMPTSDelayInMin_Type()
)
adGenAOSnmICMPTSDelayInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInMin.setStatus("current")
_AdGenAOSnmICMPTSDelayInMax_Type = Integer32
_AdGenAOSnmICMPTSDelayInMax_Object = MibTableColumn
adGenAOSnmICMPTSDelayInMax = _AdGenAOSnmICMPTSDelayInMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 6),
    _AdGenAOSnmICMPTSDelayInMax_Type()
)
adGenAOSnmICMPTSDelayInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInMax.setStatus("current")
_AdGenAOSnmICMPTSDelayOutMin_Type = Integer32
_AdGenAOSnmICMPTSDelayOutMin_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutMin = _AdGenAOSnmICMPTSDelayOutMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 7),
    _AdGenAOSnmICMPTSDelayOutMin_Type()
)
adGenAOSnmICMPTSDelayOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutMin.setStatus("current")
_AdGenAOSnmICMPTSDelayOutMax_Type = Integer32
_AdGenAOSnmICMPTSDelayOutMax_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutMax = _AdGenAOSnmICMPTSDelayOutMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 8),
    _AdGenAOSnmICMPTSDelayOutMax_Type()
)
adGenAOSnmICMPTSDelayOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutMax.setStatus("current")
_AdGenAOSnmICMPTSDelayRtMin_Type = Integer32
_AdGenAOSnmICMPTSDelayRtMin_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtMin = _AdGenAOSnmICMPTSDelayRtMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 9),
    _AdGenAOSnmICMPTSDelayRtMin_Type()
)
adGenAOSnmICMPTSDelayRtMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtMin.setStatus("current")
_AdGenAOSnmICMPTSDelayRtMax_Type = Integer32
_AdGenAOSnmICMPTSDelayRtMax_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtMax = _AdGenAOSnmICMPTSDelayRtMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 10),
    _AdGenAOSnmICMPTSDelayRtMax_Type()
)
adGenAOSnmICMPTSDelayRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtMax.setStatus("current")
_AdGenAOSnmICMPTSLossRoundTrip_Type = Counter32
_AdGenAOSnmICMPTSLossRoundTrip_Object = MibTableColumn
adGenAOSnmICMPTSLossRoundTrip = _AdGenAOSnmICMPTSLossRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 11),
    _AdGenAOSnmICMPTSLossRoundTrip_Type()
)
adGenAOSnmICMPTSLossRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSLossRoundTrip.setStatus("current")
_AdGenAOSnmICMPTSDelayOutSum_Type = Integer32
_AdGenAOSnmICMPTSDelayOutSum_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutSum = _AdGenAOSnmICMPTSDelayOutSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 12),
    _AdGenAOSnmICMPTSDelayOutSum_Type()
)
adGenAOSnmICMPTSDelayOutSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutSum.setStatus("current")
_AdGenAOSnmICMPTSDelayOutSum2_Type = Counter64
_AdGenAOSnmICMPTSDelayOutSum2_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutSum2 = _AdGenAOSnmICMPTSDelayOutSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 13),
    _AdGenAOSnmICMPTSDelayOutSum2_Type()
)
adGenAOSnmICMPTSDelayOutSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutSum2.setStatus("current")
_AdGenAOSnmICMPTSDelayOutNum_Type = Counter32
_AdGenAOSnmICMPTSDelayOutNum_Object = MibTableColumn
adGenAOSnmICMPTSDelayOutNum = _AdGenAOSnmICMPTSDelayOutNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 14),
    _AdGenAOSnmICMPTSDelayOutNum_Type()
)
adGenAOSnmICMPTSDelayOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayOutNum.setStatus("current")
_AdGenAOSnmICMPTSDelayInSum_Type = Integer32
_AdGenAOSnmICMPTSDelayInSum_Object = MibTableColumn
adGenAOSnmICMPTSDelayInSum = _AdGenAOSnmICMPTSDelayInSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 15),
    _AdGenAOSnmICMPTSDelayInSum_Type()
)
adGenAOSnmICMPTSDelayInSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInSum.setStatus("current")
_AdGenAOSnmICMPTSDelayInSum2_Type = Counter64
_AdGenAOSnmICMPTSDelayInSum2_Object = MibTableColumn
adGenAOSnmICMPTSDelayInSum2 = _AdGenAOSnmICMPTSDelayInSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 16),
    _AdGenAOSnmICMPTSDelayInSum2_Type()
)
adGenAOSnmICMPTSDelayInSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInSum2.setStatus("current")
_AdGenAOSnmICMPTSDelayInNum_Type = Counter32
_AdGenAOSnmICMPTSDelayInNum_Object = MibTableColumn
adGenAOSnmICMPTSDelayInNum = _AdGenAOSnmICMPTSDelayInNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 17),
    _AdGenAOSnmICMPTSDelayInNum_Type()
)
adGenAOSnmICMPTSDelayInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayInNum.setStatus("current")
_AdGenAOSnmICMPTSDelayRtSum_Type = Integer32
_AdGenAOSnmICMPTSDelayRtSum_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtSum = _AdGenAOSnmICMPTSDelayRtSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 18),
    _AdGenAOSnmICMPTSDelayRtSum_Type()
)
adGenAOSnmICMPTSDelayRtSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtSum.setStatus("current")
_AdGenAOSnmICMPTSDelayRtSum2_Type = Counter64
_AdGenAOSnmICMPTSDelayRtSum2_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtSum2 = _AdGenAOSnmICMPTSDelayRtSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 19),
    _AdGenAOSnmICMPTSDelayRtSum2_Type()
)
adGenAOSnmICMPTSDelayRtSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtSum2.setStatus("current")
_AdGenAOSnmICMPTSDelayRtNum_Type = Counter32
_AdGenAOSnmICMPTSDelayRtNum_Object = MibTableColumn
adGenAOSnmICMPTSDelayRtNum = _AdGenAOSnmICMPTSDelayRtNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 20),
    _AdGenAOSnmICMPTSDelayRtNum_Type()
)
adGenAOSnmICMPTSDelayRtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSDelayRtNum.setStatus("current")
_AdGenAOSnmICMPTSIpvPosInMin_Type = Counter32
_AdGenAOSnmICMPTSIpvPosInMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosInMin = _AdGenAOSnmICMPTSIpvPosInMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 21),
    _AdGenAOSnmICMPTSIpvPosInMin_Type()
)
adGenAOSnmICMPTSIpvPosInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosInMin.setStatus("current")
_AdGenAOSnmICMPTSIpvPosInMax_Type = Counter32
_AdGenAOSnmICMPTSIpvPosInMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosInMax = _AdGenAOSnmICMPTSIpvPosInMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 22),
    _AdGenAOSnmICMPTSIpvPosInMax_Type()
)
adGenAOSnmICMPTSIpvPosInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosInMax.setStatus("current")
_AdGenAOSnmICMPTSIpvPosInSum_Type = Counter32
_AdGenAOSnmICMPTSIpvPosInSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosInSum = _AdGenAOSnmICMPTSIpvPosInSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 23),
    _AdGenAOSnmICMPTSIpvPosInSum_Type()
)
adGenAOSnmICMPTSIpvPosInSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosInSum.setStatus("current")
_AdGenAOSnmICMPTSIpvPosInSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvPosInSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosInSum2 = _AdGenAOSnmICMPTSIpvPosInSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 24),
    _AdGenAOSnmICMPTSIpvPosInSum2_Type()
)
adGenAOSnmICMPTSIpvPosInSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosInSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvPosInNum_Type = Counter32
_AdGenAOSnmICMPTSIpvPosInNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosInNum = _AdGenAOSnmICMPTSIpvPosInNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 25),
    _AdGenAOSnmICMPTSIpvPosInNum_Type()
)
adGenAOSnmICMPTSIpvPosInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosInNum.setStatus("current")
_AdGenAOSnmICMPTSIpvPosOutMin_Type = Counter32
_AdGenAOSnmICMPTSIpvPosOutMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosOutMin = _AdGenAOSnmICMPTSIpvPosOutMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 26),
    _AdGenAOSnmICMPTSIpvPosOutMin_Type()
)
adGenAOSnmICMPTSIpvPosOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosOutMin.setStatus("current")
_AdGenAOSnmICMPTSIpvPosOutMax_Type = Counter32
_AdGenAOSnmICMPTSIpvPosOutMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosOutMax = _AdGenAOSnmICMPTSIpvPosOutMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 27),
    _AdGenAOSnmICMPTSIpvPosOutMax_Type()
)
adGenAOSnmICMPTSIpvPosOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosOutMax.setStatus("current")
_AdGenAOSnmICMPTSIpvPosOutSum_Type = Counter32
_AdGenAOSnmICMPTSIpvPosOutSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosOutSum = _AdGenAOSnmICMPTSIpvPosOutSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 28),
    _AdGenAOSnmICMPTSIpvPosOutSum_Type()
)
adGenAOSnmICMPTSIpvPosOutSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosOutSum.setStatus("current")
_AdGenAOSnmICMPTSIpvPosOutSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvPosOutSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosOutSum2 = _AdGenAOSnmICMPTSIpvPosOutSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 29),
    _AdGenAOSnmICMPTSIpvPosOutSum2_Type()
)
adGenAOSnmICMPTSIpvPosOutSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosOutSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvPosOutNum_Type = Counter32
_AdGenAOSnmICMPTSIpvPosOutNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosOutNum = _AdGenAOSnmICMPTSIpvPosOutNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 30),
    _AdGenAOSnmICMPTSIpvPosOutNum_Type()
)
adGenAOSnmICMPTSIpvPosOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosOutNum.setStatus("current")
_AdGenAOSnmICMPTSIpvPosRtMin_Type = Counter32
_AdGenAOSnmICMPTSIpvPosRtMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosRtMin = _AdGenAOSnmICMPTSIpvPosRtMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 31),
    _AdGenAOSnmICMPTSIpvPosRtMin_Type()
)
adGenAOSnmICMPTSIpvPosRtMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosRtMin.setStatus("current")
_AdGenAOSnmICMPTSIpvPosRtMax_Type = Counter32
_AdGenAOSnmICMPTSIpvPosRtMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosRtMax = _AdGenAOSnmICMPTSIpvPosRtMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 32),
    _AdGenAOSnmICMPTSIpvPosRtMax_Type()
)
adGenAOSnmICMPTSIpvPosRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosRtMax.setStatus("current")
_AdGenAOSnmICMPTSIpvPosRtSum_Type = Counter32
_AdGenAOSnmICMPTSIpvPosRtSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosRtSum = _AdGenAOSnmICMPTSIpvPosRtSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 33),
    _AdGenAOSnmICMPTSIpvPosRtSum_Type()
)
adGenAOSnmICMPTSIpvPosRtSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosRtSum.setStatus("current")
_AdGenAOSnmICMPTSIpvPosRtSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvPosRtSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosRtSum2 = _AdGenAOSnmICMPTSIpvPosRtSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 34),
    _AdGenAOSnmICMPTSIpvPosRtSum2_Type()
)
adGenAOSnmICMPTSIpvPosRtSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosRtSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvPosRtNum_Type = Counter32
_AdGenAOSnmICMPTSIpvPosRtNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvPosRtNum = _AdGenAOSnmICMPTSIpvPosRtNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 35),
    _AdGenAOSnmICMPTSIpvPosRtNum_Type()
)
adGenAOSnmICMPTSIpvPosRtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvPosRtNum.setStatus("current")
_AdGenAOSnmICMPTSIpvNegInMin_Type = Counter32
_AdGenAOSnmICMPTSIpvNegInMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegInMin = _AdGenAOSnmICMPTSIpvNegInMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 36),
    _AdGenAOSnmICMPTSIpvNegInMin_Type()
)
adGenAOSnmICMPTSIpvNegInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegInMin.setStatus("current")
_AdGenAOSnmICMPTSIpvNegInMax_Type = Counter32
_AdGenAOSnmICMPTSIpvNegInMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegInMax = _AdGenAOSnmICMPTSIpvNegInMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 37),
    _AdGenAOSnmICMPTSIpvNegInMax_Type()
)
adGenAOSnmICMPTSIpvNegInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegInMax.setStatus("current")
_AdGenAOSnmICMPTSIpvNegInSum_Type = Counter32
_AdGenAOSnmICMPTSIpvNegInSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegInSum = _AdGenAOSnmICMPTSIpvNegInSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 38),
    _AdGenAOSnmICMPTSIpvNegInSum_Type()
)
adGenAOSnmICMPTSIpvNegInSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegInSum.setStatus("current")
_AdGenAOSnmICMPTSIpvNegInSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvNegInSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegInSum2 = _AdGenAOSnmICMPTSIpvNegInSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 39),
    _AdGenAOSnmICMPTSIpvNegInSum2_Type()
)
adGenAOSnmICMPTSIpvNegInSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegInSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvNegInNum_Type = Counter32
_AdGenAOSnmICMPTSIpvNegInNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegInNum = _AdGenAOSnmICMPTSIpvNegInNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 40),
    _AdGenAOSnmICMPTSIpvNegInNum_Type()
)
adGenAOSnmICMPTSIpvNegInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegInNum.setStatus("current")
_AdGenAOSnmICMPTSIpvNegOutMin_Type = Counter32
_AdGenAOSnmICMPTSIpvNegOutMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegOutMin = _AdGenAOSnmICMPTSIpvNegOutMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 41),
    _AdGenAOSnmICMPTSIpvNegOutMin_Type()
)
adGenAOSnmICMPTSIpvNegOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegOutMin.setStatus("current")
_AdGenAOSnmICMPTSIpvNegOutMax_Type = Counter32
_AdGenAOSnmICMPTSIpvNegOutMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegOutMax = _AdGenAOSnmICMPTSIpvNegOutMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 42),
    _AdGenAOSnmICMPTSIpvNegOutMax_Type()
)
adGenAOSnmICMPTSIpvNegOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegOutMax.setStatus("current")
_AdGenAOSnmICMPTSIpvNegOutSum_Type = Counter32
_AdGenAOSnmICMPTSIpvNegOutSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegOutSum = _AdGenAOSnmICMPTSIpvNegOutSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 43),
    _AdGenAOSnmICMPTSIpvNegOutSum_Type()
)
adGenAOSnmICMPTSIpvNegOutSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegOutSum.setStatus("current")
_AdGenAOSnmICMPTSIpvNegOutSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvNegOutSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegOutSum2 = _AdGenAOSnmICMPTSIpvNegOutSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 44),
    _AdGenAOSnmICMPTSIpvNegOutSum2_Type()
)
adGenAOSnmICMPTSIpvNegOutSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegOutSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvNegOutNum_Type = Counter32
_AdGenAOSnmICMPTSIpvNegOutNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegOutNum = _AdGenAOSnmICMPTSIpvNegOutNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 45),
    _AdGenAOSnmICMPTSIpvNegOutNum_Type()
)
adGenAOSnmICMPTSIpvNegOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegOutNum.setStatus("current")
_AdGenAOSnmICMPTSIpvNegRtMin_Type = Counter32
_AdGenAOSnmICMPTSIpvNegRtMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegRtMin = _AdGenAOSnmICMPTSIpvNegRtMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 46),
    _AdGenAOSnmICMPTSIpvNegRtMin_Type()
)
adGenAOSnmICMPTSIpvNegRtMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegRtMin.setStatus("current")
_AdGenAOSnmICMPTSIpvNegRtMax_Type = Counter32
_AdGenAOSnmICMPTSIpvNegRtMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegRtMax = _AdGenAOSnmICMPTSIpvNegRtMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 47),
    _AdGenAOSnmICMPTSIpvNegRtMax_Type()
)
adGenAOSnmICMPTSIpvNegRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegRtMax.setStatus("current")
_AdGenAOSnmICMPTSIpvNegRtSum_Type = Counter32
_AdGenAOSnmICMPTSIpvNegRtSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegRtSum = _AdGenAOSnmICMPTSIpvNegRtSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 48),
    _AdGenAOSnmICMPTSIpvNegRtSum_Type()
)
adGenAOSnmICMPTSIpvNegRtSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegRtSum.setStatus("current")
_AdGenAOSnmICMPTSIpvNegRtSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvNegRtSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegRtSum2 = _AdGenAOSnmICMPTSIpvNegRtSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 49),
    _AdGenAOSnmICMPTSIpvNegRtSum2_Type()
)
adGenAOSnmICMPTSIpvNegRtSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegRtSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvNegRtNum_Type = Counter32
_AdGenAOSnmICMPTSIpvNegRtNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvNegRtNum = _AdGenAOSnmICMPTSIpvNegRtNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 50),
    _AdGenAOSnmICMPTSIpvNegRtNum_Type()
)
adGenAOSnmICMPTSIpvNegRtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvNegRtNum.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsInMin_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsInMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsInMin = _AdGenAOSnmICMPTSIpvAbsInMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 51),
    _AdGenAOSnmICMPTSIpvAbsInMin_Type()
)
adGenAOSnmICMPTSIpvAbsInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsInMin.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsInMax_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsInMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsInMax = _AdGenAOSnmICMPTSIpvAbsInMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 52),
    _AdGenAOSnmICMPTSIpvAbsInMax_Type()
)
adGenAOSnmICMPTSIpvAbsInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsInMax.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsInSum_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsInSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsInSum = _AdGenAOSnmICMPTSIpvAbsInSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 53),
    _AdGenAOSnmICMPTSIpvAbsInSum_Type()
)
adGenAOSnmICMPTSIpvAbsInSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsInSum.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsInSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvAbsInSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsInSum2 = _AdGenAOSnmICMPTSIpvAbsInSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 54),
    _AdGenAOSnmICMPTSIpvAbsInSum2_Type()
)
adGenAOSnmICMPTSIpvAbsInSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsInSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsInNum_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsInNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsInNum = _AdGenAOSnmICMPTSIpvAbsInNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 55),
    _AdGenAOSnmICMPTSIpvAbsInNum_Type()
)
adGenAOSnmICMPTSIpvAbsInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsInNum.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsOutMin_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsOutMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsOutMin = _AdGenAOSnmICMPTSIpvAbsOutMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 56),
    _AdGenAOSnmICMPTSIpvAbsOutMin_Type()
)
adGenAOSnmICMPTSIpvAbsOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsOutMin.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsOutMax_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsOutMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsOutMax = _AdGenAOSnmICMPTSIpvAbsOutMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 57),
    _AdGenAOSnmICMPTSIpvAbsOutMax_Type()
)
adGenAOSnmICMPTSIpvAbsOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsOutMax.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsOutSum_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsOutSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsOutSum = _AdGenAOSnmICMPTSIpvAbsOutSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 58),
    _AdGenAOSnmICMPTSIpvAbsOutSum_Type()
)
adGenAOSnmICMPTSIpvAbsOutSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsOutSum.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsOutSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvAbsOutSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsOutSum2 = _AdGenAOSnmICMPTSIpvAbsOutSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 59),
    _AdGenAOSnmICMPTSIpvAbsOutSum2_Type()
)
adGenAOSnmICMPTSIpvAbsOutSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsOutSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsOutNum_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsOutNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsOutNum = _AdGenAOSnmICMPTSIpvAbsOutNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 60),
    _AdGenAOSnmICMPTSIpvAbsOutNum_Type()
)
adGenAOSnmICMPTSIpvAbsOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsOutNum.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsRtMin_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsRtMin_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsRtMin = _AdGenAOSnmICMPTSIpvAbsRtMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 61),
    _AdGenAOSnmICMPTSIpvAbsRtMin_Type()
)
adGenAOSnmICMPTSIpvAbsRtMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsRtMin.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsRtMax_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsRtMax_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsRtMax = _AdGenAOSnmICMPTSIpvAbsRtMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 62),
    _AdGenAOSnmICMPTSIpvAbsRtMax_Type()
)
adGenAOSnmICMPTSIpvAbsRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsRtMax.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsRtSum_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsRtSum_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsRtSum = _AdGenAOSnmICMPTSIpvAbsRtSum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 63),
    _AdGenAOSnmICMPTSIpvAbsRtSum_Type()
)
adGenAOSnmICMPTSIpvAbsRtSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsRtSum.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsRtSum2_Type = Counter64
_AdGenAOSnmICMPTSIpvAbsRtSum2_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsRtSum2 = _AdGenAOSnmICMPTSIpvAbsRtSum2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 64),
    _AdGenAOSnmICMPTSIpvAbsRtSum2_Type()
)
adGenAOSnmICMPTSIpvAbsRtSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsRtSum2.setStatus("current")
_AdGenAOSnmICMPTSIpvAbsRtNum_Type = Counter32
_AdGenAOSnmICMPTSIpvAbsRtNum_Object = MibTableColumn
adGenAOSnmICMPTSIpvAbsRtNum = _AdGenAOSnmICMPTSIpvAbsRtNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 65),
    _AdGenAOSnmICMPTSIpvAbsRtNum_Type()
)
adGenAOSnmICMPTSIpvAbsRtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSIpvAbsRtNum.setStatus("current")
_AdGenAOSnmICMPTSPktSentCount_Type = Counter32
_AdGenAOSnmICMPTSPktSentCount_Object = MibTableColumn
adGenAOSnmICMPTSPktSentCount = _AdGenAOSnmICMPTSPktSentCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 8, 1, 66),
    _AdGenAOSnmICMPTSPktSentCount_Type()
)
adGenAOSnmICMPTSPktSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSPktSentCount.setStatus("current")


class _AdGenAOSnmICMPTSResponder_Type(Integer32):
    """Custom type adGenAOSnmICMPTSResponder based on Integer32"""
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


_AdGenAOSnmICMPTSResponder_Type.__name__ = "Integer32"
_AdGenAOSnmICMPTSResponder_Object = MibScalar
adGenAOSnmICMPTSResponder = _AdGenAOSnmICMPTSResponder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 9),
    _AdGenAOSnmICMPTSResponder_Type()
)
adGenAOSnmICMPTSResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSResponder.setStatus("current")


class _AdGenAOSnmTWAMPResponder_Type(Integer32):
    """Custom type adGenAOSnmTWAMPResponder based on Integer32"""
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


_AdGenAOSnmTWAMPResponder_Type.__name__ = "Integer32"
_AdGenAOSnmTWAMPResponder_Object = MibScalar
adGenAOSnmTWAMPResponder = _AdGenAOSnmTWAMPResponder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 10),
    _AdGenAOSnmTWAMPResponder_Type()
)
adGenAOSnmTWAMPResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmTWAMPResponder.setStatus("current")
_AdGenAOSnmICMPTSResponderStatsTable_Object = MibTable
adGenAOSnmICMPTSResponderStatsTable = _AdGenAOSnmICMPTSResponderStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 11)
)
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSResponderStatsTable.setStatus("current")
_AdGenAOSnmICMPTSResponderStatsEntry_Object = MibTableRow
adGenAOSnmICMPTSResponderStatsEntry = _AdGenAOSnmICMPTSResponderStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 11, 1)
)
adGenAOSnmICMPTSResponderStatsEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSResponderStatsIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSResponderStatsEntry.setStatus("current")
_AdGenAOSnmICMPTSResponderStatsIndex_Type = Unsigned32
_AdGenAOSnmICMPTSResponderStatsIndex_Object = MibTableColumn
adGenAOSnmICMPTSResponderStatsIndex = _AdGenAOSnmICMPTSResponderStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 11, 1, 1),
    _AdGenAOSnmICMPTSResponderStatsIndex_Type()
)
adGenAOSnmICMPTSResponderStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSResponderStatsIndex.setStatus("current")
_AdGenAOSnmICMPTSResponderPacketsReceived_Type = Counter32
_AdGenAOSnmICMPTSResponderPacketsReceived_Object = MibTableColumn
adGenAOSnmICMPTSResponderPacketsReceived = _AdGenAOSnmICMPTSResponderPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 11, 1, 2),
    _AdGenAOSnmICMPTSResponderPacketsReceived_Type()
)
adGenAOSnmICMPTSResponderPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSResponderPacketsReceived.setStatus("current")
_AdGenAOSnmICMPTSResponderPacketsSent_Type = Counter32
_AdGenAOSnmICMPTSResponderPacketsSent_Object = MibTableColumn
adGenAOSnmICMPTSResponderPacketsSent = _AdGenAOSnmICMPTSResponderPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 11, 1, 3),
    _AdGenAOSnmICMPTSResponderPacketsSent_Type()
)
adGenAOSnmICMPTSResponderPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSResponderPacketsSent.setStatus("current")


class _AdGenAOSnmClearICMPTSResponderCounters_Type(Integer32):
    """Custom type adGenAOSnmClearICMPTSResponderCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenAOSnmClearICMPTSResponderCounters_Type.__name__ = "Integer32"
_AdGenAOSnmClearICMPTSResponderCounters_Object = MibTableColumn
adGenAOSnmClearICMPTSResponderCounters = _AdGenAOSnmClearICMPTSResponderCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 11, 1, 4),
    _AdGenAOSnmClearICMPTSResponderCounters_Type()
)
adGenAOSnmClearICMPTSResponderCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmClearICMPTSResponderCounters.setStatus("current")
_AdGenAOSnmTwampResponderStatsTable_Object = MibTable
adGenAOSnmTwampResponderStatsTable = _AdGenAOSnmTwampResponderStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12)
)
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderStatsTable.setStatus("current")
_AdGenAOSnmTwampResponderStatsEntry_Object = MibTableRow
adGenAOSnmTwampResponderStatsEntry = _AdGenAOSnmTwampResponderStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12, 1)
)
adGenAOSnmTwampResponderStatsEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwampResponderStatsIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderStatsEntry.setStatus("current")
_AdGenAOSnmTwampResponderStatsIndex_Type = Unsigned32
_AdGenAOSnmTwampResponderStatsIndex_Object = MibTableColumn
adGenAOSnmTwampResponderStatsIndex = _AdGenAOSnmTwampResponderStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12, 1, 1),
    _AdGenAOSnmTwampResponderStatsIndex_Type()
)
adGenAOSnmTwampResponderStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderStatsIndex.setStatus("current")
_AdGenAOSnmTwampResponderPacketsReceived_Type = Counter32
_AdGenAOSnmTwampResponderPacketsReceived_Object = MibTableColumn
adGenAOSnmTwampResponderPacketsReceived = _AdGenAOSnmTwampResponderPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12, 1, 2),
    _AdGenAOSnmTwampResponderPacketsReceived_Type()
)
adGenAOSnmTwampResponderPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderPacketsReceived.setStatus("current")
_AdGenAOSnmTwampResponderPacketsSent_Type = Counter32
_AdGenAOSnmTwampResponderPacketsSent_Object = MibTableColumn
adGenAOSnmTwampResponderPacketsSent = _AdGenAOSnmTwampResponderPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12, 1, 3),
    _AdGenAOSnmTwampResponderPacketsSent_Type()
)
adGenAOSnmTwampResponderPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderPacketsSent.setStatus("current")
_AdGenAOSnmTwampResponderSessionClosed_Type = Counter32
_AdGenAOSnmTwampResponderSessionClosed_Object = MibTableColumn
adGenAOSnmTwampResponderSessionClosed = _AdGenAOSnmTwampResponderSessionClosed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12, 1, 4),
    _AdGenAOSnmTwampResponderSessionClosed_Type()
)
adGenAOSnmTwampResponderSessionClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderSessionClosed.setStatus("current")
_AdGenAOSnmTwampResponderSessionOpened_Type = Counter32
_AdGenAOSnmTwampResponderSessionOpened_Object = MibTableColumn
adGenAOSnmTwampResponderSessionOpened = _AdGenAOSnmTwampResponderSessionOpened_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12, 1, 5),
    _AdGenAOSnmTwampResponderSessionOpened_Type()
)
adGenAOSnmTwampResponderSessionOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderSessionOpened.setStatus("current")
_AdGenAOSnmTwampResponderSessionRejected_Type = Counter32
_AdGenAOSnmTwampResponderSessionRejected_Object = MibTableColumn
adGenAOSnmTwampResponderSessionRejected = _AdGenAOSnmTwampResponderSessionRejected_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12, 1, 6),
    _AdGenAOSnmTwampResponderSessionRejected_Type()
)
adGenAOSnmTwampResponderSessionRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderSessionRejected.setStatus("current")


class _AdGenAOSnmClearTwampResponderCounters_Type(Integer32):
    """Custom type adGenAOSnmClearTwampResponderCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenAOSnmClearTwampResponderCounters_Type.__name__ = "Integer32"
_AdGenAOSnmClearTwampResponderCounters_Object = MibTableColumn
adGenAOSnmClearTwampResponderCounters = _AdGenAOSnmClearTwampResponderCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 12, 1, 7),
    _AdGenAOSnmClearTwampResponderCounters_Type()
)
adGenAOSnmClearTwampResponderCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmClearTwampResponderCounters.setStatus("current")
_AdGenAOSnmCfgIEProbeTable_Object = MibTable
adGenAOSnmCfgIEProbeTable = _AdGenAOSnmCfgIEProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 13)
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgIEProbeTable.setStatus("current")
_AdGenAOSnmCfgIEProbeEntry_Object = MibTableRow
adGenAOSnmCfgIEProbeEntry = _AdGenAOSnmCfgIEProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 13, 1)
)
adGenAOSnmCfgIEProbeEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgIEProbeEntry.setStatus("current")


class _AdGenAOSnmCfgIEName_Type(OctetString):
    """Custom type adGenAOSnmCfgIEName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmCfgIEName_Type.__name__ = "OctetString"
_AdGenAOSnmCfgIEName_Object = MibTableColumn
adGenAOSnmCfgIEName = _AdGenAOSnmCfgIEName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 13, 1, 1),
    _AdGenAOSnmCfgIEName_Type()
)
adGenAOSnmCfgIEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmCfgIEName.setStatus("current")
_AdGenAOSnmIEDestHostname_Type = DisplayString
_AdGenAOSnmIEDestHostname_Object = MibTableColumn
adGenAOSnmIEDestHostname = _AdGenAOSnmIEDestHostname_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 13, 1, 2),
    _AdGenAOSnmIEDestHostname_Type()
)
adGenAOSnmIEDestHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmIEDestHostname.setStatus("current")
_AdGenAOSnmIESrcIP_Type = IpAddress
_AdGenAOSnmIESrcIP_Object = MibTableColumn
adGenAOSnmIESrcIP = _AdGenAOSnmIESrcIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 13, 1, 3),
    _AdGenAOSnmIESrcIP_Type()
)
adGenAOSnmIESrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmIESrcIP.setStatus("current")


class _AdGenAOSnmIEPacketLength_Type(Integer32):
    """Custom type adGenAOSnmIEPacketLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1462),
    )


_AdGenAOSnmIEPacketLength_Type.__name__ = "Integer32"
_AdGenAOSnmIEPacketLength_Object = MibTableColumn
adGenAOSnmIEPacketLength = _AdGenAOSnmIEPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 13, 1, 4),
    _AdGenAOSnmIEPacketLength_Type()
)
adGenAOSnmIEPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmIEPacketLength.setStatus("current")


class _AdGenAOSnmIEPacketPattern_Type(OctetString):
    """Custom type adGenAOSnmIEPacketPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_AdGenAOSnmIEPacketPattern_Type.__name__ = "OctetString"
_AdGenAOSnmIEPacketPattern_Object = MibTableColumn
adGenAOSnmIEPacketPattern = _AdGenAOSnmIEPacketPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 13, 1, 5),
    _AdGenAOSnmIEPacketPattern_Type()
)
adGenAOSnmIEPacketPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSnmIEPacketPattern.setStatus("current")
_AdGenAOSnmTrackTable_Object = MibTable
adGenAOSnmTrackTable = _AdGenAOSnmTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 14)
)
if mibBuilder.loadTexts:
    adGenAOSnmTrackTable.setStatus("current")
_AdGenAOSnmTrackEntry_Object = MibTableRow
adGenAOSnmTrackEntry = _AdGenAOSnmTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 14, 1)
)
adGenAOSnmTrackEntry.setIndexNames(
    (0, "ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSnmTrackEntry.setStatus("current")


class _AdGenAOSnmTrackIndex_Type(Integer32):
    """Custom type adGenAOSnmTrackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdGenAOSnmTrackIndex_Type.__name__ = "Integer32"
_AdGenAOSnmTrackIndex_Object = MibTableColumn
adGenAOSnmTrackIndex = _AdGenAOSnmTrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 14, 1, 1),
    _AdGenAOSnmTrackIndex_Type()
)
adGenAOSnmTrackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTrackIndex.setStatus("current")


class _AdGenAOSnmTrackName_Type(OctetString):
    """Custom type adGenAOSnmTrackName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenAOSnmTrackName_Type.__name__ = "OctetString"
_AdGenAOSnmTrackName_Object = MibTableColumn
adGenAOSnmTrackName = _AdGenAOSnmTrackName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 14, 1, 2),
    _AdGenAOSnmTrackName_Type()
)
adGenAOSnmTrackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSnmTrackName.setStatus("current")
_AdGenAOSnmConformance_ObjectIdentity = ObjectIdentity
adGenAOSnmConformance = _AdGenAOSnmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7)
)
_AdGenAOSnmGroups_ObjectIdentity = ObjectIdentity
adGenAOSnmGroups = _AdGenAOSnmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1)
)
_AdGenAOSnmCompliances_ObjectIdentity = ObjectIdentity
adGenAOSnmCompliances = _AdGenAOSnmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 2)
)

# Managed Objects groups

adGenAOSnmProbeTableNextIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 1)
)
adGenAOSnmProbeTableNextIndexGroup.setObjects(
    ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmProbeTableNextIndex")
)
if mibBuilder.loadTexts:
    adGenAOSnmProbeTableNextIndexGroup.setStatus("current")

adGenAOSnmProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 2)
)
adGenAOSnmProbeGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIndex"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmName"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmType"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmRowStatus"))
)
if mibBuilder.loadTexts:
    adGenAOSnmProbeGroup.setStatus("current")

adGenAOSnmConfigProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 3)
)
adGenAOSnmConfigProbeGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmCfgName"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmAdminStatus"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmPollPeriod"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTimeoutPeriod"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmToleranceMode"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmFailTolerance"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmPassTolerance"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmToleranceTestSize"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmClearCounters"))
)
if mibBuilder.loadTexts:
    adGenAOSnmConfigProbeGroup.setStatus("current")

adGenAOSnmProbeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 4)
)
adGenAOSnmProbeStatusGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmStatusName"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTestStatus"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTestsRun"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTestsFailed"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmStatsToleranceTestSize"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmStatsToleranceTestValue"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTimeSinceLastStatusChange"))
)
if mibBuilder.loadTexts:
    adGenAOSnmProbeStatusGroup.setStatus("current")

adGenAOSnmCfgTwampProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 5)
)
adGenAOSnmCfgTwampProbeGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmCfgTwName"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDestHostname"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDestPort"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwSrcIP"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwSrcPort"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDscp"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwPaddingLen"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwPaddingFormat"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwPaddingPattern"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDataPadType"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwPktSendCnt"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwSendScheduleType"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwSendScheduleValue"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsInMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsInAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsInMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsInMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsInAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsInMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsOutMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsOutAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsOutMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsOutMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsOutAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsOutMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsRtMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsRtAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsRtMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsRtMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsRtAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpdvAbsRtMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwPktRtLossFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwPktRtLossPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwHistoryDepth"))
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgTwampProbeGroup.setStatus("current")

adGenAOSnmTwampHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 6)
)
adGenAOSnmTwampHistoryGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwSeqNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwHistoryName"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwStartTime"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwEndTime"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwLocalSyncState"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwLocalClkErr"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwRemoteSyncState"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwRemoteClkErr"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwLossRoundTrip"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwDelayRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvPosRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvNegRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwIpvAbsRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwPktSentCount"))
)
if mibBuilder.loadTexts:
    adGenAOSnmTwampHistoryGroup.setStatus("current")

adGenAOSnmCfgICMPTSProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 7)
)
adGenAOSnmCfgICMPTSProbeGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmCfgICMPTSName"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDestHostname"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSSrcIP"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDscp"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSPaddingLen"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSPaddingFormat"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSPaddingPattern"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDataPadType"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSPktSendCnt"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSSendScheduleType"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSSendScheduleValue"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsInMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsInAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsInMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsInMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsInAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsInMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsOutMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsOutAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsOutMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsOutMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsOutAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsOutMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsRtMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsRtAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsRtMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsRtMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsRtAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpdvAbsRtMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtMinFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtAvgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtMaxFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtMinPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtAvgPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtMaxPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSPktRtLossFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSPktRtLossPass"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSHistoryDepth"))
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgICMPTSProbeGroup.setStatus("current")

adGenAOSnmICMPTSHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 8)
)
adGenAOSnmICMPTSHistoryGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSSeqNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSHistoryName"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSStartTime"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSEndTime"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSLossRoundTrip"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSDelayRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvPosRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvNegRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsInMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsInMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsInSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsInSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsInNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsOutMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsOutMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsOutSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsOutSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsOutNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsRtMin"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsRtMax"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsRtSum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsRtSum2"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSIpvAbsRtNum"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSPktSentCount"))
)
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSHistoryGroup.setStatus("current")

adGenAOSnmICMPTSResponderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 9)
)
adGenAOSnmICMPTSResponderGroup.setObjects(
    ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSResponder")
)
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSResponderGroup.setStatus("current")

adGenAOSnmTWAMPResponderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 10)
)
adGenAOSnmTWAMPResponderGroup.setObjects(
    ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTWAMPResponder")
)
if mibBuilder.loadTexts:
    adGenAOSnmTWAMPResponderGroup.setStatus("current")

adGenAOSnmICMPTSResponderStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 11)
)
adGenAOSnmICMPTSResponderStatsGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSResponderStatsIndex"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSResponderPacketsReceived"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmICMPTSResponderPacketsSent"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmClearICMPTSResponderCounters"))
)
if mibBuilder.loadTexts:
    adGenAOSnmICMPTSResponderStatsGroup.setStatus("current")

adGenAOSnmTwampResponderStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 12)
)
adGenAOSnmTwampResponderStatsGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwampResponderStatsIndex"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwampResponderPacketsReceived"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwampResponderPacketsSent"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwampResponderSessionClosed"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwampResponderSessionOpened"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTwampResponderSessionRejected"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmClearTwampResponderCounters"))
)
if mibBuilder.loadTexts:
    adGenAOSnmTwampResponderStatsGroup.setStatus("current")

adGenAOSnmCfgIEProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 13)
)
adGenAOSnmCfgIEProbeGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmCfgIEName"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIEDestHostname"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIESrcIP"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIEPacketLength"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmIEPacketPattern"))
)
if mibBuilder.loadTexts:
    adGenAOSnmCfgIEProbeGroup.setStatus("current")

adGenAOSnmTrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 14)
)
adGenAOSnmTrackGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackIndex"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackName"))
)
if mibBuilder.loadTexts:
    adGenAOSnmTrackGroup.setStatus("current")


# Notification objects

adGenAOSnmTrackStateChgFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 0, 1)
)
adGenAOSnmTrackStateChgFail.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackIndex"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackName"))
)
if mibBuilder.loadTexts:
    adGenAOSnmTrackStateChgFail.setStatus(
        "current"
    )

adGenAOSnmTrackStateChgPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 2, 0, 2)
)
adGenAOSnmTrackStateChgPass.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackIndex"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackName"))
)
if mibBuilder.loadTexts:
    adGenAOSnmTrackStateChgPass.setStatus(
        "current"
    )


# Notifications groups

adGenAOSnmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 1, 15)
)
adGenAOSnmNotificationGroup.setObjects(
      *(("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackStateChgFail"),
        ("ADTRAN-AOS-NETWORKMONITOR", "adGenAOSnmTrackStateChgPass"))
)
if mibBuilder.loadTexts:
    adGenAOSnmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSnmFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSnmFullCompliance.setStatus(
        "current"
    )

adGenAOSnmReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 7, 2, 2)
)
if mibBuilder.loadTexts:
    adGenAOSnmReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-NETWORKMONITOR",
    **{"adGenAOSNetMon": adGenAOSNetMon,
       "adGenAOSnmTrackTraps": adGenAOSnmTrackTraps,
       "adGenAOSnmTrackStateChgFail": adGenAOSnmTrackStateChgFail,
       "adGenAOSnmTrackStateChgPass": adGenAOSnmTrackStateChgPass,
       "adGenAOSnmProbeTableNextIndex": adGenAOSnmProbeTableNextIndex,
       "adGenAOSnmProbeTable": adGenAOSnmProbeTable,
       "adGenAOSnmProbeEntry": adGenAOSnmProbeEntry,
       "adGenAOSnmIndex": adGenAOSnmIndex,
       "adGenAOSnmName": adGenAOSnmName,
       "adGenAOSnmType": adGenAOSnmType,
       "adGenAOSnmRowStatus": adGenAOSnmRowStatus,
       "adGenAOSnmConfigProbeTable": adGenAOSnmConfigProbeTable,
       "adGenAOSnmConfigProbeEntry": adGenAOSnmConfigProbeEntry,
       "adGenAOSnmCfgName": adGenAOSnmCfgName,
       "adGenAOSnmAdminStatus": adGenAOSnmAdminStatus,
       "adGenAOSnmPollPeriod": adGenAOSnmPollPeriod,
       "adGenAOSnmTimeoutPeriod": adGenAOSnmTimeoutPeriod,
       "adGenAOSnmToleranceMode": adGenAOSnmToleranceMode,
       "adGenAOSnmFailTolerance": adGenAOSnmFailTolerance,
       "adGenAOSnmPassTolerance": adGenAOSnmPassTolerance,
       "adGenAOSnmToleranceTestSize": adGenAOSnmToleranceTestSize,
       "adGenAOSnmClearCounters": adGenAOSnmClearCounters,
       "adGenAOSnmProbeStatusTable": adGenAOSnmProbeStatusTable,
       "adGenAOSnmProbeStatusEntry": adGenAOSnmProbeStatusEntry,
       "adGenAOSnmStatusName": adGenAOSnmStatusName,
       "adGenAOSnmTestStatus": adGenAOSnmTestStatus,
       "adGenAOSnmTestsRun": adGenAOSnmTestsRun,
       "adGenAOSnmTestsFailed": adGenAOSnmTestsFailed,
       "adGenAOSnmStatsToleranceTestSize": adGenAOSnmStatsToleranceTestSize,
       "adGenAOSnmStatsToleranceTestValue": adGenAOSnmStatsToleranceTestValue,
       "adGenAOSnmTimeSinceLastStatusChange": adGenAOSnmTimeSinceLastStatusChange,
       "adGenAOSnmCfgTwampProbeTable": adGenAOSnmCfgTwampProbeTable,
       "adGenAOSnmCfgTwampProbeEntry": adGenAOSnmCfgTwampProbeEntry,
       "adGenAOSnmCfgTwName": adGenAOSnmCfgTwName,
       "adGenAOSnmTwDestHostname": adGenAOSnmTwDestHostname,
       "adGenAOSnmTwDestPort": adGenAOSnmTwDestPort,
       "adGenAOSnmTwSrcIP": adGenAOSnmTwSrcIP,
       "adGenAOSnmTwSrcPort": adGenAOSnmTwSrcPort,
       "adGenAOSnmTwDscp": adGenAOSnmTwDscp,
       "adGenAOSnmTwPaddingLen": adGenAOSnmTwPaddingLen,
       "adGenAOSnmTwPaddingFormat": adGenAOSnmTwPaddingFormat,
       "adGenAOSnmTwPaddingPattern": adGenAOSnmTwPaddingPattern,
       "adGenAOSnmTwDataPadType": adGenAOSnmTwDataPadType,
       "adGenAOSnmTwPktSendCnt": adGenAOSnmTwPktSendCnt,
       "adGenAOSnmTwSendScheduleType": adGenAOSnmTwSendScheduleType,
       "adGenAOSnmTwSendScheduleValue": adGenAOSnmTwSendScheduleValue,
       "adGenAOSnmTwIpdvAbsInMinFail": adGenAOSnmTwIpdvAbsInMinFail,
       "adGenAOSnmTwIpdvAbsInAvgFail": adGenAOSnmTwIpdvAbsInAvgFail,
       "adGenAOSnmTwIpdvAbsInMaxFail": adGenAOSnmTwIpdvAbsInMaxFail,
       "adGenAOSnmTwIpdvAbsInMinPass": adGenAOSnmTwIpdvAbsInMinPass,
       "adGenAOSnmTwIpdvAbsInAvgPass": adGenAOSnmTwIpdvAbsInAvgPass,
       "adGenAOSnmTwIpdvAbsInMaxPass": adGenAOSnmTwIpdvAbsInMaxPass,
       "adGenAOSnmTwIpdvAbsOutMinFail": adGenAOSnmTwIpdvAbsOutMinFail,
       "adGenAOSnmTwIpdvAbsOutAvgFail": adGenAOSnmTwIpdvAbsOutAvgFail,
       "adGenAOSnmTwIpdvAbsOutMaxFail": adGenAOSnmTwIpdvAbsOutMaxFail,
       "adGenAOSnmTwIpdvAbsOutMinPass": adGenAOSnmTwIpdvAbsOutMinPass,
       "adGenAOSnmTwIpdvAbsOutAvgPass": adGenAOSnmTwIpdvAbsOutAvgPass,
       "adGenAOSnmTwIpdvAbsOutMaxPass": adGenAOSnmTwIpdvAbsOutMaxPass,
       "adGenAOSnmTwIpdvAbsRtMinFail": adGenAOSnmTwIpdvAbsRtMinFail,
       "adGenAOSnmTwIpdvAbsRtAvgFail": adGenAOSnmTwIpdvAbsRtAvgFail,
       "adGenAOSnmTwIpdvAbsRtMaxFail": adGenAOSnmTwIpdvAbsRtMaxFail,
       "adGenAOSnmTwIpdvAbsRtMinPass": adGenAOSnmTwIpdvAbsRtMinPass,
       "adGenAOSnmTwIpdvAbsRtAvgPass": adGenAOSnmTwIpdvAbsRtAvgPass,
       "adGenAOSnmTwIpdvAbsRtMaxPass": adGenAOSnmTwIpdvAbsRtMaxPass,
       "adGenAOSnmTwDelayInMinFail": adGenAOSnmTwDelayInMinFail,
       "adGenAOSnmTwDelayInAvgFail": adGenAOSnmTwDelayInAvgFail,
       "adGenAOSnmTwDelayInMaxFail": adGenAOSnmTwDelayInMaxFail,
       "adGenAOSnmTwDelayInMinPass": adGenAOSnmTwDelayInMinPass,
       "adGenAOSnmTwDelayInAvgPass": adGenAOSnmTwDelayInAvgPass,
       "adGenAOSnmTwDelayInMaxPass": adGenAOSnmTwDelayInMaxPass,
       "adGenAOSnmTwDelayOutMinFail": adGenAOSnmTwDelayOutMinFail,
       "adGenAOSnmTwDelayOutAvgFail": adGenAOSnmTwDelayOutAvgFail,
       "adGenAOSnmTwDelayOutMaxFail": adGenAOSnmTwDelayOutMaxFail,
       "adGenAOSnmTwDelayOutMinPass": adGenAOSnmTwDelayOutMinPass,
       "adGenAOSnmTwDelayOutAvgPass": adGenAOSnmTwDelayOutAvgPass,
       "adGenAOSnmTwDelayOutMaxPass": adGenAOSnmTwDelayOutMaxPass,
       "adGenAOSnmTwDelayRtMinFail": adGenAOSnmTwDelayRtMinFail,
       "adGenAOSnmTwDelayRtAvgFail": adGenAOSnmTwDelayRtAvgFail,
       "adGenAOSnmTwDelayRtMaxFail": adGenAOSnmTwDelayRtMaxFail,
       "adGenAOSnmTwDelayRtMinPass": adGenAOSnmTwDelayRtMinPass,
       "adGenAOSnmTwDelayRtAvgPass": adGenAOSnmTwDelayRtAvgPass,
       "adGenAOSnmTwDelayRtMaxPass": adGenAOSnmTwDelayRtMaxPass,
       "adGenAOSnmTwPktRtLossFail": adGenAOSnmTwPktRtLossFail,
       "adGenAOSnmTwPktRtLossPass": adGenAOSnmTwPktRtLossPass,
       "adGenAOSnmTwHistoryDepth": adGenAOSnmTwHistoryDepth,
       "adGenAOSnmTwampHistoryTable": adGenAOSnmTwampHistoryTable,
       "adGenAOSnmTwampHistoryEntry": adGenAOSnmTwampHistoryEntry,
       "adGenAOSnmTwSeqNum": adGenAOSnmTwSeqNum,
       "adGenAOSnmTwHistoryName": adGenAOSnmTwHistoryName,
       "adGenAOSnmTwStartTime": adGenAOSnmTwStartTime,
       "adGenAOSnmTwEndTime": adGenAOSnmTwEndTime,
       "adGenAOSnmTwLocalSyncState": adGenAOSnmTwLocalSyncState,
       "adGenAOSnmTwLocalClkErr": adGenAOSnmTwLocalClkErr,
       "adGenAOSnmTwRemoteSyncState": adGenAOSnmTwRemoteSyncState,
       "adGenAOSnmTwRemoteClkErr": adGenAOSnmTwRemoteClkErr,
       "adGenAOSnmTwDelayInMin": adGenAOSnmTwDelayInMin,
       "adGenAOSnmTwDelayInMax": adGenAOSnmTwDelayInMax,
       "adGenAOSnmTwDelayOutMin": adGenAOSnmTwDelayOutMin,
       "adGenAOSnmTwDelayOutMax": adGenAOSnmTwDelayOutMax,
       "adGenAOSnmTwDelayRtMin": adGenAOSnmTwDelayRtMin,
       "adGenAOSnmTwDelayRtMax": adGenAOSnmTwDelayRtMax,
       "adGenAOSnmTwLossRoundTrip": adGenAOSnmTwLossRoundTrip,
       "adGenAOSnmTwDelayOutSum": adGenAOSnmTwDelayOutSum,
       "adGenAOSnmTwDelayOutSum2": adGenAOSnmTwDelayOutSum2,
       "adGenAOSnmTwDelayOutNum": adGenAOSnmTwDelayOutNum,
       "adGenAOSnmTwDelayInSum": adGenAOSnmTwDelayInSum,
       "adGenAOSnmTwDelayInSum2": adGenAOSnmTwDelayInSum2,
       "adGenAOSnmTwDelayInNum": adGenAOSnmTwDelayInNum,
       "adGenAOSnmTwDelayRtSum": adGenAOSnmTwDelayRtSum,
       "adGenAOSnmTwDelayRtSum2": adGenAOSnmTwDelayRtSum2,
       "adGenAOSnmTwDelayRtNum": adGenAOSnmTwDelayRtNum,
       "adGenAOSnmTwIpvPosInMin": adGenAOSnmTwIpvPosInMin,
       "adGenAOSnmTwIpvPosInMax": adGenAOSnmTwIpvPosInMax,
       "adGenAOSnmTwIpvPosInSum": adGenAOSnmTwIpvPosInSum,
       "adGenAOSnmTwIpvPosInSum2": adGenAOSnmTwIpvPosInSum2,
       "adGenAOSnmTwIpvPosInNum": adGenAOSnmTwIpvPosInNum,
       "adGenAOSnmTwIpvPosOutMin": adGenAOSnmTwIpvPosOutMin,
       "adGenAOSnmTwIpvPosOutMax": adGenAOSnmTwIpvPosOutMax,
       "adGenAOSnmTwIpvPosOutSum": adGenAOSnmTwIpvPosOutSum,
       "adGenAOSnmTwIpvPosOutSum2": adGenAOSnmTwIpvPosOutSum2,
       "adGenAOSnmTwIpvPosOutNum": adGenAOSnmTwIpvPosOutNum,
       "adGenAOSnmTwIpvPosRtMin": adGenAOSnmTwIpvPosRtMin,
       "adGenAOSnmTwIpvPosRtMax": adGenAOSnmTwIpvPosRtMax,
       "adGenAOSnmTwIpvPosRtSum": adGenAOSnmTwIpvPosRtSum,
       "adGenAOSnmTwIpvPosRtSum2": adGenAOSnmTwIpvPosRtSum2,
       "adGenAOSnmTwIpvPosRtNum": adGenAOSnmTwIpvPosRtNum,
       "adGenAOSnmTwIpvNegInMin": adGenAOSnmTwIpvNegInMin,
       "adGenAOSnmTwIpvNegInMax": adGenAOSnmTwIpvNegInMax,
       "adGenAOSnmTwIpvNegInSum": adGenAOSnmTwIpvNegInSum,
       "adGenAOSnmTwIpvNegInSum2": adGenAOSnmTwIpvNegInSum2,
       "adGenAOSnmTwIpvNegInNum": adGenAOSnmTwIpvNegInNum,
       "adGenAOSnmTwIpvNegOutMin": adGenAOSnmTwIpvNegOutMin,
       "adGenAOSnmTwIpvNegOutMax": adGenAOSnmTwIpvNegOutMax,
       "adGenAOSnmTwIpvNegOutSum": adGenAOSnmTwIpvNegOutSum,
       "adGenAOSnmTwIpvNegOutSum2": adGenAOSnmTwIpvNegOutSum2,
       "adGenAOSnmTwIpvNegOutNum": adGenAOSnmTwIpvNegOutNum,
       "adGenAOSnmTwIpvNegRtMin": adGenAOSnmTwIpvNegRtMin,
       "adGenAOSnmTwIpvNegRtMax": adGenAOSnmTwIpvNegRtMax,
       "adGenAOSnmTwIpvNegRtSum": adGenAOSnmTwIpvNegRtSum,
       "adGenAOSnmTwIpvNegRtSum2": adGenAOSnmTwIpvNegRtSum2,
       "adGenAOSnmTwIpvNegRtNum": adGenAOSnmTwIpvNegRtNum,
       "adGenAOSnmTwIpvAbsInMin": adGenAOSnmTwIpvAbsInMin,
       "adGenAOSnmTwIpvAbsInMax": adGenAOSnmTwIpvAbsInMax,
       "adGenAOSnmTwIpvAbsInSum": adGenAOSnmTwIpvAbsInSum,
       "adGenAOSnmTwIpvAbsInSum2": adGenAOSnmTwIpvAbsInSum2,
       "adGenAOSnmTwIpvAbsInNum": adGenAOSnmTwIpvAbsInNum,
       "adGenAOSnmTwIpvAbsOutMin": adGenAOSnmTwIpvAbsOutMin,
       "adGenAOSnmTwIpvAbsOutMax": adGenAOSnmTwIpvAbsOutMax,
       "adGenAOSnmTwIpvAbsOutSum": adGenAOSnmTwIpvAbsOutSum,
       "adGenAOSnmTwIpvAbsOutSum2": adGenAOSnmTwIpvAbsOutSum2,
       "adGenAOSnmTwIpvAbsOutNum": adGenAOSnmTwIpvAbsOutNum,
       "adGenAOSnmTwIpvAbsRtMin": adGenAOSnmTwIpvAbsRtMin,
       "adGenAOSnmTwIpvAbsRtMax": adGenAOSnmTwIpvAbsRtMax,
       "adGenAOSnmTwIpvAbsRtSum": adGenAOSnmTwIpvAbsRtSum,
       "adGenAOSnmTwIpvAbsRtSum2": adGenAOSnmTwIpvAbsRtSum2,
       "adGenAOSnmTwIpvAbsRtNum": adGenAOSnmTwIpvAbsRtNum,
       "adGenAOSnmTwPktSentCount": adGenAOSnmTwPktSentCount,
       "adGenAOSnmCfgICMPTSProbeTable": adGenAOSnmCfgICMPTSProbeTable,
       "adGenAOSnmCfgICMPTSProbeEntry": adGenAOSnmCfgICMPTSProbeEntry,
       "adGenAOSnmCfgICMPTSName": adGenAOSnmCfgICMPTSName,
       "adGenAOSnmICMPTSDestHostname": adGenAOSnmICMPTSDestHostname,
       "adGenAOSnmICMPTSSrcIP": adGenAOSnmICMPTSSrcIP,
       "adGenAOSnmICMPTSDscp": adGenAOSnmICMPTSDscp,
       "adGenAOSnmICMPTSPaddingLen": adGenAOSnmICMPTSPaddingLen,
       "adGenAOSnmICMPTSPaddingFormat": adGenAOSnmICMPTSPaddingFormat,
       "adGenAOSnmICMPTSPaddingPattern": adGenAOSnmICMPTSPaddingPattern,
       "adGenAOSnmICMPTSDataPadType": adGenAOSnmICMPTSDataPadType,
       "adGenAOSnmICMPTSPktSendCnt": adGenAOSnmICMPTSPktSendCnt,
       "adGenAOSnmICMPTSSendScheduleType": adGenAOSnmICMPTSSendScheduleType,
       "adGenAOSnmICMPTSSendScheduleValue": adGenAOSnmICMPTSSendScheduleValue,
       "adGenAOSnmICMPTSIpdvAbsInMinFail": adGenAOSnmICMPTSIpdvAbsInMinFail,
       "adGenAOSnmICMPTSIpdvAbsInAvgFail": adGenAOSnmICMPTSIpdvAbsInAvgFail,
       "adGenAOSnmICMPTSIpdvAbsInMaxFail": adGenAOSnmICMPTSIpdvAbsInMaxFail,
       "adGenAOSnmICMPTSIpdvAbsInMinPass": adGenAOSnmICMPTSIpdvAbsInMinPass,
       "adGenAOSnmICMPTSIpdvAbsInAvgPass": adGenAOSnmICMPTSIpdvAbsInAvgPass,
       "adGenAOSnmICMPTSIpdvAbsInMaxPass": adGenAOSnmICMPTSIpdvAbsInMaxPass,
       "adGenAOSnmICMPTSIpdvAbsOutMinFail": adGenAOSnmICMPTSIpdvAbsOutMinFail,
       "adGenAOSnmICMPTSIpdvAbsOutAvgFail": adGenAOSnmICMPTSIpdvAbsOutAvgFail,
       "adGenAOSnmICMPTSIpdvAbsOutMaxFail": adGenAOSnmICMPTSIpdvAbsOutMaxFail,
       "adGenAOSnmICMPTSIpdvAbsOutMinPass": adGenAOSnmICMPTSIpdvAbsOutMinPass,
       "adGenAOSnmICMPTSIpdvAbsOutAvgPass": adGenAOSnmICMPTSIpdvAbsOutAvgPass,
       "adGenAOSnmICMPTSIpdvAbsOutMaxPass": adGenAOSnmICMPTSIpdvAbsOutMaxPass,
       "adGenAOSnmICMPTSIpdvAbsRtMinFail": adGenAOSnmICMPTSIpdvAbsRtMinFail,
       "adGenAOSnmICMPTSIpdvAbsRtAvgFail": adGenAOSnmICMPTSIpdvAbsRtAvgFail,
       "adGenAOSnmICMPTSIpdvAbsRtMaxFail": adGenAOSnmICMPTSIpdvAbsRtMaxFail,
       "adGenAOSnmICMPTSIpdvAbsRtMinPass": adGenAOSnmICMPTSIpdvAbsRtMinPass,
       "adGenAOSnmICMPTSIpdvAbsRtAvgPass": adGenAOSnmICMPTSIpdvAbsRtAvgPass,
       "adGenAOSnmICMPTSIpdvAbsRtMaxPass": adGenAOSnmICMPTSIpdvAbsRtMaxPass,
       "adGenAOSnmICMPTSDelayInMinFail": adGenAOSnmICMPTSDelayInMinFail,
       "adGenAOSnmICMPTSDelayInAvgFail": adGenAOSnmICMPTSDelayInAvgFail,
       "adGenAOSnmICMPTSDelayInMaxFail": adGenAOSnmICMPTSDelayInMaxFail,
       "adGenAOSnmICMPTSDelayInMinPass": adGenAOSnmICMPTSDelayInMinPass,
       "adGenAOSnmICMPTSDelayInAvgPass": adGenAOSnmICMPTSDelayInAvgPass,
       "adGenAOSnmICMPTSDelayInMaxPass": adGenAOSnmICMPTSDelayInMaxPass,
       "adGenAOSnmICMPTSDelayOutMinFail": adGenAOSnmICMPTSDelayOutMinFail,
       "adGenAOSnmICMPTSDelayOutAvgFail": adGenAOSnmICMPTSDelayOutAvgFail,
       "adGenAOSnmICMPTSDelayOutMaxFail": adGenAOSnmICMPTSDelayOutMaxFail,
       "adGenAOSnmICMPTSDelayOutMinPass": adGenAOSnmICMPTSDelayOutMinPass,
       "adGenAOSnmICMPTSDelayOutAvgPass": adGenAOSnmICMPTSDelayOutAvgPass,
       "adGenAOSnmICMPTSDelayOutMaxPass": adGenAOSnmICMPTSDelayOutMaxPass,
       "adGenAOSnmICMPTSDelayRtMinFail": adGenAOSnmICMPTSDelayRtMinFail,
       "adGenAOSnmICMPTSDelayRtAvgFail": adGenAOSnmICMPTSDelayRtAvgFail,
       "adGenAOSnmICMPTSDelayRtMaxFail": adGenAOSnmICMPTSDelayRtMaxFail,
       "adGenAOSnmICMPTSDelayRtMinPass": adGenAOSnmICMPTSDelayRtMinPass,
       "adGenAOSnmICMPTSDelayRtAvgPass": adGenAOSnmICMPTSDelayRtAvgPass,
       "adGenAOSnmICMPTSDelayRtMaxPass": adGenAOSnmICMPTSDelayRtMaxPass,
       "adGenAOSnmICMPTSPktRtLossFail": adGenAOSnmICMPTSPktRtLossFail,
       "adGenAOSnmICMPTSPktRtLossPass": adGenAOSnmICMPTSPktRtLossPass,
       "adGenAOSnmICMPTSHistoryDepth": adGenAOSnmICMPTSHistoryDepth,
       "adGenAOSnmICMPTSHistoryTable": adGenAOSnmICMPTSHistoryTable,
       "adGenAOSnmICMPTSHistoryEntry": adGenAOSnmICMPTSHistoryEntry,
       "adGenAOSnmICMPTSSeqNum": adGenAOSnmICMPTSSeqNum,
       "adGenAOSnmICMPTSHistoryName": adGenAOSnmICMPTSHistoryName,
       "adGenAOSnmICMPTSStartTime": adGenAOSnmICMPTSStartTime,
       "adGenAOSnmICMPTSEndTime": adGenAOSnmICMPTSEndTime,
       "adGenAOSnmICMPTSDelayInMin": adGenAOSnmICMPTSDelayInMin,
       "adGenAOSnmICMPTSDelayInMax": adGenAOSnmICMPTSDelayInMax,
       "adGenAOSnmICMPTSDelayOutMin": adGenAOSnmICMPTSDelayOutMin,
       "adGenAOSnmICMPTSDelayOutMax": adGenAOSnmICMPTSDelayOutMax,
       "adGenAOSnmICMPTSDelayRtMin": adGenAOSnmICMPTSDelayRtMin,
       "adGenAOSnmICMPTSDelayRtMax": adGenAOSnmICMPTSDelayRtMax,
       "adGenAOSnmICMPTSLossRoundTrip": adGenAOSnmICMPTSLossRoundTrip,
       "adGenAOSnmICMPTSDelayOutSum": adGenAOSnmICMPTSDelayOutSum,
       "adGenAOSnmICMPTSDelayOutSum2": adGenAOSnmICMPTSDelayOutSum2,
       "adGenAOSnmICMPTSDelayOutNum": adGenAOSnmICMPTSDelayOutNum,
       "adGenAOSnmICMPTSDelayInSum": adGenAOSnmICMPTSDelayInSum,
       "adGenAOSnmICMPTSDelayInSum2": adGenAOSnmICMPTSDelayInSum2,
       "adGenAOSnmICMPTSDelayInNum": adGenAOSnmICMPTSDelayInNum,
       "adGenAOSnmICMPTSDelayRtSum": adGenAOSnmICMPTSDelayRtSum,
       "adGenAOSnmICMPTSDelayRtSum2": adGenAOSnmICMPTSDelayRtSum2,
       "adGenAOSnmICMPTSDelayRtNum": adGenAOSnmICMPTSDelayRtNum,
       "adGenAOSnmICMPTSIpvPosInMin": adGenAOSnmICMPTSIpvPosInMin,
       "adGenAOSnmICMPTSIpvPosInMax": adGenAOSnmICMPTSIpvPosInMax,
       "adGenAOSnmICMPTSIpvPosInSum": adGenAOSnmICMPTSIpvPosInSum,
       "adGenAOSnmICMPTSIpvPosInSum2": adGenAOSnmICMPTSIpvPosInSum2,
       "adGenAOSnmICMPTSIpvPosInNum": adGenAOSnmICMPTSIpvPosInNum,
       "adGenAOSnmICMPTSIpvPosOutMin": adGenAOSnmICMPTSIpvPosOutMin,
       "adGenAOSnmICMPTSIpvPosOutMax": adGenAOSnmICMPTSIpvPosOutMax,
       "adGenAOSnmICMPTSIpvPosOutSum": adGenAOSnmICMPTSIpvPosOutSum,
       "adGenAOSnmICMPTSIpvPosOutSum2": adGenAOSnmICMPTSIpvPosOutSum2,
       "adGenAOSnmICMPTSIpvPosOutNum": adGenAOSnmICMPTSIpvPosOutNum,
       "adGenAOSnmICMPTSIpvPosRtMin": adGenAOSnmICMPTSIpvPosRtMin,
       "adGenAOSnmICMPTSIpvPosRtMax": adGenAOSnmICMPTSIpvPosRtMax,
       "adGenAOSnmICMPTSIpvPosRtSum": adGenAOSnmICMPTSIpvPosRtSum,
       "adGenAOSnmICMPTSIpvPosRtSum2": adGenAOSnmICMPTSIpvPosRtSum2,
       "adGenAOSnmICMPTSIpvPosRtNum": adGenAOSnmICMPTSIpvPosRtNum,
       "adGenAOSnmICMPTSIpvNegInMin": adGenAOSnmICMPTSIpvNegInMin,
       "adGenAOSnmICMPTSIpvNegInMax": adGenAOSnmICMPTSIpvNegInMax,
       "adGenAOSnmICMPTSIpvNegInSum": adGenAOSnmICMPTSIpvNegInSum,
       "adGenAOSnmICMPTSIpvNegInSum2": adGenAOSnmICMPTSIpvNegInSum2,
       "adGenAOSnmICMPTSIpvNegInNum": adGenAOSnmICMPTSIpvNegInNum,
       "adGenAOSnmICMPTSIpvNegOutMin": adGenAOSnmICMPTSIpvNegOutMin,
       "adGenAOSnmICMPTSIpvNegOutMax": adGenAOSnmICMPTSIpvNegOutMax,
       "adGenAOSnmICMPTSIpvNegOutSum": adGenAOSnmICMPTSIpvNegOutSum,
       "adGenAOSnmICMPTSIpvNegOutSum2": adGenAOSnmICMPTSIpvNegOutSum2,
       "adGenAOSnmICMPTSIpvNegOutNum": adGenAOSnmICMPTSIpvNegOutNum,
       "adGenAOSnmICMPTSIpvNegRtMin": adGenAOSnmICMPTSIpvNegRtMin,
       "adGenAOSnmICMPTSIpvNegRtMax": adGenAOSnmICMPTSIpvNegRtMax,
       "adGenAOSnmICMPTSIpvNegRtSum": adGenAOSnmICMPTSIpvNegRtSum,
       "adGenAOSnmICMPTSIpvNegRtSum2": adGenAOSnmICMPTSIpvNegRtSum2,
       "adGenAOSnmICMPTSIpvNegRtNum": adGenAOSnmICMPTSIpvNegRtNum,
       "adGenAOSnmICMPTSIpvAbsInMin": adGenAOSnmICMPTSIpvAbsInMin,
       "adGenAOSnmICMPTSIpvAbsInMax": adGenAOSnmICMPTSIpvAbsInMax,
       "adGenAOSnmICMPTSIpvAbsInSum": adGenAOSnmICMPTSIpvAbsInSum,
       "adGenAOSnmICMPTSIpvAbsInSum2": adGenAOSnmICMPTSIpvAbsInSum2,
       "adGenAOSnmICMPTSIpvAbsInNum": adGenAOSnmICMPTSIpvAbsInNum,
       "adGenAOSnmICMPTSIpvAbsOutMin": adGenAOSnmICMPTSIpvAbsOutMin,
       "adGenAOSnmICMPTSIpvAbsOutMax": adGenAOSnmICMPTSIpvAbsOutMax,
       "adGenAOSnmICMPTSIpvAbsOutSum": adGenAOSnmICMPTSIpvAbsOutSum,
       "adGenAOSnmICMPTSIpvAbsOutSum2": adGenAOSnmICMPTSIpvAbsOutSum2,
       "adGenAOSnmICMPTSIpvAbsOutNum": adGenAOSnmICMPTSIpvAbsOutNum,
       "adGenAOSnmICMPTSIpvAbsRtMin": adGenAOSnmICMPTSIpvAbsRtMin,
       "adGenAOSnmICMPTSIpvAbsRtMax": adGenAOSnmICMPTSIpvAbsRtMax,
       "adGenAOSnmICMPTSIpvAbsRtSum": adGenAOSnmICMPTSIpvAbsRtSum,
       "adGenAOSnmICMPTSIpvAbsRtSum2": adGenAOSnmICMPTSIpvAbsRtSum2,
       "adGenAOSnmICMPTSIpvAbsRtNum": adGenAOSnmICMPTSIpvAbsRtNum,
       "adGenAOSnmICMPTSPktSentCount": adGenAOSnmICMPTSPktSentCount,
       "adGenAOSnmICMPTSResponder": adGenAOSnmICMPTSResponder,
       "adGenAOSnmTWAMPResponder": adGenAOSnmTWAMPResponder,
       "adGenAOSnmICMPTSResponderStatsTable": adGenAOSnmICMPTSResponderStatsTable,
       "adGenAOSnmICMPTSResponderStatsEntry": adGenAOSnmICMPTSResponderStatsEntry,
       "adGenAOSnmICMPTSResponderStatsIndex": adGenAOSnmICMPTSResponderStatsIndex,
       "adGenAOSnmICMPTSResponderPacketsReceived": adGenAOSnmICMPTSResponderPacketsReceived,
       "adGenAOSnmICMPTSResponderPacketsSent": adGenAOSnmICMPTSResponderPacketsSent,
       "adGenAOSnmClearICMPTSResponderCounters": adGenAOSnmClearICMPTSResponderCounters,
       "adGenAOSnmTwampResponderStatsTable": adGenAOSnmTwampResponderStatsTable,
       "adGenAOSnmTwampResponderStatsEntry": adGenAOSnmTwampResponderStatsEntry,
       "adGenAOSnmTwampResponderStatsIndex": adGenAOSnmTwampResponderStatsIndex,
       "adGenAOSnmTwampResponderPacketsReceived": adGenAOSnmTwampResponderPacketsReceived,
       "adGenAOSnmTwampResponderPacketsSent": adGenAOSnmTwampResponderPacketsSent,
       "adGenAOSnmTwampResponderSessionClosed": adGenAOSnmTwampResponderSessionClosed,
       "adGenAOSnmTwampResponderSessionOpened": adGenAOSnmTwampResponderSessionOpened,
       "adGenAOSnmTwampResponderSessionRejected": adGenAOSnmTwampResponderSessionRejected,
       "adGenAOSnmClearTwampResponderCounters": adGenAOSnmClearTwampResponderCounters,
       "adGenAOSnmCfgIEProbeTable": adGenAOSnmCfgIEProbeTable,
       "adGenAOSnmCfgIEProbeEntry": adGenAOSnmCfgIEProbeEntry,
       "adGenAOSnmCfgIEName": adGenAOSnmCfgIEName,
       "adGenAOSnmIEDestHostname": adGenAOSnmIEDestHostname,
       "adGenAOSnmIESrcIP": adGenAOSnmIESrcIP,
       "adGenAOSnmIEPacketLength": adGenAOSnmIEPacketLength,
       "adGenAOSnmIEPacketPattern": adGenAOSnmIEPacketPattern,
       "adGenAOSnmTrackTable": adGenAOSnmTrackTable,
       "adGenAOSnmTrackEntry": adGenAOSnmTrackEntry,
       "adGenAOSnmTrackIndex": adGenAOSnmTrackIndex,
       "adGenAOSnmTrackName": adGenAOSnmTrackName,
       "adGenAOSnmConformance": adGenAOSnmConformance,
       "adGenAOSnmGroups": adGenAOSnmGroups,
       "adGenAOSnmProbeTableNextIndexGroup": adGenAOSnmProbeTableNextIndexGroup,
       "adGenAOSnmProbeGroup": adGenAOSnmProbeGroup,
       "adGenAOSnmConfigProbeGroup": adGenAOSnmConfigProbeGroup,
       "adGenAOSnmProbeStatusGroup": adGenAOSnmProbeStatusGroup,
       "adGenAOSnmCfgTwampProbeGroup": adGenAOSnmCfgTwampProbeGroup,
       "adGenAOSnmTwampHistoryGroup": adGenAOSnmTwampHistoryGroup,
       "adGenAOSnmCfgICMPTSProbeGroup": adGenAOSnmCfgICMPTSProbeGroup,
       "adGenAOSnmICMPTSHistoryGroup": adGenAOSnmICMPTSHistoryGroup,
       "adGenAOSnmICMPTSResponderGroup": adGenAOSnmICMPTSResponderGroup,
       "adGenAOSnmTWAMPResponderGroup": adGenAOSnmTWAMPResponderGroup,
       "adGenAOSnmICMPTSResponderStatsGroup": adGenAOSnmICMPTSResponderStatsGroup,
       "adGenAOSnmTwampResponderStatsGroup": adGenAOSnmTwampResponderStatsGroup,
       "adGenAOSnmCfgIEProbeGroup": adGenAOSnmCfgIEProbeGroup,
       "adGenAOSnmTrackGroup": adGenAOSnmTrackGroup,
       "adGenAOSnmNotificationGroup": adGenAOSnmNotificationGroup,
       "adGenAOSnmCompliances": adGenAOSnmCompliances,
       "adGenAOSnmFullCompliance": adGenAOSnmFullCompliance,
       "adGenAOSnmReadOnlyCompliance": adGenAOSnmReadOnlyCompliance,
       "adGenAOSNetMonMib": adGenAOSNetMonMib}
)
