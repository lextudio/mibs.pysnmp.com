# SNMP MIB module (CADANT-IPDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-IPDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:00 2024
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

(cadExperimental,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadExperimental")

(InetAddressIPv4or6,) = mibBuilder.importSymbols(
    "CADANT-TC",
    "InetAddressIPv4or6")

(InetAddress,
 InetAddressIPv4,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType",
    "InetPortNumber")

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

cadIpdrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30)
)
cadIpdrMib.setRevisions(
        ("2015-06-25 00:00",
         "2014-04-23 00:00",
         "2009-09-28 00:00",
         "2009-09-17 00:00",
         "2009-08-17 00:00",
         "2009-01-06 00:00",
         "2007-11-19 00:00",
         "2006-05-09 00:00",
         "2005-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadIpdrMIBObjects_ObjectIdentity = ObjectIdentity
cadIpdrMIBObjects = _CadIpdrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1)
)


class _CadIpdrExportEnabled_Type(TruthValue):
    """Custom type cadIpdrExportEnabled based on TruthValue"""


_CadIpdrExportEnabled_Object = MibScalar
cadIpdrExportEnabled = _CadIpdrExportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 1),
    _CadIpdrExportEnabled_Type()
)
cadIpdrExportEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrExportEnabled.setStatus("current")


class _CadIpdrQueryPort_Type(Integer32):
    """Custom type cadIpdrQueryPort based on Integer32"""
    defaultValue = 4737

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadIpdrQueryPort_Type.__name__ = "Integer32"
_CadIpdrQueryPort_Object = MibScalar
cadIpdrQueryPort = _CadIpdrQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 2),
    _CadIpdrQueryPort_Type()
)
cadIpdrQueryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrQueryPort.setStatus("current")


class _CadIpdrStreamingPort_Type(Integer32):
    """Custom type cadIpdrStreamingPort based on Integer32"""
    defaultValue = 4737

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadIpdrStreamingPort_Type.__name__ = "Integer32"
_CadIpdrStreamingPort_Object = MibScalar
cadIpdrStreamingPort = _CadIpdrStreamingPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 3),
    _CadIpdrStreamingPort_Type()
)
cadIpdrStreamingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrStreamingPort.setStatus("current")


class _CadIpdrDataAckWindow_Type(Integer32):
    """Custom type cadIpdrDataAckWindow based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadIpdrDataAckWindow_Type.__name__ = "Integer32"
_CadIpdrDataAckWindow_Object = MibScalar
cadIpdrDataAckWindow = _CadIpdrDataAckWindow_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 4),
    _CadIpdrDataAckWindow_Type()
)
cadIpdrDataAckWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrDataAckWindow.setStatus("current")


class _CadIpdrDataAckTimeout_Type(Integer32):
    """Custom type cadIpdrDataAckTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CadIpdrDataAckTimeout_Type.__name__ = "Integer32"
_CadIpdrDataAckTimeout_Object = MibScalar
cadIpdrDataAckTimeout = _CadIpdrDataAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 5),
    _CadIpdrDataAckTimeout_Type()
)
cadIpdrDataAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrDataAckTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cadIpdrDataAckTimeout.setUnits("seconds")


class _CadIpdrKeepAliveInterval_Type(Integer32):
    """Custom type cadIpdrKeepAliveInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CadIpdrKeepAliveInterval_Type.__name__ = "Integer32"
_CadIpdrKeepAliveInterval_Object = MibScalar
cadIpdrKeepAliveInterval = _CadIpdrKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 6),
    _CadIpdrKeepAliveInterval_Type()
)
cadIpdrKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIpdrKeepAliveInterval.setUnits("seconds")


class _CadIpdrExportAllCounts_Type(TruthValue):
    """Custom type cadIpdrExportAllCounts based on TruthValue"""


_CadIpdrExportAllCounts_Object = MibScalar
cadIpdrExportAllCounts = _CadIpdrExportAllCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 7),
    _CadIpdrExportAllCounts_Type()
)
cadIpdrExportAllCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrExportAllCounts.setStatus("current")


class _CadIpdrExportCpeInfo_Type(TruthValue):
    """Custom type cadIpdrExportCpeInfo based on TruthValue"""


_CadIpdrExportCpeInfo_Object = MibScalar
cadIpdrExportCpeInfo = _CadIpdrExportCpeInfo_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 8),
    _CadIpdrExportCpeInfo_Type()
)
cadIpdrExportCpeInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrExportCpeInfo.setStatus("current")


class _CadIpdrSessionId_Type(Integer32):
    """Custom type cadIpdrSessionId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CadIpdrSessionId_Type.__name__ = "Integer32"
_CadIpdrSessionId_Object = MibScalar
cadIpdrSessionId = _CadIpdrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 9),
    _CadIpdrSessionId_Type()
)
cadIpdrSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrSessionId.setStatus("current")


class _CadIpdrExportMode_Type(Integer32):
    """Custom type cadIpdrExportMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CadIpdrExportMode_Type.__name__ = "Integer32"
_CadIpdrExportMode_Object = MibScalar
cadIpdrExportMode = _CadIpdrExportMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 10),
    _CadIpdrExportMode_Type()
)
cadIpdrExportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpdrExportMode.setStatus("current")
_CadIpdrCollectorTable_Object = MibTable
cadIpdrCollectorTable = _CadIpdrCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11)
)
if mibBuilder.loadTexts:
    cadIpdrCollectorTable.setStatus("current")
_CadIpdrCollectorEntry_Object = MibTableRow
cadIpdrCollectorEntry = _CadIpdrCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1)
)
cadIpdrCollectorEntry.setIndexNames(
    (0, "CADANT-IPDR-MIB", "cadIpdrCollectorPriority"),
    (0, "CADANT-IPDR-MIB", "cadIpdrCollectorIpAddress"),
)
if mibBuilder.loadTexts:
    cadIpdrCollectorEntry.setStatus("current")


class _CadIpdrCollectorPriority_Type(Integer32):
    """Custom type cadIpdrCollectorPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIpdrCollectorPriority_Type.__name__ = "Integer32"
