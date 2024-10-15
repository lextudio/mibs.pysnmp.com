# SNMP MIB module (CISCO-GPRS-CHARGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GPRS-CHARGING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:55 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity")

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
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

ciscoGprsChargingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192)
)
ciscoGprsChargingMIB.setRevisions(
        ("2011-03-04 00:00",
         "2010-07-27 00:00",
         "2010-06-08 00:00",
         "2010-02-01 00:00",
         "2008-12-12 00:00",
         "2008-01-29 00:00",
         "2006-08-18 00:00",
         "2006-04-04 19:00",
         "2005-09-16 18:00",
         "2004-07-26 02:00",
         "2004-03-22 03:00",
         "2002-11-11 17:00",
         "2002-06-05 10:00",
         "2001-12-04 12:00",
         "2001-09-18 16:00",
         "2000-09-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CgprsCgAlarmType(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("cgprsCgAlarmCapacityFree", 6),
          ("cgprsCgAlarmCapacityFull", 5),
          ("cgprsCgAlarmCdrBuffered", 10),
          ("cgprsCgAlarmCdrDiscard", 9),
          ("cgprsCgAlarmCgDown", 1),
          ("cgprsCgAlarmCgUp", 2),
          ("cgprsCgAlarmChargingDisabled", 11),
          ("cgprsCgAlarmChargingEnabled", 12),
          ("cgprsCgAlarmEchoFailure", 7),
          ("cgprsCgAlarmEchoRestored", 8),
          ("cgprsCgAlarmTransFailure", 3),
          ("cgprsCgAlarmTransSuccess", 4))
    )



class CgprsCgGatewayType(Integer32, TextualConvention):
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
        *(("cgprsCgGatewayPrimary", 1),
          ("cgprsCgGatewaySecondary", 2),
          ("cgprsCgGatewayTertiary", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoGprsChargingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGprsChargingMIBObjects = _CiscoGprsChargingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1)
)
_CiscoGprsChargingConfig_ObjectIdentity = ObjectIdentity
ciscoGprsChargingConfig = _CiscoGprsChargingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1)
)


class _CgprsCgEnable_Type(TruthValue):
    """Custom type cgprsCgEnable based on TruthValue"""


_CgprsCgEnable_Object = MibScalar
cgprsCgEnable = _CgprsCgEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 1),
    _CgprsCgEnable_Type()
)
cgprsCgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgEnable.setStatus("current")


class _CgprsCgCdrLocalSeqNumEnable_Type(TruthValue):
    """Custom type cgprsCgCdrLocalSeqNumEnable based on TruthValue"""


_CgprsCgCdrLocalSeqNumEnable_Object = MibScalar
cgprsCgCdrLocalSeqNumEnable = _CgprsCgCdrLocalSeqNumEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 2),
    _CgprsCgCdrLocalSeqNumEnable_Type()
)
cgprsCgCdrLocalSeqNumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrLocalSeqNumEnable.setStatus("current")


class _CgprsCgCdrNodeIdEnable_Type(TruthValue):
    """Custom type cgprsCgCdrNodeIdEnable based on TruthValue"""


_CgprsCgCdrNodeIdEnable_Object = MibScalar
cgprsCgCdrNodeIdEnable = _CgprsCgCdrNodeIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 3),
    _CgprsCgCdrNodeIdEnable_Type()
)
cgprsCgCdrNodeIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrNodeIdEnable.setStatus("current")


class _CgprsCgFlowControlEcho_Type(TruthValue):
    """Custom type cgprsCgFlowControlEcho based on TruthValue"""


_CgprsCgFlowControlEcho_Object = MibScalar
cgprsCgFlowControlEcho = _CgprsCgFlowControlEcho_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 4),
    _CgprsCgFlowControlEcho_Type()
)
cgprsCgFlowControlEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgFlowControlEcho.setStatus("current")


class _CgprsCgCdrPktsStatEnable_Type(TruthValue):
    """Custom type cgprsCgCdrPktsStatEnable based on TruthValue"""


_CgprsCgCdrPktsStatEnable_Object = MibScalar
cgprsCgCdrPktsStatEnable = _CgprsCgCdrPktsStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 5),
    _CgprsCgCdrPktsStatEnable_Type()
)
cgprsCgCdrPktsStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrPktsStatEnable.setStatus("current")


class _CgprsCgCdrNonPrimaryEnable_Type(TruthValue):
    """Custom type cgprsCgCdrNonPrimaryEnable based on TruthValue"""


_CgprsCgCdrNonPrimaryEnable_Object = MibScalar
cgprsCgCdrNonPrimaryEnable = _CgprsCgCdrNonPrimaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 6),
    _CgprsCgCdrNonPrimaryEnable_Type()
)
cgprsCgCdrNonPrimaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrNonPrimaryEnable.setStatus("obsolete")


class _CgprsCgCdrAggreLimit_Type(Unsigned32):
    """Custom type cgprsCgCdrAggreLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CgprsCgCdrAggreLimit_Type.__name__ = "Unsigned32"
_CgprsCgCdrAggreLimit_Object = MibScalar
cgprsCgCdrAggreLimit = _CgprsCgCdrAggreLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 7),
    _CgprsCgCdrAggreLimit_Type()
)
cgprsCgCdrAggreLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrAggreLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgCdrAggreLimit.setUnits("CDRs")


class _CgprsCgTransInterval_Type(Unsigned32):
    """Custom type cgprsCgTransInterval based on Unsigned32"""
    defaultValue = 105

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgTransInterval_Type.__name__ = "Unsigned32"
_CgprsCgTransInterval_Object = MibScalar
cgprsCgTransInterval = _CgprsCgTransInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 8),
    _CgprsCgTransInterval_Type()
)
cgprsCgTransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgTransInterval.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgTransInterval.setUnits("seconds")


class _CgprsCgPktsQSize_Type(Unsigned32):
    """Custom type cgprsCgPktsQSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CgprsCgPktsQSize_Type.__name__ = "Unsigned32"
_CgprsCgPktsQSize_Object = MibScalar
cgprsCgPktsQSize = _CgprsCgPktsQSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 9),
    _CgprsCgPktsQSize_Type()
)
cgprsCgPktsQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgPktsQSize.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgPktsQSize.setUnits("PDUs")


class _CgprsCgPathRequest_Type(Unsigned32):
    """Custom type cgprsCgPathRequest based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CgprsCgPathRequest_Type.__name__ = "Unsigned32"
_CgprsCgPathRequest_Object = MibScalar
cgprsCgPathRequest = _CgprsCgPathRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 10),
    _CgprsCgPathRequest_Type()
)
cgprsCgPathRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgPathRequest.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgPathRequest.setUnits("minutes")


class _CgprsCgContainerVolThresh_Type(Unsigned32):
    """Custom type cgprsCgContainerVolThresh based on Unsigned32"""
    defaultValue = 1048576

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgContainerVolThresh_Type.__name__ = "Unsigned32"
_CgprsCgContainerVolThresh_Object = MibScalar
cgprsCgContainerVolThresh = _CgprsCgContainerVolThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 11),
    _CgprsCgContainerVolThresh_Type()
)
cgprsCgContainerVolThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgContainerVolThresh.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgContainerVolThresh.setUnits("bytes")


class _CgprsCgMapDataTos_Type(Unsigned32):
    """Custom type cgprsCgMapDataTos based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CgprsCgMapDataTos_Type.__name__ = "Unsigned32"
_CgprsCgMapDataTos_Object = MibScalar
cgprsCgMapDataTos = _CgprsCgMapDataTos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 12),
    _CgprsCgMapDataTos_Type()
)
cgprsCgMapDataTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgMapDataTos.setStatus("current")


class _CgprsCgPathProtocol_Type(Integer32):
    """Custom type cgprsCgPathProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_CgprsCgPathProtocol_Type.__name__ = "Integer32"
_CgprsCgPathProtocol_Object = MibScalar
cgprsCgPathProtocol = _CgprsCgPathProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 13),
    _CgprsCgPathProtocol_Type()
)
cgprsCgPathProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgPathProtocol.setStatus("current")


class _CgprsCgServerSwitchTimeout_Type(Unsigned32):
    """Custom type cgprsCgServerSwitchTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CgprsCgServerSwitchTimeout_Type.__name__ = "Unsigned32"
_CgprsCgServerSwitchTimeout_Object = MibScalar
cgprsCgServerSwitchTimeout = _CgprsCgServerSwitchTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 14),
    _CgprsCgServerSwitchTimeout_Type()
)
cgprsCgServerSwitchTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgServerSwitchTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgServerSwitchTimeout.setUnits("seconds")


class _CgprsCgConditionLimit_Type(Unsigned32):
    """Custom type cgprsCgConditionLimit based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CgprsCgConditionLimit_Type.__name__ = "Unsigned32"
_CgprsCgConditionLimit_Object = MibScalar
cgprsCgConditionLimit = _CgprsCgConditionLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 15),
    _CgprsCgConditionLimit_Type()
)
cgprsCgConditionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgConditionLimit.setStatus("current")


class _CgprsCgGtpPrimePort_Type(Unsigned32):
    """Custom type cgprsCgGtpPrimePort based on Unsigned32"""
    defaultValue = 3386

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 10000),
    )


_CgprsCgGtpPrimePort_Type.__name__ = "Unsigned32"
_CgprsCgGtpPrimePort_Object = MibScalar
cgprsCgGtpPrimePort = _CgprsCgGtpPrimePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 16),
    _CgprsCgGtpPrimePort_Type()
)
cgprsCgGtpPrimePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgGtpPrimePort.setStatus("current")


class _CgprsCgN3BufferSize_Type(Unsigned32):
    """Custom type cgprsCgN3BufferSize based on Unsigned32"""
    defaultValue = 1460

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1460),
    )


_CgprsCgN3BufferSize_Type.__name__ = "Unsigned32"
_CgprsCgN3BufferSize_Object = MibScalar
cgprsCgN3BufferSize = _CgprsCgN3BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 17),
    _CgprsCgN3BufferSize_Type()
)
cgprsCgN3BufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgN3BufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgN3BufferSize.setUnits("bytes")


class _CgprsCgChargeForRoamersOnly_Type(TruthValue):
    """Custom type cgprsCgChargeForRoamersOnly based on TruthValue"""


_CgprsCgChargeForRoamersOnly_Object = MibScalar
cgprsCgChargeForRoamersOnly = _CgprsCgChargeForRoamersOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 18),
    _CgprsCgChargeForRoamersOnly_Type()
)
cgprsCgChargeForRoamersOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgChargeForRoamersOnly.setStatus("current")


class _CgprsCgTariffTimeMaxEntries_Type(Unsigned32):
    """Custom type cgprsCgTariffTimeMaxEntries based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CgprsCgTariffTimeMaxEntries_Type.__name__ = "Unsigned32"
_CgprsCgTariffTimeMaxEntries_Object = MibScalar
cgprsCgTariffTimeMaxEntries = _CgprsCgTariffTimeMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 19),
    _CgprsCgTariffTimeMaxEntries_Type()
)
cgprsCgTariffTimeMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeMaxEntries.setStatus("current")
_CgprsCgTariffTimeNextIndex_Type = TestAndIncr
_CgprsCgTariffTimeNextIndex_Object = MibScalar
cgprsCgTariffTimeNextIndex = _CgprsCgTariffTimeNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 20),
    _CgprsCgTariffTimeNextIndex_Type()
)
cgprsCgTariffTimeNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeNextIndex.setStatus("current")
_CgprsCgTariffTimeTable_Object = MibTable
cgprsCgTariffTimeTable = _CgprsCgTariffTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 21)
)
if mibBuilder.loadTexts:
    cgprsCgTariffTimeTable.setStatus("current")
_CgprsCgTariffTimeEntry_Object = MibTableRow
cgprsCgTariffTimeEntry = _CgprsCgTariffTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 21, 1)
)
cgprsCgTariffTimeEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeIndex"),
)
if mibBuilder.loadTexts:
    cgprsCgTariffTimeEntry.setStatus("current")
_CgprsCgTariffTimeIndex_Type = Unsigned32
_CgprsCgTariffTimeIndex_Object = MibTableColumn
cgprsCgTariffTimeIndex = _CgprsCgTariffTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 21, 1, 1),
    _CgprsCgTariffTimeIndex_Type()
)
cgprsCgTariffTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeIndex.setStatus("current")
_CgprsCgTariffTimeRowStatus_Type = RowStatus
_CgprsCgTariffTimeRowStatus_Object = MibTableColumn
cgprsCgTariffTimeRowStatus = _CgprsCgTariffTimeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 21, 1, 2),
    _CgprsCgTariffTimeRowStatus_Type()
)
cgprsCgTariffTimeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeRowStatus.setStatus("current")


class _CgprsCgTariffTimeHour_Type(Unsigned32):
    """Custom type cgprsCgTariffTimeHour based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CgprsCgTariffTimeHour_Type.__name__ = "Unsigned32"
_CgprsCgTariffTimeHour_Object = MibTableColumn
cgprsCgTariffTimeHour = _CgprsCgTariffTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 21, 1, 3),
    _CgprsCgTariffTimeHour_Type()
)
cgprsCgTariffTimeHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeHour.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeHour.setUnits("hours")


class _CgprsCgTariffTimeMin_Type(Unsigned32):
    """Custom type cgprsCgTariffTimeMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CgprsCgTariffTimeMin_Type.__name__ = "Unsigned32"
_CgprsCgTariffTimeMin_Object = MibTableColumn
cgprsCgTariffTimeMin = _CgprsCgTariffTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 21, 1, 4),
    _CgprsCgTariffTimeMin_Type()
)
cgprsCgTariffTimeMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeMin.setUnits("minutes")


class _CgprsCgTariffTimeSec_Type(Unsigned32):
    """Custom type cgprsCgTariffTimeSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CgprsCgTariffTimeSec_Type.__name__ = "Unsigned32"
_CgprsCgTariffTimeSec_Object = MibTableColumn
cgprsCgTariffTimeSec = _CgprsCgTariffTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 21, 1, 5),
    _CgprsCgTariffTimeSec_Type()
)
cgprsCgTariffTimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeSec.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgTariffTimeSec.setUnits("seconds")
_CgprsCgGatewayTable_Object = MibTable
cgprsCgGatewayTable = _CgprsCgGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 22)
)
if mibBuilder.loadTexts:
    cgprsCgGatewayTable.setStatus("deprecated")
_CgprsCgGatewayEntry_Object = MibTableRow
cgprsCgGatewayEntry = _CgprsCgGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 22, 1)
)
cgprsCgGatewayEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayIndex"),
)
if mibBuilder.loadTexts:
    cgprsCgGatewayEntry.setStatus("deprecated")


class _CgprsCgGatewayIndex_Type(Integer32):
    """Custom type cgprsCgGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CgprsCgGatewayIndex_Type.__name__ = "Integer32"
