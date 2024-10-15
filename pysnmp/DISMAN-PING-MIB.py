# SNMP MIB module (DISMAN-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DISMAN-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:44 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pingMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 80)
)
pingMIB.setRevisions(
        ("2006-06-13 00:00",
         "2000-09-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OperationResponseStatus(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("arpFailure", 8),
          ("interfaceInactiveToTarget", 7),
          ("internalError", 3),
          ("invalidHostAddress", 11),
          ("maxConcurrentLimitReached", 9),
          ("noRouteToTarget", 6),
          ("requestTimedOut", 4),
          ("responseReceived", 1),
          ("unableToResolveDnsName", 10),
          ("unknown", 2),
          ("unknownDestinationAddress", 5))
    )



# MIB Managed Objects in the order of their OIDs

_PingNotifications_ObjectIdentity = ObjectIdentity
pingNotifications = _PingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 0)
)
_PingObjects_ObjectIdentity = ObjectIdentity
pingObjects = _PingObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 1)
)


class _PingMaxConcurrentRequests_Type(Unsigned32):
    """Custom type pingMaxConcurrentRequests based on Unsigned32"""
    defaultValue = 10


_PingMaxConcurrentRequests_Object = MibScalar
pingMaxConcurrentRequests = _PingMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 1),
    _PingMaxConcurrentRequests_Type()
)
pingMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingMaxConcurrentRequests.setStatus("current")
if mibBuilder.loadTexts:
    pingMaxConcurrentRequests.setUnits("requests")
_PingCtlTable_Object = MibTable
pingCtlTable = _PingCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2)
)
if mibBuilder.loadTexts:
    pingCtlTable.setStatus("current")
_PingCtlEntry_Object = MibTableRow
pingCtlEntry = _PingCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1)
)
pingCtlEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    pingCtlEntry.setStatus("current")


class _PingCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type pingCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PingCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_PingCtlOwnerIndex_Object = MibTableColumn
pingCtlOwnerIndex = _PingCtlOwnerIndex_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 1),
    _PingCtlOwnerIndex_Type()
)
pingCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingCtlOwnerIndex.setStatus("current")


class _PingCtlTestName_Type(SnmpAdminString):
    """Custom type pingCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PingCtlTestName_Type.__name__ = "SnmpAdminString"
_PingCtlTestName_Object = MibTableColumn
pingCtlTestName = _PingCtlTestName_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 2),
    _PingCtlTestName_Type()
)
pingCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingCtlTestName.setStatus("current")


class _PingCtlTargetAddressType_Type(InetAddressType):
    """Custom type pingCtlTargetAddressType based on InetAddressType"""


_PingCtlTargetAddressType_Object = MibTableColumn
pingCtlTargetAddressType = _PingCtlTargetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 3),
    _PingCtlTargetAddressType_Type()
)
pingCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTargetAddressType.setStatus("current")


class _PingCtlTargetAddress_Type(InetAddress):
    """Custom type pingCtlTargetAddress based on InetAddress"""
    defaultHexValue = ""


_PingCtlTargetAddress_Object = MibTableColumn
pingCtlTargetAddress = _PingCtlTargetAddress_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 4),
    _PingCtlTargetAddress_Type()
)
pingCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTargetAddress.setStatus("current")


class _PingCtlDataSize_Type(Unsigned32):
    """Custom type pingCtlDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65507),
    )


_PingCtlDataSize_Type.__name__ = "Unsigned32"
_PingCtlDataSize_Object = MibTableColumn
pingCtlDataSize = _PingCtlDataSize_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 5),
    _PingCtlDataSize_Type()
)
pingCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlDataSize.setUnits("octets")


class _PingCtlTimeOut_Type(Unsigned32):
    """Custom type pingCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PingCtlTimeOut_Type.__name__ = "Unsigned32"
_PingCtlTimeOut_Object = MibTableColumn
pingCtlTimeOut = _PingCtlTimeOut_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 6),
    _PingCtlTimeOut_Type()
)
pingCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlTimeOut.setUnits("seconds")


class _PingCtlProbeCount_Type(Unsigned32):
    """Custom type pingCtlProbeCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_PingCtlProbeCount_Type.__name__ = "Unsigned32"