_CadIpdrCollectorPriority_Object = MibTableColumn
cadIpdrCollectorPriority = _CadIpdrCollectorPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 1),
    _CadIpdrCollectorPriority_Type()
)
cadIpdrCollectorPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrCollectorPriority.setStatus("current")


class _CadIpdrCollectorIpAddrType_Type(InetAddressType):
    """Custom type cadIpdrCollectorIpAddrType based on InetAddressType"""


_CadIpdrCollectorIpAddrType_Object = MibTableColumn
cadIpdrCollectorIpAddrType = _CadIpdrCollectorIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 2),
    _CadIpdrCollectorIpAddrType_Type()
)
cadIpdrCollectorIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCollectorIpAddrType.setStatus("current")
_CadIpdrCollectorIpAddress_Type = InetAddressIPv4or6
_CadIpdrCollectorIpAddress_Object = MibTableColumn
cadIpdrCollectorIpAddress = _CadIpdrCollectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 3),
    _CadIpdrCollectorIpAddress_Type()
)
cadIpdrCollectorIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrCollectorIpAddress.setStatus("current")


class _CadIpdrCollectorPort_Type(InetPortNumber):
    """Custom type cadIpdrCollectorPort based on InetPortNumber"""
    defaultValue = 4737


_CadIpdrCollectorPort_Object = MibTableColumn
cadIpdrCollectorPort = _CadIpdrCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 4),
    _CadIpdrCollectorPort_Type()
)
cadIpdrCollectorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCollectorPort.setStatus("current")


class _CadIpdrCollectorActive_Type(TruthValue):
    """Custom type cadIpdrCollectorActive based on TruthValue"""


_CadIpdrCollectorActive_Object = MibTableColumn
cadIpdrCollectorActive = _CadIpdrCollectorActive_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 5),
    _CadIpdrCollectorActive_Type()
)
cadIpdrCollectorActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCollectorActive.setStatus("current")


class _CadIpdrCollectorPrimary_Type(TruthValue):
    """Custom type cadIpdrCollectorPrimary based on TruthValue"""


_CadIpdrCollectorPrimary_Object = MibTableColumn
cadIpdrCollectorPrimary = _CadIpdrCollectorPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 6),
    _CadIpdrCollectorPrimary_Type()
)
cadIpdrCollectorPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCollectorPrimary.setStatus("current")
_CadIpdrCollectorOutIntRecs_Type = Counter64
_CadIpdrCollectorOutIntRecs_Object = MibTableColumn
cadIpdrCollectorOutIntRecs = _CadIpdrCollectorOutIntRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 7),
    _CadIpdrCollectorOutIntRecs_Type()
)
cadIpdrCollectorOutIntRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCollectorOutIntRecs.setStatus("current")
_CadIpdrCollectorOutStpRecs_Type = Counter64
_CadIpdrCollectorOutStpRecs_Object = MibTableColumn
cadIpdrCollectorOutStpRecs = _CadIpdrCollectorOutStpRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 8),
    _CadIpdrCollectorOutStpRecs_Type()
)
cadIpdrCollectorOutStpRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCollectorOutStpRecs.setStatus("current")
_CadIpdrCollectorSupIntRecs_Type = Counter64
_CadIpdrCollectorSupIntRecs_Object = MibTableColumn
cadIpdrCollectorSupIntRecs = _CadIpdrCollectorSupIntRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 9),
    _CadIpdrCollectorSupIntRecs_Type()
)
cadIpdrCollectorSupIntRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCollectorSupIntRecs.setStatus("current")
_CadIpdrCollectorStatus_Type = RowStatus
_CadIpdrCollectorStatus_Object = MibTableColumn
cadIpdrCollectorStatus = _CadIpdrCollectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 11, 1, 10),
    _CadIpdrCollectorStatus_Type()
)
cadIpdrCollectorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrCollectorStatus.setStatus("current")
_CadIpdrReportCycleTable_Object = MibTable
cadIpdrReportCycleTable = _CadIpdrReportCycleTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12)
)
if mibBuilder.loadTexts:
    cadIpdrReportCycleTable.setStatus("current")
_CadIpdrReportCycleEntry_Object = MibTableRow
cadIpdrReportCycleEntry = _CadIpdrReportCycleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1)
)
cadIpdrReportCycleEntry.setIndexNames(
    (0, "CADANT-IPDR-MIB", "cadIpdrReportStartHH"),
    (0, "CADANT-IPDR-MIB", "cadIpdrReportStartMM"),
)
if mibBuilder.loadTexts:
    cadIpdrReportCycleEntry.setStatus("current")


class _CadIpdrReportStartHH_Type(Integer32):
    """Custom type cadIpdrReportStartHH based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CadIpdrReportStartHH_Type.__name__ = "Integer32"
_CadIpdrReportStartHH_Object = MibTableColumn
cadIpdrReportStartHH = _CadIpdrReportStartHH_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 1),
    _CadIpdrReportStartHH_Type()
)
cadIpdrReportStartHH.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrReportStartHH.setStatus("current")


class _CadIpdrReportStartMM_Type(Integer32):
    """Custom type cadIpdrReportStartMM based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CadIpdrReportStartMM_Type.__name__ = "Integer32"