_CgprsCgGatewayIndex_Object = MibTableColumn
cgprsCgGatewayIndex = _CgprsCgGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 22, 1, 1),
    _CgprsCgGatewayIndex_Type()
)
cgprsCgGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgGatewayIndex.setStatus("deprecated")
_CgprsCgGatewayAddrType_Type = InetAddressType
_CgprsCgGatewayAddrType_Object = MibTableColumn
cgprsCgGatewayAddrType = _CgprsCgGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 22, 1, 2),
    _CgprsCgGatewayAddrType_Type()
)
cgprsCgGatewayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGatewayAddrType.setStatus("deprecated")
_CgprsCgGatewayAddr_Type = InetAddress
_CgprsCgGatewayAddr_Object = MibTableColumn
cgprsCgGatewayAddr = _CgprsCgGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 22, 1, 3),
    _CgprsCgGatewayAddr_Type()
)
cgprsCgGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGatewayAddr.setStatus("deprecated")
_CgprsCgGatewayRowStatus_Type = RowStatus
_CgprsCgGatewayRowStatus_Object = MibTableColumn
cgprsCgGatewayRowStatus = _CgprsCgGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 22, 1, 4),
    _CgprsCgGatewayRowStatus_Type()
)
cgprsCgGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGatewayRowStatus.setStatus("deprecated")


class _CgprsCgOperStatus_Type(Integer32):
    """Custom type cgprsCgOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 3),
          ("undefined", 1))
    )


_CgprsCgOperStatus_Type.__name__ = "Integer32"
_CgprsCgOperStatus_Object = MibTableColumn
cgprsCgOperStatus = _CgprsCgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 22, 1, 5),
    _CgprsCgOperStatus_Type()
)
cgprsCgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgOperStatus.setStatus("deprecated")


class _CgprsCgLinkState_Type(Integer32):
    """Custom type cgprsCgLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("pending", 3))
    )


_CgprsCgLinkState_Type.__name__ = "Integer32"
_CgprsCgLinkState_Object = MibTableColumn
cgprsCgLinkState = _CgprsCgLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 22, 1, 6),
    _CgprsCgLinkState_Type()
)
cgprsCgLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgLinkState.setStatus("deprecated")


class _CgprsCgClearCdrPartialCdr_Type(Integer32):
    """Custom type cgprsCgClearCdrPartialCdr based on Integer32"""
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
        *(("canCloseCdr", 2),
          ("cannotCloseCdr", 3),
          ("closeCdr", 1),
          ("closingCdr", 4))
    )


_CgprsCgClearCdrPartialCdr_Type.__name__ = "Integer32"
_CgprsCgClearCdrPartialCdr_Object = MibScalar
cgprsCgClearCdrPartialCdr = _CgprsCgClearCdrPartialCdr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 23),
    _CgprsCgClearCdrPartialCdr_Type()
)
cgprsCgClearCdrPartialCdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgClearCdrPartialCdr.setStatus("current")


class _CgprsCgSgsnChangeLimit_Type(Unsigned32):
    """Custom type cgprsCgSgsnChangeLimit based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CgprsCgSgsnChangeLimit_Type.__name__ = "Unsigned32"
_CgprsCgSgsnChangeLimit_Object = MibScalar
cgprsCgSgsnChangeLimit = _CgprsCgSgsnChangeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 24),
    _CgprsCgSgsnChangeLimit_Type()
)
cgprsCgSgsnChangeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgSgsnChangeLimit.setStatus("deprecated")


class _CgprsCgCdrSgsnChangeLimit_Type(Integer32):
    """Custom type cgprsCgCdrSgsnChangeLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_CgprsCgCdrSgsnChangeLimit_Type.__name__ = "Integer32"
_CgprsCgCdrSgsnChangeLimit_Object = MibScalar
cgprsCgCdrSgsnChangeLimit = _CgprsCgCdrSgsnChangeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 25),
    _CgprsCgCdrSgsnChangeLimit_Type()
)
cgprsCgCdrSgsnChangeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrSgsnChangeLimit.setStatus("current")


class _CgprsCgRelease_Type(Integer32):
    """Custom type cgprsCgRelease based on Integer32"""
    defaultValue = 2

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
        *(("release4", 3),
          ("release5", 4),
          ("release98", 1),
          ("release99", 2))
    )


_CgprsCgRelease_Type.__name__ = "Integer32"
_CgprsCgRelease_Object = MibScalar
cgprsCgRelease = _CgprsCgRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 26),
    _CgprsCgRelease_Type()
)
cgprsCgRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgRelease.setStatus("current")


class _CgprsCgGtpShortHeaderEnable_Type(TruthValue):
    """Custom type cgprsCgGtpShortHeaderEnable based on TruthValue"""


_CgprsCgGtpShortHeaderEnable_Object = MibScalar
cgprsCgGtpShortHeaderEnable = _CgprsCgGtpShortHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 27),
    _CgprsCgGtpShortHeaderEnable_Type()
)
cgprsCgGtpShortHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgGtpShortHeaderEnable.setStatus("current")


class _CgprsCgTransFormNumRespEnable_Type(TruthValue):
    """Custom type cgprsCgTransFormNumRespEnable based on TruthValue"""


_CgprsCgTransFormNumRespEnable_Object = MibScalar
cgprsCgTransFormNumRespEnable = _CgprsCgTransFormNumRespEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 28),
    _CgprsCgTransFormNumRespEnable_Type()
)
cgprsCgTransFormNumRespEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgTransFormNumRespEnable.setStatus("current")


class _CgprsCgContainerTimeLimit_Type(Unsigned32):
    """Custom type cgprsCgContainerTimeLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 4294967295),
    )


_CgprsCgContainerTimeLimit_Type.__name__ = "Unsigned32"
_CgprsCgContainerTimeLimit_Object = MibScalar
cgprsCgContainerTimeLimit = _CgprsCgContainerTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 29),
    _CgprsCgContainerTimeLimit_Type()
)
cgprsCgContainerTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgContainerTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgContainerTimeLimit.setUnits("seconds")
_CgprsCgProfileTable_Object = MibTable
cgprsCgProfileTable = _CgprsCgProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30)
)
if mibBuilder.loadTexts:
    cgprsCgProfileTable.setStatus("current")
_CgprsCgProfileEntry_Object = MibTableRow
cgprsCgProfileEntry = _CgprsCgProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1)
)
cgprsCgProfileEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileNum"),
)
if mibBuilder.loadTexts:
    cgprsCgProfileEntry.setStatus("current")


class _CgprsCgProfileNum_Type(Unsigned32):
    """Custom type cgprsCgProfileNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgprsCgProfileNum_Type.__name__ = "Unsigned32"
_CgprsCgProfileNum_Object = MibTableColumn
cgprsCgProfileNum = _CgprsCgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 1),
    _CgprsCgProfileNum_Type()
)
cgprsCgProfileNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgProfileNum.setStatus("current")
_CgprsCgProfileRowStatus_Type = RowStatus
_CgprsCgProfileRowStatus_Object = MibTableColumn
cgprsCgProfileRowStatus = _CgprsCgProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 2),
    _CgprsCgProfileRowStatus_Type()
)
cgprsCgProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileRowStatus.setStatus("current")


class _CgprsCgProfileDesc_Type(SnmpAdminString):
    """Custom type cgprsCgProfileDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 99),
    )


_CgprsCgProfileDesc_Type.__name__ = "SnmpAdminString"
_CgprsCgProfileDesc_Object = MibTableColumn
cgprsCgProfileDesc = _CgprsCgProfileDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 3),
    _CgprsCgProfileDesc_Type()
)
cgprsCgProfileDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileDesc.setStatus("current")


class _CgprsCgProfileCategory_Type(Integer32):
    """Custom type cgprsCgProfileCategory based on Integer32"""
    defaultValue = 3

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
        *(("flat", 1),
          ("hotRate", 0),
          ("normal", 3),
          ("prepaid", 2))
    )


_CgprsCgProfileCategory_Type.__name__ = "Integer32"
_CgprsCgProfileCategory_Object = MibTableColumn
cgprsCgProfileCategory = _CgprsCgProfileCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 4),
    _CgprsCgProfileCategory_Type()
)
cgprsCgProfileCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileCategory.setStatus("current")


class _CgprsCgProfileCdrSuppress_Type(TruthValue):
    """Custom type cgprsCgProfileCdrSuppress based on TruthValue"""


_CgprsCgProfileCdrSuppress_Object = MibTableColumn
cgprsCgProfileCdrSuppress = _CgprsCgProfileCdrSuppress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 5),
    _CgprsCgProfileCdrSuppress_Type()
)
cgprsCgProfileCdrSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileCdrSuppress.setStatus("current")


class _CgprsCgProfileVolumeLimit_Type(Unsigned32):
    """Custom type cgprsCgProfileVolumeLimit based on Unsigned32"""
    defaultValue = 1048576

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgProfileVolumeLimit_Type.__name__ = "Unsigned32"
_CgprsCgProfileVolumeLimit_Object = MibTableColumn
cgprsCgProfileVolumeLimit = _CgprsCgProfileVolumeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 6),
    _CgprsCgProfileVolumeLimit_Type()
)
cgprsCgProfileVolumeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileVolumeLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgProfileVolumeLimit.setUnits("bytes")


class _CgprsCgProfileVolumeLimitReset_Type(TruthValue):
    """Custom type cgprsCgProfileVolumeLimitReset based on TruthValue"""


_CgprsCgProfileVolumeLimitReset_Object = MibTableColumn
cgprsCgProfileVolumeLimitReset = _CgprsCgProfileVolumeLimitReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 7),
    _CgprsCgProfileVolumeLimitReset_Type()
)
cgprsCgProfileVolumeLimitReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileVolumeLimitReset.setStatus("current")


class _CgprsCgProfileDurLimit_Type(Unsigned32):
    """Custom type cgprsCgProfileDurLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 4294967295),
    )


_CgprsCgProfileDurLimit_Type.__name__ = "Unsigned32"
_CgprsCgProfileDurLimit_Object = MibTableColumn
cgprsCgProfileDurLimit = _CgprsCgProfileDurLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 8),
    _CgprsCgProfileDurLimit_Type()
)
cgprsCgProfileDurLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileDurLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgProfileDurLimit.setUnits("minutes")


class _CgprsCgProfileDurLimitReset_Type(TruthValue):
    """Custom type cgprsCgProfileDurLimitReset based on TruthValue"""


_CgprsCgProfileDurLimitReset_Object = MibTableColumn
cgprsCgProfileDurLimitReset = _CgprsCgProfileDurLimitReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 9),
    _CgprsCgProfileDurLimitReset_Type()
)
cgprsCgProfileDurLimitReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileDurLimitReset.setStatus("current")


class _CgprsCgProfileTariffTime_Type(TruthValue):
    """Custom type cgprsCgProfileTariffTime based on TruthValue"""


_CgprsCgProfileTariffTime_Object = MibTableColumn
cgprsCgProfileTariffTime = _CgprsCgProfileTariffTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 10),
    _CgprsCgProfileTariffTime_Type()
)
cgprsCgProfileTariffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileTariffTime.setStatus("current")


class _CgprsCgProfileSgsnChange_Type(Integer32):
    """Custom type cgprsCgProfileSgsnChange based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_CgprsCgProfileSgsnChange_Type.__name__ = "Integer32"
_CgprsCgProfileSgsnChange_Object = MibTableColumn
cgprsCgProfileSgsnChange = _CgprsCgProfileSgsnChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 11),
    _CgprsCgProfileSgsnChange_Type()
)
cgprsCgProfileSgsnChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileSgsnChange.setStatus("current")


class _CgprsCgProfileCdrSuppressPrepaid_Type(TruthValue):
    """Custom type cgprsCgProfileCdrSuppressPrepaid based on TruthValue"""


_CgprsCgProfileCdrSuppressPrepaid_Object = MibTableColumn
cgprsCgProfileCdrSuppressPrepaid = _CgprsCgProfileCdrSuppressPrepaid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 12),
    _CgprsCgProfileCdrSuppressPrepaid_Type()
)
cgprsCgProfileCdrSuppressPrepaid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileCdrSuppressPrepaid.setStatus("current")
_CgprsCgProfileContentDccaProfile_Type = SnmpAdminString
_CgprsCgProfileContentDccaProfile_Object = MibTableColumn
cgprsCgProfileContentDccaProfile = _CgprsCgProfileContentDccaProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 13),
    _CgprsCgProfileContentDccaProfile_Type()
)
cgprsCgProfileContentDccaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentDccaProfile.setStatus("deprecated")


class _CgprsCgProfileContentPostTime_Type(Unsigned32):
    """Custom type cgprsCgProfileContentPostTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 4294967295),
    )


_CgprsCgProfileContentPostTime_Type.__name__ = "Unsigned32"
_CgprsCgProfileContentPostTime_Object = MibTableColumn
cgprsCgProfileContentPostTime = _CgprsCgProfileContentPostTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 14),
    _CgprsCgProfileContentPostTime_Type()
)
cgprsCgProfileContentPostTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostTime.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostTime.setUnits("seconds")


class _CgprsCgProfileContentPostValTime_Type(Unsigned32):
    """Custom type cgprsCgProfileContentPostValTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 4294967295),
    )


_CgprsCgProfileContentPostValTime_Type.__name__ = "Unsigned32"
_CgprsCgProfileContentPostValTime_Object = MibTableColumn
cgprsCgProfileContentPostValTime = _CgprsCgProfileContentPostValTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 15),
    _CgprsCgProfileContentPostValTime_Type()
)
cgprsCgProfileContentPostValTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostValTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostValTime.setUnits("seconds")


class _CgprsCgProfileContentPostVolume_Type(Unsigned32):
    """Custom type cgprsCgProfileContentPostVolume based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgProfileContentPostVolume_Type.__name__ = "Unsigned32"
_CgprsCgProfileContentPostVolume_Object = MibTableColumn
cgprsCgProfileContentPostVolume = _CgprsCgProfileContentPostVolume_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 16),
    _CgprsCgProfileContentPostVolume_Type()
)
cgprsCgProfileContentPostVolume.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostVolume.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostVolume.setUnits("bytes")
_CgprsCgProfileContentRulebaseId_Type = SnmpAdminString
_CgprsCgProfileContentRulebaseId_Object = MibTableColumn
cgprsCgProfileContentRulebaseId = _CgprsCgProfileContentRulebaseId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 17),
    _CgprsCgProfileContentRulebaseId_Type()
)
cgprsCgProfileContentRulebaseId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentRulebaseId.setStatus("current")


class _CgprsCgProfileContentPostQosChange_Type(TruthValue):
    """Custom type cgprsCgProfileContentPostQosChange based on TruthValue"""


_CgprsCgProfileContentPostQosChange_Object = MibTableColumn
cgprsCgProfileContentPostQosChange = _CgprsCgProfileContentPostQosChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 18),
    _CgprsCgProfileContentPostQosChange_Type()
)
cgprsCgProfileContentPostQosChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostQosChange.setStatus("current")


class _CgprsCgProfileContentPostSgsnChange_Type(TruthValue):
    """Custom type cgprsCgProfileContentPostSgsnChange based on TruthValue"""


_CgprsCgProfileContentPostSgsnChange_Object = MibTableColumn
cgprsCgProfileContentPostSgsnChange = _CgprsCgProfileContentPostSgsnChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 19),
    _CgprsCgProfileContentPostSgsnChange_Type()
)
cgprsCgProfileContentPostSgsnChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostSgsnChange.setStatus("current")