_PingCtlProbeCount_Object = MibTableColumn
pingCtlProbeCount = _PingCtlProbeCount_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 7),
    _PingCtlProbeCount_Type()
)
pingCtlProbeCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlProbeCount.setUnits("probes")


class _PingCtlAdminStatus_Type(Integer32):
    """Custom type pingCtlAdminStatus based on Integer32"""
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


_PingCtlAdminStatus_Type.__name__ = "Integer32"
_PingCtlAdminStatus_Object = MibTableColumn
pingCtlAdminStatus = _PingCtlAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 8),
    _PingCtlAdminStatus_Type()
)
pingCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlAdminStatus.setStatus("current")


class _PingCtlDataFill_Type(OctetString):
    """Custom type pingCtlDataFill based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PingCtlDataFill_Type.__name__ = "OctetString"
_PingCtlDataFill_Object = MibTableColumn
pingCtlDataFill = _PingCtlDataFill_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 9),
    _PingCtlDataFill_Type()
)
pingCtlDataFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlDataFill.setStatus("current")


class _PingCtlFrequency_Type(Unsigned32):
    """Custom type pingCtlFrequency based on Unsigned32"""
    defaultValue = 0


_PingCtlFrequency_Object = MibTableColumn
pingCtlFrequency = _PingCtlFrequency_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 10),
    _PingCtlFrequency_Type()
)
pingCtlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlFrequency.setUnits("seconds")


class _PingCtlMaxRows_Type(Unsigned32):
    """Custom type pingCtlMaxRows based on Unsigned32"""
    defaultValue = 50


_PingCtlMaxRows_Object = MibTableColumn
pingCtlMaxRows = _PingCtlMaxRows_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 11),
    _PingCtlMaxRows_Type()
)
pingCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlMaxRows.setUnits("rows")


class _PingCtlStorageType_Type(StorageType):
    """Custom type pingCtlStorageType based on StorageType"""


_PingCtlStorageType_Object = MibTableColumn
pingCtlStorageType = _PingCtlStorageType_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 12),
    _PingCtlStorageType_Type()
)
pingCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlStorageType.setStatus("current")


class _PingCtlTrapGeneration_Type(Bits):
    """Custom type pingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("probeFailure", 0),
          ("testCompletion", 2),
          ("testFailure", 1))
    )

_PingCtlTrapGeneration_Type.__name__ = "Bits"
_PingCtlTrapGeneration_Object = MibTableColumn
pingCtlTrapGeneration = _PingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 13),
    _PingCtlTrapGeneration_Type()
)
pingCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTrapGeneration.setStatus("current")


class _PingCtlTrapProbeFailureFilter_Type(Unsigned32):
    """Custom type pingCtlTrapProbeFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PingCtlTrapProbeFailureFilter_Type.__name__ = "Unsigned32"
_PingCtlTrapProbeFailureFilter_Object = MibTableColumn
pingCtlTrapProbeFailureFilter = _PingCtlTrapProbeFailureFilter_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 14),
    _PingCtlTrapProbeFailureFilter_Type()
)
pingCtlTrapProbeFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTrapProbeFailureFilter.setStatus("current")


class _PingCtlTrapTestFailureFilter_Type(Unsigned32):
    """Custom type pingCtlTrapTestFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PingCtlTrapTestFailureFilter_Type.__name__ = "Unsigned32"
_PingCtlTrapTestFailureFilter_Object = MibTableColumn
pingCtlTrapTestFailureFilter = _PingCtlTrapTestFailureFilter_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 15),
    _PingCtlTrapTestFailureFilter_Type()
)
pingCtlTrapTestFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTrapTestFailureFilter.setStatus("current")