_CadIpdrReportStartMM_Object = MibTableColumn
cadIpdrReportStartMM = _CadIpdrReportStartMM_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 2),
    _CadIpdrReportStartMM_Type()
)
cadIpdrReportStartMM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrReportStartMM.setStatus("current")


class _CadIpdrReportInterval_Type(Integer32):
    """Custom type cadIpdrReportInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1440),
    )


_CadIpdrReportInterval_Type.__name__ = "Integer32"
_CadIpdrReportInterval_Object = MibTableColumn
cadIpdrReportInterval = _CadIpdrReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 3),
    _CadIpdrReportInterval_Type()
)
cadIpdrReportInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIpdrReportInterval.setUnits("minutes")
_CadIpdrReportOutIntRecs_Type = Counter64
_CadIpdrReportOutIntRecs_Object = MibTableColumn
cadIpdrReportOutIntRecs = _CadIpdrReportOutIntRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 4),
    _CadIpdrReportOutIntRecs_Type()
)
cadIpdrReportOutIntRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrReportOutIntRecs.setStatus("current")
_CadIpdrReportOutStpRecs_Type = Counter64
_CadIpdrReportOutStpRecs_Object = MibTableColumn
cadIpdrReportOutStpRecs = _CadIpdrReportOutStpRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 5),
    _CadIpdrReportOutStpRecs_Type()
)
cadIpdrReportOutStpRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrReportOutStpRecs.setStatus("current")
_CadIpdrReportSupIntRecs_Type = Counter64
_CadIpdrReportSupIntRecs_Object = MibTableColumn
cadIpdrReportSupIntRecs = _CadIpdrReportSupIntRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 6),
    _CadIpdrReportSupIntRecs_Type()
)
cadIpdrReportSupIntRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrReportSupIntRecs.setStatus("current")
_CadIpdrReportStatus_Type = RowStatus
_CadIpdrReportStatus_Object = MibTableColumn
cadIpdrReportStatus = _CadIpdrReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 12, 1, 7),
    _CadIpdrReportStatus_Type()
)
cadIpdrReportStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrReportStatus.setStatus("current")
_CadIpdrServiceTable_Object = MibTable
cadIpdrServiceTable = _CadIpdrServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13)
)
if mibBuilder.loadTexts:
    cadIpdrServiceTable.setStatus("current")
_CadIpdrServiceEntry_Object = MibTableRow
cadIpdrServiceEntry = _CadIpdrServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1)
)
cadIpdrServiceEntry.setIndexNames(
    (0, "CADANT-IPDR-MIB", "cadIpdrServiceSessionId"),
)
if mibBuilder.loadTexts:
    cadIpdrServiceEntry.setStatus("current")


class _CadIpdrServiceSessionId_Type(Integer32):
    """Custom type cadIpdrServiceSessionId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIpdrServiceSessionId_Type.__name__ = "Integer32"
_CadIpdrServiceSessionId_Object = MibTableColumn
cadIpdrServiceSessionId = _CadIpdrServiceSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 1),
    _CadIpdrServiceSessionId_Type()
)
cadIpdrServiceSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrServiceSessionId.setStatus("current")


class _CadIpdrServiceType_Type(Integer32):
    """Custom type cadIpdrServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_CadIpdrServiceType_Type.__name__ = "Integer32"
_CadIpdrServiceType_Object = MibTableColumn
cadIpdrServiceType = _CadIpdrServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 2),
    _CadIpdrServiceType_Type()
)
cadIpdrServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServiceType.setStatus("current")


class _CadIpdrServiceMethod_Type(Integer32):
    """Custom type cadIpdrServiceMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CadIpdrServiceMethod_Type.__name__ = "Integer32"
_CadIpdrServiceMethod_Object = MibTableColumn
cadIpdrServiceMethod = _CadIpdrServiceMethod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 3),
    _CadIpdrServiceMethod_Type()
)
cadIpdrServiceMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServiceMethod.setStatus("current")


class _CadIpdrServicePriority_Type(Integer32):
    """Custom type cadIpdrServicePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CadIpdrServicePriority_Type.__name__ = "Integer32"
_CadIpdrServicePriority_Object = MibTableColumn
cadIpdrServicePriority = _CadIpdrServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 4),
    _CadIpdrServicePriority_Type()
)
cadIpdrServicePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServicePriority.setStatus("current")


class _CadIpdrServiceDataAckWindow_Type(Integer32):
    """Custom type cadIpdrServiceDataAckWindow based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadIpdrServiceDataAckWindow_Type.__name__ = "Integer32"
_CadIpdrServiceDataAckWindow_Object = MibTableColumn
cadIpdrServiceDataAckWindow = _CadIpdrServiceDataAckWindow_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 5),
    _CadIpdrServiceDataAckWindow_Type()
)
cadIpdrServiceDataAckWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServiceDataAckWindow.setStatus("current")


class _CadIpdrServiceDataAckTimeout_Type(Integer32):
    """Custom type cadIpdrServiceDataAckTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CadIpdrServiceDataAckTimeout_Type.__name__ = "Integer32"
_CadIpdrServiceDataAckTimeout_Object = MibTableColumn
cadIpdrServiceDataAckTimeout = _CadIpdrServiceDataAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 6),
    _CadIpdrServiceDataAckTimeout_Type()
)
cadIpdrServiceDataAckTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServiceDataAckTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cadIpdrServiceDataAckTimeout.setUnits("seconds")


class _CadIpdrServiceReportCycleSet_Type(Integer32):
    """Custom type cadIpdrServiceReportCycleSet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIpdrServiceReportCycleSet_Type.__name__ = "Integer32"