class _CgprsCgProfileContentPostRatChange_Type(TruthValue):
    """Custom type cgprsCgProfileContentPostRatChange based on TruthValue"""


_CgprsCgProfileContentPostRatChange_Object = MibTableColumn
cgprsCgProfileContentPostRatChange = _CgprsCgProfileContentPostRatChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 20),
    _CgprsCgProfileContentPostRatChange_Type()
)
cgprsCgProfileContentPostRatChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostRatChange.setStatus("current")


class _CgprsCgProfileContentPostPlmnChange_Type(TruthValue):
    """Custom type cgprsCgProfileContentPostPlmnChange based on TruthValue"""


_CgprsCgProfileContentPostPlmnChange_Object = MibTableColumn
cgprsCgProfileContentPostPlmnChange = _CgprsCgProfileContentPostPlmnChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 21),
    _CgprsCgProfileContentPostPlmnChange_Type()
)
cgprsCgProfileContentPostPlmnChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostPlmnChange.setStatus("current")


class _CgprsCgProfileStorageType_Type(StorageType):
    """Custom type cgprsCgProfileStorageType based on StorageType"""


_CgprsCgProfileStorageType_Object = MibTableColumn
cgprsCgProfileStorageType = _CgprsCgProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 22),
    _CgprsCgProfileStorageType_Type()
)
cgprsCgProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileStorageType.setStatus("current")


class _CgprsCgProfileContentPostValidityTime_Type(Unsigned32):
    """Custom type cgprsCgProfileContentPostValidityTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(900, 4294967295),
    )


_CgprsCgProfileContentPostValidityTime_Type.__name__ = "Unsigned32"
_CgprsCgProfileContentPostValidityTime_Object = MibTableColumn
cgprsCgProfileContentPostValidityTime = _CgprsCgProfileContentPostValidityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 23),
    _CgprsCgProfileContentPostValidityTime_Type()
)
cgprsCgProfileContentPostValidityTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostValidityTime.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostValidityTime.setUnits("seconds")


class _CgprsCgProfileContentPostUserLocChange_Type(TruthValue):
    """Custom type cgprsCgProfileContentPostUserLocChange based on TruthValue"""


_CgprsCgProfileContentPostUserLocChange_Object = MibTableColumn
cgprsCgProfileContentPostUserLocChange = _CgprsCgProfileContentPostUserLocChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 24),
    _CgprsCgProfileContentPostUserLocChange_Type()
)
cgprsCgProfileContentPostUserLocChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentPostUserLocChange.setStatus("current")


class _CgprsCgProfileScdrEnable_Type(TruthValue):
    """Custom type cgprsCgProfileScdrEnable based on TruthValue"""


_CgprsCgProfileScdrEnable_Object = MibTableColumn
cgprsCgProfileScdrEnable = _CgprsCgProfileScdrEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 30, 1, 25),
    _CgprsCgProfileScdrEnable_Type()
)
cgprsCgProfileScdrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileScdrEnable.setStatus("current")
_CgprsCgProfileMapTable_Object = MibTable
cgprsCgProfileMapTable = _CgprsCgProfileMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 31)
)
if mibBuilder.loadTexts:
    cgprsCgProfileMapTable.setStatus("current")
_CgprsCgProfileMapEntry_Object = MibTableRow
cgprsCgProfileMapEntry = _CgprsCgProfileMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 31, 1)
)
cgprsCgProfileMapEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapCategory"),
)
if mibBuilder.loadTexts:
    cgprsCgProfileMapEntry.setStatus("current")


class _CgprsCgProfileMapCategory_Type(Integer32):
    """Custom type cgprsCgProfileMapCategory based on Integer32"""
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
        *(("any", 1),
          ("home", 2),
          ("roaming", 3),
          ("visitor", 4))
    )


_CgprsCgProfileMapCategory_Type.__name__ = "Integer32"
_CgprsCgProfileMapCategory_Object = MibTableColumn
cgprsCgProfileMapCategory = _CgprsCgProfileMapCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 31, 1, 1),
    _CgprsCgProfileMapCategory_Type()
)
cgprsCgProfileMapCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgProfileMapCategory.setStatus("current")


class _CgprsCgProfileMapNum_Type(Integer32):
    """Custom type cgprsCgProfileMapNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgprsCgProfileMapNum_Type.__name__ = "Integer32"
_CgprsCgProfileMapNum_Object = MibTableColumn
cgprsCgProfileMapNum = _CgprsCgProfileMapNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 31, 1, 2),
    _CgprsCgProfileMapNum_Type()
)
cgprsCgProfileMapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgProfileMapNum.setStatus("deprecated")


class _CgprsCgProfileMapOverride_Type(TruthValue):
    """Custom type cgprsCgProfileMapOverride based on TruthValue"""


_CgprsCgProfileMapOverride_Object = MibTableColumn
cgprsCgProfileMapOverride = _CgprsCgProfileMapOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 31, 1, 3),
    _CgprsCgProfileMapOverride_Type()
)
cgprsCgProfileMapOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgProfileMapOverride.setStatus("current")


class _CgprsCgProfileMapTrusted_Type(TruthValue):
    """Custom type cgprsCgProfileMapTrusted based on TruthValue"""


_CgprsCgProfileMapTrusted_Object = MibTableColumn
cgprsCgProfileMapTrusted = _CgprsCgProfileMapTrusted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 31, 1, 4),
    _CgprsCgProfileMapTrusted_Type()
)
cgprsCgProfileMapTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgProfileMapTrusted.setStatus("current")


class _CgprsCgProfileMapNumber_Type(Integer32):
    """Custom type cgprsCgProfileMapNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CgprsCgProfileMapNumber_Type.__name__ = "Integer32"
_CgprsCgProfileMapNumber_Object = MibTableColumn
cgprsCgProfileMapNumber = _CgprsCgProfileMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 31, 1, 5),
    _CgprsCgProfileMapNumber_Type()
)
cgprsCgProfileMapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgProfileMapNumber.setStatus("current")


class _CgprsCgChargingCharReject_Type(TruthValue):
    """Custom type cgprsCgChargingCharReject based on TruthValue"""


_CgprsCgChargingCharReject_Object = MibScalar
cgprsCgChargingCharReject = _CgprsCgChargingCharReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 32),
    _CgprsCgChargingCharReject_Type()
)
cgprsCgChargingCharReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgChargingCharReject.setStatus("current")


class _CgprsCgServiceMode_Type(Integer32):
    """Custom type cgprsCgServiceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 2),
          ("operational", 1))
    )


_CgprsCgServiceMode_Type.__name__ = "Integer32"
_CgprsCgServiceMode_Object = MibScalar
cgprsCgServiceMode = _CgprsCgServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 33),
    _CgprsCgServiceMode_Type()
)
cgprsCgServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgServiceMode.setStatus("deprecated")


class _CgprsCgPartialCdrGenEnable_Type(TruthValue):
    """Custom type cgprsCgPartialCdrGenEnable based on TruthValue"""


_CgprsCgPartialCdrGenEnable_Object = MibScalar
cgprsCgPartialCdrGenEnable = _CgprsCgPartialCdrGenEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 34),
    _CgprsCgPartialCdrGenEnable_Type()
)
cgprsCgPartialCdrGenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgPartialCdrGenEnable.setStatus("current")


class _CgprsCgSwitchOverPriority_Type(TruthValue):
    """Custom type cgprsCgSwitchOverPriority based on TruthValue"""


_CgprsCgSwitchOverPriority_Object = MibScalar
cgprsCgSwitchOverPriority = _CgprsCgSwitchOverPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 35),
    _CgprsCgSwitchOverPriority_Type()
)
cgprsCgSwitchOverPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgSwitchOverPriority.setStatus("deprecated")


class _CgprsCgCharSelectionMode_Type(TruthValue):
    """Custom type cgprsCgCharSelectionMode based on TruthValue"""


_CgprsCgCharSelectionMode_Object = MibScalar
cgprsCgCharSelectionMode = _CgprsCgCharSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 36),
    _CgprsCgCharSelectionMode_Type()
)
cgprsCgCharSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCharSelectionMode.setStatus("current")


class _CgprsCgReconnect_Type(Integer32):
    """Custom type cgprsCgReconnect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CgprsCgReconnect_Type.__name__ = "Integer32"
_CgprsCgReconnect_Object = MibScalar
cgprsCgReconnect = _CgprsCgReconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 37),
    _CgprsCgReconnect_Type()
)
cgprsCgReconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgReconnect.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgReconnect.setUnits("minutes")


class _CgprsCgPtcEnable_Type(TruthValue):
    """Custom type cgprsCgPtcEnable based on TruthValue"""


_CgprsCgPtcEnable_Object = MibScalar
cgprsCgPtcEnable = _CgprsCgPtcEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 38),
    _CgprsCgPtcEnable_Type()
)
cgprsCgPtcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgPtcEnable.setStatus("current")


class _CgprsCgPtcPossiblyDupEnable_Type(TruthValue):
    """Custom type cgprsCgPtcPossiblyDupEnable based on TruthValue"""


_CgprsCgPtcPossiblyDupEnable_Object = MibScalar
cgprsCgPtcPossiblyDupEnable = _CgprsCgPtcPossiblyDupEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 39),
    _CgprsCgPtcPossiblyDupEnable_Type()
)
cgprsCgPtcPossiblyDupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgPtcPossiblyDupEnable.setStatus("current")


class _CgprsCgCdrOptionServiceRecord_Type(Unsigned32):
    """Custom type cgprsCgCdrOptionServiceRecord based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CgprsCgCdrOptionServiceRecord_Type.__name__ = "Unsigned32"
_CgprsCgCdrOptionServiceRecord_Object = MibScalar
cgprsCgCdrOptionServiceRecord = _CgprsCgCdrOptionServiceRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 40),
    _CgprsCgCdrOptionServiceRecord_Type()
)
cgprsCgCdrOptionServiceRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionServiceRecord.setStatus("current")


class _CgprsCgPartialCdrGenEnableAll_Type(TruthValue):
    """Custom type cgprsCgPartialCdrGenEnableAll based on TruthValue"""


_CgprsCgPartialCdrGenEnableAll_Object = MibScalar
cgprsCgPartialCdrGenEnableAll = _CgprsCgPartialCdrGenEnableAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 41),
    _CgprsCgPartialCdrGenEnableAll_Type()
)
cgprsCgPartialCdrGenEnableAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgPartialCdrGenEnableAll.setStatus("current")


class _CgprsCgCdrOptionApn_Type(TruthValue):
    """Custom type cgprsCgCdrOptionApn based on TruthValue"""


_CgprsCgCdrOptionApn_Object = MibScalar
cgprsCgCdrOptionApn = _CgprsCgCdrOptionApn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 42),
    _CgprsCgCdrOptionApn_Type()
)
cgprsCgCdrOptionApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionApn.setStatus("current")


class _CgprsCgCdrOptionVirtualApn_Type(TruthValue):
    """Custom type cgprsCgCdrOptionVirtualApn based on TruthValue"""


_CgprsCgCdrOptionVirtualApn_Object = MibScalar
cgprsCgCdrOptionVirtualApn = _CgprsCgCdrOptionVirtualApn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 43),
    _CgprsCgCdrOptionVirtualApn_Type()
)
cgprsCgCdrOptionVirtualApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionVirtualApn.setStatus("current")


class _CgprsCgCdrOptionApnSelMode_Type(TruthValue):
    """Custom type cgprsCgCdrOptionApnSelMode based on TruthValue"""


_CgprsCgCdrOptionApnSelMode_Object = MibScalar
cgprsCgCdrOptionApnSelMode = _CgprsCgCdrOptionApnSelMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 44),
    _CgprsCgCdrOptionApnSelMode_Type()
)
cgprsCgCdrOptionApnSelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionApnSelMode.setStatus("current")


class _CgprsCgCdrOptionDynamicAddr_Type(TruthValue):
    """Custom type cgprsCgCdrOptionDynamicAddr based on TruthValue"""


_CgprsCgCdrOptionDynamicAddr_Object = MibScalar
cgprsCgCdrOptionDynamicAddr = _CgprsCgCdrOptionDynamicAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 45),
    _CgprsCgCdrOptionDynamicAddr_Type()
)
cgprsCgCdrOptionDynamicAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionDynamicAddr.setStatus("current")


class _CgprsCgCdrOptionNip_Type(TruthValue):
    """Custom type cgprsCgCdrOptionNip based on TruthValue"""


_CgprsCgCdrOptionNip_Object = MibScalar
cgprsCgCdrOptionNip = _CgprsCgCdrOptionNip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 46),
    _CgprsCgCdrOptionNip_Type()
)
cgprsCgCdrOptionNip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionNip.setStatus("current")


class _CgprsCgCdrOptionPdpAddress_Type(TruthValue):
    """Custom type cgprsCgCdrOptionPdpAddress based on TruthValue"""


_CgprsCgCdrOptionPdpAddress_Object = MibScalar
cgprsCgCdrOptionPdpAddress = _CgprsCgCdrOptionPdpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 47),
    _CgprsCgCdrOptionPdpAddress_Type()
)
cgprsCgCdrOptionPdpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionPdpAddress.setStatus("current")


class _CgprsCgCdrOptionPdpType_Type(TruthValue):
    """Custom type cgprsCgCdrOptionPdpType based on TruthValue"""


_CgprsCgCdrOptionPdpType_Object = MibScalar
cgprsCgCdrOptionPdpType = _CgprsCgCdrOptionPdpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 48),
    _CgprsCgCdrOptionPdpType_Type()
)
cgprsCgCdrOptionPdpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionPdpType.setStatus("current")


class _CgprsCgCdrOptionSerMsisdn_Type(TruthValue):
    """Custom type cgprsCgCdrOptionSerMsisdn based on TruthValue"""


_CgprsCgCdrOptionSerMsisdn_Object = MibScalar
cgprsCgCdrOptionSerMsisdn = _CgprsCgCdrOptionSerMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 49),
    _CgprsCgCdrOptionSerMsisdn_Type()
)
cgprsCgCdrOptionSerMsisdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionSerMsisdn.setStatus("current")


class _CgprsCgCdrOptionSgsnPlmn_Type(TruthValue):
    """Custom type cgprsCgCdrOptionSgsnPlmn based on TruthValue"""


_CgprsCgCdrOptionSgsnPlmn_Object = MibScalar
cgprsCgCdrOptionSgsnPlmn = _CgprsCgCdrOptionSgsnPlmn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 50),
    _CgprsCgCdrOptionSgsnPlmn_Type()
)
cgprsCgCdrOptionSgsnPlmn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionSgsnPlmn.setStatus("current")


class _CgprsCgCdrOptionCamelCharInfo_Type(TruthValue):
    """Custom type cgprsCgCdrOptionCamelCharInfo based on TruthValue"""


_CgprsCgCdrOptionCamelCharInfo_Object = MibScalar
cgprsCgCdrOptionCamelCharInfo = _CgprsCgCdrOptionCamelCharInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 51),
    _CgprsCgCdrOptionCamelCharInfo_Type()
)
cgprsCgCdrOptionCamelCharInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionCamelCharInfo.setStatus("current")


class _CgprsCgCdrOptionImeisv_Type(TruthValue):
    """Custom type cgprsCgCdrOptionImeisv based on TruthValue"""