class _PingCtlType_Type(ObjectIdentifier):
    """Custom type pingCtlType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 80, 3, 1)


_PingCtlType_Object = MibTableColumn
pingCtlType = _PingCtlType_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 16),
    _PingCtlType_Type()
)
pingCtlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlType.setStatus("current")


class _PingCtlDescr_Type(SnmpAdminString):
    """Custom type pingCtlDescr based on SnmpAdminString"""
    defaultHexValue = ""


_PingCtlDescr_Object = MibTableColumn
pingCtlDescr = _PingCtlDescr_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 17),
    _PingCtlDescr_Type()
)
pingCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlDescr.setStatus("current")


class _PingCtlSourceAddressType_Type(InetAddressType):
    """Custom type pingCtlSourceAddressType based on InetAddressType"""


_PingCtlSourceAddressType_Object = MibTableColumn
pingCtlSourceAddressType = _PingCtlSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 18),
    _PingCtlSourceAddressType_Type()
)
pingCtlSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlSourceAddressType.setStatus("current")


class _PingCtlSourceAddress_Type(InetAddress):
    """Custom type pingCtlSourceAddress based on InetAddress"""
    defaultHexValue = ""


_PingCtlSourceAddress_Object = MibTableColumn
pingCtlSourceAddress = _PingCtlSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 19),
    _PingCtlSourceAddress_Type()
)
pingCtlSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlSourceAddress.setStatus("current")


class _PingCtlIfIndex_Type(InterfaceIndexOrZero):
    """Custom type pingCtlIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PingCtlIfIndex_Object = MibTableColumn
pingCtlIfIndex = _PingCtlIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 20),
    _PingCtlIfIndex_Type()
)
pingCtlIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlIfIndex.setStatus("current")


class _PingCtlByPassRouteTable_Type(TruthValue):
    """Custom type pingCtlByPassRouteTable based on TruthValue"""


_PingCtlByPassRouteTable_Object = MibTableColumn
pingCtlByPassRouteTable = _PingCtlByPassRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 21),
    _PingCtlByPassRouteTable_Type()
)
pingCtlByPassRouteTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlByPassRouteTable.setStatus("current")


class _PingCtlDSField_Type(Unsigned32):
    """Custom type pingCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PingCtlDSField_Type.__name__ = "Unsigned32"
_PingCtlDSField_Object = MibTableColumn
pingCtlDSField = _PingCtlDSField_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 22),
    _PingCtlDSField_Type()
)
pingCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlDSField.setStatus("current")
_PingCtlRowStatus_Type = RowStatus
_PingCtlRowStatus_Object = MibTableColumn
pingCtlRowStatus = _PingCtlRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 23),
    _PingCtlRowStatus_Type()
)
pingCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlRowStatus.setStatus("current")
_PingResultsTable_Object = MibTable
pingResultsTable = _PingResultsTable_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3)
)
if mibBuilder.loadTexts:
    pingResultsTable.setStatus("current")
_PingResultsEntry_Object = MibTableRow
pingResultsEntry = _PingResultsEntry_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1)
)
pingResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    pingResultsEntry.setStatus("current")


class _PingResultsOperStatus_Type(Integer32):
    """Custom type pingResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_PingResultsOperStatus_Type.__name__ = "Integer32"
_PingResultsOperStatus_Object = MibTableColumn
pingResultsOperStatus = _PingResultsOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 1),
    _PingResultsOperStatus_Type()
)
pingResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsOperStatus.setStatus("current")


class _PingResultsIpTargetAddressType_Type(InetAddressType):
    """Custom type pingResultsIpTargetAddressType based on InetAddressType"""


_PingResultsIpTargetAddressType_Object = MibTableColumn
pingResultsIpTargetAddressType = _PingResultsIpTargetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 2),
    _PingResultsIpTargetAddressType_Type()
)
pingResultsIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsIpTargetAddressType.setStatus("current")