_CadIpdrServiceReportCycleSet_Object = MibTableColumn
cadIpdrServiceReportCycleSet = _CadIpdrServiceReportCycleSet_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 7),
    _CadIpdrServiceReportCycleSet_Type()
)
cadIpdrServiceReportCycleSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServiceReportCycleSet.setStatus("current")


class _CadIpdrServiceEvtPaceGap_Type(Integer32):
    """Custom type cadIpdrServiceEvtPaceGap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CadIpdrServiceEvtPaceGap_Type.__name__ = "Integer32"
_CadIpdrServiceEvtPaceGap_Object = MibTableColumn
cadIpdrServiceEvtPaceGap = _CadIpdrServiceEvtPaceGap_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 8),
    _CadIpdrServiceEvtPaceGap_Type()
)
cadIpdrServiceEvtPaceGap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServiceEvtPaceGap.setStatus("current")


class _CadIpdrServiceAllCounts_Type(TruthValue):
    """Custom type cadIpdrServiceAllCounts based on TruthValue"""


_CadIpdrServiceAllCounts_Object = MibTableColumn
cadIpdrServiceAllCounts = _CadIpdrServiceAllCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 9),
    _CadIpdrServiceAllCounts_Type()
)
cadIpdrServiceAllCounts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServiceAllCounts.setStatus("current")
_CadIpdrServiceStatus_Type = RowStatus
_CadIpdrServiceStatus_Object = MibTableColumn
cadIpdrServiceStatus = _CadIpdrServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 13, 1, 10),
    _CadIpdrServiceStatus_Type()
)
cadIpdrServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrServiceStatus.setStatus("current")
_CadIpdrReportCycleSetTable_Object = MibTable
cadIpdrReportCycleSetTable = _CadIpdrReportCycleSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14)
)
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetTable.setStatus("current")
_CadIpdrReportCycleSetEntry_Object = MibTableRow
cadIpdrReportCycleSetEntry = _CadIpdrReportCycleSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1)
)
cadIpdrReportCycleSetEntry.setIndexNames(
    (0, "CADANT-IPDR-MIB", "cadIpdrReportCycleSetSet"),
    (0, "CADANT-IPDR-MIB", "cadIpdrReportCycleSetStartHH"),
    (0, "CADANT-IPDR-MIB", "cadIpdrReportCycleSetStartMM"),
)
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetEntry.setStatus("current")


class _CadIpdrReportCycleSetSet_Type(Integer32):
    """Custom type cadIpdrReportCycleSetSet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIpdrReportCycleSetSet_Type.__name__ = "Integer32"
_CadIpdrReportCycleSetSet_Object = MibTableColumn
cadIpdrReportCycleSetSet = _CadIpdrReportCycleSetSet_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 1),
    _CadIpdrReportCycleSetSet_Type()
)
cadIpdrReportCycleSetSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetSet.setStatus("current")


class _CadIpdrReportCycleSetStartHH_Type(Integer32):
    """Custom type cadIpdrReportCycleSetStartHH based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CadIpdrReportCycleSetStartHH_Type.__name__ = "Integer32"
_CadIpdrReportCycleSetStartHH_Object = MibTableColumn
cadIpdrReportCycleSetStartHH = _CadIpdrReportCycleSetStartHH_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 2),
    _CadIpdrReportCycleSetStartHH_Type()
)
cadIpdrReportCycleSetStartHH.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetStartHH.setStatus("current")


class _CadIpdrReportCycleSetStartMM_Type(Integer32):
    """Custom type cadIpdrReportCycleSetStartMM based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CadIpdrReportCycleSetStartMM_Type.__name__ = "Integer32"
_CadIpdrReportCycleSetStartMM_Object = MibTableColumn
cadIpdrReportCycleSetStartMM = _CadIpdrReportCycleSetStartMM_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 3),
    _CadIpdrReportCycleSetStartMM_Type()
)
cadIpdrReportCycleSetStartMM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetStartMM.setStatus("current")


class _CadIpdrReportCycleSetInterval_Type(Integer32):
    """Custom type cadIpdrReportCycleSetInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1440),
    )


_CadIpdrReportCycleSetInterval_Type.__name__ = "Integer32"
_CadIpdrReportCycleSetInterval_Object = MibTableColumn
cadIpdrReportCycleSetInterval = _CadIpdrReportCycleSetInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 4),
    _CadIpdrReportCycleSetInterval_Type()
)
cadIpdrReportCycleSetInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetInterval.setUnits("minutes")
_CadIpdrReportCycleSetStatus_Type = RowStatus
_CadIpdrReportCycleSetStatus_Object = MibTableColumn
cadIpdrReportCycleSetStatus = _CadIpdrReportCycleSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 14, 1, 5),
    _CadIpdrReportCycleSetStatus_Type()
)
cadIpdrReportCycleSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetStatus.setStatus("current")
_CadIpdrCountsTable_Object = MibTable
cadIpdrCountsTable = _CadIpdrCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15)
)
if mibBuilder.loadTexts:
    cadIpdrCountsTable.setStatus("current")
_CadIpdrCountsEntry_Object = MibTableRow
cadIpdrCountsEntry = _CadIpdrCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1)
)
cadIpdrCountsEntry.setIndexNames(
    (0, "CADANT-IPDR-MIB", "cadIpdrCountsSessionId"),
    (0, "CADANT-IPDR-MIB", "cadIpdrCountsCollectorPriority"),
    (0, "CADANT-IPDR-MIB", "cadIpdrCountsCollectorIpAddress"),
    (0, "CADANT-IPDR-MIB", "cadIpdrCountsStartHH"),
    (0, "CADANT-IPDR-MIB", "cadIpdrCountsStartMM"),
    (0, "CADANT-IPDR-MIB", "cadIpdrCountsAdhocIndex"),
)
if mibBuilder.loadTexts:
    cadIpdrCountsEntry.setStatus("current")


class _CadIpdrCountsSessionId_Type(Integer32):
    """Custom type cadIpdrCountsSessionId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIpdrCountsSessionId_Type.__name__ = "Integer32"