_CgprsCgCdrOptionImeisv_Object = MibScalar
cgprsCgCdrOptionImeisv = _CgprsCgCdrOptionImeisv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 52),
    _CgprsCgCdrOptionImeisv_Type()
)
cgprsCgCdrOptionImeisv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionImeisv.setStatus("current")


class _CgprsCgCdrOptionMsTimeZone_Type(TruthValue):
    """Custom type cgprsCgCdrOptionMsTimeZone based on TruthValue"""


_CgprsCgCdrOptionMsTimeZone_Object = MibScalar
cgprsCgCdrOptionMsTimeZone = _CgprsCgCdrOptionMsTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 53),
    _CgprsCgCdrOptionMsTimeZone_Type()
)
cgprsCgCdrOptionMsTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionMsTimeZone.setStatus("current")


class _CgprsCgCdrOptionRatType_Type(TruthValue):
    """Custom type cgprsCgCdrOptionRatType based on TruthValue"""


_CgprsCgCdrOptionRatType_Object = MibScalar
cgprsCgCdrOptionRatType = _CgprsCgCdrOptionRatType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 54),
    _CgprsCgCdrOptionRatType_Type()
)
cgprsCgCdrOptionRatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionRatType.setStatus("current")


class _CgprsCgCdrOptionUserLocInfo_Type(TruthValue):
    """Custom type cgprsCgCdrOptionUserLocInfo based on TruthValue"""


_CgprsCgCdrOptionUserLocInfo_Object = MibScalar
cgprsCgCdrOptionUserLocInfo = _CgprsCgCdrOptionUserLocInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 55),
    _CgprsCgCdrOptionUserLocInfo_Type()
)
cgprsCgCdrOptionUserLocInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgCdrOptionUserLocInfo.setStatus("current")


class _CgprsCgServiceRecordIncludeRat_Type(TruthValue):
    """Custom type cgprsCgServiceRecordIncludeRat based on TruthValue"""


_CgprsCgServiceRecordIncludeRat_Object = MibScalar
cgprsCgServiceRecordIncludeRat = _CgprsCgServiceRecordIncludeRat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 56),
    _CgprsCgServiceRecordIncludeRat_Type()
)
cgprsCgServiceRecordIncludeRat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgServiceRecordIncludeRat.setStatus("current")


class _CgprsCgServiceRecordIncludePlmn_Type(TruthValue):
    """Custom type cgprsCgServiceRecordIncludePlmn based on TruthValue"""


_CgprsCgServiceRecordIncludePlmn_Object = MibScalar
cgprsCgServiceRecordIncludePlmn = _CgprsCgServiceRecordIncludePlmn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 57),
    _CgprsCgServiceRecordIncludePlmn_Type()
)
cgprsCgServiceRecordIncludePlmn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgServiceRecordIncludePlmn.setStatus("current")


class _CgprsCgChargingSrcInterface_Type(Integer32):
    """Custom type cgprsCgChargingSrcInterface based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CgprsCgChargingSrcInterface_Type.__name__ = "Integer32"
_CgprsCgChargingSrcInterface_Object = MibScalar
cgprsCgChargingSrcInterface = _CgprsCgChargingSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 58),
    _CgprsCgChargingSrcInterface_Type()
)
cgprsCgChargingSrcInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgChargingSrcInterface.setStatus("current")


class _CgprsCgServiceRecordIncludeUserLocInfo_Type(TruthValue):
    """Custom type cgprsCgServiceRecordIncludeUserLocInfo based on TruthValue"""


_CgprsCgServiceRecordIncludeUserLocInfo_Object = MibScalar
cgprsCgServiceRecordIncludeUserLocInfo = _CgprsCgServiceRecordIncludeUserLocInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 59),
    _CgprsCgServiceRecordIncludeUserLocInfo_Type()
)
cgprsCgServiceRecordIncludeUserLocInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgServiceRecordIncludeUserLocInfo.setStatus("current")
_CgprsCgGroupTable_Object = MibTable
cgprsCgGroupTable = _CgprsCgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 60)
)
if mibBuilder.loadTexts:
    cgprsCgGroupTable.setStatus("current")
_CgprsCgGroupEntry_Object = MibTableRow
cgprsCgGroupEntry = _CgprsCgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 60, 1)
)
cgprsCgGroupEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupIndex"),
)
if mibBuilder.loadTexts:
    cgprsCgGroupEntry.setStatus("current")


class _CgprsCgGroupIndex_Type(Integer32):
    """Custom type cgprsCgGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_CgprsCgGroupIndex_Type.__name__ = "Integer32"
_CgprsCgGroupIndex_Object = MibTableColumn
cgprsCgGroupIndex = _CgprsCgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 60, 1, 1),
    _CgprsCgGroupIndex_Type()
)
cgprsCgGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgGroupIndex.setStatus("current")
_CgprsCgGroupIscsi_Type = SnmpAdminString
_CgprsCgGroupIscsi_Object = MibTableColumn
cgprsCgGroupIscsi = _CgprsCgGroupIscsi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 60, 1, 2),
    _CgprsCgGroupIscsi_Type()
)
cgprsCgGroupIscsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGroupIscsi.setStatus("current")


class _CgprsCgGroupServiceMode_Type(Integer32):
    """Custom type cgprsCgGroupServiceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 2),
          ("operational", 1))
    )


_CgprsCgGroupServiceMode_Type.__name__ = "Integer32"
_CgprsCgGroupServiceMode_Object = MibTableColumn
cgprsCgGroupServiceMode = _CgprsCgGroupServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 60, 1, 3),
    _CgprsCgGroupServiceMode_Type()
)
cgprsCgGroupServiceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGroupServiceMode.setStatus("current")


class _CgprsCgGroupSwitchOverPriority_Type(TruthValue):
    """Custom type cgprsCgGroupSwitchOverPriority based on TruthValue"""


_CgprsCgGroupSwitchOverPriority_Object = MibTableColumn
cgprsCgGroupSwitchOverPriority = _CgprsCgGroupSwitchOverPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 60, 1, 4),
    _CgprsCgGroupSwitchOverPriority_Type()
)
cgprsCgGroupSwitchOverPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGroupSwitchOverPriority.setStatus("current")
_CgprsCgGroupRowStatus_Type = RowStatus
_CgprsCgGroupRowStatus_Object = MibTableColumn
cgprsCgGroupRowStatus = _CgprsCgGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 60, 1, 5),
    _CgprsCgGroupRowStatus_Type()
)
cgprsCgGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGroupRowStatus.setStatus("current")
_CgprsCgGatewayIpTable_Object = MibTable
cgprsCgGatewayIpTable = _CgprsCgGatewayIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61)
)
if mibBuilder.loadTexts:
    cgprsCgGatewayIpTable.setStatus("current")
_CgprsCgGatewayIpEntry_Object = MibTableRow
cgprsCgGatewayIpEntry = _CgprsCgGatewayIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61, 1)
)
cgprsCgGatewayIpEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupIndex"),
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayIpIndex"),
)
if mibBuilder.loadTexts:
    cgprsCgGatewayIpEntry.setStatus("current")


class _CgprsCgGatewayIpIndex_Type(Unsigned32):
    """Custom type cgprsCgGatewayIpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgGatewayIpIndex_Type.__name__ = "Unsigned32"
_CgprsCgGatewayIpIndex_Object = MibTableColumn
cgprsCgGatewayIpIndex = _CgprsCgGatewayIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61, 1, 1),
    _CgprsCgGatewayIpIndex_Type()
)
cgprsCgGatewayIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgGatewayIpIndex.setStatus("current")
_CgprsCgGatewayIpAddrType_Type = InetAddressType
_CgprsCgGatewayIpAddrType_Object = MibTableColumn
cgprsCgGatewayIpAddrType = _CgprsCgGatewayIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61, 1, 2),
    _CgprsCgGatewayIpAddrType_Type()
)
cgprsCgGatewayIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGatewayIpAddrType.setStatus("current")
_CgprsCgGatewayIpAddr_Type = InetAddress
_CgprsCgGatewayIpAddr_Object = MibTableColumn
cgprsCgGatewayIpAddr = _CgprsCgGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61, 1, 3),
    _CgprsCgGatewayIpAddr_Type()
)
cgprsCgGatewayIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGatewayIpAddr.setStatus("current")


class _CgprsCgGatewayOperStatus_Type(Integer32):
    """Custom type cgprsCgGatewayOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 3),
          ("undefined", 1))
    )


_CgprsCgGatewayOperStatus_Type.__name__ = "Integer32"
_CgprsCgGatewayOperStatus_Object = MibTableColumn
cgprsCgGatewayOperStatus = _CgprsCgGatewayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61, 1, 4),
    _CgprsCgGatewayOperStatus_Type()
)
cgprsCgGatewayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayOperStatus.setStatus("current")


class _CgprsCgGatewayLinkState_Type(Integer32):
    """Custom type cgprsCgGatewayLinkState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("pending", 3))
    )


_CgprsCgGatewayLinkState_Type.__name__ = "Integer32"
_CgprsCgGatewayLinkState_Object = MibTableColumn
cgprsCgGatewayLinkState = _CgprsCgGatewayLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61, 1, 5),
    _CgprsCgGatewayLinkState_Type()
)
cgprsCgGatewayLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayLinkState.setStatus("current")
_CgprsCgGateway_Type = CgprsCgGatewayType
_CgprsCgGateway_Object = MibTableColumn
cgprsCgGateway = _CgprsCgGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61, 1, 6),
    _CgprsCgGateway_Type()
)
cgprsCgGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGateway.setStatus("current")
_CgprsCgGatewayIpRowStatus_Type = RowStatus
_CgprsCgGatewayIpRowStatus_Object = MibTableColumn
cgprsCgGatewayIpRowStatus = _CgprsCgGatewayIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 61, 1, 7),
    _CgprsCgGatewayIpRowStatus_Type()
)
cgprsCgGatewayIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgGatewayIpRowStatus.setStatus("current")
_CgprsCgProfileContentDccaProfileTable_Object = MibTable
cgprsCgProfileContentDccaProfileTable = _CgprsCgProfileContentDccaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 62)
)
if mibBuilder.loadTexts:
    cgprsCgProfileContentDccaProfileTable.setStatus("current")
_CgprsCgProfileContentDccaProfileEntry_Object = MibTableRow
cgprsCgProfileContentDccaProfileEntry = _CgprsCgProfileContentDccaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 62, 1)
)
cgprsCgProfileContentDccaProfileEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileNum"),
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentDccaProfileName"),
)
if mibBuilder.loadTexts:
    cgprsCgProfileContentDccaProfileEntry.setStatus("current")


class _CgprsCgProfileContentDccaProfileName_Type(SnmpAdminString):
    """Custom type cgprsCgProfileContentDccaProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CgprsCgProfileContentDccaProfileName_Type.__name__ = "SnmpAdminString"
_CgprsCgProfileContentDccaProfileName_Object = MibTableColumn
cgprsCgProfileContentDccaProfileName = _CgprsCgProfileContentDccaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 62, 1, 1),
    _CgprsCgProfileContentDccaProfileName_Type()
)
cgprsCgProfileContentDccaProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgProfileContentDccaProfileName.setStatus("current")
_CgprsCgProfileContentDccaProfileRowStatus_Type = RowStatus
_CgprsCgProfileContentDccaProfileRowStatus_Object = MibTableColumn
cgprsCgProfileContentDccaProfileRowStatus = _CgprsCgProfileContentDccaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 62, 1, 2),
    _CgprsCgProfileContentDccaProfileRowStatus_Type()
)
cgprsCgProfileContentDccaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentDccaProfileRowStatus.setStatus("current")


class _CgprsCgProfileContentDccaProfileWeight_Type(Unsigned32):
    """Custom type cgprsCgProfileContentDccaProfileWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CgprsCgProfileContentDccaProfileWeight_Type.__name__ = "Unsigned32"
_CgprsCgProfileContentDccaProfileWeight_Object = MibTableColumn
cgprsCgProfileContentDccaProfileWeight = _CgprsCgProfileContentDccaProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 62, 1, 3),
    _CgprsCgProfileContentDccaProfileWeight_Type()
)
cgprsCgProfileContentDccaProfileWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsCgProfileContentDccaProfileWeight.setStatus("current")


class _CgprsCgScdrEnable_Type(TruthValue):
    """Custom type cgprsCgScdrEnable based on TruthValue"""


_CgprsCgScdrEnable_Object = MibScalar
cgprsCgScdrEnable = _CgprsCgScdrEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 1, 63),
    _CgprsCgScdrEnable_Type()
)
cgprsCgScdrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgScdrEnable.setStatus("current")
_CiscoGprsChargingOthers_ObjectIdentity = ObjectIdentity
ciscoGprsChargingOthers = _CiscoGprsChargingOthers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 2)
)
_CiscoGprsChargingStats_ObjectIdentity = ObjectIdentity
ciscoGprsChargingStats = _CiscoGprsChargingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3)
)
_CgprsCgDownTimes_Type = Counter32
_CgprsCgDownTimes_Object = MibScalar
cgprsCgDownTimes = _CgprsCgDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 1),
    _CgprsCgDownTimes_Type()
)
cgprsCgDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgDownTimes.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgDownTimes.setUnits("transitions")
_CgprsCgAccPtNum_Type = Counter32
_CgprsCgAccPtNum_Object = MibScalar
cgprsCgAccPtNum = _CgprsCgAccPtNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 2),
    _CgprsCgAccPtNum_Type()
)
cgprsCgAccPtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgAccPtNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgAccPtNum.setUnits("access-points")
_CgprsCgCdrOpenedNum_Type = Gauge32
_CgprsCgCdrOpenedNum_Object = MibScalar
cgprsCgCdrOpenedNum = _CgprsCgCdrOpenedNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 3),
    _CgprsCgCdrOpenedNum_Type()
)
cgprsCgCdrOpenedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgCdrOpenedNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgCdrOpenedNum.setUnits("CDRs")
_CgprsCgCdrClosedNum_Type = Gauge32
_CgprsCgCdrClosedNum_Object = MibScalar
cgprsCgCdrClosedNum = _CgprsCgCdrClosedNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 4),
    _CgprsCgCdrClosedNum_Type()
)
cgprsCgCdrClosedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgCdrClosedNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgCdrClosedNum.setUnits("CDRs")
_CgprsCgContainerNum_Type = Gauge32
_CgprsCgContainerNum_Object = MibScalar
cgprsCgContainerNum = _CgprsCgContainerNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 5),
    _CgprsCgContainerNum_Type()
)
cgprsCgContainerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgContainerNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgContainerNum.setUnits("containers")
_CgprsCgPendingMsgNum_Type = Gauge32
_CgprsCgPendingMsgNum_Object = MibScalar
cgprsCgPendingMsgNum = _CgprsCgPendingMsgNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 6),
    _CgprsCgPendingMsgNum_Type()
)
cgprsCgPendingMsgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgPendingMsgNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgPendingMsgNum.setUnits("messages")
_CgprsCgSentMsgNum_Type = Counter32
_CgprsCgSentMsgNum_Object = MibScalar
cgprsCgSentMsgNum = _CgprsCgSentMsgNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 7),
    _CgprsCgSentMsgNum_Type()
)
cgprsCgSentMsgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgSentMsgNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgSentMsgNum.setUnits("messages")
_CgprsCgTotalCdrOpened_Type = Counter32
_CgprsCgTotalCdrOpened_Object = MibScalar
cgprsCgTotalCdrOpened = _CgprsCgTotalCdrOpened_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 8),
    _CgprsCgTotalCdrOpened_Type()
)
cgprsCgTotalCdrOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgTotalCdrOpened.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgTotalCdrOpened.setUnits("CDRs")
_CgprsCgTotalContainerCreated_Type = Counter32
_CgprsCgTotalContainerCreated_Object = MibScalar
cgprsCgTotalContainerCreated = _CgprsCgTotalContainerCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 9),
    _CgprsCgTotalContainerCreated_Type()
)
cgprsCgTotalContainerCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgTotalContainerCreated.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgTotalContainerCreated.setUnits("containers")
_CgprsCgTotalServiceRecords_Type = Counter32
_CgprsCgTotalServiceRecords_Object = MibScalar
cgprsCgTotalServiceRecords = _CgprsCgTotalServiceRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 10),
    _CgprsCgTotalServiceRecords_Type()
)
cgprsCgTotalServiceRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgTotalServiceRecords.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgTotalServiceRecords.setUnits("records")
_CgprsCgGatewayGroupStatisticsTable_Object = MibTable
cgprsCgGatewayGroupStatisticsTable = _CgprsCgGatewayGroupStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11)
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupStatisticsTable.setStatus("current")
_CgprsCgGatewayGroupStatisticsEntry_Object = MibTableRow
cgprsCgGatewayGroupStatisticsEntry = _CgprsCgGatewayGroupStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1)
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupStatisticsEntry.setStatus("current")
_CgprsCgGatewayGroupCgDownTimes_Type = Counter32
_CgprsCgGatewayGroupCgDownTimes_Object = MibTableColumn
cgprsCgGatewayGroupCgDownTimes = _CgprsCgGatewayGroupCgDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 1),
    _CgprsCgGatewayGroupCgDownTimes_Type()
)
cgprsCgGatewayGroupCgDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCgDownTimes.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCgDownTimes.setUnits("transitions")
_CgprsCgGatewayGroupAccPtNum_Type = Counter32
_CgprsCgGatewayGroupAccPtNum_Object = MibTableColumn
cgprsCgGatewayGroupAccPtNum = _CgprsCgGatewayGroupAccPtNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 2),
    _CgprsCgGatewayGroupAccPtNum_Type()
)
cgprsCgGatewayGroupAccPtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAccPtNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAccPtNum.setUnits("access-points")