class _PingResultsIpTargetAddress_Type(InetAddress):
    """Custom type pingResultsIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_PingResultsIpTargetAddress_Object = MibTableColumn
pingResultsIpTargetAddress = _PingResultsIpTargetAddress_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 3),
    _PingResultsIpTargetAddress_Type()
)
pingResultsIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsIpTargetAddress.setStatus("current")
_PingResultsMinRtt_Type = Unsigned32
_PingResultsMinRtt_Object = MibTableColumn
pingResultsMinRtt = _PingResultsMinRtt_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 4),
    _PingResultsMinRtt_Type()
)
pingResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsMinRtt.setUnits("milliseconds")
_PingResultsMaxRtt_Type = Unsigned32
_PingResultsMaxRtt_Object = MibTableColumn
pingResultsMaxRtt = _PingResultsMaxRtt_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 5),
    _PingResultsMaxRtt_Type()
)
pingResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsMaxRtt.setUnits("milliseconds")
_PingResultsAverageRtt_Type = Unsigned32
_PingResultsAverageRtt_Object = MibTableColumn
pingResultsAverageRtt = _PingResultsAverageRtt_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 6),
    _PingResultsAverageRtt_Type()
)
pingResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsAverageRtt.setUnits("milliseconds")
_PingResultsProbeResponses_Type = Gauge32
_PingResultsProbeResponses_Object = MibTableColumn
pingResultsProbeResponses = _PingResultsProbeResponses_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 7),
    _PingResultsProbeResponses_Type()
)
pingResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsProbeResponses.setUnits("responses")
_PingResultsSentProbes_Type = Gauge32
_PingResultsSentProbes_Object = MibTableColumn
pingResultsSentProbes = _PingResultsSentProbes_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 8),
    _PingResultsSentProbes_Type()
)
pingResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsSentProbes.setUnits("probes")
_PingResultsRttSumOfSquares_Type = Unsigned32
_PingResultsRttSumOfSquares_Object = MibTableColumn
pingResultsRttSumOfSquares = _PingResultsRttSumOfSquares_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 9),
    _PingResultsRttSumOfSquares_Type()
)
pingResultsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsRttSumOfSquares.setUnits("milliseconds")
_PingResultsLastGoodProbe_Type = DateAndTime
_PingResultsLastGoodProbe_Object = MibTableColumn
pingResultsLastGoodProbe = _PingResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 10),
    _PingResultsLastGoodProbe_Type()
)
pingResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsLastGoodProbe.setStatus("current")
_PingProbeHistoryTable_Object = MibTable
pingProbeHistoryTable = _PingProbeHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 4)
)
if mibBuilder.loadTexts:
    pingProbeHistoryTable.setStatus("current")
_PingProbeHistoryEntry_Object = MibTableRow
pingProbeHistoryEntry = _PingProbeHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 4, 1)
)
pingProbeHistoryEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "DISMAN-PING-MIB", "pingProbeHistoryIndex"),
)
if mibBuilder.loadTexts:
    pingProbeHistoryEntry.setStatus("current")


class _PingProbeHistoryIndex_Type(Unsigned32):
    """Custom type pingProbeHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PingProbeHistoryIndex_Type.__name__ = "Unsigned32"
_PingProbeHistoryIndex_Object = MibTableColumn
pingProbeHistoryIndex = _PingProbeHistoryIndex_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 1),
    _PingProbeHistoryIndex_Type()
)
pingProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingProbeHistoryIndex.setStatus("current")
_PingProbeHistoryResponse_Type = Unsigned32
_PingProbeHistoryResponse_Object = MibTableColumn
pingProbeHistoryResponse = _PingProbeHistoryResponse_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 2),
    _PingProbeHistoryResponse_Type()
)
pingProbeHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingProbeHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    pingProbeHistoryResponse.setUnits("milliseconds")
_PingProbeHistoryStatus_Type = OperationResponseStatus
_PingProbeHistoryStatus_Object = MibTableColumn
pingProbeHistoryStatus = _PingProbeHistoryStatus_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 3),
    _PingProbeHistoryStatus_Type()
)
pingProbeHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingProbeHistoryStatus.setStatus("current")
_PingProbeHistoryLastRC_Type = Integer32
_PingProbeHistoryLastRC_Object = MibTableColumn
pingProbeHistoryLastRC = _PingProbeHistoryLastRC_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 4),
    _PingProbeHistoryLastRC_Type()
)
pingProbeHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingProbeHistoryLastRC.setStatus("current")
_PingProbeHistoryTime_Type = DateAndTime
_PingProbeHistoryTime_Object = MibTableColumn
pingProbeHistoryTime = _PingProbeHistoryTime_Object(
    (1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 5),
    _PingProbeHistoryTime_Type()
)
pingProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingProbeHistoryTime.setStatus("current")
_PingConformance_ObjectIdentity = ObjectIdentity
pingConformance = _PingConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 2)
)
_PingCompliances_ObjectIdentity = ObjectIdentity
pingCompliances = _PingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 2, 1)
)
_PingGroups_ObjectIdentity = ObjectIdentity
pingGroups = _PingGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 2, 2)
)
_PingImplementationTypeDomains_ObjectIdentity = ObjectIdentity
pingImplementationTypeDomains = _PingImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 3)
)
_PingIcmpEcho_ObjectIdentity = ObjectIdentity
pingIcmpEcho = _PingIcmpEcho_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 3, 1)
)
if mibBuilder.loadTexts:
    pingIcmpEcho.setStatus("current")