_CadIpdrCountsSessionId_Object = MibTableColumn
cadIpdrCountsSessionId = _CadIpdrCountsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 1),
    _CadIpdrCountsSessionId_Type()
)
cadIpdrCountsSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrCountsSessionId.setStatus("current")


class _CadIpdrCountsCollectorPriority_Type(Integer32):
    """Custom type cadIpdrCountsCollectorPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIpdrCountsCollectorPriority_Type.__name__ = "Integer32"
_CadIpdrCountsCollectorPriority_Object = MibTableColumn
cadIpdrCountsCollectorPriority = _CadIpdrCountsCollectorPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 2),
    _CadIpdrCountsCollectorPriority_Type()
)
cadIpdrCountsCollectorPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrCountsCollectorPriority.setStatus("current")
_CadIpdrCountsCollectorIpAddress_Type = InetAddressIPv4or6
_CadIpdrCountsCollectorIpAddress_Object = MibTableColumn
cadIpdrCountsCollectorIpAddress = _CadIpdrCountsCollectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 3),
    _CadIpdrCountsCollectorIpAddress_Type()
)
cadIpdrCountsCollectorIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrCountsCollectorIpAddress.setStatus("current")


class _CadIpdrCountsStartHH_Type(Integer32):
    """Custom type cadIpdrCountsStartHH based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CadIpdrCountsStartHH_Type.__name__ = "Integer32"
_CadIpdrCountsStartHH_Object = MibTableColumn
cadIpdrCountsStartHH = _CadIpdrCountsStartHH_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 4),
    _CadIpdrCountsStartHH_Type()
)
cadIpdrCountsStartHH.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrCountsStartHH.setStatus("current")


class _CadIpdrCountsStartMM_Type(Integer32):
    """Custom type cadIpdrCountsStartMM based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CadIpdrCountsStartMM_Type.__name__ = "Integer32"
_CadIpdrCountsStartMM_Object = MibTableColumn
cadIpdrCountsStartMM = _CadIpdrCountsStartMM_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 5),
    _CadIpdrCountsStartMM_Type()
)
cadIpdrCountsStartMM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrCountsStartMM.setStatus("current")


class _CadIpdrCountsAdhocIndex_Type(Unsigned32):
    """Custom type cadIpdrCountsAdhocIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CadIpdrCountsAdhocIndex_Type.__name__ = "Unsigned32"
_CadIpdrCountsAdhocIndex_Object = MibTableColumn
cadIpdrCountsAdhocIndex = _CadIpdrCountsAdhocIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 6),
    _CadIpdrCountsAdhocIndex_Type()
)
cadIpdrCountsAdhocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrCountsAdhocIndex.setStatus("current")


class _CadIpdrCountsStartTime_Type(OctetString):
    """Custom type cadIpdrCountsStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadIpdrCountsStartTime_Type.__name__ = "OctetString"
_CadIpdrCountsStartTime_Object = MibTableColumn
cadIpdrCountsStartTime = _CadIpdrCountsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 7),
    _CadIpdrCountsStartTime_Type()
)
cadIpdrCountsStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrCountsStartTime.setStatus("current")


class _CadIpdrCountsStopTime_Type(OctetString):
    """Custom type cadIpdrCountsStopTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadIpdrCountsStopTime_Type.__name__ = "OctetString"
_CadIpdrCountsStopTime_Object = MibTableColumn
cadIpdrCountsStopTime = _CadIpdrCountsStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 8),
    _CadIpdrCountsStopTime_Type()
)
cadIpdrCountsStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrCountsStopTime.setStatus("current")
_CadIpdrCountsIntRecs_Type = Counter64
_CadIpdrCountsIntRecs_Object = MibTableColumn
cadIpdrCountsIntRecs = _CadIpdrCountsIntRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 9),
    _CadIpdrCountsIntRecs_Type()
)
cadIpdrCountsIntRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCountsIntRecs.setStatus("current")
_CadIpdrCountsSupIntRecs_Type = Counter64
_CadIpdrCountsSupIntRecs_Object = MibTableColumn
cadIpdrCountsSupIntRecs = _CadIpdrCountsSupIntRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 10),
    _CadIpdrCountsSupIntRecs_Type()
)
cadIpdrCountsSupIntRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCountsSupIntRecs.setStatus("current")
_CadIpdrCountsStartRecs_Type = Counter64
_CadIpdrCountsStartRecs_Object = MibTableColumn
cadIpdrCountsStartRecs = _CadIpdrCountsStartRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 11),
    _CadIpdrCountsStartRecs_Type()
)
cadIpdrCountsStartRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCountsStartRecs.setStatus("current")
_CadIpdrCountsStopRecs_Type = Counter64
_CadIpdrCountsStopRecs_Object = MibTableColumn
cadIpdrCountsStopRecs = _CadIpdrCountsStopRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 12),
    _CadIpdrCountsStopRecs_Type()
)
cadIpdrCountsStopRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCountsStopRecs.setStatus("current")
_CadIpdrCountsEventRecs_Type = Counter64
_CadIpdrCountsEventRecs_Object = MibTableColumn
cadIpdrCountsEventRecs = _CadIpdrCountsEventRecs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 13),
    _CadIpdrCountsEventRecs_Type()
)
cadIpdrCountsEventRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrCountsEventRecs.setStatus("current")
_CadIpdrCountsStatus_Type = RowStatus
_CadIpdrCountsStatus_Object = MibTableColumn
cadIpdrCountsStatus = _CadIpdrCountsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 15, 1, 14),
    _CadIpdrCountsStatus_Type()
)
cadIpdrCountsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrCountsStatus.setStatus("current")
_CadIpdrSessionCollectorTable_Object = MibTable
cadIpdrSessionCollectorTable = _CadIpdrSessionCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16)
)
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorTable.setStatus("current")
_CadIpdrSessionCollectorEntry_Object = MibTableRow
cadIpdrSessionCollectorEntry = _CadIpdrSessionCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1)
)
cadIpdrSessionCollectorEntry.setIndexNames(
    (0, "CADANT-IPDR-MIB", "cadIpdrSessionCollectorSessionId"),
    (0, "CADANT-IPDR-MIB", "cadIpdrSessionCollectorPriority"),
    (0, "CADANT-IPDR-MIB", "cadIpdrSessionCollectorIpAddress"),
)
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorEntry.setStatus("current")