class _CgprsCgGatewayGroupCdrOpenedNum_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupCdrOpenedNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgprsCgGatewayGroupCdrOpenedNum_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupCdrOpenedNum_Object = MibTableColumn
cgprsCgGatewayGroupCdrOpenedNum = _CgprsCgGatewayGroupCdrOpenedNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 3),
    _CgprsCgGatewayGroupCdrOpenedNum_Type()
)
cgprsCgGatewayGroupCdrOpenedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrOpenedNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrOpenedNum.setUnits("CDRs")


class _CgprsCgGatewayGroupCdrClosedNum_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupCdrClosedNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgprsCgGatewayGroupCdrClosedNum_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupCdrClosedNum_Object = MibTableColumn
cgprsCgGatewayGroupCdrClosedNum = _CgprsCgGatewayGroupCdrClosedNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 4),
    _CgprsCgGatewayGroupCdrClosedNum_Type()
)
cgprsCgGatewayGroupCdrClosedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrClosedNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrClosedNum.setUnits("CDRs")


class _CgprsCgGatewayGroupContainerNum_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupContainerNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgprsCgGatewayGroupContainerNum_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupContainerNum_Object = MibTableColumn
cgprsCgGatewayGroupContainerNum = _CgprsCgGatewayGroupContainerNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 5),
    _CgprsCgGatewayGroupContainerNum_Type()
)
cgprsCgGatewayGroupContainerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupContainerNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupContainerNum.setUnits("containers")


class _CgprsCgGatewayGroupServiceRecordsNum_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupServiceRecordsNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgprsCgGatewayGroupServiceRecordsNum_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupServiceRecordsNum_Object = MibTableColumn
cgprsCgGatewayGroupServiceRecordsNum = _CgprsCgGatewayGroupServiceRecordsNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 6),
    _CgprsCgGatewayGroupServiceRecordsNum_Type()
)
cgprsCgGatewayGroupServiceRecordsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupServiceRecordsNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupServiceRecordsNum.setUnits("records")


class _CgprsCgGatewayGroupPendingMsgNum_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupPendingMsgNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgprsCgGatewayGroupPendingMsgNum_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupPendingMsgNum_Object = MibTableColumn
cgprsCgGatewayGroupPendingMsgNum = _CgprsCgGatewayGroupPendingMsgNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 7),
    _CgprsCgGatewayGroupPendingMsgNum_Type()
)
cgprsCgGatewayGroupPendingMsgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupPendingMsgNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupPendingMsgNum.setUnits("messages")


class _CgprsCgGatewayGroupCdrPendingMsgIscsiNum_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupCdrPendingMsgIscsiNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgprsCgGatewayGroupCdrPendingMsgIscsiNum_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupCdrPendingMsgIscsiNum_Object = MibTableColumn
cgprsCgGatewayGroupCdrPendingMsgIscsiNum = _CgprsCgGatewayGroupCdrPendingMsgIscsiNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 8),
    _CgprsCgGatewayGroupCdrPendingMsgIscsiNum_Type()
)
cgprsCgGatewayGroupCdrPendingMsgIscsiNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrPendingMsgIscsiNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrPendingMsgIscsiNum.setUnits("messages")


class _CgprsCgGatewayGroupCdrPendingMsgCgPathNum_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupCdrPendingMsgCgPathNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgprsCgGatewayGroupCdrPendingMsgCgPathNum_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupCdrPendingMsgCgPathNum_Object = MibTableColumn
cgprsCgGatewayGroupCdrPendingMsgCgPathNum = _CgprsCgGatewayGroupCdrPendingMsgCgPathNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 9),
    _CgprsCgGatewayGroupCdrPendingMsgCgPathNum_Type()
)
cgprsCgGatewayGroupCdrPendingMsgCgPathNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrPendingMsgCgPathNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrPendingMsgCgPathNum.setUnits("messages")


class _CgprsCgGatewayGroupCdrPendingMsgMaintNum_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupCdrPendingMsgMaintNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgprsCgGatewayGroupCdrPendingMsgMaintNum_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupCdrPendingMsgMaintNum_Object = MibTableColumn
cgprsCgGatewayGroupCdrPendingMsgMaintNum = _CgprsCgGatewayGroupCdrPendingMsgMaintNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 10),
    _CgprsCgGatewayGroupCdrPendingMsgMaintNum_Type()
)
cgprsCgGatewayGroupCdrPendingMsgMaintNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrPendingMsgMaintNum.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupCdrPendingMsgMaintNum.setUnits("messages")
_CgprsCgGatewayGroupTotalCdrOpened_Type = Counter32
_CgprsCgGatewayGroupTotalCdrOpened_Object = MibTableColumn
cgprsCgGatewayGroupTotalCdrOpened = _CgprsCgGatewayGroupTotalCdrOpened_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 11),
    _CgprsCgGatewayGroupTotalCdrOpened_Type()
)
cgprsCgGatewayGroupTotalCdrOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalCdrOpened.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalCdrOpened.setUnits("CDRs")
_CgprsCgGatewayGroupTotalContainerCreated_Type = Counter32
_CgprsCgGatewayGroupTotalContainerCreated_Object = MibTableColumn
cgprsCgGatewayGroupTotalContainerCreated = _CgprsCgGatewayGroupTotalContainerCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 12),
    _CgprsCgGatewayGroupTotalContainerCreated_Type()
)
cgprsCgGatewayGroupTotalContainerCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalContainerCreated.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalContainerCreated.setUnits("containers")
_CgprsCgGatewayGroupTotalServiceRecords_Type = Counter32
_CgprsCgGatewayGroupTotalServiceRecords_Object = MibTableColumn
cgprsCgGatewayGroupTotalServiceRecords = _CgprsCgGatewayGroupTotalServiceRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 13),
    _CgprsCgGatewayGroupTotalServiceRecords_Type()
)
cgprsCgGatewayGroupTotalServiceRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalServiceRecords.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalServiceRecords.setUnits("records")
_CgprsCgGatewayGroupTotalSentMsg_Type = Counter32
_CgprsCgGatewayGroupTotalSentMsg_Object = MibTableColumn
cgprsCgGatewayGroupTotalSentMsg = _CgprsCgGatewayGroupTotalSentMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 14),
    _CgprsCgGatewayGroupTotalSentMsg_Type()
)
cgprsCgGatewayGroupTotalSentMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalSentMsg.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalSentMsg.setUnits("messages")
_CgprsCgGatewayGroupTotalSentMsgToIscsi_Type = Counter32
_CgprsCgGatewayGroupTotalSentMsgToIscsi_Object = MibTableColumn
cgprsCgGatewayGroupTotalSentMsgToIscsi = _CgprsCgGatewayGroupTotalSentMsgToIscsi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 15),
    _CgprsCgGatewayGroupTotalSentMsgToIscsi_Type()
)
cgprsCgGatewayGroupTotalSentMsgToIscsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalSentMsgToIscsi.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalSentMsgToIscsi.setUnits("messages")
_CgprsCgGatewayGroupTotalSentMsgToCg_Type = Counter32
_CgprsCgGatewayGroupTotalSentMsgToCg_Object = MibTableColumn
cgprsCgGatewayGroupTotalSentMsgToCg = _CgprsCgGatewayGroupTotalSentMsgToCg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 3, 11, 1, 16),
    _CgprsCgGatewayGroupTotalSentMsgToCg_Type()
)
cgprsCgGatewayGroupTotalSentMsgToCg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalSentMsgToCg.setStatus("current")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupTotalSentMsgToCg.setUnits("messages")
_CiscoGprsChargingAlarms_ObjectIdentity = ObjectIdentity
ciscoGprsChargingAlarms = _CiscoGprsChargingAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4)
)
_CgprsCgAlarmEnable_Type = TruthValue
_CgprsCgAlarmEnable_Object = MibScalar
cgprsCgAlarmEnable = _CgprsCgAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 1),
    _CgprsCgAlarmEnable_Type()
)
cgprsCgAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgAlarmEnable.setStatus("deprecated")


class _CgprsCgAlarmHistTableMax_Type(Unsigned32):
    """Custom type cgprsCgAlarmHistTableMax based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgAlarmHistTableMax_Type.__name__ = "Unsigned32"
_CgprsCgAlarmHistTableMax_Object = MibScalar
cgprsCgAlarmHistTableMax = _CgprsCgAlarmHistTableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 2),
    _CgprsCgAlarmHistTableMax_Type()
)
cgprsCgAlarmHistTableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgAlarmHistTableMax.setStatus("current")
_CgprsCgAlarmHistTable_Object = MibTable
cgprsCgAlarmHistTable = _CgprsCgAlarmHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cgprsCgAlarmHistTable.setStatus("deprecated")
_CgprsCgAlarmHistEntry_Object = MibTableRow
cgprsCgAlarmHistEntry = _CgprsCgAlarmHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 3, 1)
)
cgprsCgAlarmHistEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistIndex"),
)
if mibBuilder.loadTexts:
    cgprsCgAlarmHistEntry.setStatus("deprecated")


class _CgprsCgAlarmHistIndex_Type(Unsigned32):
    """Custom type cgprsCgAlarmHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgAlarmHistIndex_Type.__name__ = "Unsigned32"
_CgprsCgAlarmHistIndex_Object = MibTableColumn
cgprsCgAlarmHistIndex = _CgprsCgAlarmHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 3, 1, 1),
    _CgprsCgAlarmHistIndex_Type()
)
cgprsCgAlarmHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgAlarmHistIndex.setStatus("deprecated")
_CgprsCgAlarmHistType_Type = CgprsCgAlarmType
_CgprsCgAlarmHistType_Object = MibTableColumn
cgprsCgAlarmHistType = _CgprsCgAlarmHistType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 3, 1, 2),
    _CgprsCgAlarmHistType_Type()
)
cgprsCgAlarmHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgAlarmHistType.setStatus("deprecated")
_CgprsCgAlarmHistAddrType_Type = InetAddressType
_CgprsCgAlarmHistAddrType_Object = MibTableColumn
cgprsCgAlarmHistAddrType = _CgprsCgAlarmHistAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 3, 1, 3),
    _CgprsCgAlarmHistAddrType_Type()
)
cgprsCgAlarmHistAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgAlarmHistAddrType.setStatus("deprecated")
_CgprsCgAlarmHistAddress_Type = InetAddress
_CgprsCgAlarmHistAddress_Object = MibTableColumn
cgprsCgAlarmHistAddress = _CgprsCgAlarmHistAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 3, 1, 4),
    _CgprsCgAlarmHistAddress_Type()
)
cgprsCgAlarmHistAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgAlarmHistAddress.setStatus("deprecated")
_CgprsCgAlarmHistSeverity_Type = CiscoAlarmSeverity
_CgprsCgAlarmHistSeverity_Object = MibTableColumn
cgprsCgAlarmHistSeverity = _CgprsCgAlarmHistSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 3, 1, 5),
    _CgprsCgAlarmHistSeverity_Type()
)
cgprsCgAlarmHistSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgAlarmHistSeverity.setStatus("deprecated")
_CgprsCgAlarmHistInfo_Type = SnmpAdminString
_CgprsCgAlarmHistInfo_Object = MibTableColumn
cgprsCgAlarmHistInfo = _CgprsCgAlarmHistInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 3, 1, 6),
    _CgprsCgAlarmHistInfo_Type()
)
cgprsCgAlarmHistInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgAlarmHistInfo.setStatus("deprecated")


class _CgprsCgAlarmHistLatestIndex_Type(Unsigned32):
    """Custom type cgprsCgAlarmHistLatestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgAlarmHistLatestIndex_Type.__name__ = "Unsigned32"
_CgprsCgAlarmHistLatestIndex_Object = MibScalar
cgprsCgAlarmHistLatestIndex = _CgprsCgAlarmHistLatestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 4),
    _CgprsCgAlarmHistLatestIndex_Type()
)
cgprsCgAlarmHistLatestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgAlarmHistLatestIndex.setStatus("current")
_CgprsCgGatewayGroupAlarmHistTable_Object = MibTable
cgprsCgGatewayGroupAlarmHistTable = _CgprsCgGatewayGroupAlarmHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmHistTable.setStatus("current")
_CgprsCgGatewayGroupAlarmHistEntry_Object = MibTableRow
cgprsCgGatewayGroupAlarmHistEntry = _CgprsCgGatewayGroupAlarmHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 5, 1)
)
cgprsCgGatewayGroupAlarmHistEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupIndex"),
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistIndex"),
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmHistEntry.setStatus("current")


class _CgprsCgGatewayGroupAlarmHistIndex_Type(Unsigned32):
    """Custom type cgprsCgGatewayGroupAlarmHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsCgGatewayGroupAlarmHistIndex_Type.__name__ = "Unsigned32"