_PingUdpEcho_ObjectIdentity = ObjectIdentity
pingUdpEcho = _PingUdpEcho_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 3, 2)
)
if mibBuilder.loadTexts:
    pingUdpEcho.setStatus("current")
_PingSnmpQuery_ObjectIdentity = ObjectIdentity
pingSnmpQuery = _PingSnmpQuery_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 3, 3)
)
if mibBuilder.loadTexts:
    pingSnmpQuery.setStatus("current")
_PingTcpConnectionAttempt_ObjectIdentity = ObjectIdentity
pingTcpConnectionAttempt = _PingTcpConnectionAttempt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 80, 3, 4)
)
if mibBuilder.loadTexts:
    pingTcpConnectionAttempt.setStatus("current")

# Managed Objects groups

pingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 80, 2, 2, 1)
)
pingGroup.setObjects(
      *(("DISMAN-PING-MIB", "pingMaxConcurrentRequests"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlDataSize"),
        ("DISMAN-PING-MIB", "pingCtlTimeOut"),
        ("DISMAN-PING-MIB", "pingCtlProbeCount"),
        ("DISMAN-PING-MIB", "pingCtlAdminStatus"),
        ("DISMAN-PING-MIB", "pingCtlDataFill"),
        ("DISMAN-PING-MIB", "pingCtlFrequency"),
        ("DISMAN-PING-MIB", "pingCtlMaxRows"),
        ("DISMAN-PING-MIB", "pingCtlStorageType"),
        ("DISMAN-PING-MIB", "pingCtlTrapGeneration"),
        ("DISMAN-PING-MIB", "pingCtlTrapProbeFailureFilter"),
        ("DISMAN-PING-MIB", "pingCtlTrapTestFailureFilter"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("DISMAN-PING-MIB", "pingCtlByPassRouteTable"),
        ("DISMAN-PING-MIB", "pingCtlSourceAddressType"),
        ("DISMAN-PING-MIB", "pingCtlSourceAddress"),
        ("DISMAN-PING-MIB", "pingCtlIfIndex"),
        ("DISMAN-PING-MIB", "pingCtlDSField"),
        ("DISMAN-PING-MIB", "pingCtlRowStatus"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsMinRtt"),
        ("DISMAN-PING-MIB", "pingResultsMaxRtt"),
        ("DISMAN-PING-MIB", "pingResultsAverageRtt"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"),
        ("DISMAN-PING-MIB", "pingProbeHistoryResponse"),
        ("DISMAN-PING-MIB", "pingProbeHistoryStatus"),
        ("DISMAN-PING-MIB", "pingProbeHistoryLastRC"))
)
if mibBuilder.loadTexts:
    pingGroup.setStatus("deprecated")

pingTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 80, 2, 2, 2)
)
pingTimeStampGroup.setObjects(
      *(("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("DISMAN-PING-MIB", "pingProbeHistoryTime"))
)
if mibBuilder.loadTexts:
    pingTimeStampGroup.setStatus("deprecated")

pingMinimumGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 80, 2, 2, 4)
)
pingMinimumGroup.setObjects(
      *(("DISMAN-PING-MIB", "pingMaxConcurrentRequests"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlDataSize"),
        ("DISMAN-PING-MIB", "pingCtlTimeOut"),
        ("DISMAN-PING-MIB", "pingCtlProbeCount"),
        ("DISMAN-PING-MIB", "pingCtlAdminStatus"),
        ("DISMAN-PING-MIB", "pingCtlDataFill"),
        ("DISMAN-PING-MIB", "pingCtlFrequency"),
        ("DISMAN-PING-MIB", "pingCtlMaxRows"),
        ("DISMAN-PING-MIB", "pingCtlStorageType"),
        ("DISMAN-PING-MIB", "pingCtlTrapGeneration"),
        ("DISMAN-PING-MIB", "pingCtlTrapProbeFailureFilter"),
        ("DISMAN-PING-MIB", "pingCtlTrapTestFailureFilter"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("DISMAN-PING-MIB", "pingCtlByPassRouteTable"),
        ("DISMAN-PING-MIB", "pingCtlSourceAddressType"),
        ("DISMAN-PING-MIB", "pingCtlSourceAddress"),
        ("DISMAN-PING-MIB", "pingCtlIfIndex"),
        ("DISMAN-PING-MIB", "pingCtlDSField"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsMinRtt"),
        ("DISMAN-PING-MIB", "pingResultsMaxRtt"),
        ("DISMAN-PING-MIB", "pingResultsAverageRtt"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    pingMinimumGroup.setStatus("current")

pingCtlRowStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 80, 2, 2, 5)
)
pingCtlRowStatusGroup.setObjects(
    ("DISMAN-PING-MIB", "pingCtlRowStatus")
)
if mibBuilder.loadTexts:
    pingCtlRowStatusGroup.setStatus("current")

pingHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 80, 2, 2, 6)
)
pingHistoryGroup.setObjects(
      *(("DISMAN-PING-MIB", "pingProbeHistoryResponse"),
        ("DISMAN-PING-MIB", "pingProbeHistoryStatus"),
        ("DISMAN-PING-MIB", "pingProbeHistoryLastRC"),
        ("DISMAN-PING-MIB", "pingProbeHistoryTime"))
)
if mibBuilder.loadTexts:
    pingHistoryGroup.setStatus("current")


# Notification objects

pingProbeFailed = NotificationType(
    (1, 3, 6, 1, 2, 1, 80, 0, 1)
)
pingProbeFailed.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsMinRtt"),
        ("DISMAN-PING-MIB", "pingResultsMaxRtt"),
        ("DISMAN-PING-MIB", "pingResultsAverageRtt"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    pingProbeFailed.setStatus(
        "current"
    )

pingTestFailed = NotificationType(
    (1, 3, 6, 1, 2, 1, 80, 0, 2)
)
pingTestFailed.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsMinRtt"),
        ("DISMAN-PING-MIB", "pingResultsMaxRtt"),
        ("DISMAN-PING-MIB", "pingResultsAverageRtt"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    pingTestFailed.setStatus(
        "current"
    )

pingTestCompleted = NotificationType(
    (1, 3, 6, 1, 2, 1, 80, 0, 3)
)
pingTestCompleted.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsMinRtt"),
        ("DISMAN-PING-MIB", "pingResultsMaxRtt"),
        ("DISMAN-PING-MIB", "pingResultsAverageRtt"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    pingTestCompleted.setStatus(
        "current"
    )


# Notifications groups

pingNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 80, 2, 2, 3)
)
pingNotificationsGroup.setObjects(
      *(("DISMAN-PING-MIB", "pingProbeFailed"),
        ("DISMAN-PING-MIB", "pingTestFailed"),
        ("DISMAN-PING-MIB", "pingTestCompleted"))
)
if mibBuilder.loadTexts:
    pingNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 80, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pingCompliance.setStatus(
        "deprecated"
    )

pingFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 80, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pingFullCompliance.setStatus(
        "current"
    )

pingMinimumCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 80, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pingMinimumCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISMAN-PING-MIB",
    **{"OperationResponseStatus": OperationResponseStatus,
       "pingMIB": pingMIB,
       "pingNotifications": pingNotifications,
       "pingProbeFailed": pingProbeFailed,
       "pingTestFailed": pingTestFailed,
       "pingTestCompleted": pingTestCompleted,
       "pingObjects": pingObjects,
       "pingMaxConcurrentRequests": pingMaxConcurrentRequests,
       "pingCtlTable": pingCtlTable,
       "pingCtlEntry": pingCtlEntry,
       "pingCtlOwnerIndex": pingCtlOwnerIndex,
       "pingCtlTestName": pingCtlTestName,
       "pingCtlTargetAddressType": pingCtlTargetAddressType,
       "pingCtlTargetAddress": pingCtlTargetAddress,
       "pingCtlDataSize": pingCtlDataSize,
       "pingCtlTimeOut": pingCtlTimeOut,
       "pingCtlProbeCount": pingCtlProbeCount,
       "pingCtlAdminStatus": pingCtlAdminStatus,
       "pingCtlDataFill": pingCtlDataFill,
       "pingCtlFrequency": pingCtlFrequency,
       "pingCtlMaxRows": pingCtlMaxRows,
       "pingCtlStorageType": pingCtlStorageType,
       "pingCtlTrapGeneration": pingCtlTrapGeneration,
       "pingCtlTrapProbeFailureFilter": pingCtlTrapProbeFailureFilter,
       "pingCtlTrapTestFailureFilter": pingCtlTrapTestFailureFilter,
       "pingCtlType": pingCtlType,
       "pingCtlDescr": pingCtlDescr,
       "pingCtlSourceAddressType": pingCtlSourceAddressType,
       "pingCtlSourceAddress": pingCtlSourceAddress,
       "pingCtlIfIndex": pingCtlIfIndex,
       "pingCtlByPassRouteTable": pingCtlByPassRouteTable,
       "pingCtlDSField": pingCtlDSField,
       "pingCtlRowStatus": pingCtlRowStatus,
       "pingResultsTable": pingResultsTable,
       "pingResultsEntry": pingResultsEntry,
       "pingResultsOperStatus": pingResultsOperStatus,
       "pingResultsIpTargetAddressType": pingResultsIpTargetAddressType,
       "pingResultsIpTargetAddress": pingResultsIpTargetAddress,
       "pingResultsMinRtt": pingResultsMinRtt,
       "pingResultsMaxRtt": pingResultsMaxRtt,
       "pingResultsAverageRtt": pingResultsAverageRtt,
       "pingResultsProbeResponses": pingResultsProbeResponses,
       "pingResultsSentProbes": pingResultsSentProbes,
       "pingResultsRttSumOfSquares": pingResultsRttSumOfSquares,
       "pingResultsLastGoodProbe": pingResultsLastGoodProbe,
       "pingProbeHistoryTable": pingProbeHistoryTable,
       "pingProbeHistoryEntry": pingProbeHistoryEntry,
       "pingProbeHistoryIndex": pingProbeHistoryIndex,
       "pingProbeHistoryResponse": pingProbeHistoryResponse,
       "pingProbeHistoryStatus": pingProbeHistoryStatus,
       "pingProbeHistoryLastRC": pingProbeHistoryLastRC,
       "pingProbeHistoryTime": pingProbeHistoryTime,
       "pingConformance": pingConformance,
       "pingCompliances": pingCompliances,
       "pingCompliance": pingCompliance,
       "pingFullCompliance": pingFullCompliance,
       "pingMinimumCompliance": pingMinimumCompliance,
       "pingGroups": pingGroups,
       "pingGroup": pingGroup,
       "pingTimeStampGroup": pingTimeStampGroup,
       "pingNotificationsGroup": pingNotificationsGroup,
       "pingMinimumGroup": pingMinimumGroup,
       "pingCtlRowStatusGroup": pingCtlRowStatusGroup,
       "pingHistoryGroup": pingHistoryGroup,
       "pingImplementationTypeDomains": pingImplementationTypeDomains,
       "pingIcmpEcho": pingIcmpEcho,
       "pingUdpEcho": pingUdpEcho,
       "pingSnmpQuery": pingSnmpQuery,
       "pingTcpConnectionAttempt": pingTcpConnectionAttempt}
)