class _CadIpdrSessionCollectorSessionId_Type(Integer32):
    """Custom type cadIpdrSessionCollectorSessionId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIpdrSessionCollectorSessionId_Type.__name__ = "Integer32"
_CadIpdrSessionCollectorSessionId_Object = MibTableColumn
cadIpdrSessionCollectorSessionId = _CadIpdrSessionCollectorSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 1),
    _CadIpdrSessionCollectorSessionId_Type()
)
cadIpdrSessionCollectorSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorSessionId.setStatus("current")


class _CadIpdrSessionCollectorPriority_Type(Integer32):
    """Custom type cadIpdrSessionCollectorPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIpdrSessionCollectorPriority_Type.__name__ = "Integer32"
_CadIpdrSessionCollectorPriority_Object = MibTableColumn
cadIpdrSessionCollectorPriority = _CadIpdrSessionCollectorPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 2),
    _CadIpdrSessionCollectorPriority_Type()
)
cadIpdrSessionCollectorPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorPriority.setStatus("current")


class _CadIpdrSessionCollectorIpAddrType_Type(InetAddressType):
    """Custom type cadIpdrSessionCollectorIpAddrType based on InetAddressType"""


_CadIpdrSessionCollectorIpAddrType_Object = MibTableColumn
cadIpdrSessionCollectorIpAddrType = _CadIpdrSessionCollectorIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 3),
    _CadIpdrSessionCollectorIpAddrType_Type()
)
cadIpdrSessionCollectorIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorIpAddrType.setStatus("current")
_CadIpdrSessionCollectorIpAddress_Type = InetAddressIPv4or6
_CadIpdrSessionCollectorIpAddress_Object = MibTableColumn
cadIpdrSessionCollectorIpAddress = _CadIpdrSessionCollectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 4),
    _CadIpdrSessionCollectorIpAddress_Type()
)
cadIpdrSessionCollectorIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorIpAddress.setStatus("current")


class _CadIpdrSessionCollectorPort_Type(InetPortNumber):
    """Custom type cadIpdrSessionCollectorPort based on InetPortNumber"""
    defaultValue = 4737


_CadIpdrSessionCollectorPort_Object = MibTableColumn
cadIpdrSessionCollectorPort = _CadIpdrSessionCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 5),
    _CadIpdrSessionCollectorPort_Type()
)
cadIpdrSessionCollectorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorPort.setStatus("current")


class _CadIpdrSessionCollectorActive_Type(TruthValue):
    """Custom type cadIpdrSessionCollectorActive based on TruthValue"""


_CadIpdrSessionCollectorActive_Object = MibTableColumn
cadIpdrSessionCollectorActive = _CadIpdrSessionCollectorActive_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 6),
    _CadIpdrSessionCollectorActive_Type()
)
cadIpdrSessionCollectorActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorActive.setStatus("current")


class _CadIpdrSessionCollectorPrimary_Type(TruthValue):
    """Custom type cadIpdrSessionCollectorPrimary based on TruthValue"""


_CadIpdrSessionCollectorPrimary_Object = MibTableColumn
cadIpdrSessionCollectorPrimary = _CadIpdrSessionCollectorPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 7),
    _CadIpdrSessionCollectorPrimary_Type()
)
cadIpdrSessionCollectorPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorPrimary.setStatus("current")
_CadIpdrSessionCollectorStatus_Type = RowStatus
_CadIpdrSessionCollectorStatus_Object = MibTableColumn
cadIpdrSessionCollectorStatus = _CadIpdrSessionCollectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 1, 16, 1, 8),
    _CadIpdrSessionCollectorStatus_Type()
)
cadIpdrSessionCollectorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorStatus.setStatus("current")
_CadIpdrMIBConformance_ObjectIdentity = ObjectIdentity
cadIpdrMIBConformance = _CadIpdrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2)
)
_CadIpdrMIBCompliances_ObjectIdentity = ObjectIdentity
cadIpdrMIBCompliances = _CadIpdrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 1)
)
_CadIpdrMIBGroups_ObjectIdentity = ObjectIdentity
cadIpdrMIBGroups = _CadIpdrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2)
)

# Managed Objects groups

cadIpdrBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 1)
)
cadIpdrBasicGroup.setObjects(
      *(("CADANT-IPDR-MIB", "cadIpdrExportEnabled"),
        ("CADANT-IPDR-MIB", "cadIpdrQueryPort"),
        ("CADANT-IPDR-MIB", "cadIpdrStreamingPort"),
        ("CADANT-IPDR-MIB", "cadIpdrDataAckWindow"),
        ("CADANT-IPDR-MIB", "cadIpdrDataAckTimeout"),
        ("CADANT-IPDR-MIB", "cadIpdrKeepAliveInterval"),
        ("CADANT-IPDR-MIB", "cadIpdrExportAllCounts"),
        ("CADANT-IPDR-MIB", "cadIpdrExportCpeInfo"),
        ("CADANT-IPDR-MIB", "cadIpdrSessionId"),
        ("CADANT-IPDR-MIB", "cadIpdrExportMode"))
)
if mibBuilder.loadTexts:
    cadIpdrBasicGroup.setStatus("current")

cadIpdrCollectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 2)
)
cadIpdrCollectorGroup.setObjects(
      *(("CADANT-IPDR-MIB", "cadIpdrCollectorIpAddrType"),
        ("CADANT-IPDR-MIB", "cadIpdrCollectorPort"),
        ("CADANT-IPDR-MIB", "cadIpdrCollectorActive"),
        ("CADANT-IPDR-MIB", "cadIpdrCollectorPrimary"),
        ("CADANT-IPDR-MIB", "cadIpdrCollectorOutIntRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrCollectorOutStpRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrCollectorSupIntRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrCollectorStatus"))
)
if mibBuilder.loadTexts:
    cadIpdrCollectorGroup.setStatus("current")

cadIpdrReportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 3)
)
cadIpdrReportGroup.setObjects(
      *(("CADANT-IPDR-MIB", "cadIpdrReportOutIntRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrReportOutStpRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrReportSupIntRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrReportStatus"))
)
if mibBuilder.loadTexts:
    cadIpdrReportGroup.setStatus("current")

cadIpdrServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 4)
)
cadIpdrServiceGroup.setObjects(
      *(("CADANT-IPDR-MIB", "cadIpdrServiceType"),
        ("CADANT-IPDR-MIB", "cadIpdrServiceMethod"),
        ("CADANT-IPDR-MIB", "cadIpdrServicePriority"),
        ("CADANT-IPDR-MIB", "cadIpdrServiceDataAckWindow"),
        ("CADANT-IPDR-MIB", "cadIpdrServiceDataAckTimeout"),
        ("CADANT-IPDR-MIB", "cadIpdrServiceReportCycleSet"),
        ("CADANT-IPDR-MIB", "cadIpdrServiceEvtPaceGap"),
        ("CADANT-IPDR-MIB", "cadIpdrServiceAllCounts"),
        ("CADANT-IPDR-MIB", "cadIpdrServiceStatus"))
)
if mibBuilder.loadTexts:
    cadIpdrServiceGroup.setStatus("current")

cadIpdrReportCycleSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 5)
)
cadIpdrReportCycleSetGroup.setObjects(
      *(("CADANT-IPDR-MIB", "cadIpdrReportCycleSetInterval"),
        ("CADANT-IPDR-MIB", "cadIpdrReportCycleSetStatus"))
)
if mibBuilder.loadTexts:
    cadIpdrReportCycleSetGroup.setStatus("current")

cadIpdrCountsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 6)
)
cadIpdrCountsGroup.setObjects(
      *(("CADANT-IPDR-MIB", "cadIpdrCountsStartTime"),
        ("CADANT-IPDR-MIB", "cadIpdrCountsStopTime"),
        ("CADANT-IPDR-MIB", "cadIpdrCountsIntRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrCountsSupIntRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrCountsStartRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrCountsStopRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrCountsEventRecs"),
        ("CADANT-IPDR-MIB", "cadIpdrCountsStatus"))
)
if mibBuilder.loadTexts:
    cadIpdrCountsGroup.setStatus("current")

cadIpdrSessionCollectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 2, 7)
)
cadIpdrSessionCollectorGroup.setObjects(
      *(("CADANT-IPDR-MIB", "cadIpdrSessionCollectorIpAddrType"),
        ("CADANT-IPDR-MIB", "cadIpdrSessionCollectorPort"),
        ("CADANT-IPDR-MIB", "cadIpdrSessionCollectorActive"),
        ("CADANT-IPDR-MIB", "cadIpdrSessionCollectorPrimary"),
        ("CADANT-IPDR-MIB", "cadIpdrSessionCollectorStatus"))
)
if mibBuilder.loadTexts:
    cadIpdrSessionCollectorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cadIpdrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cadIpdrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-IPDR-MIB",
    **{"cadIpdrMib": cadIpdrMib,
       "cadIpdrMIBObjects": cadIpdrMIBObjects,
       "cadIpdrExportEnabled": cadIpdrExportEnabled,
       "cadIpdrQueryPort": cadIpdrQueryPort,
       "cadIpdrStreamingPort": cadIpdrStreamingPort,
       "cadIpdrDataAckWindow": cadIpdrDataAckWindow,
       "cadIpdrDataAckTimeout": cadIpdrDataAckTimeout,
       "cadIpdrKeepAliveInterval": cadIpdrKeepAliveInterval,
       "cadIpdrExportAllCounts": cadIpdrExportAllCounts,
       "cadIpdrExportCpeInfo": cadIpdrExportCpeInfo,
       "cadIpdrSessionId": cadIpdrSessionId,
       "cadIpdrExportMode": cadIpdrExportMode,
       "cadIpdrCollectorTable": cadIpdrCollectorTable,
       "cadIpdrCollectorEntry": cadIpdrCollectorEntry,
       "cadIpdrCollectorPriority": cadIpdrCollectorPriority,
       "cadIpdrCollectorIpAddrType": cadIpdrCollectorIpAddrType,
       "cadIpdrCollectorIpAddress": cadIpdrCollectorIpAddress,
       "cadIpdrCollectorPort": cadIpdrCollectorPort,
       "cadIpdrCollectorActive": cadIpdrCollectorActive,
       "cadIpdrCollectorPrimary": cadIpdrCollectorPrimary,
       "cadIpdrCollectorOutIntRecs": cadIpdrCollectorOutIntRecs,
       "cadIpdrCollectorOutStpRecs": cadIpdrCollectorOutStpRecs,
       "cadIpdrCollectorSupIntRecs": cadIpdrCollectorSupIntRecs,
       "cadIpdrCollectorStatus": cadIpdrCollectorStatus,
       "cadIpdrReportCycleTable": cadIpdrReportCycleTable,
       "cadIpdrReportCycleEntry": cadIpdrReportCycleEntry,
       "cadIpdrReportStartHH": cadIpdrReportStartHH,
       "cadIpdrReportStartMM": cadIpdrReportStartMM,
       "cadIpdrReportInterval": cadIpdrReportInterval,
       "cadIpdrReportOutIntRecs": cadIpdrReportOutIntRecs,
       "cadIpdrReportOutStpRecs": cadIpdrReportOutStpRecs,
       "cadIpdrReportSupIntRecs": cadIpdrReportSupIntRecs,
       "cadIpdrReportStatus": cadIpdrReportStatus,
       "cadIpdrServiceTable": cadIpdrServiceTable,
       "cadIpdrServiceEntry": cadIpdrServiceEntry,
       "cadIpdrServiceSessionId": cadIpdrServiceSessionId,
       "cadIpdrServiceType": cadIpdrServiceType,
       "cadIpdrServiceMethod": cadIpdrServiceMethod,
       "cadIpdrServicePriority": cadIpdrServicePriority,
       "cadIpdrServiceDataAckWindow": cadIpdrServiceDataAckWindow,
       "cadIpdrServiceDataAckTimeout": cadIpdrServiceDataAckTimeout,
       "cadIpdrServiceReportCycleSet": cadIpdrServiceReportCycleSet,
       "cadIpdrServiceEvtPaceGap": cadIpdrServiceEvtPaceGap,
       "cadIpdrServiceAllCounts": cadIpdrServiceAllCounts,
       "cadIpdrServiceStatus": cadIpdrServiceStatus,
       "cadIpdrReportCycleSetTable": cadIpdrReportCycleSetTable,
       "cadIpdrReportCycleSetEntry": cadIpdrReportCycleSetEntry,
       "cadIpdrReportCycleSetSet": cadIpdrReportCycleSetSet,
       "cadIpdrReportCycleSetStartHH": cadIpdrReportCycleSetStartHH,
       "cadIpdrReportCycleSetStartMM": cadIpdrReportCycleSetStartMM,
       "cadIpdrReportCycleSetInterval": cadIpdrReportCycleSetInterval,
       "cadIpdrReportCycleSetStatus": cadIpdrReportCycleSetStatus,
       "cadIpdrCountsTable": cadIpdrCountsTable,
       "cadIpdrCountsEntry": cadIpdrCountsEntry,
       "cadIpdrCountsSessionId": cadIpdrCountsSessionId,
       "cadIpdrCountsCollectorPriority": cadIpdrCountsCollectorPriority,
       "cadIpdrCountsCollectorIpAddress": cadIpdrCountsCollectorIpAddress,
       "cadIpdrCountsStartHH": cadIpdrCountsStartHH,
       "cadIpdrCountsStartMM": cadIpdrCountsStartMM,
       "cadIpdrCountsAdhocIndex": cadIpdrCountsAdhocIndex,
       "cadIpdrCountsStartTime": cadIpdrCountsStartTime,
       "cadIpdrCountsStopTime": cadIpdrCountsStopTime,
       "cadIpdrCountsIntRecs": cadIpdrCountsIntRecs,
       "cadIpdrCountsSupIntRecs": cadIpdrCountsSupIntRecs,
       "cadIpdrCountsStartRecs": cadIpdrCountsStartRecs,
       "cadIpdrCountsStopRecs": cadIpdrCountsStopRecs,
       "cadIpdrCountsEventRecs": cadIpdrCountsEventRecs,
       "cadIpdrCountsStatus": cadIpdrCountsStatus,
       "cadIpdrSessionCollectorTable": cadIpdrSessionCollectorTable,
       "cadIpdrSessionCollectorEntry": cadIpdrSessionCollectorEntry,
       "cadIpdrSessionCollectorSessionId": cadIpdrSessionCollectorSessionId,
       "cadIpdrSessionCollectorPriority": cadIpdrSessionCollectorPriority,
       "cadIpdrSessionCollectorIpAddrType": cadIpdrSessionCollectorIpAddrType,
       "cadIpdrSessionCollectorIpAddress": cadIpdrSessionCollectorIpAddress,
       "cadIpdrSessionCollectorPort": cadIpdrSessionCollectorPort,
       "cadIpdrSessionCollectorActive": cadIpdrSessionCollectorActive,
       "cadIpdrSessionCollectorPrimary": cadIpdrSessionCollectorPrimary,
       "cadIpdrSessionCollectorStatus": cadIpdrSessionCollectorStatus,
       "cadIpdrMIBConformance": cadIpdrMIBConformance,
       "cadIpdrMIBCompliances": cadIpdrMIBCompliances,
       "cadIpdrMIBCompliance": cadIpdrMIBCompliance,
       "cadIpdrMIBGroups": cadIpdrMIBGroups,
       "cadIpdrBasicGroup": cadIpdrBasicGroup,
       "cadIpdrCollectorGroup": cadIpdrCollectorGroup,
       "cadIpdrReportGroup": cadIpdrReportGroup,
       "cadIpdrServiceGroup": cadIpdrServiceGroup,
       "cadIpdrReportCycleSetGroup": cadIpdrReportCycleSetGroup,
       "cadIpdrCountsGroup": cadIpdrCountsGroup,
       "cadIpdrSessionCollectorGroup": cadIpdrSessionCollectorGroup}
)