_CgprsCgGatewayGroupAlarmHistIndex_Object = MibTableColumn
cgprsCgGatewayGroupAlarmHistIndex = _CgprsCgGatewayGroupAlarmHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 5, 1, 1),
    _CgprsCgGatewayGroupAlarmHistIndex_Type()
)
cgprsCgGatewayGroupAlarmHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmHistIndex.setStatus("current")
_CgprsCgGatewayGroupAlarmHistType_Type = CgprsCgAlarmType
_CgprsCgGatewayGroupAlarmHistType_Object = MibTableColumn
cgprsCgGatewayGroupAlarmHistType = _CgprsCgGatewayGroupAlarmHistType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 5, 1, 2),
    _CgprsCgGatewayGroupAlarmHistType_Type()
)
cgprsCgGatewayGroupAlarmHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmHistType.setStatus("current")
_CgprsCgGatewayGroupAlarmHistAddrType_Type = InetAddressType
_CgprsCgGatewayGroupAlarmHistAddrType_Object = MibTableColumn
cgprsCgGatewayGroupAlarmHistAddrType = _CgprsCgGatewayGroupAlarmHistAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 5, 1, 3),
    _CgprsCgGatewayGroupAlarmHistAddrType_Type()
)
cgprsCgGatewayGroupAlarmHistAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmHistAddrType.setStatus("current")
_CgprsCgGatewayGroupAlarmHistAddress_Type = InetAddress
_CgprsCgGatewayGroupAlarmHistAddress_Object = MibTableColumn
cgprsCgGatewayGroupAlarmHistAddress = _CgprsCgGatewayGroupAlarmHistAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 5, 1, 4),
    _CgprsCgGatewayGroupAlarmHistAddress_Type()
)
cgprsCgGatewayGroupAlarmHistAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmHistAddress.setStatus("current")
_CgprsCgGatewayGroupAlarmHistSeverity_Type = CiscoAlarmSeverity
_CgprsCgGatewayGroupAlarmHistSeverity_Object = MibTableColumn
cgprsCgGatewayGroupAlarmHistSeverity = _CgprsCgGatewayGroupAlarmHistSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 5, 1, 5),
    _CgprsCgGatewayGroupAlarmHistSeverity_Type()
)
cgprsCgGatewayGroupAlarmHistSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmHistSeverity.setStatus("current")
_CgprsCgGatewayGroupAlarmHistInfo_Type = SnmpAdminString
_CgprsCgGatewayGroupAlarmHistInfo_Object = MibTableColumn
cgprsCgGatewayGroupAlarmHistInfo = _CgprsCgGatewayGroupAlarmHistInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 5, 1, 6),
    _CgprsCgGatewayGroupAlarmHistInfo_Type()
)
cgprsCgGatewayGroupAlarmHistInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmHistInfo.setStatus("current")
_CgprsCgGatewayGroupAlarmEnable_Type = TruthValue
_CgprsCgGatewayGroupAlarmEnable_Object = MibScalar
cgprsCgGatewayGroupAlarmEnable = _CgprsCgGatewayGroupAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 4, 6),
    _CgprsCgGatewayGroupAlarmEnable_Type()
)
cgprsCgGatewayGroupAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmEnable.setStatus("current")
_CiscoGprsChargingStatus_ObjectIdentity = ObjectIdentity
ciscoGprsChargingStatus = _CiscoGprsChargingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5)
)
_CgprsCgActiveChgGatewayAddrType_Type = InetAddressType
_CgprsCgActiveChgGatewayAddrType_Object = MibScalar
cgprsCgActiveChgGatewayAddrType = _CgprsCgActiveChgGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5, 1),
    _CgprsCgActiveChgGatewayAddrType_Type()
)
cgprsCgActiveChgGatewayAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgActiveChgGatewayAddrType.setStatus("deprecated")
_CgprsCgActiveChgGatewayAddress_Type = InetAddress
_CgprsCgActiveChgGatewayAddress_Object = MibScalar
cgprsCgActiveChgGatewayAddress = _CgprsCgActiveChgGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5, 2),
    _CgprsCgActiveChgGatewayAddress_Type()
)
cgprsCgActiveChgGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgActiveChgGatewayAddress.setStatus("deprecated")
_CgprsCgOldChgGatewayAddress_Type = InetAddress
_CgprsCgOldChgGatewayAddress_Object = MibScalar
cgprsCgOldChgGatewayAddress = _CgprsCgOldChgGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5, 3),
    _CgprsCgOldChgGatewayAddress_Type()
)
cgprsCgOldChgGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgOldChgGatewayAddress.setStatus("deprecated")
_CgprsCgGatewayGroupStatusTable_Object = MibTable
cgprsCgGatewayGroupStatusTable = _CgprsCgGatewayGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupStatusTable.setStatus("current")
_CgprsCgGatewayGroupStatusEntry_Object = MibTableRow
cgprsCgGatewayGroupStatusEntry = _CgprsCgGatewayGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5, 4, 1)
)
cgprsCgGatewayGroupStatusEntry.setIndexNames(
    (0, "CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupIndex"),
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupStatusEntry.setStatus("current")
_CgprsCgGatewayGroupStatusAddrType_Type = InetAddressType
_CgprsCgGatewayGroupStatusAddrType_Object = MibTableColumn
cgprsCgGatewayGroupStatusAddrType = _CgprsCgGatewayGroupStatusAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5, 4, 1, 1),
    _CgprsCgGatewayGroupStatusAddrType_Type()
)
cgprsCgGatewayGroupStatusAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupStatusAddrType.setStatus("current")
_CgprsCgGatewayGroupStatusActiveCgAddr_Type = InetAddress
_CgprsCgGatewayGroupStatusActiveCgAddr_Object = MibTableColumn
cgprsCgGatewayGroupStatusActiveCgAddr = _CgprsCgGatewayGroupStatusActiveCgAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5, 4, 1, 2),
    _CgprsCgGatewayGroupStatusActiveCgAddr_Type()
)
cgprsCgGatewayGroupStatusActiveCgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupStatusActiveCgAddr.setStatus("current")
_CgprsCgGatewayGroupStatusOldCgAddr_Type = InetAddress
_CgprsCgGatewayGroupStatusOldCgAddr_Object = MibTableColumn
cgprsCgGatewayGroupStatusOldCgAddr = _CgprsCgGatewayGroupStatusOldCgAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 1, 5, 4, 1, 3),
    _CgprsCgGatewayGroupStatusOldCgAddr_Type()
)
cgprsCgGatewayGroupStatusOldCgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupStatusOldCgAddr.setStatus("current")
_CiscoGprsCharNotifPrefix_ObjectIdentity = ObjectIdentity
ciscoGprsCharNotifPrefix = _CiscoGprsCharNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2)
)
_CiscoGprsCharNotifs_ObjectIdentity = ObjectIdentity
ciscoGprsCharNotifs = _CiscoGprsCharNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0)
)
_CiscoGprsCharMIBConformances_ObjectIdentity = ObjectIdentity
ciscoGprsCharMIBConformances = _CiscoGprsCharMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3)
)
_CgprsCgMIBCompliances_ObjectIdentity = ObjectIdentity
cgprsCgMIBCompliances = _CgprsCgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1)
)
_CgprsCgMIBGroups_ObjectIdentity = ObjectIdentity
cgprsCgMIBGroups = _CgprsCgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2)
)
cgprsCgGroupEntry.registerAugmentions(
    ("CISCO-GPRS-CHARGING-MIB",
     "cgprsCgGatewayGroupStatisticsEntry")
)
cgprsCgGatewayGroupStatisticsEntry.setIndexNames(*cgprsCgGroupEntry.getIndexNames())

# Managed Objects groups

cgprsCgMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 1)
)
cgprsCgMIBConfigGroup.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgOperStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgLinkState"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrLocalSeqNumEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrNodeIdEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgFlowControlEcho"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrPktsStatEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrNonPrimaryEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrAggreLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransInterval"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPktsQSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathRequest"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerVolThresh"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgMapDataTos"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathProtocol"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServerSwitchTimeout"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgConditionLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpPrimePort"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgN3BufferSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargeForRoamersOnly"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMaxEntries"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeNextIndex"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeHour"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMin"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeSec"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroup.setStatus("obsolete")

cgprsCgMIBStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 2)
)
cgprsCgMIBStatsGroup.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgDownTimes"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAccPtNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOpenedNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrClosedNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPendingMsgNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgSentMsgNum"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBStatsGroup.setStatus("obsolete")

cgprsCgMIBAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 3)
)
cgprsCgMIBAlarmsGroup.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistTableMax"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistSeverity"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistInfo"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBAlarmsGroup.setStatus("deprecated")

cgprsCgMIBConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 5)
)
cgprsCgMIBConfigGroupRev1.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgOperStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgLinkState"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrLocalSeqNumEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrNodeIdEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgFlowControlEcho"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrPktsStatEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrNonPrimaryEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrAggreLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransInterval"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPktsQSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathRequest"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerVolThresh"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgMapDataTos"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathProtocol"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServerSwitchTimeout"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgConditionLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpPrimePort"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgN3BufferSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargeForRoamersOnly"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMaxEntries"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeNextIndex"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeHour"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMin"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeSec"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgClearCdrPartialCdr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgSgsnChangeLimit"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupRev1.setStatus("obsolete")

cgprsCgMIBStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 6)
)
cgprsCgMIBStatsGroupRev1.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgDownTimes"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAccPtNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOpenedNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrClosedNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPendingMsgNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgSentMsgNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTotalCdrOpened"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTotalContainerCreated"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBStatsGroupRev1.setStatus("deprecated")

cgprsCgMIBConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 7)
)
cgprsCgMIBConfigGroupRev2.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgOperStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgLinkState"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrLocalSeqNumEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrNodeIdEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgFlowControlEcho"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrPktsStatEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrAggreLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransInterval"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPktsQSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathRequest"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerVolThresh"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgMapDataTos"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathProtocol"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServerSwitchTimeout"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgConditionLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpPrimePort"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgN3BufferSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargeForRoamersOnly"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMaxEntries"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeNextIndex"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeHour"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMin"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeSec"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgClearCdrPartialCdr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrSgsnChangeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgSgsnChangeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgRelease"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpShortHeaderEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransFormNumRespEnable"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupRev2.setStatus("deprecated")

cgprsCgMIBAlarmsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 8)
)
cgprsCgMIBAlarmsGroupRev1.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistTableMax"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistSeverity"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistInfo"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistLatestIndex"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBAlarmsGroupRev1.setStatus("deprecated")

cgprsCgMIBConfigGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 9)
)
cgprsCgMIBConfigGroupRev3.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgOperStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgLinkState"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrLocalSeqNumEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrNodeIdEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgFlowControlEcho"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrPktsStatEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrAggreLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransInterval"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPktsQSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathRequest"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerVolThresh"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgMapDataTos"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathProtocol"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServerSwitchTimeout"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgConditionLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpPrimePort"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgN3BufferSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargeForRoamersOnly"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMaxEntries"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeNextIndex"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeHour"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMin"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeSec"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgClearCdrPartialCdr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrSgsnChangeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgRelease"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpShortHeaderEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransFormNumRespEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerTimeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDesc"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCategory"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCdrSuppress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileVolumeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileVolumeLimitReset"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDurLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDurLimitReset"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileTariffTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileSgsnChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapOverride"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapTrusted"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargingCharReject"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServiceMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPartialCdrGenEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgSwitchOverPriority"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCharSelectionMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgReconnect"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPtcEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPtcPossiblyDupEnable"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupRev3.setStatus("deprecated")

cgprsCgMIBStatsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 11)
)
cgprsCgMIBStatsGroupRev2.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgDownTimes"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAccPtNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOpenedNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrClosedNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPendingMsgNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgSentMsgNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTotalCdrOpened"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTotalContainerCreated"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBStatsGroupRev2.setStatus("current")

cgprsCgMIBStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 12)
)
cgprsCgMIBStatusGroup.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgActiveChgGatewayAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgActiveChgGatewayAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgOldChgGatewayAddress"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBStatusGroup.setStatus("deprecated")

cgprsCgMIBConfigGroupR60 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 13)
)
cgprsCgMIBConfigGroupR60.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionServiceRecord"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPartialCdrGenEnableAll"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCdrSuppressPrepaid"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentDccaProfile"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostValTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostVolume"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentRulebaseId"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionApn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionVirtualApn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionApnSelMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionDynamicAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionNip"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionPdpAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionPdpType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionSerMsisdn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionSgsnPlmn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionCamelCharInfo"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionImeisv"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionMsTimeZone"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionRatType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionUserLocInfo"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupR60.setStatus("deprecated")

cgprsCgMIBStatusGroupR60 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 14)
)
cgprsCgMIBStatusGroupR60.setObjects(
    ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTotalServiceRecords")
)
if mibBuilder.loadTexts:
    cgprsCgMIBStatusGroupR60.setStatus("current")

cgprsCgMIBConfigProfileChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 15)
)
cgprsCgMIBConfigProfileChangeGroup.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostQosChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostSgsnChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostRatChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostPlmnChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileStorageType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServiceRecordIncludeRat"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServiceRecordIncludePlmn"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigProfileChangeGroup.setStatus("deprecated")

cgprsCgMIBConfigGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 16)
)
cgprsCgMIBConfigGroupRev4.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgOperStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgLinkState"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrLocalSeqNumEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrNodeIdEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgFlowControlEcho"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrPktsStatEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrAggreLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransInterval"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPktsQSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathRequest"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerVolThresh"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgMapDataTos"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathProtocol"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServerSwitchTimeout"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgConditionLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpPrimePort"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgN3BufferSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargeForRoamersOnly"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMaxEntries"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeNextIndex"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeHour"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMin"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeSec"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgClearCdrPartialCdr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrSgsnChangeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgRelease"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpShortHeaderEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransFormNumRespEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerTimeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDesc"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCategory"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCdrSuppress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileVolumeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileVolumeLimitReset"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDurLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDurLimitReset"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileTariffTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileSgsnChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapNumber"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapOverride"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapTrusted"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargingCharReject"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServiceMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPartialCdrGenEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgSwitchOverPriority"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCharSelectionMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgReconnect"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPtcEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPtcPossiblyDupEnable"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupRev4.setStatus("deprecated")

cgprsCgMIBExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 17)
)
cgprsCgMIBExtConfigGroup.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionServiceRecord"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPartialCdrGenEnableAll"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCdrSuppressPrepaid"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentDccaProfile"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostValidityTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostVolume"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentRulebaseId"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionApn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionVirtualApn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionApnSelMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionDynamicAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionNip"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionPdpAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionPdpType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionSerMsisdn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionSgsnPlmn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionCamelCharInfo"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionImeisv"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionMsTimeZone"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionRatType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionUserLocInfo"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBExtConfigGroup.setStatus("deprecated")

cgprsCgMIBConfigGroupR80 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 18)
)
cgprsCgMIBConfigGroupR80.setObjects(
    ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargingSrcInterface")
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupR80.setStatus("current")

cgprsCgMIBConfigProfileChangeGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 19)
)
cgprsCgMIBConfigProfileChangeGroupRev1.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostQosChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostSgsnChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostRatChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostPlmnChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostUserLocChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileStorageType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServiceRecordIncludeRat"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServiceRecordIncludePlmn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServiceRecordIncludeUserLocInfo"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigProfileChangeGroupRev1.setStatus("current")

cgprsCgMIBConfigGroupR90 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 20)
)
cgprsCgMIBConfigGroupR90.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayIpAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayIpAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayOperStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayLinkState"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGateway"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayIpRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupIscsi"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupServiceMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupSwitchOverPriority"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupRowStatus"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupR90.setStatus("current")

cgprsCgMIBStatsGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 21)
)
cgprsCgMIBStatsGroupRev3.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupCgDownTimes"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAccPtNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupCdrOpenedNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupCdrClosedNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupContainerNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupServiceRecordsNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupPendingMsgNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupCdrPendingMsgIscsiNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupCdrPendingMsgCgPathNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupCdrPendingMsgMaintNum"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupTotalCdrOpened"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupTotalContainerCreated"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupTotalServiceRecords"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupTotalSentMsg"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupTotalSentMsgToIscsi"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupTotalSentMsgToCg"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBStatsGroupRev3.setStatus("current")

cgprsCgMIBAlarmsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 22)
)
cgprsCgMIBAlarmsGroupRev2.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistTableMax"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistSeverity"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistInfo"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBAlarmsGroupRev2.setStatus("current")

cgprsCgMIBStatusGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 23)
)
cgprsCgMIBStatusGroupRev1.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupStatusAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupStatusActiveCgAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupStatusOldCgAddr"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBStatusGroupRev1.setStatus("current")

cgprsCgMIBConfigGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 24)
)
cgprsCgMIBConfigGroupRev5.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrLocalSeqNumEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrNodeIdEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgFlowControlEcho"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrPktsStatEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrAggreLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransInterval"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPktsQSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathRequest"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerVolThresh"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgMapDataTos"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPathProtocol"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgServerSwitchTimeout"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgConditionLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpPrimePort"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgN3BufferSize"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargeForRoamersOnly"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMaxEntries"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeNextIndex"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeHour"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeMin"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTariffTimeSec"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgClearCdrPartialCdr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrSgsnChangeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgRelease"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGtpShortHeaderEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgTransFormNumRespEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgContainerTimeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDesc"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCategory"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCdrSuppress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileVolumeLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileVolumeLimitReset"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDurLimit"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileDurLimitReset"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileTariffTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileSgsnChange"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapNumber"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapOverride"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileMapTrusted"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgChargingCharReject"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPartialCdrGenEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCharSelectionMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgReconnect"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPtcEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPtcPossiblyDupEnable"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupRev5.setStatus("current")

cgprsCgMIBConfigGroupR100 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 26)
)
cgprsCgMIBConfigGroupR100.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionServiceRecord"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPartialCdrGenEnableAll"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCdrSuppressPrepaid"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostValidityTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostVolume"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentRulebaseId"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionApn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionVirtualApn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionApnSelMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionDynamicAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionNip"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionPdpAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionPdpType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionSerMsisdn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionSgsnPlmn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionCamelCharInfo"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionImeisv"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionMsTimeZone"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionRatType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionUserLocInfo"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentDccaProfileRowStatus"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupR100.setStatus("deprecated")

cgprsCgMIBConfigGroupR100Rev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 27)
)
cgprsCgMIBConfigGroupR100Rev1.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionServiceRecord"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgPartialCdrGenEnableAll"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileCdrSuppressPrepaid"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostValidityTime"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentPostVolume"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentRulebaseId"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionApn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionVirtualApn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionApnSelMode"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionDynamicAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionNip"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionPdpAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionPdpType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionSerMsisdn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionSgsnPlmn"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionCamelCharInfo"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionImeisv"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionMsTimeZone"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionRatType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgCdrOptionUserLocInfo"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentDccaProfileRowStatus"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileContentDccaProfileWeight"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigGroupR100Rev1.setStatus("current")

cgprsCgMIBConfigProfileChangeGroupRev1Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 28)
)
cgprsCgMIBConfigProfileChangeGroupRev1Sup1.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgProfileScdrEnable"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgScdrEnable"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBConfigProfileChangeGroupRev1Sup1.setStatus("current")


# Notification objects

cgprsCgAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0, 1)
)
cgprsCgAlarmNotif.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistSeverity"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmHistInfo"))
)
if mibBuilder.loadTexts:
    cgprsCgAlarmNotif.setStatus(
        "deprecated"
    )

cgprsCgGatewaySwitchoverNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0, 2)
)
cgprsCgGatewaySwitchoverNotif.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgActiveChgGatewayAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgActiveChgGatewayAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgOldChgGatewayAddress"))
)
if mibBuilder.loadTexts:
    cgprsCgGatewaySwitchoverNotif.setStatus(
        "deprecated"
    )

cgprsCgInServiceModeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0, 3)
)
if mibBuilder.loadTexts:
    cgprsCgInServiceModeNotif.setStatus(
        "deprecated"
    )

cgprsCgMaintenanceModeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0, 4)
)
if mibBuilder.loadTexts:
    cgprsCgMaintenanceModeNotif.setStatus(
        "deprecated"
    )

cgprsCgGatewayGroupAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0, 5)
)
cgprsCgGatewayGroupAlarmNotif.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistAddress"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistSeverity"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmHistInfo"))
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupAlarmNotif.setStatus(
        "current"
    )

cgprsCgGatewayGroupSwitchoverNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0, 6)
)
cgprsCgGatewayGroupSwitchoverNotif.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupStatusAddrType"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupStatusActiveCgAddr"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupStatusOldCgAddr"))
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupSwitchoverNotif.setStatus(
        "current"
    )

cgprsCgGatewayGroupInServiceModeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0, 7)
)
cgprsCgGatewayGroupInServiceModeNotif.setObjects(
    ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupServiceMode")
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupInServiceModeNotif.setStatus(
        "current"
    )

cgprsCgGatewayGroupMaintenanceModeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 2, 0, 8)
)
cgprsCgGatewayGroupMaintenanceModeNotif.setObjects(
    ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGroupServiceMode")
)
if mibBuilder.loadTexts:
    cgprsCgGatewayGroupMaintenanceModeNotif.setStatus(
        "current"
    )


# Notifications groups

cgprsCgMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 4)
)
cgprsCgMIBNotifGroup.setObjects(
    ("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmNotif")
)
if mibBuilder.loadTexts:
    cgprsCgMIBNotifGroup.setStatus(
        "deprecated"
    )

cgprsCgMIBNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 10)
)
cgprsCgMIBNotifGroupRev1.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgAlarmNotif"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewaySwitchoverNotif"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgInServiceModeNotif"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgMaintenanceModeNotif"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBNotifGroupRev1.setStatus(
        "deprecated"
    )

cgprsCgMIBNotifGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 2, 25)
)
cgprsCgMIBNotifGroupRev2.setObjects(
      *(("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupAlarmNotif"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupSwitchoverNotif"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupInServiceModeNotif"),
        ("CISCO-GPRS-CHARGING-MIB", "cgprsCgGatewayGroupMaintenanceModeNotif"))
)
if mibBuilder.loadTexts:
    cgprsCgMIBNotifGroupRev2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cgprsCgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsCgCompliance.setStatus(
        "obsolete"
    )

cgprsCgComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev1.setStatus(
        "obsolete"
    )

cgprsCgComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev2.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev3.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev4.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev5.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev6.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev7.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev8.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev9.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 11)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev10.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 12)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev11.setStatus(
        "deprecated"
    )

cgprsCgComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 192, 3, 1, 13)
)
if mibBuilder.loadTexts:
    cgprsCgComplianceRev12.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GPRS-CHARGING-MIB",
    **{"CgprsCgAlarmType": CgprsCgAlarmType,
       "CgprsCgGatewayType": CgprsCgGatewayType,
       "ciscoGprsChargingMIB": ciscoGprsChargingMIB,
       "ciscoGprsChargingMIBObjects": ciscoGprsChargingMIBObjects,
       "ciscoGprsChargingConfig": ciscoGprsChargingConfig,
       "cgprsCgEnable": cgprsCgEnable,
       "cgprsCgCdrLocalSeqNumEnable": cgprsCgCdrLocalSeqNumEnable,
       "cgprsCgCdrNodeIdEnable": cgprsCgCdrNodeIdEnable,
       "cgprsCgFlowControlEcho": cgprsCgFlowControlEcho,
       "cgprsCgCdrPktsStatEnable": cgprsCgCdrPktsStatEnable,
       "cgprsCgCdrNonPrimaryEnable": cgprsCgCdrNonPrimaryEnable,
       "cgprsCgCdrAggreLimit": cgprsCgCdrAggreLimit,
       "cgprsCgTransInterval": cgprsCgTransInterval,
       "cgprsCgPktsQSize": cgprsCgPktsQSize,
       "cgprsCgPathRequest": cgprsCgPathRequest,
       "cgprsCgContainerVolThresh": cgprsCgContainerVolThresh,
       "cgprsCgMapDataTos": cgprsCgMapDataTos,
       "cgprsCgPathProtocol": cgprsCgPathProtocol,
       "cgprsCgServerSwitchTimeout": cgprsCgServerSwitchTimeout,
       "cgprsCgConditionLimit": cgprsCgConditionLimit,
       "cgprsCgGtpPrimePort": cgprsCgGtpPrimePort,
       "cgprsCgN3BufferSize": cgprsCgN3BufferSize,
       "cgprsCgChargeForRoamersOnly": cgprsCgChargeForRoamersOnly,
       "cgprsCgTariffTimeMaxEntries": cgprsCgTariffTimeMaxEntries,
       "cgprsCgTariffTimeNextIndex": cgprsCgTariffTimeNextIndex,
       "cgprsCgTariffTimeTable": cgprsCgTariffTimeTable,
       "cgprsCgTariffTimeEntry": cgprsCgTariffTimeEntry,
       "cgprsCgTariffTimeIndex": cgprsCgTariffTimeIndex,
       "cgprsCgTariffTimeRowStatus": cgprsCgTariffTimeRowStatus,
       "cgprsCgTariffTimeHour": cgprsCgTariffTimeHour,
       "cgprsCgTariffTimeMin": cgprsCgTariffTimeMin,
       "cgprsCgTariffTimeSec": cgprsCgTariffTimeSec,
       "cgprsCgGatewayTable": cgprsCgGatewayTable,
       "cgprsCgGatewayEntry": cgprsCgGatewayEntry,
       "cgprsCgGatewayIndex": cgprsCgGatewayIndex,
       "cgprsCgGatewayAddrType": cgprsCgGatewayAddrType,
       "cgprsCgGatewayAddr": cgprsCgGatewayAddr,
       "cgprsCgGatewayRowStatus": cgprsCgGatewayRowStatus,
       "cgprsCgOperStatus": cgprsCgOperStatus,
       "cgprsCgLinkState": cgprsCgLinkState,
       "cgprsCgClearCdrPartialCdr": cgprsCgClearCdrPartialCdr,
       "cgprsCgSgsnChangeLimit": cgprsCgSgsnChangeLimit,
       "cgprsCgCdrSgsnChangeLimit": cgprsCgCdrSgsnChangeLimit,
       "cgprsCgRelease": cgprsCgRelease,
       "cgprsCgGtpShortHeaderEnable": cgprsCgGtpShortHeaderEnable,
       "cgprsCgTransFormNumRespEnable": cgprsCgTransFormNumRespEnable,
       "cgprsCgContainerTimeLimit": cgprsCgContainerTimeLimit,
       "cgprsCgProfileTable": cgprsCgProfileTable,
       "cgprsCgProfileEntry": cgprsCgProfileEntry,
       "cgprsCgProfileNum": cgprsCgProfileNum,
       "cgprsCgProfileRowStatus": cgprsCgProfileRowStatus,
       "cgprsCgProfileDesc": cgprsCgProfileDesc,
       "cgprsCgProfileCategory": cgprsCgProfileCategory,
       "cgprsCgProfileCdrSuppress": cgprsCgProfileCdrSuppress,
       "cgprsCgProfileVolumeLimit": cgprsCgProfileVolumeLimit,
       "cgprsCgProfileVolumeLimitReset": cgprsCgProfileVolumeLimitReset,
       "cgprsCgProfileDurLimit": cgprsCgProfileDurLimit,
       "cgprsCgProfileDurLimitReset": cgprsCgProfileDurLimitReset,
       "cgprsCgProfileTariffTime": cgprsCgProfileTariffTime,
       "cgprsCgProfileSgsnChange": cgprsCgProfileSgsnChange,
       "cgprsCgProfileCdrSuppressPrepaid": cgprsCgProfileCdrSuppressPrepaid,
       "cgprsCgProfileContentDccaProfile": cgprsCgProfileContentDccaProfile,
       "cgprsCgProfileContentPostTime": cgprsCgProfileContentPostTime,
       "cgprsCgProfileContentPostValTime": cgprsCgProfileContentPostValTime,
       "cgprsCgProfileContentPostVolume": cgprsCgProfileContentPostVolume,
       "cgprsCgProfileContentRulebaseId": cgprsCgProfileContentRulebaseId,
       "cgprsCgProfileContentPostQosChange": cgprsCgProfileContentPostQosChange,
       "cgprsCgProfileContentPostSgsnChange": cgprsCgProfileContentPostSgsnChange,
       "cgprsCgProfileContentPostRatChange": cgprsCgProfileContentPostRatChange,
       "cgprsCgProfileContentPostPlmnChange": cgprsCgProfileContentPostPlmnChange,
       "cgprsCgProfileStorageType": cgprsCgProfileStorageType,
       "cgprsCgProfileContentPostValidityTime": cgprsCgProfileContentPostValidityTime,
       "cgprsCgProfileContentPostUserLocChange": cgprsCgProfileContentPostUserLocChange,
       "cgprsCgProfileScdrEnable": cgprsCgProfileScdrEnable,
       "cgprsCgProfileMapTable": cgprsCgProfileMapTable,
       "cgprsCgProfileMapEntry": cgprsCgProfileMapEntry,
       "cgprsCgProfileMapCategory": cgprsCgProfileMapCategory,
       "cgprsCgProfileMapNum": cgprsCgProfileMapNum,
       "cgprsCgProfileMapOverride": cgprsCgProfileMapOverride,
       "cgprsCgProfileMapTrusted": cgprsCgProfileMapTrusted,
       "cgprsCgProfileMapNumber": cgprsCgProfileMapNumber,
       "cgprsCgChargingCharReject": cgprsCgChargingCharReject,
       "cgprsCgServiceMode": cgprsCgServiceMode,
       "cgprsCgPartialCdrGenEnable": cgprsCgPartialCdrGenEnable,
       "cgprsCgSwitchOverPriority": cgprsCgSwitchOverPriority,
       "cgprsCgCharSelectionMode": cgprsCgCharSelectionMode,
       "cgprsCgReconnect": cgprsCgReconnect,
       "cgprsCgPtcEnable": cgprsCgPtcEnable,
       "cgprsCgPtcPossiblyDupEnable": cgprsCgPtcPossiblyDupEnable,
       "cgprsCgCdrOptionServiceRecord": cgprsCgCdrOptionServiceRecord,
       "cgprsCgPartialCdrGenEnableAll": cgprsCgPartialCdrGenEnableAll,
       "cgprsCgCdrOptionApn": cgprsCgCdrOptionApn,
       "cgprsCgCdrOptionVirtualApn": cgprsCgCdrOptionVirtualApn,
       "cgprsCgCdrOptionApnSelMode": cgprsCgCdrOptionApnSelMode,
       "cgprsCgCdrOptionDynamicAddr": cgprsCgCdrOptionDynamicAddr,
       "cgprsCgCdrOptionNip": cgprsCgCdrOptionNip,
       "cgprsCgCdrOptionPdpAddress": cgprsCgCdrOptionPdpAddress,
       "cgprsCgCdrOptionPdpType": cgprsCgCdrOptionPdpType,
       "cgprsCgCdrOptionSerMsisdn": cgprsCgCdrOptionSerMsisdn,
       "cgprsCgCdrOptionSgsnPlmn": cgprsCgCdrOptionSgsnPlmn,
       "cgprsCgCdrOptionCamelCharInfo": cgprsCgCdrOptionCamelCharInfo,
       "cgprsCgCdrOptionImeisv": cgprsCgCdrOptionImeisv,
       "cgprsCgCdrOptionMsTimeZone": cgprsCgCdrOptionMsTimeZone,
       "cgprsCgCdrOptionRatType": cgprsCgCdrOptionRatType,
       "cgprsCgCdrOptionUserLocInfo": cgprsCgCdrOptionUserLocInfo,
       "cgprsCgServiceRecordIncludeRat": cgprsCgServiceRecordIncludeRat,
       "cgprsCgServiceRecordIncludePlmn": cgprsCgServiceRecordIncludePlmn,
       "cgprsCgChargingSrcInterface": cgprsCgChargingSrcInterface,
       "cgprsCgServiceRecordIncludeUserLocInfo": cgprsCgServiceRecordIncludeUserLocInfo,
       "cgprsCgGroupTable": cgprsCgGroupTable,
       "cgprsCgGroupEntry": cgprsCgGroupEntry,
       "cgprsCgGroupIndex": cgprsCgGroupIndex,
       "cgprsCgGroupIscsi": cgprsCgGroupIscsi,
       "cgprsCgGroupServiceMode": cgprsCgGroupServiceMode,
       "cgprsCgGroupSwitchOverPriority": cgprsCgGroupSwitchOverPriority,
       "cgprsCgGroupRowStatus": cgprsCgGroupRowStatus,
       "cgprsCgGatewayIpTable": cgprsCgGatewayIpTable,
       "cgprsCgGatewayIpEntry": cgprsCgGatewayIpEntry,
       "cgprsCgGatewayIpIndex": cgprsCgGatewayIpIndex,
       "cgprsCgGatewayIpAddrType": cgprsCgGatewayIpAddrType,
       "cgprsCgGatewayIpAddr": cgprsCgGatewayIpAddr,
       "cgprsCgGatewayOperStatus": cgprsCgGatewayOperStatus,
       "cgprsCgGatewayLinkState": cgprsCgGatewayLinkState,
       "cgprsCgGateway": cgprsCgGateway,
       "cgprsCgGatewayIpRowStatus": cgprsCgGatewayIpRowStatus,
       "cgprsCgProfileContentDccaProfileTable": cgprsCgProfileContentDccaProfileTable,
       "cgprsCgProfileContentDccaProfileEntry": cgprsCgProfileContentDccaProfileEntry,
       "cgprsCgProfileContentDccaProfileName": cgprsCgProfileContentDccaProfileName,
       "cgprsCgProfileContentDccaProfileRowStatus": cgprsCgProfileContentDccaProfileRowStatus,
       "cgprsCgProfileContentDccaProfileWeight": cgprsCgProfileContentDccaProfileWeight,
       "cgprsCgScdrEnable": cgprsCgScdrEnable,
       "ciscoGprsChargingOthers": ciscoGprsChargingOthers,
       "ciscoGprsChargingStats": ciscoGprsChargingStats,
       "cgprsCgDownTimes": cgprsCgDownTimes,
       "cgprsCgAccPtNum": cgprsCgAccPtNum,
       "cgprsCgCdrOpenedNum": cgprsCgCdrOpenedNum,
       "cgprsCgCdrClosedNum": cgprsCgCdrClosedNum,
       "cgprsCgContainerNum": cgprsCgContainerNum,
       "cgprsCgPendingMsgNum": cgprsCgPendingMsgNum,
       "cgprsCgSentMsgNum": cgprsCgSentMsgNum,
       "cgprsCgTotalCdrOpened": cgprsCgTotalCdrOpened,
       "cgprsCgTotalContainerCreated": cgprsCgTotalContainerCreated,
       "cgprsCgTotalServiceRecords": cgprsCgTotalServiceRecords,
       "cgprsCgGatewayGroupStatisticsTable": cgprsCgGatewayGroupStatisticsTable,
       "cgprsCgGatewayGroupStatisticsEntry": cgprsCgGatewayGroupStatisticsEntry,
       "cgprsCgGatewayGroupCgDownTimes": cgprsCgGatewayGroupCgDownTimes,
       "cgprsCgGatewayGroupAccPtNum": cgprsCgGatewayGroupAccPtNum,
       "cgprsCgGatewayGroupCdrOpenedNum": cgprsCgGatewayGroupCdrOpenedNum,
       "cgprsCgGatewayGroupCdrClosedNum": cgprsCgGatewayGroupCdrClosedNum,
       "cgprsCgGatewayGroupContainerNum": cgprsCgGatewayGroupContainerNum,
       "cgprsCgGatewayGroupServiceRecordsNum": cgprsCgGatewayGroupServiceRecordsNum,
       "cgprsCgGatewayGroupPendingMsgNum": cgprsCgGatewayGroupPendingMsgNum,
       "cgprsCgGatewayGroupCdrPendingMsgIscsiNum": cgprsCgGatewayGroupCdrPendingMsgIscsiNum,
       "cgprsCgGatewayGroupCdrPendingMsgCgPathNum": cgprsCgGatewayGroupCdrPendingMsgCgPathNum,
       "cgprsCgGatewayGroupCdrPendingMsgMaintNum": cgprsCgGatewayGroupCdrPendingMsgMaintNum,
       "cgprsCgGatewayGroupTotalCdrOpened": cgprsCgGatewayGroupTotalCdrOpened,
       "cgprsCgGatewayGroupTotalContainerCreated": cgprsCgGatewayGroupTotalContainerCreated,
       "cgprsCgGatewayGroupTotalServiceRecords": cgprsCgGatewayGroupTotalServiceRecords,
       "cgprsCgGatewayGroupTotalSentMsg": cgprsCgGatewayGroupTotalSentMsg,
       "cgprsCgGatewayGroupTotalSentMsgToIscsi": cgprsCgGatewayGroupTotalSentMsgToIscsi,
       "cgprsCgGatewayGroupTotalSentMsgToCg": cgprsCgGatewayGroupTotalSentMsgToCg,
       "ciscoGprsChargingAlarms": ciscoGprsChargingAlarms,
       "cgprsCgAlarmEnable": cgprsCgAlarmEnable,
       "cgprsCgAlarmHistTableMax": cgprsCgAlarmHistTableMax,
       "cgprsCgAlarmHistTable": cgprsCgAlarmHistTable,
       "cgprsCgAlarmHistEntry": cgprsCgAlarmHistEntry,
       "cgprsCgAlarmHistIndex": cgprsCgAlarmHistIndex,
       "cgprsCgAlarmHistType": cgprsCgAlarmHistType,
       "cgprsCgAlarmHistAddrType": cgprsCgAlarmHistAddrType,
       "cgprsCgAlarmHistAddress": cgprsCgAlarmHistAddress,
       "cgprsCgAlarmHistSeverity": cgprsCgAlarmHistSeverity,
       "cgprsCgAlarmHistInfo": cgprsCgAlarmHistInfo,
       "cgprsCgAlarmHistLatestIndex": cgprsCgAlarmHistLatestIndex,
       "cgprsCgGatewayGroupAlarmHistTable": cgprsCgGatewayGroupAlarmHistTable,
       "cgprsCgGatewayGroupAlarmHistEntry": cgprsCgGatewayGroupAlarmHistEntry,
       "cgprsCgGatewayGroupAlarmHistIndex": cgprsCgGatewayGroupAlarmHistIndex,
       "cgprsCgGatewayGroupAlarmHistType": cgprsCgGatewayGroupAlarmHistType,
       "cgprsCgGatewayGroupAlarmHistAddrType": cgprsCgGatewayGroupAlarmHistAddrType,
       "cgprsCgGatewayGroupAlarmHistAddress": cgprsCgGatewayGroupAlarmHistAddress,
       "cgprsCgGatewayGroupAlarmHistSeverity": cgprsCgGatewayGroupAlarmHistSeverity,
       "cgprsCgGatewayGroupAlarmHistInfo": cgprsCgGatewayGroupAlarmHistInfo,
       "cgprsCgGatewayGroupAlarmEnable": cgprsCgGatewayGroupAlarmEnable,
       "ciscoGprsChargingStatus": ciscoGprsChargingStatus,
       "cgprsCgActiveChgGatewayAddrType": cgprsCgActiveChgGatewayAddrType,
       "cgprsCgActiveChgGatewayAddress": cgprsCgActiveChgGatewayAddress,
       "cgprsCgOldChgGatewayAddress": cgprsCgOldChgGatewayAddress,
       "cgprsCgGatewayGroupStatusTable": cgprsCgGatewayGroupStatusTable,
       "cgprsCgGatewayGroupStatusEntry": cgprsCgGatewayGroupStatusEntry,
       "cgprsCgGatewayGroupStatusAddrType": cgprsCgGatewayGroupStatusAddrType,
       "cgprsCgGatewayGroupStatusActiveCgAddr": cgprsCgGatewayGroupStatusActiveCgAddr,
       "cgprsCgGatewayGroupStatusOldCgAddr": cgprsCgGatewayGroupStatusOldCgAddr,
       "ciscoGprsCharNotifPrefix": ciscoGprsCharNotifPrefix,
       "ciscoGprsCharNotifs": ciscoGprsCharNotifs,
       "cgprsCgAlarmNotif": cgprsCgAlarmNotif,
       "cgprsCgGatewaySwitchoverNotif": cgprsCgGatewaySwitchoverNotif,
       "cgprsCgInServiceModeNotif": cgprsCgInServiceModeNotif,
       "cgprsCgMaintenanceModeNotif": cgprsCgMaintenanceModeNotif,
       "cgprsCgGatewayGroupAlarmNotif": cgprsCgGatewayGroupAlarmNotif,
       "cgprsCgGatewayGroupSwitchoverNotif": cgprsCgGatewayGroupSwitchoverNotif,
       "cgprsCgGatewayGroupInServiceModeNotif": cgprsCgGatewayGroupInServiceModeNotif,
       "cgprsCgGatewayGroupMaintenanceModeNotif": cgprsCgGatewayGroupMaintenanceModeNotif,
       "ciscoGprsCharMIBConformances": ciscoGprsCharMIBConformances,
       "cgprsCgMIBCompliances": cgprsCgMIBCompliances,
       "cgprsCgCompliance": cgprsCgCompliance,
       "cgprsCgComplianceRev1": cgprsCgComplianceRev1,
       "cgprsCgComplianceRev2": cgprsCgComplianceRev2,
       "cgprsCgComplianceRev3": cgprsCgComplianceRev3,
       "cgprsCgComplianceRev4": cgprsCgComplianceRev4,
       "cgprsCgComplianceRev5": cgprsCgComplianceRev5,
       "cgprsCgComplianceRev6": cgprsCgComplianceRev6,
       "cgprsCgComplianceRev7": cgprsCgComplianceRev7,
       "cgprsCgComplianceRev8": cgprsCgComplianceRev8,
       "cgprsCgComplianceRev9": cgprsCgComplianceRev9,
       "cgprsCgComplianceRev10": cgprsCgComplianceRev10,
       "cgprsCgComplianceRev11": cgprsCgComplianceRev11,
       "cgprsCgComplianceRev12": cgprsCgComplianceRev12,
       "cgprsCgMIBGroups": cgprsCgMIBGroups,
       "cgprsCgMIBConfigGroup": cgprsCgMIBConfigGroup,
       "cgprsCgMIBStatsGroup": cgprsCgMIBStatsGroup,
       "cgprsCgMIBAlarmsGroup": cgprsCgMIBAlarmsGroup,
       "cgprsCgMIBNotifGroup": cgprsCgMIBNotifGroup,
       "cgprsCgMIBConfigGroupRev1": cgprsCgMIBConfigGroupRev1,
       "cgprsCgMIBStatsGroupRev1": cgprsCgMIBStatsGroupRev1,
       "cgprsCgMIBConfigGroupRev2": cgprsCgMIBConfigGroupRev2,
       "cgprsCgMIBAlarmsGroupRev1": cgprsCgMIBAlarmsGroupRev1,
       "cgprsCgMIBConfigGroupRev3": cgprsCgMIBConfigGroupRev3,
       "cgprsCgMIBNotifGroupRev1": cgprsCgMIBNotifGroupRev1,
       "cgprsCgMIBStatsGroupRev2": cgprsCgMIBStatsGroupRev2,
       "cgprsCgMIBStatusGroup": cgprsCgMIBStatusGroup,
       "cgprsCgMIBConfigGroupR60": cgprsCgMIBConfigGroupR60,
       "cgprsCgMIBStatusGroupR60": cgprsCgMIBStatusGroupR60,
       "cgprsCgMIBConfigProfileChangeGroup": cgprsCgMIBConfigProfileChangeGroup,
       "cgprsCgMIBConfigGroupRev4": cgprsCgMIBConfigGroupRev4,
       "cgprsCgMIBExtConfigGroup": cgprsCgMIBExtConfigGroup,
       "cgprsCgMIBConfigGroupR80": cgprsCgMIBConfigGroupR80,
       "cgprsCgMIBConfigProfileChangeGroupRev1": cgprsCgMIBConfigProfileChangeGroupRev1,
       "cgprsCgMIBConfigGroupR90": cgprsCgMIBConfigGroupR90,
       "cgprsCgMIBStatsGroupRev3": cgprsCgMIBStatsGroupRev3,
       "cgprsCgMIBAlarmsGroupRev2": cgprsCgMIBAlarmsGroupRev2,
       "cgprsCgMIBStatusGroupRev1": cgprsCgMIBStatusGroupRev1,
       "cgprsCgMIBConfigGroupRev5": cgprsCgMIBConfigGroupRev5,
       "cgprsCgMIBNotifGroupRev2": cgprsCgMIBNotifGroupRev2,
       "cgprsCgMIBConfigGroupR100": cgprsCgMIBConfigGroupR100,
       "cgprsCgMIBConfigGroupR100Rev1": cgprsCgMIBConfigGroupR100Rev1,
       "cgprsCgMIBConfigProfileChangeGroupRev1Sup1": cgprsCgMIBConfigProfileChangeGroupRev1Sup1}
)
